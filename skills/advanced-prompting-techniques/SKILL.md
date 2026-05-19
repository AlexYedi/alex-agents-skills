---
name: advanced-prompting-techniques
description: >
  Apply advanced prompting techniques beyond basic instructions: Chain-of-Thought,
  Self-Consistency, Tree-of-Thoughts, Constrained Sampling, and modular prompt
  engineering. Use when basic prompts hit a quality ceiling, when reasoning
  tasks need step-by-step thinking, when output format must be guaranteed, or
  when designing prompts as composable modules. Triggers: "improve my prompt
  reasoning", "Chain-of-Thought for X", "force JSON output", "Tree-of-Thoughts",
  "self-consistency check", "modular prompt design". Produces concrete prompting
  strategy with technique selection and prompt template.
---

# Advanced Prompting Techniques

You apply prompting beyond basic instructions to improve reasoning, output
reliability, and quality. Most teams stop at "give the model an instruction"
and miss the techniques that 5-10x performance on hard tasks.

---

## When to Use This Skill

- Basic prompts hit a quality ceiling on reasoning-heavy tasks
- Output format must be guaranteed (JSON, structured data)
- Need to reduce randomness in repeated runs
- Designing prompts as composable modules across an application
- Selecting between Chain-of-Thought variants

---

## The Modular Prompt Framework

Treat every prompt as composed of these components. Tune each independently.

| Component | What it does | Example |
|---|---|---|
| **Persona** | Role the model should adopt | "You are a senior incident responder." |
| **Instruction** | The specific task | "Triage this alert and recommend next steps." |
| **Context** | Background needed for the task | Recent on-call notes, system topology |
| **Format** | Structure of the output | "Return JSON with fields: severity, root_cause_hypothesis, next_steps[]" |
| **Audience** | Who reads the output | "Output for an engineer who was just paged at 3am" |
| **Tone** | Voice characteristics | "Direct, no preamble, action-oriented" |
| **Data** | Inputs the task operates on | The alert text, logs, metrics |
| **Examples** (few-shot) | Concrete demonstrations | 2-3 input/output pairs |

### Why Modular?

When a prompt fails, you can fix the broken component without rewriting the
whole thing. You can also reuse strong components across prompts.

---

## Chain-of-Thought (CoT)

Force the model to reason explicitly before answering. Massively improves
performance on multi-step reasoning.

### Variants

| Variant | When to use | Cost |
|---|---|---|
| **Zero-Shot CoT** | "Let's think step by step" appended to prompt | Free |
| **Few-Shot CoT** | Provide reasoning examples in the prompt | Higher token cost, better quality |
| **Auto-CoT** | Generate reasoning examples programmatically | One-time setup |

**Default:** Zero-shot CoT for any reasoning task. Add few-shot examples if accuracy is still insufficient.

---

## Self-Consistency

Sample the same prompt N times with temperature > 0, then majority-vote the
final answer.

| When | Why |
|---|---|
| Tasks with discrete answers (math, classification, code generation) | Reduces variance from sampling randomness |
| Stakes are high enough to justify N× cost | 3-5 samples is typical sweet spot |

**Key tradeoff:** N× cost for variance reduction. Use sparingly on critical decisions.

---

## Tree-of-Thoughts (ToT)

Explore multiple reasoning paths, evaluate them, and prune low-probability branches.

| Variant | Mechanism | Use when |
|---|---|---|
| **Full ToT** | Iterative model calls; tree expansion + evaluation + pruning | Complex multi-step problems where wrong moves are costly |
| **Zero-Shot ToT** | Single prompt simulating multi-expert conversation | Lighter alternative; cheaper but less rigorous |

**Caveat:** ToT is expensive. Reserve for hard problems where CoT + Self-Consistency are insufficient.

---

## Constrained Sampling

Force output adherence to a specific format by restricting valid tokens at
generation time.

| Method | How it works |
|---|---|
| **Logit filtering** | Mask invalid tokens during sampling |
| **Grammar constraints** | Use a grammar (BNF, regex) to constrain output |
| **JSON mode** (OpenAI/Anthropic) | API-level JSON enforcement |
| **Outlines / Guidance** | Libraries that wrap constrained sampling |

**When to use:** Structured outputs that must validate (JSON, regex, enums).
Don't rely on prompt instructions alone for structured outputs at scale —
constrained sampling is the only reliable way.

