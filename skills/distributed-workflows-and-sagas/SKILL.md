---
name: distributed-workflows-and-sagas
description: >
  Walks through choosing a transactional saga pattern for a distributed
  workflow. Covers the full 8-saga taxonomy from Ford/Richards/Sadalage/Dehghani
  (Epic Saga, Phone Tag Saga, Fairy Tale Saga, Time Travel Saga, Fantasy Fiction
  Saga, Horror Story, Parallel Saga, Anthology Saga) plus orchestration vs
  choreography, atomic vs eventual consistency, sync vs async communication,
  stamp coupling for workflow state, and semantic coupling. Use when designing
  a distributed transaction, picking a saga pattern, deciding between
  orchestration and choreography, or analyzing why your "saga" feels too
  coupled. Triggers - "saga pattern", "distributed transaction", "Epic Saga",
  "Anthology Saga", "Parallel Saga", "choreography vs orchestration",
  "orchestrator service", "compensating transaction", "saga rollback",
  "atomic across services", "eventual consistency across services",
  "should we use a saga?", "which saga", "the saga is too coupled",
  "stamp coupling workflow", "semantic coupling". Produces a saga decision
  with ADR and named pattern from the 8-saga taxonomy. Step-by-step workflow.
---

# Distributed Workflows and Transactional Sagas

You guide architects through picking a **named saga pattern** from the 8-pattern taxonomy in *Software Architecture: The Hard Parts* (Ford, Richards, Sadalage, Dehghani — 2021, Ch 11–12). This is a **workflow** skill, not a knowledge dump — when loaded, you march the user through a 5-step decision and produce an ADR at the end.

The taxonomy and matrix are the "8 Transactional Sagas" and "Saga Selection Matrix" frameworks in *The Hard Parts*, Ch. 11–12. Don't restate them here — reference them by name when needed.

---

## Related

- **Related skills**
  - `trade-off-analysis-method` — load this if the saga choice has high downstream impact and needs explicit characteristic scoring
  - `data-ownership-and-distributed-data` — load alongside if the workflow involves cross-service data writes
  - `service-contracts-and-coupling` — load alongside for the contract design between participants
  - `eventual-consistency-mechanics` — orthogonal: business-level EC (here) ≠ storage-level EC (that skill)
  - `microservices-resilience-patterns` — orthogonal: failure handling at the call level, not the workflow level
- **Related references**
  - *The Hard Parts*, "The 8 Transactional Sagas" — the catalog
  - *The Hard Parts*, "Saga Selection Matrix" — the matrix this skill walks
  - *The Hard Parts*, "Workflow Coordination" — orchestration vs choreography deep dive
  - *The Hard Parts*, Sysops Squad worked example — the worked example landed on **Parallel Saga (aeo)**

---

## Contract for this skill

When loaded, this skill marches the user through **5 steps**. Don't skip — each step's output feeds the next. Produce an ADR at the end. The whole flow should take 10–20 minutes of conversation.

If the user pushes back on doing the steps, that's a signal to switch into reference mode and just point them at `frameworks.md#the-8-transactional-sagas` to read.

---

## Step 1 — Frame the workflow

Get the concrete shape of the distributed transaction. Ask:

1. **What's the business workflow?** One sentence. ("When a customer files a ticket, the system assigns an expert, notifies the customer, schedules the visit, and triggers post-visit survey.")
2. **Who are the participants?** Name each service involved. Count them.
3. **What's the triggering event?** Sync request (user clicks button)? Async event (scheduled job fires)?
4. **What's the success outcome?** What does "the workflow completed" mean at the data layer?
5. **What's the failure outcome?** What must roll back, what can stay, what can be reconciled later?

**Output of Step 1:** participants list, trigger style, success criterion, failure criterion.

### Checkpoint

If the user can't answer #4 or #5, **stop**. You can't pick a saga without knowing what success and failure look like at the data layer. Push back: "Before we choose a saga, we need to agree on what the workflow must guarantee."

---

## Step 2 — Pin the three axes

The 8-saga matrix has three axes. Pin each from the business requirements, not from preference.

### Axis 1 — Communication: synchronous or asynchronous?

