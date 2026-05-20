---
name: code-reuse-in-distributed-systems
description: >
  Walks through choosing a code reuse pattern in a distributed system
  using the four named patterns from Ford/Richards/Sadalage/Dehghani
  Software Architecture: The Hard Parts Ch 8 - Replicated Code (copy
  into each service), Shared Library (versioned dependency), Shared
  Service (runtime call), and Sidecar/Service Mesh (operational
  cross-cutting concerns). Use when deciding how to share code between
  microservices, deciding between a shared library and a shared service,
  considering a sidecar for operational concerns, or diagnosing why a
  shared library / service has become a bottleneck. Triggers - "shared
  library vs shared service", "common code in microservices", "should
  this be a shared service", "sidecar pattern", "service mesh Istio
  Linkerd", "operational cross-cutting concerns", "duplicate code
  microservices", "version skew shared library", "Istio Envoy sidecar",
  "infrastructure code in every service", "auth in every service".
  Produces a reuse pattern choice with ADR. Step-by-step workflow.
---

# Code Reuse in Distributed Systems

You walk architects through picking a **named reuse pattern** from *Software Architecture: The Hard Parts* (Ch 8). The book's strong claim: reuse is *harder* in distributed systems than in monoliths, and the four named patterns have distinct trade-offs that most teams collapse into "shared library or shared service."

This is a **workflow** skill. When loaded, you march the user through a 4-step decision and produce an ADR.

