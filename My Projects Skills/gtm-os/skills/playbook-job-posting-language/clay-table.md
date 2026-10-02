# Clay table build: Job Posting Language

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.**

## Where the columns go

The table behind your email gate.

## Integration check

| Provider | Native? | Use |
|---|---|---|
| A jobs provider with a Clay integration | often **yes** (`leadmagic-find-jobs`, `cpj-find-lists-of-jobs`, `enrich-job`) | the **native action** |
| A jobs provider without one | no | `http-api-v2`, correctly |
| The model | yes | **native AI column on `gpt-4o-mini`** — see below |

⚠️ **Do not use a nano-class reasoning model in a native AI column here.** Clay does not expose
reasoning effort, and at default effort this exact prompt returned **empty content on all 8 generating
rows** while rows that had nothing to say succeeded normally. **Your abstains look healthy and only
the rows worth having die silently.**

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free, `type: "bare"` |
| 2 | Company Profile URL | action / HTTP | `{{Domain}}` | `!!{{f_Domain}}` | domain → job-board company profile |
| 3 | Name Match | Formula | see below | `!!{{f_Profile}}` | **mandatory.** A resolution can land on the wrong company |
| 4 | Job Postings Raw | action / HTTP | `{{f_Profile}}` | `{{f_NameMatch}} === "pass"` | **filter server-side** — description keywords in the request, never scanned locally |
| 5 | Job Postings Deduped | Formula | dedupe on title+url, keep ≤5, keep `title`, `url`, `date_posted` | `!!{{f_PostingsRaw}}` | free |
| 6 | Job Line Raw | AI | `gpt-4o-mini`, `SKILL.md` §6 prompt | `!!{{f_PostingsDeduped}}` | the only paid column |
| 7 | job_posting_line | Formula | parse the line from 6 | `!!{{f_LineRaw}}` | **ungated. Audit only — never bind copy here** |
| 8 | job_role_named | Formula | parse from 6 | same | |
| 9 | job_evidence_url | Formula | parse from 6 | same | |
| 10 | job_posted_date | Formula | the `date_posted` of the posting whose URL matches column 9 | same | drives column 12 |
| 11 | job_confidence | Formula | parse from 6 | same | |
| 12 | **job_posting_line_safe** | Formula | see below | none | ⚠️ **THIS is the field you push.** Skip this column and you rebuild the one failure in the live test |

## Column 3: the name-match gate

```js
(() => {
  const norm = s => String(s || "").toLowerCase().replace(/[^a-z0-9]/g, "");
  const want = norm({{f_CompanyName}});
  const got  = norm({{f_Profile}}?.company_name);
  if (!want || !got) return "unknown";
  return (want.includes(got) || got.includes(want)) ? "pass" : "fail";
})()
```

A domain→profile resolution can land on a different company, and every posting after that point is
about the wrong business. Gate column 4 on `"pass"`.

## Column 12: the freshness gate

```js
(() => {
  const d = {{f_JobPostedDate}};
  const line = String({{f_JobPostingLine}} || "");
  if (!line || !d) return "";
  const days = (Date.now() - Date.parse(d)) / 86400000;
  // Detect on 60 days, but only CLAIM on 30. A date_posted is when the provider
  // observed the posting, not proof the job is live. One live-test row quoted a
  // 53-day-old posting that was already gone from the company's own board.
  return days <= 30 ? line : "";
})()
```

**Accept that this kills some genuinely open roles.** One verified-open posting at 49 days blanks by
design. That is the price of an age proxy, and it costs you volume rather than credibility.

## Credit gate

Column 6 is the only paid column, gated on postings existing. Everything upstream is free or nearly
so.

**Add an AI classifier column only if the recall measurement in `SKILL.md` note C says to** — and if
you do, gate it on the rows the keyword filter **missed**, not on every row.

## Push to your sequencer

`{{job_posting_line_safe}}` — **column 12, never column 7.**

Also push `job_evidence_url` as a lead-level field so a reply can be answered without re-researching.

## Smoke test

Run 10 rows.

- Model column ran but every line is empty → you used a reasoning model in a native AI column.
- Postings come back but never match your keywords → you are scanning returned fields instead of
  filtering server-side. **1 of 8 vs 5 of 8.**
- A posting belongs to a different company → the name-match gate is missing.
- Copy references a dead role → you bound column 7 instead of column 12.
