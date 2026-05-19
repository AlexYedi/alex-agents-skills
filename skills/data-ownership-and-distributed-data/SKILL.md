---
name: data-ownership-and-distributed-data
description: >
  Walks through assigning data ownership across services and choosing a
  data access pattern for cross-service reads. Covers the three ownership
  models (Single, Joint, Common), the four joint-ownership resolution
  patterns (Table Split, Data Domain, Delegate, Service Consolidation),
  and the four data access patterns (Inter-Service Communication, Column
  Schema Replication, Replicated Cache, Data Domain). Derived from
  Ford/Richards/Sadalage/Dehghani Software Architecture: The Hard Parts
  Ch 6, 9, 10. Use when a service needs data another service owns, when
  multiple services write the same table, when read latency from sync
  calls is too high, when designing the data layer for a newly
  decomposed system, or when an enterprise integration is fighting over
  who owns a table. Triggers - "data ownership", "who owns this table",
  "single ownership", "joint ownership", "common ownership", "shared
  database", "table split", "data domain", "delegate pattern",
  "replicated cache", "column schema replication", "Apache Ignite",
  "Hazelcast", "inter-service communication for data", "cross-service
  query", "stale read", "data freshness", "two services write same
  data", "we have a shared schema". Produces a per-table ownership map +
  per-read-path access pattern + ADRs. Step-by-step workflow.
---

# Data Ownership and Distributed Data Access

You walk architects through the **data ownership** decision (Ch 9) and the **data access pattern** decision (Ch 10) from *Software Architecture: The Hard Parts*. These are typically the two hardest decisions when decomposing a monolith — harder than service decomposition, and the place enterprise integration projects most often fail.

This is a **workflow** skill. When loaded, you march the user through two phases: ownership assignment first, then access pattern per cross-service read path.

Pattern definitions live at:
- `references/software-architecture-the-hard-parts/frameworks.md#data-ownership-patterns`
- `references/software-architecture-the-hard-parts/frameworks.md#data-access-patterns`
- `references/software-architecture-the-hard-parts/frameworks.md#data-decomposition`

---

## Related

- **Related skills**
  - `service-and-data-decomposition` — load this *first* if the data hasn't yet been split into data domains
  - `trade-off-analysis-method` — the meta-method; use for any controversial ownership decision
  - `scalable-database-design-and-sharding` — orthogonal: this skill is cross-service ownership, that skill is intra-service scaling
  - `eventual-consistency-mechanics` — load alongside if Replicated Cache or Column Schema Replication is on the table (their EC is different from storage-level EC)
  - `distributed-workflows-and-sagas` — load alongside if cross-service writes need transactional coordination
- **Related references**
  - `references/software-architecture-the-hard-parts/frameworks.md#data-ownership-patterns`
  - `references/software-architecture-the-hard-parts/frameworks.md#data-access-patterns`
  - `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md` — Ch 9 (Single Table Ownership ADR), Ch 10 (Replicated Cache for Expert Profile ADR)

---

## Contract for this skill

When loaded, this skill marches the user through **2 phases × ~5 steps each**. Total: ~30–45 min for a real decomposition. Don't try to do it for the entire data model in one sitting; do it data-domain by data-domain.

Bring in the **DBA / data platform owner** before starting. The Sysops Squad case study (Ch 6) makes this explicit: the database team being absent from early decomposition decisions is a leading cause of project failure.

---

# Phase 1 — Assign Data Ownership

For each table (or set of tables in a data domain), decide who *writes* it. Reads come later.

## Step 1.1 — Inventory the writes

Build a table:

```
Table              | Writing services
-------------------|------------------
customer           | CustomerService
ticket             | TicketService, AssignmentService
expert_profile     | ExpertService, AdminService
billing            | BillingService
survey             | SurveyService
notification_log   | NotificationService, AuditService
```

The list of writing services per table is the input to ownership decisions. **If you don't have this list, stop and build it first** — most decomposition decisions fail because nobody mapped writes before drawing boxes.

## Step 1.2 — Classify each table

Walk down the list. For each table:

| Number of writers | Ownership model | Action |
|---|---|---|
| 1 | **Single Ownership** | Done. The lone writer is the owner. Move on. |
| 2–3 | **Joint Ownership** | Continue to Step 1.3 to pick a resolution pattern |
| Many (4+) | **Common Ownership** | Stop. This is usually a decomposition flaw, not an ownership decision. Reconsider the service boundary. |

**Bias hard toward Single Ownership.** It's not always possible, but it is always preferred. If you're landing in Joint or Common too often, the service boundaries may be wrong.

### Checkpoint

If >30% of tables are Joint or Common, **stop and reconsider service decomposition**. Load `service-and-data-decomposition` and walk back. Continuing past this point with bad boundaries embeds the problem in production.

## Step 1.3 — Resolve Joint Ownership

For each table flagged Joint, pick one of the four resolution patterns:

### Pattern A — Table Split

Split the shared table into multiple tables by column. Each resulting table has a single writer.

