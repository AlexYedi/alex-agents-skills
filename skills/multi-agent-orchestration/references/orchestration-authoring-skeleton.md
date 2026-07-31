# Orchestration authoring skeleton

The required shape for any **runnable orchestration** — a slash command or an orchestrating skill that
dispatches subagents. It exists because the common failure mode is a *thin declarative* file: one that
*names* agents but ships no orchestration (no dispatch order, no parallel/serial control, no output
destination, no failure modes). A user running that gets nothing deterministic — it's a spec, not a
runnable thing.

**The orchestration file IS the orchestration.** The *methodology* (what "good" looks like) belongs in a
SKILL.md or agent definition; the *orchestrator* says **who runs, in what order, with what input, and where
the result lands.** Medium-agnostic: the skeleton is the same whether the entry point is a command or a
skill.

## The skeleton — each step is load-bearing

1. **Intake & validate (parent thread — never a subagent).** Enumerate every input, mark which are
   required, and **refuse to proceed if a required one is missing** (ask, don't guess). Carry any pasted
   source as a `VERBATIM SOURCE` block, unchanged, into every dispatch. If the flow dedups/persists, do the
   **dedup read here** so later writes upsert, not duplicate.
2. **Dispatch / fan-out (parent thread, explicit).** State exactly which agents run, **in parallel or
   serially**, and *why*. Parallel = independent `Agent` calls **in one message**. Each dispatch leads with
   the verbatim source + a one-line framing of what that specialist returns. **Hard SDK constraint:**
   subagents can't spawn subagents — the fan-out lives in the parent, not in a "lead" agent (see
   `claude-code-sdk-constraints.md`).
3. **Collect & handle thin returns.** Wait for all dispatched agents. If one returns thin, **re-invoke just
   that one** with deeper scope — don't restart the whole run.
4. **Synthesize (a synthesis-only subagent, or inline).** One agent (text-in/text-out, no dispatch, no MCP)
   assembles the deliverable to a named structure, OR synthesize inline in the parent. Say which.
5. **Quality gate (advisory) — only if the output is quality-graded.** Score against a named rubric,
   per-criterion + composite; **advisory** (never hard-block). Omit for outputs that aren't graded — don't
   add ceremony.
6. **Output destination — NAME IT.** Every orchestrator states where the result lands and how: the
   **conversation** (the honest lean default for analysis/briefs — don't invent a write); a **deck/visual
   generator**; a **system-of-record** (e.g. Notion/CRM) for artifacts that enter a review loop — and if so,
   remember MCP writes happen in the **parent thread**, not a subagent. **Do not promise a write the file
   doesn't perform** — fabricated specificity is an anti-pattern.
7. **Failure modes.** At minimum: a required input missing; a specialist returns thin/empty; an external
   dependency (MCP/API/key) unavailable. Say what happens in each case — **degrade, don't crash.**

## Conventions
- **Frontmatter:** `description` (required) + `argument-hint`. Reference plugin skills by their invocation
  prefix (e.g. `alex:message-architecture`), not the bare name.
- **Scaffold ≠ shipped.** An orchestrator with dispatch deferred is a **draft** — mark it `DRAFT` / keep it
  out of the runnable set until steps 1–7 are real (or explicitly N/A-with-reason).
- **Completeness is judged against this skeleton.** A file that lists agents without dispatch/collect/output
  logic **fails** completeness — it is not "done."
