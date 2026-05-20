# AI Stack Master — Canonical Spec

**Version:** 1.0 (draft for review)
**Date:** 2026-05-20
**Owner:** Alex Yedi
**Purpose:** Single source of truth for the AI Stack consolidation. Every chapter writer and every plate generator reads this file first. Names, numbering, lens definitions, and terminology defined here are canonical. Changes happen here, then propagate to `chapters/*.md` and `plates/*`.

---

## 1. Goal of this artifact

A single readable workbook — markdown source + EPUB export — that consolidates the AI-stack thesis Alex is acting on. Replaces the scattered pile of `AI_STACK_REPORT.docx`, `AI_STACK_ADDENDUM.docx`, `OCQ_TRACKER.md`, `HANDOVER_*.md`, and 12 unreadable matplotlib plates.

**Design posture:** educational density, not aesthetic homage. The "Substrate" visual philosophy is archived. Plates earn their place only when they carry information prose can't (positional, comparative, or pattern-revealing). Polished design-to-delight is deferred to the future "growth engineering" public-facing surface.

**Operating posture:** living workbook. Markdown is the editable source of truth; EPUB is a regenerable read-anywhere export. Update cadence is locked in §10.

---

## 2. Source materials (read-only inheritance)

Located in `../ai-stack/`:

| File | Role | Disposition |
|---|---|---|
| `AI_STACK_REPORT.docx` (~8.5k words) | Foundation prose, 14 strata + 4 meta | Source for Ch 1; extract done |
| `AI_STACK_ADDENDUM.docx` (~18.7k words, Parts VI–XII) | Frameworks + 7 Bets + Action Map | Source for Ch 2, 3; extract done |
| `OCQ_TRACKER.md` | Living tracker (bets, talent, capital, ARR, cruxes, risks) | Source for Ch 4 |
| `design_philosophy.md` | Substrate aesthetic philosophy | Archive; not used |
| `HANDOVER_A_AGENTS.md` | Brief for downstream agent-layer session | Archive; cross-session scaffolding, not for Alex |
| `HANDOVER_B_AGENTS_GTM.md` | Brief for downstream GTM-layer session | Archive |
| `AI_STACK_SUBSTRATE.pdf` Vol I (6 plates) | Decorative + informational mix | Source for Plate 1 redesign |
| `AI_STACK_SUBSTRATE_VOL2.pdf` Vol II (5 plates) | OCQ heat, Wardley, 7 Powers, JTBD, Action Portfolio | Source for Plates 2–4 redesign |
| `AI_STACK_MASTER_PLATE.pdf` | Master synthesis (the unreadable one) | Source for Plate 5 redesign at much lower density |
| `build_*.py` / `build_*.js` | Original generators | Reference only; new pipeline replaces |

---

## 3. Canonical taxonomy

### 3.1 The 18 strata

Numbered I–XIV plus four meta-strata A–D. Numbering and names match `AI_STACK_REPORT.docx` so cross-references in `OCQ_TRACKER.md` (e.g. "Stratum IX/Meta-B/Meta-C", "Stratum X 15/15") remain valid.

**Part I — Power and Facility**
- **Stratum I — Power** (the grid, PPAs, nuclear restarts, transformer lead times)
- **Stratum II — Facility** (hyperscale DC, liquid cooling, 132kW → 600kW racks)

**Part II — Compute and Networking**
- **Stratum III — Compute** (GPUs/TPUs/custom silicon, Blackwell, Rubin)
- **Stratum IV — Fabric** (NVLink, InfiniBand, optical interconnect)
- **Stratum V — Parallelism** (training/inference parallelism strategies, MFU)

**Part III — Data, Pretraining, Post-training**
- **Stratum VI — Data** (corpora, licensing, synthetic, web-vs-licensed mix)
- **Stratum VII — Pretraining** (training runs, MoE, scaling laws state)
- **Stratum VIII — Post-training** (RLHF/DPO/RLVR/GRPO, alignment training)

