# AI Agents × GTM Master — Canonical Spec (Volume IV)

**Version:** 1.0 (draft)
**Date:** 2026-05-20
**Owner:** Alex Yedi
**Parents:** `output/ai-stack/_spec.md` (V1/II — full stack) + `output/ai-agents/_spec.md` (V3 — agent layer)
**Purpose:** Single source of truth for the Volume IV consolidation. Zooms the agents × GTM intersection to **cell-resolution** — 12 GTM functions × 13 agent capabilities = 156 cells. Companion artifact: the published AI Vendor Procurement Playbook (Bet #1 deliverable).

---

## 1. Goal of this artifact

Two artifacts in one folder:

1. **AGENTS_GTM_MASTER.epub** — internal workbook (Ch 0–6). The analytical layer. Consolidates the existing `AGENTS_GTM_ADDENDUM.md`, `AGENTS_GTM_TRACKER.md`, `BETS_DELTA_NOTE.md`, wave1/wave2 framework files, and the visual atlases into one readable workbook.

2. **AI_VENDOR_PROCUREMENT_PLAYBOOK.epub** — externally-facing artifact (Bet #1 deliverable). Polished form of `PLAYBOOK_part_A/B/C.md`. Different audience (F1000 procurement counterparties), different update cadence, different governance.

**Design posture:** identical to V1/V3 — educational density, plates earn their place, no aesthetic homage. V4 adds one structural innovation: **cell-coordinate notation** `(function#, capability_letter)` recurs throughout the workbook. Glossary anchors the notation.

**Operating posture:** V4 is a sub-tracker of V3 (which is a sub-tracker of V1). Conviction or cell-status changes here propagate up through V3's monthly ritual to V1 Ch 4.

**Relationship to V1/V3:** V4 COMPOSES on top of both. The 7 bets carry forward with explicit V4 deltas (mostly: things get sequenced, modules get folded, the cell matrix surfaces 10 candidate Bet-C's of which 3 promoted and 7 absorbed). Do not re-derive V1 or V3 analysis here.

---

## 2. Source materials

In `../agents-gtm/`:

| File | Role | Disposition |
|---|---|---|
| `AGENTS_GTM_ADDENDUM.md` (~30k words) | Parts VI–XI: Methodology + OCQ × Cell Matrix + Wardley + 7 Powers + JTBD + Synthesis | Source for Ch 1, 2, 3 |
| `AGENTS_GTM_TRACKER.md` (~5k words) | Living tracker, cell-resolution | Source for Ch 4 |
| `BETS_DELTA_NOTE.md` (~4k words) | Per-bet deltas back to V1+V3 | Source for Ch 3 §3.1 |
| `PLAYBOOK_part_A/B/C.md` (~190k words) | The published Procurement Playbook | Source for the PLAYBOOK EPUB |
| `AI_VENDOR_PROCUREMENT_PLAYBOOK.md` (~190k words) | Polished form of the playbook | Cross-check with parts A/B/C |
| `wave1_synthesis.md` | Phase 2a synthesis with the unified cell map | Source for Ch 1 |
| `wave1_C1.md`–`wave1_C6.md` | OCQ per bucket of functions (1–12 grouped) | Source for Ch 2 §2.1 |
| `wave2_F1_wardley.md` / `F2_seven_powers.md` / `F3_jtbd.md` | Framework analyses (cell-resolution) | Source for Ch 2 §2.2–§2.4 |
| `AGENTS_GTM_MASTER_READTHROUGH.md` (~80k words) | Linear read-through narration | Reference for register |
| 5 source PDFs (Decisions, Master Plate, Substrate, Matrix) | Plate sources | Source for plate redesign |
| `wave1_F4.md` / `F5.md` / `F6.md` | Phase 1 buckets (companies/products/economics) | Reference data |
| `wave1_playbook_draft.md` (~9.7k words) | Earlier playbook draft | Reference; superseded by PLAYBOOK_part_A/B/C |

Parents:
- V1 — `output/ai-stack/` (full-stack thesis, master rituals)
- V3 — `output/ai-agents/` (agent-layer zoom, agent-specific overlays)

---

## 3. Canonical taxonomy

### 3.1 The 12 GTM functions (rows of the cell matrix)

1. **Demand-gen / brand**
2. **Content / SEO**
3. **Inbound / PLG**
4. **Outbound SDR**
5. **Account-based marketing (ABM)**
6. **New-business AE**
7. **Enablement / training**
8. **RevOps / Sales Ops**
9. **Deal-desk / pricing / procurement** — *the cell of record* (9, G) scores 19/20
10. **Customer success / onboarding**
11. **AM / renewals / expansion**
12. **Forecasting / strategy**

### 3.2 The 13 agent capabilities (columns of the cell matrix)

- **A** — Research / enrichment
- **B** — Personalization + content
- **C** — Multi-channel orchestration
- **D** — Conversation handling
- **E** — Meeting prep / listen / follow-up
- **F** — CRM hygiene / graph
- **G** — Multi-step task execution
- **H** — Forecasting / decision support
- **I** — Negotiation / pricing
- **J** — Coaching / performance
- **K** — Computer-use
- **L** — Persistent memory
- **M** — Trajectory observability

Cell notation: `(function#, capability_letter)`, e.g. `(9, G)` = deal-desk × multi-step execution.

### 3.3 The 5 frameworks (same as V1/V3, applied at cell resolution)

OCQ × Cell Matrix, Wardley, 7 Powers, Ecosystem JTBD (5 GTM-org jobs in V4), Talent & Capital Flow.

### 3.4 OCQ lens definitions (same as V1, scored /20 not /15 at V4)

Note: V4 uses a /20 scale not /15. This is because the cell-matrix resolution surfaces a fourth dimension — Density (how dense the vendor landscape is at this cell). Each lens scored 1–5 on four dimensions:

- **OPPORTUNITY**: Confidence × Time-to-Monetize × Claimability × Density
- **CHALLENGE**: Severity × Probability × Alex Exposure × Time-Sensitivity
- **OPEN QUESTION**: Decidability × Asymmetry × Bet-Size × Cell-Coverage (how many cells the answer re-rates)

Each total /20.

### 3.5 The 5 GTM-org JTBD jobs (Addendum Part X)

Different from V3's 7 agent-workflow jobs. V4 jobs are GTM-organization-shape:

1. **Job 1** — Hit the number this quarter
2. **Job 2** — Hit next year without doubling headcount
3. **Job 3** — Make the GTM motion legible (forecast, attribution, accountability)
4. **Job 4** — Defend net revenue retention (renewals, expansion)
5. **Job 5** — Stay current and act on what changes in the field

Cross-walk to V3's 7 agent-jobs is in the addendum Part X.5.

### 3.6 The 7 Big Bets — V4 cell-resolution refresh (from `BETS_DELTA_NOTE.md`)

The seven bets carry from V1/V3 with V4 deltas:

1. **Bet #1** — Enterprise AI Procurement Operating Standard — **REINFORCED + EXPANDED**. Anchor cell (9, G) = 19/20. Seven counterparties (was six in V3). Modules absorbed from Bets #4 and #5. (★★★★★)
2. **Bet #2** — Vertical Agent GTM Leadership Role — **SHARPENED**. Hebbia #1 ranked composite NYC target; MBB-network feed-stock activated Feb–Apr 2026. (★★★★★)
3. **Bet #3** — MCP-Native Practice — **SPLIT INTO 3a + 3b**. 3a (advisory + gateway-partner) runs CONCURRENT with Bet #1 from H2 2026. 3b (productized servers) remains parked. (★★★★ for 3a)
4. **Bet #4** — Inference Cost Optimization — **SUBSUMED into Bet #1 as a module** (the per-trajectory FinOps audit overlay).
5. **Bet #5** — RAG / Memory Architecture — **SUBSUMED standalone + Bet-C9 PROMOTED**. Memory as service line repositioned as Q3 2026 productization vector after Playbook earns trust.
6. **Bet #6** — Operator's Translation Newsletter — **CONFIRMED as distribution layer** for Bets #1–#3.
7. **Bet #7** — VC Operating Partner — fallback (★★★ / ★★★★ contingent).

### 3.7 The candidate Bet-C's (synthesis surfaced 10; 3 promoted, 7 absorbed)

From `wave1_synthesis.md §5` and Addendum XI.4:

**Promoted to active candidates:**
- **Bet-C5** — Common Room senior PMM/GTM operator path (sub-target under Bet #2)
- **Bet-C8** — Deal-Diagnosis Causation Engine (operator-target if credible startup emerges at (6, E))
- **Bet-C9** — Persistent Memory as Service Line (Q3 2026 productization decision vector under Bet #5)

**Absorbed / parked:**
- Bet-C1 (folded into Bet #1)
- Bet-C2 procurement-seam coach (follow-on to Bet #1)
- Bet-C3 extended per-trajectory FinOps (Bet #1 module)
- Bet-C4 outcome-pricing contract template (Bet #1 module)
- Bet-C6 open-spec stewardship (Bet #1 reframe)
- Bet-C7 (parked)
- Bet-C10 Article 14 tie-out standard (Bet #1 module)

### 3.8 The 5 Risks (carry from V1/V3 with cell-resolution framing)

Same 5 as V1. V4 framing emphasizes cell-coverage: each risk threatens specific cells. Example: Risk 4 (Federal preemption volatility) threatens all M-column cells (trajectory observability) because state-vs-federal divergence reshapes audit requirements.

### 3.9 The 6 Cruxes (V4 adds one new beyond V3's 5)

1. **Anthropic ARR** — $24B or $30B?
2. **Inference compute** — 10× growth or flat?
3. **MCP** — commons or fork?
4. **EU AI Act Article 14** — teeth or paper tiger?
5. **Long-term memory** — standalone or absorbed?
6. **(NEW V4)** — **Outcome-based pricing economics — sustainable or vapor?** Triggered by Klarna reversal, Sierra/Decagon outcome-pricing experiments, SOX rev-rec risk. Decidability horizon: Q4 2026.

Plus the V3 OSWorld sub-crux carries forward (now feeds Cruxes 2 + 5 + the new pricing crux).

### 3.10 Glossary additions

V4-specific terms layered on V1+V3 glossary:

| Term | Definition |
|---|---|
| Cell | A function × capability intersection in the 12 × 13 matrix |
| Cell of record | (9, G) — agent procurement gauntlet — the highest-OCQ cell at 19/20 |
| Bet-C | Candidate bet surfaced by Wave 2 synthesis; either promoted (C5/C8/C9) or absorbed |
| Seven counterparties | The F1000 AI procurement gauntlet: InfoSec, Legal, Privacy, AI Governance, Procurement, Business Sponsor, Enterprise Architecture / IT Ops |
| Bilateral evidence pack | The signed reproducible eval report format that becomes the canonical Playbook artifact |
| Gateway control plane | Cloudflare / Kong / Pomerium — where Bet #3a's Switching Costs power lives |
| MBB feed-stock | Berger BCG → Hebbia, Park McKinsey → Sierra, Sinclair Bain → Harvey — the third career-feed-stock for Bet #2 (after Stripe/Ramp/Datadog and foundation-lab AE departures) |
| Open-spec stewardship | The maintainer role Bet #1 absorbs (Process Power flavor) |

---

## 4. Output structure

```
output/agents-gtm-v2/  →  becomes output/agents-gtm/  at swap
├── _spec.md
├── _archive/                                       ← original PDFs, build scripts, design files
├── _extract/                                       ← raw extracts + wave files
├── chapters/                                       ← workbook chapters (Ch 0–6)
│   ├── 00_frame.md                                 ~1,500 words
│   ├── 01_cell_matrix.md                           ~6,500 words (THE NEW CH 1 — 12×13 matrix)
│   ├── 02_frameworks.md                            ~6,500 words
│   ├── 03_bets_risks_cruxes.md                     ~5,000 words (7 bets + 3 Bet-Cs + 5 risks + 6 cruxes + action map)
│   ├── 04_tracker.md                               ~3,000 words
│   ├── 05_rituals.md                               ~1,200 words (defers to V1+V3)
│   └── 06_appendix.md                              ~2,500 words
├── plates/                                         ← workbook plates
│   ├── 01_cell_matrix.svg                          (THE 12×13 heatmap — V4 signature plate)
│   ├── 02_top_15_cells.svg
│   ├── 03_gtm_wardley_map.svg
│   ├── 04_gtm_powers_grid.svg
│   ├── 05_bet_coupling_flows.svg
│   └── build_plates.py
├── playbook/                                       ← the published Bet #1 deliverable
│   ├── _title.md
│   ├── PLAYBOOK_part_A.md                          ← Section I + II (7 counterparties)
│   ├── PLAYBOOK_part_B.md                          ← Section III + IV
│   ├── PLAYBOOK_part_C.md                          ← Section V–VII + Appendix
│   └── build_playbook_epub.sh
├── AI_VENDOR_PROCUREMENT_PLAYBOOK.epub             ← published artifact
├── build_epub.sh                                   ← workbook build
└── AGENTS_GTM_MASTER.epub                          ← internal workbook
```

**Total target:** ~26,200 words for the workbook + the polished playbook EPUB.

---

## 5. Chapter scope

### Ch 0 — Frame (~1,500 words)
Volume IV positioning (cell-resolution zoom on V3's agent layer), the cell-matrix introduction, how V4 composes on V1/V3, three reading paths (workbook full, playbook standalone, both bundled).

### Ch 1 — The Cell Matrix (~6,500 words)
THE structural innovation of V4. Sections:
- §1.1 The 12 GTM functions (one paragraph each, ~150 words × 12 = 1,800)
- §1.2 The 13 agent capabilities (one paragraph each, ~120 words × 13 = 1,560)
- §1.3 The 156-cell view — how to read the matrix
- §1.4 Top-15 cells by OCQ (the highest-leverage intersections) — ~80 words per cell × 15 = 1,200
- §1.5 The cell-coverage map — which cells cluster, which are barren, the pattern read
- Apply drill at end
Plate 1 (Cell Matrix heatmap) is the visual key.

### Ch 2 — Framework Lenses at Cell Resolution (~6,500 words)
- §2.1 OCQ × Cell Matrix (~2,200 words) — top O/C/Q per function-row, scored /20
- §2.2 Wardley at cell resolution (~1,400 words) — six punctuated equilibria with cell-coverage implications
- §2.3 7 Powers (~1,200 words) — power-per-Bet mapping, 5 most durable, 5 most over-rated, triple-confirmation finding
- §2.4 Ecosystem JTBD (5 GTM-org jobs) (~1,200 words) — 15 highest-gap underserved outcomes
- §2.5 Talent & Capital Flow methodology (~300 words) — data lives in Ch 4

### Ch 3 — Bets, Risks, Cruxes (~5,000 words)
- §3.1 The 7 Big Bets refreshed at cell resolution (~3,200 words) — same template as V1/V3 with Cell Anchors row added
- §3.2 The 3 promoted Bet-Cs (~600 words) — C5, C8, C9
- §3.3 The 5 Risks at cell resolution (~500 words) — cell-coverage framing
- §3.4 The 6 Cruxes (~500 words) — five carried plus new V4 outcome-pricing crux
- §3.5 6/12/18-month Action Map (~400 words)
- Apply drill (~100 words)

### Ch 4 — Operating Tracker (~3,000 words)
Same shape as V3 Ch 4: bets status board with cell-coordinate column, talent + capital tables, ARR watchlist, NYC snapshot with Hebbia first, cruxes/risks status, update log.

### Ch 5 — Operating Rituals V4 Add-ons (~1,200 words)
Defers most to V1+V3. Adds:
- §5.1 Cell-resolution quarterly: re-rate the top-15 cells; mark any cell that crossed Mature → Saturated or Forming → Mature
- §5.2 V4 trigger events: outcome-pricing earnings prints, Ironclad AI-clause-library release, Common Room roadmap reveal, MBB-feed-stock hire events
- §5.3 Playbook publication ritual (Q3 2026 one-time): the actual publish-the-playbook checklist

### Ch 6 — Appendix (~2,500 words)
Glossary additions (cell notation, the C-bets, seven counterparties, etc.), sources (Ironclad / Vanta / Drata / Cloudflare watch URLs, sectoral overlay sources), methodology notes (why /20 not /15, why 5 jobs not 7, why cells not strata), update protocol, change log.

---

## 6. Plate inventory (5 workbook plates)

### Plate 1 — Cell Matrix Heatmap (V4 signature)
12 functions × 13 capabilities = 156 cells. Each cell shaded by OCQ score. Top-15 cells outlined with the accent color. Cell of record (9, G) marked with a distinct outline. Cell labels show the named lead vendor where one exists.

### Plate 2 — Top-15 Cells (ranked bar chart or annotated cell list)
Visual ranking of the top-15 cells with OCQ scores and the lead vendors (or "no incumbent owner" tag where applicable).

### Plate 3 — GTM Wardley Map at Cell Resolution
2D map of named GTM agent products by evolution × value chain. ~40 named components. Punctuated equilibrium arrows on 6 transitions.

### Plate 4 — Powers × Cell Grid
Compressed: powers × function (not full cell × power matrix — that'd be 156 × 7). 12 rows × 7 columns. Cell content: which power dominates that function and who holds it.

### Plate 5 — Bet Coupling and Module Flows
Directed graph showing: which bets contain which modules (Bet #1 absorbs #4, #5, C2, C3, C4, C6, C10); which cells anchor which bets; which cruxes re-rate which bets; the seven counterparties as anchored nodes around Bet #1.

---

## 7. Playbook EPUB (separate artifact)

A second EPUB built from `playbook/PLAYBOOK_part_A.md` + `PLAYBOOK_part_B.md` + `PLAYBOOK_part_C.md`. Minimal cleanup:
- Single title page with the Bet #1 framing
- Pandoc assembles into `AI_VENDOR_PROCUREMENT_PLAYBOOK.epub`
- No new plates for v1 (the playbook is text-heavy; plates can be added in a future polish pass)

This artifact is for external distribution. The internal workbook (`AGENTS_GTM_MASTER.epub`) references it as the Bet #1 deliverable.

---

## 8. Style rules (same as V1 §7)

Same. Cross-references add a layer: `(V1 Ch X §X.Y)` for V1, `(V3 Ch X §X.Y)` for V3, `(Ch X §X.Y)` in-volume. Cell coordinates use parentheses: `(9, G)` for deal-desk × multi-step execution.

---

## 9. Plate style rules (same as V1 §8)

Black on white, single accent `#1d4ed8`, sans-serif. Continuity with V1/V3.

---

## 10. Build pipeline

```
1. Edit chapters/*.md
2. Run python plates/build_plates.py
3. Run bash build_epub.sh → AGENTS_GTM_MASTER.epub
4. Run bash playbook/build_playbook_epub.sh → AI_VENDOR_PROCUREMENT_PLAYBOOK.epub
```

---

## 11. Update protocol

Defers to V1 Ch 5 master rituals. V4 add-ons in V4 Ch 5. Playbook updates on a different cadence (event-driven: new EU enforcement, new clause library, new procurement-incident learning).

---

## 12. Open items (resolved at swap)

- [x] Folder strategy: build in `agents-gtm-v2/`, swap at end.
- [x] Two EPUBs (workbook + playbook).
- [x] OCQ scale /20 not /15 (V4-specific resolution).
- [x] 5 GTM-org jobs not 7 agent-workflow jobs (different unit of analysis).

---

## 13. Change log

| Date | Version | Change |
|---|---|---|
| 2026-05-20 | 1.0 | Initial V4 consolidation; produces TWO EPUBs (workbook + procurement playbook); cell-resolution refresh of 7 bets; 3 Bet-Cs promoted; one new crux (outcome pricing). |
