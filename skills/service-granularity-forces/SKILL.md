---
name: service-granularity-forces
description: >
  Walks through deciding service granularity using the named forces
  framework from Ford/Richards/Sadalage/Dehghani Software Architecture:
  The Hard Parts Ch 7 - granularity disintegrators (service scope, code
  volatility, scalability differential, fault tolerance, security,
  extensibility) push toward smaller services, granularity integrators
  (database transactions, data dependency, workflow coupling, shared
  code) push toward larger. The architect's job is to name the forces
  in this situation, weigh them against system characteristics, and
  derive granularity instead of choosing it up front. Use when sizing a
  service, deciding whether to split or merge, debating "is this too
  big" or "is this too small", deciding whether a microservice is
  actually micro enough or too micro. Triggers - "how big should this
  service be", "service granularity", "too many microservices",
  "nano-services", "split this service", "merge these services",
  "extract this functionality", "service size", "right-sizing services",
  "should this be one service or two". Produces a granularity decision
  with forces table and ADR. Step-by-step workflow.
---

# Service Granularity Forces

You walk architects through the **"how big should this service be?"** decision using the named forces framework from *Software Architecture: The Hard Parts* (Ch 7). The book refuses to give a service-size answer. It gives the forces. Your job is to name which forces are present in this situation and weigh them.

This is a **workflow** skill. When loaded, you march the user through identifying disintegrators and integrators, weighing them, and writing an ADR.

