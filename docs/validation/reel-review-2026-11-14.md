# Reel review tooling validation

Date: 2026-11-14. Baseline: `0d9de3d43c80f9ed36af25a10134e4a586a3433e`.

Scope: first-party edit records and reproducible export review, plus a selective MIT review-room adaptation from Tal Siach's `talsiach/take-one` at `43fd27b8878241deb50a5884a154b173272b858f`. Both repositories were inspected; Take One's checkout was left unmodified. Carousel procedures, styling and registry recipes were preserved.

## Checks run

- `python3 -m unittest discover -s tests -v`: four tests passed, including a real headless Chromium flow. A real FFmpeg fixture contains a red shot followed by a blue shot and an AAC tone. Extracted frames immediately before and after the known cut were checked against their actual colors. The review record retains pending human checks, rejects out-of-range cuts and existing destinations, escapes a filename containing HTML characters, and distinguishes QuickTime MOV from the MP4 preset. Timestamp selection also covers variable intervals and non-finite/out-of-range input.
- Review-room API: verified source-hash binding, stale-source rejection, exact 60fps and variable-interval frame indexing, resolution only against a different cut/hash, media byte-range delivery and same-origin handling.
- Review-room browser: saved a pinned Hebrew note on an actual portrait video, verified that its JPEG snapshot retained the 180×320 aspect, finished a local review batch, switched to a 60fps cut and stepped exactly 1/60 second. Checked the 390px viewport for horizontal overflow and captured browser errors (none). Tests used temporary media and notes.
- `python3 scripts/check_content_registry.py --smoke`: JSON Schema passed and all eight existing routing scenarios passed across 17 recipes.
- Existing one-shot renderer: rendered temporary synthetic footage with a 90-degree display matrix and mixed Hebrew text, punctuation and a number. Output verified as 1080×1920 with zero rotation.
- New review CLI with `--expect-reel`: full video/audio decoding passed, frames extracted, all seven export checks passed, source hash recorded, and HTML/JSON read back. Human playback and listening remained pending in the generated report.
- Inspected one extracted frame at full resolution: the synthetic image was upright; Hebrew text, mixed number and punctuation appeared in the expected order. This is a sampled fixture check, not approval of real footage or a complete film.
- `git diff --check`: passed.

Environment: Python 3.11+; FFmpeg/ffprobe 7.1.5 with libass, HarfBuzz and FriBidi available; Node and Playwright/Chromium for the review-room checks. The first sandboxed server attempt could not bind loopback; the authorized test rerun outside that sandbox passed. Fixtures and generated review media stayed in temporary directories or ignored `.work/`.

## Limits and next production capabilities

No real campaign footage, complete editorial playback, audio listening, destination preview or live publishing was reviewed. The separate static browser board is a local file with a relative link to the source video; its generated markup and frame files were inspected. The adapted review room was exercised in Chromium. Metadata checks cover the existing Reel export preset; intentionally different deliverables can omit `--expect-reel`.

The [comparison](../research/video-harness-review.md) records which upstream capabilities were adapted, reinforced or deferred. Take One's complete canvas renderer, audio/music stack, gallery and macOS tools were not installed or tested. The current change does not implement montage assembly, transcription, caption alignment or audio mixing. A concrete Reel production brief should guide the next capability selected.
