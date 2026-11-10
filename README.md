# Ela Maayan content harness

Our working instructions for carousels, brand work and video editing.

| System | Owns |
| --- | --- |
| This repository | Skills, workflows, scripts, empty templates and stable references |
| Notion | Knowledge, decisions, briefs, approved copy, feedback, results and item status |
| Drive | Photos, footage, working files, visual variants and exports |

Start with [AGENTS.md](AGENTS.md) and [the source map](references/sources.json). The source map points to the connected Notion knowledge home, existing content bank, brand knowledge and Drive resources. Use the existing records rather than creating a parallel content backlog.

## Start a session

Read the current content item and the relevant knowledge in Notion, then load the applicable skill from [the skill catalog](skills/README.md). Fetch media from its Drive source into ignored local working space. Save knowledge and item progress in Notion, production outputs in Drive, and reusable procedure changes in Git.

This repository does not sync Notion or Drive automatically. A reference grants no additional access. An agent needs the appropriate connection and must actually read the source.

## Imported material

Eight first-party skill instruction files and two scripts are preserved from the installed source packages. The [import manifest](references/import-manifest.json) records their hashes. Knowledge references have been moved to Notion; the relative reference files here are pointers. No photo/video previews, raw performance CSV, personal correspondence, or account credentials are included.

Some upstream skill instructions mention bundled previews or a bundled metrics CSV. Those are intentionally external in this harness: follow the Notion pointers and fetch the real Drive asset, or temporarily export the archived/live metrics outside Git. Do not invent a file or run a command against a missing bundled asset. The root instructions specify this storage adaptation and the current optional-CTA policy.

The present focus is carousels and brand, with the existing Reel workflow available. Tal's material has not been imported; assess its source and license before a future adaptation.

## Layout

- `skills/`: procedures and scripts; discover by the frontmatter name.
- `references/`: source map, import provenance and knowledge pointers.
- `templates/`: empty reusable forms for Notion records and Drive asset references.
- `workflows/`: session and review routines.
- `.work/`: ignored local downloads, render scratch and temporary metric exports.

Changes to a creative asset receive a Drive version; changes to a skill receive a Git commit. Record the relevant commit and source versions on the Notion content item. Keep files such as generated images, video, datasets and account exports out of every Git branch.
