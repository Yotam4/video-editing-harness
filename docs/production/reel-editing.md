# Reel editing and review

Version: 2. Checked: 2026-11-14. First-party production guidance adapted from the confirmed Tal the Traveler comparison.

Use the existing Reel procedure for footage and the product-video procedure for app proof. This document gives both a shared edit record and a reproducible review step. It adds no new content recipe or publishing automation.

## Start with the material and the accepted version

Read the current content record. Inspect real footage with its sound, displayed orientation, duration and available action. Record source Drive IDs and versions. A clip description is a search aid; it cannot establish the best in/out points. On a revision, preserve accepted copy, font files, actual weights, framing, renderer and unaffected timing.

Choose an editing treatment that fits the material:

| Treatment | Editing decisions | Current tool boundary |
| --- | --- | --- |
| Natural one-shot | One useful in/out range, native frame, one readable overlay and a visible payoff | Existing `skills/el-hamaayan-reel/scripts/render_one_shot_reel.py` |
| Montage | Selects, shot order, continuity, cut points and a reason for every cut | `scripts/render_reel_edit.py` assembles a JSON shot list at natural speed |
| Spoken story | Speech selects, necessary context, captions, useful supporting shots and audible pauses | The shot-list renderer supports timed captions from supplied alignment; transcription/forced alignment requires a selected tool |
| Product/demo | Verified start, action and settled result; legible UI and accurate tap/cursor targets | Use the [product-video playbook](product-video-playbook.md) and the chosen production project |

The one-shot look remains an approved style. A request for a different treatment does not inherit its full-duration text or 10–15 second recommendation automatically.

## Make an edit record before assembling a complex Reel

Use [the edit template](../../templates/reel-edit.md) inside the existing content record. For a small revision, fill only the affected rows.

Keep source time distinct from timeline time. Record the source in/out range, timeline start/end and output frame rate for each shot. Note whether an out point is exclusive. Put caption changes, taps, reveals, cut frames and the settled payoff on the same timeline. For a product interaction, retain the states required to understand the result.

Lock exact on-screen copy separately from line breaks and caption timing. Do not rewrite speech into a quote without checking the recording. Inspect Hebrew shaping, punctuation and mixed numbers on the actual render. A transcript alone does not establish subtitle timing.

Choose what leads the pace: speech, a natural action, a reveal, or measured music beats. Remove repeated setup; hold the result long enough to understand. Music is optional. Record the role and source of speech, ambient sound, music and effects; check their balance through listening. Do not treat a stream being present or decoded as proof that it is audible, intelligible or synchronized.

## Select moments before adding effects

Inspect the relevant source collection before choosing a cut. Filenames, model tags and transcript scores can find candidates; they cannot prove which moment carries the story. For one conversation, keep its context, complete thoughts, reactions and real payoff together. A scenic reveal can be complete with no dialogue or CTA. For a reference-led edit, explain what makes it work and match that reason to our own footage before copying its cut times or typography.

Protect word tails and reactions at each in/out point. A quiet beat can carry meaning. Listen around the actual cut rather than deleting every gap or applying a fixed shot length. On two-camera footage, confirm shared event timing and which microphone is useful before choosing the angle. These are editorial checks; the renderer does not infer a good story or verify speech from text.

## Render an editable shot list

Copy [the JSON template](../../templates/reel-edit.json) into an ignored `.work/<item>/` production folder and replace the placeholder sources with real downloads. Source paths resolve relative to the plan file. Keep the approved plan/version and stable Drive references in the content record; derivative build logs, cue dumps and media stay outside Git.

```sh
python3 scripts/render_reel_edit.py .work/item/edit-v1.json --check
python3 scripts/render_reel_edit.py .work/item/edit-v1.json .work/item/preview-v1 --preview
python3 scripts/render_reel_edit.py .work/item/edit-v1.json .work/item/export-v1
```

