"""
SUBSTRATE  ·  Volume IV  ·  AGENTS GTM SUBSTRATE — 5 plates.

A stratigraphic atlas of the agent-GTM intersection. Five plates total:

  I    · CELL INDEX                 (the 156-coordinate reference register)
  II   · BY-FUNCTION DEEP-DIVE A    (Functions I-VI · Marketing + Selling)
  III  · BY-FUNCTION DEEP-DIVE B    (Functions VII-XII · Operations + Post-sale)
  IV   · THE SEVEN-COUNTERPARTY GAUNTLET  (the buyer-side procurement gauntlet)
  V    · TALENT FLOW · NYC PEAK Q2 2026   (feed-stocks → vertical-agent destinations)

Inherits SUBSTRATE design language from Volumes I-III and Volume IV plates I+M:
ink-on-cream palette, hairline rules, condensed display caps, single oxidized
vermilion accent, monospace marginalia, depth-scale tick rule on every page.

Output: AGENTS_GTM_SUBSTRATE.pdf · five pages, plate-by-plate save discipline.
"""
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
import numpy as np

# ============================================================
# Fonts
# ============================================================
FONT_DIR = "/Users/sameoldexpressions/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/f85326cc-c479-4349-956a-d3d47e404d0b/d1370235-0ed8-47e6-859d-0bec833074a3/skills/canvas-design/canvas-fonts"
if os.path.isdir(FONT_DIR):
    for fp in os.listdir(FONT_DIR):
        if fp.endswith((".ttf", ".otf")):
            fm.fontManager.addfont(os.path.join(FONT_DIR, fp))


def fam(filename):
    path = os.path.join(FONT_DIR, filename)
    if os.path.isfile(path):
        return fm.FontProperties(fname=path).get_name()
    return "DejaVu Sans"


F_DISPLAY       = fam("BigShoulders-Bold.ttf")
F_DISPLAY_REG   = fam("BigShoulders-Regular.ttf")
F_NARROW        = fam("Boldonse-Regular.ttf")
F_SERIF         = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT      = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP    = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT = fam("InstrumentSerif-Italic.ttf")
F_MONO          = fam("GeistMono-Regular.ttf")
F_MONO_BOLD     = fam("GeistMono-Bold.ttf")
F_DMMONO        = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
# Treat raw text as text — no math-mode interpretation of $ etc.
mpl.rcParams["text.parse_math"] = False


# ============================================================
# Palette
# ============================================================
PAPER       = "#F1E9D6"
INK         = "#171210"
INK_SOFT    = "#3A2F26"
GRAY        = "#7A6E60"
GRAY_LIGHT  = "#C9BFA9"
GRAY_FAINT  = "#E4DCC4"
RULE        = "#2A211B"
VERMILION   = "#A6371F"
VERDIGRIS   = "#456C5C"
OCHRE       = "#A37425"

DPI = 300
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm/AGENTS_GTM_SUBSTRATE.pdf"


def sp(text, n=1):
    """Letter-space `text` by inserting `n` spaces between glyphs."""
    if n <= 0:
        return text
    sep = " " * n
    out = []
    for ch in text:
        if out:
            out.append(sep)
        out.append(ch)
    return "".join(out)


# ============================================================
# Cell data (shared with build_matrix_plate.py)
# ============================================================
CAPABILITIES = [
    ("A", "RESEARCH",   "Research / enrichment"),
    ("B", "PERSONAL.",  "Personalization + content"),
    ("C", "ORCHESTR.",  "Multi-channel orchestration"),
    ("D", "DIALOG.",    "Conversation handling"),
    ("E", "MEETING",    "Meeting prep / listen / follow-up"),
    ("F", "CRM-GRAPH",  "CRM hygiene / graph"),
    ("G", "MULTI-STEP", "Multi-step task execution"),
    ("H", "FORECAST",   "Forecasting / decision support"),
    ("I", "NEGOTIATE",  "Negotiation / pricing"),
    ("J", "COACH",      "Coaching / performance"),
    ("K", "COMP-USE",   "Computer-use (OSWorld-gated)"),
    ("L", "MEMORY",     "Persistent memory"),
    ("M", "OBSERVE",    "Trajectory observability"),
]

FUNCTIONS = [
    ("1",  "DEMAND-GEN",  "Demand-gen / brand"),
    ("2",  "CONTENT",     "Content / SEO"),
    ("3",  "INBOUND-PLG", "Inbound / PLG"),
    ("4",  "OUTBOUND",    "Outbound SDR"),
    ("5",  "ABM",         "Account-based marketing"),
    ("6",  "NEW-BIZ AE",  "New-biz AE"),
    ("7",  "ENABLE",      "Enablement / training"),
    ("8",  "REV-OPS",     "RevOps / Sales Ops"),
    ("9",  "DEAL-DESK",   "Deal desk / pricing / procurement"),
    ("10", "CS",          "CS / onboarding"),
    ("11", "AM-RENEW",    "AM / renewals / expansion"),
    ("12", "FORECAST",    "Forecasting / strategy"),
]

TOP15 = {
    (9, "G"), (5, "F"), (6, "E"), (4, "A"), (6, "L"),
    (9, "I"), (8, "G"), (4, "K"), (12, "F"), (12, "H"),
    (4, "M"), (9, "M"), (11, "L"), (3, "A"), (6, "K"),
}

