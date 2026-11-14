"""Exercise shot clocks, real mixed-rate assembly and rendered caption windows."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from render_reel_edit import compile_edit, render_edit  # noqa: E402


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg is required")
class ReelEditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name, color, size, fps, audio in [("raw-red.mp4", "red", "320x180", 24, True),
                                              ("blue.mp4", "blue", "180x320", 60, False)]:
            command = ["ffmpeg", "-v", "error", "-f", "lavfi", "-i", f"color={color}:s={size}:r={fps}:d=1"]
            if audio:
                command += ["-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000:duration=1", "-c:a", "aac"]
            subprocess.run([*command, "-c:v", "libx264", "-pix_fmt", "yuv420p", str(self.root / name)],
                           check=True, capture_output=True)
        subprocess.run(["ffmpeg", "-v", "error", "-display_rotation", "90", "-i", str(self.root / "raw-red.mp4"),
                        "-c", "copy", str(self.root / "red.mp4")], check=True, capture_output=True)
        self.plan = {"schema_version": 1, "sources": [
            {"id": "red", "path": "red.mp4", "clock_start": 10, "alignment_id": "fixture-clock-not-ASR"},
            {"id": "blue", "path": "blue.mp4", "clock_start": 30}],
            "shots": [{"id": "s1", "source": "red", "source_in": 10.25, "frames": 15},
                      {"id": "s2", "source": "blue", "source_in": 30.25, "frames": 15}],
            "captions": [
                {"id": "c1", "role": "speech", "shot": "s1", "source_in": 10.35, "source_out": 10.65,
                 "text": "אל המעיין: 3 מסלולים?", "source_language": "he", "display_language": "he",
                 "alignment_id": "fixture-clock-not-ASR"},
                {"id": "c2", "role": "overlay", "start_frame": 17, "end_frame": 26, "text": "בואו לטייל!"}]}

    def test_rendered_cut_and_caption_windows_keep_source_clocks(self) -> None:
        before = {name: hashlib.sha256((self.root / name).read_bytes()).hexdigest() for name in ("red.mp4", "blue.mp4")}
        plan_file = self.root / "edit.json"
        plan_file.write_text(json.dumps(self.plan, ensure_ascii=False))
        result = render_edit(plan_file, self.root / "v1")
        self.assertEqual(result["frames"], 30)
        self.assertEqual(result["duration"], 1)
        cues = json.loads((self.root / "v1/cues.json").read_text())
        self.assertEqual((cues[0]["start_frame"], cues[0]["end_frame"]), (3, 12))
        self.assertEqual(cues[0]["text"], self.plan["captions"][0]["text"])
        report = json.loads((self.root / "v1/review/review.json").read_text())
        self.assertTrue(all(report["automated_checks"]["reel_export"].values()))
        self.assertEqual(report["video"]["color_range"], "tv")
        self.assertEqual(report["source"], str(self.root / "v1/cut.mp4"))
        frames = {frame["frame"]: self.root / "v1/review" / frame["image"] for frame in report["frames"]}
        def white_pixels(frame: int) -> int:
            pixels = subprocess.run(["ffmpeg", "-v", "error", "-i", str(frames[frame]),
                                     "-vf", "crop=1080:300:0:600,format=gray", "-f", "rawvideo", "-"],
                                    check=True, capture_output=True).stdout
            return sum(pixel > 200 for pixel in pixels)
        self.assertGreater(white_pixels(3), 100, "Caption must appear at its compiled onset")
        self.assertLess(white_pixels(12), 10, "Caption must clear at its exclusive out point")
        self.assertGreater(white_pixels(17), 100, "ASS centiseconds must not delay a fractional-frame onset")
        self.assertLess(white_pixels(26), 10, "ASS centiseconds must not extend a fractional-frame out point")
        self.assertNotEqual(frames[14].read_bytes(), frames[15].read_bytes(), "The second shot must begin exactly on frame 15")
        for name, digest in before.items():
            self.assertEqual(hashlib.sha256((self.root / name).read_bytes()).hexdigest(), digest)
        with self.assertRaisesRegex(ValueError, "already exists"):
            render_edit(plan_file, self.root / "v1")

    def test_rejects_mixed_alignments_overlaps_and_wrong_source_clocks(self) -> None:
        edit = compile_edit(self.plan, self.root)
        self.assertAlmostEqual(edit["shots"][0]["local_in"], 0.25)
        for change, message in [
            (lambda plan: plan["captions"][0].update(alignment_id="another-clock"), "alignment_id"),
            (lambda plan: plan["captions"][0].update(source_out=10.9), "shot boundary"),
            (lambda plan: plan["sources"][0].update(clock_start=11), "outside the local source"),
            (lambda plan: plan["captions"][1].update(start_frame=10), "overlap"),
            (lambda plan: plan["shots"][0].update(rotate=90), "not displayed 9:16"),
            (lambda plan: plan["shots"][0].update(speed=2), "Unsupported shot fields"),
        ]:
            with self.subTest(message=message):
                altered = copy.deepcopy(self.plan); change(altered)
                with self.assertRaisesRegex(ValueError, message):
                    compile_edit(altered, self.root)

    def test_preview_explicitly_pads_a_wide_shot_and_mutes_audio(self) -> None:
        plan = copy.deepcopy(self.plan)
        plan["shots"] = [{**plan["shots"][0], "rotate": 90, "fit": "pad", "audio": "mute"}]
        plan["captions"] = []
        file = self.root / "padded.json"; file.write_text(json.dumps(plan))
        render_edit(file, self.root / "preview", preview=True)
        report = json.loads((self.root / "preview/review/review.json").read_text())
        self.assertEqual((report["video"]["width"], report["video"]["height"]), (432, 768))
        self.assertEqual(report["audio_streams"], [])
        pixel = subprocess.run(["ffmpeg", "-v", "error", "-i", str(self.root / "preview/review/frame-0001.png"),
                                "-vf", "crop=1:1:0:0,format=rgb24", "-f", "rawvideo", "-"],
                               check=True, capture_output=True).stdout
        self.assertTrue(all(value < 5 for value in pixel), "The explicit letterbox must preserve black padding")


if __name__ == "__main__":
    unittest.main()