`--check` probes sources and validates timing without rendering. Preview is 432×768; export is 1080×1920. Both use 30fps and the same shot/caption clock. Shots play at their natural speed, with input frame rates sampled onto the output clock. The renderer supplies hard cuts, an optional explicit rotation, native framing or explicit black padding, and original source audio or mute. It does not add automatic zooms, denoising, music, grading or transitions. Known HDR inputs are rejected until an explicit SDR derivative has been prepared and inspected.

Each shot has a source, `source_in` in the original source's seconds and an integer `frames` count. Its exclusive out point is `source_in + frames / 30`. When a local file is only a fetched excerpt, `clock_start` states which original-source timestamp its local zero represents. For example, a local excerpt starting at original second 40 with `source_in: 42` seeks local second 2. A window outside the available excerpt fails. Extra `rotate` is clockwise after metadata rotation; inspect feet, hands and faces for content that is upside down despite valid metadata.

Captions have separate roles. `overlay` uses final-timeline `start_frame` and exclusive `end_frame`, and can remain through a quiet scenic shot. `speech` uses a shot ID, source in/out seconds and the same `alignment_id` as its source. For example, after verified alignment, a cue may be:

```json
{
  "id": "spoken-1", "role": "speech", "shot": "payoff",
  "source_in": 1.2, "source_out": 2.4,
  "text": "EXACT APPROVED DISPLAY WORDING",
  "original_text": "VERBATIM SOURCE WORDING",
  "source_language": "he", "display_language": "he",
  "alignment_id": "VERIFIED_ALIGNMENT_ID",
  "translation_status": "not_applicable", "uncertainty": []
}
```

The example is a field guide, not approved copy. Keep original and displayed wording separate when translating and label translation review honestly. An alignment label enforces a shared clock; it does not establish that the supplied timing or transcription is correct. Use a suitable full-source alignment tool, then inspect and listen to the export. Do not estimate word timing from sentence length. Caption starts are mapped independently and rounded to the nearest output frame; earlier reading holds cannot delay later speech. Overlapping or cross-shot speech cues are rejected. Short holds produce review warnings without changing locked words or timing.

Each new version directory contains `cut.mp4`, renderer-emitted `cues.json`, `edit-build.json`, `captions.ass` and `review/`. Cues record exact text and its hash, source/alignment fields and final frame range. The build records the plan hash and resolved shot clocks. The review pack checks frame count and export properties and samples actual frames at cuts and caption changes. Caption times use an explicit 1/30-second timeline after joining, so concatenation rounding cannot leave a caption on screen past its out point. A successful build remains `not_approved`; readability, wording, physical orientation, full playback and listening still need review.

Source media and existing output directories are never overwritten. For a revision, save a new plan version, change the affected shot/cue only and render a new version directory. Reuse the original renderer for an existing approved one-shot revision unless changing its rendering is requested. Use a representative preview before expanding a new treatment into a batch, while continuing work already authorized by the owner.

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

The baseline had a one-shot overlay renderer and product-video planning. This change adds basic shot-list assembly, supplied-timing Hebrew captions, build-emitted cue data and review tools. It does not add transcription/forced alignment, semantic moment selection, automatic camera tracking or audio mixing.

The [two-repo review](../research/video-harness-review.md) compares this baseline with the confirmed [talthetraveler/VIDEO-EDITING at `0f8f1be`](https://github.com/talthetraveler/VIDEO-EDITING/tree/0f8f1bea35a32d16659a58b8c203bc70ddf1d24b). Its source clocks, caption discipline, selection/QA and scoped-learning methods inform our first-party implementation. [The source manifest](../../references/tal-video-editing-review.json) records what was inspected. The optional MIT review room is separately adapted from Take One and retains its own attribution.

Next opportunities are Hebrew forced alignment, speaker/camera coverage and speech/music/ambient mixing. Select those tools for a concrete production brief. Tal's Windows paths, accounts and personal style are separate from these methods; choose a capability for the job instead of installing the whole repository.
