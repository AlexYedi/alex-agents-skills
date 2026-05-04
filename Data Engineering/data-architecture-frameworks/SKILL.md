---
name: data-architecture-frameworks
description: >
  Pick and apply data architecture frameworks: TOGAF, DAMA-DMBOK, AWS
  Well-Architected (six pillars), Google's Five Cloud-Native Principles,
  Lambda vs Kappa, Modern Data Stack vs Live Data Stack, Data Mesh, Strangler
  Fig, FinOps, plus build-vs-buy and the four tech-selection axes (size,
  speed, cost, integration). Use when designing or evaluating a data platform's
  high-level architecture, deciding monolith vs modular vs serverless, or
  choosing between Lambda and Kappa for streaming workloads. Triggers: "Lambda
  or Kappa", "Modern Data Stack vs Data Mesh", "build vs buy data tooling",
  "evaluate our data architecture", "AWS Well-Architected for data", "Strangler
  Fig migration", "FinOps approach". Produces a chosen framework + reasoned
  technology selection.
---

# Data Architecture Frameworks

You apply Reis & Housley's catalog of data architecture frameworks: enterprise
frameworks (TOGAF, DAMA), cloud frameworks (AWS Well-Architected, Google's Five
Principles), processing patterns (Lambda, Kappa), platform models (Modern Data
Stack, Live Data Stack, Data Mesh), and migration strategies (Strangler Fig).
You navigate build-vs-buy and the technology-selection tradeoffs.

---

## When to Use This Skill

- Designing a new data platform's high-level architecture
- Evaluating an existing platform against an established framework
- Deciding monolith vs modular for a data system
- Choosing between Lambda and Kappa for streaming
- Adopting (or moving away from) the Modern Data Stack
- Migrating a legacy data warehouse to cloud
- Build-vs-buy decisions on a specific component
- Establishing a FinOps practice

---

## The Enterprise Frameworks (Big-Picture)

### TOGAF (The Open Group Architecture Framework)

**Scope:** All information, technology services, processes, infrastructure across an enterprise. Generic — for any architecture, not just data.

**When useful:** Large enterprise context where data architecture must align with overall enterprise architecture. Government, banking, regulated industries.

**Practical takeaway for data:** Adopts TOGAF's domain-crossing model — architecture spans business, application, data, technology layers. Useful framing for "we need to think above just the data layer."

### DAMA-DMBOK (Data Management Body of Knowledge)

**Scope:** Data architecture as identifying enterprise data needs and designing master blueprints to meet them. The reference for data management as a discipline.

**When useful:** Establishing a Data Management practice. Defining roles like Chief Data Officer. Documenting governance policies.

**Practical takeaway:** Don't just architect the technology — architect the *governance* and *quality* practices alongside.

---

## Cloud Architecture Frameworks

### AWS Well-Architected — Six Pillars

| Pillar | Question to ask |
|---|---|
| Operational Excellence | Can we operate it safely? Runbooks, monitoring, automation? |
| Security | Defense in depth? Least privilege? Audit? |
| Reliability | Will it survive component failures? RTO / RPO defined? |
| Performance Efficiency | Right-sized resources? Caching? Workload-appropriate compute? |
| Cost Optimization | Reserved capacity where stable, spot/serverless where spiky? |
| Sustainability | Energy-efficient regions? Right-sized to avoid waste? |

**Use as:** Architecture review checklist. Each pillar gets a section. Gaps become work items.

### Google Cloud — Five Principles for Cloud-Native Architecture

1. **Design for automation** — every operational task should be code, not a runbook step
2. **Be smart with state** — minimize stateful services; understand where state lives
3. **Favor managed services** — don't run your own DB unless you have a reason
4. **Practice defense in depth** — security layers, not perimeters
5. **Always be architecting** — refactor continuously; no "freeze and rewrite"

Compare with Reis & Housley's nine principles (see `data-engineering-lifecycle-and-principles`). They overlap and reinforce each other.

---

## Processing Pattern: Lambda vs Kappa

```
LAMBDA Architecture                       KAPPA Architecture
─────────────────                          ─────────────────

Source                                     Source
  │                                          │
  ▼                                          ▼
[Speed Layer]   [Batch Layer]              [Streaming Storage]
   ↓                ↓                              │
[Real-time]     [Batch view]                       │
   view              ↓                             ▼
   ↓             Master                    [Streaming Compute]
   ↓             dataset                          │
   └──merge──────────┘                            ▼
       ↓                                      [Serving]
   [Serving]                                      │
                                              All queries
                                              are stream-replays
```

