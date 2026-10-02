# Clay table build: New in Role

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first —
it carries the generic procedure, the formula rules, and the AI-column empty-output trap. This
file only carries what is specific to this signal.

⚠️ **Status: specification. This table has never been built and run.** The graded path is the
script path in `SKILL.md` §4. Build this on 5 rows and read the output before you trust it.

## Where the columns go

Put them on the table that already sits **behind your email gate**, so no paid column ever runs on
a row whose email failed validation.

## Prerequisite: where the imported columns come from

Five columns below are marked "(imported with the row)": `Role Start Date`, `Positions At Current
Company`, `Prior Title`, `Prior Company`, `Current Title (from job_history)`. They all derive from
the people database's `job_history` array, and **most list sources do not carry that array.**

This is the single most likely way this recipe appears "broken but not erroring". If rows arrive
from a generic contact import rather than from this playbook's own pull, all five columns are
null, the downstream formulas evaluate to null/false, the credit gate never opens, and the AI
column **silently produces nothing forever with no error**.

Pick one and write it into the campaign brief:

1. **Import-only (default).** The recipe runs only on rows from this playbook's own pull, where the
   five fields ride along with the row. Rows from other sources are expected to sit blank. Filter
   the table view to `Role Start Date is not empty` so the blanks are **visible rather than
   silent**.
2. **Re-hydrate.** Add a person-search HTTP column *before* column 1, scoped to the row's own
   company and name, and parse the five fields out of `results[0].person.job_history`:

   ```jsonc
   POST https://api.prospeo.io/search-person      // header X-KEY from workspace auth, never inline
   { "page": 1, "filters": {
       "company": { "websites": { "include": ["{{Company Domain}}"] } },
       "person_name_search": { "include": ["{{First Name}} {{Last Name}}"] } } }
   ```

   One request per row, so respect the 2 to 2.5 req/s ceiling, and gate it on
   `!{{f_RoleStartDate}}` so it never re-runs on a row that already has the data.

   ⚠️ Confirm the person-name filter key against the provider's filter documentation before wiring
   this. An `INVALID_FILTERS` response cannot tell you whether a key exists or its value was bad.

## Integration check

Native integrations first; the HTTP API column is the fallback.

| Provider | Native integration? | What to use |
|---|---|---|
| The people database (re-hydrate column) | usually yes | the native person-lookup action **if it exposes `job_history`**. If it does not, the raw HTTP call above is correct, and that is a real parameter-coverage reason — note it in the column |
| The model (column 11) | yes | native AI column |

Native action columns carry an `authAccountId`; a raw HTTP column never does. Check with:

```bash
clay tables columns get <tableId> | jq -r '.columns[] | select(.authAccountId) | .name'
```

## Columns

The `{{f_...}}` IDs below are **placeholders**. After creating each column, run
`clay tables columns get <tableId>`, read the real `f_...` id, and paste it into the formulas that
consume it. A formula that still contains a placeholder never fires.

| Order | Column name | Type | Action | Input binding | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | Role Start Date | Text | (imported) | `job_history[current].start_year` + `start_month` as `YYYY-MM` | n/a | machine format, used only for math |
| 2 | Months In Role | Formula | JS | Role Start Date | n/a | F1. Recomputed at send time so a row that ages out is caught |
| 3 | Role Start Month Label | Formula | JS | Role Start Date | n/a | F2. `2026-04` → `April 2026`. **This is what the prompt reads**, not column 1 |
| 4 | Positions At Current Company | Number | (imported) | count of `job_history` entries sharing `company_id` with the current role | n/a | this is what makes column 5 deterministic |
| 5 | Role Change Type | Formula | JS | Positions At Current Company | n/a | F3. `> 1` → `promotion`, `= 1` → `new_hire`. **Never let AI decide this** |
| 6 | Prior Title | Text | (imported) | most recent non-current `job_history` title | n/a | may be empty |
| 7 | Prior Company | Text | (imported) | prior `job_history` entry `company_name` | n/a | **Required.** The prompt binds `prior_company`. Omit this and every row sends an unbound variable |
| 8 | Current Title (from job_history) | Text | (imported) | `job_history[current].title` | n/a | **not** `person.current_job_title`, which disagrees and was the source of the one live miss |
| 9 | Title Conforms | Formula | JS | Current Title (from job_history) | n/a | F4. The title gate. Returns the string `"true"` or `"false"` |
| 10 | Company Name Clean | Text | see `playbook-company-name-cleaning` | Company Name | `!{{f_CompanyNameClean}}` | run BEFORE column 11 if the list has legal suffixes |
| 11 | New In Role Line Raw | AI | the model, prompt from `SKILL.md` §6 | columns 1-10 plus First Name | the credit gate below | **the only paid column.** Returns a JSON object, not a string. See bindings below |
| 12 | New In Role Line | Formula | JS | New In Role Line Raw | n/a | F5. Pulls the string out of the JSON blob |
| 13 | New In Role Line QC | Formula | JS | New In Role Line | n/a | F6. Fails the row on mechanical problems |

