---
name: dataops-and-modern-data-platforms
description: >
  Apply DataOps practice (SLOs, monitoring, deployment discipline for data),
  Modern Data Stack composition, Live Data Stack patterns, Data Mesh adoption,
  Semantic Layer design, Reverse ETL (BLT), Analytics Engineering / Analytics-
  as-Code (dbt-style), and FinOps for data. Use when establishing operations
  for a data team, choosing a data platform pattern (MDS vs Live vs Mesh),
  building a semantic layer, or operationalizing analytics. Triggers: "DataOps
  practice", "Modern Data Stack composition", "Live Data Stack", "Data Mesh
  rollout", "semantic layer", "Reverse ETL", "analytics engineering", "dbt
  workflow", "FinOps for data", "data platform SLOs". Produces a defined
  ops practice + chosen platform composition with rationale.
---

# DataOps and Modern Data Platforms

You apply *Fundamentals of Data Engineering*'s operational discipline: DataOps
practices that bring software-engineering rigor to data, plus the modern
platform patterns (MDS, Live Data Stack, Data Mesh) that compose around them.

---

## When to Use This Skill

- Establishing on-call, SLOs, and monitoring for a data team
- Composing a Modern Data Stack from scratch
- Deciding when to evolve to Live Data Stack or Data Mesh
- Designing a semantic layer for consistent metrics
- Setting up Reverse ETL to operationalize analytics
- Adopting Analytics Engineering practices (dbt, version control, CI/CD)
- Standing up FinOps cost discipline for cloud data platforms

---

## DataOps — Software Engineering for Data

DataOps applies DevOps principles to data: monitoring, automation, deployment
discipline, SLOs.

### Core Practices

| Practice | What it looks like | Why |
|---|---|---|
| **Version control for everything** | dbt models, Airflow DAGs, IaC, even SQL one-offs in a `transient/` folder | Roll back; review; trace |
| **CI/CD for transformations** | PR triggers dbt run + tests + linting; gate on green | Catch regressions before prod |
| **Automated testing of data** | dbt tests, Great Expectations, custom assertions | Data quality is code-tested, not eyeballed |
| **Monitoring & SLOs** | Freshness, volume, schema, distribution. Pages when violated. | Outages caught by automation, not by execs at 9am |
| **Runbooks** | Per-pipeline doc: what it does, who owns it, common failures, rollback steps | Anyone on-call can recover |
| **Blameless postmortems** | Document root cause, action items, share team-wide | Continuous improvement |
| **Data contracts** | Producer commits to schema + SLAs; consumer can rely on them | Reduces silent breakage from upstream changes |

### SLOs for Data

| SLO | Example |
|---|---|
| **Freshness** | "Order facts updated within 30 min of source change, 99% of days" |
| **Volume** | "Daily event count between 80%-120% of 7-day rolling average" |
| **Schema stability** | "No breaking schema change without 7-day notice" |
| **Quality** | "Null rate on customer_id < 0.1% in fact_orders" |
| **Availability** | "BI dashboards return < 10s response time, 99.9% uptime business hours" |

**Tools:** Great Expectations, Monte Carlo, Soda, Datafold, Anomalo for monitoring; OpenLineage / DataHub / Atlan for lineage; PagerDuty / Opsgenie for alerting.

---

## Modern Data Stack (MDS) Composition

```
SOURCES                    INGESTION              STORAGE/COMPUTE             TRANSFORMATION         SERVING            REVERSE ETL
─────────                  ─────────              ──────────────              ──────────────         ────────           ───────────

Application DB         →   Fivetran/Airbyte   →   Snowflake/BigQuery/    →   dbt              →    Looker /        →   Hightouch
SaaS (Stripe, HS,           Stitch                Redshift/Databricks                              Mode/                Census
  Salesforce)                                                                                      Tableau /
Product events         →   Segment/                                                                Hex/                 (push back to
  (Segment/RudderStack)     RudderStack                                                            Sigma                 SaaS systems)
                                                                                                       │
Files                  →   Custom +                                                                    │
                            Airflow                                                                    ▼
                                                                                              Semantic Layer
                                                                                              (LookML / dbt
                                                                                               Semantic Layer)
```

### Component selection heuristics

