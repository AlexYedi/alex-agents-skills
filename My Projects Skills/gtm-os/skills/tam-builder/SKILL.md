---
name: tam-builder
description: |
  Enumerate a total addressable market from an ICP definition and report how much of it you
  can prove you have — a population figure with a per-slice coverage receipt, not a list of
  whatever fitted in one search. It partitions the ICP into disjoint slices, enumerates each
  to exhaustion, and marks every slice exhausted or truncated, so the TAM is stated exact
  where it is exact and a lower bound where it is not. Use whenever someone asks: how big is
  our TAM, size this market, enumerate every company matching our ICP, how many accounts are
  addressable, or build the full target-account universe. Do NOT use it to build a working
  prospect list of companies plus buyers (build-prospect-list), to source local businesses by
  place (source-local-businesses), to enrich a list you already have (enrich-account-list), or
  to audit stored fields (account-health-audit). Search results meter against a yearly
  workspace allowance, not credits, and the quote states both.
category: build-lists
personas: [revops, founder]
mechanism: functions
touches: read-only
keywords: []
---

# TAM builder (enumerate, then prove coverage)

The insight: **a TAM is a coverage claim, and the surface will not sell you one — it sells
rows.** The two things a market size actually needs are a population count and a reliable
identity, and neither exists here:

- **Count-mode queries are forbidden.** The search grammar's own policy is "never use
  count-mode clauses" and "never include `limit` clauses". You cannot ask how many companies
  match an ICP. The only way to a number is to enumerate the population and count what
  arrived, which is metered.
- **The obvious identity key is polluted.** Verified live: a query for one well-known payment
  processor's domain returned **33 organizations, all carrying that domain**, with 28 distinct
  company ids — micro-businesses and creators whose company page lists a payment link as their
  website, one of them claiming 10,001+ employees. So `domain` is a *claimed attribute*, not a
  key. Deduping a TAM by domain merges unrelated companies; keeping every id keeps the junk.

What the surface *does* give you is the one thing that makes an honest TAM possible: when a
search stops, **`exhaustionReason` says why** — `no_more_results` (you have every matching
record) or `query_limit` (something stopped you first). That is a per-slice **proof of
completeness**, not an estimate. So the whole design follows:

**Partition the ICP into disjoint slices, enumerate each to exhaustion, and report the TAM as a
sum of proven-complete slices plus explicitly-declared lower bounds.** A slice that ends in
`query_limit` has not told you the market is smaller — it has told you your plan stopped
counting.

And the failure this prevents: one broad search returns 500 rows, someone writes "TAM: 500" on
a slide, and the number is the per-request cap wearing a market's clothes.

## Declared inputs

**Nothing here ships with a value.** Each one is the installer's, not the author's: ask for it, never
substitute a plausible default, and where an answer does not exist say which step becomes unavailable
rather than guessing. Where a default IS defensible it is named below, and using it means saying so in
the output.

| Input | What the installer supplies | If it is missing |
|---|---|---|
| **The ICP dimensions** | industry, headcount band and HQ country are required; revenue band and tech or signal criteria as applicable | **stop rather than defaulting.** Mid-build ICP changes are the largest source of re-work here, and they waste an allowance that does not refill until the period turns |
| **Which dimensions are required versus nice-to-have** | the split | their call — it decides what filters and what merely scores |
| **The plan's search limits** | read at the start of every build | not an input they supply so much as one they must confirm: the limits are plan-dependent, and the plan changes the design rather than only the budget |

**If an answer sheet is present beside this skill, load it and ask only for what it does not cover.**
A partial sheet is normal; a value it is missing gets asked for on its own rather than restarting the
interview. **Say which values came from the sheet** before using them — a sheet applied silently is a
wrong field nobody catches. **If there is no sheet, say nothing about sheets** — the check is a file
lookup, not a question, so run the interview as though the feature did not exist rather than reporting
an absence. At delivery, offer to save the answers back (identifiers only — never a token or a
password), private and never published — and phrase the offer so it explains itself: *"want me to save
your answers to a file, so the next person on your team doesn't have to answer these again?"*

