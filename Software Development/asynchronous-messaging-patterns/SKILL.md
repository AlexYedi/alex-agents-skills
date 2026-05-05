---
name: asynchronous-messaging-patterns
description: >
  Apply asynchronous messaging correctly - producer / consumer / queue /
  topic primitives, push vs pull, persistent queues + manual acks +
  publisher confirms for data safety, competing-consumer and pub/sub
  patterns, broker replication (mirrored vs Raft-based quorum queues),
  channel pooling, idempotency keys, and dead-letter queues for poison
  messages. Use when adopting RabbitMQ / SQS / JMS / IBM MQ, designing a
  decoupled producer-consumer flow, or diagnosing message loss / duplication
  / queue backups. Triggers - "RabbitMQ vs SQS", "publisher confirm",
  "manual ack", "persistent queue", "competing consumers", "publish /
  subscribe", "dead letter queue", "poison message", "channel pool",
  "AMQP", "JMS", "MQTT". Produces a messaging design with explicit
  delivery, durability, and failure-handling decisions.
---

# Asynchronous Messaging Patterns

You design and operate messaging-based decoupling between services. Async
messaging absorbs spikes, decouples deployments, and lets producers and
consumers scale independently. The constant trade-offs are data safety vs
throughput, availability vs performance, and what to do when messages can't
be processed.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 7): the
RabbitMQ-flavored canonical messaging model, persistent / acked / replicated
patterns, and the operational realities (poison messages, channel pools,
duplicate detection).

---

## When to Use This Skill

- Choosing or adopting a message broker (RabbitMQ, SQS, ActiveMQ, IBM MQ,
  Pulsar)
- Designing a producer/consumer flow between services
- Configuring durability, replication, acks for message safety
- Diagnosing message loss, duplication, or queue backups
- Implementing dead-letter handling and poison-message protection
- Sizing queues, channels, and consumer parallelism

---

## The Primitives

```
                    ┌─────────────────────┐
                    │       Broker        │
                    │   (RabbitMQ / SQS / │
                    │    JMS / Pulsar)    │
                    └──────────┬──────────┘
                               │
       ┌───────────┐    ┌──────┴──────┐    ┌───────────┐
       │ Producer  │───►│   Queue /   │◄───│ Consumer  │
       │           │    │    Topic    │    │           │
       └───────────┘    └─────────────┘    └───────────┘
       publishes          holds messages    pulls / receives
       messages           in order          messages
```

| Term | Meaning |
|---|---|
| **Producer** | Sender of messages |
| **Consumer** | Receiver of messages |
| **Queue** | One-to-one delivery; each message goes to exactly one consumer |
| **Topic** | Pub-sub; each message goes to all subscribers |
| **Broker** | The middleware (RabbitMQ, IBM MQ, ActiveMQ, SQS, Pulsar) |
| **AMQP** | Open binary protocol implemented by RabbitMQ and others |
| **JMS** | Java's queue API spec (vendor-neutral interface) |

---

## Push vs Pull (Polling)

| | Push (callback / streaming) | Pull (polling) |
|---|---|---|
| Mechanism | Broker calls consumer when message arrives | Consumer asks "any messages?" on a loop |
| Latency | Sub-ms when broker has work | Bounded by polling interval |
| Throughput | Higher | Lower (overhead of empty polls) |
| Examples | RabbitMQ basic_consume, JMS MessageListener, Kafka long-poll | Plain SQS poll, simple HTTP-based message consumers |

**Default:** push. Polling makes sense only when the consumer needs fine-grained
control over when it accepts work (e.g., backpressure-aware batch processors).

---

## The Data-Safety Stack

The book's central trade-off: every layer of safety costs throughput. Here's
the layered model — adopt as much as your use case requires.

```
LEAST SAFE                                              MOST SAFE
──────────                                              ─────────

Memory-only          + Persistent      + Publisher       + Manual
queue                  queue            confirms           consumer
+ auto-ack             + persistent     (broker acks       acks
                       messages          producer write)
                       + auto-ack

Data lost on:
- Broker crash         - Producer       - Consumer        - All known
- Consumer crash         crash mid-        crash mid-       failures except
                         publish           process          partial-network
```

### Levels of Safety