**Part IV — Inference, Middleware, Application**
- **Stratum IX — Model Providers** (Anthropic, OpenAI, Google, Meta, DeepSeek, Mistral)
- **Stratum X — Inference Engines** (vLLM, SGLang, TensorRT-LLM, FP8/FP4 quantization, speculative decoding)
- **Strata XI–XII — Retrieval, Memory, Orchestration** (handled jointly: vector DBs, rerankers, RAG, GraphRAG, LangGraph/LlamaIndex/DSPy/Mastra/Vercel AI SDK)
- **Stratum XIII — Application Layer** (vertical agent products, AI-native SaaS)
- **Stratum XIV — The User** (end-user surfaces: chat, voice, IDE, browser, mobile)

**Part V — The Meta-Strata** (wrap the whole column)
- **Meta-A — Safety and Alignment**
- **Meta-B — Regulation** (EU AI Act, US sectoral, CA SB 53, federal preemption)
- **Meta-C — Economics** (capex, FCF, unit economics, inference cost curves)
- **Meta-D — Geopolitics** (export controls, Stargate, Gulf/India/EU sovereign AI)

> **Note on XI–XII:** The original report treats Retrieval, Memory, and Orchestration as one combined band. Preserve that framing — do not renumber.

### 3.2 The 5 frameworks (Ch 2 lenses)

| # | Framework | What it does | Source |
|---|---|---|---|
| 1 | **OCQ × Layer Matrix** | Score each stratum on Opportunity, Challenge, Open Question | Original to this work |
| 2 | **Wardley Mapping** | Position components by evolution × value chain | Simon Wardley |
| 3 | **Helmer's 7 Powers** | Identify durable strategic powers per layer | Hamilton Helmer |
| 4 | **Ecosystem JTBD** | 6 ecosystem-level jobs, 8-phase map per job | Christensen / Ulwick / Bettencourt |
| 5 | **Talent & Capital Flow** | Empirical signal layer; tracker-driven | Original to this work |

### 3.3 OCQ lens definitions (verbatim from Addendum Part VI)

**OPPORTUNITY** — Where is value being created faster than the field's prevailing narrative reflects. Specifically: structural inefficiency, underserved jobs-to-be-done, mispriced talent, mispositioned distribution. Not "things that are good." Scored 1–5 on three dimensions:
- **Confidence** (how sure we are)
- **Time-to-Monetize** (5 = soon)
- **Claimability for Alex** (can someone with enterprise B2B GTM + AI-builder fluency act on it)

Total: /15.

**CHALLENGE** — The binding constraint or latent feedback loop that, if it tightens or fires, materially reprices everything above it. Not "things that are hard"; things that bind. Scored:
- **Severity** (how much it reprices)
- **Probability** (likelihood it bites)
- **Alex Exposure** (how much it affects his bets specifically)

Total: /15.

**OPEN QUESTION** — A crux the field is betting on without admitting it; an answer would change other answers. Phrased as actual questions. Scored:
- **Decidability Horizon** (5 = decidable soon)
- **Answer-Asymmetry** (how much bets diverge based on the answer)
- **Bet-Size Implication** (how much the playbook would shift)

Total: /15.

