---
name: el-hamaayan-reel
description: Use when creating, editing, reviewing, or exporting an El Hamaayan / אל המעיין Instagram Reel (ריל). Covers footage selects, edit records, cut and caption review, audio checks, and the approved natural one-shot renderer with Hebrew overlay text and native 9:16 framing.
---

# El Hamaayan Reel

Create El Hamaayan Reels that feel like real travel footage with one strong idea, not polished ads. Preserve approved footage and copy; revise only what the owner asked to change.

Read [Reel editing and review](../../docs/production/reel-editing.md) for the shared editing procedure and current tool capabilities. Choose one-shot, montage, spoken story or product/demo from the brief. The existing renderer implements the one-shot style; use an available editor or a selected production project for other treatments. Do not silently flatten them into a single static overlay.

## Required routing

- Read `el-hamaayan-brand-voice-wordmark` before drafting or rewriting Hebrew copy. Use `humanize-he` when available; otherwise use the available natural-Hebrew guidance, including `speak-like-yotam` when writing in the owner's voice. Do not block on an unavailable legacy skill name.
- Once the owner approves or dictates copy, lock the words and punctuation. Only visual line breaks may change without renewed approval.
- Use the Google Drive skill to find, download, version, or upload shared footage. Do not publish to Instagram unless explicitly requested.

- For new Reel concepts, use `el-hamaayan-engagement-lab` for own-post evidence and the creative brief, `el-hamaayan-visual-design` for image/text hierarchy and placement, and `el-hamaayan-social-templates` for verified references. Resolve companions by frontmatter name. For a small approved revision, preserve the existing concept and run only the relevant checks; do not reopen analytics or redesign by default.

## Default creative direction

Use this one-shot format when the user asks for a simple, natural Reel or references the approved Sarit Hadad/Nahal El Al Reel:

- One continuous 10–15 second shot with motion throughout and a natural reveal.
- Prefer genuinely vertical 9:16 footage. Respect rotation metadata: a file reported as landscape pixels may already display vertically.
- Keep the full native frame. Never crop, zoom, track, or reframe silently.
- Show the complete text from the first frame through the last frame unless the user asks for timed changes.
- Use small, clean white Hebrew text, bold enough for a phone screen, centered slightly above the middle.
- Use no text card, opaque background, logo, transition, artificial zoom, or ad-like effect.
- A subtle dark outline is allowed only to keep white text readable over footage.

This is a default, not a universal Reel rule. Follow an explicit montage, logo, animation, audio, or timing brief when the user requests one.

## Workflow

1. Ground the Reel.
   - Determine whether this is a new Reel or a revision.
   - Inspect the selected video itself at the beginning, middle, and end; filenames and media-index descriptions are not visual QA.
   - For a new one-shot Reel, choose a clip with continuous movement, a visible subject, and a payoff or reveal.
2. Protect the frame.
   - Read coded dimensions and rotation metadata.
   - Compute displayed dimensions after rotation before deciding whether the source is vertical.
   - If the displayed aspect ratio is not close to 9:16, choose another clip or show the owner crop/padding options. Do not invent a crop.
3. Lay out Hebrew correctly.
   - Keep locked copy character-for-character.
   - Choose deliberate phone-readable line breaks; keep the block to roughly five lines when possible.
   - Wrap each rendered line with Unicode RTL controls and an ending right-to-left mark so colons, quotation marks, numbers, and mixed-language fragments land correctly.
   - Render a sample frame and inspect the punctuation visually. Do not infer RTL correctness from the source string.
4. Render and verify.
   - Default export: MP4, H.264, 1080×1920, 30fps, square pixels, `yuv420p`.
   - Use `scripts/render_one_shot_reel.py` for the approved one-shot style.
   - Run `python3 scripts/review_video.py <export> .work/<review-version> --expect-reel` from the repository root for a review board, full-resolution opening/middle/ending frames, measured export properties and decoding checks. Use `--at`, `--cut-frame` and `--cover-frame` for actual caption, action, cut and cover checks.
   - Verify that the scenery and people remain visible, the text never leaves frame, punctuation is RTL-correct, and no unintended crop or rotation remains.
   - Play the entire sequence muted at phone size, then listen and check audio/caption timing. Record playback or listening as pending when unavailable; successful decoding and sampled frames cannot approve either.
5. Deliver.
   - Use a new version number for each approved revision.
   - Upload to the established Reel folder only when requested or already authorized by the ongoing task.
   - Report the duration, dimensions, and what changed in one short handoff.

## Approved one-shot typography

| Property | Default |
| --- | --- |
| Font | DejaVu Sans Bold or the closest clean Hebrew sans |
| Size | 58 px at 1080×1920 |
| Color | White |
| Readability | 2 px translucent dark outline; no shadow or box |
| Position | Top-center alignment with the block starting around y=650 |
| Line count | About 3–5 |
| Timing | Full duration |

Treat these as the preserved Sarit Hadad Reel settings. Change them when the footage or explicit brief requires it.

## Sharp edges

- DJI clips often store a 90° rotation tag while reporting landscape coded dimensions. Cropping from the coded dimensions can remove the hikers and most of the landscape.
- Center alignment does not make Hebrew RTL. Use bidi controls and inspect punctuation on the rendered frame.
- Do not cover a failed crop with a pan, zoom, or duplicated blurred background. Return to the native frame.
- A contact sheet scaled too small can hide punctuation errors. Inspect at least one full-resolution frame.

## Keep in sync

- `humanize-he`, when available, and the applicable owner-voice guidance support natural Hebrew.
- `el-hamaayan-engagement-lab`, `el-hamaayan-visual-design`, `el-hamaayan-social-templates`, and `self-attention` own evidence, composition, templates, and carousel sequence respectively; keep production and the approved one-shot settings here.
- `el-hamaayan-brand-voice-wordmark` owns El Hamaayan voice.
- Update this skill when the owner explicitly approves a reusable Reel rule; do not generalize a one-off creative choice.
