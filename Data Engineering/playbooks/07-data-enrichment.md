# Playbook 07 — Data Enrichment

End-to-end chain for enriching contacts, accounts, or building intelligence dossiers via the `enrichment-pipeline` bundle. The bundle has a lead orchestrator agent — this playbook describes the chain that wraps it.

## When to Use

- "Enrich [these leads / contacts / accounts]"
- "Find emails for [list]"
- "Build account intelligence on [target]"
- "Add firmographics / technographics / intent to [dataset]"
- Bulk data fill on an existing CSV/CRM list

## When to Skip

- You already designed the waterfall — go direct to `/enrichment-pipeline:run-waterfall-enrichment`
- You only need to look up *what a single provider does* — read `pipelines/enrichment-pipeline/references/providers-catalog.md`
- The task is single-record lookup with default sequence — `/enrichment-pipeline:enrich-leads`

## Sequence

| Step | Skill / agent / command | Output |
|---|---|---|
| 1 | `architecture/integration-patterns` | Delivery shape: sync vs async, batch vs CDC, where the enriched data lands (CRM / CDP / warehouse) |
| 2 | **`pipelines/enrichment-pipeline/agents/enrichment-expert`** | Lead orchestrator scopes the request and delegates to specialists below |
| 3 | `pipelines/enrichment-pipeline/skills/waterfall-blueprint` | Designed waterfall: provider sequence, credit budget, branching by available input |
| 4 | `pipelines/enrichment-pipeline/commands/run-waterfall-enrichment` | Execution — delegated by the lead to provider-ops-lead + signal-integrator agents |
| 5 | `pipelines/enrichment-pipeline/skills/validation-rulebook` | Validation rules applied by data-quality-steward agent before delivery |
| 6 | `governance-and-quality/data-quality-auditor` | Post-run audit: confirm delivered data meets quality bar |

## Specialist Roles (already wired into step 2 lead delegation)

| Specialist | Owns | Invoked at step |
|---|---|---|
| `signal-integrator` | Provider APIs, normalization, delivery | 4 |
| `provider-ops-lead` | Sequence, credit budget, failover | 3, 4 |
| `data-quality-steward` | Validation rules, freshness, compliance | 5 |
| `company-analyst` | Firmographic dossiers (if enrichment includes account intelligence) | 4–5 |
| `data-specialist` | Decision-maker discovery (if enrichment includes contacts) | 4 |

## Decision Points

- **Single record vs bulk** (step 4): use `enrich-leads` for single records, `run-waterfall-enrichment` for bulk. The bundle supports both.
- **Pre-defined sequence vs design new** (step 3): if a known motion exists ("ICP outbound enrichment"), use the existing waterfall. Design a new one only when the motion is genuinely new.
- **Strict budget vs quality-first** (step 3): cost-conscious / balanced / quality-first profiles documented in `waterfall-blueprint/SKILL.md`. Default is balanced.
- **Skip the post-audit?** (step 6): only if the volume is small and manually reviewable. Otherwise the audit catches the silent quality regressions.

## Compliance Reminder

`data-quality-steward` halts the run if it flags GDPR / CCPA risk. Do not bypass — escalate and fix the lawful-basis gap, then resume.

## References

- `pipelines/enrichment-pipeline/README.md` — bundle overview
- `pipelines/enrichment-pipeline/references/providers-catalog.md` — 150+ provider catalog (capabilities, costs, success rates)
- `pipelines/enrichment-pipeline/skills/waterfall-blueprint/references/provider_cheat_sheet.md`

## Cross-folder pointers (optional)

- `architecture/dataops-and-platforms` — if the enrichment is part of a recurring pipeline rather than one-off

## Bypass Phrases

*"Use my existing waterfall"* / *"Skip step 1 — I have the delivery shape"* / *"Skip the post-audit"*.
