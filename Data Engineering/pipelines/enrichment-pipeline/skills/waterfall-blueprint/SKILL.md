---
name: waterfall-blueprint
description: Design provider sequences, throttling logic, and credit policies for enrichment waterfalls across 150+ B2B data sources. Use when building or tuning waterfall sequences, selecting provider stacks per enrichment type, or auditing credit consumption.
---

# Waterfall Blueprint Skill

## When to Use

- Building contact/company/intent enrichment workflows across multiple providers
- Updating fallback rules after provider outages or cost shifts
- Selecting provider stacks for email, phone, company, or intent enrichment
- Auditing credit consumption or routing logic
- Documenting waterfall logic for RevOps + engineering handoffs

## Framework

Five-step design loop:

1. **Goal & constraints** — enrichment type, required fields, credit ceiling, SLA, compliance scope
2. **Provider catalog** — eligible providers with success %, latency, cost, regional/industry coverage
3. **Routing logic** — sequence, branching by available input, retry intervals, stop conditions
4. **Safeguards** — throttles, dedupe, cache TTLs, exception triggers, compliance gates
5. **Versioning** — change log with owner, rationale, effective date, A/B test results

## Core Principles

1. **Quality–cost balance** — optimize for highest data quality within budget; do not chase tail credits
2. **Smart routing** — pick providers based on input type and success probability, not alphabetic order
3. **Sequential failover** — try cheapest-likely-to-win first, escalate only on miss
4. **Cache aggressively** — most-recently-enriched records dominate API spend; cache before you call
5. **Bulk where possible** — batch similar records for volume discounts (Apollo, ZoomInfo, etc.)

## Provider Selection Matrix

### Email Discovery — pick by available input

| Input you have | Best sequence |
|---|---|
| LinkedIn URL | ContactOut → RocketReach → Apollo |
| Name + Company | Apollo → Hunter → RocketReach → FindyMail |
| Domain only | Hunter → Apollo → Clearbit |
| Email (validate) | ZeroBounce → NeverBounce → Debounce |

**Quality tiers:**
- Premium (90%+ success): ZoomInfo, BetterContact waterfall
- Standard (75%+ success): Apollo, Hunter, RocketReach
- Budget (60%+ success): Snov.io, Prospeo, ContactOut

### Company Intelligence — pick by data type

| Data type | Sequence |
|---|---|
| Basic firmographics | Clearbit → Ocean.io → Apollo |
| Financial / funding | Crunchbase → PitchBook → Dealroom |
| Tech stack | BuiltWith → HG Insights → Clearbit |
| Intent signals | B2D AI → ZoomInfo Intent → 6sense |
| News / social | Google News → social platforms → Owler |

### Industry specialization

| Industry | Primary | Secondary |
|---|---|---|
| SaaS / Tech | Apollo, Clearbit, BuiltWith | ZoomInfo, HG Insights, G2, 6sense |
| Financial Services | PitchBook, ZoomInfo | LexisNexis, D&B, Bloomberg |
| Healthcare | Definitive Healthcare | NPPES, ZoomInfo (healthcare filters) |
| E-commerce | Store Leads, BuiltWith | Shopify data, Clearbit |
| Startups | Crunchbase, Dealroom, AngelList | Owler |

## Credit Cost Tiers

```
Tier 0 (free)        Native ops, cached data, manual inputs
Tier 1 (0.5 cr)      Validation, verification, basic lookups
Tier 2 (1–2 cr)      Standard enrichments (Apollo, Hunter, Clearbit)
Tier 3 (2–3 cr)      Premium data (ZoomInfo, technographics, intent)
Tier 4 (3–5 cr)      Enterprise intelligence (PitchBook, custom AI)
Tier 5 (5–10 cr)     Specialized services (deep AI research)
```

## Three Reference Waterfall Profiles

### Maximum Success
```yaml
priority: success_rate
sequence:
  - BetterContact          # aggregates 10+ sources
  - ZoomInfo               # if enterprise
  - Apollo + Hunter + RocketReach
  - AI web research
expected_success: 95%+
avg_cost: 8–12 credits
```

### Balanced
```yaml
priority: success_with_reasonable_cost
sequence:
  - Apollo
  - Hunter (if domain match)
  - RocketReach (if name match)
  - stop_on_confidence: 0.85
expected_success: 80%
avg_cost: 3–5 credits
```

### Budget
```yaml
priority: minimize_cost
sequence:
  - cache_check
  - Hunter (domain only)
  - free_sources (Google, public LinkedIn)
  - stop_on_first_result
expected_success: 60%
avg_cost: 1–2 credits
```

## Optimization Tactics

### Cache TTL defaults
- Email: 30 days; refresh on bounce
- Phone: 60 days; refresh on validation failure
- Company: 90 days; refresh on funding / acquisition / IPO
- Intent: 7 days; always refresh on read
- Static metadata: indefinite

