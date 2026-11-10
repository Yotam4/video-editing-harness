# Content taxonomy and routing

This taxonomy is a planning system, not a claim about Instagram's ranking model. Its rules are our synthesis, checked on 2026-11-10. Read [audience stages](audience-stages.md) before using TOFU/MOFU/BOFU shorthand and [type lifecycle](type-lifecycle.md) before adding a new recipe or skill.

The machine-readable source is [content-types.json](../../registry/content-types.json), validated against [its schema](../../registry/content-types.schema.json). It starts with 17 recipes. `starter` means useful to try, not proven to outperform another format for Ela Maayan.

## Keep the axes separate

| Axis | Question | Example |
| --- | --- | --- |
| Production format | What are we making? | Carousel, short video, single image, Story sequence |
| Placement | Where will it appear? | Feed, Reels, Stories, several placements, undecided |
| Recipe/type | Which repeatable narrative structure fits? | Place guide, feature walkthrough, app screen demo |
| Purpose | What should the audience receive? | Enjoyment, useful planning, understanding, connection, action |
| Audience stage | What context or readiness are we assuming? | Discovery, evaluation, action, existing user, not applicable, unknown |
| CTA | Is a requested action useful here? | None, save, open a feature, contact; undecided is also allowed |
| Campaign | What distribution/commercial context applies? | Organic, paid, partner, mixed, undecided |
| Asset mode | What evidence/material carries the piece? | Real photo, real footage, real UI, data graphic, motion, mixed |

A Reel is a short-video production with Reels placement. An infographic is an explanatory treatment that may use a carousel, one image or motion. A commercial is promotional intent/campaign context; it does not specify the production format. A post can be promotional and educational at the same time, but the brief should choose the intended outcome used to judge this piece.

For example, “show public transport navigation” can become an educational carousel for existing users, a short discovery video for unfamiliar viewers, or a direct feature demo for people ready to try it. The feature is shared; the entry, proof, context and next step differ. These are variants unless they require a materially different reusable structure.

## Starter recipes

| ID | Structure | Possible formats |
| --- | --- | --- |
| `place-guide` | Place/context → experience → practical access → limits | Carousel, short video, image |
| `route-collection` | Selection promise → criteria → distinct choices → useful comparison | Carousel, short video |
| `infographic-explainer` | Question/model → explanation → worked example → limits | Carousel, image, short video |
| `founder-story` | Concrete moment → tension/change → human payoff | Carousel, short video, Stories |
| `community-story` | Person → contribution → experience → recognition | Carousel, short video, Stories |
| `feature-walkthrough` | User job → entry point → real steps → visible result | Carousel, short video |
| `comparison` | Decision question → fair criteria → evidence → situation fit | Carousel, short video, image |
| `launch-announcement` | Relevant new thing → benefit → proof → availability → optional step | Any supported format |
| `natural-one-shot` | Continuous real moment → movement/reveal → one overlay idea | Short video |
| `field-story` | Scene → journey/problem → specific moments → earned payoff | Short video, Stories |
| `app-screen-demo` | Task → actual input/action → screen response → result | Short video |
| `feature-benefit-video` | Recognizable need → benefit → real demo → outcome | Short video |
| `proof-results-video` | Specific claim → evidence → timeframe/context → meaning | Short video, carousel |
| `motion-explainer` | Concept → visual relationship → progressive reveal → example | Short video |
| `behind-the-scenes` | Real work moment → specific detail → people/process → payoff | Carousel, short video, Stories |
| `humor-observation` | Recognition → setup → turn → payoff | Any supported format |
| `testimonial-case-study` | Person/context → need → experience → verified outcome → limits | Carousel, short video |

The registry adds required inputs, proof requirements, quality checks, examples and applicable skills to each recipe. It does not make every possible variant its own skill.

## Start every content request