# Imported full-resolution from build_matrix_plate.py; status glyph derived from
# the synthesis. (function, capability, ocq, vendor_abbr, stratum, status, desc)
CELLS = [
    # F1 — Demand-gen / brand
    (1, "A", 11, "6sn Dmb",  "IX",  "M", "TAL firmographic+intent"),
    (1, "B", None,"Mut Jsp",  "IX",  "M", "50-variant CAC drag"),
    (1, "C", None,"Optm Mkt", "IX",  "F", "Cross-channel handoff"),
    (1, "D", None,"Drft Itr", "IX",  "M", "Visitor->MQL dialogue"),
    (1, "F", None,"6sn Dmb",  "IX",  "F", "Account-graph hygiene"),
    (1, "G", None,"Jsp Sf",   "IX",  "F", "Multi-step demand"),
    (1, "H", None,"6sn SF",   "IX",  "F", "Spend allocation"),
    (1, "K", 13,  "Adb Cnv",  "IX",  "U", "Creative GUI ops"),
    (1, "L", None,"6sn",      "IX",  "F", "Acct-only memory"),
    (1, "M", 14,  "[gap]",    "VII", "G", "FTC/EU audit gap"),
    # F2 — Content / SEO
    (2, "A", None,"Srf Clr",  "IX",  "M", "Topic-cluster research"),
    (2, "B", None,"Jsp Wrt",  "IX",  "M", "Most commoditized cell"),
    (2, "G", 9,   "Jsp Cpy",  "IX",  "F", "Brief->draft->publish"),
    (2, "K", 13,  "Rnw Adb",  "IX",  "U", "Creative GUI ops"),
    (2, "L", None,"Wrtr",     "IX",  "F", "Brand-voice memory"),
    (2, "M", 12,  "[gap]",    "VII", "G", "FTC AI-washing"),
    (2, "H", None,"Clr Mrk",  "IX",  "M", "Topic-traffic predict"),
    # F3 — Inbound / PLG
    (3, "A", 14,  "ComR Pcs", "IX",  "F", "PQL identification"),
    (3, "D", None,"Itc Drf",  "IX",  "M", "In-product qualify+book"),
    (3, "F", None,"ComR",     "IX",  "F", "PQL signal routing"),
    (3, "G", None,"ComR Def", "IX",  "F", "PQL->enrich->assign"),
    (3, "H", None,"Pcs",      "IX",  "F", "Free->paid conv predict"),
    (3, "K", None,"HyG Tvs",  "IX",  "U", "In-product walkthrough"),
    (3, "L", None,"ComR",     "IX",  "F", "Cross-org PLG memory"),
    (3, "M", None,"[gap]",    "VII", "G", "PLG-funnel agent audit"),
    # F4 — Outbound SDR
    (4, "A", 16,  "Cly Apl",  "IX",  "M", "<30s pre-call research"),
    (4, "B", 10,  "11x AiS",  "IX",  "M", "Synthetic SDR ceiling"),
    (4, "C", 11,  "Otr Slf",  "IX",  "M", "Cross-channel sequencing"),
    (4, "D", 12,  "11x Nks",  "IX",  "F", "Auto-resolve low stakes"),
    (4, "E", 13,  "Grn Gng",  "IX",  "U", "SDR->AE handoff seam"),
    (4, "F", 14,  "Cly ComR", "IX",  "U", "Hygiene-as-code"),
    (4, "G", 9,   "11x AiS",  "IX",  "V", "Autonomous SDR loop"),
    (4, "H", 11,  "Cla BUp",  "IX",  "U", "SDR-quality decay"),
    (4, "J", 11,  "Gng Chr",  "IX",  "M", "Call quality at scale"),
    (4, "K", 15,  "Ant Opr",  "II",  "U", "LinkedIn GUI driving"),
    (4, "L", 12,  "Mm0 Lta",  "IV",  "U", "Cross-prospect memory"),
    (4, "M", 14,  "LSm Brn",  "VII", "U", "TCPA evidence audit"),
    # F5 — ABM
    (5, "A", 12,  "6sn Cly",  "IX",  "M", "Account intent"),
    (5, "B", 9,   "Mut 6sn",  "IX",  "M", "Named-acct personalize"),
    (5, "C", 10,  "Dmb 6sn",  "IX",  "M", "Cross-acct orchestration"),
    (5, "D", 9,   "Drf Qlf",  "IX",  "F", "Named-acct routing"),
    (5, "E", 11,  "Gng Dlh",  "IX",  "U", "Cross-committee brief"),
    (5, "F", 18,  "ComR SNv", "IX",  "U", "Top single cell — committee map"),
    (5, "G", 8,   "6sn Dmb",  "IX",  "V", "Autonomous ABM"),
    (5, "H", 9,   "6sn Cla",  "IX",  "M", "ABM forecasting"),
    (5, "K", 9,   "Mar Opr",  "II",  "F", "ABM platform driving"),
    (5, "L", 13,  "[gap]",    "IV",  "U", "Multi-year ABM memory"),
    (5, "M", 11,  "[gap]",    "VII", "U", "ABM agent observability"),
    # F6 — New-biz AE
    (6, "A", 14,  "Hbb Rog",  "IX",  "M", "Hebbia/Rogo NYC anchor"),
    (6, "B", 12,  "Acv Cla",  "IX",  "F", "Post-call MAP draft"),
    (6, "C", 9,   "Otr Slf",  "IX",  "M", "AE cadences"),
    (6, "D", 13,  "Acv Crs",  "IX",  "M", "Real-time objection"),
    (6, "E", 17,  "Gng Chr",  "IX",  "U", "Deal-diagnosis causation"),
    (6, "F", 11,  "Pep Scr",  "IX",  "M", "Activity capture"),
    (6, "G", 8,   "Agf 11x",  "IX",  "V", "Autonomous AE"),
    (6, "H", 12,  "Cla BUp",  "IX",  "M", "AE deal-level forecast"),
    (6, "I", 13,  "Prf DLH",  "IX",  "U", "Real-time discount nego"),
    (6, "J", 12,  "Gng Crs",  "IX",  "M", "AE manager coaching"),
    (6, "K", 14,  "Ant Opr",  "II",  "F", "AE motion GUI ops"),
    (6, "L", 16,  "Mm0 Lta",  "IV",  "U", "6-9mo deal cycle memory"),
    (6, "M", 13,  "LSm Brn",  "VII", "U", "AE agent audit pre-auto"),
    # F7 — Enablement / training
    (7, "A", 8,   "Hsp Sm",   "IX",  "M", "Enablement research"),
    (7, "B", 8,   "Hsp Sm",   "IX",  "M", "Content personalize"),
    (7, "C", 8,   "Hsp Sm",   "IX",  "M", "Multi-channel enable"),
    (7, "D", 9,   "Gng Grn",  "IX",  "M", "Role-play / sim"),
    (7, "E", 9,   "MTk Grn",  "IX",  "M", "Meeting practice"),
    (7, "G", 11,  "MTk Spk",  "IX",  "U", "Cert end-to-end"),
    (7, "J", 13,  "Hsp MTk",  "IX",  "U", "Trajectory-grade coach"),
    (7, "K", 9,   "HyB SN",   "IX",  "F", "Coach via screen"),
    (7, "L", 8,   "[gap]",    "IV",  "U", "Per-rep memory"),
    (7, "M", 13,  "Glo Brn",  "VII", "U", "Coaching agent audit"),
    # F8 — RevOps / Sales Ops
    (8, "A", 7,   "Cla Pcs",  "IX",  "M", "RevOps Account 360"),
    (8, "F", 11,  "Sft Trv",  "IX",  "M", "CRM hygiene multi-tenant"),
    (8, "G", 15,  "Cla BUp",  "IX",  "U", "Pipeline-scrub loop closure"),
    (8, "H", 10,  "Cla Avi",  "IX",  "M", "Forecasting MAPE plateau"),
    (8, "K", 12,  "Ant CU",   "II",  "U", "RevOps drives SFDC UI"),
    (8, "L", 7,   "Cla BUp",  "IX",  "M", "History-aware forecast"),
    (8, "M", 12,  "Gng Glo",  "VII", "F", "RevOps automation audit"),
    # F9 — Deal desk / procurement
    (9, "A", 9,   "AS CBI",   "IX",  "U", "Deal-desk buyer brief"),
    (9, "B", 8,   "DLH Sub",  "IX",  "F", "Proposal personalize"),
    (9, "G", 19,  "Lpo Vnt",  "IX",  "U", "THE CELL OF RECORD — procurement gauntlet"),
    (9, "I", 16,  "Irc LSq",  "IX",  "U", "AI-specific contract addenda"),
    (9, "K", 13,  "SF Sub",   "IX",  "F", "Coupa/Ariba automation"),
    (9, "L", 10,  "Irc LSq",  "IX",  "U", "Counterparty-history mem"),
    (9, "M", 14,  "Glo Lng",  "VII", "U", "Trajectory evidence pack"),
    # F10 — CS / onboarding
    (10,"A", 8,   "Zd Itc",   "IX",  "M", "Customer research"),
    (10,"B", 8,   "Zd Itc",   "IX",  "M", "Onboarding personalize"),
    (10,"C", 9,   "Itc Frt",  "IX",  "M", "Cross-channel CS"),
    (10,"D", 14,  "Sie Dec",  "IX",  "M", "Densest cell in agent-GTM by $"),
    (10,"E", 12,  "Gst Cat",  "IX",  "U", "QBR/kickoff brief"),
    (10,"F", 11,  "Itc Pyl",  "IX",  "M", "CDP-class hygiene"),
    (10,"G", 13,  "Sie Dec",  "IX",  "F", "Refunds w/ rollback"),
    (10,"K", 10,  "Ant CU",   "II",  "F", "Help-desk GUI"),
    (10,"L", 11,  "Sie Dec",  "IX",  "F", "RAG ≠ durable memory"),
    (10,"M", 12,  "Lkr Glo",  "VII", "F", "Audit when agent fails"),
    # F11 — AM / renewals / expansion
    (11,"A", 10,  "Gst Cat",  "IX",  "U", "Renewal-cycle research"),
    (11,"B", 9,   "[gap]",    "IX",  "U", "Renewal pitch personalize"),
    (11,"E", 11,  "Gst Grn",  "IX",  "U", "QBR/EBR briefing"),
    (11,"G", 13,  "SF Gst",   "IX",  "U", "Renewal trajectory loop"),
    (11,"H", 12,  "Gst CZ",   "IX",  "M", "NRR forecast"),
    (11,"I", 13,  "Sie Itc",  "IX",  "U", "Outcome-pricing experiment"),
    (11,"K", 9,   "[gap]",    "II",  "U", "ERP/CS for renewal ops"),
    (11,"L", 14,  "Sie Mm0",  "IX",  "U", "Multi-quarter agent memory"),
    (11,"M", 11,  "Lkr Glo",  "VII", "F", "AM agent audit"),
    # F12 — Forecasting / strategy
    (12,"A", 8,   "Cla Pgm",  "IX",  "F", "Strat research"),
    (12,"B", 8,   "Cla Pgm",  "IX",  "F", "Strat personalize"),
    (12,"C", 9,   "Cla Pgm",  "IX",  "F", "Strat orchestrate"),
    (12,"D", 14,  "Hex Def",  "IX",  "F", "NL->SQL Hex NYC"),
    (12,"F", 15,  "Cla Gln",  "IX",  "M", "Cross-system narrative"),
    (12,"G", 10,  "Pgm Mos",  "IX",  "F", "Strat multi-step"),
    (12,"H", 15,  "Cla Avi",  "IX",  "M", "ARR landing ±5%"),
    (12,"I", 8,   "[gap]",    "IX",  "U", "Self-correct past miss"),
    (12,"J", 9,   "Cla Pgm",  "IX",  "F", "Strategy coaching"),
    (12,"K", 11,  "Pgm Mos",  "IX",  "F", "Cross-BI GUI assembly"),
    (12,"L", 13,  "BUp Mm0",  "IV",  "U", "8-quarter decay memory"),
    (12,"M", 10,  "Glo Arz",  "VII", "U", "Meta-observability"),
]

CELL_BY = {(f, c): (ocq, vnd, strat, st, desc)
           for (f, c, ocq, vnd, strat, st, desc) in CELLS}


# Status colors (geological-discipline glyph grammar drawn with patches)
#   M = mature (filled circle)
#   F = forming (half-filled circle)
#   U = under-served (open circle, vermilion)
#   V = vapor (cross — x)
#   G = gap (open square, verdigris)
STATUS_COLOR = {
    "M": INK,
    "F": INK_SOFT,
    "U": VERMILION,
    "V": GRAY,
    "G": VERDIGRIS,
}


def draw_status_glyph(ax, x, y, status, *, size=0.55):
    """Render a 5-letter status glyph as a small geometric mark."""
    color = STATUS_COLOR.get(status, GRAY)
    if status == "M":
        ax.add_patch(mpatches.Circle((x, y), size, fc=color, ec=color, lw=0))
    elif status == "F":
        # Half-filled circle — ring + half-fill wedge
        ax.add_patch(mpatches.Circle((x, y), size, fill=False, ec=color, lw=0.55))
        ax.add_patch(mpatches.Wedge((x, y), size, 90, 270,
                                    fc=color, ec=color, lw=0))
    elif status == "U":
        # Open circle
        ax.add_patch(mpatches.Circle((x, y), size, fill=False, ec=color, lw=0.7))
    elif status == "V":
        # Cross — two short rules
        d = size * 0.85
        ax.plot([x - d, x + d], [y - d, y + d], color=color, lw=0.55)
        ax.plot([x - d, x + d], [y + d, y - d], color=color, lw=0.55)
    elif status == "G":
        # Open square
        d = size * 0.9
        ax.add_patch(mpatches.Rectangle((x - d, y - d), 2 * d, 2 * d,
                                        fill=False, ec=color, lw=0.55))


