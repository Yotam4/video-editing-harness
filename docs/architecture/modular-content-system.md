# Modular content system

## What starts a session

`el-hamaayan-content-router` is the ChatGPT/personal-skill entry point. Repository agents also start from root AGENTS.md. Both load the current Git knowledge and type registry; neither treats an old copied skill as the full knowledge base. Personal skill discovery is contextual rather than a guaranteed global startup hook. An old chat may have a cached skill catalog; explicitly invoke the router when it is absent from that chat.

The registry and docs live in this Git repository. Notion is the human-readable mirror only under the Ela Maayan Hub. Media stays in Drive, referenced by stable source IDs and version labels. No background classifier, bidirectional sync or posting automation is implied.

## Compose independent axes

| Axis | Examples | Why separate it |
| --- | --- | --- |
| Format | carousel, short video, single image, story sequence | Defines the physical artifact |
| Placement | feed, Reels, Stories, website, ad placement | Determines delivery and safe-area checks |
| Recipe/subtype | place guide, comparison, founder story, feature demo | Defines reusable structure, proof and inputs |
| Treatment | infographic, real footage, screen recording, motion graphics | Defines visual language without dictating the purpose |
| Purpose | entertain, inform, connect, demonstrate, announce, convert | Defines the viewer's job and the intended value |
| Audience stage | discovery, consideration, action, existing user, unknown, not applicable | Helps choose context and proof when useful |
| Outcome | recognition, understanding, saves, follows, qualified action | Defines a useful measure without forcing a sale |
| CTA | optional request, or none | Follows value and audience readiness |
| Campaign and assets | campaign ID, actual screenshots, footage, source claims | Adds context and production constraints |

A feature walkthrough can be a carousel or video. A commercial can contain animation or actual footage. A funny Reel can be complete without a funnel stage or CTA. These are composition choices, not separate independent skill copies.

## Layers and ownership

| Layer | Location | Holds |
| --- | --- | --- |
| Evidence and knowledge | `docs/research/`, `docs/analysis/`, `docs/knowledge/` | Sources, dates, limitations and findings |
| Strategy | `docs/strategy/` | Audience needs, funnel hypotheses, brainstorming and measurement choices |
| Registry and recipes | `registry/`, `docs/taxonomy/` | Reusable types, inputs, proof, checks and classification rules |
| Thin procedures | `skills/` | What to do, what to load, checks and handoffs |
| Production | `docs/production/` and relevant scripts | Asset preparation, storyboards, capture, motion and export |
| Item state | `docs/content/<format>/<recipe-or-candidate>/<slug>/` | Brief, classification, copy, decisions, versions, feedback and handoff |
| Recommendations | Inside the brief, with evidence labels | Optional tactics tied to a goal; never disguised as universal rules |

Keep a detailed claim or theory in docs and a short operational instruction in a skill. A type deserves a registry entry when its structure/proof/output differs meaningfully. A separate skill is warranted when it owns a repeatable procedure or specialized tool workflow; a new topic or color scheme is insufficient.

## Creation and revision paths

1. Load the record and infer the intended outcome. An approved edit follows a short revision path.
2. Classify format and recipe, keeping independent labels. Use `scripts/classify_content.py` as a deterministic lexical aid, not semantic authority.
3. For a new or unclear concept, brainstorm meaningfully different approaches and converge on a brief. Reuse known preferences and ask only consequential questions.
4. Load the matching recipe, evidence and production procedures. State gaps in facts or available assets.
5. Produce and inspect the actual artifact for readability, RTL, proof, pacing and payoff.
6. Save source/output references and text state, commit, then refresh the mapped Notion mirror.
7. After publication, record available outcomes and limits at comparable ages. Promote supported learning into docs and, when justified, procedure defaults.

## New-type lifecycle

Use `matched` when the registered structure fits; `needs_choice` when multiple recipes or explicit formats conflict; `unclassified` for weak evidence or an unfamiliar structure. Keep candidate types in the content record with proposed name, parent format, examples, unique requirements and why existing recipes fall short. Do not silently expand the registry or install skills from a single heuristic result.

An accepted candidate receives a stable recipe ID and registry entry, docs, input/proof/output checks and examples. Preserve the original classification history and item ID if a record moves. Reuse existing skill modules unless the new procedure really differs.

## Evidence discipline

Use platform facts, observed account patterns, practitioner recommendations, design principles, owner preferences and hypotheses as explicit labels. Neither lexical scores nor funnel labels predict reach. General Instagram advice must be checked against current primary sources and the actual account interface. Our own creative evidence must distinguish exact export matches from filename/caption hypotheses.
