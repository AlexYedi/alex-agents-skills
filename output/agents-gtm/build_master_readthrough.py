#!/usr/bin/env python3
"""
build_master_readthrough.py — assembles AGENTS_GTM_MASTER_READTHROUGH.md
from the four canonical Volume IV source documents plus connective tissue.

Output: ~53K words. One linear read-through.
"""

from pathlib import Path
import re

OUT_DIR = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm")
OUT_FILE = OUT_DIR / "AGENTS_GTM_MASTER_READTHROUGH.md"

# ---- Helpers ------------------------------------------------------------

def read(name):
    return (OUT_DIR / name).read_text()

def strip_top_title(text, title_marker="# "):
    """Strip the leading H1 title block from a lifted file so we don't get
    duplicate top-level titles inside the master document."""
    lines = text.splitlines()
    out, started = [], False
    for ln in lines:
        if not started and (ln.startswith("# ") or ln.startswith("---") or ln.strip() == ""):
            continue
        started = True
        out.append(ln)
    return "\n".join(out).lstrip()

def extract_section(text, start_pattern, end_pattern=None):
    """Extract content between two heading patterns (regex). If end_pattern
    is None, take everything from start to EOF."""
    start_match = re.search(start_pattern, text, re.MULTILINE)
    if not start_match:
        return f"\n[ERROR: section '{start_pattern}' not found]\n"
    start_idx = start_match.start()
    if end_pattern is None:
        return text[start_idx:]
    end_match = re.search(end_pattern, text[start_match.end():], re.MULTILINE)
    if not end_match:
        return text[start_idx:]
    end_idx = start_match.end() + end_match.start()
    return text[start_idx:end_idx]

# ---- Source loads --------------------------------------------------------

ADDENDUM = read("AGENTS_GTM_ADDENDUM.md")
PLAYBOOK = read("AI_VENDOR_PROCUREMENT_PLAYBOOK.md")
TRACKER = read("AGENTS_GTM_TRACKER.md")
BETS_DELTA = read("BETS_DELTA_NOTE.md")

# ---- Connective tissue (the only original writing) ---------------------

TITLE_BLOCK = """# AGENTS × GTM · Master Read-Through
## Volume IV · The Intersection at Cell Resolution

**Author:** Alex Yedi
**Date:** May 2026
**Edition:** v1.0
**Read time:** ~4 hours end-to-end. Core synthesis chapters (1–5 + 7) run ~90 min. Chapter 6 — the Procurement Playbook in full — runs another ~90 min.

---
"""

CH0 = """## Chapter 0 · How to Read This Document

This is the Volume IV body of work assembled into one linear read. Four source documents — the BETS_DELTA_NOTE that records what shifted from Volume III, the AGENTS_GTM_TRACKER that becomes the live operating surface, the AGENTS_GTM_ADDENDUM that holds the cell matrix and the five frameworks, and the AI_VENDOR_PROCUREMENT_PLAYBOOK that is Bet #1 made tangible — composed as one document so the through-line reads cleanly without window-switching. Nothing here is new analysis. The connective tissue between chapters is the only original writing; the rest is curated lift from material already produced in Phase 5.

The chapter sequence is synthesis-first then breadth-then-depth. Chapter 1 gives you the headline thesis in one page. Chapter 2 walks the 12 × 13 cell matrix function-by-function so you see the field. Chapter 3 walks the three load-bearing frameworks (Wardley, 7 Powers, JTBD; OCQ and Talent + Capital Flow are operationalized through the others). Chapter 4 records the Updated Seven Bets with the per-bet deltas from Volume III. Chapter 5 is the 6 / 12 / 18-month action map. Chapter 6 is the Playbook in full — the headline deliverable, ~28,000 words, structurally the half of this document that does the actual work for an outside reader. Chapter 7 is the living tracker. Chapter 8 is the framework reflections. Chapter 9 is the Visual Atlas reference. Chapter 10 is the source-material index.

Four reading shapes work. The full read takes about four hours and is the right approach when you re-enter the work cold or are preparing to share it externally. The core-only read — Chapters 1 through 5 plus 7 — runs about 90 minutes and is what you reach for at the start of any planning conversation. The Playbook-only read is Chapter 6 and runs about 90 minutes; that is the chapter you hand to a buyer-side reader who does not need the strategic framing. The reference-only read is Chapter 7 plus Appendix B and is the right path when you are doing forensic lookup ("where did the (5, F) buying-committee finding originate?").

The four PDFs that pair with this document — `AGENTS_GTM_MATRIX.pdf`, `AGENTS_GTM_MASTER_PLATE.pdf`, `AGENTS_GTM_SUBSTRATE.pdf`, and `AGENTS_GTM_DECISIONS.pdf` — are visual companions. Open them in a separate window when each chapter calls them by name. Do not try to read this document and the plates in series; read them in parallel.

---
"""