### Batch processing
```python
if record_count > 1000:
    use_provider("apollo_bulk")     # 10–30% volume discount
elif record_count > 100:
    use_parallel_processing()
else:
    use_standard_processing()
```

### Smart waterfall pattern
```python
waterfall = [
    {"provider": "cache",         "credits": 0},
    {"provider": "apollo",        "credits": 1.5, "stop_on_success": True},
    {"provider": "hunter",        "credits": 1.2, "stop_on_success": True},
    {"provider": "bettercontact", "credits": 3,   "stop_on_success": True},
    {"provider": "ai_research",   "credits": 5,   "last_resort": True},
]
```

### Progressive enrichment by lifecycle stage
```python
def progressive_enrichment(lead):
    if lead.stage == "new":          # cheap base data on import
        return basic_enrichment(lead)        # 1–2 credits
    if lead.stage == "engaged":      # expand on email open
        return standard_enrichment(lead)     # 3–5 credits
    if lead.stage == "qualified":    # comprehensive on meeting booked
        return comprehensive_enrichment(lead) # 10+ credits
```

### Hybrid AI + provider
```python
def hybrid_enrichment(company):
    base = clearbit_lookup(company)
    if not base.get("description"):
        base["description"] = ai_generate_description(company)
    if is_enterprise_account(base):
        base.update(zoominfo_enrich(company))
    return base
```

## Provider-Specific Notes

| Provider | Strengths | Weaknesses | Tip |
|---|---|---|---|
| Apollo.io | US B2B, LinkedIn data, phone numbers | International, personal email | Use bulk API for ~10% discount |
| ZoomInfo | Enterprise data, org charts, intent | Expensive, weak SMB | Reserve for high-value accounts |
| Hunter | Domain searches, email patterns, API reliability | Phone, deep contact info | Best for initial domain exploration |
| Clearbit | Real-time API, company data, speed | Email discovery rates | Pair with contact provider |
| BuiltWith | Technology detection, historical data | Contact info, financials | Filter accounts before enrichment |

## Quality Scoring

```python
def calculate_data_quality_score(data, sources):
    score = 0
    # Multi-source validation (30 pts)
    if len(sources) > 1:
        score += min(len(sources) * 10, 30)
    # Completeness (40 pts — 10 each)
    for field in ("email", "phone", "title", "company"):
        if data.get(field):
            score += 10
    # Verification (20 pts)
    if data.get("email_verified"): score += 10
    if data.get("phone_verified"): score += 10
    # Recency (20 pts)
    days_old = get_data_age(data)
    if days_old < 30:   score += 20
    elif days_old < 90: score += 10
    return score
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Low email discovery | Wrong waterfall for input | Check pattern with Hunter; try AI for execs |
| High credit burn | Cache miss / wrong sequence | Audit TTL, raise cache hit floor |
| Poor data quality | No verification / single source | Add ZeroBounce; require 2+ source agreement |
| Provider outage | Single-vendor dependency | Add failover; check `provider-scorecard` |

## Templates

- **Provider cheat sheet**: `references/provider_cheat_sheet.md`
- **Cost calculator**: `scripts/cost_calculator.py`
- **Waterfall diagram**: sequence, inputs, outputs, fallback paths
- **Routing table**: provider, criteria, cost, notes
- **Change log**: owner, rationale, effective date, A/B test results

## Reference integration code

```javascript
const enrichContact = async (name, company) => {
  const cached = await checkCache(name, company);
  if (cached) return cached;

  for (const provider of ['apollo', 'hunter', 'rocketreach']) {
    try {
      const result = await callProvider(provider, { name, company });
      if (result.email) {
        await saveToCache(result);
        return result;
      }
    } catch (error) {
      console.log(`${provider} failed, trying next...`);
    }
  }
  return await aiResearch(name, company);
};
```

## Tips

- **Pre-build waterfalls per motion** so GTM teams call one orchestration command instead of juggling providers
- **Instrument cache hit rates**; alert RevOps when below target — credit spikes follow cache decay
- **Rotate premium providers** quarterly to negotiate volume discounts and diversify coverage gaps
- **Pair with QA hooks** (verification APIs, sampling) before CRM sync to prevent bad-data cascades
- **Keep sequences short for real-time use cases**; reserve long chains for batch mode
- **A/B test new providers** before full rollout — `provider-scorecard` is the scoreboard

## Cross-references

- `provider-scorecard` skill — continuous routing optimization based on observed performance
- `validation-rulebook` skill — QA rules applied after waterfall completes
- `signal-taxonomy` skill — schema/taxonomy for tagging enriched records
- `run-waterfall-enrichment` command — the executor for blueprints designed here
