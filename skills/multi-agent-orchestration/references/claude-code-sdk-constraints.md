# Claude Code SDK constraints — the rules that govern agent/command design

Three durable, non-obvious runtime constraints of the Claude Code harness. They are not configurable —
design around them. Consolidated from hard-won project experience; consumed by anyone building
multi-agent workflows, subagents, or slash commands.

## 1. Subagents cannot spawn other subagents

The `Agent` tool (formerly `Task` — renamed ~v2.1.63; both names alias) is **not exposed inside a
subagent's context**. It exists by design, to prevent runaway nesting.

- **Official docs** ([sub-agents](https://code.claude.com/docs/en/sub-agents.md)): *"Subagents cannot
  spawn other subagents. If your workflow requires nested delegation, use Skills or chain subagents from
  the main conversation."*
- **Empirically confirmed:** across a parent + 5 subagents, `Agent`/`Task` was absent from every
  subagent's tool surface — both directly and via `ToolSearch select:Task,Agent` ("No matching deferred
  tools found").

**Implication — the orchestrator anti-pattern.** Any fan-out to specialists must run from the **parent
thread** (the slash-command's main conversation), *not* from inside a "lead/orchestrator" subagent. A
design that says "agent X orchestrates the others" is wrong and will silently fail to dispatch. What DOES
work as a subagent: **synthesis-only** agents (text in → text out, no dispatch). The reliable shape is:
*parent fans out N specialists in parallel → collects their returns → hands them to one synthesis-only
subagent (or synthesizes inline).*

## 2. The agent registry is session-frozen

The harness loads the list of available agents from `.claude/agents/**/*.md` **once, at conversation
start**, and uses that snapshot for the whole session. Adding, editing, deleting, or renaming an agent
file mid-conversation is written to disk but **not** reflected in the live registry.

- Confirmed: after deleting agent A and creating agent B mid-session, the runtime still listed A and could
  not find B (or any newly-named agent).
- **Validation rule:** any change to a `.claude/agents/` file (frontmatter, body, model, tools, name)
  requires a **fresh conversation** to test. You cannot smoke-test an agent change in the same session
  that made it. (Same root cause as the general "custom-agent discoverability mid-conversation is
  unreliable" gotcha — but it applies to *all* agent-definition changes, not just new ones.)

## 3. Give every subagent an explicit, minimal `tools:` frontmatter line

A subagent with **no** `tools:` line inherits the parent's full deferred tool list (which can be ~250
tools). Under a smaller model's context window (e.g. Haiku), the harness pre-flight check can then reject
the invocation before the agent even runs — the failure looks like `"Prompt is too long"` with
`total_tokens: 0, tool_uses: 0`.

**Rule:** every subagent in `.claude/agents/` declares an explicit `tools:` line scoped to the minimum it
needs. This prevents context bloat **and** makes the agent's contract reviewable at a glance. Examples:
a research specialist → `tools: WebSearch, WebFetch, Read`; a synthesis-only agent → `tools: Read`; a
systems analyst → `tools: Read, Bash, WebSearch, WebFetch, Grep, Glob`.

---

**See also:** `orchestration-authoring-skeleton.md` (this dir) — how to encode a fan-out in a command/skill
file so it respects constraint #1.
