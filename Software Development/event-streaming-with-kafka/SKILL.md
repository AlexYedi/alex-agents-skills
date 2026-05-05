---
name: event-streaming-with-kafka
description: >
  Design event-driven architectures on Apache Kafka - immutable append-only
  event logs, topics / partitions / offsets, producer batching, delivery
  guarantees (acks=0/1/all and enable.idempotence), pull-based consumer
  groups with rebalancing, in-sync replicas (ISR) and min.insync.replicas,
  semantic partitioning, per-partition ordering, and using Kafka as a
  system of record vs as a queue replacement. Use when adopting Kafka,
  designing event-driven microservices, choosing partitioning keys, or
  diagnosing Kafka delivery / ordering / replication issues. Triggers -
  "Kafka topic / partition / offset", "consumer group rebalancing",
  "acks=all", "min.insync.replicas", "exactly-once Kafka", "enable.
  idempotence", "ISR", "Kafka vs RabbitMQ", "event sourcing", "log
  compaction", "Confluent". Produces a Kafka design with explicit
  partitioning, replication, delivery, and consumer policies.
---

# Event Streaming with Kafka

You design event-driven architectures on Apache Kafka. Kafka reframes
messaging: instead of destructive queues that consume-and-delete, it's an
**immutable, append-only event log** that retains messages for a configured
period. Multiple independent consumers can read at their own pace. The log
itself can be the system of record.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 14):
the topic / partition / offset model, producer and consumer semantics,
ISR-based replication, and the patterns that make Kafka useful (vs treating
it as a fancy queue).

For traditional message brokers (RabbitMQ, SQS), see
`asynchronous-messaging-patterns`. For stream processing on top of Kafka
(Flink, Kafka Streams), see `stream-processing-with-flink`.

---

## When to Use This Skill

- Adopting Kafka for event-driven microservices
- Designing topic structure and partitioning
- Configuring producer / consumer / replication for required durability
- Choosing Kafka over RabbitMQ / SQS / Pulsar (or vice versa)
- Diagnosing delivery, ordering, replication issues
- Implementing event sourcing or CQRS

---

## The Kafka Mental Model

```
                          Topic: orders
   ┌──────────────────────────────────────────────────────────────┐
   │                                                                │
   │  Partition 0:    [0][1][2][3][4][5][6][7][8][9]→               │
   │                                              ▲                 │
   │                                              │ append          │
   │                                                                │
   │  Partition 1:    [0][1][2][3][4][5][6][7]→                     │
   │                                                                │
   │  Partition 2:    [0][1][2][3][4][5][6][7][8][9][10][11]→       │
   │                                                                │
   └──────────────────────────────────────────────────────────────┘

   Producers:
       Append events to partitions (which one is determined by key
       or round-robin).

   Consumers:
       Track an OFFSET per partition; read forward from offset.
       Multiple consumers can read independently — no destructive
       consumption.

   Retention:
       Messages stay until retention.ms expires (e.g., 7 days, 30 days,
       or forever).
```

**The shifts from traditional messaging:**

| | RabbitMQ / SQS | Kafka |
|---|---|---|
| Message lifetime | Consumed = deleted | Retained for period (or forever) |
| Consumers | Compete for messages | Each tracks own offset; can replay |
| Ordering | Per queue (single consumer) or none | Per partition |
| Throughput | Tens of thousands msg/s typical | Millions msg/s capable |
| Multi-consumer | Pub-sub via topics | Native — N consumer groups all see all messages |
| Use as system of record | No | Yes — log is durable |
| Replay | Generally not | Yes — re-read from old offset |

---

## Topics, Partitions, Offsets

| Concept | Definition |
|---|---|
| **Topic** | Logical category of events (`orders`, `user_events`, `clicks`) |
| **Partition** | Append-only log within a topic; the unit of parallelism |
| **Offset** | Sequential ID of an event within a partition |
| **Replication factor** | Copies of each partition across brokers (typical: 3) |
| **Leader / Follower** | One leader per partition handles writes; followers replicate |
| **Retention** | How long messages are kept (`retention.ms`, default 7 days) |

