# Clay table harness (browser-driven)

The generic procedure for building **any** playbook's signal into a live Clay table. Read this
once. Then read the playbook's own `clay-table.md`, which only carries what is specific to that
signal: its column list, its formulas, its prompt, and its credit gate.

## Why this one is browser-driven

The `clay` CLI cannot create tables or columns. Its `tables` group is read-only:

```bash
clay tables list                      # enumerate
clay tables get <tableId>             # metadata
clay tables columns get <tableId>     # column ids and config   <- you WILL need this one
clay tables rows list <tableId>       # read rows
clay tables query --input '{...}'     # structured query
```

So the build happens in the browser. The CLI is still load-bearing during the build, for one
reason: **Clay formulas reference column IDs, not column names**, and `clay tables columns get` is
how you read the real IDs out after creating each column.

Any browser automation works — Claude in Chrome, a Playwright MCP, or a browser-use harness. The
steps below are written as instructions to a browser agent, so they name what to click rather than
what to call.

## Before you start

Have these decided and written down. Guessing any of them mid-build is how tables end up with
orphan columns nobody can explain later.

1. **Which table.** Signal columns belong on the table that already sits *behind* your email gate,
   so a paid enrichment never runs on a row whose email failed validation. If your table is not
   organized that way, the gate in step 6 does the same job, just later and after more spend.
2. **Which rows.** The playbook's `SKILL.md` § "Inputs required per row" lists the fields that must
   already be on the row. If those fields arrive on some rows and not others, decide now whether
   the blank rows are expected to stay blank or need a re-hydrate column. A signal column that
   silently produces nothing forever is almost always this.
3. **Cheap or robust pass**, where the playbook offers both. This changes cost by 50x or more.
4. **The abstain behavior.** If the line comes back empty, does the row still send with the clause
   spintaxed out, or does the row get excluded? Campaigns whose entire premise is the signal must
   exclude. Everything else should keep the row.

## The build, step by step

### 1. Open the table and confirm the input fields exist

Navigate to the table. Confirm every field in the playbook's inputs list is present and populated
on at least a few rows. If an input field is missing, stop — adding the signal column first just
produces a column of blanks.

### 2. Add the columns in order

The playbook's `clay-table.md` gives an ordered table with these headers:

| Order | Column name | Type | Action / integration | Input binding | Run condition | Notes |

Add them **in that order**, because later columns reference earlier ones. For each:

- **Add column** → pick the type from the Type field.
- For a **Formula** column, paste the formula from the playbook's formula block. It will contain
  placeholder IDs like `{{f_RoleStartDate}}` — those are not real, see step 3.
- For an **integration / action** column, search the action by the name in the Action field and
  bind its inputs to the columns named in the Input binding field.
- For an **AI** column, see step 5 — it has more required settings than the UI implies.

### 3. Replace every placeholder ID with the real one

This is the step people skip, and a formula that still contains a placeholder never fires — it
fails silently and the column stays blank.

After creating the columns, read the real IDs:

```bash
clay tables columns get <tableId> | jq -r '.columns[] | "\(.id)\t\(.name)"'
```

You get real IDs shaped like `f_6XuoXW8Zrv1m`. Go back through every formula and every run
condition and swap each placeholder for the matching real ID.

### 4. Know what a Clay formula actually is

Clay formulas are **JavaScript**, not spreadsheet syntax. This trips up everyone once.

- No `DATEDIF`, no `TODAY()`, no `VLOOKUP`.
- `&&` and `||`, never `AND` / `OR`.
- `==` for equality, never a single `=`.
- "Is empty" is `!{{f_x}}`. "Is not empty" is `!!{{f_x}}`.
- String compare wants explicit lowercasing: `String({{f_x}} || "").toLowerCase()`.

Real shapes, for calibration:

```js
!!{{f_6XuoXW8Zrv1m}} && {{f_gQGWRTeeBMYy}}?.length > 40
{{f_0t6np7pJzbu3TP2b54n}} == "true"
!!{{f_VSPIsv8tZXfj}} && !{{f_VSPIsv8tZXfj}}.toLowerCase().includes("purple")
```

**Constructs that fail silently in a Clay formula column** — they return null with no error, which
looks exactly like "no data yet":

- immediately-invoked function expressions wrapped in `try`/`catch`
- regular expressions in some contexts
- anything that throws

Keep formulas short, total, and free of exceptions. If a formula needs more than a few lines,
that is a sign it should be a code node in a workflow instead.

### 5. The AI column, and the empty-column trap

⚠️ **The single most common way a playbook build ships broken.**

