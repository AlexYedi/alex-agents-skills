---
name: consensus-and-strong-consistency
description: >
  Apply strong consistency mechanisms in distributed systems - ACID
  transactions, two-phase commit (2PC) for cross-partition transactions
  and its blocking pathology, consensus algorithms (Paxos, Multi-Paxos,
  Raft) with terms / AppendEntries / heartbeats / quorum-based commit,
  linearizability vs serializability, TrueTime + commit-wait (Spanner),
  single-threaded per-partition execution (VoltDB), and deterministic
  transaction execution (Calvin / FaunaDB). Use when designing on Spanner /
  CockroachDB / VoltDB / etcd, picking a consensus algorithm, or
  diagnosing transactional behavior in a distributed DB. Triggers - "2PC",
  "Paxos vs Raft", "linearizability vs serializability", "TrueTime",
  "Spanner", "CockroachDB", "VoltDB", "etcd Raft", "ACID across partitions",
  "compensating action", "XA transaction". Produces a strong-consistency
  design with explicit algorithm choice and trade-offs.
---

# Consensus and Strong Consistency

You design and operate distributed systems that require strong consistency
across partitions or replicas — ACID transactions, replicated state machines,
linearizable reads. Strong consistency at scale is genuinely expensive: 2PC
blocks on coordinator failure, consensus algorithms add latency, linearizability
across regions requires bounded clocks. This skill is the toolkit.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 12): ACID,
2PC, Paxos / Multi-Paxos / Raft, linearizability vs serializability,
Spanner's TrueTime + commit-wait, VoltDB's single-threaded-per-partition
approach, and Calvin-style deterministic transactions.

For eventually consistent mechanisms (RYOWs, quorums, version vectors,
CRDTs), see `eventual-consistency-mechanics`.

---

## When to Use This Skill

- Designing on Spanner, CockroachDB, YugabyteDB, VoltDB, etcd
- Picking a consensus algorithm for replicated state
- Implementing distributed transactions across partitions or services
- Diagnosing long latency on distributed-transaction workloads
- Choosing between strong consistency and eventual for a workload
- Deciding when 2PC's blocking pathology is acceptable

---

## ACID, Recapped for Distributed Systems

| Letter | Single-server meaning | Distributed meaning |
|---|---|---|
| **A**tomicity | All operations in a transaction commit or none do | Hard — requires 2PC across partitions |
| **C**onsistency | Database invariants preserved | App-level; mostly the same |
| **I**solation | Concurrent transactions don't interfere | Even harder distributed; requires distributed locks or MVCC + timestamps |
| **D**urability | Committed data survives crash | Replicated to multiple nodes / disks |

**Two senses of "consistency":**

1. **Transactional consistency** — business rules (the C in ACID).
2. **Replica consistency** — all replicas see the same state.

Strong consistency in distributed systems usually means *both*: ACID
transactions + linearizable replica behavior.

---

## Two-Phase Commit (2PC)

The classic algorithm for atomicity across partitions or services. Designed
by Jim Gray in 1978; still in use everywhere.

```
Phase 1: PREPARE                       Phase 2: COMMIT
                                                          
Coordinator                            Coordinator                            
    │                                      │                                  
    ├── prepare? ────► P1                  ├── commit ─────► P1               
    │                                      │                                  
    ├── prepare? ────► P2                  ├── commit ─────► P2               
    │                                      │                                  
    ├── prepare? ────► P3                  ├── commit ─────► P3               
    │                                      │                                  
    │ ◄──── yes ─── P1                     │ ◄──── ack ─── P1                 
    │ ◄──── yes ─── P2                     │ ◄──── ack ─── P2                 
    │ ◄──── yes ─── P3                     │ ◄──── ack ─── P3                 
    │                                      │
    │   (or "no" → abort)                  │   ── DONE ──                     
```

**Roles:**

- **Coordinator:** orchestrates the transaction.
- **Participants:** the partitions/services holding pieces of the transaction.
- **Transaction context:** identifier passed to all participants.

**Phases:**

