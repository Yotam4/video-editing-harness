# Git knowledge with a Notion mirror

Date: 2026-11-10. Status: accepted by the owner in this setup conversation.

## Decision

Use our existing `Yotam4/video-editing-harness` for first-party carousel, brand and video skills. Store the actual knowledge home and documents in Git under `docs/`. Notion mirrors that knowledge only under the Ela Maayan Hub. Drive stores media and production files; Git stores their stable references.

Git holds knowledge, decisions, briefs, approved wording, feedback, learning and handoffs. Existing operational content-bank status remains in its current database.

## Rationale

The owner wants the same model used for engineering docs: knowledge can be read and versioned with the harness, with a browsable Notion mirror. A repository containing only links to Notion is insufficient.

## Superseded arrangement

The initial setup placed knowledge in Notion with pointer files in Git. This decision replaces that split. The skill reference files now resolve to local knowledge documents. Original procedure files and scripts remain unchanged; the root policy governs storage and optional CTAs.

## Operation

Commit knowledge first, then refresh the mapped Notion pages and record the source commit. Preserve conflicting Notion edits as proposed Git changes. Retain the committed knowledge if mirror refresh fails. No background sync was requested or installed.

Move the existing mirror home under the Ela Maayan Hub, preserving its children and history. Do not create duplicate knowledge trees outside the Hub or import unrelated engineering docs or third-party video material.
