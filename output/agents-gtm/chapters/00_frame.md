# Chapter 0 — Frame

## Why this exists

Volume IV zooms the agent × GTM intersection to **cell-resolution** — 12 GTM functions × 13 agent capabilities = 156 cells. V1 and V3 both treat vertical agent products as one band (V1 Stratum XIII, V3 Stratum IX). That single-band treatment is correct at V1/V3 resolution and insufficient at the resolution Alex's buyer experiences. A procurement officer at Citi does not buy "Stratum IX." She buys a specific cell — renewal forecasting (11, H), AE deal-cycle memory (6, L), or the procurement gauntlet itself (9, G). V4 cuts the band into the cell matrix where every operator conversation lands.

The cell matrix is V4's structural innovation. Plate 1 (Cell Matrix Heatmap) is the signature visual; cell-coordinate notation `(function#, capability_letter)` recurs throughout, anchored in the Ch 6 glossary. The matrix surfaces three things V3's stratum view could not: that one cell — (9, G) deal-desk × multi-step execution — scores OCQ 19/20, the matrix peak; that ten Wave 2 candidate Bet-Cs collapse to three promotions and seven absorptions once cells are visible; and that the F1000 procurement gauntlet's seven counterparties (V3 had six) form a structured graph around (9, G) rather than a flat stakeholder list.

V4 also produces a second artifact — the **AI Vendor Procurement Playbook**, published as a separate EPUB. Bet #1's deliverable made tangible; external-facing, governed differently from the workbook. Two artifacts in one folder; one cell of record connecting them.

## Alex's profile (in 5 lines)

- 12 years enterprise B2B sales and GTM — SaaS through procurement gauntlets at Meltwater, Bazaarvoice, and Cohley; ICP-led motion across F1000 marketing, legal, and InfoSec counterparties.
- AI-builder track since 2023 — shipping with Claude, the AI SDK, n8n, Supabase, Vercel, Cursor, Linear, PostHog; published skills, agent stacks, and the substrate this workbook lives in.
- NYC-based; active senior search across vertical-agent GTM leadership roles (Hebbia, Sierra, Rogo, Harvey, Glean, Hippocratic, Augment) plus advisory and operator-partner paths.
- The unique combination: commercial fluency the AI labs lack + AI-builder fluency the enterprise sales bench lacks + buyer-side procurement scar tissue most NYC GTM talent does not carry.
- 18-month bet horizon — May 2026 to late 2027; V4 zooms inside that window to cell-resolution where every buyer conversation lands.

## The thesis (in one sentence)

At cell-resolution, three independent frameworks converge unambiguously: Bet #1 (Procurement Operating Standard) anchored at cell (9, G) at OCQ 19/20 is the single most asymmetric position in the matrix; Bet #2 (Hebbia #1, triple-confirmed) is the operator-shape claim on Alex's career asymmetry; Bet #3a (advisory + gateway-partner) runs concurrent rather than sequenced from H2 2026 because PE-4 closes the window faster than V3 modeled; and Bet #6 newsletter is the distribution layer connecting all three.

## How Volume IV composes on V1 + V3

V4 is the third-order zoom — V1 maps the full stack at 18 strata, V3 zooms the agent band to 14 sub-strata, V4 zooms the agent × GTM intersection to 156 cells. V4 does not re-derive V1 or V3 conclusions — the five framework methods carry from V1 Ch 2, applied at cell-resolution; the 7 Bets and 5 Risks carry with V3 deltas already applied and V4 deltas annotated in Ch 3.

The headline V4 shifts (full text in `_extract/BETS_DELTA_NOTE.md` and Ch 3 §3.1):

