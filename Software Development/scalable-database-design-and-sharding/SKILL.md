---
name: scalable-database-design-and-sharding
description: >
  Design distributed OLTP databases - choose between scale-up vs scale-out,
  primary-secondary read replication, horizontal vs vertical partitioning,
  shared-everything vs shared-nothing, NewSQL vs NoSQL, the four NoSQL data
  models (Key-Value, Document, Wide Column, Graph), sharding strategies
  (hash, value-based, range-based, consistent hashing), and the CAP
  theorem as a tunable knob. Use when picking a database, choosing a shard
  key, modeling for NoSQL, or deciding when to denormalize. Triggers - "SQL
  vs NoSQL", "MongoDB vs Cassandra vs DynamoDB", "shard key choice",
  "consistent hashing", "CAP theorem", "denormalization for queries",
  "wide column vs document", "partition vs replication". Produces a
  concrete database choice, sharding plan, and data model.
---

# Scalable Database Design and Sharding

You design the data tier for systems that outgrow a single database server.
The choice of database (SQL vs NoSQL, which NoSQL data model, which sharding
strategy) constrains everything downstream — query patterns, consistency,
ops complexity, and migration cost. Once data is in production, schema and
distribution choices are expensive to change.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 10 + 13):
the relational scaling history, the four NoSQL data models, sharding
strategies, replication for availability, the CAP theorem, and the
real-system trade-offs of Redis / MongoDB / DynamoDB.

This skill is about **OLTP at scale**. For analytics-side modeling (Kimball
star schemas, Inmon, Data Vault, SCDs), see `data-storage-and-modeling-patterns`
in the Data Engineering folder.

---

## When to Use This Skill

- Picking a database for a new service
- Choosing a shard key for a partitioned table or collection
- Modeling data for a NoSQL store
- Deciding whether to denormalize, embed, or normalize
- Choosing replication strategy (leader-follower, leaderless)
- Diagnosing scaling problems on an existing database
- Choosing between Redis / MongoDB / DynamoDB / Cassandra / Postgres / Spanner

---

## The Scaling Lineage

```
Single DB     ──►   Bigger box     ──►   Read replicas     ──►   Sharding
(default)         (scale up)            (read scaling)         (write scaling)
                                                                       │
                                                                       ▼
                                                         ┌─────────────────────┐
                                                         │   Diverging paths   │
                                                         └─────────────────────┘
                                                                  │
                              ┌───────────────────────────────────┼───────────────────────────────────┐
                              ▼                                   ▼                                   ▼
                    Shared-everything                NewSQL / Distributed SQL                 NoSQL
                    (Oracle RAC + SAN)                (Spanner, CockroachDB,                  (Cassandra,
                                                       VoltDB, YugabyteDB)                    MongoDB,
                                                                                              DynamoDB,
                                                                                              Redis)
```

| Move | When |
|---|---|
| **Scale up** | First step. Always start here. |
| **Read replicas** | Read-heavy with stale-tolerant data |
| **Horizontal sharding** | Write-heavy beyond single-server capacity |
| **NewSQL** | Need ACID + relational + distributed |
| **NoSQL** | Need scale-out and don't need relational |

---

## SQL vs NoSQL: The Honest Picture

The "SQL vs NoSQL" framing is mostly misleading. The real questions:

1. **Do you need relational integrity / multi-row transactions?**
   - Yes → SQL (Postgres, MySQL, Spanner, CockroachDB, VoltDB)
   - No → either is fine

2. **What's your scale?**
   - Single-server fit → Postgres / MySQL is great
   - Beyond single-server → distributed (NewSQL or NoSQL)

3. **What's your query pattern?**
   - Ad-hoc analytics, joins → SQL
   - Known query patterns, key-based lookups → NoSQL fits well

4. **What's your data shape?**
   - Highly relational, fixed schema → SQL
   - Document-oriented, evolving schema → Document NoSQL
   - Time-series / wide-row → Wide-column NoSQL
   - Graph traversal → Graph DB

**Default for most product systems in 2026:** Postgres until it doesn't fit.
It scales further than people think (read replicas, partitioning, Citus
extension), and it's relational with strong consistency.

---

## Replication and Sharding (the Two Distribution Strategies)

