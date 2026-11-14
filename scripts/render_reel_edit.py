#!/usr/bin/env python3
"""Render a non-destructive shot list and timed captions with a review pack.

First-party implementation informed by the comparison in
docs/research/video-harness-review.md; no upstream source code is vendored.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import sys
import tempfile

from review_video import build_review, inspect_video, run

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/el-hamaayan-reel/scripts"))
from render_one_shot_reel import build_ass, rtl_line  # noqa: E402

FPS = 30


def number(value, label: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must be a finite number")
    if value < 0 or (positive and value == 0):
        raise ValueError(f"{label} must be {'positive' if positive else 'non-negative'}")
    return float(value)


def identifier(value, label: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[a-zA-Z0-9_-]+", value):
        raise ValueError(f"{label} must use letters, digits, underscores or hyphens")
    return value


def fields(value: dict, allowed: set[str], label: str) -> None:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    unknown = set(value) - allowed
    if unknown:
        raise ValueError(f"Unsupported {label} fields: {', '.join(sorted(unknown))}")


def compile_edit(plan: dict, base: Path) -> dict:
    fields(plan, {"schema_version", "sources", "shots", "captions", "caption_style"}, "plan")
    if plan.get("schema_version") != 1:
        raise ValueError("Use schema_version: 1")
    sources = {}
    for raw in plan.get("sources", []):
        fields(raw, {"id", "path", "drive_id", "clock_start", "alignment_id", "reference"}, "source")
        source_id = identifier(raw.get("id"), "Source id")
        if source_id in sources:
            raise ValueError(f"Duplicate source id: {source_id}")
        source = (base / raw["path"]).resolve()
        if not source.is_file():
            raise FileNotFoundError(source)
        metadata = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(source)]))
        video = next((stream for stream in metadata.get("streams", []) if stream.get("codec_type") == "video"), None)
        if video is None:
            raise ValueError(f"No video in source {source_id}")
        if video.get("color_transfer") in {"smpte2084", "arib-std-b67"}:
            raise ValueError(f"Source {source_id} is HDR; prepare and inspect an explicit SDR derivative first")
        duration = float(video.get("duration") or metadata.get("format", {}).get("duration", 0))
        number(duration, f"Duration of {source_id}", positive=True)
        sar = video.get("sample_aspect_ratio", "1:1")
        if sar in {"N/A", "0:1"}:
            sar = "1:1"
        numerator, denominator = map(float, sar.split(":"))
        aspect = numerator / denominator
        width, height = video["width"] * aspect, video["height"]
        rotation = next((float(item["rotation"]) for item in video.get("side_data_list", []) if "rotation" in item),
                        float(video.get("tags", {}).get("rotate", 0))) % 360
        if rotation not in (0, 90, 180, 270):
            raise ValueError(f"Source {source_id} needs an explicit orientation derivative")
        if rotation in (90, 270):
            width, height = height, width
        sources[source_id] = {**raw, "path": str(source), "duration": duration,
                              "clock_start": number(raw.get("clock_start", 0), "clock_start"),
                              "display_width": width, "display_height": height,
                              "audio_present": any(stream.get("codec_type") == "audio" for stream in metadata["streams"])}
    shots, by_id, cursor = [], {}, 0
    for raw in plan.get("shots", []):
        fields(raw, {"id", "source", "source_in", "frames", "rotate", "fit", "audio", "reason"}, "shot")
        shot_id = identifier(raw.get("id"), "Shot id")
        if shot_id in by_id:
            raise ValueError(f"Duplicate shot id: {shot_id}")
        if raw.get("source") not in sources:
            raise ValueError(f"Unknown source for {shot_id}")
        source = sources[raw["source"]]
        frames = raw.get("frames")
        if type(frames) is not int or frames <= 0:
            raise ValueError(f"Shot {shot_id} needs a positive integer frame count")
        start = number(raw.get("source_in"), "source_in")
        local = start - source["clock_start"]
        if local < 0 or local + frames / FPS > source["duration"] + 0.000001:
            raise ValueError(f"Shot {shot_id} is outside the local source span; check clock_start and source_in")
        rotation = raw.get("rotate", 0)
        if type(rotation) is not int or rotation not in (0, 90, 180, 270):
            raise ValueError("rotate must be 0, 90, 180 or 270 degrees clockwise after metadata rotation")
        width, height = source["display_width"], source["display_height"]
        if rotation in (90, 270):
            width, height = height, width
        fit = raw.get("fit", "native")
        if fit not in ("native", "pad"):
            raise ValueError("fit must be native or pad; cropping is not implicit")
        if fit == "native" and abs(width / height - 9 / 16) / (9 / 16) > 0.025:
            raise ValueError(f"Shot {shot_id} is not displayed 9:16; choose a source or explicitly request fit: pad")
        audio = raw.get("audio", "keep")
        if audio not in ("keep", "mute"):
            raise ValueError("audio must be keep or mute")
        shot = {**raw, "id": shot_id, "source_in": start, "local_in": local, "frames": frames,
                "timeline_start_frame": cursor, "timeline_end_frame": cursor + frames,
                "rotate": rotation, "fit": fit, "audio": audio}
        shots.append(shot); by_id[shot_id] = shot; cursor += frames
    if not shots:
        raise ValueError("At least one shot is required")
    cues, cue_ids = [], set()
    for raw in plan.get("captions", []):
        fields(raw, {"id", "role", "text", "shot", "source_in", "source_out", "alignment_id", "source_language",
                     "display_language", "translation_status", "original_text", "uncertainty", "start_frame", "end_frame"}, "caption")
        cue_id = identifier(raw.get("id"), "Caption id")
        if cue_id in cue_ids:
            raise ValueError(f"Duplicate caption id: {cue_id}")
        cue_ids.add(cue_id)
        text = raw.get("text")
        if not isinstance(text, str) or not text.strip() or len(text.splitlines()) > 6 or "\r" in text:
            raise ValueError("Caption text needs 1–6 nonempty lines; use LF line breaks")
        if raw.get("role") == "speech":
            shot = by_id.get(raw.get("shot"))
            if shot is None:
                raise ValueError(f"Caption {cue_id} needs a valid shot")
            source = sources[shot["source"]]
            alignment = source.get("alignment_id")
            if not isinstance(alignment, str) or not alignment or raw.get("alignment_id") != alignment:
                raise ValueError(f"Caption {cue_id} must use the shot source's alignment_id")
            if not raw.get("source_language") or not raw.get("display_language"):
                raise ValueError("Speech captions need source_language and display_language")
            start = (number(raw.get("source_in"), "Caption source_in") - shot["source_in"]) * FPS + shot["timeline_start_frame"]
            end = (number(raw.get("source_out"), "Caption source_out") - shot["source_in"]) * FPS + shot["timeline_start_frame"]
            if not shot["timeline_start_frame"] <= start < end <= shot["timeline_end_frame"] + 0.000001:
                raise ValueError(f"Speech caption {cue_id} crosses its shot boundary or clips its speech span")
            # Snap each absolute onset independently: never queue behind a previous hold.
            start, end = round(start), round(end)
        elif raw.get("role") == "overlay":
            start, end = raw.get("start_frame"), raw.get("end_frame")
            if type(start) is not int or type(end) is not int:
                raise ValueError("Overlay captions need integer start_frame and end_frame")
        else:
            raise ValueError("Caption role must be speech or overlay")
        if not 0 <= start < end <= cursor:
            raise ValueError(f"Caption {cue_id} has an empty or out-of-timeline span")
        cues.append({**raw, "start_frame": start, "end_frame": end,
                     "text_sha256": hashlib.sha256(text.encode()).hexdigest()})
    cues.sort(key=lambda cue: cue["start_frame"])
    if any(left["end_frame"] > right["start_frame"] for left, right in zip(cues, cues[1:])):
        raise ValueError("Captions overlap; revise their timing or grouping without delaying speech onsets")
    fields(plan.get("caption_style", {}), {"font", "font_size", "top"}, "caption style")
    style = {"font": "DejaVu Sans", "font_size": 58, "top": 650, **plan.get("caption_style", {})}
    if not isinstance(style["font"], str) or any(char in style["font"] for char in ",\r\n"):
        raise ValueError("Invalid caption font family")
    for key, minimum, maximum in [("font_size", 1, 300), ("top", 0, 1800)]:
        if type(style[key]) is not int or not minimum <= style[key] <= maximum:
            raise ValueError(f"Invalid caption {key}")
    return {"fps": FPS, "sources": sources, "shots": shots, "captions": cues,
            "caption_style": style, "total_frames": cursor,
            "warnings": [f"Caption {cue['id']} holds under 0.6s; inspect reading time" for cue in cues
                         if cue["end_frame"] - cue["start_frame"] < 0.6 * FPS]}


def ass_time(frame: int) -> str:
    # ASS stores centiseconds. Floor the boundary into the gap before this
    # frame; rounding upward would delay/extend cues by one 30fps frame.
    centiseconds = frame * 100 // FPS
    return f"{centiseconds // 360000}:{centiseconds // 6000 % 60:02}:{centiseconds // 100 % 60:02}.{centiseconds % 100:02}"


def caption_file(edit: dict) -> str:
    style = edit["caption_style"]
    header = build_ass([""], style["font"], style["font_size"], style["top"]).split("Dialogue:", 1)[0]
    events = []
    for cue in edit["captions"]:
        text = r"\N".join(rtl_line(line) for line in cue["text"].split("\n"))
        events.append(f"Dialogue: 0,{ass_time(cue['start_frame'])},{ass_time(cue['end_frame'])},Main,,0,0,0,,{text}")
    return header + "\n".join(events) + "\n"


def render_edit(plan_path: Path, destination: Path, *, preview: bool = False) -> dict:
    plan_path, destination = plan_path.resolve(), destination.resolve()
    if destination.exists():
        raise ValueError("Output directory already exists; use a new version")
    edit = compile_edit(json.loads(plan_path.read_text(encoding="utf-8")), plan_path.parent)
    width, height = (432, 768) if preview else (1080, 1920)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Stage everything together. A failed build never becomes the requested version.
    with tempfile.TemporaryDirectory(prefix="reel-edit-", dir=destination.parent) as temporary:
        work = Path(temporary)
        (work / "captions.ass").write_text(caption_file(edit), encoding="utf-8")
        command = ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error"]
        graph, labels, keep_audio = [], [], False
        for i, shot in enumerate(edit["shots"]):
            source = edit["sources"][shot["source"]]
            duration = shot["frames"] / FPS
            command += ["-ss", str(shot["local_in"]), "-t", str(duration), "-i", source["path"]]
            rotation = {0: "", 90: "transpose=clock,", 180: "hflip,vflip,", 270: "transpose=cclock,"}[shot["rotate"]]
            graph.append(f"[{i}:v:0]setpts=PTS-STARTPTS,{rotation}fps={FPS},"
                         f"scale=w='trunc(iw*sar/2)*2':h=ih,setsar=1,"
                         f"scale={width}:{height}:force_original_aspect_ratio=decrease:out_range=tv,"
                         f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black,"
                         f"trim=end_frame={shot['frames']},format=yuv420p[v{i}]")
            if source["audio_present"] and shot["audio"] == "keep":
                keep_audio = True
                graph.append(f"[{i}:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
                             f"apad=whole_dur={duration},atrim=duration={duration},asetpts=PTS-STARTPTS[a{i}]")
            else:
                graph.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={duration},asetpts=PTS-STARTPTS[a{i}]")
            labels += [f"[v{i}][a{i}]"]
        graph.append(f"{''.join(labels)}concat=n={len(labels)}:v=1:a=1[vcut][acut]")
        if edit["captions"]:
            graph.append(f"[vcut]settb=1/{FPS},setpts=N,subtitles=captions.ass[out]")
        else:
            graph.append(f"[vcut]settb=1/{FPS},setpts=N[out]")
        if not keep_audio:
            graph.append("[acut]anullsink")
        command += ["-filter_complex_threads", "1", "-filter_complex", ";".join(graph), "-map", "[out]"]
        if keep_audio:
            command += ["-map", "[acut]", "-c:a", "aac", "-b:a", "192k"]
        command += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-threads", "2",
                    "-pix_fmt", "yuv420p", "-color_range", "tv", "-metadata:s:v:0", "rotate=0",
                    "-movflags", "+faststart+write_colr", str(work / "cut.mp4")]
        # The ASS path is relative to a generated scratch directory, avoiding filter-path escaping.
        import subprocess
        result = subprocess.run(command, cwd=work, text=True, capture_output=True)
        if result.returncode:
            raise RuntimeError(result.stderr.strip())
        _, timestamps = inspect_video(work / "cut.mp4")
        if len(timestamps) != edit["total_frames"]:
            raise RuntimeError(f"Expected {edit['total_frames']} frames, decoded {len(timestamps)}; source span may end early")
        (work / "cues.json").write_text(json.dumps(edit["captions"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (work / "edit-build.json").write_text(json.dumps({**edit, "plan_sha256": hashlib.sha256(plan_path.read_bytes()).hexdigest(),
            "profile": "preview" if preview else "reel", "review_status": "not_approved"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        cuts = [shot["timeline_start_frame"] for shot in edit["shots"][1:]]
        points = {frame for cue in edit["captions"] for frame in
                  (cue["start_frame"], cue["end_frame"] - 1, min(cue["end_frame"], len(timestamps) - 1))}
        report = build_review(work / "cut.mp4", work / "review", times=[timestamps[index] for index in sorted(points)],
                              cuts=cuts, cover=None, expect_reel=not preview)
        if not all(report["automated_checks"]["reel_export"].values()):
            raise RuntimeError("Rendered output failed the Reel export preset checks")
        # Review assets use relative links. Fix the report's source path after moving the staged directory.
        report["source"] = str(destination / "cut.mp4")
        (work / "review/review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if destination.exists():
            raise ValueError("Output version was created while rendering; choose a new version")
        work.rename(destination)
    return {"output": str(destination / "cut.mp4"), "frames": edit["total_frames"],
            "duration": edit["total_frames"] / FPS, "warnings": edit["warnings"],
            "review_board": str(destination / "review/index.html"), "approval": "not_approved"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("output_dir", type=Path, nargs="?")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--check", action="store_true", help="Validate sources, clocks and cue structure without rendering")
    args = parser.parse_args()
    try:
        for binary in ("ffmpeg", "ffprobe"):
            if not shutil.which(binary):
                raise RuntimeError(f"{binary} is required")
        if args.check:
            result = compile_edit(json.loads(args.plan.read_text(encoding="utf-8")), args.plan.resolve().parent)
        else:
            if args.output_dir is None:
                parser.error("output_dir is required unless --check is used")
            result = render_edit(args.plan, args.output_dir, preview=args.preview)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