| Pick **sync** if… | Pick **async** if… |
|---|---|
| Caller needs an immediate response | Caller can be notified later |
| Workflow takes <1 second end-to-end | Workflow takes seconds to minutes |
| Failure response must reach the user inline | Failure response can be a status update |

**Push the user toward async.** Most teams reflex toward sync. Most workflows don't need it. Make them defend sync if they pick it.

### Axis 2 — Consistency: atomic or eventual?

| Pick **atomic** if… | Pick **eventual** if… |
|---|---|
| Partial completion is unacceptable | Partial completion is OK with reconciliation |
| Money / regulated data is involved | Notifications / surveys / non-critical writes |
| Business explicitly demands all-or-nothing | Business can tolerate "settled in seconds" |

**Push the user toward eventual.** Atomic across services is the source of most distributed-systems pain. Make them defend atomic with a specific business requirement.

### Axis 3 — Coordination: orchestrated or choreographed?

| Pick **orchestrated** if… | Pick **choreographed** if… |
|---|---|
| ≥4 participants | ≤3 participants |
| Complex compensation logic | Simple flow |
| Workflow visibility matters for debugging | Loose coupling matters more than visibility |
| The flow has branches or loops | The flow is linear |

**Default to orchestrated above 4 participants.** Choreography is elegant on slides and miserable to debug at 6 participants.

### Checkpoint

State the three picks back to the user. Confirm. Each pick should have a one-sentence reason tied to a business requirement, not a technical preference.

**Output of Step 2:** (sync|async, atomic|eventual, orchestrated|choreographed) — a 3-bit address.

---

## Step 3 — Land in the 8-saga matrix

Use the 3-bit address as an index. The 8 cells:

| Address | Pattern | Coupling |
|---|---|---|
| (s, a, o) | **Epic Saga** | very high |
| (s, a, c) | **Phone Tag Saga** | high |
| (s, e, o) | **Fairy Tale Saga** | high |
| (s, e, c) | **Time Travel Saga** | medium |
| (a, a, o) | **Fantasy Fiction Saga** | high |
| (a, a, c) | **Horror Story** | medium |
| (a, e, o) | **Parallel Saga** | low |
| (a, e, c) | **Anthology Saga** | very low |

State the named pattern to the user. The detail of each pattern is in the "8 Transactional Sagas" framework in *The Hard Parts*, Ch. 12.

### One-line shape of each (for fast recognition)

- **Epic Saga (sao)** — orchestrator runs synchronous atomic flow. The "Saga pattern" most other books describe. Highest coupling. Only when domain demands it.
- **Phone Tag Saga (sac)** — services call each other sync in a chain, atomic via compensation. Very brittle.
- **Fairy Tale Saga (seo)** — sync orchestrated, eventual consistency. Useful when calls must be sync but atomic isn't required.
- **Time Travel Saga (sec)** — sync chain, eventual consistency, no orchestrator. Hardest to reason about.
- **Fantasy Fiction Saga (aao)** — async messages, atomic outcome, orchestrator. Rare; needs distributed transaction across async messaging.
- **Horror Story (aac)** — async, atomic, choreographed. Name says it.
- **Parallel Saga (aeo)** — async, eventual, orchestrator. Modern default for complex workflows.
- **Anthology Saga (aec)** — async, eventual, choreographed. Lowest coupling. Modern default for simple workflows.

---

## Step 4 — Evaluate the chosen pattern

State the pattern back. Then test it against four questions:

1. **Operational complexity** — can the team run this in production? Orchestrators need to be HA. Async needs a broker. Choreography needs observability for distributed flows. Score: low / med / high effort to operate.
2. **Failure modes** — what compensation logic is needed? Write out the failure paths. If you can't enumerate them in 5 minutes, the pattern is likely too coupled or too unstructured.
3. **Coupling strength** — does this saga create a quantum boundary you don't want? Sync atomic = one quantum across all participants. Async eventual = independent quanta.
4. **Performance** — does sync introduce latency you can't afford? Does async introduce reconciliation delay the business can't tolerate?

### Checkpoint — the "walk back" check

