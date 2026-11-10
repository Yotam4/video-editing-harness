# Maintain the Notion mirror

1. Read the Git source and existing mapped Notion page. Use `references/notion-mirror.json` to locate source and destination. All new knowledge mirrors belong beneath the Ela Maayan Hub.
2. Reconcile unexpected direct mirror edits into a proposed Git change; do not discard them. Commit accepted knowledge changes first.
3. Refresh the existing page from the committed document. Preserve child pages and unrelated operational data. Include the Git file permalink at the source commit and the mirror date.
4. Create mirrors for new documents beneath the same knowledge home and record their mappings in Git. Do not create a second tree elsewhere.
5. Verify the write result. Report inaccessible or stale mirrors. A failed refresh never makes Notion the only copy.

This is an explicit session workflow, not an installed background or bidirectional sync. Media and raw metric exports remain external.
