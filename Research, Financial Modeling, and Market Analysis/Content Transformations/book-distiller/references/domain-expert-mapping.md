# Book → Domain Expert Mapping

Used by `book-distiller` at Stage 2 (PARSE) and Stage 3 (PRODUCTIZE) to select
the persona skill that will read and distill the chapter.

The same expert is used for both passes — consistency matters more than
multi-perspective coverage at this stage.

## Default Mapping by Domain

| Book domain | Primary expert | Secondary (rare, only for synthesis pass) |
|---|---|---|
| AI / ML engineering | `anthropic-skills:cto-architect` | `systems-thinking` |
| AI product strategy | `ai-product-strategy` | `head-of-product-engineering` |
| Software architecture / system design | `engineering:system-design` or `anthropic-skills:cto-architect` | — |
| Modern software engineering practices | `anthropic-skills:cto-architect` | `engineering:tech-debt` |
| LLMs / agents / prompting | `ai-product-strategy` | `anthropic-skills:cto-architect` |
| Product management | `head-of-product-engineering` | `defining-product-vision` |
| Sales methodology | `anthropic-skills:winning-by-design-sales-excellence-framework` | `anthropic-skills:the-meddpicc-enterprise-deal-desk` |
| Enterprise sales | `anthropic-skills:the-meddpicc-enterprise-deal-desk` | — |
| Marketing / GTM strategy | `marketing:campaign-plan` (closest available) | — |
| Research methods | `conducting-user-interviews` | — |
| Org leadership / management | `head-of-product-engineering` | `systems-thinking` |
| Data / analytics | `data:explore-data` or `data:analyze` | — |

## Rules

1. **Default to one primary expert.** Adding a secondary doubles cost without
   typically doubling quality. Only invoke a secondary at the book-level
   cross-chapter synthesis stage (post-Stage 4, future enhancement).

2. **If the book is multi-domain, choose the dominant lens.** A book on "AI
   product management" is product-strategy primary, not split between AI and PM.

3. **If unsure, ask Alex.** The choice shapes every downstream output. Cost of
   a 30-second clarification is much lower than re-running the pipeline with
   the wrong persona.

## Current v1 Book Library

| Book | Domain | Primary Expert |
|---|---|---|
| Building AI-Powered Products | AI product strategy | `ai-product-strategy` |
| AI Engineering | AI / ML engineering | `anthropic-skills:cto-architect` |
| Hands On LLMs | LLMs / agents | `ai-product-strategy` |
| Modern Software Engineering | Software practices | `anthropic-skills:cto-architect` |
| Software Architecture Fundamentals | System design | `engineering:system-design` |