If any of the four scores is bad, **walk back to Step 2** and ask whether the axis answer is actually forced by the domain or whether the team is over-constraining.

Most teams over-constrain in this order:
1. Pick **atomic** when **eventual** would work (default to eventual; force atomic to defend itself)
2. Pick **sync** when **async** would work (default to async; force sync to defend itself)
3. Pick **choreographed** when **orchestrated** would be simpler (the "we don't want a central service" reflex)

If the walk-back surfaces a softer answer, re-run Step 3 with the new address. The new landing is almost always a lower-coupling cell.

---

## Step 5 — Write the ADR

The output of this skill is **always an ADR**, regardless of how confident the team feels.

```
ADR-NNN: <pattern name> for <workflow name>

Context:
  Workflow: <one-sentence business workflow>
  Participants: <list of services>
  Trigger: <sync/async>
  Success criterion: <what success means at the data layer>
  Failure criterion: <what failure means at the data layer>

Decision:
  We will use <pattern name> (<3-letter code>) for this workflow.

Axis answers:
  Communication: <sync|async> — because <reason>
  Consistency:   <atomic|eventual> — because <reason>
  Coordination:  <orchestrated|choreographed> — because <reason>

Trade-off table:
  | Property | Score | Notes |
  |---|---|---|
  | Operational complexity | low/med/high | <…> |
  | Failure-handling effort | low/med/high | <…> |
  | Coupling strength | very high/high/medium/low/very low | <…> |
  | Performance | adequate/concerning | <…> |

Consequences:
  Positive:
    - <…>
  Negative:
    - <…>
  Mitigations:
    - <…>
```

The ADR is the artifact. Without it, the next architect can't tell intentional from incidental. The book is explicit on this.

---

## Common failure modes (call these out when you see them)

### "We need a saga because we have microservices"

That's not a reason. A saga is a *workflow coordination* pattern. If there's no workflow crossing services, there's no saga. Ask: what's the workflow?

### "We picked Epic Saga because the docs called it the Saga pattern"

This is the most common mistake. Epic Saga (sao) is the **highest-coupling** pattern in the taxonomy. Most teams should default to Parallel Saga (aeo) or Anthology Saga (aec). Walk them back through Step 2 with the bias toward async/eventual.

### "We're using choreography but we have 7 services"

Choreography above 4 participants is a debugging nightmare. The team will either drift into ad-hoc orchestration (worse than picking it explicitly) or rebuild it as orchestration later. Recommend orchestration now.

### "We want atomic but eventual would be fine"

The business almost never *needs* atomic outside money / regulated domains. Force a specific business requirement to justify atomic. If they can't produce one, default to eventual.

### "We're passing the entire workflow state through each service"

That's **stamp coupling** (Ch 11, Ch 13). Trade-off: low semantic coupling, high data-volume coupling, hidden field dependencies. Acceptable when explicit; problematic when accidental. Flag it.

### "We can't tell where the workflow is in choreography"

That's the choreography tax. Either add explicit workflow-state observation (queryable per-service status, distributed tracing) or switch to orchestration. Don't pretend it's free.

---

## When to deviate from this skill

- **Long-running workflows (hours to days):** sagas as described here assume seconds-to-minutes. For hours-to-days, layer in durable workflow engines (Temporal, Cadence, AWS Step Functions). The saga *pattern* still applies; the runtime is different.
- **Workflows that are actually just request/response:** if there's no compensation logic, it's not a saga, it's an API call. Don't over-engineer.
- **Workflows that span organizations:** contracts dominate; load `service-contracts-and-coupling` before this skill.

---

## Worked example reference

The Sysops Squad team (in the book's case study) landed on **Parallel Saga (aeo)** for ticket management. Six participants, sync was wrong (mobile app could be offline), atomic was wrong (notification timing not critical), choreographed was wrong (too many participants). See *The Hard Parts*, Sysops Squad worked example, Ch. 12 (Transactional Sagas — The Big Pick) for the full walkthrough.

If your workflow shape resembles theirs (multi-step, multi-service, customer-facing, with notifications and audits), the same axis answers usually apply. Re-derive, don't copy.
