"""
SUBSTRATE  ·  Vol IV  ·  Plate I of I  —  Agents GTM Cell Matrix.
A single large plate: 12 GTM functions x 13 agent capabilities.
Cell intensity = OCQ score.  Vermilion accent = Top-15.

Inherits the SUBSTRATE design language from Volumes I-III:
ink-on-cream palette, hairline rules, condensed display caps,
whisper-thin marginalia, vermilion as the single oxidized accent.

Output: AGENTS_GTM_MATRIX.pdf (Tabloid 11x17, single page).
"""
# plate-fonts-scaled-v1
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
import numpy as np

# -- Font loading (canvas-design fonts) ------------------------------------
FONT_DIR = "/Users/sameoldexpressions/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/f85326cc-c479-4349-956a-d3d47e404d0b/d1370235-0ed8-47e6-859d-0bec833074a3/skills/canvas-design/canvas-fonts"
if os.path.isdir(FONT_DIR):
    for fp in os.listdir(FONT_DIR):
        if fp.endswith((".ttf", ".otf")):
            fm.fontManager.addfont(os.path.join(FONT_DIR, fp))


def fam(filename):
    path = os.path.join(FONT_DIR, filename)
    if os.path.isfile(path):
        return fm.FontProperties(fname=path).get_name()
    # Fallback: DejaVu Sans is universally available with matplotlib.
    return "DejaVu Sans"


F_DISPLAY      = fam("BigShoulders-Bold.ttf")       # condensed display caps
F_DISPLAY_REG  = fam("BigShoulders-Regular.ttf")
F_SERIF        = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT     = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP   = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT= fam("InstrumentSerif-Italic.ttf")
F_MONO         = fam("GeistMono-Regular.ttf")
F_MONO_BOLD    = fam("GeistMono-Bold.ttf")
F_DMMONO       = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"]  = 42

# -- Chromatic palette (identical to Volumes I-III) ------------------------
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

# Tabloid landscape — wide plate. The 12 functions fit comfortably as rows;
# the 13 capability columns fit horizontally.
PAGE_W, PAGE_H = 23.8, 15.4
DPI = 300
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm/AGENTS_GTM_MATRIX.pdf"


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


# -- Capability columns (13) ----------------------------------------------
# (letter, short caps title, longer descriptor for footer key)
CAPABILITIES = [
    ("A", "RESEARCH",      "Research / enrichment"),
    ("B", "PERSONAL.",     "Personalization + content"),
    ("C", "ORCHESTR.",     "Multi-channel orchestration"),
    ("D", "DIALOG.",       "Conversation handling"),
    ("E", "MEETING",       "Meeting prep / listen / follow-up"),
    ("F", "CRM-GRAPH",     "CRM hygiene / graph"),
    ("G", "MULTI-STEP",    "Multi-step task execution"),
    ("H", "FORECAST",      "Forecasting / decision support"),
    ("I", "NEGOTIATE",     "Negotiation / pricing"),
    ("J", "COACH",         "Coaching / performance"),
    ("K", "COMP-USE",      "Computer-use (OSWorld-gated)"),
    ("L", "MEMORY",        "Persistent memory"),
    ("M", "OBSERVE",       "Trajectory observability"),
]

# -- Function rows (12) ---------------------------------------------------
FUNCTIONS = [
    ("1",  "DEMAND-GEN",   "Demand-gen / brand"),
    ("2",  "CONTENT",      "Content / SEO"),
    ("3",  "INBOUND-PLG",  "Inbound / PLG"),
    ("4",  "OUTBOUND",     "Outbound SDR"),
    ("5",  "ABM",          "Account-based marketing"),
    ("6",  "NEW-BIZ AE",   "New-biz AE"),
    ("7",  "ENABLE",       "Enablement / training"),
    ("8",  "REV-OPS",      "RevOps / Sales Ops"),
    ("9",  "DEAL-DESK",    "Deal desk / pricing / procurement"),
    ("10", "CS",           "CS / onboarding"),
    ("11", "AM-RENEW",     "AM / renewals / expansion"),
    ("12", "FORECAST",     "Forecasting / strategy"),
]

