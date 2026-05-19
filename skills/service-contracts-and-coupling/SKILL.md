---
name: service-contracts-and-coupling
description: >
  Walks through designing service contracts between distributed components.
  Covers the strict-vs-loose contract spectrum, stamp coupling (passing
  more data than needed), semantic coupling (coupling on field meaning),
  consumer-driven contracts (Pact, Spring Cloud Contract), and contract
  versioning strategies. Derived from Ford/Richards/Sadalage/Dehghani
  Software Architecture: The Hard Parts Ch 13. Use when designing or
  reviewing the contract between two services, picking between Protobuf
  /Avro/GraphQL/OpenAPI/JSON, deciding how to evolve an API without
  breaking consumers, choosing whether to enforce contracts in CI, or
  diagnosing why a contract feels too brittle or too loose. Triggers -
  "strict contract", "loose contract", "tight contract", "Protobuf",
  "Avro", "GraphQL schema", "OpenAPI", "gRPC", "consumer-driven
  contract", "Pact", "Spring Cloud Contract", "stamp coupling",
  "semantic coupling", "contract versioning", "API versioning", "v1 v2
  endpoint", "contract testing", "mobile contract", "internal vs
  external API", "field meaning change", "rename a field". Produces a
  contract design ADR with chosen position on the strict-loose spectrum
  and explicit stamp/semantic coupling analysis. Step-by-step workflow.
---

# Service Contracts and Coupling

You walk architects through the **contract design** decision (Ch 13) from *Software Architecture: The Hard Parts*. Contracts are the deepest coupling decision between services — strict contracts catch errors early but bind tightly; loose contracts survive change but defer error detection. The book's framing: contracts are a *cross-cutting* concern that affects every other dimension (communication, consistency, coordination).

This is a **workflow** skill. When loaded, you march the user through a 5-step decision per contract boundary and produce an ADR.

Pattern definitions live at `references/software-architecture-the-hard-parts/frameworks.md#contracts` and `#coupling-vocabulary`.

---

## Related

- **Related skills**
  - `trade-off-analysis-method` — for high-impact contract decisions
  - `distributed-workflows-and-sagas` — contracts between saga participants are a separate decision per participant
  - `data-ownership-and-distributed-data` — the data-access pattern (Inter-Service Communication) needs a contract designed via this skill
  - `api-design-and-evolution` — overlapping; that skill covers Bernardez/Olejár's full API methodology, this skill is just the Hard Parts contract decision
  - `architectural-quanta-and-modularity` — contracts at quantum boundaries deserve more rigor than intra-quantum contracts
- **Related references**
  - `references/software-architecture-the-hard-parts/frameworks.md#contracts`
  - `references/software-architecture-the-hard-parts/frameworks.md#coupling-vocabulary` (stamp + semantic coupling definitions)
  - `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md#ch-13-sysops-squad-saga-expert-mobile-app-contract`

---

## Contract for this skill

When loaded, this skill marches the user through **5 steps** per contract boundary. Total: ~15–25 min per contract. For a microservices system with N services, expect to run the skill ~N–2N times (often once per consumer-producer pair).

A common shortcut: pick **one contract style per *boundary class*** (internal-service ↔ internal-service, internal ↔ mobile, internal ↔ external partner) rather than per individual contract. The book endorses this — granularity at the boundary class is usually right.

---

## Step 1 — Identify the contract boundary

Get clear on what the contract spans. Ask:

1. **Who is the producer?** Which service publishes the contract?
2. **Who is the consumer?** One service, many services, an external client (mobile, third party)?
3. **What's the communication style?** Sync request/response? Async event? Streaming?
4. **What's the deployment cadence asymmetry?** Can producer and consumer ship simultaneously, or does one lag (mobile app store, partner integration)?
5. **What's the trust boundary?** Same team? Different teams in the same company? External org?

### Boundary classes (the book's implicit taxonomy)

| Class | Examples | Default lean |
|---|---|---|
| Intra-team | Two services owned by same team | Strict (low coordination cost) |
| Cross-team internal | Two services, different teams, same company | Strict + Consumer-Driven Contracts |
| Internal ↔ Mobile | Backend service ↔ mobile app | **Loose** (app deployment lag) |
| Internal ↔ Partner | Backend service ↔ external API consumer | Strict + versioned (clear SLA) |
| Internal ↔ Public | Backend service ↔ unknown consumers | Loose + versioned (max compatibility) |

Pick the boundary class. It frames the default. You can deviate, but you should be defending the deviation.

### Output of Step 1

```
Producer: <service>
Consumer: <service or class>
Communication: <sync/async/streaming>
Cadence asymmetry: <description>
Trust boundary: <description>
Boundary class: <one of the above>
Default lean: <strict/loose>
```

---

## Step 2 — Score the strict-vs-loose trade-off

