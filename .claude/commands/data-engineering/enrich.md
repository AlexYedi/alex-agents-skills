---
description: Walk the data enrichment chain — delivery shape, lead orchestrator delegation, waterfall design, execution, validation, post-audit.
---

You are guiding a data enrichment workflow using the chain documented at `Data Engineering/playbooks/07-data-enrichment.md`.

Walk these steps in order:

1. **Delivery shape** — `Data Engineering/architecture/integration-patterns` — sync vs async, batch vs CDC, where the enriched data lands (CRM / CDP / warehouse).
2. **Engage the lead orchestrator** — `Data Engineering/pipelines/enrichment-pipeline/agents/enrichment-expert` — scope the request, choose specialists. The lead delegates to:
   - `signal-integrator` for provider APIs / normalization / delivery
   - `provider-ops-lead` for sequence / credit budget / failover
   - `data-quality-steward` for validation / freshness / compliance
   - `company-analyst` for firmographic dossiers (account intelligence)
   - `data-specialist` for decision-maker discovery (contact enrichment)
3. **Design the waterfall** — `Data Engineering/pipelines/enrichment-pipeline/skills/waterfall-blueprint` — provider sequence, credit budget, branching by available input. Choose a profile: cost-conscious / balanced / quality-first.
4. **Execute** — `/enrichment-pipeline:run-waterfall-enrichment` for bulk, or `/enrichment-pipeline:enrich-leads` for single record.
5. **Validate before delivery** — `Data Engineering/pipelines/enrichment-pipeline/skills/validation-rulebook` — applied automatically by `data-quality-steward`. If a compliance flag fires, the run halts — fix the lawful-basis gap, do not bypass.
6. **Post-run audit** — `Data Engineering/governance-and-quality/data-quality-auditor` — confirm delivered data meets the quality bar. Skip only if volume is small and manually reviewable.

Provider catalog (capabilities, costs, success rates per provider): `Data Engineering/pipelines/enrichment-pipeline/references/providers-catalog.md`.
Provider cheat sheet (at-a-glance shortlist): `Data Engineering/pipelines/enrichment-pipeline/skills/waterfall-blueprint/references/provider_cheat_sheet.md`.

For each step:
- State the decision being made
- Capture the user's choice before advancing

Bypass: *"Use my existing waterfall"* / *"Skip the post-audit"* / *"Just enrich this one record"*.

Reference the full playbook for specialist roles and decision points:
**`Data Engineering/playbooks/07-data-enrichment.md`**