# -- Cell map -------------------------------------------------------------
# Row = function (1..12).  Col = capability letter (A..M).
# Each cell is (status, ocq_or_None, vendor_abbrev_or_None, stratum_or_None).
# status: M=mature, F=forming, U=under-served gap, V=vapor, N=N/A, E=empty
#   B = breakout (Top-15 vermilion)
# ocq: None if not scored in synthesis
# vendor: 1-2 short abbreviation glyphs
# stratum: capital letter or roman key (II,IV,VII,VIII,IX,X) — sub-stratum tag

# Top-15 cells (vermilion):
# 1.(9,G) 19  2.(5,F) 18  3.(6,E) 17  4.(4,A) 16  5.(6,L) 16
# 6.(9,I) 16  7.(8,G) 15  8.(4,K) 15  9.(12,F) 15 10.(12,H) 15
# 11.(4,M) 14 12.(9,M) 14 13.(11,L) 14 14.(3,A+L+F) 14  15.(6,K) 14
TOP15 = {
    (9, "G"), (5, "F"), (6, "E"), (4, "A"), (6, "L"),
    (9, "I"), (8, "G"), (4, "K"), (12, "F"), (12, "H"),
    (4, "M"), (9, "M"), (11, "L"), (3, "A"), (6, "K"),
}