**Per-partition ordering only.** Kafka guarantees order within a partition,
*never* across partitions. This is the central design constraint.

**Partition count = upper bound on consumer parallelism.** A consumer group
with C consumers and a topic with P partitions has at most `min(C, P)`
parallel consumers — extra consumers sit idle.

**Topics typically have many partitions.** 10–100 is common; 1,000+ exists.
Repartitioning later breaks key ordering for new events — provision
generously.

---

## Producers

### Producer Side: `acks` and Durability

```
Producer        ┌─────────────────────────────────┐
                │                                  │
                │  Leader partition replica        │
                │                                  │
                │  ┌────┐  ┌────┐                  │
   send() ───►  │  │log │  │ISR │                  │
                │  └────┘  └────┘                  │
                │                                  │
                │  Followers (in-sync replicas)    │
                │                                  │
                └──────────┬──────────┬────────────┘
                           │          │
                           ▼          ▼
                       Replica 1  Replica 2
```

**`acks` options:**

| Setting | Behavior | Loss possible? |
|---|---|---|
| `acks=0` | Fire and forget; no wait | Yes — broker may not have received |
| `acks=1` | Leader acks once written to leader log | Yes — if leader fails before replication |
| `acks=all` | Leader acks once written to all in-sync replicas | No (within ISR) |

**`enable.idempotence=true`** (default in newer Kafka): broker dedups by
producer ID + sequence number. Together with `acks=all` this gives
**exactly-once** semantics from producer to broker.

**For data safety:**
```
acks=all
enable.idempotence=true
min.insync.replicas=2  (with replication.factor=3)
```

This durably writes to a majority of replicas and tolerates one follower
failure.

### Producer Side: Batching

```
batch.size  = max bytes per batch (default 16 KB)
linger.ms   = max wait time before sending a non-full batch (default 0)
```

`linger.ms=0` sends immediately on every produce. `linger.ms=20` waits up
to 20 ms for more events to fill a batch — significantly higher throughput
at small latency cost.

**Tune:** `linger.ms=10–50` for high-throughput producers, plus a generous
`batch.size`.

### Semantic Partitioning

```
Producer → topic.partition(key)
  if key:    partition = hash(key) mod num_partitions
  if no key: round-robin among partitions
```

**Keyed events go to the same partition.** This is how you get ordering
guarantees per entity.

| Key | Effect |
|---|---|
| `userId` | All events for one user in order, parallelized across users |
| `orderId` | All events for one order in order |
| Random / null | Round-robin; no per-entity order |

---

## Consumers

### Consumer Groups

```
Consumer group "billing-service":
                                          
   ┌──────────────────────┐               ┌──────────────────┐
   │  topic: orders       │               │  Group "billing" │
   │                      │               │                  │
   │  Partition 0  ──────►│               │  Consumer A      │
   │  Partition 1  ──────►│ ─────────────►│  Consumer B      │
   │  Partition 2  ──────►│               │  Consumer C      │
   │  Partition 3  ──────►│               │                  │
   └──────────────────────┘               └──────────────────┘
                                              4 partitions, 3 consumers:
                                                A gets 0, 1
                                                B gets 2
                                                C gets 3

   Each partition is consumed by EXACTLY ONE consumer in the group.

   Different groups read independently:

   Group "billing"      reads all 4 partitions
   Group "analytics"   reads all 4 partitions
```

**Adding a consumer to a group triggers rebalancing** — the group
coordinator reassigns partitions across the new set of consumers. This
takes seconds and pauses consumption.

**Removing a consumer** also triggers rebalancing.

**Consumer group offsets** are persisted in a special internal topic
(`__consumer_offsets`).

### Consumer Side: At-Most-Once vs At-Least-Once

```
Pseudocode:                          Semantics

records = consumer.poll()            # Pull from broker
consumer.commitSync()                # Commit offsets ── BEFORE process
process(records)                     # If we crash here, records lost
                                     #
                                     # → AT-MOST-ONCE

# vs

records = consumer.poll()
process(records)                     # Process first
consumer.commitSync()                # Commit offset AFTER process
                                     # If we crash here, records reprocessed
                                     # next time (offset wasn't committed)
                                     #
                                     # → AT-LEAST-ONCE

# Exactly-once requires idempotent processing OR transactional consumer-
# producer for "consume → process → produce → commit" loops.
```