## What this skill touches

- **Reads** — the ICP dimensions you define, against Clay's company search index.
- **Writes** — nothing. The deliverable is handed back to you.
- **Never** — writes to a CRM, or reports a market size beyond what the search actually returned.

## Step 0 — Verify Clay, and read the plan before designing anything

Run `clay whoami; echo "exit_code=$?"`. If it fails, run the Clay plugin's `setup` skill and
re-run. Tell the user which workspace they're in.

Then read the limits, because **the plan changes the design, not just the budget**:

```
clay search --help          # per-request / per-search / period caps for this plan tier
                            # what those limits mean for the design, and what the surface
                            # will NOT tell you: `references/search-surface.md`
```

| Plan | Per request | Per search | Period allowance |
|---|---|---|---|
| Free | 50 | **50 — a hard stop** | 100 / month |
| Trial | 50 | 50 | 10,000 for the trial |
| Paid | 500 | — | 1,000,000 / year |
| Enterprise | 500 | — | 10,000,000 / year |

**On Free, a single search cannot exceed 50 results at all**, so slices must be small enough to
finish inside 50 rows or the TAM is a floor with no way to raise it. Say this before designing
the partition; do not design a 500-per-slice plan and discover the ceiling mid-run.

The live remaining allowance rides on a page as `periodQuota`
(`limit` / `used` / `remaining` / `resetsAt`). **It is optional in the published schema — only
`data`, `has_more` and `source_type` are required — so read it defensively.** A build that
dereferences it unconditionally gets nothing on the page that omits it. Read it when it is there and
quote against it.

## Step 1 — Lock the ICP in testable criteria (interview; do not guess)

Per the KB spine's stage 0, and for the same reason: **mid-build ICP changes are the largest
source of re-work**, and here they also waste allowance that does not come back until January.

| Dimension | Operator | Value | Required? |
|---|---|---|---|
| Industry | IN | … | required |
| Headcount band | BETWEEN | … | required |
| HQ country | IN | … | required |
| Revenue band | ≥ | … | nice-to-have |
| Tech / signal criteria | HAS / WITHIN | … | as applicable |

Two grammar facts that change what you can ask for:

- **Aggregates are filters, not projections.** `people.count(is_current = true and job_title
  is_similar_to ("Engineer")) >= 5` filters companies by their headcount *in a role* — a rich
  ICP criterion available at no extra cost. But you cannot read the count out; only filter on
  it. Do not nest aggregates inside aggregates.
- **A filter on a low-coverage field silently shrinks the TAM.** The grammar names
  `ai_business_types` as low-coverage and requires an `is_null` fallback in the same logical
  block — `(ai_business_types contains "B2B" or ai_business_types is_null)`. Without the
  fallback, every record where the field was never populated is excluded, and a *sparse field*
  becomes a *smaller market*. Adding the fallback is the recall-preserving default; removing it
  is a deliberate tightening the user asks for.

## Step 2 — Partition into DISJOINT slices

The partition is the whole method. Slice on a dimension whose values cannot overlap, so that
every matching company falls in exactly one slice and the slice counts are summable:

- **Good partition keys**: HQ country, headcount band, industry (where the taxonomy is a single
  value per company), founding-year range.
- **Bad partition keys**: anything semantic or multi-valued — keyword matches, descriptions,
  products, `is_similar_to` predicates. Two such slices overlap, and overlap is not just
  double-counted, it is **double-metered against an allowance that resets in January**.

Size each slice so it can plausibly finish under the per-search ceiling. When a slice turns out
not to, step 4 subdivides it — the partition is iterative, and that is expected rather than a
failure.

**Disjointness by construction, never by dedupe-after.** You cannot fix an overlapping
partition after the fact: the rows are already paid for, and the identity field you would
dedupe on is the polluted one (see step 5).

## Step 3 — Quote in BOTH currencies, then get approval

