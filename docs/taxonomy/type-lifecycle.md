# When an unfamiliar brief becomes a type

This is a repository design decision and editorial workflow, not a platform requirement.

## Reuse before multiplying modules

A recipe packages a repeatable structure, required inputs, proof, output contract and checks. A skill owns the procedure used to perform a job. A document stores explanations, evidence and recommendations. A content record stores one creative decision and its revisions. Keep these separate.

| Observation | Usually change |
| --- | --- |
| Same narrative, another topic/place | Content record and asset references |
| Same structure, another audience stage | Stage/purpose treatment in the brief |
| Same concept, carousel and Reel variants | Separate format records with a shared campaign ID |
| Same structure, a distinctive visual treatment | Template or asset references |
| Existing recipe, an optional infographic section | Supporting treatment, not necessarily a new primary type |
| New repeatable sequence and distinct proof/output needs | Candidate recipe |
| Reusable multi-step procedure that existing skills do not cover | Candidate skill, after the procedural gap is demonstrated |
| A new empirical observation or a disputed tactic | Evidence/recommendation document, not an unconditional skill rule |

## Candidate path

1. Capture the unfamiliar brief in `docs/content/<format>/candidate/<slug>/`. Record the intended outcome and why existing recipes may be insufficient. The path is a convention; the helper does not create it.
2. Check vocabulary and missing context first. The lexical classifier may miss a familiar concept described in new words. A weak score is not proof of a new type.
3. Compare the nearest recipe. State the substantive gap: different production inputs, narrative sequence, proof burden, output or review checks. A new color, location or marketing label is not sufficient.
4. Prototype the structure on the current item. Record changes, approval, production issues and the resulting artifact’s Drive reference.
5. When the owner accepts the reusable pattern, add a stable ID and `experimental` recipe entry. Validate the registry and link this rationale. One real prototype can justify an experiment; it does not establish performance superiority.
6. When multiple relevant uses demonstrate the structure’s usefulness, promote it to `established` with evidence. There is no universal minimum sample or automatic promotion score.
7. Create or adapt a narrow skill only if a distinct repeatable procedure remains. Reuse generic brainstorming, evidence, attention, composition and production skills rather than copying them into every subtype.

The initial seeded entries use `starter`: they are researched and recognizable content structures, but not all have been produced or validated by Ela Maayan. `retired` retains the historical ID and rationale so earlier records remain readable. Do not silently reuse a retired ID for a different meaning.

## Registry change checklist

- Give the pattern one stable ID and a concise structural name.
- Keep allowed formats distinct from placement, purpose, funnel stage and CTA.
- Define inputs, proof, editable output and relevant quality checks.
- Include examples without treating them as current product specifications.
- Link existing skills; do not create dangling or duplicate procedures.
- Keep `cta_policy` optional; a stage suggestion is never a compulsory action.
- Add lexical signals only to improve transparent assistance, without presenting their scores as probabilities.
- Run `python scripts/check_content_registry.py --smoke` and inspect a real new brief.
- Commit the taxonomy, evidence/rationale and related routing changes together; refresh the existing Notion mirror under the Ela Maayan Hub.

## What belongs where

| Layer | Contents | Avoid |
| --- | --- | --- |
| Docs | Research, source limitations, audience-stage reasoning, examples, experiment outcomes | Turning every suggestion into a universal command |
| Registry | Stable recipe contracts and routing metadata | Duplicated full skills, private asset bytes, invented performance grades |
| Skills | Narrow repeatable procedures and decision gates | A separate copy of the entire workflow per subtype |
| Content records | The actual brief, selected axes, copy, revisions and outcome | Hiding the sole record in a chat or Notion mirror |
| Recommendations | Conditional choices with rationale and uncertainty | Implying a platform ranking guarantee |
| External asset store | Real photos, video, design masters, raw datasets and exports | Committing those files to Git |

Unknowns remain visible until resolved. Classification can assist brainstorming; it must not replace understanding the user’s intended outcome.
