# Reel review tooling validation

Date: 2026-11-14. Baseline: `0d9de3d43c80f9ed36af25a10134e4a586a3433e`.

Scope: first-party edit records and reproducible export review. Tal's repository remains unidentified; no comparison or third-party import is claimed. Carousel procedures, styling and registry recipes were preserved.

## Checks run

- `python3 -m unittest discover -s tests -v`: two tests passed. A real FFmpeg fixture contains a red shot followed by a blue shot and an AAC tone. Extracted frames immediately before and after the known cut were checked against their actual colors. The review record retains pending human checks, rejects out-of-range cuts and existing destinations, and escapes a filename containing HTML characters. Timestamp selection also covers variable intervals and non-finite/out-of-range input.
- `python3 scripts/check_content_registry.py --smoke`: JSON Schema passed and all eight existing routing scenarios passed across 17 recipes.
- Existing one-shot renderer: rendered temporary synthetic footage with a 90-degree display matrix and mixed Hebrew text, punctuation and a number. Output verified as 1080×1920 with zero rotation.
- New review CLI with `--expect-reel`: full video/audio decoding passed, frames extracted, all seven export checks passed, source hash recorded, and HTML/JSON read back. Human playback and listening remained pending in the generated report.
- Inspected one extracted frame at full resolution: the synthetic image was upright; Hebrew text, mixed number and punctuation appeared in the expected order. This is a sampled fixture check, not approval of real footage or a complete film.
- `git diff --check`: passed.

Environment: Python 3.11+; FFmpeg/ffprobe 7.1.5 with libass, HarfBuzz and FriBidi available. Fixtures and generated review media stayed in temporary directories or ignored `.work/`.

## Limits and next input

No real campaign footage, full playback, audio listening, destination preview or live publishing was reviewed. The browser board is a local file with a relative link to the source video; this round checked generated markup and frame files, not browser behavior. Metadata checks cover the existing Reel export preset; intentionally different deliverables can omit `--expect-reel`.

The next comparison requires Tal's exact repository URL. Inspect that source's revision, license, skills and representative editing pipeline before selecting timeline, caption or audio capabilities to adapt. The current change does not implement montage assembly, transcription, caption alignment or audio mixing.
