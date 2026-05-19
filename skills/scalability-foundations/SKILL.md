---
name: scalability-foundations
description: >
  Frame scalability as a primary design driver, distinguish scaling strategies
  (replication vs optimization, scale-up vs scale-out), apply Amdahl's law to
  reason about hardware ceilings, and walk through the canonical multitier
  scaling moves (load-balanced stateless services, distributed caching,
  partitioned databases, async queueing). Use when starting a new system,
  explaining scalability trade-offs to non-architects, deciding whether and
  how to invest in scaling, or diagnosing whether the right scaling strategy
  is being applied. Triggers - "how do we scale this", "scale up vs scale
  out", "do we need a load balancer / cache / queue", "Amdahl's law",
  "multitier architecture", "we're hitting a bottleneck", "premature
  optimization vs premature distribution". Produces a scaling-strategy
  recommendation grounded in concrete bottleneck and trade-off analysis.
---

# Scalability Foundations

You frame and direct early scaling decisions. Scalability is the system's
ability to absorb growth — concurrent requests, data volume, derived insights —
without a redesign. Most systems that fail at scale weren't built to scale;
the cost of retrofitting is often higher than rebuilding.

This skill captures the foundational mental models from Gorton's *Foundations
of Scalable Systems* (Ch 1–2): the two universal scaling strategies, Amdahl's
law as the hardware-scaling ceiling, and the canonical sequence of multitier
scaling moves.

---

## When to Use This Skill

- Starting a new system and deciding how much to invest in scalability up front
- Explaining trade-offs between scalability and performance / availability /
  security / manageability to engineers, PMs, or executives