| Aspect | Lambda | Kappa |
|---|---|---|
| **Pattern** | Two paths: streaming (low-latency, lossy) + batch (accurate, slow). Merge at serving. | One path: everything's a stream; batch is just streaming with infinite retention. |
| **Pro** | Each path optimized. Real-time AND historical accuracy. | Single codebase. No drift between batch and streaming. |
| **Con** | Two codepaths to maintain; merge logic is complex. | Streaming storage costs at long retention; complex semantics. |
| **When** | Established big data platforms. Heterogeneous source systems. | Modern stacks built around Kafka/Flink/Pulsar. Streaming-native teams. |

**Apache Beam / Dataflow Model:** treats unbounded (streaming) and bounded (batch) data uniformly. The unified API makes Kappa more practical.

**Practical guidance (2026):** For new platforms, prefer Kappa-leaning approaches with managed streaming (Kafka + Flink, or BigQuery streaming + scheduled queries). Lambda's two-codebase tax is rarely worth it now that streaming is mature.

---

## Platform Models: Modern Data Stack vs Live Data Stack vs Data Mesh

### Modern Data Stack (MDS)

```
Sources → Fivetran/Airbyte → Snowflake/BigQuery/Redshift → dbt → Looker/Mode
                                                            ↓
                                                    Reverse ETL (Hightouch/Census)
                                                            ↓
                                                       SaaS systems
```

**Defining traits:** ELT (not ETL), cloud DW center, SaaS integrations, dbt for transformation, BI on top, Reverse ETL closing the loop.

**Strengths:** Off-the-shelf. Fast to deploy. Composable. Each component is best-of-breed.

**Limits:** Real-time is hard (DWs are batch-oriented). Tool sprawl. Cost can spiral. SaaS-vendor lock-in spread across many small contracts.

### Live Data Stack (the successor)

```
Sources → Streaming (Kafka/Pulsar) → Streaming Compute (Flink/Materialize) →
   ↓                                        ↓
   ↓                                  ML / Inference
   └──── Streaming Storage ──── Serving (real-time + historical)
```

**Defining traits:** Real-time end-to-end. Streaming-first. Materialized views. Often Apache Iceberg / Delta / Hudi as storage.

**When:** Real-time analytics is genuinely required (financial, fraud, operational alerting). Or when the team is streaming-native.

**Cautions:** Most companies don't need this. The MDS handles 90% of use cases at 1/10th the operational complexity.

### Data Mesh

```
Domain A team    Domain B team    Domain C team
     │                │                │
   Owns           Owns             Owns
   - source        - source         - source
   - pipeline      - pipeline       - pipeline
   - Data Product  - Data Product   - Data Product
   - SLAs          - SLAs           - SLAs
     │                │                │
     └────────────────┴────────────────┘
              Federated Catalog
              Data Product Marketplace
              Self-service Platform
```

**Defining traits:** Decentralized. Domain teams own data end-to-end as "data products" with SLAs. Central platform team provides infrastructure (the "self-serve data platform"), not pipelines.

**When:** Large organizations with distinct business domains. Data team can no longer scale centrally. Multiple analytics teams duplicating pipelines.

**Cautions:** Premature for small companies. Requires real platform engineering investment. Without strong governance and discoverability, becomes "decentralized chaos." See Zhamak Dehghani's original framing for the founding constraints.

---

## Migration: The Strangler Fig Pattern

```
Time t=0                Time t=1                    Time t=2
─────────               ─────────                   ─────────

[Legacy]                [Legacy ← shrinking]        [Legacy retired]
   │                        │      ↓                       
   ▼                        ▼  [New piece A]          [New piece A]
[All clients]           [Clients route to            [All clients]
                         A or legacy]                       │
                                                            ▼
                                                       [New piece B]
                                                       [...]
```

**Mechanics:** Wrap the legacy system. Route portions of traffic / use cases to new components. Shrink the legacy until it can be decommissioned.

**When:** Migrating any legacy data system. Especially old DWs, ETL platforms, custom-built tools.

**Why:** Reversibility (Reis & Housley principle 7). At every step, you can roll back individual pieces. No "big bang cutover" weekend.

**Operationally:** Requires routing layer (API gateway, view abstraction, message routing). Worth the upfront investment.

---

## Build vs Buy

```
                 LOW                              HIGH
                 ◄───────  Strategic value  ──────►

LOW  ▲           [BUY]                          [BUY (for now)]
     │           Off-the-shelf SaaS              Time-to-market matters
Cost │           Don't reinvent commodity        Buy now, build later if it
to   │                                          becomes core
build│
     │
HIGH ▼           [BUY]                          [BUILD]
                 Don't ever build                 Core competitive
                 commodity yourself               advantage.
                 (e.g., authentication            Rare.
                  for an analytics co.)
```

**Reis & Housley's heuristics:**
- Default to buy unless competitive advantage is clear.
- If you build, plan for ongoing maintenance — it's not a one-time cost.
- Total Cost of Ownership > sticker price. Engineering time, security patching, ops burden all count.
- Cloud-scale threshold: only consider self-hosting at exabytes/terabits — below that, managed wins.

