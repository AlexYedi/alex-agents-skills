"""
SUBSTRATE  ·  Vol IV  ·  Decisions Playbook  ·  Plates VI–X.

A 5-plate framework-analysis volume that closes Volume IV with the analytical
findings (heat-map at cell resolution, Wardley evolution map, 7 Powers grid,
JTBD phase canvas, action portfolio + 18-month map).

Mirrors Volume III's Volume-II-of-plates build style: framework synthesis,
ink-on-cream, hairline rules, condensed display caps, single vermilion accent.

Output: AGENTS_GTM_DECISIONS.pdf — 5 plates (Tabloid where landscape, US Letter
where portrait), all written via PdfPages with per-plate savefig + close.
"""
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
import numpy as np

# ============================================================
# FONTS  ·  PALETTE  ·  GRAMMAR
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
F_SERIF         = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT      = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP    = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT = fam("InstrumentSerif-Italic.ttf")
F_MONO          = fam("GeistMono-Regular.ttf")
F_MONO_BOLD     = fam("GeistMono-Bold.ttf")
F_DMMONO        = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"]  = 42

PAPER      = "#F1E9D6"
INK        = "#171210"
INK_SOFT   = "#3A2F26"
GRAY       = "#7A6E60"
GRAY_LIGHT = "#C9BFA9"
GRAY_FAINT = "#E4DCC4"
RULE       = "#2A211B"
VERMILION  = "#A6371F"
VERDIGRIS  = "#456C5C"
OCHRE      = "#A37425"

DPI = 300
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm/AGENTS_GTM_DECISIONS.pdf"


# ============================================================
# UTILITIES
# ============================================================

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


