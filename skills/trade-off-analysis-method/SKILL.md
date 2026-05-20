---
name: trade-off-analysis-method
description: >
  Walks through the 3-step trade-off analysis method from Ford/Richards/
  Sadalage/Dehghani's "Software Architecture: The Hard Parts" (Ch 2 + Ch 15).
  Surface entangled dimensions, analyze how they're coupled, assess
  impact of change, score candidate solutions against architectural
  characteristics, and produce a defensible ADR. Use when making any
  architecture decision someone will second-guess later, when picking
  between two or more viable options, when the team is stuck between
  competing concerns, or when an ADR needs a trade-off table to defend
  it. This is the meta-skill the book teaches; load it before specific
  pattern-selection skills if the decision has high downstream impact.
  Triggers - "trade-off analysis", "tradeoff analysis", "build your own
  trade-off", "architecture decision", "ADR", "Architecture Decision
  Record", "we're stuck between X and Y", "how do we decide", "defensible
  architecture decision", "score the options", "trade-off table",
  "what are the trade-offs", "discipline for architecture decisions",
  "explicit trade-off". Produces a fully-scored ADR with trade-off table.
  Step-by-step workflow.
---

# Trade-Off Analysis Method (The Hard Parts' Build-Your-Own)

You walk architects through the **3-step trade-off analysis method** that is the meta-thesis of *Software Architecture: The Hard Parts* (Ford, Richards, Sadalage, Dehghani — 2021, Ch 1, 2, 15). This is a **workflow** skill, not a knowledge dump — when loaded, you march the user through the steps and produce an ADR at the end.

The book's framing: most architecture decisions have no best practice. The architect's job is the **method**, not the answer. The method is the discipline that lets future engineers tell intentional decisions from incidental ones.

