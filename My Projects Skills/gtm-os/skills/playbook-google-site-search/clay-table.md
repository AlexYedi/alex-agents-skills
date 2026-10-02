# Clay table build: Google `site:` Keyword Filter

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.** The 9/10 verdict covers the script path only.

⚠️ **Do step 0 in `SKILL.md` §5 before you build a single column.** Run the exact query for 3 to 5
real domains from your actual list and read the results with your own eyes. Ten minutes there saves
a rebuilt table.

## Where the columns go

The table behind your email gate, so these columns run **after** email validation. Rows that will
not survive the email gate must not consume search or model calls.

## The dependency cycle, and why column 6 exists

Read this before you "simplify" the column list, because the obvious simplification **makes the
table impossible to build.**

The hit guard (col 7) and the copy field (col 9) **both** need the sanitized line text. Col 9 is
gated on col 8, which is gated on col 7. So if you compute the sanitizer *inside* col 9, you get
**7 → 9 → 8 → 7**, and **Clay rejects cyclic formula references. The table will not build.**

The escape that will tempt you — dropping the "line is not empty" clause from column 7 — **removes
the exact guard that stopped `Noticed .` from rendering into a live email.**

So: sanitize once, in its own column, before anything that gates on it.

## Columns

**The order below is a dependency order, not a display preference:** 4 → 6 → 7 → 8 → 9/11.

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Site Keyword Query | Formula | `"site:" + {{Domain}} + " \"" + {{Keyword}} + "\""` | `!!{{f_Domain}}` | builds the query in **one visible place** so the team can eyeball it. One keyword, never an OR chain |
| 2 | Site Search Raw | HTTP API | your SERP endpoint, query **percent-encoded**, limit 10, key from a workspace secret | `!!{{f_Query}}` | ⚠️ **percent-encode** — raw quotes and colons in a URL are rejected |
| 3 | Site Keyword Literal | Formula | a **normalized** contains check, see below | `!!{{f_SearchRaw}}` | **THIS COLUMN IS THE CREDIT GATE.** It short-circuited 3 of 10 rows in the live test |
| 4 | Site Keyword Judge | AI | the §6 prompt, per-row data last | `!!{{f_Literal}}` | returns the JSON blob |
| 5 | Site Keyword Error | Formula | see below | always | **Mandatory. Error rows are re-run, never treated as no-signal** |
| 6 | Line Sanitized | Formula | sanitize the judge's line **unconditionally** | `!!{{f_Judge}}` | **exists to break the cycle. Never a pushed variable** — it is populated on rows that fail the gate |
| 7 | Site Keyword Hit | Formula | `mentions == true && status != "none" && sanitized line is not empty` | `!!{{f_Judge}}` | the consistency guard. **Do not drop the line-is-not-empty clause** |
| 8 | campaign_usable | Formula | `{{Hit}} && status == "has" && confidence == "high"` | `!!{{f_Judge}}` | **compute this BEFORE the copy columns** |
| 9 | site_keyword_line | Formula | `{{campaign_usable}} ? {{LineSanitized}} : ""` | `!!{{f_campaign_usable}}` | ⚠️ **the run condition is `campaign_usable`, never "the judge returned something"** |
| 10 | site_keyword_url | Formula | the evidence URL from the judge | `!!{{f_Hit}}` | gated on **Hit**, not `campaign_usable` — you want the evidence URL for suppressed rows too |
| 11 | site_keyword_sentence | Formula | `{{campaign_usable}} ? "Noticed " + {{site_keyword_line}} + ". " : ""` | `!!{{f_campaign_usable}}` | **this is the field you push, not column 9.** Note the trailing space inside the quotes |

## Column 3: the literal filter

Not a plain lowercase `contains`. Lowercase both sides, collapse every run of spaces and hyphens to
one space, then accept **either** the normalized form **or** the space-free form — so `SOC 2` matches
`SOC 2`, `soc-2`, **and** `SOC2`. A plain contains silently drops the `SOC2` spelling.

Run it over the concatenated titles and snippets, **excluding** results whose host starts
`community.` `forum.` `forums.` `discuss.` `answers.` `feedback.` `ideas.` `status.` `help.` — those
are users talking, not the company.

## Column 5: the error column

Non-empty when the search returned an HTTP error or an empty body **while a query was built**, or
when the judge is empty / unparseable / truncated **while the literal filter was non-empty**.

⚠️ **Without this column, a rate limit, a 5xx, or a model truncation leaves an empty judge cell that
column 8 silently converts to `campaign_usable = false`** — a wrong abstain on a company that
genuinely mentions the keyword. That is exactly what happened in the live test.

**Filter on this column and re-run those rows before you read any coverage number.**

## Column 6: the sanitizer

Unconditionally: strip a leading `Noticed` / `noticed` / `I noticed` / `that`; strip trailing
periods; replace em and en dashes with commas; strip stray quotes; **then** lowercase the first
letter **only** when it is an ordinary word — skip when the first word is an all-caps acronym (SOC,
HIPAA), carries an internal capital (HubSpot), or matches the domain root.

⚠️ That carve-out prevents the sanitizer from lowercasing a brand. **It does not re-capitalize a
brand the model itself wrote lowercase.** That is a prompt problem, and it is why the 20-sample read
in `SKILL.md` §7 exists.

## Credit gates

- **Column 2** costs a search call, gated on the query having been built.
- **Column 4** is the only model spend, gated on the **literal filter** having matched.

No paid action runs unless every cheaper upstream step produced something.

## Push to your sequencer

Push **`{{site_keyword_sentence}}` (column 11)** as the copy field, and `site_keyword_url` as a
second lead-level field so an operator can check any claim a prospect challenges.

Both column 9 and column 11 already emit `""` for every row that fails the gate, so an ungated upload
cannot leak a suppressed claim. **That is the only reason it is safe — so never "simplify" either
column back to a judge-is-not-empty gate.**

⛔ **Never push column 6, the raw judge output, or any audit field.** Those are intermediate and
**are populated on suppressed rows.**

At upload, filter on `campaign_usable == true` if the campaign exists only to reach companies with
the signal.

## Smoke test

Run 10 rows including one domain you expect to miss.

- Model column ran on every row → the literal filter in column 3 is not gating.
- Everything `campaign_usable` → your keyword is too generic to filter on.
- The table will not save, citing a cyclic reference → you collapsed the sanitizer into column 9.
- `Noticed .` appears anywhere → column 7 lost its line-is-not-empty clause, or the body is framing
  column 9 instead of using column 11.

Then run the 20-sample grammar read in `SKILL.md` §7 before launch.