---

## Principles

- **Be explicit and unambiguous.** "Score 1-5" is ambiguous. "Score 1-5 where 1=poor and 5=excellent, return only the integer" is testable.
- **Specify output format with markers.** Use clear delimiters (XML tags, code fences, specific keys) so downstream parsing is reliable.
- **Provide context, not just instructions.** Reference texts, examples, and constraints reduce hallucinations more than clever instructions.
- **Decompose complex tasks.** Break large prompts into subtasks. Each subtask is easier to optimize independently.
- **Encourage thinking when answers are non-obvious.** CoT is cheap; use it for any task where reasoning matters.
- **Treat prompts as code.** Version them. Eval them. Refactor them. Don't ship "the prompt that worked yesterday."

---

## Anti-Patterns to Avoid

### Vague Instructions

**Looks like:** "Summarize this in a helpful way."

**Why it fails:** "Helpful" is undefined; output varies wildly across runs.

**The fix:** Specify length, format, audience, and tone explicitly. Provide an example output.

### Output Format via Instruction Only

**Looks like:** "Return your answer as JSON" without constrained sampling.

**Why it fails:** Models occasionally violate format. Downstream parsers crash.

**The fix:** Use constrained sampling (JSON mode, grammar) for structured outputs. Instructions alone are insufficient at scale.

### One Giant Prompt

**Looks like:** A 2000-token prompt trying to do task analysis, planning, execution, and output formatting in one call.

**Why it fails:** Hard to debug; each subtask gets less attention; output quality degrades.

**The fix:** Decompose. Separate prompts for analysis, planning, execution, formatting. Compose them programmatically.

### Skipping CoT on Reasoning Tasks

**Looks like:** Asking a math or logic question with no "think step by step."

**Why it fails:** Model jumps to answer; reasoning is wrong; quality is poor.

**The fix:** Always add CoT for reasoning. Cost is low; quality gain is large.

---

## Decision Rules

| Condition | Action |
|---|---|
| Multi-step reasoning task | Chain-of-Thought (zero-shot first) |
| High-stakes discrete answer (math, classification) | Self-Consistency on top of CoT |
| Complex problem, wrong moves costly | Tree-of-Thoughts |
| Output must be JSON / structured | Constrained sampling, NOT just instructions |
| Output format keeps drifting | Add explicit format markers + example output |
| Prompt is failing in unclear ways | Decompose into smaller subtask prompts |
| Repeated runs vary too much | Lower temperature OR Self-Consistency with majority vote |

---

## Worked Example: Triaging Production Incidents

**Bad prompt:** "Given this alert, decide what to do."

**Good prompt (modular + CoT + constrained):**

```
Persona: You are a senior incident responder.
Instruction: Analyze the alert and produce a triage decision.

Context:
- Service topology: <embedded JSON>
- Recent on-call notes: <embedded text>
- Current SLO budget: <number>

Format: Return JSON with these keys, in this order:
  reasoning: string (your step-by-step analysis)
  severity: "P0" | "P1" | "P2" | "P3"
  root_cause_hypothesis: string
  next_steps: string[] (max 3, ranked)
  confidence: number (0-1)

Process:
1. First, restate what you observe in the alert.
2. Cross-reference with topology and recent notes.
3. Consider what could cause this pattern.
4. Decide severity based on user impact.
5. Output the JSON.

Alert: <alert text>
```

**What this does:** Decomposes the task (steps 1-5), forces reasoning before
answer, specifies format precisely, gives the model the relevant context.

---

## Gotchas

- **CoT can hide errors.** Models sometimes generate plausible-looking reasoning that's wrong. Validate critical reasoning steps independently.
- **Self-Consistency cost compounds.** N samples × T tokens per sample. Budget accordingly.
- **Constrained sampling can hurt quality.** Forcing JSON when the natural answer is prose can produce stilted outputs. Test before relying.
- **Few-shot examples can poison.** Models pattern-match strongly to examples. If examples have errors, model copies the errors.
- **Prompt versions matter.** Two prompts that look "the same" can score 10% apart. Always A/B test prompt changes against a fixed eval set.

Source: *Hands-On Large Language Models* by Jay Alammar and Maarten Grootendorst, prompt engineering chapters.