## Column 11 bindings

Full explanation in the harness § "The AI column, and the empty-column trap". Specific to this
playbook:

| Binding | Value |
|---|---|
| `model` | the small reasoning model from `SKILL.md` §6 |
| `systemPrompt` | everything **above** the `PER-ROW DATA` marker, byte-identical |
| `prompt` | the `Facts: ...` line only |
| `reasoningLevel` | **lowest / minimal.** Without this, measured empty content on **10 of 10 rows** |
| `reasoningBudget` | leave unset. Raising it also "works" and costs ~35x per row |
| `maxTokens` | `2000` |
| `jsonMode` | `true` |
| `answerSchemaType` | JSON: `new_in_role_line` (string), `confidence` (string). **Do not add `role_change_type`** — that is column 5's job |
| `temperature` | leave unset |
| `maxCostInCents` | a small per-row ceiling |

## Formulas

```js
// F1  Months In Role
(() => { const s = {{f_RoleStartDate}}; if (!s) return null;
  const [y, m] = String(s).split("-").map(Number); const n = new Date();
  return (n.getFullYear() - y) * 12 + (n.getMonth() + 1 - m); })()

// F2  Role Start Month Label  ->  "April 2026"
(() => { const s = String({{f_RoleStartDate}} || ""); const [y, m] = s.split("-");
  const M = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  return (m && M[Number(m) - 1] && y) ? M[Number(m) - 1] + " " + y : ""; })()

// F3  Role Change Type
{{f_PositionsAtCompany}} > 1 ? "promotion" : "new_hire"

// F4  Title Conforms  (the title gate)
// Replace the keyword list with THIS campaign's target titles, lowercase.
// ⚠️ THE GATE LIST IS NOT THE SEARCH LIST. It must be the search titles PLUS every
// abbreviation and variant people actually put on LinkedIn ("coo", "vp ops",
// "svp operations"). Gate on the search list alone and you silently drop every
// person whose job_history title is literally "COO", which is very common.
(() => { const t = String({{f_CurrentTitleFromHistory}} || "").toLowerCase();
  const keys = ["chief operating officer", "coo", "vp of operations", "head of operations", "director of operations"];
  return keys.some(k => t.includes(k)) ? "true" : "false"; })()

// F5  New In Role Line
{{f_NewInRoleLineRaw}}?.new_in_role_line || ""

// F6  New In Role Line QC
(() => { const v = String({{f_NewInRoleLine}} || ""); if (!v) return "empty";
  if (v.includes("—") || v.includes("–")) return "fail: dash";
  if (v.endsWith(".")) return "fail: trailing period";
  if (v[0] !== v[0].toLowerCase()) return "fail: uppercase start";
  if (v.length > 90) return "fail: too long";
  return "pass"; })()
```

## Credit gate (column 11's run condition)

```js
{{f_MonthsInRole}} <= 6 && {{f_TitleConforms}} == "true" && {{f_EmailStatus}}?.toLowerCase() == "valid"
```

No paid action runs unless every cheaper upstream step succeeded, the title actually conforms, and
the row is sendable. Note the operators: `&&` not `AND`, `==` not `=`, and `"true"` as a **string**
because F4 returns a string.

## Push to your sequencer

Lead-level custom variable `{{new_in_role_line}}`. Also push `{{role_change_type}}` if the copy
branches between "congrats on the new seat" and "congrats on taking over".

## Smoke test

Run column 11 on 5 rows and read the sentences.

- All 5 empty → `reasoningLevel` did not take. **Fix the reasoning level**, do not raise
  `reasoningBudget`.
- All 5 blank because upstream columns are blank → you have the imported-columns problem above.
- Sentences fluent but the title is wrong → that is the ~10% source-error rate, not a prompt bug.
  Add the leadership-page cross-check or accept it knowingly.
