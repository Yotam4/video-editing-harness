# Product-video playbook

Version: 3. Checked: 2026-11-14. Status: first-party planning and production guidance.

Use this when showing Ela Maayan's actual product through a screen demo, feature story, launch film, verified proof/milestone film or motion explainer. Keep the existing natural one-shot Reel workflow for an actual field clip; a video being vertical does not make it a product demo.

## 1. Choose the job independently of the format

Decide what the viewer should understand, feel or do. Awareness, consideration, action and existing-user activation are audience situations, not mandatory sequential funnels. A feature demo can introduce the product to a stranger or teach an existing user. A commercial can be a carousel or video. An infographic can be static, a carousel or animated. Classify these axes separately.

| Archetype | Main viewer job | Essential proof | Suggested story skeleton | Suitable callout |
| --- | --- | --- | --- | --- |
| App screen demo | Understand one real task | Current starting/action/result states | Recognizable task → action → visible result | Name the action the viewer needs to notice; optional invitation to try it |
| Feature video | Understand why a capability helps | Working capability and concrete situation | Situation → capability in use → useful payoff | Explain the benefit when demonstrated; avoid a disconnected feature list |
| Workflow/tutorial | Complete a task correctly | Every necessary step and current labels | Outcome preview → ordered steps → completion state | Step labels, prerequisites and a concise troubleshooting note |
| Proof/brag/milestone film | Believe a specific achievement | Dated metric, authentic usage example, accepted release or attributable quote | Achievement → evidence → human meaning | Exact scope and period; thanks can be the complete ending |
| Launch/commercial | Evaluate or act on an offer | Available feature or truthful offer and a working destination | Recognizable need → real demonstration → offer/action | One supported action and any necessary material condition |
| Motion explainer | Understand a concept quickly | Verified relationships, labels or data | Question → model/process → concrete example | Clarify the relationship; label illustrations or simulated states |
| Before/after comparison | Understand a meaningful difference | Comparable starting conditions and equivalent output | Old situation → changed action → comparable result | Name what changed, what did not, and any important limitation |

These skeletons are editorial recommendations. The intended outcome may be enjoyment, connection or brand recognition, and a CTA may be absent. Do not force a download invitation onto a complete story.

## 2. Gather the minimum useful inputs

Read the current Git knowledge and prior decisions. Infer routine choices from the request and known brand; ask only for a decision that changes the work. Record assumptions as editable choices.

- Audience situation and intended outcome; chosen archetype, format and placement.
- Current product route/version, rollout or feature-flag status and the exact task to demonstrate.
- Proof for each factual claim; approved Hebrew strings and current screen labels.
- Stable Drive IDs for source recordings, logos, screenshots and any licensed audio.
- Aspect ratio, target duration, required outputs and the existing accepted look when this is a revision.
- Voiceover/music/silence preference and caption needs; rights/source for any external asset.
- The useful next action, if one is intended, and its real destination.

A production task can start with the verified inputs available. An unsupported metric or unavailable feature is a missing proof item, not a reason to invent a sample success.

## 3. Inspect the working app

Use a current authorized build. Capture the user-facing flow rather than relying on README claims or marketing screenshots. Read code to locate the relevant components and labels when useful, then verify the behavior itself.

Prefer this source order:

1. Real recording of the intended flow with representative, publishable data.
2. Capture/render of the actual product component at the intended viewport and state.
3. A clearly identified stylized reconstruction, derived from verified states and labels, when capture is unsuitable.
4. A labeled schematic to explain an idea that has no appropriate live UI, without presenting it as an available feature.

Keep the recognizable context that explains the feature. For a forum demonstration, showing the actual forum structure can be part of the product proof; cropping it away to enlarge one label may defeat the purpose. If a screen is too dense, use a context view followed by a targeted view rather than replacing the whole flow with generic cards.

Prepare demo data and record what was substituted. Avoid putting personal account data or private messages on screen. Never fabricate a customer quote, number of users, visit, discount, performance uplift or review. Compression of a wait state must not imply a measured real-world speed claim.

## 4. Write one creative argument and a scene contract

One sentence should explain why these moments belong in this film. Then map the minimum sequence needed to deliver it. Begin with the subject or real result when that makes the idea understandable; a logo animation is not a required opening.

| Scene field | What to record |
| --- | --- |
| Job | What the viewer learns or feels in this beat |
| Source | Stable Drive ID/version or app route, build and state |
| Claim | Exact statement, evidence URL and verification date, or none |
| On-screen copy | Exact approved string and intentional line breaks |
| Interaction | Start state, action, target and resulting state |
| Timing | Start/duration, fully readable hold and intended transition |
| Motion | What changes, why it directs attention and what stays still |
| Audio | Speech/music/SFX role and asset reference; silence is valid |
| Acceptance | The observable condition that makes the scene correct |

