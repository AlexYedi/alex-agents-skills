# Fundamentals of Data Engineering — Frameworks Catalog

## Index (Alphabetical)

| Name | Domain | One-line |
|---|---|---|
| Apache Beam / Dataflow Model | Streaming | Unified API for bounded + unbounded data |
| AWS Well-Architected | Architecture | Six-pillar cloud architecture review framework |
| BASE (Eventual Consistency) | Storage | Consistency tradeoff for scaling |
| Build vs Buy | Architecture | Strategic value × build cost decision |
| Cache Hierarchy | Storage | CPU → RAM → SSD → HDD → Object → Archive tiers |
| Change Data Capture (CDC) | Ingestion | Replicate DB changes via log reading |
| Cloud-Native (Google's 5) | Architecture | Automation, state, managed services, depth, architecting |
| Conformed Dimensions | Modeling | Shared dimensions across fact tables |
| Containers | Compute | Lightweight isolation for processes |
| CRUD vs Insert-Only | Modeling | Transactional vs append patterns |
| DAMA-DMBOK | Architecture | Data management body of knowledge |
| Data Engineering Lifecycle | Discipline | Generation → Storage → Ingestion → Transformation → Serving |
| Data Lake | Storage | Raw data on object storage |
| Data Lakehouse | Storage | Lake + warehouse via open table format |
| Data Mart | Modeling | Department-specific denormalized views |
| Data Maturity Model | Discipline | Starting / Scaling / Leading |
| Data Mesh | Platform | Decentralized domain-owned data products |
| Data Vault | Modeling | Hubs + Links + Satellites |
| Data Warehouse | Storage | Curated, structured analytics storage |
| DataOps | Discipline | DevOps for data |
| Dimensional Modeling (Kimball) | Modeling | Star schema with facts and dimensions |
| Distributed Joins | Query | Broadcast vs Shuffle Hash |
| Event-Streaming Platform | Ingestion | Append-only log (Kafka, Pulsar) |
| Fact Tables | Modeling | Append-only event records at lowest grain |
| File Storage | Storage | Hierarchical, finite-length files |
| FinOps | Discipline | Cost discipline as a continuous practice |
| Inmon Data Warehouse | Modeling | 3NF central warehouse + denormalized marts |
| Kappa Architecture | Processing | Streaming-first; batch as special case |
| Kimball Data Model | Modeling | Star schema with conformed dimensions |
| Lambda Architecture | Processing | Speed (streaming) + batch layers merged |
| Live Data Stack | Platform | Streaming-first end-to-end |
| MapReduce | Compute | Map → Shuffle → Reduce parallel pattern |
| Message Queue | Ingestion | Publisher → consumer; once-delivered |
| Modern Data Stack (MDS) | Platform | Cloud DW + ELT + dbt + BI + Reverse ETL |
| Modular Architecture | Compute | Decoupled components via APIs |
| Monolith | Compute | Self-contained system; one codebase |
| Object Storage | Storage | Bucket + key; immutable; massive scale |
| Reverse ETL (BLT) | Platform | Push DW data back to operational SaaS |
| Schema-on-Read | Storage | Structure imposed at query time |
| Schema-on-Write | Storage | Structure enforced at ingest |
| Semantic Layer | Platform | Single source of truth for metrics |
| Serverless | Compute | Code on demand; no server mgmt |
| Slowly Changing Dimensions (SCD) | Modeling | Type 1/2/3 history-handling strategies |
| Snowflake Schema | Modeling | Normalized variant of star schema |
| Star Schema | Modeling | Central fact table + dimension tables |
| Strangler Fig | Migration | Incrementally replace legacy components |
| Streaming DAG | Orchestration | Dependency graph for streaming workflows |
| TOGAF | Architecture | Enterprise architecture framework |
| Type A vs Type B Data Engineer | Discipline | Abstraction vs custom-build orientations |
| Undercurrents (6) | Discipline | Security, governance, DataOps, architecture, orchestration, SE |
| Update Patterns | Modeling | Truncate-reload / insert-only / upsert-merge |

## Detailed Catalog

### Data Engineering Lifecycle
**Origin:** Reis & Housley's organizing framework.
**Structure:** Generation → Storage → Ingestion → Transformation → Serving. Storage spans all stages.
**When:** Planning a platform; debugging an outage upstream/downstream; aligning a team.
**Cross-refs:** Undercurrents (cross-cutting concerns).

### Undercurrents (6)
**Origin:** Reis & Housley.
**Structure:** Security, Data Management, DataOps, Data Architecture, Orchestration, Software Engineering — concerns that span every lifecycle stage.
**When:** Diagnosing a failing data team. Audit each undercurrent independently.
**Cross-refs:** Lifecycle (the stages); 9 Architecture Principles (the design ideals).

### Data Maturity Model
**Origin:** Reis & Housley distillation.
**Structure:** Starting (ad hoc) → Scaling (formal practices) → Leading (mature, often Mesh).
**When:** Self-assessment; org planning.
**Cross-refs:** Undercurrents (maturity is per-undercurrent, not single-axis).

### Type A vs Type B Data Engineer
**Origin:** Reis & Housley.
**Structure:** Type A = Abstraction-oriented (composes managed services). Type B = Build-oriented (custom platforms).
**When:** Hiring. Job description writing. Team composition.
**Cross-refs:** Internal-facing vs External-facing classification.

### AWS Well-Architected Framework
**Origin:** AWS, formalized 2015.
**Structure:** Six pillars — Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.
**When:** Architecture review checklist.
**Cross-refs:** Google Cloud's Five Principles (overlapping content).

### Google Cloud Five Principles for Cloud-Native
**Origin:** Google Cloud, formalized ~2018.
**Structure:** Design for automation; smart with state; favor managed services; defense in depth; always be architecting.
**When:** Architecture decisions on GCP or any cloud.
**Cross-refs:** AWS Well-Architected; Reis & Housley's 9 principles.

### Lambda Architecture
**Origin:** Nathan Marz, ~2011.
**Structure:** Two paths — speed layer (streaming, real-time, lossy) + batch layer (slow, accurate). Merged at serving.
**When:** Established big data platforms with both real-time and accurate-historical needs.
**Cross-refs:** Kappa (the simpler successor); Apache Beam (unifies them).
**Caveats:** Two codepaths to maintain. High complexity tax.

### Kappa Architecture
**Origin:** Jay Kreps (LinkedIn), 2014.
**Structure:** Single streaming pipeline. Batch is just streaming with infinite retention. Replay-based historical analytics.
**When:** Streaming-native teams; modern stacks; unified codepath preferred.
**Cross-refs:** Lambda; Apache Beam / Dataflow Model.

### Apache Beam / Dataflow Model
**Origin:** Google Cloud Dataflow paper, 2015; open-sourced as Apache Beam.
**Structure:** Unified API for bounded (batch) and unbounded (streaming) data. Windows + watermarks + triggers.
**When:** Writing pipelines that should run identically in batch and streaming modes.
**Cross-refs:** Kappa (Beam makes Kappa practical).

### Modern Data Stack (MDS)
**Origin:** Industry pattern, ~2018-2020.
**Structure:** Cloud DW center (Snowflake/BQ/Redshift/Databricks) + ELT (Fivetran/Airbyte) + dbt + BI + Reverse ETL.
**When:** Most companies, most use cases. Default for greenfield.
**Cross-refs:** Live Data Stack (the streaming successor); Data Mesh (decentralization).

### Live Data Stack
**Origin:** Reis & Housley framing of the streaming-first pattern.
**Structure:** Streaming sources + streaming storage (Kafka + Iceberg) + streaming compute (Flink, Materialize) + serving layer.
**When:** Real-time analytics genuinely required; streaming-native team.
**Cross-refs:** MDS; Kappa.

### Data Mesh
**Origin:** Zhamak Dehghani (ThoughtWorks), 2019.
**Structure:** Decentralized. Domain teams own data end-to-end as products with SLAs. Central platform team provides infrastructure.
**Four principles:** domain ownership, data as product, self-serve platform, federated computational governance.
**When:** Large organizations (typically 100+ engineers); central data team bottlenecked.
**Cross-refs:** MDS (pre-Mesh state); FinOps (cost decentralization).

### Strangler Fig Pattern
**Origin:** Martin Fowler, 2004 (general migration); Reis & Housley apply to data.
**Structure:** Wrap legacy system; route portions to new components; shrink legacy until decommissioned.
**When:** Any legacy migration. DW migrations especially.
**Cross-refs:** Reversibility (Principle 7).

### TOGAF
**Origin:** The Open Group, 1995.
**Structure:** Enterprise architecture framework spanning business, application, data, technology layers.
**When:** Large enterprises with formal architecture practice.
**Caveats:** Overkill for most data teams.

### DAMA-DMBOK
**Origin:** Data Management Association International.
**Structure:** Comprehensive reference for data management as a discipline. Architecture is one chapter.
**When:** Establishing formal data management practice. Defining CDO role.

### Cache Hierarchy
**Structure:** CPU cache (ns) → RAM (100 ns) → SSD (100 µs) → HDD (10 ms) → Object Storage (50 ms) → Archive (100s+).
**When:** Selecting storage tier per workload.
**Cross-refs:** File / Object / Block storage.

### File Storage / Object Storage / Block Storage
**Distinctions:** File = hierarchical (NFS, EFS). Object = bucket+key, immutable (S3, GCS). Block = raw disk for DB engines (EBS).
**When:** Object is the modern default for analytics; file for legacy interop; block for backing OLTP DBs.

### Strong vs Eventual Consistency (BASE)
**Strong:** Reads always reflect latest write. Distributed consensus required. Latency tax.
**Eventual (BASE):** Best-effort consistency. Allows for soft state and basic availability. No consensus.
**When:** Most analytics is fine eventual. Strong is for transactional / financial.

### Data Warehouse / Data Lake / Data Lakehouse
**Warehouse:** Schema-on-write, structured, expensive, fast.
**Lake:** Schema-on-read, raw, cheap, slow.
**Lakehouse:** Hybrid via open table formats (Iceberg / Delta / Hudi). The convergence pattern.

### Schema-on-Write / Schema-on-Read
**Write:** Enforce structure at ingestion. Strict, governed.
**Read:** Impose structure at query. Flexible, exploratory.
**Mixed:** Bronze (read) → Silver/Gold (write). Layered strictness.

### Ingestion Frequencies
**Spectrum:** Annual → Monthly → Daily → Hourly → Minutes → Seconds → Sub-second.
**Heuristic:** "Real-time" usually means "near-real-time" (1-10 min) on close inspection.

### Batch Patterns
**Time-interval:** Fixed schedule.
**Size-based:** Triggered by accumulated volume.
**Snapshot vs Differential:** Full state dump vs only-changes-since.

### Change Data Capture (CDC)
**Mechanism:** Read DB transaction log; emit change events.
**Tools:** Debezium (OSS), Fivetran HVR, AWS DMS.
**When:** Source is a database; near-real-time replication needed.
**Cross-refs:** vs scheduled SELECTs (which miss deletes).

### Message Queue / Event-Streaming Platform
**Queue:** Once-delivered (RabbitMQ, SQS).
**Stream:** Append-only log; replay supported (Kafka, Pulsar, Kinesis).
**When:** Queue for routing; stream for analytics + multiple consumers.

### Kimball Data Model (Star Schema)
**Origin:** Ralph Kimball, *The Data Warehouse Toolkit* (1996).
**Structure:** Central fact table (events at lowest grain) surrounded by dimension tables (descriptive context). Conformed dimensions shared across facts.
**When:** Default for analytics. Most warehouses end up Kimball-shaped.

### Inmon Data Warehouse
**Origin:** Bill Inmon, *Building the Data Warehouse* (1992).
**Structure:** Central 3NF (highly normalized) warehouse. Department-specific data marts derived as denormalized views.
**When:** Large enterprises with strong governance. Increasingly rare in cloud-native shops.

### Data Vault
**Origin:** Daniel Linstedt, ~2000.
**Structure:** Hubs (business keys) + Links (relationships) + Satellites (descriptive attributes, time-stamped). Insert-only.
**When:** Highly regulated; multi-source integration; audit-heavy.
**Caveats:** Complex; usually needs presentation layer (often Kimball marts) on top.

### Slowly Changing Dimensions (SCDs)
**Type 1:** Overwrite (no history).
**Type 2:** New row per change with effective dates (full history). **Default.**
**Type 3:** Add "previous value" column (limited history).
**When:** Any dimension where attribute changes matter for analytics.

### Distributed Joins (Broadcast vs Shuffle Hash)
**Broadcast:** Send small table to all nodes; join locally. Fast when small side fits in memory.
**Shuffle Hash:** Repartition both tables by join key. Network-heavy. Default for large+large.
**When:** Spark, BigQuery, Snowflake, Trino — all use these patterns.

### MapReduce
**Origin:** Google paper (2004); Hadoop implementation.
**Structure:** Map (parallel transform) → Shuffle (redistribute by key) → Reduce (aggregate).
**When:** Conceptual pattern underlying Spark, Flink, etc.
**Caveats:** Original Hadoop MapReduce is largely retired.

### Update Patterns
**Truncate-and-reload:** Drop target; full rebuild.
**Insert-only:** Append; query "latest by primary key."
**Upsert/Merge:** Match keys; update existing, insert new. Default for incremental fact tables.

### DataOps
**Origin:** Industry term; popularized ~2017.
**Structure:** Apply DevOps principles to data — monitoring, deployment automation, SLOs, on-call, postmortems.
**When:** Always. Foundational undercurrent.

### FinOps
**Origin:** Cloud cost management discipline; FinOps Foundation.
**Structure:** Continuous, data-driven cost management. Engineering + Finance collaboration.
**When:** Any cloud-based data platform. From day 1.
**Cross-refs:** Reis & Housley's Principle 9.

### Semantic Layer
**Structure:** Single source of truth for metric definitions. Consumed by all BI tools and downstream queries.
**Implementations:** LookML, dbt Semantic Layer, Cube, AtScale.
**When:** Multiple BI tools or multiple metric definitions drifting.

### Reverse ETL (BLT — Bidirectional Load and Transform)
**Structure:** DW → curated tables → push to operational SaaS (Salesforce, HubSpot, etc.).
**Tools:** Hightouch, Census.
**When:** Operationalize DW-modeled data in tools where business users already work.

### Analytics Engineering / Analytics-as-Code
**Discipline:** Software engineering practices applied to transformations. Version control, PRs, tests, CI/CD.
**Tooling:** dbt is the canonical implementation.
**Role:** Analytics Engineer — between data engineer and analyst.

### Build vs Buy
**Heuristic:** Default to buy. Build only if competitive advantage. Compute 5-year TCO.
**When:** Any tooling decision.

### 9 Architecture Principles (Reis & Housley)
1. Choose common components wisely
2. Plan for failure
3. Architect for scalability
4. Architecture is leadership
5. Always be architecting
6. Build loosely coupled systems
7. Make reversible decisions
8. Prioritize security
9. Embrace FinOps

## Cross-Reference Map

```
DATA ENGINEERING LIFECYCLE (Generation → Storage → Ingestion → Transformation → Serving)
                              ▲ (storage spans all)
              UNDERCURRENTS (Security, Governance, DataOps, Architecture, Orchestration, SE)
                              ▲
                  9 PRINCIPLES (1-9 above)
                              │
        ┌─────────────────────┼─────────────────────────────────────┐
        ▼                     ▼                                     ▼
  ARCHITECTURE             PROCESSING                           PLATFORMS
  FRAMEWORKS               PATTERNS                          
  - TOGAF                  - Lambda                           - Modern Data Stack
  - DAMA-DMBOK             - Kappa                            - Live Data Stack
  - AWS Well-Arch          - Beam (unifies)                   - Data Mesh
  - Google 5 (cloud-native)
  - Strangler Fig (migration)
        │                      │                                     │
        │                      │                                     │
        ▼                      ▼                                     ▼
  STORAGE                  INGESTION                            DISCIPLINE
  - Cache hierarchy        - Batch (interval, size)             - DataOps
  - Object/File/Block      - Streaming (queue, log)             - FinOps
  - Warehouse / Lake /     - CDC                                - Analytics Eng
    Lakehouse              - Ingestion frequencies              - Semantic Layer
  - Strong vs Eventual                                          - Reverse ETL
    Consistency
        │
        ▼
  MODELING                                            QUERY EXECUTION
  - Schema-on-write/read                              - Distributed Joins
  - Kimball Star Schema                                 (Broadcast / Shuffle)
  - Inmon 3NF                                         - MapReduce pattern
  - Data Vault
  - SCD Types 1/2/3
  - Update patterns
```

## How to Use This Catalog

- **Encounter a name in design discussion** → look up here
- **Choosing between two patterns** → find both, compare cross-refs
- **Architecture review** → use the cross-reference map as a coverage checklist
- **Onboarding new engineer** → walk the alphabetical index as a vocabulary list

Source: *Fundamentals of Data Engineering* (Reis & Housley, O'Reilly 2022).
