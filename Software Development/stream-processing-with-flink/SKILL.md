---
name: stream-processing-with-flink
description: >
  Design real-time stream processing on Apache Flink (and contrast with
  Storm, Kafka Streams, Spark Streaming, Kinesis) - DataStream / Table /
  SQL APIs, logical-to-physical DAG with task slots, parallelism,
  sliding vs tumbling windows, watermarks for event-time vs processing-
  time and late events, stateful operators with RocksDB backend, stream
  barriers (Chandy-Lamport) for consistent distributed checkpoints, and
  the Lambda vs Kappa architectural choice. Use when building real-time
  analytics, fraud detection, anomaly detection, or any data-in-motion
  workload. Triggers - "Flink", "stream processing", "windowing",
  "watermark", "late events", "checkpoint", "Lambda architecture",
  "Kappa architecture", "event time vs processing time", "Storm",
  "Kafka Streams", "stream barriers", "RocksDB state". Produces a
  stream-processing design with explicit windows, watermarks, parallelism,
  and checkpointing.
---

# Stream Processing with Flink

You design and operate stream-processing applications — extracting insight
from data **in motion**, before it lands in a warehouse. Real-time analytics,
fraud detection, anomaly detection, real-time route planning, trending-topic
detection. The defining trade-off: freshness vs completeness vs operational
complexity.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 15): the
batch-vs-stream framing, the Lambda architecture and its decline in favor
of all-stream architectures, Apache Storm's explicit topologies, Apache
Flink's functional DataStream API with windowing / watermarks / state /
checkpoints, and the distributed-snapshot mechanism (stream barriers) that
makes fault-tolerant streaming possible.

For the messaging substrate that streams sit on, see
`event-streaming-with-kafka`. For analytics-side batch modeling, see
`data-storage-and-modeling-patterns`.

---

## When to Use This Skill

- Designing real-time analytics, fraud detection, monitoring, alerting
- Choosing Flink vs Kafka Streams vs Spark Streaming vs Storm vs Kinesis
- Sizing windows (sliding vs tumbling, size vs slide)
- Configuring watermarks for late-arriving events
- Configuring Flink checkpointing for fault tolerance
- Deciding between Lambda architecture and all-stream

---

## Stream vs Batch: The Trade-Off

```
              Latency           Volume               Completeness        Cost
              ───────           ──────               ─────────────       ────
   Batch     minutes-hours      huge                 100% (waits for    Lower
              (nightly /         (TBs/day             all data)
              hourly)             OK)

   Stream    sub-second to       individual events    Bounded by         Higher
              seconds             or microbatches      watermark (some    (always-on
                                                       events arrive       infra)
                                                       too late)
```

**When stream wins:** freshness matters more than absolute completeness.
- Fraud detection (a fraudulent transaction needs to be flagged in seconds)
- Anomaly / outage detection
- Real-time dashboards (operational, not nightly)
- Recommendations responding to recent activity
- IoT / industrial monitoring

