# Video harness comparison: Tal the Traveler and Ela Maayan

Checked: 2026-11-14. Confirmed source: **[talthetraveler/VIDEO-EDITING](https://github.com/talthetraveler/VIDEO-EDITING)**, identified by the owner's repository screenshot. Pinned revision: [`0f8f1bea35a32d16659a58b8c203bc70ddf1d24b`](https://github.com/talthetraveler/VIDEO-EDITING/commit/0f8f1bea35a32d16659a58b8c203bc70ddf1d24b).

## Source identity and scope

This is Tal Dooreck Aloni's footage-editing system, described in its AGENTS.md as the editor for `@talthetraveler`. It is the source the owner requested. The earlier selection of Tal Siach's Take One was incorrect. Take One remains a separately credited source of the optional review room already in this branch; it is not evidence for what Tal the Traveler's harness does.

Our baseline is `Yotam4/video-editing-harness` at `0d9de3d43c80f9ed36af25a10134e4a586a3433e`. Both checkouts were inspected; the reference checkout was left unmodified. Its root has no LICENSE and `system/package.json` declares `UNLICENSED` and `private: true`. This round adapts methods with first-party code and knowledge, rather than vendoring its scripts, skills, personal standards or media. [Source paths and hashes](../../references/tal-video-editing-review.json) record the exact evidence.

Inspected material includes AGENTS.md, README.md, master-instruction and router sections, MASTER-PROMPT.md, selected LESSONS entries including recent corrections, `formats/human-story.md`, the caption/multilingual/reference toolboxes, and the actual autotrim, project, caption-timing, builder, self-review and beat-check code. The full upstream pipeline was not installed or run. Several scripts contain fixed Windows paths and depend on unavailable footage, Frame.io caches or large audio/model installations.

## What the two repositories contribute

Our harness is stronger in Ela Maayan brand/context, own-post evidence, independent content axes, Hebrew copy/design preservation and the approved native one-shot style. Tal's repo goes much further into raw-footage editing: source indexing, story selection, per-shot edit specifications, proxy/HQ clocks, caption alignment, final-file QA and feedback recorded as lessons. Its useful lesson is to improve selection and timing before adding more visual effects.

The toolbox is deliberately subordinate to one entry procedure because overlapping skill triggers previously lost the house rules. We retain our existing content router and thin production skills, adding a focused footage-editing procedure rather than installing all of Tal's toolbox triggers.

| Upstream source or method | Decision | Ela Maayan implementation or boundary |
| --- | --- | --- |
| Editable project and source pointers (`system/scripts/lib/project.mjs`, master §2b) | Adapt | A first-party JSON shot list keeps source references, selected ranges, frame counts and exact copy separate from exports. The renderer reads it without rewriting it, writes a new version directory, and keeps the original files unchanged. Named plan versions remain recoverable in the content record; typed undo/redo operations are not implemented. |
| Story selection before assembly (`tal-video-editor/SKILL.md`, `formats/human-story.md`, LESSONS 173–174) | Adopt method | Read and inspect the full relevant source before ranking moments. Keep reactions and the actual payoff; do not turn a coherent story into a collection of high-scoring fragments. Natural one-shots stay valid. |
| Speech-based cut boundaries (`autotrim.mjs`, LESSONS 22) | Adapt | Select complete thoughts from verified timings and listen around cuts. Lead/tail padding is footage-specific; Tal's numerical pads are not universal defaults. The new renderer checks selected source spans and refuses a speech cue crossing its shot boundary. It does not detect complete thoughts or words by itself. |
| Proxy/HQ timestamp rebasing (`check-beats.mjs`) | Implement | Each local source declares `clock_start`; selected full-source time maps to local-file time once. Out-of-span windows fail before rendering. This prevents using full-clip timestamps directly on a fetched HQ excerpt. |
| One alignment clock for beat boundaries and captions (`lib/caption-timing.mjs`, `caption-qc`) | Implement | Speech cues must reference the same `alignment_id` as their source. Starts map independently to the output timeline; a minimum reading hold cannot queue later captions behind earlier ones. Overlap fails for revision instead of silently delaying speech. |
| Caption evidence emitted by the build (`selfreview.mjs`, `caption-qc`) | Implement | The build writes `cues.json` with the exact text, source timing, final frame range and text hash. Review frames come from the rendered MP4 at caption changes and both sides of every cut. This is structural evidence, not independent ASR or wording verification. |
| Multilingual records (`multilingual-dialogue-qc`) | Adapt | Original wording, displayed text, source/display language, alignment identity, translation status and uncertainty have separate fields. Do not infer language from a fluent translated transcript. Timing, wording and visual RTL checks are reported separately. |
| Orientation and range defects (LESSONS 17, 184; builder color-range conversion) | Adapt | Honor display metadata, inspect content orientation, allow an explicit post-metadata rotation, and never crop silently. Normalize pixel aspect/range per source before joining. Known HDR inputs require a deliberate inspected SDR derivative. The final frame count, CFR preset and limited-range tag are checked on fixtures. |
| Low-resolution first cut and one successful example before batching (master §2b; LESSONS 171) | Adopt proportionately | A 432×768 preview and 1080×1920 export use the same shot/cue clock. Use a representative draft to learn taste before generating a batch. Existing authorization for a complete film still applies; this adds no mandatory permission stop. |
| Final-file QA and false-positive discipline (`selfreview.mjs`, `check-beats.mjs`, `caption-qc`) | Adopt | Decode the export, inspect actual frames and play/listen when available. Energy, face detection and re-transcription are leads, especially in noisy field footage; a flag is not permission to recut automatically. A no-face frame can be correct scenic footage. |
| Lessons carry evidence and scope (`LESSONS.md`) | Adopt | Save accepted feedback with source/version, reason, affected treatment and superseded choice. A correction from one content format does not become a universal brand rule. |
| Tal's look, audio defaults and distribution | Keep source-specific | English all-caps/yellow emphasis, Social Accords titles/logo/outro, fixed cut rates, Frame.io paths, Metricool/ShortSync behavior and deletion rules are Tal's preferences and environment. Keep Ela Maayan's Hebrew, optional music/CTA and Git/Drive/Notion model. |

## Resolve conflicts before adapting defaults

This repository contains dated, conflicting instructions. The master and LESSONS 176 (2026-11-02) ask for cleaning noise under speech, replacing the 2026-10-21 raw-audio preference. Older router/toolbox text still describes no denoise or per-shot denoise, and `build-edit.mjs` defaults denoising off unless requested. Its AGENTS.md introduction also says everyday denoising always runs. The master is the declared instruction authority; the executable default is a separate observed fact. We do not import any of these as Ela Maayan's default or claim the executable pipeline already implements the latest direction.

The same caution applies to one-word versus phrase captions and old machine/tool availability. Read the relevant format, current accepted correction and code together. Measurements and owner preferences remain dated; none establishes an Instagram ranking rule or a prediction that our Reels will perform better.

## Shipped and deferred

Shipped here: `scripts/render_reel_edit.py`, the [JSON plan template](../../templates/reel-edit.json), the [editing workflow](../production/reel-editing.md), automatic build-emitted cue and review data, and integration tests for source clocks, mixed frame rates, rotation, exact caption boundaries and immutable source/output versions. Existing one-shot rendering remains available.

Still requires a selected production tool: transcription/forced alignment, semantic moment selection, typed undo/redo, automatic camera tracking, denoising, music ducking and audio mixing. The new renderer preserves or mutes source audio; it does not implement those processors. Keep technical validity, editorial judgment, listening and translation review separate.

## Separate Take One review-room provenance

The optional `scripts/review-room/` code was adapted from [talsiach/take-one](https://github.com/talsiach/take-one) at `43fd27b8878241deb50a5884a154b173272b858f`, under MIT, copyright 2026 Tal Siach. It supplies frame-pinned notes and comparison between cuts. It is a supplemental source, not the repo identified in the owner's screenshot. Its [adaptation manifest](../../references/take-one-adaptation.json) and [license notice](../../THIRD_PARTY.md) remain accurate. No Take One branding, music or rendering stack is imported.

## Separate sources actually inspected

These are independent references inspected on 2026-11-10, **not claimed to be Tal's**.

| Source | Pinned revision / license | Inspected material | Useful contribution |
| --- | --- | --- | --- |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | [`669ab9286aa28b6c3ee30e75f181ee74319d012a`](https://github.com/latent-spaces/brag/commit/669ab9286aa28b6c3ee30e75f181ee74319d012a), release 0.5.0; MIT, copyright Shunit Haviv Hakimi | README, LICENSE, `skills/brag-slim/SKILL.md`, classic inspect/plan/deliver references and file tree | Inspect the actual app flow, make a concise creative plan, separate creative intent from rendering, choose a settled poster, package share copy separately |
| [noamdorr/saas-product-demo-video](https://github.com/noamdorr/saas-product-demo-video) | [`c93c00ff44a65eea25ac1bb773a4565c68893ff9`](https://github.com/noamdorr/saas-product-demo-video/commit/c93c00ff44a65eea25ac1bb773a4565c68893ff9); MIT, copyright Noam Dorr | README, LICENSE, skill entry point, self-check reference, iteration playbook | Asset intake; one visual argument; render critical click/cut/text frames; maintain locked decisions and narrow revision waves |
| [Official Remotion skills](https://www.remotion.dev/docs/ai/skills) and [Remotion docs](https://www.remotion.dev/docs/) | Live documentation checked 2026-11-10; no framework or skill files vendored | Skills, parameterized rendering, animation, Sequence, transitions, captions and license index | A maintained technical source for a future programmatic renderer; reusable composition props and timeline primitives |

The references in this historical table contributed planning synthesis, not copied code or media. The separate Take One review-room adaptation is attributed in THIRD_PARTY.md; it is not the requested Tal source. Recommendations are not measured performance findings. A repository's software license does not automatically settle rights to each bundled media asset; Brag's README separately credits its music and SFX. Remotion's framework licensing is separate from the license of an external skill; check its [current terms](https://www.remotion.dev/docs/license) before deployment.

## Adopt, adapt and defer

| Method | Decision | Our implementation boundary |
| --- | --- | --- |
| Product inspection before story | Adopt | Prove the actual live/released interaction. Code can identify a candidate feature; it does not prove rollout, availability or the result seen by a user. |
| App use as centerpiece | Adopt | Show a real starting state, one action and the resulting state. This is stronger product evidence than a sequence of landing-page slogans. |
| Brief distinct from renderer | Adopt | The creative brief names the viewer outcome, proof, scene beats, text and motion intent. A renderer receives an implementation contract. |
| Reusable animation primitives | Adapt | Shared camera, cursor, crop, reveal, type and caption modules get parameterized inputs. A single signature motion may unify a film; animation remains optional. |
| Review exact interaction/cut frames | Adopt | Inspect the target under the cursor, text hold, longest Hebrew line, last/first frame across every cut, cover and end state. Still-frame QA does not prove playback or audio quality. |
| Preserve locked decisions | Adopt | Use Git decisions, source versions and named variants; fix a requested word or timing without resetting the entire concept. |
| Default polished launch tone, music and roughly 20-second length | Adapt | Offer as one direction. Our brand may prefer friends, warmth, humor or a quiet practical demonstration; choose duration from the job and reading needs. |
| Fixed scene counts, reading-speed numbers, beat grids | Recommendation only | Starting hypotheses from practitioner workflows. Test phone readability and real playback; Hebrew text and narration can set the pace instead of music. |
| Reconstructed UI | Restrict | Prefer real capture or the actual source component. A stylized reconstruction needs verified labels, states and geometry and must be identified as such; never imply an unbuilt feature exists. |
| First-frame replacement guarantees every platform's thumbnail | Do not adopt as a guarantee | Export a deliberately chosen cover. Check the destination's actual cover interface; do not assume all services select the first frame or silently modify accepted timing. |
| Claimed validation percentages or automatic render success | Do not adopt | Report the checks actually run and their coverage. A successful build does not prove readable content, correct clicks or smooth motion. |
| Additional motion renderer or music bundle | Defer | Choose tooling for an authorized production task. The separately scoped Take One review-room adaptation does not import its rendering or music stack. |

## What belongs where

- **Knowledge documents:** methods, evidence, source revisions, limitations, motion vocabulary, video archetypes and QA reasoning.
- **Small production skill:** detect a product-video request; inspect the app; choose the archetype; obtain proof; produce a plan; hand a constrained scene contract to the selected renderer; inspect and deliver.
- **Recommendations:** tone, target duration, signature move, music posture, stronger comparison and a proposed experiment. Explain the reason and allow the brief to override them.
- **Per-item Git record:** brief, exact copy, factual claims and evidence, scene timing, locked decisions, accepted version, asset references and unresolved checks.
- **Drive:** recordings, stills, narration, music, rendered previews and final exports. Git keeps their stable source IDs/URLs and version labels.

Use the [first-party product-video playbook](../production/product-video-playbook.md) with the [shared editing/review workflow](../production/reel-editing.md). Further upstream imports should name the exact source files and license at a pinned revision rather than installing the whole toolkit by default.
