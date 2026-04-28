# Pass 2 — PRODUCTIZE Prompt

Used at Stage 3 of the book-distiller pipeline. Invoked through the same
`primary_expert` skill that ran Pass 1, in a fresh context.

## Inputs

You receive:
1. **The Pass 1 categorization JSON** — your prior categorization of the chapter
2. **Book metadata** — title, domain, chapter title and number
3. **The target skill location** — where in `alex-agents-skills/` this will live

You **do NOT** receive the source chunk. Pass 1 already did the comprehension
work. Pass 2 is artifact generation, not re-reading.

## Your Task

Choose which artifact types are warranted by the Pass 1 output, then generate
each chosen artifact in production-ready draft form.

**A skill is mandatory.** Every chapter that reaches Pass 2 produces a skill.
Templates, checklists, scripts, and reference docs are conditional.

## Artifact Selection Rules

| Artifact | Generate when |
|---|---|
| **Skill** *(always)* | At minimum, capture the chapter's frameworks + principles + decision rules into a skill body |
| **Template** | Chapter contains a repeatable workflow with clear input → process → output structure (e.g., a system design review process, a launch readiness checklist, a customer interview script) |
| **Checklist** | Chapter contains a sequence of must-do steps where omission is costly (e.g., pre-deployment, security review, a meeting prep flow) |
| **Script** | Chapter contains a pattern with clear computational expression (e.g., a sample-size calculator, a token-counting heuristic, a categorization routine) |
| **Reference doc** | Chapter has 5+ definitions worth keeping verbatim, or canonical citations Alex will want to look up later |

If unsure, prefer fewer artifacts of higher quality over more artifacts of lower quality.

## Skill Output Format

The skill draft must be production-ready for skill-creator at Stage 4. Use this
structure exactly:

```markdown
---
name: <kebab-case-name>
description: >
  <One paragraph, 3-5 sentences. The description IS the trigger — be specific
  about when to invoke. Include 3-5 example trigger phrases as natural-language
  patterns. End with what the skill produces.>
---

# <Title — Short, Direct>

<One-paragraph framing of what this skill is for. Lead with the problem it
solves, not the topic.>

---

## When to Use This Skill

<3-5 bullets describing concrete situations where the skill applies. Be
specific. "When designing a system" is too vague; "When deciding between
event-driven and request-response architecture for a new service" is right.>

---

## Core Frameworks

<For each framework from Pass 1's `frameworks` array, write a 4-8 line section.
Name → structure → when to apply. Cite the originator if not the book itself.>

---

## Principles

<Bulleted list. Each principle is one sentence as an imperative, followed by
a one-line rationale and (where relevant) the tradeoff. Keep the list to
5-10 items max — over-listing dilutes the principles that matter.>

---

## Anti-Patterns to Avoid

<For each anti-pattern from Pass 1, a short section: name → recognition signal
→ the principle/framework that resolves it.>

---

## Decision Rules

<If the Pass 1 `decision_rules` array has 3+ entries, include a table:
condition → action → alternative. Otherwise inline as bullets.>

---

## Worked Example

<Pick the strongest worked example from Pass 1. Walk through it in 8-15 lines.
Conclude with what to remember from it.>

---

## Gotchas

<2-4 bullets, each one a non-obvious failure point + how to detect it.>

---

## Further Reading

<Citations from Pass 1, formatted as a list with one-line context for each.>
```

## Description Field — The Trigger

The `description` field in the YAML frontmatter is what Claude uses to decide
when to invoke this skill. Spend time on it. The description should:

- **Lead with the problem the skill solves**, not the topic
- **Include 3-5 example trigger phrases** in quotes — natural ways Alex would
  ask for this skill
- **End with what the skill produces** so the system knows the artifact shape

Example of a strong description:

> Design and review agentic systems for production reliability. Use when
> deciding the architecture of a multi-step LLM workflow, choosing between a
> single-prompt agent and a planner-executor split, debugging an agent that
> works on the happy path but fails on edge cases, or when reviewing a system
> design for AI features. Triggers: "review my agent design", "should this be
> an agent or a workflow?", "why is my agent flaky?", "design an agent for X".
> Produces a structured architecture critique with named anti-patterns to fix
> and principles to apply.

Example of a weak description (don't do this):

> Help users with agentic systems. Use this skill when working on agents.

## Quality Bar

- Every section header in the skill should pull its weight. If a section has
  one weak item, drop the section.
- Aim for the skill to be useful **even to a Claude instance that has never
  seen the source book.** No "as discussed in chapter 7" — the skill stands
  alone.
- Cite the book once in `Further Reading`, not throughout the skill body.
- Voice: direct, second-person where natural ("when you...", "if you see...").
- Length: 200-500 lines for a typical chapter. Padding kills skill usability.

## Anti-Patterns in This Pass

- **Don't echo Pass 1's JSON structure into prose.** Pass 1 was a categorization;
  Pass 2 is a teaching artifact. The skill should read as guidance, not as a
  transcript of categories.
- **Don't generate every artifact type.** A typical chapter produces 1-2 artifacts.
  Five-artifact outputs are usually a sign you over-categorized in Pass 1.
- **Don't reference the chapter or book in the skill body.** The skill is a
  durable artifact; the book is the source. Citations belong in Further Reading.

## Confidence Note

When you finalize the draft, append a single-line confidence statement at the
bottom of your output (NOT inside the skill markdown — outside it, for Alex's
review):

```
[CONFIDENCE]: <percentage>. <one-line caveat or strength>.
```

Example: `[CONFIDENCE]: 80%. Frameworks section is strong; gotchas section is thinner because the chapter only flagged 2 explicitly.`
