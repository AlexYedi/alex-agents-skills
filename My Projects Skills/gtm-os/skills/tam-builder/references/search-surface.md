# The search surface — limits, contract, and what it will not tell you

Read from `clay search --help`, `clay search query-mode {create,run,reference} --help` and the
grammar reference, plus one live enumeration run to exhaustion, on **2026-08-13**. Re-read
`clay search --help` at the start of every build: the limits are **plan-dependent**, and the plan
changes the design rather than only the budget.

## Limits, by plan tier

| Plan | Per request | Per search | Period allowance |
|---|---|---|---|
| Free | 50 | **50 — hard stop** | 100 / month, resets 1st UTC |
| Trial | 50 | 50 | 10,000 for the trial |
| Paid | 500 | — | 1,000,000 / year, resets 1 Jan UTC |
| Enterprise | 500 | — | 10,000,000 / year, resets 1 Jan UTC |

**Search results are a separate currency from Clay Credits.** They meter against this yearly
workspace allowance. A cost quote naming only credits reports the discovery half of a TAM build as
free. Verified live: `periodQuota` came back on every page of that run as
`{limit, used, remaining, resetsAt}`, and `used` incremented by exactly the number of rows
returned — 33 rows for the probe, metered to the row.

**But it is OPTIONAL, not guaranteed** (checked against Clay's published schema 2026-08-28: only
`data`, `has_more` and `source_type` are required). "Came back on every page" is what one run did,
not a contract. Read it defensively.

On **Free**, the 50-per-*search* stop means a slice cannot be enumerated past 50 records at all —
no paging around it. A partition designed for 500-row slices is not executable there.

## The two things the surface will not give you

### 1. No population count

The grammar's own query-mode policy, verbatim:

```
- Always use `select from ...` queries.
- Never use count-mode clauses.
- Never include `limit` clauses.
```

and `query-mode create` repeats it: *"Count-mode and jobs queries are not supported."* So "how many
companies match this ICP" is not askable. A TAM figure can only be an enumeration that was counted.

Note the second consequence of banning `limit` clauses: in query mode you never write a LIMIT, so
an `exhaustionReason` of `query_limit` is **not** your limit — it is the platform's cap surfacing
under the same name. It means *something stopped you*, and on Free that something is 50.

### 2. No reliable identity — `domain` is a claimed attribute

Verified by enumerating `select from companies where domain = "<a major payment processor>"` to
exhaustion:

```
page 1 (--limit 5)   →  5 rows, hasMore true
page 2 (--limit 50)  → 28 rows, hasMore false, exhaustionReason: no_more_results
                        33 records total, ALL carrying that domain
                        28 distinct clay_company_id on page 2 alone
```

The records are not one company. They are unrelated micro-businesses, creators and small
organizations across several countries whose company page lists a payment link as its website —
one of them reporting a size band of `10,001+`. Consequences:

| You might | It actually |
|---|---|
| dedupe the TAM on `domain` | merges dozens of unrelated organizations into one |
| count distinct domains as companies | undercounts wherever pollution clusters |
| dedupe on `clay_company_id` | keeps all 33 — they are distinct records, not duplicates |

There is no key that fixes this at TAM scale. The workable move is to **flag rather than resolve**:
a domain shared by many records whose names, countries and size bands are mutually unrelated is a
pasted-link artifact, not a corporate family. Hold those records out as `identity_unresolved`, count
them, and list them.

## The contract that makes coverage provable

`clay search query-mode run <searchId>` returns:

```
data[]           the page of records
hasMore          whether the iterator has more
exhaustionReason present only when hasMore is false:
                   "no_more_results"  → every matching record was returned  ← PROOF of completeness
                   "query_limit"      → something capped it first
periodQuota      { limit, used, remaining, resetsAt }
sourceType       "people" | "companies"
```

Verified live: `hasMore: true` with `exhaustionReason: None` mid-enumeration, then `hasMore: false`
with `exhaustionReason: "no_more_results"` at the end. This is the one field that turns a TAM from
an estimate into a sum of proven-complete slices.

**`--limit` is 1–500 and defaults to 20.** The default does not change what you spend — quota is
per row — but it multiplies your call count 25×.

**The iterator is forward-only and non-replayable.** From the help: *"There is no cursor - the
iterator position is server-side and cannot be replayed."* So a dropped page is paid-for data that
must be paid for again. Persist on arrival.

**`quota_exceeded` is terminal on both `create` and `run`** — documented as "Do not retry."

## Row shape (companies)

Twelve fields, observed live:

```
name  domain  industry  country  location  description  linkedin_url
size                          ← a BAND string, not a number
annual_revenue                ← a BAND string
total_funding_amount_range_usd ← a BAND string
type
clay_company_id
```

**No exact headcount.** An ICP that needs one requires an enrichment call per surviving row, in
credits, on top of the search rows — and the enrichment arms disagree with each other on headcount
by wide margins (see `account-health-audit`'s reference). For a TAM, filter on the band and do not
promise a number.

## Grammar facts that change what an ICP can say

- **Aggregates are filters, not projections** (companies queries only):
  `people.count(predicate) >= N`, `people.exists(predicate)`, `jobs.count(predicate) >= N`,
  `jobs.exists(predicate)`. So "companies with ≥5 current engineers" is a free ICP criterion —
  but the count cannot be read out, only filtered on. `.count(...)` requires a trailing
  comparison; `.exists(...)` takes none. Aggregates do not nest (the one exception the grammar
  names is `person.education.any(...)`).
- **Low-coverage fields silently shrink the population.** The grammar names `ai_business_types`
  and requires an `is_null` fallback in the same logical block:
  `(ai_business_types contains "B2B" or ai_business_types is_null)`. Omit it and every record
  whose sparse field was never populated is excluded — a sparse field becomes a smaller market.
  Including the fallback is the recall-preserving default.
- Two modes exist: `query-mode` (advanced query string, the default recommendation) and
  `filters-mode` (JSON filters, for existing filters-mode searches). Discover filters-mode fields
  with `clay search filters-mode fields --source-type <type>`.
