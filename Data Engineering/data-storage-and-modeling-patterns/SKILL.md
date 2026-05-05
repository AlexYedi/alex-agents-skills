---
name: data-storage-and-modeling-patterns
description: >
  Apply data storage and modeling patterns: cache hierarchy, consistency
  paradigms (strong vs eventual), file/object/block storage, warehouse vs
  lake vs lakehouse, ingestion patterns (batch, streaming, CDC, snapshot vs
  differential), schema-on-write vs schema-on-read, dimensional modeling
  (Kimball star schema, Inmon 3NF, Data Vault), Slowly Changing Dimensions
  (SCD types 1/2/3), and distributed-query patterns (broadcast vs shuffle
  hash join, MapReduce). Use when designing storage layers, modeling a
  warehouse, choosing ingestion frequency, or evaluating a transformation
  approach. Triggers: "warehouse vs lake", "Kimball vs Inmon vs Data Vault",
  "SCD type 2", "schema on read", "CDC vs scheduled extract", "broadcast
  join", "data lakehouse", "Iceberg / Delta / Hudi". Produces a chosen
  storage architecture + data model with rationale.
---

# Data Storage and Modeling Patterns

You apply the storage architecture and dimensional-modeling toolkit from
*Fundamentals of Data Engineering*: where data lives (cache hierarchy,
warehouse, lake, lakehouse), how it gets there (ingestion patterns), and how
it's shaped for query (Kimball, Inmon, Data Vault, SCDs).

---

## When to Use This Skill

- Designing the storage layers of a new data platform
- Choosing between warehouse, lake, and lakehouse
- Picking an ingestion frequency (batch vs streaming vs CDC)
- Modeling a fact-and-dimension star schema vs Inmon vs Data Vault
- Implementing slowly-changing dimensions correctly
- Optimizing a slow distributed query
- Choosing between schema-on-write and schema-on-read for a use case

---

## The Cache Hierarchy

```
Latency:           Cost per GB:                Use:
──────────         ───────────                 ───
ns      CPU cache  Highest                     Hot inner loops
                                               (compute optimization)

100ns   RAM        High                        Active working set,
                                               in-memory caches

100μs   SSD        Moderate                    Hot data,
                                               OLTP workloads

10ms    HDD        Low                         Warm data,
                                               batch processing

50ms    Object     Very low                    Cold data, analytics,
        storage                                data lake foundation

100s+   Archival   Lowest                      Compliance retention,
        (Glacier)                              recovery
```

**Design rule:** Match data access frequency to storage tier. Frequent reads on cold storage = expensive. Infrequent reads on hot storage = wasteful.

**Reverse cache pattern:** Object storage as the system-of-record; warmer caches (SSD, RAM) hold derived/queried views. Common in modern lakehouses.

---

## Storage Categories

### File Storage

- Finite-length files; append + random access
- Hierarchical (directories)
- POSIX semantics (mostly)
- Examples: NFS, EFS, EBS

**Use when:** Tools require file semantics (legacy ETL, on-prem analytics).

### Object Storage

- Key-value: bucket + object key → blob
- Objects are **immutable** — overwrite = full rewrite
- Massive scalability, eleven 9s of durability
- Examples: S3, GCS, Azure Blob

**Use when:** Modern lakehouses. Data lake foundation. Backup/archival. Analytics on cold data.

### Block Storage

- Raw disk blocks (LUN-style)
- Database engines build their own filesystems on top
- Examples: EBS, Persistent Disks

**Use when:** Backing OLTP databases, custom storage engines.

### Database-Specific (Columnar, Row, Document, KV, Graph)

Specialized for query patterns. Don't confuse storage tier with database type — a columnar DB sits on object storage internally.

---

## Warehouse vs Lake vs Lakehouse

| | Data Warehouse | Data Lake | Data Lakehouse |
|---|---|---|---|
| Storage | Proprietary or columnar (DW vendor) | Object storage, raw files | Object storage + open table format (Iceberg / Delta / Hudi) |
| Schema | Schema-on-write (strict) | Schema-on-read (flexible) | Schema enforced via table format, but flexible underneath |
| Update support | Yes | No (rewrites only) | Yes (ACID via table format) |
| Cost (storage) | High | Low | Low |
| Query speed | Fast (optimized) | Slow (scan-heavy) | Approaching warehouse for properly modeled tables |
| Best for | Curated analytics, BI | Raw landing, exploration, ML training data | Both — the convergence pattern |