Keep this contract in `docs/content/<format>/<recipe-or-candidate>/<slug>/`. Keep the render's source code with the production project and store media/render files in Drive. Record the harness commit and production-source version so the accepted result is reproducible.

## 5. Reusable motion modules

Build these only when a production task needs them. Each module should accept the brand, source asset, timing and crop/viewport as inputs, rather than baking one post's text or colors into a universal skill.

| Module | Useful role | Important bound |
| --- | --- | --- |
| Context-to-detail crop | Keep the real screen recognizable while making one control legible | Preserve meaning and disclose a stylized view where relevant |
| Tap/cursor indicator | Point to a verified action | Its hotspot must land on the actual target at the action frame |
| Focus mask/highlight | Guide attention to the relevant region | It must not hide evidence needed to understand the task |
| Shared-element transition | Carry a real card/map/result between views | Do not imply a transition or feature that the app does not have |
| Label/caption reveal | Explain a step without covering it | Verify Hebrew shaping, mixed numbers and reading time |
| Counter/proof card | Show a verified dated measurement | Preserve metric definition, period and source; no decorative invented values |
| Map/route animation | Explain a relationship or sequence | Use verified coordinates/order and mark illustrative motion |
| Brand sign-off | Make the ending recognizably ours | Optional; do not replace a useful payoff with a long logo hold |

Use a coherent motion vocabulary. A different effect in every scene rarely clarifies the story. If narration must be understood, its cadence can lead; if the film is music-led, align meaningful events to a measured beat map only when the track supports one. A beat never justifies removing text before it can be read.

### Choreograph the viewer's attention

Use this when motion explains an action, a relationship or a change of state.

1. Choose the first thing the viewer should see and the result they should remember. Keep an anchor such as the phone frame, map pin, card or presenter stable across the change.
2. Set the key poses: recognizable start, action or reveal, settled result. Decide where the eye goes in each pose. Stage cues in order: a brief lead-in or tap cue, the main movement, then a supporting accent only if it clarifies the result. Use easing that fits the move and hold the result long enough to read at phone size.
3. For a motion comparison, keep the input, crop, scale and labels matched. Change one behavior so the viewer can see its effect. Use a side-by-side when both states stay legible, or play the two states in sequence when real UI needs the full phone width.
4. Match the timing to its job. Keep familiar in-app reactions quick and reserve stronger flourishes for moments that benefit from emphasis. The duration of an app microinteraction, an editorial transition and a readable text hold are three different choices. Keep the actual app response and any editorial motion distinguishable.
5. Check a muted pass at phone size. The focal point, action and result should still read. Check the lead-in, action frame and settled state, especially when a Hebrew heading, a crop or a callout changes near the same time.

