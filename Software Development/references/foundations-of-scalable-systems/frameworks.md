# Frameworks Index: Foundations of Scalable Systems

Quick-reference catalog of every named framework, pattern, algorithm, and
concept Gorton uses in the book. Use this as a lookup table when you want to
recall a definition without re-reading a chapter.

Source: Ian Gorton, *Foundations of Scalable Systems* (O'Reilly, 2022).

---

## Foundational Concepts

| Concept | One-line definition |
|---|---|
| **Scalability** | A system's ability to handle increased operational load by adding resources, ideally with linear cost growth. |
| **Hyperscale system** | Exhibits exponential growth in computational/storage capability with linear cost growth. |
| **Replication strategy** | Add more identical processing/storage units to absorb load. |
| **Optimization strategy** | Use existing resources better via faster algorithms, smarter serialization, hardware-friendly code. |
| **Quality attribute** | A non-functional requirement (scalability, performance, availability, security, manageability, maintainability). |
| **CIA triad** | Confidentiality, Integrity, Availability — the security framing. |
| **DevOps** | The automation discipline that keeps manageability cost from blowing up as systems scale out. |
| **Replica consistency** | The new problem the moment you replicate stateful resources. |

---

## The Two Essential Problems of Distributed Systems

1. **Components fail individually** while the system as a whole keeps running.
2. **Coordination across components** must work without a global clock and
   under partial failure.

Every distributed pattern in the book is fundamentally a response to one of
these.

---

## Amdahl's Law

> *Speedup ≤ 1 / (s + (1 − s) / n)*
>
> where `s` is the serialized fraction of work, `n` is the number of
> processors.

| Serialized fraction | Practical ceiling |
|---|---|
| 5% | ~20× speedup, regardless of cores beyond ~2,048 |
| 25% | ~4× speedup |
| 50% | ~2× speedup, no benefit beyond ~8 cores |

**Implication:** Code parallelism is the upper bound on hardware scalability.
Critical sections must be small; serialized I/O patterns must be eliminated;
single-threaded code does not benefit from a bigger box.

---

## Concurrency

| Concept | Definition |
|---|---|
| **Thread** | An OS-scheduled execution context within a process. |
| **Race condition** | Interleaved access to shared state producing incorrect, intermittent results. |
| **Critical section** | Code that mutates shared state and must execute atomically. |
| **Synchronized / monitor lock** | Java's per-object intrinsic lock; "the bathroom on a long-distance bus." |
| **Deadlock / deadly embrace** | Circular wait on locks acquired in inconsistent order. |
| **Dining philosophers** | Canonical deadlock illustration; fix by imposing a global lock-acquisition order. |
| **Producer-consumer** | A pattern with a thread-safe FIFO buffer between the two roles. |
| **Thread pool** | Pre-allocated worker threads that accept tasks (Java: ExecutorService). |
| **Barrier synchronization** | All threads block until N reach a point (Java: CountDownLatch). |
| **CSP / Goroutines / Channels** | Go's concurrency model. |
| **Actor model** | Erlang's concurrency model — independent actors with mailboxes. |
| **Event loop** | Node.js's single-threaded async I/O model. |

---

## Distributed Systems Substrate

| Concept | Definition |
|---|---|
| **LAN vs WAN** | Sub-ms latency vs tens of ms; WAN bounded by speed of light in fiber. |
| **TCP** | Reliable, connection-oriented, in-order. |
| **UDP** | Unreliable, fire-and-forget; datagram. |
| **DNS** | Hierarchical replicated address book of the internet. |
| **RPC / RMI** | Remote procedure call abstraction with location transparency, marshalling, stubs/skeletons. |
| **gRPC** | Modern RPC over HTTP/2 with Protobuf. |
| **Asynchronous network** | No bound on message delivery time; no synchronized clocks. |
| **Partial failure** | Slow / lost / never-arriving responses are indistinguishable from the client. |
| **Idempotence** | Multiple identical requests produce the same effect as one — required for at-least-once delivery. |
| **Idempotency key** | Unique client-generated identifier stored server-side to filter duplicates. |
| **At-most-once delivery** | Fire and forget; messages may be lost; no duplicates. |
| **At-least-once delivery** | Messages won't be lost; duplicates possible. |
| **Exactly-once delivery** | Each message takes effect exactly once — built on at-least-once + idempotence. |
| **Two Generals' Problem** | Coordination on a lossy channel cannot guarantee mutual agreement in bounded time. |
| **FLP Impossibility** | Consensus on an asynchronous network with crash faults is not bounded. |
| **Byzantine fault** | Malicious failure; out of scope inside trusted enterprise networks. |
| **Wall-clock time** | Time-of-day; can jump backward (NTP). |
| **Monotonic time** | Only moves forward; correct for measuring elapsed time. |
| **NTP / Chrony / Amazon Time Sync** | Clock-sync services with varying accuracy. |

---

## Application Tier

| Concept | Definition |
|---|---|
| **REST / RESTful API** | HTTP API treating URIs as resources, verbs as operations. |
| **Stateless service** | All state external; required for free load distribution. |
| **Session affinity / sticky sessions** | LB binds a client to a single replica; needed for stateful, costs load balance. |
| **Application server** | Listener thread → sockets backlog → HTTP connector → app thread pool → DB connection pool. |
| **Tomcat** | Apache servlet container; default 25 min threads. |
| **Sockets backlog** | OS-level pending-connection queue (Linux default 100). |
| **L4 load balancer** | Network-layer LB (TCP/UDP); fast, dumb. |
| **L7 load balancer** | Application-layer LB (HTTP); request-aware, slower. |
| **Round robin / least connections / fastest response / weighted** | LB distribution policies (HAProxy ~10). |
| **Auto-scaling group** | Replica set with min/max counts that grows/shrinks by schedule or metric. |
| **JMX / MBeans** | JVM's instrumentation/observability standard. |

---

## Caching

| Concept | Definition |
|---|---|
| **Cache hit / cache miss** | Data found vs not found in cache. |
| **TTL (time-to-live)** | Eviction time per entry. |
| **Stale data** | Cached value diverged from source of truth. |
| **Cache-aside** | App checks cache, falls back to DB on miss, populates cache. Most resilient. |
| **Read-through** | Cache transparently fetches on miss via provider hook. |
| **Write-through** | App writes to cache; cache writes to DB synchronously. Consistent, slower. |
| **Write-behind / write-back** | App writes to cache; cache writes to DB asynchronously. Fast, lossy on crash. |
| **Hash partitioning (Redis/memcached)** | Distribute keys across nodes via hash function. |
| **Multi-level web cache** | Browser → org proxy → ISP proxy → reverse proxy → origin. |
| **Cache-Control / ETag / Expires / Last-Modified** | HTTP cache directives. |
| **CDN edge cache** | Caches content close to users (CloudFront, Akamai, Fastly). |

---

## Asynchronous Messaging

| Concept | Definition |
|---|---|
| **Message broker** | The middleware between producers and consumers (RabbitMQ, ActiveMQ, IBM MQ, SQS). |
| **Producer / consumer / queue / topic** | The four primitives. |
| **AMQP** | Open binary message-queue protocol implemented by RabbitMQ. |
| **JMS** | Java's message-queue API spec. |
| **Push (callback) vs pull (polling)** | Broker-driven delivery vs consumer-driven fetch. |
| **Auto-ack vs manual ack** | Auto-ack is fast but loses messages on consumer crash. |
| **Persistent queue / durable queue** | Writes to disk before ack; trades latency for safety. |
| **Publisher confirm** | Broker-acknowledged send. |
| **Competing consumers** | Multiple consumers reading the same queue for parallelism. |
| **Publish-subscribe** | One-to-many delivery via a topic. |
| **Exchange / routing key / binding** | RabbitMQ's flexible routing layer. |
| **Connection vs channel (RabbitMQ)** | Heavyweight TCP connection multiplexes lightweight logical channels. |
| **Channel pool** | Pattern for thread-safe channel reuse. |
| **Mirrored queue** | Older RabbitMQ replication scheme. |
| **Quorum queue** | Newer Raft-based RabbitMQ replication. |
| **Idempotency key / duplicate detection** | E.g., HDR_DUPLICATE_DETECTION_ID in ActiveMQ. |
| **Poison message** | A message that crashes consumers or is rejected repeatedly. |
| **Dead-letter queue** | Holding pen for failed messages. |
| **maxReceiveCount** | Number of redeliveries before DLQ routing (typical 3–5). |

---

## Serverless

| Concept | Definition |
|---|---|
| **IaaS** | Pay for provisioned VMs (EC2, etc.). |
| **FaaS / Serverless** | Pay per request/duration with auto-scale. |
| **GAE Standard / Flexible** | Tightly managed (rapid scale) vs Docker-on-VM. |
| **target_cpu_utilization** | GAE: scale up when above this. (0.5–0.95) |
| **max_concurrent_requests** | GAE: requests per instance before scaling. (1–80) |
| **target_throughput_utilization** | GAE: similar for throughput. (0.5–0.95) |
| **max-pending-latency** | GAE: max acceptable request queue time. |
| **Cold start** | First-invocation latency for a new function instance (100s of ms to seconds). |
| **Freezing / thawing** | Lambda's lifecycle states: freeze idle environments, thaw to reuse. |
| **Lambda memory** | Tuning knob; at 1,769 MB you get one full vCPU. |
| **Burst limit** | Region-specific concurrent-invocation cap (e.g., 3,000 in us-west-1). |
| **Reserved concurrency** | Per-function cap to isolate noisy-neighbor effects. |
| **Throttling / 429** | "Too many requests" — Lambda's signal to retry. |
| **Parameter study** | Sweep over a range of config combinations to find a Pareto-optimal point. |

---

## Microservices

| Concept | Definition |
|---|---|
| **Two-pizza rule** | A team should be small enough to feed with two pizzas. |
| **Bounded context** | DDD-derived scope each microservice owns. |
| **API gateway** | Single client-facing entry point; auth, throttling, caching, routing. |
| **Workflow** | A multi-microservice request orchestration. |
| **Orchestration** | Central coordinator drives the workflow. |
| **Choreography** | Event-driven decentralization; services subscribe and react. |
| **Cascading failure** | Slow downstream exhausts upstream thread pools, propagates back through the call chain. |
| **Long-tail response time** | Small % of requests take 20–100× the average (GC pauses, contention, page faults, dropped packets). |
| **Throttling / rate limiting** | LB or gateway feature; protects backends. |
| **Read timeout** | Client-side time before declaring a request failed. Critical for fail-fast. |
| **Default / fallback response** | Degraded but available service. |
| **Circuit breaker** | Wraps a call; OPEN on repeated failure, HALF_OPEN to probe recovery, CLOSED when healthy. |
| **Bulkhead** | Partitioned thread pools per API to prevent cross-API thread starvation. |
| **Exponential backoff** | Retry with increasing delays to avoid retry storms. |
| **Fault isolation** | A failing service can't bring down the whole system. |

---

## Database Distribution

| Concept | Definition |
|---|---|
| **Scale up vs scale out** | Bigger box vs more boxes. |
| **Read replication / primary–secondary** | Read scaling via async-replicated followers; stale reads possible. |
| **Horizontal partitioning (sharding)** | Split rows across nodes by key. |
| **Vertical partitioning** | Split columns within a row across stores. |
| **Shared-everything** | Cluster nodes share storage (Oracle RAC + SAN). |
| **Shared-nothing** | Each node owns its data (most NoSQL, NewSQL). |
| **NewSQL / distributed SQL** | Born-distributed relational DBs (Spanner, CockroachDB, YugabyteDB, VoltDB). |
| **NoSQL data models** | Key-Value, Document, Wide Column, Graph. |
| **Schemaless** | No upfront format declaration. |
| **Denormalization** | Duplicating data across logical tables to avoid joins; central NoSQL design tenet. |
| **Hash sharding** | Hash(key) mod N → node. Even distribution, no range queries. |
| **Range-based sharding** | Contiguous key ranges per node. Range queries cheap, hot-spot risk. |
| **Value-based sharding** | Specific values map to specific nodes. |
| **Consistent hashing** | Refinement of hash sharding that minimizes redistribution on resize. |
| **CAP theorem** | Under network partition: pick CP or AP, not both. (Healthy network: both achievable.) |

---

## Eventual Consistency

| Concept | Definition |
|---|---|
| **Inconsistency window** | Period between a write at one replica and convergence across all. |
| **Stale read** | Read returns a value older than the latest committed write. |
| **Read your own writes (RYOW)** | Guarantee a client sees its own updates on subsequent reads. |
| **Tunable consistency** | (N, W, R) — N replicas, W writes ack, R reads ack. |
| **Quorum** | Majority — `(N/2)+1`. R+W > N guarantees latest read on healthy cluster. |
| **Coordinator** | The replica handling a given request in a leaderless system. |
| **Sloppy quorum + hinted handoff** | Accept writes on stand-in nodes when home replicas unavailable; replay later. |
| **Anti-entropy** | Background reconciliation between replicas. |
| **Merkle tree** | Tree of hashes used by anti-entropy; only divergent branches need transfer. |
| **Last-writer-wins (LWW)** | Timestamp-ordered conflict resolution; silently loses concurrent updates. |
| **Version vector** | Per-replica logical clock attached to objects; detects concurrent writes. |
| **Sibling** | Riak's term for divergent versions returned together for app-level resolution. |
| **CRDT** | Conflict-free replicated data type whose semantics let the DB resolve conflicts deterministically (counters, sets, hash tables, lists, logs). |

---

## Strong Consistency and Consensus

| Concept | Definition |
|---|---|
| **ACID** | Atomicity, Consistency, Isolation, Durability. |
| **Transactional consistency** | Business-rule preservation across a transaction's writes. |
| **Replica consistency** | All replicas see the same state. |
| **Two-phase commit (2PC)** | Coordinator + participants; prepare phase, resolve phase. Blocks on coordinator failure. |
| **Compensating action** | Manual rollback when transactions aren't available. |
| **XA protocol** | The cross-resource 2PC standard. |
| **JTA / JTS** | Java Transaction API / Service. |
| **Atomic broadcast** | Leader-based ordered delivery. |
| **Paxos** | Leslie Lamport, 1998. Leaderless consensus. Hard. |
| **Multi-Paxos** | Optimization for repeated consensus rounds. |
| **Raft** | Diego Ongaro, 2013. "An understandable consensus algorithm." Leader-based, with terms, AppendEntries, heartbeats. |
| **Raft term** | Monotonically increasing logical clock per leadership period. |
| **AppendEntries / heartbeat** | Raft's log replication and liveness signal (300–500 ms typical). |
| **Quorum-based commit** | Leader commits an entry once a majority of followers have replicated it. |
| **Linearizability** | Real-time ordering preserved (distributed-systems community). |
| **Serializability** | Transactions appear to execute sequentially (DB community). |
| **TrueTime** | Google's GPS+atomic clock service with bounded clock skew (~7 ms). |
| **Commit-wait** | Block until bounded clock skew has elapsed; ensures global ordering. |
| **Strongly consistent reads** | Explicit setting routing reads to leader (e.g., DynamoDB `ConsistentRead=true`). |
| **Single-threaded per partition** | VoltDB's approach: eliminates locking inside a partition. |
| **Deterministic transaction execution** | Calvin / Fauna: pre-order all transactions; replicas produce identical outputs. |

---

## Real-System Mappings (Ch 13)

### Redis
| Concept | Notes |
|---|---|
| **Snapshots vs AOF** | Two persistence options; combine for max safety. |
| **Hash slots** | 16,384 partitions; hash(key) mod 16,384 → slot → node. |
| **Cluster Bus / gossip** | Inter-node membership/state propagation. |
| **Hash tags** | Force keys into the same slot for cross-key ops. |
| **WAIT** | Block writes until N replicas ack. |
| **MULTI / EXEC** | Sequence guarantee; not ACID, no rollback. |

### MongoDB
| Concept | Notes |
|---|---|
| **WiredTiger** | Pluggable storage engine since 3.2; document-level locking, snapshot isolation. |
| **mongod / mongos / config servers** | Daemon, query router, metadata cluster. |
| **Hash vs range sharding** | Two sharding strategies. |
| **Chunk** | 64 MB default; auto-split, auto-rebalanced. |
| **Replica set** | Primary + secondaries; oplog ships to secondaries; Raft-based election. |
| **Heartbeat** | Every 2 s; 10 s without one → election. |
| **Write concern** | Durability requirement — `majority` is default since 5.0. |
| **Read preference** | `primary` (default), `secondary`, `nearest`, etc. |
| **Causal consistency / sessions** | RYOWs at the session level. |

### DynamoDB
| Concept | Notes |
|---|---|
| **Capacity modes** | On-demand vs provisioned (with autoscaling). |
| **RCU / WCU** | Read/write capacity unit. Transactions cost 2× per item. |
| **Adaptive capacity** | Rebalances partitions to match load (hot-key mitigation). |
| **Partition key + sort key** | Composite primary key; group items in one partition. |
| **GSI / LSI** | Global Secondary Index (independent partitioning) vs Local Secondary Index (same partition key). |
| **3 AZ replicas** | Per-region durability. |
| **ConsistentRead=true** | Strongly consistent, against leader, costs 2 RCU. |
| **Global tables** | Multi-region, multi-leader, last-writer-wins on conflicts. |
| **Point-in-time recovery** | Continuous backups for last 35 days. |

---

## Event Streaming (Kafka)

| Concept | Definition |
|---|---|
| **Append-only event log** | Immutable, monotonically increasing offsets. |
| **Destructive vs nondestructive consumption** | Ack-and-remove (RabbitMQ) vs retention-period-based (Kafka). |
| **Topic / partition / offset** | Persistent log organization. |
| **Producer batching** | `batch.size`, `linger.ms` — accumulate before send for throughput. |
| **acks=0/1/all** | Fire-and-forget / leader-only / all ISRs. |
| **enable.idempotence=true** | Broker-side dedup → exactly-once delivery semantics. |
| **Pull (poll) consumer model** | Consumer drives the rate. |
| **commitSync** | Manual offset commit; before processing = at-most-once, after = at-least-once. |
| **Semantic partitioning** | Keyed events all land in the same partition (e.g., by `userID`). |
| **Per-partition ordering** | Kafka guarantees ordering only within a partition, never across. |
| **Consumer group** | Set of consumers that share a topic; partitions distributed among them. |
| **Rebalancing** | Group coordinator reassigns partitions when membership changes. |
| **In-sync replica (ISR)** | Replicas caught up with the leader; leader-eligible. |
| **min.insync.replicas** | Required ISR count for `acks=all` writes. |
| **ZooKeeper** | Externalized cluster metadata (slated for removal in future Kafka). |

---

## Stream Processing

| Concept | Definition |
|---|---|
| **Data in motion** | Process events as they arrive, without batch ETL. |
| **Microbatch** | Aggregate small windows of stream events for periodic computation. |
| **Lambda architecture** | Batch (correct, slow) + speed (approximate, fast) + serving layers. |
| **All-stream / Kappa-style** | Single immutable log + reprocessable streams; replaces Lambda. |
| **Topology / spout / bolt** | Storm's explicit-DAG model. |
| **fieldsGrouping / globalGrouping** | Storm routing strategies. |
| **DataStream API / Table API / SQL API** | Flink's three abstraction levels. |
| **Logical → physical DAG / task slot** | Flink deployment mapping. |
| **Parallelism / setParallelism** | Per-operator concurrency control. |
| **Sliding window** | Overlapping intervals (e.g., 10-min window every 5 min). |
| **Tumbling window** | Disjoint intervals. |
| **Watermark** | Flink's mechanism for handling event-time vs processing-time and late events. |
| **WatermarkStrategy** | API for specifying event-time extraction and out-of-order tolerance. |
| **Stateful operator / RocksDB backend** | Persistent local state for windowed/aggregated computations. |
| **Stream barriers** | Chandy–Lamport-style barriers injected into the source stream for consistent distributed checkpoints. |
| **Checkpoint recovery** | Restart, restore state from latest checkpoint, resume from offset N+1. |

---

## Decision Spectra (For Quick Reference)

### Consistency Spectrum
```
Strong                                                     Eventual
──────                                                     ────────
ACID  →  Linearizable  →  Causal  →  Read-your-writes  →  Eventual
2PC      Spanner          Sessions     Leader reads         Async repl
R+W>N    TrueTime         Bookmarks    Tunable W/R         W=R=1
```

### Delivery Guarantees
```
At-most-once  →  At-least-once  →  Exactly-once
Fire-and-forget   TCP / publisher    Idempotency keys
Auto-ack          confirms           or enable.idempotence
```

### Real-Time Latency Tiers
```
Annual    Daily    Hourly   Minutes   Seconds   Sub-second
batch     batch    batch    micro-    real-     true real-
                            batch     time      time
```

### Microservice Resilience Defense in Depth
```
1. Tight read timeouts (P99 + headroom)  →  fail fast
2. Circuit breaker per dependency        →  don't keep calling broken thing
3. Bulkhead per API endpoint             →  contain blast radius
4. Default fallback responses            →  degrade gracefully
5. Exponential backoff on retries        →  avoid retry storms
6. API gateway throttling                →  cap upstream pressure
```

---

## Source

*Foundations of Scalable Systems: Designing Distributed Architectures* by Ian
Gorton (O'Reilly Media, 2022).
