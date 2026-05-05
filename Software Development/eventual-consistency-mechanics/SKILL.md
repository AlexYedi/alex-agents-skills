---
name: eventual-consistency-mechanics
description: >
  Apply eventually consistent storage correctly - reason about the
  inconsistency window, implement read your own writes (RYOWs), tune
  consistency via N/W/R quorums, use sloppy quorums + hinted handoff,
  reconcile via anti-entropy / Merkle trees, and resolve conflicts with
  last-writer-wins (and its data-loss caveat), version vectors / siblings,
  or CRDTs. Use when designing on Cassandra / DynamoDB / Riak / Voldemort
  / Cosmos DB, diagnosing stale reads or lost updates, or choosing a
  conflict-resolution strategy. Triggers - "stale reads", "tunable
  consistency", "N W R quorum", "RYOWs", "version vector", "CRDT", "last
  writer wins", "sloppy quorum", "hinted handoff", "Merkle tree
  anti-entropy", "siblings". Produces a consistency design with explicit
  N/W/R, conflict-resolution strategy, and operational guarantees.
---

# Eventual Consistency Mechanics

You design and operate eventually consistent data stores. The promise is
high availability and low latency: any replica accepts writes, reads can
hit any replica, the network can partition without losing service. The
catch: clients can read stale data, concurrent writes can clash, and the
mechanics of "eventually" are surprisingly subtle.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 11): the
inconsistency window, RYOWs, tunable consistency (N/W/R), quorums and sloppy
quorums, anti-entropy, and the three conflict-resolution strategies (LWW,
version vectors, CRDTs).

For strong consistency mechanisms (2PC, Paxos, Raft, linearizability), see
`consensus-and-strong-consistency`.

---

## When to Use This Skill

- Designing on Cassandra, DynamoDB, Riak, Voldemort, Cosmos DB, MongoDB
  (with eventual settings)
- Diagnosing stale reads or lost updates in a replicated store
- Choosing N/W/R quorum settings
- Implementing read-your-own-writes for user-facing flows
- Choosing a conflict-resolution strategy (LWW vs version vectors vs CRDTs)
- Reasoning about replica behavior under partition

---

## The Inconsistency Window

```
 Time:   0    +5ms                                +50ms              +200ms
 ───────────────────────────────────────────────────────────────────────────►

  Client                  
    │                     
    └── write K=v2 ──► Replica 1                                              
                         │ (acks success at +5ms)                             
                         │
                         │                                                    
                         │              ┌── async replication ──┐             
                         │              │                       │             
                         ├──────────────►  Replica 2  ───────────► converged 
                         │   +50ms                                            
                         │
                         │              ┌── async replication ──┐             
                         │              │ (slow node / network) │             
                         └──────────────►  Replica 3  ───────────► converged 
                                                                  +200ms

       ◄──── INCONSISTENCY WINDOW ────► (clients reading from R3 see old v1)
```

The **inconsistency window** is the period between a write succeeding at one
replica and converging across all replicas.

**Drivers of window length:**

| Factor | Effect |
|---|---|
| **Number of replicas (N)** | More replicas = more updates to coordinate |
| **Operational load** | Heavy read/write workload at a node delays propagation |
| **Network distance** | Cross-continent replicas: bound by speed of light + congestion |
| **Replica-to-replica health** | Slow / failing replicas extend the window |

> "You don't have control over the duration of the inconsistency window. You
> can't provide or know an upper bound."

**Implication:** Design assuming clients will sometimes see stale data.
Either prevent it (RYOWs, quorums) or tolerate it (UI shows "syncing", users
warned, async UX).

---

## Read Your Own Writes (RYOWs)

A guarantee that **a client sees its own updates on subsequent reads**, even
though other clients may not yet.

**Why it matters:** the canonical user-experience problem. User updates their
profile, refreshes the page, sees the old version, panics.

```
Client A                 Replicas               Client B (or A's later read)
──────────                ────────               ─────────────────────────────

write K=v2 ──────────► R1, R2 (acked)
                       R3 (delayed)

A reads K?  ──────► must hit R1 or R2 (sees v2)   B reads K?  ──────► may hit R3
                                                                       (sees v1)

         ────  RYOWs guarantee  ────                ──── Eventual only ────
```

**Implementation patterns:**

| Pattern | How |
|---|---|
| **Leader-based + read-from-leader for the originating client** | After write to leader, that client's reads also go to leader |
| **MongoDB causal consistency / sessions** | Session token causes reads to wait for the session's last write |
| **Neo4j bookmarks** | Write returns a bookmark; subsequent read passes bookmark, ensuring replica has caught up |
| **Cassandra `LOCAL_QUORUM` for both writes and reads** | If R+W > N, you read the latest |

