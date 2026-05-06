# Playbook 04 — Data Quality Audit + Remediation

Chain for auditing a dataset's quality and remediating root causes. Triggered automatically by phrases like "audit my data", "data quality issues", "anomalies in [X]" (UserPromptSubmit hook).

## When to Use

- "Audit the [table / dataset / warehouse]"
- "Why is [metric] wrong?"
- "Find data quality issues in X"
- "Profile this dataset — what's broken?"
- "Anomalies in [X]"
- Routine quarterly data health review

## When to Skip

- You only need to fix one bad row — just fix it
- The issue is a known schema bug — go straight to `databases/database-designer`
- You're profiling a brand-new dataset for *exploration* (not quality) — use general data-exploration tooling

## Sequence

| Step | Skill | Output |
|---|---|---|
| 1 | **`governance-and-quality/data-quality-auditor`** | Profile (distributions, nulls, dupes, outliers), DQS score, prioritized remediation plan |
| 2 | **Branch on root cause:** | |
|   | → `databases/database-designer` | If issues are schema-rooted (missing constraints, wrong types, no foreign keys) |
|   | → `governance-and-quality/mdm-and-federated-governance` | If issues are policy-rooted (no data contract, RLS gap, ABAC drift, governance ownership unclear) |
|   | → `pipelines/analytics-pipeline-orchestration/skills/quality-gates` | Forward prevention — gate the pipeline so this issue can't recur |
| 3 | Re-run step 1 after remediation | Confirm fixes landed; record DQS delta |

## Decision Tree for Step 2

```
Audit found:
├── Wrong types / missing FKs / no NOT NULL where required
│   └── → database-designer (schema-level fix)
├── Stale data / unowned domain / "who's responsible?"
│   └── → mdm-and-federated-governance (data contracts + ownership)
├── Bad data flowing in (upstream pipeline issue)
│   └── → quality-gates skill in analytics-pipeline-orchestration (gate the input)
└── Already-bad data in production
    └── → remediation plan from data-quality-auditor (one-time fix), THEN one of the above for prevention
```

## Distinction: Audit vs Test

- **This playbook (audit)** is for *finding* issues in production data after the fact.
- **Pipeline `quality-gates` skill** is for *preventing* issues at ingest.
- **Database constraints** (NOT NULL, CHECK, FK) are for *enforcing* invariants at write time.

A mature setup uses all three. The audit is the safety net, not the front line.

## References

- `governance-and-quality/data-quality-auditor/references/data-quality-concepts.md` — MCAR/MAR/MNAR theory, DQS methodology, outlier detection methods
- `governance-and-quality/data-quality-auditor/scripts/data_profiler.py` — profile runner
- `governance-and-quality/data-quality-auditor/scripts/missing_value_analyzer.py`
- `governance-and-quality/data-quality-auditor/scripts/outlier_detector.py`

## Bypass Phrases

To skip the playbook when the hook fires: *"Just profile the data — skip remediation"* / *"I know the root cause, jump to [skill]"* / *"Skip the playbook"*.