# Cells data, full map from synthesis Section 1.
# Tuple: (function, capability, ocq, vendor_abbr, stratum, status)
# stratum:  IX/II/IV/VII/VIII/X for sub-stratum tag
CELLS = [
    # Function 1 — Demand-gen / brand
    (1, "A", 11, "6sn Dmb",  "IX",   "M"),
    (1, "B", None, "Mut Jsp", "IX",  "M"),
    (1, "C", None, "Optm Mkt","IX",  "F"),
    (1, "D", None, "Drft Itr","IX",  "M"),
    (1, "F", None, "6sn Dmb", "IX",  "F"),
    (1, "G", None, "Jsp Sf",  "IX",  "F"),
    (1, "H", None, "6sn SF",  "IX",  "F"),
    (1, "K", 13,  "Adb Cnv",  "IX",  "U"),
    (1, "L", None, "6sn",     "IX",  "F"),
    (1, "M", 14,  "[gap]",    "VII", "U"),
    # Function 2 — Content / SEO
    (2, "A", None, "Srf Clr", "IX",  "M"),
    (2, "B", None, "Jsp Wrt", "IX",  "M"),
    (2, "G", 9,   "Jsp Cpy",  "IX",  "F"),
    (2, "K", 13,  "Rnw Adb",  "IX",  "U"),
    (2, "L", None, "Wrtr",    "IX",  "F"),
    (2, "M", 12,  "[gap]",    "VII", "U"),
    (2, "H", None, "Clr Mrk", "IX",  "M"),
    # Function 3 — Inbound / PLG
    (3, "A", 14,  "ComR Pcs", "IX",  "F"),  # (3, A+L+F)
    (3, "D", None, "Itc Drf", "IX",  "M"),
    (3, "F", None, "ComR",    "IX",  "F"),
    (3, "G", None, "ComR Def","IX",  "F"),
    (3, "H", None, "Pcs",     "IX",  "F"),
    (3, "K", None, "HyG Tvs", "IX",  "U"),
    (3, "L", None, "ComR",    "IX",  "F"),
    (3, "M", None, "[gap]",   "VII", "U"),
    # Function 4 — Outbound SDR
    (4, "A", 16,  "Cly Apl",  "IX",  "M"),
    (4, "B", 10,  "11x AiS",  "IX",  "M"),
    (4, "C", 11,  "Otr Slf",  "IX",  "M"),
    (4, "D", 12,  "11x Nks",  "IX",  "F"),
    (4, "E", 13,  "Grn Gng",  "IX",  "U"),
    (4, "F", 14,  "Cly ComR", "IX",  "U"),
    (4, "G", 9,   "11x AiS",  "IX",  "V"),
    (4, "H", 11,  "Cla BUp",  "IX",  "U"),
    (4, "J", 11,  "Gng Chr",  "IX",  "M"),
    (4, "K", 15,  "Ant Opr",  "II",  "U"),
    (4, "L", 12,  "Mm0 Lta",  "IV",  "U"),
    (4, "M", 14,  "LSm Brn",  "VII", "U"),
    # Function 5 — ABM
    (5, "A", 12,  "6sn Cly",  "IX",  "M"),
    (5, "B", 9,   "Mut 6sn",  "IX",  "M"),
    (5, "C", 10,  "Dmb 6sn",  "IX",  "M"),
    (5, "D", 9,   "Drf Qlf",  "IX",  "F"),
    (5, "E", 11,  "Gng Dlh",  "IX",  "U"),
    (5, "F", 18,  "ComR SNv", "IX",  "U"),
    (5, "G", 8,   "6sn Dmb",  "IX",  "V"),
    (5, "H", 9,   "6sn Cla",  "IX",  "M"),
    (5, "K", 9,   "Mar Opr",  "II",  "F"),
    (5, "L", 13,  "[gap]",    "IV",  "U"),
    (5, "M", 11,  "[gap]",    "VII", "U"),
    # Function 6 — New-biz AE
    (6, "A", 14,  "Hbb Rog",  "IX",  "M"),  # Hebbia/Rogo/Glean anchor cell
    (6, "B", 12,  "Acv Cla",  "IX",  "F"),
    (6, "C", 9,   "Otr Slf",  "IX",  "M"),
    (6, "D", 13,  "Acv Crs",  "IX",  "M"),
    (6, "E", 17,  "Gng Chr",  "IX",  "U"),
    (6, "F", 11,  "Pep Scr",  "IX",  "M"),
    (6, "G", 8,   "Agf 11x",  "IX",  "V"),
    (6, "H", 12,  "Cla BUp",  "IX",  "M"),
    (6, "I", 13,  "Prf DLH",  "IX",  "U"),
    (6, "J", 12,  "Gng Crs",  "IX",  "M"),
    (6, "K", 14,  "Ant Opr",  "II",  "F"),
    (6, "L", 16,  "Mm0 Lta",  "IV",  "U"),
    (6, "M", 13,  "LSm Brn",  "VII", "U"),
    # Function 7 — Enablement / training
    (7, "A", 8,   "Hsp Sm",   "IX",  "M"),
    (7, "B", 8,   "Hsp Sm",   "IX",  "M"),
    (7, "C", 8,   "Hsp Sm",   "IX",  "M"),
    (7, "D", 9,   "Gng Grn",  "IX",  "M"),
    (7, "E", 9,   "MTk Grn",  "IX",  "M"),
    (7, "G", 11,  "MTk Spk",  "IX",  "U"),
    (7, "J", 13,  "Hsp MTk",  "IX",  "U"),
    (7, "K", 9,   "HyB SN",   "IX",  "F"),
    (7, "L", 8,   "[gap]",    "IV",  "U"),
    (7, "M", 13,  "Glo Brn",  "VII", "U"),
    # Function 8 — RevOps / Sales Ops
    (8, "A", 7,   "Cla Pcs",  "IX",  "M"),
    (8, "F", 11,  "Sft Trv",  "IX",  "M"),
    (8, "G", 15,  "Cla BUp",  "IX",  "U"),
    (8, "H", 10,  "Cla Avi",  "IX",  "M"),
    (8, "K", 12,  "Ant CU",   "II",  "U"),
    (8, "L", 7,   "Cla BUp",  "IX",  "M"),
    (8, "M", 12,  "Gng Glo",  "VII", "F"),
    # Function 9 — Deal desk / procurement
    (9, "A", 9,   "AS CBI",   "IX",  "U"),
    (9, "B", 8,   "DLH Sub",  "IX",  "F"),
    (9, "G", 19,  "Lpo Vnt",  "IX",  "U"),   # THE CELL OF RECORD
    (9, "I", 16,  "Irc LSq",  "IX",  "U"),
    (9, "K", 13,  "SF Sub",   "IX",  "F"),
    (9, "L", 10,  "Irc LSq",  "IX",  "U"),
    (9, "M", 14,  "Glo Lng",  "VII", "U"),
    # Function 10 — CS / onboarding
    (10,"A", 8,   "Zd Itc",   "IX",  "M"),
    (10,"B", 8,   "Zd Itc",   "IX",  "M"),
    (10,"C", 9,   "Itc Frt",  "IX",  "M"),
    (10,"D", 14,  "Sie Dec",  "IX",  "M"),
    (10,"E", 12,  "Gst Cat",  "IX",  "U"),
    (10,"F", 11,  "Itc Pyl",  "IX",  "M"),
    (10,"G", 13,  "Sie Dec",  "IX",  "F"),
    (10,"K", 10,  "Ant CU",   "II",  "F"),
    (10,"L", 11,  "Sie Dec",  "IX",  "F"),
    (10,"M", 12,  "Lkr Glo",  "VII", "F"),
    # Function 11 — AM / renewals / expansion
    (11,"A", 10,  "Gst Cat",  "IX",  "U"),
    (11,"B", 9,   "[gap]",    "IX",  "U"),
    (11,"E", 11,  "Gst Grn",  "IX",  "U"),
    (11,"G", 13,  "SF Gst",   "IX",  "U"),
    (11,"H", 12,  "Gst CZ",   "IX",  "M"),
    (11,"I", 13,  "Sie Itc",  "IX",  "U"),
    (11,"K", 9,   "[gap]",    "II",  "U"),
    (11,"L", 14,  "Sie Mm0",  "IX",  "U"),
    (11,"M", 11,  "Lkr Glo",  "VII", "F"),
    # Function 12 — Forecasting / strategy
    (12,"A", 8,   "Cla Pgm",  "IX",  "F"),
    (12,"B", 8,   "Cla Pgm",  "IX",  "F"),
    (12,"C", 9,   "Cla Pgm",  "IX",  "F"),
    (12,"D", 14,  "Hex Def",  "IX",  "F"),  # Hex NYC
    (12,"F", 15,  "Cla Gln",  "IX",  "M"),
    (12,"G", 10,  "Pgm Mos",  "IX",  "F"),
    (12,"H", 15,  "Cla Avi",  "IX",  "M"),
    (12,"I", 8,   "[gap]",    "IX",  "U"),
    (12,"J", 9,   "Cla Pgm",  "IX",  "F"),
    (12,"K", 11,  "Pgm Mos",  "IX",  "F"),
    (12,"L", 13,  "BUp Mm0",  "IV",  "U"),
    (12,"M", 10,  "Glo Arz",  "VII", "U"),
]

