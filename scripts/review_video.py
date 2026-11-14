#!/usr/bin/env python3
"""Build a local video review board; extracted frames are not playback approval."""

from __future__ import annotations

import argparse
from bisect import bisect_right
import hashlib
import html
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.parse import quote


def run(command: list[str]) -> str:
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"Command failed: {command[0]}")
    return result.stdout


def inspect_video(source: Path) -> tuple[dict, list[float]]:
    metadata = json.loads(run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format",
        "-of", "json", str(source),
    ]))
    frames = json.loads(run([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_frames",
        "-show_entries", "frame=best_effort_timestamp_time", "-of", "json",
        str(source),
    ])).get("frames", [])
    if not frames:
        raise ValueError("Input has no decodable video frames")
    try:
        timestamps = [float(frame["best_effort_timestamp_time"]) for frame in frames]
    except (KeyError, ValueError) as exc:
        raise ValueError("Every video frame needs a presentation timestamp") from exc
    timestamps = [value - timestamps[0] for value in timestamps]
    if not all(math.isfinite(value) for value in timestamps):
        raise ValueError("Frame timestamps must be finite")
    if timestamps != sorted(timestamps):
        raise ValueError("Video presentation timestamps are not ordered")
    return metadata, timestamps


def select_frames(timestamps: list[float], times: list[float],
                  cuts: list[int], cover: int | None) -> dict[int, list[str]]:
    count = len(timestamps)
    selected: dict[int, list[str]] = {}

    def add(index: int, reason: str) -> None:
        selected.setdefault(index, []).append(reason)

    for index, reason in [(0, "opening"), (count // 2, "middle"), (count - 1, "ending")]:
        add(index, reason)
    for time in times:
        if not math.isfinite(time) or time < 0 or time > timestamps[-1]:
            raise ValueError(f"Review time {time} is outside 0–{timestamps[-1]:.3f}s")
        add(bisect_right(timestamps, time) - 1, f"requested time {time:g}s")
    for cut in cuts:
        if not 0 < cut < count:
            raise ValueError(f"Cut frame {cut} must be between 1 and {count - 1}")
        add(cut - 1, f"before cut at frame {cut}")
        add(cut, f"after cut at frame {cut}")
    if cover is not None:
        if not 0 <= cover < count:
            raise ValueError(f"Cover frame must be between 0 and {count - 1}")
        add(cover, "cover candidate")
    return dict(sorted(selected.items()))


def export_checks(video: dict, metadata: dict, timestamps: list[float]) -> dict[str, bool]:
    rotations = [float(item["rotation"]) % 360
                 for item in video.get("side_data_list", []) if "rotation" in item]
    legacy_rotation = float(video.get("tags", {}).get("rotate", 0)) % 360
    # FFprobe reports the same demuxer list for MOV and MP4; use the file brand.
    major_brand = metadata.get("format", {}).get("tags", {}).get("major_brand", "").strip()
    return {
        "dimensions_1080x1920": (video.get("width"), video.get("height")) == (1080, 1920),
        "rotation_zero": all(value == 0 for value in rotations) and legacy_rotation == 0,
        "h264": video.get("codec_name") == "h264",
        "yuv420p": video.get("pix_fmt") == "yuv420p",
        "square_pixels": video.get("sample_aspect_ratio") == "1:1",
        "mp4_container": major_brand in {"isom", "iso2", "iso3", "iso4", "iso5", "iso6", "mp41", "mp42", "avc1"},
        "constant_30fps_timestamps": len(timestamps) > 1 and all(
            abs(time - index / 30) < 0.001 for index, time in enumerate(timestamps)
        ),
    }


def build_review(source: Path, destination: Path, *, times: list[float],
                 cuts: list[int], cover: int | None, expect_reel: bool) -> dict:
    source = source.resolve()
    destination = destination.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    if destination.exists():
        raise ValueError("Review destination already exists; choose a new version directory")
    metadata, timestamps = inspect_video(source)
    selected = select_frames(timestamps, times, cuts, cover)
    video = next(stream for stream in metadata["streams"] if stream["codec_type"] == "video")
    audio = [stream for stream in metadata["streams"] if stream["codec_type"] == "audio"]
    checks = export_checks(video, metadata, timestamps) if expect_reel else {}
    # Decode both streams; successful decoding does not prove audible quality or sync.
    run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-xerror", "-i", str(source),
         "-map", "0:v:0", "-map", "0:a?", "-f", "null", "-"])
    destination.mkdir(parents=True)
    expression = "+".join(f"eq(n\\,{index})" for index in selected)
    run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-xerror", "-i", str(source),
         "-map", "0:v:0", "-an", "-vf", f"select={expression}", "-fps_mode", "vfr",
         "-frames:v", str(len(selected)), str(destination / "frame-%04d.png")])
    frames = []
    for number, (index, reasons) in enumerate(selected.items(), start=1):
        name = f"frame-{number:04d}.png"
        if not (destination / name).is_file():
            raise RuntimeError(f"Missing extracted frame: {name}")
        frames.append({"frame": index, "seconds": timestamps[index], "reasons": reasons, "image": name})
    with source.open("rb") as handle:
        source_sha256 = hashlib.file_digest(handle, "sha256").hexdigest()
    report = {
        "source": str(source),
        "source_sha256": source_sha256,
        "container": {key: metadata.get("format", {}).get(key) for key in ["format_name", "tags", "duration"]},
        "video": {key: video.get(key) for key in [
            "codec_name", "width", "height", "pix_fmt", "sample_aspect_ratio",
            "avg_frame_rate", "r_frame_rate", "duration", "start_time", "side_data_list",
        ]},
        "decoded_frame_count": len(timestamps),
        "last_frame_seconds": timestamps[-1],
        "audio_streams": [{key: stream.get(key) for key in [
            "codec_name", "sample_rate", "channels", "duration", "start_time",
        ]} for stream in audio],
        "automated_checks": {"full_video_and_audio_decode": "passed", "reel_export": checks},
        "manual_review": {
            "frames_and_hebrew_punctuation": "not_reviewed",
            "phone_size_muted_playback": "not_reviewed",
            "audio_listening_and_sync": "not_reviewed" if audio else "no_audio_stream",
            "cover_and_destination_ui": "not_reviewed",
        },
        "frames": frames,
        "limitations": [
            "No cuts are detected automatically; cut indices are supplied by the editor and are zero-based.",
            "Requested times select the frame at or immediately before that timestamp, relative to the first frame.",
            "Frame extraction, metadata and decoding do not approve copy, framing, pacing, motion, audio or rights.",
            "Browser playback depends on local codec support. No platform safe-area guarantee is inferred.",
        ],
    }
    (destination / "review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cards = "\n".join(
        f'<figure><a href="{frame["image"]}"><img src="{frame["image"]}" alt="Frame {frame["frame"]}"></a>'
        f'<figcaption>Frame {frame["frame"]} · {frame["seconds"]:.3f}s<br>'
        f'{html.escape(", ".join(frame["reasons"]))}</figcaption></figure>' for frame in frames
    )
    relative_video = quote(os.path.relpath(source, destination), safe="/")
    check_text = ("Reel export checks passed" if all(checks.values()) else
                  "Failed Reel export checks: " + ", ".join(key for key, passed in checks.items() if not passed)) if checks else "Reel export checks not requested"
    board = f'''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Video review</title>
<style>body{{font:16px system-ui;margin:24px;background:#111;color:#eee}}video{{width:min(100%,360px);max-height:75vh}}
.frames{{display:flex;flex-wrap:wrap;gap:20px}}figure{{margin:0;width:270px}}img{{width:100%;height:auto}}
figcaption{{padding:8px 0}}a{{color:#9dd9ff}}pre{{white-space:pre-wrap}} </style>
<h1>Video review</h1><p>{html.escape(source.name)}</p>
<p>Decode passed. {html.escape(check_text)}. Human review is pending.</p>
<video controls preload="metadata" src="{relative_video}"></video>
<p>Play once muted at phone size, then listen and check caption timing and sync. Click a frame for full resolution.</p>
<div class="frames">{cards}</div><p><a href="review.json">Measured metadata and review record</a></p>
</html>'''
    (destination / "index.html").write_text(board, encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--at", action="append", type=float, default=[], help="Seconds from first frame; repeat for caption/action checks")
    parser.add_argument("--cut-frame", action="append", type=int, default=[], help="Zero-based first frame after a cut; extracts both sides")
    parser.add_argument("--cover-frame", type=int)
    parser.add_argument("--expect-reel", action="store_true", help="Check 1080x1920, H.264, yuv420p, square pixels, rotation, MP4 and constant 30fps")
    args = parser.parse_args()
    try:
        for binary in ("ffmpeg", "ffprobe"):
            if shutil.which(binary) is None:
                raise RuntimeError(f"{binary} is required")
        report = build_review(args.input, args.output_dir, times=args.at, cuts=args.cut_frame,
                              cover=args.cover_frame, expect_reel=args.expect_reel)
        print(json.dumps({"review_board": str((args.output_dir / "index.html").resolve()),
                          "extracted_frames": len(report["frames"]),
                          "automated_checks": report["automated_checks"],
                          "manual_review": report["manual_review"]}, indent=2))
        return 0 if all(report["automated_checks"]["reel_export"].values()) else 1
    except (OSError, ValueError, RuntimeError, KeyError, StopIteration) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