**Practical guidance (2026):** For new builds, **lakehouse with Iceberg or Delta** is the converging pattern. You get warehouse-like ACID + open formats. Snowflake, Databricks, BigQuery all support these table formats.

**Data platforms** (Snowflake, BigQuery, Databricks Lakehouse) bundle these tightly. The line between "platform" and "warehouse" is blurring.

---

## Consistency Paradigms

### Strong Consistency (ACID)

- Reads always reflect the latest write
- Distributed consensus required (Paxos, Raft)
- Latency cost
- **Use when:** Correctness > latency. Financial transactions, OLTP.

### Eventual Consistency (BASE)

- Writes propagate; reads may temporarily be stale
- No consensus, no latency tax
- **Use when:** Latency-sensitive analytics, social-media-style reads, distributed caches.

**Most analytics is fine with eventual consistency.** Fighting for strong consistency where it isn't needed is a common over-engineering mistake.

---

## Ingestion Patterns

### Frequency Spectrum

```
SLOW                                                              FAST
────                                                              ────

Annual    Monthly    Daily    Hourly    Minutes    Seconds    Sub-second
batch     batch      batch    batch     micro-     real-time   true real-time
                                        batches    streaming
```

**Reality check:** Most "real-time" requirements collapse to "near-real-time" (1-10 min) on close inspection. Sub-second is genuinely required only for trading, fraud detection, operational alerting.

### Batch Patterns

| Pattern | Mechanics | When |
|---|---|---|
| Time-interval | Daily / hourly schedule pulls | Standard reporting; predictable load |
| Size-based | Process when N events / N bytes accumulated | Continuous data with bursty volume |
| Snapshot | Full state of source dumped each cycle | Small dimensions; sources without change tracking |
| Differential | Only what changed since last run | Large fact tables; sources with timestamps or CDC |

### Streaming Patterns

| Pattern | Mechanics |
|---|---|
| **CDC (Change Data Capture)** | Read database logs (binlog, WAL); emit change events as a stream. Near-real-time replication. Tools: Debezium, Fivetran HVR. |
| **Message queue** | Publisher → queue → consumer. Each message delivered once. Ordering may not be guaranteed. (RabbitMQ, SQS) |
| **Event-streaming platform** | Append-only log. Consumers read at their own pace. Replay is supported. (Kafka, Pulsar, Kinesis) |

**Choosing CDC:** When the source is a database, CDC is almost always better than scheduled SELECTs. Lower latency, lower load on source, captures deletes (which polling misses).

---

## Schema Strategies

### Schema-on-Write

- Schema defined and enforced at ingestion
- Failed writes for malformed data
- Best for: curated layers, marts, governed data

### Schema-on-Read

- Data written as-is; structure imposed at query time
- Maximum flexibility
- Best for: raw landing zones, exploration, semi-structured data

**Modern pattern:** Layered storage. **Bronze** (raw, schema-on-read) → **Silver** (cleaned, schema enforced) → **Gold** (curated, modeled, schema-on-write). Each layer has appropriate strictness.

---

## Dimensional Modeling

### Kimball — Star Schema

```
                    ┌──────────────┐
                    │  dim_date    │
                    └──────┬───────┘
                           │
┌──────────────┐    ┌──────▼───────┐    ┌──────────────┐
│ dim_customer ├───►│  fact_orders │◄───┤ dim_product  │
└──────────────┘    └──────┬───────┘    └──────────────┘
                           │
                    ┌──────▼───────┐
                    │  dim_store   │
                    └──────────────┘
```

**Structure:**
- **Fact tables** at the center: quantitative, immutable, append-only events at the lowest grain (one row per business event).
- **Dimension tables** around: descriptive context (who/what/when/where).
- **Conformed dimensions:** shared across fact tables for cross-process analysis.

**Pros:** Query-fast, intuitive for BI users, well-supported by tools.

**Cons:** Denormalized; storage redundancy (acceptable in cheap-storage era).

**When:** Default for analytics. Most data warehouses end up roughly Kimball-shaped even when they didn't start that way.

### Inmon — Subject-Oriented 3NF

**Structure:** Highly normalized (3NF) central warehouse. Department-specific *data marts* derived as denormalized views.

**Pros:** Single source of truth; minimal redundancy.

**Cons:** Complex; queries against the warehouse are slow without marts; modeling overhead is significant.

