"""Verify real browser notes, source versions and different export frame rates."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(all(shutil.which(binary) for binary in ("node", "ffmpeg", "ffprobe")), "Node and FFmpeg are required")
class ReviewRoomTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary = tempfile.TemporaryDirectory()
        cls.folder = Path(cls.temporary.name)
        for name, color, size, fps in [("portrait-30.mp4", "red", "180x320", 30), ("wide-60.mp4", "blue", "320x180", 60),
                                       ("variable.mp4", "green", "180x320", 30)]:
            filters = ["-vf", "setpts=if(lt(N\\,15)\\,N/(30*TB)\\,(0.5+(N-15)/15)/TB)"] if name == "variable.mp4" else []
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i",
                            f"color={color}:s={size}:r={fps}:d=1", *filters, "-fps_mode", "vfr", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                            str(cls.folder / name)], check=True, capture_output=True)
        cls.server = subprocess.Popen(["node", str(ROOT / "scripts/review-room/server.mjs"), str(cls.folder), "0"],
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        line = cls.server.stdout.readline().strip()
        if not line.startswith("Ela Maayan review room: "):
            raise RuntimeError(line or cls.server.stderr.read())
        cls.base = line.split("room: ", 1)[1]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.terminate()
        cls.server.communicate(timeout=10)
        cls.temporary.cleanup()

    def request(self, route: str, body: dict | None = None, headers: dict | None = None):
        request = urllib.request.Request(self.base + route, data=json.dumps(body).encode() if body is not None else None,
                                         headers=headers or {})
        try:
            response = urllib.request.urlopen(request, timeout=15)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            return response.status, response.read()

    def test_notes_are_bound_to_export_and_resolution(self) -> None:
        status, raw = self.request("/api/cuts")
        self.assertEqual(status, 200)
        cuts = {cut["name"]: cut for cut in json.loads(raw)}
        portrait, wide = cuts["portrait-30.mp4"], cuts["wide-60.mp4"]
        self.assertEqual(len(portrait["frame_times"]), 30)
        self.assertEqual(len(wide["frame_times"]), 60)
        body = {"cut": wide["name"], "cut_sha256": wide["sha256"], "t": wide["frame_times"][1],
                "x": 0.2, "y": 0.5, "text": "Keep this exact note"}
        status, raw = self.request("/api/notes", body)
        self.assertEqual(status, 201)
        note = json.loads(raw)
        self.assertEqual(note["frame"], 1, "A 60fps frame must not be labeled as 30fps")
        self.assertEqual(note["text"], body["text"])
        status, _ = self.request("/api/notes", {**body, "cut_sha256": "stale"})
        self.assertEqual(status, 409)
        status, _ = self.request("/api/notes/" + note["id"], {"done": True, "resolved_in": wide["name"]})
        self.assertEqual(status, 400)
        status, raw = self.request("/api/notes/" + note["id"], {"done": True, "resolved_in": portrait["name"]})
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(raw)["resolved_in"]["sha256"], portrait["sha256"])
        variable = cuts["variable.mp4"]
        times = variable["frame_times"]
        self.assertGreater(len({round(b - a, 3) for a, b in zip(times, times[1:])}), 1)
        status, raw = self.request("/api/notes", {"cut": variable["name"], "cut_sha256": variable["sha256"],
                                                "t": times[20], "text": "Variable frame interval"})
        self.assertEqual(status, 201)
        self.assertEqual(json.loads(raw)["frame"], 20)
        status, raw = self.request("/video/portrait-30.mp4", headers={"Range": "bytes=-8"})
        self.assertEqual(status, 206)
        self.assertEqual(raw, (self.folder / "portrait-30.mp4").read_bytes()[-8:])
        status, _ = self.request("/api/notes", body, {"Origin": "https://example.com"})
        self.assertEqual(status, 403)

    @unittest.skipUnless(importlib.util.find_spec("playwright") and shutil.which("chromium"), "Playwright and Chromium are required")
    def test_browser_portrait_pin_and_60fps_step(self) -> None:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=shutil.which("chromium"), headless=True,
                                                  args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(self.base)
            page.wait_for_function("document.querySelector('#cut').options.length === 3")
            page.select_option("#cut", "portrait-30.mp4")
            page.wait_for_function("document.querySelector('#v').readyState >= 2 && document.querySelector('#v').videoHeight === 320")
            page.click("#hit", position={"x": 100, "y": 200})
            page.fill("#text", "הטקסט מכסה את הפנים")
            page.click("#add")
            page.get_by_text("הטקסט מכסה את הפנים", exact=True).wait_for()
            page.wait_for_function("[...document.querySelectorAll('.note img')].some(image => image.complete && image.naturalHeight === 320)")
            sizes = page.locator(".note img").evaluate_all("images => images.map(image => [image.naturalWidth,image.naturalHeight])")
            self.assertIn([180, 320], sizes, "A portrait snapshot must retain its aspect ratio")
            page.click("#send")
            page.get_by_text("Review saved locally. Notes are ready for the next edit.", exact=True).wait_for()
            page.select_option("#cut", "wide-60.mp4")
            page.wait_for_function("document.querySelector('#v').readyState >= 2 && document.querySelector('#v').videoWidth === 320")
            page.click("#fwd")
            page.wait_for_function("document.querySelector('#v').currentTime > 0")
            self.assertAlmostEqual(page.locator("#v").evaluate("video => video.currentTime"), 1 / 60, places=5)
            page.set_viewport_size({"width": 390, "height": 844})
            self.assertLessEqual(page.evaluate("document.documentElement.scrollWidth"), 390)
            self.assertEqual(errors, [])
            browser.close()


if __name__ == "__main__":
    unittest.main()
