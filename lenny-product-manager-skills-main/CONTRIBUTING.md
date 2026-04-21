# Contributing to Lenny's Product Skills

Thanks for your interest in improving these skills! This guide will help you contribute effectively.

## Ways to Contribute

### 1. Fix Errors or Outdated Information
- Incorrect attributions
- Outdated frameworks
- Typos or formatting issues

### 2. Improve Existing Skills
- Add missing frameworks from podcast episodes
- Make advice more actionable and specific
- Add better diagnostic questions
- Improve the "Common Mistakes to Flag" section

### 3. Add New Skills
- Skills should be based on insights from Lenny's Podcast guests
- Must have at least 3-5 substantive principles with attribution
- Should be actionable, not just informational

## Skill File Format

Each skill lives in `skills/{skill-name}/SKILL.md`:

```markdown
---
name: skill-name
description: Help users [action verb]. Use when someone is [trigger conditions].
---

# Skill Title

Help the user [purpose] using frameworks and insights from [N] product leaders.

## How to Help

When the user asks for help with [topic]:

1. **First step** - [What to do]
2. **Second step** - [What to do]
3. **Third step** - [What to do]
4. **Fourth step** - [What to do]

## Core Principles

### Principle title
[Guest Name]: "[Direct quote or close paraphrase]" [Actionable guidance explaining how to apply this.]

### Another principle
[Guest Name]: "[Quote]" [Guidance]

## Questions to Help Users

- "[Diagnostic question]"
- "[Another question]"

## Common Mistakes to Flag

- **[Mistake pattern]** - [Why it's wrong and what to do instead]
- **[Another mistake]** - [Explanation]

## Deep Dive

For all [N] insights from [M] guests, see `references/guest-insights.md`

## Related Skills

- [Related skill 1]
- [Related skill 2]
```

## Quality Standards

### Descriptions
- Start with "Help users [verb]"
- Include specific trigger phrases: "Use when someone is..."
- Keep under 200 characters

### Principles
- Always attribute to a specific guest
- Include direct quotes where possible
- Add actionable guidance after the quote
- Aim for 5-15 principles per skill

### Questions
- Should be diagnostic, not leading
- Help Claude understand the user's specific situation
- Should be questions Claude would actually ask

### Common Mistakes
- Should be specific, observable patterns
- Include why it's problematic
- Suggest what to do instead

## Pull Request Process

1. Fork the repository
2. Create a branch: `git checkout -b improve-skill-name`
3. Make your changes
4. Test by copying to `.claude/skills/` and trying it
5. Submit a PR with:
   - What you changed
   - Why (reference podcast episode if adding new content)
   - How you tested it

## Code of Conduct

- Be respectful and constructive
- Attribute sources accurately
- Focus on actionable, practical advice
- Keep the user's success as the priority

## Questions?

Open an issue if you're unsure about anything!