| Level | Setting | What you avoid |
|---|---|---|
| **Default (RabbitMQ memory queue, auto-ack)** | None | Just speed; nothing else |
| **Persistent queue + persistent message** | `durable: true`, `persistent: true` | Broker crash data loss |
| **Publisher confirms** | `channel.confirmSelect()` | Producer-broker network drop |
| **Manual consumer ack** | `autoAck: false`, `basicAck()` after processing | Consumer crash mid-processing |

**For data safety:** persistent queue + persistent messages + publisher
confirms + manual consumer acks. Accept the perf hit (typically 5–20× slower
than memory-only).

---

## Replication / High Availability

Brokers replicate to survive node failure.

| Pattern | RabbitMQ name | How it works |
|---|---|---|
| **Active-passive (hot standby)** | Mirrored queues (legacy) | Primary holds queue; secondaries mirror it; failover on primary loss |
| **Quorum-based** | Quorum queues (Raft) | Raft consensus across N nodes; majority must ack write |

**Mirrored queues are deprecated** in favor of quorum queues in RabbitMQ
3.8+. Use quorum queues for new deployments.

**SQS handles replication transparently** — three-AZ replication with no
configuration needed.

---

## The Two Core Delivery Patterns

### Competing Consumers (One Queue, Many Consumers)

```
                ┌──────────┐
   Producer  ──►│  Queue   │
                └────┬─────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
  ┌───────────┐ ┌───────────┐ ┌───────────┐
  │Consumer 1 │ │Consumer 2 │ │Consumer 3 │
  └───────────┘ └───────────┘ └───────────┘

  Each message goes to ONE consumer.
  Parallelism = number of consumers.
```

Use for parallel work where order doesn't matter and any consumer can handle
any message. Classic example: image-resize jobs, billing webhooks, email
sending.

### Publish-Subscribe (One Topic, Many Subscribers)

```
                ┌──────────┐
   Producer  ──►│  Topic   │
                └────┬─────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
  ┌───────────┐ ┌───────────┐ ┌───────────┐
  │Subscriber1│ │Subscriber2│ │Subscriber3│
  └───────────┘ └───────────┘ └───────────┘

  Each message goes to ALL subscribers.
  Each subscriber gets its own copy.
```

Use for event broadcasting where multiple independent consumers care.
Classic example: order placed → notify shipping, billing, inventory,
analytics.

**RabbitMQ implements both** via *exchanges*: direct exchange → queue (point-
to-point), fanout exchange → all bound queues (pub-sub), topic exchange →
queues matching routing keys (selective fanout).

---

## RabbitMQ-Specific Operational Patterns

### Connections vs Channels

```
┌─────────────────────────────────────────┐
│              Application                │
│                                          │
│   ┌────────────────────────────────┐    │
│   │     TCP Connection (heavy)     │    │
│   │                                 │    │
│   │  ┌─────────┐  ┌─────────┐      │    │
│   │  │ Channel │  │ Channel │ ...  │    │
│   │  │  #1     │  │  #2     │      │    │
│   │  └─────────┘  └─────────┘      │    │
│   │  per-thread, lightweight       │    │
│   └────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

| | Connection | Channel |
|---|---|---|
| Cost | Heavyweight TCP | Lightweight logical |
| Thread-safe | Yes | **No** — never share across threads |
| Pattern | One per app process | One per producer/consumer thread |

**Channel pool pattern:** for server-managed thread environments (servlet
containers, framework worker pools), use Apache Commons Pool to manage
channels. Never share a channel across threads.

### Provisioning Queues for the Broker

Gorton's tip: RabbitMQ uses one thread per queue. Provision enough queues
to match cores on the broker for full throughput. A broker with 8 cores and
1 queue uses 1 core.

### Memory Pressure and Throttling

RabbitMQ throttles producers at ~40% memory by default. Symptom: producers
silently slow down, queues stop growing, throughput plummets. Configure
`vm_memory_high_watermark` and disk thresholds explicitly for production.

---

## Duplicate Detection (Idempotency)

At-least-once delivery means consumers may see a message multiple times.
Two ways to handle it:

### App-Side Idempotency (Universal)

Producer attaches an `Idempotency-Key`. Consumer stores keys in a fast lookup
(Redis) and skips already-seen ones.

```python
def process(msg):
    key = msg.headers["Idempotency-Key"]
    if redis.set(key, 1, nx=True, ex=86400):
        do_work(msg)
        ack(msg)
    else:
        # already seen — just ack
        ack(msg)