**MongoDB defaults to RYOWs** by reading from the primary (configurable via
`readPreference`). **Cassandra does not by default** — you must use quorum
reads.

**Scope:** RYOWs is per-client / per-session. Other clients' reads are still
eventual.

---

## Tunable Consistency: N / W / R

```
N = number of replicas
W = number of replicas a write must contact before acking
R = number of replicas a read must contact before returning

If R + W > N    →  read sees the latest write (on a healthy cluster)
If R + W ≤ N    →  reads may be stale
```

### The Trade-Off

| Setting | Behavior | Use case |
|---|---|---|
| `W=1, R=1, N=3` | Fastest reads and writes; reads may be stale | Caches, telemetry, low-stakes |
| `W=N, R=1` | Strong on read; slow writes | Read-heavy workloads, write durability matters less |
| `W=1, R=N` | Slow reads but always see latest; fast writes | Rare; usually unbalanced |
| `W=quorum, R=quorum` (e.g., 2/2 of 3) | Balanced strong-ish; tolerates one node failure | **Default for many production workloads** |
| `W=N, R=N` | Strong but sensitive to any failure | Don't — use quorum |

### Quorum Math

**Quorum** = majority = `(N/2) + 1`.

| N | Quorum |
|---|---|
| 3 | 2 |
| 5 | 3 |
| 7 | 4 |

**Why quorum reads + quorum writes work:**

```
N = 3, W = 2, R = 2

Write reaches at least 2 of 3 replicas (call them set W).
Read contacts at least 2 of 3 replicas (call them set R).

|W| + |R| = 4 > 3 = N
→ W ∩ R ≠ ∅  (intersection guaranteed)
→ The read contacts at least one replica that has the latest write.
→ Coordinator picks the latest version (by version vector / timestamp).
```

This is the durability/freshness guarantee that quorum buys you.

---

## Sloppy Quorum + Hinted Handoff

What if some of the W replicas are unreachable?

**Strict quorum:** write fails. High consistency, lower availability.

**Sloppy quorum:** write to W of *any* available nodes, even nodes that don't
own this key. Use **hinted handoff** to replay to the rightful owners later.

```
N=3, W=2

Owners of key K: nodes A, B, C
Network partition:  A reachable;  B unreachable;  C reachable;
                    plus stand-in node D reachable

Strict quorum:  reach A, C (W=2) → success
Sloppy quorum:  if only A reachable, also write to D (stand-in)
                D holds a "hint" that this write belongs to B
                When B comes back, D forwards the hint → B catches up
```

**Pros:** Higher write availability under partition.

**Cons:** Reads may still see stale data even with `R+W > N`, because the
sloppy write didn't go to the owners. Hinted handoff repairs eventually.

**Examples:** Dynamo, DynamoDB, Riak, Voldemort, Cassandra all support
this. It's the Dynamo lineage's "always writable" promise.

---

## Anti-Entropy via Merkle Trees

Periodic background reconciliation between replicas.

```
Replica 1 builds a Merkle tree of its data:

                    [root hash]
                      ╱      ╲
                  [hash]    [hash]
                  ╱  ╲       ╱   ╲
              [h1] [h2]    [h3] [h4]
              keys keys    keys keys
              1-N  N+1-2N  ...

Replica 2 builds the same tree.

To reconcile:
  Compare root hashes.
  If equal:    done (no divergence).
  If unequal:  recurse into divergent branches.

Only divergent leaves transfer the actual data.
```

**Why it matters:** With many replicas and lots of data, naive replica
comparison would transfer everything. Merkle trees let you compare TBs of
data with a few KB of hash exchange and only transfer the diff.

**Cassandra's "repair" runs anti-entropy.** Schedule it. Skipping
repair leads to divergence accumulating until reads return inconsistent
results.

---

## Conflict Resolution

When concurrent writes happen at different replicas, you have to decide
which wins (or merge them).

### Last-Writer-Wins (LWW)

Each write carries a timestamp. On conflict, higher timestamp wins.

```
Replica 1: K = v2  (timestamp 100)
Replica 2: K = v3  (timestamp 99)   ← lower

Reconcile: K = v2 (LWW)
```

**Pros:** Simple. Cheap.

**Cons:** **Silently loses data** when concurrent writes happen.

> "Data loss with a last writer wins conflict resolution policy is
> inevitable."

**Use only when:**
- Objects are immutable (write-once with unique keys)
- Or you genuinely don't care about losing concurrent updates
- Or one client owns the key (no concurrent writes possible)

**Clock skew makes LWW worse.** Cross-node timestamps are unreliable. See
`distributed-systems-essentials`.

### Version Vectors

