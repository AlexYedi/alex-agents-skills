---
description: Walk the production pipeline build chain — dataops operating model, integration patterns, destination modeling, then branch into analytics-pipeline-orchestration or enrichment-pipeline.
---

You are guiding a production data pipeline build using the chain documented at `Data Engineering/playbooks/03-pipeline-build.md`.

Walk these steps in order:

1. **Operating model** — `Data Engineering/architecture/dataops-and-platforms` — SLOs, freshness targets, FinOps budget, semantic layer fit.
2. **Integration shape** — `Data Engineering/architecture/integration-patterns` — sync vs async, batch vs event vs CDC, choreography vs orchestration.
3. **Destination model** — `Data Engineering/architecture/storage-and-modeling-patterns` — warehouse layer (raw → staging → intermediate → marts), SCD strategy.
4. **Branch on pipeline type:**
   - Analytics / event tracking / dbt models / BI dashboards → `Data Engineering/pipelines/analytics-pipeline-orchestration/` (use the bundle's agents and commands)
   - Provider-based enrichment → `Data Engineering/pipelines/enrichment-pipeline/` — if so, also walk playbook 07
5. **Forward gates** — `Data Engineering/pipelines/analytics-pipeline-orchestration/skills/quality-gates` — define gates so this pipeline doesn't become a future quality-audit ticket.

For each step:
- State the decision and trade-offs from the named skill
- Capture the user's choice before advancing

If the user already has the pipeline shape and just needs implementation help, jump to step 4 directly.

Bypass at any time: *"I have the shape — go to step N"* or *"Just help me write the [specific artifact]"*.

Reference the full playbook for decision-point details and cross-folder pointers (Kafka, Flink, eventual-consistency):
**`Data Engineering/playbooks/03-pipeline-build.md`**
