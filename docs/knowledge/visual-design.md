<!-- Migrated from https://app.notion.com/p/414c4747654f8102844aea35c3c78cf8?pvs=204; source last edited 2026-11-10T19:57:27.812Z. Git is canonical from this migration onward; the source page becomes its mirror. -->

צילום מצב של חומרי הייחוס שהיו ארוזים עם ה־Skill בעת ההקמה ב־2026-11-10. אלה חומרי ידע היסטוריים; יש לקרוא את המקור העדכני לפני שימוש במידע שתלוי בזמן. לא הועתקו לכאן תמונות או סרטונים.

## design-evidence.md

# Design evidence and source status

Checked 2026-11-10. Use these sources to explain principles, not to claim isolated Instagram engagement effects.

- [NN/g: Visual Hierarchy in UX](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/), 2021-01-17: explains scale, contrast, grouping, and intended reading order. Relative contrast matters in context. Apply as a general design principle, not as an organic Instagram experiment or universal RTL eye path.
- [W3C: Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): provides text contrast thresholds and warns that display size and rendering matter. Use as a readability reference, preserving its definitions rather than translating export pixels directly into legal claims.
- [OpenAI image prompting](https://developers.openai.com/api/docs/guides/image-prompting): recommends concrete briefs, defined reference roles, exact text, placement, and explicit preservation constraints. This is image-production guidance, not evidence of social performance.
- [OpenAI image generation](https://developers.openai.com/api/docs/guides/image-generation), including its limitations section: identifies text clarity/placement, composition, and recurring brand consistency as remaining limitations. Model capability does not remove output review.
- Meta [Reels placement guide](https://www.facebook.com/business/ads-guide/update/video/instagram-reels/outcome-engagement) and [safe-zone help](https://www.facebook.com/business/help/980593475366490) were attempted but redirected to login/blocking. Third-party summaries cite ad-specific margins. Do not present those numbers as directly verified current organic safe zones.

Own-source authority:

- [Marketing Brand System v1](https://docs.google.com/document/d/16e_s97lLWQs7m_ORepH_czHlNRjnh4wKfa-14lV6q_w/edit): Assistant/Inter, identity and semantic colors, authentic photos/UI, deliberate ratio variants, versioned changes.
- [Template Library](https://docs.google.com/document/d/1UkajDYwHo4yGxn9FN2IOVGiTLyAeNePRFsRuLJ_fU8s/edit): distinct founder, place, product, community, announcement, and Reel-cover families.
- [Product/UI guide](https://docs.google.com/document/d/1lpUnrOMDevFgAiZeQrZs3Gx-GvWJJwuaFIMJajjlom8/edit): authentic screens, one feature, readable crops, optional frames.
- [Photography guide](https://docs.google.com/document/d/1WFqfLihpE8iwlG8HGmggywrJuQ8hOatXHZCye_zhlYw/edit): real lived-in photography, people/place/product priority by story type.
- [September 29 story design notes](https://drive.google.com/file/d/1kVv-r3iYqdD9-eNI8fwLd6-czbzMFKal/view): a specific approved historical family using Heebo and charcoal/orange. Do not silently replace it using the more general September 22 guide.

Use the template registry for exact visual reference IDs and the engagement lab for results. Separate observed design conventions, owner preferences, general principles, and experiments whenever giving a reason for a change.

## image-model-briefs.md

# ChatGPT Images 2.5: reference-based briefs

Checked 2026-11-10. Official OpenAI image documentation includes GPT Image 2.5 Flare and Sunburst. Preserve the owner's requested 2.5 model when an explicit selector exists. The built-in tool in this session has no model selector: do not claim it ran a specific version, silently substitute a named model, or require an API key for the built-in workflow. Recheck model availability for future API work.

Use the image model as a design collaborator for raster layout proposals, permitted edits, and original illustrative/backplate work. It does not have automatic access to our Drive, results, or brand references, and it cannot prove which placement will maximize engagement. Supply relevant images and an explicit brief; inspect the result.

## Required brief fields

- Purpose, audience situation, and one promised payoff.
- Canvas/ratio and the actual placement to preview.
- Reference roles: image A = authentic subject, image B = approved layout/style, image C = real screen, image D = supplied wordmark. Omit unused roles.
- Approved exact copy and RTL requirements, with no extra invented text.
- Focal subject, usable copy region, hierarchy, palette family, and important exclusions.
- Elements to preserve: people/identity, scene geography, screen state, brand marks, and approved framing.
- The one change requested in this round and what success looks like on a phone.

## Example: founder/photo layout proposal

“Create a 4:5 editorial layout proposal for Ela Maayan. Use the supplied photo as the real subject and the supplied founder reference for visual direction. Keep all people and meaningful gestures visible. Use the quiet area identified in the brief for the headline, strong readable hierarchy, and the specified palette. Include only this exact approved Hebrew text: \[COPY\]. Keep right-to-left punctuation correct. Add no words, people, locations, or invented UI. Change only the requested text layout. Treat the supplied logo as a reference; the final original logo will be composited separately.”

Replace placeholders with real approved text before generation. If a real photo should not be transformed, ask for a separate layout/backplate proposal rather than sending it for a generative edit.

## Example: app-feature visual

“Create a 4:5 composition/backplate for a benefit-led Ela Maayan feature post. Reserve a large flat area at \[BOUNDS\] for a real screenshot to be inserted after generation. Use \[PALETTE FAMILY\], a clear headline region at \[BOUNDS\], and subtle emphasis pointing toward the relevant behavior. Do not draw an app interface, phone screen text, logo, store badge, route, or fabricated product data. Use only the approved headline if text is requested: \[COPY\].”

Composite the authentic screen and original logo into the proposal for final production. Do not redraw the screenshot to make it look more polished. Keep useful source crops readable and proportional.

## Iteration and final checks

Request the smallest necessary change and state what must remain. Inspect Hebrew character-for-character, line breaks, punctuation, actual asset integrity, and small-screen hierarchy. Text placement and brand consistency remain failure modes even for capable models. When exact typography/UI matters, retain them as deterministic source layers rather than accepting approximate generated versions.

Do not paste a catch-all “make this viral” prompt. Give the model the actual goal and constraints. Do not call its layout critique eye tracking or evidence of a measured engagement lift.

## layout-decisions.md

# Layout decisions

## Initial composition defaults

These are editable starting values based on reference inspection and phone readability, not platform ranking rules or measured optimum positions.

| Surface | Starting canvas | Working space | Text hierarchy |
| --- | --- | --- | --- |
| Carousel | 1080x1350 | Usually 5–8% edge breathing room; choose copy zones around the photo | Rough headline 70–110px, body 36–50px; adapt after phone-size inspection. |
| Reel | 1080x1920 | Start essential overlays in the central area; avoid top/bottom UI and right action rail; validate the actual preview | Short hook readable immediately; subtitles and location labels must fit the scene and voice. |
| Approved one-shot Reel | 1080x1920 | Preserve its source framing | Existing Reel skill specifies 58px bold white Hebrew with a subtle outline and a block starting near y=650; reuse only for that mode. |

A 1080px-wide export displayed around 360px wide scales text down to about one third of its pixel size. Use actual small previews rather than trusting export-size typography. Avoid shrinking a long paragraph until it technically fits.

Do not impose the conservative Reels-ad margins found in third-party summaries on every organic Reel or carousel. Meta's original safe-zone pages required login during the initial research. Record any current verified placement requirements separately from these heuristics.

## Three useful compositions

### Person and story

Protect face/gesture and story context first. Put the hook in sky, wall, water, or another quiet region. Use a small source wordmark. If there is no quiet area, pick a different photo or use a restrained treatment from the selected family; do not cover the person with a giant card by default.

### Place and practical detail

Leave the view/water/trail recognizable. A lower darkened field with white title and concise detail is an existing destination-card convention. In carousel 2, a place name plus one reason to go can also act as a new entry. Keep navigation/app invitations subordinate to the place's value.

### Real screen and benefit

Use one benefit headline and one enlarged authentic screen/crop. Point to one control/behavior only when necessary. Preserve labels, state, data, and semantic color. Avoid a decorative phone frame that makes proof unreadable. Use a real travel photo when it clarifies use rather than competing with the screen.

## Color and hierarchy

- General identity: Navy #0B3E56, Fountain Blue #BFE5F4, Fountain Soft #E5F3F5, Warm Ground #F9FBF6.
- Functional colors in the documented system: Trail/Action #007938, Water/Spring #007CAB, Sun/Highlight #EE9733, Lookout #BF5630. Do not change the actual app's tokens.
- Historical September 29 story family: charcoal #171B21, warm white #FFFDF8, orange #F27A48, sand #F3CB8D, with Heebo and the original handwritten wordmark.
- Prefer one accent role per slide. Saturation and local contrast determine salience in context; a universal “red/orange gets clicks” rule is unsupported.
- Use W3C contrast guidance (4.5:1 normal text, 3:1 large text under its definitions) as a readability reference. A desktop pixel size alone does not establish the displayed large-text category. Do not label a social image legally compliant solely from this checklist.

## Visual review prompts

1. At thumbnail size, what is the one dominant element? Does it match the story?
2. Can the headline be read without zooming, with no need to inspect a tiny phone?
3. Is there a distinct next level of detail rather than five equally loud elements?
4. Does the photo prove or clarify the words? Are meaningful faces, gestures, terrain, and UI visible?
5. Does slide 2 make sense alone and move the story forward when read after slide 1?
6. Does the video preserve contrast and placement across motion, not only in a hero frame?
7. Does the image remain recognizably ours without a large watermark?
