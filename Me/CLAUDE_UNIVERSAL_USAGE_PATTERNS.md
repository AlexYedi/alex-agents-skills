# Universal usage patterns — deep reference

This document is the **deep reference** for how `alex-agents-skills` (the plugin) and the user-scope discipline hooks work in practice. It complements but does not replace:

- **`Me/canonical-claude-md.md`** — the canonical CLAUDE.md fragment with the 6 invariant blocks (source-of-truth, build-better-not-faster, event-triggered habits, skill-bundling, communication rules, behavioral rules). Every project's CLAUDE.md should import that file via `@~/Documents/GitHub/alex-agents-skills/Me/canonical-claude-md.md`.

If you only need the rules a new project should inherit, start with the canonical fragment. This file is for the operational details — editing flows, adding new hooks, plugin internals.

## How alex-agents-skills reaches every project (YED-28)

This repo is a Claude Code plugin. It loads automatically in every session.

- Plugin name: `alex`. Skills are invoked as `alex:<skill-name>` (e.g., `alex:systems-thinking`).
- Source of truth: `skills/<name>/SKILL.md` at this repo root. Domain folders (`Product/`, `Software Development/`, `GTM/`, etc.) hold the un-migrated archive — they are NOT loaded by the plugin.
- Installed at user scope. See `~/.claude/plugins/installed_plugins.json`.
- Project-local skills (`<project>/.claude/skills/<name>/`) and plugin skills are namespaced separately, so they coexist without conflict. Project-local takes the short name (`event-research`); plugin takes the namespaced name (`alex:cto-architect`).

### Editing skills
1. Edit `skills/<name>/SKILL.md` in this repo.
2. Commit. The YED-35 post-commit hook runs `claude plugin update alex@alex-agents-skills` automatically.
3. For active editing without committing, run Claude Code with `--plugin-dir /path/to/alex-agents-skills`. The local copy overrides the installed cache for that session.

### Adding a new skill
1. Create `skills/<kebab-name>/SKILL.md` with frontmatter `description: <when to use it>`.
2. Keep names unique across `skills/` — no nested subdirectories under `skills/` are discovered.
3. Commit; post-commit hook refreshes the user-scope cache.

### Plugin scope (as of YED-31, 2026-05-20)
256 skills migrated into `skills/<name>/SKILL.md` form across 5 waves. See `CONTRIBUTING.md` for the wave-by-wave breakdown and any remaining residue.

### Plugin agents (YED-33)
5 agents bundled with the plugin and invocable via the Agent tool with `subagent_type: alex:<name>`: `cto-principal-architect`, `head-of-product`, `learning-coach-mentor`, `research-analyst`, `content-correspondent`. Each was promoted from a loose `*-prompt.md` file. See `agents/` and `CONTRIBUTING.md` "Adding agents and commands".

## Universal discipline hooks (YED-29)

User-scope hooks fire in every Claude Code session, in every project, automatically. They live at `~/.claude/hooks/` and are registered in `~/.claude/settings.json`.

### What fires

| Hook | Event | Behavior |
|---|---|---|
| `linear-priorities.sh` | SessionStart | Pulls up to 5 open Medium+ priority Linear issues, formats as markdown, injects at session start. Graceful-fallback if `LINEAR_API_KEY` not set. |
| `repo-touch-tally.sh` | PostToolUse (Edit/Write) | Silently counts edits under `.claude/{skills,agents,commands,proposals}/` per session, per project. |
| `repo-touch-remind.sh` | Stop | If the tally > 0, emits a reminder to reconcile with Linear (open issue / comment / acknowledge doc-only). |

### Disable / opt out

Add `"hooks": {"disable": ["<hook-name>"]}` to either:
- `.claude/settings.local.json` in a project — disables for that project only
- `~/.claude/settings.local.json` — disables for every project

Hook names: `linear-priorities`, `repo-touch-nudge`.

### Project-scope hooks coexist

Per-project `.claude/settings.json` can register additional hooks that fire alongside the universal ones. Empire State keeps `v2-trigger-detect.sh` + `v2-trigger-log.sh` at project scope because the v2 triggers are pipeline-specific. Stop-event hooks from both layers fire; their `additionalContext` outputs concatenate.

### Adding a new universal hook

1. Drop script into `~/.claude/hooks/`, chmod +x.
2. Register in `~/.claude/settings.json` under the relevant event.
3. Use `$HOME/.claude/hooks/<name>.sh` in the `command` field (env var expansion works).
4. Honor both `.claude/settings.local.json` and `~/.claude/settings.local.json` `hooks.disable[]` overrides.
5. Use relative paths (`.claude/.state/`) for per-project state so each project gets isolated bookkeeping.

## Three-layer architecture (durable framing)

| Layer | What it does | Where it lives |
|---|---|---|
| **A. Distribution** | Skills/agents/commands ship to projects | `alex-agents-skills` as a Claude Code plugin — YED-28 (MVP) + YED-31 (256 skills, shipped 2026-05-20) |
| **B. Discipline** | Cross-project invariants (Linear source of truth, event-triggered habits) | User-scope hooks at `~/.claude/hooks/` — YED-29 |
| **C. Workspace** | Project-specific overlays inherit canonical defaults | `Me/canonical-claude-md.md` (imported by every project's CLAUDE.md) + `Me/starter-kit/` (new-project scaffolding) — YED-30 |

The whole arc ends with: starting any new project = inheriting all of Alex's accumulated discipline + skill conventions automatically.
