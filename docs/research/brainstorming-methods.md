# Brainstorming methods and adaptation record

Checked: 2026-11-10. This is a first-party synthesis for the social harness, not a copy of an engineering workflow and not evidence that any brainstorming method increases Instagram reach.

## Sources inspected

| Source | Immutable or original reference | What was inspected | Status and boundary |
| --- | --- | --- | --- |
| Maayan's existing brainstorming fork | [SKILL.md at 27b7f083](https://github.com/Yotam4/maayan-trail-planner/blob/27b7f083222aab6cfb6f0a90a45bf727abda996b/.claude/skills/brainstorming/SKILL.md) | Full skill; contextual exploration, alternatives, design review, local ambiguity safeguards | Existing first-party fork of Superpowers; engineering-specific gates do not automatically apply to this social repository |
| Maayan's fork provenance | [SUPERPOWERS-SKILLS-NOTICE.md](https://github.com/Yotam4/maayan-trail-planner/blob/27b7f083222aab6cfb6f0a90a45bf727abda996b/.claude/skills/SUPERPOWERS-SKILLS-NOTICE.md) and [retained license](https://github.com/Yotam4/maayan-trail-planner/blob/27b7f083222aab6cfb6f0a90a45bf727abda996b/.claude/skills/SUPERPOWERS-SKILLS-LICENSE.txt) | Full provenance notice and license | Records upstream snapshot 3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9, vendored 2026-07-24; later owner-authorized edits make it a fork, not a current upstream mirror |
| Maayan's context architecture | [CLAUDE.md at 27b7f083](https://github.com/Yotam4/maayan-trail-planner/blob/27b7f083222aab6cfb6f0a90a45bf727abda996b/CLAUDE.md) | Agent map and context layers | Procedural skills are separate from canonical docs; Notion is a product/owner mirror rather than agent source of truth |
| Current Superpowers brainstorming | [SKILL.md at 22f0b46](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) and [MIT license](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/LICENSE) | Full skill and license pinned to the resolved main commit | MIT, copyright 2025 Jesse Vincent. Context before questions, scale effort to the request, expose meaningful choices; its implementation approval and software planning gates are not adopted here |
| Design Council | [Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/) and [Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) | Original explanation of exploration, definition, alternative development and small-scale testing | Design-process framework, not social-platform evidence. The diagram is CC BY 4.0; no diagram is copied here |
| IDEO.org Design Kit | [Brainstorm Rules](https://www.designkit.org/methods/brainstorm-rules.html), [How Might We](https://www.designkit.org/methods/how-might-we.html), [Gut Check](https://www.designkit.org/methods/gut-check.html) | Original practitioner method descriptions | Creative-facilitation advice. Separate generating alternatives from checking feasibility; a focused challenge should still permit different solutions |

Do not infer that the observed main commit remains current indefinitely. Recheck before an upstream update, rather than automatically replacing our adapted procedures.

## Adopt, adapt, omit

| Idea | Decision for social work | Reason |
| --- | --- | --- |
| Read project context before questioning | Adopt | Existing briefs, approved copy, current brand guidance and asset references often already answer the question |
| Understand the intended result before choosing execution | Adopt | A beautiful place post, useful trip list, joke, product lesson and acquisition ad have different jobs |
| Generate real alternatives, then compare | Adopt | Three rewordings of the same hook are not three creative concepts |
| Identify which constraint each option assumes | Adapt | Separate truly fixed facts, brand boundaries and available footage from optional visual choices |
| Resolve conflicting sources explicitly | Adapt | Live instructions, an old content-bank record and dictated wording can conflict; preserve the latest explicit correction and flag unresolved conflicts |
| Repeat a selected option by its meaning | Adopt | Prevents confusion when the user answers with a number, a letter or a reason |
| Document a reusable brief and remaining unknowns | Adopt | The next session should continue from the actual decision, not reconstruct it from chat |
| Explore first, narrow later, test cheaply | Adapt | A hook board, slide map, storyboard or rough animatic can resolve uncertainty before full rendering |
| One open question on every message | Omit as a universal rule | Ask only when a missing answer materially changes the work; do not re-ask known context or prolong a clear revision |
| Approval of a formal design before every implementation | Omit as a social default | User authorization and the current creative brief govern; a reversible draft need not await a new software-style approval gate |
| Mandatory writing-plans invocation or local visual server | Omit | Content production uses the relevant creative skills and available preview mechanism; it does not require a software delivery chain |
| A funnel stage, CTA or sales claim on every post | Omit | Audience connection, entertainment and expression can be complete outcomes without a transactional action |

## Layer boundaries

**Docs own knowledge:** frameworks, evidence, source limitations, type definitions, examples, accepted decisions and experiment outcomes. Their role is to explain why a choice may work and when it does not apply.

**Skills own repeatable behavior:** read the right context, size the session, identify the intended result, compare concepts, route to a type, record the brief and hand off to production. Keep them short and link to owning docs rather than copying the research.

**Recommendations belong to a specific item:** which concept to make, whether to include a CTA, what to show first, which asset to use and what to measure. Preserve their rationale, but do not promote them into permanent rules after a single post.

**Registry owns supported type metadata:** format, subtype, intent, inputs, proof, output shape and skill routing. A plausible new idea is a type candidate until its reusable difference is clear. A different location, language, funnel stage or campaign does not by itself create a new type.

## Evaluation scenarios

Use these as forward-test situations, not predicted performance tests:

- An approved carousel needs the Moovit option highlighted. The workflow should apply the correction and preserve the rest, rather than initiate a full brainstorm.
- The request is “announce the forum.” The workflow should find the current feature behavior and available real screenshots, then compare a community-origin story, an action walkthrough and a real use-case demonstration.
- The brief is a funny clip of friends. The workflow should allow entertainment as the intended result and no CTA; it should not turn the joke into an app commercial.
- The user wants a “brag video.” The workflow should ask what can actually be demonstrated, distinguish verified outcomes from promotional adjectives, and route to a proof-led video only when proof exists.
- A requested subtype has no registry match. The workflow should describe the reusable production difference and record a candidate, rather than silently manufacture a permanent skill.

## Reuse and attribution

The documents in this change contain newly written synthesis and no copied skill implementation or server code. They credit the inspected Maayan fork, obra/Superpowers and original design-method sources above. If a later change vendors a substantial portion of Superpowers, retain its complete MIT copyright and permission notice with that material, record the upstream commit, and distinguish our modifications. A source URL alone is not a replacement for the license notice required when distributing copied material.