**Common mistakes:**
- Building data tooling because "we're an engineering company" — this is rarely sufficient justification
- Buying without modeling 5-year TCO; vendor pricing scales painfully
- Buying multiple overlapping tools; consolidate during procurement, not after

---

## Technology Selection — The Four Axes

When choosing any data tech (warehouse, queue, ETL tool, BI):

| Axis | Question |
|---|---|
| **Size** | What's the data volume now and projected? Wrong scale → wrong tool. |
| **Speed** | What's the freshness SLA? Sub-second? Minutes? Hourly? Daily? |
| **Cost** | What's the cost model — per query, per GB, per node-hour? Total at projected scale? |
| **Integration** | Does it speak standard formats (Parquet, Iceberg, JDBC) and protocols (SQL, REST, Kafka)? |

A common pattern: pick on speed, regret on cost; pick on cost, regret on integration. Walk through all four for any decision.

---

## FinOps for Data

**The discipline:** Continuous, data-driven cost management. Cooperation between Engineering and Finance.

**Core practices:**
- **Tag everything.** Workload, team, project, environment. Every resource. Untagged spend is unmanaged spend.
- **Cost telemetry close to the engineer.** Per-query cost. Per-pipeline cost. Per-team monthly burn. Visible in dashboards engineers see daily.
- **Right-sizing rituals.** Monthly review of warehouses, instances, storage tiers.
- **Auto-suspend / auto-scale-to-zero.** Idle compute is waste. Configure aggressively.
- **Reserved capacity for stable load, spot/serverless for spiky.** Match cost model to workload shape.
- **Engineering KPIs include $/business-outcome.** "We processed X events for $Y" is a real metric.
- **Cost is a code review concern.** PR includes "cost impact" line where relevant (new pipeline, new warehouse, new feature with traffic implications).

---

## Principles

- **Architecture serves use cases.** Frameworks are tools, not goals. Pick the framework that helps; ignore the rest.
- **Reversibility > perfection.** Choose architectures that can evolve. Don't lock in for theoretical optimization.
- **Loose coupling at platform boundaries.** Every component should be replaceable without rewiring everything.
- **Start with managed services.** Self-host only when justified by scale or genuine competitive need.
- **Cost is a design dimension.** Not an afterthought. FinOps mindset from day 1.
- **Migration is iterative, never big-bang.** Strangler Fig as default for any nontrivial migration.
- **Document architecture decisions in ADRs.** Future you (and your successors) deserve to know *why*.

---

## Anti-Patterns

### Big-Bang Migration

**Looks like:** "We'll cut over the entire warehouse on March 31st."

**Why it fails:** Risk concentrates. Rollback is painful. Bugs surface in production with no fallback.

**The fix:** Strangler Fig. Migrate workload by workload. Both systems live in parallel during transition.

### Cargo-Culted Modern Data Stack

**Looks like:** "Everyone has Snowflake + dbt + Fivetran + Looker, so we need them too." No analysis of fit.

**Why it fails:** MDS is great for many; expensive overkill for some, insufficient for others. Tool-first thinking.

**The fix:** Use case → access patterns → tool. The MDS may be right; verify rather than assume.

### Premature Data Mesh

**Looks like:** 30-person company adopting "Data Mesh" because it's trendy. No domain teams. No platform.

**Why it fails:** Data Mesh requires significant platform engineering investment and clear domain boundaries. Below ~100 engineers, central is faster and cheaper.

**The fix:** Centralized data team until pain of central is real. Then Data Mesh is justified.

### Lambda Without Pain

**Looks like:** Adopting Lambda Architecture because "we need real-time and accurate." Two codepaths. Tons of complexity.

**Why it fails:** Maintaining two transformation pipelines doubles the work. Drift accumulates.

**The fix:** Kappa with Apache Beam (or similar unified API). Or: question whether real-time is actually needed; near-real-time on MDS often suffices.

### Build-Everything Mentality

**Looks like:** Custom data quality framework. Custom orchestrator. Custom transformation engine. All written in-house.

**Why it fails:** TCO is enormous. Engineers leave; tooling rots. You're maintaining commodity tools poorly.

**The fix:** Buy or adopt OSS for everything that's commodity. Build only the truly differentiated 5%.

### Cloud Lock-In Without Eyes Open

**Looks like:** Adopting AWS-specific services across the stack with no abstraction. Three years later: cost-prohibitive to leave.

**Why it fails:** Reversibility is gone. Pricing leverage is gone.

