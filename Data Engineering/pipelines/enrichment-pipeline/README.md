# Enrichment Pipeline

End-to-end B2B data enrichment bundle covering contact discovery, company intelligence, technographics, intent signals, validation, and CRM/CDP delivery. Built to orchestrate 150+ providers via cost-aware waterfalls with governed quality and compliance.

## When to Use This Bundle

- Running multi-provider enrichment waterfalls (single record or bulk)
- Building or tuning provider sequences for a specific GTM motion
- Auditing provider performance, credit spend, or data quality
- Normalizing enriched data into CRM / CDP / warehouse with identity resolution
- Building firmographic dossiers or contact packages for outreach

If your goal is broader integration architecture (event vs batch, CQRS, message queues) rather than enrichment specifically, see `architecture/integration-patterns/`. If your goal is governance/MDM/policy around the enriched data, see `governance-and-quality/mdm-and-federated-governance/`.

## Bundle Structure

```
enrichment-pipeline/
├── README.md                 (you are here)
├── config/
│   └── providers.yaml        ← 150+ providers with costs, SLAs, coverage notes
├── agents/                   ← personas the lead orchestrator delegates to
│   ├── enrichment-expert.md      (lead — scopes work, delegates, aggregates)
│   ├── signal-integrator.md      (provider APIs, normalization, delivery)
│   ├── provider-ops-lead.md      (rosters, SLAs, credit budgets, failover)
│   ├── data-quality-steward.md   (validation, freshness, compliance)
│   ├── company-analyst.md        (firmographic dossiers, buying triggers)
│   └── data-specialist.md        (decision-maker discovery, contact validation)
├── commands/                 ← invokable slash commands
│   ├── run-waterfall-enrichment.md   (the workhorse — single or bulk)
│   ├── enrich-leads.md               (targeted single-record enrichment)
│   ├── append-data.md                (bulk attribute fill on existing list)
│   ├── clean-database.md             (dedup + validate + suppress)
│   ├── normalize-signals.md          (identity resolution + tagging)
│   └── audit-provider-health.md      (provider performance review)
└── skills/                   ← reusable design + analysis playbooks
    ├── waterfall-blueprint/      (provider sequences, credit policies)
    ├── identity-resolution/      (cross-source matching rules)
    ├── provider-scorecard/       (success / cost / latency tracking)
    ├── signal-taxonomy/          (schema + topic tags + lineage)
    ├── validation-rulebook/      (QA rules before activation)
    └── firmographic-analysis/    (interpreting enriched company data)
```

## How to Invoke

| Goal | Start with |
|---|---|
| "Enrich these leads end-to-end" | `enrichment-expert` agent (it orchestrates the rest) |
| Run a known waterfall | `/enrichment-pipeline:run-waterfall-enrichment` |
| Single targeted lookup | `/enrichment-pipeline:enrich-leads` |
| Fill missing attributes on a list | `/enrichment-pipeline:append-data` |
| Pre-CRM dedup + validation | `/enrichment-pipeline:clean-database` |
| CRM/CDP normalization step | `/enrichment-pipeline:normalize-signals` |
| Vendor performance review | `/enrichment-pipeline:audit-provider-health` |
| Design or tune a waterfall | `waterfall-blueprint` skill |
| Analyze enriched companies for GTM | `firmographic-analysis` skill |

## Compliance Defaults

All workflows assume GDPR / CCPA scope and require:
- Lawful basis tracked per record
- Opt-out / deletion respected
- Audit logs retained per retention policy
- Provider compliance verified before inclusion in `providers.yaml`

The `data-quality-steward` agent owns enforcement. If it flags a compliance issue, the run **halts** — do not silently bypass.

## Operational Notes

- **Caching** — defaults: email 30d, phone 60d, company 90d, intent 7d (always refresh)
- **Credit budgets** — set per command via `--max-credits`; exceeding triggers an alert via `provider-scorecard`
- **Provider catalog** — `config/providers.yaml` is the source of truth for cost / SLA / coverage; update there, not in skill docs

## Cross-references

- `architecture/integration-patterns/` — APIs vs events vs batch for moving the enriched data
- `architecture/dataops-and-platforms/` — where this bundle sits in a Modern Data Stack / Live Data Stack
- `governance-and-quality/mdm-and-federated-governance/` — data contracts, ABAC, and the enriched data's downstream contracts
- `governance-and-quality/data-quality-auditor/` — broader quality auditing for any dataset (not just enrichment)

## Open TODOs

- `config/providers.yaml` schema is undocumented — add a header section describing the fields, expected types, and update process.
- Cross-skill *chaining* (programmatic invocation between agents/skills) is deferred to a future iteration; today, chaining is documented in agent prompts and the lead orchestrator routes manually.