**When:** Large enterprises with strong governance and clear data ownership. Increasingly rare in cloud-native shops.

### Data Vault

```
HUBS         LINKS                   SATELLITES

[H_Customer]                         [S_Customer_Profile]
  hash_key     [L_Customer_Order]    [S_Customer_Address]
  business_key   hash_key            
  load_date      hub_keys            [S_Order_Status]
  source         load_date           [S_Order_Items]
                 source
[H_Order]
  hash_key
  business_key
```

**Structure:** Three table types:
- **Hubs:** unique business keys with metadata (load date, source). Insert-only.
- **Links:** relationships between hubs.
- **Satellites:** descriptive attributes for hubs / links, time-stamped.

**Pros:** Insert-only (high concurrency), audit-friendly (everything is timestamped), easy to add sources.

**Cons:** Complex; more joins for queries; usually needs a presentation layer (often Kimball-shaped marts) on top.

**When:** Highly regulated environments (banking, healthcare). Multi-source integration where audit trail matters. Probably overkill for most product companies.

---

## Slowly Changing Dimensions (SCD)

How to handle dimension attributes that change over time (e.g., customer changes address).

| Type | Mechanism | History? | When |
|---|---|---|---|
| **Type 1** | Overwrite | No | Attribute changes don't matter historically. Simplest. |
| **Type 2** | New row per change, with effective date range | Full | Standard for any analytics that depends on point-in-time correctness. **Default choice.** |
| **Type 3** | Add a "previous value" column | Limited | Rare; useful only when comparing exactly current vs previous. |

**Type 2 in practice:**

```sql
customer_id   name    address      effective_from  effective_to    is_current
1            Alice   "Old Addr"   2024-01-01      2024-06-15      false
1            Alice   "New Addr"   2024-06-15      9999-12-31      true
```

Joins to fact tables use effective date ranges. dbt has good support; many cloud DWs have helpers.

---

## Distributed Query Patterns

### Broadcast Join

```
Driver
  │
  ├── Send small_table to all nodes
  ▼
[Node 1]    [Node 2]    [Node 3]
 large_part  large_part  large_part
 + small     + small     + small
 → join      → join      → join
```

**When:** One side fits in memory of every node (typically < ~10 GB).

**Cost:** Network bandwidth × number of nodes.

### Shuffle Hash Join

```
[Node 1]    [Node 2]    [Node 3]
 left_part   left_part   left_part
 right_part  right_part  right_part
        │       │       │
        └───shuffle by key────┘
        ▼       ▼       ▼
   [Node 1]  [Node 2]  [Node 3]
   (rows w/  (rows w/  (rows w/
    keys     keys      keys
    A,B,C)   D,E,F)    G,H,I)
   → join   → join    → join
```

**When:** Both sides are large; neither fits in node memory.

**Cost:** Massive network shuffle. Often the dominant cost in big-data joins.

**Optimization:** If one side is much smaller, force broadcast. If shuffle is unavoidable, partition source data by join key to minimize movement.

### MapReduce (the conceptual pattern)

```
INPUT → [Map tasks] → SHUFFLE (by key) → [Reduce tasks] → OUTPUT
```

Map: parallel transform of input chunks.
Shuffle: redistribute by key.
Reduce: aggregate per key.

**Modern incarnations:** Spark, Flink, BigQuery, Snowflake all use variants of this. Hadoop's original MapReduce is largely retired.

---

## Update Patterns (for Transformations)

| Pattern | Mechanics | When |
|---|---|---|
| **Truncate and reload** | Drop target; rerun full transformation | Small dimensions; idempotent transformations |
| **Insert only** | Append new rows; query "latest by primary key" | Audit-heavy environments; immutable history |
| **Upsert / Merge** | Match keys; update existing, insert new | The default for incremental fact tables |

**Iceberg / Delta / Hudi** all support full ACID merges, removing the historical tradeoff between "data lake" and "incremental updates."

---

## Principles

- **Storage tier matches access pattern.** Hot data on hot storage. Cold data on cold storage. Stop overpaying.
- **Object storage is the new system-of-record for analytics.** Lakehouse table formats (Iceberg, Delta, Hudi) are how to make it queryable.
- **Schema-on-write at gold layer; schema-on-read at bronze.** Layered strictness.
- **CDC > scheduled SELECTs** when the source is a database.
- **Default to Kimball star schema for analytics.** It's the common path for a reason.
- **SCD Type 2 by default** for dimensions where history matters (which is most of them).
- **Don't fight for strong consistency** in analytics where eventual is sufficient.
- **Sub-second real-time is rare.** Most "real-time" requirements collapse to near-real-time on close inspection.
- **Sensitive data needs deliberate handling** at every layer. Tokenization, masking, access control. Don't punt to "we'll add it later."