1. Read the user’s brief and any existing item/handoff. Preserve approved words and established choices before brainstorming.
2. Identify the format, intended outcome, audience context, actual proof/assets and material constraints. Keep unknowns visible. Ask only the question whose answer changes the next decision.
3. Propose a matching recipe and, when useful, one meaningfully different alternative. Explain what changes in the entry, proof and payoff. Do not offer three cosmetic rewrites as three strategies.
4. Select the few skills that own the actual work. A place carousel needs the carousel sequence/design procedures; a real app demo needs authentic product capture and video production. A supporting infographic does not necessarily change the primary recipe.
5. Save the chosen axes and rationale with the Git content record. Use the stage table to adapt the treatment; do not infer funnel readiness from the format.
6. When the structure does not fit, use the candidate process. Unfamiliar wording alone is not a new type.

## Folder and record convention

Use `docs/content/<format>/<recipe-id-or-candidate>/<slug>/`. For example:

- `docs/content/carousel/feature-walkthrough/public-transport/`
- `docs/content/short_video/app-screen-demo/trip-builder/`
- `docs/content/short_video/humor-observation/packing-too-much/`

Keep the slug stable across revisions. Store the current brief/copy, decisions, asset IDs and handoff there. A campaign spanning multiple formats gets sibling records with a shared campaign ID; do not hide the format distinction in one ambiguous folder. If a later accepted type changes the canonical path, record the move and old path rather than duplicating the content history.

Minimal record labels:

```json
{
  "format": "carousel",
  "placement": "feed",
  "type_id": "feature-walkthrough",
  "purpose": "product_understanding",
  "audience_stage": "existing_user",
  "cta": "open_feature",
  "campaign": "organic",
  "asset_mode": "real_ui",
  "campaign_id": null,
  "source_asset_ids": [],
  "classification_status": "human_confirmed"
}
```

These are metadata, not a new database or an installed automatic folder creator. Filled content and knowledge live in Git; mirror them in the existing Notion tree under the Ela Maayan Hub. Media stays in Drive.

## Optional deterministic helper

```bash
python scripts/classify_content.py "A carousel of three springs for the weekend"
python scripts/classify_content.py "A funny moment with friends as a reel" --purpose entertainment --stage none --no-cta
python scripts/classify_content.py "An app demo" --format reel --stage bofu --purpose activation
python scripts/classify_content.py "Make the highlight orange" --revision --existing-type feature-walkthrough --format carousel
python scripts/check_content_registry.py --smoke
```

The helper uses disclosed phrase matches and weights. It is **not** semantic AI, a confidence estimate, a reach prediction or proof that the necessary assets exist. Its job is to make common routing repeatable and expose ambiguity; the conversational agent must interpret the brief and confirm the decision.

| Status | Meaning | Next step |
| --- | --- | --- |
| `matched` | A unique lexical lead reached the assistance threshold | Check the proposed recipe against the actual brief, proof and assets |
| `needs_choice` | The brief names several formats or recipe evidence is close | Resolve the main deliverable/structure; consider separate variants |
| `unclassified` | Signals are absent or too weak | Clarify the outcome/structure, then assess whether a candidate type is needed |

`format_proposal_only` never silently settles an unspecified format. `suggested_stages_only` is a menu of possible applications; actual `audience_stage` stays `unknown` unless explicitly supplied. `cta: null` means undecided; `cta: "none"` is a deliberate, valid choice. `inputs_to_confirm` lists facts/assets not explicitly marked verified with `--known-input`; a phrase match is not verification.

For a small approved revision, pass `--revision --existing-type <stored-id>` after reading the existing record. It returns the stored recipe with `classification_basis: "existing_record"`; it does not classify “make it orange” as a new concept. Without the stored recipe, revision mode asks for its record. The actual existing format, outcome and approved copy still come from that record.

Simple explicit absence such as “no current screen recording” is excluded from positive keyword evidence and disclosed in `excluded_signals`. This is a narrow lexical safeguard, not complete negation or asset understanding. Always inspect the actual materials before planning production.

The helper does not create files, types, skills, schedules or publications. New type registration is a separate editorial decision.