**Use when:** Each service writes a *different subset* of columns. Common case when "joint ownership" really means "co-located writes that aren't actually overlapping."
**Cost:** Increases the data-domain count. Adds joins for readers.
**Best for:** Tables where joint writes are largely additive (different services own different fields).

### Pattern B — Data Domain

Two services share a *data domain* explicitly. Both write to the table, with clear rules on who writes which rows/columns. The shared domain becomes a small co-owned unit.

**Use when:** The writes genuinely overlap and Table Split won't work because the writers really do need the same columns/rows.
**Cost:** Couples the two services. They co-evolve.
**Best for:** Stable, well-understood joint-write patterns. **Don't use as a default** — it's the highest-coupling resolution.

### Pattern C — Delegate

One service is the writer; the others request via API. Routes back to Single Ownership.

**Use when:** One service is the *natural* owner and the others just need write access for convenience.
**Cost:** Adds runtime coupling. Latency. The delegate becomes a hot service.
**Best for:** Cases where Single Ownership is the goal and you want to enforce it through process.

### Pattern D — Service Consolidation

Merge the joint-writing services into one. Loses decomposition benefit.

**Use when:** The two services are so tightly coupled around this data that they're effectively one service trying to be two.
**Cost:** Reverses a decomposition. Last resort.
**Best for:** Cases where the joint ownership is *evidence* that the decomposition was wrong.

### Selection cheat sheet

```
Different columns / disjoint writes  → Table Split
Overlapping writes, willing to couple → Data Domain
Want to enforce single ownership      → Delegate
Decomposition was wrong               → Service Consolidation
```

## Step 1.4 — Reconsider Common Ownership

If any table landed as Common (4+ writers), **don't pick a resolution pattern yet**. The book is explicit: Common Ownership is almost always a sign that the service decomposition is wrong.

Walk back to service boundaries:
- Are these 4+ services actually one service split for the wrong reason?
- Is one of these services actually the true owner, with others using it because it was convenient?
- Should this table be at a higher level of the architecture (a shared platform service)?

If after honest reconsideration the table genuinely has many writers, treat it as a **platform / utility concern** (auth, audit log, feature flags) and document the exception explicitly.

## Step 1.5 — Write the ownership ADR

For each non-trivial ownership decision (typically one ADR per data domain):

```
ADR-NNN: <table or data domain> ownership

Context:
  <which services touched it before; why ownership matters>

Decision:
  <Service X> is the single owner of <table>.
  [If joint: <Service X> and <Service Y> jointly own via <Table Split / Data Domain / Delegate>]

Writers: <list>
Readers: <list — feeds into Phase 2>

Consequences:
  Positive: <...>
  Negative: <...>
  Mitigations: <...>
```

The Sysops Squad case study has a clean example: **ADR: Single Table Ownership for Bounded Contexts** (Ch 9). One ADR establishing the principle; per-domain ADRs for the exceptions.

### Checkpoint — end of Phase 1

You should now have:
- A per-table ownership map
- ADRs for each non-trivial ownership decision
- A list of **read paths** — for each table, the services that *don't* own it but need to read it

The read-path list is the input to Phase 2.

---

# Phase 2 — Pick Data Access Patterns