---

## Anti-Patterns

### One Storage Tier for Everything

**Looks like:** Everything in expensive Snowflake. Or everything in S3 with no warehouse.

**Why it fails:** Workloads have different access patterns. Forcing one tier overpays for some, underdelivers for others.

**The fix:** Layered storage. Hot path (DW or Materialize). Warm path (lakehouse on S3 with Iceberg). Cold path (S3 IA / Glacier).

### Schema-on-Read Everywhere

**Looks like:** Raw JSON in S3, queried directly by analysts. No structure ever imposed.

**Why it fails:** Every query reinvents schema interpretation. Drift goes undetected. Performance is bad.

**The fix:** Bronze is schema-on-read; silver and gold are schema-on-write. Promote data through layers as it's understood.

### Type 1 SCD When You Need Type 2

**Looks like:** "Update" the dimension when an attribute changes. History is gone.

**Why it fails:** Analytics depending on point-in-time correctness silently break. "Customer's region last year" is no longer queryable.

**The fix:** Type 2 by default. Storage is cheap.

### Polling Source DBs Instead of CDC

**Looks like:** Nightly `SELECT * FROM orders WHERE updated_at > <last_run>`. Misses deletes. Heavy load on source.

**Why it fails:** Deletes vanish silently. Source DB pays a perf cost. Latency is hours, not seconds.

**The fix:** CDC via Debezium or a managed equivalent (Fivetran HVR, AWS DMS).

### Storing PII Everywhere

**Looks like:** Raw PII in bronze, silver, gold. Test environments. Analyst notebooks.

**Why it fails:** Compliance bomb. Breach blast radius is enormous.

**The fix:** Tokenize / hash at ingestion. Hold raw PII only in a single, gated location with audited access. Mask in lower environments.

### Premature Real-Time

**Looks like:** "We need real-time analytics" → Kafka + Flink + Materialize built before any use case requires sub-second.

**Why it fails:** Streaming infrastructure is 10x the operational burden. Premature investment that nobody uses.

**The fix:** Hourly batch first. Validate that real-time is genuinely needed before adopting streaming. Most BI workloads aren't.

### Ignoring Skew in Distributed Joins

**Looks like:** Big shuffle join. One key has 90% of the data. One node does all the work. Job runs 10x slower than expected.

**Why it fails:** Skew defeats parallelism. Slowest node = slowest query.

**The fix:** Detect skew (most engines have hints). Salt skewed keys. Or pre-aggregate the heavy key separately.

### Treating Object Storage Updates as Cheap

**Looks like:** Updating a Parquet file by rewriting it on every change. Massive S3 PUT bills.

**Why it fails:** Object storage is immutable. "Update" = full rewrite. Frequent updates = frequent full file rewrites.

**The fix:** Use a table format (Iceberg, Delta, Hudi) that handles incremental updates as small delta files + compaction. Or batch updates to amortize the rewrite cost.

---

## Decision Rules

| Situation | Action |
|---|---|
| New analytics platform, 2026 | Lakehouse on Iceberg / Delta. Snowflake or Databricks tightly integrated. |
| Need ACID + open format | Iceberg or Delta, not raw Parquet. |
| Source is a database, need analytics ingestion | CDC (Debezium / Fivetran HVR / AWS DMS). Not scheduled SELECTs. |
| Dimension changes need history | SCD Type 2. Default. |
| Modeling default | Kimball star schema unless audit / compliance requires Data Vault. |
| Heavily-regulated industry | Data Vault for raw layer; Kimball marts on top. |
| "We need real-time" | Verify sub-second is required. Usually it isn't. Batch hourly until it is. |
| Storage cost surging | Audit access patterns. Move cold tables to cheaper tier. |
| Slow distributed join | Check skew first. Then check broadcast eligibility. Pre-aggregate hot keys. |
| Choosing schema-on-write vs read | By layer: bronze read, silver/gold write. |
| PII in bronze layer | Tokenize / hash at ingestion. Don't propagate raw. |
| Big bang dimension reload | Truncate-reload only for small dims. Use upsert/merge for large fact tables. |