1. **Prepare:** coordinator asks each participant if it can commit. Each
   votes yes or no. Yes = "I have written this and I'm ready; I won't fail
   unilaterally." No = "Abort."
2. **Resolve:** if all said yes, coordinator sends commit. Otherwise abort.
   Participants then make the change durable (or roll back) and ack.

**The fundamental pathology:** **coordinator failure between prepare and
commit**.

```
    ┌───────────────────┐
    │   Coordinator     │
    │   (failed)        │
    └─────────┬─────────┘
              │
   ┌──────────┼──────────┐
   ▼          ▼          ▼
 ┌────┐    ┌────┐     ┌────┐
 │ P1 │    │ P2 │     │ P3 │   ← all said "yes" in prepare
 │    │    │    │     │    │   ← waiting for commit/abort
 │ ?  │    │ ?  │     │ ?  │   ← cannot commit alone
 │    │    │    │     │    │   ← cannot abort alone (others may have committed)
 └────┘    └────┘     └────┘   ← BLOCKED until coordinator recovers
```

**Participants cannot autonomously decide.** They must wait for the
coordinator to recover. Locks held during this time. Other transactions
can pile up.

**Mitigations:**
- Highly available coordinator (replicated)
- Tight coordinator-failure detection
- Recovery from coordinator log on restart
- Write-ahead log on participants
- Three-phase commit (3PC) — adds an extra phase to bound participant
  blocking, but makes other failure modes worse; rarely used in practice

**XA / JTA / JTS:** the standardized 2PC across heterogeneous databases.
Java EE's JTS implements XA. SQL Server, Oracle, IBM DB2 all support XA.

**Compensating actions:** an alternative to 2PC. Each step has a forward
operation and a compensating operation that semantically reverses it. Used
in Sagas (see `distributed-system-patterns`). No coordinator blocking; eventual
atomicity instead of immediate.

---

## Consensus Algorithms

Where 2PC handles cross-partition transactions, **consensus algorithms** let
multiple replicas agree on a sequence of state-machine commands. They power
replicated state machines, leader elections, distributed locks, and
configuration stores.

### The Family Tree

```
Lamport's Paxos (1998)              "Correct, hard to understand"
    │
    ▼
Multi-Paxos                         "Optimization for repeated rounds"
    │
    ▼
Raft (2013, Ongaro & Ousterhout)    "An understandable consensus algorithm"
                                    Now the dominant production choice
```

### Raft: The Practical Choice

```
Replicas play one of three roles:

  ┌──────────┐            ┌──────────┐            ┌──────────┐
  │  Leader  │  ◄───────► │ Follower │  ◄───────► │ Follower │
  │          │            │          │            │          │
  │ Receives │            │ Replicates           │ Replicates
  │ writes   │            │ leader's log         │ leader's log
  │          │            │                       │
  └──────────┘            └──────────┘            └──────────┘

Concepts:

  Term            Monotonically increasing logical clock per leadership period.
                  Leaders are elected per term.

  AppendEntries   The leader's RPC for replicating log entries to followers.
                  Heartbeat is AppendEntries with no entries.

  Heartbeat       Leader sends to followers every 300-500ms typical.
                  Missing heartbeat → follower may start an election.

  Quorum-based commit
                  Leader marks an entry committed once a MAJORITY of followers
                  have replicated it.

  Election        On leader failure, a follower becomes candidate, requests
                  votes, becomes leader if it gets a majority.
```