CH1 = """## Chapter 1 · The Whole Thesis in One Page

Open `AGENTS_GTM_MASTER_PLATE.pdf` in a separate window. The next 500 words are the prose caption.

The cell-matrix work converted the 7 Bets from a portfolio of options into a sequenced operating plan. Three independent frameworks — Wardley, 7 Powers, and Ecosystem JTBD — converged on Bet #1 (the Enterprise AI Procurement Operating Standard) as the highest-leverage and most-Power-footed position in the matrix. The convergence matters because the three frameworks were applied independently, with different evidence and different scoring discipline; where they agree, conviction stacks. Bet #5 was repositioned, not killed. Bet #3 was re-sequenced from "after Bet #1" to "concurrent with Bet #1" because the Wardley-dated MCP-gateway window (PE-4, H2 2026) closes faster than Volume III modeled. The 10 candidate new bets surfaced in Phase 2a synthesis were winnowed to three promotions (Bet-C5 Common Room JOIN, Bet-C6 open-spec stewardship, Bet-C9 Persistent Memory as Service Line), four absorptions (Bet-C2 procurement-seam coach, Bet-C3 per-trajectory FinOps, Bet-C4 outcome-pricing template, Bet-C10 Article 14 tie-out), and three watch-list / parks (Bet-C1 BCG product, Bet-C7 RevOps trajectory agent, Bet-C8 deal-diagnosis causation engine).

The shape of the seven bets after Volume IV:

| # | Bet | Status | Sequence | Conviction |
|---|---|---|---|---|
| **1** | **Enterprise AI Procurement Operating Standard** — open-spec stewardship via Bet-C6 reframe; absorbs Bets #4, #5, modules from C2/C3/C4/C10 | reinforced + expanded | **NOW** | ★★★★★ |
| **2** | **Vertical Agent GTM Role** — Hebbia > Sierra > Rogo > Harvey > Glean; Bet-C5 Common Room as sub-target | reinforced + sharpened | **Concurrent with Bet #1** | ★★★★★ |
| **3a** | **Advisory + gateway-partner positioning** — Cloudflare / Kong / Pomerium pair | held + re-sequenced concurrent | **Concurrent with Bet #1 from H2 2026** | ★★★★ |
| 3b | Productized MCP server practice | parked | — | parked |
| 4 | **FinOps for Tokens** — module of Bet #1 §III.8 | subsumed | inside Bet #1 | ★★★★ (as module) |
| 5 | **RAG / Memory architecture** — module of Bet #1; Bet-C9 productization at Q3 2026 gate | subsumed standalone; Bet-C9 promoted | inside Bet #1, then Bet-C9 Q3 2026 | ★★★★ (as Bet-C9) |
| 6 | **Operator Translation Newsletter** — distribution layer for #1–#3 | reframed | from Q3 2026 ongoing | ★★★ |
| 7 | **VC Operating Partner** — fallback only | held | background | ★★★ |

Three operator-shape Power flavors stack on Bet #1: Process Power from twelve years of procurement scar tissue, Branding from the Playbook becoming the canonical buyer-side voice, and downstream Switching Costs from the rubric vocabulary becoming the procurement-default reference. EU AI Act Article 14 first enforcement (PE-2, late 2026) is the 5× TAM expansion event. Anthropic ARR Q3 2026 resolution (PE-5) is the single load-bearing Bet #2 timing variable. The MBB-network 30-day push opens Hebbia / Sierra / Harvey pipelines via three named Feb–Apr 2026 hires (Berger BCG → Hebbia, Park McKinsey → Sierra, Sinclair Bain → Harvey).

The whole sequence in one line:

**Publish (Bet #1), then rent equity (Bet #2), with advisory + gateway-pair (Bet #3a) running concurrent from H2 2026, distributed via newsletter (Bet #6), with Bet #4 + Bet #5 as modules of #1.**

That is the thesis. The remaining chapters expand each layer. The next chapter walks the matrix.

---
"""

