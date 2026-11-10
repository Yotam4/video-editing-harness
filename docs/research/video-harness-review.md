# Video harness review and adaptation boundary

Checked: 2026-11-10. Scope: reusable product-video methods for our own `Yotam4/video-editing-harness`.

## Identity finding

**The exact harness referred to as Tal's, Tala Travelers or Trail Travelers has not been identified.** Personal Context was unavailable for this investigation. Exact-name public searches, Tal Raviv searches and connected GitHub searches did not establish an attributable repository. A search result about Tal Raviv's AI tutorials is not evidence that he owns a particular video harness. Our target repository is our own; do not relabel it as Tal's.

The remaining missing input is the third-party repository URL or an original post linking it. Once supplied, inspect its exact revision, entry point, dependencies, license and examples before adding code. This finding does not block first-party product-video planning.

## Separate sources actually inspected

These are independent references, **not claimed to be Tal's**.

| Source | Pinned revision / license | Inspected material | Useful contribution |
| --- | --- | --- | --- |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | [`669ab9286aa28b6c3ee30e75f181ee74319d012a`](https://github.com/latent-spaces/brag/commit/669ab9286aa28b6c3ee30e75f181ee74319d012a), release 0.5.0; MIT, copyright Shunit Haviv Hakimi | README, LICENSE, `skills/brag-slim/SKILL.md`, classic inspect/plan/deliver references and file tree | Inspect the actual app flow, make a concise creative plan, separate creative intent from rendering, choose a settled poster, package share copy separately |
| [noamdorr/saas-product-demo-video](https://github.com/noamdorr/saas-product-demo-video) | [`c93c00ff44a65eea25ac1bb773a4565c68893ff9`](https://github.com/noamdorr/saas-product-demo-video/commit/c93c00ff44a65eea25ac1bb773a4565c68893ff9); MIT, copyright Noam Dorr | README, LICENSE, skill entry point, self-check reference, iteration playbook | Asset intake; one visual argument; render critical click/cut/text frames; maintain locked decisions and narrow revision waves |
| [Official Remotion skills](https://www.remotion.dev/docs/ai/skills) and [Remotion docs](https://www.remotion.dev/docs/) | Live documentation checked 2026-11-10; no framework or skill files vendored | Skills, parameterized rendering, animation, Sequence, transitions, captions and license index | A maintained technical source for a future programmatic renderer; reusable composition props and timeline primitives |

All recommendations below are synthesis for Ela Maayan, not measured performance findings. No third-party source code, music, SFX, example projects, photos or videos were copied into this harness, and no renderer was installed or tested. If substantial MIT-licensed material is copied later, retain its copyright and permission notice. A repository's software license does not automatically settle rights to each bundled media asset; Brag's README separately credits its music and SFX. Remotion's framework licensing is separate from the license of an external skill; check its [current terms](https://www.remotion.dev/docs/license) before deployment.

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
| New renderer, music bundle or Tal source import | Defer | Not needed to classify, brainstorm or create a verified storyboard. Choose tooling only for an authorized production task. |

## What belongs where

- **Knowledge documents:** methods, evidence, source revisions, limitations, motion vocabulary, video archetypes and QA reasoning.
- **Small production skill:** detect a product-video request; inspect the app; choose the archetype; obtain proof; produce a plan; hand a constrained scene contract to the selected renderer; inspect and deliver.
- **Recommendations:** tone, target duration, signature move, music posture, stronger comparison and a proposed experiment. Explain the reason and allow the brief to override them.
- **Per-item Git record:** brief, exact copy, factual claims and evidence, scene timing, locked decisions, accepted version, asset references and unresolved checks.
- **Drive:** recordings, stills, narration, music, rendered previews and final exports. Git keeps their stable source IDs/URLs and version labels.

Use the [first-party product-video playbook](../production/product-video-playbook.md) now. Keep the unidentified Tal URL as an explicit unresolved source, rather than silently installing a plausible alternative.