```
Replication                      Sharding
───────────                      ────────

Same data, copied across N       Different data partitions, each
nodes for availability and       on a different node, for scale-out
read scaling.                    and write scaling.

┌─────┐  ┌─────┐  ┌─────┐        ┌─────┐  ┌─────┐  ┌─────┐
│ All │  │ All │  │ All │        │ A-G │  │ H-N │  │ O-Z │
│ data│  │ data│  │ data│        │     │  │     │  │     │
└─────┘  └─────┘  └─────┘        └─────┘  └─────┘  └─────┘

Leader-follower or leaderless.   Hash, range, or value-based.
Reads scale; writes don't.       Both reads and writes scale.

Compose: each shard typically replicated for availability.
```

### Replication Patterns

| Pattern | How it works | When to use |
|---|---|---|
| **Leader-follower (primary-secondary)** | Writes to leader; async/sync replication to followers; reads from any | The default. Most relational DBs work this way. |
| **Leaderless** | Any replica accepts writes; quorum-based reads | High availability, eventual consistency (Cassandra, Riak, DynamoDB) |
| **Multi-leader** | Multiple leaders; conflicts resolved on merge | Multi-region active-active (DynamoDB Global Tables, MongoDB sharded multi-region) |

### Sharding Strategies

| Strategy | How keys map to shards | Pros | Cons |
|---|---|---|---|
| **Hash sharding** | `hash(key) mod N` | Even distribution | No range queries; resharding is hard |
| **Consistent hashing** | Hash ring; each node owns an arc | Adding nodes redistributes only ~1/N of data | No range queries |
| **Range sharding** | Contiguous key ranges (A-G, H-N, ...) | Range queries cheap | Hot-spot risk if keys cluster |
| **Value-based** | Specific values map to specific nodes | Domain-aligned (e.g., region) | Manual; rebalancing is manual |

**Choosing a shard key:**

| Goal | Pick |
|---|---|
| Even distribution | High-cardinality, randomly-distributed values (`user_id` UUID) |
| Avoid hot shards | Avoid timestamps as primary shard key (writes pile on newest shard) |
| Locality (group related data together) | Tenant ID, user ID, customer ID |
| Cross-shard query support | Pick a key that matches your query patterns |

**Bad shard keys:**
- Monotonically increasing (timestamps, auto-increment IDs) → all writes go
  to one shard