```
search rows  = Σ (expected rows per slice)          ← metered against the PERIOD allowance
credits      = Σ (per-row cost of any validation or enrichment) × surviving rows
```

**These are different currencies and a quote naming only credits reports the discovery half as
free.** Search results draw on a yearly workspace allowance that resets on 1 January; credits
are separate. State both, state `periodQuota.remaining` alongside the search-row figure, and
note that enumeration spend is not recoverable if the ICP changes afterwards.

Note also what search returns and what it does not: rows carry `name`, `domain`, `industry`,
`country`, `location`, `size` **as a band**, `annual_revenue` as a band, `type`,
`total_funding_amount_range_usd`, `linkedin_url`, `description`, `clay_company_id`. There is
**no exact headcount** — if the ICP needs one, that is an enrichment call per row, in credits,
on top.

## Step 4 — Enumerate each slice to exhaustion

Per slice: `create` the search, then `run` repeatedly while `hasMore` is true, with `--limit`
set explicitly (1–500; **the default is 20**, so leaving it unset multiplies your call count
without changing what you spend).

Three rules, and the first is operational rather than analytical:

1. **Persist every page the moment it arrives.** The iterator is forward-only, server-side, and
   **cannot be replayed** — there is no cursor. A page you drop is data you have already paid
   for and must pay for again. Write each page to disk before requesting the next.
2. **Stop on `quota_exceeded` and do not retry.** Both `create` and `run` document it as
   terminal. Report how far the enumeration got, per slice.
3. **Read `exhaustionReason` when `hasMore` goes false**, and record it against the slice. This
   is the measurement; the rows are just the by-product.

## Step 5 — Resolve identity WITHOUT the domain field

Verified: 33 organizations in the search dataset share one payment processor's domain, with 28
distinct company ids among them. So:

- **Never dedupe a TAM on `domain`.** It merges unrelated organizations, and the more popular
  the platform whose URL got pasted, the worse the collapse.
- **Never treat one `domain` as one company** when counting. The count is of records, and
  records-per-domain is not one.
- **`clay_company_id` distinguishes records but does not identify companies** — 28 ids on a
  polluted domain are 28 different organizations, not 28 duplicates of one. Deduping on id
  keeps the junk; deduping on domain destroys the signal.
- The honest move at TAM scale is to **flag domain collisions rather than resolve them**:
  report how many records share a domain with other records, treat those records as
  `identity_unresolved`, and exclude them from the headline figure while listing them. A
  cheap tell for the specific pollution above: a domain shared by many records whose names,
  countries and size bands are unrelated is a pasted-link artifact, not a corporate family.

## Step 6 — Grade coverage, per slice then overall

Per slice, exactly one verdict, in this order:

1. **`exhausted`** — `hasMore` went false with `exhaustionReason: no_more_results`. Every
   matching record has been returned. This slice's count is **exact**.
2. **`truncated`** — `hasMore` went false with `exhaustionReason: query_limit`. Something
   capped the enumeration before the records ran out. **Subdivide the slice on a disjoint key
   and re-enumerate**, or declare the slice a lower bound and say which.
3. **`incomplete`** — enumeration stopped for any other reason: quota exhausted, an error, an
   abandoned run. Not a statement about the market at all.

Then the overall figure, and its status is determined, not chosen:

| Condition | TAM figure |
|---|---|
| every slice `exhausted` | **exact** — the sum is the population matching the ICP |
| any slice `truncated` or `incomplete` | **lower bound** — the sum plus "and at least this much more, unmeasured" |

The three slice verdicts are mutually exclusive by construction (`hasMore` false with one of
two reasons, or not finished), and the two overall states partition on whether any slice is
non-exhausted, so both ladders are single-valued.

**Never report a lower bound as a TAM.** "We found 2,140 accounts" and "the market is 2,140
accounts" are different claims, and only one of them is supportable when a slice hit a cap.

## Step 7 — Deliver