- **Bet #1 absorbs modules from #4 and #5** — per-trajectory FinOps audit and memory-architecture overlay ride inside the Playbook as overlays §III.6 and §III.8. Three Bet-Cs (C2 coach, C4 outcome-pricing template, C10 Article 14 tie-out) absorb into the same Playbook.
- **Bet #3 splits into 3a + 3b.** 3a (advisory + Cloudflare/Kong/Pomerium gateway-partner) runs concurrent with Bet #1 from H2 2026 — the gateway window closes faster than V3 deferred-sequencing assumed. 3b (productized servers) parked.
- **Three Bet-Cs promoted** — C5 Common Room operator path (Bet #2 sub-target), C8 Deal-Diagnosis Causation Engine (watch), C9 Persistent Memory as Service Line (Q3 2026 productization vector at trust-earned gate).
- **New crux added** — Crux #6 (outcome-pricing: sustainable or vapor?), decidability Q4 2026, triggered by Klarna reversal + Sierra/Decagon experiments + SOX rev-rec risk for per-resolution contracts.
- **Cell of record is (9, G)** at 19/20 — agent procurement gauntlet × multi-step execution. That cell is the surface area of the published Playbook. The Playbook is BOTH a deliverable AND the operationalization of the V4 thesis.

V4 is a sub-tracker of V3 (sub-tracker of V1). Conviction or cell-status changes propagate up through V3's monthly to V1 Ch 4. Read V1 → V3 → V4; for cell-specific buyer conversations go straight to V4 Ch 1; for Playbook drills go straight to the published EPUB.

## How to read this volume

Three reading paths.

- **Workbook full read (~2 hours).** Ch 0 → Ch 6 in order. Use once on first contact and again at each twice-yearly major refresh. The order is the reasoning path: cell matrix → frameworks at cell resolution → bets/risks/cruxes refreshed → tracker → V4-specific rituals → appendix.
- **Playbook standalone (~1.5 hours).** `AI_VENDOR_PROCUREMENT_PLAYBOOK.epub` — the externally-facing artifact, polished form of `playbook/PLAYBOOK_part_A/B/C.md`. For sharing with F1000 procurement counterparties. For Bet #1's published-artifact role this is the canonical surface.
- **Workbook + Playbook bundle (~3.5 hours).** Full V4 read. Use at the twice-yearly refresh and any time the operating thesis needs end-to-end re-grounding.

Cell-coordinate notation `(function#, capability_letter)` recurs throughout — `(9, G)` for deal-desk × multi-step execution, `(5, F)` for ABM × CRM hygiene, `(6, E)` for new-business AE × meeting prep. The glossary in Ch 6 §6.1 anchors the notation and lists the 12 functions and 13 capabilities in full. Markdown is canonical; EPUBs regenerate via `build_epub.sh` (workbook) and `playbook/build_playbook_epub.sh` (Playbook). Plates are SVG, regenerated from `plates/build_plates.py`.

## What's in each chapter

1. **Ch 0 — Frame.** This chapter. Cell-matrix introduction, V4 composition on V1+V3, three reading paths, the dual-artifact framing.
2. **Ch 1 — The Cell Matrix.** V4's structural innovation. The 12 GTM functions (§1.1), the 13 agent capabilities (§1.2), the 156-cell view (§1.3), the top-15 cells by OCQ (§1.4 — the highest-leverage intersections), and the cell-coverage map showing clustering, barren regions, and the pattern read (§1.5). Plate 1 is the visual key.
3. **Ch 2 — Framework Lenses at Cell Resolution.** OCQ × Cell Matrix scored /20; Wardley with six punctuated equilibria and cell-coverage implications; 7 Powers across functions with the triple-confirmation finding for Bet #2; Ecosystem JTBD applied at GTM-organization scale with 5 jobs (not V3's 7 agent-workflow jobs).
4. **Ch 3 — Bets, Risks, Cruxes.** The 7 Bets refreshed at cell resolution with Cell Anchors added; the 3 promoted Bet-Cs (C5, C8, C9); the 5 Risks framed at cell-coverage; the 6 Cruxes (V3's 5 plus V4's new outcome-pricing crux); the 6/12/18-month Action Map sequenced as publish (Bet #1) → rent equity (Bet #2) → gateway-pair (Bet #3a) concurrent.
5. **Ch 4 — Operating Tracker.** Same shape as V3 Ch 4 with cell-coordinate columns added. Bets status board, talent + capital flow, ARR watchlist with Hebbia #1, NYC snapshot, cruxes/risks status, update log.
6. **Ch 5 — Operating Rituals (V4 Add-Ons).** Intentionally thin — defers most cadences to V1 Ch 5 and V3 Ch 5. Adds three things: cell-resolution quarterly add-on, V4 trigger events (outcome-pricing prints, Ironclad clause library, Common Room reveal, MBB hires, Article 14 enforcement), and the one-time Playbook publication ritual (Q3 2026).
7. **Ch 6 — Appendix.** V4-specific glossary (extends V1 §6.1 and V3 §6.1 with cell terms), V4-specific sources, methodology notes (why /20 not /15, why 5 jobs not 7, why cells not strata), update protocol, change log.
8. **The Playbook (separate EPUB).** `AI_VENDOR_PROCUREMENT_PLAYBOOK.epub` — the Bet #1 deliverable. Seven sections; ~190k words polished from `PLAYBOOK_part_A/B/C.md`. External audience. Different cadence, different governance.

## Pointers to companion artifacts

- **`_spec.md`** — canonical V4 taxonomy. The 12 functions and 13 capabilities, OCQ /20 lens definitions with the new Density dimension, 5 GTM-org jobs (cross-walked to V3's 7 agent-workflow jobs), the V4 deltas to the 7 Bets, the 3 promoted Bet-Cs and 7 absorbed, the 6 Cruxes including the new outcome-pricing crux, the V4 glossary additions. Read once; revisit on any contradiction.
- **`plates/*.svg`** — five workbook plates. Plate 1 Cell Matrix Heatmap is the V4 signature — 12 × 13 cells shaded by OCQ, top-15 outlined, (9, G) marked distinctly. Plate 2 Top-15 Cells ranked. Plate 3 GTM Wardley Map at cell resolution. Plate 4 Powers × Cell Grid compressed to 12 × 7. Plate 5 Bet Coupling and Module Flows — the directed graph showing Bet #1 absorbing #4, #5, C2/C3/C4/C6/C10, with the seven counterparties as anchored nodes.
- **`playbook/`** folder — `_title.md` + `PLAYBOOK_part_A/B/C.md` + `build_playbook_epub.sh`. Source for the published Procurement Playbook EPUB.
- **`AI_VENDOR_PROCUREMENT_PLAYBOOK.epub`** — the Bet #1 deliverable. Published artifact. Bet #1 falsifiability depends on its 60-day post-publish download and inbound-conversation count.
- **`_archive/`** — original visual plates, build scripts, design files from the pre-consolidation V4 pile. Reference only.
- **`_extract/`** — raw extracts and wave files. Wave 1 buckets C1–C6 (OCQ per function group). Wave 2 framework files F1 Wardley / F2 7 Powers / F3 JTBD. `BETS_DELTA_NOTE.md` is the bet-by-bet V4 reconciliation; `AGENTS_GTM_TRACKER.md` is the source for Ch 4 and the canonical V4 voice; `AGENTS_GTM_ADDENDUM.md` is the methodology-heavy companion. Source material for the chapter writers, not for direct reading.
- **Parents.** `output/ai-stack/` (V1 full-stack workbook, master rituals in V1 Ch 5) + `output/ai-agents/` (V3 agent-layer zoom, agent-specific overlays in V3 Ch 3 §3.5). Read V1 Ch 0 §thesis, V3 Ch 0 §thesis, and the V1+V3 Ch 5 rituals as the inheritance baseline before any V4 read.

## Apply

Pick one cell from §1.4's top-15 list that you could not sell to a buyer in 60 seconds. The cells are not abstract — they are where every conversation you have lands. If you cannot speak to your three highest-leverage cells — (9, G) procurement gauntlet, (5, F) ABM × CRM graph, (6, E) AE × meeting prep — the workbook is theatre, not operating substrate. Re-read Ch 1 §1.4 until those three cells parse fluently in the same register you use to describe a Linear ticket.
