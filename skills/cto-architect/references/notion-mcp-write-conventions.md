# Notion MCP write conventions & gotchas

Non-obvious property-format and markdown-flavor rules for the Notion MCP's `notion-create-pages` and
`notion-update-page`. Each was learned live — the rejected syntax was observed to land as escaped literal
text. Follow them mechanically; the API error messages are the source of truth if anything drifts. Applies
to **any** project writing to Notion via MCP.

## `create-pages` property formats

a. **Multi-select properties take a JSON-array-STRING** — not a comma-separated string and not a native array.
   - Correct: `"<Prop>": "[\"AI/ML\",\"Enterprise Software\"]"`
   - Rejected: `"<Prop>": "AI/ML,Enterprise Software"` and `"<Prop>": ["AI/ML","Enterprise Software"]`
b. **Select properties must exactly match a defined DB option.** On failure the API error lists the valid
   options — trust the error, not any doc; the live DB schema is authoritative.
c. **Relations take a JSON-array-string of full page URLs** (not bare page IDs). Use the `url` field
   returned by `notion-create-pages` verbatim: `"<Rel>": "[\"https://www.notion.so/347d3699...\"]"`.
d. **Date properties use expanded keys:** `"date:<Prop>:start"` + `"date:<Prop>:is_datetime"` (0/1); add
   `"date:<Prop>:end"` for ranges.
e. **Verify live schema first.** Before a batch create against an unfamiliar DB, `notion-fetch` the
   data-source URL — property names, option sets, and types drift between docs and the live DB.
f. **Write order for bidirectional relations:** create the no-dependency ends first, then the dependents,
   using each created page's returned URL for the next level's relation field. (Setting one side of a
   bidirectional relation auto-populates the other — but only if you pass the URL that already exists.)
   Skipping the order silently produces empty relation fields.

## `update-page` (and `create-pages` body) markdown flavor

g. **Toggles use `<details><summary>…</summary>…</details>` HTML — and ONLY this form.** Notion's
   `+++ title … +++` markdown does NOT work (lands as literal `+++`). `<details>` is the only allowlisted
   toggle HTML. (Good for preserving superseded content inline without sub-page sprawl.)
h. **No markdown TOC syntax works via the MCP.** `[[toc]]`, `[TOC]`, `+++`, `<toc/>`,
   `<table_of_contents/>` all land as literal text. The only real auto-updating TOC is the `/toc` slash
   command in the Notion UI (one-time per page). Write-time workaround: a static "page-index" callout (see i).
i. **Page-index callout convention** (any multi-section page worth scanning): a blockquote with a 📑 emoji,
   bold "Page index", a bullet list of H1 sections each with a one-line description, ending with the italic
   tip *"Place cursor below this callout and type `/toc` to add Notion's interactive auto-updating table of
   contents — one-time per page."* Static structure now; `/toc` is opt-in in the UI.
j. **`<` in body text auto-escapes to `\<`** in stored markdown but renders correctly (`\<5min` → `<5min`).
   Cosmetic — don't "fix" it.
k. **Markdown `|`-tables auto-convert to native `<table header-row="true">` blocks** on write (sortable,
   filterable, resizable) — preferred over raw markdown.
l. **`update_content` `old_str` must match the STORED markdown, not what you authored.** Notion normalizes
   emphasis on write: `_italics_` is stored as `*italics*`. An `old_str` with underscores fails with
   `"No matches found"` though the rendered text looks identical. Fetch the page and copy the exact stored
   snippet, or author the match with `*`. (Emphasis markers are the trap; em-dashes etc. are preserved.)
m. **`notion-update-page` `insert_content`/`update_content` mangles `\n` escapes into a literal "n".**
   Author multi-line *update* payloads with REAL newlines, not `\n`. `create-pages` is unaffected — it
   handles `\n` correctly.

## The two-line summary
Structured/filterable data → **properties** (with the exact JSON-array-string formats above); long-form
text → **page body**. Verify the live schema before batch writes, and for updates always diff against the
*stored* (normalized) markdown, with real newlines.
