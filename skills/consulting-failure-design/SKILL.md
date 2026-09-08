---
name: consulting-failure-design
description: >
  Combines Failure Mode and Effects Analysis (FMEA — MIL-STD-1629A; AIAG-VDA FMEA Handbook,
  2019) with Gary Klein's Pre-Mortem ("Performing a Project Premortem," Harvard Business Review,
  September 2007) to design against how an agent or automation will fail before you build it.
  Runs a divergent pre-mortem to surface failure modes, then scores each convergently with
  Severity x Occurrence x Detection to rank and mitigate the worst offenders.
  Triggers - "pre-mortem", "premortem", "FMEA", "failure mode analysis", "risk priority number",
  "RPN", "what could go wrong before we build this", "how could this agent fail", "failure
  modes for this agent", "score the risks before launch", "assume this already failed", "design
  for failure", "prospective hindsight". Produces a pre-mortem reason list plus a scored FMEA
  table (failure mode, effect, cause, S, O, D, RPN, mitigation, owner, residual RPN) with
  detection-improving mitigations flagged as candidate monitors.
---

# Failure Design (FMEA + Pre-Mortem, Klein, HBR, 2007)

Before you build, you assume the thing has already failed — spectacularly — and work backward.
Gary Klein's pre-mortem ("Performing a Project Premortem," *Harvard Business Review*, September
2007) is a technique of prospective hindsight: research on the technique found that imagining an
outcome as having already happened increases people's ability to correctly identify the reasons
for it by roughly 30%, because it gives permission to voice doubts that hierarchy, optimism, and
groupthink otherwise suppress.

Failure Mode and Effects Analysis (FMEA) is the convergent half. Originating in US military
standard MIL-STD-1629A and standardized for industry by the automotive and aerospace world (the
AIAG-VDA FMEA Handbook, 2019), FMEA takes each candidate failure mode and scores it on three
1–10 scales — Severity, Occurrence, Detection — multiplies them into a Risk Priority Number, and
ranks the result so mitigation effort goes where it matters most.

---

## Where this sits in the engagement

This is step 13 of 14, the third skill in Phase D (Specify & build safely). It takes the
pre/postconditions and invariants from `consulting-agent-contract` (step 12) as the object under
test — you are asking "how does *this contract* get violated in the real world?" Its output feeds
`consulting-acceptance-bar` (step 14): mitigations that reduce Detection are exactly the checks
and monitors that become the go-live acceptance bar and the run-time error budget.

---

## When to use this skill

- An agent contract exists and you're about to move from spec to build.
- Stakeholders are optimistic ("this will be fine") and you need a structured way to surface doubt.
- You need a defensible, ranked list of what could go wrong — not a vague risk paragraph.
- The system is autonomous or semi-autonomous and failures could be silent (wrong answer, no
  error thrown) rather than loud (crash, exception).
- You're deciding what to monitor at run time and need to justify each monitor by the risk it detects.
- A prior incident or near-miss suggests the team's mental model of failure modes is incomplete.

---

## The method

### Step 1 — Pre-mortem (divergent)

Gather the team that owns the agent contract. Pose Klein's frame exactly:

> "It is six months from now. This agent/automation has failed — badly. Spend two minutes,
> working alone and in silence, writing down every reason you believe it failed."

Rules that make it work:
- **Independent and silent first.** Each person writes their own list before anyone speaks —
  this is what defeats groupthink and hierarchy suppression; a shared brainstorm collapses back
  into the same biases the technique exists to escape.
- **Past tense, certainty framing.** Not "what might go wrong" (hedged, optimistic) but "why did
  this fail" (assumed, already happened) — this framing is the mechanism behind the ~30% lift in
  identified reasons.
- **No filtering, no scoring yet.** Name fears, edge cases, embarrassing possibilities, and
  political/organizational failure modes, not just technical ones.
- Go around the room and have each person read one reason at a time, round-robin, until lists are
  exhausted. Capture everything verbatim before consolidating.

### Step 2 — Consolidate into failure modes

Cluster the raw reasons into distinct **failure modes**, each with an **effect** (what the user
or business experiences) and a **cause** (the mechanism). For an AI agent, expect failure modes
across at least these families — do not let the pre-mortem stop at "the model is wrong":

- **Hallucination** — confident, fabricated output presented as fact.
- **Tool/API errors** — a called tool fails, times out, or returns malformed/stale data.
- **Prompt injection** — untrusted content in context redirects the agent's behavior.
- **Silent wrong answers** — output is wrong but structurally well-formed, so nothing flags it.
- **Cascading autonomy** — one bad decision triggers further autonomous actions before a human
  can intervene.

### Step 3 — FMEA scoring (convergent)

For every failure mode, score three factors, each 1–10:

| Factor | Question | 1 = | 10 = |
|---|---|---|---|
| **Severity (S)** | How bad is the effect if it occurs? | Negligible | Catastrophic / safety, legal, irreversible |
| **Occurrence (O)** | How likely is the cause to occur? | Practically never | Near-certain, frequent |
| **Detection (D)** | How unlikely are you to catch it before it reaches the customer? | Always caught pre-release | No mechanism catches it — first sign is the customer |

