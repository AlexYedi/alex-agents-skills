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
15 skills migrated: systems-thinking, head-of-product-engineering, cto-architect, writing-prds, shipping-products, defining-product-vision, prioritizing-roadmap, ai-product-strategy, brand-storytelling, conducting-user-interviews, writing-north-star-metrics, karpathy-coder, risk-playbooks, launch-tiering, iterative-engineering-practices. Remaining ~205 skills stay in domain folders pending follow-up migration.