CH2_INTRO = """## Chapter 2 · The Cell Matrix · Field Survey

Open `AGENTS_GTM_MATRIX.pdf` in a separate window. The matrix is the unit of analysis. Twelve GTM functions × thirteen agent capabilities = 156 cells. Each cell answers four questions: what exists; how mature; where the unserved JTBD is; where the buyer is paying. What follows is the methodology, then the function-by-function walk-through with the top-15 cells called out. The matrix prose deepens what the plate compresses.

---
"""

CH2_OUTRO = """
---

What you have now seen is the field. The next chapter brings five frameworks to bear on what is happening across that field.

---
"""

CH3_INTRO = """## Chapter 3 · The Five Frameworks · Analytical Depth

Open `AGENTS_GTM_DECISIONS.pdf` in a separate window. Plates VII (Wardley), VIII (7 Powers), and IX (JTBD phase map) are the visual companions to the prose that follows. Three frameworks in the order they were applied. Wardley says where things sit in their evolution. 7 Powers says which positions are durable. JTBD says which buyer-jobs they serve. Each framework was applied independently, with different evidence and different scoring discipline. Where they converged, conviction stacked. Where they diverged, the open questions are honest.

---
"""

CH3_OUTRO = """
---

Three frameworks. Three independent screens. Where they converged, the bets sharpened. The next chapter records the reconciliations.

---
"""

CH4_INTRO = """## Chapter 4 · The Updated Seven Bets

Six artifacts went into this reconciliation: ten Wave 1 cell-population reports, three Wave 2 framework agents, the Phase 2a synthesis, and the Procurement Playbook draft. The seven Bets that came out are different from the seven Bets that went in. Not by much — by enough. What follows is the BETS_DELTA note (the per-bet reconciliations as they were drafted), then the Addendum's Part XI synthesis (the same conclusions in narrative form, with the candidate-bet verdicts table). The two documents are presented in sequence because they were produced in sequence; the BETS_DELTA framed the decisions, the Addendum carried them into prose.

---
"""

CH4_OUTRO = """
---

Bets in. Bets out. Where they live now is the action map.

---
"""

CH5_INTRO = """## Chapter 5 · 6 / 12 / 18-Month Action Map

Open `AGENTS_GTM_DECISIONS.pdf` to Plate X. The 18-month Gantt is the visual companion. The text below names the people, the calendar windows, and the decision triggers. The MBB-network 30-day push opens this week.

---
"""

CH5_OUTRO = """
---

Strategy through tactics is now in your head. The next chapter is the artifact you publish. Ninety minutes. Read it as if you are a CIO at JPMorgan being handed it for the first time.

---
"""

CH6_INTRO = """## Chapter 6 · The AI Vendor Procurement Playbook

This is the headline deliverable. ~28,000 words. Bet #1 made tangible. The audience is a Fortune 1000 senior buyer-side reader — CIO, CISO, AI Council Chair, Chief Procurement Officer, GC, Chief Architect. The voice is mine — direct, commercial, position-taking. Read this last so you have the matrix + framework + bet context. You will see why §III.5 (Signed Reproducible Eval Reports) is the Bet #1 wedge, not just what it says.

If you only ever distribute one chapter of this Master Read-Through, distribute Chapter 6. It is the chapter that does the work for an outside reader.

---
"""