For each read path (non-owner service needs to read owner's data), pick one of the four access patterns.

## Step 2.1 — Characterize the read path

For each read path, gather:

1. **Read volume** — calls per second, per minute, per day
2. **Freshness tolerance** — how stale can the data be? Milliseconds? Seconds? Minutes? Hours? "Eventually consistent" without a number is too vague.
3. **Data size** — how much data per read? Single row? Page? Entire dataset?
4. **Read availability requirement** — what happens if the owner is down? Must reads still work?
5. **Read SLA** — p50 / p99 latency requirements

These five inputs determine the pattern. **If the user can't answer freshness tolerance, stop** and force a business answer first.

## Step 2.2 — Match to a pattern

| If you need… | Pick |
|---|---|
| Always-fresh data, low read volume, owner-up dependency acceptable | **Inter-Service Communication** |
| High read volume, stale-read tolerance (seconds), data fits in consumer DB | **Column Schema Replication** |
| Reference data read by many services, in-memory speed required | **Replicated Cache** |
| Two services that genuinely co-evolve around shared data | **Data Domain** |

### Inter-Service Communication

Reader calls owner's API synchronously every read.

| Pro | Con |
|---|---|
| Always fresh | Network RTT every read |
| Owner enforces all data rules | Owner outage breaks all readers |
| Simplest to reason about | Highest runtime coupling |

**Use when:** Low read volume + always-fresh required + owner has acceptable SLA.

### Column Schema Replication

Owner replicates relevant columns into reader's DB on change. Reader queries locally.

| Pro | Con |
|---|---|
| Reads are local — no network | Replication infrastructure required |
| Reader survives owner outage | Eventual freshness (replication lag) |
| Low runtime coupling | Data coupling — owner schema change propagates |

**Use when:** High read volume + stale-read tolerant + data size manageable.

### Replicated Cache

In-memory replicated cache (Apache Ignite, Hazelcast, Redis Cluster). Owner populates; readers read from local cache replica.

| Pro | Con |
|---|---|
| Microsecond reads | Cache memory cost |
| Survives owner outage (cache is the source) | Stale during cache invalidation lag |
| Bounded data size (cache size limit) | Operational complexity (cluster management) |

**Use when:** Reference data (small, frequently read), in-memory speed required, bounded data size.

**Sysops Squad picked this for Expert Profile data** (Ch 10) — hundreds of services read it; data is small; replicated cache via Apache Ignite.

### Data Domain (last resort)

Two services share a data domain (single schema, both read directly). The book treats this as a last resort.

| Pro | Con |
|---|---|
| Always-fresh, local reads, no replication | Couples the two services strongly |
| Simplest implementation | Joint ownership rules required |
| | Decomposition partially reverses |

**Use when:** Two services genuinely co-evolve. Anywhere else, **don't**.

## Step 2.3 — Score the pick against the read path

For the chosen pattern, sanity-check:

```
                       Inter-Service   Column Replication   Replicated Cache   Data Domain
Read volume capacity    low             high                 very high          high
Freshness                 immediate       seconds              cache lag          immediate
Owner-down survival     no              yes                  yes                yes
Operational complexity  low             medium               high               low
Coupling                high            medium               medium             very high
```

If the pick scores poorly on a dimension that matters, reconsider.

## Step 2.4 — Write the access pattern ADR

```
ADR-NNN: <read path> access pattern

Context:
  Reader: <service>
  Owner: <service> (per ADR-NNN ownership decision)
  Read volume: <number>
  Freshness tolerance: <number with unit>
  Data size: <description>

Decision:
  Use <Inter-Service Communication | Column Schema Replication | Replicated Cache | Data Domain>
  for the <reader> → <owner> read path.

Trade-off table: [from Step 2.3]

Consequences:
  Positive: <…>
  Negative: <…>
  Mitigations: <…>
```

The Sysops Squad case study has a clean example: **ADR: Use of In-Memory Replicated Caching for Expert Profile Data** (Ch 10).

---

## Common failure modes (call these out when you see them)

### "Our services share a database — that's fine, it's just one DB"

That's **one architectural quantum**, not multiple services. The book is explicit: shared-DB microservices are a distributed monolith. Either commit to single quantum (which is fine!) or actually decompose the data.

### "We'll figure out data ownership later, after we split services"

Almost guaranteed failure mode. Service boundaries that don't respect data ownership produce constant cross-service write contention. The Sysops Squad team learns this in Ch 6 when Dana the DBA joins the conversation late. Get the data ownership decisions in Phase 1 *before* extracting services.

### "We picked Inter-Service Communication everywhere because it's simplest"

Simplest at decision time. Highest coupling at runtime. Owner outages cascade. Latency stacks. If >70% of read paths are Inter-Service Communication, you're building a distributed monolith. Review the high-volume paths and consider Replication or Cache.

### "Joint Ownership is fine, we'll just be careful"

Joint Ownership without a *named resolution pattern* (Table Split / Data Domain / Delegate / Consolidation) is the most common decomposition failure. Either pick a pattern explicitly or back out to Single Ownership.

### "We have a 'shared data' microservice that holds the common tables"

That's a **Shared Service for data** — usually an anti-pattern in this taxonomy. Either it's a platform service (auth, audit) and document it as an exception, or it's a sign that the services consuming it should be reconsidered.

### "Replicated Cache solves everything"

Replicated Cache has operational complexity that many teams underestimate. Cache cluster management, memory budgeting, invalidation correctness, multi-region replication — all real costs. Don't reach for Replicated Cache before measuring whether Column Schema Replication or Inter-Service Communication is adequate.

### "We don't have a DBA team"

If the system is enterprise-scale and you're decomposing data, find one. The Sysops Squad case study's strongest lesson (Ch 6) is that data decomposition without the database team is malpractice. If you don't have one, surface that gap to leadership before continuing.

---

## When to deviate from this skill

- **Analytical data** — this skill is *operational* data. Analytical data (reporting, ML, BI) follows the Data Mesh / DPQ pattern (Ch 14). Don't apply this skill there.
- **Event sourcing** — the ownership model is different. Each event is owned by its producer; reads via projections. Use this skill's vocabulary but the patterns differ.
- **Single-team monolith** — overkill. Single Ownership of everything; no Phase 2.

---

## Worked example

The Sysops Squad team's data ownership journey:

- **Ch 6** — 6 data domains identified: Customer, Ticket, Expert, Billing, Reporting, Survey
- **Ch 9** — Single Ownership rule established; Survey Service owns survey table; joint ownership of expert_profile resolved via **Table Split** (skill data owned by Expert Service, billing data owned by Billing Service)
- **Ch 10** — Expert Profile read path: **Replicated Cache** (Apache Ignite) because hundreds of services read it, data is small, microsecond reads required
- **Ch 13** — Contract design for the cross-service reads (load `service-contracts-and-coupling` skill for that phase)

See `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md#ch-9-sysops-squad-saga-data-ownership` and `#ch-10-sysops-squad-saga-expert-profile-data-access`.