Per-replica logical clock attached to each object. Detects concurrent writes
and can return them as **siblings** for application-level merging.

```
Object K, version vector: { R1: 3, R2: 2, R3: 1 }

R1 writes:                R2 writes (concurrent):
  v_new = old + R1++         v_other = old + R2++
  vector: {R1:4, R2:2,       vector: {R1:3, R2:3,
           R3:1}                       R3:1}

When reconciling:
  Vector A: {R1:4, R2:2, R3:1}
  Vector B: {R1:3, R2:3, R3:1}
  Neither dominates — these are CONCURRENT.
  Both versions returned to client as SIBLINGS.
  Application decides how to merge.
```

**Pros:** No silent data loss. Application can implement domain-aware merge
(e.g., union of items in a shopping cart).

**Cons:** Application complexity. Reads return multiple versions sometimes.
Vector size grows with replica count.

**Used by:** Riak (siblings are explicit), Dynamo, Voldemort.

### CRDTs (Conflict-Free Replicated Data Types)

Data types whose semantics let the database resolve conflicts deterministically
without app involvement.

| CRDT type | Semantics |
|---|---|
| **G-Counter** | Grow-only counter; merge = max per replica, then sum |
| **PN-Counter** | Counter supporting decrement (two G-Counters) |
| **OR-Set** | Observed-Remove Set; concurrent add wins over remove |
| **LWW-Element-Set** | Set with LWW for member adds/removes |
| **2P-Set** | Add + tombstone (no re-add) |
| **MV-Register** | Multi-value register (returns siblings) |
| **List CRDT** | Ordered list with concurrent inserts (RGA, Treedoc) |
| **Hash table CRDT** | Map of CRDTs |

**Pros:** App doesn't see conflicts. Deterministic merge.

**Cons:** Limited set of types. Some operations don't fit CRDT semantics
(uniqueness constraints, transactions).

**Used by:** Redis (counters), Riak (CRDTs), Cosmos DB (limited), Akka
Distributed Data, Y.js / Automerge for collaborative editing.

**Prefer CRDTs when available.** They make conflict resolution invisible to
the application.

### Choosing a Strategy

| Situation | Strategy |
|---|---|
| Immutable objects, unique keys | LWW (or just append) |
| Counters, sets, maps | CRDT |
| Domain-specific merge logic (carts, profiles) | Version vectors + siblings |
| Distributed text editing | List CRDTs (Y.js, Automerge) |
| Single-writer keys | Anything works |

---

## Principles

- **The inconsistency window has no upper bound** under operational stress.
  Design for clients to sometimes see stale data.
- **Use RYOWs for any flow where a user updates and immediately re-reads.**
  Profiles, carts, settings.
- **Choose N/W/R based on workload.** `R+W > N` for effective strong
  consistency on a healthy cluster; `W=R=1` for fastest at the cost of
  inconsistency.
- **Sloppy quorum trades read consistency for write availability** under
  partition.
- **Anti-entropy / repair is required.** Schedule it. Without it, divergence
  grows.
- **LWW silently loses data on concurrent writes.** Use only when objects
  are immutable or single-writer.
- **Prefer CRDTs when available.** Invisible conflict resolution.
- **Version vectors with siblings** require application-level merge logic
  but preserve all writes.
- **Don't trust cross-node timestamps.** Use logical clocks (version vectors,
  Lamport).

---

## Anti-Patterns

### LWW for Concurrent-Write Workloads

**Looks like:** Shopping cart with LWW. Two devices add items concurrently.
Last-write timestamp wins; the other device's items are silently dropped.

**Why it fails:** LWW can't merge — it picks one and discards the other.

**The fix:** Version vectors with sibling resolution, or an OR-Set CRDT.

### Reading from One Replica Always

**Looks like:** `R=1` on a replicated store. App randomly picks a replica.
User sometimes sees stale data.

**Why it fails:** Without quorum or RYOWs, freshness isn't guaranteed.

**The fix:** Quorum reads (R = quorum) or RYOWs (read from leader / latest
session).

### Strong Consistency on an AP System

**Looks like:** "We need strong consistency, let's use Cassandra with
`consistency=ALL`." First node failure → all writes fail.

**Why it fails:** AP systems sacrifice consistency for availability under
partition. Forcing strong consistency removes the availability you went to
Cassandra for.

**The fix:** Use a CP system if you need strong consistency. Or accept
quorum-level guarantees.

### Skipping Anti-Entropy / Repair

**Looks like:** Cassandra cluster running for a year, no repairs. Reads return
inconsistent results across replicas.

**Why it fails:** Drift accumulates without active reconciliation.

**The fix:** Schedule weekly repair (`nodetool repair`).

