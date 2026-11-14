# Video harness review and adaptation boundary

Checked: 2026-11-14. Scope: video editing and review improvements for `Yotam4/video-editing-harness`, compared with Tal Siach's `talsiach/take-one`.

## Identity finding

The working source for this round is **[Take One by Tal Siach](https://github.com/talsiach/take-one)**, pinned at [`43fd27b8878241deb50a5884a154b173272b858f`](https://github.com/talsiach/take-one/commit/43fd27b8878241deb50a5884a154b173272b858f), package version 0.1.0, MIT, copyright 2026 Tal Siach. Its public description, author and broad script/reference collection match the owner's remembered “tal video harness something.” The owner did not provide an exact URL; this is the source selected from that description. It is not Tal Raviv's work or the unrelated Tal the Traveler onboarding document.

The 2026-11-10 investigation left Tal's identity unresolved. That dated finding explains the previous boundary; the pinned source above now supplies the comparison. Our own baseline was `0d9de3d43c80f9ed36af25a10134e4a586a3433e`. Both repositories were checked out and inspected. Tal's checkout remains a reference, with no edits.

## What the two repositories contribute

Our harness already has the brand and Hebrew procedures, own-post evidence, content classification, copy/design preservation, authentic product proof and the one-shot FFmpeg renderer. Its video planning exceeds its executable editing support. Take One adds a broad code-rendered studio workflow, deterministic canvas rendering, text/edge/plate/audio audits, a review pack and a frame-note review room. Its README reports macOS-only experience and emphasizes product/brand films. Those limits matter for natural field footage and this Linux environment.

Inspected source: `README.md`, `SKILL.md`, `LICENSE`, `THIRD_PARTY.md`, `package.json`; `references/pipeline.md`, `before-the-first-cut.md`, `reviewer-brief.md`, `review-room.md`, `vertical.md`, `words.md`, `audio.md`; `scripts/clip.py`, `cutseq.py`, and both review-room files. Its package lists Node 18+, Chrome, FFmpeg and `playwright-core`; caption/music helpers can need additional tools. We did not install or claim to run its entire pipeline.

| Source method or tool | Decision | Concrete change or boundary |
| --- | --- | --- |
| Frame-pinned notes and cut comparison (`scripts/review-room/`) | Adapt now | Port the MIT review room under `scripts/review-room/`; keep notes and snapshots local, compare versions, bind each note to the export hash and record which revised cut resolved it. |
| Review-room frame stepping | Improve during adaptation | Upstream assumes 30fps. Our room uses decoded presentation timestamps, so notes and stepping work with 30fps, 60fps and variable frame intervals. |
| Review-room image geometry | Improve during adaptation | Upstream fixes the player and snapshot to 16:9. Our player uses the actual video's aspect and snapshots retain it, keeping vertical pins on the subject. |
| Review pack, exact action/cut frames (`reviewer-brief.md`, `pipeline.md`) | Adopt method | Shared `scripts/review_video.py` extracts full-resolution frames around supplied cut indices, caption/action times and cover; measures export properties and decoding; leaves human review pending. The script is first-party code written in this round. |
| Before-first-cut review | Adapt | Check representative frames, continuity, text placement and settled payoff early; play the whole film at phone size and listen before delivery. Timing numbers are starting hypotheses, not mandatory Hebrew reading speeds. |
| Owner taste and locked decisions | Adopt within existing records | Use prior accepted brand/voice decisions at planning, copy and review. Store exact feedback, affected event/shot and accepted version in the edit record; preserve unaffected choices. No new parallel taste database. |
| Real product as proof and vertical recomposition | Reinforce | Preserve real captures and native footage; inspect people, hands, key UI and text at final aspect. Destination UI is checked in its actual preview, not guaranteed by fixed safe-area coordinates. |
| Audio measurement plus listening (`audio.md`) | Adopt distinction | Record speech, ambient, music and effect roles separately. Meters are diagnostics; they cannot approve intelligibility, seams, musical phrasing or caption sync. No automatic music, SFX or generated score is added. |
| Canvas text/plate/edge audits and deterministic `renderFrame(t)` | Defer runtime import | Useful for a future code-motion project. They cannot inspect all text already inside real footage and do not justify changing the approved renderer. |
| `clip.py` / `cutseq.py` | Do not import | `clip.py` scales to a fixed wide ratio and replays source frame sequences at 30fps, intentionally changing other source rates. `cutseq.py` depends on macOS Swift subject matting. Neither is a safe default for our native field footage on Linux. |
| Fixed 60fps master, one effect per event, every-axis 8/10 score gate | Do not make defaults | Keep the established 30fps Reel preset, purposeful sound/motion and observable acceptance conditions. Reviewer scores and upstream “7/10 ceiling” anecdotes do not predict engagement or prove quality. |
| Twelve studio jobs and hosted generation services | Selective workflow only | Use the responsibilities relevant to the brief; do not spawn twelve agents, impose repeated approval stops, add affiliate links or install paid services. Existing authorization and owner choices govern the session. |

The implementation keeps the supported one-shot renderer and adds shared review tooling; it does not yet supply montage assembly, transcription alignment or audio mixing. See [Reel editing and review](../production/reel-editing.md), [the edit record](../../templates/reel-edit.md), [validation](../validation/reel-review-2026-11-14.md) and [license/provenance](../../THIRD_PARTY.md). Imported files, source hashes and local changes are recorded in [the adaptation manifest](../../references/take-one-adaptation.json).

## Separate sources actually inspected

These are independent references inspected on 2026-11-10, **not claimed to be Tal's**.

| Source | Pinned revision / license | Inspected material | Useful contribution |
| --- | --- | --- | --- |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | [`669ab9286aa28b6c3ee30e75f181ee74319d012a`](https://github.com/latent-spaces/brag/commit/669ab9286aa28b6c3ee30e75f181ee74319d012a), release 0.5.0; MIT, copyright Shunit Haviv Hakimi | README, LICENSE, `skills/brag-slim/SKILL.md`, classic inspect/plan/deliver references and file tree | Inspect the actual app flow, make a concise creative plan, separate creative intent from rendering, choose a settled poster, package share copy separately |
| [noamdorr/saas-product-demo-video](https://github.com/noamdorr/saas-product-demo-video) | [`c93c00ff44a65eea25ac1bb773a4565c68893ff9`](https://github.com/noamdorr/saas-product-demo-video/commit/c93c00ff44a65eea25ac1bb773a4565c68893ff9); MIT, copyright Noam Dorr | README, LICENSE, skill entry point, self-check reference, iteration playbook | Asset intake; one visual argument; render critical click/cut/text frames; maintain locked decisions and narrow revision waves |
| [Official Remotion skills](https://www.remotion.dev/docs/ai/skills) and [Remotion docs](https://www.remotion.dev/docs/) | Live documentation checked 2026-11-10; no framework or skill files vendored | Skills, parameterized rendering, animation, Sequence, transitions, captions and license index | A maintained technical source for a future programmatic renderer; reusable composition props and timeline primitives |

The references in this historical table contributed planning synthesis, not copied code or media. The Take One review-room adaptation above is separately attributed and licensed. Recommendations are not measured performance findings. A repository's software license does not automatically settle rights to each bundled media asset; Brag's README separately credits its music and SFX. Remotion's framework licensing is separate from the license of an external skill; check its [current terms](https://www.remotion.dev/docs/license) before deployment.

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
| New renderer or music bundle | Defer | Choose tooling for an authorized production task. The separately scoped Take One review-room adaptation does not import its rendering or music stack. |

## What belongs where

- **Knowledge documents:** methods, evidence, source revisions, limitations, motion vocabulary, video archetypes and QA reasoning.
- **Small production skill:** detect a product-video request; inspect the app; choose the archetype; obtain proof; produce a plan; hand a constrained scene contract to the selected renderer; inspect and deliver.
- **Recommendations:** tone, target duration, signature move, music posture, stronger comparison and a proposed experiment. Explain the reason and allow the brief to override them.
- **Per-item Git record:** brief, exact copy, factual claims and evidence, scene timing, locked decisions, accepted version, asset references and unresolved checks.
- **Drive:** recordings, stills, narration, music, rendered previews and final exports. Git keeps their stable source IDs/URLs and version labels.

Use the [first-party product-video playbook](../production/product-video-playbook.md) with the [shared editing/review workflow](../production/reel-editing.md). Further upstream imports should name the exact source files and license at a pinned revision rather than installing the whole toolkit by default.
