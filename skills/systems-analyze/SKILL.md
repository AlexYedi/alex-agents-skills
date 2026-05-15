---
name: systems-analyze
description: Run a deep systems-thinking diagnostic on a problem. Use for chronic dysfunction, multi-stakeholder problems, "why does this keep happening" questions, or second-opinion analyses on high-stakes decisions. Dispatches the systems-analyst subagent for the eight-phase Meadows analysis so the walk happens without burning main-context tokens.
argument-hint: "[problem statement, artifact URL, component name, or file path]"
---

# Systems Analyze — Workflow

Run a structured systems-thinking analysis on a problem and return a diagnostic the parent thread (you + the user) can act on. The analysis is delegated to the `alex:systems-analyst` subagent so the eight-phase walk happens without burning main-context tokens; the parent thread bounds the problem, dispatches, and decides what to do with the result.

**Input:** any of —
- Free-text problem statement ("the content pipeline keeps producing drafts that don't get published")
- URL to a relevant artifact (Notion page, Linear issue, doc)
- A named system component or skill ("the `pre-event-content` pipeline")
- Path to a local artifact (`.claude/artifacts/<file>.md`)
- Combination of the above

**Output:**
- A structured eight-phase diagnostic presented in conversation
- Optionally saved to a local artifact path for durable reference
- Optionally followed by a tracker-issue draft (Linear, GitHub, etc.) if the recommendation maps to actionable follow-through

---

## Trigger

This skill runs when:
- The user types `/alex:systems-analyze` followed by a framing question or artifact reference
- The user says any of: "run a systems analysis on X", "why does X keep happening", "diagnose X with systems-thinking", "second-opinion on this decision", "systems-thinking pass on Y"
- A higher-level workflow asks for a delegated systems pass

## Required inputs

1. **Problem framing** — at minimum a one-sentence statement of what feels wrong, stuck, or surprising. The framing itself may be the problem; the analyst will surface that if so.
2. **(Optional) Artifacts** — URLs, file paths, or prior diagnostic artifacts the analyst should read before walking the phases.
3. **(Optional) Stated scope** — "this week," "this quarter," "long-term paradigm question." Drives where the analyst lands on a horizon view if the parent project defines one.

If only a vague gesture is provided ("things feel stuck"), ask one clarifying question before dispatching. Don't dispatch on a malformed problem statement.

## Step 1 — Bound the problem (this conversation, NOT a subagent)

Run this in the parent thread:

1. Restate the problem in one sentence — what is the system, what is the observed behavior, and what is the gap between observed and desired.
2. List any artifacts the analyst should read (file paths, URLs). Verify each exists before dispatching.
3. If the project has a horizon framework, note which horizon the user is asking about. If not, skip.
4. Identify what success looks like — a list of leverage points, a decision, an archetype confirmation, etc. State this so the analyst can tune the diagnostic.
5. Confirm with the user before dispatching. Allow override of scope.

**Do NOT delegate this step.** Building the framing requires conversation with the user.

## Step 2 — Dispatch the systems-analyst subagent (this conversation)

Invoke the `alex:systems-analyst` subagent via the Task tool with `subagent_type: "alex:systems-analyst"`. The dispatch prompt must include:

- The bounded problem statement from Step 1
- All artifact paths/URLs the analyst should read
- Horizon scope (or "no horizon framework defined" if the project has none)
- The user's stated success criteria
- An explicit instruction to walk all eight phases — do not skip even if a phase produces a thin result (thin results are findings).

The analyst is a synthesis-only subagent — it reads, walks the phases, returns markdown. It does NOT dispatch further subagents.

**Wait for the analyst to return before continuing.** If the return is thin or skips phases, re-invoke once with a sharper framing — do not stitch a partial diagnostic in the parent thread.

## Step 3 — Present the diagnostic (this conversation)

When the analyst returns:

1. **Surface the recommendation up top** — one line, with confidence percentage and what would falsify the analysis. Don't bury the actionable bit under the eight phases.
2. **Show the horizon view verbatim** if the project has a horizon framework — the user prioritizes by horizon.
3. **Flag any archetype match with high confidence** — these are the system traps. Name the archetype and its canonical escape.
4. **Identify the highest-leverage intervention** — quote it from the diagnostic.
5. **Surface posture-check items** — what the analyst said it might be wrong about, what would warrant more evidence.
6. **Present the full diagnostic in collapsed form** if appropriate — the user can expand for full eight-phase detail.

## Step 4 — Decide and route (this conversation, with the user)

After the user reads the diagnostic, ask which of the following applies:

a. **Save the artifact.** Write the full diagnostic to a project-conventional artifacts path (e.g., `.claude/artifacts/systems-analyst-<slug>-<YYYY-MM-DD>.md`). Default = yes when the analysis surfaces a high-confidence archetype match OR a recommendation the user agrees with.

b. **Open tracker issue(s) for the recommended interventions.** If the project uses Linear, GitHub Issues, Jira, etc., create issue(s) with priority mapped from the horizon (near-term → High, mid-term → Medium, long-term → Low). Link back to the saved artifact. Default = yes when the recommendation is actionable in <2 weeks AND the user confirms intent to execute.

c. **Update project-level docs** (CLAUDE.md, README, etc.) if the diagnostic changes a project-level invariant (e.g., a new gotcha, a structural rule, a deprecated pattern). Default = ask the user explicitly before editing project docs.

d. **Run a follow-on workflow.** Examples:
   - If the diagnostic recommends a build → invoke `alex:head-of-product-engineering` Discovery phase
   - If the diagnostic surfaces a structural issue with a specific pipeline → revisit project-level proposals or roadmaps
   - If the diagnostic identifies a missing measurement → propose the metric in conversation, don't auto-create

e. **Park the diagnostic.** Default when posture-check confidence is below 60% or the recommendation is "wait for more signal." Save the artifact anyway so the framing is preserved.

## Step 5 — Optional: chain into another skill

If this skill was invoked as a pre-step inside a larger workflow (e.g., an orchestrator flagged a high-stakes decision where structural framing matters), return the diagnostic to that workflow as additional context. Do NOT auto-trigger other workflows from this skill; chaining is upstream's choice.

---

## Anti-patterns

- **Don't dispatch the analyst on a malformed problem statement.** "Things feel off" is not a problem statement — ask one clarifying question first.
- **Don't summarize the analyst's diagnostic into a one-paragraph TL;DR that drops the posture-check.** The posture-check is where the analysis becomes actionable; keep it.
- **Don't auto-create tracker issues from paradigm-level recommendations.** Paradigm-level work is almost always premature. Park it explicitly.
- **Don't use this skill for single-step tactical asks.** If the answer is obvious, the systems analysis is overhead. Trust the question filter in the agent definition.

## Known gotchas

- **Subagent registries can be session-frozen in some Claude Code environments.** Edits to `agents/systems-analyst.md` mid-conversation may not be picked up until a fresh session. Validate any analyst changes in a fresh conversation.
- **The analyst reads the `alex:systems-thinking` skill's references.** Edits to those reference files may require a fresh conversation to land in the analyst's loaded context.
- **Horizon framing is project-specific.** If your project doesn't define a horizon framework (H1/H2/H3 or equivalent), the analyst will omit that section rather than fabricate one.

## Related skills + agents

- `alex:systems-thinking` — the methodology this skill operationalizes (referenced by the analyst)
- `alex:systems-analyst` (agent) — the subagent this skill dispatches for the eight-phase walk
- `alex:head-of-product-engineering` — may call this skill during Discovery / Prioritization phases