CH6_OUTRO = """
---

That is the Playbook. v1.0. The next edition is informed by the gauntlet you run vendors through. The next chapter is the operational surface that maintains all of the above.

---
"""

CH7_INTRO = """## Chapter 7 · The Living Tracker

The tracker is the maintenance surface. Three operating cadences: bi-weekly talent + capital, monthly bet status, trigger-based cruxes. What follows is the document you actually update. Read it once now to know its shape, then update it on the cadence.

---
"""

CH7_OUTRO = """
---

The tracker is alive. Update it on the cadence. Where the Volume IV view changes a parent-tracker bet, mirror to `output/ai-stack/OCQ_TRACKER.md` via the BETS_DELTA annotations.

---
"""

CH8_INTRO = """## Chapter 8 · Best-Use-Case Reflections per Framework

What follows is the meta-pass. What each framework was best at; what it missed; when to use it next. Useful when planning Volume V.

---
"""

CH8_OUTRO = """
---

Five frameworks. One Volume IV. The compounding lives in the stack.

---
"""

CH9 = """## Chapter 9 · Appendix A · Visual Atlas Reference

Four PDFs, twelve plates total. Each plate pairs with one or more chapters in this Master Read-Through. The table below tells you what is on which plate and when in the read to open it.

| File | Plate | Title | What it shows | Open during |
|---|---|---|---|---|
| `AGENTS_GTM_MATRIX.pdf` | I | Cell Matrix (labeled) | 12 × 13 cells with vendor abbreviations, sub-stratum tags, OCQ scores; vermilion-flagged top-15 cells | Chapter 2 |
| `AGENTS_GTM_MASTER_PLATE.pdf` | M | Whole-Thesis Synthesis | Cell-matrix heat inset, three-paragraph thesis, seven-counterparty gauntlet, Updated 7 Bets with star conviction marks, NYC operator ranking (Hebbia #1 vermilion), six Cruxes with date triggers | Chapter 1 |
| `AGENTS_GTM_SUBSTRATE.pdf` | I | Cell Index | Two-column register: all 102 mapped cells with status glyphs + OCQ; right column ranked top-30 by OCQ with vendor + stratum tags | Chapter 2 (reference) |
| `AGENTS_GTM_SUBSTRATE.pdf` | II | Functions I–VI Deep-Dive | Marketing + Selling at higher cell-resolution; six function rows × thirteen capability columns; vermilion top-15 cells called out in callout register | Chapter 2 |
| `AGENTS_GTM_SUBSTRATE.pdf` | III | Functions VII–XII Deep-Dive | Operations + Post-Sale + Planning at higher cell-resolution; (9, G) marked with full-width vermilion frame as "THE CELL OF RECORD · OCQ 19/20" | Chapter 2 |
| `AGENTS_GTM_SUBSTRATE.pdf` | IV | Seven-Counterparty Gauntlet | Seven vertical chair-columns left-to-right (InfoSec → Legal → Privacy → AI Governance → Procurement → Sponsor → EA) with three verbatim 2026 questions each; calendar-time axis with three regime bars; sectoral overlays | Chapters 4 + 6 (Playbook §II) |
| `AGENTS_GTM_SUBSTRATE.pdf` | V | Talent Flow · NYC Q2 2026 | Sankey-style flow from four feed-stocks (Stripe/Ramp/Datadog/Snowflake · MBB · Foundation-lab AE · Enterprise B2B) into ten ranked NYC destinations with Hebbia vermilion #1 | Chapter 5 |
| `AGENTS_GTM_DECISIONS.pdf` | VI | OCQ Cell-Heat | Pure intensity-only 12 × 13 heat-map (no labels in cells); three saturation bands; right-side OCQ distribution histogram | Chapter 2 (overview) |
| `AGENTS_GTM_DECISIONS.pdf` | VII | Wardley Evolution Map | Four anchored user needs at top; ~35 components placed along Genesis → Custom → Product → Commodity axis; six punctuated equilibria as vermilion arrows; Pioneer/Settle/Town-Plan/Partner quadrants with Alex's vermilion star in Pioneer | Chapter 3 |
| `AGENTS_GTM_DECISIONS.pdf` | VIII | 7 Powers Durability Screen | 30 companies in sub-grouped rows × 7 Powers columns; top-5 most-durable in vermilion; top-5 most-over-rated with horizontal slash; per-row dominant-power verdict | Chapter 3 |
| `AGENTS_GTM_DECISIONS.pdf` | IX | JTBD 5-Jobs × 8-Phases | Five jobs as rows, eight Ulwick phases as columns; high-gap cells (≥7) flagged vermilion; Alex-fit jobs (J1, J4, J2) marked with vermilion brackets | Chapter 3 |
| `AGENTS_GTM_DECISIONS.pdf` | X | Action Portfolio · 18-Month Map | Updated 8 Bets as star-conviction cards (top register); 18-month Gantt May 2026 → Nov 2027; six Cruxes as vermilion date markers; ten candidate-bet verdicts | Chapters 4 + 5 |

Use the visual atlas as a parallel surface to the document. The plates were designed to be readable in two minutes each; together they take ~24 minutes of looking. The document chapters that pair with each plate take longer to read but make the plate land harder.

---
"""

