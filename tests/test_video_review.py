"""Exercise the review tool against a real cut, audio and rejected edit points."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from review_video import build_review, export_checks, inspect_video, select_frames  # noqa: E402


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg is required")
class VideoReviewTests(unittest.TestCase):
    def test_exact_cut_frames_and_human_review_remains_pending(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "clip & <test>.mp4"
            subprocess.run([
                "ffmpeg", "-hide_banner", "-loglevel", "error",
                "-f", "lavfi", "-i", "color=red:s=180x320:r=10:d=1",
                "-f", "lavfi", "-i", "color=blue:s=180x320:r=10:d=1",
                "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000:duration=2",
                "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[v]",
                "-map", "[v]", "-map", "2:a", "-c:v", "libx264",
                "-pix_fmt", "yuv420p", "-c:a", "aac", str(source),
            ], check=True, capture_output=True)
            destination = root / "review-v1"
            report = build_review(source, destination, times=[0.95], cuts=[10],
                                  cover=10, expect_reel=True)
            self.assertEqual(report["decoded_frame_count"], 20)
            self.assertEqual([frame["frame"] for frame in report["frames"]], [0, 9, 10, 19])
            self.assertEqual(report["frames"][1]["seconds"], 0.9)
            self.assertEqual(report["audio_streams"][0]["codec_name"], "aac")
            self.assertFalse(report["automated_checks"]["reel_export"]["dimensions_1080x1920"])
            self.assertFalse(report["automated_checks"]["reel_export"]["constant_30fps_timestamps"])
            self.assertEqual(report["manual_review"]["audio_listening_and_sync"], "not_reviewed")
            for number, channel in [(2, 0), (3, 2)]:
                pixel = subprocess.run([
                    "ffmpeg", "-v", "error", "-i", str(destination / f"frame-{number:04d}.png"),
                    "-vf", "scale=1:1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-",
                ], check=True, capture_output=True).stdout
                self.assertGreater(pixel[channel], 200, "Cut frame must show the correct shot")
                self.assertLess(pixel[2 - channel], 30)
            board = (destination / "index.html").read_text()
            self.assertIn("clip &amp; &lt;test&gt;.mp4", board)
            self.assertIn("clip%20%26%20%3Ctest%3E.mp4", board)
            self.assertEqual(json.loads((destination / "review.json").read_text()), report)
            with self.assertRaisesRegex(ValueError, "already exists"):
                build_review(source, destination, times=[], cuts=[], cover=None, expect_reel=False)
            with self.assertRaisesRegex(ValueError, "Cut frame"):
                build_review(source, root / "invalid", times=[], cuts=[20], cover=None, expect_reel=False)
            self.assertFalse((root / "invalid").exists())
            mov = root / "quicktime.mov"
            subprocess.run(["ffmpeg", "-v", "error", "-i", str(source), "-c", "copy", str(mov)],
                           check=True, capture_output=True)
            mov_metadata, mov_times = inspect_video(mov)
            self.assertFalse(export_checks(mov_metadata["streams"][0], mov_metadata, mov_times)["mp4_container"])

    def test_variable_frame_intervals_use_presentation_time(self) -> None:
        frames = select_frames([0.0, 0.04, 0.12, 0.9], [0.1], [], None)
        self.assertIn(1, frames)
        for invalid in (-0.1, 1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                select_frames([0.0, 0.04, 0.12, 0.9], [invalid], [], None)


if __name__ == "__main__":
    unittest.main()