- Low cardinality (boolean, enum) → can't distribute evenly
- Frequently changing (user's current state) → expensive resharding

**Hash tags / forced co-location:** Some systems let you co-locate related
keys (e.g., Redis hash tags `user:{42}:profile`, `user:{42}:orders` both
hash on `42`) so cross-key operations stay on one shard.

---

## CAP Theorem: A Tunable, Not a Binary

The textbook framing: under network partition, pick **C** (consistency) or
**A** (availability), not both.

The reality: most modern databases offer **knobs** that let you trade
consistency for latency request-by-request.

| DB | Knob | What it does |
|---|---|---|
| Cassandra | `consistency_level` | ONE / QUORUM / ALL / LOCAL_QUORUM per query |
| DynamoDB | `ConsistentRead=true` | Strong vs eventual on a per-read basis |
| MongoDB | `writeConcern` / `readConcern` | Per-operation durability and consistency |
| Riak | N, R, W | Per-bucket tunable quorums |
| Kafka | `acks=0/1/all` | Producer-side durability |

**The book's framing:** AP/CP labels on databases are oversimplifications.
Most provide both modes; the question is what you ask for per request.

When the network is healthy, you can have both. When it isn't, you choose.
See `eventual-consistency-mechanics` for the mechanics and
`consensus-and-strong-consistency` for what strong consistency actually costs.

---

## The Four NoSQL Data Models

```
┌──────────────────┐  ┌──────────────────┐
│ (a) Key-Value    │  │ (b) Document     │
├──────────────────┤  ├──────────────────┤
│  key  →  value   │  │  key →           │
│                  │  │   { JSON         │
│  opaque blob     │  │     document }   │
│                  │  │  ↑               │
│                  │  │  indexable       │
│                  │  │  fields          │
└──────────────────┘  └──────────────────┘

┌──────────────────┐  ┌──────────────────┐
│ (c) Wide Column  │  │ (d) Graph        │
├──────────────────┤  ├──────────────────┤
│  row key →       │  │  Nodes + edges   │
│   { col → val,   │  │   ──•══►•══►•    │
│     col → val,   │  │       ╲      ╱   │
│     ... }        │  │        •──•      │
│  2D hash map     │  │   Relationships  │
│                  │  │   are first-     │
│                  │  │   class          │
└──────────────────┘  └──────────────────┘
```

### Key-Value (KV)

| Property | Value |
|---|---|
| Model | `key → value`, opaque blob |
| Examples | Redis, DynamoDB, Riak, Memcached |
| Best for | Caches, sessions, simple lookups |
| Query | By key only |

### Document

| Property | Value |
|---|---|
| Model | `key → JSON document`, fields indexable |
| Examples | MongoDB, Couchbase, DocumentDB, Firestore |
| Best for | App-record-per-document, flexible schema |
| Query | By key + by indexed fields |

### Wide Column

| Property | Value |
|---|---|
| Model | `row key → { column → value }`, sparse 2D hash map |
| Examples | Cassandra, Bigtable, HBase, ScyllaDB |
| Best for | Time-series, write-heavy, very high throughput |
| Query | By row key + range of columns |

### Graph

| Property | Value |
|---|---|
| Model | Nodes + edges with first-class relationships |
| Examples | Neo4j, Amazon Neptune, JanusGraph, ArangoDB |
| Best for | Social graphs, fraud detection, recommendations, knowledge graphs |
| Query | Graph traversal (Cypher, Gremlin, SPARQL) |

**Hard problem:** distributing graph databases. Partitioning a graph well
(minimizing cross-node traversals) is a research-level problem. Neo4j Fabric
uses manual partitioning. Most production graph workloads are kept on a
single beefy node.

---

## Schemaless and Denormalization-for-Queries

**NoSQL stores are usually termed "schemaless"** — no upfront format
declaration. In practice, schemas exist; they just live in application
code.

**The central NoSQL design tenet:** denormalize and duplicate data so each
query reads from one place.

```
Relational (3NF)                     NoSQL (denormalized)
─────────────────                    ─────────────────────
users                                user_orders
  id, name, email                      user_id, name, email,
                                       orders: [
orders                                   {order_id, items, total},
  id, user_id, total                     {order_id, items, total},
                                         ...
order_items                            ]
  order_id, item_id, qty
                                       (one read returns
items                                   everything for the
  id, name, price                       user)
```

**The trade-off:**

| | Relational | NoSQL denormalized |
|---|---|---|
| Read paths | Joins | Single-document read |
| Write paths | Single insert | Update many places |
| Schema evolution | Migrations | Application handles old + new shapes |
| Storage | Compact | Larger (duplication) |
| Consistency | DB-enforced | App-enforced |

> "Design your NoSQL data model around the queries you need to serve —
> denormalize and duplicate."

---

## Three Real Systems (Ch 13)

### Redis (in-memory KV with rich data types)

| Property | Value |
|---|---|
| Model | KV with rich types (strings, lists, sets, sorted sets, hashes) |
| Sharding | 16,384 hash slots; assign ranges to nodes |
| Replication | Async leader-follower; **WAIT** for sync writes |
| Persistence | Snapshots (RDB) + append-only file (AOF); combine for safety |
| Transactions | `MULTI`/`EXEC` — sequence guarantee, **no rollback**, not ACID |
| Use cases | Cache, session store, rate limiter, leaderboard, pub/sub |

**Caution:** Redis primary election can promote an out-of-date replica → data
loss. Don't use as primary if data loss is unacceptable, unless you've
tuned `min-replicas-to-write` and AOF carefully.

### MongoDB (document, sharded)

| Property | Value |
|---|---|
| Model | JSON-like documents (BSON) in collections |
| Storage engine | WiredTiger (since 3.2); document-level locking, snapshot isolation |
| Topology | `mongod` (data) + `mongos` (router) + config servers (metadata) |
| Sharding | Hash-based or range-based; 64 MB chunks auto-rebalanced |
| Replication | Replica set: primary + secondaries; oplog ships to secondaries; Raft-based election |
| Transactions | ACID multi-document since v4.0 (via 2PC + snapshot isolation) |
| Write concern | `majority` is default since 5.0 (durable to majority) |
| Read preference | `primary`, `secondary`, `nearest`, etc. |

**Caution:** Minority-side primary steps down on partition; writes unavailable
until majority elects new primary.

### DynamoDB (managed KV/document)

| Property | Value |
|---|---|
| Model | KV with optional document values; partition key + sort key |
| Capacity | On-demand or provisioned (RCUs/WCUs); transactions cost 2× per item |
| Sharding | Auto; adaptive capacity rebalances partitions to match load |
| Replication | 3 replicas across AZs; leader for writes |
| Reads | Eventually consistent default; `ConsistentRead=true` for strong |
| Global tables | Multi-region multi-leader; LWW conflict resolution |
| Indexes | GSI (independent partitioning) or LSI (same partition key) |
| Transactions | ACID via 2PC, single region only |
| SLA | 99.999% global tables, 99.99% single-region |

**Caution:** Hot keys can be capped at 3K RCU / 1K WCU per partition even
with adaptive capacity. Design composite keys to avoid this.

### Choosing Among Them

| Scenario | Pick |
|---|---|
| Cache / session / leaderboard | Redis |
| Document app data, complex queries, transactions | MongoDB |
| AWS-native, fully managed, serverless-friendly | DynamoDB |
| Wide-column, high write throughput, multi-region | Cassandra |
| Graph traversal | Neo4j (single beefy node) |
| Relational + global ACID | Spanner |
| Relational + open-source distributed | CockroachDB / YugabyteDB |
| Single-server-friendly relational | Postgres (still the right answer for many systems) |

---

## Principles

- **Postgres until it doesn't fit.** It scales further than most think.
- **Design your NoSQL model around your queries.** Denormalize and
  duplicate.
- **Choose a shard key with even distribution and query alignment.**
  Avoid monotonically increasing or low-cardinality keys.
- **Sharding goes with replication.** Each shard should be replicated for
  availability; total = shards × replicas.
- **CAP is a tunable.** Most modern databases let you choose per request.
- **Don't fight for strong consistency where eventual is fine.** Most
  workloads tolerate it.
- **Multi-document transactions are expensive in a sharded world.** Design
  schemas to keep transactions partition-local.
- **Test with the join algorithm.** For high-throughput SQL, specify the
  best join method explicitly.
- **Graph databases don't auto-partition well.** Plan for a single beefy
  node or manual partitioning.

---

## Anti-Patterns

### Auto-Increment as Shard Key

**Looks like:** Sharding by primary key that auto-increments. All new writes
land on the highest-keyed shard.

**Why it fails:** Hot shard. Other shards idle.

**The fix:** Hash the key first, or use a UUID-based key.

### Joins Across Shards

**Looks like:** Application-level joins between data on different shards.
Latency and cost balloon.

**Why it fails:** Each join may pull from many shards.

**The fix:** Co-locate joinable data via shared shard key, or denormalize.

### "We'll add sharding later"

**Looks like:** Schema designed without a shard key. When scale demands
sharding, every table needs a migration.

**Why it fails:** Resharding live data is painful.

**The fix:** Pick a shard key from day 1 even if you only have one shard.
Design schemas to make it easy.

### MongoDB Without WiredTiger

**Looks like:** Legacy MongoDB on MMAPv1 storage engine. Coarse locking;
contention under load.

**Why it fails:** MMAPv1 was abandoned for a reason.

**The fix:** WiredTiger (default since 3.2). Older clusters: migrate.

### Redis as Primary Store

**Looks like:** Application data lives only in Redis. Crash → data loss.

**Why it fails:** In-memory store; persistence is best-effort even with AOF.

**The fix:** Persistent backing store + Redis as cache. Or accept the
tradeoff explicitly with AOF `always` fsync (and lose throughput).

### DynamoDB Hot Partition

**Looks like:** Key design that puts heavy load on one partition key.
DynamoDB caps at 3K RCU / 1K WCU per partition; adaptive capacity helps
but won't save you.

**Why it fails:** Single partition limit.

**The fix:** Composite key with high-cardinality partition key. Sharded
write keys (write-heavy) like `partition = base_key#shard_index`, then
`shard_index = random(0, N)`.

### Trying to Strongly-Consistency Everything

**Looks like:** All reads in DynamoDB use `ConsistentRead=true`. RCU usage
doubles. Bill spikes.

**Why it fails:** Strong consistency costs more capacity. Most reads are
fine eventual.

**The fix:** Use strong consistency only where stale reads cause real
problems.

---

## Decision Rules

| Situation | Action |
|---|---|
| Greenfield, single-server fit | Postgres |
| Greenfield, AWS-native, key-value access | DynamoDB |
| Document model, complex queries | MongoDB |
| Time-series / write-heavy / multi-DC | Cassandra |
| Graph traversal | Neo4j |
| Need ACID + global distribution | Spanner / CockroachDB / YugabyteDB |
| Need cache | Redis |
| Picking a shard key | High-cardinality, query-aligned, avoids hot spots |
| Multi-document transaction needed often | Reconsider model — denormalize, embed |
| Strongly-consistent reads | Per-query setting (`ConsistentRead`, `QUORUM`, `linearizable`) |
| Hot key in DynamoDB | Composite key with random suffix shard |
| High read load | Read replicas before sharding |
| High write load | Sharding |

---

## Worked Example: Modeling a Multi-Tenant SaaS Workload

**Context:** B2B SaaS, ~1000 tenants, ~100K-1M records per tenant. CRUD-heavy.
Need: per-tenant isolation, predictable performance, ACID for cross-record
transactions within a tenant.

**Choice:** Postgres with `tenant_id` as a shard key (Citus extension or
sharding via app routing).

**Schema design:**

```sql
CREATE TABLE customers (
    tenant_id   uuid NOT NULL,
    customer_id uuid NOT NULL,
    name        text,
    email       text,
    -- ... fields ...
    PRIMARY KEY (tenant_id, customer_id)
);

CREATE TABLE orders (
    tenant_id   uuid NOT NULL,
    order_id    uuid NOT NULL,
    customer_id uuid NOT NULL,
    -- ... fields ...
    PRIMARY KEY (tenant_id, order_id)
);

-- Sharding: hash(tenant_id) → shard
```

**Why this works:**
- All transactions within a tenant stay on one shard.
- `tenant_id` is high-cardinality and roughly evenly distributed.
- Adding tenants doesn't reshuffle existing data.
- Cross-tenant queries are admin-only and rare; fan out via app code.

**Replication:** Each shard has a primary and 2 read replicas (different
AZs).

**When to switch:**
- If a single tenant's data grows beyond shard capacity → split that tenant.
- If tenant count grows to 100K+ → consider DynamoDB with `tenant_id` as
  partition key.

---

## Gotchas

- **Iceberg, Delta, Hudi exist for *analytics* layers.** This skill is OLTP;
  see `data-storage-and-modeling-patterns` for those.
- **Cassandra hits write throughput easily** — multi-DC, ring-based — but
  modeling is unforgiving. Query-first schema design.
- **MongoDB's BatchExecuteStatement and PartiQL APIs** are more flexible than
  classic CRUD but come with their own perf surprises.
- **DynamoDB autoscaling lags** spike loads — provisioned mode + autoscale
  can throttle for several minutes during a step change. On-demand mode
  trades cost for elasticity.
- **Postgres logical replication** has improved markedly; for many systems
  it replaces tools like Debezium for CDC.
- **Spanner is genuinely different** — TrueTime + commit-wait give global
  linearizability but at a cost. Not for every workload.
- **MongoDB transactions across shards are slow** — they trigger 2PC. Design
  to keep transactions partition-local.
- **DynamoDB Global Tables resolve conflicts via LWW silently.** Don't
  expect ACID across regions.
- **Schemaless does not mean unstructured.** Documents must follow consistent
  shapes for queries and indexes to work.

---

## Related Skills

- `data-storage-and-modeling-patterns` — analytics-side modeling (Kimball,
  Inmon, Data Vault)
- `data-architecture-frameworks` — higher-level data platform frameworks
- `eventual-consistency-mechanics` — what eventually consistent really means
- `consensus-and-strong-consistency` — Paxos, Raft, 2PC, linearizability
- `distributed-system-patterns` — Database-per-Service, Saga
- `distributed-caching-patterns` — caching layer in front of databases

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapters 10 and 13.
Martin Kleppmann's *Designing Data-Intensive Applications* is the canonical
deeper reference.