**For exactly-once across consume-process-produce:**

```java
producer.initTransactions();
while (running) {
    records = consumer.poll();
    producer.beginTransaction();
    for (record : records) {
        producer.send(transformedRecord);
    }
    producer.sendOffsetsToTransaction(currentOffsets, consumerGroupId);
    producer.commitTransaction();
}
```

This binds offset commit to the produced output, atomically.

### Pull-Based Model

Kafka consumers **poll** — they pull batches at their own rate. This is
different from RabbitMQ's push model. The consumer drives backpressure;
no overflow at the broker.

---

## Replication: In-Sync Replicas (ISR)

```
Partition 0
  Leader:        Broker 1
  Replicas:      Broker 1, Broker 2, Broker 3   (replication.factor=3)
  ISR:           Broker 1, Broker 2, Broker 3   (when all healthy)

If Broker 3 falls behind (slow disk, network):
  ISR:           Broker 1, Broker 2             (Broker 3 dropped)

If acks=all + min.insync.replicas=2:
  Writes succeed (ISR has 2)

If ISR drops to 1:
  Writes fail (below min.insync.replicas)
  → Producer gets NotEnoughReplicasException

If Broker 1 (leader) fails:
  Election from ISR — pick a member of ISR as new leader.
  Brokers NOT in ISR cannot be elected (they would lose data).
```

**Custom leader election:** Kafka picks new leaders only from the ISR.
Followers that have fallen behind aren't eligible — promoting them would
silently lose data.

**`min.insync.replicas`** is the durability lever:

| Setting | Behavior |
|---|---|
| `min.insync.replicas=1` | Always writable; no replication safety |
| `min.insync.replicas=2` (with RF=3) | Tolerates 1 follower failure; loses availability if 2 followers fail |
| `min.insync.replicas=N` (= RF) | Strict; one slow follower halts writes |

**Default for production:** `RF=3, min.insync.replicas=2, acks=all`.

---

## When Kafka Wins (and Loses)

| Use case | Kafka? |
|---|---|
| Event log as system of record | ✅ The killer use case |
| Multiple independent consumers | ✅ Each gets full stream |
| Replay events after a bug fix | ✅ Re-read from old offset |
| High-throughput stream (>10K msg/s sustained) | ✅ |
| Strict total ordering across all events | ❌ Per-partition only |
| Single-consumer queue with low latency | ❌ — RabbitMQ / SQS simpler |
| Low-volume task queue | ❌ — overkill |
| Complex routing (header-based, dynamic subscriptions) | ❌ — RabbitMQ wins |
| Microservice integration via events | ✅ |
| Stream processing input | ✅ (Flink, Kafka Streams, Spark Streaming) |

**Rule of thumb:** Use Kafka when you want **event replay, multiple
independent consumers, or a system of record**. Don't use it just because
it's trendy — RabbitMQ / SQS are often the right answer for traditional
queueing.

---

## Production Examples (from Ch 14)

| Org | Use |
|---|---|
| **Slack** | Buffer for events too expensive to process synchronously; >1B messages/day on 16 brokers; 32 partitions/topic (2018) |
| **Big Fish Games** | Game telemetry capture into Kafka, fed into real-time analytics |
| **LinkedIn** | Origin (created Kafka). Event bus for everything. |
| **Netflix** | Multiple Kafka clusters; ingestion bus for analytics, monitoring, recommendations |
| **Confluent** | Commercial backers; provide cloud Kafka + ecosystem (connectors, schema registry, ksqlDB) |

---

## Architecture Patterns

### Event-Driven Microservice Integration

```
   Order Service ───► topic: orders
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
         Billing     Shipping    Analytics
         Service     Service     Service
```

Each downstream service reads `orders` independently, builds its own
projection, and reacts.

### Event Sourcing / CQRS

