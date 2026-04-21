
## Skill format

Every skill follows the progressive-disclosure pattern: a `SKILL.md` with YAML
frontmatter (name + description), optionally supported by a `references/` folder
for bulky context that only loads when needed. Descriptions are written to
trigger aggressively on Alex's natural phrasing — the description is the router,
not just documentation.

## The sales methodology stack

The five sales methodology skills are designed to compose. Rough mental model:

- **Challenger** creates the pipeline (commercial insight, reframe the problem).
- **Command of the Message** gives the persistent language (Before / PBO /
  Required Capabilities) across the motion.
- **Winning by Design** designs the motion itself (bowtie, SPICED, handoffs,
  Moments That Matter) from SDR through CSM.
- **MEDDPICC** qualifies and runs the deal (scorecard, gap list, business case,
  MAP).
- **Never Split the Difference** sharpens the late-stage conversation
  (procurement, stalled deals, price, escalation).

Each skill explicitly flags what it pairs with, conflicts with, and when to
reach for a different one instead.

## Install

### User-level skills

Symlink each skill directory into `~/.claude/skills/`:

```bash
cd ~/.claude/skills
ln -s /path/to/alex-claude-skills/user-skills/cto-architect .
ln -s /path/to/alex-claude-skills/user-skills/content-correspondent .
ln -s /path/to/alex-claude-skills/user-skills/post-event-content-generator .
ln -s /path/to/alex-claude-skills/user-skills/the-meddpicc-enterprise-deal-desk .
ln -s /path/to/alex-claude-skills/user-skills/command-of-the-message-value-framework .
ln -s /path/to/alex-claude-skills/user-skills/winning-by-design-sales-excellence-framework .
ln -s /path/to/alex-claude-skills/user-skills/the-challenger-sale .
ln -s /path/to/alex-claude-skills/user-skills/never-split-the-difference-negotiation .
