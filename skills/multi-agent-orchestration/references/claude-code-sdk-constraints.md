# Claude Code SDK constraints — the rules that govern agent/command design

Durable runtime facts of the Claude Code harness that shape agent and command design. **Re-verified
2026-10-15 against the live docs and changelog (v2.1.300)**: the first two rules below were platform
limits until mid-2026 and are now design choices. Re-check this file against the changelog before
relying on it.

## 1. Parent fan-out is a design choice, not a platform limit

Subagents **can** dispatch subagents, up to three levels below the main conversation
(`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, default 3 since v2.1.219; it was impossible before that). A
fork cannot spawn further forks.

**Still prefer parent fan-out for predictable workflows.** One thread then owns concurrency, ordering
and the chain, which is what Anthropic's *Building Effective Agents* recommends when the steps are
known, and what Cognition's *Don't Build Multi-Agents* argues for (context is lost at every handoff;
parallel workers make conflicting implicit decisions). The reliable shape is unchanged: *parent fans out
N specialists → collects returns → hands them to one synthesis-only agent*. Use nesting deliberately,
for genuinely dynamic delegation, and budget it (below).

**Budget every wave.** At most 20 subagents run at once per session (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`,
raisable, cannot be disabled; the 21st fails with `Concurrent subagent limit reached`). WebSearch is
capped at 200 calls per session across all subagents. Background agents are killed when the account
spend limit is reached. Stop and report on a bounce; never retry silently.

## 2. Agent files hot-reload; prove every edit with a dispatch

The harness watches `~/.claude/agents/` and `.claude/agents/` and picks up edits within seconds, with
three exceptions: the first file in a new `agents` directory, `--add-dir` directories, and
`--disable-slash-commands`. **Plugin agents refresh only when the plugin is updated** (this repo's
pull/merge hook runs the update). Rule: after any agent edit, prove it with one real dispatch before
relying on it; if it doesn't load, start a fresh conversation.

Also: a `model:` override on the `Agent` call works on every agent, including plugin agents, so choose
the agent for the job and the model separately. Plugin agents ignore `hooks`, `mcpServers` and
`permissionMode` frontmatter, so their `tools:` line is the only enforcement lever. Subagents inherit
the parent's MCP tools by default, which is why the `tools:` line below matters.

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
