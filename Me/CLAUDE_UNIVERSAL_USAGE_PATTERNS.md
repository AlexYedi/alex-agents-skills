# How I work

## Roles
I operate as CTO (architecture/strategy) and IC (building).
"Build X" = write production-ready code and deploy it.
"Plan X" = help me think through architecture first.

## Communication
- Lead with the decision, then reasoning
- Flag blockers immediately, don't bury them
- Be direct. If something won't work, say so and propose the alternative
- Short responses for tactical work

## Code standards
- Never put secrets in code files — keys in .env or native UI only
- Write complete files, never partial snippets
- Validate against the actual API contract before writing requests
- Check the real schema before assuming column names

## Workflow
- Check the Linear issue before building
- Update Linear status when Done
- New n8n workflows = new files, never bolt onto existing ones

## Stack I use everywhere
n8n · Supabase · Claude API · Linear · Cursor · Gmail · Google Calendar
Full stack details always live in STACK_README.md at the repo root.

## How alex-agents-skills reaches every project (YED-28)

This repo is a Claude Code plugin. It loads automatically in every session.

- Plugin name: `alex`. Skills are invoked as `alex:<skill-name>` (e.g., `alex:systems-thinking`).
- Source of truth: `skills/<name>/SKILL.md` at this repo root. Domain folders (`Product/`, `Software Development/`, `GTM/`, etc.) hold the un-migrated archive — they are NOT loaded by the plugin.
- Installed at user scope. See `~/.claude/plugins/installed_plugins.json`.
- Project-local skills (`<project>/.claude/skills/<name>/`) and plugin skills are namespaced separately, so they coexist without conflict. Project-local takes the short name (`event-research`); plugin takes the namespaced name (`alex:cto-architect`).

### Editing skills
1. Edit `skills/<name>/SKILL.md` in this repo.
2. Commit.
3. `claude plugin update alex@alex-agents-skills` — refreshes the user-scope cache to your latest commit.
4. For active editing without committing, run Claude Code with `--plugin-dir /path/to/alex-agents-skills`. The local copy overrides the installed cache for that session.

### Adding a new skill
1. Create `skills/<kebab-name>/SKILL.md` with frontmatter `description: <when to use it>`.
2. Keep names unique across `skills/` — no nested subdirectories under `skills/` are discovered.
3. Commit, run `claude plugin update alex@alex-agents-skills`.

### MVP scope (as of YED-28)
15 skills migrated: systems-thinking, head-of-product-engineering, cto-architect, writing-prds, shipping-products, defining-product-vision, prioritizing-roadmap, ai-product-strategy, brand-storytelling, conducting-user-interviews, writing-north-star-metrics, karpathy-coder, risk-playbooks, launch-tiering, iterative-engineering-practices. Remaining ~205 skills stay in domain folders pending follow-up migration (YED-31).

### Plugin agents (YED-33)
5 agents bundled with the plugin and invocable via the Task tool with `subagent_type: alex:<name>`: `cto-principal-architect`, `head-of-product`, `learning-coach-mentor`, `research-analyst`, `content-correspondent`. Each was promoted from a loose `*-prompt.md` file. See `agents/` and `CONTRIBUTING.md` "Adding agents and commands".

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