Pattern definitions are in *Software Architecture: The Hard Parts* (Ford et al., O'Reilly 2021), "Reuse Patterns" framework.

---

## Related

- **Related skills**
  - `service-and-data-decomposition` — Pattern 2 (Gather Common Components) hands off to this skill
  - `trade-off-analysis-method` — for high-impact reuse decisions
  - `service-contracts-and-coupling` — if Shared Service is being considered, the contract becomes important
  - `distributed-system-patterns` — Sidecar / Service Mesh overview (this skill drills into when to pick)
- **Related references**
  - *The Hard Parts*, "Reuse Patterns" framework
  - *The Hard Parts*, Sysops Squad worked example, Ch. 8 (Common Infrastructure Logic)

---

## Contract for this skill

When loaded, this skill marches the user through **4 steps** per reuse decision. Apply it per piece of common code, not once globally — the right answer for one piece of common code is rarely the right answer for another.

---

## Step 1 — Characterize the code

Before picking a pattern, characterize the code that's a candidate for reuse:

| Property | Ask |
|---|---|
| **Domain or operational?** | Is this *business logic* (validation, pricing) or *infrastructure* (logging, mTLS, metrics)? |
| **Change rate** | How often does this code change? Daily? Quarterly? Yearly? |
| **Data heaviness** | Does the code own data or just compute? |
| **Consistency need** | Must every caller agree on the result at the same instant? |
| **Size** | LOC / complexity |
| **Security risk** | What's the blast radius if there's a bug? |
| **Number of consumers** | How many services use it? |

### Output of Step 1

A profile of the code:

```
Code: Sysops Squad Ticketing DB validation
Domain or operational: Domain
Change rate: Monthly
Data heaviness: No (validates inputs only)
Consistency need: All callers see same rules eventually
Size: ~400 LOC
Security risk: Medium (input validation)
Consumers: 4 services
```

---

## Step 2 — Apply the pattern decision tree

Walk the decision tree top-down:

```
Is this operational/cross-cutting (logging, mTLS, metrics, auth)?
├── YES → Sidecar / Service Mesh
└── NO  → continue
    │
    Is the code small + stable + low-security?
    ├── YES → Replicated Code (copy into each service)
    └── NO  → continue
        │
        Is it data-heavy AND must callers see consistent state?
        ├── YES → Shared Service (rare; almost always reconsider)
        └── NO  → Shared Library (default)
```

The book's strong opinions encoded in this tree:

- **Operational concerns → Sidecar.** Almost always. Don't bake auth/logging/mTLS into every service.
- **Domain reuse → Shared Library.** The default for non-trivial domain code.
- **Replicated Code is under-used.** Teams reflexively avoid duplication, but for small + stable + low-risk code, duplication is *less* coupling than a shared library.
- **Shared Service is over-used.** Most "shared services" should be libraries. The runtime coupling rarely pays for itself.

## Step 3 — Score the chosen pattern

For the chosen pattern, sanity-check against the code profile.

### Replicated Code

| Trade-off | Detail |
|---|---|
| Coupling | None at runtime; drift over time |
| Best for | Small, stable, low-security utility code |
| Worst for | Code that needs central updates (e.g., security fixes) |

### Shared Library

| Trade-off | Detail |
|---|---|
| Coupling | Low runtime; version skew at build time |
| Best for | Utility code, well-defined functions, mature interfaces |
| Worst for | Frequently-changing code (forces frequent service redeploys) |
| Gotchas | Multiple consumers on different library versions; diamond dependency problem |

### Shared Service

| Trade-off | Detail |
|---|---|
| Coupling | High runtime |
| Best for | Data-heavy operations that *must* be consistent (rare) |
| Worst for | Anything else; especially anything in the request-path critical path |
| Gotchas | Becomes a hot service; single point of failure; latency stacks |

### Sidecar / Service Mesh

| Trade-off | Detail |
|---|---|
| Coupling | High operational, zero domain |
| Best for | Logging, mTLS, metrics, service discovery, rate limiting, authentication |
| Worst for | Domain logic (please don't) |
| Gotchas | Sidecar can grow into a god-component; service mesh control plane adds significant ops complexity |

## Step 4 — Write the ADR

```
ADR-NNN: Reuse pattern for <code>

Context:
  Code: <name and brief description>
  Profile: <result of Step 1>

Decision:
  Use <Replicated Code | Shared Library | Shared Service | Sidecar>.

Rationale:
  <Step 2 decision-tree reasoning>

Trade-off table:
  | Property | Score | Notes |
  |---|---|---|
  | Runtime coupling | low/med/high | <…> |
  | Operational complexity | low/med/high | <…> |
  | Change cadence support | good/poor | <…> |
  | Consistency support | strong/eventual/none | <…> |

Consequences:
  Positive: <…>
  Negative: <…>
  Mitigations: <…>
```

---

## The four patterns in detail

### Replicated Code

Each service has its own copy of the code. No runtime dependency.

**Use when:**
- Code is small (~hundreds of LOC)
- Code is stable (changes rarely)
- No security-critical centralization need
- Number of consumers is bounded (5–10)

**Don't use when:**
- Code embodies a single source of truth that must update everywhere on a fix (e.g., security validation logic with frequent updates)
- Many consumers (drift becomes unmanageable)

**Example:** small utility functions, well-defined formatting code, simple validation rules.

### Shared Library

Versioned dependency, statically linked or imported via package manager.

**Use when:**
- Code is meaningful in size (>1k LOC) or complexity
- Interfaces are mature
- Consumers can tolerate version skew during rollouts
- Runtime independence matters

**Don't use when:**
- Code changes very frequently (forces frequent dependent service redeploys)
- Consumers can't coordinate version updates (e.g., independent teams with different release cadences)
- The library needs runtime data only available at deploy time of the consumer (rare)

**Versioning discipline:**
- Semver
- Long deprecation windows
- Maintain N–1 / N–2 majors for cross-team consumption

**Example:** Sysops Squad's ticketing DB logic library — *"ADR: Use of a Shared Library for Common Ticketing Database Logic"* (Ch 8).

### Shared Service

A separate service called at runtime for the shared functionality.

**Use when:**
- The shared logic owns *data* that must be consistent across all callers in real-time
- The shared logic is genuinely independent (deployable, scalable, observable on its own)
- The latency cost is acceptable

**Don't use when:**
- The shared functionality is in the request-path critical path of many other services
- The functionality is stateless (then it's a library candidate)
- "Just to centralize for consistency" — that's usually a library + good versioning

**Why this is the book's least-recommended pattern:**
- Adds runtime coupling
- Becomes a hot service (high QPS, high blast radius)
- Operational overhead (separate service to monitor / on-call)
- Hard to evolve (every change is a wire-compatible change for N consumers)

**Example:** A central authorization service that owns dynamic permission rules. Even here, the book recommends auth via sidecar where possible.

### Sidecar / Service Mesh

A companion process deployed alongside each service, handling cross-cutting operational concerns.

**Use when:**
- The concern is *operational*, not domain (logging, mTLS, metrics, auth, service discovery, rate limiting)
- The concern is consistent across the fleet
- Domain teams shouldn't have to maintain this infrastructure code

**Don't use when:**
- The concern is domain logic
- The team doesn't have a Kubernetes / container orchestration platform
- There are <5 services (the sidecar overhead isn't justified)

**Implementations:**
- Envoy (Istio's data plane)
- Linkerd
- AWS App Mesh
- Consul Connect

**Trade-off (from book Table 8-4):**
| Pro | Con |
|---|---|
| Allows consistent infrastructure coordination | Sidecar component may grow in scope |
| Decouples operational concerns from domain | Adds deployment complexity |
| Enables service mesh patterns | Requires orchestration platform |

**Example:** Sysops Squad uses a sidecar pattern for logging, mTLS, and metrics — *"common infrastructure logic"* (Ch 8).

---

## Common failure modes (call these out when you see them)

### "Auth should be a shared service — it's the source of truth"

For authentication (validating tokens), use a **sidecar** at the edge. For authorization (deciding what a user can do), use a **shared library** with policy rules, or a sidecar embedding an OPA-style policy engine. **Shared Service for auth** is usually a hot service that becomes a SPOF.

The Sysops Squad team debates this in Ch 8 and lands on shared library + sidecar.

### "We have 10 microservices and 10 copies of the same validation"

Three options to consider:
- Validation is small + stable → Replicated Code is fine (and might be what you already have)
- Validation evolves → Shared Library
- Validation owns dynamic rules from a central system → Shared Service (last resort)

Drift is usually the worry, but **drift across stable, small, low-risk code is rarely the problem teams fear it is**. Force the change-rate evidence.

### "Shared service so we have one source of truth"

Shared library can also be one source of truth (one repo, one published version, one published binary). The question is whether the consumer reads the truth at *build time* (library) or *request time* (service). Library suffices for most domain code.

### "Sidecar for everything"

Sidecars are for *operational* concerns. Putting domain logic in a sidecar (e.g., "the assignment logic sidecar") is the same as having a Shared Service with extra steps. Domain logic belongs in the service, not the sidecar.

### "We don't have a service mesh, can't use sidecars"

A sidecar is just a co-deployed process. Kubernetes pods, ECS task definitions, even systemd unit files can co-deploy a sidecar. You don't need Istio for sidecar patterns. Adopt the sidecar pattern incrementally; consider a service mesh when service count + complexity justify it.

### "Version skew with shared library is too painful"

Real cost, but solvable: semver discipline, long deprecation, dependency-bot for updates. If version skew is the primary reason to avoid Shared Library, you have a process problem more than an architecture problem.

---

## When to deviate from this skill

- **Single-team systems** — overkill; just pick what works
- **Code generation / interface definitions (Protobuf, OpenAPI)** — these are contracts, not code reuse. Use `service-contracts-and-coupling` skill.
- **Database access libraries** — sometimes domain, sometimes infrastructure. Apply this skill's tree; the answer is usually Shared Library, but examine the data ownership implications (load `data-ownership-and-distributed-data` skill).

---

## Worked example

The Sysops Squad team (Ch 8) makes several reuse decisions:

| Code | Pattern | ADR |
|---|---|---|
| Common ticketing DB logic | Shared Library | ADR: Use of a Shared Library for Common Ticketing Database Logic |
| Logging, mTLS, metrics | Sidecar | (sidecar pattern, no separate ADR) |
| Notification logic | Shared Library | Shared Library — small, stable, low consistency need |
| Authorization | Shared Library (rules) + Sidecar (enforcement) | Two patterns combined |

Different code, different patterns. **The framework is the constant; the answer varies.**

See *The Hard Parts*, Sysops Squad worked example, Ch. 8 (Common Infrastructure Logic) and Ch. 8 (Shared Domain Functionality).
