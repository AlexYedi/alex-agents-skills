---
name: architecture-characteristics-and-tradeoffs
description: >
  Identify, prioritize, and trade off architectural characteristics ("ilities").
  Use when architecting a new system and selecting which characteristics matter,
  translating business goals into measurable architectural requirements, doing
  trade-off analysis between competing concerns, or applying the Connascence
  framework to analyze coupling. Triggers: "architectural characteristics for
  X", "what are the ilities for our system?", "tradeoff analysis for X",
  "translate business goals to architecture", "Connascence between modules",
  "Architecture Decision Record". Produces structured architectural assessment.
---

# Architecture Characteristics and Trade-offs

You guide the meta-decisions of system architecture: choosing which
characteristics matter, how to measure them, and how to trade them off when
they conflict. The book Software Architecture: The Hard Parts and Fundamentals
of Software Architecture call these "architectural characteristics" or "ilities."

---

## When to Use This Skill

- Architecting a new system and selecting which characteristics matter most
- Translating business goals into measurable architectural requirements
- Doing trade-off analysis when characteristics conflict
- Applying Connascence to analyze module coupling
- Writing or reviewing an Architecture Decision Record (ADR)

---

## The Three Laws of Software Architecture

| Law | Statement | Implication |
|---|---|---|
| **First** | Everything is a trade-off | No architecture is "right"; all are trade-off resolutions |
| **Second** | Why is more important than how | Document rationale; the implementation can change, the reasoning shouldn't |
| **Third** | Most decisions exist on a spectrum, not binary | Avoid forced binary thinking |

---

## Architectural Characteristics: The "Ilities"

### Definition Criteria

