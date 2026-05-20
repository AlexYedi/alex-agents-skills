# New-project starter kit

Drop-in scaffolding for any new project that should inherit Alex's accumulated discipline (Layer C — Workspace Inheritance, YED-30).

After bootstrapping, the new project automatically gets:

- **Layer A — Distribution** (from YED-28 plugin): every skill, agent, and command in `alex-agents-skills` loads via the `alex` plugin, with `alex:<name>` namespacing.
- **Layer B — Discipline** (from YED-29 user-scope hooks): Linear-priorities at session start, repo-touch nudge at session end.
- **Layer C — Workspace** (this kit): the 6 invariant CLAUDE.md blocks inherited via `@`-import, with project-specific overlays for what's unique.

## How to use this kit

### Option A — Manual copy (1 minute)

From inside the new project's root:

```bash
TARGET="$(pwd)"
SOURCE="$HOME/Documents/GitHub/alex-agents-skills/Me/starter-kit"

# 1. Copy the .claude/ scaffolding
cp -R "$SOURCE/.claude" "$TARGET/.claude"

# 2. Copy the CLAUDE.md template
cp "$SOURCE/CLAUDE.md.template" "$TARGET/CLAUDE.md"

# 3. Edit CLAUDE.md — replace {{...}} placeholders with project-specific content
$EDITOR "$TARGET/CLAUDE.md"
```

### Option B — Bootstrap script (deferred — YED-30 Step 3)

A `bootstrap.sh` will land here once Option A is battle-tested on at least one new project. The script will:

1. Take a target directory as argument
2. Copy the starter kit into the target's `.claude/`
3. Initialize CLAUDE.md from the template with prompts for project-specific fields
4. Verify the `alex` plugin is installed
5. Emit a "next steps" checklist

Until then, use Option A.

## What's in the kit

| File / Dir | Purpose |
|---|---|
| `CLAUDE.md.template` | Project CLAUDE.md skeleton. Imports `Me/canonical-claude-md.md` for the 6 invariant blocks; has `{{...}}` placeholders for project-specific overlays. |
| `.claude/settings.json.template` | Project-scope settings. The universal hooks already fire from `~/.claude/settings.json` — this file is only for project-specific hook registrations. |
| `.claude/skills/.gitkeep` | Establishes the project-local skills directory. Project-local skills with the same short name as a plugin skill take precedence. |
| `.claude/agents/.gitkeep` | Project-local agent definitions. |
| `.claude/commands/.gitkeep` | Project-local slash commands. |
| `.claude/proposals/.gitkeep` | Where to draft proposals for non-trivial work before building. |
| `.claude/artifacts/.gitkeep` | Where session outputs land (analyses, plans, reports). |

## What you do NOT need to do

- **Do not duplicate the canonical fragment's blocks into the new project's CLAUDE.md.** That's what the `@`-import is for. If you find yourself copying communication-rules or behavioral-rules into the project's CLAUDE.md, stop — they're already inherited.
- **Do not register user-scope hooks in the project's `.claude/settings.json`.** They already fire from `~/.claude/settings.json`. Only add project-scope hooks that are specific to this codebase.

## Validation

After bootstrapping, open a fresh Claude Code session in the new project and confirm:

1. The Linear priorities block appears at session start (Layer B hook firing).
2. The `alex:` namespaced skills are listed in the available skills (Layer A plugin loading).
3. CLAUDE.md's `@`-imported canonical content is visible at session start (Layer C inheritance).

If any of those fail, see `Me/CLAUDE_UNIVERSAL_USAGE_PATTERNS.md` for troubleshooting (env vars, hook disable overrides, plugin install state).

## Governance

The canonical fragment is high-leverage — changes affect every project that imports it. Changes require:

1. A Linear issue describing what changes and why.
2. A commit on `alex-agents-skills` with the issue ID in the message.
3. Spot-check at least one downstream project (Empire State or gtm-os or job-hunt-system) before merging.
