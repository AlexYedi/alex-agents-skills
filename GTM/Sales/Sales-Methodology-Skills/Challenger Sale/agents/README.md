# Challenger Agents — Orchestrating the Sales Process

Seven specialized agents support the Challenger sales motion. Each owns
one focused responsibility. The orchestrator routes work across them
based on which sales stage Alex is in.

| Agent | Owns | Routes from / to |
|---|---|---|
| `challenger-orchestrator.md` | Routing across stages; deal-level state | Routes to all others |
| `commercial-insight-generator.md` | Stage 0 — segment-level Reframes | → reframe-architect |
| `reframe-architect.md` | Stages 1–4 — the 6-step pitch | → safe-bold-auditor; → mobilizer-mapper |
| `safe-bold-auditor.md` | Quality gate on every Reframe + pitch | ↔ reframe-architect, ↔ content-companion |
| `mobilizer-mapper.md` | Stage 5 — stakeholder classification | → take-control-coach (for foils) |
| `take-control-coach.md` | Stages 1, 5–8 — assertiveness scripts | Returns to current stage |
| `content-companion.md` | Challenger-voiced drafting of all 10 artifacts | → safe-bold-auditor; ← reframe-architect |

## How to invoke

In conversation Alex can say:

- *"Run the orchestrator on [account]"* → `challenger-orchestrator`
- *"Generate a commercial insight for [segment]"* → `commercial-insight-generator`
- *"Build the Reframe for [account]"* → `reframe-architect`
- *"SAFE-BOLD audit on this pitch"* → `safe-bold-auditor`
- *"Mobilizer check on [contact list]"* → `mobilizer-mapper`
- *"Take Control script for [moment]"* → `take-control-coach`
- *"Draft the [cold email / LinkedIn post / Reframe slide / one-pager
  / peer story / follow-up / MAP opener / Mobilizer 1-pager / proposal
  cover / pitch deck] for [account]"* → `content-companion`
- *"Challenger this email"* / *"Rewrite this in Challenger voice"* →
  `content-companion`

The orchestrator is the default entry point when the deal stage is
ambiguous or multiple agents need to coordinate.

## Why agents (not just sub-skills)

These are agent-shaped because each one:

- Has a **specific input contract** (what it needs from Alex).
- Produces a **specific output artifact** (deterministic shape).
- **Hands off** to a specific next agent or back to Alex.
- Can be invoked **standalone** mid-deal without re-priming Alex on the
  whole framework.

The parent `Challenger-Sale` body file is the *theory*. These agents
are the *operating system* that runs the theory through the live deal.

## Stage-to-agent map

| Sales stage | Primary agent(s) | Content companion fires for |
|---|---|---|
| 0 — Account selection + insight prep | `commercial-insight-generator` | LinkedIn post (segment-level), pitch-deck Reframe slide |
| 1 — First contact | `reframe-architect`, `take-control-coach` (foil) | Cold email cadence (Touches 1–3) |
| 2 — First meeting (Warmer + Reframe) | `reframe-architect`, `safe-bold-auditor` | Reframe slide, executive pitch deck, follow-up email |
| 3 — Insight validation | `reframe-architect`, `safe-bold-auditor` | Rational Drowning one-pager, peer story |
| 4 — Solution alignment | `reframe-architect` | Tailored economic-impact appendix |
| 5 — Mobilizer activation | `mobilizer-mapper`, `take-control-coach` | Mobilizer enablement 1-pager |
| 6 — Buying process coaching | `take-control-coach` | Mutual Action Plan opener |
| 7 — Pricing / procurement | `take-control-coach` | Proposal / order form cover letter |
| 8 — Verbal yes → close | `take-control-coach` | Follow-up + MAP refresh |
| 9 — Handoff / expansion | (defer to Winning by Design) | Handoff brief, QBR template |

The `content-companion` fires alongside the primary agent at every
stage where an artifact is produced. It is the voice layer over the
methodology layer.

## Pairs with

- Parent `Challenger-Sale` — full methodology body file.
- `references/sales-process-stage-playbook.md` — what each stage
  requires.
- `references/challenger-skills-catalog.md` — the rep skills the
  agents coach.
- `references/voice-and-style-guide.md` — the content voice the
  agents enforce.
