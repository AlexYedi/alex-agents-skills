# Columns, types, and the write that succeeds without landing

## Where the data can live

Two tables are needed, one of companies and one of people. **A table is not necessarily a CSV**, and
every command takes `FILE` or `FILE#TAB`:

| Shape | How to point at it |
|---|---|
| Two CSV or TSV files | `--companies companies.csv --contacts contacts.csv` |
| One `.xlsx` workbook, a tab each | `--companies 'book.xlsx#Companies' --contacts 'book.xlsx#People'` |
| A Google Sheet | not readable from here — it needs credentials this skill does not take and must never ask for. File → Download → Comma-separated values, once per tab. An agent with a Drive connector can fetch them instead |
| An old `.xls` | Save As `.xlsx` first, or export each tab |

`loader_lib.py sheets --companies <book.xlsx>` lists the tabs and proposes which is which, so a
workbook is shown mapped rather than interrogated.

**The `.xlsx` reader uses only the standard library** — an `.xlsx` is a zip of XML — because the
installer may have neither openpyxl nor pandas, and a loader that cannot open the file it was
pointed at is no loader.

**A spreadsheet stores a date as a number of days since 1899-12-30.** Read without its cell format
it is a plausible five-digit integer: `2011-04-02` arrives as `40635`, passes a numeric check, and
lands in Clay as nonsense — the same silent wrongness as a band in a number field, through a new
door. Date-formatted cells are converted to ISO on read. If a date column ever shows a bare
five-digit number, that conversion did not happen and the load should stop rather than continue.

## The six types, and there is no seventh

`clay audiences fields create --entity-type people|companies --name "<name>" --data-type <type>`

| Type | Holds |
|---|---|
| `text` | short free text |
| `number` | a numeric value |
| `email` | an email address |
| `url` | a URL |
| `date` | a date or datetime |
| `boolean` | true / false |

**There is no list or multi-value type.** A column holding `SaaS; Fintech; Payments` becomes one
`text` field. It can be matched with `contains`; it cannot be counted, split or faceted. Say that
while the mapping is on screen, not afterwards — an installer who knows will often split the column
into three booleans instead, and that decision is only cheap before the fields exist.

**A workspace has a per-data-type field budget.** Its size is not readable from anywhere the CLI
exposes, so it is handled as an error rather than planned against: `fields create` returns a
validation error, and the honest response is to report which columns did not get a field and let the
installer cut the mapping. Never quietly drop one.

## The failure this whole page exists for

A value the field's declared type cannot parse is **accepted, acknowledged, stored verbatim, and
invisible to every query.** Measured on one workspace:

| Sent | Into | The write said | The audience says |
|---|---|---|---|
| `512` | number | `✅ Success`, 4 fields updated | matches `> 100`. Populated. |
| `1,001-5,000` | number | `✅ Success`, 4 fields updated | `is_not_null` does **not** match it. `> 100` does not match it. |
| `87` | number | `✅ Success`, 4 fields updated | populated. |
| `Q3 2017` | date | `✅ Success`, 4 fields updated | `is_not_null` → **0 of 1** |

Two companies, both carrying a non-blank value in the same number field, both written and
acknowledged: `is_not_null` → **1**, `is_null` → **1**. The text field beside it → **2 of 2**.

Reading the record back with `clay audiences records get` shows `1,001-5,000` present on the record.
So three of the four places you would look — the run's success flag, its `fieldsUpdatedCount`, and
the record read — all agree the value is there, and only a filter disagrees. A TAM is a thing you
filter.

**This is not number-specific.** It reproduced on date, which suggests it is how the store treats a
value it cannot coerce to the field's type generally. It is reported as what was observed on one
workspace on one day, not as documented behaviour.

### What follows

- **Check every value against its column's type before the load**, and report per column: how many
  values fail, and two of them. That is the only cheap moment.
- **A column where many values fail is usually a bad inference, not bad data.** Offer `text`.
- **After the load, ask Clay for the populated count per field** and hold it against the count the
  CSV carried. That is the only honest completion test, and it is the reason Step 8 exists.

