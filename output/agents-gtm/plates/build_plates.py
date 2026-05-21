"""
AGENTS_GTM_MASTER (Volume IV) — Plate generator
================================================
Generates 5 SVG plates that accompany AGENTS_GTM_MASTER Volume IV.
Educational, NOT aesthetic. Black on white, one accent color (#1d4ed8).
Visual continuity with V1 + V3 plates.

Run from agents-gtm-v2/ directory:
    python plates/build_plates.py

Output:
    plates/01_cell_matrix.svg
    plates/02_top_15_cells.svg
    plates/03_gtm_wardley_map.svg
    plates/04_gtm_powers_grid.svg
    plates/05_bet_coupling_flows.svg
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch
from matplotlib.lines import Line2D
import numpy as np

# -----------------------------------------------------------------------------
# Global style — binding per V1 §8 (visual continuity)
# -----------------------------------------------------------------------------
ACCENT = "#1d4ed8"          # one accent color (saturated dark blue)
BLACK = "#000000"
GRAY_MED = "#6b7280"
GRAY_LIGHT = "#d1d5db"
GRAY_VLIGHT = "#f3f4f6"
WHITE = "#ffffff"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["axes.edgecolor"] = BLACK
plt.rcParams["axes.linewidth"] = 0.5
plt.rcParams["pdf.fonttype"] = 42

# Page sizes (inches)
PAGE_W = 8.5
PAGE_H = 11.0
PAGE_LANDSCAPE_W = 14.0   # wider page for the 13-col matrix
PAGE_LANDSCAPE_H = 10.0

PLATES_DIR = Path(__file__).parent

# -----------------------------------------------------------------------------
# Canonical data — sourced from Ch 1, Ch 2, Ch 3 (May 2026)
# -----------------------------------------------------------------------------

# 12 function rows
FUNCTIONS = [
    (1,  "Demand-gen / brand"),
    (2,  "Content / SEO"),
    (3,  "Inbound / PLG"),
    (4,  "Outbound SDR"),
    (5,  "ABM"),
    (6,  "New-business AE"),
    (7,  "Enablement / training"),
    (8,  "RevOps / Sales Ops"),
    (9,  "Deal-desk / pricing / proc."),
    (10, "CS / onboarding"),
    (11, "AM / renewals / expansion"),
    (12, "Forecasting / strategy"),
]

# 13 capability columns
CAPABILITIES = [
    ("A", "Research /\nenrichment"),
    ("B", "Personali-\nzation +\ncontent"),
    ("C", "Multi-channel\norchestration"),
    ("D", "Conversation\nhandling"),
    ("E", "Meeting prep\n+ follow-up"),
    ("F", "CRM hygiene\n/ graph"),
    ("G", "Multi-step\ntask exec"),
    ("H", "Forecasting\n/ decision"),
    ("I", "Negotiation\n/ pricing"),
    ("J", "Coaching /\nperformance"),
    ("K", "Computer-\nuse"),
    ("L", "Persistent\nmemory"),
    ("M", "Trajectory\nobservability"),
]

# -----------------------------------------------------------------------------
# Cell matrix data (12 x 13 = 156 cells)
# Cell state: "ocq:<score>", "na", "gap" (gap with no score yet but identified)
# Score 0 = inactive/background (treated as very pale)
# Built from Ch 1 §1.1, §1.4, §1.5 and Ch 2 §2.1 cluster reads
# Each row is a function; each entry is a (capability_letter, state, score) tuple
# -----------------------------------------------------------------------------

# Default score for "background" cell when present but below ~8
def _bg(s): return ("ocq", s)

# Each cell entry: (state, score_or_None)
# state: "ocq" (populated, has score), "na" (structurally inapplicable), "gap" (identified gap)
# Score is /20 if state == "ocq"
CELL_MATRIX = {
    # F1 Demand-gen / brand
    (1, "A"):  ("ocq", 11),
    (1, "B"):  ("ocq", 10),  # mature, CAC-drag warning, Mutiny/Jasper
    (1, "C"):  ("ocq", 10),  # forming
    (1, "D"):  ("ocq", 10),  # mature: Drift/Salesloft, Qualified
    (1, "E"):  ("na", None), # brand has no meetings
    (1, "F"):  ("ocq", 8),
    (1, "G"):  ("ocq", 7),
    (1, "H"):  ("ocq", 8),
    (1, "I"):  ("na", None),
    (1, "J"):  ("na", None),
    (1, "K"):  ("ocq", 13),  # creative GUI ops — OSWorld gated
    (1, "L"):  ("ocq", 8),
    (1, "M"):  ("ocq", 14),  # marketing-agent obs — FTC AI-washing + EU Art 50

    # F2 Content / SEO
    (2, "A"):  ("ocq", 9),
    (2, "B"):  ("ocq", 8),   # most commoditized cell — E-E-A-T suppression caps score
    (2, "C"):  ("ocq", 7),
    (2, "D"):  ("ocq", 6),
    (2, "E"):  ("na", None),
    (2, "F"):  ("ocq", 7),
    (2, "G"):  ("ocq", 7),
    (2, "H"):  ("ocq", 7),
    (2, "I"):  ("na", None),
    (2, "J"):  ("na", None),
    (2, "K"):  ("ocq", 13),  # creative GUI ops bundle
    (2, "L"):  ("ocq", 13),  # Writer Knowledge Graph — locked
    (2, "M"):  ("ocq", 12),

    # F3 Inbound / PLG
    (3, "A"):  ("ocq", 13),
    (3, "B"):  ("ocq", 9),
    (3, "C"):  ("ocq", 9),
    (3, "D"):  ("ocq", 12),  # Intercom Fin $100M+ ARR
    (3, "E"):  ("ocq", 8),
    (3, "F"):  ("ocq", 11),
    (3, "G"):  ("ocq", 11),  # PLG-to-pipeline multi-step forming
    (3, "H"):  ("ocq", 9),
    (3, "I"):  ("na", None),
    (3, "J"):  ("na", None),
    (3, "K"):  ("ocq", 9),
    (3, "L"):  ("ocq", 11),
    (3, "M"):  ("gap", None), # empty

    # F4 Outbound SDR
    (4, "A"):  ("ocq", 16),  # TOP-15: Clay $100M/$1.5B
    (4, "B"):  ("ocq", 10),  # 11x ceiling — flat $20M ARR
    (4, "C"):  ("ocq", 10),
    (4, "D"):  ("ocq", 9),
    (4, "E"):  ("ocq", 11),  # SDR-AE handoff seam, Granola
    (4, "F"):  ("ocq", 14),  # Clay's deeper play
    (4, "G"):  ("ocq", 9),
    (4, "H"):  ("ocq", 8),
    (4, "I"):  ("na", None),
    (4, "J"):  ("ocq", 8),
    (4, "K"):  ("ocq", 15),  # TOP-15: CU in outbound — OSWorld gated
    (4, "L"):  ("ocq", 9),
    (4, "M"):  ("ocq", 14),  # TOP-15: SDR trajectory obs — TCPA etc.

    # F5 ABM
    (5, "A"):  ("ocq", 11),
    (5, "B"):  ("ocq", 9),   # attribution vapor
    (5, "C"):  ("ocq", 11),  # Demandbase One, 6sense — incumbent-locked
    (5, "D"):  ("ocq", 8),
    (5, "E"):  ("ocq", 9),
    (5, "F"):  ("ocq", 18),  # TOP-15 #2: buying-committee mapping GAP, no incumbent
    (5, "G"):  ("ocq", 8),
    (5, "H"):  ("ocq", 8),
    (5, "I"):  ("na", None),
    (5, "J"):  ("na", None),
    (5, "K"):  ("ocq", 9),   # nascent
    (5, "L"):  ("ocq", 13),
    (5, "M"):  ("gap", None),

    # F6 New-business AE
    (6, "A"):  ("ocq", 14),  # TOP-15: Hebbia/Rogo/Glean, MS Sales Copilot
    (6, "B"):  ("ocq", 10),
    (6, "C"):  ("ocq", 11),
    (6, "D"):  ("ocq", 11),  # Cresta, Aircover, Gong Assist
    (6, "E"):  ("ocq", 17),  # TOP-15 #3: deal-diagnosis causation GAP
    (6, "F"):  ("ocq", 12),
    (6, "G"):  ("ocq", 11),
    (6, "H"):  ("ocq", 10),
    (6, "I"):  ("ocq", 13),
    (6, "J"):  ("ocq", 9),
    (6, "K"):  ("ocq", 14),  # TOP-15: AE motion GUI driving, MS structural adv
    (6, "L"):  ("ocq", 16),  # TOP-15: AE deal-cycle memory GAP
    (6, "M"):  ("ocq", 13),

    # F7 Enablement / training
    (7, "A"):  ("ocq", 8),   # saturated
    (7, "B"):  ("ocq", 8),
    (7, "C"):  ("ocq", 8),
    (7, "D"):  ("ocq", 9),
    (7, "E"):  ("ocq", 9),
    (7, "F"):  ("ocq", 8),
    (7, "G"):  ("ocq", 9),
    (7, "H"):  ("ocq", 8),
    (7, "I"):  ("na", None),
    (7, "J"):  ("ocq", 13),  # J+M convergence — procurement-seam coaching
    (7, "K"):  ("ocq", 8),
    (7, "L"):  ("ocq", 9),
    (7, "M"):  ("ocq", 12),

    # F8 RevOps / Sales Ops
    (8, "A"):  ("ocq", 11),
    (8, "B"):  ("ocq", 7),
    (8, "C"):  ("ocq", 8),
    (8, "D"):  ("ocq", 8),
    (8, "E"):  ("ocq", 8),
    (8, "F"):  ("ocq", 11),  # CRM hygiene multi-tenant write governance
    (8, "G"):  ("ocq", 15),  # TOP-15: RevOps multi-step trajectory agent
    (8, "H"):  ("ocq", 11),  # saturated (Clari/BoostUp/Aviso)
    (8, "I"):  ("ocq", 9),
    (8, "J"):  ("ocq", 8),
    (8, "K"):  ("ocq", 11),  # underserved
    (8, "L"):  ("ocq", 10),
    (8, "M"):  ("ocq", 12),

    # F9 Deal-desk / pricing / procurement — CELL OF RECORD
    (9, "A"):  ("ocq", 11),  # underserved
    (9, "B"):  ("ocq", 8),
    (9, "C"):  ("ocq", 8),
    (9, "D"):  ("ocq", 9),
    (9, "E"):  ("ocq", 9),
    (9, "F"):  ("ocq", 11),
    (9, "G"):  ("ocq", 19),  # *** CELL OF RECORD *** 19/20 matrix peak
    (9, "H"):  ("ocq", 10),
    (9, "I"):  ("ocq", 16),  # TOP-15: AI-specific contract addenda
    (9, "J"):  ("ocq", 9),
    (9, "K"):  ("ocq", 13),  # Coupa/Ariba/Workday Procurement driving
    (9, "L"):  ("ocq", 10),
    (9, "M"):  ("ocq", 14),  # TOP-15: deal-desk trajectory evidence pack

    # F10 CS / onboarding
    (10, "A"): ("ocq", 11),
    (10, "B"): ("ocq", 10),
    (10, "C"): ("ocq", 10),
    (10, "D"): ("ocq", 14),  # densest cell by dollars — Sierra $175M+, Decagon, Intercom Fin
    (10, "E"): ("ocq", 11),
    (10, "F"): ("ocq", 11),
    (10, "G"): ("ocq", 13),  # multi-step refund/order-change
    (10, "H"): ("ocq", 10),
    (10, "I"): ("na", None), # lives at (11, I)
    (10, "J"): ("ocq", 9),
    (10, "K"): ("ocq", 11),
    (10, "L"): ("ocq", 11),  # claimed-everywhere, real-nowhere
    (10, "M"): ("ocq", 12),

    # F11 AM / renewals / expansion
    (11, "A"): ("ocq", 11),
    (11, "B"): ("ocq", 9),
    (11, "C"): ("ocq", 9),
    (11, "D"): ("ocq", 10),
    (11, "E"): ("ocq", 10),
    (11, "F"): ("ocq", 10),
    (11, "G"): ("ocq", 13),  # pull-usage to procurement single trajectory
    (11, "H"): ("ocq", 11),  # Gainsight home turf, weak
    (11, "I"): ("ocq", 13),  # outcome-based pricing operator playbook
    (11, "J"): ("ocq", 9),
    (11, "K"): ("ocq", 10),
    (11, "L"): ("ocq", 14),  # TOP-15: renewal cross-quarter memory
    (11, "M"): ("ocq", 11),

    # F12 Forecasting / strategy
    (12, "A"): ("ocq", 10),
    (12, "B"): ("ocq", 7),
    (12, "C"): ("ocq", 8),
    (12, "D"): ("ocq", 14),  # NL->SQL->chart for analysts — Hex, Definite, Mosaic
    (12, "E"): ("ocq", 9),
    (12, "F"): ("ocq", 15),  # TOP-15: cross-system narrative retrieval, Gong Deal Stories
    (12, "G"): ("ocq", 11),
    (12, "H"): ("ocq", 15),  # TOP-15: $1.5B saturated category, MAPE plateau
    (12, "I"): ("ocq", 9),
    (12, "J"): ("ocq", 8),
    (12, "K"): ("ocq", 10),
    (12, "L"): ("ocq", 13),  # 8-quarter pipeline-decay memory
    (12, "M"): ("ocq", 10),
}

# Top-15 cells from Ch 1 §1.4 (in ranked order)
# (function, capability, score, lead_vendor, gap_one_liner)
TOP_15 = [
    (9,  "G", 19, "Loopio/Vanta/Ironclad/Vendr",
        "Zero of seven sources ship unified bilateral evidence pack."),
    (5,  "F", 18, "no incumbent owner",
        "Dynamic 9-person buying-committee map, weekly refresh — unbuilt."),
    (6,  "E", 17, "Gong/Chorus/Aircover",
        "Causation @ 73% confidence — no vendor ships it."),
    (4,  "A", 16, "Clay ($100M / $1.5B)",
        "Winner-eats-most; commoditizing; low Alex claimability."),
    (6,  "L", 16, "Mem0/Letta/Zep (dev-side only)",
        "6-9 month AE deal-cycle memory — no AE-shape product exists."),
    (9,  "I", 16, "Ironclad AI / LinkSquares",
        "12-15 AI-specific MSA clauses still unbuilt."),
    (8,  "G", 15, "Clari/BoostUp/Aviso/Tomo",
        "Pieces ship; nobody closes the RevOps loop end-to-end."),
    (4,  "K", 15, "Anthropic CU / Operator / Mariner",
        "OSWorld 65% pending; LinkedIn TOS structural moat-killer."),
    (12, "F", 15, "Gong / Clari / Glean",
        "Mature; Deal Stories widely adopted."),
    (12, "H", 15, "Clari/BoostUp/Aviso/Einstein",
        "$1.5B saturated; honest 5-15% MAPE lift; accountability cap."),
    (4,  "M", 14, "LangSmith/Galileo (eng-shape)",
        "TCPA/CAN-SPAM mandatory <=18 mo; no SDR-shape vendor."),
    (9,  "M", 14, "Galileo/Arize/Langfuse (eng-shape)",
        "Deal-desk trajectory evidence pack — nobody ships turnkey."),
    (11, "L", 14, "Sierra/Gainsight (shallow)",
        "Cross-quarter renewal memory — no production CS agent has it."),
    (3,  "A+L+F", 14, "Common Room ($30M ARR)",
        "PLG signal-fusion; multi-source product one step away."),
    (6,  "K", 14, "Anthropic CU / MS Sales Copilot",
        "AE motion GUI driving; non-MS-shop cell open."),
]

# Build set of top-15 cells for outline rendering on plate 1
TOP_15_CELLS = set()
for (f, c, *_) in TOP_15:
    # Handle (3, "A+L+F") special — treat A column as the convergence anchor in plate 1
    if "+" in c:
        # Mark each underlying letter as in-cluster, but also flag the convergence
        # On plate 1 we will draw outline only on (3, A) since that's the column header
        TOP_15_CELLS.add((f, c.split("+")[0]))
    else:
        TOP_15_CELLS.add((f, c))

CELL_OF_RECORD = (9, "G")

# -----------------------------------------------------------------------------
# Plate 3 — Wardley map components (from Ch 2 §2.2)
# (label, evolution_x [0-1], value_chain_y [0-1])
# -----------------------------------------------------------------------------
GTM_WARDLEY = [
    # USER-VISIBLE / VERTICAL AGENT PRODUCTS (top)
    ("Sierra",            0.62, 0.96),
    ("Decagon",           0.60, 0.93),
    ("Hebbia",            0.44, 0.94),
    ("Rogo",              0.40, 0.91),
    ("Harvey",            0.50, 0.91),
    ("Hippocratic",       0.46, 0.88),
    ("Glean",             0.66, 0.92),
    ("Cresta",            0.60, 0.87),
    ("Common Room",       0.55, 0.89),
    ("Mutiny",            0.60, 0.84),
    ("Jasper",            0.78, 0.86),
    ("Writer",            0.56, 0.83),
    ("Clay",              0.68, 0.89),
    ("Apollo",            0.74, 0.85),
    ("ZoomInfo",          0.82, 0.85),
    ("6sense",            0.74, 0.82),
    ("Demandbase",        0.76, 0.79),
    ("Intercom Fin",      0.70, 0.94),
    ("Ironclad AI",       0.50, 0.78),
    ("Vanta",             0.70, 0.75),
    ("Drata",             0.72, 0.73),
    ("Loopio",            0.74, 0.76),
    ("M365 Copilot Sales",0.80, 0.95),
    ("Agentforce (SF)",   0.72, 0.91),
    # MIDDLE / COMPUTER-USE LAYER
    ("Anthropic CU",      0.18, 0.66),
    ("OpenAI Operator",   0.22, 0.64),
    ("Mariner",           0.16, 0.62),
    ("Browserbase",       0.66, 0.58),
    # MEMORY / OBS / EVAL
    ("Mem0",              0.22, 0.46),
    ("Letta",             0.18, 0.44),
    ("Zep",               0.28, 0.46),
    ("LangSmith",         0.62, 0.42),
    ("Braintrust",        0.58, 0.40),
    ("Galileo",           0.56, 0.38),
    ("Arize",             0.62, 0.38),
    ("Langfuse",          0.60, 0.36),
    # GATEWAYS (lower)
    ("Cloudflare Gateway",0.52, 0.26),
    ("Kong AI Gateway",   0.56, 0.24),
    ("Pomerium",          0.46, 0.22),
    # PROTOCOL / SUBSTRATE
    ("MCP spec",          0.62, 0.16),
    ("Claude Opus",       0.58, 0.08),
    ("GPT-5",             0.62, 0.06),
    ("Gemini",            0.60, 0.04),
    # PROCUREMENT GAUNTLET (cross-cutting, Genesis)
    ("(9,G) Procurement\ngauntlet pack (unclaimed)", 0.06, 0.50),
]

# 6 punctuated equilibria arrows (Ch 2 §2.2)
# (anchor_label, dx) — arrow length along evolution axis
GTM_WARDLEY_ARROWS = [
    ("Kong AI Gateway",           0.18),   # PE-4 MCP gateways Custom -> Product H2 2026
    ("Anthropic CU",              0.20),   # PE-1 OSWorld 65% Q3 2026
    ("(9,G) Procurement\ngauntlet pack (unclaimed)", 0.22),  # PE-2 Article 14 first enforcement
    ("Sierra",                    0.12),   # PE-3 Sierra ARR $500M mid-2027
    ("M365 Copilot Sales",        0.10),   # PE-6 MS 365 Copilot $10B ARR
    ("Mem0",                      0.18),   # outcome-pricing / memory absorption
]

GTM_WARDLEY_PE_LABELS = [
    ("PE-4", "MCP gateways -> Product H2'26"),
    ("PE-1", "OSWorld 65% Q3'26"),
    ("PE-2", "Art. 14 first enforcement late'26"),
    ("PE-3", "Sierra ARR $500M mid-2027"),
    ("PE-6", "M365 Copilot $10B ARR H1'27"),
    ("PE-5", "Anthropic ARR Q3'26 resolution"),
]

# Dependency lines (light gray)
GTM_WARDLEY_DEPS = [
    ("Sierra",              "Claude Opus"),
    ("Decagon",             "GPT-5"),
    ("Hebbia",              "Claude Opus"),
    ("Cresta",              "GPT-5"),
    ("Intercom Fin",        "GPT-5"),
    ("M365 Copilot Sales",  "GPT-5"),
    ("Anthropic CU",        "Claude Opus"),
    ("MCP spec",            "Cloudflare Gateway"),
    ("MCP spec",            "Kong AI Gateway"),
    ("Vanta",               "Ironclad AI"),
    ("Ironclad AI",         "(9,G) Procurement\ngauntlet pack (unclaimed)"),
]

# -----------------------------------------------------------------------------
# Plate 4 — Powers x Function Grid (12 rows x 7 cols)
# From Ch 2 §2.3 — Helmer's 7 Powers across the 12 GTM functions
# Status: "F" = held filled, "S" = strengthening (accent), "E" = eroding (outline), "" = absent
# Columns: Scale / Network / Counter-Pos / Switching / Branding / Cornered / Process
# -----------------------------------------------------------------------------
POWERS_COLS = [
    "Scale\nEconomies",
    "Network\nEconomies",
    "Counter-\nPositioning",
    "Switching\nCosts",
    "Branding",
    "Cornered\nResource",
    "Process\nPower",
]

# (label, Scale, Net, CP, Sw, Br, CR, Pr, holder)
POWERS_BY_FUNCTION = [
    ("F1 — Demand-gen / brand",   "F",  "F",  "",   "F",  "F",  "",   "",
        "6sense / Demandbase / Mutiny"),
    ("F2 — Content / SEO",        "",   "",   "",   "E",  "F",  "F",  "",
        "Writer (Knowledge Graph)"),
    ("F3 — Inbound / PLG",        "",   "F",  "",   "F",  "",   "",   "S",
        "Common Room (forming)"),
    ("F4 — Outbound SDR",         "F",  "",   "",   "E",  "F",  "F",  "F",
        "Clay / Apollo / Outreach (eroding)"),
    ("F5 — ABM",                  "F",  "F",  "",   "F",  "F",  "",   "",
        "Demandbase / 6sense / ZoomInfo"),
    ("F6 — New-business AE",      "F",  "F",  "",   "F",  "F",  "F",  "F",
        "MS Sales Copilot / Hebbia / Harvey"),
    ("F7 — Enablement / training","",   "",   "",   "F",  "F",  "",   "",
        "Highspot / Seismic (saturated)"),
    ("F8 — RevOps / Sales Ops",   "",   "",   "",   "F",  "F",  "",   "F",
        "Clari (substrate); Gong (Process)"),
    ("F9 — Deal-desk / proc.",    "",   "",   "S",  "S",  "S",  "F",  "S",
        "(9,G) unclaimed — Bet #1 target"),
    ("F10 — CS / onboarding",     "F",  "F",  "F",  "F",  "F",  "F",  "F",
        "Sierra / Decagon / Intercom Fin"),
    ("F11 — AM / renewals",       "",   "F",  "",   "F",  "F",  "",   "F",
        "Gainsight (structured data)"),
    ("F12 — Forecasting",         "F",  "F",  "",   "F",  "F",  "",   "F",
        "Clari / BoostUp / Gong"),
]

# -----------------------------------------------------------------------------
# Plate 5 — Bet coupling and module flows (Ch 3 §3.1, §3.2, §3.6)
# -----------------------------------------------------------------------------

# Bet nodes + 3 promoted Bet-Cs
BET_NODES = [
    # id, label, kind, x, y
    ("B1",  "Bet #1\nProcurement\nPlaybook",        "bet",  5.0,  9.5),
    ("B2",  "Bet #2\nVertical Agent\nNYC Role",     "bet",  9.0,  9.5),
    ("B3a", "Bet #3a\nMCP Gateway\nAdvisory",       "bet", 11.0,  7.5),
    ("B4",  "Bet #4\nFinOps\n(absorbed)",           "absorbed",  2.0, 11.5),
    ("B5",  "Bet #5\nMemory Arch.\n(absorbed)",     "absorbed",  3.5, 11.5),
    ("B6",  "Bet #6\nNewsletter\n(distribution)",   "bet",  7.0,  3.0),
    ("B7",  "Bet #7\nVC Operating\nPartner",        "bet", 11.0,  2.5),
    # Promoted Bet-Cs
    ("C5",  "Bet-C5\nCommon Room\nJOIN",            "betc", 11.0,  11.0),
    ("C8",  "Bet-C8\nDeal-Diagnosis\n(watch)",      "betc", 11.0, 10.0),
    ("C9",  "Bet-C9\nMemory Service\n(post-trust)", "betc",  3.5,  7.5),
    # Absorbed modules (smaller, gray)
    ("C2",  "Bet-C2\nproc-seam coach",              "mod",   0.5,  9.5),
    ("C3",  "Bet-C3\nFinOps trajectory",            "mod",   0.5, 10.5),
    ("C4",  "Bet-C4\noutcome-pricing tpl",          "mod",   0.5,  8.5),
    ("C6",  "Bet-C6\nopen-spec stewardship",        "mod",   0.5,  7.5),
    ("C10", "Bet-C10\nArt. 14 tie-out",             "mod",   0.5,  6.5),
]

# Cruxes (small nodes feeding into bets)
CRUX_NODES = [
    ("CR1", "Crux 1\nAnthropic ARR\n($24B vs $30B)",   3.5,  4.5),
    ("CR3", "Crux 3\nMCP commons\nor fork",            8.5,  5.5),
    ("CR5", "Crux 5\nMemory:\nstandalone/absorbed",    1.5,  5.5),
    ("CR6", "Crux 6 (NEW)\nOutcome-pricing\nsustainable?", 7.0,  5.0),
]

# Edges
# Module absorption (gray, into B1)
ABSORPTION_EDGES = [
    ("B4",  "B1"),
    ("B5",  "B1"),
    ("C2",  "B1"),
    ("C3",  "B1"),
    ("C4",  "B1"),
    ("C6",  "B1"),
    ("C10", "B1"),
]

# Crux coupling (accent thick)
CRUX_EDGES = [
    ("CR1", "B2"),
    ("CR1", "B4"),  # absorbed but kept as historical link
    ("CR1", "B5"),
    ("CR3", "B3a"),
    ("CR5", "B5"),
    ("CR5", "C9"),
    ("CR6", "B2"),
    ("CR6", "B5"),
    ("CR6", "C9"),
]

# Bet-C promotion arrows (dotted accent)
PROMOTION_EDGES = [
    ("C5", "B2"),   # under Bet #2
    ("C8", "B2"),   # watchlist
    ("C9", "B5"),   # productization (B5 absorbed)
]

# Sequencing arrows (gray, large) Bet #1 -> #2 -> #3a (concurrent)
SEQUENCE_EDGES = [
    ("B1", "B2"),
    ("B2", "B3a"),
    ("B1", "B3a"),   # 3a concurrent with #1
]

# Distribution arrow Bet #6 -> #1, #2, #3a
DISTRIBUTION_EDGES = [
    ("B6", "B1"),
    ("B6", "B2"),
    ("B6", "B3a"),
]

# Risk-propagation paths (labeled R1-R5)
RISK_BOX_DATA = [
    ("R1", "Foundation labs walk up-stack",         14/20, ["B2"]),
    ("R2", "MCP silent fork (Responses-API)",       13/20, ["B3a"]),
    ("R3", "Vanta/Ironclad AI-vendor bundle Q4'26", 15/20, ["B1"]),
    ("R4", "Per-trajectory pricing transparency",   14/20, ["B1"]),
    ("R5", "EU Art. 14 paper-tiger outcome",        13/20, ["B1"]),
]


# =============================================================================
# Helpers
# =============================================================================

def _new_fig(landscape=False, large_landscape=False):
    if large_landscape:
        return plt.figure(figsize=(PAGE_LANDSCAPE_W, PAGE_LANDSCAPE_H), facecolor=WHITE)
    if landscape:
        return plt.figure(figsize=(PAGE_H, PAGE_W), facecolor=WHITE)
    return plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=WHITE)


def _save(fig, path):
    fig.savefig(path, format="svg", bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


def _shade_for_score(score, max_score=20):
    """Single-hue gradient white -> ACCENT for given OCQ score."""
    t = max(0.0, min(1.0, score / max_score))
    # white -> accent #1d4ed8 (29, 78, 216)
    r0, g0, b0 = 1.0, 1.0, 1.0
    r1, g1, b1 = 29/255.0, 78/255.0, 216/255.0
    # Compress the lower range so even low scores are visible
    return (r0 + (r1 - r0) * t, g0 + (g1 - g0) * t, b0 + (b1 - b0) * t)


# =============================================================================
# Plate 1 — Cell Matrix Heatmap (V4 SIGNATURE)
# =============================================================================

def build_cell_matrix():
    """The 12 functions x 13 capabilities matrix. Landscape orientation."""
    fig = _new_fig(large_landscape=True)
    # Reserve top for title, bottom for legend
    ax = fig.add_axes([0.16, 0.10, 0.78, 0.74])

    n_rows = len(FUNCTIONS)        # 12
    n_cols = len(CAPABILITIES)     # 13

    # Draw cells
    for ri, (fnum, fname) in enumerate(FUNCTIONS):
        y = n_rows - ri - 1
        for ci, (cletter, ccap) in enumerate(CAPABILITIES):
            x = ci
            state, score = CELL_MATRIX.get((fnum, cletter), ("na", None))

            if state == "na":
                # light gray, "n/a" label
                rect = Rectangle((x, y), 1, 1, facecolor=GRAY_VLIGHT,
                                 edgecolor=GRAY_LIGHT, linewidth=0.4)
                ax.add_patch(rect)
                ax.text(x + 0.5, y + 0.5, "n/a",
                        ha="center", va="center", fontsize=7,
                        color=GRAY_MED, style="italic")
            elif state == "gap":
                # diagonal hatching
                rect = Rectangle((x, y), 1, 1, facecolor=WHITE,
                                 edgecolor=GRAY_LIGHT, linewidth=0.4,
                                 hatch="///")
                ax.add_patch(rect)
                ax.text(x + 0.5, y + 0.5, "gap",
                        ha="center", va="center", fontsize=7,
                        color=GRAY_MED, style="italic")
            else:
                # ocq state — shaded by score
                color = _shade_for_score(score)
                rect = Rectangle((x, y), 1, 1, facecolor=color,
                                 edgecolor=GRAY_LIGHT, linewidth=0.4)
                ax.add_patch(rect)
                # Print numeric score
                txt_color = WHITE if score >= 13 else BLACK
                ax.text(x + 0.5, y + 0.5, f"{int(score)}",
                        ha="center", va="center", fontsize=8.5,
                        fontweight="bold", color=txt_color)

            # Top-15 outline (accent, thicker)
            if (fnum, cletter) in TOP_15_CELLS and (fnum, cletter) != CELL_OF_RECORD:
                outline = Rectangle((x + 0.04, y + 0.04), 0.92, 0.92,
                                    facecolor="none", edgecolor=ACCENT,
                                    linewidth=1.8, zorder=5)
                ax.add_patch(outline)

            # Cell of record (9, G) — double outline
            if (fnum, cletter) == CELL_OF_RECORD:
                outline1 = Rectangle((x + 0.03, y + 0.03), 0.94, 0.94,
                                     facecolor="none", edgecolor=ACCENT,
                                     linewidth=2.4, zorder=6)
                outline2 = Rectangle((x + 0.13, y + 0.13), 0.74, 0.74,
                                     facecolor="none", edgecolor=ACCENT,
                                     linewidth=1.2, zorder=6)
                ax.add_patch(outline1)
                ax.add_patch(outline2)

    # Row labels (function names) on the left
    for ri, (fnum, fname) in enumerate(FUNCTIONS):
        y = n_rows - ri - 1 + 0.5
        # Highlight row 9 (cell of record)
        weight = "bold" if fnum == 9 else "normal"
        color = ACCENT if fnum == 9 else BLACK
        ax.text(-0.20, y, f"{fnum}. {fname}",
                ha="right", va="center", fontsize=8.5,
                color=color, fontweight=weight)

    # Column letter labels at top
    for ci, (cletter, ccap) in enumerate(CAPABILITIES):
        x = ci + 0.5
        # Highlight column G (cell of record)
        weight = "bold" if cletter == "G" else "normal"
        color = ACCENT if cletter == "G" else BLACK
        ax.text(x, n_rows + 0.18, cletter,
                ha="center", va="bottom", fontsize=11,
                fontweight="bold", color=color)
        # Short capability description below the letter
        ax.text(x, n_rows + 1.0, ccap,
                ha="center", va="top", fontsize=6.5,
                color=BLACK)

    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows + 2.5)
    ax.set_aspect("equal")
    ax.set_axis_off()

    # Title + subtitle (figure-level)
    fig.text(0.06, 0.95, "Plate 1 — The 12 × 13 Cell Matrix",
             fontsize=18, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.925,
             "Volume IV  ·  156 cells  ·  OCQ /20  ·  Top-15 outlined  ·  "
             "(9, G) is the cell of record",
             fontsize=10.5, color=BLACK, ha="left")
    fig.text(0.06, 0.905,
             "12 GTM functions on the rows  ·  13 agent capabilities on the columns  ·  "
             "cell coordinate notation (function#, capability_letter).",
             fontsize=9, color=BLACK, ha="left")

    # Legend ribbon (bottom)
    leg_ax = fig.add_axes([0.16, 0.04, 0.78, 0.04])
    leg_ax.set_xlim(0, 100)
    leg_ax.set_ylim(0, 1)
    leg_ax.set_axis_off()

    # Color scale (left half of legend)
    scale_steps = 21
    scale_left = 0.0
    scale_right = 30.0
    bin_w = (scale_right - scale_left) / scale_steps
    for k in range(scale_steps):
        leg_ax.add_patch(Rectangle((scale_left + k * bin_w, 0.55),
                                   bin_w, 0.30,
                                   facecolor=_shade_for_score(k),
                                   edgecolor=GRAY_LIGHT, linewidth=0.2))
    leg_ax.text(scale_left, 0.92, "OCQ shading 0 -> 20 (darker = higher)",
                fontsize=7.5, color=BLACK, ha="left", va="bottom")
    for k in [0, 5, 10, 15, 20]:
        leg_ax.text(scale_left + (k / scale_steps) * (scale_right - scale_left) + bin_w/2,
                    0.40, str(k), fontsize=6.5, color=BLACK,
                    ha="center", va="top")

    # Cell-state legend (right half)
    # Top-15 outline swatch
    leg_ax.add_patch(Rectangle((40, 0.55), 3.5, 0.30,
                               facecolor=_shade_for_score(15),
                               edgecolor=ACCENT, linewidth=1.8))
    leg_ax.text(44, 0.70, "Top-15 cell (accent outline)",
                fontsize=7.5, color=BLACK, ha="left", va="center")

    # Cell of record swatch
    leg_ax.add_patch(Rectangle((58, 0.55), 3.5, 0.30,
                               facecolor=_shade_for_score(19),
                               edgecolor=ACCENT, linewidth=2.4))
    leg_ax.add_patch(Rectangle((58.6, 0.61), 2.3, 0.18,
                               facecolor="none", edgecolor=ACCENT,
                               linewidth=1.0))
    leg_ax.text(62, 0.70, "(9, G) cell of record",
                fontsize=7.5, color=BLACK, ha="left", va="center")

    # n/a swatch
    leg_ax.add_patch(Rectangle((76, 0.55), 3.5, 0.30,
                               facecolor=GRAY_VLIGHT,
                               edgecolor=GRAY_LIGHT, linewidth=0.4))
    leg_ax.text(76 + 1.75, 0.70, "n/a",
                fontsize=6.5, color=GRAY_MED, ha="center", va="center",
                style="italic")
    leg_ax.text(80, 0.70, "structurally inapplicable",
                fontsize=7.5, color=BLACK, ha="left", va="center")

    # gap swatch
    leg_ax.add_patch(Rectangle((76, 0.10), 3.5, 0.30,
                               facecolor=WHITE,
                               edgecolor=GRAY_LIGHT, linewidth=0.4,
                               hatch="///"))
    leg_ax.text(80, 0.25, "identified gap (no score yet)",
                fontsize=7.5, color=BLACK, ha="left", va="center")

    # Source caption
    fig.text(0.06, 0.015,
             "Source: AGENTS_GTM_MASTER Ch 1 §1.1, §1.4, §1.5 and Ch 2 §2.1 cluster reads.",
             fontsize=7.5, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "01_cell_matrix.svg")


# =============================================================================
# Plate 2 — Top-15 Cells Ranked
# =============================================================================

def build_top_15_cells():
    """Horizontal bar chart of the top-15 cells with annotations."""
    fig = _new_fig()
    # Vertical layout — bars go top to bottom (highest OCQ at top)
    ax = fig.add_axes([0.16, 0.07, 0.78, 0.79])

    n = len(TOP_15)
    bar_h = 0.62
    max_score = 20

    # Bars are horizontal, longest = highest OCQ at top
    for i, (fn, cap, score, vendor, gap_text) in enumerate(TOP_15):
        y = n - i - 1   # top of list at top of axis

        # Bar
        is_cor = (fn == CELL_OF_RECORD[0] and cap == CELL_OF_RECORD[1])
        bar_color = ACCENT if is_cor else _shade_for_score(score)
        edge_color = ACCENT if is_cor else BLACK
        edge_w = 2.2 if is_cor else 0.5
        ax.add_patch(Rectangle((0, y - bar_h/2), score, bar_h,
                               facecolor=bar_color,
                               edgecolor=edge_color,
                               linewidth=edge_w))

        # Cell coordinate label (LEFT of bar, large monospace)
        coord_str = f"({fn}, {cap})"
        ax.text(-0.4, y, coord_str,
                ha="right", va="center", fontsize=10,
                fontweight="bold", color=BLACK, family="monospace")

        # OCQ score (right end of bar, white if dark bar)
        txt_color = WHITE if score >= 14 else BLACK
        ax.text(score - 0.3, y, f"{score}/20",
                ha="right", va="center", fontsize=9,
                fontweight="bold", color=txt_color)

        # Vendor (italic, smaller) — RIGHT of bar
        ax.text(max_score + 0.4, y + 0.15, vendor,
                ha="left", va="center", fontsize=7.5,
                color=BLACK, style="italic")
        # Gap one-liner
        ax.text(max_score + 0.4, y - 0.20, gap_text,
                ha="left", va="center", fontsize=6.5,
                color=GRAY_MED)

        # Rank number on far left
        rank_color = ACCENT if is_cor else GRAY_MED
        rank_weight = "bold" if is_cor else "normal"
        ax.text(-3.4, y, f"#{i+1}",
                ha="left", va="center", fontsize=8.5,
                color=rank_color, fontweight=rank_weight)

    # X axis (0..20 OCQ scale at the top)
    ax.set_xlim(-3.5, max_score + 13)
    ax.set_ylim(-0.6, n - 0.2)

    # Top axis ticks for OCQ scale
    for x_tick in [0, 5, 10, 15, 20]:
        ax.plot([x_tick, x_tick], [n - 0.5, n - 0.3],
                color=BLACK, linewidth=0.5)
        ax.text(x_tick, n - 0.15, str(x_tick),
                ha="center", va="bottom", fontsize=7, color=BLACK)
    ax.plot([0, max_score], [n - 0.5, n - 0.5],
            color=BLACK, linewidth=0.5)
    ax.text(max_score / 2, n + 0.05, "OCQ score /20",
            ha="center", va="bottom", fontsize=8, color=BLACK)

    ax.set_axis_off()

    # Title + subtitle
    fig.text(0.06, 0.96, "Plate 2 — Top-15 Cells by OCQ",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.935,
             "Volume IV  ·  ranked by 4-dimension aggregate OCQ score /20.",
             fontsize=10, color=BLACK, ha="left")
    fig.text(0.06, 0.915,
             "(9, G) — agent procurement gauntlet — at the top with 19/20 (cell of record).",
             fontsize=9, color=BLACK, ha="left")

    # Source caption
    fig.text(0.06, 0.02,
             "Source: AGENTS_GTM_MASTER Ch 1 §1.4 (top-15 ranked) cross-checked with Ch 2 §2.1.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "02_top_15_cells.svg")


# =============================================================================
# Plate 3 — GTM Wardley Map at Cell Resolution
# =============================================================================

def build_gtm_wardley_map():
    fig = plt.figure(figsize=(PAGE_H, PAGE_W), facecolor=WHITE)  # 11 x 8.5 landscape
    ax = fig.add_axes([0.07, 0.10, 0.88, 0.78])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()

    # Background grid: 4 evolution columns
    boundaries = [0.0, 0.25, 0.50, 0.75, 1.0]
    stage_labels = ["Genesis", "Custom-Built", "Product", "Commodity / Utility"]
    for b in boundaries:
        ax.plot([b, b], [0, 1], color=GRAY_LIGHT, linewidth=0.5)
    # Axes box
    ax.plot([0, 1], [0, 0], color=BLACK, linewidth=0.6)
    ax.plot([0, 1], [1, 1], color=BLACK, linewidth=0.6)
    ax.plot([0, 0], [0, 1], color=BLACK, linewidth=0.6)
    ax.plot([1, 1], [0, 1], color=BLACK, linewidth=0.6)

    # Stage labels along bottom
    for i, lbl in enumerate(stage_labels):
        cx = (boundaries[i] + boundaries[i+1]) / 2
        ax.text(cx, -0.04, lbl,
                ha="center", va="top", fontsize=9, color=BLACK)

    # Evolution arrow under axis
    ax.annotate("", xy=(0.98, -0.085), xytext=(0.02, -0.085),
                arrowprops=dict(arrowstyle="->", color=BLACK, lw=0.7))
    ax.text(0.5, -0.105, "Evolution",
            ha="center", va="top", fontsize=8, color=BLACK)

    # Y axis label
    ax.text(-0.04, 0.5,
            "Value Chain  (invisible substrate  ->  user-visible)",
            rotation=90, ha="center", va="center", fontsize=9, color=BLACK)

    # Lookup
    comp_pos = {c[0]: (c[1], c[2]) for c in GTM_WARDLEY}

    # Dependency lines (light gray, thin)
    for src, dst in GTM_WARDLEY_DEPS:
        if src in comp_pos and dst in comp_pos:
            x1, y1 = comp_pos[src]
            x2, y2 = comp_pos[dst]
            ax.plot([x1, x2], [y1, y2],
                    color=GRAY_LIGHT, linewidth=0.7, zorder=1)

    # Plot components
    for label, x, y in GTM_WARDLEY:
        is_unclaimed = "unclaimed" in label
        marker_color = ACCENT if is_unclaimed else BLACK
        marker_size = 30 if is_unclaimed else 18
        marker_edge = BLACK if is_unclaimed else None
        ax.scatter([x], [y], s=marker_size, color=marker_color,
                   edgecolors=marker_edge, linewidths=0.6, zorder=3)
        text_weight = "bold" if is_unclaimed else "normal"
        text_color = ACCENT if is_unclaimed else BLACK
        ax.text(x + 0.010, y, label,
                fontsize=6.5, color=text_color,
                fontweight=text_weight,
                ha="left", va="center", zorder=4)

    # Punctuated equilibria arrows (accent)
    pe_codes = ["PE-4", "PE-1", "PE-2", "PE-3", "PE-6", "PE-5"]
    for i, (anchor, dx) in enumerate(GTM_WARDLEY_ARROWS):
        if anchor in comp_pos:
            x, y = comp_pos[anchor]
            x_end = min(x + dx, 0.98)
            ax.annotate("", xy=(x_end, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->", color=ACCENT,
                                        lw=1.8),
                        zorder=5)
            # PE label above arrow midpoint
            ax.text((x + x_end) / 2, y + 0.012, pe_codes[i],
                    fontsize=6.5, color=ACCENT, fontweight="bold",
                    ha="center", va="bottom", zorder=6)

    # Title + subtitle
    fig.text(0.07, 0.94, "Plate 3 — GTM Wardley Map",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.07, 0.915,
             "Volume IV  ·  agent-GTM components by evolution × value chain  ·  "
             "arrows = 2026-2027 punctuated equilibria.",
             fontsize=10, color=BLACK, ha="left")

    # Legend (top right)
    leg_x = 0.74
    leg_y_top = 0.88
    fig.text(leg_x, leg_y_top, "Legend",
             fontsize=8.5, fontweight="bold", color=BLACK, ha="left")

    leg_items = [
        ("Component (named vendor)",         "scatter_black"),
        ("Unclaimed cell of record (9, G)",  "scatter_accent"),
        ("Dependency",                       "line_gray"),
        ("Punctuated equilibrium",           "arrow_accent"),
    ]
    for i, (txt, kind) in enumerate(leg_items):
        y = leg_y_top - 0.022 - i * 0.022
        if kind == "scatter_black":
            fig.add_artist(plt.Circle((leg_x + 0.005, y), 0.004,
                                      color=BLACK, transform=fig.transFigure))
            fig.text(leg_x + 0.018, y, txt,
                     fontsize=7.5, color=BLACK, ha="left", va="center")
        elif kind == "scatter_accent":
            fig.add_artist(plt.Circle((leg_x + 0.005, y), 0.005,
                                      color=ACCENT,
                                      transform=fig.transFigure))
            fig.text(leg_x + 0.018, y, txt,
                     fontsize=7.5, color=BLACK, ha="left", va="center")
        elif kind == "line_gray":
            fig.add_artist(Line2D([leg_x - 0.005, leg_x + 0.015],
                                  [y, y],
                                  color=GRAY_LIGHT, lw=1.2,
                                  transform=fig.transFigure))
            fig.text(leg_x + 0.020, y, txt,
                     fontsize=7.5, color=BLACK, ha="left", va="center")
        elif kind == "arrow_accent":
            fig.add_artist(FancyArrowPatch((leg_x - 0.005, y),
                                           (leg_x + 0.015, y),
                                           arrowstyle="->",
                                           color=ACCENT, lw=1.6,
                                           mutation_scale=10,
                                           transform=fig.transFigure))
            fig.text(leg_x + 0.020, y, txt,
                     fontsize=7.5, color=BLACK, ha="left", va="center")

    # PE key (lower right)
    pe_y_top = 0.75
    fig.text(leg_x, pe_y_top, "Punctuated equilibria",
             fontsize=8.5, fontweight="bold", color=BLACK, ha="left")
    for i, (code, descr) in enumerate(GTM_WARDLEY_PE_LABELS):
        y = pe_y_top - 0.020 - i * 0.020
        fig.text(leg_x, y, f"{code}  {descr}",
                 fontsize=7, color=BLACK, ha="left", va="center")

    fig.text(0.07, 0.01,
             "Source: AGENTS_GTM_MASTER Ch 2 §2.2 component placement + 6 punctuated equilibria.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "03_gtm_wardley_map.svg")


# =============================================================================
# Plate 4 — Powers × Function Grid (12 rows × 7 cols)
# =============================================================================

def build_gtm_powers_grid():
    fig = _new_fig()
    ax = fig.add_axes([0.26, 0.10, 0.70, 0.78])

    n_rows = len(POWERS_BY_FUNCTION)
    n_cols = len(POWERS_COLS)
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows + 0.8)
    ax.set_aspect("equal")
    ax.set_axis_off()

    # Header cells
    for j, c in enumerate(POWERS_COLS):
        ax.text(j + 0.5, n_rows + 0.30, c,
                ha="center", va="bottom", fontsize=7.5,
                fontweight="bold", color=BLACK)

    # Cells + markers
    for i, row in enumerate(POWERS_BY_FUNCTION):
        label = row[0]
        statuses = row[1:8]
        holder = row[8] if len(row) > 8 else ""

        # Row label (LEFT side)
        # Highlight function 9 (cell of record row)
        is_cor_row = "F9" in label
        text_weight = "bold" if is_cor_row else "normal"
        text_color = ACCENT if is_cor_row else BLACK
        ax.text(-0.10, n_rows - i - 1 + 0.5, label,
                ha="right", va="center", fontsize=7.5,
                color=text_color, fontweight=text_weight)

        # Holder annotation (RIGHT side)
        if holder:
            holder_color = ACCENT if is_cor_row else GRAY_MED
            ax.text(n_cols + 0.10, n_rows - i - 1 + 0.5, holder,
                    ha="left", va="center", fontsize=6.5,
                    color=holder_color, style="italic")

        # Cells
        for j, st in enumerate(statuses):
            cx = j + 0.5
            cy = n_rows - i - 1 + 0.5
            rect = Rectangle((j, n_rows - i - 1), 1, 1,
                             facecolor=WHITE, edgecolor=GRAY_LIGHT,
                             linewidth=0.3)
            ax.add_patch(rect)
            if st == "F":
                ax.scatter([cx], [cy], s=70, color=BLACK, zorder=3)
            elif st == "S":
                ax.scatter([cx], [cy], s=80, color=ACCENT, zorder=3,
                           edgecolors=BLACK, linewidths=0.6)
            elif st == "E":
                ax.scatter([cx], [cy], s=70, facecolors="none",
                           edgecolors=BLACK, linewidths=1.0, zorder=3)

    # Title + subtitle
    fig.text(0.06, 0.94, "Plate 4 — Powers × Function Grid",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.915,
             "Volume IV  ·  Helmer's 7 Powers across the 12 GTM functions.",
             fontsize=10, color=BLACK, ha="left")
    fig.text(0.06, 0.895,
             "Who holds, where strengthening or eroding.  F9 (deal-desk) is the cell of record row.",
             fontsize=9, color=BLACK, ha="left")

    # Legend (bottom)
    leg_ax = fig.add_axes([0.26, 0.04, 0.70, 0.04])
    leg_ax.set_xlim(0, 10)
    leg_ax.set_ylim(0, 1)
    leg_ax.set_axis_off()

    leg_ax.scatter([0.3], [0.5], s=70, color=BLACK)
    leg_ax.text(0.55, 0.5, "Held (filled black)",
                fontsize=8, va="center", color=BLACK)

    leg_ax.scatter([2.8], [0.5], s=80, color=ACCENT,
                   edgecolors=BLACK, linewidths=0.6)
    leg_ax.text(3.1, 0.5, "Strengthening (accent blue)",
                fontsize=8, va="center", color=BLACK)

    leg_ax.scatter([6.0], [0.5], s=70, facecolors="none",
                   edgecolors=BLACK, linewidths=1.0)
    leg_ax.text(6.3, 0.5, "Eroding (outline)",
                fontsize=8, va="center", color=BLACK)

    leg_ax.text(8.4, 0.5, "Blank = absent",
                fontsize=8, va="center", color=BLACK)

    fig.text(0.06, 0.005,
             "Source: AGENTS_GTM_MASTER Ch 2 §2.3 (7 Powers per GTM function).",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "04_gtm_powers_grid.svg")


# =============================================================================
# Plate 5 — Bet Coupling and Module Flows
# =============================================================================

def build_bet_coupling_flows():
    """Directed graph: 7 bets + 3 promoted Bet-Cs + absorbed modules + cruxes."""
    fig = plt.figure(figsize=(PAGE_H, PAGE_W), facecolor=WHITE)  # landscape
    ax = fig.add_axes([0.04, 0.05, 0.92, 0.84])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 13)
    ax.set_axis_off()

    # Build lookup of all nodes
    nodes = {}
    for nid, label, kind, x, y in BET_NODES:
        nodes[nid] = (label, kind, x, y)
    for cid, label, x, y in CRUX_NODES:
        nodes[cid] = (label, "crux", x, y)

    # ---- Draw absorption arrows first (gray, thin, into B1) ----
    for src, dst in ABSORPTION_EDGES:
        if src in nodes and dst in nodes:
            _, _, x1, y1 = nodes[src]
            _, _, x2, y2 = nodes[dst]
            ax.annotate("", xy=(x2 - 0.6, y2 + 0.1),
                        xytext=(x1 + 0.5, y1),
                        arrowprops=dict(arrowstyle="->",
                                        color=GRAY_LIGHT,
                                        lw=0.8,
                                        connectionstyle="arc3,rad=0.10"),
                        zorder=1)

    # ---- Draw sequencing arrows (gray, thick) ----
    for src, dst in SEQUENCE_EDGES:
        if src in nodes and dst in nodes:
            _, _, x1, y1 = nodes[src]
            _, _, x2, y2 = nodes[dst]
            # offset so it doesn't overlap node markers
            ax.annotate("", xy=(x2 - 0.55, y2),
                        xytext=(x1 + 0.55, y1),
                        arrowprops=dict(arrowstyle="->",
                                        color=GRAY_MED,
                                        lw=1.6,
                                        connectionstyle="arc3,rad=0.0"),
                        zorder=2)

    # ---- Draw distribution arrows (Bet #6 -> #1, #2, #3a) ----
    for src, dst in DISTRIBUTION_EDGES:
        if src in nodes and dst in nodes:
            _, _, x1, y1 = nodes[src]
            _, _, x2, y2 = nodes[dst]
            ax.annotate("", xy=(x2, y2 - 0.6),
                        xytext=(x1, y1 + 0.4),
                        arrowprops=dict(arrowstyle="->",
                                        color=GRAY_MED,
                                        lw=1.0,
                                        linestyle="--",
                                        connectionstyle="arc3,rad=-0.10"),
                        zorder=2)

    # ---- Draw promotion arrows (dotted accent) ----
    for src, dst in PROMOTION_EDGES:
        if src in nodes and dst in nodes:
            _, _, x1, y1 = nodes[src]
            _, _, x2, y2 = nodes[dst]
            ax.annotate("", xy=(x2 + 0.5, y2 + 0.1),
                        xytext=(x1 - 0.4, y1),
                        arrowprops=dict(arrowstyle="->",
                                        color=ACCENT,
                                        lw=1.5,
                                        linestyle=":",
                                        connectionstyle="arc3,rad=0.15"),
                        zorder=3)

    # ---- Draw crux coupling (accent thick) ----
    for src, dst in CRUX_EDGES:
        if src in nodes and dst in nodes:
            _, _, x1, y1 = nodes[src]
            _, _, x2, y2 = nodes[dst]
            ax.annotate("", xy=(x2 - 0.3, y2 - 0.3),
                        xytext=(x1, y1 + 0.4),
                        arrowprops=dict(arrowstyle="->",
                                        color=ACCENT,
                                        lw=1.4,
                                        alpha=0.75,
                                        connectionstyle="arc3,rad=0.15"),
                        zorder=2.5)

    # ---- Draw nodes (on top) ----
    for nid, (label, kind, x, y) in nodes.items():
        if kind == "bet":
            # Larger filled bet node
            w, h = 1.6, 1.0
            rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                                  boxstyle="round,pad=0.05",
                                  facecolor=WHITE, edgecolor=ACCENT,
                                  linewidth=2.0, zorder=5)
            ax.add_patch(rect)
            ax.text(x, y, label,
                    ha="center", va="center",
                    fontsize=7.5, fontweight="bold",
                    color=ACCENT, zorder=6)
        elif kind == "betc":
            # Bet-C node (smaller, accent dashed)
            w, h = 1.4, 0.85
            rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                                  boxstyle="round,pad=0.04",
                                  facecolor=WHITE, edgecolor=ACCENT,
                                  linewidth=1.4, linestyle="--", zorder=5)
            ax.add_patch(rect)
            ax.text(x, y, label,
                    ha="center", va="center",
                    fontsize=6.5, fontweight="bold",
                    color=ACCENT, zorder=6)
        elif kind == "absorbed":
            # Absorbed bet — gray strikethrough style
            w, h = 1.4, 0.85
            rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                                  boxstyle="round,pad=0.04",
                                  facecolor=GRAY_VLIGHT, edgecolor=GRAY_MED,
                                  linewidth=1.0, zorder=5)
            ax.add_patch(rect)
            ax.text(x, y, label,
                    ha="center", va="center",
                    fontsize=6.5,
                    color=GRAY_MED, zorder=6)
        elif kind == "mod":
            # Absorbed module — small gray pill
            w, h = 1.4, 0.5
            rect = Rectangle((x - w/2, y - h/2), w, h,
                             facecolor=GRAY_VLIGHT, edgecolor=GRAY_LIGHT,
                             linewidth=0.6, zorder=5)
            ax.add_patch(rect)
            ax.text(x, y, label,
                    ha="center", va="center",
                    fontsize=5.8,
                    color=GRAY_MED, zorder=6)
        elif kind == "crux":
            # Crux nodes — small accent circles
            w, h = 1.5, 0.85
            rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                                  boxstyle="round,pad=0.04",
                                  facecolor=WHITE, edgecolor=BLACK,
                                  linewidth=0.8, zorder=5)
            ax.add_patch(rect)
            ax.text(x, y, label,
                    ha="center", va="center",
                    fontsize=6,
                    color=BLACK, zorder=6)

    # ---- Risk-propagation paths (right side, accent thick labeled) ----
    # Place 5 risk boxes along the right edge
    risk_x = 12.3
    risk_y_top = 8.5
    risk_dy = 1.0
    for i, (rid, rlabel, rscore, targets) in enumerate(RISK_BOX_DATA):
        ry = risk_y_top - i * risk_dy
        # Risk box
        rect = Rectangle((risk_x - 0.05, ry - 0.32), 0.7, 0.55,
                         facecolor=WHITE, edgecolor=ACCENT,
                         linewidth=1.2, zorder=7)
        ax.add_patch(rect)
        ax.text(risk_x + 0.30, ry + 0.05, rid,
                ha="center", va="center", fontsize=8,
                fontweight="bold", color=ACCENT, zorder=8)
        ax.text(risk_x + 0.30, ry - 0.17, f"{int(rscore*20)}/20",
                ha="center", va="center", fontsize=6,
                color=ACCENT, zorder=8)

        # Risk label to the right of icon
        ax.text(risk_x - 0.20, ry, rlabel,
                ha="right", va="center", fontsize=6.5,
                color=ACCENT, zorder=8)

        # Arrow from risk to its target bets
        for tgt in targets:
            if tgt in nodes:
                _, _, tx, ty = nodes[tgt]
                arrow = FancyArrowPatch((risk_x - 0.05, ry),
                                        (tx + 0.7, ty),
                                        arrowstyle="->",
                                        color=ACCENT,
                                        lw=1.4,
                                        alpha=0.6,
                                        mutation_scale=10,
                                        connectionstyle="arc3,rad=-0.20",
                                        zorder=2.5)
                ax.add_patch(arrow)

    # ---- Section labels ----
    ax.text(0.5, 12.5, "Absorbed modules", fontsize=8.5, fontweight="bold",
            color=GRAY_MED, ha="left")
    ax.text(5.0, 12.5, "Active Bets (sequenced)", fontsize=8.5,
            fontweight="bold", color=ACCENT, ha="left")
    ax.text(11.0, 12.5, "Promoted Bet-Cs / Risks", fontsize=8.5,
            fontweight="bold", color=ACCENT, ha="left")
    ax.text(3.5, 6.3, "Cruxes (re-rate bets)", fontsize=8.5,
            fontweight="bold", color=BLACK, ha="left")

    # Title + subtitle
    fig.text(0.04, 0.95, "Plate 5 — Bet Coupling and Module Flows",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.04, 0.925,
             "Volume IV  ·  which bets absorb which modules  ·  "
             "which cruxes re-rate which bets  ·  sequencing.",
             fontsize=10, color=BLACK, ha="left")

    # Legend (bottom)
    leg_y = 0.8
    items = [
        ("Bet (active)",           "bet_marker"),
        ("Bet-C (promoted)",       "betc_marker"),
        ("Module (absorbed)",      "mod_marker"),
        ("Crux",                   "crux_marker"),
        ("Module absorption",      "absorption_arrow"),
        ("Sequencing",             "sequence_arrow"),
        ("Bet-C promotion",        "promotion_arrow"),
        ("Crux coupling",          "crux_arrow"),
        ("Risk propagation R1-R5", "risk_arrow"),
        ("Distribution (Bet #6)",  "distribution_arrow"),
    ]
    # 5 per column
    col_x = [0.4, 4.8, 9.2]
    per_col = 4
    for i, (txt, kind) in enumerate(items):
        col = i // per_col
        row = i % per_col
        x = col_x[col]
        y = leg_y - row * 0.45
        if kind == "bet_marker":
            ax.add_patch(FancyBboxPatch((x, y - 0.15), 0.5, 0.30,
                                        boxstyle="round,pad=0.02",
                                        facecolor=WHITE, edgecolor=ACCENT,
                                        linewidth=1.6))
        elif kind == "betc_marker":
            ax.add_patch(FancyBboxPatch((x, y - 0.15), 0.5, 0.30,
                                        boxstyle="round,pad=0.02",
                                        facecolor=WHITE, edgecolor=ACCENT,
                                        linewidth=1.2, linestyle="--"))
        elif kind == "mod_marker":
            ax.add_patch(Rectangle((x, y - 0.12), 0.5, 0.24,
                                   facecolor=GRAY_VLIGHT,
                                   edgecolor=GRAY_LIGHT, linewidth=0.5))
        elif kind == "crux_marker":
            ax.add_patch(FancyBboxPatch((x, y - 0.13), 0.5, 0.26,
                                        boxstyle="round,pad=0.02",
                                        facecolor=WHITE, edgecolor=BLACK,
                                        linewidth=0.8))
        elif kind == "absorption_arrow":
            ax.annotate("", xy=(x + 0.5, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->",
                                        color=GRAY_LIGHT, lw=0.8))
        elif kind == "sequence_arrow":
            ax.annotate("", xy=(x + 0.5, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->",
                                        color=GRAY_MED, lw=1.6))
        elif kind == "promotion_arrow":
            ax.annotate("", xy=(x + 0.5, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->",
                                        color=ACCENT, lw=1.5,
                                        linestyle=":"))
        elif kind == "crux_arrow":
            ax.annotate("", xy=(x + 0.5, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->",
                                        color=ACCENT, lw=1.4, alpha=0.75))
        elif kind == "risk_arrow":
            ax.annotate("", xy=(x + 0.5, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->",
                                        color=ACCENT, lw=1.4, alpha=0.6))
        elif kind == "distribution_arrow":
            ax.annotate("", xy=(x + 0.5, y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->",
                                        color=GRAY_MED, lw=1.0,
                                        linestyle="--"))
        ax.text(x + 0.6, y, txt, ha="left", va="center",
                fontsize=7, color=BLACK)

    fig.text(0.04, 0.01,
             "Source: AGENTS_GTM_MASTER Ch 3 §3.1 (7 bets), §3.2 (3 promoted Bet-Cs), §3.4 (6 cruxes), §3.6.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "05_bet_coupling_flows.svg")


# =============================================================================
# main
# =============================================================================

def main():
    PLATES_DIR.mkdir(parents=True, exist_ok=True)
    build_cell_matrix()
    build_top_15_cells()
    build_gtm_wardley_map()
    build_gtm_powers_grid()
    build_bet_coupling_flows()
    print("Generated:")
    for p in sorted(PLATES_DIR.glob("0*.svg")):
        print(f"  {p}  ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