The strict-loose decision is the central one. Score on these dimensions:

### Strict contracts (Protobuf, Avro, GraphQL schemas, OpenAPI with validation)

| Property | Strict score |
|---|---|
| Error detection | Compile-time / call-time |
| Change tolerance | Low — breaking changes break consumers immediately |
| Versioning need | High — schema versioning required |
| Tooling | Mature (code gen, validators, type-safe SDKs) |
| Operational cost | Moderate (schema registry, versioning discipline) |
| Best for | Internal cross-team APIs, partner integrations |

### Loose contracts (raw JSON, name-value pairs, no schema validation)

| Property | Loose score |
|---|---|
| Error detection | Runtime |
| Change tolerance | High — consumers ignore unknown fields |
| Versioning need | Low — field-additive often sufficient |
| Tooling | Manual; type-safety must be enforced in code |
| Operational cost | Low (no schema infra) |
| Best for | Mobile clients, public APIs, evolving contracts |

### Decision table

Score the contract boundary on these questions:

| Question | Strict if… | Loose if… |
|---|---|---|
| How often will the contract change? | Rarely | Often |
| Can consumer redeploy on demand? | Yes | No (mobile / partner / public) |
| What's the cost of a runtime contract failure? | Low | High |
| Is type-safety end-to-end valuable? | Yes | Not critical |
| Will multiple consumer teams need code gen? | Yes | No |

Count strict-leaning answers vs loose-leaning answers. The majority wins, with strong weight on "Can consumer redeploy on demand?" — if the answer is *no*, lean loose regardless.

### Output of Step 2

A position on the strict-loose spectrum, justified by the question scoring.

---

## Step 3 — Audit for stamp coupling

**Stamp coupling** = passing more data than the consumer needs. The most common contract anti-pattern. Found in:

- API responses that return full entities when the consumer needed two fields
- Event payloads that include upstream context the consumer doesn't process
- Workflow state passed through every step
- Generic "everything object" payloads

### Detection

Walk through the draft contract field-by-field. For each field, ask:

1. **Which consumer needs this field?**
2. **What does the consumer *do* with it?**
3. **Would the consumer fail without it?**

Fields that fail the "would the consumer fail without it?" question are stamp coupling candidates.

### Trade-off

| Stamp coupling tolerance | When acceptable |
|---|---|
| Tight (only needed fields) | Cross-team contracts; mobile contracts; public APIs |
| Loose (full entities) | Intra-team contracts where consumer needs are stable; cases where the alternative is N specialized endpoints |

The book is firm: **make stamp coupling explicit**. If you're passing more than needed, name the reason. ("We pass full entity because all 6 consumers need different subsets and maintaining 6 endpoints is worse.")

### Output of Step 3

A field-by-field justification. Annotated contract showing which fields are essential vs. convenience.

---

## Step 4 — Audit for semantic coupling

**Semantic coupling** = coupling on the *meaning* of fields, not their names. The hardest coupling to detect.

Examples:

- A field named `status` whose meaning changes from "ticket workflow state" to "user-visible status string" → consumers reading the value start displaying engineering codes to customers
- A field `amount` whose unit changes from cents to dollars without renaming → all downstream calculations wrong
- A field `expert_id` that starts referring to a different ID space → joins break silently

### Detection

For each field in the contract, document:

1. **Meaning** — what does this field semantically represent?
2. **Unit / range / format** — explicit specification
3. **Allowed values** — enumerated if finite
4. **Stability promise** — under what conditions can the meaning change?

Fields without these documented are semantic-coupling time bombs.

### Mitigation

- **Document semantics in the contract itself** — OpenAPI descriptions, Protobuf comments, Avro doc fields. Don't put them only in wiki pages.
- **Use semantic types** — `AmountUSD` vs `AmountCents`, `ExpertId` vs `UserId`. Cheap in strict-contract languages, free in TypeScript.
- **Consumer-Driven Contracts** (Step 5) — consumers express their semantic expectations as testable artifacts.

### Output of Step 4

A semantic dictionary for the contract. Every field has: meaning, format, allowed values, stability promise.

---

## Step 5 — Decide on Consumer-Driven Contracts (CDC)

For contracts crossing team boundaries, consider **Consumer-Driven Contracts** — consumers specify what they need; the producer tests against those specs in CI.

### Tools

- **Pact** — language-agnostic, broad ecosystem
- **Spring Cloud Contract** — JVM-centric
- **Schemathesis / Postman Contract Testing** — OpenAPI-driven

### When to adopt CDC

| Adopt CDC if… | Skip CDC if… |
|---|---|
| Cross-team boundary | Same team owns both sides |
| Producer changes often | Contract is stable |
| Producer can't easily test consumers | Producer can spin up consumers in CI |
| Multiple consumers with different needs | Single consumer, simple contract |