CH10 = """## Chapter 10 · Appendix B · Source-Material Index

These are the underlying source files that fed the Addendum + Playbook. You should not read these end-to-end. They are forensic-lookup material for questions like: "where did the (5, F) buying-committee mapping finding originate?" (answer: `wave1_C2.md`). Or: "what was the 7 Powers verdict on Sierra?" (answer: `wave2_F2_seven_powers.md`).

All files live in `/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm/`.

### Wave 1 — Cell Population (10 files)

| File | What's in it | When to reach for it |
|---|---|---|
| `wave1_C1.md` | Functions 1–3 (Demand-gen / Content-SEO / Inbound-PLG) × 13 capabilities. 39 cells. ~2,500 words. Includes (1, K) / (2, K) creative GUI cell flagged as Alex-claimable from Bazaarvoice/Curalate background. | Marketing-side cell deep dive |
| `wave1_C2.md` | Functions 4–6 (Outbound / ABM / New-biz AE) × 13 capabilities. 39 cells. ~3,670 words. Surfaces (5, F) buying-committee mapping at OCQ 18, (6, E) deal-diagnosis at OCQ 17, (6, L) persistent AE memory at OCQ 16. The densest funded bucket. | Sales-side cell deep dive |
| `wave1_C3.md` | Functions 7–9 (Enablement / RevOps / Deal-desk) × 13 capabilities. 39 cells + 600w on (9, G) procurement-seam. ~4,050 words. The most load-bearing C-agent — surfaced (9, G) at OCQ 19/20. | The procurement-seam cell origin |
| `wave1_C4.md` | Functions 10–11 (CS / AM-Renewals) × 13 capabilities. 26 cells. ~2,380 words. Klarna reversal Feb 2025 + (11, L) cross-quarter persistent memory gap. | CX/CS deep dive |
| `wave1_C5.md` | Function 12 (Forecasting / GTM Strategy) × 13 capabilities. 13 cells. ~1,780 words. GTM-strategy-design cell confirmed empty. | Forecasting deep dive |
| `wave1_C6.md` | Cross-function platforms (Glean, Microsoft 365 Copilot, Salesforce Agentforce, Cloudflare gateway, etc.). ~2,180 words. Includes the gateway-control-plane analysis for Bet #3. | Horizontal-vs-vertical analysis |
| `wave1_F4.md` | Talent + capital flow. ~5,900 words (table-heavy). 27 named senior moves; 14 NYC-friendly open roles; ranked target list with Hebbia #1; MBB feed-stock activation. | Career strategy + NYC targeting |
| `wave1_F5.md` | Seven-counterparty buyer-side gauntlet. ~5,000 words. The chapter-grade source for Playbook Section II + 14 addenda + 3 sectoral overlays. F5 recommended 7 counterparties, not 6 (EA/IT added). | Procurement gauntlet primary source |
| `wave1_F6.md` | Pricing & packaging. ~2,460 words. 22% inference cost at Sierra scale. Outcome-pricing exportability rule of thumb. Per-trajectory FinOps window. | Playbook Section IV.15 + Decision Tree branch 8 source |
| `wave1_playbook_draft.md` | First-pass Playbook draft from Phase 1. ~9,700 words. Foreword + 7 overlay chapters + Decision Tree (7 branches) + 38-term Glossary. Source of Sections I, III.1–7, V.1–7, VII of the final Playbook. | Playbook draft origin |

### Wave 1 — Synthesis (1 file)

| File | What's in it |
|---|---|
| `wave1_synthesis.md` | Phase 2a unified view (~3,500 words). 12 × 13 cell map with OCQ scores; top-15 cell ranking; cross-bucket convergence findings; 8 contradictions for Phase 4 arbitration; 10 candidate new bets; Alex's "where to claim" map; Wave 2 carry-forward facts. **This is the most reach-back-able single source file.** |

### Wave 2 — Framework Analysis (3 files)

| File | What's in it |
|---|---|
| `wave2_F1_wardley.md` | Wardley map at agent-GTM cell-resolution. ~2,400 words. Six punctuated equilibria with dates. Strategic quadrants for Alex (Pioneer / Settle / Town-Plan / Partner). Bet #3 sequencing-change finding (must run concurrent with Bet #1, not deferred). |
| `wave2_F2_seven_powers.md` | Helmer's 7 Powers across 30 companies. ~2,400 words. Top 5 most-durable + top 5 most-over-rated. Operator-shape Powers Alex can claim. JOIN ranking Hebbia > Sierra > Rogo > Harvey > Glean. Bet #5 standalone least-Power-footed verdict. |
| `wave2_F3_jtbd.md` | Ecosystem JTBD applied to GTM org as customer. ~2,800 words. Five jobs with owners and struggling moments. 15 highest-gap underserved outcomes. Three Alex-fit jobs with bet mapping. Common Room JOIN-vs-BUILD verdict. |

### Phase 4 / 5 Intermediate Files (the document halves before concatenation)

| File | What's in it |
|---|---|
| `AGENTS_GTM_ADDENDUM_part_A.md` | Addendum Parts VI–IX (Methodology + OCQ Matrix + Wardley + 7 Powers). ~10,000 words. |
| `AGENTS_GTM_ADDENDUM_part_B.md` | Addendum Parts X–XIII (JTBD + Updated Bets + Action Map + Reflections). ~8,600 words. |
| `PLAYBOOK_part_A.md` | Playbook Title + Foreword + 7 Counterparty chapters. ~8,500 words. |
| `PLAYBOOK_part_B.md` | Playbook Sections III (8 overlays) + IV (15 addenda + 3 sectoral). ~12,300 words. |
| `PLAYBOOK_part_C.md` | Playbook Sections V (Decision Tree) + VI (Rubric) + VII (Glossary 47 terms) + VIII (Reference Clauses) + Closing. ~7,300 words. |

### Build Scripts

| File | What it does |
|---|---|
| `build_matrix_plate.py` | Renders `AGENTS_GTM_MATRIX.pdf` (Plate I — 12 × 13 labeled matrix). |
| `build_master_plate.py` | Renders `AGENTS_GTM_MASTER_PLATE.pdf` (Plate M — whole-thesis synthesis). |
| `build_substrate.py` | Renders `AGENTS_GTM_SUBSTRATE.pdf` (Plates I–V — atlas: cell index + function deep-dives + buyer's map + talent flow). |
| `build_decisions.py` | Renders `AGENTS_GTM_DECISIONS.pdf` (Plates VI–X — frameworks: OCQ heat + Wardley + 7 Powers + JTBD + Action Portfolio). |
| `build_master_readthrough.py` | Renders this Master Read-Through document by concatenating the four canonical sources with connective tissue. |

If you need to regenerate any plate with edits to the underlying data, run the relevant `build_*.py`. The scripts inherit the SUBSTRATE design philosophy (`output/ai-stack/design_philosophy.md`) and the Volume III continuity note (`output/ai-agents/design_philosophy_agents.md`).

---
"""