---

## Worked Example: Modeling a SaaS Product's Analytics

**Context:** B2B SaaS, ~100K customers, ~10M events/day. Need product analytics, customer health scoring, exec dashboards.

**Layers:**

```
Source systems              Storage                 Modeling
──────────────              ───────                 ────────

Postgres (app DB)    →  Bronze: S3 + Iceberg    →  Silver: dbt models
                          (CDC via Debezium)         (cleaned, typed,
                                                      deduplicated)
SaaS (Stripe,        →  Bronze: S3 + Iceberg    →  
HubSpot, Zendesk)        (Fivetran)
                                                  →  Gold: dbt models
                                                      (Kimball star schema)
Product events       →  Bronze: S3 + Iceberg
(Segment / RudderStack)  (event log)               
                                                      ↓
                                                  Snowflake views
                                                      ↓
                                                   Looker

PII handling: tokenized at ingestion; raw kept only in gated bronze
```

**Modeling — Gold layer (Kimball):**

```
fact_product_events    (one row per user action)
fact_subscriptions     (one row per subscription change)
fact_invoices          (one row per Stripe invoice)

dim_customer           (SCD Type 2)
dim_user               (SCD Type 2)
dim_subscription_plan  (SCD Type 1 — plans rarely change retroactively)
dim_date               (standard)
dim_geography          (standard)
```

**Updates:**
- Fact tables: append-only with upsert for late-arriving events
- Dimensions: SCD Type 2 via dbt snapshots

**Result:** Analysts query gold star schema in Looker. Bronze available for raw exploration. Three-layer flow that survives growth.

---

## Gotchas

- **Iceberg vs Delta vs Hudi:** All three solve the same problem (ACID on object storage); ecosystem differs. Iceberg has broader engine support; Delta is Databricks-led; Hudi excels at high-update workloads.
- **Snowflake's "lake-like" features**: Snowflake supports external tables on Iceberg. You can keep data on S3 and query from Snowflake — useful for some hybrid setups.
- **CDC is not free.** Source DB has to expose logical replication or binlog access. Some legacy DBs make this painful or impossible.
- **Compaction matters.** Iceberg / Delta / Hudi accumulate small files; periodic compaction is required for query performance.
- **Strong consistency in distributed analytics is a red flag.** Most analytics is fine eventually consistent; demand for strong consistency usually means a use case is actually OLTP.
- **Star schema with too many dimensions** (snowflake schema) loses the speed advantage. Keep it flat.
- **Type 2 SCD with dbt snapshots requires a stable "valid_from" / "valid_to" column convention.** Don't roll your own; use dbt's snapshot.
- **Distributed joins on object storage are slow.** Lakehouse tables joined directly in Spark/Trino can be slow; promoting hot tables into a warehouse layer for serving is common.

---

## Further Reading

- *The Data Warehouse Toolkit* by Kimball — the canonical reference for star-schema modeling
- *Building the Data Warehouse* by Inmon — the original Inmon approach
- *Building a Scalable Data Warehouse with Data Vault 2.0* — for Data Vault deep dive
- *Designing Data-Intensive Applications* by Kleppmann — for distributed query patterns and consistency
- See `data-architecture-frameworks` for the higher-level frameworks (MDS, Lakehouse, Data Mesh)
- See `dataops-and-modern-data-platforms` for operational practices around the model

## Related Skills

This skill is **analytics-side** modeling (Kimball / Inmon / Data Vault, SCDs,
ingestion). For **OLTP-side** distributed databases — NoSQL data models,
sharding, CAP, replication, consensus — see the Gorton-derived skills:

- `scalable-database-design-and-sharding` — NoSQL data models, sharding,
  replication, CAP
- `eventual-consistency-mechanics` — RYOWs, quorums, version vectors, CRDTs
- `consensus-and-strong-consistency` — 2PC, Paxos, Raft, linearizability
- `event-streaming-with-kafka` — event log as system of record
- `stream-processing-with-flink` — real-time stream analytics

Source: *Fundamentals of Data Engineering* (Reis & Housley), Chapters 5-8
(Storage, Ingestion, Transformation). For OLTP distribution and consistency,
*Foundations of Scalable Systems* (Gorton) is distilled in
`Software Development/references/foundations-of-scalable-systems/`.