**The fix:** Use cloud services (they're great), but keep core data in open formats (Parquet, Iceberg) and use portable abstractions (Kubernetes, Terraform, dbt) where reasonable.

### Architecture Document That Nobody Reads

**Looks like:** 80-page Word doc from 2 years ago describing the architecture. Nobody updates it. Reality has drifted.

**Why it fails:** Stale docs are worse than no docs — they actively mislead.

**The fix:** ADRs (Architecture Decision Records) for individual decisions, kept in version control. Architecture diagrams as code. Owned by the team, not by an architect.

---

## Decision Rules

| Situation | Action |
|---|---|
| Greenfield platform, < 100 engineers | Modern Data Stack (Snowflake/BQ + Fivetran/Airbyte + dbt + Looker/Mode) |
| Greenfield, 100+ engineers, multiple domains | MDS centrally, plan toward Data Mesh in 2 years |
| Real-time analytics is genuinely required | Live Data Stack (Kafka + Flink/Materialize + streaming-friendly storage) |
| Real-time is "nice to have" | MDS with hourly batches. Don't take on streaming complexity. |
| Migrating legacy DW | Strangler Fig. No big-bang weekends. |
| Self-hosting question | Manage > self-host unless data is in exabytes or strict regulatory pin. |
| Cost surging | Establish FinOps practice. Tag everything. Engineer-visible cost dashboards. |
| Tool sprawl | Audit by undercurrent. Likely 4 tools doing what 1 should. Consolidate. |
| Vendor pitch with 3-year contract | Negotiate 1-year. Reversibility wins. |
| "Should we build X" | Default no. Compute 3-year TCO of build vs buy. Build only if competitive advantage. |
| Lambda vs Kappa decision | Default Kappa with Beam. Lambda only if streaming infra is genuinely insufficient. |
| Architecture review cadence | Quarterly. Always Be Architecting. |

---

## Worked Example: Choosing a Stack for a Series-B Startup

**Context:** 80-person company, B2B SaaS, $5M ARR. Needs analytics for execs, product team, customer success. No data platform yet.

**Selection process:**

| Decision | Choice | Why |
|---|---|---|
| Architectural pattern | Modern Data Stack | Right scale; team is small; speed-to-value matters more than novelty |
| Storage | Snowflake | Best-of-breed cloud DW; per-second compute pricing fits spiky workloads |
| Ingestion | Fivetran for SaaS sources; custom for app DB CDC (Debezium) | Buy commodity; build the differentiated piece |
| Transformation | dbt | Industry standard; SQL-native; strong ecosystem |
| Orchestration | dbt Cloud (initially); Airflow when complexity grows | Don't over-engineer; defer complexity |
| BI | Looker | Semantic layer matters; LookML is reusable |
| Reverse ETL | Hightouch | Operational analytics back to SaaS — saves CS team work |
| Cost | Tag every Snowflake warehouse by team. Auto-suspend at 1 min. | FinOps from day 1. |
| Streaming? | NO | No genuine sub-second use case. Defer until we have one. |
| Data Mesh? | NO | Too small. Centralize. Revisit at 200 engineers. |

**Total ~$15K/month at this scale.** Documented in 6 ADRs. Revisit annually.

**Lesson:** The MDS is the safe answer for most companies in this size range. Resist the urge to build differentiated tooling on commodity needs.

---

## Gotchas

- **Cloud architecture frameworks overlap.** AWS Well-Architected and Google's Five Principles are 80% the same content with different framings. Pick one for your team's vocabulary.
- **TOGAF is overkill for most data teams.** It's an enterprise architecture framework. Use only if your enterprise is already TOGAF-aligned.
- **DAMA-DMBOK is comprehensive but dense.** Use as a reference for governance topics, not a beach read.
- **Lambda's complexity tax is underestimated.** People who advocate Lambda haven't maintained two codepaths through 3 years of schema changes.
- **Data Mesh ≠ "no central team."** Mesh requires a central platform team that's stronger than most companies' central data teams.
- **MDS lock-in is real.** Each vendor is fine alone; together they form a stack you can't easily leave.
- **Strangler Fig requires upfront routing investment.** It's not free. But it's the safest way to migrate.
- **FinOps without engineer involvement fails.** Finance teams don't know what to cut. Cost telemetry must reach the engineer who can act.

---

## Further Reading

- *Fundamentals of Data Engineering* by Reis & Housley, Chapters 3-4
- *Designing Data-Intensive Applications* by Martin Kleppmann (the canonical deep reference)
- AWS Well-Architected Framework documentation
- Zhamak Dehghani's original *Data Mesh Principles and Logical Architecture* posts
- See `data-engineering-lifecycle-and-principles` for the lifecycle/undercurrents context
- See `data-storage-and-modeling-patterns` for storage tier and dimensional modeling
- See `dataops-and-modern-data-platforms` for DataOps discipline + Live Data Stack details

Source: *Fundamentals of Data Engineering* (Reis & Housley), Chapters 3-4 (Architecture).
