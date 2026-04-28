# Pass 1 — PARSE Prompt

Used at Stage 2 of the book-distiller pipeline. Invoked through the metadata's
`primary_expert` skill (e.g. `ai-product-strategy`, `cto-architect`).

## Inputs

You receive:
1. **Source chunk** — the full chapter text (post-OCR, post-chapter-extraction)
2. **ScaleDown entity index** — pre-computed entities with confidence scores and
   500-char context windows around each entity
3. **ScaleDown digest** — a structured chapter summary (FRAMEWORKS, PRINCIPLES,
   ANTI-PATTERNS sections)
4. **Book metadata** — title, domain, chapter title and number

## Your Task

Read the source chunk through your domain-expert lens. Use the entity index as
a navigation aid (it tells you where the named concepts live in the chunk),
and the digest as a sanity check on coverage. **Do not trust the digest or
index as ground truth — read the source.**

Produce a structured categorization of every transferable idea in the chapter.

## Output Contract

Return a single JSON object with these top-level keys. Each key holds an array
of objects. Empty arrays are valid where the chapter has no instances of a
category.

```json
{
  "main_ideas": [
    {
      "claim": "<thesis-level claim, 1-2 sentences>",
      "evidence": "<how the chapter supports it>",
      "transferable_to": "<what kinds of work this applies to>"
    }
  ],
  "frameworks": [
    {
      "name": "<canonical name as used in the chapter>",
      "originator": "<author/paper if cited, else 'this book'>",
      "structure": "<the parts/components in 2-4 lines>",
      "when_to_apply": "<conditions for using this framework>",
      "source_offset": "<approximate page or section reference>"
    }
  ],
  "principles": [
    {
      "rule": "<the principle as an imperative>",
      "rationale": "<why it works>",
      "tension": "<what it trades off against, if anything>"
    }
  ],
  "anti_patterns": [
    {
      "name": "<canonical name as used in the chapter>",
      "what_it_looks_like": "<how to recognize it>",
      "why_it_fails": "<the underlying mechanism>",
      "the_fix": "<the principle or framework that resolves it>"
    }
  ],
  "decision_rules": [
    {
      "condition": "<when X is true>",
      "action": "<do Y>",
      "alternative": "<what to do otherwise>",
      "scope": "<where this rule applies>"
    }
  ],
  "mental_models": [
    {
      "analogy": "<the analogy or framing>",
      "what_it_clarifies": "<the underlying concept it makes intuitive>",
      "limits": "<where the analogy breaks down>"
    }
  ],
  "worked_examples": [
    {
      "name": "<example name or one-line summary>",
      "applies_concept": "<which framework/principle it instantiates>",
      "key_steps": ["<step 1>", "<step 2>", "..."],
      "what_makes_it_useful": "<why it's worth remembering>"
    }
  ],
  "gotchas": [
    {
      "trap": "<the non-obvious failure point>",
      "why_easy_to_miss": "<the cognitive bias or surface plausibility>",
      "detection_signal": "<what tells you you're falling into it>"
    }
  ],
  "citations": [
    {
      "reference": "<author/paper/book name>",
      "year": "<year if given>",
      "what_for": "<what idea the chapter draws from this source>"
    }
  ],
  "definitions": [
    {
      "term": "<term being defined>",
      "definition": "<the definition as given>",
      "distinguishes_from": "<related concept it's contrasted with, if any>"
    }
  ]
}
```

## Quality Bar

A category should appear in the output **only if it's named or explicit in the chapter**.
Do not infer categories. If the chapter has 1 framework and 0 anti-patterns,
return 1 framework and an empty `anti_patterns` array. Padding the output with
implicit-but-not-stated material degrades downstream artifacts.

**Trust your domain-expert judgment.** A `cto-architect`-loaded expert will see
different patterns than a `head-of-product-engineering`-loaded expert reading
the same chapter, and that's the point. The categorization reflects the lens.

## Anti-Patterns in This Pass

- **Don't paraphrase the digest.** The digest is for cross-checking coverage,
  not as input to your own categorization. Read the source.
- **Don't treat marketing-style phrases as frameworks.** "Disruptive innovation"
  used as a slogan is not a framework; "Christensen's Disruptive Innovation
  Theory" with named jobs-to-be-done structure is.
- **Don't skip the "tension" or "limits" fields.** A principle without
  knowing what it trades against is half-useful. A mental model without
  knowing where the analogy breaks is dangerous.
- **Don't merge categories.** A principle is not a framework. A decision rule
  is not a principle. Keep them clean — Pass 2 depends on the structure.

## Confidence Calibration

If uncertain whether something belongs in a category, prefer omitting it. Pass 2
amplifies what's in Pass 1. False positives at this stage become bad
recommendations in the final skill.