```

### Broker-Side Duplicate Detection (Some Brokers)

ActiveMQ Artemis: `HDR_DUPLICATE_DETECTION_ID` header. Broker tracks recent
IDs and silently drops duplicates.

**Use both when available.** Broker-side catches network-replay duplicates;
app-side catches everything else.

---

## Poison Messages and Dead-Letter Queues

A **poison message** is one a consumer can't process — bad payload, schema
mismatch, infinite-loop bug. Without intervention, the broker keeps redelivering
it; consumers crash repeatedly; the queue blocks.

```
                Queue ◄───────────┐
                  │               │
                  ▼  redelivery   │
              Consumer crashes ───┘
                  
              (Repeat forever — queue blocked)
```

**The fix:** dead-letter queue (DLQ).

```
                Queue ──────────► Consumer
                  │                  │
                  │ ◄────────────────┤  reject (negative ack)
                  │                  │
   maxReceiveCount: 5
                  │ exceeded?
                  ▼
                DLQ  ────────►  Manual / alerting / replay tooling
```

**Settings:**

| Knob | Typical | Why |
|---|---|---|
| `maxReceiveCount` | 3–5 | Few enough to detect quickly, enough to ride out transient failures |
| DLQ retention | Days | Time to investigate and fix |
| Alert on DLQ growth | Yes | Otherwise you find out about silent failures the hard way |

**Don't run a DLQ without alerting.** A silent DLQ is worse than no DLQ.

---

## Principles

- **Push beats pull for high-throughput consumers.** Use polling only for
  controlled-batch use cases.
- **For data safety: publisher confirms + persistent queues + persistent
  messages + manual consumer acks.** Accept the perf hit.
- **One thread per channel, or use a channel pool.** Channels are not
  thread-safe.
- **Provision enough queues to match broker cores** for full throughput.
- **Keep queue depth low.** Broker performance degrades as memory pressure
  rises (RabbitMQ throttles at ~40%).
- **Use idempotency keys at the producer; idempotent processing at the
  consumer.**
- **Set `maxReceiveCount=3–5` and route failures to a DLQ. Alert on DLQ
  growth.**
- **Don't roll your own replication / consensus.** "Your solution will not
  work as well as existing solutions."
- **Quorum queues over mirrored queues** for new RabbitMQ deployments.

---

## Anti-Patterns

### Auto-Ack with Critical Work

**Looks like:** Consumer pulls message, broker auto-acks, consumer crashes
mid-processing. Message gone forever.

**Why it fails:** Auto-ack means "broker assumes you got it." Crash mid-
processing = silent loss.

**The fix:** `autoAck=false`. Manually ack only after processing succeeds.

### No Publisher Confirms

**Looks like:** Producer publishes; network drops; producer thinks it succeeded.
Message never reached the broker.

**Why it fails:** Without publisher confirms, the producer has no way to
know.

**The fix:** Enable publisher confirms. Use synchronous or batched
confirmation depending on throughput needs.

### Memory-Only Queues for Important Data

**Looks like:** RabbitMQ broker crashes; queue contents gone.

**Why it fails:** Memory-only queues don't survive broker restart.

**The fix:** `durable: true` on the queue + `persistent: true` on messages
(`deliveryMode=2` in AMQP).

### Channel Per Operation

**Looks like:** Open a channel for each publish, close it after. Throughput
collapses.

**Why it fails:** Channels are cheap relative to connections but not free
to create. Constant churn destroys throughput.

**The fix:** Channel pool or one channel per long-lived thread.

### Sharing a Channel Across Threads

**Looks like:** Multiple worker threads call `basicPublish` on the same
channel. Random message corruption / errors.

**Why it fails:** Channels aren't thread-safe.

**The fix:** Channel-per-thread or channel pool.

### No DLQ — or DLQ Without Alerts

**Looks like:** Poison message redelivers forever; consumer keeps crashing;
no one notices for hours.

**Why it fails:** Failures need to surface.

**The fix:** DLQ with `maxReceiveCount=3–5`, alerting on DLQ growth, and
investigation tooling (reading messages, replaying after fix).

### Rolling Your Own Replication

**Looks like:** Building a "highly available" custom messaging layer over
some primitive store.

**Why it fails:** Distributed consensus, leader election, split-brain handling
— each one is a research-paper-sized problem. Your version misses edge cases.

**The fix:** Use the boring, well-tested platform. RabbitMQ quorum queues,
SQS, Kafka — they've been hardened.

---

## Decision Rules

| Situation | Action |
|---|---|
| Decoupled producer/consumer, AWS-only | SQS (managed, simple, scales) |
| On-prem or multi-cloud, rich routing | RabbitMQ |
| Java enterprise integration | JMS implementation (ActiveMQ Artemis, IBM MQ) |
| Event log + replay needed | Kafka — see `event-streaming-with-kafka` |
| MQTT IoT-style fan-out | MQTT broker (Mosquitto, HiveMQ) |
| Strict ordering needed | Single consumer per partition (Kafka) or single-consumer queue |
| Parallel work, order doesn't matter | Competing consumers |
| Multiple independent listeners on one event | Pub-sub (topic / fanout exchange) |
| Need data safety | Persistent queue + persistent message + publisher confirms + manual ack |
| Network partition / broker fault tolerance | Quorum queues (RabbitMQ) or SQS / Kafka |
| Risk of bad messages | DLQ with `maxReceiveCount` 3–5 + alerts |
| Multiple consumers want different message subsets | Topic exchange (RabbitMQ) or filtered subscriptions |

---

## Worked Example: Order-Placed Event Fanout

**Context:** E-commerce checkout. When an order is placed, multiple
downstream services need to react: shipping, billing, inventory adjustment,
analytics, notifications.

**Design:**

| Component | Choice | Why |
|---|---|---|
| Broker | RabbitMQ Cluster (3 nodes) | On-prem, rich routing, quorum queues |
| Pattern | Pub-sub via fanout exchange | Independent consumers each get a copy |
| Exchange | `orders.fanout` | Fanout = all bound queues receive |
| Queues | One per consumer service: `shipping.q`, `billing.q`, `inventory.q`, `analytics.q`, `notifications.q` | Each service has its own queue, scales consumers independently |
| Queue type | Quorum queue, durable | Survives broker failure |
| Message | Persistent, with `Idempotency-Key` | Survives broker restart; consumers dedup |
| Consumers | Manual ack after processing | No mid-processing loss |
| Publisher | Publisher confirms enabled | No silent producer-side loss |
| DLQ | One per service queue, `maxReceiveCount=3` | Each service handles its own failures |

**Topology:**

```
                       fanout exchange
                         orders.fanout
                              │
          ┌────────┬──────────┼──────────┬─────────┐
          ▼        ▼          ▼          ▼         ▼
      shipping   billing  inventory  analytics  notifications
        .q        .q        .q         .q          .q
          │        │         │          │           │
          ▼        ▼         ▼          ▼           ▼
     shipping  billing   inventory  analytics  notifications
     consumers consumers consumers  consumers   consumers

     each service-queue has its own DLQ
