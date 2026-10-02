# Clay workflow build: Case-Study Lookalikes

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

**This is the playbook where a workflow beats a table most clearly**, because the whole thing is a
loop with a decomposition step, a search step and a judge — none of which fit the one-row-at-a-time
column model.

Relevant catalog actions:

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | "\(.packageId)\t\(.actionKey)"' \
  | grep -iE 'lookalike|enrich-company|scrape-website'
# e251a70e...  find-people-lookalikes
# e5f3b09f...  enrich-company
# 4299091f...  scrape-website
```

Also useful: `clay search` and `clay audiences` from the CLI, for the discovery half.

## Two workflows, not one

| Workflow | Runs | Input | Output |
|---|---|---|---|
| **A — decompose** | **once per case study** | case study text, company profile, offer summary | the attribute card |
| **B — judge** | **once per company** | attribute card + one company | qualified, ref, reason |

⚠️ **Do not fold A into B.** A runs once and B runs thousands of times; merging them means paying for
the decomposition on every row and, worse, letting the attribute card drift row to row so your
segment is no longer one segment.

## Workflow A — decompose

```
[1 trigger: case_study_text, case_study_domain, offer_summary]
   -> [2 tool: look up the case-study company's own record]
   -> [3 agent: prompt A]
   -> [4 code: shape the attribute card + emit the enum candidates to bake off]
```

Node 4 should return the candidates **explicitly**, because the bake-off is a human step:

```python
def run(card, db_industry):
    cands = list(card.get("industry_enum_candidates") or [])
    # The database's own tag on the case-study company is a CANDIDATE, never the
    # answer. One marketing-software vendor is tagged "Advertising Services" --
    # which is the bucket the AGENCIES live in, and exactly the bucket that made
    # the naive lookalike arm score 40% usable.
    if db_industry and db_industry not in cands:
        cands.append(db_industry)
    return {
        "attribute_card": card,
        "bake_off_candidates": cands,
        "next_step": "Run the step-3 search once per candidate with only the enum "
                     "swapped. Keep the one whose first 10 results are the right TYPE "
                     "of company. Record the rejects and why.",
    }
```

The bake-off itself is free — a page-1 total count costs nothing — and you run it from the shell:

```bash
for enum in "Software Development" "Advertising Services" "Marketing Services"; do
  echo "== $enum"
  # same search body, only company_industry.include swapped, read total_count
done
```

## Workflow B — judge

```
[1 trigger: attribute_card + domain + company_name + description]
   -> [2 tool: enrich-company]        only when no description came in
   -> [3 agent: prompt B]
   -> [4 tool: scrape-website]        LIVENESS, only on qualified rows
   -> [5 code: final gate + contract]
```

### Node 2 — the description

Use a **free** company-enrichment action. You are feeding a text judge, not building a profile, and a
high-credit company lookup per row is how a widening pass stops being cheap.

### Node 3 — the judge

Prompt B byte-identical as the system message, JSON mode, cap 300, no `temperature`. Route on a
description existing — **a thin description is `qualified: false` anyway, so paying to judge one is
pure waste.**

### Node 4 — liveness

**The verification this playbook actually needs.** Company databases happily describe companies that
no longer trade, and a description-only judge qualifies them confidently.

Route it on `qualified == true` only, so you fetch homepages for the small qualified set rather than
the whole pull.

### Node 5 — the final gate

```python
DEAD_MARKERS = ("domain is for sale", "buy this domain", "parked", "coming soon",
                "under construction", "account suspended", "this site can’t be reached")

def run(judge, site, card):
    j = judge or {}
    qualified = bool(j.get("qualified"))
    ref = (j.get("case_study_ref") or "") if qualified else ""

    text = ((site or {}).get("content") or "").lower()
    live = bool(text) and len(text) > 400 and not any(m in text for m in DEAD_MARKERS)

    # qualified and case_study_ref ALWAYS agree. A false never carries a ref.
    ok = qualified and bool(ref) and live
    return {
        "qualified":               ok,
        "case_study_ref":          ref if ok else "",
        # The descriptor, NOT the brand name. Naming a third party's brand in cold
        # copy is a client-facing decision; the descriptor carries the same
        # recognition and never creates a permissions problem.
        "lookalike_case_study_line": (card or {}).get("descriptor", "") if ok else "",
        # Internal QA text. Populated on REJECTED rows too, so it must never be pushed.
        "case_study_match_reason": j.get("case_study_match_reason", ""),
        "liveness":                "live" if live else "dead_or_parked",
        "confidence":              j.get("confidence", "low"),
    }
```

## Build and run

```bash
# A, once per case study
WFA=$(clay workflows create --name "Lookalikes: decompose" | jq -r '.id')
clay workflows publish "$WFA"
RTA=$(clay routines create workflow "$WFA" --name "lookalike-decompose" | jq -r '.id')
clay routines runs start "$RTA" --input '{"items":[{"case_study_domain":"attentive.com","case_study_text":"..."}]}'

# B, per company, bulk
WFB=$(clay workflows create --name "Lookalikes: judge" | jq -r '.id')
clay workflows publish "$WFB"
RTB=$(clay routines create workflow "$WFB" --name "lookalike-judge" | jq -r '.id')
clay routines runs start "$RTB" --bulk companies.jsonl
```

## The loop this sits inside

1. Decompose (workflow A).
2. **Bake off the industry enums by hand.** Free, and it is the step that decides everything.
3. Search **with** the lookalike anchor. Expect a small, very clean set — around 20 companies.
4. Search **without** the anchor, judge every row (workflow B). Raw precision ~70%, ~95% after the
   judge.
5. **Snowball:** re-run step 3 with each confirmed member as a new seed, union, repeat. **Stop when
   net-new drops below 2 to 3% per round.**

**Never skip step 4's judge to save time.** The raw 70% is exactly what makes unanchored filters
dangerous, and it is invisible until someone reads the list.

## Smoke test

| What you see | What it means |
|---|---|
| Nearly everything qualifies | the resonance reasons are not testable. "is innovative" is not a filter |
| Nearly nothing qualifies | the card is over-specified, or the industry enum is wrong |
| Agencies and publishers qualify | add exclude keywords and re-run the bake-off |
| Dead companies qualify | node 4 is not running, or is routed on the wrong branch |
| The segment never grows past ~20 | you are still anchored. Drop the anchor and lean on the judge |
| Snowball never converges | you are unioning without deduping on bare domain |
