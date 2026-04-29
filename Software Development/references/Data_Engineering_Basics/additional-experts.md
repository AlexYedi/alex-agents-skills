# Fundamentals of Data Engineering — Additional Expert Notes

> Best practices and advice from Joe Reis & Matt Housley (O'Reilly, 2022).

## About the Authors

**Joe Reis** — Co-founder of Ternary Data, ex-data engineer at Mailchimp and Wedge. Active on the data engineering speaking circuit. Voice: pragmatic, vendor-skeptical, focused on the discipline rather than the trend cycle.

**Matt Housley** — Long-time data architect, ex-Google. Voice: framework-oriented, math-friendly, comfortable with formalism.

**Joint voice:** They're explicit that the book is *not* a tools tutorial — it's a discipline framework. They name 50+ tools but never recommend a single stack. The lifecycle and undercurrents are the durable contribution; the tool list is a snapshot.

## Foundational Mindset Shifts

1. **Lifecycle thinking, not stage thinking.** A failure at "Serving" usually originated in "Generation" or "Storage." Trace upstream when debugging.
2. **Undercurrents are non-negotiable.** Missing one — security, governance, DataOps, architecture, orchestration, software engineering — is where the next outage will originate.
3. **Business value beats technology novelty.** A boring Postgres + cron stack shipping weekly analytics beats a bespoke streaming Kappa setup that's 6 months from production.
4. **Reversibility beats optimization.** Choose architectures that can evolve. Don't lock in for theoretical optimization gains.
5. **Cost is a design dimension.** Not an afterthought. FinOps mindset from day 1.
6. **"Big data" is rarely your data.** Most companies have small-to-medium data. Distributed everything is unnecessary overhead.

## Best Practices by Topic

### Greenfield platform setup
- Cloud DW (Snowflake, BigQuery, Redshift, Databricks SQL) as the center
- dbt for transformations from day 1
- Fivetran or Airbyte for SaaS ingestion
- Debezium / managed CDC for app DB
- Looker / Mode / Hex for BI; semantic layer (LookML or dbt Semantic Layer) early
- All infrastructure as code (Terraform); all transformations in version control
- CI/CD on the dbt project; PRs trigger model builds + tests
- Monitoring (Monte Carlo / Datafold / Soda) on tier-1 tables
- PagerDuty for freshness/quality SLO violations

### Hiring in the right order
1. Data engineer (Type A, internal-facing) — builds the foundation
2. Analytics engineer — owns the modeling layer
3. Data scientist — only after foundation is reliable
4. ML engineer — only after data science has produced models worth deploying
5. Platform engineer / data architect — emerges as the team scales past 5-7 people

### Data quality discipline
- Tests on every model: not_null, unique, accepted_values, relationships
- Schema contracts at ingestion boundaries
- Anomaly detection on volume + freshness + distribution
- Data contracts for high-stakes producer/consumer relationships
- Blameless postmortems documented and shared

### Cost discipline
- Tag every workload (team, environment, project)
- Auto-suspend warehouses aggressively (60s for Snowflake)
- Per-query cost telemetry visible to engineers
- Monthly review of top 10 expensive queries + warehouses
- Engineering KPIs include $/business outcome

### Storage tier optimization
- Hot path: BI dashboards, OLTP — cloud DW or Materialize
- Warm path: ad hoc queries, ML training — lakehouse on object storage with Iceberg/Delta
- Cold path: archival, compliance — S3 Glacier / Coldline

### Data Mesh adoption (when truly justified)
- Invest in self-serve platform first; without infrastructure, decentralization = chaos
- Define data products with explicit SLAs
- Federated governance via automated policy enforcement
- Domain teams must want it, not have it imposed

## Specific Advice with Rationale

### "Choose common components wisely" (Principle 1)
**Why:** Standard tools have communities, hires, integrations. Custom = lonely + expensive forever.
**Apply:** Don't build a custom orchestrator. Don't write a custom DW. Don't roll your own data quality framework.

### "Plan for failure" (Principle 2)
**Why:** Every cloud component fails. Without explicit RTO/RPO, your "reliability" is hope.
**Apply:** Define RTO/RPO per workload. Multi-region for tier 1. Idempotent writes. Practiced restores.

### "Architect for scalability" (Principle 3)
**Why:** Scaling up matters; scaling down matters more (cost). Idle resources kill margins.
**Apply:** Auto-scaling. Auto-suspend. Serverless for spiky loads. Reserved capacity only for stable baseline.

### "Architecture is leadership" (Principle 4)
**Why:** Architects who don't code lose touch. Decisions go stale. Engineers feel disempowered.
**Apply:** Architects on PRs. Architects writing ADRs. Architects pairing with juniors.

### "Always be architecting" (Principle 5)
**Why:** Static architecture rots as business and tech evolve. The "next rewrite" balloons until it's existential.
**Apply:** Quarterly architecture reviews. Strangler-fig refactors. No 6-month freezes.

### "Build loosely coupled systems" (Principle 6)
**Why:** Tight coupling = every change cascades. Loose = components can evolve independently.
**Apply:** API contracts. Event-driven where producers shouldn't know consumers. No shared DB mutations between services.

### "Make reversible decisions" (Principle 7)
**Why:** Locked-in choices accumulate. Today's "best" tool is rarely the right one in 3 years.
**Apply:** Open formats (Parquet, Iceberg). Cloud-portable infra (Terraform). Avoid 3-year vendor contracts.

### "Prioritize security" (Principle 8)
**Why:** Compliance is increasingly stringent (GDPR, CCPA, HIPAA). Breach costs are existential.
**Apply:** Least privilege. Encryption everywhere. PII tokenization. Audit logs. No long-lived admin credentials.

### "Embrace FinOps" (Principle 9)
**Why:** Cloud bills surprise; cost mistakes compound; engineering choices have $ implications.
**Apply:** Tagging discipline. Cost telemetry near engineers. Right-sizing rituals. Cost as code review concern.

## Worked Examples

### Diagnosing a failing data team (5 of 6 undercurrents broken)
See `data-engineering-lifecycle-and-principles` skill for full worked example.

### Choosing the stack for a Series-B SaaS
See `data-architecture-frameworks` skill for full worked example.

### Modeling a SaaS product's analytics
See `data-storage-and-modeling-patterns` skill for full worked example.

### Six-month DataOps transformation
See `dataops-and-modern-data-platforms` skill for full worked example.

## Anti-Patterns Deeper Than Skill Files

- **"We're a data-driven company" without data infrastructure.** A common slogan that promises capability the foundation can't deliver.
- **Modeling first, ingestion later.** Building dimensional models on shaky CDC. The model is only as good as the source pipeline.
- **PII proliferation.** Raw PII in bronze, silver, gold, dev, staging. One breach is catastrophic.
- **"We need real-time" without a use case.** Streaming infrastructure adopted before any use case requires sub-second.
- **Multi-DW mess.** Each team buys their own warehouse "for autonomy." Reconciliation becomes the team's full-time job.
- **Premature Kappa abandonment.** Adopting Kappa, hitting streaming complexity, retreating to Lambda. Should have started with Lambda.
- **Self-hosting Kafka.** A specialized full-time job. Use a managed service unless you have unique requirements.
- **Spreadsheet metrics.** Definitions of "MRR" / "MAU" / "Revenue" living in different spreadsheets, drifting silently.
- **The "data council" without authority.** Cross-functional committee that recommends but can't enforce. Theater.
- **Vendor demo-driven roadmap.** Buying tools because the demo was impressive, not because of a confirmed need.

## Process Wisdom

- **Architecture decisions are documented (ADRs)**, kept in version control, reviewed quarterly.
- **Postmortems are blameless and public** within the team. Action items with owners and dates.
- **On-call has a runbook for every tier-1 pipeline.** "How to recover from this failure."
- **New analyst onboarding includes a contribution PR within week 1.** Otherwise they don't internalize the workflow.
- **Schema changes follow a contract-style cadence:** notice, deprecate, change. Minimum 7-day window for breaking changes.
- **Storage tiers are explicit and reviewed.** Cold tables periodically migrated to cheaper storage.

## Career / Context Wisdom

- **The "Type A vs Type B" data engineer distinction matters in hiring.** Confusing them produces bad hires.
- **Internal-facing vs external-facing changes everything.** Latency, reliability, schema stability — all different.
- **Analytics Engineer is a real role now.** Not a junior data engineer; a discipline of its own.
- **Data architect is a leadership role, not a tower role.** They code. They write ADRs. They mentor.
- **Resist the "hire a data scientist first" instinct.** Data engineers create the foundation; data scientists need it.
- **The lifecycle and undercurrents framework is portable across companies.** Carry it with you.
- **Tools change every 2-3 years. The discipline doesn't.** Invest in the discipline.

Source: *Fundamentals of Data Engineering* (Reis & Housley, O'Reilly, 2022).
