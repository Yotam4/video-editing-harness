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

## Revise with notes on the actual frame

For an editing session with multiple exported cuts, use the adapted local review room (Node 18+, FFmpeg/ffprobe and a browser):

```sh
node scripts/review-room/server.mjs .work/reel-cuts 4400
```

Open `http://127.0.0.1:4400`. The room lists MP4 files in that folder, newest first. Pick a cut, play or step through its decoded frame timestamps, then click the picture to pin a note. The player and saved snapshot preserve the video's displayed aspect. A 60fps export is not mislabeled as 30fps. Choose a second cut to compare their playback at matching elapsed times; different shot timings still need editorial judgment.

Notes and snapshots stay in `<cuts-folder>/review-notes/`. “Finish review” records a local batch in `sent.log`; it sends no external message and does not wake an inactive agent. During revision, read `notes.json` and the matching `shots/<id>.jpg`, preserve the exact feedback in the Git content record, then change the affected shot/event. The room records the source export's SHA-256 so feedback stays tied to the version reviewed. If a filename is reused for a different export, old notes are labeled as belonging to the earlier export and are not jumped to as if they matched.

Keep prior cuts. After checking the requested fix in a new export, select that export in “Compare with” before marking the original note done. The stored resolution names the replacement cut and its hash. Marking a note done records a human/editor decision; it does not automatically prove the fix. Reopen unresolved notes and report any disagreement. Save a new named export instead of silently replacing the accepted version.

The room adapts [Take One's MIT code](../../THIRD_PARTY.md). It adds frame timing, portrait geometry, version binding and resolution records to that workflow. The static review board remains useful for a single-export technical review. Neither tool assembles a montage or checks music quality by listening.

## Current gaps and the two-repo comparison

Baseline inspected at [`0d9de3d43c80f9ed36af25a10134e4a586a3433e`](https://github.com/Yotam4/video-editing-harness/commit/0d9de3d43c80f9ed36af25a10134e4a586a3433e).

Our planning guidance is substantially broader than our executable editing tools. The baseline has a one-shot overlay renderer and product-video planning; it has no general timeline assembler, transcript alignment, audio mixing pipeline or automated cut review. This change supplies cut review and an edit record. It does not claim the other capabilities are implemented.

The [two-repo review](../research/video-harness-review.md) compares this baseline with Tal Siach's [Take One at `43fd27b`](https://github.com/talsiach/take-one/tree/43fd27b8878241deb50a5884a154b173272b858f). The review-room files are the selective code adaptation; the export-review CLI and edit template are first-party additions. Source hashes, license and changes are retained in [the manifest](../../references/take-one-adaptation.json).

Next opportunities are timeline assembly, Hebrew caption alignment and speech/music/ambient mixing. Select those tools for a concrete production brief. Take One's wide-frame clip extraction, intentional playback-rate changes and macOS subject matting are unsuitable defaults for our native footage. Do not import its entire rendering/music stack to close one editing gap.