```
Commands ──► Service ──► topic: events ──► Materialized read views
                                   │
                                   └──► Audit log
```

Topic is the source of truth. State is derived by replaying events.

### Outbox Pattern

Service writes to its DB and the outbox table in one transaction. CDC
(Debezium) reads the outbox and publishes to Kafka. Avoids the dual-write
problem (DB write + Kafka send not transactional).

### Log Compaction

Topic configured with `cleanup.policy=compact` keeps the latest value per
key forever. Useful as a stream-table — entity state log, deduplicated.

---

## Principles

- **Use Kafka for event replay, multiple independent consumers, or a
  system of record.** Otherwise consider RabbitMQ / SQS.
- **Use a key for events that should land in the same partition.**
  Preserves order per entity.
- **Manually commit offsets after processing for at-least-once.** Commit
  before for at-most-once. Choose deliberately.
- **For data safety:** `acks=all` + `enable.idempotence=true` +
  `min.insync.replicas=2` (with RF=3).
- **Provision partitions generously.** Adding partitions later breaks per-
  key ordering for new events.
- **Use batching (`batch.size`, `linger.ms`) to trade tiny latency for
  throughput.**
- **Don't share consumer instances across threads** — Kafka's Consumer API
  isn't thread-safe. Thread-per-consumer or single-fetch-thread + worker
  pool.
- **Monitor consumer lag.** Lag = current end offset minus consumer offset.
  If it grows unbounded, consumers can't keep up.

---

## Anti-Patterns

### Treating Kafka Like a Queue

**Looks like:** Single consumer per topic. No replay. Default 7-day retention
discarded as "we don't need that."

**Why it fails:** Kafka's unique value is the log. If you don't use it,
RabbitMQ would do the same job with less complexity.

**The fix:** Either use Kafka's strengths (replay, multi-consumer, system
of record) or pick a queueing system instead.

### Assuming Total Order Across Partitions

**Looks like:** App expects `event_id` increases globally. Sees `event_id=5`
followed by `event_id=3`.

**Why it fails:** Kafka guarantees order only within a partition.

**The fix:** Use 1 partition (loses parallelism), or design consumers to not
require global order, or sequence at the source.

### Reducing Partition Count

**Looks like:** "Let's reduce from 32 partitions to 8 to simplify ops."
Kafka doesn't let you.

**Why it fails:** Per-partition logs can't be merged without losing order.
Kafka forbids decreasing partition count.

**The fix:** Provision generously up front. If you must reduce, create a
new topic and migrate.

### Increasing Partitions Mid-Flight

**Looks like:** Add partitions to a topic with active keyed events. New
events for the same key now hash to a different partition; ordering broken.

**Why it fails:** Hash mod N changes when N changes.

**The fix:** Provision partitions early. If absolutely necessary, plan a
clean cutover (compact, backfill, switch consumers).

### `acks=1` for Critical Data

**Looks like:** Default `acks=1`. Leader fails before replication completes.
Data lost silently.

**Why it fails:** Followers don't have the message; new leader doesn't
either.

**The fix:** `acks=all` + `min.insync.replicas=2`. Accept slightly higher
write latency.

### Sharing Consumer Across Threads

**Looks like:** One Consumer instance, multiple threads call `poll()`.
Random `ConcurrentModificationException`.

**Why it fails:** Consumer API isn't thread-safe.

**The fix:** Thread-per-consumer (each in its own group / partition).
Or single fetch thread + work-queue distributing records to workers.

### Forgetting to Monitor Lag

**Looks like:** Consumer slow path; lag grows from minutes to hours unnoticed.
Topic retention drops messages before consumer catches up.

**Why it fails:** Lag → data loss when retention expires.

**The fix:** Alert on consumer lag. Monitor lag per partition.

---

## Decision Rules

