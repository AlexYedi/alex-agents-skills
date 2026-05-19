# Contributing to alex-agents-skills

This repo is a Claude Code plugin (`alex`). Changes here ship to every Claude Code session via the user-scope install.

## Repository layout

```
alex-agents-skills/
├── .claude-plugin/
│   ├── plugin.json          # Plugin manifest (name, version, author)
│   └── marketplace.json     # Marketplace manifest (registers the plugin)
├── skills/                  # Plugin-loaded skills. FLAT, one level deep.
│   └── <skill-name>/
│       ├── SKILL.md         # Required. Frontmatter + instructions.
│       └── references/      # Optional supporting files.
├── Product/                 # Archive — un-migrated skills (not plugin-loaded)
├── Software Development/    # Archive
├── GTM/                     # Archive
├── Data Engineering/        # Archive
├── ...                      # Other archive domains
├── Me/                      # Personal context and usage patterns
└── output/                  # Generated artifacts (gitignored where relevant)
```

Only `skills/<name>/SKILL.md` files are auto-discovered by Claude Code. Anything under domain folders is treated as documentation/source-of-truth for future migration, not a live skill.

## Adding a new skill

1. Create `skills/<kebab-name>/` (lowercase, hyphen-separated, max 64 chars).
2. Create `skills/<kebab-name>/SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   description: One sentence on what the skill does and when to use it. This is what Claude reads to decide whether to invoke it.
   ---

   # Skill title

   Body — instructions, frameworks, examples.
   ```
3. Keep the body concise. Once invoked, the full SKILL.md sits in context for the rest of the session.
4. Skill names must be unique across `skills/`. There's no nested subdirectory discovery.

## Editing an existing skill

1. Edit `skills/<name>/SKILL.md` directly.
2. Commit.
3. (Automatic if `scripts/install-git-hooks.sh` has been run — see [One-time setup](#one-time-setup).) Otherwise: run `claude plugin update alex@alex-agents-skills` to refresh the user-scope cache.
4. To preview changes without committing, run Claude Code with `--plugin-dir /Users/<you>/Documents/GitHub/alex-agents-skills` — the local copy overrides the installed cache for that session.

## One-time setup

Run once per clone of this repo:

```bash
bash scripts/install-git-hooks.sh
```

Installs a `post-commit` hook in `.git/hooks/` (local, not tracked) that runs `claude plugin update alex@alex-agents-skills` in the background after every commit. Output goes to `${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log` — check it if a commit doesn't seem to have propagated.

To remove: `rm .git/hooks/post-commit`. If you don't run the installer, the manual `claude plugin update` step in step 3 above is required.

## Naming conventions

- Skill folder name = invocation name. `skills/cto-architect/` → `alex:cto-architect`.
- The `alex:` prefix is the plugin namespace; it's added automatically.
- Avoid collisions across `skills/`. The first migration audit (YED-32) found 3 collisions (`suppression-logic`, `signal-scoring`, `outbound-plays`) under `GTM/Growth/intent-signal-orchestration/` and `GTM/Marketing/intent-signal-orchestration/`. Both umbrellas were byte-identical (Marketing was a copy of Growth from commit `7d16627`), so the Marketing umbrella was deleted and Growth is canonical. For future collisions: if byte-identical, dedupe by deleting the copy; if truly distinct, prefix with the lower-precedence umbrella name (e.g., `marketing-foo`).
- For project-specific skills, put them in `<project>/.claude/skills/<name>/`. They get a short name (no namespace) and override any same-named plugin skill.

## Adding agents and commands

Plugin-loaded:
- `agents/<name>.md` at repo root — plugin agents. Each file must have YAML frontmatter with `name` + `description`. List the path in `.claude-plugin/plugin.json` under the `agents` array. Invoke via the Task tool with `subagent_type: alex:<agent-name>`.
- `commands/<name>.md` at repo root — plugin commands (deprecated by Anthropic; prefer skills).

`agents/` currently holds 5 agents migrated in YED-33 from loose `*-prompt.md` files: `cto-principal-architect`, `head-of-product`, `learning-coach-mentor`, `research-analyst`, `content-correspondent`. One known un-migrated prompt remains at `GTM/Sales/sales-operations/sales-strategy-consultant-prompt.md`; it lives inside an umbrella skill folder and will be promoted as part of the YED-34 umbrella audit.

## Migration policy (resolves drift from YED-25)

The "frozen forks" pattern from YED-25 — copying skills into individual project repos — is replaced by:

1. **One source of truth**: `skills/<name>/SKILL.md` in this repo.
2. **One distribution mechanism**: the `alex` plugin, installed at user scope.
3. **Project-local overrides allowed**: each project can keep skills in its own `.claude/skills/` that take precedence over the plugin version for that project only.

When porting a skill that lives both here and in a project repo, treat this repo as canonical. If a project version has diverged in ways that should be universal, port the changes back here and remove the project-local copy.

## Releasing a new version

1. Edit `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` — bump `version`.
2. Commit.
3. (Optional) `claude plugin tag` to create a `alex--v<version>` git tag.
4. Anyone with the plugin installed runs `claude plugin update alex@alex-agents-skills`.

## What does NOT belong in `skills/`

- Reference material that isn't an action skill — put it in domain folders or inside the skill's own `references/` subdir.
- Project-specific skills (Empire State, gtm-os, job-hunt-system) — they live in the project's `.claude/skills/`.
- Agent prompt files — they go in `agents/` (not yet present in this repo).
- Slash commands — they go in `commands/` (deprecated; convert to a skill).

## Migration backlog

Migration is happening in waves under YED-31.

- **MVP (YED-28)** — 15 skills migrated on 2026-05-15.
- **Wave 2a — Product (YED-31)** — 23 skills migrated on 2026-05-19: 18 standalone Product skills plus 5 sub-skills promoted out of the `product-launch-orchestration` and `product-led-growth` umbrellas (`war-room-ops`, `usage-health-scorecard`, `in-app-messaging-kit`, `onboarding-blueprint`, `pql-framework`). The umbrellas' `agents/` and `commands/` subdirs are out of scope for YED-31 and remain pending under YED-34.
- **Wave 2b — Software Development** — pending (~40 skills).
- **Wave 2c — GTM** — pending (~80 skills).
- **Wave 2d — Data Engineering** — pending (~20 skills).
- **Wave 2e — Long tail** — pending (Evals/Harness/Observability, Organizational Leadership, Research/Financial Modeling).

`Product/references/` is shared reference material (Decision_Intelligence, Jobs_to_be_Done, building-ai-powered-products) that the migrated skills still draw from; it stays under `Product/` pending a later decision on whether to move it under each skill's local `references/`.
