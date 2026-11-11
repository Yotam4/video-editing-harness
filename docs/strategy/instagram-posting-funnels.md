# Instagram posting funnels

Reviewed 2026-11-11. Use this playbook when choosing how an organic Reel, carousel, or Story should earn attention and deliver value. Start with the viewer's situation, the promise, and the outcome. Add an action when it is useful to that viewer.

[Reels](#reels) · [Carousels](#carousels) · [Stories](#stories) · [Feature example](#one-feature-across-three-formats)

## From the source diagrams to the brief

The three diagrams supplied from @swastik.nandakumar suggest a useful question at each step: what can the viewer do next, and what in the post makes that worthwhile? The diagrams simplify distribution into deterministic branches. Meta describes personalized ranking systems that use combinations of predictions. Use the paths below to plan and diagnose creative, with the surface and audience stated in the brief. [Creator reference and claim checks](../research/social-evidence-ledger.json) · [Meta system cards overview](https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/)

| Format | Viewer path | Creative priority | Measures to check when exposed |
| --- | --- | --- | --- |
| Reel | See the opening → keep watching → get the payoff → replay, share, or follow | Make the first visible action relevant and resolve the promise | Early view/skip rate, average watch time, shares per reach, follows |
| Carousel | See an entry slide → get the first useful point → read or swipe → save or send | Give slides 1 and 2 independent context and build useful progression | Reach mix, saves per reach, shares per reach, follows |
| Story | See it in the tray → open → continue, respond, or leave | Give existing viewers timely context and a reason to return or respond | Frame reach, replies, sticker or link actions, navigation events |

Discovery, consideration, action and existing-user follow-through are audience stages. A format can serve any of them. The paths describe choices viewers can make, and an entertaining or complete piece can end at its payoff.

## Reels

| Beat | What to build | How to diagnose |
| --- | --- | --- |
| First impression | Start with a visible action, a specific result, or a short premise that gives the shot meaning. Keep the first frame readable on a phone. | If early viewing is weaker on comparable posts, compare whether the first frame shows the subject and promise. |
| Continue | Move from premise to proof. Cut repeated setup and keep the steps required to understand the scene. | If people start watching but average watch time is weak, inspect the pacing, legibility, and time to the first useful beat. |
| Payoff | Deliver the route, result, human moment, or answer promised. Make the ending clear enough to remember or send. | If viewing holds but few people take the intended action, inspect the relevance and usability of the payoff. |
| Wider discovery | Give a stranger the context to understand the Reel and a specific reason someone might share it. | Separate follower and non-follower reach where available. Check recommendation eligibility before attributing a reach change to the edit. |

Meta identifies skip rate as feedback relevant to distribution. Three-second viewing is a useful diagnostic when the account exposes it, with no published cutoff that determines when distribution stops. Meta's 2024 rollout described showing eligible recommended content to a small likely-interested audience and expanding distribution based on performance. Scope that description to its dated rollout. Trial Reels are a separate publishing option designed to reach non-followers first. [Edits and skip rate](https://about.fb.com/news/2025/04/introducing-edits-streamlined-video-creation-app/) · [2024 recommendation rollout](https://about.fb.com/br/news/2024/04/ajudando-o-criador-de-conteudo-a-encontrar-novos-publicos/) · [Trial Reels](https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/)

Compare similar durations, publication ages and distribution modes. Average watch time, completion and replays measure different things. Capture the provider's definition for each metric. Compare Trial Reels separately when audience and distribution differ. Use the existing Reel procedure for field footage and the product-video procedure for app interaction or animation. [Product-video playbook](../production/product-video-playbook.md)

## Carousels

| Beat | What to build | How to diagnose |
| --- | --- | --- |
| Slide 1 | Name the concrete subject and make the value recognizable at a glance. | Read the cover at feed size. Check whether the subject and promise make sense without the caption. |
| Slide 2 | Give an independent entry and advance the story with a useful detail, a real example, or the first proof. | Review slide 2 alone and then read 1 → 2 → 3. Check that the two openings earn their space. |
| Middle | Make each swipe add a place, decision, step, or proof point. Keep real screens and map details readable. | Find repetitive setup, dense labels, and slides that do not move the viewer forward. |
| Payoff | Deliver something that a viewer could use, remember, or send to a particular person. | Compare saves and shares per reach by topic, format, and post age. Compare the intended outcome first. |

Use slide 2 as a second creative entry even when no resurfacing data is available. Mosseri's dated guidance says Instagram can resurface an unswiped carousel on the second item. The harness records that guidance and its source-access limits. Feed includes recommendations, so a followers-first launch or a permanent stop after a scroll-past cannot be inferred from the creator diagram. Aggregate post metrics also cannot identify which slide lost viewers. [Carousel attention research](../knowledge/carousel-attention.md) · [Meta on recommendation systems](https://ai.meta.com/blog/ai-unconnected-content-recommendations-facebook-instagram/)

## Stories

| Beat | What to build | How to diagnose |
| --- | --- | --- |
| Open | Name the timely reason to look on the first frame. Use a real update, question, or moment people can recognize. | Use first-frame reach as observed exposure. Calculate an open rate only if the provider supplies an eligible tray-exposure denominator. |
| Continue | Give each frame one job. Put the first useful detail early and make each follow-up easy to understand. | Compare frame reach within similar sequences and read navigation labels carefully. A forward tap can reflect fast reading or skipping. |
| Respond | Invite a reply, poll vote, sticker action, or link tap when it serves a specific purpose. | Count actions with the provider's definitions. Compare against reach on the frame that carried the action if that denominator is available. |
| Follow through | Close the question, report what happened, or point viewers to the resource you promised. | Review whether the sequence produced the intended response and whether the continuation actually worked. |

Instagram's 2023 explanation describes viewing history, past engagement, and closeness as examples of Stories signals. It describes predictions about opening, replying, and moving on. The public explanation leaves exact signal weights and any guaranteed effect of a sticker tap or skip unspecified. [Instagram's published explanation, republished on WebWire](https://www.webwire.com/ViewPressRel.asp?aId=305828)

Where timing and audience are comparable, last-frame reach ÷ first-frame reach can describe the sequence's exposure pattern. It cannot establish individual completion without linked viewer data.

## One feature across three formats

For a public-transport discovery feature, choose the pieces that serve the campaign's actual goals.

| Piece | Example viewer experience | Outcome to observe |
| --- | --- | --- |
| Reel | Open with the familiar problem of planning a hike without a car. Show one verified action and the real result in the app. | Early viewing and watch time, then shares or tracked interest |
| Carousel | Lead with the trip-planning problem. Let slide 2 name the feature and show real proof. Give the viewer a concrete example they can save. | Saves or shares per reach, with tracked action if available |
| Stories | Answer a real question about the feature, show one short app interaction, and follow up on replies. | Replies, relevant sticker or link actions, and unresolved questions |

Verify the current feature and any route details before producing this example. One piece can be enough. Use a linked next step when the viewer needs it and the destination works.

## How the harness uses it

1. The content router identifies placement and audience outcome, then loads the relevant section when planning or reviewing Instagram distribution.
2. The brief records **viewer situation, opening, payoff, optional next action, primary measure, and one variable to test**.
3. The relevant procedure handles production and review. Self Attention owns carousel sequencing, the Reel or product-video procedure owns video execution, and the engagement lab compares the results.
4. Record the metric, denominator, observation age, distribution mode, and relevant confounders. Start with same-age comparisons when feasible and document what the data can answer. Use repeat observations before promoting a tactic to a default. [Experiment log](../analysis/ela-maayan-experiments.md)