A valid architectural characteristic must:
1. Specify a **non-domain** design consideration (not "user authentication" — that's a feature)
2. Influence some **structural** aspect of the design
3. Be **critical or important** to the application's success

### Categories (ISO Quality Model)

| Category | Characteristics |
|---|---|
| **Performance efficiency** | Latency, throughput, capacity |
| **Compatibility** | Interoperability, coexistence |
| **Usability** | Learnability, operability, accessibility |
| **Reliability** | Availability, fault tolerance, recoverability |
| **Security** | Confidentiality, integrity, authentication |
| **Maintainability** | Modularity, reusability, testability, modifiability |
| **Portability** | Adaptability, installability |
| **Functional suitability** | Completeness, correctness, appropriateness |

### Implicit vs Explicit

- **Explicit:** Stated in requirements (e.g., "system must handle 10K req/sec")
- **Implicit:** Necessary but not stated (security, availability, basic usability)

**Architect's job:** Surface the implicit characteristics. They're often the ones that bite if missed.

---

## Translating Business Goals to Architectural Characteristics

| Business goal | Architectural characteristic |
|---|---|
| Mergers and acquisitions | **Interoperability** |
| Time to market | **Agility** (deployability + modularity + testability) |
| User satisfaction | **Performance** + **availability** + **usability** |
| Competitive advantage | **Time to market** + **scalability** |
| Time and budget | **Simplicity** + **feasibility** |

### Composite Characteristics

Some characteristics decompose into measurable parts. **"Agility"** isn't directly measurable, but its components are:

```
Agility = Deployability + Modularity + Testability
```

Always decompose composite characteristics to their measurable parts before treating them as requirements.

---

## The Least Worst Architecture Principle

**You can't maximize every characteristic.** They conflict.

| Conflict | Trade-off |
|---|---|
| Performance vs Security | Encryption costs latency |
| Availability vs Consistency | CAP theorem in distributed systems |
| Simplicity vs Flexibility | More plug points = more complexity |
| Modularity vs Performance | Module boundaries can prevent cache-friendly layouts |

**The rule:** Choose the **fewest** characteristics critical to success. Aim
for "least worst" rather than "best." 3-7 characteristics is typical.

---

## Connascence: Analyzing Coupling

Connascence measures coupling strength. Ranked from weakest to strongest:

### Static Connascence (visible in source code)

| Type | What it means | Example |
|---|---|---|
| **Connascence of Name** | Components agree on identifier names | Method name, variable name |
| **Connascence of Type** | Components agree on types | Function expects an `int` |
| **Connascence of Meaning** | Components agree on values | "0 means inactive, 1 means active" — magic numbers |
| **Connascence of Position** | Components agree on order | Argument order in function calls |
| **Connascence of Algorithm** | Components agree on algorithm | Both sides hash the same way |

### Dynamic Connascence (only at runtime)

| Type | What it means |
|---|---|
| **Connascence of Execution** | Components must execute in a specific order |
| **Connascence of Timing** | Components must run within timing constraints |
| **Connascence of Values** | Multiple values must agree (e.g., distributed transaction) |
| **Connascence of Identity** | Components must reference the same instance |

### Three Properties

For each connascence:
- **Strength:** How easy to refactor (Name = easy; Identity = hard)
- **Locality:** Closer = better tolerated (same module > across services)
- **Degree:** How many components share the connascence

### Rules

1. Stronger connascence = worse coupling. Reduce strength.
2. Closer locality = stronger connascence is acceptable. Across-service connascence should be weak.
3. Lower degree = better. Fewer entangled components.

---

## Principles

- **Trade-off analysis is the architect's job.** No right answers, only trade-offs informed by business context.
- **Technical breadth > technical depth for architects.** Know a little about a lot. Engineers go deep; architects go wide.
- **Decompose composite characteristics.** "Agility" → Deployability + Modularity + Testability. Make it measurable.
- **Limit the characteristics list.** 3-7 is right; more dilutes focus and creates conflicts.
- **Beware the Bottleneck Trap.** Don't write critical path code; delegate. Architects who become coding bottlenecks block teams.
- **Last Responsible Moment.** Defer decisions until you have enough information, but not so long that analysis paralysis sets in.
- **Single source of truth for decisions.** ADRs in a wiki, not emails. Future-you and team need findability.

---

## Anti-Patterns to Avoid

### Frozen Caveman

**Looks like:** Architect insists on patterns that worked 10 years ago, ignoring modern alternatives.

**Why it fails:** Tools and patterns evolve. Yesterday's best practice is today's anti-pattern.

**The fix:** Use the Thoughtworks Technology Radar pattern: Hold / Assess / Trial / Adopt. Continually re-evaluate.

### Ivory Tower Architecture

**Looks like:** Architect makes decisions in isolation; hands them down to implementation team.

**Why it fails:** Misses on-the-ground reality; team has no buy-in; decisions don't survive contact with code.

**The fix:** Collaborate with implementers. Participate in code reviews. Validate decisions in code, not just diagrams.

### Bottleneck Architect

**Looks like:** Architect is on critical path for all coding; team blocked waiting.

**Why it fails:** Architect becomes throughput limit; team can't scale.

**The fix:** Code on minor business functionality, not critical path. Stay technical without becoming the bottleneck.

### Maximum Characteristic Optimization

**Looks like:** Trying to make the system maximally fast AND scalable AND secure AND simple AND portable.

**Why it fails:** Characteristics conflict. Maximizing all of them is impossible.

**The fix:** Pick the 3-7 most critical to business success. Accept being "good enough" on the rest.

### Specifying Without Measuring

**Looks like:** "The system must be highly available." No definition. No measurement.

**Why it fails:** Can't verify the requirement is met. Endless arguments about whether the system is "available enough."

**The fix:** Specify with numbers. "99.9% uptime, p99 latency < 200ms, RPO < 5min."

---

## Decision Rules

| Condition | Action |
|---|---|
| New system architecture work | List all relevant ilities; pick 3-7 critical ones |
| Composite characteristic in requirements (e.g., "agility") | Decompose into measurable components |
| Two characteristics conflict | Trade-off analysis with business context |
| Module coupling is hard to reason about | Apply Connascence to identify the strength |
| Decision has long-term implications | Write an ADR; archive in wiki |
| Tempted to specify without numbers | Stop. Define measurement. Then decide. |
| Facing premature decision pressure | Apply Last Responsible Moment principle |

---

## Worked Example: Architectural Characteristics for a Notification Service

**Business context:** Internal company notification service; sends emails, Slack messages, mobile push. Used by all internal product teams.

| Characteristic | Selected? | Rationale |
|---|---|---|
| **Reliability** | Yes (top 3) | Notifications are downstream of user-impacting events; can't drop them |
| **Scalability** | Yes (top 3) | Internal use grows with company headcount + feature surface |
| **Modularity** | Yes (top 3) | Many integration points (email/Slack/push); modular plug-ins enable independent change |
| **Performance** | No (medium) | Notification latency tolerated up to seconds; not a hot path |
| **Availability** | Implicit | Always required; not unique to this system |
| **Security** | Implicit | Always required; not unique |
| **Portability** | No | Internal infra; no need to port |
| **Usability** | No | Backend service; consumed via API |

**Decomposition:** "Modularity" measured as: "Add new channel without modifying core orchestration code." Concrete, testable.

**Trade-off:** Selected reliability over performance. If a notification fails, retry. Latency is acceptable; loss is not.

---

## Gotchas

- **Implicit characteristics are the silent killers.** Security, basic usability, baseline availability — never in requirements, always required. Surface them yourself.
- **Composite characteristics are slippery.** "Quality" is meaningless. Decompose to measurable parts.
- **Architecture characteristics drift.** What's critical at year 0 isn't critical at year 5. Revisit periodically.
- **Connascence within a module is fine; across modules is risk.** Locality matters as much as strength.
- **ADRs are write-once but read-many.** Spend time on the rationale section. Future-you will thank you.

Source: *Fundamentals of Software Architecture* by Mark Richards and Neal Ford, Chapters 1-4.
