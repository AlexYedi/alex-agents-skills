# Stage 0 — SCREEN Prompt

Used at the triage stage to decide whether a chapter is worth full distillation.

## Inputs

You receive:
1. A ScaleDown digest of the chapter (~400 tokens)
2. A ScaleDown entity index (~600 tokens)
3. The chapter title and chapter number

## Output Contract

Return a single JSON object:

```json
{
  "chapter_id": "<chapter number>",
  "chapter_title": "<title>",
  "scores": {
    "density": <1-5>,
    "transferability": <1-5>,
    "freshness": <1-5>
  },
  "score_total": <average of three scores, 1.0-5.0>,
  "recommendation": "distill | skim | skip",
  "reason": "<one sentence>"
}
```

## Scoring Rubric

### Density (1-5)
*How rich is this chapter in named frameworks, principles, and anti-patterns?*

- **5**: Multiple named frameworks, explicit principles, named anti-patterns. Chapter is a goldmine.
- **4**: Several frameworks or principles, some named, some implicit. Worth distilling.
- **3**: A few transferable ideas mixed with narrative or filler. Borderline.
- **2**: Mostly narrative with one or two ideas worth keeping.
- **1**: Mostly anecdotes, marketing language, or self-promotion. Low signal.

### Transferability (1-5)
*Will the ideas in this chapter apply across multiple future projects?*

- **5**: Foundational concepts that apply to almost any technical work in the domain.
- **4**: Strong patterns that apply to most projects of a certain type.
- **3**: Useful for specific scenarios but limited reach.
- **2**: Niche applicability — useful for narrow contexts only.
- **1**: One-off observations or autobiographical content.

### Freshness (1-5)
*Is the content current and durable, or dated/superseded?*

- **5**: Foundational ideas that have aged well; or genuinely new patterns from the last 1-2 years.
- **4**: Modern best practices, mostly still relevant.
- **3**: Mixed — some durable ideas, some stale framing.
- **2**: Mostly dated framing or superseded approaches.
- **1**: Reflects an era's thinking that has been clearly superseded.

## Recommendation Mapping

- `score_total >= 4.0` → `distill` (full pipeline)
- `score_total 2.5-3.9` → `skim` (keep digest only, no skill generated)
- `score_total < 2.5` → `skip` (no further processing)

## Calibration Notes

- Be honest. Dropping marginal chapters is more valuable than over-producing weak skills.
- A book with 12 chapters typically has 3-6 worth distilling. The rest are connective tissue.
- "Hot takes" and marketing language should pull density and freshness scores down.
- Code-heavy chapters can score high on transferability even with thin prose.