# Lookup
CELL_BY = {(f, c): (ocq, vnd, strat, st) for (f, c, ocq, vnd, strat, st) in CELLS}


# ============================================================
# Page setup
# ============================================================
def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    # 170 x 110 user-units; matches 17 x 11 inches at 10 units/inch.
    ax.set_xlim(0, 170)
    ax.set_ylim(0, 110)
    ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax):
    LEFT, RIGHT = 7.5, 162.5
    TOP, BOTTOM = 104.5, 6.0
    # Outer rule
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.6))
    # Header-rule + footer-rule
    ax.plot([LEFT, RIGHT], [TOP - 8.5, TOP - 8.5], color=RULE, lw=0.5)
    ax.plot([LEFT, RIGHT], [BOTTOM + 9.5, BOTTOM + 9.5], color=RULE, lw=0.5)

    # Left depth-scale tick rule (geologist's column)
    tickx = LEFT - 2.6
    ax.plot([tickx, tickx], [BOTTOM + 9.5, TOP - 8.5], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 9.5, TOP - 8.5, 25)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([tickx - (1.0 if long else 0.5), tickx], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(tickx - 1.6, y, f"{i*4:02d}", ha="right", va="center",
                    fontsize=10, fontname=F_DMMONO, color=GRAY)

    # Title block
    ax.text(LEFT, TOP - 1.5,
            sp("AN ATLAS OF THE AGENT STRATA   ·   VOLUME IV   ·   GO-TO-MARKET CELLULAR MAP", 3),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 3.0, "AGENTS GTM  ·  CELL MATRIX",
            ha="left", va="top", fontsize=28.8, fontname=F_DISPLAY, color=INK)
    ax.text(LEFT, TOP - 6.7,
            "Twelve revenue functions stratified against thirteen agent capabilities — "
            "one hundred fifty-six cells of demand, density, and vapour.",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 8.0,
            "Tabula cellularum agenticarum  ·  functio per capacitatem  ·  intensitas opportunitatis",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # Plate badge — vermilion ring with 'I'
    ax.add_patch(mpatches.Circle((RIGHT - 2.0, TOP - 3.2), 1.4,
                                 fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 2.0, TOP - 3.2, "I", ha="center", va="center",
            fontsize=12, fontname=F_MONO_BOLD, color=VERMILION)
    ax.text(RIGHT, TOP - 6.3, sp("PLATE I OF I", 2),
            ha="right", va="top", fontsize=10, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(RIGHT, TOP - 8.0, sp("VOL IV  ·  MMXXVI  ·  MAY", 2),
            ha="right", va="top", fontsize=10, fontname=F_DMMONO, color=GRAY)

    # Footer
    ax.text(LEFT, BOTTOM + 4.5,
            sp("SUBSTRATE  ·  VOL IV  ·  CELL MATRIX  ·  PLATE I OF I", 3),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 2.6,
            sp("Compiled for A. Yedi  ·  Cycle MMXXVI  ·  Rev. I", 2),
            ha="left", va="top", fontsize=10, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 2.6, sp("MMXXVI · V", 2), ha="right", va="top",
            fontsize=10, fontname=F_DMMONO, color=GRAY)

    return LEFT, RIGHT, TOP - 8.5, BOTTOM + 9.5


# ============================================================
# Ink-density helper for OCQ
# ============================================================
def cell_color(ocq, is_top15):
    """
    Light = low OCQ. Dark = high OCQ. Top-15 are vermilion-flagged.
    """
    if ocq is None:
        # Unscored cell — faint cream wash.
        return GRAY_FAINT, 0.30
    if is_top15:
        # Vermilion saturation by OCQ height.
        s = (ocq - 13) / 6.0  # 13 -> 0, 19 -> 1
        s = max(0.45, min(1.0, 0.55 + 0.45 * s))
        return VERMILION, s
    # Non-Top-15: ink density gradient by OCQ score.
    # Map 6..15 to alpha 0.10..0.65
    s = (ocq - 6) / 9.0
    s = max(0.10, min(0.65, 0.10 + 0.55 * s))
    return INK, s


# ============================================================
# THE PLATE
# ============================================================
def render_matrix(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax)

    # Grid coordinates: rows 12 functions (top to bottom = 1..12),
    # cols 13 capabilities (left to right = A..M).

    # Left label gutter and top header strip carved from the matrix area.
    row_label_w = 22.0   # left gutter for function labels
    col_header_h = 8.0   # top strip for capability headers

    grid_left   = L + row_label_w
    grid_right  = R - 2.0
    grid_top    = TOP - col_header_h - 1.0
    grid_bottom = BOT + 12.0   # leave room for legend / footer block

    n_rows = len(FUNCTIONS)
    n_cols = len(CAPABILITIES)
    col_w = (grid_right - grid_left) / n_cols
    row_h = (grid_top - grid_bottom) / n_rows

    # ---- Capability column headers (top strip) ---------------------------
    # Letter (large) and short-caps name (below)
    header_band_y = grid_top + 0.6
    ax.plot([grid_left, grid_right], [grid_top + col_header_h - 0.5,
            grid_top + col_header_h - 0.5], color=RULE, lw=0.4)

    for ci, (letter, short, _) in enumerate(CAPABILITIES):
        cx = grid_left + ci * col_w + col_w / 2
        # Vertical tick from column position down through grid bottom.
        ax.plot([cx, cx], [grid_top + col_header_h - 0.5, grid_top + col_header_h - 0.2],
                color=RULE, lw=0.35)
        # Letter (display caps)
        ax.text(cx, grid_top + col_header_h - 2.4, letter,
                ha="center", va="center",
                fontsize=12, fontname=F_DISPLAY, color=INK)
        # Short name caps
        ax.text(cx, grid_top + col_header_h - 5.5, sp(short, 0),
                ha="center", va="center",
                fontsize=10, fontname=F_MONO, color=VERMILION)

    # Top hairline above grid
    ax.plot([grid_left, grid_right], [grid_top, grid_top], color=RULE, lw=0.55)
    # Header marker for the function column
    ax.text(L + 1.0, grid_top + col_header_h - 2.4, sp("FUNCTIONS", 1),
            ha="left", va="center",
            fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.text(L + 1.0, grid_top + col_header_h - 5.5, sp("12 ROWS  ·  REVENUE STRATA", 1),
            ha="left", va="center",
            fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # Header marker for capability columns
    ax.text(grid_left + (grid_right - grid_left) / 2, grid_top + col_header_h - 7.0,
            sp("CAPABILITIES  ·  13 COLUMNS  ·  A — M", 2),
            ha="center", va="center",
            fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # ---- Function row labels (left gutter) -------------------------------
    for ri, (num, short, desc) in enumerate(FUNCTIONS):
        y_mid = grid_top - (ri + 0.5) * row_h
        # Number badge
        ax.add_patch(mpatches.Circle((L + 1.4, y_mid), 1.1,
                                     fc=PAPER, ec=VERMILION, lw=0.55))
        ax.text(L + 1.4, y_mid, num, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=VERMILION)
        # Short display caps
        ax.text(L + 3.5, y_mid + 0.6, short, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        # Italic descriptor
        ax.text(L + 3.5, y_mid - 1.6, desc, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # ---- The 156 cells ---------------------------------------------------
    for ri, (fnum_s, _, _) in enumerate(FUNCTIONS):
        fnum = int(fnum_s)
        y_top = grid_top - ri * row_h
        y_bot = y_top - row_h
        for ci, (letter, _, _) in enumerate(CAPABILITIES):
            x_left = grid_left + ci * col_w
            x_right = x_left + col_w

            # Cell bounding hairline (thin)
            ax.add_patch(mpatches.Rectangle((x_left, y_bot),
                                             col_w, row_h,
                                             fill=False,
                                             ec=GRAY_LIGHT, lw=0.25))

            data = CELL_BY.get((fnum, letter))
            if data is None:
                # N/A or unmapped cell — leave faint
                ax.add_patch(mpatches.Rectangle((x_left + 0.15, y_bot + 0.15),
                                                 col_w - 0.3, row_h - 0.3,
                                                 fc=PAPER, ec="none"))
                continue

            ocq, vnd, strat, st = data
            is_top15 = (fnum, letter) in TOP15
            fc, alpha = cell_color(ocq, is_top15)

            # Filled cell with the ink-density / vermilion intensity.
            ax.add_patch(mpatches.Rectangle((x_left + 0.15, y_bot + 0.15),
                                             col_w - 0.3, row_h - 0.3,
                                             fc=fc, ec="none", alpha=alpha))

            # For Top-15: extra ring + vermilion border
            if is_top15:
                ax.add_patch(mpatches.Rectangle((x_left + 0.15, y_bot + 0.15),
                                                 col_w - 0.3, row_h - 0.3,
                                                 fill=False, ec=VERMILION, lw=0.7))

            # Annotation: vendor abbrev + stratum + OCQ
            # Choose text color so it remains legible across ink-density.
            if is_top15 and alpha > 0.55:
                txt_c = PAPER
                strat_c = PAPER
            elif (fc == INK) and alpha > 0.45:
                txt_c = PAPER
                strat_c = GRAY_LIGHT
            else:
                txt_c = INK
                strat_c = VERMILION

            # Vendor abbreviation (top of cell)
            if vnd:
                ax.text(x_left + col_w / 2, y_bot + row_h - 1.5, vnd,
                        ha="center", va="center",
                        fontsize=10, fontname=F_DMMONO, color=txt_c)
            # Stratum tag (middle, small bracketed letter)
            if strat:
                ax.text(x_left + col_w / 2, y_bot + row_h / 2 + 0.1,
                        f"[{strat}]",
                        ha="center", va="center",
                        fontsize=10, fontname=F_SERIF_IT, color=strat_c)
            # OCQ score (bottom)
            if ocq is not None:
                ax.text(x_left + col_w / 2, y_bot + 1.4, f"{ocq:02d}",
                        ha="center", va="center",
                        fontsize=10, fontname=F_MONO_BOLD, color=txt_c)
            else:
                ax.text(x_left + col_w / 2, y_bot + 1.4, "—",
                        ha="center", va="center",
                        fontsize=10, fontname=F_DMMONO, color=GRAY)

    # Grid bounding rule
    ax.add_patch(mpatches.Rectangle((grid_left, grid_bottom),
                                     grid_right - grid_left, grid_top - grid_bottom,
                                     fill=False, ec=RULE, lw=0.5))

    # Major divisions: thicker horizontal rule between marketing (1-3),
    # sales-motion (4-7), ops (8-9), post-sale (10-12)
    for boundary_ri in (3, 7, 9):
        y = grid_top - boundary_ri * row_h
        ax.plot([grid_left, grid_right], [y, y], color=RULE, lw=0.55)
        # Cluster annotation in the gutter
    cluster_labels = [
        (0, 3, "MARKETING"),
        (3, 7, "SELLING"),
        (7, 9, "OPERATIONS"),
        (9, 12, "POST-SALE"),
    ]
    for r0, r1, name in cluster_labels:
        y_mid = grid_top - (r0 + r1) / 2 * row_h
        ax.text(L - 5.5, y_mid, sp(name, 2),
                ha="center", va="center", rotation=90,
                fontsize=10, fontname=F_MONO, color=VERDIGRIS)

    # ---- Footer block: legend + key + cruxes -----------------------------
    leg_y_top = grid_bottom - 1.0
    legend_y  = leg_y_top - 1.0
    ax.plot([L + 1.0, R - 1.0], [legend_y, legend_y], color=RULE, lw=0.45)

    # Legend column 1 — OCQ intensity bar
    lx = L + 1.0
    ax.text(lx, legend_y - 0.8, sp("OCQ INTENSITY  ·  CELL FILL", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    bar_y0 = legend_y - 4.5
    swatch_w = 2.2
    swatch_h = 1.6
    # Non-Top-15 (ink density)
    for i, s_ocq in enumerate([6, 9, 11, 13, 15]):
        x = lx + i * (swatch_w + 0.4)
        fc, alpha = cell_color(s_ocq, False)
        ax.add_patch(mpatches.Rectangle((x, bar_y0), swatch_w, swatch_h,
                                         fc=fc, ec=INK_SOFT, lw=0.3, alpha=alpha))
        ax.text(x + swatch_w / 2, bar_y0 - 1.0, str(s_ocq),
                ha="center", va="top", fontsize=10, fontname=F_DMMONO, color=GRAY)
    # Top-15 vermilion swatch
    for i, s_ocq in enumerate([14, 16, 19]):
        x = lx + (5 + i) * (swatch_w + 0.4) + 1.0
        fc, alpha = cell_color(s_ocq, True)
        ax.add_patch(mpatches.Rectangle((x, bar_y0), swatch_w, swatch_h,
                                         fc=fc, ec=VERMILION, lw=0.55, alpha=alpha))
        ax.text(x + swatch_w / 2, bar_y0 - 1.0, str(s_ocq),
                ha="center", va="top", fontsize=10, fontname=F_DMMONO, color=VERMILION)
    ax.text(lx + 5 * (swatch_w + 0.4) + 0.6, bar_y0 + swatch_h / 2, "TOP-15",
            ha="left", va="center", fontsize=10, fontname=F_MONO, color=VERMILION)

    # Legend column 2 — stratum-letter key
    sx = L + 50.0
    ax.text(sx, legend_y - 0.8, sp("STRATUM KEY  ·  [BRACKET]", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    stratum_entries = [
        ("II",   "Agent runtimes"),
        ("IV",   "Memory · state"),
        ("VII",  "Eval · observability"),
        ("VIII", "Runtime safety"),
        ("IX",   "Vertical products"),
        ("X",    "End-user surfaces"),
    ]
    for i, (k, v) in enumerate(stratum_entries):
        col = i // 3
        row = i % 3
        x = sx + col * 19
        y = legend_y - 2.5 - row * 1.5
        ax.text(x, y, f"[{k}]", fontsize=10, fontname=F_SERIF_IT, color=VERMILION,
                va="center")
        ax.text(x + 5.5, y, v, fontsize=10, fontname=F_SERIF, color=INK_SOFT,
                va="center")

    # Legend column 3 — vermilion meaning
    vx = L + 92.0
    ax.text(vx, legend_y - 0.8, sp("VERMILION  ·  TOP-15 BY OCQ", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.text(vx, legend_y - 2.5,
            "Vermilion-bordered cells are the fifteen highest OCQ scores in the",
            fontsize=10, fontname=F_SERIF, color=INK_SOFT, va="center")
    ax.text(vx, legend_y - 3.7,
            "matrix — opportunity × claimability × time-to-monetize. The cell",
            fontsize=10, fontname=F_SERIF, color=INK_SOFT, va="center")
    ax.text(vx, legend_y - 4.9,
            "of record is (9, G) at 19/20 — the agent-procurement gauntlet.",
            fontsize=10, fontname=F_SERIF_IT, color=INK, va="center")

    # Legend column 4 — anatomy of a cell glyph
    ax_x = L + 138.0
    ax.text(ax_x, legend_y - 0.8, sp("ANATOMY OF A CELL", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    # Sample cell mockup
    sx0 = ax_x
    sy0 = legend_y - 6.5
    sw = 8.0
    sh = 5.0
    ax.add_patch(mpatches.Rectangle((sx0, sy0), sw, sh,
                                     fc=VERMILION, ec=VERMILION, lw=0.7, alpha=0.7))
    ax.text(sx0 + sw / 2, sy0 + sh - 1.0, "Lpo Vnt",
            ha="center", va="center", fontsize=10, fontname=F_DMMONO, color=PAPER)
    ax.text(sx0 + sw / 2, sy0 + sh / 2, "[IX]",
            ha="center", va="center", fontsize=10, fontname=F_SERIF_IT, color=PAPER)
    ax.text(sx0 + sw / 2, sy0 + 0.8, "19",
            ha="center", va="center", fontsize=10, fontname=F_MONO_BOLD, color=PAPER)
    # Annotation lines
    ax.plot([sx0 + sw + 0.4, sx0 + sw + 1.8], [sy0 + sh - 1.0, sy0 + sh - 1.0],
            color=GRAY, lw=0.3)
    ax.text(sx0 + sw + 2.0, sy0 + sh - 1.0, "vendor abbrev.",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT, va="center")
    ax.plot([sx0 + sw + 0.4, sx0 + sw + 1.8], [sy0 + sh / 2, sy0 + sh / 2],
            color=GRAY, lw=0.3)
    ax.text(sx0 + sw + 2.0, sy0 + sh / 2, "stratum tag",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT, va="center")
    ax.plot([sx0 + sw + 0.4, sx0 + sw + 1.8], [sy0 + 0.8, sy0 + 0.8],
            color=GRAY, lw=0.3)
    ax.text(sx0 + sw + 2.0, sy0 + 0.8, "OCQ /20",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT, va="center")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        render_matrix(pdf)
    sz_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"Wrote {OUT_PATH}  ·  {sz_kb:.1f} KB")