### Time-Stamping Across Time Zones

**Looks like:** "We'll order writes by `Date.now()` from each client." Clients
in different time zones, with skewed clocks, write concurrently. LWW picks
arbitrary winners.

**Why it fails:** Wall-clock time is meaningless for ordering across nodes.

**The fix:** Logical clocks. Or server-side timestamps from a single
authoritative source.

### Forgetting the Window Grows Under Load

**Looks like:** Tested at low load with 50 ms inconsistency window. In
production at peak load, window grows to 30 seconds. User-facing flows break.

**Why it fails:** Tested under unrealistic conditions.

**The fix:** Load-test with realistic write rates. Architect for unbounded
window (RYOWs, async UX, "syncing" indicators).

---

## Decision Rules

| Situation | Action |
|---|---|
| User updates and immediately reads (profile, cart) | RYOWs (read from leader / session-aware) |
| Low-stakes telemetry, fastest possible | `W=1, R=1` (no quorum) |
| Production read+write workload | Quorum reads + quorum writes |
| Need write availability during partition | Sloppy quorum + hinted handoff (Cassandra, Dynamo) |
| Counter / set / map workload | CRDT |
| Domain-specific merge logic | Version vectors + siblings |
| Immutable objects (write-once) | LWW is fine |
| Mutable shared objects | NOT LWW. Use VV or CRDT |
| Multi-region writes | Multi-leader with explicit conflict resolution |
| Schedule anti-entropy | Weekly minimum on Cassandra-style systems |

---

## Worked Example: Multi-Device Shopping Cart

**Context:** User has two devices (laptop, phone). Both can add items to a
cart simultaneously. Cart is stored in DynamoDB Global Tables (multi-region,
multi-leader).

**Naive design (LWW):**
- Laptop adds 3 items at 12:00:00.000
- Phone adds 2 items at 12:00:00.001
- LWW: phone's write wins. Laptop's 3 items silently lost.

**Better design (CRDT-style — using DynamoDB sets):**

```python
# Cart is a Set of (item_id, qty) tuples.
# Add operations append to the set.
# Remove operations append a tombstone.
# On read, reconstruct: items_added - items_removed.

dynamodb.update_item(
    Key={"user_id": user_id, "cart_id": cart_id},
    UpdateExpression="ADD items :new_item",
    ExpressionAttributeValues={":new_item": {item_id, qty}},
)
```

DynamoDB's `ADD` to a set is conflict-free — concurrent adds union the sets.
Remove via tombstone.

**Or with version vectors (Riak-style):**

Each cart object has a vector clock. On read, if siblings returned, app
merges:

```python
def merge_carts(siblings):
    items = {}
    for sibling in siblings:
        for item in sibling["items"]:
            # Take max quantity if same item appears in multiple siblings
            items[item.id] = max(items.get(item.id, 0), item.qty)
    return list(items.values())
```

**RYOWs:** when the user's device reads the cart, route to the same region
that holds the device's recent writes. Or use DynamoDB's strongly consistent
read for that region.

**Result:** No silent loss of cart additions across devices. Eventual
convergence via CRDT semantics or app-level merge.

---

## Gotchas

- **`R+W > N` only works on a healthy cluster.** Sloppy quorum can produce
  stale reads even with the math right.
- **Vector clock size grows with replica count.** For very large clusters,
  this is non-trivial.
- **Sibling resolution is application code.** Forgetting to handle siblings
  silently picks one (often the most recent), losing data.
- **Cassandra repair runs but isn't free.** It's I/O-heavy. Stagger across
  nodes.
- **DynamoDB Global Tables resolve via LWW silently.** This is fine for
  immutable objects, dangerous for mutable ones — design accordingly.
- **MongoDB is technically CP** (with `writeConcern=majority`) but you can
  weaken it via `readPreference=secondary`. Choose deliberately.
- **Cosmos DB has 5 explicit consistency levels** (strong, bounded staleness,
  session, consistent prefix, eventual). Pick the weakest that satisfies the
  use case.
- **Causal consistency** is stronger than eventual but weaker than strong.
  MongoDB and some others offer it explicitly.
- **Strong-consistent reads cost extra** — Spanner: extra round-trip;
  DynamoDB: 2× RCUs.

---

## Related Skills

- `consensus-and-strong-consistency` — strong consistency mechanisms
- `scalable-database-design-and-sharding` — choosing the database
- `distributed-systems-essentials` — clocks, idempotency
- `distributed-system-patterns` — Saga handles cross-service eventual
  consistency

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 11. The
Dynamo paper (SOSP 2007) is the foundational reference for this style of
system. Marc Shapiro's CRDT papers and Y.js / Automerge are good entry
points to the CRDT literature.