**Reference, visually reviewed 2026-11-13.** In Charles Liu's 31.5-second [UX and animation Reel](https://www.instagram.com/reel/DfphRvFBx54/), the presenter, running list and timer stay in place as a lower panel changes examples. Around 0:04, one card comes forward from a grid to demonstrate staging. Around 0:05, a single timeline shows key poses. Around 0:07, matched tracks compare constant speed and easing. Around 0:10, matching save buttons isolate secondary feedback. The panel disappears for the close, with the timer stopped around 0:27. The small list has weak contrast against the live background. Use the stable layout and isolated comparison as reference techniques. Give essential copy a stable, high-contrast background and set its hold by phone readability. The review sampled visual playback with audio muted. The creator's caption credits animation and UX sources, including [Raphael Salaja's UI Wiki](https://ui-wiki.org/) and [Emil Kowalski's guidance on purposeful motion and frequency of use](https://emilkowal.ski/ui/great-animations).

For a future Remotion implementation, official docs provide parameterized inputs, frame-based animation, timeline composition, transitions and caption tools. Keep runtime/package versions consistent and consult their current API rather than copying remembered snippets. Choosing Remotion does not remove the need for capture, proof, art direction or visual review.

## 6. Review in increasing cost

1. Review the storyboard against the intended outcome and proof. Catch an unsupported claim before animation work.
2. Produce the opening and a representative product scene as an early visual sample when the look is uncertain. This is a useful review checkpoint, not a new mandatory approval flow when the user has already authorized a complete film.
3. Inspect rendered frames: every tap, the longest line, settled main label, densest screen, last/first frame across a cut, end state and chosen cover. Typechecking alone cannot find these errors.
4. Inspect the full video at target phone size. Check the actual sequence, timing, readability and transitions. Inspect audio/captions with audio playback when available; do not claim to have heard it from stills or waveform data alone.
5. Verify technical output with media metadata: intended dimensions, frame rate, duration, orientation, playable codec and audio presence/absence. Confirm the export matches the accepted source/version.
6. Select a settled, clear poster/cover and inspect it independently. Use the platform's actual cover controls when publishing is authorized; do not promise that every player selects the same frame.

Report separately: what was visually inspected, what was measured, what was played back and what remains unverified. A contact sheet proves selected frames, not smooth motion or intelligible audio.

## 7. Revise without resetting the film

Classify a note as a copy/timing fix, visual reskin, scene replacement or story rebuild. Preserve locked wording, accepted framing and unaffected timing. Use a named variant or a focused commit for alternatives. A rejected version remains recoverable; it is not silently overwritten.

For a new scene direction, show two meaningfully different concepts when useful. Make the distinction concrete: task-first demo versus human situation followed by proof, for example, rather than three color variations. Keep an unresolved idea in the handoff instead of adding it to the accepted master unasked.

## 8. Measure the actual job

- Awareness: qualified reach/views and available viewing measures, with their exact definitions.
- Product understanding: relevant questions, documented user feedback and an appropriate comprehension check when feasible.
- Activation/action: a tracked destination or event and an attribution window; aggregate social engagement alone does not establish installs or feature use.
- Proof/community: quality of response and the intended community outcome; likes alone do not validate trust.

Compare similar topics, ages and distribution conditions. Keep one main creative variable in a practical experiment. Our first product-video tests are experiments, not predictions that motion will outperform carousels.

## Minimal production-skill handoff

A narrow skill can route a product-video request to this document without repeating the knowledge base:

1. Identify archetype, format, audience situation and intended outcome; brainstorm when the angle is still open.
2. Read current Git brand decisions and inspect the actual app flow.
3. List claims with proof and current assets; label missing or simulated states.
4. Produce the exact-copy scene contract and recommend a coherent look, motion/audio posture and optional CTA.
5. Select the smallest adequate production tool; reuse the existing one-shot Reel skill when the job is simply field footage with overlay text.
6. Render and review observable acceptance conditions; preserve approved decisions through revision.
7. Save documents in Git, files in Drive, then refresh the Notion mirror only under the Ela Maayan Hub.

The corresponding `el-hamaayan-product-video` procedure is provided by this harness.

## Sources and scope

Primary sources checked 2026-11-10:

- [Brag inspect method at pinned revision](https://github.com/latent-spaces/brag/blob/669ab9286aa28b6c3ee30e75f181ee74319d012a/skills/brag/references/step-1-inspect.md)
- [Brag plan method at pinned revision](https://github.com/latent-spaces/brag/blob/669ab9286aa28b6c3ee30e75f181ee74319d012a/skills/brag/references/step-2-plan.md)
- [SaaS product demo entry point at pinned revision](https://github.com/noamdorr/saas-product-demo-video/blob/c93c00ff44a65eea25ac1bb773a4565c68893ff9/skills/saas-product-demo-video/SKILL.md)
- [SaaS product demo self-check at pinned revision](https://github.com/noamdorr/saas-product-demo-video/blob/c93c00ff44a65eea25ac1bb773a4565c68893ff9/skills/saas-product-demo-video/references/self-check.md)
- [SaaS product demo iteration playbook at pinned revision](https://github.com/noamdorr/saas-product-demo-video/blob/c93c00ff44a65eea25ac1bb773a4565c68893ff9/skills/saas-product-demo-video/references/iteration-playbook.md)
- [Official Remotion skills](https://www.remotion.dev/docs/ai/skills), [parameterized rendering](https://www.remotion.dev/docs/parametrized-rendering), [animation](https://www.remotion.dev/docs/animating-properties), [Sequence](https://www.remotion.dev/docs/sequence), [transitions](https://www.remotion.dev/docs/transitions/) and [captions](https://www.remotion.dev/docs/captions/).

The workflow above is first-party synthesis adapted to Ela Maayan's Git/Notion/Drive model, authentic product proof, Hebrew and optional CTA policy. The [review](../research/video-harness-review.md) records the confirmed Tal the Traveler comparison, the separately credited Take One review room and earlier references. Use the [shared Reel editing and review workflow](reel-editing.md) for shot lists, supplied-timing captions, export frames and versioned feedback.
