---
name: run-waterfall-enrichment
description: Execute multi-provider enrichment waterfalls with credit governance, failover rules, validation, and delivery targets.
usage: /enrichment-pipeline:run-waterfall-enrichment --type contact --input "Taylor Reed, Nimbus" --sequence apollo,hunter,rocketreach --max-credits 5
---

# Command: run-waterfall-enrichment

Execute multi-provider enrichment waterfalls to maximize discovery success while staying within credit budget and compliance constraints.

## Inputs

| Flag | Required | Values | Notes |
|---|---|---|---|
| `--type` | yes | `contact` \| `company` \| `email` \| `phone` \| `technographic` \| `intent` \| `full` | Enrichment surface |
| `--input` | yes | record payload, CSV path, or warehouse query | Single record or batch |
| `--sequence` | no | comma-separated provider IDs | Overrides default ops config |
| `--max-credits` | no | integer (default `10`) | Per-record ceiling; halts on overflow |
| `--validate` | no | `true` (default) \| `false` | Run validation pipeline after discovery |
| `--cache` | no | `true` (default) \| `false` | Honor cached results (TTL set per record type) |
| `--parallel` | no | `true` (default) \| `false` | Concurrent processing for batch input |
| `--delivery` | no | `crm` \| `csv` \| `warehouse` \| `json` (default) | Output target |
| `--dry-run` | no | `true` \| `false` (default) | Validate inputs and sequence without consuming credits |

## Workflow

1. **Request validation** — confirm fields, dedupe against recent runs, enforce rate limits, check compliance flags.
2. **Sequence selection** — pull provider order from `provider-ops-lead` config, adjust for `--sequence` overrides or active outages.
3. **Execution loop** — call providers in order, capture response metadata, stop on first success per field unless `--validate` requires cross-reference.
4. **Aggregation & scoring** — merge best data, attach confidence + provenance tags via `signal-taxonomy` rules.
5. **Validation** — `data-quality-steward` runs `validation-rulebook` checks; flag low-confidence records.
6. **Delivery & logging** — push to destination, append credits + latency to `provider-scorecard`, trigger alerts if thresholds exceeded.

## Default Waterfall Sequences

### Email Discovery
```
1. Cache check                    (0 credits)
2. Apollo.io                      (1–2 credits)
3. Hunter                         (1–2 credits)
4. RocketReach                    (1–2 credits)
5. People Data Labs               (1–2 credits)
6. ContactOut                     (1–2 credits)
7. BetterContact                  (2–5 credits)
8. AI web research                 (2–5 credits, last resort)

Validation: ZeroBounce → NeverBounce backup (0.5 credits each)
```

### Phone Discovery
```
1. Cache check                    (0 credits)
2. Apollo.io                      (1–2 credits)
3. RocketReach                    (1–2 credits)
4. LeadMagic                      (1–2 credits)
5. SignalHire                     (1–2 credits)
6. BetterContact Phone            (2–5 credits)

Validation: ClearoutPhone (0.5 credits) + line-type detection
```

### Company Enrichment
```
1. Clearbit                       (1–2 credits)
2. Ocean.io                       (2–3 credits)
3. ZoomInfo                       (2–3 credits, enterprise only)
4. Crunchbase                     (1–2 credits, if funded)
5. BuiltWith                      (1–2 credits, technographics)
6. HG Insights                    (2–3 credits, tech spend)
7. Intent providers               (3–5 credits, qualified accounts)
```

### Full Contact (chained)
Email waterfall → phone waterfall → social profile discovery → company enrichment → technographics → intent signals → validation & scoring.

## Provider Selection Logic

Route by available input — better signal, fewer wasted credits:

```python
def select_providers(input_type, data_available, target_quality):
    if input_type == "email":
        if has_linkedin_url(data_available):
            return ["contactout", "rocketreach", "apollo"]
        if has_full_name_and_company(data_available):
            return ["apollo", "hunter", "rocketreach"]
        if has_domain_only(data_available):
            return ["hunter", "apollo", "clearbit"]
        return ["people_data_labs", "bettercontact", "ai_research"]
    if input_type == "phone":
        if has_email(data_available):
            return ["apollo", "rocketreach", "leadmagic"]
        return ["bettercontact_phone", "signalhire", "lusha"]
    # ... see waterfall-blueprint skill for full matrix
```

