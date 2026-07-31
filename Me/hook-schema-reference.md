# Claude Code Hook Schema Reference

> Read this BEFORE writing a new hook. The output schema is **event-specific** and not obvious from copying
> one event type's example to another. Universal reference — applies to user-scope hooks (`~/.claude/hooks/`)
> and project-scope hooks (`<project>/.claude/hooks/`) alike.
>
> Authoritative source: Claude Code's hook validator. The error messages it returns are accurate — trust
> them over docs that may have drifted.

---

## Event types + supported output

Hooks fire on one of these events. Each event has a different supported output schema. **You cannot
mix-and-match across events.**

| Event | Supports `hookSpecificOutput.additionalContext`? | Where the output goes | Typical use |
|---|---|---|---|
| `SessionStart` | ✅ YES | Injected into Claude's context as a system reminder | Pre-load priorities, project state, env warnings |
| `UserPromptSubmit` | ✅ YES | Injected into Claude's context for that turn | Auto-suggest skills, inject relevant docs, log prompts |
| `PostToolUse` | ✅ YES (optional) | Injected into Claude's context after the tool call | Append context after specific tools fire |
| `PostToolBatch` | ✅ YES (optional) | Injected into Claude's context after a batch | Same as PostToolUse but for batched calls |
| `PreToolUse` | ❌ NO — uses `permissionDecision` instead | Gates the tool call (allow/deny/ask/defer) | Guard rails on specific tools |
| `Stop` | ❌ NO — use top-level `systemMessage` | Displayed to the user in their terminal at session end | End-of-session prompts, reminders, summaries |

---

## Top-level output fields (work on ANY event)

These fields appear at the JSON root, NOT nested under `hookSpecificOutput`:

| Field | Type | Used by | Effect |
|---|---|---|---|
| `continue` | boolean | any | Lets Claude continue normally if false-ish blocks |
| `suppressOutput` | boolean | any | Hides the hook's stdout from the user |
| `stopReason` | string | Stop | Reason text shown when Claude stops |
| `decision` | `"approve"` \| `"block"` | PreToolUse / Stop | Approves or blocks the action |
| `reason` | string | accompanies `decision` | Why the decision was made |
| `systemMessage` | string | **Stop hooks** + any event that wants a user-visible message | Displayed to the user in their terminal |
| `terminalSequence` | string | any | Raw terminal escape sequence to emit |
| `permissionDecision` | `"allow"` \| `"deny"` \| `"ask"` | PreToolUse | Permission gate for the tool |

---

## The two gotchas that motivate this card

### Gotcha 1 — Stop hooks cannot use `additionalContext`

A Stop hook that emits:
```json
{"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": "..."}}
```
**fails schema validation.** Stop hooks support only the top-level fields (`systemMessage`, `stopReason`,
etc.) — there is no `hookSpecificOutput` schema entry for Stop at all.

**Fix:** emit `{"systemMessage": "..."}` at the top level. The text displays in the user's terminal at
session end, which is what such a hook wants anyway.

The misleading pattern: a SessionStart hook (e.g. `linear-priorities.sh`) uses
`hookSpecificOutput.additionalContext` correctly. Copy-pasting that pattern to a Stop hook silently breaks
until the schema validator catches it. **When two hook layers both fire on Stop, it is their `systemMessage`
outputs that concatenate — not `additionalContext`.**

### Gotcha 2 — `additionalContext` is invisible to the user in the terminal

`additionalContext` (on SessionStart / UserPromptSubmit / PostToolUse / PostToolBatch) injects into
**Claude's context window** — not the user's terminal. Claude sees it; the user doesn't (unless Claude reads
it back).

If you want the user to see something in their terminal:
- For Stop events → use `systemMessage`.
- For SessionStart events → there's no clean "show in terminal" path; either `echo >&2` from the hook script
  (visible in the terminal as the hook runs) or have Claude reference the context proactively.

For session-start in particular, the trick that works:
```bash
# Print to stderr (visible in terminal before Claude responds)
echo "## Priorities" >&2
cat priorities.txt >&2

# Also emit JSON for Claude's context
printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":%s}}\n' "$ESCAPED"
```

---

## Disable pattern

Every hook should respect a disable flag in `.claude/settings.local.json`. Standard shape:

```json
{
  "hooks": {
    "disable": ["hook-name-1", "hook-name-2"]
  }
}
```

Hook script preamble:
```bash
SETTINGS_LOCAL=".claude/settings.local.json"
if [ -f "$SETTINGS_LOCAL" ]; then
  if jq -e '.hooks.disable | index("hook-name")' "$SETTINGS_LOCAL" >/dev/null 2>&1; then
    exit 0
  fi
fi
```

For user-scoped hooks, also check `$HOME/.claude/settings.local.json` for the same flag.

---

## Debugging a hook

1. **Read the schema validation error verbatim.** It lists the expected schema and shows your actual
   output. The diff is usually obvious once you compare.
2. **Run the hook script manually** with sample input piped in:
   ```bash
   echo '{"session_id":"test","prompt":"test"}' | bash ~/.claude/hooks/your-hook.sh
   ```
   Check stdout (the JSON output) and stderr (any errors).
3. **Validate the JSON** with `jq`: `bash ~/.claude/hooks/your-hook.sh | jq .` — if `jq` errors, your JSON
   is malformed.
4. **Check for `set -e` traps.** With `set -e` / `set -euo pipefail`, a partial failure mid-script can exit
   before emitting JSON, leaving the harness with empty stdout (also a schema error).

---

## Quick decision tree

> "I want to..."

- **...show text in the user's terminal at session start** → SessionStart hook + `echo >&2` (the
  `additionalContext` is for Claude, not the user)
- **...inject context into Claude's view at session start** → SessionStart hook +
  `hookSpecificOutput.additionalContext`
- **...show a prompt/reminder to the user when they finish a session** → Stop hook + `systemMessage`
- **...let Claude see something after a specific tool call fires** → PostToolUse hook +
  `hookSpecificOutput.additionalContext`
- **...gate or block a tool call** → PreToolUse hook + `permissionDecision`
- **...add per-turn context to Claude based on what the user typed** → UserPromptSubmit hook +
  `hookSpecificOutput.additionalContext`

When writing a new hook, start by copying the one whose **event type matches yours** — not whose use case
looks similar. Event type determines the schema; use case is secondary.