The canonical method is described in *Software Architecture: The Hard Parts* (Ford, Richards, Sadalage, Dehghani — O'Reilly, 2021), Ch. 1 under "Trade-Off Analysis 3-Step". The steps below are the operational distillation.

---

## Related

- **Related skills**
  - `distributed-workflows-and-sagas` — pattern-selection workflow that uses this method
  - `data-ownership-and-distributed-data` — pattern-selection workflow that uses this method
  - `service-contracts-and-coupling` — pattern-selection workflow that uses this method
  - `architecture-characteristics-and-tradeoffs` — defines the *characteristics* this method scores against (load this if the characteristics for the system aren't yet defined)
  - `cto-architect` — loads this skill as part of CTO-level decisions
- **Related references** (bibliographic — for human/maintainer use)
  - *Software Architecture: The Hard Parts* (Ford, Richards, Sadalage, Dehghani — O'Reilly, 2021), "Trade-Off Analysis 3-Step" framework — the canonical method
  - *The Hard Parts*, Sysops Squad worked example — every ADR in the case study uses this method
  - *Fundamentals of Software Architecture* (Richards & Ford — O'Reilly, 2020), characteristics catalog ("ilities")

---

## Contract for this skill

When loaded, this skill marches the user through **the 3-step method** + framing + ADR write-up. Total: 5 numbered steps, ~15–30 minutes of conversation depending on complexity.

If the user resists doing the method ("can't we just pick one?"), surface this question: *"Will anyone second-guess this decision in 6 months? If yes, we need the trade-off table to defend it. If no, you don't need this skill."*

---

## Step 0 — Frame the decision

Before the method starts. Get a one-sentence statement of the decision.

Ask:

1. **What is the decision?** ("Should we use a saga pattern or distributed transactions?")
2. **What are the candidate options?** List 2–N. Minimum 2; usually 2–4. If only 1, there's no decision; if >4, narrow first.
3. **Why does it matter?** What changes downstream if you pick the wrong option?
4. **Who can second-guess it later?** Future engineers, other teams, leadership, auditors, security.

### Checkpoint

If the user can name only one option, **stop**. Either there's no decision (just do it) or they haven't surfaced the alternatives. Push them to name at least one credible alternative before continuing.

---

## Step 1 — Find what parts are entangled together (Method Step 1)

Identify the **dimensions** that interact in this decision. The book lists at least these dimension types:

| Dimension type | Example |
|---|---|
| Static coupling | OS deps, framework deps, DB deps, libraries |
| Dynamic coupling | Sync/async calls, message passing |
| Semantic coupling | Domain meaning shared across services |
| Stamp coupling | Data volume passed in contracts |
| Data coupling | Shared schemas, replicated data |
| Operational coupling | Shared infrastructure, monitoring |
| Team coupling | Conway's Law shaping the answer |

Ask: **for each candidate option, which of these dimensions get touched?**

### Build the static-coupling diagram (when applicable)

For architectural decisions involving service quanta, the book recommends a **static-coupling diagram** with these elements:

- OS / container dependencies
- Transitive dependencies (frameworks, libraries)
- Persistence dependencies (DBs, search engines, cloud services)
- Architecture integration points required for the service to bootstrap
- Messaging infrastructure required to enable communication

For each candidate option, draw (or describe in text) the diagram. The diagrams are the input to Step 2.

### Output of Step 1

A list of entangled dimensions, with each option mapped to the dimensions it touches.

```
Option A: <name>
  - touches: static, dynamic, semantic
  - static-coupling diagram: <description>

Option B: <name>
  - touches: static, dynamic, data
  - static-coupling diagram: <description>
```

---

## Step 2 — Analyze how they are coupled to one another (Method Step 2)

For each dimension the options touch, **name the type of coupling and score the strength**.

| Coupling strength | Meaning |
|---|---|
| very high | Quantum boundary — these things move together |
| high | Strong dependency; change in one forces change in others |
| medium | Notable dependency; some change tolerance |
| low | Minor dependency; mostly independent |
| very low | Negligible dependency |

The 8-saga matrix uses these same five buckets (very high → very low). Apply the same vocabulary here.

### Score each option per dimension

```
                Static   Dynamic   Semantic   Stamp   Data
Option A         high     med       med       low     low
Option B         med      low       high      med     high
```

If the user can't score, that's a signal to load `architecture-characteristics-and-tradeoffs` first to get the vocabulary calibrated.

### Output of Step 2

A coupling matrix: candidate options × dimensions × strength score.

---

## Step 3 — Assess trade-offs by determining impact of change (Method Step 3)

For each option, ask: **what happens when something changes?** Change sources:

- Business requirements shift
- A participant service gets rewritten
- A team owning a service gets reorganized
- Volume scales 10×
- A new participant joins the workflow

For each change source × each option, estimate **blast radius** — how many other things must change in response.

### Score against architectural characteristics

Identify the **3–7 architectural characteristics** that matter most for this system. If not already defined, load `architecture-characteristics-and-tradeoffs` first. Then score each option:

```
Characteristic       Weight   Option A   Option B   Option C
Performance          high     med        high       low
Availability         high     high       med        med
Maintainability      med      low        high       high
Deployability        med      med        high       high
Cost                 low      low        med        high
```

Use a 3-point scale (low / med / high) for first-pass scoring. Numeric scales tempt false precision. The book uses qualitative scoring throughout.

### Output of Step 3

A trade-off table: characteristics × options × score, plus a "what changes when…" analysis.

---

## Step 4 — Pick the option and write the ADR

The output of this method is **always an ADR**. Even if the team feels obvious about the answer. The ADR is the artifact that defends the decision when it's second-guessed.

### ADR template (Hard Parts style)

```
ADR-NNN: <decision title>

Context:
  <2-4 sentences: the situation, the constraints, the assumptions>

Decision:
  We will <chosen option>.

Options considered:
  - Option A: <name> — <one-line>
  - Option B: <name> — <one-line>
  - Option C: <name> — <one-line>

Coupling analysis:
  | Option | Static | Dynamic | Semantic | Stamp | Data |
  |---|---|---|---|---|---|
  | A | … | … | … | … | … |
  | B | … | … | … | … | … |
  | C | … | … | … | … | … |

Trade-off table (against system's architectural characteristics):
  | Characteristic | Weight | A | B | C |
  |---|---|---|---|---|
  | Performance | high | med | high | low |
  | Availability | high | high | med | med |
  | … | … | … | … | … |

Rationale for chosen option:
  <2-4 sentences explaining why this option wins on the weighted characteristics>

Consequences:
  Positive:
    - <…>
  Negative:
    - <…>
  Mitigations:
    - <…>

Fitness functions (governance):
  - <test or guardrail that protects this decision over time>
```

### Where the ADR lives

Adopt one consistent location per project — typically `docs/adr/` or `architecture/decisions/`. Number sequentially. **Don't amend existing ADRs**; when a decision is superseded, write a new ADR that links to the prior one with `Supersedes: ADR-XXX`.

---

## Step 5 — Add fitness functions (optional but endorsed)

The book endorses **architectural fitness functions** — automated tests that protect the characteristics named in the ADR.

Examples:
- ADR picked Parallel Saga because the team needs low coupling between services → fitness function: a CI test that fails if any service's static dependency on another service rises above a threshold.
- ADR picked a strict contract because the team needs early error detection → fitness function: a CI test that fails if any consumer-driven contract test breaks.

Not every ADR needs a fitness function. Critical ones — especially ones that the team will drift away from — do.

This is the bridge to `Building Evolutionary Architectures` (Ford/Parsons/Kua); the Hard Parts treatment is brief. If you need a deeper fitness-function design, suggest that book.

---

## When to invoke this skill

| Trigger | Why this method |
|---|---|
| Choosing between viable patterns (saga, contract, data ownership) | The trade-offs aren't obvious without scoring |
| Two engineers strongly disagree on an architecture decision | The method surfaces the actual coupling each is optimizing for |
| Leadership asks "why did we pick this?" 6 months later | The ADR is the answer |
| Compliance / audit needs decision rationale | The ADR is the audit trail |
| Re-architecting a system; many decisions cluster | Run the method once; reuse the dimensions/characteristics across decisions |

## When NOT to invoke this skill

- **Reversible, low-impact decisions.** If picking wrong costs an hour, don't spend an hour analyzing.
- **Decisions with one viable option.** That's not a decision; do it.
- **Tactical implementation choices** (which library, which framework version) — usually too granular. The method is for architecture-level decisions.
- **Decisions already made well in another ADR** that fits this situation. Cite the prior ADR instead.

---

## Common failure modes (call these out when you see them)

### "We don't have time for this method"

The book's response (Ch 15, Logan to Morgan): *"That's architecture. And as you can see, it works."*

Practical response: time spent now is small compared to the cost of a wrong decision discovered in 6 months. Surface the cost of being wrong; the cost of analysis usually justifies itself.

### "We don't know the characteristics yet"

That's a separate decision. Load `architecture-characteristics-and-tradeoffs` first, fix the characteristics, then come back.

### "All options score the same"

That's a real outcome. It means the decision is genuinely insensitive to the trade-offs you scored. Pick the cheapest / fastest / most reversible option and document that the analysis was insensitive. The ADR is still valuable — future engineers will see that this *was* analyzed.

### "We can't decide between two options"

The matrix usually breaks ties via the weighted characteristics. If after weighting it's still a tie, run a small spike on the cheaper option for 1–2 days, see what surfaces, then re-score. Don't pick by gut when you've gone this far.

### "The team won't read ADRs"

That's a team-culture problem, not a method problem. The book is firm: without the discipline, you don't have architecture, you have luck. If the team won't engage, surface that to leadership as a process gap.

### "We wrote an ADR but never look at it again"

ADRs are read when:
- A new engineer joins and asks "why this?"
- A decision is being revisited
- Leadership asks "why this?" in a review
- An audit asks for decision history

If none of those happen, the ADR still served its purpose: it forced the team to *think* before deciding. The artifact is a side-benefit; the discipline is the point.

---

## Worked example

The Sysops Squad case study is 15 chapters of this method applied repeatedly. Specific worked ADRs to study:

| ADR | What it shows |
|---|---|
| Ch 4 — Migration via Component-Based Decomposition | How to pick a decomposition approach with the method |
| Ch 7 — Consolidated Service for Ticket Assignment | Two different granularity decisions, same method, different answers |
| Ch 10 — In-Memory Replicated Caching for Expert Profile | Data access pattern choice with explicit trade-off table |
| Ch 12 — Parallel Saga for ticket workflow | Saga selection with explicit axis scoring |
| Ch 13 — Loose Contract for Mobile App | Strict-vs-loose contract decision with explicit trade-off |

See *The Hard Parts*, Sysops Squad worked example, for the full walkthrough.

---

## How to teach this method to a team

If the user is trying to introduce this discipline at a team or org level, the book's implicit recommendation:

1. **Pick one upcoming decision** that everyone agrees is important.
2. **Run the method on it** with the team in the room. Make it visible.
3. **Write the ADR** together. Show it to leadership.
4. **Reference the ADR** the next time the topic comes up in a meeting.
5. **Don't mandate it** for every decision; let the team discover when it's worth doing.

The Sysops Squad case study is exactly this arc: Logan introduces the method on the first big decision (Ch 4), and by Ch 15 the team uses it reflexively. The discipline grew because it worked, not because it was mandated.