Full provider matrix and tuning guidance live in `skills/waterfall-blueprint/SKILL.md`.

## Credit Optimization

```python
def optimize_provider_sequence(providers, max_credits, historical_success):
    scored = sorted(
        providers,
        key=lambda p: efficiency_score(
            success_rate=historical_success[p],
            credit_cost=PROVIDER_COSTS[p],
            data_quality=PROVIDER_QUALITY[p],
        ),
        reverse=True,
    )
    sequence, remaining = [], max_credits
    for p in scored:
        if PROVIDER_COSTS[p] <= remaining:
            sequence.append(p)
            remaining -= PROVIDER_COSTS[p]
    return sequence
```

## Examples

```bash
# Single record, default sequence
/enrichment-pipeline:run-waterfall-enrichment \
  --type contact \
  --input "Taylor Reed, Nimbus"

# Bulk email enrichment with strict budget
/enrichment-pipeline:run-waterfall-enrichment \
  --type email \
  --input "prospects.csv" \
  --max-credits 5 \
  --validate true

# Custom sequence into Salesforce
/enrichment-pipeline:run-waterfall-enrichment \
  --type full \
  --input "target_accounts.csv" \
  --sequence "clearbit,apollo,hunter,zoominfo" \
  --max-credits 20 \
  --delivery crm

# Validate plan before spending
/enrichment-pipeline:run-waterfall-enrichment \
  --type company \
  --input "acme.com" \
  --dry-run true
```

## Output Schemas

### JSON (default)
```json
{
  "input": { "name": "Taylor Reed", "company": "Nimbus" },
  "results": {
    "email": "taylor@nimbus.com",
    "email_confidence": 95,
    "email_deliverable": true,
    "phone": "+1-555-0123",
    "phone_type": "mobile",
    "linkedin": "linkedin.com/in/taylorreed",
    "providers_used": ["apollo", "zerobounce"],
    "credits_used": 2.5
  },
  "metadata": {
    "enriched_at": "2026-05-06T10:30:00Z",
    "cache_hit": false,
    "processing_time_ms": 1200
  }
}
```

### CSV
```csv
name,company,email,email_confidence,phone,phone_type,linkedin,credits_used
Taylor Reed,Nimbus,taylor@nimbus.com,95,+1-555-0123,mobile,linkedin.com/in/taylorreed,2.5
```

### Salesforce Lead payload
```json
{
  "Lead": {
    "FirstName": "Taylor",
    "LastName": "Reed",
    "Company": "Nimbus",
    "Email": "taylor@nimbus.com",
    "Phone": "+1-555-0123",
    "LinkedIn__c": "linkedin.com/in/taylorreed",
    "Enrichment_Score__c": 95,
    "Last_Enriched__c": "2026-05-06T10:30:00Z"
  }
}
```

## Caching Policy

| Record Type | TTL | Refresh Trigger |
|---|---|---|
| email | 30 days | Bounce reported |
| phone | 60 days | Validation failure |
| company | 90 days | Funding / acquisition / IPO event |
| intent | 7 days | Always refresh on read |

## Error Handling

| Error | Action |
|---|---|
| Rate limit | Exponential backoff; reschedule |
| Auth failure | Alert ops; skip provider |
| Data not found | Continue to next provider |
| Generic error | Retry once; then skip |
| Compliance flag | **Halt run**; escalate to `data-quality-steward` |

## Agent / Skill Invocations

- `provider-ops-lead` — supplies sequence + credit policy
- `signal-integrator` — handles normalization + delivery
- `data-quality-steward` — validates results before release
- `waterfall-blueprint` skill — sequencing template
- `provider-scorecard` skill — logs performance + cost metrics
- `validation-rulebook` skill — QA checks