- **The figure, with its status** — exact or lower bound — stated in the first line.
- **The coverage receipt**: one row per slice with its criteria, rows returned, verdict, and
  for truncated slices what it was subdivided into or why it was not.
- **The list**, with `identity_unresolved` records separated out and counted, not silently
  dropped and not silently included.
- **Both spends**: search rows consumed against `periodQuota`, credits consumed on any
  validation, and the remaining allowance after.
- **What was excluded and why** — low-coverage-field fallbacks used, slices declared lower
  bounds, records held out for identity collisions.

Hand the list on: `build-prospect-list` finds the buyers at these accounts,
`account-tier-scoring` tiers them, `enrich-account-list` fills them out. This play sizes and
enumerates; it does not enrich, score or contact.

## What this skill does not claim

- Slice enumeration verified on single slices; the multi-slice partition loop and the truncation rate are unexercised.
- The truncated-result branch of the verdict ladder has never been triggered against a live response.
- People-side TAM is out of scope for this version and not claimed.

## What good looks like

- The headline number carries "exact" or "lower bound", and the reader knows which without
  asking.
- Every slice has a verdict, and a truncated slice was either subdivided or declared.
- Nobody deduped on domain.
- The quote named search rows *and* credits, and the allowance remaining was stated.
- The common failure: one broad search, 500 rows returned, "TAM = 500" — the per-request cap
  reported as a market. The second-worst: a low-coverage filter with no `is_null` fallback,
  quietly excluding every company whose sparse field was never populated.

## Rules

- MUST read the plan's limits and `periodQuota` before designing the partition; NEVER design a
  slice plan that the plan tier cannot execute.
- MUST partition on disjoint, single-valued keys; NEVER partition on semantic or multi-valued
  predicates, and never fix an overlapping partition by deduping afterwards.
- MUST record `exhaustionReason` per slice and grade it; NEVER treat `query_limit` as evidence
  the market is small.
- MUST report the TAM as a lower bound whenever any slice is truncated or incomplete; NEVER
  present a capped enumeration as a population.
- MUST persist each page on arrival; the iterator is forward-only and non-replayable, and a
  dropped page is paid data lost.
- MUST include an `is_null` fallback when filtering a low-coverage field, or state that it was
  deliberately omitted to tighten the search.
- MUST quote search rows AND credits as separate currencies, with the remaining period
  allowance; NEVER quote credits alone.
- NEVER dedupe or count on `domain`, and never treat one domain as one company.
- NEVER use count-mode or `limit` clauses in a query — the grammar forbids both.
- MUST stop on `quota_exceeded` and report progress; NEVER retry it.

## Worked example

ICP: software companies, 50–2,000 headcount band, HQ in US / CA / UK. The workspace is on a
paid tier — 500 per request, 1,000,000 per year — and `periodQuota` reports 964,000 remaining.

Partition on the two disjoint keys the ICP already names: 3 countries × 3 headcount bands =
**9 slices**, each expected in the hundreds. Cost quote: **~2,600 search rows** against 964,000
remaining, plus **0 credits** because no enrichment is requested — and the quote says so
explicitly rather than omitting the credit line.

Eight slices end `hasMore: false` with `no_more_results` → `exhausted`, exact counts. The ninth
— US, largest band — ends with `query_limit` at 500 → `truncated`. It is subdivided on a third
disjoint key (founding-year range) into three sub-slices; two exhaust, one truncates again and
is declared a lower bound rather than subdivided a third time, because the user's budget for
this run is spent and saying so is better than spending more without asking.

Identity: 47 records share a domain with at least one other record. Sixteen of those are
clearly one corporate family; 31 carry a payment-platform domain alongside unrelated names,
countries and size bands, and are held out as `identity_unresolved`.

Delivered: **"At least 2,412 accounts match this ICP — a lower bound. 8 of 9 slices are
exhaustively enumerated; one is capped."** Then the nine-row coverage receipt, the 31 held-out
records listed, 2,459 search rows consumed with 961,541 remaining, and 0 credits.
