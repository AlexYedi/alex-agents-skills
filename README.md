# alex-claude-skills

Personal Claude skills repo. Authored-only — no forks, no vendored stock Anthropic
skills. Every skill here was written for Alex's specific workflow and voice.

The repo is split by **install scope** — where the skill belongs in Claude's
discovery hierarchy:

```
alex-claude-skills/
├── user-skills/                          # Install to ~/.claude/skills/
│   ├── content-correspondent/            # Post-event content + outreach sequencing
│   ├── cto-architect/                    # Principal-level architecture + build planning
│   │   └── references/                   # ADR template, stack context, reading list
│   ├── post-event-content-generator/     # Raw event notes → DMs + posts
│   ├── the-meddpicc-enterprise-deal-desk/# Enterprise deal evaluation + business cases
│   └── winning-by-design-sales-excellence-framework/
│                                          # WbD-style playbook/journey/messaging design
│
└── project-skills/
    └── empire-state-events/              # Install to <project>/.claude/skills/
        ├── event-research/                # Calendar invite → Notion + HubSpot research
        ├── pre-event-content/             # Research brief → pre-event posts + DMs
        ├── pattern-synthesis/             # Two event briefs → two-thesis LinkedIn post
        ├── content-patterns/              # Shared pattern library (no SKILL.md here)
        │   └── two-thesis-synthesis.md    # Canonical 6-part shape + voice rules
        ├── project-ideation/              # Event topics → scored project proposals
        ├── update-voice-and-style/        # Cascade voice learnings across files
        └── update-anti-patterns/          # Manage content anti-patterns list
```

## Skill format

Every skill follows the progressive-disclosure pattern: a `SKILL.md` with YAML
frontmatter (name + description), optionally supported by a `references/` folder
for bulky context that only loads when needed. Descriptions are written to
trigger aggressively on Alex's natural phrasing — the description is the router,
not just documentation.

## Install

### User-level skills

Symlink each skill directory into `~/.claude/skills/`:

```bash
cd ~/.claude/skills
ln -s /path/to/alex-claude-skills/user-skills/cto-architect .
ln -s /path/to/alex-claude-skills/user-skills/content-correspondent .
# repeat for each
```

Or copy if you don't want the symlink:

```bash
cp -r /path/to/alex-claude-skills/user-skills/* ~/.claude/skills/
```

### Empire State project skills

These only make sense inside the Empire State Events Pipeline project (they
reference its Notion schema, HubSpot setup, and reference files). Symlink into
the project's `.claude/skills/`:

```bash
cd /path/to/Empire_State_Events_Pipeline_Take_3/.claude/skills
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/event-research .
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/pre-event-content .
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/pattern-synthesis .
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/content-patterns .
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/project-ideation .
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/update-voice-and-style .
ln -s /path/to/alex-claude-skills/project-skills/empire-state-events/update-anti-patterns .
```

## What's NOT in this repo

- **Stock Anthropic skills** (`docx`, `pdf`, `pptx`, `xlsx`, `canvas-design`,
  `skill-creator`, etc.) — they ship with Claude, no reason to version them here.
- **Plugin-provided skills** (the `data:*`, `engineering:*`, `finance:*`,
  `marketing:*`, `product-management:*`, `sales:*` suites) — installed via
  plugins, not authored.
- **Reference files that live in the project** (`content-style-guide.md`,
  `content-anti-patterns.md`, `outreach-templates.md`, `portfolio-tracker.md`) —
  these belong in the Empire State project's `.claude/references/` directory,
  not here. The skills reference them by relative path.

## Conventions

- **One skill = one directory** with `SKILL.md` at its root. Flat `.md` files
  without a directory are legacy and being migrated.
- **Frontmatter has both `name` and `description`.** The name matches the
  directory. The description is trigger-rich — list Alex's actual phrases, not
  generic use-cases.
- **Progressive disclosure for bulk.** If context exceeds ~500 lines, break it
  into `references/` subfiles and have `SKILL.md` point to them on demand.
- **Shared libraries sit alongside skills, without their own SKILL.md.** See
  `project-skills/empire-state-events/content-patterns/` for the pattern.

## Changelog

- **2026-04-19** — Initial repo. 5 user-level skills, 7 project-level skills
  (including new `pattern-synthesis` + `content-patterns/two-thesis-synthesis`).
  All flat project files migrated to directory/SKILL.md form with frontmatter.