## Inferring a type from a column

The inference is a proposal, and the two sample values shown beside it are what makes it
correctable. It is deliberately conservative — **`text` is the fallback, and falling back is not a
failure.** A text field that holds everything beats a number field that silently holds nothing.

| Proposed | When | The trap it walks into |
|---|---|---|
| `number` | every non-blank value parses as a number after stripping thousands separators | a band (`1,001-5,000`), an approximation (`~250`), a range, or a trailing unit further down the file |
| `date` | every non-blank value parses as a date | a quarter (`Q3 2017`), a year alone, `TBD`, or two formats mixed in one column |
| `email` | every non-blank value contains exactly one `@` | several addresses in one cell |
| `url` | every non-blank value starts `http://` or `https://` | a bare domain with no scheme, which is a fine `text` value and a bad `url` one |
| `boolean` | every non-blank value is in one recognised pair | a third value — `unknown`, `n/a` — turning a boolean into a three-state column |
| `text` | anything else | nothing. This is the safe one |

**Sample from the whole file, never from the first rows.** Export order is rarely random and the
well-formed rows are usually at the top. The inference in `scripts/loader_lib.py` reads every
non-blank value in the column, because reading the whole file is cheap and being wrong is not.

**A number sent as a string is fine.** `"512"` filtered correctly at `> 100`. There is no need to
coerce types on the way out — only to make sure the value is one the field can parse at all.

## A boolean cannot be coverage-checked, so think twice before choosing one

Measured: on a boolean field, `is_not_null` returns exactly what `= true` returns, and `= false`
returns **everything else, including every record the field was never set on**. Counted on one
workspace: 15 true plus 21 false equals 36, which was every person in it, against 28 the loader had
written to.

So a boolean is effectively two-valued at query time — true, or not-true — and **no query separates
"explicitly false" from "never set".** Three consequences:

- A fill-rate or coverage reading on a boolean is wrong by the number of `false` rows, and this is
  true of any audit of an audience, not just of a load.
- The verification step reports booleans as unmeasurable rather than short.
- **If telling false from unset matters, do not use a boolean.** A text field holding `yes` / `no` /
  `unknown` keeps all three readable, which is usually what a research column meant anyway.

## Blank is a value, and which kind of blank matters

| | Blank in a **lookup** field | Blank in a **record** field |
|---|---|---|
| What happens | the node fails before it runs, `missing required inputs` | dropped by `removeNullValues: true`; the write succeeds |
| So | never route a row to a writer whose key it does not carry | a sparse column is harmless; it just writes fewer fields |

This asymmetry is the entire routing problem. A row's *record* fields can be as empty as they like;
its *match key* cannot be empty at all.

**And a match key is checked for being that KIND of thing, not merely for being non-empty.** A
malformed email, a phone with no digits, and a LinkedIn URL whose host is not `linkedin.com` are all
refused with wording that reads as though the field were blank. A `.example` domain and a `.example`
email address are both accepted, so this is not a check on whether the thing is real. Screen the
shape before firing, and fall through to the next key rather than losing the row.

## The row key, and minting one

The row key identifies a row in your file and in the ledger, and joins a contact to its company. It
is **not** the key Clay matches on, and it never can be.

Prefer, in order:

1. **A stable id column the file already carries** — a CRM id, an internal account id. Best, because
   it survives re-exports that reorder or reword everything else.
2. **The domain**, normalised: lowercased, scheme and `www.` stripped, trailing slash removed.
3. **A minted slug of the company name**, normalised: lowercased, accents folded, punctuation and
   legal suffixes removed, whitespace collapsed to single hyphens.

Minting from the name is a real answer for a file that has nothing else, and it has a real cost
worth stating when you use it: two genuinely different companies with the same name collapse, and a
company that gets renamed between exports becomes a new row. **Say which rule produced the key**, so
that a re-run with a differently-shaped export is recognisable as the different thing it is.

**Row keys must be unique within a file.** Two rows with the same row key is a file problem, not a
Clay problem, and the check reports it as its own count rather than folding it in with the match-key
collisions — they have different causes and different fixes.