| Situation | Action |
|---|---|
| Multiple services need same events | Kafka with consumer-per-service group |
| Need event replay after bug fix | Kafka with long retention |
| High-throughput single-consumer queue | RabbitMQ or SQS |
| Cross-region replication | Kafka MirrorMaker 2 / Confluent Replicator |
| Strict ordering across all events | One partition (low parallelism) or sequence at source |
| Per-entity ordering | Key by entity ID |
| Data safety required | `acks=all` + `enable.idempotence=true` + `min.insync.replicas=2` (RF=3) |
| At-least-once consumer | Commit offsets after processing |
| At-most-once consumer | Commit offsets before processing |
| Exactly-once stream processing | Transactional producer-consumer pairing |
| Need to dedupe stream | Kafka Streams or Flink with idempotent operations |
| Schema management | Confluent Schema Registry (Avro / Protobuf / JSON Schema) |

---

## Worked Example: Order Event Pipeline

**Context:** E-commerce platform. Order events drive multiple downstream
services. Need: durability, replay capability, per-order ordering, scaling
to 50K events/sec.

**Topic design:**

| Topic | Partitions | Replication factor | Retention | Key |
|---|---|---|---|---|
| `orders.placed` | 64 | 3 | 30 days | `order_id` |
| `orders.fulfilled` | 64 | 3 | 30 days | `order_id` |
| `orders.cancelled` | 64 | 3 | 30 days | `order_id` |
| `customers.events` | 32 | 3 | compact (forever) | `customer_id` |

**Producer config:**

```
acks=all
enable.idempotence=true
linger.ms=20
batch.size=65536
compression.type=lz4
```

**Broker config:**

```
min.insync.replicas=2  (with RF=3)
unclean.leader.election.enable=false
```

**Consumer groups:**

| Group | Reads | Behavior |
|---|---|---|
| `billing-service` | `orders.placed`, `orders.cancelled` | At-least-once + idempotent processing (idempotency key on internal calls) |
| `shipping-service` | `orders.placed`, `orders.cancelled` | At-least-once |
| `analytics` | All `orders.*` | At-least-once; lag tolerated (not customer-facing) |
| `search-indexer` | `customers.events` | At-least-once + materialized into Elasticsearch |

**Topology:** 9 brokers across 3 AZs (3 per AZ). Total partitions:
`(64 × 3) + 32 = 224`. Each broker hosts ~25 partitions × 3 (incl. replicas)
= ~75 partition-replicas. Comfortably within typical broker capacity.

**Failure modes monitored:**
- Consumer lag per group (alert if > 5 min behind).
- ISR shrinkage (alert if any partition's ISR < `min.insync.replicas + 1`).
- Producer error rate (alert on `NotEnoughReplicasException`).

---

## Gotchas

- **Kafka isn't a queue.** Treating it like one wastes its strengths.
- **No total order across partitions.** Design accordingly.
- **Increasing partitions breaks per-key ordering** for new events.
- **Decreasing partitions is impossible.**
- **Rebalancing pauses consumers** — sometimes for several seconds.
- **Consumer API isn't thread-safe.** Don't share instances.
- **Default 7-day retention drops messages.** If consumers fall behind too
  long, data is lost.
- **`acks=all` with `min.insync.replicas=N` (=RF)** halts writes when one
  follower lags. Use `min.insync.replicas=2` with RF=3.
- **Compacted topics retain only the latest value per key.** Use for state-of-
  entity logs (user profile, latest config).
- **ZooKeeper is being phased out** in favor of KRaft (Kafka's own Raft-based
  metadata). Plan migration for long-running clusters.
- **`enable.idempotence=true`** is producer-side dedup; doesn't dedup across
  producer restarts unless you set a stable `transactional.id`.
- **MirrorMaker 2 doesn't preserve consumer offsets across regions** by
  default — design for it.

---

## Related Skills

- `asynchronous-messaging-patterns` — RabbitMQ / SQS for traditional queueing
- `stream-processing-with-flink` — building applications on top of Kafka
- `eventual-consistency-mechanics` — Kafka events → eventual replica state
- `distributed-systems-essentials` — at-least-once / exactly-once
- `architecture-styles-monolithic-and-distributed` — Event-Driven style

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 14. Ben
Stopford's *Designing Event-Driven Systems* (free Confluent ebook) is the
canonical deeper reference. The official Kafka documentation at
kafka.apache.org/documentation is well-maintained.