# ============================================================
# Shared page-frame helper (Tabloid portrait 11×17 by default)
# ============================================================
def new_page(page_w=11.0, page_h=17.0, xlim=100, ylim=154.5):
    fig = plt.figure(figsize=(page_w, page_h), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)
    ax.set_facecolor(PAPER)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax, *, plate_no, plate_label, title, subtitle, latin,
               xlim=100, ylim=154.5, landscape=False):
    """Shared frame chrome — outer rule, header/footer rules, depth-scale,
    title block, vermilion plate badge, marginalia."""
    if landscape:
        LEFT, RIGHT = 7.5, xlim - 7.5
        TOP, BOTTOM = ylim - 5.5, 6.0
    else:
        LEFT, RIGHT = 8.5, xlim - 7.5
        TOP, BOTTOM = ylim - 6.0, 9.5

    # Outer rectangle
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.55))
    # Header / footer internal rules
    ax.plot([LEFT, RIGHT], [TOP - 6.0, TOP - 6.0], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 4.5, BOTTOM + 4.5], color=RULE, lw=0.45)

    # Left depth-scale tick rule
    ax.plot([LEFT - 2.6, LEFT - 2.6], [BOTTOM + 4.5, TOP - 6.0],
            color=RULE, lw=0.4)
    n_ticks = 28 if not landscape else 22
    ys = np.linspace(BOTTOM + 4.5, TOP - 6.0, n_ticks)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([LEFT - 2.6 - (1.0 if long else 0.5), LEFT - 2.6],
                [y, y], color=RULE, lw=0.35)
        if long:
            ax.text(LEFT - 4.1, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=4.4, fontname=F_DMMONO, color=GRAY)

    # Title block — top-left
    ax.text(LEFT, TOP - 1.0,
            sp("AN ATLAS OF THE AGENT STRATA  ·  VOL IV  ·  AGENTS GTM SUBSTRATE", 4),
            ha="left", va="top", fontsize=6.0, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 1.9, title.upper(),
            ha="left", va="top", fontsize=18, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.6, TOP - 2.0, sp(plate_label, 2),
            ha="right", va="top", fontsize=7.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 4.5, subtitle,
            ha="left", va="top", fontsize=6.2, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4, latin,
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)

    # Vermilion plate badge — top-right
    ax.add_patch(mpatches.Circle((RIGHT - 1.4, TOP - 2.0), 1.05,
                                 fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 1.4, TOP - 2.0, plate_no, ha="center", va="center",
            fontsize=6.2, fontname=F_MONO_BOLD, color=VERMILION)

    # Footer marginalia
    ax.text(LEFT, BOTTOM + 3.0,
            sp("SUBSTRATE  ·  VOL IV  ·  AGENTS GTM  ·  MMXXVI  ·  MAY", 3),
            ha="left", va="top", fontsize=4.6, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.4,
            sp("Compiled for A. Yedi  ·  Cycle MMXXVI  ·  Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, plate_label, ha="right", va="top",
            fontsize=5.4, fontname=F_DMMONO, color=GRAY)
    ax.text((LEFT + RIGHT) / 2, BOTTOM + 1.4, "·   ·   ·   ·   ·",
            ha="center", va="top", fontsize=5, fontname=F_MONO, color=GRAY_LIGHT)

    return LEFT, RIGHT, TOP - 6.5, BOTTOM + 4.7


# ============================================================
# PLATE I — CELL INDEX (the 156-coordinate textbook register)
# ============================================================
def plate_I_cell_index(pdf):
    fig, ax = new_page(11.0, 17.0)
    L, R, TOP, BOT = page_frame(
        ax,
        plate_no="I",
        plate_label="PLATE I OF V",
        title="Cell Index · 12 × 13 = 156 Coordinates",
        subtitle="The full cellular register of the agent-GTM intersection — every coordinate, every status glyph, every score in descending OCQ.",
        latin="Tabula coordinatarum CLVI · ordo per OCQ descendens · status per glypham · forma referendi",
    )

    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Header strip
    ax.text(inner_x0, TOP - 0.6,
            sp("TWO COLUMN REGISTER  ·  GEOGRAPHIC LEFT  ·  RANKED RIGHT", 2),
            ha="left", va="top", fontsize=6.6, fontname=F_DISPLAY, color=VERMILION)
    ax.plot([inner_x0, inner_x1], [TOP - 2.4, TOP - 2.4], color=RULE, lw=0.4)

    # ---- LEFT COLUMN — geographic-order register --------------------------
    # 156 rows organized as f1A...f1M, f2A...f12M; we render only the 102
    # mapped cells (omit empties for readability) but in geographic order.
    mid_x = (inner_x0 + inner_x1) / 2 - 1.0
    left_x0 = inner_x0
    left_x1 = mid_x - 1.0
    right_x0 = mid_x + 1.0
    right_x1 = inner_x1

    # Column headers
    col_top = TOP - 4.0
    ax.text(left_x0, col_top + 0.3, sp("LEFT  ·  GEOGRAPHIC ORDER  ·  F1A - F12M", 2),
            fontsize=5.0, fontname=F_MONO, color=INK_SOFT)
    ax.text(right_x0, col_top + 0.3, sp("RIGHT  ·  TOP 30 BY OCQ  ·  19 - 12", 2),
            fontsize=5.0, fontname=F_MONO, color=VERMILION)
    ax.plot([left_x0, left_x1], [col_top - 0.6, col_top - 0.6],
            color=RULE, lw=0.35)
    ax.plot([right_x0, right_x1], [col_top - 0.6, col_top - 0.6],
            color=RULE, lw=0.35)

    # The geographic register (sorted by function, then capability)
    rows_geo = sorted(CELLS, key=lambda r: (r[0], r[1]))

    # We have ~102 rows; render in two sub-columns within the left half to fit.
    avail_top = col_top - 1.5
    avail_bot = BOT + 22.0

    # Split left side into two sub-cols
    n_geo = len(rows_geo)
    half = (n_geo + 1) // 2
    left_subcols = [rows_geo[:half], rows_geo[half:]]
    sub_w = (left_x1 - left_x0) / 2

    row_h_geo = (avail_top - avail_bot) / max(half, 1)
    row_h_geo = min(row_h_geo, 1.25)  # cap so the rows don't get giant

    for sub_i, sub_rows in enumerate(left_subcols):
        sx0 = left_x0 + sub_i * sub_w + 0.3
        sx1 = sx0 + sub_w - 0.5
        y_cursor = avail_top - 0.2
        # mini header
        ax.text(sx0, y_cursor + 0.0,
                sp("COORD  STATUS  OCQ  · DESCRIPTOR", 1),
                ha="left", va="bottom",
                fontsize=3.6, fontname=F_MONO, color=GRAY)
        ax.plot([sx0, sx1], [y_cursor - 0.2, y_cursor - 0.2],
                color=RULE, lw=0.2)
        for (f, c, ocq, vnd, strat, st, desc) in sub_rows:
            y_cursor -= row_h_geo
            if y_cursor < avail_bot:
                break
            coord = f"({f:>2},{c})"
            # is this a top-15 cell?
            is_top = (f, c) in TOP15
            coord_color = VERMILION if is_top else INK_SOFT
            # coord
            ax.text(sx0, y_cursor, coord, ha="left", va="center",
                    fontsize=4.6, fontname=F_DMMONO, color=coord_color)
            # status glyph (drawn as a geometric mark)
            draw_status_glyph(ax, sx0 + 6.5, y_cursor, st, size=0.40)
            # ocq
            ocq_s = f"{ocq:>2}" if ocq is not None else " -"
            ax.text(sx0 + 9.5, y_cursor, ocq_s, ha="left", va="center",
                    fontsize=4.5, fontname=F_MONO_BOLD,
                    color=VERMILION if is_top else INK_SOFT)
            # descriptor (truncated)
            d = desc if len(desc) <= 32 else desc[:31] + "..."
            ax.text(sx0 + 13.0, y_cursor, d, ha="left", va="center",
                    fontsize=4.2, fontname=F_SERIF_IT, color=INK)

    # ---- RIGHT COLUMN — top 30 by OCQ ------------------------------------
    rows_scored = [r for r in CELLS if r[2] is not None]
    rows_top = sorted(rows_scored, key=lambda r: (-r[2], r[0], r[1]))[:30]

    y_cursor = avail_top - 0.2
    ax.text(right_x0 + 0.2, y_cursor,
            sp("RANK  COORD  STATUS  OCQ  · DESCRIPTOR", 1),
            ha="left", va="bottom",
            fontsize=3.8, fontname=F_MONO, color=VERMILION)
    ax.plot([right_x0, right_x1], [y_cursor - 0.2, y_cursor - 0.2],
            color=RULE, lw=0.25)

    row_h_top = min(1.55, (avail_top - avail_bot) / max(len(rows_top), 1))

    for rank, (f, c, ocq, vnd, strat, st, desc) in enumerate(rows_top, start=1):
        y_cursor -= row_h_top
        if y_cursor < avail_bot:
            break
        coord = f"({f:>2},{c})"
        is_top = (f, c) in TOP15

        # Rank in a tiny circle
        cx = right_x0 + 1.0
        ax.add_patch(mpatches.Circle((cx, y_cursor), 0.85,
                                     fc=VERMILION if is_top else PAPER,
                                     ec=VERMILION, lw=0.5))
        ax.text(cx, y_cursor, f"{rank:02d}",
                ha="center", va="center",
                fontsize=4.4, fontname=F_DMMONO,
                color=PAPER if is_top else VERMILION)
        # coord
        ax.text(right_x0 + 2.8, y_cursor, coord, ha="left", va="center",
                fontsize=5.2, fontname=F_DMMONO,
                color=VERMILION if is_top else INK)
        # status glyph (geometric)
        draw_status_glyph(ax, right_x0 + 9.0, y_cursor, st, size=0.55)
        # ocq
        ax.text(right_x0 + 11.5, y_cursor, f"{ocq:>2}", ha="left", va="center",
                fontsize=6.2, fontname=F_MONO_BOLD,
                color=VERMILION if is_top else INK)
        # vendor
        v = vnd if vnd and vnd != "[gap]" else "-"
        ax.text(right_x0 + 16.0, y_cursor, v, ha="left", va="center",
                fontsize=4.1, fontname=F_DMMONO, color=GRAY)
        # descriptor
        d = desc if len(desc) <= 36 else desc[:35] + "..."
        ax.text(right_x0 + 23.0, y_cursor, d, ha="left", va="center",
                fontsize=4.4, fontname=F_SERIF_IT, color=INK_SOFT)
        # stratum tag (right edge)
        ax.text(right_x1 - 0.3, y_cursor, f"[{strat}]", ha="right", va="center",
                fontsize=4.0, fontname=F_SERIF_IT, color=GRAY)

    # ---- KEY (footer) ----------------------------------------------------
    key_top = BOT + 19.0
    ax.plot([inner_x0, inner_x1], [key_top, key_top], color=RULE, lw=0.45)
    ax.text(inner_x0, key_top - 0.6, sp("HOW TO READ THE GLYPHS", 3),
            ha="left", va="top", fontsize=5.0, fontname=F_MONO, color=VERMILION)

    key_entries = [
        ("M", "MATURE",        "Saturated category; incumbents installed."),
        ("F", "FORMING",       "Real vendors, real revenue, category not crystallized."),
        ("U", "UNDER-SERVED",  "Demand visible, supply thin or sub-scale - the working ground."),
        ("V", "VAPOR",         "Vendor noise high; production deployments rare or failing."),
        ("G", "GAP",           "No incumbent owner; regulatorily forced or strategically open."),
    ]
    for i, (st, name, desc) in enumerate(key_entries):
        x = inner_x0 + 0.4 + i * ((inner_x1 - inner_x0) / 5)
        # Geometric glyph + lettered legend
        draw_status_glyph(ax, x + 0.6, key_top - 3.0, st, size=0.85)
        ax.text(x + 2.5, key_top - 2.2, name, ha="left", va="center",
                fontsize=6.0, fontname=F_DISPLAY, color=INK)
        ax.text(x + 2.5, key_top - 3.8, desc, ha="left", va="center",
                fontsize=4.3, fontname=F_SERIF_IT, color=INK_SOFT)

    # Second key row — OCQ + stratum tags + Top-15 marker
    ax.plot([inner_x0, inner_x1], [key_top - 5.5, key_top - 5.5],
            color=RULE, lw=0.25)
    ax.text(inner_x0, key_top - 6.1, sp("AUXILIARY MARKS", 3),
            ha="left", va="top", fontsize=4.8, fontname=F_MONO, color=GRAY)

    aux = [
        ("OCQ /20", "Composite of opportunity × claimability × time-to-monetize."),
        ("[II/IV/VII/VIII/IX/X]", "Stratum tag — substrate vs vertical product layer."),
        ("Vermilion ring", "Top-15 by OCQ — the cells of accruing equity."),
        ("Coord (F, C)", "Function 1-12 × Capability A-M (see Plate II/III)."),
    ]
    for i, (label, desc) in enumerate(aux):
        x = inner_x0 + 0.4 + i * ((inner_x1 - inner_x0) / 4)
        ax.text(x, key_top - 7.5, label, ha="left", va="center",
                fontsize=4.8, fontname=F_DMMONO, color=VERMILION)
        ax.text(x, key_top - 8.8, desc, ha="left", va="center",
                fontsize=4.1, fontname=F_SERIF_IT, color=INK_SOFT)

    # Tally
    ax.plot([inner_x0, inner_x1], [key_top - 10.5, key_top - 10.5],
            color=RULE, lw=0.25)
    ax.text(inner_x0, key_top - 11.2, sp("TALLY", 3),
            ha="left", va="top", fontsize=4.8, fontname=F_MONO, color=GRAY)
    tally_text = [
        ("156", "TOTAL COORDINATES"),
        (str(len(CELLS)), "CELLS MAPPED MAY 2026"),
        (str(len([r for r in CELLS if r[2] is not None])), "WITH OCQ SCORE"),
        ("15", "TOP-15 VERMILION"),
        ("19/20", "PEAK (9, G)"),
    ]
    for i, (val, lbl) in enumerate(tally_text):
        x = inner_x0 + 0.4 + i * ((inner_x1 - inner_x0) / 5)
        ax.text(x, key_top - 13.0, val, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        ax.text(x, key_top - 14.5, lbl, ha="left", va="center",
                fontsize=4.0, fontname=F_MONO, color=GRAY)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# Function-deep-dive shared helpers (Plates II + III)
# ============================================================
def cell_fill_intensity(ocq, is_top):
    """Return (color, alpha) for cell fill in function-row registers."""
    if ocq is None:
        return GRAY_FAINT, 0.30
    if is_top:
        s = (ocq - 13) / 6.0
        return VERMILION, max(0.55, min(1.0, 0.55 + 0.45 * s))
    s = (ocq - 6) / 9.0
    return INK, max(0.10, min(0.65, 0.10 + 0.55 * s))


def render_function_register(ax, *, x0, x1, y_top, y_bot, functions_subset,
                              cluster_brackets, header_text):
    """
    Renders a horizontal-per-function register:
        F# | F NAME | [A B C D E F G H I J K L M] | callouts
    Cells filled by OCQ intensity; Top-15 vermilion-bordered.
    """
    n_funcs = len(functions_subset)
    n_caps = len(CAPABILITIES)

    # Layout: left gutter for function label, then 13 column cells
    gutter_w = 18.0
    row_h = (y_top - y_bot) / n_funcs
    cell_x0 = x0 + gutter_w
    cell_x1 = x1 - 1.5
    col_w = (cell_x1 - cell_x0) / n_caps

    # Capability headers above the first row
    head_y = y_top + 1.4
    ax.plot([cell_x0, cell_x1], [y_top + 0.4, y_top + 0.4], color=RULE, lw=0.4)
    for ci, (letter, short, _) in enumerate(CAPABILITIES):
        cx = cell_x0 + ci * col_w + col_w / 2
        ax.text(cx, head_y + 0.4, letter, ha="center", va="center",
                fontsize=7.5, fontname=F_DISPLAY, color=INK)
        ax.text(cx, head_y - 0.9, sp(short, 0), ha="center", va="center",
                fontsize=3.6, fontname=F_MONO, color=VERMILION)

    # Section header text (above letters)
    ax.text(x0, head_y + 1.8, header_text,
            ha="left", va="center", fontsize=5.0, fontname=F_MONO, color=GRAY)

    # The function rows
    for ri, (fnum_s, short, desc) in enumerate(functions_subset):
        fnum = int(fnum_s)
        y_t = y_top - ri * row_h
        y_b = y_t - row_h

        # gutter: F#, name, descriptor
        ax.add_patch(mpatches.Circle((x0 + 1.4, (y_t + y_b) / 2),
                                     1.1, fc=PAPER, ec=VERMILION, lw=0.55))
        ax.text(x0 + 1.4, (y_t + y_b) / 2, fnum_s,
                ha="center", va="center",
                fontsize=5.6, fontname=F_DMMONO, color=VERMILION)
        ax.text(x0 + 3.5, (y_t + y_b) / 2 + 0.7, short,
                ha="left", va="center",
                fontsize=7.3, fontname=F_DISPLAY, color=INK)
        ax.text(x0 + 3.5, (y_t + y_b) / 2 - 1.0, desc,
                ha="left", va="center",
                fontsize=4.0, fontname=F_SERIF_IT, color=GRAY)

        # Cells across capabilities
        for ci, (letter, _, _) in enumerate(CAPABILITIES):
            x_left = cell_x0 + ci * col_w
            cell_top = y_t - 0.05
            cell_bot = y_b + 0.15

            # Cell outline
            ax.add_patch(mpatches.Rectangle((x_left, cell_bot),
                                            col_w - 0.05,
                                            cell_top - cell_bot,
                                            fill=False, ec=GRAY_LIGHT,
                                            lw=0.2))
            data = CELL_BY.get((fnum, letter))
            if data is None:
                continue
            ocq, vnd, strat, st, desc = data
            is_top = (fnum, letter) in TOP15
            fc, a = cell_fill_intensity(ocq, is_top)
            ax.add_patch(mpatches.Rectangle((x_left + 0.15, cell_bot + 0.10),
                                            col_w - 0.35,
                                            cell_top - cell_bot - 0.2,
                                            fc=fc, ec="none", alpha=a))
            if is_top:
                ax.add_patch(mpatches.Rectangle((x_left + 0.15, cell_bot + 0.10),
                                                col_w - 0.35,
                                                cell_top - cell_bot - 0.2,
                                                fill=False, ec=VERMILION,
                                                lw=0.7))
            # Inscription rules
            #  - High-OCQ vermilion cells: dark-on-light vendor name + ocq
            #  - Mid cells: ocq small
            if is_top:
                txt_c = PAPER if a > 0.55 else INK
                ax.text(x_left + col_w / 2, cell_top - 0.7, vnd,
                        ha="center", va="center",
                        fontsize=3.8, fontname=F_DMMONO, color=txt_c)
                ax.text(x_left + col_w / 2, cell_bot + 0.55, f"{ocq:02d}",
                        ha="center", va="center",
                        fontsize=4.8, fontname=F_MONO_BOLD, color=txt_c)
            else:
                txt_c = PAPER if (fc == INK and a > 0.45) else INK_SOFT
                if ocq is not None:
                    ax.text(x_left + col_w / 2, (cell_top + cell_bot) / 2,
                            f"{ocq:02d}",
                            ha="center", va="center",
                            fontsize=4.0, fontname=F_MONO_BOLD, color=txt_c)
                else:
                    ax.text(x_left + col_w / 2, (cell_top + cell_bot) / 2,
                            "—",
                            ha="center", va="center",
                            fontsize=3.4, fontname=F_DMMONO, color=GRAY)

        # row hairline
        ax.plot([cell_x0, cell_x1], [y_b, y_b], color=GRAY_LIGHT, lw=0.25)

    # Final outer rule under the matrix
    ax.add_patch(mpatches.Rectangle((cell_x0, y_bot),
                                    cell_x1 - cell_x0,
                                    y_top - y_bot,
                                    fill=False, ec=RULE, lw=0.4))

    # Cluster brackets in left-edge marginalia (vertical rotated caps)
    for (r0, r1, name) in cluster_brackets:
        # r0/r1 are 0-indexed within the SUBSET, not global function numbers
        y_a = y_top - r0 * row_h
        y_z = y_top - r1 * row_h
        y_mid = (y_a + y_z) / 2
        # Vertical hairline
        bx = x0 - 4.0
        ax.plot([bx, bx], [y_a - 0.1, y_z + 0.1], color=VERDIGRIS, lw=0.45)
        # Short tick caps
        ax.plot([bx - 0.4, bx], [y_a - 0.1, y_a - 0.1], color=VERDIGRIS, lw=0.45)
        ax.plot([bx - 0.4, bx], [y_z + 0.1, y_z + 0.1], color=VERDIGRIS, lw=0.45)
        ax.text(bx - 0.7, y_mid, sp(name, 2),
                ha="center", va="center", rotation=90,
                fontsize=5.0, fontname=F_MONO, color=VERDIGRIS)


# ============================================================
# PLATE II — BY-FUNCTION A · MARKETING + SELLING (F1-6)
# ============================================================
def plate_II_marketing_selling(pdf):
    fig, ax = new_page(11.0, 17.0)
    L, R, TOP, BOT = page_frame(
        ax,
        plate_no="II",
        plate_label="PLATE II OF V",
        title="Functions I-VI · Marketing & Selling",
        subtitle="Per-function horizontal register across the thirteen capabilities — vermilion flags the highest-OCQ cells in each row.",
        latin="Functio per capacitatem · stratum primum sex functionum · ordo emptionis et venditionis",
    )

    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Title strip
    ax.text(inner_x0, TOP - 0.5,
            sp("MARKETING (1-3)  +  SELLING (4-6)  ·  CELLS A - M", 2),
            ha="left", va="top", fontsize=7.5, fontname=F_DISPLAY, color=VERMILION)
    ax.plot([inner_x0, inner_x1], [TOP - 2.2, TOP - 2.2], color=RULE, lw=0.4)

    # Functions 1-6 register
    reg_top = TOP - 7.0
    reg_bot = BOT + 32.0
    subset = FUNCTIONS[:6]
    cluster_brackets = [(0, 3, "MARKETING"), (3, 6, "SELLING")]
    render_function_register(
        ax, x0=inner_x0 + 2.0, x1=inner_x1, y_top=reg_top, y_bot=reg_bot,
        functions_subset=subset, cluster_brackets=cluster_brackets,
        header_text=sp("A=research  B=personalize  C=orchestrate  D=dialog  "
                       "E=meeting  F=CRM-graph  G=multi-step  H=forecast  "
                       "I=negotiate  J=coach  K=comp-use  L=memory  M=observe", 0),
    )

    # ---- Annotation block — the high-OCQ vermilion cells for this plate ---
    ann_top = reg_bot - 2.5
    ax.plot([inner_x0, inner_x1], [ann_top + 0.6, ann_top + 0.6],
            color=RULE, lw=0.4)
    ax.text(inner_x0, ann_top,
            sp("HIGH-OCQ CELLS IN MARKETING + SELLING", 2),
            ha="left", va="top", fontsize=5.6, fontname=F_MONO, color=VERMILION)
    ax.text(inner_x0, ann_top - 1.5,
            "Each cell is one open accruing-equity coordinate — the procurement seam reaches into the AE motion here.",
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_DISP_IT, color=INK_SOFT)

    callouts = [
        ("(4, A)", 16, "Clay · Apollo",
         "SDR research/enrichment — winner-eats-most; Clay $80M ARR Q1'26, $1.5B Jan'26."),
        ("(4, M)", 14, "[gap]",
         "SDR trajectory observability — regulatorily mandatory ≤18 mo (TCPA, CAN-SPAM, GDPR, Art. 14)."),
        ("(4, K)", 15, "Anthropic CU · Mariner",
         "Computer-use in outbound — post-OSWorld-65% (Q3 '26 expected); LinkedIn-TOS as moat-killer."),
        ("(5, F)", 18, "Common Room · Sales Nav",
         "Buying-committee mapping — top single cell, NO INCUMBENT OWNER. JTBD Job 1 gap = 7."),
        ("(6, E)", 17, "Gong · Chorus · Aircover",
         "Deal-diagnosis CAUSATION — Gong sees activity; nobody ships causation @ 73 % confidence."),
        ("(6, L)", 16, "Mem0 · Letta · Zep [IV]",
         "Persistent memory across 6-9 mo deal cycle — dev-side only; AE-shape product unbuilt."),
        ("(6, K)", 14, "Anthropic CU · MS Sales Copilot",
         "Computer-use in AE motion — MS structural advantage; non-MS-shop AE stack open."),
    ]
    ann_row_y = ann_top - 3.0
    row_h = 2.4
    for i, (coord, ocq, vnd, txt) in enumerate(callouts):
        y = ann_row_y - i * row_h
        # vermilion mini-square swatch
        ax.add_patch(mpatches.Rectangle((inner_x0 + 0.3, y - 0.7),
                                        2.2, 1.4,
                                        fc=VERMILION, ec=VERMILION, lw=0.5))
        ax.text(inner_x0 + 1.4, y, f"{ocq}",
                ha="center", va="center",
                fontsize=5.5, fontname=F_MONO_BOLD, color=PAPER)
        # coord
        ax.text(inner_x0 + 3.2, y + 0.4, coord,
                ha="left", va="center",
                fontsize=7.0, fontname=F_DISPLAY, color=INK)
        # vendor mono
        ax.text(inner_x0 + 3.2, y - 0.9, vnd,
                ha="left", va="center",
                fontsize=4.3, fontname=F_DMMONO, color=GRAY)
        # detail serif
        ax.text(inner_x0 + 16.5, y, txt,
                ha="left", va="center",
                fontsize=5.0, fontname=F_SERIF_IT, color=INK_SOFT)
        # tiny rule between rows
        ax.plot([inner_x0, inner_x1], [y - row_h / 2, y - row_h / 2],
                color=GRAY_LIGHT, lw=0.2)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE III — BY-FUNCTION B · OPERATIONS + POST-SALE (F7-12)
# ============================================================
def plate_III_operations_postsale(pdf):
    fig, ax = new_page(11.0, 17.0)
    L, R, TOP, BOT = page_frame(
        ax,
        plate_no="III",
        plate_label="PLATE III OF V",
        title="Functions VII-XII · Operations & Post-Sale",
        subtitle="The procurement seam, the customer-success machine, and the planning loop — where the cell of record (9, G) lives.",
        latin="Functio per capacitatem · stratum secundum sex functionum · operatio et conservatio",
    )

    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    ax.text(inner_x0, TOP - 0.5,
            sp("OPERATIONS (7-9)  ·  POST-SALE (10-11)  ·  PLANNING (12)", 2),
            ha="left", va="top", fontsize=7.5, fontname=F_DISPLAY, color=VERMILION)
    ax.plot([inner_x0, inner_x1], [TOP - 2.2, TOP - 2.2], color=RULE, lw=0.4)

    reg_top = TOP - 7.0
    reg_bot = BOT + 38.0
    subset = FUNCTIONS[6:]
    cluster_brackets = [(0, 3, "OPERATIONS"), (3, 5, "POST-SALE"), (5, 6, "PLANNING")]
    render_function_register(
        ax, x0=inner_x0 + 2.0, x1=inner_x1, y_top=reg_top, y_bot=reg_bot,
        functions_subset=subset, cluster_brackets=cluster_brackets,
        header_text=sp("A=research  B=personalize  C=orchestrate  D=dialog  "
                       "E=meeting  F=CRM-graph  G=multi-step  H=forecast  "
                       "I=negotiate  J=coach  K=comp-use  L=memory  M=observe", 0),
    )

    # ---- Cell of Record highlight box ---------------------------------------
    cor_top = reg_bot - 2.5
    cor_bot = cor_top - 6.0
    ax.add_patch(mpatches.Rectangle((inner_x0, cor_bot),
                                    inner_x1 - inner_x0,
                                    cor_top - cor_bot,
                                    fill=False, ec=VERMILION, lw=0.9))
    ax.add_patch(mpatches.Rectangle((inner_x0 + 0.2, cor_bot + 0.2),
                                    (inner_x1 - inner_x0) - 0.4,
                                    (cor_top - cor_bot) - 0.4,
                                    fc=VERMILION, ec="none", alpha=0.05))
    ax.text(inner_x0 + 1.0, cor_top - 1.0,
            sp("THE CELL OF RECORD  ·  (9, G)  ·  OCQ 19 / 20", 3),
            ha="left", va="top", fontsize=8, fontname=F_DISPLAY, color=VERMILION)
    ax.text(inner_x0 + 1.0, cor_top - 2.6,
            "Agent procurement gauntlet bilateral evidence pack — zero of seven counterparty overlays shipped",
            ha="left", va="top", fontsize=5.4, fontname=F_SERIF_IT, color=INK)
    ax.text(inner_x0 + 1.0, cor_top - 3.6,
            "turnkey as of May 2026. Vanta · Drata · Ironclad on roadmap; Article 14 enforcement late 2026 closes",
            ha="left", va="top", fontsize=5.4, fontname=F_SERIF_IT, color=INK)
    ax.text(inner_x0 + 1.0, cor_top - 4.6,
            "the door for incumbents. The anchor cell of Bet #1. Loopio · Vendr · Tropic the closest hand.",
            ha="left", va="top", fontsize=5.4, fontname=F_SERIF_IT, color=INK)

    # ---- Annotation block --------------------------------------------------
    ann_top = cor_bot - 2.0
    ax.plot([inner_x0, inner_x1], [ann_top + 0.6, ann_top + 0.6],
            color=RULE, lw=0.4)
    ax.text(inner_x0, ann_top,
            sp("THE OTHER HIGH-OCQ CELLS IN OPERATIONS + POST-SALE", 2),
            ha="left", va="top", fontsize=5.6, fontname=F_MONO, color=VERMILION)

    callouts = [
        ("(7, J+M)", 13, "Highspot · Galileo (cross)",
         "Trajectory-grade coaching of procurement-seam work — ramp gap; accident-of-light."),
        ("(8, G)",   15, "Clari · BoostUp · Aviso",
         "RevOps trajectory loop closure — pipeline scrub + forecast prep + territory rebalance."),
        ("(9, G)",   19, "Loopio · Vendr · Ironclad",
         "Procurement gauntlet evidence pack — the through-line · the cell of record · Bet #1 anchor."),
        ("(9, I)",   16, "Ironclad · LinkSquares · Pactum",
         "AI-specific contract addenda — 12-15 clauses; Ironclad Q2 '26 commit · Bet #1 falsifier."),
        ("(9, M)",   14, "Galileo · Arize · Langfuse [VII]",
         "Deal-desk agent-trajectory evidence pack — Part XIII §3 signed eval as product surface."),
        ("(10, D)",  14, "Sierra · Decagon · Intercom Fin",
         "Densest agent-GTM cell by $ — tier-1/2 issue resolution; Klarna reversal reset budgets."),
        ("(11, L)",  14, "Sierra · Mem0 · Letta [IV]",
         "Persistent memory for renewal — 3-stage moat (integrations · deletion · curation)."),
        ("(11, I)",  13, "Sierra · Decagon · Hippocratic",
         "Outcome-based pricing — per-resolution / per-task; SOX rev-rec risk."),
        ("(12, F)",  15, "Clari · BoostUp · Glean",
         "Cross-system narrative retrieval · Gong 'Deal Stories' adoption · ~$300M Gong rev '25."),
        ("(12, H)",  15, "Clari · BoostUp · Aviso",
         "Decision support — $1.5B saturated category; AI augments, doesn't replace."),
    ]
    ann_row_y = ann_top - 1.8
    row_h = 1.85
    for i, (coord, ocq, vnd, txt) in enumerate(callouts):
        y = ann_row_y - i * row_h
        if y < BOT + 6.0:
            break
        ax.add_patch(mpatches.Rectangle((inner_x0 + 0.3, y - 0.6),
                                        2.2, 1.2,
                                        fc=VERMILION, ec=VERMILION, lw=0.5))
        ax.text(inner_x0 + 1.4, y, f"{ocq}",
                ha="center", va="center",
                fontsize=5.0, fontname=F_MONO_BOLD, color=PAPER)
        ax.text(inner_x0 + 3.2, y + 0.35, coord,
                ha="left", va="center",
                fontsize=6.6, fontname=F_DISPLAY, color=INK)
        ax.text(inner_x0 + 3.2, y - 0.75, vnd,
                ha="left", va="center",
                fontsize=4.0, fontname=F_DMMONO, color=GRAY)
        ax.text(inner_x0 + 19.0, y, txt,
                ha="left", va="center",
                fontsize=4.8, fontname=F_SERIF_IT, color=INK_SOFT)
        ax.plot([inner_x0, inner_x1], [y - row_h / 2, y - row_h / 2],
                color=GRAY_LIGHT, lw=0.18)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE IV — THE SEVEN-COUNTERPARTY GAUNTLET (Tabloid LANDSCAPE)
# ============================================================
def plate_IV_gauntlet(pdf):
    # Landscape tabloid: 17 wide × 11 tall, with extended user-units.
    PAGE_W = 17.0
    PAGE_H = 11.0
    XLIM = 170
    YLIM = 110
    fig, ax = new_page(PAGE_W, PAGE_H, xlim=XLIM, ylim=YLIM)

    # Custom landscape frame
    LEFT, RIGHT = 7.5, 162.5
    TOP, BOTTOM = 104.5, 6.0

    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.6))
    ax.plot([LEFT, RIGHT], [TOP - 8.5, TOP - 8.5], color=RULE, lw=0.5)
    ax.plot([LEFT, RIGHT], [BOTTOM + 9.5, BOTTOM + 9.5], color=RULE, lw=0.5)

    # Left depth-scale tick rule
    tickx = LEFT - 2.6
    ax.plot([tickx, tickx], [BOTTOM + 9.5, TOP - 8.5], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 9.5, TOP - 8.5, 22)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([tickx - (1.0 if long else 0.5), tickx], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(tickx - 1.6, y, f"{i*4:02d}", ha="right", va="center",
                    fontsize=4.6, fontname=F_DMMONO, color=GRAY)

    # Title
    ax.text(LEFT, TOP - 1.5,
            sp("AN ATLAS OF THE AGENT STRATA  ·  VOL IV  ·  THE BUYER-SIDE", 3),
            ha="left", va="top", fontsize=6.5, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 3.0,
            "THE SEVEN-COUNTERPARTY GAUNTLET",
            ha="left", va="top", fontsize=24, fontname=F_DISPLAY, color=INK)
    ax.text(LEFT, TOP - 6.7,
            "Seven approver chairs in the F1000 procurement room — each evaluates on a different vector and "
            "rejects for a different reason. An agent vendor that does not pre-answer all seven does not ship.",
            ha="left", va="top", fontsize=7.0, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 8.0,
            "Septem capitula procurationis · ordo causarum · forma negotii agentici · ratio temporis",
            ha="left", va="top", fontsize=5.3, fontname=F_SERIF_IT, color=GRAY)

    # Plate badge
    ax.add_patch(mpatches.Circle((RIGHT - 2.0, TOP - 3.2), 1.4,
                                 fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 2.0, TOP - 3.2, "IV", ha="center", va="center",
            fontsize=10, fontname=F_MONO_BOLD, color=VERMILION)
    ax.text(RIGHT - 4.5, TOP - 6.0, sp("PLATE IV OF V", 2),
            ha="right", va="top", fontsize=6.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(RIGHT - 4.5, TOP - 7.6, sp("VOL IV  ·  MMXXVI  ·  MAY", 2),
            ha="right", va="top", fontsize=5.0, fontname=F_DMMONO, color=GRAY)

    # Footer
    ax.text(LEFT, BOTTOM + 4.5,
            sp("SUBSTRATE  ·  VOL IV  ·  AGENTS GTM  ·  PLATE IV OF V", 3),
            ha="left", va="top", fontsize=4.8, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 2.6,
            sp("Compiled for A. Yedi  ·  Cycle MMXXVI  ·  Rev. I", 2),
            ha="left", va="top", fontsize=5.3, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 2.6, sp("MMXXVI · V", 2),
            ha="right", va="top", fontsize=5.4, fontname=F_DMMONO, color=GRAY)

    # ---- The seven counterparties --------------------------------------------
    # NOTE: counterparty questions are kept short (3 pairs of lines per chair)
    # so the column band fits and leaves room for the calendar + sectoral
    # registers beneath.
    counterparties = [
        ("01", "INFOSEC", "CISO · GRC", VERMILION,
         "10-20 wks",
         [
             "Walk me through your tool-boundary policy. What can your",
             "agent call, on whose authority, enforced at runtime.",
             "Show me your indirect-prompt-injection defense —",
             "adaptive-adversary red-team report, not a benchmark.",
             "If your foundation-model provider issues an update tomorrow,",
             "what happens to our deployment and our right to pin.",
         ]),
        ("02", "LEGAL", "GC · AI Counsel", VERMILION,
         "8-16 wks",
         [
             "Walk me through your indemnity stack. Cap on IP infringement,",
             "hallucination, agent action, and the insurance tower.",
             "Show me the AI Addendum. Training-data carve-out, model-",
             "update notice, output ownership, kill-switch, termination.",
             "Who is your foundation-model sub-processor, and contingency",
             "if their terms change against you mid-contract.",
         ]),
        ("03", "PRIVACY", "CPO · DPO", VERMILION,
         "6-12 wks",
         [
             "Show me your data-flow diagram. Where does the prompt go,",
             "the output go, the memory persist, what borders does it cross.",
             "If a data subject asks us to delete their data, what is the",
             "surgical-deletion mechanism and your SLA.",
             "For automated decisions about EU subjects, show me the",
             "human-in-the-loop and Article 22 conformance.",
         ]),
        ("04", "AI GOVERNANCE", "AI Council · CAO", VERMILION,
         "8-16 wks",
         [
             "Show me your evaluation report — signed, reproducible, with",
             "model pin, dataset hash, harness version, methodology.",
             "Map your controls to NIST AI RMF GenAI Profile and ISO 42001.",
             "If you have an EU AI Act conformity assessment, show it.",
             "Show me the human-oversight design for our use-case.",
             "Article 14 in practice. Not the marketing version.",
         ]),
        ("05", "PROCUREMENT", "CPO · AI Cat Mgr", VERMILION,
         "10-24 wks",
         [
             "Model your pricing three years out at our projected usage,",
             "stress-tested for 20 % model price increase and 3x usage spike.",
             "Three at-scale references in our industry. I will call them.",
             "I will ask what they would change about the contract.",
             "What does my exit look like on day 1, 30, 90, 365?",
             "Where is my data, my agent state, what is migration cost.",
         ]),
        ("06", "SPONSOR", "CRO · CMO · VP CS", VERMILION,
         "2-6 wks",
         [
             "What did the last three customers at my scale do in their",
             "first 90 days, measurable outcome at day 90.",
             "My line manager runs this day-to-day. Show me their week.",
             "When the model drifts or the agent acts wrong, who calls",
             "me, when, what is the playbook.",
         ]),
        ("07", "ENTERPRISE ARCH", "CIO · Chief Arch", VERMILION,
         "6-12 wks",
         [
             "Reference-architecture fit. Identity, observability, secrets,",
             "deployment, multi-region. Tell me where you don't fit.",
             "Sub-agent fan-out behavior under failure. Circuit breaker,",
             "cost ceiling per trajectory, what does my SIEM see.",
             "Per-trajectory cost telemetry. Show me the data model",
             "and the export. EA cannot govern what it cannot see.",
         ]),
    ]
    n = len(counterparties)

    # The horizontal flow band (must fit above the calendar + sectoral blocks)
    band_top = TOP - 11.0
    band_bot = band_top - 42.0
    avail_w = RIGHT - LEFT - 4.0
    col_w = avail_w / n
    col_h = band_top - band_bot

    # Background hairline guide across the band
    ax.plot([LEFT + 2.0, RIGHT - 2.0], [band_top - 2.5, band_top - 2.5],
            color=RULE, lw=0.4)

    # Section header
    ax.text(LEFT + 2.0, band_top - 0.6,
            sp("FLOW  ·  LEFT TO RIGHT  ·  EACH CHAIR REJECTS ON ITS OWN VECTOR", 2),
            ha="left", va="top", fontsize=5.4, fontname=F_MONO, color=VERMILION)

    for i, (num, name, who, color, cycle, qs) in enumerate(counterparties):
        x0 = LEFT + 2.0 + i * col_w
        x1 = x0 + col_w
        cx = (x0 + x1) / 2

        # Number badge
        ax.add_patch(mpatches.Circle((cx, band_top - 5.0), 2.2,
                                     fc=PAPER, ec=color, lw=0.8))
        ax.text(cx, band_top - 5.0, num, ha="center", va="center",
                fontsize=8, fontname=F_DMMONO, color=color)

        # Name caps
        ax.text(cx, band_top - 9.4, name, ha="center", va="center",
                fontsize=9, fontname=F_DISPLAY, color=INK)
        # Who italic
        ax.text(cx, band_top - 11.5, who, ha="center", va="center",
                fontsize=5.2, fontname=F_SERIF_IT, color=GRAY)

        # cycle window — pale rule above the questions
        ax.plot([x0 + 1.5, x1 - 1.5], [band_top - 13.0, band_top - 13.0],
                color=GRAY_LIGHT, lw=0.4)
        ax.text(cx, band_top - 13.9, cycle, ha="center", va="center",
                fontsize=5.3, fontname=F_DMMONO, color=VERDIGRIS)

        # questions
        ax.plot([x0 + 1.5, x1 - 1.5], [band_top - 15.5, band_top - 15.5],
                color=RULE, lw=0.35)
        ax.text(cx, band_top - 16.3, sp("2026 QUESTIONS · VERBATIM", 1),
                ha="center", va="center",
                fontsize=3.8, fontname=F_MONO, color=VERMILION)

        # The three questions as line-wrapped serif italic
        y_q = band_top - 18.0
        # Each question is two display lines; insert separator after every 2
        for j, line in enumerate(qs):
            # add a small bullet (drawn as a rectangle) on the first line of each pair
            if j % 2 == 0:
                ax.add_patch(mpatches.Rectangle((x0 + 1.6, y_q - 0.3),
                                                0.5, 0.5,
                                                fc=VERMILION, ec=VERMILION,
                                                lw=0))
            tx_left = x0 + 2.6
            ax.text(tx_left, y_q, line,
                    ha="left", va="center",
                    fontsize=4.3, fontname=F_SERIF_IT, color=INK)
            y_q -= 1.45
            # Spacer line between questions
            if j % 2 == 1:
                y_q -= 0.4

        # Vertical guide between columns
        if i < n - 1:
            ax.plot([x1, x1], [band_top - 4.0, band_bot + 1.0],
                    color=GRAY_LIGHT, lw=0.25, ls=(0, (0.6, 0.9)))

        # Arrow at top connecting columns
        if i < n - 1:
            ax.annotate("",
                        xy=(x1 + 0.7, band_top - 5.0),
                        xytext=(x1 - 0.7, band_top - 5.0),
                        arrowprops=dict(arrowstyle="-|>",
                                        color=VERMILION, lw=0.5,
                                        shrinkA=2, shrinkB=2))

    # ---- Calendar-time axis below the column band -----------------------------
    cal_top = band_bot - 2.0
    cal_bot = cal_top - 14.0  # taller so timeline + ticks + labels all fit
    ax.plot([LEFT + 2.0, RIGHT - 2.0], [cal_top + 0.5, cal_top + 0.5],
            color=RULE, lw=0.4)
    ax.text(LEFT + 2.0, cal_top - 0.3,
            sp("CALENDAR-TIME FLOOR  ·  F1000 PROCUREMENT GAUNTLET", 3),
            ha="left", va="top", fontsize=5.6, fontname=F_MONO, color=VERMILION)
    ax.text(LEFT + 2.0, cal_top - 1.7,
            "Three regimes — the prepared vendor; the unprepared vendor; the regulated vendor. The schedule is unforgiving and the seller controls almost none of it.",
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=INK_SOFT)

    # Three timeline bars stacked
    bar_x0 = LEFT + 28.0
    bar_x1 = RIGHT - 12.0
    bar_y_top = cal_top - 5.5
    bar_h = 1.4
    bar_gap = 1.7

    def render_bar(y, color, label, weeks_label, x_frac, style="solid"):
        x_end = bar_x0 + (bar_x1 - bar_x0) * x_frac
        if style == "solid":
            ax.plot([bar_x0, x_end], [y, y], color=color, lw=2.5,
                    solid_capstyle="butt")
        else:
            ax.plot([bar_x0, x_end], [y, y], color=color, lw=1.2,
                    ls=(0, (1.4, 1.0)))
        # End cap
        ax.plot([x_end, x_end], [y - 0.5, y + 0.5], color=color, lw=0.7)
        # label left
        ax.text(bar_x0 - 1.0, y, label, ha="right", va="center",
                fontsize=5.3, fontname=F_DISPLAY, color=INK)
        # weeks right
        ax.text(x_end + 1.0, y, weeks_label, ha="left", va="center",
                fontsize=4.6, fontname=F_DMMONO, color=color)

    # Scale on top: 4-week ticks 0..104 weeks
    scale_y = bar_y_top + 0.9
    ax.plot([bar_x0, bar_x1], [scale_y, scale_y], color=RULE, lw=0.3)
    for w in range(0, 105, 4):
        x = bar_x0 + (bar_x1 - bar_x0) * (w / 104.0)
        long_tk = (w % 12 == 0)
        ax.plot([x, x], [scale_y, scale_y + (0.5 if long_tk else 0.3)],
                color=RULE, lw=0.3)
        if long_tk:
            ax.text(x, scale_y + 1.0, f"{w}", ha="center", va="bottom",
                    fontsize=3.8, fontname=F_DMMONO, color=GRAY)
    ax.text(bar_x1 + 1.0, scale_y + 1.0, "wks",
            ha="left", va="bottom",
            fontsize=3.8, fontname=F_DMMONO, color=GRAY)

    render_bar(bar_y_top - 0.5, VERMILION,
               "VENDOR PREPARED",  "16 — 24 wks", 24 / 104.0, "solid")
    render_bar(bar_y_top - 0.5 - bar_h - bar_gap, GRAY,
               "VENDOR NOT PREPARED",  "32 — 52 wks", 52 / 104.0, "solid")
    render_bar(bar_y_top - 0.5 - 2 * (bar_h + bar_gap), VERDIGRIS,
               "REGULATED SECTORS",  "52 — 104 wks", 104 / 104.0, "dashed")

    # ---- Sectoral overlay sub-register ------------------------------------
    sec_top = cal_bot - 2.0
    sec_bot = BOTTOM + 11.5
    ax.plot([LEFT + 2.0, RIGHT - 2.0], [sec_top + 0.5, sec_top + 0.5],
            color=RULE, lw=0.4)
    ax.text(LEFT + 2.0, sec_top - 0.3,
            sp("SECTORAL OVERLAYS  ·  ADDITIONAL COUNTERPARTIES + CYCLE TIME", 3),
            ha="left", va="top", fontsize=5.6, fontname=F_MONO, color=VERMILION)

    sectors = [
        ("FSI",     "SR 11-7 · NYDFS 500 · FINRA 4511 · DORA",
         "Model-risk function as 8th counterparty",
         "+ 8 — 16 wks", VERMILION),
        ("HEALTHCARE", "HIPAA · HITECH · ONC HTI-2 · FDA SaMD",
         "BAA at signature; clinical SaMD if decision support",
         "+ 6 — 14 wks", VERDIGRIS),
        ("DEFENSE / GOV", "FedRAMP Mod/High · DoD IL4/5/6 · CMMC · ITAR",
         "Sponsor-agency ATO; FedRAMP alone 12-18 mo",
         "6 — 18 mo total", OCHRE),
    ]
    sec_y = sec_top - 2.6
    sec_gap = (RIGHT - 2.0 - (LEFT + 2.0)) / 3
    for i, (nm, regs, role, delta, color) in enumerate(sectors):
        x = LEFT + 2.0 + i * sec_gap + 0.4
        ax.text(x, sec_y, nm, ha="left", va="top",
                fontsize=8.0, fontname=F_DISPLAY, color=color)
        ax.text(x, sec_y - 1.6, regs, ha="left", va="top",
                fontsize=4.6, fontname=F_DMMONO, color=GRAY)
        ax.text(x, sec_y - 2.8, role, ha="left", va="top",
                fontsize=4.8, fontname=F_SERIF_IT, color=INK)
        ax.text(x, sec_y - 4.0, delta, ha="left", va="top",
                fontsize=5.2, fontname=F_MONO_BOLD, color=color)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE V — TALENT FLOW · NYC PEAK Q2 2026 (Tabloid LANDSCAPE)
# ============================================================
def plate_V_talent_flow(pdf):
    PAGE_W = 17.0
    PAGE_H = 11.0
    XLIM = 170
    YLIM = 110
    fig, ax = new_page(PAGE_W, PAGE_H, xlim=XLIM, ylim=YLIM)

    LEFT, RIGHT = 7.5, 162.5
    TOP, BOTTOM = 104.5, 6.0

    # Frame chrome
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.6))
    ax.plot([LEFT, RIGHT], [TOP - 8.5, TOP - 8.5], color=RULE, lw=0.5)
    ax.plot([LEFT, RIGHT], [BOTTOM + 9.5, BOTTOM + 9.5], color=RULE, lw=0.5)

    tickx = LEFT - 2.6
    ax.plot([tickx, tickx], [BOTTOM + 9.5, TOP - 8.5], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 9.5, TOP - 8.5, 22)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([tickx - (1.0 if long else 0.5), tickx], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(tickx - 1.6, y, f"{i*4:02d}", ha="right", va="center",
                    fontsize=4.6, fontname=F_DMMONO, color=GRAY)

    # Title
    ax.text(LEFT, TOP - 1.5,
            sp("AN ATLAS OF THE AGENT STRATA  ·  VOL IV  ·  TALENT MIGRATION", 3),
            ha="left", va="top", fontsize=6.5, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 3.0,
            "TALENT FLOW  ·  Q2 2026  ·  NYC PEAK",
            ha="left", va="top", fontsize=24, fontname=F_DISPLAY, color=INK)
    ax.text(LEFT, TOP - 6.7,
            "Four feed-stocks empty into the ten NYC-anchored vertical-agent destinations. The Stripe / Datadog / "
            "Snowflake pattern that built SaaS now redirects to the agent layer.",
            ha="left", va="top", fontsize=7.0, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 8.0,
            "Quattuor venae operariorum · decem destinationes · pretium liminale · forma fenestrae sex menses",
            ha="left", va="top", fontsize=5.3, fontname=F_SERIF_IT, color=GRAY)

    # Plate badge
    ax.add_patch(mpatches.Circle((RIGHT - 2.0, TOP - 3.2), 1.4,
                                 fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 2.0, TOP - 3.2, "V", ha="center", va="center",
            fontsize=10, fontname=F_MONO_BOLD, color=VERMILION)
    ax.text(RIGHT - 4.5, TOP - 6.0, sp("PLATE V OF V", 2),
            ha="right", va="top", fontsize=6.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(RIGHT - 4.5, TOP - 7.6, sp("VOL IV  ·  MMXXVI  ·  MAY", 2),
            ha="right", va="top", fontsize=5.0, fontname=F_DMMONO, color=GRAY)

    # Footer
    ax.text(LEFT, BOTTOM + 4.5,
            sp("SUBSTRATE  ·  VOL IV  ·  AGENTS GTM  ·  PLATE V OF V", 3),
            ha="left", va="top", fontsize=4.8, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 2.6,
            sp("Compiled for A. Yedi  ·  Cycle MMXXVI  ·  Rev. I", 2),
            ha="left", va="top", fontsize=5.3, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 2.6, sp("MMXXVI · V", 2),
            ha="right", va="top", fontsize=5.4, fontname=F_DMMONO, color=GRAY)

    # ---- The flow diagram ------------------------------------------------
    flow_top = TOP - 11.0
    flow_bot = flow_top - 60.0   # tall flow band

    # Left feed-stocks
    feeds = [
        ("01", "STRIPE · RAMP · DATADOG · SNOWFLAKE",
         "Enterprise B2B AE / Field SE / Industry Lead",
         "10+ examples Stripe>Sierra · Mike Yu Snowflake>Glean · Sinha Datadog>Decagon"),
        ("02", "MBB CONSULTING",
         "BCG · McKinsey QuantumBlack · Bain AI Practice",
         "Berger BCG>Hebbia Feb '26 · Park McKinsey>Sierra Mar · Sinclair Bain>Harvey Apr"),
        ("03", "FOUNDATION-LAB AE",
         "OpenAI NYC · Anthropic NYC enterprise",
         "Early Q2 '26 LI clusters · emerging fourth feed-stock · 2-3 confirmed moves"),
        ("04", "ENTERPRISE B2B (Alex)",
         "GKY · Bazaarvoice · Curalate-class operators",
         "12-yr procurement scar-tissue · MBB beat on execution depth · NYC profile match"),
    ]

    # Right destinations
    dests = [
        ("01", "HEBBIA",      "$50M+ ARR · ratio 2.5-5% · 0.20-0.40% equity",
         "MBB+Stripe anchor · Mehta Mar '26 · 2-quarter window before Series C", True),
        ("02", "SIERRA",      "$175M+ ARR · 15+ senior moves 12mo · 0.10-0.25%",
         "Schmidt anchor · Taylor monthly NYC · cleanest secondary-liquidity path", False),
        ("03", "ROGO",        "$30M+ ARR · ratio 7.5% · 0.30-0.60% equity",
         "Tekriwal Goldman>Rogo Jan '26 · banker-fluent · highest equity asymmetry", False),
        ("04", "HARVEY",      "$100M+ ARR · NYC tripling Q3 '26 · 0.05-0.15%",
         "10+ moves 12mo · BigLaw + Bain feed · Series E priced at $5B", False),
        ("05", "CLAY",        "$80M+ ARR · 40 GTM hires H1 '26 · 0.15-0.30%",
         "Amin's largest single push · best NYC-culture-fit signal", False),
        ("06", "DECAGON",     "$80M+ ARR · 8+ moves · 0.10-0.20% equity",
         "Sinha (Datadog) Field CTO · NYC office expanded Q1 '26", False),
        ("07", "HIPPOCRATIC", "$50M+ ARR · 0.10-0.25% · Munjal Shah NYC",
         "Healthcare wedge · voice agent novelty · outcome pricing", False),
        ("08", "GLEAN",       "$300M+ ARR · 8+ moves · 0.05-0.15% (priced high)",
         "Yehoshua CPO Oct '25 · Snowflake-cluster destination · E-stage", False),
        ("09", "RUNWAY",      "$100M+ ARR · Chelsea HQ · 0.10-0.20%",
         "Adobe/Frame.io cluster Mar '26 · NYC creative wedge", False),
        ("10", "RAMP AI ORG", "$700M+ co · NYC native · 0.01-0.05%",
         "Internal AI org expansion post-Q2 '26 raise · lowest asymmetry safer pick", False),
    ]

    # Layout: feed-stocks on left, destinations on right, sankey-style bands
    feed_x_l = LEFT + 4.0
    feed_x_r = LEFT + 38.0
    dest_x_l = LEFT + 90.0
    dest_x_r = LEFT + 140.0

    # Header bars
    ax.text(feed_x_l, flow_top + 2.0,
            sp("FOUR FEED-STOCKS", 3),
            ha="left", va="top", fontsize=6.6, fontname=F_DISPLAY, color=VERMILION)
    ax.plot([feed_x_l, feed_x_r], [flow_top + 0.5, flow_top + 0.5],
            color=RULE, lw=0.4)
    ax.text(dest_x_l, flow_top + 2.0,
            sp("TEN NYC VERTICAL-AGENT DESTINATIONS", 3),
            ha="left", va="top", fontsize=6.6, fontname=F_DISPLAY, color=VERMILION)
    ax.plot([dest_x_l, dest_x_r], [flow_top + 0.5, flow_top + 0.5],
            color=RULE, lw=0.4)

    # Feed-stock blocks
    nf = len(feeds)
    nd = len(dests)
    feed_h = (flow_top - flow_bot) / nf - 1.0
    dest_h = (flow_top - flow_bot) / nd - 0.4

    feed_centers = []
    for i, (num, title, role, examples) in enumerate(feeds):
        y_top = flow_top - 1.5 - i * (feed_h + 1.0)
        y_bot = y_top - feed_h
        y_mid = (y_top + y_bot) / 2
        feed_centers.append((feed_x_r, y_mid))

        # Block outline
        ax.add_patch(mpatches.Rectangle((feed_x_l, y_bot),
                                        feed_x_r - feed_x_l,
                                        y_top - y_bot,
                                        fill=False, ec=INK_SOFT, lw=0.5))
        # Number badge
        ax.add_patch(mpatches.Circle((feed_x_l + 1.6, y_top - 1.4), 1.0,
                                     fc=PAPER, ec=VERMILION, lw=0.5))
        ax.text(feed_x_l + 1.6, y_top - 1.4, num,
                ha="center", va="center",
                fontsize=4.8, fontname=F_DMMONO, color=VERMILION)
        # Title display
        ax.text(feed_x_l + 3.5, y_top - 1.2, title,
                ha="left", va="top", fontsize=7.6,
                fontname=F_DISPLAY, color=INK)
        # Role italic
        ax.text(feed_x_l + 0.7, y_mid + 0.4, role,
                ha="left", va="center", fontsize=4.8,
                fontname=F_SERIF_IT, color=INK_SOFT)
        # Examples mono
        ax.text(feed_x_l + 0.7, y_bot + 1.4, examples,
                ha="left", va="center", fontsize=3.9,
                fontname=F_DMMONO, color=GRAY)

    dest_centers = []
    for i, (rank, name, terms, why, is_vermilion) in enumerate(dests):
        y_top = flow_top - 1.0 - i * (dest_h + 0.4)
        y_bot = y_top - dest_h
        y_mid = (y_top + y_bot) / 2
        dest_centers.append((dest_x_l, y_mid))

        # Subtle frame
        ec_color = VERMILION if is_vermilion else GRAY_LIGHT
        lw = 0.7 if is_vermilion else 0.3
        ax.add_patch(mpatches.Rectangle((dest_x_l, y_bot),
                                        dest_x_r - dest_x_l,
                                        y_top - y_bot,
                                        fill=False, ec=ec_color, lw=lw))
        # Rank badge
        ax.add_patch(mpatches.Circle((dest_x_l + 1.4, y_mid),
                                     1.0,
                                     fc=VERMILION if is_vermilion else PAPER,
                                     ec=VERMILION, lw=0.5))
        ax.text(dest_x_l + 1.4, y_mid, rank,
                ha="center", va="center",
                fontsize=4.8, fontname=F_DMMONO,
                color=PAPER if is_vermilion else VERMILION)
        # Name display caps
        name_color = VERMILION if is_vermilion else INK
        ax.text(dest_x_l + 3.5, y_mid + 1.0, name,
                ha="left", va="center", fontsize=8.5,
                fontname=F_DISPLAY, color=name_color)
        # Terms mono
        ax.text(dest_x_l + 3.5, y_mid - 0.4, terms,
                ha="left", va="center", fontsize=4.0,
                fontname=F_DMMONO, color=GRAY)
        # Why italic
        ax.text(dest_x_l + 3.5, y_mid - 1.6, why,
                ha="left", va="center", fontsize=4.2,
                fontname=F_SERIF_IT, color=INK_SOFT)

    # ---- The flow arcs between feeds and destinations -------------------------
    # Heuristic mapping: each feed connects to a subset of destinations
    flow_map = {
        0: [0, 1, 2, 3, 5, 6, 7, 8, 9],   # Stripe/Ramp/DD/SF goes broad
        1: [0, 1, 3, 4],                  # MBB into Hebbia/Sierra/Harvey/Clay
        2: [0, 1, 5],                     # Foundation-lab AE → Hebbia/Sierra/Decagon
        3: [0, 1, 4, 8],                  # Enterprise B2B (Alex) → Hebbia/Sierra/Clay/Runway
    }

    # Use Bezier-like curves via matplotlib Path
    from matplotlib.path import Path as MPath
    for f_idx, dests_list in flow_map.items():
        x0, y0 = feed_centers[f_idx]
        for d_idx in dests_list:
            x1, y1 = dest_centers[d_idx]
            # Curve through control points
            ctrl1_x = x0 + (x1 - x0) * 0.45
            ctrl2_x = x0 + (x1 - x0) * 0.55
            verts = [(x0, y0), (ctrl1_x, y0), (ctrl2_x, y1), (x1, y1)]
            codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4]
            path = MPath(verts, codes)
            patch = mpatches.PathPatch(path, fc="none",
                                       ec=VERMILION if d_idx == 0 else INK_SOFT,
                                       lw=0.5 if d_idx == 0 else 0.3,
                                       alpha=0.85 if d_idx == 0 else 0.55)
            ax.add_patch(patch)

    # ---- Named-moves register at bottom + equity-window note --------------
    moves_top = flow_bot - 1.5
    moves_bot = BOTTOM + 11.5
    ax.plot([LEFT + 2.0, RIGHT - 2.0], [moves_top, moves_top],
            color=RULE, lw=0.4)
    ax.text(LEFT + 2.0, moves_top - 0.7,
            sp("NAMED MOVES Q1-Q2 2026  ·  THE PATTERN MADE LITERAL", 3),
            ha="left", va="top",
            fontsize=5.6, fontname=F_MONO, color=VERMILION)
    ax.text(LEFT + 2.0, moves_top - 2.0,
            "Three confirmed activations of the MBB > vertical-agent feed-stock; one Goldman MBD anchor at Rogo. Listed verbatim from F4 hire register.",
            ha="left", va="top",
            fontsize=4.8, fontname=F_SERIF_IT, color=INK_SOFT)

    moves = [
        ("FEB 2026", "MATEO BERGER",   "BCG NYC Principal",      ">  HEBBIA",  "Head of GTM Strategy"),
        ("MAR 2026", "DIVYA MEHTA",    "Stripe Enterprise",      ">  HEBBIA",  "VP Revenue (NYC)"),
        ("MAR 2026", "SARAH PARK",     "McKinsey QuantumBlack",  ">  SIERRA",  "Head of Industry (FinServ)"),
        ("MAR 2026", "VIVEK RAGHUNATHAN","Meta AI Infra",         ">  SIERRA",  "Head of Platform Eng"),
        ("APR 2026", "ANDREW SINCLAIR","Bain Boston AI",         ">  HARVEY",  "Director GTM Strategy"),
        ("JAN 2026", "YASH TEKRIWAL",  "Goldman MBD VP",         ">  ROGO",    "Head of Enterprise Sales"),
    ]
    move_y = moves_top - 3.5
    move_row_h = 1.4
    for i, (date, person, fr, to, role) in enumerate(moves):
        y = move_y - i * move_row_h
        ax.text(LEFT + 3.0, y, date, ha="left", va="center",
                fontsize=4.4, fontname=F_DMMONO, color=VERMILION)
        ax.text(LEFT + 17.0, y, person, ha="left", va="center",
                fontsize=5.5, fontname=F_DISPLAY, color=INK)
        ax.text(LEFT + 50.0, y, fr, ha="left", va="center",
                fontsize=4.6, fontname=F_SERIF_IT, color=GRAY)
        ax.text(LEFT + 90.0, y, to, ha="left", va="center",
                fontsize=5.6, fontname=F_DISPLAY, color=VERMILION)
        ax.text(LEFT + 116.0, y, role, ha="left", va="center",
                fontsize=4.8, fontname=F_SERIF_IT, color=INK_SOFT)
        ax.plot([LEFT + 2.5, RIGHT - 2.5],
                [y - move_row_h / 2, y - move_row_h / 2],
                color=GRAY_LIGHT, lw=0.18)

    # ---- Equity-band window sub-register ---------------------------------
    eq_top = move_y - len(moves) * move_row_h - 1.5
    ax.plot([LEFT + 2.0, RIGHT - 2.0], [eq_top + 0.3, eq_top + 0.3],
            color=RULE, lw=0.35)
    ax.text(LEFT + 2.0, eq_top - 0.6,
            sp("THE 6 — 9 MONTH EQUITY WINDOW", 3),
            ha="left", va="top",
            fontsize=5.0, fontname=F_MONO, color=VERMILION)
    ax.text(LEFT + 2.0, eq_top - 2.0,
            "Hebbia · Rogo · Harvey · Augment most likely to reprice upward in this window. Sign BEFORE — not after — Anthropic ARR Q3 2026 resolution. "
            "If $24B lower-bound resolves, vertical-agent vals compress 20-30 % and equity bands strengthen for Alex. If $30B upper resolves, comp bands hold "
            "but equity tightens further. The load-bearing valuation variable for the next four quarters is named.",
            ha="left", va="top",
            fontsize=4.6, fontname=F_SERIF_IT, color=INK)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# BUILD
# ============================================================
if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        plate_I_cell_index(pdf)
        plate_II_marketing_selling(pdf)
        plate_III_operations_postsale(pdf)
        plate_IV_gauntlet(pdf)
        plate_V_talent_flow(pdf)

    sz_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"Wrote {OUT_PATH}  ·  {sz_kb:.1f} KB")
