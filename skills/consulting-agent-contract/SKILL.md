---
name: consulting-agent-contract
description: >
  Applies Bertrand Meyer's Design by Contract (Eiffel, 1986; Object-Oriented Software
  Construction, 1988/1997) and C.A.R. Hoare's axiomatic semantics ("An Axiomatic Basis for
  Computer Programming," CACM, 1969) to make an AI agent's obligations formal. For each
  automated behaviour, states the precondition (client's obligation), postcondition
  (supplier's guarantee), and class invariant (property true at every stable state), then
  expresses the critical paths as Hoare triples {P} action {Q}.
  Triggers - "what's the agent's contract", "design by contract for this agent", "Hoare triple",
  "preconditions and postconditions", "what must be true before the agent runs", "what does the
  agent guarantee", "agent invariants", "guardrails for this automation", "when should the agent
  reject vs roll back", "formalize the agent's obligations", "what happens if the precondition
  is violated", "blame assignment when the agent breaks". Produces an agent-contract spec per
  behaviour: preconditions | postconditions | invariants (guardrails) | violation responses,
  plus Hoare triples for the critical paths.
---

# The Agent Contract (Design by Contract, Meyer, 1986; Hoare logic, 1969)

Bertrand Meyer built Design by Contract into the Eiffel language in 1986 and formalized it in
*Object-Oriented Software Construction* (Prentice Hall, 1988/1997): the relationship between a
software element and its clients is a formal contract, with a precondition the client must
guarantee before calling, a postcondition the supplier guarantees on return, and a class
invariant that holds in every stable state. The slogan is exact — "if you promise to call me
with the precondition satisfied, I promise to deliver a state satisfying the postcondition." No
redundant checking on either side, and when something breaks, the contract tells you whose
fault it is.

C.A.R. Hoare gave this its formal foundation eleven years earlier: "An Axiomatic Basis for
Computer Programming" (*Communications of the ACM*, 12(10), 1969) defines the Hoare triple
`{P} C {Q}` — if precondition `P` holds and command `C` executes and terminates, postcondition
`Q` holds — along with the axioms and inference rules (assignment, composition, conditionals,
while-loops, weakest-precondition reasoning) for proving it. DbC is the engineering practice;
Hoare logic is why it's provable rather than aspirational. This skill applies both to an AI
agent or automation: its inputs, its guaranteed outputs and side effects, and the safety
properties that must hold no matter what path it takes.

---

## Where this sits in the engagement

Step 12 of 14, Phase D (Specify & build safely). It takes the automation design from
`consulting-automation-design` (step 7) and the verifiable behaviour spec from
`consulting-behaviour-specification` (step 11) and turns them into a formal contract per
behaviour — preconditions, postconditions, invariants, and violation responses. It pairs with
`consulting-failure-design` (step 13): the contract defines what "correct" means; FMEA defines
what happens when a clause is violated. Its invariants and postconditions become the monitored
SLOs in `consulting-acceptance-bar` (step 14).

---

## When to use this skill

- An automation design (step 7) or Given-When-Then spec (step 11) exists and now needs formal
  obligations before anyone builds against it.
- You need to decide, precisely, what the agent is allowed to assume about its inputs and what
  it must guarantee on a successful run.
- You're defining guardrails — PII handling, spend caps, authorization boundaries — that must
  hold on every path, not just the happy path.
- A build is underway and it's unclear whether a bug is a caller error (bad input, precondition
  violated) or a supplier error (broken promise, postcondition violated) — you need blame
  assignment.
- You're about to hand the spec to failure-mode analysis (step 13) or acceptance criteria
  (step 14) and need the contract clauses those steps will consume.
- Stakeholders are debating "what should the agent do when X is wrong" and need a designed
  response, not an ad hoc one.

---

## The method

### 1. The three assertion types (Meyer, Design by Contract)

- **Precondition** — what the client must guarantee is true BEFORE calling the agent. This is
  the client's obligation and the supplier's benefit: the agent need not handle, defend against,
  or even check for inputs that violate it.
- **Postcondition** — what the agent guarantees is true ON RETURN, *provided the precondition
  held*. This is the supplier's obligation and the client's benefit.
- **Class invariant** — a property that holds before and after every operation: true in every
  stable state, regardless of which path was taken to get there.

The contract slogan: *"If you promise to call me with the precondition satisfied, I promise to
deliver a state satisfying the postcondition."* Benefits: no redundant checking on either side,
and unambiguous blame assignment when a run fails.

### 2. The Hoare triple (Hoare, 1969)

`{P} C {Q}` — if precondition `P` holds and command `C` executes and terminates, then
postcondition `Q` holds. Use it to state, formally and compactly, the contract for one critical
action: what must be true going in, what the action does, what must be true coming out. Hoare
logic's rules (composition, conditionals, loops, weakest precondition) are the machinery for
proving `{P} C {Q}` actually holds — for this skill's purposes, write the triple as the
precise, checkable statement of the contract; formal proof is optional but the triple should be
tight enough that it *could* be checked.

### 3. Translating the three assertion types to an AI agent / automation

| Assertion | For an agent, means |
|---|---|
| **Precondition** | Valid & authenticated inputs; required tools/permissions available; budget/rate limits not exceeded; required context present. |
| **Postcondition** | The guaranteed output shape and side effects (a record written, a ticket created); what must be TRUE after a successful run. |
| **Invariant** | Safety / PII / authorization properties that hold at EVERY step regardless of path — never exfiltrate PII, never exceed the spend cap, always leave an audit trail. **These invariants are the guardrails.** |

### 4. The response to a violated clause

A contract is incomplete without a designed response to each way it can break:

- **Violated precondition** → **reject or escalate.** The agent must not proceed on bad input.
  It either refuses the call outright (return an error, no side effects) or escalates to a
  human, per the human-in-loop points set in step 7.
- **Broken postcondition** → **roll back or alert.** If the agent ran with the precondition
  satisfied but failed to deliver the guaranteed output/state, it must undo any partial side
  effects (roll back) and/or raise an alert — never leave the system in a half-committed state.
- **Violated invariant** → treat as the most severe case regardless of where in the run it's
  caught: halt immediately, roll back any effects, and alert — an invariant break means a
  guardrail failed, which is a different severity class from a normal postcondition miss.

This response design is the handoff surface to `consulting-failure-design` (step 13): the
contract says what "correct" is and what response each violation gets; FMEA scores how likely
and severe each violation is and designs the mitigation around the response already chosen here.

---

## Workflow (what you do when invoked)

1. Pull each automated behaviour from `consulting-automation-design` (step 7, the function
   allocation and human-in-loop points) and `consulting-behaviour-specification` (step 11, the
   Given-When-Then scenarios).
2. For each behaviour, state its **preconditions**: valid/authenticated inputs, required
   tools/permissions, budget or rate-limit headroom, required context.
3. State its **postconditions**: guaranteed output shape, guaranteed side effects, what must be
   true on successful return.
4. State its **invariants**: the safety/PII/authorization properties that must hold at every
   step of this behaviour regardless of path — these are the guardrails, list them explicitly.
5. For the critical path(s) of each behaviour, write one or more Hoare triples `{P} action {Q}`
   that compress steps 2–3 into a single checkable statement.
6. For every precondition and postcondition, and for every invariant, decide and record the
   violation response: reject/escalate (precondition) vs. rollback/alert (postcondition) vs.
   halt/rollback/alert (invariant).
7. Hand the completed contract to `consulting-failure-design` (step 13, to score likelihood and
   severity of each violation and design mitigations) and flag which invariants and
   postconditions should become monitored SLOs in `consulting-acceptance-bar` (step 14).

---

## Deliverable & templates

```
## Agent contract — <behaviour name>

### Preconditions (client's obligation — agent may assume these hold)
- 
- 

### Postconditions (supplier's guarantee — true on successful return)
- 
- 

### Invariants (guardrails — true at every step, regardless of path)
- 
- 

### Hoare triples — critical paths
{P: ...} <action> {Q: ...}
{P: ...} <action> {Q: ...}

### Violation responses
| Clause type | Clause | Violation response (reject/escalate vs rollback/alert) | Owner |
|---|---|---|---|
| Precondition | | | |
| Postcondition | | | |
| Invariant | | | |
```

Repeat one block per automated behaviour carried over from steps 7 and 11.

---

## Pitfalls

- **Precondition doubles as defensive code.** If the agent checks for and gracefully handles a
  violated precondition, that condition isn't actually a precondition — it's part of the
  postcondition-bearing logic. Decide which one it is and write it there.
- **Postconditions describe intent, not verifiable state.** "The agent handles the request
  well" is not a postcondition. Write what must be TRUE and checkable — a record with specific
  fields, a status code, a ticket ID returned.
- **Invariants smuggled in as postconditions.** A property that must hold mid-run (never exceed
  spend cap) is an invariant, not something to check only at the end — by then the damage is
  done. Invariants need to be checkable during execution, not just at the end.
- **No designed response for a violation.** A precondition/postcondition list with no
  reject/escalate or rollback/alert decision leaves the agent's failure behavior undefined —
  that decision belongs here, not improvised at runtime or discovered in an incident.
- **Contract too loose to be checkable.** A Hoare triple whose `P` or `Q` can't be evaluated
  against real system state isn't a contract, it's a mission statement. Tighten until it's
  something a test or a monitor could actually assert.
- **Contract never revisited after step 13/14.** FMEA findings and acceptance-bar SLOs often
  reveal a missing invariant or an underspecified postcondition — treat the contract as living
  until the acceptance bar is set, not frozen at first draft.

---

## Related

- **In-suite** — `consulting-automation-design` (step 7, upstream): supplies the function
  allocation and human-in-loop points this contract formalizes. `consulting-behaviour-
  specification` (step 11, upstream): supplies the Given-When-Then scenarios this contract
  turns into pre/postconditions. `consulting-failure-design` (step 13, downstream/pairs): scores
  likelihood and severity of each violation and designs mitigations around the responses set
  here. `consulting-acceptance-bar` (step 14, downstream): promotes invariants and
  postconditions into monitored SLOs and the run-time error budget.
- **Elsewhere in the library** — `agent-memory-and-guardrails`, `ai-agent-design-patterns`,
  `ai-evals`.
- **References** — *Object-Oriented Software Construction* (Bertrand Meyer, Prentice Hall,
  1988/1997), including the 1986 Design by Contract concept from the Eiffel language; "An
  Axiomatic Basis for Computer Programming" (C.A.R. Hoare, *Communications of the ACM*, 12(10),
  1969).
