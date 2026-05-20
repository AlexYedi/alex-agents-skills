# B2 — OCQ Matrix: Memory, Planning, Capability Safety

**Date:** 2026-05-12 • **Inputs:** A2, A3, OCQ_TRACKER (May 2026). **Voice:** OCQ register. **Discipline:** if >2 of 9 opportunities score 5/5/5, the lens has collapsed.

---

## Layer 1 — Sub-stratum 4: Memory & State

**Framing.** May 2026 evidence on CRUX #5 leans absorbed-for-consumer, niche-standalone-for-compliance. Claude Projects memory GA Apr 2026, Gemini Mar 2026, ChatGPT ~800M MAU vs. Mem0 <50K dev accounts. Survives: Zep's compliance wedge (Hitachi + second F500 healthcare logo May 2026); Letta's stateful-runtime reframe (rumored ~$70M Series A — flag, unconfirmed); buyer-side audit gap no vendor ships. Alex's leverage is procurement.

### Opportunities

**O1 — Memory Audit Lane in the Procurement Playbook (Bet #1 fold-in).**
Mem0 shipped GDPR Art. 17 forget APIs only Feb 2026 after losing an F500 deal on deletion-auditability. ChatGPT/Claude memory still ship opaque deletion. F1000 InfoSec has no canonical memory-audit checklist. Alex ships a 6-question audit (residency, deletion, Schrems-II, BAA, contextual integrity, EU AI Act Art. 13). Compounds Bet #1.
- **Confidence: 4 • Time-to-Monetize: 4 • Claimability: 5**
- **Falsifiability:** Playbook ships memory module, <10 inbound in 90 days → fold into generic vendor-audit chapter.

**O2 — Compliance-First Memory Architecture (Bet #5 fold-in).**
Zep is the only May 2026 vendor with credible compliance posture (SOC 2 Type II, HIPAA via Athelas, EU residency Q3 2026 roadmap). For F500 healthcare/financial-services agents, the decision is "which architecture survives audit" — same buyer as Bet #5's RAG practice. Three-product sale, one buyer.
- **Confidence: 4 • Time-to-Monetize: 3 • Claimability: 4**
- **Falsifiability:** Anthropic/OpenAI ship BAA + auditable-deletion native memory before Q4 2026 → wedge closes.

**O3 — Contextual-Integrity Frame (Bet #6 beat).**
Nissenbaum's contextual integrity — memory written in B2B sales surfacing in HR is a violation regardless of consent — is not vendor-engaged in May 2026. No vendor ships a contextual-flow primitive. Translate to operator language, plant named voice. Low cost, high positioning.
- **Confidence: 3 • Time-to-Monetize: 2 • Claimability: 4**
- **Falsifiability:** 3 essays, no inbound from privacy counsel / AI governance leads in 6 months → academically interesting, not commercially activated.

### Challenges

**C1 — Lab absorption faster than productization window.**
Claude Projects + Gemini + ChatGPT memory compress the developer-API thesis inside 12 months. Standalone-memory-architecture service has a shrinking buyer set.
- **Severity: 4 • Probability: 4 • Alex's exposure: 2** (selling around it, not building it)
- **Watch signal:** Anthropic/OpenAI cross-org memory with audit + BAA — track Trust Center posts.

**C2 — Buyers don't yet rank memory as a distinct audit category.**
F1000 AI councils pattern-match memory to generic SaaS data-handling. Contextual-integrity harms are real but not on the audit form. Alex risks being early on a frame buyers don't pay for until an incident.
- **Severity: 3 • Probability: 4 • Alex's exposure: 4**
- **Watch signal:** first named memory-leakage incident in healthcare/finserv → category instantiates overnight.

### Open Questions

**OQ1 — Does Letta's stateful-runtime reframe land?**
If the rumored ~$70M Series A closes with the reframe, it implicitly concedes memory-as-category is losing — creates a "stateful runtime" category overlapping LangGraph/Pydantic-AI. Re-ranks Bet #3 adjacent.
- **Decidability: 4 • Asymmetry: 3 • Bet-size: 2**
- **Answer-event:** Letta funding + customer-named launches by Q3 2026.

**OQ2 — Does a memory-portability standard emerge?**
Lab memory is single-tenant lab-locked. Multi-model enterprise stacks need portability. MCP-shaped memory schema is plausible by 2027 — or labs fight it for the same lock-in reason they hesitated on MCP.
- **Decidability: 3 • Asymmetry: 4 • Bet-size: 3**
- **Answer-event:** Anthropic / OpenAI / Linux Foundation memory schema proposal, or Mem0/Letta/Zep co-signed portability standard.

---

## Layer 2 — Sub-stratum 5: Planning, Reasoning, Test-Time Compute

**Framing.** A3's verdict: production agents are 3–7 step ReAct loops with a reasoning model, prompts, and a verifier. Graph/tree/meta-planner is inside the model now (o-series, Claude extended thinking, Deep Think) or research-only. Planner-executor-verifier is the durable architecture — shipping at Sierra ($150M ARR Q1 2026), Decagon ($100M), Cursor, Cognition. Test-time compute bends past 8k reasoning tokens; `reasoning_effort=high` wastes on CX/RAG, pays on coding and compliance. DeepSeek R2 Apr 2026 at ~$0.55/M input tokens reprices floor 4–6× below GPT-5. Alex's leverage: translate "reasoning model" from procurement category to task-class economics.

### Opportunities

**O4 — Trajectory Cost & Latency Audit (Bet #4 FinOps fold-in).**
Sierra/Decagon/Cursor pattern — planner (Opus/GPT-5) once, executor (Sonnet/Flash) N times, verifier once — routes 70–85% tokens cheap. Vercel AI Gateway, Bedrock, OpenRouter expose this as config (Q1–Q2 2026). Median enterprise is *not* routing; running `high` on every call for 0–2pt gains at 5–12× cost. Audit-and-rewire sellable today.
- **Confidence: 5 • Time-to-Monetize: 5 • Claimability: 5**
- **Falsifiability:** Bedrock/Azure ship default-on auto-tier routing in 2026 → 12-month window slams. Decide by Q3 2026.

**O5 — DeepSeek/Qwen On-Prem Procurement Playbook.**
DeepSeek R2 at ~$0.55/M input tokens + open weights gives F1000 CIOs credible on-prem at 20–40% of US frontier cost. Bottleneck is geopolitics, not capability. Alex is the right messenger: US enterprise-buyer voice writing "how to evaluate a Chinese open-weight reasoner for F1000." Compounds Bet #1.
- **Confidence: 3 • Time-to-Monetize: 3 • Claimability: 4**
- **Falsifiability:** US Commerce extends export restrictions to weights in 2026, OR no F500 publicly deploys by Q4 2026 → reframe as "open-weight generally."

**O6 — Task-Class Eval Brokerage (Bet #6 beat).**
"Reasoning model" is a procurement category, not a capability claim. Buyers cannot evaluate CoT faithfulness or RLVR durability, but they can evaluate benchmarks resembling their task class. τ-bench v2 (Apr 2026) is first credible CX-agent proxy; SWE-Lancer (Feb 2025) is best "would I pay" framing. Translate for RevOps/CX/Legal-Ops.
- **Confidence: 3 • Time-to-Monetize: 2 • Claimability: 4**
- **Falsifiability:** 6 months, <2K subs, no advisory inbound → interesting to writers not buyers.

### Challenges

**C3 — Hyperscaler auto-routing absorbs FinOps wedge inside 18 months.**
Bedrock + Vercel AI Gateway + OpenRouter shipping tier routing as config (Q1–Q2 2026) is the leading edge. Default-on auto-routing with cost SLOs plausible by H2 2027. Window is short.
- **Severity: 4 • Probability: 4 • Alex's exposure: 5** (Bet #4's core risk)
- **Watch signal:** AWS / Azure / GCP AI cost auto-optimization announcements.

**C4 — "Planning is overrated" is a hard sell post-procurement.**
A 3-step ReAct loop matches fancy planner-executor on >80% of typical jobs. Saying this to a buyer who already procured planner-heavy kills the conversation. Time the message pre-procurement.
- **Severity: 3 • Probability: 4 • Alex's exposure: 4**
- **Watch signal:** vendor messaging shifts from "planner architecture" to "task-class benchmarks."

### Open Questions

**OQ3 — Does test-time compute keep paying past 32k reasoning tokens in 2026–2027?**
METR's "doubling every ~7 months" is real but bench-curated. If >32k unlocks new task classes (multi-hour autonomous coding, real deep research), Bet #4's "10× is waste" ages badly. If it plateaus, planner-executor-verifier is durable for years.
- **Decidability: 4 • Asymmetry: 4 • Bet-size: 3**
- **Answer-event:** METR Q4 2026 update; first F500 publicly-named >$10/task agent at scale; SWE-Lancer crossing 50% of $ earned.

**OQ4 — Do Chinese open-weight reasoners cross the F500 line in 2026?**
DeepSeek/Qwen/Kimi parity on recipe + 4–6× cost advantage is real. Gating factor is geopolitics. If one F500 publicly deploys on-prem (or via US reseller), the dam breaks; if Commerce restricts weights or an incident occurs, it stays research curiosity. Asymmetric for Alex's positioning.
- **Decidability: 3 • Asymmetry: 5 • Bet-size: 3**
- **Answer-event:** named F500 on-prem deployment, OR US Commerce weight-export rule.

---

## Layer 3 — Meta-A: Capability-Level Safety Regimes

**Framing.** Capability-level safety is *pre-deployment*: ASL, OpenAI Preparedness Framework (PF), Google FSF, model cards for agents, deployment-freeze precedent, external evaluators (METR, UK AISI, US AISI, Singapore AISI, EU AI Office). Distinct from B3 runtime guardrails. Honest read: voluntary frameworks are politically fragile, evaluator capacity is the binding constraint, and **Anthropic's ASL framework has reputational durability but contested regulatory durability** — OpenAI PF has a competitive-adjustment clause, EU AI Code of Practice (Aug 2026 GPAI obligations) does not specify ASL/PF/FSF as conformity paths, and UK AISI's Inspect is quietly the closest vendor-neutral standard (cited in EU AI Act conformity drafts, Feb 2026). Alex is wrong profile for capability evals, right profile for translating safety claims into procurement questions.

### Opportunities

**O7 — Capability-Safety Translation in the Playbook.**
Every frontier vendor's safety posture is a marketing artifact buyers cannot evaluate. Procurement asks "are they safe?" and gets a model card. Alex publishes an 8-question audit (which evaluator ran the test, pre/post-deployment, adjustment-clause invocation, rollback precedent, EU Code alignment). Pure procurement-translation. Compounds Bet #1.
- **Confidence: 4 • Time-to-Monetize: 3 • Claimability: 5**
- **Falsifiability:** Playbook chapter, <5 inbound from F1000 AI governance leads in 90 days → lives inside Bet #1 forever, never a standalone advisory line. Acceptable.

**O8 — Inspect AI as Vendor-Neutral Procurement Standard.**
UK AISI Inspect (OSS, MIT) cited in EU AI Act conformity drafts (Feb 2026) — closest non-lab-aligned eval standard. F1000s want defensible third-party signal, not vendor self-report. Alex writes the playbook for "Inspect-based evals in vendor onboarding." Depth: configure tasks, not write evals.
- **Confidence: 3 • Time-to-Monetize: 2 • Claimability: 3**
- **Falsifiability:** EU AI Office finalizes a conformity standard excluding Inspect by Q4 2026 → wedge closes. Watch Aug 2026 GPAI Code of Practice.

**O9 — Deployment-Freeze Precedent Watch (Bet #6 beat).**
Thin precedent — Claude 4 staged release with extended pre-deployment evals, OpenAI GPT-4 system-card delays. No F1000 procurement contract addresses "what if the vendor freezes the model my agent depends on." Track in newsletter, build standard contract clause for Bet #1.
- **Confidence: 2 • Time-to-Monetize: 1 • Claimability: 4**
- **Falsifiability:** 2026 produces no public freeze event → stays a Playbook chapter, never a beat.

### Challenges

**C5 — Anthropic ASL framework's regulatory durability is contested.**
ASL-3/4 is reputationally durable inside AI-safety audiences. Not baked into EU AI Code of Practice (Aug 2026), NIST AI RMF GenAI Profile, or ISO 42001. OpenAI PF's adjustment clause and Google FSF's looser thresholds mean buyers cannot procure on "ASL-3" as a control. Alex risks over-indexing on Anthropic framing.
- **Severity: 3 • Probability: 4 • Alex's exposure: 3**
- **Watch signal:** EU AI Office Aug 2026 GPAI guidance — does it specify ASL/PF/FSF or set independent thresholds?

**C6 — Evaluator capacity is binding and Alex cannot solve it.**
METR, UK AISI, US AISI, Singapore AISI, EU AI Office collectively run a few dozen frontier evals per year against dozens of releases. Bottleneck is research-scientist hiring. Alex translates, doesn't increase supply.
- **Severity: 4 • Probability: 5 • Alex's exposure: 2** (low because he isn't pretending to solve it)
- **Watch signal:** AISI hiring, METR funding, EU AI Office staff growth.

### Open Questions

**OQ5 — Does OpenAI's Preparedness adjustment clause get invoked in 2026?**
Logged as Structural Risk #3. The clause permits OpenAI to adjust thresholds if a competitor releases comparable without safeguards. Public invocation destabilizes voluntary-safety regimes; Anthropic's "we are different" becomes more valuable; EU may shift from voluntary to mandatory thresholds.
- **Decidability: 4 • Asymmetry: 5 • Bet-size: 4**
- **Answer-event:** OpenAI public adjustment notice OR Anthropic counter-statement OR EU regulatory response.

**OQ6 — Does a non-US AISI become the de-facto procurement standard?**
UK AISI Inspect leads non-aligned candidates; Singapore AISI's MLCommons AILuminate is real but narrower; EU AI Office is young. F1000 procurement wants defensible third-party signal. If a non-US standard wins, ASL/PF/FSF become brand attributes, not controls.
- **Decidability: 3 • Asymmetry: 4 • Bet-size: 3**
- **Answer-event:** EU AI Code of Practice Aug 2026 references a specific evaluator framework as a conformity path.

---

## Scorecard

Confidence: 1×5 (O4), 4×4, 3×3, 1×2. Time-to-Monetize: 1×5 (O4), 2×4, 3×3, 2×2, 1×1. Claimability: 3×5 (O1, O4, O7), 4×4, 2×3. Only **O4** scores 5/5/5 — tracks Bet #4's velocity-to-cash and named-scale shipping (Sierra $150M, Decagon $100M Q1 2026). Window is explicit-short (18mo); 5s reflect *current* fit, not durable fit. Inside discipline.

*Cross-refs: Bet #1 absorbs O1, O5, O7, O9, C2, C5. Bet #4 absorbs O4, C3, OQ3. Bet #5 absorbs O2. Bet #6 absorbs O3, O6, O9. CRUX #5 reaffirmed: absorbed for consumer, niche-standalone for compliance.*
