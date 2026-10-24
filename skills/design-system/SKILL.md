---
name: design-system
description: Use this skill to generate or audit design systems, check visual consistency, review PRs that touch styling, and decide when to invest in a design system and how to drive its adoption.
origin: ECC
---

# Design System — Generate & Audit Visual Systems

## When to Use

- Starting a new project that needs a design system
- Auditing an existing codebase for visual consistency
- Before a redesign — understand what you have
- When the UI looks "off" but you can't pinpoint why
- Reviewing PRs that touch styling

## How It Works

### Mode 1: Generate Design System

Analyzes your codebase and generates a cohesive design system:

```
1. Scan CSS/Tailwind/styled-components for existing patterns
2. Extract: colors, typography, spacing, border-radius, shadows, breakpoints
3. Research 3 competitor sites for inspiration (via browser MCP)
4. Propose a design token set (JSON + CSS custom properties)
5. Generate DESIGN.md with rationale for each decision
6. Create an interactive HTML preview page (self-contained, no deps)
```

Output: `DESIGN.md` + `design-tokens.json` + `design-preview.html`

### Mode 2: Visual Audit

Scores your UI across 10 dimensions (0-10 each):

```
1. Color consistency — are you using your palette or random hex values?
2. Typography hierarchy — clear h1 > h2 > h3 > body > caption?
3. Spacing rhythm — consistent scale (4px/8px/16px) or arbitrary?
4. Component consistency — do similar elements look similar?
5. Responsive behavior — fluid or broken at breakpoints?
6. Dark mode — complete or half-done?
7. Animation — purposeful or gratuitous?
8. Accessibility — contrast ratios, focus states, touch targets
9. Information density — cluttered or clean?
10. Polish — hover states, transitions, loading states, empty states
```

Each dimension gets a score, specific examples, and a fix with exact file:line.

### Mode 3: AI Slop Detection

Identifies generic AI-generated design patterns:

```
- Gratuitous gradients on everything
- Purple-to-blue defaults
- "Glass morphism" cards with no purpose
- Rounded corners on things that shouldn't be rounded
- Excessive animations on scroll
- Generic hero with centered text over stock gradient
- Sans-serif font stack with no personality
```

## Examples

**Generate for a SaaS app:**
```
/design-system generate --style minimal --palette earth-tones
```

**Audit existing UI:**
```
/design-system audit --url http://localhost:3000 --pages / /pricing /docs
```

**Check for AI slop:**
```
/design-system slop-check
```

## Strategy: when to invest, how to drive adoption

Generating and auditing are the production layer. Before either, decide whether the team needs a system yet and how it will get adopted.

### Core Principles

#### Separate concept from production
Bob Baxley: "Once we locked down on the block frames, we could send it to an agency and they could do the full high-res comps in a day, because they knew exactly what they were doing." Use low-fidelity 'block brain diagrams' to lock down conceptual logic, then apply the design system for rapid high-fidelity output.

#### Design systems drive enterprise expansion
Claire Butler: "Design systems are one of the main reasons you upgrade from pro to org or enterprise. That became just the key thing we leaned in on." Design systems practitioners are key internal champions for organizational scaling.

#### Assets should teach their own usage
Jessica Hische: "My goal always when designing a logo is to design a logo that's so easy to use that you don't have to be an extremely skilled designer to design well with it." Design assets that 'teach' the user how to apply them through their inherent structure, prioritizing ease of use over complexity.

#### Flat design is evolving
Brian Chesky: "I think flat design is over or ending. We're going to move back into a world with color, texture, dimensionality, more haptic feedback." Interface design is shifting from flat aesthetics to more dimensional, tactile, and AI-enhanced experiences.

### Questions to Help Users

- "What's the biggest inconsistency problem you're facing today?"
- "Who will be using this design system - designers only, or engineers too?"
- "How will you measure adoption and success of the design system?"
- "Do you have the resources to maintain and evolve the system over time?"
- "What's the smallest viable version you could ship first?"

### Common Mistakes to Flag

- **Building too early** - Creating a design system before you have enough patterns to systematize
- **Over-engineering** - Building complex systems that require expert designers to use correctly
- **No ownership** - Creating a design system without dedicated resources to maintain it
- **Ignoring adoption** - Building a beautiful system that no one actually uses
- **Static systems** - Treating the design system as 'done' rather than continuously evolving

For all 4 insights from 4 guests, see `references/guest-insights.md`.