Building an AI column with only a model and a prompt produces **empty output on every row** for
the short rewrite prompts these playbooks use. The reason: at default reasoning effort, the model
spends its entire token budget on reasoning and returns `finish_reason=length` with empty content.
Measured on this exact prompt shape: empty on 10 of 10 rows.

Clay AI columns expose these bindings. Set all of the ones marked required.

| Binding | Value | Required | Why it matters |
|---|---|---|---|
| `model` | the model named in the playbook's locked prompt | yes | cost math assumes it |
| `systemPrompt` | the static prefix from the playbook, byte-identical | yes | prompt caching depends on the prefix never varying |
| `prompt` | the per-row `Facts: ...` line only | yes | per-row data goes last, never merged into the prefix |
| `reasoningLevel` | lowest / minimal | **yes** | **this is the fix for the empty column.** Read the literal accepted value out of the UI dropdown |
| `reasoningBudget` | leave unset if `reasoningLevel` took | no | raising the budget also "works" and costs roughly 35x per row for a pure rewrite. Do not use it as the fix |
| `maxTokens` | `2000` | yes | matches the API path |
| `jsonMode` | `true` | yes, when the prompt returns JSON | without it the column can return prose and the extract formula yields nothing |
| `answerSchemaType` | JSON, with only the fields the playbook lists | yes | makes the extract formula's `?.field` access reliable |
| `temperature` | leave unset | — | reasoning models reject it |
| `maxCostInCents` | a small per-row ceiling | recommended | cheap insurance against a runaway |

**Do not add deterministic fields to `answerSchemaType`.** If the playbook computes an enum in a
formula column, the model must not also return it. A model-flipped enum makes the copy claim
something false in a fluent sentence, which passes every structural check.

### 6. Wire the credit gate

Every paid column gets a run condition so it only fires on rows that are worth paying for. The
generic shape, which each playbook specializes:

```js
{{f_UpstreamCheckPassed}} == "true" && {{f_EmailStatus}}?.toLowerCase() == "valid"
```

Three things belong in almost every gate:

1. **The free upstream check passed.** Whatever cheap signal proves the row qualifies.
2. **The email is valid.** Never pay to personalize a row you cannot send to.
3. **The output is not already filled.** `!{{f_TheOutputColumn}}` stops re-runs from re-charging.

### 7. Add the QC formula column

Every playbook ends with a QC column that fails the row on the mechanical stuff. Generic version:

```js
(() => { const v = String({{f_TheLine}} || ""); if (!v) return "empty";
  if (v.includes("—") || v.includes("–")) return "fail: dash";
  if (v.endsWith(".")) return "fail: trailing period";
  if (v[0] !== v[0].toLowerCase()) return "fail: uppercase start";
  if (v.length > 90) return "fail: too long";
  return "pass"; })()
```

Filter the table view to `QC != "pass"` before every push. This catches formatting, never truth.

### 8. Smoke test on 5 rows, and actually read them

Run the AI column on 5 rows. Then **read the five sentences out loud**.

- All 5 empty → `reasoningLevel` did not take effect. Fix the reasoning level. Do not "fix" it by
  raising `reasoningBudget`.
- All 5 identical → a per-row variable is unbound. Check the `prompt` binding.
- Sentences fluent but wrong → your source is wrong, not your prompt. No downstream check catches
  this. Add the playbook's cross-check, or accept the documented error rate knowingly.
- Sentences contain a legal suffix or a parenthetical → run `playbook-company-name-cleaning`
  into a clean-name column upstream and bind the prompt to that instead.

Only after the 5 rows read correctly do you add rows in bulk.

### 9. Push the field to your sending tool

The signal column becomes a lead-level custom variable in your sequencer. Keep the field name
identical to the playbook's output field so copy written against one playbook works against any
table that runs it.

## Failure modes, generic

| Symptom | Cause | Fix |
|---|---|---|
| Column is blank on every row, no error | AI column reasoning effort at default | set `reasoningLevel` to minimal, step 5 |
| Column is blank on every row, no error | A formula still contains a placeholder ID | step 3 |
| Column is blank on **some** rows forever | Those rows came from a source that does not carry the input fields | re-hydrate column, or filter the view so the blanks are visible rather than silent |
| Gate drops every row | `==` vs `=`, or comparing against a boolean when the formula returns the string `"true"` | Clay formula columns commonly return strings. Compare to `"true"`, not `true` |
| Output has an em dash | The prompt's ban was reworded | prompts are locked for a reason. Restore the exact line |
| Costs 10x the estimate | `reasoningBudget` was raised instead of `reasoningLevel` lowered | step 5 |
| The same company enriched 40 times | No dedupe upstream | dedupe on bare lowercase domain before the paid column, always |