**Ingestion:**
- SaaS sources → Fivetran (premium) or Airbyte (OSS, cheaper)
- Database CDC → Debezium (OSS), Fivetran HVR, or AWS DMS
- Product events → Segment (mature) or RudderStack (OSS)

**Storage / compute:**
- Snowflake — the conservative default; great UX
- BigQuery — best if you're on GCP; serverless model
- Databricks — best for ML-heavy workflows
- Redshift — only if AWS-native is a hard requirement

**Transformation:**
- dbt is the industry default. Use dbt Cloud for managed (small teams) or dbt Core + Airflow/Dagster (larger teams).

**BI:**
- Looker — semantic layer first-class; expensive
- Mode — analyst-friendly; SQL + Python notebooks
- Hex — modern, collaborative, growing share
- Tableau — entrenched in big enterprise
- Sigma — spreadsheet-style for business users

**Reverse ETL:**
- Hightouch — broad source/dest support
- Census — strong dbt integration

### MDS Strengths and Limits

**Strengths:** Off-the-shelf. Best-of-breed components. Composable. Fast to deploy. Documented.

**Limits:**
- Real-time is hard. DWs are batch-first.
- Tool sprawl. Each tool fine alone; together a learning curve.
- Cost scales unpredictably. Snowflake bill grows with usage; analysts don't always see the cost.
- SaaS lock-in. Moving off Fivetran is real work.

---

## The Live Data Stack (Successor)

```
SOURCES   →  STREAMING INGESTION  →  STREAMING STORAGE  →  STREAMING COMPUTE  →  SERVING
            (Kafka, Pulsar,          (Kafka with long       (Flink, Spark         (Materialize,
             Kinesis)                 retention; Iceberg     Streaming;            Pinot, ClickHouse,
                                      tables)                Materialize)          custom APIs)
                                                                  ↓
                                                               ML / Inference
```

**Defining traits:**
- Streaming-first. No "we'll batch this part."
- Materialized views maintained continuously.
- ML inference on live features.
- Lakehouse table formats (Iceberg, Delta) provide ACID storage that streaming engines can write to.

**When to adopt:**
- Real-time analytics is genuinely required (operational alerting, fraud, financial)
- The team has streaming expertise (or plans to invest in it)
- Data freshness is a competitive feature

**When NOT to adopt:**
- Real-time isn't actually required (most cases)
- Team is small; ops burden is significant
- Existing MDS works and isn't blocking value

---

## Data Mesh — Decentralized Ownership

```
Platform Team
(provides self-serve infrastructure: catalog, compute, observability)
         │
         ├──────────┬──────────┬──────────┐
         ▼          ▼          ▼          ▼
    Domain A    Domain B    Domain C    Domain D
    │           │           │           │
   Owns:       Owns:       Owns:       Owns:
   - sources    - sources   - sources   - sources
   - pipelines  - pipelines - pipelines - pipelines
   - data       - data      - data      - data
     products    products    products    products
   - SLAs       - SLAs      - SLAs      - SLAs
   - on-call    - on-call   - on-call   - on-call

Federated catalog + data contracts + cross-domain queries
```

### Zhamak Dehghani's Four Principles

1. **Domain ownership** — domain teams own their data end-to-end
2. **Data as a product** — data has owners, SLAs, documentation, consumers, satisfaction metrics
3. **Self-serve data platform** — central platform team builds infrastructure that lets domain teams operate independently
4. **Federated computational governance** — automated enforcement of cross-domain rules (security, quality, schemas)

### When Data Mesh Works

- Large organization (typically 100+ engineers, multiple business domains)
- Central data team is bottlenecked by request queue
- Domain teams are willing and able to own their data
- Platform engineering capability exists (or is being built)

### When Data Mesh Fails

- Premature: applied to small companies with no domain bottleneck
- Decentralization without governance: chaos, not autonomy
- No platform investment: domains end up rebuilding the same plumbing
- Branding exercise: rebrand existing teams as "domains" without changing how they work

**Practical advice:** Start centralized. Add Data Mesh principles as the central team becomes the bottleneck. Don't begin with Mesh.

---

## Semantic Layer

A **single source of truth for business definitions** — metrics, dimensions, calculations — defined once and consumed by all tools.

### Why it matters

