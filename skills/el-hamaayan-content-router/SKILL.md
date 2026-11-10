---
name: el-hamaayan-content-router
description: Start and organize Ela Maayan / אל המעיין social content work in ChatGPT or coding agents. Use for new posts, carousels, infographics, commercials, Reels, app demos, feature videos, brand pieces, content brainstorming, or revisions. Identify format, reusable type, purpose, audience stage and intended outcome; route to the relevant skills and versioned knowledge; flag a possible new type without creating unnecessary skills.
---

# El Hamaayan Content Router

Start relevant content sessions with a proportionate routing pass. Preserve the user's actual goal and approved choices. A minor edit does not need a new strategy exercise.

## Load the current system

Use `Yotam4/video-editing-harness` as the canonical harness. With a checkout, read its `AGENTS.md`, `docs/README.md`, `registry/content-types.json` and relevant docs. In ChatGPT without a checkout, use connected GitHub tools to fetch the same files from the current default branch. Source: https://github.com/Yotam4/video-editing-harness

Read `docs/architecture/modular-content-system.md` for the boundaries and `docs/taxonomy/` for classification. Do not assume this installed entry skill contains the latest registry. If a source is inaccessible, state the limitation, use available context for a provisional brief, and do not invent its contents or claim a remote update.

## Understand and classify

1. Infer the audience, intended outcome, constraints, assets, approved wording and distribution from the request and existing record. Ask only for information that materially changes the work; continue independent work when possible.
2. Separate format and placement from recipe/subtype, purpose, audience awareness/funnel stage, CTA, campaign and asset mode. An infographic is a treatment and a commercial is a purpose, not necessarily a separate media format. A Reel need not be a sales funnel. Keep stage unknown or not applicable when appropriate.
3. Match the registry by required inputs, proof, narrative and outputs. If the repository's classifier is available, use it as an explainable lexical aid, then apply judgment. Never describe its scores as semantic certainty or predicted engagement.
4. If recipes overlap, explain the useful distinction. If none fits, propose a candidate recipe with examples and required inputs in the content record. Reuse generic modules meanwhile. Do not invent a permanent type or new skill for one ambiguous request; promote a candidate only when a repeatable structural difference is established and the owner accepts it.

## Choose the work path

- New or unclear concept: use `el-hamaayan-social-brainstorm` to explore genuinely different approaches and converge on a brief.
- Own-post evidence: use `el-hamaayan-engagement-lab`; distinguish findings, preferences and experiments.
- Carousel: combine `self-attention`, `el-hamaayan-visual-design` and `el-hamaayan-social-templates` with the selected recipe.
- Natural footage Reel: use `el-hamaayan-reel` and preserve approved native framing/copy.
- App demo, feature video, proof/brag piece or motion explainer: use `el-hamaayan-product-video` plus the production docs. Make real app proof legible; do not replace it with invented UI.
- Brand/logo: use the existing brand voice, logo variation and archive skills.

Resolve companions by frontmatter name. If a companion is unavailable, use the relevant documented workflow and say what was actually loaded. Do not install third-party dependencies or change publishing access merely because a recipe mentions them.

## Produce and preserve

Return the inferred outcome, proposed classification, relevant concept/production choices, important missing proof and next step in a natural response. CTA is optional; do not add an install pitch to a complete joke, story or scenic piece. Funnel recommendations are hypotheses about audience needs, not universal calls to action.

Keep knowledge and text records in Git under `docs/content/<format>/<recipe-or-candidate>/<slug>/`; use stable IDs if reclassification changes the folder. Store media/exports in Drive and record their source IDs/versions. Mirror committed knowledge only beneath the existing Ela Maayan Notion Hub, following the repository workflow. Do not claim background sync or saving when tools did not perform it.

For every completed session, preserve the classification and reasons, brief, approved copy, evidence, feedback, current version, checks, unresolved questions and next step. Reuse the existing record for revisions. Publish or schedule only when explicitly requested.
