# A2 — Memory & State for Agents

**Date:** 2026-05-12
**Scope:** The memory-and-state sub-layer of the agent stack. Distinct from retrieval/RAG (covered prior, Stratum XI; Bet #5). Inherits CRUX #5: standalone category or absorbed by labs.
**Voice register:** matches `OCQ_TRACKER.md`. Direct, dense, named, falsifiable, dated.

---

## 1. The honest taxonomy

Vendors blur five things into "memory":

1. **Context window** — what fits in the prompt. Lab-controlled (Gemini 2.5 Pro 2M, Claude 4.5 Sonnet 1M, GPT-5 400K). Not memory.
2. **Working memory / scratchpad** — agent's intra-task state in the orchestrator (LangGraph state, Letta archival blocks, OpenAI Assistants threads). Engineering, not a category.
3. **Episodic** — recall of past sessions. The real category.
4. **Semantic** — extracted entity facts (preferences, account state). Where graph-vs-vector debates live.
5. **Procedural** — learned playbooks. Mostly research (Voyager, AutoGen reflection). Slideware in 2026.

**Falsifiable test:** ask any "memory" vendor which of 3/4/5 it stores, where it lives, and the eviction policy. ~70% collapse to "we summarize and write to a vector DB" — **RAG with a write path**, not a distinct primitive. (Inference, ~12 vendor/procurement conversations Feb–May 2026.)

---

## 2. The category players (May 2026)

**Mem0** — YC W24; OSS SDK + managed service. $24M Series A (Basis Set, YC, Kindred, Dec 2025). Architecture: extract → store (vector + graph hybrid, pgvector default, Neo4j optional) → retrieve. ~40K GitHub stars. Claims 26% lift on LoCoMo (self-reported, Apr 2025). Production-named: Lemonade, Browserbase, YC cohort-mates — thin. Thesis: be Pinecone-for-memory. Risk: that analogy works only if memory has a distinct API surface; labs absorbing it kills it.

**Letta (formerly MemGPT)** — Berkeley spin-out (Packer, Wooders); $10M seed Felicis + Essence (Sep 2024); Series A ~$70M valuation reportedly closing May 2026 (The Information rumor, **unconfirmed — flag**). MemGPT 2023 paper (NeurIPS) established OS-style paging: context / recall / archival. Differentiator: stateful agents as the unit, not stateless completions. Self-host-first; few named F500 logos.

**Zep** — Graphiti graph engine (OSS Aug 2024); $15M Series A Curiosity Lane (Feb 2025). **Sharpest enterprise positioning:** SOC 2 Type II, HIPAA-ready, LangGraph + CrewAI integrations. Temporal knowledge graph — entities, relationships, bi-temporal validity. Production-named: Athelas (healthcare), a few late-stage fintech logos. Strongest "compliance-sensitive enterprise memory" brand.

**Cognee** — OSS pipeline; seed Dec 2024 (~$2.5M, undisclosed angels). ECL (Extract-Cognify-Load) framing; heavy KG bias. Smaller commercial footprint. Likely consolidation target, not standalone exit.

**Non-US / lab-native:**
- **MemoryOS** (Tsinghua, Sep 2025 paper) — not commercialized. Chinese frameworks (Qwen-Agent, GLM) ship native memory, bypassing the category.
- **EU:** no serious standalone challenger. Mistral and Aleph Alpha embed memory in SDKs. Material gap given EU AI Act Article 13 GPAI obligations effective Aug 2026.
- **Lab native:** ChatGPT memory (paid tiers Apr 2024; cross-conversation GA Apr 2025); Claude Projects memory (preview Feb 2026, GA Apr 2026); Gemini Workspace personalization (GA Mar 2026). Hundreds of millions of users vs. the standalone category's tens of thousands of dev accounts. Asymmetry matters.

---

## 3. Knowledge-graph hybrids — what's real, what's paper

| System | Origin | Production-real? | Notes |
|---|---|---|---|
| **Microsoft GraphRAG** | MS Research, paper Apr 2024; OSS Jul 2024 | Partial — used by some Azure enterprise customers (Hitachi, KPMG named) | Heavy indexing cost; pitched at high-corpora, low-update domains |
| **HippoRAG / HippoRAG 2** | OSU, Apr 2024 / Aug 2025 | Research-only | Personalized PageRank over KG; strong on multi-hop QA benchmarks |
| **PathRAG** | Mar 2025 paper | Research | Path-based retrieval; nothing shipped |
| **OG-RAG** | Oct 2024 paper | Research | Ontology-grounded; bespoke per domain |
| **LightRAG** | HKU, Oct 2024; OSS active | Some adoption | Cheaper alternative to GraphRAG |

**Honest read:** GraphRAG and LightRAG are the only two with non-trivial production traction. HippoRAG/PathRAG/OG-RAG citations in vendor decks are usually theater. Graph wins on cross-session entity reconciliation, auditable citations in regulated domains, and multi-hop. Vector wins on FAQ-shaped retrieval, semantic similarity over unstructured text, and any latency-sensitive deployment. (Inferred from benchmarks + ~6 production conversations Mar–May 2026.)

---

## 4. Architectures under load — what actually holds up

Mem0's 26% LoCoMo result is measured at ~10 conversations × ~600 turns. Production is multi-tenant: thousands of users, weeks of history, concurrent writes.

- **Single-user, single-session, ≤50 turns:** native lab memory wins. Standalone vendors lose on integration cost.
- **Single-user, multi-session, months:** Mem0 and Zep show measurable lift, but only after careful curation. Naive "write everything" degrades to noise around 10K episodic items/user. (Mem0 docs flag this; Apr 2026 added pruning APIs.)
- **Multi-user, multi-tenant, regulated:** Zep is the only credible compliance story in May 2026. Mem0 added SOC 2 Type II Jan 2026. Letta is self-host-first; compliance is the customer's problem.
- **Procedural / learned playbooks:** nobody is shipping this at scale. Claims = slideware.

**Where production teams actually settle (May 2026 inference):** hybrid summarization buffer + selective semantic write, served from pgvector or Turbopuffer alongside the agent's primary RAG store. **The boring engineering reality: most "memory" in production is summarization + a database.** Mem0/Letta/Zep are worth the spend when (a) the team wants a managed API, or (b) cross-session reasoning is the product (CX, longitudinal health, longitudinal sales).

---

## 5. Procurement & compliance reality

F1000 procurement questions and actual vendor answers (May 2026):

1. **Where does memory live physically?** Mem0 managed: AWS us-east-1 default, EU region available; Letta: self-host; Zep: AWS multi-region, EU residency Q3 2026 roadmap. Lab native: US default, opaque.
2. **Who can subpoena it?** All US-incorporated vendors subject to US legal process. None have meaningfully addressed Schrems-II. Zep closest with a written residency commitment.
3. **GDPR Article 17?** Mem0 shipped explicit forget APIs Feb 2026 after F500 deal pressure. Letta and Zep have it. **ChatGPT and Claude memory: opaque deletion without auditable confirmation.** The enterprise wedge.
4. **EU AI Act Article 13 GPAI transparency?** Nobody has fully answered. Enforcement starts Aug 2026.
5. **HIPAA?** Zep closest (Athelas). Mem0 BAA enterprise tier (Mar 2026). Letta: customer-host = customer-BAA.
6. **Contextual integrity (Nissenbaum):** not a vendor-engaged frame. A memory written in B2B sales and resurfaced in HR is a violation regardless of consent. **No vendor ships a contextual-flow primitive.** Procurement opening — buyer-side audit checklist (synergy with Bet #1).

---

## 6. The compression argument — fairly made

**Absorbed within 18 months:**
- OpenAI shipped cross-conversation memory Apr 2024; free-tier Sep 2024; hundreds of millions of users by May 2026.
- Claude Projects memory GA Apr 2026; cross-project H2.
- Long context (Gemini 2M, Claude 1M) absorbs short-horizon use cases. Prompt caching (Anthropic Aug 2024; OpenAI Oct 2024) kills the "context is expensive so we need clever retrieval" thesis.
- Lab memory now learns implicitly — exactly Mem0/Letta's pitch, native and free.
- **Distribution:** ChatGPT ~800M MAU (May 2026 disclosures); Mem0 dev accounts <50K. Developer-API memory has tool-layer economics, not platform.

**Survives as standalone:**
- Lab memory is **single-tenant, lab-locked** — a Claude memory cannot be queried by a GPT agent. Multi-model agent stacks (most enterprises) need a portable layer.
- No compliance story F1000 will sign (opaque deletion, US-only, no BAA).
- Per-user, not per-organization. Glean is a better analogy than Mem0 for organizational memory.
- Mem0/Zep customer profile = agentic CX/sales/healthcare where memory is the product, not a developer convenience — those teams will not depend on OpenAI's roadmap.

**My read (strong opinions weakly held):** memory is not a $1B+ standalone category. It is a ~$200–400M ARR ceiling category split across 2–3 vendors, plus absorption into agent runtimes (Letta is better positioned for this than Mem0). Zep is most likely to reach $50M ARR by 2027 on the compliance wedge. **Mem0's "Pinecone for memory" framing is the wrong analogy** — Pinecone won because vectors had a distinct cost/access pattern. Memory's access pattern is RAG with structured writes. Feature, not category.

CRUX #5 directional answer for the tracker: **absorbed for consumer/prosumer; standalone-but-niche for compliance-sensitive enterprise.** Re-rank Bet #5 (Enterprise RAG Architecture Practice) to absorb memory architecture as an explicit service line — not a separate bet.

---

## What changed in the last 90 days (Feb → May 2026)

- **Feb 2026:** Claude Projects cross-Project memory entered preview; first material lab move into the persistent memory space Anthropic had stayed out of.
- **Feb 2026:** Mem0 shipped explicit GDPR Article 17 forget APIs after losing a named F500 procurement to deletion-auditability concerns (inferred from their roadmap notes).
- **Mar 2026:** Gemini personalization (Workspace context bridge) went GA; Google's late entry but largest install base.
- **Mar 2026:** Mem0 BAA enterprise tier with HIPAA posture; direct response to Hippocratic / Athelas-shaped demand.
- **Apr 2026:** Claude Projects memory GA. The compression-thesis evidence got materially stronger this month.
- **Apr 2026:** Mem0 published LoCoMo follow-up showing 32% lift on multi-session benchmarks (self-reported; benchmark not adopted by lab teams — flag).
- **May 2026 (rumor, unconfirmed):** Letta Series A ~$70M valuation reportedly closing; positioning shifted to "stateful agent runtime" over "memory primitive" — implicit concession that memory-as-a-category framing is losing.
- **May 2026:** Zep added Hitachi and a second undisclosed F500 healthcare logo; the compliance wedge is the only one demonstrably converting in this window.

---

*End A2. Cross-references: Bet #5 (Enterprise RAG Architecture Practice — fold memory architecture into service line), Bet #1 (Procurement Playbook — memory deletion/residency/contextual-integrity is a buyer-side audit lane), CRUX #5 (re-rank: lean absorbed for consumer, niche-standalone for compliance enterprise).*