Without a semantic layer:
- "Revenue" means different things in Looker, Mode, and the exec spreadsheet
- Each tool has its own SQL definitions
- Updating a metric requires changes in N tools

With a semantic layer:
- "Revenue" is defined once
- All tools query it the same way
- Updates propagate automatically

### Implementation options

| Option | What it is | When |
|---|---|---|
| **LookML** (Looker) | Embedded in the BI tool | Already on Looker; one-tool BI |
| **dbt Semantic Layer** (formerly MetricFlow) | Tool-agnostic; consumed via dbt's API | Multi-tool BI; want metrics decoupled from any one BI |
| **Cube / AtScale** | Standalone semantic layer | Need to support many tools; want OLAP-style queries |
| **Code-first metrics** | Custom (SQL macros, GraphQL) | Smaller teams; prefer code over config |

**Practical guidance:** dbt Semantic Layer is the trajectory for tool-agnostic teams. LookML works if you're committed to Looker.

---

## Reverse ETL (Bidirectional Load and Transform / BLT)

```
Sources → DW → Curated tables → Reverse ETL → Salesforce / HubSpot / Zendesk / Slack
                                              (operationalized data)
```

**The pattern:** Take data that's been modeled in your warehouse and push it back into operational SaaS systems. Examples:

- Customer health scores → Salesforce contact field → CSMs see in their UI
- Product feature usage → HubSpot for marketing segmentation
- Fraud risk score → operations dashboard that's not your DW

**Tools:** Hightouch, Census, RudderStack, custom (for simple pushes).

**Why it matters:** The DW is no longer an analytics terminus. It's a hub. Operational teams get DW-modeled data in the tools they already use, without learning SQL or BI.

**Cautions:**
- Round-tripping data through SaaS introduces latency
- SaaS API rate limits constrain refresh frequency
- "What we send to Salesforce" becomes a contract — version it like one

---

## Analytics Engineering / Analytics-as-Code

The role:
- Lives between data engineering (raw ingestion, infra) and analytics (BI, exploration)
- Owns transformation: dbt models, semantic definitions, tests, documentation
- Practices software engineering: PRs, tests, CI/CD, code review

