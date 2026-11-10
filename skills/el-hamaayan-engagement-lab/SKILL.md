---
name: el-hamaayan-engagement-lab
description: Research what works for Ela Maayan / אל המעיין using its own Instagram posts and Reels, Metricool results, and matched Drive creative. Use when planning social content, evaluating successful posts, improving hooks or engagement, or updating the team's social playbook. Routes into Self Attention, visual design, social templates, and Reel production. Keeps measured findings separate from preferences and hypotheses.
---

# El Hamaayan Engagement Lab

Turn evidence from our own posts into a specific creative decision. Start with [our findings](references/our-findings.md) and [research and measurement](references/research-and-measurement.md). Use the bundled dated snapshot for historical evidence, and refresh connected data when the decision needs current performance.

## Working order

1. Identify the post's job: discovery, saveable trip planning, founder/community connection, product understanding, or a concrete action. Choose one primary outcome before judging popularity.
2. Retrieve our relevant posts and compare within format and topic. Match the actual creative where possible; captions are not spoken hooks or on-screen text.
3. Prepare a brief: audience situation, promise, proof, primary action, hook options, visual subject, reference family, and one variable worth testing.
4. Use `self-attention` for carousel sequence and the two entry points; use `el-hamaayan-visual-design` for composition and image-model briefs; use `el-hamaayan-social-templates` for actual Drive references. Use `el-hamaayan-reel` for Reel production, preserving its approved one-shot mode when requested.
5. Review the first impression and full payoff on a phone. Hand off the evidence and creative decisions together.

Resolve companion skills by frontmatter name in the available personal-skills directory, since their folders can change. Never pretend an unavailable skill was read or an existing integration was updated. Keep each skill's role narrow: this skill chooses the evidence and brief; the others own sequence, visual composition, template selection, and production.

## Hooks in our voice

- Be specific about the viewer's situation, place, number, effort, or benefit. Verify numbers and travel facts rather than inventing specificity.
- Include a relevant question as a hook option. Compare it with a direct benefit, an honest surprise, or a concrete moment. Do not turn “always start with a question” into a rule: our major founder post's caption starts with a statement, and a candidate founder cover starts with an introduction.
- Follow the owner's preference to avoid swearing at the start. Treat that as a creative preference, not an established Instagram profanity penalty. Do not add swearing later simply because it is allowed.
- Give the viewer something to recognize or anticipate immediately. Avoid generic “wait for it,” long logo intros, unexplained inside jokes, and inflated “crazy/secret/best ever” claims.
- Match the opening words to the visible action. A hand opening a hatch can be a visual hook without a question; do not force text that blocks the reveal.
- Give a useful or emotional payoff. Keep humor, real friends, imperfect real moments, and natural Hebrew when they serve the story.
- Choose one primary action that follows the value. A genuine comment-to-receive list is a distribution mechanism to measure, not proof of stronger interest than unprompted shares or saves. Count campaign comments separately when possible.
- Preserve approved wording. Use `el-hamaayan-brand-voice-wordmark` for brand voice; use the owner's supplied words as the controlling source.

## Evidence protocol

Read Metricool's metric catalog before querying; do not guess field IDs. For Instagram brand `ela.maayan`, the checked brand ID was `6887760` on 2026-11-10; verify identity before refreshing.

Retrieve publication timestamp, permalink/ID, type, caption, organic reach, views, likes, comments, saves, shares, and post follows where available. For Reels also request average watch time, duration if valid, view rate past three seconds, and skip rate. Record the date range and extraction date. Keep raw fields locally for inspection; save a compact reusable snapshot without expiring CDN links or account secrets.

- Deduplicate by publication ID. Mark repeated edits, collabs, boosts, trials, and reposts when known. Null paid fields mean unknown, not proof of zero paid distribution.
- Keep image, carousel, and Reel populations separate. Exclude Stories unless requested.
- Rank separately for reach, saves/reach, shares/reach, and follows/reach. State denominators. Do not substitute views for unique accounts or shares for DM sends.
- Compare similar publication age where possible. Lifetime snapshots of differently aged posts support hypotheses, not controlled uplift estimates.
- Inspect representative winners and ordinary/lower performers, including strong-looking posts that underperformed. Use several examples so one viral post does not set a universal style.
- Treat reach below 100 as unsuitable for the default creative baseline; retain those rows and explain the exclusion. This is a practical filter, not an Instagram rule. Check trial/draft/availability status before drawing conclusions from them.
- Do not infer per-slide completion or dwell from views. Do not compute Reel completion from average watch time without a valid matching duration; repeated viewing can also complicate the ratio.
- Label every rule as owner preference, observed pattern, general design principle, platform statement, or experiment. Reserve causal language for a design that supports it.

Use `python scripts/summarize_snapshot.py assets/performance-snapshot-2026-11-10.csv` for a reproducible baseline. Read the script before adapting it to a new schema.

## Evolve the playbook

Update the evidence after a requested review or when enough new comparable work changes a decision. Do not create recurring jobs just because this skill is reusable. Keep the prior dated snapshot, add a new one, and record which rule changed and why. Promote a test into a default only when several relevant posts support it; call mixed evidence mixed. Preserve the winning material while revising one meaningful variable at a time.

## Output

Return the recommended format and primary action, the few own-post examples supporting them, two or three hook directions, the visual/template handoff, and a small measurement plan. Keep unsupported ideas labeled as tests. Never promise virality, claim an AI model knows our audience without evidence, or present current performance from an old snapshot.
