# Reel editing and review

Version: 1. Checked: 2026-11-14. First-party production guidance.

Use the existing Reel procedure for footage and the product-video procedure for app proof. This document gives both a shared edit record and a reproducible review step. It adds no new content recipe or publishing automation.

## Start with the material and the accepted version

Read the current content record. Inspect real footage with its sound, displayed orientation, duration and available action. Record source Drive IDs and versions. A clip description is a search aid; it cannot establish the best in/out points. On a revision, preserve accepted copy, font files, actual weights, framing, renderer and unaffected timing.

Choose an editing treatment that fits the material:

| Treatment | Editing decisions | Current tool boundary |
| --- | --- | --- |
| Natural one-shot | One useful in/out range, native frame, one readable overlay and a visible payoff | Existing `skills/el-hamaayan-reel/scripts/render_one_shot_reel.py` |
| Montage | Selects, shot order, continuity, cut points and a reason for every cut | Use an available editor or an explicitly selected production project; there is no bundled montage renderer yet |
| Spoken story | Speech selects, necessary context, captions, useful supporting shots and audible pauses | Requires an editor/caption workflow; no transcription or word timing is inferred from the footage |
| Product/demo | Verified start, action and settled result; legible UI and accurate tap/cursor targets | Use the [product-video playbook](product-video-playbook.md) and the chosen production project |

The one-shot look remains an approved style. A request for a different treatment does not inherit its full-duration text or 10–15 second recommendation automatically.

## Make an edit record before assembling a complex Reel

Use [the edit template](../../templates/reel-edit.md) inside the existing content record. For a small revision, fill only the affected rows.

Keep source time distinct from timeline time. Record the source in/out range, timeline start/end and output frame rate for each shot. Note whether an out point is exclusive. Put caption changes, taps, reveals, cut frames and the settled payoff on the same timeline. For a product interaction, retain the states required to understand the result.

Lock exact on-screen copy separately from line breaks and caption timing. Do not rewrite speech into a quote without checking the recording. Inspect Hebrew shaping, punctuation and mixed numbers on the actual render. A transcript alone does not establish subtitle timing.

Choose what leads the pace: speech, a natural action, a reveal, or measured music beats. Remove repeated setup; hold the result long enough to understand. Music is optional. Record the role and source of speech, ambient sound, music and effects; check their balance through listening. Do not treat a stream being present or decoded as proof that it is audible, intelligible or synchronized.

## Review the actual export

With Python 3.11+ and FFmpeg/ffprobe on PATH, run from the repository root:

```sh
python3 scripts/review_video.py .work/reel-v2.mp4 .work/review-v2 \
  --at 1.2 --at 4.5 --cut-frame 90 --cover-frame 150 --expect-reel
```

Use actual edit points. This example's numbers are placeholders, not a timing preset. `--cut-frame 90` means zero-based frame 90 is the first frame of the new shot. The tool extracts frames 89 and 90. `--at` uses presentation timestamps relative to the first decoded frame, so it also works with variable frame intervals; it selects the frame at or immediately before that time. Times must fall between the first and last frame timestamps. The tool does not detect cuts automatically.

The tool writes:

- `index.html`: local playback at phone width and a board linking to full-resolution frames.
- `frame-*.png`: opening, middle, ending and the requested cut/action/cover frames.
- `review.json`: source hash, measured metadata, audio presence, decode results, selected timestamps and pending human checks.

The review directory must be new. Keep it under ignored `.work/` during production; save authorized review media with the production files in Drive. The HTML links to the original video with a relative path. Keep that relationship when moving the board, or provide the video separately. The board does not upload or embed a copy of the source.

`--expect-reel` checks the existing default export: 1080×1920, H.264, `yuv420p`, square pixels, zero rotation, MP4 and constant 30fps presentation timestamps. A failed expected property returns exit code 1 and leaves the report for diagnosis. Omit this option for an intentionally different delivery specification. Decoding checks video and available audio streams; it cannot assess creative quality.

Complete these human passes and record who checked which version:

1. Inspect opening, longest line, mixed Hebrew/numbers, exact action, both sides of each important cut, settled result and cover at full resolution.
2. Play the whole sequence muted at phone size. Check that a stranger can understand the premise, action and payoff, and that text holds and continuity work in motion.
3. Listen to the whole export. Check speech clarity, competing music, clipped words, abrupt audio cuts, ambience and caption sync. If listening is unavailable, leave it pending.
4. Check the actual destination preview for UI obstruction and the independent cover crop when publishing is authorized. No fixed safe rectangle guarantees every destination's UI.

The tool always starts human checks as `not_reviewed`. Summarize completed checks in the Git handoff; never promote an automated decode or a contact sheet to playback approval.

## Current gaps and Tal comparison

Baseline inspected at [`0d9de3d43c80f9ed36af25a10134e4a586a3433e`](https://github.com/Yotam4/video-editing-harness/commit/0d9de3d43c80f9ed36af25a10134e4a586a3433e).

Our planning guidance is substantially broader than our executable editing tools. The baseline has a one-shot overlay renderer and product-video planning; it has no general timeline assembler, transcript alignment, audio mixing pipeline or automated cut review. This change supplies cut review and an edit record. It does not claim the other capabilities are implemented.

Tal's exact repository URL is still required for the requested comparison. The [source review](../research/video-harness-review.md) records the unresolved identity. Do not substitute another project or describe these first-party additions as an import from Tal.

Once the URL is supplied, inspect the exact revision, entry point, license, dependencies and a representative editing project. Compare selective opportunities in this order: footage selects and edit decisions; timeline assembly and revision; Hebrew captions and timing; speech/music/ambient mixing; preview and final-render checks. Record adopt/adapt/defer decisions with source paths and versions. Retain notices for any copied licensed material, keep media external, and test the selected tools with temporary fixtures before calling them supported.