The discipline:
- Transformations are version-controlled SQL (dbt-style)
- CI runs `dbt test`, lint (e.g., SQLFluff), and prevents broken merges
- Production deploys are automated, not manual
- New analysts contribute via PRs, not direct DW edits
- Documentation co-located with code (dbt's `models/.../*.yml`)

**Analytics Engineer is now a distinct role** at most data-mature companies. The skills overlap data engineering (SQL, DW, modeling) and software engineering (Git, testing, deployment).

---

## FinOps for Data

Already covered briefly in `data-engineering-lifecycle-and-principles`; deeper here.

### Core practices

**Tag every resource:**
- Workload (e.g., "marketing-attribution")
- Team owner
- Environment
- Cost center
Untagged resources are unmanaged spend.

**Per-query cost telemetry:**
- Snowflake `query_history` includes `total_elapsed_time` and credits consumed
- BigQuery has `INFORMATION_SCHEMA.JOBS_BY_PROJECT` with cost
- Pipe these into a Looker / Tableau dashboard owned by the data team
- Engineers see the cost of the queries they wrote

**Compute warehouse hygiene:**
- Auto-suspend at 60 seconds (Snowflake) or equivalent
- Right-size warehouses; don't run XL when L is enough
- Multi-cluster for concurrency, not single-cluster XXL
- Reserved capacity for steady baseline; on-demand for spikes

**Storage tier optimization:**
- Move cold tables to cheaper tiers (Snowflake's transient + Iceberg external; BigQuery's long-term storage tier)
- Drop unused tables (with audit trail)
- Compact small files in lakehouses regularly

**Monthly review ritual:**
- Top 10 expensive queries — can they be optimized?
- Top 10 expensive warehouses — are they sized right?
- New cost spikes — what changed?

**Engineering KPIs:**
- $/GB processed
- $/active user (for product analytics)
- $/dashboard load (for BI)

---

## Principles

- **Data quality is everyone's job.** Tests in dbt, contracts at ingestion, monitoring on freshness. Not "one person's responsibility."
- **Observability before optimization.** You can't fix what you can't measure.
- **Version control everything.** SQL, configs, dashboards-as-code where possible.
- **Production deploys are automated.** Manual deploys are a code smell.
- **Cost telemetry close to engineers.** Engineers can act on what they can see.
- **Semantic layer prevents metric drift.** Define once; consume everywhere.
- **Defer Data Mesh.** Centralized works longer than people expect; Mesh is rarely the right first move.
- **MDS is the safe default.** Resist the urge to bypass for trendy alternatives unless you have a clear use case.

---

## Anti-Patterns

### "We'll Add Tests Later"

**Looks like:** dbt models without `tests:` blocks. Pipelines without assertions.

**Why it fails:** Quality issues silently propagate. Trust erodes. Recovery is reactive.

**The fix:** Adopt at least `unique`, `not_null`, `accepted_values`, `relationships` tests as defaults. Increase from there.

### Manual Production Deploys

**Looks like:** "Let me apply this to prod manually." Pipeline production state diverges from main.

**Why it fails:** No rollback path. State drifts. Outages compound.

**The fix:** CI/CD that deploys main to prod automatically. Manual override is the exception, not the rule.

### "We Need Real-Time" When You Don't

**Looks like:** Adopting Live Data Stack because "real-time is the future." No use case requires sub-second.

**Why it fails:** Streaming infrastructure is 10x the operational complexity. Premature investment that doesn't move the needle.

**The fix:** Hourly batch first. When you have a sub-second use case, then streaming. Not before.

### Cost Visible Only to Finance

**Looks like:** Engineers don't know what their queries cost. Cloud bill is a finance-team problem.

**Why it fails:** Cost surfaces miles from the engineer who can act. By the time finance complains, architecture is locked in.

**The fix:** Cost telemetry on the engineer's dashboard. Per-query cost in dbt docs. Per-team monthly burn in Slack.

### Premature Data Mesh

**Looks like:** 30-engineer company adopting "Data Mesh" because it's trendy. No domains. No platform.

**Why it fails:** Decentralization without infrastructure produces chaos. Each "domain" rebuilds plumbing. Worse than central.

**The fix:** Centralize. Adopt Mesh principles when central is genuinely the bottleneck and you can invest in platform engineering.

### One Metric Definition Per Tool

**Looks like:** "Revenue" defined separately in Looker, Mode, the exec spreadsheet, and Salesforce. They drift.

**Why it fails:** Decisions get made on inconsistent numbers. Trust evaporates. Endless reconciliation meetings.

**The fix:** Semantic layer. Define once; consume in all tools.

### Snowflake on 24/7 Auto-Suspend Disabled

**Looks like:** Warehouse runs all night. Nobody queries it. $5K/month wasted.

**Why it fails:** Idle compute is the most common Snowflake cost mistake.

**The fix:** Auto-suspend at 60 seconds. The startup cost is negligible.

### Reverse ETL Without Versioning

**Looks like:** Push customer health score to Salesforce. Schema changes silently. CSM dashboards break.

**Why it fails:** Reverse ETL is an API contract. Treating it as informal causes consumer breakage.

**The fix:** Version the contract. Notify CSM team before changes. Treat the destination schema like a public API.

---

## Decision Rules

| Situation | Action |
|---|---|
| Greenfield platform, < 100 engineers | MDS (Snowflake/BQ + Fivetran/Airbyte + dbt + Looker/Mode) |
| Real-time analytics genuinely required | Live Data Stack (Kafka + Flink/Materialize + Iceberg) |
| 100+ engineers, multiple business domains, central team bottlenecked | Plan toward Data Mesh; invest in platform team first |
| 100+ engineers, no clear domains | Stay centralized. Mesh isn't the answer. |
| Adopting dbt | Start with dbt Cloud (small team) or dbt Core + Airflow/Dagster (larger). Always with tests. |
| Need consistent metrics across tools | Semantic layer (LookML or dbt Semantic Layer) |
| Sales team wants product usage in Salesforce | Reverse ETL (Hightouch / Census) |
| New data hire, "what should they do first?" | Wire up monitoring + alerting. Tests on every model. CI/CD. |
| Cost surge | Establish FinOps practice. Tagging + per-query cost dashboards. |
| Manual deploy ritual | Replace with CI/CD. Manual is the exception. |
| "We need a data scientist" | Verify undercurrents are healthy. If not, hire DE first. |
| dbt model failing in prod | Run tests in CI. Block merges on failure. Use `--defer` for cheap PR builds. |
| Multiple BI tools fighting | Standardize on a semantic layer; let tools query it. |

---

## Worked Example: Six-Month DataOps Transformation

**Starting point:** 6-person data team. Snowflake + Fivetran + Looker. No tests. Manual deploys. No alerting. 3 outages/week.

**Month 1: Stop the bleeding.**
- Adopt dbt + dbt Cloud. Migrate top 20 SQL queries to dbt models.
- Add `not_null` and `unique` tests on primary keys. CI blocks merges on failures.
- Subscribe to Snowflake account events; alert on warehouse credit anomalies.

**Month 2: Establish observability.**
- Adopt Monte Carlo (or Datafold or Soda — pick one).
- Add freshness SLOs on tier-1 tables. PagerDuty on violations.
- Build cost dashboard in Looker — per-team Snowflake credit burn, per-query top 10.

**Month 3: Code review + CI/CD.**
- All dbt model changes via PR. Two-person review.
- CI runs `dbt build --select state:modified+ --defer --state ./prod-manifest`.
- Auto-deploy main to prod via dbt Cloud.

**Month 4: Documentation + lineage.**
- Adopt dbt's column-level docs. Require docs on new models.
- Implement OpenLineage ingestion into DataHub (or use dbt-to-DataHub integration).
- Document top 10 pipelines with runbooks.

**Month 5: Semantic layer.**
- Identify top 20 metrics. Define in dbt Semantic Layer.
- Migrate Looker LookML to use the semantic layer.
- Sunset spreadsheet "metric definitions" — owned by data team now.

**Month 6: FinOps + on-call.**
- Engineering KPI: per-team Snowflake credits/month
- Right-size warehouses (down from XL to M for most workloads)
- Establish on-call rotation. Runbook for every tier-1 pipeline.

**Result:** Outages drop from 3/week to 1/month. Engineer trust in data jumps. Snowflake bill down 30% from right-sizing.

**Lesson:** DataOps maturity is a 6-12 month investment. The wins compound. The biggest leverage point is automated quality gates — fix that first.

---

## Gotchas

- **dbt is not magic.** Bad SQL with dbt is still bad SQL. dbt's value is the discipline + ecosystem, not the models themselves.
- **Looker license cost scales fast.** Per-developer pricing makes self-serve analytics expensive at scale. Some teams move to Mode / Hex / Sigma for analyst tooling.
- **Reverse ETL latency matters.** Hightouch and Census batch by default. If your CSM workflow assumes 5-minute freshness, configure accordingly.
- **dbt Cloud vs dbt Core:** Cloud is great for small teams; Core+Airflow gives you more control and avoids per-developer pricing.
- **Semantic layers are immature.** dbt Semantic Layer is improving fast but isn't yet at LookML's maturity for complex business definitions. Plan for some custom work.
- **Data Mesh requires real platform engineering.** "We'll figure out the platform later" is the most common failure mode.
- **Live Data Stack ops is hard.** Kafka cluster management, schema registries, exactly-once semantics — these are full-time jobs.
- **FinOps without engineer buy-in fails.** If engineers feel surveilled, the practice becomes adversarial. Frame it as engineering excellence, not cost-policing.
- **Reverse ETL into SaaS APIs hits rate limits.** Plan for partial syncs and incremental updates; full refreshes don't scale.

---

## Further Reading

- *Fundamentals of Data Engineering* (Reis & Housley), Chapters 9-11 (Serving, Security/Privacy, Future)
- Tristan Handy's blog (dbt Labs founder) on Analytics Engineering
- Zhamak Dehghani's *Data Mesh* book and posts
- Chad Sanderson's *Data Contracts* writing
- See `data-engineering-lifecycle-and-principles` for foundational lifecycle/undercurrents
- See `data-architecture-frameworks` for higher-level architecture choices
- See `data-storage-and-modeling-patterns` for storage tiers and dimensional modeling

Source: *Fundamentals of Data Engineering* (Reis & Housley), Chapters 9-11.
