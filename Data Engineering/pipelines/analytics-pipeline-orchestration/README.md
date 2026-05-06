# Analytics Pipeline Orchestration

Agent bundle for instrumenting, modeling, and shipping analytics — event tracking → semantic models → BI dashboards.

## Bundle Structure

```
analytics-pipeline-orchestration/
├── agents/
│   ├── analytics-data-strategist.md   (event taxonomy, KPI tree, governance)
│   ├── analytics-modeling-lead.md     (dbt-style modeling, semantic layer)
│   └── bi-publisher.md                (dashboard design, distribution)
├── commands/
│   ├── define-events.md               (event schema + tracking plan)
│   ├── build-model.md                 (transform raw → marts)
│   └── ship-dashboards.md             (BI publish + access)
└── skills/
    ├── instrumentation/               (event capture playbook)
    ├── quality-gates/                 (SLOs + QA checklist)
    └── visualization-patterns/        (chart selection + dashboard structure)
```

## How to Invoke

| Goal | Start with |
|---|---|
| Define a new tracking plan | `/analytics-pipeline-orchestration:define-events` or `analytics-data-strategist` agent |
| Build dbt models for a new domain | `/analytics-pipeline-orchestration:build-model` |
| Ship a stakeholder dashboard | `/analytics-pipeline-orchestration:ship-dashboards` or `bi-publisher` agent |

## Cross-references

- **`architecture/dataops-and-platforms`** — the *operating model* for everything in this bundle (DataOps SLOs, Modern Data Stack composition, semantic layer design, FinOps). Read that skill to understand the *why*; use this bundle to ship the *what*.
- **`architecture/storage-and-modeling-patterns`** — pick the model (Kimball star, Inmon, Data Vault) before invoking `build-model`.
- **`governance-and-quality/data-quality-auditor`** — pair with `quality-gates` skill when an audit reveals a quality issue this bundle should prevent in the future.
