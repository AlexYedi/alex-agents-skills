# Playbook 03 — Production Pipeline Build

Chain for building or operating a production data pipeline (ETL/ELT, dbt models, dashboards, or enrichment flow).

## When to Use

- "Build a pipeline to ingest X to Y"
- "Set up dbt models for [domain]"
- "Ship a dashboard for [stakeholder]"
- "ETL / ELT for [source → destination]"
- "Add an event tracking plan"

## When to Skip

- You're tweaking one existing model, not building new — go direct to `pipelines/analytics-pipeline-orchestration`
- Single ad-hoc enrichment lookup — use `/data-engineering:enrich` (playbook 07) instead
- You're only changing infrastructure (Airflow config, Kubernetes) — this is platform work, not pipeline design

## Sequence

| Step | Skill | Output |
|---|---|---|
| 1 | `architecture/dataops-and-platforms` | Operating model context: SLOs, freshness targets, FinOps budget, semantic layer fit |
| 2 | `architecture/integration-patterns` | Sync vs async, batch vs event vs CDC, choreography vs orchestration |
| 3 | `architecture/storage-and-modeling-patterns` | Destination model: warehouse layer, staging→intermediate→marts, SCD strategy |
| 4 | **Branch on pipeline type:** | |
|   | → **`pipelines/analytics-pipeline-orchestration`** | If purpose is event tracking, dbt models, BI dashboards |
|   | → **`pipelines/enrichment-pipeline`** | If purpose is provider-based enrichment / waterfalls — also see playbook 07 |
| 5 | `pipelines/analytics-pipeline-orchestration/skills/quality-gates` | Forward-looking gates so this pipeline doesn't become a future quality-audit ticket |

## Decision Points

- **Batch vs event-driven** (step 2): if downstream tolerates >5min staleness and the source is queryable, batch wins on simplicity. Event-driven only when freshness materially changes the use case.
- **Where to model** (step 3): raw → staging → intermediate → marts is the dbt-default. Compress to staging → marts only for genuinely simple domains.
- **Schema-on-write vs schema-on-read** (step 3): write for warehouse (Kimball), read for lake (Iceberg/Delta).
- **Single big DAG vs many small DAGs**: many small > one big, almost always. Each domain owns its DAG; orchestrator wires dependencies.

## Cross-folder pointers (optional)

- `Software Development/event-streaming-with-kafka` — if step 4 picks event-driven
- `Software Development/stream-processing-with-flink` — if real-time stream analytics
- `Software Development/eventual-consistency-mechanics` — if cross-system eventual consistency is in scope

## Bundle contents (step 4 destinations)

- **`analytics-pipeline-orchestration/`** has agents (analytics-data-strategist, analytics-modeling-lead, bi-publisher), commands (define-events, build-model, ship-dashboards), and sub-skills (instrumentation, quality-gates, visualization-patterns).
- **`enrichment-pipeline/`** has agents (enrichment-expert lead + 5 specialists), commands (run-waterfall-enrichment, enrich-leads, etc.), and sub-skills (waterfall-blueprint, identity-resolution, etc.).

## Bypass Phrases

To skip the architecture steps: *"I have the pipeline shape — go to step 4"* / *"Just help me write the dbt model"*.
