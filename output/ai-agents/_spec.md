# AI Agents Master — Canonical Spec (Volume III)

**Version:** 1.0 (draft)
**Date:** 2026-05-20
**Owner:** Alex Yedi
**Parent:** `output/ai-stack/_spec.md` (Volume I/II — the full AI stack)
**Purpose:** Single source of truth for the Volume III consolidation. Zooms the agent layer (Stratum XIII in Volume I) into its own 10-sub-stratum + 4-meta taxonomy. Every chapter writer and every plate generator reads this file first.

---

## 1. Goal of this artifact

A single readable workbook — markdown source + EPUB export — that consolidates the agent-layer thesis Alex is acting on. Replaces the scattered pile of `AI_AGENTS_REPORT.docx`, `AI_AGENTS_ADDENDUM.docx`, `AI_AGENTS_TRACKER.md`, `AI_AGENTS_MASTER_READTHROUGH.docx`, and 11 unreadable matplotlib plates.

**Design posture:** identical to Volume I — educational density, no aesthetic homage, plates earn their place via "what would prose miss?" test.

**Operating posture:** sub-tracker that feeds the parent (`output/ai-stack/chapters/04_tracker.md`). Where the agent-layer view materially deltas a parent Bet (especially #1, #3, #4), the delta is named here AND mirrored back into the parent tracker on the next monthly ritual.

**Relationship to Volume I:** Volume III COMPOSES on top of Volume I — does not duplicate. The five frameworks, the 7 Bets, the 5 Risks, and the 5 Cruxes carry over with explicit agent-layer deltas annotated. Do not re-derive the full-stack analysis here.

---

## 2. Source materials (read-only inheritance)

Located in `../ai-agents/`:

| File | Role | Disposition |
|---|---|---|
| `AI_AGENTS_REPORT.docx` (~7.5k words estimated) | Foundation prose, 10 sub-strata + 4 meta | Source for Ch 1; extract done |
| `AI_AGENTS_ADDENDUM.docx` (~30k words, Parts VI–XIII) | Frameworks + 7 Bets refresh + Action Map + Procurement Rubric | Source for Ch 2, 3, 6; extract done |
| `AI_AGENTS_TRACKER.md` | Living tracker, agent-layer | Source for Ch 4 |
| `AI_AGENTS_MASTER_READTHROUGH.docx` | Master read-through (linear narration of the full volume) | Reference for register; not consolidated separately |
| `framework_analysis/B1-B4_ocq_*.md` | OCQ chunks across the sub-strata | Source for Ch 2 §2.1 |
| `framework_analysis/B5_wardley.md` | Wardley analysis | Source for Ch 2 §2.2 |
| `framework_analysis/B6_seven_powers.md` | 7 Powers analysis | Source for Ch 2 §2.3 |
| `framework_analysis/B7_ecosystem_jtbd.md` | Ecosystem JTBD (7 jobs) | Source for Ch 2 §2.4 |
| `framework_analysis/B8_talent_capital_flow.md` | Talent + capital flow data | Source for Ch 4 |
| `design_philosophy_agents.md` | Agent-aesthetic philosophy | Archive; not used |
| `AI_AGENTS_SUBSTRATE.pdf` / `_VOL2.pdf` / `_MASTER_PLATE.pdf` / `_MASTER_PLATES.pdf` / `_MASTER_VOLUME.pdf` | 11+ plates, unreadable | Source for plate redesign |
| `build_*.py` / `build_*.js` | Original generators | Reference only |

Parent volume (read-only cross-references): `output/ai-stack/` — especially Ch 3 (bets), Ch 4 (tracker), Ch 6 (glossary).

---

## 3. Canonical taxonomy

### 3.1 The 14 agent sub-strata (10 numbered + 4 meta)

Numbered I–X plus four meta-strata A–D. Names match `AI_AGENTS_REPORT.docx` so cross-references in `AI_AGENTS_TRACKER.md` remain valid.

**Part I — The Capability Substrate**
- **Stratum I — Foundation models as agentic engines** (Claude Opus 4.5, GPT-5, Gemini 2.5 Deep Think, Llama 4, DeepSeek R1/V4)
- **Stratum II — Agent runtimes and harnesses** (Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph 1.0, Mastra, Pydantic AI, CrewAI, Smolagents, AutoGen)
- **Stratum III — Tool use and the Model Context Protocol (MCP)** (Anthropic origin, Linux Foundation governance, 10,000+ servers, hyperscaler gateways)

**Part II — The Loops of Cognition**
- **Stratum IV — Memory and state** (Mem0, Letta, Zep, Cognee; native lab memory; GraphRAG/HippoRAG hybrids)
- **Stratum V — Planning, reasoning, test-time compute** (single-turn → ReAct → ToT → planner-executor → meta-planning; extended thinking budgets)

**Part III — Action and Defense Surfaces**
- **Stratum VI — Action surfaces** (code sandboxes, browser automation, computer use, voice, telephony, multi-agent orchestration)
- **Stratum VII — Evaluation and observability** (Braintrust, Langfuse, LangSmith, Arize, Inspect, METR, Patronus, Galileo)
- **Stratum VIII — Runtime safety and guardrails** (Lakera, Robust Intelligence, NeMo Guardrails, Llama Guard, prompt-injection defense)

**Part IV — The Productized Layer**
- **Stratum IX — Vertical agent products** (coding, CX, knowledge worker, legal, healthcare, RevOps, finance, creative)
- **Stratum X — End-user surfaces and form factor** (chat, voice, IDE, browser extension, mobile, on-device)

**Part V — The Meta-Strata** (wrap the whole agent stack)
- **Meta-A — Capability-level safety regimes** (ASL-4 thresholds, deployment freezes, RSPs, voluntary commitments)
- **Meta-B — Regulation** (EU AI Act Article 14 human-oversight, US sectoral, agent-specific transparency)
- **Meta-C — Economics** (per-trajectory cost curves; outcome-based pricing; thinking-budget economics)
- **Meta-D — Geopolitics** (sovereign agent products, export controls, agent-specific Gulf/India/EU)

### 3.2 The 5 frameworks (same as Volume I, tuned to agent context)

Identical to V1: OCQ × Sub-Stratum Matrix, Wardley Mapping, Helmer's 7 Powers, Ecosystem JTBD, Talent & Capital Flow. Tuned to agent context — see V1 spec §3.2 for lens definitions (carried verbatim into V3 Ch 2).

### 3.3 OCQ lens definitions (verbatim from V1 spec §3.3)

Carried over from Volume I. Same dimensions, same /15 totals. Tightened for the agent context — see Addendum Part VI Methodology for the agent-specific edge:

- **OPPORTUNITY (agent layer):** where in the agent stack is value being created faster than the field's prevailing narrative, AND where can someone with enterprise B2B GTM + AI-builder skill claim it inside a 12–18 month window before the layer commoditizes? Scored C/T/Cl, /15.
- **CHALLENGE (agent layer):** binding constraint or latent feedback loop that, if it tightens or fires, materially reprices everything above it. Specifically agent-layer: protocol fragmentation, model-vendor reasoning regression, inference-cost spikes, action-consequence liability, eval-trust collapse. Scored S/P/E, /15.
- **OPEN QUESTION (agent layer):** the agent-specific crux the field is betting on without admitting. Examples: does memory become permanent or absorbed; does MCP fork; does computer-use cross 80% reliability in 2026 or 2027; does test-time compute hit diminishing returns; does ASL-4 emerge in 2026 and force a freeze. Scored D/A/B, /15.

### 3.4 The 7 ecosystem JTBD jobs (Addendum Part X — different from V1's 6)

1. **Job 1** — Complete a discrete back-office task without babysitting
2. **Job 2** — Run a customer-facing conversation to resolution
3. **Job 3** — Execute a multi-step coding change including PR review and merge
4. **Job 4** — Operate a SaaS application on the user's behalf
5. **Job 5** — Stay current on a domain and act on what changes
6. **Job 6** — Pass agent-specific enterprise procurement and risk review **[PRIORITY — feeds Bet #1]**
7. **Job 7** — Onboard or ramp a new role using an agent-augmented training stack

V1's 6 jobs and V3's 7 jobs are NOT a 1:1 remap. V1 jobs were ecosystem-of-the-AI-field; V3 jobs are ecosystem-of-the-agent. Cross-walk: V3 Job 6 ≅ V1 Job 4 (procurement); other jobs are V3-specific.

### 3.5 The 7 Big Bets — agent-layer refresh (from `AI_AGENTS_TRACKER.md` §A)

Same 7 bets as Volume I, with deltas. The biggest sequencing change: **Bet #1 moves to first position** (was implicit third). Convictions:

1. **Bet #1** — Enterprise AI Procurement Operating Standard (agent-specific overlays) (★★★★★)
2. **Bet #2** — Vertical Agent GTM Leadership Role (★★★★★)
3. **Bet #3** — MCP-Native Enterprise Integration Practice — **REFRAMED** to advisory + gateway-adjacent (★★★★)
4. **Bet #4** — Inference Cost Optimization — **SPLIT** into per-token + per-trajectory FinOps (★★★★)
5. **Bet #5** — Enterprise RAG + Memory Architecture — **FOLDS memory in** (★★★★)
6. **Bet #6** — Operator's Translation Newsletter (★★★)
7. **Bet #7** — VC Operating Partner — fallback only (★★★ / ★★★★ contingent)

### 3.6 The 5 Structural Risks — agent layer

Same 5 as Volume I, with agent-specific framing. See Ch 3 §3.2 for the full treatments. Notable agent-layer specifics:
1. HBM4 / CoWoS-L slip (agent impact: per-trajectory cost surge)
2. Hyperscaler FCF reckoning (agent impact: vertical-agent valuation compression)
3. OpenAI Preparedness adjustment-clause activation
4. Federal preemption volatility on AI rules (agent impact: human-oversight regulation)
5. Foundation labs walking up-stack into vertical agents

### 3.7 The 5 Cruxes — agent layer

Same 5 as Volume I, with two agent-specific additions noted in the addendum:
1. **Anthropic ARR** — $24B or $30B? (load-bearing for Bet #2)
2. **Inference compute** — 10× growth or flat?
3. **MCP** — commons or fork? (load-bearing for Bet #3)
4. **EU AI Act Article 14** — human-oversight teeth or paper tiger?
5. **Long-term memory** — standalone or absorbed?

Plus the agent-specific Crux raised in HANDOVER_A: **OSWorld 65% on a frontier system (Q3 2026)** — re-rated as a sub-crux feeding Cruxes 2 and 5.

### 3.8 Glossary (agent-specific terms)

Volume I glossary carries over. Additions:

| Term | Definition |
|---|---|
| Agent runtime | Software framework that hosts the agent loop (perception, planning, action, observation) |
| MCP | Model Context Protocol — Anthropic-originated, Linux Foundation governed since Dec 2025 |
| Computer use | Agent action surface that operates a desktop OS via screenshots + mouse/keyboard |
| ReAct | Reasoning + Acting interleaved prompting pattern |
| Tree-of-thoughts (ToT) | Planning architecture that explores multiple reasoning branches |
| Trajectory | Full sequence of agent actions from goal to completion |
| Per-trajectory cost | Total inference cost across an entire agent execution (vs. per-token or per-call) |
| Action-confirmation gate | Procurement requirement: agent must confirm high-stakes actions before executing |
| Indirect prompt injection | Adversarial input arriving via tool output (vs. direct user input) |
| OSWorld | Computer-use agent benchmark — 65% threshold = reliable production deployment marker |
| WebArena | Browser-agent benchmark |
| Sub-agent privilege separation | Multi-agent architecture where downstream sub-agents run with reduced permissions |
| Planner-executor split | Architectural pattern: one model plans, a cheaper/faster model executes |
| Procurement rubric | The agent-specific section of the Bet #1 Playbook — see Ch 3 Appendix |
| ASL-4 | Anthropic's Responsible Scaling Policy Level 4 — capability threshold that triggers deployment-freeze obligations |

---

## 4. Output structure

```
output/ai-agents-v2/  →  becomes output/ai-agents/  at swap
├── _spec.md                          ← this file
├── _archive/                         ← original design philosophy, scaffolding
├── _extract/                         ← raw extracts, framework_analysis copies
├── chapters/
│   ├── 00_frame.md                   ← ~1,500 words
│   ├── 01_substrate.md               ← ~5,500 words (10 sub-strata + 4 meta)
│   ├── 02_frameworks.md              ← ~6,000 words (OCQ, Wardley, 7P, JTBD)
│   ├── 03_bets_risks_cruxes.md       ← ~4,500 words (7 bets refreshed + 5 risks + 5 cruxes + action map + procurement rubric)
│   ├── 04_tracker.md                 ← ~3,000 words (agent-layer living tracker)
│   ├── 05_rituals.md                 ← ~1,200 words (defers to V1 rituals; V3-specific add-ons)
│   └── 06_appendix.md                ← ~2,000 words (agent-specific glossary, sources, methodology)
├── plates/
│   ├── 01_agent_substrate_column.svg
│   ├── 02_agent_ocq_heatmap.svg
│   ├── 03_agent_wardley_map.svg
│   ├── 04_agent_powers_grid.svg
│   ├── 05_agent_cross_substratum_flows.svg
│   └── build_plates.py
├── build_epub.sh
└── AI_AGENTS_MASTER.epub
```

**Total target:** ~23,500 words + 5 plates.

---

## 5. Chapter scope (no overlap with Volume I)

### Ch 0 — Frame (~1,500 words)
Volume III positioning. Why zoom the agent layer. The cycle-time difference vs full-stack (12–24 month windows inside agent layer vs 18-month at full-stack). The three things V3 produces that V1 couldn't: per-sub-stratum opportunity rankings, tactical company-by-company target maps for Alex's profile, agent-specific procurement rubric. How to read alongside Volume I.

### Ch 1 — Agent Sub-Strata (~5,500 words)
10 sub-strata + 4 meta, same four-subheading structure as V1 Ch 1 (Position / What lives there / Binding constraints / Evolution stage / What changed in last 12 months). Stratum II includes the agent-runtime / SDK consolidation story; Stratum III owns the MCP timeline; Stratum IX is the heaviest section (vertical agent products by domain).

### Ch 2 — Framework Lenses (agent-tuned) (~6,000 words)
- §2.1 OCQ × Agent Sub-Stratum Matrix (~2,200 words) — score each of 14 sub-strata
- §2.2 Wardley Map of the agent stack (~1,200 words) — anchor needs are agent-jobs from §3.4
- §2.3 7 Powers across agent sub-strata (~1,000 words) — which powers cluster where
- §2.4 Ecosystem JTBD with 7 jobs (~1,200 words) — Job 6 priority lock
- §2.5 Talent & Capital Flow methodology — same as V1 §2.5, data lives in Ch 4

### Ch 3 — Bets, Risks, Cruxes (agent-layer refresh) (~4,500 words)
- §3.1 The 7 Big Bets — each one carries a "Delta from V1" subsection (~3,000 words)
- §3.2 5 Risks (agent-layer framing) (~500 words)
- §3.3 5 Cruxes + the OSWorld sub-crux (~500 words)
- §3.4 6/12/18-Month Action Map for Alex (~400 words)
- §3.5 Procurement Rubric appendix (NEW — Addendum Part XIII) (~200 words inline, with link to full rubric)
- Apply drill (~100 words)

### Ch 4 — Operating Tracker (agent-layer) (~3,000 words)
- §4.1 How to use + cadences (defers to V1 Ch 5 rituals)
- §4.2 Bets status with V3 deltas
- §4.3 Senior moves into agent-specific companies
- §4.4 Capital events ($50M+ agent platform rounds)
- §4.5 Agent-layer ARR watchlist
- §4.6 Public statements decoded (agent founders)
- §4.7 NYC agent-company snapshot
- §4.8 Cruxes status (with OSWorld sub-crux)
- §4.9 Risks status
- §4.10 Update log

### Ch 5 — Operating Rituals (V3 add-ons) (~1,200 words)
Defers most rituals to V1 Ch 5. Adds the V3-specific rituals:
- §5.1 V3 quarterly: re-check the V3-V1 deltas — are any bet reframes (esp. Bet #3) ready to fold back into V1 as the parent framing?
- §5.2 V3 trigger-based: OSWorld benchmark monitoring; ASL-4 announcement watch; major MCP governance events
- §5.3 V3 twice-yearly: composability audit with Volume IV (GTM) once that lands

### Ch 6 — Appendix (~2,000 words)
Agent-specific glossary (extends V1 §6.1), agent-specific sources, methodology notes (why 7 JTBD jobs not 6, why memory folded into Bet #5, why Bet #3 was reframed), update protocol (defers to V1 §6.4 + V3 add-ons), change log.

---

## 6. Plate inventory (5 plates)

### Plate 1 — Agent Substrate Column
- Owns: vertical ordering of 14 agent sub-strata + binding constraints + evolution stage tag
- Earns place because: spatial stacking shows agent-layer dependency direction
- Inputs: Ch 1

### Plate 2 — Agent OCQ Heatmap (14 × 3)
- Owns: aggregate O/C/Q intensity per sub-stratum
- Inputs: Ch 2 §2.1

### Plate 3 — Agent Wardley Map
- Owns: 2D positioning by evolution × value chain for agent-stack components
- Inputs: Ch 2 §2.2

### Plate 4 — Agent Powers × Sub-Stratum Grid
- Owns: 7 powers held at which sub-strata + trajectory
- Inputs: Ch 2 §2.3

### Plate 5 — Agent Cross-Sub-Stratum Flows
- Owns: dependency edges + agent-specific risk-propagation paths + bet coupling
- Inputs: Ch 1 binding constraints + Ch 3 risks + bet coupling
- Replaces the unreadable AI_AGENTS_MASTER_PLATE.pdf

---

## 7. Style rules (binding — same as V1 §7)

Educational register, declarative, no literary flourish. Plain prose, dashes for lists, bold for lead-ins, markdown tables, no emoji. Cross-references "(Ch X §X.Y)" or "(Plate N)". When referencing the parent volume, use "(V1 Ch X §X.Y)" — the "V1" prefix is explicit so the reader knows when they need to open the other workbook.

---

## 8. Plate style rules (binding — same as V1 §8)

Black on white, sans-serif, one accent color (the same dark blue `#1d4ed8` as Volume I — visual continuity across the volumes).

---

## 9. Build pipeline (identical to V1 §9)

```
1. Edit chapters/*.md
2. Run python plates/build_plates.py if data changed
3. Run bash build_epub.sh → AI_AGENTS_MASTER.epub
```

---

## 10. Update protocol

Defers to V1 Ch 5 rituals for cadence. Volume III is updated alongside Volume I — when a monthly conviction ritual fires in V1, it also fires in V3 if any agent-layer delta has moved. The trigger-based path is the most-used in V3 (OSWorld benchmark, MCP governance, ASL-4 events).

---

## 11. Open items (resolved at swap)

- [x] Folder strategy: build in `ai-agents-v2/`, swap at end (same pattern as V1).
- [x] EPUB builder: pandoc, identical script structure.
- [x] Plate 5: keep as Agent Cross-Sub-Stratum Flows (replaces unreadable Master Plate).
- [x] Exercises: defer most to V1 Ch 5; V3 Ch 5 owns V3-specific rituals only.

---

## 12. Change log

| Date | Version | Change |
|---|---|---|
| 2026-05-20 | 1.0 | Initial V3 consolidation; built on top of V1 Ch 5 rituals; absorbed AI_AGENTS_REPORT + ADDENDUM + TRACKER + READTHROUGH + 11 plates into 7 chapters + 5 plates + EPUB. |