**Risk Priority Number: RPN = S × O × D** (range 1–1000). Rank all failure modes by RPN,
descending. (The modern AIAG-VDA handbook also computes an Action Priority category from the
S/O/D combination, but RPN remains the classic ranking mechanism and is what you compute here.)

### Step 4 — Mitigate and re-score

For the highest-RPN failure modes, define a **recommended action** — a mitigation that reduces
S, O, or D — and assign an **owner**. Then **re-score** S, O, D after the mitigation is assumed
in place to get the **residual RPN**. A mitigation that only reduces Detection (adds a check, a
monitor, a human-in-the-loop gate) is exactly the kind of control that step 14 turns into an
acceptance-bar monitor — flag these explicitly.

---

## Workflow (what you do when invoked)

1. **Pull the agent contract** from `consulting-agent-contract` — its pre/postconditions and
   invariants are what you're stress-testing.
2. **Run the pre-mortem.** Frame it in Klein's exact language ("it's six months from now and this
   failed badly — why?"), have each participant write independently and silently first, then
   collect round-robin. Do not let anyone score or filter during this pass.
3. **Consolidate** the raw list into distinct failure modes with effect and cause, checking
   coverage against the five AI-specific families (hallucination, tool/API error, prompt
   injection, silent wrong answer, cascading autonomy) and adding any missing.
4. **Score S, O, D** for every failure mode (1–10 each) and compute RPN = S × O × D.
5. **Rank by RPN** and define recommended actions + owners for the highest-ranked failure modes;
   don't try to mitigate everything — work down the ranked list until returns diminish.
6. **Re-score residual RPN** for each mitigated failure mode, assuming the action is in place.
7. **Hand off** the failure modes whose mitigation reduces Detection — with the specific
   check/monitor named — to `consulting-acceptance-bar` as candidate monitors and error-budget inputs.

---

## Deliverable & templates

**Pre-mortem reason list** (raw, pre-consolidation):

```
Participant | Reason the project/agent failed (verbatim, past tense)
------------|---------------------------------------------------------
A. Rivera   | It kept citing sources that don't exist.
A. Rivera   | Nobody noticed the tool was returning cached stale data.
J. Okafor   | A user pasted instructions into a form field and the agent obeyed them.
...
```

**FMEA table** (consolidated, scored):

| Failure mode | Effect | Cause | S | O | D | RPN | Mitigation | Owner | Residual RPN |
|---|---|---|---|---|---|---|---|---|---|
| Hallucinated citation | User acts on fabricated source | No grounding check on generated citations | 8 | 6 | 7 | 336 | Require citation-to-source-doc verification before output | J. Okafor | 8 x 3 x 2 = 48 |
| Prompt injection via pasted content | Agent executes attacker instructions | Untrusted text treated as trusted context | 9 | 4 | 8 | 288 | Sanitize/quarantine untrusted spans; instruction-hierarchy check | A. Rivera | 9 x 3 x 2 = 54 |
| Silent wrong answer | Wrong output looks well-formed, ships | No output-vs-postcondition check | 7 | 5 | 9 | 315 | Postcondition assertion from agent contract runs pre-return | (owner) | ... |

**Top failure modes for the acceptance bar** — the short list that becomes step 14 input:

```
Failure mode | Detection-improving mitigation | Proposed monitor/check | Owner
```

---

## Pitfalls

- **Skipping the silent, independent-write step.** Going straight to open discussion collapses
  the pre-mortem back into the same hierarchy/optimism bias it's designed to defeat — the ~30%
  lift depends on individuals committing to their own list first.
- **Scoring during the pre-mortem.** Divergent (generate) and convergent (score) are different
  cognitive modes; scoring too early kills the volume and honesty of failure modes surfaced.
- **Only technical failure modes.** Missing organizational, political, and adoption failure modes
  (e.g. "the team ignored the alerts," "nobody owned the escalation") because the pre-mortem was
  run only with engineers.
- **Treating RPN as the only signal.** A high-Severity, low-Occurrence, low-Detection failure
  mode (e.g. rare but catastrophic and invisible) can have a middling RPN yet demand priority
  mitigation anyway — sanity-check the ranked list, don't follow it blindly.
- **No residual re-score.** Listing a mitigation without re-scoring leaves you unable to tell
  whether the action actually moved the needle, or whether it just felt like it should.
- **Losing the pre-mortem's AI-specific coverage.** Generic FMEA templates default to mechanical
  failure modes; explicitly check hallucination, tool/API error, prompt injection, silent wrong
  answers, and cascading autonomy are each represented.

---

## Related

- **In-suite** — `consulting-agent-contract` (step 12, upstream): supplies the pre/postconditions
  and invariants this skill stress-tests. `consulting-acceptance-bar` (step 14, downstream):
  receives the detection-improving mitigations as candidate monitors and error-budget inputs,
  closing the loop with `consulting-benefits-case` and `consulting-behaviour-specification`.
- **Elsewhere in the library** — `risk-register`, `risk-scoring-framework`, `post-mortems-retrospectives`.
- **References** — *Performing a Project Premortem* (Gary Klein, 2007), Harvard Business Review;
  FMEA per MIL-STD-1629A; *AIAG-VDA FMEA Handbook* (2019).