CLOSING = """## Closing

This Master Read-Through is the linear assembly of Volume IV. It is not new analysis. It is curated lift across four canonical documents, sequenced so the through-line reads cleanly, with the four PDF plates as visual companions.

What is next, when you choose to act on it: Volume V drilling into the three promoted candidate bets (Bet-C5 Common Room operator path, Bet-C6 open-spec stewardship, Bet-C9 Persistent Memory as Service Line). A SUBSTRATE-themed DOCX styling pass to render the documents in the same aesthetic as the plates. External-share preparation — a one-pager PDF derived from the Master Plate for cold investor / buyer outreach. None of those are required. All are available.

The Playbook publishes Q3 2026. The MBB-network 30-day push opens this week. The tracker updates bi-weekly.

— *Alex Yedi · May 2026*
"""

# ---- Section extraction from the source documents ----------------------

# ADDENDUM contains Parts VI through XIII. We carve out the parts we need.
# The Addendum is split across part_A (VI-IX) and part_B (X-XIII), already
# concatenated into AGENTS_GTM_ADDENDUM.md.

# Part VI Methodology + Part VII OCQ × Cell Matrix → Chapter 2
ADDENDUM_PARTS_VI_VII = extract_section(
    ADDENDUM,
    r"^## Part VI",
    r"^## Part VIII"
)