**When batch wins:** completeness matters more than freshness.
- Daily / weekly / monthly reports
- ML training (needs full dataset)
- Compliance / regulatory reporting
- Most BI dashboards (yesterday's data is fine)

**Reality check:** most "real-time" requirements collapse to "near-real-
time" (1–10 minutes) on inspection. Stream processing is 10× the operational
complexity of batch — verify the use case demands it.

> "Late results — even a few seconds late — are as bad as no results at all."
> — applies only to genuinely real-time use cases.

---

## Lambda vs Kappa Architectures

### Lambda Architecture (the historical default)

```
                ┌──────────────────────────────────┐
                │            Speed Layer            │
                │   (fast, approximate)             │
   Events ────► │   Storm / Spark Streaming         │ ─►──┐
                └──────────────────────────────────┘     │
                                                          │
                                                          ▼
                                                ┌─────────────────┐
                                                │ Serving layer   │
                                                │ Combine batch + │
                                                │ speed views     │ ──► Queries
                                                └─────────────────┘
                                                          ▲
                                                          │
   Events ────►  ┌─────────────────────────────────┐ ─►──┘
                 │            Batch Layer            │
                 │   (correct, slow)                 │
                 │   Hadoop / Spark batch            │
                 └─────────────────────────────────┘
```

**Pros:** Batch layer is reliable, correct ground truth. Speed layer fills
the freshness gap.

**Cons:** **Two codebases for the same logic.** Bug fixes must be applied
twice. Consistency between the layers is its own problem. The "Lambda tax."

### Kappa / All-Stream Architecture (the modern direction)

```
                                       ┌────────────────┐
                                       │  Stream        │
                                       │  processor     │
   Events ──► Kafka log ────────────►  │  (Flink /      │ ──► Materialized
                                       │   Spark        │     views, alerts,
                                       │   Streams /    │     dashboards
                                       │   Kafka        │
                                       │   Streams)     │
                                       └────────────────┘

                                          (To "rerun batch":
                                           replay from Kafka offset 0)
```

**Pros:** Single codebase. Kafka's retention is the historical record.
"Reprocess" = rewind and replay.

**Cons:** Stream processor must handle the volume of historical replay.
Less mature than batch tooling for ad-hoc analytics.

**Default in 2026:** Kappa-style for new systems where the use case allows.
Lambda persists where batch tooling (BigQuery, Snowflake) is essential
for analytics.

---

## Storm: Explicit Topologies

Older but still in use.

```java
TopologyBuilder builder = new TopologyBuilder();
builder.setSpout("source", new KafkaSpout(...));      // event source
builder.setBolt("parse",  new ParseBolt())             // transform
       .shuffleGrouping("source");
builder.setBolt("aggregate", new AggregateBolt())
       .fieldsGrouping("parse", new Fields("key"));    // route by key
builder.setBolt("output", new ESSinkBolt())
       .globalGrouping("aggregate");                   // all to one
```

| Concept | Meaning |
|---|---|
| **Spout** | Source of stream events |
| **Bolt** | Processing node (transform / aggregate / sink) |
| **`shuffleGrouping`** | Random distribution to bolt instances |
| **`fieldsGrouping`** | Hash by field — keyed routing |
| **`globalGrouping`** | All events to one bolt instance |

**Storm is imperative.** You build the DAG explicitly. Verbose but
transparent.

**Mostly superseded by Flink** for new development.

---

## Flink: Functional DataStream API

```java
DataStream<Event> events = env
    .addSource(new FlinkKafkaConsumer<>(...))
    .assignTimestampsAndWatermarks(...);

DataStream<Result> result = events
    .keyBy(Event::getUserId)
    .window(SlidingEventTimeWindows.of(Time.minutes(10), Time.minutes(5)))
    .aggregate(new RideCounter());

result.addSink(new FlinkKafkaProducer<>(...));
```

**Flink compiles your functional pipeline to a logical DAG, then to a
physical DAG of task slots across TaskManagers.**

```
Logical:        Source ──► keyBy ──► window ──► aggregate ──► sink

Physical:       
            ┌────────────┐  ┌────────────┐  ┌──────────────┐
            │ Source     │  │ keyBy +    │  │ Sink         │
            │ (parallel  │─►│ window +   │─►│ (parallel    │
            │  reads     │  │ aggregate  │  │  writes)     │
            │  Kafka     │  │            │  │              │
            │  partitions)│  │ (parallel  │  │              │
            │            │  │  per key)  │  │              │
            └────────────┘  └────────────┘  └──────────────┘
                  4 slots         8 slots         4 slots
```

| Concept | Meaning |
|---|---|
| **TaskManager** | Worker process |
| **Task slot** | Unit of parallelism within a TaskManager |
| **Parallelism** | How many parallel subtasks for an operator (`.setParallelism(8)`) |
| **DataStream API** | Primary functional API |
| **Table API / SQL API** | Higher-level, for SQL-like analytics |

---

## Windowing

Stream operations rarely care about *all* events — they care about a recent
window of events.

### Tumbling Windows (disjoint)

```
Time:    [────10min────][────10min────][────10min────]
Events:    a b c d e      f g            h i j k

Tumbling 10-min windows:
  Window 1 (00:00-00:10): a, b, c, d, e
  Window 2 (00:10-00:20): f, g
  Window 3 (00:20-00:30): h, i, j, k
```

Each event in exactly one window.

**Use for:** disjoint reporting periods (per-hour, per-day metrics).

### Sliding Windows (overlapping)

```
Time:    0    5    10   15   20

Sliding 10-min window every 5 min:
  Window A (00:00-00:10)
       Window B (00:05-00:15)
            Window C (00:10-00:20)
                Window D (00:15-00:25)
```

Each event appears in *multiple* windows (size / slide of them).

**Use for:** trend metrics ("requests per minute, smoothed over 10").

```java
SlidingEventTimeWindows.of(Time.minutes(10), Time.minutes(5))
//                      size              slide
```

**Cost:** sliding windows are 2-10× the state vs tumbling.

### Session Windows

Window starts when an event arrives, extends until inactivity gap.

**Use for:** user-session-level analytics ("count events per user session").

---

## Watermarks: Event Time vs Processing Time

```
Event time     = when the event happened in the real world
Processing time = when Flink saw the event

Real workloads have a gap: events arrive late.
```

**Watermark:** Flink's mechanism for asserting "all events with timestamp
≤ W have been seen." Operators use watermarks to decide when to close a
window.

```java
WatermarkStrategy
    .<Event>forBoundedOutOfOrderness(Duration.ofSeconds(20))
    .withTimestampAssigner((e, ts) -> e.getTimestamp())
```

**Behavior:**

| Event arrival | What happens |
|---|---|
| Within out-of-orderness bound | Counted in normal window |
| After watermark passes window end | **Late event** — by default, dropped |

**Late events handling:**

```java
.window(...)
.allowedLateness(Time.minutes(1))
.sideOutputLateData(lateOutputTag)
```

Allow late updates to existing windows; route truly-late events to a side
stream for separate handling.

**Watermark tuning is the central operational challenge in event-time
streaming.** Too tight → drops legitimate late events. Too loose → window
results lag for no reason.

---

## State and RocksDB

Stream operators are often stateful — counts, aggregations, joins.

| Backend | Stored | Pros | Cons |
|---|---|---|---|
| **MemoryStateBackend** | JVM heap | Fast | Limited by heap; lost on crash |
| **FsStateBackend** | Heap (small state) + filesystem (snapshots) | Fast for small state; durable snapshots | State must fit in memory |
| **RocksDB** | Local RocksDB on disk; snapshots to filesystem | Large state; durable | Slower than memory |

**Default for production:** RocksDB. Operator state can be hundreds of GBs
per task slot.

```java
env.setStateBackend(new EmbeddedRocksDBStateBackend());
```

---

## Stream Barriers and Checkpoints

Flink's fault tolerance hinges on **distributed snapshots** taken via
**stream barriers** (Chandy-Lamport algorithm, 1985).

```
Source ──► barrier injection every N seconds

  Stream:  ── e1 ── e2 ── BARRIER_5 ── e3 ── e4 ── BARRIER_6 ── e5 ──►

When an operator receives BARRIER_5 on ALL its input streams:
  1. Snapshot its state (write to durable storage)
  2. Forward BARRIER_5 downstream

When all sinks have processed BARRIER_5: snapshot 5 is complete.
```

```
                                               
  Source 1                Op A                    Op B                Sink
  [b5][e3][e2][e1]   →   [b5][e3'][e2'][e1']  → [b5][...]        →   [...]
                                                                       
  Source 2                                       Op B aligns until
  [b5][f3][f2][f1]   ──────────────────────────►barrier from BOTH
                                                  inputs reaches it
```

**Failure recovery:**

1. Stop the application.
2. Restore each operator's state from the latest **complete** checkpoint.
3. Resume sources from the offset stored in that checkpoint (e.g., Kafka
   offset N+1).
4. Stream resumes; effectively zero data loss.

**Configuration:**

```java
env.enableCheckpointing(60_000);  // every 60 seconds
env.getCheckpointConfig()
   .setMinPauseBetweenCheckpoints(2000);  // at least 2s between checkpoints
env.getCheckpointConfig()
   .setCheckpointTimeout(120_000);
```

**Tuning:**

| Knob | Effect |
|---|---|
| Checkpoint interval | Shorter = less recovery work but more overhead |
| Min pause between | Prevents checkpoints from piling on each other |
| State size | Linear cost per checkpoint |
| RocksDB incremental checkpoints | Only changed SST files written — much cheaper for large state |

**Checkpointing is OFF BY DEFAULT in Flink.** Easy to deploy without it
and only discover the lack on first failure. Always enable.

---

## Choosing a Stream Processor

| | Flink | Kafka Streams | Spark Streaming | Storm | Kinesis Data Analytics |
|---|---|---|---|---|---|
| Style | Functional DataStream | Library, embedded in app | Microbatch RDD | Imperative topology | Managed Flink |
| Latency | Sub-second | Sub-second | Microbatch (sec+) | Sub-second | Sub-second |
| State management | Built-in, RocksDB | RocksDB-backed | Spark RDD | Manual | Built-in |
| Fault tolerance | Stream barriers, exactly-once | At-least-once + idempotent | Microbatch | At-least-once | Inherits Flink |
| Deployment | Standalone cluster | Application-embedded | Spark cluster | Storm cluster | AWS-managed |
| Best for | Mature streaming workloads | Kafka-only stream apps | Mixed batch+stream | Legacy / specific use | AWS-native |

**Default in 2026:** **Flink** for new development. Kafka Streams when the
processor is co-located with a Kafka-native app and you don't want a
separate cluster. Spark Streaming where you already have a Spark cluster.

---

## Principles

- **Use stream processing when freshness matters more than completeness.**
  Fraud, anomalies, monitoring.
- **Most "real-time" is near-real-time.** Quantify the SLA before building
  streaming infrastructure.
- **Default to Kappa-style** (all-stream over Kafka) for new systems.
  Lambda only when batch tooling is essential.
- **Choose Flink for new development.** Functional DataStream is more
  maintainable than Storm's imperative topology.
- **Use sliding windows for trend metrics; tumbling windows for disjoint
  reporting periods.**
- **Configure RocksDB checkpointing for any stateful operator that needs
  to survive failures.**
- **Tune checkpoint frequency to match state size.** Large state + frequent
  checkpoints can tank throughput.
- **Set minimum elapsed time between checkpoints** so they don't pile up.
- **Enable checkpointing.** It's off by default. Easy to forget.
- **Tune watermarks empirically.** Too tight drops events; too loose lags
  results.

---

## Anti-Patterns

### Streaming for Daily Reports

**Looks like:** Building a Flink pipeline to compute daily-aggregated
metrics that get displayed in a BI dashboard at 9 AM.

**Why it fails:** Batch (nightly Spark / dbt / Airflow) is simpler, cheaper,
and just as fresh enough.

**The fix:** Quantify the freshness SLA. If "by 9 AM" works, batch wins.

### Forgetting to Enable Checkpointing

**Looks like:** Flink job runs in production for weeks. TaskManager fails.
State lost. Job restarts from scratch.

**Why it fails:** Checkpointing is off by default.

**The fix:** Enable checkpointing as part of the job submission template.

### Sliding Window with Tiny Slide

**Looks like:** 10-min window, 1-second slide. State is 600 windows per
key. Memory blows up.

**Why it fails:** State scales as size/slide.

**The fix:** Use a more reasonable slide (e.g., size/10). Or use
incremental aggregation.

### Watermark Too Tight

**Looks like:** `forBoundedOutOfOrderness(Duration.ofMillis(100))`. Most
late events dropped silently.

**Why it fails:** Real-world out-of-orderness is rarely sub-second.

**The fix:** Measure actual lateness distribution. Set bound at P99 + safety.
Use side-output for outliers.

### Confusing Event Time with Processing Time

**Looks like:** Aggregating "events per minute" using processing time. When
events arrive late, they go in the wrong window.

**Why it fails:** Processing-time windows tell you about Flink's clock, not
the real world.

**The fix:** Use event-time windows + watermarks. Reserve processing-time
for cases where it doesn't matter (real-time monitoring, dashboards).

### Lambda Architecture's Two Codebases

**Looks like:** Maintaining a Spark batch job and a Flink streaming job
that compute "the same metric." Bugs diverge.

**Why it fails:** The "Lambda tax."

**The fix:** All-stream over Kafka. Or accept eventual reconciliation via
batch-of-record.

### Stateful Operator Without Backend Tuning

**Looks like:** Default `MemoryStateBackend` with 100 GB of state. OOMs on
checkpoint.

**Why it fails:** Memory can't hold the state.

**The fix:** RocksDB backend. Incremental checkpoints. Tune RocksDB
parameters for state size.

---

## Decision Rules

| Situation | Action |
|---|---|
| Real-time alerting / fraud / anomaly | Flink or Kafka Streams |
| Already have Spark cluster | Spark Streaming (microbatch) |
| Kafka-native app, no separate cluster | Kafka Streams |
| AWS-managed | Kinesis Data Analytics for Apache Flink |
| Legacy Storm | Plan migration to Flink |
| Per-entity aggregation | `keyBy` + window |
| Trend metric (smoothed) | Sliding window |
| Disjoint reporting period | Tumbling window |
| User-session analytics | Session window |
| Fault-tolerant stateful job | Enable checkpointing + RocksDB |
| Late events critical | Allowed lateness + side output |
| Large state | RocksDB + incremental checkpoints |
| Need exactly-once across stream → external | Two-phase commit sink (Kafka, JDBC) |

---

## Worked Example: Real-Time Ski Lift Analytics

**Context:** Ski-resort lift turnstiles emit events. Need: count rides per
lift in 10-minute sliding windows (every 5 minutes) for an operations
dashboard. Late events up to 30s should be counted; later events flagged.

**Flink job:**

```java
DataStream<LiftRide> rides = env
    .addSource(new FlinkKafkaConsumer<>(
        "lift-rides", new LiftRideSchema(), kafkaProps))
    .assignTimestampsAndWatermarks(
        WatermarkStrategy
            .<LiftRide>forBoundedOutOfOrderness(Duration.ofSeconds(30))
            .withTimestampAssigner((e, ts) -> e.getTime()));

DataStream<LiftCount> counts = rides
    .keyBy(LiftRide::getLiftId)
    .window(SlidingEventTimeWindows.of(Time.minutes(10), Time.minutes(5)))
    .allowedLateness(Time.seconds(30))
    .sideOutputLateData(lateLiftRides)
    .aggregate(new RideCountAggregator());

counts.addSink(new FlinkKafkaProducer<>("lift-counts", ...));
```

**Settings:**
- Parallelism: 16 (matches Kafka source partitions).
- Checkpoint every 60s.
- RocksDB state backend.
- Min pause between checkpoints: 2s.
- Watermark: 30s out-of-orderness.

**Failure modes monitored:**
- Watermark progress (alert if stalled).
- Checkpoint duration (alert if > 30s).
- Kafka consumer lag.
- Late-event side stream (alert on volume spike — maybe systems clock issue).

**Outcome:** Live count of rides per lift, smoothed over 10 minutes,
updating every 5. Late-arriving events (up to 30s) counted. Truly-late
events surfaced separately for investigation.

---

## Gotchas

- **Watermarks pause when sources idle.** Configure `withIdleness(...)` to
  unblock windows when one Kafka partition has no traffic.
- **Stateful joins require careful keyBy.** Both sides must be keyed on the
  same field for the join to find matches.
- **RocksDB checkpoints can be huge.** Enable incremental checkpointing
  (`state.backend.incremental: true`) for large state.
- **Flink upgrades sometimes break savepoint compatibility.** Test
  upgrade paths.
- **Storm's `at-most-once` semantics** are easy to miss. If you need
  exactly-once, ensure you've configured Trident or use Flink instead.
- **Kafka Streams stores state in local RocksDB and a Kafka changelog
  topic.** Recovery means replaying the changelog — slow for large state.
- **Spark Streaming uses microbatches.** True per-record latency below the
  microbatch interval is impossible.
- **Lambda architecture's persistence has reasons.** Some workloads
  genuinely benefit from the slow-but-correct batch layer alongside the
  fast-but-approximate speed layer.
- **Stream processing observability** is its own challenge. Watermarks,
  backpressure, checkpointing, lag — all need dashboards.

---

## Related Skills

- `event-streaming-with-kafka` — the substrate stream processors usually
  read from
- `data-storage-and-modeling-patterns` — analytics-side batch counterpart
- `scalability-foundations` — when sub-second is genuinely required
- `serverless-processing-systems` — Kinesis Data Analytics is a managed
  Flink alternative
- `architecture-styles-monolithic-and-distributed` — Event-Driven style

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 15.
Tyler Akidau et al.'s *Streaming Systems* (O'Reilly, 2018) is the canonical
deeper reference. Fabian Hueske and Vasiliki Kalavri's *Stream Processing
with Apache Flink* (O'Reilly, 2019) for Flink depth.