def new_page_landscape():
    """Tabloid landscape, 17 x 11 in.  ax coords 0–170 x 0–110."""
    fig = plt.figure(figsize=(17.0, 11.0), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 170); ax.set_ylim(0, 110)
    ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def new_page_portrait():
    """US Letter portrait, 8.5 x 11 in.  ax coords 0–100 x 0–129.5."""
    fig = plt.figure(figsize=(8.5, 11.0), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 129.5)
    ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame_landscape(ax, plate_no, title_top, subtitle_top, latin, plate_label):
    """Frame for tabloid-landscape plates."""
    LEFT, RIGHT = 7.5, 162.5
    TOP, BOTTOM = 104.5, 6.0
    # Outer rule
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.6))
    # Header rule
    ax.plot([LEFT, RIGHT], [TOP - 8.0, TOP - 8.0], color=RULE, lw=0.5)
    # Footer rule
    ax.plot([LEFT, RIGHT], [BOTTOM + 9.0, BOTTOM + 9.0], color=RULE, lw=0.5)

    # Left depth-scale tick rule
    tickx = LEFT - 2.6
    ax.plot([tickx, tickx], [BOTTOM + 9.0, TOP - 8.0], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 9.0, TOP - 8.0, 25)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([tickx - (1.0 if long else 0.5), tickx], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(tickx - 1.6, y, f"{i*4:02d}", ha="right", va="center",
                    fontsize=4.4, fontname=F_DMMONO, color=GRAY)

    # Title block
    ax.text(LEFT, TOP - 1.5,
            sp("AN ATLAS OF THE AGENT STRATA   ·   VOLUME IV   ·   DECISIONS PLAYBOOK", 3),
            ha="left", va="top", fontsize=6.5, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 3.1, title_top.upper(),
            ha="left", va="top", fontsize=22, fontname=F_DISPLAY, color=INK)
    ax.text(LEFT, TOP - 6.4, subtitle_top,
            ha="left", va="top", fontsize=6.8, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 7.6, latin,
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_IT, color=GRAY)

    # Plate badge — vermilion ring with Roman numeral
    ax.add_patch(mpatches.Circle((RIGHT - 2.2, TOP - 3.3), 1.5,
                                 fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 2.2, TOP - 3.3, plate_no, ha="center", va="center",
            fontsize=9, fontname=F_MONO_BOLD, color=VERMILION)
    ax.text(RIGHT, TOP - 6.4, sp(plate_label, 2),
            ha="right", va="top", fontsize=6.2, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(RIGHT, TOP - 7.7, sp("VOL IV  ·  MMXXVI  ·  MAY", 2),
            ha="right", va="top", fontsize=4.8, fontname=F_DMMONO, color=GRAY)

    # Footer
    ax.text(LEFT, BOTTOM + 4.5,
            sp("SUBSTRATE  ·  VOL IV  ·  DECISIONS  ·  " + plate_label, 3),
            ha="left", va="top", fontsize=4.7, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 2.6,
            sp("Compiled for A. Yedi  ·  Cycle MMXXVI  ·  Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 2.6, sp("MMXXVI · V", 2), ha="right", va="top",
            fontsize=5.3, fontname=F_DMMONO, color=GRAY)

    return LEFT, RIGHT, TOP - 8.0, BOTTOM + 9.0


def page_frame_portrait(ax, plate_no, title_top, subtitle_top, latin, plate_label):
    """Frame for portrait plates (Letter).  Returns inner bounds."""
    LEFT, RIGHT = 7.5, 92.5
    TOP, BOTTOM = 123.5, 6.0
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.6))
    ax.plot([LEFT, RIGHT], [TOP - 7.0, TOP - 7.0], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 7.5, BOTTOM + 7.5], color=RULE, lw=0.45)

    tickx = LEFT - 2.6
    ax.plot([tickx, tickx], [BOTTOM + 7.5, TOP - 7.0], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 7.5, TOP - 7.0, 28)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([tickx - (1.0 if long else 0.5), tickx], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(tickx - 1.6, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=4.3, fontname=F_DMMONO, color=GRAY)

    ax.text(LEFT, TOP - 1.2,
            sp("AN ATLAS OF THE AGENT STRATA   ·   VOLUME IV   ·   DECISIONS", 3),
            ha="left", va="top", fontsize=5.8, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 2.5, title_top.upper(),
            ha="left", va="top", fontsize=18, fontname=F_DISPLAY, color=INK)
    ax.text(LEFT, TOP - 5.2, subtitle_top,
            ha="left", va="top", fontsize=6.0, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 6.3, latin,
            ha="left", va="top", fontsize=4.8, fontname=F_SERIF_IT, color=GRAY)

    ax.add_patch(mpatches.Circle((RIGHT - 1.8, TOP - 2.4), 1.3,
                                 fill=False, ec=VERMILION, lw=0.65))
    ax.text(RIGHT - 1.8, TOP - 2.4, plate_no, ha="center", va="center",
            fontsize=8, fontname=F_MONO_BOLD, color=VERMILION)
    ax.text(RIGHT, TOP - 5.3, sp(plate_label, 2),
            ha="right", va="top", fontsize=5.6, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(RIGHT, TOP - 6.4, sp("VOL IV · MMXXVI · MAY", 2),
            ha="right", va="top", fontsize=4.4, fontname=F_DMMONO, color=GRAY)

    ax.text(LEFT, BOTTOM + 4.5,
            sp("SUBSTRATE  ·  VOL IV  ·  DECISIONS  ·  " + plate_label, 3),
            ha="left", va="top", fontsize=4.4, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 2.4,
            sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=4.9, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 2.4, sp("MMXXVI · V", 2), ha="right", va="top",
            fontsize=5.0, fontname=F_DMMONO, color=GRAY)

    return LEFT, RIGHT, TOP - 7.0, BOTTOM + 7.5


# ============================================================
# DATA  ·  reused from matrix script  ·  CELLS + scores
# ============================================================

CAPABILITIES = [
    ("A", "RESEARCH"),    ("B", "PERSONAL."),  ("C", "ORCHESTR."),
    ("D", "DIALOG."),     ("E", "MEETING"),    ("F", "CRM-GRAPH"),
    ("G", "MULTI-STEP"),  ("H", "FORECAST"),   ("I", "NEGOTIATE"),
    ("J", "COACH"),       ("K", "COMP-USE"),   ("L", "MEMORY"),
    ("M", "OBSERVE"),
]

FUNCTIONS = [
    ("1",  "DEMAND-GEN"),  ("2",  "CONTENT"),       ("3",  "INBOUND-PLG"),
    ("4",  "OUTBOUND"),    ("5",  "ABM"),           ("6",  "NEW-BIZ AE"),
    ("7",  "ENABLE"),      ("8",  "REV-OPS"),       ("9",  "DEAL-DESK"),
    ("10", "CS"),          ("11", "AM-RENEW"),      ("12", "FORECAST"),
]

# Cell OCQ scores  ·  None = unscored cell
# Layout matches matrix script.
CELL_OCQ = {
    (1, "A"): 11, (1, "K"): 13, (1, "M"): 14,
    (2, "G"): 9, (2, "K"): 13, (2, "M"): 12,
    (3, "A"): 14,
    (4, "A"): 16, (4, "B"): 10, (4, "C"): 11, (4, "D"): 12, (4, "E"): 13,
    (4, "F"): 14, (4, "G"): 9, (4, "H"): 11, (4, "J"): 11, (4, "K"): 15,
    (4, "L"): 12, (4, "M"): 14,
    (5, "A"): 12, (5, "B"): 9, (5, "C"): 10, (5, "D"): 9, (5, "E"): 11,
    (5, "F"): 18, (5, "G"): 8, (5, "H"): 9, (5, "K"): 9, (5, "L"): 13,
    (5, "M"): 11,
    (6, "A"): 14, (6, "B"): 12, (6, "C"): 9, (6, "D"): 13, (6, "E"): 17,
    (6, "F"): 11, (6, "G"): 8, (6, "H"): 12, (6, "I"): 13, (6, "J"): 12,
    (6, "K"): 14, (6, "L"): 16, (6, "M"): 13,
    (7, "A"): 8, (7, "B"): 8, (7, "C"): 8, (7, "D"): 9, (7, "E"): 9,
    (7, "G"): 11, (7, "J"): 13, (7, "K"): 9, (7, "L"): 8, (7, "M"): 13,
    (8, "A"): 7, (8, "F"): 11, (8, "G"): 15, (8, "H"): 10, (8, "K"): 12,
    (8, "L"): 7, (8, "M"): 12,
    (9, "A"): 9, (9, "B"): 8, (9, "G"): 19, (9, "I"): 16, (9, "K"): 13,
    (9, "L"): 10, (9, "M"): 14,
    (10, "A"): 8, (10, "B"): 8, (10, "C"): 9, (10, "D"): 14, (10, "E"): 12,
    (10, "F"): 11, (10, "G"): 13, (10, "K"): 10, (10, "L"): 11, (10, "M"): 12,
    (11, "A"): 10, (11, "B"): 9, (11, "E"): 11, (11, "G"): 13, (11, "H"): 12,
    (11, "I"): 13, (11, "K"): 9, (11, "L"): 14, (11, "M"): 11,
    (12, "A"): 8, (12, "B"): 8, (12, "C"): 9, (12, "D"): 14, (12, "F"): 15,
    (12, "G"): 10, (12, "H"): 15, (12, "I"): 8, (12, "J"): 9, (12, "K"): 11,
    (12, "L"): 13, (12, "M"): 10,
}

# Top-15 high-OCQ cells (vermilion band)
TOP15 = {
    (9, "G"), (5, "F"), (6, "E"), (4, "A"), (6, "L"),
    (9, "I"), (8, "G"), (4, "K"), (12, "F"), (12, "H"),
    (4, "M"), (9, "M"), (11, "L"), (3, "A"), (6, "K"),
}


# ============================================================
# PLATE VI  ·  OCQ CELL-HEAT (pure intensity, no labels in cells)
# ============================================================

def plate_vi(pdf):
    fig, ax = new_page_landscape()
    L, R, TOP, BOT = page_frame_landscape(
        ax, "VI",
        "OCQ Cell-Heat · 156 Coordinates",
        "The full 12×13 agent-GTM cellular map rendered as pure intensity. "
        "Three saturation bands: vermilion for Top-15, mid-ink for 11—15, low-ink for 6—10.",
        "Tabula opportunitatum sine vocabulis · intensitas pura · clavem candentem ad cellam claram",
        "PLATE VI OF X")

    # Grid frame
    grid_left   = L + 22.0
    grid_right  = R - 38.0     # leave room for histogram on right
    grid_top    = TOP - 6.0
    grid_bottom = BOT + 14.0

    n_rows = len(FUNCTIONS)
    n_cols = len(CAPABILITIES)
    col_w = (grid_right - grid_left) / n_cols
    row_h = (grid_top - grid_bottom) / n_rows

    # Capability column headers (only letters, terse)
    for ci, (letter, short) in enumerate(CAPABILITIES):
        cx = grid_left + (ci + 0.5) * col_w
        ax.text(cx, grid_top + 2.6, letter,
                ha="center", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        ax.text(cx, grid_top + 0.8, sp(short, 0),
                ha="center", va="center",
                fontsize=4.2, fontname=F_MONO, color=VERMILION)

    # Function row labels (terse, leftside)
    for ri, (num, short) in enumerate(FUNCTIONS):
        y_mid = grid_top - (ri + 0.5) * row_h
        ax.add_patch(mpatches.Circle((L + 2.0, y_mid), 1.1,
                                     fc=PAPER, ec=VERMILION, lw=0.5))
        ax.text(L + 2.0, y_mid, num, ha="center", va="center",
                fontsize=5.2, fontname=F_DMMONO, color=VERMILION)
        ax.text(L + 4.2, y_mid, short, ha="left", va="center",
                fontsize=6.6, fontname=F_DISPLAY, color=INK)

    # Render heat cells (NO text, only intensity bands)
    for ri, (fnum_s, _) in enumerate(FUNCTIONS):
        fnum = int(fnum_s)
        y_bot = grid_top - (ri + 1) * row_h
        for ci, (letter, _) in enumerate(CAPABILITIES):
            x_left = grid_left + ci * col_w

            # Hairline border on every cell
            ax.add_patch(mpatches.Rectangle((x_left, y_bot), col_w, row_h,
                                            fill=False, ec=GRAY_LIGHT, lw=0.25))

            ocq = CELL_OCQ.get((fnum, letter))
            if ocq is None:
                # Empty / gap = paper-color with hairline border only
                continue

            is_top15 = (fnum, letter) in TOP15
            if is_top15:
                # Top-15 vermilion saturation band
                s = (ocq - 13) / 6.0
                alpha = max(0.55, min(1.0, 0.55 + 0.45 * s))
                fc = VERMILION
                ec = VERMILION
                lw = 0.55
            elif ocq >= 11:
                # Mid-ink band  ·  11–15 non-top-15
                s = (ocq - 11) / 4.0
                alpha = 0.35 + 0.30 * s
                fc = INK
                ec = "none"
                lw = 0.0
            else:
                # Low-ink band  ·  ≤10
                s = (ocq - 6) / 4.0
                alpha = 0.10 + 0.18 * max(0.0, min(1.0, s))
                fc = INK
                ec = "none"
                lw = 0.0

            ax.add_patch(mpatches.Rectangle((x_left + 0.18, y_bot + 0.18),
                                            col_w - 0.36, row_h - 0.36,
                                            fc=fc, ec=ec, lw=lw, alpha=alpha))

    # Outer grid rule
    ax.add_patch(mpatches.Rectangle((grid_left, grid_bottom),
                                    grid_right - grid_left, grid_top - grid_bottom,
                                    fill=False, ec=RULE, lw=0.5))

    # Major divisions
    for boundary_ri in (3, 7, 9):
        y = grid_top - boundary_ri * row_h
        ax.plot([grid_left, grid_right], [y, y], color=RULE, lw=0.5)
    cluster_labels = [
        (0, 3, "MARKETING"),
        (3, 7, "SELLING"),
        (7, 9, "OPERATIONS"),
        (9, 12, "POST-SALE"),
    ]
    for r0, r1, name in cluster_labels:
        y_mid = grid_top - (r0 + r1) / 2 * row_h
        ax.text(L - 6.0, y_mid, sp(name, 2),
                ha="center", va="center", rotation=90,
                fontsize=4.5, fontname=F_MONO, color=VERDIGRIS)

    # ---- Right-side histogram of OCQ distribution ------------------------
    hist_left  = grid_right + 5.0
    hist_right = R - 2.0
    hist_top   = grid_top
    hist_bot   = grid_bottom

    scores = [v for v in CELL_OCQ.values() if v is not None]
    bins = list(range(6, 20))  # 6..19 inclusive
    counts = [sum(1 for s in scores if s == b) for b in bins]
    max_c = max(counts) if counts else 1

    ax.text(hist_left, hist_top + 2.5, sp("OCQ DISTRIBUTION", 2),
            ha="left", va="bottom",
            fontsize=5.4, fontname=F_MONO, color=VERMILION)
    ax.text(hist_left, hist_top + 0.9,
            "Counts of scored cells by OCQ band.",
            ha="left", va="bottom",
            fontsize=4.6, fontname=F_SERIF_IT, color=GRAY)

    bar_h = (hist_top - hist_bot) / len(bins)
    bar_max_w = hist_right - hist_left - 8.0
    for i, (b, c) in enumerate(zip(bins, counts)):
        y_mid = hist_top - (i + 0.5) * bar_h
        # Score label on left
        is_top15_band = b >= 14
        col = VERMILION if is_top15_band else (INK if b >= 11 else GRAY)
        ax.text(hist_left + 1.0, y_mid, f"{b:02d}",
                ha="right", va="center",
                fontsize=4.8, fontname=F_DMMONO, color=col)
        # Bar
        bw = (c / max_c) * bar_max_w if c > 0 else 0
        if c > 0:
            ax.add_patch(mpatches.Rectangle((hist_left + 2.0, y_mid - bar_h * 0.32),
                                            bw, bar_h * 0.64,
                                            fc=col, ec="none",
                                            alpha=0.75 if is_top15_band else 0.55))
        # Count text
        ax.text(hist_left + 2.5 + bw, y_mid, f" {c}",
                ha="left", va="center",
                fontsize=4.2, fontname=F_DMMONO, color=INK_SOFT)
    # Frame around histogram axis
    ax.plot([hist_left + 2.0, hist_left + 2.0], [hist_bot, hist_top],
            color=RULE, lw=0.4)

    # ---- Footer legend  ·  three saturation bands -----------------------
    leg_y = BOT + 6.0
    ax.plot([L + 1.0, R - 1.0], [leg_y + 1.5, leg_y + 1.5], color=RULE, lw=0.45)
    ax.text(L + 1.0, leg_y + 0.5, sp("SATURATION BANDS  ·  THREE  ·  SCORE 6—19", 2),
            ha="left", va="top", fontsize=5.0, fontname=F_MONO, color=VERMILION)

    # Three band swatches
    band_defs = [
        ("TOP-15  ·  OCQ 13—19 vermilion-flagged", VERMILION, [14, 16, 19], True),
        ("MID-INK  ·  OCQ 11—15 non-flagged",      INK,       [11, 13, 15], False),
        ("LOW-INK  ·  OCQ 6—10",                   INK,       [7, 9, 10],   False),
    ]
    for bi, (label, base, samples, is_top) in enumerate(band_defs):
        x = L + 1.0 + bi * 52.0
        ax.text(x, leg_y - 1.5, label,
                ha="left", va="top",
                fontsize=4.6, fontname=F_SERIF_IT, color=INK)
        for j, s_ocq in enumerate(samples):
            sx = x + 1.0 + j * 5.0
            sy = leg_y - 4.5
            sw = 4.0
            sh = 2.2
            if is_top:
                alpha = max(0.55, min(1.0, 0.55 + 0.45 * (s_ocq - 13) / 6.0))
                fc, ec = VERMILION, VERMILION
            elif s_ocq >= 11:
                alpha = 0.35 + 0.30 * (s_ocq - 11) / 4.0
                fc, ec = INK, "none"
            else:
                alpha = 0.10 + 0.18 * max(0, (s_ocq - 6) / 4.0)
                fc, ec = INK, "none"
            ax.add_patch(mpatches.Rectangle((sx, sy), sw, sh,
                                            fc=fc, ec=ec, lw=0.4, alpha=alpha))
            ax.text(sx + sw / 2, sy - 0.9, str(s_ocq),
                    ha="center", va="top",
                    fontsize=4.2, fontname=F_DMMONO, color=col if False else GRAY)

    # Empty cell key (placed inline with last band sample)
    x_empty = L + 1.0 + 2 * 52.0 + 22.0
    ax.text(x_empty, leg_y - 1.5, "EMPTY  ·  unscored",
            ha="left", va="top",
            fontsize=4.6, fontname=F_SERIF_IT, color=INK)
    ax.add_patch(mpatches.Rectangle((x_empty + 1.0, leg_y - 4.5), 4.0, 2.2,
                                    fill=False, ec=GRAY_LIGHT, lw=0.4))

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE VII  ·  WARDLEY EVOLUTION MAP
# ============================================================

def plate_vii(pdf):
    fig, ax = new_page_landscape()
    L, R, TOP, BOT = page_frame_landscape(
        ax, "VII",
        "Wardley · Agent-GTM Evolution · 2026—2027",
        "Four anchored user-needs cascading through the matrix · evolution stage along the X-axis · "
        "six punctuated equilibria · strategic-quadrant overlay.",
        "Cartographia agenticum × functio per actorem · stadium evolutionis MMXXVI–MMXXVII",
        "PLATE VII OF X")

    # Map frame
    mx0 = L + 18.0
    mx1 = R - 38.0
    my0 = BOT + 18.0   # bottom of map  ·  Foundation
    my1 = TOP - 5.0    # top of map  ·  User

    sw = (mx1 - mx0) / 4
    stages = ["GENESIS", "CUSTOM-BUILT", "PRODUCT / RENTAL", "COMMODITY / UTILITY"]
    scolors = [VERMILION, OCHRE, VERDIGRIS, GRAY]
    # Quadrant background bands (faint) — Pioneer (Genesis-Custom top), Settle (Custom-Product mid),
    # Town-Plan (Product-Commodity bottom), Partner (rightmost).
    # Render as faint horizontal bands
    band_alpha = 0.06
    ax.add_patch(mpatches.Rectangle((mx0, my0 + (my1 - my0) * 0.55),
                                    sw * 2, (my1 - my0) * 0.45,
                                    fc=VERMILION, ec="none", alpha=band_alpha))
    ax.add_patch(mpatches.Rectangle((mx0 + sw, my0 + (my1 - my0) * 0.25),
                                    sw * 2, (my1 - my0) * 0.55,
                                    fc=OCHRE, ec="none", alpha=band_alpha))
    ax.add_patch(mpatches.Rectangle((mx0 + sw * 2, my0),
                                    sw * 2, (my1 - my0) * 0.45,
                                    fc=VERDIGRIS, ec="none", alpha=band_alpha))
    # Quadrant labels (tiny corner glyphs)
    ax.text(mx0 + 0.5, my1 - 1.0, sp("PIONEER", 2),
            ha="left", va="top", fontsize=5.5, fontname=F_DISPLAY, color=VERMILION)
    ax.text(mx0 + sw * 1.5 + 0.5, my0 + (my1 - my0) * 0.55, sp("SETTLE", 2),
            ha="left", va="bottom", fontsize=5.5, fontname=F_DISPLAY, color=OCHRE)
    ax.text(mx1 - 0.6, my0 + 1.0, sp("TOWN-PLAN", 2),
            ha="right", va="bottom", fontsize=5.5, fontname=F_DISPLAY, color=VERDIGRIS)
    ax.text(mx1 - 0.6, my1 - 1.0, sp("PARTNER", 2),
            ha="right", va="top", fontsize=5.5, fontname=F_DISPLAY, color=GRAY)

    # Stage gridlines
    for i, (s, c) in enumerate(zip(stages, scolors)):
        sx = mx0 + i * sw
        ax.plot([sx, sx], [my0, my1], color=GRAY_LIGHT, lw=0.4, ls=(0, (1, 2)))
        ax.text(sx + sw / 2, my0 - 2.0, sp(s, 2),
                fontsize=5.2, fontname=F_MONO, color=c,
                ha="center", va="top")
    ax.plot([mx1, mx1], [my0, my1], color=GRAY_LIGHT, lw=0.4, ls=(0, (1, 2)))

    # Axes
    ax.plot([mx0, mx0], [my0, my1], color=RULE, lw=0.6)
    ax.plot([mx0, mx1], [my0, my0], color=RULE, lw=0.6)
    ax.text(mx0 - 4.5, my1, "USER", fontsize=8, fontname=F_DISPLAY,
            color=INK, ha="right", va="top", rotation=90)
    ax.text(mx0 - 4.5, my0 + 0.5, "FOUNDATION", fontsize=8, fontname=F_DISPLAY,
            color=INK, ha="right", va="bottom", rotation=90)
    ax.text(mx0 + 0.5, my1 + 1.2, sp("VISIBILITY (up)", 2),
            fontsize=5, fontname=F_MONO, color=GRAY, va="bottom")
    ax.text(mx1, my0 - 5.0, sp("EVOLUTION (rightward)", 2),
            fontsize=5, fontname=F_MONO, color=GRAY, ha="right", va="top")

    # ------- Four anchored user needs (at top of map) ----------------
    needs = [
        ("Fill funnel · no headcount scaling",   1.2),
        ("Compress sales cycle · procurement",   2.1),
        ("Increase NRR via CS · expansion",      2.5),
        ("Forecast board trusts (±5%)",          2.8),
    ]
    need_y = 0.96
    for label, sx in needs:
        x = mx0 + sx * sw
        y = my0 + need_y * (my1 - my0)
        ax.add_patch(mpatches.Circle((x, y), 0.7, fc=INK, ec=INK, lw=0))
        ax.text(x + 1.0, y, label, fontsize=4.8, fontname=F_SERIF,
                color=INK, va="center")

    # ------- Components: matrix cells placed by stage and visibility ----
    # (label, x_stage_position 0..4, y_visibility 0..1, color)
    components = [
        # End-user surfaces / functions  ·  high visibility
        ("(10,D) CX resolution", 2.8, 0.88, VERDIGRIS),
        ("MS 365 Copilot · Sales", 2.7, 0.84, VERDIGRIS),
        ("SF Agentforce", 2.6, 0.82, OCHRE),
        ("Glean · cross-system retrieval", 2.5, 0.86, VERDIGRIS),
        ("Hebbia · Rogo (NYC verticals)", 2.0, 0.80, OCHRE),
        ("Sierra · Decagon (CX)", 2.4, 0.78, VERDIGRIS),
        ("Harvey · Hippocratic", 2.1, 0.76, OCHRE),

        # Mid-stack: Common Room, Clay, Pocus
        ("(3,A+L+F) Common Room", 2.0, 0.68, OCHRE),
        ("(4,A) Clay enrichment", 2.4, 0.66, VERDIGRIS),
        ("(8,F) Default · Syft · Truva", 2.2, 0.64, OCHRE),

        # Genesis cells (vermilion) — load-bearing
        ("(9,G) Procurement gauntlet", 0.5, 0.58, VERMILION),
        ("(9,M) Trajectory evidence pack", 0.6, 0.54, VERMILION),
        ("(4,M) SDR trajectory obs.", 0.45, 0.50, VERMILION),
        ("(5,F) BCG dynamic", 0.6, 0.62, VERMILION),
        ("(6,E) Deal-stall causation", 0.7, 0.56, VERMILION),
        ("(11,L) Renewal memory", 0.55, 0.46, VERMILION),
        ("(6,L) AE deal-cycle memory", 0.6, 0.42, VERMILION),
        ("(7,J+M) Procurement-seam coach", 0.4, 0.48, VERMILION),

        # Early Custom (ochre)
        ("(4,K) CU LinkedIn / Sales-Nav", 1.3, 0.52, OCHRE),
        ("(6,K) AE motion GUI driving", 1.4, 0.46, OCHRE),
        ("(11,I) Outcome pricing template", 1.2, 0.44, OCHRE),
        ("(9,I) AI MSA addenda library", 1.3, 0.40, OCHRE),
        ("(8,G) RevOps loop closure", 1.5, 0.50, OCHRE),
        ("(12,L) Forecast-decay memory", 1.2, 0.38, OCHRE),

        # MCP gateways layer
        ("Cloudflare AI Gateway", 2.1, 0.32, VERDIGRIS),
        ("Kong AI Gateway", 2.2, 0.28, VERDIGRIS),
        ("Pomerium · Settle", 1.5, 0.30, OCHRE),

        # Eval / observability
        ("LangSmith · Braintrust · Galileo", 2.8, 0.22, VERDIGRIS),
        ("OTel GenAI", 3.1, 0.18, GRAY),

        # Action / memory / runtime substrate
        ("E2B · Modal · V-Sandbox", 2.9, 0.14, GRAY),
        ("LiveKit · Cartesia · Twilio", 3.0, 0.12, GRAY),
        ("Mem0 · Letta · Zep", 0.8, 0.25, VERMILION),
        ("Anthropic CU · OAI Operator", 0.9, 0.16, VERMILION),
        ("MCP spec", 2.5, 0.10, VERDIGRIS),

        # Foundation (bottom)
        ("Frontier model · agentic cap", 1.8, 0.06, OCHRE),
        ("Open-weight reasoners", 1.4, 0.04, OCHRE),
    ]
    for label, sx, sy, color in components:
        x = mx0 + sx * sw
        y = my0 + sy * (my1 - my0)
        ax.add_patch(mpatches.Circle((x, y), 0.45, fc=color, ec=color, lw=0, alpha=0.9))
        ax.text(x + 0.7, y, label, fontsize=4.3, fontname=F_SERIF,
                color=INK, va="center")

    # Alex's positioning marker (vermilion star) in Pioneer quadrant
    star_x = mx0 + 0.45 * sw
    star_y = my0 + 0.66 * (my1 - my0)
    # Draw a simple star (4-point cross + diagonal)
    ax.plot([star_x - 1.2, star_x + 1.2], [star_y, star_y], color=VERMILION, lw=1.0)
    ax.plot([star_x, star_x], [star_y - 1.2, star_y + 1.2], color=VERMILION, lw=1.0)
    ax.plot([star_x - 0.85, star_x + 0.85], [star_y - 0.85, star_y + 0.85],
            color=VERMILION, lw=0.7)
    ax.plot([star_x - 0.85, star_x + 0.85], [star_y + 0.85, star_y - 0.85],
            color=VERMILION, lw=0.7)
    ax.add_patch(mpatches.Circle((star_x, star_y), 0.35, fc=VERMILION, ec=VERMILION))
    ax.text(star_x + 1.6, star_y + 0.9, "ALEX  ·  Pioneer flag",
            fontsize=4.8, fontname=F_DISPLAY, color=VERMILION, va="center")

    # ------- Six Punctuated Equilibria as vermilion arrows ------------
    # Each PE is an arrow showing direction of movement
    pe_arrows = [
        # (label, x_start_stage, y_visibility, dx, dy)
        ("PE-1 · OSWorld 65% · K-col moves",     1.0, 0.51, 0.55, 0.0),
        ("PE-2 · Article 14 · M-col mandatory",  0.55, 0.49, 0.50, 0.0),
        ("PE-3 · Sierra crosses $500M",          2.7, 0.78, 0.30, 0.0),
        ("PE-4 · MCP gateways to Product",       2.1, 0.30, 0.30, 0.0),
        ("PE-5 · Anthropic ARR resolution",      1.95, 0.06, 0.0, 0.05),
        ("PE-6 · MS Copilot $10B ARR",           2.75, 0.85, 0.25, 0.0),
    ]
    for label, sx, sy, dx, dy in pe_arrows:
        x0 = mx0 + sx * sw
        y0 = my0 + sy * (my1 - my0)
        x1 = mx0 + (sx + dx) * sw
        y1 = my0 + (sy + dy) * (my1 - my0)
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color=VERMILION,
                                    lw=1.0, shrinkA=2, shrinkB=2))
    # ------- PE legend block on right -----------------------
    pe_x = mx1 + 5.0
    pe_y = my1 - 1.5
    ax.text(pe_x, pe_y, sp("PUNCTUATED EQUILIBRIA · 6", 2),
            fontsize=5.2, fontname=F_MONO, color=VERMILION, va="top")
    pe_text = [
        "PE-1 · OSWorld 65% on frontier · Q3 '26",
        "         entire K-column moves Genesis to Custom",
        "PE-2 · Article 14 first enforcement · late '26",
        "         entire M-column flips mandatory",
        "PE-3 · Sierra ARR crosses $500M · mid '27",
        "         outcome-pricing reference set",
        "PE-4 · MCP gateways to Product · H2 '26",
        "         gateway-control-plane consolidates",
        "PE-5 · Anthropic ARR resolution · Q3 '26",
        "         all IX cells vibrate ±20%",
        "PE-6 · MS 365 Copilot $10B ARR · H1 '27",
        "         horizontal suite floor solidifies",
    ]
    for i, line in enumerate(pe_text):
        is_head = not line.startswith("        ")
        ax.text(pe_x, pe_y - 2.4 - i * 1.45, line,
                fontsize=4.5 if is_head else 4.2,
                fontname=F_SERIF if is_head else F_SERIF_IT,
                color=INK if is_head else INK_SOFT, va="top")

    # ------- Footer legend ---------------------------
    leg_y = BOT + 5.0
    ax.plot([L + 1.0, R - 1.0], [leg_y + 1.5, leg_y + 1.5], color=RULE, lw=0.45)
    ax.text(L + 1.0, leg_y + 0.5,
            sp("STRATEGIC QUADRANT  ·  ALEX POSITIONING  ·  PIONEER", 2),
            ha="left", va="top", fontsize=5.0, fontname=F_MONO, color=VERMILION)
    ax.text(L + 1.0, leg_y - 1.5,
            "Pioneer = Genesis cells where Alex publishes flag and earns Process Power + Branding. "
            "Settle = Custom-to-Product cells where Alex rents Power inside a vertical-agent operator role. "
            "Partner = pair-with at the gateway control plane. Town-Plan = rent, do not build.",
            fontsize=4.8, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE VIII  ·  7 POWERS · 30-COMPANY DURABILITY GRID
# ============================================================

def plate_viii(pdf):
    fig, ax = new_page_landscape()
    L, R, TOP, BOT = page_frame_landscape(
        ax, "VIII",
        "Helmer's 7 Powers · 30-Company Durability Screen",
        "Strict Benefit + Barrier discipline. Top-5 most durable in vermilion · "
        "Top-5 most over-rated marked with horizontal slash.",
        "Septem potestates Helmeri · triginta entia · classificatio durabilitatis",
        "PLATE VIII OF X")

    # ----- 30 companies (sub-grouped) -----
    # Each: (id, name, scoring [Scale, Network, C-Pos, Switch, Brand, Corner, Process])
    # Score: 'Y' yes, 'F' forming, 'N' no.  Plus dominant_power line.
    # Top-5 durable flagged (vermilion).  Top-5 over-rated flagged with slash.
    companies = [
        # Sub-group: CX vertical
        ("CX", "Sierra",            ["N", "F", "F", "F", "F", "N", "Y"], "Process Power · outcome-ops scar tissue",       True,  False),
        ("CX", "Decagon",           ["N", "F", "N", "F", "F", "N", "F"], "Process forming · one cycle behind Sierra",      False, False),
        ("CX", "Intercom Fin",      ["F", "N", "N", "Y", "F", "N", "F"], "Switching · install base + $0.99 list",          False, False),
        ("CX", "Ada · Forethought", ["N", "N", "N", "F", "F", "N", "N"], "Brand fading · CCaaS legacy",                    False, True),
        # Sub-group: Knowledge / research
        ("KN", "Glean",             ["N", "Y", "N", "Y", "F", "N", "F"], "Network Economies · org graph + Switching",      True,  False),
        ("KN", "Harvey",            ["N", "N", "N", "Y", "Y", "Y", "Y"], "Three-stack: Corner + Process + Switching",      True,  False),
        ("KN", "Hippocratic AI",    ["N", "N", "F", "Y", "F", "Y", "F"], "Cornered Resource · BAAs + Epic embed",          False, False),
        ("KN", "Abridge",           ["N", "N", "N", "Y", "F", "F", "Y"], "Process Power · Epic clinician workflow",        False, False),
        ("KN", "Hebbia",            ["N", "F", "N", "F", "F", "F", "Y"], "Process Power · FinServ/MBB workflow",           False, False),
        ("KN", "Rogo",              ["N", "F", "N", "F", "F", "F", "F"], "Process forming · banker-fluent eval",           False, False),
        # Sub-group: Sales / RevOps
        ("SR", "Clay",              ["N", "F", "N", "Y", "F", "N", "Y"], "Process + Switching · RevOps orch",              False, False),
        ("SR", "Common Room",       ["N", "F", "N", "F", "F", "N", "F"], "Process forming · PQL signal fusion",            False, False),
        ("SR", "11x",               ["N", "N", "N", "N", "F", "N", "N"], "None · $20M flat · ceiling concession",          False, True),
        ("SR", "Apollo · ZI Copilot", ["F", "F", "N", "F", "F", "F", "F"], "Corner flavor · ZI data inventory",            False, False),
        ("SR", "Outreach / Salesloft", ["F", "N", "N", "Y", "F", "N", "N"], "Switching eroding 8-12%/yr",                  False, True),
        ("SR", "Aircover",          ["N", "N", "N", "N", "N", "N", "F"], "None durable · (6,D) wedge",                     False, False),
        ("SR", "Gong + Chorus",     ["F", "F", "N", "Y", "Y", "F", "Y"], "Process + Switching + Brand · call corpus",      True,  False),
        # Sub-group: Horizontal suite
        ("HZ", "MS 365 Copilot",    ["Y", "Y", "N", "Y", "Y", "Y", "F"], "Four-stack: Scale + Switch + Network + Corner",  True,  False),
        ("HZ", "SF Agentforce",     ["Y", "F", "N", "Y", "Y", "F", "F"], "Scale + Switching + Brand (per-conv retreat)",   False, False),
        ("HZ", "HubSpot Breeze",    ["F", "F", "N", "Y", "Y", "N", "N"], "Switching + Brand · SMB only",                   False, False),
        ("HZ", "ServiceNow AI",     ["Y", "F", "N", "Y", "Y", "N", "F"], "Scale + Switching · ITSM lock-in",               False, False),
        ("HZ", "Notion AI",         ["F", "F", "N", "F", "Y", "N", "N"], "Brand + workspace Switching · 0 GTM",            False, True),
        # Sub-group: Forecasting
        ("FC", "Clari",             ["F", "N", "N", "Y", "F", "N", "F"], "Switching · forecasting embedded RevOps",        False, False),
        ("FC", "BoostUp · Aviso",   ["N", "N", "N", "F", "F", "N", "F"], "Switching shallow · 98% claim disputed",         False, True),
        # Sub-group: Gateway
        ("GW", "Cloudflare AI GW",  ["Y", "F", "F", "Y", "Y", "F", "F"], "Scale + Switching + Brand · edge plumbing",      True,  False),
        ("GW", "Kong AI GW",        ["F", "N", "N", "Y", "F", "N", "F"], "Switching · API-gateway install base",           False, False),
        ("GW", "Pomerium",          ["N", "N", "F", "F", "N", "N", "F"], "Counter-Pos. flavor · zero-trust native",        False, False),
        # Sub-group: Eval / obs
        ("EV", "LangSmith · BTrust · Galileo · Arize", ["N", "F", "N", "F", "F", "N", "F"], "Switching · eval-as-CI · OTel killed ingest", False, False),
        # Sub-group: Memory
        ("ME", "Mem0 · Letta · Zep", ["N", "N", "N", "F", "F", "F", "F"], "Zep niche · Mem0/Letta absorbed",               False, False),
        # Sub-group: CRESTA
        ("CX", "Cresta",            ["N", "N", "N", "F", "N", "N", "F"], "Switching · integration shallow",                False, False),
    ]

    powers = ["Scale", "Network", "C-Pos", "Switch", "Brand", "Corner", "Process"]

    # Layout: name column on left, then 7 powers grid, then verdict text on right
    name_w = 32.0
    grid_left = L + name_w
    verdict_w = 56.0
    grid_right = R - verdict_w
    n_cols = len(powers)
    col_w = (grid_right - grid_left) / n_cols

    grid_top = TOP - 5.0
    grid_bot = BOT + 11.0
    n_rows = len(companies)
    row_h = (grid_top - grid_bot) / n_rows

    # Power column headers
    ax.text(L + 1.0, grid_top + 1.4, sp("COMPANY", 1),
            fontsize=5.4, fontname=F_MONO, color=VERMILION, va="bottom")
    for ci, pw in enumerate(powers):
        cx = grid_left + (ci + 0.5) * col_w
        ax.text(cx, grid_top + 2.4, sp(pw.upper(), 1),
                fontsize=4.6, fontname=F_MONO, color=VERMILION,
                ha="center", va="bottom", rotation=25)
    ax.text(grid_right + 1.0, grid_top + 1.4, sp("DOMINANT POWER  ·  VERDICT", 1),
            fontsize=5.4, fontname=F_MONO, color=VERMILION, va="bottom")
    ax.plot([L + 0.5, R - 0.5], [grid_top, grid_top], color=RULE, lw=0.5)

    # Sub-group color mapping
    sg_color = {"CX": OCHRE, "KN": VERDIGRIS, "SR": VERMILION,
                "HZ": INK_SOFT, "FC": GRAY, "GW": INK, "EV": VERDIGRIS, "ME": OCHRE}
    sg_label = {"CX": "CX vertical", "KN": "knowledge / vertical",
                "SR": "sales · RevOps", "HZ": "horizontal suite",
                "FC": "forecasting", "GW": "gateway",
                "EV": "eval / observability", "ME": "memory"}

    last_sg = None
    for i, (sg, name, marks, verdict, is_top5, is_overrated) in enumerate(companies):
        y_top = grid_top - i * row_h
        y_mid = y_top - row_h / 2
        y_bot = y_top - row_h
        # Sub-group divider when changes
        if sg != last_sg and i > 0:
            ax.plot([L + 0.5, R - 0.5], [y_top, y_top], color=GRAY_LIGHT, lw=0.4)
        last_sg = sg

        # Subgroup color tab on far left
        ax.plot([L + 0.4, L + 0.4], [y_top, y_bot], color=sg_color[sg], lw=1.2)

        # Name (display)
        name_col = VERMILION if is_top5 else INK
        ax.text(L + 1.5, y_mid + 0.3, name, fontsize=6.5,
                fontname=F_DISPLAY, color=name_col, va="center")
        # Sub-group label below name (tiny italic)
        ax.text(L + 1.5, y_mid - 1.6, sg_label[sg],
                fontsize=3.7, fontname=F_SERIF_IT, color=GRAY, va="center")

        # Over-rated slash (horizontal vermilion strike across the name)
        if is_overrated:
            ax.plot([L + 1.3, L + name_w - 1.0], [y_mid + 0.2, y_mid + 0.2],
                    color=VERMILION, lw=0.8, alpha=0.7)

        # Power scoring dots
        for ci, mark in enumerate(marks):
            cx = grid_left + (ci + 0.5) * col_w
            if mark == "Y":
                # filled-ink dot
                fc = VERMILION if is_top5 else INK
                ax.add_patch(mpatches.Circle((cx, y_mid), 0.85,
                                             fc=fc, ec=fc, lw=0))
            elif mark == "F":
                # half-circle (filled half + open half)
                ax.add_patch(mpatches.Wedge((cx, y_mid), 0.85, 90, 270,
                                            fc=INK_SOFT, ec=INK_SOFT, lw=0))
                ax.add_patch(mpatches.Circle((cx, y_mid), 0.85,
                                             fill=False, ec=INK_SOFT, lw=0.45))
            elif mark == "N":
                # empty small dot
                ax.add_patch(mpatches.Circle((cx, y_mid), 0.4,
                                             fill=False, ec=GRAY_LIGHT, lw=0.4))

        # Verdict text (right)
        v_color = VERMILION if is_top5 else INK_SOFT
        ax.text(grid_right + 1.0, y_mid, verdict,
                fontsize=4.5, fontname=F_SERIF if not is_top5 else F_SERIF_IT,
                color=v_color, va="center")

    # Grid bottom rule
    ax.plot([L + 0.5, R - 0.5], [grid_bot, grid_bot], color=RULE, lw=0.5)
    # Vertical grid lines between power columns
    for ci in range(1, n_cols):
        x = grid_left + ci * col_w
        ax.plot([x, x], [grid_top, grid_bot], color=GRAY_LIGHT, lw=0.25)
    # Outer grid box for powers
    ax.add_patch(mpatches.Rectangle((grid_left, grid_bot),
                                    grid_right - grid_left, grid_top - grid_bot,
                                    fill=False, ec=RULE, lw=0.45))

    # ----- Footer legend -----
    leg_y = BOT + 6.5
    ax.plot([L + 1.0, R - 1.0], [leg_y + 1.5, leg_y + 1.5], color=RULE, lw=0.45)
    ax.text(L + 1.0, leg_y + 0.5,
            sp("LEGEND  ·  YES  /  FORMING  /  NO  ·  TOP-5 DURABLE  ·  TOP-5 OVER-RATED", 2),
            ha="left", va="top", fontsize=4.9, fontname=F_MONO, color=VERMILION)
    # Y / F / N samples
    samples = [
        ("Yes · Benefit + Barrier", VERMILION, "Y"),
        ("Forming · one present", INK_SOFT, "F"),
        ("No · neither", GRAY_LIGHT, "N"),
    ]
    for i, (lbl, c, mark) in enumerate(samples):
        x = L + 1.0 + i * 26.0
        y = leg_y - 2.8
        if mark == "Y":
            ax.add_patch(mpatches.Circle((x + 0.7, y), 0.85, fc=c, ec=c, lw=0))
        elif mark == "F":
            ax.add_patch(mpatches.Wedge((x + 0.7, y), 0.85, 90, 270,
                                        fc=c, ec=c, lw=0))
            ax.add_patch(mpatches.Circle((x + 0.7, y), 0.85,
                                         fill=False, ec=c, lw=0.45))
        else:
            ax.add_patch(mpatches.Circle((x + 0.7, y), 0.4,
                                         fill=False, ec=c, lw=0.4))
        ax.text(x + 2.4, y, lbl, fontsize=4.6, fontname=F_SERIF_IT,
                color=INK_SOFT, va="center")

    # Top-5 durable + over-rated marker examples
    x = L + 1.0 + 3 * 26.0
    y = leg_y - 2.8
    ax.text(x, y, "vermilion name = top-5 durable  ·  horizontal slash = top-5 over-rated",
            fontsize=4.6, fontname=F_SERIF_IT, color=INK_SOFT, va="center")

    ax.text(L + 1.0, leg_y - 5.0,
            "Discipline: ARR is not a Power. Brand recall is not a Power. A Power requires Benefit + Barrier. "
            "Six entities clear the strict bar with one or more 'Yes'; another eight carry forming structures.",
            fontsize=4.6, fontname=F_SERIF_IT, color=INK, va="center")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE IX  ·  ECOSYSTEM JTBD · 5 JOBS × 8 PHASES
# ============================================================

def plate_ix(pdf):
    fig, ax = new_page_landscape()
    L, R, TOP, BOT = page_frame_landscape(
        ax, "IX",
        "Ecosystem JTBD · 5 Jobs × 8 Phases",
        "The GTM organization as customer. Each cell carries the matrix coordinate where the agent capability lands, "
        "the compressed outcome, and a 1—10 gap score. High-gap outcomes (7 and above) in vermilion.",
        "Quinque opera quaesita organisationis · phases octo · gradus desiderii N",
        "PLATE IX OF X")

    phases = ["DEFINE", "LOCATE", "PREPARE", "CONFIRM", "EXECUTE", "MONITOR", "MODIFY", "CONCLUDE"]

    # Jobs: (id, name, [phase entries])
    # Each phase entry: (cell_coord, outcome_compressed, gap_int)
    jobs = [
        ("J1", "HIT-THE-NUMBER-NOW", "CRO + VP Sales", [
            ("(12,F)", "Quota gap to action list", 5),
            ("(5,F)",  "F500 committee map (incumbent-bound)", 8),
            ("(6,A)",  "AE walks in w/ MAP context", 6),
            ("(6,E)",  "Stalled deal · causal diagnosis", 9),
            ("(9,G)",  "Procurement-seam in-quarter close", 10),
            ("(6,H)",  "Slipping-stage MTTR", 6),
            ("(6,I)",  "Discount auth · guardrails", 6),
            ("(9,M)",  "Signed evidence pack + hygiene", 7),
        ]),
        ("J2", "HIT-WITHOUT-DOUBLING-HEADS", "CRO + CFO", [
            ("(12,S)", "FY plan w/ AI-lift assumption", 7),
            ("(8,A)",  "Productivity bottleneck locate", 6),
            ("(9,G)",  "Approve to AE-productive compress", 9),
            ("(4,M)",  "AI-lift empirically defensible", 8),
            ("(6,L)",  "AE 6—9mo cycle memory", 9),
            ("(4,H)",  "Augmented cohort underperform", 7),
            ("(7,J+M)","Re-tune capabilities per cohort", 8),
            ("(8,G)",  "Saved hours to pipeline", 7),
        ]),
        ("J3", "CAC PAYBACK <18 MO", "CFO + CRO + Board", [
            ("(12,F)", "CAC decompose · segment × stage", 5),
            ("(1,A)",  "AI-sub candidates per channel", 6),
            ("(11,I)", "Per-seat to outcome blast-radius", 9),
            ("(8,M)",  "Post-substitution unit-economics", 7),
            ("(4,M)",  "Synth-SDR adverse-selection trap", 9),
            ("(1,H)",  "CAC drift detection", 6),
            ("(1,G)",  "Reallocate spend AI vs paid", 6),
            ("(11,L)", "CAC gain holds 4Q", 8),
        ]),
        ("J4", "NRR > 120%", "CCO + CRO", [
            ("(11,H)", "Logo vs expansion vs price", 6),
            ("(11,A)", "Slip-customer signal pre-AE", 8),
            ("(10,E)", "CSM QBR w/ context", 7),
            ("(11,L)", "CSM remembers 9-mo commit", 10),
            ("(11,G)", "Expansion no-slow-renewal", 7),
            ("(10,G)", "At-risk MTTR · usage drop", 7),
            ("(11,I)", "Outcome SLA dispute · keep acct", 8),
            ("(9,I)",  "Multi-year auto-renew clauses", 6),
        ]),
        ("J5", "FORECAST RIGHT (±5%)", "CRO + Board", [
            ("(12,H)", "Commit / upside / best methodology", 6),
            ("(12,F)", "Signal-set across CRM + Gong", 6),
            ("(12,L)", "6Q decay board-explainable", 9),
            ("(6,E)",  "CRM had signal 14d prior", 9),
            ("(12,H)", "MAPE w/o accountability vacuum", 7),
            ("(12,M)", "Forecasting-agent drift detect", 7),
            ("(12,I)", "Re-tune model post-miss", 8),
            ("(12,M)", "Board evidence pack · any Q", 9),
        ]),
    ]

    # Alex-fit jobs: J1, J4, J2 — get a vermilion bracket on the left
    alex_fit_jobs = {"J1", "J4", "J2"}

    # Layout
    job_w = 26.0
    grid_left  = L + job_w
    grid_right = R - 2.0
    grid_top   = TOP - 6.5
    grid_bot   = BOT + 11.0
    n_cols = len(phases)
    n_rows = len(jobs)
    col_w = (grid_right - grid_left) / n_cols
    row_h = (grid_top - grid_bot) / n_rows

    # Phase headers
    for ci, ph in enumerate(phases):
        cx = grid_left + (ci + 0.5) * col_w
        ax.text(cx, grid_top + 2.4, sp(ph, 1),
                fontsize=5.4, fontname=F_MONO, color=VERMILION,
                ha="center", va="bottom")
        # tick down
        ax.plot([cx, cx], [grid_top, grid_top - 0.4],
                color=RULE, lw=0.35)
    ax.text(L + 1.0, grid_top + 2.4, sp("JOB", 1),
            fontsize=5.4, fontname=F_MONO, color=VERMILION, va="bottom")
    ax.plot([L + 0.5, R - 0.5], [grid_top, grid_top], color=RULE, lw=0.5)

    # Job rows
    for ri, (jid, jname, owner, cells) in enumerate(jobs):
        y_top = grid_top - ri * row_h
        y_mid = y_top - row_h / 2
        y_bot = y_top - row_h

        # Bottom rule
        ax.plot([L + 0.5, R - 0.5], [y_bot, y_bot],
                color=GRAY_LIGHT, lw=0.3)

        # Alex-fit bracket (vermilion bracket on far left)
        if jid in alex_fit_jobs:
            bx = L - 1.0
            ax.plot([bx, bx], [y_top - 0.5, y_bot + 0.5],
                    color=VERMILION, lw=1.0)
            ax.plot([bx, bx + 0.8], [y_top - 0.5, y_top - 0.5],
                    color=VERMILION, lw=1.0)
            ax.plot([bx, bx + 0.8], [y_bot + 0.5, y_bot + 0.5],
                    color=VERMILION, lw=1.0)

        # Job label
        job_c = VERMILION if jid in alex_fit_jobs else INK
        ax.text(L + 0.5, y_mid + 0.7, jid,
                fontsize=6.5, fontname=F_DMMONO, color=VERMILION, va="center")
        ax.text(L + 3.5, y_mid + 0.7, jname,
                fontsize=6.4, fontname=F_DISPLAY, color=job_c, va="center")
        ax.text(L + 3.5, y_mid - 1.6, owner,
                fontsize=4.0, fontname=F_SERIF_IT, color=GRAY, va="center")

        # Phase cells
        for ci, (cell_coord, outcome, gap) in enumerate(cells):
            x_left = grid_left + ci * col_w
            # Cell border
            ax.add_patch(mpatches.Rectangle((x_left, y_bot), col_w, row_h,
                                            fill=False, ec=GRAY_LIGHT, lw=0.25))
            # High-gap fill background
            if gap >= 7:
                alpha = 0.08 + (gap - 7) * 0.06   # gap 7..10 → 0.08..0.26
                ax.add_patch(mpatches.Rectangle((x_left + 0.2, y_bot + 0.2),
                                                col_w - 0.4, row_h - 0.4,
                                                fc=VERMILION, ec="none", alpha=alpha))

            # Cell coordinate (top)
            ax.text(x_left + col_w / 2, y_top - 1.0, cell_coord,
                    ha="center", va="top",
                    fontsize=5.0, fontname=F_DMMONO,
                    color=VERMILION if gap >= 7 else INK)
            # Outcome compressed (middle)
            ax.text(x_left + col_w / 2, y_mid + 0.4, outcome,
                    ha="center", va="center",
                    fontsize=3.7, fontname=F_SERIF, color=INK_SOFT,
                    wrap=True)
            # Gap badge (bottom)
            gap_color = VERMILION if gap >= 7 else GRAY
            ax.text(x_left + col_w / 2, y_bot + 1.0, f"gap {gap}",
                    ha="center", va="center",
                    fontsize=4.2, fontname=F_MONO_BOLD, color=gap_color)

    # Grid box
    ax.add_patch(mpatches.Rectangle((grid_left, grid_bot),
                                    grid_right - grid_left, grid_top - grid_bot,
                                    fill=False, ec=RULE, lw=0.45))

    # ----- Footer legend -----
    leg_y = BOT + 7.0
    ax.plot([L + 1.0, R - 1.0], [leg_y + 1.5, leg_y + 1.5], color=RULE, lw=0.45)
    ax.text(L + 1.0, leg_y + 0.5,
            sp("LEGEND  ·  GAP SCORE 1—10  ·  ALEX-FIT JOBS BRACKETED", 2),
            ha="left", va="top", fontsize=5.0, fontname=F_MONO, color=VERMILION)

    ax.text(L + 1.0, leg_y - 1.5,
            "Gap = Ulwick ODI proxy at GTM-org scale (10 = critical unsolved). "
            "Vermilion fills mark gap 7 and above. Alex-fit jobs (1, 4, 2) get a vermilion bracket — "
            "12yr enterprise B2B + procurement scar-tissue lands directly here.",   # gap = N where N is integer
            fontsize=4.7, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    # L-column callout
    ax.text(L + 1.0, leg_y - 5.0,
            sp("L-COLUMN LIGHTS UP AT 3 OF 5 JOBS  ·  M-COLUMN AT 3 CONCLUDES  ·  (9,G) AT JOBS 1 + 2", 2),
            ha="left", va="top", fontsize=4.4, fontname=F_MONO, color=VERMILION)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE X  ·  ACTION PORTFOLIO · 18-MONTH MAP
# ============================================================

def plate_x(pdf):
    fig, ax = new_page_landscape()
    L, R, TOP, BOT = page_frame_landscape(
        ax, "X",
        "Action Portfolio · 18-Month Map · MAY 2026 to NOV 2027",
        "Updated 7 Bets in star-conviction · Gantt of timelines · 6 cruxes as date markers · "
        "10 candidate-bet verdicts (3 promotions · 4 absorptions · 3 parks).",
        "Portfolium actionum · septem electa · sex cruces · decem candidata",
        "PLATE X OF X")

    # ----- TOP REGISTER  ·  Updated 7 Bets w/ stars  -----
    top_band_top = TOP - 5.0
    top_band_bot = TOP - 22.0
    ax.plot([L + 0.5, R - 0.5], [top_band_bot, top_band_bot], color=RULE, lw=0.4)
    ax.text(L + 1.0, top_band_top - 0.5, sp("UPDATED  ·  THE SEVEN BETS  ·  STAR CONVICTION", 2),
            fontsize=5.4, fontname=F_MONO, color=VERMILION, va="top")

    bets = [
        ("1",  "Enterprise AI Procurement Operating Standard", 5, VERMILION,
         "open-spec stewardship  ·  absorbs #4, #5, C2/C3/C4/C10"),
        ("2",  "Vertical Agent GTM Role · NYC",             5, VERMILION,
         "Hebbia > Sierra > Rogo > Harvey > Glean"),
        ("3a", "Advisory + Gateway-Partner pair",            4, OCHRE,
         "Cloudflare / Kong / Pomerium  ·  concurrent w/ Bet #1"),
        ("3b", "Productized MCP server practice",            0, GRAY,
         "parked"),
        ("4",  "FinOps for Tokens · subsumed",               4, OCHRE,
         "Bet #1 §III.8 module"),
        ("5",  "RAG / Memory architecture · subsumed",       4, OCHRE,
         "Bet #1 module · Bet-C9 productization gate Q3'26"),
        ("6",  "Operator Translation Newsletter",            3, VERDIGRIS,
         "distribution layer for #1–#3"),
        ("7",  "VC Operating Partner · fallback",            3, VERDIGRIS,
         "background; primary if #1–#3 stall"),
    ]
    n = len(bets)
    bet_card_w = (R - L - 2.0) / n
    for i, (num, name, stars, color, sub) in enumerate(bets):
        x0 = L + 1.0 + i * bet_card_w
        y0 = top_band_top - 1.5
        # Badge
        ax.add_patch(mpatches.Circle((x0 + 1.4, y0 - 2.0), 1.2,
                                     fc=color, ec=color, lw=0))
        ax.text(x0 + 1.4, y0 - 2.0, num, ha="center", va="center",
                fontsize=6.0, fontname=F_DMMONO, color=PAPER)
        # Stars
        if stars > 0:
            # Filled circles for active stars, open circles for unfilled
            for k in range(5):
                sx = x0 + 3.0 + k * 1.4
                sy = y0 - 1.3
                if k < stars:
                    ax.add_patch(mpatches.Circle((sx, sy), 0.45,
                                                 fc=color, ec=color, lw=0))
                else:
                    ax.add_patch(mpatches.Circle((sx, sy), 0.45,
                                                 fill=False, ec=GRAY_LIGHT, lw=0.45))
        else:
            ax.text(x0 + 3.0, y0 - 1.3, sp("PARK", 1),
                    fontsize=5.0, fontname=F_MONO, color=GRAY, va="center")
        # Name (wrap manually with double-line if long)
        ax.text(x0 + 0.4, y0 - 4.5, name,
                fontsize=5.5, fontname=F_DISPLAY, color=INK,
                va="top", wrap=True)
        # Sub-caption
        ax.text(x0 + 0.4, y0 - 9.5, sub,
                fontsize=3.9, fontname=F_SERIF_IT, color=INK_SOFT,
                va="top", wrap=True)

    # ----- MIDDLE REGISTER  ·  GANTT 18 months  -----
    gantt_top = top_band_bot - 2.0
    gantt_bot = BOT + 26.0
    ax.plot([L + 0.5, R - 0.5], [gantt_top + 1.5, gantt_top + 1.5], color=RULE, lw=0.4)
    ax.text(L + 1.0, gantt_top + 0.5,
            sp("EIGHTEEN-MONTH GANTT  ·  MAY 2026 — NOV 2027", 2),
            fontsize=5.4, fontname=F_MONO, color=VERMILION, va="top")

    # Time axis: 18 months from May 2026 (m=0) to Nov 2027 (m=17)
    # Quarters: Q2'26 (m=0-1) ·  Q3'26 (m=2-4) · Q4'26 (m=5-7) · Q1'27 (m=8-10) · Q2'27 (11-13) · Q3'27 (14-16) · Q4'27 (17)
    timeline_left  = L + 22.0
    timeline_right = R - 38.0   # leave room for candidate-bet column
    n_months = 18
    month_w = (timeline_right - timeline_left) / n_months

    # Month axis below header — month labels at every quarter
    month_labels = [
        ("May'26", 0), ("Q3'26", 3), ("Q4'26", 6),
        ("Q1'27", 9), ("Q2'27", 12), ("Q3'27", 15), ("Q4'27", 17),
    ]
    axis_y = gantt_bot + 1.5
    ax.plot([timeline_left, timeline_right], [axis_y, axis_y], color=RULE, lw=0.45)
    for label, m in month_labels:
        x = timeline_left + m * month_w
        ax.plot([x, x], [axis_y - 0.4, axis_y + 0.4], color=RULE, lw=0.35)
        ax.text(x, axis_y - 1.0, label, ha="center", va="top",
                fontsize=4.4, fontname=F_DMMONO, color=GRAY)

    # Gantt rows (bets that need timelines)
    # (bet_id, label, start_month, end_month, color, style)
    # style: 'solid', 'dashed' (planned ongoing), 'dotted' (background)
    gantt_rows = [
        ("1",  "Bet #1 · Playbook publish",        0, 3, VERMILION, "solid"),
        ("1",  "Bet #1 · 30 expert interviews",    0, 2, VERMILION, "solid"),
        ("1",  "Bet #1 · ongoing maintenance",     3, 17, VERMILION, "dashed"),
        ("2",  "Bet #2 · NYC join window",         2, 7, VERMILION, "solid"),
        ("2",  "Bet #2 · ongoing in role",         7, 17, VERMILION, "dashed"),
        ("3a", "Bet #3a · gateway-partner pair",   2, 8, OCHRE, "solid"),
        ("3a", "Bet #3a · advisory ongoing",       8, 17, OCHRE, "dashed"),
        ("4",  "Bet #4 · module audit pilots",     2, 6, OCHRE, "solid"),
        ("5",  "Bet #5 · Bet-C9 productization gate", 6, 8, OCHRE, "solid"),
        ("5",  "Bet #5 · Bet-C9 build (if go)",    8, 17, OCHRE, "dashed"),
        ("6",  "Bet #6 · newsletter launch",       0, 2, VERDIGRIS, "solid"),
        ("6",  "Bet #6 · cadence ongoing",         2, 17, VERDIGRIS, "dashed"),
        ("7",  "Bet #7 · VC fallback background",  0, 17, GRAY, "dotted"),
    ]
    row_h = (gantt_top - axis_y - 2.0) / len(gantt_rows)
    for i, (bid, label, m0, m1, color, style) in enumerate(gantt_rows):
        y = gantt_top - 1.5 - (i + 0.5) * row_h
        # Label column
        ax.text(L + 1.0, y, label, fontsize=4.5, fontname=F_SERIF, color=INK,
                va="center")
        # Bar
        bar_x = timeline_left + m0 * month_w
        bar_w = (m1 - m0) * month_w
        bar_h = row_h * 0.50
        if style == "solid":
            ax.add_patch(mpatches.Rectangle((bar_x, y - bar_h / 2),
                                            bar_w, bar_h,
                                            fc=color, ec=color, lw=0,
                                            alpha=0.85))
        elif style == "dashed":
            ax.add_patch(mpatches.Rectangle((bar_x, y - bar_h / 2),
                                            bar_w, bar_h,
                                            fc=color, ec="none", alpha=0.30))
            # Add hatch indicator via small ticks
            for tk in np.linspace(bar_x + 0.5, bar_x + bar_w - 0.5, max(2, int(bar_w / 2.5))):
                ax.plot([tk, tk], [y - bar_h / 2, y + bar_h / 2],
                        color=color, lw=0.4, alpha=0.7)
        elif style == "dotted":
            # Series of dots
            for dx in np.linspace(bar_x + 0.5, bar_x + bar_w - 0.5,
                                  max(4, int(bar_w / 1.2))):
                ax.add_patch(mpatches.Circle((dx, y), 0.15,
                                             fc=color, ec=color, lw=0, alpha=0.8))

    # Vertical month gridlines (light)
    for m in range(0, n_months + 1):
        x = timeline_left + m * month_w
        ax.plot([x, x], [axis_y, gantt_top - 1.5], color=GRAY_LIGHT, lw=0.2, alpha=0.6)

    # ----- BOTTOM REGISTER  ·  CRUXES + CANDIDATE BETS  -----
    crux_top = gantt_bot - 1.5
    crux_bot = BOT + 9.5
    ax.plot([L + 0.5, R - 0.5], [crux_top, crux_top], color=RULE, lw=0.4)
    ax.text(L + 1.0, crux_top - 1.0, sp("SIX CRUXES  ·  DECIDABILITY TRIGGERS", 2),
            fontsize=5.4, fontname=F_MONO, color=VERMILION, va="top")

    # Cruxes positioned along timeline by their decidability date.
    # Stagger vertically by row_idx (0/1) to avoid label collision.
    # row_idx column position: alternate to spread legibility.
    cruxes = [
        ("GC1", "OSWorld 65%",         2.5, "Q3 '26 frontier scoreboard event", 0),
        ("GC6", "Common Room 2Q",      2.5, "next 2Q roadmap reveal",           1),
        ("GC2", "Anthropic ARR",       4.0, "Q3 '26 audited or leaked",         0),
        ("GC3", "Article 14 teeth",    6.5, "late '26 first enforcement",       0),
        ("GC5", "Ironclad/Vanta ship", 6.5, "Q4 '26 AI-vendor module",          1),
        ("GC4", "MCP fork",            8.0, "EOY '26 commons vs fork",          0),
    ]
    cy_base = crux_top - 5.0
    row_drop = 3.5
    for cid, label, mpos, sub, row_idx in cruxes:
        x = timeline_left + mpos * month_w
        cy = cy_base - row_idx * row_drop
        # Vertical date marker only on row 0 (skip for row 1 to avoid clutter)
        if row_idx == 0:
            ax.plot([x, x], [crux_top - 2.5, axis_y],
                    color=VERMILION, lw=0.6, ls=(0, (3, 2)), alpha=0.55)
        # Label badge
        ax.add_patch(mpatches.Circle((x, cy), 1.1,
                                     fc=PAPER, ec=VERMILION, lw=0.7))
        ax.text(x, cy, cid, ha="center", va="center",
                fontsize=4.5, fontname=F_MONO_BOLD, color=VERMILION)
        ax.text(x + 1.6, cy + 0.6, label,
                fontsize=4.6, fontname=F_DISPLAY, color=INK,
                va="center")
        ax.text(x + 1.6, cy - 0.9, sub,
                fontsize=3.7, fontname=F_SERIF_IT, color=INK_SOFT, va="center")

    # ----- RIGHT-SIDE MICRO-REGISTER  ·  10 candidate-bet verdicts -----
    cb_x = timeline_right + 4.0
    cb_top = gantt_top - 2.5
    cb_bot = gantt_bot + 2.0
    ax.text(cb_x, cb_top + 0.5, sp("CANDIDATE BETS  ·  10  ·  VERDICTS", 1),
            fontsize=5.0, fontname=F_MONO, color=VERMILION, va="top")
    candidates = [
        ("C1",  "Buying-Committee Graph",          "PARK",     GRAY),
        ("C2",  "Procurement-seam coach",          "ABSORB",   INK),
        ("C3",  "Per-trajectory FinOps audit",     "ABSORB",   INK),
        ("C4",  "Outcome-pricing template",        "ABSORB",   INK),
        ("C5",  "Common Room operator",            "PROMOTE",  VERMILION),
        ("C6",  "Procurement std as open spec",    "PROMOTE",  VERMILION),
        ("C7",  "RevOps trajectory agent",         "WATCH",    GRAY),
        ("C8",  "Deal-diagnosis causation",        "WATCH",    GRAY),
        ("C9",  "Memory as Service Line",          "PROMOTE",  VERMILION),
        ("C10", "Article 14 Tie-Out std",          "ABSORB",   INK),
    ]
    cb_row_h = (cb_top - cb_bot) / len(candidates)
    for i, (cid, name, verdict, color) in enumerate(candidates):
        y = cb_top - 1.5 - (i + 0.5) * cb_row_h
        ax.text(cb_x, y, cid,
                fontsize=4.4, fontname=F_DMMONO, color=VERMILION, va="center")
        ax.text(cb_x + 3.5, y + 0.3, name,
                fontsize=4.6, fontname=F_DISPLAY, color=INK, va="center")
        # Verdict badge
        v_alpha = 1.0 if color == VERMILION else (0.85 if color == INK else 0.55)
        ax.text(cb_x + 28.0, y, verdict,
                fontsize=4.8, fontname=F_MONO_BOLD, color=color, alpha=v_alpha,
                va="center", ha="right")

    # Counts footer
    ax.text(cb_x, cb_bot - 0.5,
            "3 promotions  ·  4 absorptions  ·  3 parks / watch",
            fontsize=4.5, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    # ----- FOOTER LEGEND -----
    leg_y = BOT + 5.5
    ax.plot([L + 1.0, R - 1.0], [leg_y + 1.5, leg_y + 1.5], color=RULE, lw=0.45)
    ax.text(L + 1.0, leg_y + 0.5,
            sp("OPERATING PLAN  ·  PUBLISH (#1)  ·  RENT EQUITY (#2)  ·  COMPOUND (#3a)  ·  DISTRIBUTE (#6)  ·  FALLBACK (#7)", 2),
            ha="left", va="top", fontsize=4.8, fontname=F_MONO, color=VERMILION)
    ax.text(L + 1.0, leg_y - 1.5,
            "Solid bars = active build window. Hatched = ongoing maintenance / role continuity. Dotted = background. "
            "Cruxes are decidability triggers: a 'wrong' answer at any one re-ranks the portfolio.",
            fontsize=4.6, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# BUILD
# ============================================================

if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        plate_vi(pdf)
        plate_vii(pdf)
        plate_viii(pdf)
        plate_ix(pdf)
        plate_x(pdf)
    sz_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"Wrote {OUT_PATH}  ·  {sz_kb:.1f} KB")
