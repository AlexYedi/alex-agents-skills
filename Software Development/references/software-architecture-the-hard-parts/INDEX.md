# INDEX — Software Architecture: The Hard Parts

**Source:** *Software Architecture: The Hard Parts — Modern Trade-Off Analyses for Distributed Architectures* by Neal Ford, Mark Richards, Pramod Sadalage & Zhamak Dehghani (O'Reilly, 2021)

**Purpose of this folder:** distilled knowledge from the book, structured so an agent (or human) can load the smallest useful slice instead of the whole 334-page text.

**Use this file first.** It's a routing layer. Open the file/section it points you to, not the others.

---

## Files in this folder

| File | What's in it | When to load |
|---|---|---|
| `complete-distillation.md` | Full book summary: thesis, big takeaways, chapter-by-chapter | You want the whole picture in one read |
| `frameworks.md` | Every named framework/matrix/pattern catalog from the book | You need the canonical definition or trade-off table for a specific concept |
| `sysops-squad-worked-example.md` | The book's running case study: characters, decisions, ADRs ratified per chapter | You need a worked example to ground a method in practice |
| `additional-experts.md` | Adjacent reading, related thinkers, links to other distilled books in this repo | You finished the book and want to broaden |
| `scripts/ocr_pipeline.sh` | Reproducible OCR pipeline (the source PDF was image-only) | You want to re-extract the text yourself |
| `scripts/saga_picker.py` | Fast non-conversational saga lookup (3 prompts → saga name + ADR scaffold) | You know your axis answers and want a quick lookup; use SKILL `distributed-workflows-and-sagas` for real decisions |

---

## If you need X, load Y

| Question / symptom | Canonical asset | Section anchor |
|---|---|---|
| "Should we use a saga?" | SKILL `distributed-workflows-and-sagas` | `frameworks.md#the-8-transactional-sagas` |
| "Which saga pattern fits?" | SKILL `distributed-workflows-and-sagas` | `frameworks.md#saga-selection-matrix` |
| "How do we own this data across services?" | SKILL `data-ownership-and-distributed-data` | `frameworks.md#data-ownership-patterns` |
| "How do services share data without a shared DB?" | SKILL `data-ownership-and-distributed-data` | `frameworks.md#data-access-patterns` |
| "Strict vs loose contracts?" | SKILL `service-contracts-and-coupling` | `frameworks.md#contracts` |
| "What's an architectural quantum?" | SKILL `architectural-quanta-and-modularity` | `frameworks.md#architectural-quantum` |
| "Should we break this monolith apart?" | SKILL `service-and-data-decomposition` | `frameworks.md#decomposition-patterns` |
| "How big should this service be?" | SKILL `service-granularity-forces` | `frameworks.md#granularity-forces` |
| "Replicated code, shared library, shared service, or sidecar?" | SKILL `code-reuse-in-distributed-systems` | `frameworks.md#reuse-patterns` |
| "How do I make a defensible architecture decision?" | SKILL `trade-off-analysis-method` | `frameworks.md#trade-off-analysis-3-step` |
| "I just want to read the book" | `complete-distillation.md` | (whole file) |
| "Give me a worked example" | `sysops-squad-worked-example.md` | (whole file) |

---

## Don't load this folder for

- Runtime resilience (circuit breakers, bulkheads, timeouts) → use `microservices-resilience-patterns` skill instead
- Storage-level eventual consistency (N/W/R quorums, CRDTs) → use `eventual-consistency-mechanics` skill — the Hard Parts saga model is *business-level* EC, different problem
- Architectural characteristics catalog ("ilities") → use the `fundamentals-of-software-architecture` reference; this book assumes you've read that one
- General distributed systems theory (CAP, consensus, gossip) → use `distributed-systems-essentials` skill

---

## How the book maps to the repo

| Book chapter | Primary skill it backs | Reference section |
|---|---|---|
| Ch 1 — No best practices | `trade-off-analysis-method` | `complete-distillation.md#ch-1` |
| Ch 2 — Discerning coupling | `architectural-quanta-and-modularity` | `frameworks.md#coupling-vocabulary` |
| Ch 3 — Architectural modularity | `architectural-quanta-and-modularity` | `frameworks.md#modularity-drivers` |
| Ch 4 — Architectural decomposition | `service-and-data-decomposition` | `frameworks.md#decomposition-patterns` |
| Ch 5 — Component-based decomposition | `service-and-data-decomposition` | `frameworks.md#component-based-decomposition` |
| Ch 6 — Pulling apart operational data | `data-ownership-and-distributed-data` | `frameworks.md#data-decomposition` |
| Ch 7 — Service granularity | `service-granularity-forces` | `frameworks.md#granularity-forces` |
| Ch 8 — Reuse patterns | `code-reuse-in-distributed-systems` | `frameworks.md#reuse-patterns` |
| Ch 9 — Data ownership | `data-ownership-and-distributed-data` | `frameworks.md#data-ownership-patterns` |
| Ch 10 — Distributed data access | `data-ownership-and-distributed-data` | `frameworks.md#data-access-patterns` |
| Ch 11 — Distributed workflows | `distributed-workflows-and-sagas` | `frameworks.md#workflow-coordination` |
| Ch 12 — Transactional sagas | `distributed-workflows-and-sagas` | `frameworks.md#the-8-transactional-sagas` |
| Ch 13 — Contracts | `service-contracts-and-coupling` | `frameworks.md#contracts` |
| Ch 14 — Analytical data | (optional — Data Engineering folder) | `frameworks.md#analytical-data` |
| Ch 15 — Build your own trade-off analysis | `trade-off-analysis-method` | `frameworks.md#trade-off-analysis-3-step` |

---

## How to update this folder

- Skills point here. Don't duplicate framework definitions into skills — link to the section anchor.
- If a new framework gets added to `frameworks.md`, add a row to "If you need X, load Y" above.
- Keep this file under 150 lines. It's a routing layer, not content.