# Part VIII Wardley + Part IX Seven Powers + Part X JTBD → Chapter 3
ADDENDUM_PARTS_VIII_IX_X = extract_section(
    ADDENDUM,
    r"^## Part VIII",
    r"^## Part XI"
)

# Part XI Synthesis (Updated 7 Bets etc.) → Chapter 4 (after BETS_DELTA)
ADDENDUM_PART_XI = extract_section(
    ADDENDUM,
    r"^## Part XI",
    r"^## Part XII"
)

# Part XII Action Map → Chapter 5
ADDENDUM_PART_XII = extract_section(
    ADDENDUM,
    r"^## Part XII",
    r"^## Part XIII"
)

# Part XIII Reflections → Chapter 8
ADDENDUM_PART_XIII = extract_section(
    ADDENDUM,
    r"^## Part XIII",
    None
)

# BETS_DELTA — strip top H1 title only; keep all sections
BETS_DELTA_BODY = strip_top_title(BETS_DELTA)

# PLAYBOOK — strip top H1 title only; keep entire document for Chapter 6
PLAYBOOK_BODY = strip_top_title(PLAYBOOK)

# TRACKER — strip top H1 title only; keep entire document for Chapter 7
TRACKER_BODY = strip_top_title(TRACKER)

# ---- Assembly ------------------------------------------------------------

doc = []
doc.append(TITLE_BLOCK)
doc.append(CH0)
doc.append(CH1)
doc.append(CH2_INTRO)
doc.append(ADDENDUM_PARTS_VI_VII)
doc.append(CH2_OUTRO)
doc.append(CH3_INTRO)
doc.append(ADDENDUM_PARTS_VIII_IX_X)
doc.append(CH3_OUTRO)
doc.append(CH4_INTRO)
doc.append(BETS_DELTA_BODY)
doc.append("\n---\n")
doc.append(ADDENDUM_PART_XI)
doc.append(CH4_OUTRO)
doc.append(CH5_INTRO)
doc.append(ADDENDUM_PART_XII)
doc.append(CH5_OUTRO)
doc.append(CH6_INTRO)
doc.append(PLAYBOOK_BODY)
doc.append(CH6_OUTRO)
doc.append(CH7_INTRO)
doc.append(TRACKER_BODY)
doc.append(CH7_OUTRO)
doc.append(CH8_INTRO)
doc.append(ADDENDUM_PART_XIII)
doc.append(CH8_OUTRO)
doc.append(CH9)
doc.append(CH10)
doc.append(CLOSING)

OUT_FILE.write_text("\n".join(doc))

# Quick stats
text = OUT_FILE.read_text()
words = len(text.split())
chars = len(text)
print(f"Wrote {OUT_FILE.name}: {words:,} words, {chars:,} chars")