The book endorses CDC for cross-team work because it forces semantic agreement to the surface — consumer expectations become testable artifacts the producer must satisfy.

### Output of Step 5

A decision: CDC adopted or not, with tool choice if adopted.

---

## Step 6 — Write the ADR

```
ADR-NNN: <contract boundary name> contract design

Context:
  Producer: <service>
  Consumer: <service or class>
  Communication: <sync/async/streaming>
  Boundary class: <intra-team / cross-team / mobile / partner / public>
  Cadence asymmetry: <description>

Decision:
  Contract style: <strict | loose | hybrid>
  Schema technology: <Protobuf | Avro | GraphQL | OpenAPI | JSON without schema>
  Versioning strategy: <semver in URL / header / no versioning>
  Consumer-Driven Contracts: <adopted via Pact / not adopted because…>

Coupling analysis:
  - Strict-vs-loose score: <table from Step 2>
  - Stamp coupling: <fields justified per Step 3>
  - Semantic coupling: <semantic dictionary per Step 4>

Trade-off table:
  | Dimension | Score | Notes |
  |---|---|---|
  | Error detection latency | compile / runtime | … |
  | Change tolerance | low / med / high | … |
  | Operational cost | low / med / high | … |
  | Type-safety end-to-end | yes / partial / no | … |

Consequences:
  Positive: <…>
  Negative: <…>
  Mitigations: <…>
```

---

## Common failure modes (call these out when you see them)

### "We picked gRPC because it's fast"

That's an implementation, not a contract decision. The book's Sysops Squad example (Ch 13, Addison to Sydney): *"That's an implementation, not architecture. We need to decide what types of contracts we want before we choose how to implement them."* Pick strict-vs-loose first; gRPC/Protobuf/Avro/etc. are downstream implementation choices.

### "Strict everywhere because type-safety"

Type-safety is valuable, but at boundaries you can't control deployment for (mobile, partner, public), strict contracts create release-coordination headaches. The Sysops Squad team picks **loose** for the mobile contract specifically because the mobile app's deployment lags the backend (app store delays). Match contract style to the boundary, not to engineering preference.

### "We'll just version the API"

Versioning is a *mitigation* for strict contracts, not a substitute for picking strict vs loose. Versioning has its own costs: maintenance of multiple versions, deprecation campaigns, dual-write logic. Treat it as a cost of strict, not a free lunch.

### "We pass the whole user object because we might need fields later"

That's stamp coupling rationalized as future-proofing. The downstream cost: every consumer is now indirectly coupled to every field of the user object, even ones they don't read. Field additions become risky because adding a field can change consumer behavior they didn't intend.

### "The contract is in JSON, so it's loose"

Format ≠ strictness. JSON with strict schema validation (OpenAPI + validator middleware) is a strict contract. JSON without validation is a loose contract. Don't conflate wire format with contract strictness.

### "We don't need contract tests — we'll catch issues in integration tests"

Integration tests run too late and too rarely to catch contract drift. Consumer-Driven Contracts run in CI on every change and catch issues before deploy. For cross-team boundaries, CDC pays back its setup cost within weeks.

### "We renamed a field but kept it backward compatible"

Backward-compatible naming isn't the same as backward-compatible *meaning*. If you rename `status` to `workflow_state`, consumers reading the new field still have to understand whether the *meaning* changed. Surface the semantic question explicitly.

---

## When to deviate from this skill

- **Event-streaming systems (Kafka, Kinesis, Pulsar)** — same trade-offs apply but the contract is on the event payload + topic schema. The strict-vs-loose decision is the same; the implementation differs. Use Avro + Schema Registry as a defensible default.
- **GraphQL-everywhere** — GraphQL is strict by design but has loose-leaning characteristics (consumers select fields). The strict-vs-loose decision collapses; the stamp coupling decision becomes "what fields can be queried?" instead of "what fields are returned?"
- **Async/RPC hybrids (gRPC streaming, WebSockets)** — both contract on payload + connection semantics. Layer this skill on the payload contract; treat the connection semantics as separate.

---

## Worked example

The Sysops Squad team's contract decisions:

- **Internal service ↔ internal service** (e.g., Ticket Orchestrator ↔ Assignment Service): strict (Protobuf or OpenAPI with validation)
- **Internal ↔ Mobile expert app**: **loose** (JSON, no schema validation, name-value pairs)
  - ADR: Loose Contract for Sysops Squad Expert Mobile Application (Ch 13)
  - Reason: mobile deployment cadence is much slower than backend; loose contract protects the mobile app from server-side evolution
- **Internal ↔ Customer-facing web**: strict (OpenAPI with validation) — web client redeploys with backend; full type-safety end-to-end

See `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md#ch-13-sysops-squad-saga-expert-mobile-app-contract` for the full walkthrough.

Different boundaries → different contract styles. Same framework. **The framework produces defensible decisions, not uniform decisions.**
