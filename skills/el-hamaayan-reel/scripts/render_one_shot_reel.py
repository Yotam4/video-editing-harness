#!/usr/bin/env python3
"""Render El Hamaayan's clean one-shot Reel style without silently cropping."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


TARGET_RATIO = 9 / 16


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, text=True, capture_output=True)


def probe_video(path: Path) -> dict:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,duration,nb_frames:stream_side_data=rotation",
            "-of",
            "json",
            str(path),
        ]
    )
    payload = json.loads(result.stdout)
    if not payload.get("streams"):
        raise ValueError("Input has no video stream")
    return payload["streams"][0]


def displayed_dimensions(stream: dict) -> tuple[int, int, int]:
    width = int(stream["width"])
    height = int(stream["height"])
    rotation = 0
    for item in stream.get("side_data_list", []):
        if "rotation" in item:
            rotation = int(item["rotation"]) % 360
            break
    if rotation in (90, 270):
        width, height = height, width
    return width, height, rotation


def ass_escape(text: str) -> str:
    return text.replace("\\", r"\\").replace("{", r"\{").replace("}", r"\}")


def rtl_line(text: str) -> str:
    # RLE plus an ending RLM keeps trailing punctuation on the Hebrew side.
    return "\u202b" + ass_escape(text) + "\u200f\u202c"


def build_ass(lines: list[str], font: str, font_size: int, top: int) -> str:
    rendered_text = r"\N".join(rtl_line(line) for line in lines)
    return f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Main,{font},{font_size},&H00FFFFFF,&H00FFFFFF,&H74000000,&H00000000,-1,0,0,0,100,100,0,0,1,2.0,0,8,70,70,{top},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,9:59:59.00,Main,,0,0,0,,{rendered_text}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--text-file", required=True, type=Path)
    parser.add_argument("--start", type=float, default=0.0)
    parser.add_argument("--duration", type=float)
    parser.add_argument("--font", default="DejaVu Sans")
    parser.add_argument("--font-size", type=int, default=58)
    parser.add_argument("--text-top", type=int, default=650)
    parser.add_argument(
        "--allow-padding",
        action="store_true",
        help="Allow letterboxing for a source that is not close to 9:16.",
    )
    args = parser.parse_args()

    for binary in ("ffmpeg", "ffprobe"):
        if shutil.which(binary) is None:
            raise RuntimeError(f"{binary} is required")
    if not args.input.is_file():
        raise FileNotFoundError(args.input)
    if not args.text_file.is_file():
        raise FileNotFoundError(args.text_file)
    if args.start < 0 or (args.duration is not None and args.duration <= 0):
        raise ValueError("start must be non-negative and duration must be positive")

    lines = args.text_file.read_text(encoding="utf-8-sig").splitlines()
    if not lines or not any(lines):
        raise ValueError("Text file is empty")
    if len(lines) > 6:
        raise ValueError("Use six lines or fewer; revise line breaks before rendering")

    stream = probe_video(args.input)
    display_width, display_height, rotation = displayed_dimensions(stream)
    ratio = display_width / display_height
    ratio_error = abs(ratio - TARGET_RATIO) / TARGET_RATIO
    if ratio_error > 0.025 and not args.allow_padding:
        raise ValueError(
            f"Displayed source is {display_width}x{display_height} "
            f"(rotation {rotation}°), not native 9:16. "
            "Choose another source or get approval before padding/cropping."
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="el-hamaayan-reel-") as tmp:
        ass_path = Path(tmp) / "overlay.ass"
        ass_path.write_text(
            build_ass(lines, args.font, args.font_size, args.text_top),
            encoding="utf-8",
        )
        escaped_ass = str(ass_path).replace("\\", "/").replace(":", r"\:")
        filters = (
            "scale=1080:1920:force_original_aspect_ratio=decrease:flags=lanczos,"
            "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,"
            "setsar=1,"
            f"subtitles='{escaped_ass}',"
            "format=yuv420p"
        )
        command = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
        if args.start:
            command += ["-ss", str(args.start)]
        command += ["-i", str(args.input)]
        if args.duration is not None:
            command += ["-t", str(args.duration)]
        command += [
            "-map",
            "0:v:0",
            "-map",
            "0:a?",
            "-vf",
            filters,
            "-r",
            "30",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-metadata:s:v:0",
            "rotate=0",
            "-movflags",
            "+faststart",
            str(args.output),
        ]
        run(command)

    output_probe = probe_video(args.output)
    output_width, output_height, output_rotation = displayed_dimensions(output_probe)
    if (output_width, output_height, output_rotation) != (1080, 1920, 0):
        raise RuntimeError(
            "Output verification failed: "
            f"{output_width}x{output_height}, rotation {output_rotation}°"
        )
    print(
        json.dumps(
            {
                "output": str(args.output.resolve()),
                "display_dimensions": [output_width, output_height],
                "rotation": output_rotation,
                "source_display_dimensions": [display_width, display_height],
                "source_rotation": rotation,
                "lines": len(lines),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