**Why Raft beat Paxos in practice:**
- Reference implementation (etcd's raft library) is mature and reusable.
- Leader-based simplifies log replication.
- The Raft paper is readable in one sitting; Paxos requires multiple.
- Configuration changes (adding/removing nodes) have a clean specification.

**Raft adopters (Ch 12 + 13):**
- **etcd** (Kubernetes' config store)
- **Consul**, **Nomad** (HashiCorp)
- **Hazelcast**
- **YugabyteDB**, **CockroachDB** (per-tablet Raft)
- **MongoDB** (replica set elections)
- **Neo4j** (clusters)
- **RabbitMQ** (quorum queues)

### Multi-Paxos / Paxos Adopters

- **Spanner** (per-Paxos-group within a split)
- **Chubby** (Google's lock service, Paxos-based)
- **ZooKeeper** uses Zab, a Paxos-flavored protocol
- Kafka used ZooKeeper historically (moving to KRaft, a Raft variant)

**Default in 2026:** Raft for new systems. Use Multi-Paxos when an existing
codebase or organizational expertise demands it.

---

## Linearizability vs Serializability

The two strongest consistency models, from different communities:

| | Linearizability | Serializability |
|---|---|---|
| Community | Distributed systems | Databases |
| Definition | Every operation appears to take effect at a single point in real time, between its invocation and response | Concurrent transactions appear to execute in *some* sequential order |
| Real-time ordering | Yes — if T1 finished before T2 started, T1 must precede T2 | No — order can be any serial order |
| Strength | Stronger (real-time + total order) | Weaker (just total order) |
| Achievability | Hard at scale (needs synchronized clocks) | Easier (snapshot isolation, MVCC, distributed locks) |

**Strict serializability** = linearizability + serializability. Spanner's
flagship guarantee.

**Practical guidance:**
- **Default to serializability** for transactional workloads.
- **Linearizability** when external clients need real-time guarantees
  (financial transactions, leader-election outputs, distributed locks).

---

## Spanner: TrueTime and Commit Wait

Spanner offers **external consistency** — a fancy name for strict
serializability across the globe.

**The challenge:** without a synchronized clock, you can't agree on real-
time order across regions.

**TrueTime:** Google's clock service backed by GPS receivers + atomic clocks
in every datacenter, with **bounded uncertainty** (typically ε ≈ 7 ms).

```
TrueTime API:
  TT.now() → [earliest, latest]    ← interval, not point

Example: TT.now() = [12:00:00.043, 12:00:00.057]
  → "real time is somewhere in this 14ms window"
```

**Commit wait:** when a transaction commits, Spanner picks a commit
timestamp and **waits ε milliseconds** before reporting success. This
guarantees no other node will see a TrueTime that contradicts the order.

```
Transaction commits at TrueTime = [t-ε, t+ε]
Pick commit_ts = t+ε
Wait until TT.now().earliest > t+ε
Report success

Now any other node querying TrueTime will report > t+ε,
so they'll order this transaction strictly before their reads.
```

**Cost:** ~7 ms added to every commit. Worth it for global linearizability
in financial / inventory / regulated workloads.

**Implication:** **CockroachDB and YugabyteDB don't have TrueTime hardware.**
They approximate with HLC (Hybrid Logical Clocks) and NTP, accepting weaker
guarantees (snapshot isolation, not external consistency by default). This
is one reason Spanner is special.

---

## VoltDB: Single-Threaded Per Partition

A different approach. Within a partition, run **one transaction at a time
on one thread**. No locks, no isolation puzzles — just sequential execution
in memory.

```
Partition #1                    Partition #2                    Partition #3
───────────                     ───────────                     ───────────
  Single thread                   Single thread                   Single thread

  txn 1 → done                    txn 4 → done                    txn 7 → done
  txn 2 → done                    txn 5 → done                    txn 8 → done
  txn 3 → done                    txn 6 → done                    txn 9 → done
  ...                             ...                             ...

Cross-partition transactions: 2PC across partitions.
```

| Property | Value |
|---|---|
| Single-partition transaction | Cheap (no locking, in-memory) |
| Multi-partition transaction | Expensive (2PC) |
| Storage | In-memory primarily; command log + snapshots for durability |
| Linearizability | Since v6.4 (Jepsen surfaced earlier issues) |

**Design implication:** model your data so transactions are partition-local.
Multi-partition is an escape hatch, not the default.

---

## Calvin / FaunaDB: Deterministic Transactions

Another approach: **pre-order all transactions globally**, then execute on
each replica. Because all replicas see the same input order, they produce
the same output. No coordination per transaction — coordination is in the
ordering layer.

```
Client 1 ──┐                         All replicas process the same
           │                          ordered stream:
Client 2 ──┼──► Sequencer ──► Stream  ─────►  Replica 1 → state
           │   (consensus on            ────►  Replica 2 → state
Client 3 ──┘    transaction order)      ────►  Replica 3 → state

Each replica's output is deterministic given the input order.
```

**Pros:** No 2PC. Replicas independently produce identical state.

**Cons:** The sequencer is a bottleneck. Less common in production than
Spanner / Raft-based systems.

**Used in:** Calvin (research), FaunaDB (commercial).

---

## Strongly Consistent Reads

Even on systems that default to eventual reads, you can usually request
strong reads explicitly:

| System | API |
|---|---|
| DynamoDB | `ConsistentRead=true` (extra RCU cost) |
| Cassandra | `consistency_level=QUORUM` or `ALL` |
| MongoDB | `readPreference=primary` |
| Cloud Spanner | Default; or `read --strong` |
| Bigtable | Default within a row |

**Cost:** an extra round-trip to the leader. Use only where stale reads
cause real problems.

---

## Principles

- **Prefer transactional consistency where possible.** Spanner team:
  > "It is better to have application programmers deal with performance
  > problems due to overuse of transactions than coding around the lack of
  > transactions."
- **Single-partition transactions are cheap; multi-partition trigger 2PC and
  are slow.** Design data models to keep transactions partition-local.
- **Use Raft (or Multi-Paxos) for replica state.** Raft's reference
  implementation makes it the practical choice.
- **2PC blocks on coordinator failure.** Make the coordinator highly
  available; have a recovery path.
- **Strong consistency at scale costs latency.** Don't pay it where eventual
  is fine.
- **Linearizability requires synchronized clocks** for global guarantees.
  TrueTime is the production example; HLC is the open-source approximation.
- **Verify consistency claims against Jepsen reports.** Marketing
  consistency != actual consistency under partition.
- **Compensating actions (Saga) are the alternative to 2PC** for
  microservices — eventual atomicity, no coordinator blocking. See
  `distributed-system-patterns`.

---

## Anti-Patterns

### 2PC Across Microservices Without a Hardened Coordinator

**Looks like:** Distributed transaction across 5 microservices using XA.
Coordinator is the API gateway; if it crashes mid-commit, all 5 services
hang waiting.

**Why it fails:** Coordinator failure blocks participants indefinitely.

**The fix:** Saga pattern with compensating actions. Or use a workflow
engine (Temporal, AWS Step Functions) as the durable, replicated coordinator.

### Multi-Partition Transactions as the Norm

**Looks like:** Schema designed without partition awareness. Every
transaction crosses 2-3 partitions.

**Why it fails:** Each transaction triggers 2PC. Throughput collapses.

**The fix:** Model partition-local transactions. Co-locate joinable data
via shared partition key.

### Rolling Your Own Consensus

**Looks like:** "We'll just use a leader and have followers ack writes." 
Slowly turns into a half-built Raft.

**Why it fails:** The edge cases (split-brain, partial ack, leader during
partition, log divergence) are exactly the hard ones.

**The fix:** Use etcd, Consul, or embed a Raft library (etcd-io/raft,
hashicorp/raft).

### Trusting NTP Clocks for Linearizability

**Looks like:** "We have NTP, so timestamps are accurate enough." Two
events with timestamps 50ms apart actually happened in the opposite order.

**Why it fails:** NTP skew can be 100ms+. No bound on skew.

**The fix:** TrueTime (if you're Google) or HLC. Or accept snapshot isolation,
not linearizability.

### Strongly Consistent Reads Everywhere

**Looks like:** Every DynamoDB read sets `ConsistentRead=true`. RCU usage
doubles. Bill spikes.

**Why it fails:** Most reads are fine eventual.

**The fix:** Strong consistency only where stale reads break the user
experience.

### Ignoring Jepsen

**Looks like:** Vendor claims "linearizable consistency under all conditions"
without a Jepsen report.

**Why it fails:** Jepsen has found bugs in nearly every distributed
database. Untested claims are marketing.

**The fix:** Look for Jepsen reports at jepsen.io. Read them carefully —
even systems Jepsen approves of usually have caveats.

---

## Decision Rules

| Situation | Action |
|---|---|
| Replicated config / metadata store | etcd (Raft) |
| Distributed lock | etcd, Consul, or ZooKeeper |
| Replica state machine | Raft library (hashicorp/raft, etcd raft) |
| Cross-partition transactions in OLTP | Spanner / CockroachDB / VoltDB |
| Global linearizability | Spanner (only) |
| ACID open-source distributed | CockroachDB or YugabyteDB |
| Cross-microservice transaction | Saga with compensating actions, not 2PC |
| Transaction within a single shard | Native DB transaction |
| Need linearizable reads | Read from leader via consensus protocol |
| Need to verify consistency claim | Read the Jepsen report |
| Choosing Paxos vs Raft | Raft, unless you have specific Paxos expertise |

---

## Worked Example: Replicated Configuration Store

**Context:** Microservices fleet needs a shared configuration store with
strong consistency. Updates rare (humans push config); reads frequent
(every service starts with `read config`); must survive single-node failure.

**Choice:** etcd (Raft-backed key-value store).

**Topology:** 5-node etcd cluster across 3 AZs. Quorum = 3.

**Operations:**

| Op | Mechanism |
|---|---|
| Read | Default: linearizable read via leader |
| Read (relaxed) | Serializable read from any node (slightly stale, fast) |
| Write | Raft consensus across quorum |
| Watch | Long-poll on key changes |

**Failure modes:**

| Failure | Behavior |
|---|---|
| Single node down | Quorum (3 of 4 remaining) maintained; service continues |
| 2 nodes down | Quorum (3 of 3) maintained; tight |
| 3 nodes down | No quorum; reads/writes fail until recovery |
| Network partition | Minority side can't accept writes |

**Why etcd over a custom solution:**
- Battle-tested (powers Kubernetes).
- Raft library reused.
- Watch / lease / compare-and-swap built in.
- Jepsen-tested; known guarantees.

**What we deliberately didn't do:**
- Write our own Raft.
- Use ZooKeeper (heavier, JVM, older operational model).
- Use a relational DB (no native watch; consensus would be bolted on).

---

## Gotchas

- **Spanner is not magic.** TrueTime is hardware-dependent. Don't assume
  CockroachDB / YugabyteDB give you the same guarantees.
- **2PC participant blocking is rare in practice but devastating when it
  happens.** Plan for coordinator recovery; monitor coordinator availability
  separately.
- **Raft membership changes have edge cases.** Use joint consensus or
  single-server changes; never multi-server changes at once.
- **etcd is not a database.** It's a small-key-value store for metadata,
  not for application data. Volumes: KBs to MBs total, not GBs.
- **Cassandra's `LWT` (lightweight transactions) use Paxos** for compare-
  and-swap. Slow — don't overuse.
- **MongoDB transactions across shards trigger 2PC.** Single-shard
  transactions are cheap; cross-shard are expensive.
- **Snapshot isolation ≠ serializability.** Snapshot isolation has
  write-skew anomalies. PostgreSQL serializable mode (SSI) closes them.
- **Jepsen has surfaced consistency bugs in nearly every system.** Read
  reports for the version you're running.
- **HLC (Hybrid Logical Clocks)** combine wall and logical clocks; used by
  CockroachDB and others to bound the clock-uncertainty window without
  TrueTime hardware.
- **Workflow engines (Temporal, AWS Step Functions, Cadence)** are
  effectively durable, replicated coordinators for long-running multi-service
  transactions. They sidestep 2PC by making the coordinator itself fault-
  tolerant.

---

## Related Skills

- `eventual-consistency-mechanics` — the cheaper alternative
- `distributed-system-patterns` — Saga (compensating actions instead of 2PC)
- `scalable-database-design-and-sharding` — choosing the database
- `distributed-systems-essentials` — clocks, idempotency, partial failure
- `microservices-resilience-patterns` — patterns at the service layer

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 12. Read
the Raft paper (Ongaro & Ousterhout, 2014), the Spanner paper (Corbett et
al., 2012), and the Jepsen reports for the system you're using.