Pattern definitions are in *Software Architecture: The Hard Parts* (Ford et al., O'Reilly 2021), "Granularity Forces" framework (Ch. 7).

---

## Related

- **Related skills**
  - `architectural-quanta-and-modularity` — load first if quantum vocabulary isn't established
  - `service-and-data-decomposition` — granularity decisions feed into decomposition Pattern 5–6
  - `trade-off-analysis-method` — for high-impact granularity decisions
  - `data-ownership-and-distributed-data` — data integrators are a strong signal here
- **Related references**
  - *The Hard Parts*, "Granularity Forces" framework
  - *The Hard Parts*, Sysops Squad worked example, Ch. 7 (Ticket Assignment Granularity)

---

## Contract for this skill

When loaded, this skill marches the user through **4 steps** per granularity decision. Apply it *per candidate service or per merge/split decision*, not once globally.

The same framework will land on different answers for different parts of the system (the Sysops Squad case study explicitly demonstrates this — Ticket Assignment splits, Customer Registration consolidates).

---

## Step 1 — Frame the granularity question

Get the concrete question:

| Question shape | Example |
|---|---|
| **Sizing a new service** | "Should TicketAssignment be its own service or part of TicketService?" |
| **Splitting an existing service** | "ExpertService is doing too much. What should split off?" |
| **Merging existing services** | "We have 4 nano-services for customer profile. Merge?" |
| **Right-sizing** | "TicketService is 200K LOC. Is this too big?" |

Force the question into one of these shapes. "It feels too big / small" is not a question; it's a hypothesis. Force the specifics.

---

## Step 2 — Enumerate the disintegrators

**Disintegrators** push toward smaller services. For each candidate service, walk the list and note which apply.

### The six disintegrators

| Disintegrator | Apply when |
|---|---|
| **Service scope and function** | The service does multiple unrelated things |
| **Code volatility** | Parts of the service change at very different rates |
| **Scalability and throughput** | Parts need very different scaling (e.g., one part is 10× more loaded than the rest) |
| **Fault tolerance** | Failures in one part shouldn't affect others |
| **Security** | Different parts have different access requirements (sensitive data should be isolated) |
| **Extensibility** | Frequent additions of new capabilities to one part |

### Output of Step 2

A list of present disintegrators with evidence:

```
TicketAssignment within TicketService:
  - Scalability differential: assignment runs 10× more often than other ticket ops
  - Code volatility: assignment algorithm changes every 2 weeks; ticket lifecycle stable
  - Security: expert location data needs tighter access controls

CustomerRegistration:
  - Security: PII handling, but no separate access requirement from rest of customer service
  - No scalability differential
  - No volatility differential
```

Disintegrators with evidence are *real*. Vague "we might want to scale this later" is not a disintegrator — name the actual measured difference.

---

## Step 3 — Enumerate the integrators

**Integrators** push toward larger services. For each candidate, walk this list.

### The four integrators

| Integrator | Apply when |
|---|---|
| **Database transactions** | Atomic multi-step updates required across the data |
| **Data dependency** | The functions can't run without each other's data |
| **Workflow coupling** | Service-to-service calls would be chatty (multiple calls per business operation) |
| **Shared code** | Significant logic duplicated; would require Replicated Code or Shared Library |

### Output of Step 3

```
TicketAssignment within TicketService:
  - Data dependency: assignment needs ticket + expert + customer data (split adds cross-service reads)
  - Workflow coupling: assignment is called as part of every ticket creation (1:1)

CustomerRegistration:
  - Database transaction: customer profile + customer preferences must be atomic
  - Data dependency: registration touches profile, preferences, billing setup
  - Workflow coupling: chatty calls across customer subsystems
```

---

## Step 4 — Weigh forces against system characteristics

The disintegrators and integrators conflict. The architectural characteristics that matter most for the system break the tie.

### Build the trade-off table

```
                      Disintegrator vs Integrator weight
                      ──────────────────────────────────────────────────
Characteristic          TicketAssignment      CustomerRegistration
                        split    keep        split    keep
─────────────────────  ──────  ─────────    ──────  ─────────
Scalability             ++       --           o       o
Maintainability         +        -            -       +
Deployability           ++       -            o       o
Security                +        -            +       o
Fault tolerance         ++       --           -       +
Operational simplicity  --       ++           --      ++
Performance             -        +            -       +
```

The matrix surfaces the answer. **For TicketAssignment, split wins** — scalability, deployability, and fault tolerance dominate. **For CustomerRegistration, keep wins** — operational simplicity, maintainability, and performance dominate.

### Granularity is derived

The book is firm on this: granularity is the *output* of the forces analysis, not the *input*. You don't pick "microservices" then decide what fits in each service; you analyze the forces and derive what size each emerges at.

### Output of Step 4

A granularity decision per candidate: split / keep / merge, with the forces table backing it.

---

## Step 5 — Write the ADR

```
ADR-NNN: Granularity for <candidate>

Context:
  Service / candidate: <name>
  Granularity question shape: <sizing / splitting / merging / right-sizing>

Disintegrators present:
  - <list with evidence>

Integrators present:
  - <list with evidence>

System characteristics (top 3-5):
  - <ranked list>

Forces table:
  <Step 4 table>

Decision:
  <Split TicketAssignment into its own service | Keep CustomerRegistration consolidated | …>

Consequences:
  Positive: <…>
  Negative: <…>
  Mitigations: <…>
```

---

## Common failure modes (call these out when you see them)

### "Microservices should be small"

That's a slogan, not a force. The book is explicit: granularity is derived from forces, not from a target size. Some services will be 1k LOC; some will be 100k LOC. The forces analysis decides.

### "Each service should be one business capability"

Reasonable starting heuristic, but not a hard rule. The Sysops Squad case study consolidates Customer Registration even though "registration" and "profile management" could be split. The forces (database transaction, data dependency, workflow coupling) win against the disintegrators (none present).

### "If a function changes often, split it out"

That's one disintegrator (code volatility). It's *necessary* (probably) but not *sufficient*. Weigh it against integrators. If splitting forces a chatty workflow that kills performance, the integrators win.

### "If we share data, we need to share a service"

That's confusing data ownership with service granularity. Two services can share *read access* to data via Inter-Service Communication or Replicated Cache (`data-ownership-and-distributed-data` skill). They don't need to be one service to access the same data. Granularity and data access are separate decisions.

### "Nano-services are good, more isolation is better"

The book pushes back hard. Operational complexity is real cost. Many small services = many deploy pipelines, monitoring dashboards, on-call rotations, contract negotiations. The operational-simplicity characteristic almost always wins for the 4th, 5th, 6th split unless the disintegrators are very strong.

### "We can split now and merge later if needed"

Easier said than done. Splitting carries decomposition cost; merging carries integration cost. **Splitting in error is more expensive than merging in error**, because splitting introduces operational coupling that survives the technical merge.

---

## When to deviate from this skill

- **Greenfield, single-team, simple system** — overkill. Granularity follows team boundaries (Conway's Law); revisit when team scales.
- **Library / SDK granularity** — different problem (semver, public API surface). Use library design principles instead.
- **Frontend bundle granularity** — different forces (initial-load size, code-splitting, route boundaries). Frontend-specific skills apply.

---

## Worked example

The Sysops Squad team faces granularity decisions throughout Ch 7. Two of them have **different answers from the same framework**:

### Ticket Assignment — split

| Force | Strength |
|---|---|
| Scalability differential (10× higher load) | Strong disintegrator |
| Code volatility (algorithm changes weekly) | Strong disintegrator |
| Security (expert location data) | Disintegrator |
| Data dependency (needs ticket + expert + customer) | Integrator |

**Decision:** Consolidated service for Ticket Assignment and Routing (separate from TicketService).
ADR ratified in Ch 7: *"Consolidated Service for Ticket Assignment and Routing"*.

### Customer Registration — keep consolidated

| Force | Strength |
|---|---|
| Database transaction (customer + preferences atomic) | Strong integrator |
| Data dependency (touches multiple customer subsystems) | Integrator |
| Workflow coupling (chatty cross-subsystem calls if split) | Integrator |
| No scalability differential | (No disintegrator) |
| No code volatility differential | (No disintegrator) |

**Decision:** keep registration consolidated within the larger Customer service. (No separate ADR in the book; the case study notes the discussion.)

**Same framework, different forces, different answers.** That's the point of the method — it produces defensible decisions, not uniform ones.

See *The Hard Parts*, Sysops Squad worked example, Ch. 7 (Ticket Assignment Granularity) and Ch. 7 (Customer Registration Granularity).