```

**Failure handling:**
- Shipping service is down: messages accumulate in `shipping.q`. Other services
  unaffected. When shipping recovers, queue drains.
- Bad message format: redelivered up to 3 times, then to `shipping.q.dlq`.
  Alert fires; engineer investigates.
- Producer crash mid-publish: publisher confirms ensure no silent loss.

---

## Gotchas

- **Default RabbitMQ acks are auto-ack.** Many tutorials show this. Don't use
  it for anything you care about.
- **Persistent message + non-durable queue = loss on restart.** Both flags
  must be set.
- **Channel churn** (constant create/close) tanks throughput more than people
  expect.
- **RabbitMQ memory pressure throttles producers silently.** Watch
  `vm_memory_high_watermark`.
- **Mirrored queue replication has known edge cases.** Quorum queues (Raft-
  based) replace them.
- **SQS visibility timeout** is the SQS equivalent of "until ack." Too short
  → messages reprocessed; too long → slow recovery from consumer crashes.
- **SQS standard queues are at-least-once.** If you need exactly-once,
  combine with idempotency keys (or use SQS FIFO, which adds dedup at the
  cost of throughput).
- **JMS is an interface spec, not an implementation.** Different JMS providers
  have different reliability guarantees.
- **Kafka isn't a queue** in the RabbitMQ sense — see
  `event-streaming-with-kafka`.

---

## Related Skills

- `distributed-systems-essentials` — at-least-once / exactly-once / idempotency
- `microservices-resilience-patterns` — circuit breakers around message
  publishing
- `event-streaming-with-kafka` — Kafka's different model (event log vs queue)
- `distributed-system-patterns` — Saga pattern uses messaging
- `serverless-processing-systems` — Lambda triggered by SQS / SNS / EventBridge

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 7. Hohpe and
Woolf's *Enterprise Integration Patterns* is the canonical pattern catalog.
