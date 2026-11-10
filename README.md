# Ela Maayan content harness

Skills and versioned knowledge for carousels, brand work and video editing.

| System | Role |
| --- | --- |
| Git | Canonical skills, knowledge, decisions, briefs, approved copy, feedback, learning and handoffs |
| Notion under the Ela Maayan Hub | Reading mirror; existing content-bank publishing status remains operational |
| Drive | Photos, footage, production files, variants and exports; Git records stable references |

Start at the [knowledge home](docs/README.md), then read [AGENTS.md](AGENTS.md) and the [skill catalog](skills/README.md). Knowledge is available in the checkout without a Notion connection.

Edit and commit knowledge in Git first. Refresh the existing Notion mirror under the Ela Maayan Hub after the commit, including a source permalink. Reconcile direct Notion edits into Git before refreshing them. There is no background sync.

## Layout

- `docs/`: knowledge, brand, decisions, content records and learning.
- `skills/`: eight first-party procedures and two scripts, with local knowledge pointers.
- `references/`: stable sources, import hashes and mirror mapping.
- `templates/`: reusable forms for Git documents.
- `workflows/`: production and mirror maintenance.
- `.work/`: ignored downloads, render scratch and temporary raw metric exports.

Media and raw datasets stay outside Git. Imported instructions mentioning bundled preview images or a CSV must resolve their external source instead. Root instructions define storage and optional CTAs.

The focus is carousels and brand, with our Reel workflow included. Tal's material has not been imported. Original procedure/script hashes remain in [the import manifest](references/import-manifest.json).