- Diagnosing whether the right tier is being scaled (often it isn't)
- Deciding when to introduce a load balancer / cache / queue / shard
- Pushing back on "premature distribution" or "premature optimization" in
  either direction

---

## The Two Universal Scaling Strategies

```
┌─────────────────────────────────┐    ┌─────────────────────────────────┐
│         REPLICATION             │    │         OPTIMIZATION            │
│                                 │    │                                 │
│   Add more identical units      │    │   Use existing units better     │
│   ─────────────────────────     │    │   ─────────────────────────     │
│   • More app servers            │    │   • Faster algorithms           │
│   • More cache nodes            │    │   • Better serialization        │
│   • More DB shards              │    │   • Connection pooling          │
│   • More message brokers        │    │   • Batching                    │
│   • More replicas               │    │   • Hardware-friendly code      │
│                                 │    │                                 │
│   Cost: scales linearly         │    │   Cost: bounded — eventually    │
│   with capacity                 │    │   the well runs dry             │
└─────────────────────────────────┘    └─────────────────────────────────┘
```

**Almost every chapter of every distributed-systems book is one of these in
disguise.** Recognizing which one a tactic belongs to is the fastest way to
reason about it.

| Tier | Replication move | Optimization move |
|---|---|---|
| App tier | Stateless replicas behind LB | Async I/O, connection pooling |
| Cache tier | Distributed cache cluster | Hash partitioning, cache-aside |
| DB tier | Sharding + replica sets | Indexes, denormalization, batching |
| Messaging | Quorum queues, mirrored queues | Channel pooling, batching |
| Streaming | Partitioned topics | RocksDB state, checkpoints |

**Rule:** Replicate to alleviate *real* bottlenecks. Replicating non-bottlenecks
adds cost without benefit. Measure first.

---

## Scale Up vs Scale Out

| | Scale Up (vertical) | Scale Out (horizontal) |
|---|---|---|
| Mechanism | Bigger box: more cores, RAM, disk | More boxes behind a coordinator |
| Diminishing returns | Steep — at the high end you pay 4× for 1.5× perf | Gentler — adding box N+1 is similar to N |
| Hardware cap | A single machine's max | None practical |
| Failure domain | Single box → 100% outage | Single box → 1/N outage |
| Code requirements | Should be multithreaded; otherwise pointless | Must be stateless or have a shared state plane |
| Operational complexity | Low (one machine) | Higher (LB, deploys, distributed debugging) |

**Default in 2026:** Scale out for production. Scale up the database tier where
shared-everything is operationally simpler than sharding.

**Reality check:** AWS RDS benchmarks (db.t2.micro through db.t2.2xlarge) show
diminishing returns long before you hit the largest box. Always measure.

---

## Amdahl's Law: The Ceiling on Hardware Scaling

```
Speedup ≤ 1 / (s + (1 − s) / n)

s = serialized fraction of work
n = number of processors
```

| Serialized fraction | Practical ceiling |
|---|---|
| 5% serial | ~20× speedup, no benefit beyond ~2,048 cores |
| 25% serial | ~4× speedup |
| 50% serial | ~2× speedup, no benefit beyond ~8 cores |

**Implications:**

1. Single-threaded code does not scale up. Spending money on cores you can't
   use is a category error.
2. Critical sections in concurrent code are the serialized portion. Keep them
   small.
3. Database row-level locks under high contention behave like serial code.
   The DB is the world's most popular Amdahl bottleneck.
4. Distributed scalability is bounded by per-node serialization too — coordination,
   shared mutexes, hot leaders, single-threaded broker dispatch.

> "Not even money will buy you scalability" if your code is single-threaded.

---

## The Canonical Multitier Scaling Sequence

Most internet-facing systems evolve along this path. Each move responds to a
specific bottleneck — apply only the moves that match yours.

```
                ┌───────────────────────────────────────────┐
       Step 0 → │  Single box: app + DB on one machine      │
                └───────────────────────┬───────────────────┘
                                        │ (CPU saturation)
                ┌───────────────────────▼───────────────────┐
       Step 1 → │  Scale up: bigger box                     │
                └───────────────────────┬───────────────────┘
                                        │ (single-machine ceiling)
                ┌───────────────────────▼───────────────────┐
       Step 2 → │  Stateless services + load balancer       │
                │  (session state moves to external store)  │
                └───────────────────────┬───────────────────┘
                                        │ (DB read-saturation)
                ┌───────────────────────▼───────────────────┐
       Step 3 → │  Distributed cache (Redis / memcached)    │
                │  (target ≥80% hit rate)                   │
                └───────────────────────┬───────────────────┘
                                        │ (DB write/storage saturation)
                ┌───────────────────────▼───────────────────┐
       Step 4 → │  Partition the database (shard / split)   │
                │  or replicate read replicas               │
                └───────────────────────┬───────────────────┘
                                        │ (write spikes / sync waits)
                ┌───────────────────────▼───────────────────┐
       Step 5 → │  Async queueing for non-blocking writes   │
                │  (RabbitMQ / SQS / Kafka)                 │
                └───────────────────────┬───────────────────┘
                                        │ (one BFF for all clients
                                        │  becomes a god-API)
                ┌───────────────────────▼───────────────────┐
       Step 6 → │  Backend for Frontend (BFF) per client    │
                └───────────────────────────────────────────┘
```

**Rule:** Stop moving forward when you don't have a measured bottleneck for
the next move. Premature steps are tech debt.

---

## Quality Attribute Trade-Offs

Scalability never lives alone. The book frames it against four others
explicitly:

| Other attribute | How it interacts with scalability |
|---|---|
| **Performance** | Some optimizations hurt scalability. Caching state in memory reduces per-request DB cost but caps concurrent capacity. |
| **Availability** | Replicas help both — but eventual consistency creeps in as the cost. |
| **Security** | TLS, auth, encryption add per-request overhead at every tier. They are *opposing* forces to scalability; the question is how much overhead is acceptable. |
| **Manageability** | Scaling out multiplies the operational surface. Without DevOps automation, the manageability cost outpaces the capacity gain. |

**Translate business concerns to characteristics.** "Black Friday traffic"
becomes elasticity, throughput, response-time-under-load. "Customer trust"
becomes availability + integrity. Always do this translation before debating
architecture.

---

## Hyperscale Economics

Gorton's definition: **a system exhibiting exponential growth in computational
and storage capabilities while exhibiting linear growth in costs.** This is
the goal of horizontal scaling done right — and the failure mode of horizontal
scaling done wrong (where ops cost goes superlinear).

**The lever for hyperscale economics:** automation. DevOps, infrastructure-as-
code, auto-scaling groups, deployment pipelines, observability dashboards.
Replication of stateful systems without automation = manageability collapse.

> "You can't manage what you can't measure."

---

## Principles

- **Replication and optimization are the two strategies.** Recognize which one
  a tactic belongs to.
- **You cannot bolt scalability on later.** The retrofit cost is brutal —
  HealthCare.gov, COVID-era unemployment systems, every Black Friday outage.
  Architecture *has* to support scaling even if you don't apply every pattern
  yet.
- **Scale the actual bottleneck.** Replicating non-bottlenecks adds cost
  without benefit.
- **Measure before scaling.** Bigger isn't always faster. Run the experiment.
- **Stateless or it doesn't scale.** Move session state to an external store.
- **Aim for ≥80% cache hit rate** when introducing caching, or it isn't
  earning its complexity.
- **Use queues whenever the write result isn't needed synchronously.**
- **Automation is the lever for hyperscale economics.** Without it, ops cost
  outpaces capacity gain.
- **Keep critical sections small** — Amdahl's law sets the per-node ceiling.

---

## Anti-Patterns

### Premature Distribution

**Looks like:** A 3-engineer team architects 8 microservices, Kafka, a service
mesh, and global multi-region deployment "for future scale."

**Why it fails:** You pay all the operational complexity of a distributed
system before having a single load problem to justify it. Velocity collapses.

**The fix:** Start with a well-modularized monolith on a single load-balanced
tier. Add distributed pieces only when a measured bottleneck demands it.

### Bolt-On Scalability

**Looks like:** Stateful sessions everywhere, schema with no shard key, every
service calls every other service synchronously. Then traffic spikes and the
team panics-builds a cache, then a queue, then sharding, in a quarter.

**Why it fails:** Each retrofit changes a contract that hundreds of code paths
depend on. Bug count spikes; reliability tanks.

**The fix:** Architect for scale from the beginning even if you don't deploy
every piece. Keep services stateless. Plan a shard key from day one even if
you only have one shard.

### Throwing Hardware at Single-Threaded Code

**Looks like:** "We're CPU-bound, let's get a 96-core machine." The serial
fraction is 50%. Speedup is ~2×.

**Why it fails:** Amdahl's law caps you. The bigger box is mostly idle.

**The fix:** Profile. Find the serialized hot path. Refactor for concurrency
or shard the workload across nodes.

### Scaling the Wrong Tier

**Looks like:** App tier saturated (CPU >80%), team adds DB read replicas.

**Why it fails:** The bottleneck isn't the DB. The replicas sit idle. The
app tier still saturates.

**The fix:** Profile *which* tier is the bottleneck. Replicate that tier.

### Reading "Real-Time" Literally

**Looks like:** A reporting use case becomes "we need real-time analytics" → 
team builds Kafka + Flink + low-latency dashboards. It runs at 8% utilization
and consumes a quarter of the budget.

**Why it fails:** "Real-time" usually meant "fresher than the nightly
batch" — i.e., 5–10 min. Streaming is 10× the operational complexity of
batch.

**The fix:** Quantify the freshness requirement. Build the simplest thing
that meets it. Most "real-time" requirements collapse to near-real-time on
inspection.

---

## Decision Rules

| Situation | Action |
|---|---|
| New system, unknown scale | Stateless services + load balancer + external state store. Architect for scaling out without doing it yet. |
| App tier saturating | Add replicas behind LB. Verify session state is external first. |
| DB read-saturated, hit rate-friendly data | Distributed cache (cache-aside). Aim ≥80% hit rate. |
| DB write-saturated | Partition / shard. Pick a shard key with even distribution. |
| Read-heavy with stale-tolerant data | Read replicas before sharding. |
| Spiky writes, result not needed sync | Async queue. |
| Multiple distinct client types | BFF per client class. |
| Single-machine ceiling reached | Stop scaling up; start scaling out. |
| Load is highly bursty (1% peak / 99% idle) | Serverless (Lambda, GAE) — see `serverless-processing-systems`. |
| Engineers asking for service mesh on a 3-service system | Decline. Add one when service count + ops maturity justifies it. |

---

## Worked Example: Sizing a Greenfield SaaS Backend

**Context:** B2B SaaS, expected 5K MAUs in 6 months, 100K MAUs in 24 months.
Two engineers. Database-heavy CRUD app + a few async jobs.

**Top critical characteristics:**
1. Time-to-market (engineering velocity)
2. Manageability (small ops surface)
3. Scalability headroom (24-month plan)

**Plan:**

| Stage | Architecture | Why |
|---|---|---|
| Day 0 (5K MAUs) | Single Postgres + Node/Express on a small VM. No LB. | Time-to-market. Single box handles 5K easily. |
| Month 6 (5K → 25K) | Add LB; deploy 2-3 stateless app instances. Move sessions to Redis. | Stateless tier, free horizontal scaling. |
| Month 12 (25K → 75K) | Add Redis cache for hot reads. Add async queue for emails / billing webhooks. | Reduce DB load; decouple non-blocking work. |
| Month 18 (75K → 100K) | Read replicas on Postgres if read load > write load. Otherwise consider partitioning. | Replicate the actual bottleneck. |

**What we deliberately don't do up front:**
- Microservices (team too small)
- Kafka (no event-replay or multi-consumer use case)
- Multi-region (cost without business case)
- Service mesh (3-tier system doesn't justify it)

**Lesson:** Architect to support each future move (stateless services from
day 0, shard key in schema). Defer cost until a measured bottleneck demands it.

---

## Gotchas

- **"Real-time" almost always means "near real-time."** Quantify the freshness
  SLA before building streaming infrastructure.
- **Cache layer requires explicit miss-handling logic and invalidation
  policy.** Cache-aside is rarely free; design before you adopt.
- **Sticky sessions silently sabotage horizontal scaling.** Replicas accumulate
  long-lived sessions and become persistent hot spots. Use only when truly
  necessary.
- **Bigger hardware doesn't fix slow code.** Profile first.
- **Single-DB bottlenecks emerge once the stateless tier is well scaled.** Be
  ready for it; don't be surprised.
- **Security and scalability oppose each other.** Every TLS handshake, every
  auth check, every encryption pass adds overhead. The question is *how much
  overhead* you can afford, not whether to have any.

---

## Related Skills

- `architecture-styles-monolithic-and-distributed` — choosing the top-level style
- `distributed-systems-essentials` — networking, RPC, partial failure substrate
- `concurrent-systems-foundations` — per-node concurrency under Amdahl's law
- `load-balancing-and-app-services` — the request-handling tier
- `distributed-caching-patterns` — when and how to add caching
- `asynchronous-messaging-patterns` — when and how to add queueing
- `microservices-resilience-patterns` — circuit breakers, bulkheads
- `architecture-characteristics-and-tradeoffs` — translating business goals
  to architectural characteristics

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapters 1–2.