> **Score discipline note (from the prior session's lessons):** Resist 15/15 grade inflation. The lens definitions exist to produce a distribution, not validation.

### 3.4 The 6 ecosystem JTBD jobs (Addendum Part IX)

1. **Job 1** — Run a complete enterprise sales motion using AI as primary leverage
2. **Job 2** — Build, ship, instrument, and iterate an AI-native product as a small team
3. **Job 3** — Stay current on the AI ecosystem and act on it
4. **Job 4** — Pass enterprise procurement, security, and compliance review for an AI vendor **[PRIORITY]**
5. **Job 5** — Recruit, evaluate, and ramp talent in AI-native roles
6. **Job 6** — Govern AI usage across an enterprise

Each job carries an 8-phase Job Map (Define → Locate → Prepare → Confirm → Execute → Monitor → Modify → Conclude) and top-3 underserved outcomes in the addendum source.

### 3.5 The 7 Big Bets (from `OCQ_TRACKER.md` §A)

1. **Bet #1** — The Enterprise AI Procurement Operating Standard (★★★★★)
2. **Bet #2** — Vertical Agent GTM Leadership Role (★★★★★)
3. **Bet #3** — MCP-Native Enterprise Integration Practice (★★★★)
4. **Bet #4** — Inference Cost Optimization / FinOps for Tokens (★★★★)
5. **Bet #5** — Enterprise RAG Architecture Practice (★★★★)
6. **Bet #6** — Operator's Translation Newsletter / Public Voice (★★★)
7. **Bet #7** — VC Operating Partner / Platform Path (★★★ / ★★★★ contingent)

Hypothesis, falsifiability, conviction, leading indicators, and next action live in Ch 3; status updates live in Ch 4.

### 3.6 The 5 Structural Risks (`OCQ_TRACKER.md` §D)

1. HBM4 / CoWoS-L slip
2. Hyperscaler FCF reckoning
3. OpenAI Preparedness adjustment-clause activation
4. Federal preemption volatility on AI rules
5. Foundation labs walking up-stack into vertical apps

### 3.7 The 5 Cruxes (`OCQ_TRACKER.md` §C)

1. **Anthropic ARR** — $24B or $30B? (Q2–Q3 2026)
2. **Inference compute** — 10× growth or flat? (2026 Q4 hyperscaler earnings)
3. **MCP** — commons or fork? (H2 2026)
4. **EU AI Act** — teeth or paper tiger? (Late 2026 enforcement)
5. **Long-term memory** — standalone or absorbed? (12–18 months)

### 3.8 Glossary (canonical terms used across chapters/plates)

| Term | Definition |
|---|---|
| MFU | Model FLOPs Utilization — fraction of theoretical FLOPs achieved during a training run |
| MoE | Mixture of Experts — sparse activation architecture |
| MCP | Model Context Protocol — Anthropic-originated tool-use standard, donated to Linux Foundation Dec 2025 |
| RLVR | Reinforcement Learning from Verifiable Rewards |
| GRPO | Group Relative Policy Optimization |
| OCQ | Opportunity / Challenge / Open Question — the matrix lens |
| ARR | Annual Recurring Revenue |
| GPAI | General-Purpose AI (EU AI Act term) |
| Stratum / strata | A horizontal layer in the AI stack; numbered I–XIV plus Meta A–D |
| Crux | An unresolved question whose answer re-ranks every bet |
| Bet | A named opportunity Alex is choosing to pursue or hold |

---

## 4. Output structure

```
output/ai-stack-v2/
├── _spec.md                          ← this file (canonical)
├── _archive/                         ← original handovers, design philosophy
├── _extract/                         ← raw extracts from .docx (for chapter writers)
├── chapters/
│   ├── 00_frame.md                   ← ~1,500 words
│   ├── 01_substrate.md               ← ~5,500 words (the 18 strata)
│   ├── 02_frameworks.md              ← ~6,000 words (OCQ, Wardley, 7P, JTBD)
│   ├── 03_bets_risks_cruxes.md       ← ~4,000 words (7 bets, 5 risks, 5 cruxes, action map)
│   ├── 04_tracker.md                 ← ~3,500 words (living tracker, cleaned)
│   ├── 05_exercises.md               ← ~1,500 words
│   └── 06_appendix.md                ← ~2,000 words (glossary, sources, methodology, update protocol)
├── plates/
│   ├── 01_substrate_column.svg
│   ├── 02_ocq_heatmap.svg
│   ├── 03_wardley_map.svg
│   ├── 04_powers_layer_grid.svg
│   ├── 05_cross_stratum_flows.svg
│   └── build_plates.py
├── build_epub.sh                     ← pandoc assembly
└── AI_STACK_MASTER.epub              ← regenerable artifact
```

**Total target:** ~24,000 words of prose + 5 plates. Down from ~27,000 words across 4 docs + 12 cluttered plates.

---

## 5. Chapter scope (what each chapter owns; no overlap)

### Ch 0 — Frame (~1,500 words)
- One-paragraph thesis (the operator's-translation conclusion from the original report)
- Alex's profile in 5 lines (12y enterprise B2B + AI builder + NYC + active search + writes/translates)
- Why this document exists (operating substrate for next 18 months of bets)
- How to use this doc (reading paths: full read; framework-only; tracker-only; exercise-only; monthly update ritual)
- Pointers to other chapters

### Ch 1 — The Substrate (~5,500 words)
- 200-word intro: why stratify the AI stack
- One section per stratum (I–XIV + Meta A–D), each ~250–350 words:
  - **Position:** what it is, what it depends on, what depends on it
  - **What lives there:** named players + binding metrics
  - **Binding constraints:** what limits scaling at this layer
  - **Evolution stage:** Genesis / Custom / Product / Commodity (Wardley) + 1-line justification
  - **What changed in the last 12 months:** 2–3 datapoints with dates
- Plate 1 (Substrate Column) is the visual key

### Ch 2 — Framework Lenses (~6,000 words)
- **§2.1 OCQ × Layer Matrix** (~2,200 words): lens definitions (from §3.3); per-stratum top opportunity / challenge / open question with scores. Plate 2 visualizes the score grid.
- **§2.2 Wardley Mapping** (~1,200 words): anchor needs, dependency chains, evolution placements, 5 punctuated equilibria expected. Plate 3 is the map.
- **§2.3 Helmer's 7 Powers** (~1,000 words): per-stratum power inventory, durable vs eroding. Plate 4 is the powers-layer grid.
- **§2.4 Ecosystem JTBD** (~1,200 words): the 6 jobs (§3.4), top-3 underserved outcomes per job, cross-job synthesis. No new plate — tables only.
- **§2.5 Talent & Capital Flow** (~400 words): methodology (cadence, sources, signal-vs-noise rules). Data lives in Ch 4.

### Ch 3 — Big Bets, Risks, Cruxes (~4,000 words)
- The 7 Big Bets (§3.5): each gets a one-page treatment — hypothesis, falsifiability, conviction, leading indicators, next action, links to relevant strata & frameworks
- The 5 Structural Risks (§3.6): each gets ~150 words — what triggers it, what it threatens, what to watch
- The 5 Cruxes (§3.7): each gets ~150 words — the question, the answer-event, the re-rank consequence
- **§3.4 Action Map** (~600 words): 6 / 12 / 18-month horizon synthesis. Bullet-list per horizon.
- Plate 5 (Cross-Stratum Flows) shows bet-coupling and risk-propagation

### Ch 4 — Operating Tracker (~3,500 words)
The living tracker — same content as `OCQ_TRACKER.md` but cleaned, with HOW-TO-USE moved up front. Sections:
- **§4.1 How to use & update cadences**
- **§4.2 Bets status board** (re-rated monthly)
- **§4.3 Senior frontier talent moves** (rolling 12mo, updated bi-weekly)
- **§4.4 Capital events** ($100M+ rounds, M&A, infra commits)
- **§4.5 ARR watchlist**
- **§4.6 Public statements decoded**
- **§4.7 NYC snapshot** (companies, events, people)
- **§4.8 Cruxes status** (when answered, log the date)
- **§4.9 Risks status** (quarterly re-check)
- **§4.10 Update log**

### Ch 5 — Operating Rituals (~1,500 words)
Per the "both" decision: chapter-end drills live inline at the end of Ch 1–4; Ch 5 owns the cross-chapter rituals tied to time cadence.
- **§5.1 Weekly reflection prompts** (3 prompts, ~2 min each): "what did you hear this week that re-priced any bet?"; "what crux moved?"; "what conversation could you have had that you didn't?"
- **§5.2 Monthly conviction ritual** (15 min): re-rate each bet ★★★–★★★★★; mark which leading indicators moved; tag any crux that fired
- **§5.3 Quarterly deep review** (60 min): re-read frameworks; check for grade-inflation drift; rotate inline drills; consider archive/version bump
- **§5.4 Twice-yearly major refresh** (half-day): re-extract from new source material, regenerate plates, version bump _spec

**Inline drills (own subsection at the end of Ch 1–4):**
- Ch 1 "Apply": pick three strata you couldn't explain to a buyer; write a 2-sentence explanation of each
- Ch 2 "Apply": score one new opportunity against the OCQ lens; place one new player on the Wardley map
- Ch 3 "Apply": re-rate one bet's conviction with explicit reasoning; identify which leading indicator you actually saw move this month
- Ch 4 "Apply": add one new talent move and one new capital event from the last 14 days

### Ch 6 — Appendix (~2,000 words)
- **§6.1 Glossary** (from §3.8)
- **§6.2 Sources & further reading** (companies, reports, newsletters, primary docs)
- **§6.3 Methodology notes** (scoring scales, framework definitions, why XI–XII are combined)
- **§6.4 Update protocol** (which sections update when, how to bump version)
- **§6.5 Change log** (this doc's own version history)

---

## 6. Plate inventory (5 plates, each must earn its place)

### Plate 1 — Substrate Column
- **Owns:** vertical ordering of 18 strata + binding constraints + evolution-stage tag per stratum.
- **Earns place because:** the column geometry is the information; spatial stacking shows dependency direction.
- **Inputs:** Ch 1 (all strata).
- **Format:** single SVG, portrait orientation. Plain black-on-white. Sans-serif labels.

### Plate 2 — OCQ Heatmap (18 × 3)
- **Owns:** aggregate Opportunity / Challenge / Open Question intensity per stratum.
- **Earns place because:** pattern-scanning across 54 cells is hostile to prose.
- **Inputs:** Ch 2 §2.1 scores.
- **Format:** 18-row × 3-column grid, cell shade = aggregate score, small numeric label.

### Plate 3 — Wardley Map
- **Owns:** 2D positioning of components by evolution × value chain.
- **Earns place because:** position **is** the framework; degenerates to nonsense in prose.
- **Inputs:** Ch 2 §2.2.
- **Format:** annotated 2D map, ~30–50 nodes, dependency lines.

### Plate 4 — 7 Powers × Layer Grid
- **Owns:** which of Helmer's 7 powers exist at which strata + trajectory (strengthening / eroding).
- **Earns place because:** cross-strata power clusters and barrens become visible.
- **Inputs:** Ch 2 §2.3.
- **Format:** 7-col × 18-row matrix; cell marker shows holder + arrow for trajectory.

### Plate 5 — Cross-Stratum Flows
- **Owns:** 5–7 critical cross-strata dependencies + the 5 risk-propagation paths.
- **Earns place because:** directed graph of coupling is unreadable in prose.
- **Inputs:** Ch 1 binding constraints, Ch 3 risks, Ch 3 bet coupling.
- **Format:** directed graph; small number of edges, each labeled. Replaces the unreadable original Master Plate.

**Cut from the original 12 plates:** decorative stratigraphic styling, design-tradition motifs, the dense Master Plate. JTBD canvas demoted to a markdown table (didn't earn the plate slot).

---

## 7. Style rules (binding on all writers)

- **Register:** educational, declarative, direct. Short sentences over long. No "the work proceeds through accumulation" register. The original report's literary tone is archived along with the visual philosophy.
- **Headings:** `# Chapter`, `## Section`, `### Subsection`. No `####`.
- **Citations:** inline parenthetical (Source, YYYY-MM). Full sources in Ch 6 §6.2.
- **Numbers:** always with units and dates. "$300M Q1 2026", not "around 300M".
- **Tables:** native markdown. Never an image-of-table.
- **Lists:** dashes (`-`), not asterisks. Keep nested levels ≤ 2.
- **Bold:** for term-definition lead-ins and bet/risk/crux names. Sparingly otherwise.
- **No filler:** no "in summary", "as we've seen", "it's important to note". Trust the reader.
- **No emoji.**
- **Cross-references:** by chapter+section, e.g. "(see §2.3)" or "(Ch 4 §4.5)". Plates referenced as "Plate 3" with no further decoration.

---

## 8. Plate style rules

- Black on white. One accent color allowed (functional, e.g. trajectory arrows). No textures, gradients, paper grain.
- Sans-serif (system default; no custom font loading). Type sizes legible at half-page print.
- Labels are labels. No marginalia, ornament, or "curator's notes."
- Each plate has: title, one-line subtitle (what it shows), small legend, source caption.
- Vector (SVG) is canonical. PNG export only when SVG can't render (none expected).
- The plate must answer: *"What would the reader miss if this were prose only?"* If "nothing meaningful" — kill the plate.

---

## 9. Build pipeline

```
1. Edit `chapters/*.md` directly.
2. Edit plate specifications (data + structure) in `plates/build_plates.py`.
3. Run `python plates/build_plates.py` → regenerates all SVGs.
4. Run `bash build_epub.sh` → pandoc assembles chapters + plates → AI_STACK_MASTER.epub.
5. Markdown source is canonical. EPUB is regenerable.
```

**Toolchain dependencies:** Python 3 + matplotlib (existing), pandoc (install once via Homebrew). No node_modules. Optional: Sigil for manual EPUB polish before sharing — the pandoc build is the regenerable pipeline, Sigil is a one-off polish surface that does not get committed back to source.

---

## 10. Update protocol

| Cadence | What updates | Where | Owner |
|---|---|---|---|
| **Bi-weekly** | Talent moves, capital events | Ch 4 §4.3, §4.4 | Alex |
| **Monthly** | Bet status, conviction, leading indicators | Ch 3, Ch 4 §4.2 | Alex |
| **Trigger-based** | Crux resolved, risk fired | Ch 4 §4.8, §4.9 | Alex |
| **Quarterly** | Risk re-check, exercise rotation, score-discipline audit | Ch 3, Ch 5 | Alex |
| **Major (twice a year)** | Re-extract from new source material, regenerate plates, version bump | All | Alex |

---

## 11. Open items (resolve before parallel build kickoff)

- [x] **Folder strategy.** Build in `ai-stack-v2/`. Final step: archive existing `ai-stack/` (move to sibling backup), then rename `ai-stack-v2/` → `ai-stack/`. End-state path is `output/ai-stack/`. (Resolved 2026-05-20.)
- [x] **EPUB builder.** Pandoc primary (`pandoc chapters/*.md -o AI_STACK_MASTER.epub --toc --metadata ...`). Sigil reserved for optional manual polish before sharing; not in the regenerable pipeline. (Resolved 2026-05-20.)
- [x] **Plate 5.** Keep as Cross-Stratum Flows. Replaces the unreadable Master Plate at lower density. (Resolved 2026-05-20.)
- [x] **Exercises placement.** Both — inline "Apply" drills at end of Ch 1–4, plus Ch 5 owns cross-chapter time-cadence rituals (weekly/monthly/quarterly/twice-yearly). (Resolved 2026-05-20.)

---

## 12. Change log

| Date | Version | Change |
|---|---|---|
| 2026-05-20 | 1.0 | Initial draft for Alex's sanity check |
