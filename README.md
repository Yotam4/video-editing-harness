# Ela Maayan content harness

Skills and versioned knowledge for carousels, brand work and video editing.

| System | Role |
| --- | --- |
| Git | Canonical skills, knowledge, decisions, briefs, approved copy, feedback, learning and handoffs |
| Notion under the Ela Maayan Hub | Reading mirror; existing content-bank publishing status remains operational |
| Drive | Photos, footage, production files, variants and exports; Git records stable references |

Start new social work with `el-hamaayan-content-router`: clarify the outcome, classify the content, brainstorm proportionately, then load the matching production modules. Use the [type registry](registry/content-types.json), [taxonomy](docs/taxonomy/README.md) and [architecture](docs/architecture/modular-content-system.md). Unfamiliar structures become candidates for review rather than automatic new skills.

Start at the [knowledge home](docs/README.md), then read [AGENTS.md](AGENTS.md) and the [skill catalog](skills/README.md). Knowledge is available in the checkout without a Notion connection.

Edit and commit knowledge in Git first. Refresh the existing Notion mirror under the Ela Maayan Hub after the commit, including a source permalink. Reconcile direct Notion edits into Git before refreshing them. There is no background sync.

## Layout

- `docs/`: knowledge, brand, decisions, content records and learning.
- `skills/`: existing first-party procedures, plus routing, brainstorming and product-video entry procedures, with local knowledge pointers.
- `references/`: stable sources, import hashes and mirror mapping.
- `registry/`: modular types and schema.
- `scripts/`: explainable classification and registry checks.
- `templates/`: reusable forms for Git documents.
- `workflows/`: production and mirror maintenance.
- `.work/`: ignored downloads, render scratch and temporary raw metric exports.

For Reel production, use the [editing and review workflow](docs/production/reel-editing.md) and [edit record](templates/reel-edit.md). `python3 scripts/review_video.py <video> .work/<review-version> --expect-reel` builds a local playback board and extracts exact review frames. FFmpeg/ffprobe and Python 3.11+ are required. The existing one-shot renderer is supported; montage assembly, transcription and audio mixing still require a selected production tool.

Media and raw datasets stay outside Git. Imported instructions mentioning bundled preview images or a CSV must resolve their external source instead. Root instructions define storage and optional CTAs.

The video workflow selectively adapts [Tal Siach's Take One](https://github.com/talsiach/take-one): run `node scripts/review-room/server.mjs <cuts-folder>` for local frame-pinned notes and cut comparison. See [the two-repo comparison](docs/research/video-harness-review.md), [attribution and license](THIRD_PARTY.md), and [the adaptation manifest](references/take-one-adaptation.json). Carousels and brand retain their established workflows. Original procedure/script hashes remain in [the import manifest](references/import-manifest.json).
