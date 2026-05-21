"""
SUBSTRATE  ·  Vol IV  ·  Master Plate (Plate M)  —  Agents GTM synthesis.

A single tabloid plate that mirrors Volume III's Master Plate construction:
- the cell matrix as a small heat-map inset (no labels — just the intensity)
- the seven-counterparty buyer-side gauntlet as a horizontal register
- the Updated Seven Bets list with star-conviction marks
- the Five Cruxes with date triggers
- the Hebbia / Sierra / Rogo NYC operator ranking, vermilion on Hebbia
- one italic-serif framing line — the field-narrative-lag thesis
"""
# plate-fonts-scaled-v1
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.path import Path
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
import numpy as np

FONT_DIR = "/Users/sameoldexpressions/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/f85326cc-c479-4349-956a-d3d47e404d0b/d1370235-0ed8-47e6-859d-0bec833074a3/skills/canvas-design/canvas-fonts"
if os.path.isdir(FONT_DIR):
    for fp in os.listdir(FONT_DIR):
        if fp.endswith((".ttf", ".otf")):
            fm.fontManager.addfont(os.path.join(FONT_DIR, fp))


def fam(filename):
    path = os.path.join(FONT_DIR, filename)
    if os.path.isfile(path):
        return fm.FontProperties(fname=path).get_name()
    # Fallback if font missing
    return "DejaVu Sans"


F_DISPLAY      = fam("BigShoulders-Bold.ttf")
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

PAGE_W, PAGE_H = 15.4, 23.8
DPI = 300
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm/AGENTS_GTM_MASTER_PLATE.pdf"


def sp(text, n=1):
    if n <= 0:
        return text
    sep = " " * n
    out = []
    for ch in text:
        if out:
            out.append(sep)
        out.append(ch)
    return "".join(out)


def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 154.5)
    ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax):
    LEFT, RIGHT = 6.0, 94.0
    TOP, BOTTOM = 149.5, 7.5
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT,
                                    TOP - BOTTOM, fill=False, ec=RULE, lw=0.55))
    ax.plot([LEFT, RIGHT], [TOP - 7.5, TOP - 7.5], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 5.0, BOTTOM + 5.0], color=RULE, lw=0.45)
    # Margin tick rule (geologist's column)
    ax.plot([LEFT - 2.6, LEFT - 2.6], [BOTTOM + 5.0, TOP - 7.5],
            color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 5.0, TOP - 7.5, 28)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([LEFT - 2.6 - (1.0 if long else 0.5), LEFT - 2.6],
                [y, y], color=RULE, lw=0.35)
        if long:
            ax.text(LEFT - 4.1, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=10, fontname=F_DMMONO, color=GRAY)

    # Title block
    ax.text(LEFT, TOP - 1.4,
            sp("AN ATLAS OF THE AGENT STRATA  ·  VOLUME IV  ·  MASTER SECTION", 4),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 2.6, "AGENTS GTM, SEEN WHOLE",
            ha="left", va="top", fontsize=26.4, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.4, TOP - 2.8, sp("MASTER PLATE", 2),
            ha="right", va="top", fontsize=10, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4,
            "The 12 × 13 cell field condensed · the seven-counterparty gauntlet · the seven Bets sequenced · the five Cruxes that re-rank everything.",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 6.5,
            "Mercatura agenticum tota machina  ·  ubi opus emat  ·  ubi opus laboret",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # Master plate badge — letter M in vermilion ring
    ax.add_patch(mpatches.Circle((RIGHT - 1.6, TOP - 2.6), 1.1,
                                 fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 1.6, TOP - 2.6, "M", ha="center", va="center",
            fontsize=10, fontname=F_MONO_BOLD, color=VERMILION)

    # Footer
    ax.text(LEFT, BOTTOM + 3.0,
            sp("SUBSTRATE  ·  VOL IV  ·  AGENTS GTM  ·  MASTER PLATE", 3),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.4,
            sp("Compiled for A. Yedi  ·  Cycle MMXXVI  ·  May  ·  Rev. I", 2),
            ha="left", va="top", fontsize=10, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, sp("MMXXVI · V", 2),
            ha="right", va="top", fontsize=10, fontname=F_DMMONO, color=GRAY)

    return LEFT, RIGHT, TOP - 7.5, BOTTOM + 5.0


# ------- The Top-15 cells (for inset rendering) -----------------------
TOP15_CELLS = {
    (9, "G"): 19, (5, "F"): 18, (6, "E"): 17, (4, "A"): 16, (6, "L"): 16,
    (9, "I"): 16, (8, "G"): 15, (4, "K"): 15, (12, "F"): 15, (12, "H"): 15,
    (4, "M"): 14, (9, "M"): 14, (11, "L"): 14, (3, "A"): 14, (6, "K"): 14,
}

# Tier-2 mid-density cells (for context in inset)
MID_CELLS = {
    (1, "A"): 11, (1, "K"): 13, (1, "M"): 14, (2, "G"): 9, (2, "K"): 13,
    (2, "M"): 12, (3, "G"): 11, (4, "B"): 10, (4, "C"): 11, (4, "D"): 12,
    (4, "E"): 13, (4, "F"): 14, (4, "G"): 9, (4, "H"): 11, (4, "J"): 11,
    (4, "L"): 12, (5, "A"): 12, (5, "B"): 9, (5, "C"): 10, (5, "D"): 9,
    (5, "E"): 11, (5, "G"): 8, (5, "H"): 9, (5, "K"): 9, (5, "L"): 13,
    (5, "M"): 11, (6, "A"): 14, (6, "B"): 12, (6, "C"): 9, (6, "D"): 13,
    (6, "F"): 11, (6, "G"): 8, (6, "H"): 12, (6, "I"): 13, (6, "J"): 12,
    (6, "M"): 13, (7, "G"): 11, (7, "J"): 13, (7, "K"): 9, (7, "M"): 13,
    (8, "A"): 7, (8, "F"): 11, (8, "H"): 10, (8, "K"): 12, (8, "L"): 7,
    (8, "M"): 12, (9, "A"): 9, (9, "B"): 8, (9, "K"): 13, (9, "L"): 10,
    (10, "A"): 8, (10, "B"): 8, (10, "C"): 9, (10, "D"): 14, (10, "E"): 12,
    (10, "F"): 11, (10, "G"): 13, (10, "K"): 10, (10, "L"): 11, (10, "M"): 12,
    (11, "A"): 10, (11, "B"): 9, (11, "E"): 11, (11, "G"): 13, (11, "H"): 12,
    (11, "I"): 13, (11, "K"): 9, (11, "M"): 11, (12, "A"): 8, (12, "B"): 8,
    (12, "C"): 9, (12, "D"): 14, (12, "G"): 10, (12, "I"): 8, (12, "J"): 9,
    (12, "K"): 11, (12, "L"): 13, (12, "M"): 10,
}


def render_master(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax)

    # ---- Layout zones --------------------------------------------------
    # Three rough horizontal bands beneath the heat-map inset
    inset_top    = TOP - 1.5
    inset_bot    = TOP - 28
    inset_left   = L + 1.0
    inset_right  = L + 38

    # The thesis paragraph (italic serif) sits to the right of the inset
    thesis_x0 = inset_right + 3
    thesis_x1 = R - 1.0
    thesis_y_top = inset_top - 1.0

    # ---- (A) The cell-matrix heat-map inset ----------------------------
    n_rows, n_cols = 12, 13
    cell_w = (inset_right - inset_left) / n_cols
    cell_h = (inset_top - inset_bot) / n_rows
    caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]

    # Title above the inset
    ax.text(inset_left, inset_top + 0.5,
            sp("12 X 13 CELL FIELD  ·  HEAT INTENSITY = OCQ", 1),
            ha="left", va="bottom",
            fontsize=10, fontname=F_MONO, color=VERMILION)

    # Outline
    ax.add_patch(mpatches.Rectangle((inset_left, inset_bot),
                                     inset_right - inset_left,
                                     inset_top - inset_bot,
                                     fill=False, ec=RULE, lw=0.45))

    for ri in range(n_rows):
        f_num = ri + 1
        y_top = inset_top - ri * cell_h
        y_bot = y_top - cell_h
        for ci in range(n_cols):
            c_let = caps[ci]
            x0 = inset_left + ci * cell_w
            x1 = x0 + cell_w
            ax.add_patch(mpatches.Rectangle((x0, y_bot), cell_w, cell_h,
                                             fill=False, ec=GRAY_LIGHT, lw=0.18))
            if (f_num, c_let) in TOP15_CELLS:
                ocq = TOP15_CELLS[(f_num, c_let)]
                s = (ocq - 13) / 6.0
                a = max(0.55, min(1.0, 0.55 + 0.45 * s))
                ax.add_patch(mpatches.Rectangle((x0 + 0.05, y_bot + 0.05),
                                                 cell_w - 0.1, cell_h - 0.1,
                                                 fc=VERMILION, ec=VERMILION,
                                                 lw=0.3, alpha=a))
            elif (f_num, c_let) in MID_CELLS:
                ocq = MID_CELLS[(f_num, c_let)]
                s = (ocq - 6) / 9.0
                a = max(0.10, min(0.55, 0.10 + 0.45 * s))
                ax.add_patch(mpatches.Rectangle((x0 + 0.05, y_bot + 0.05),
                                                 cell_w - 0.1, cell_h - 0.1,
                                                 fc=INK, ec="none", alpha=a))

    # Inset annotations: top capability labels and side function numbers
    for ci, lt in enumerate(caps):
        cx = inset_left + ci * cell_w + cell_w / 2
        ax.text(cx, inset_top + 0.05 - 0.1, lt,
                ha="center", va="bottom",
                fontsize=10, fontname=F_DMMONO, color=GRAY)
    for ri in range(n_rows):
        cy = inset_top - ri * cell_h - cell_h / 2
        ax.text(inset_left - 0.4, cy, str(ri + 1),
                ha="right", va="center",
                fontsize=10, fontname=F_DMMONO, color=GRAY)

    # Inset caption
    ax.text(inset_left, inset_bot - 0.5,
            "Vermilion = the fifteen highest-OCQ cells. Ink density = mid-tier "
            "scored cells.\nFull-resolution version on Plate I of I.",
            ha="left", va="top",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)
    ax.plot([inset_left, inset_right], [inset_bot - 3.0, inset_bot - 3.0],
            color=GRAY_LIGHT, lw=0.3)

    # ---- (B) Field-narrative-lag thesis (italic serif) -----------------
    ax.text(thesis_x0, thesis_y_top,
            sp("THE FIELD-NARRATIVE LAG", 2),
            ha="left", va="top",
            fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.plot([thesis_x0, thesis_x1], [thesis_y_top - 1.0, thesis_y_top - 1.0],
            color=RULE, lw=0.35)

    thesis_lines = [
        "The agent-GTM map of May 2026 is a field whose narrative still lags its facts. The",
        "vendors that headline the press cycle — synthetic-SDR, autonomous AE, agentic for-",
        "ecasting — sit in the matrix's vapour quadrants: high vendor-noise, low completion,",
        "negative net-revenue. The cells that carry actual durability — procurement-seam",
        "evidence packs, buying-committee graphs, deal-causation engines, persistent",
        "memory across multi-quarter cycles — are quiet, regulatorily forced, and largely",
        "unclaimed by name. The Top-15 above is the working list of where the decade's real",
        "agent-GTM equity will accrue. The Bets to the right are the operator's response.",
        "",
        "Three structural truths anchor the page. First, the procurement seam is load-",
        "bearing: cell (9, G) at OCQ 19 is the cell of record, and seven counterparties at",
        "F1000 — InfoSec, Legal, Privacy, AI Governance, Procurement, Sponsor, Enterprise",
        "Architecture — must each be answered before any agent ships. Second, the L and",
        "M columns (memory and trajectory observability) are the matrix's most consistent",
        "gaps; they are where standalone craft survives the foundation-lab walk-up. Third,",
        "the K column (computer-use) is gated almost entirely on a single capability crux —",
        "OSWorld 65 percent — that flips a dozen cells inside one quarter. Sequencing matters.",
    ]
    for i, line in enumerate(thesis_lines):
        ax.text(thesis_x0, thesis_y_top - 2.6 - i * 1.35, line,
                ha="left", va="top",
                fontsize=10, fontname=F_SERIF_IT if i < 8 else F_SERIF, color=INK)

    # ---- (C) The Seven-Counterparty Gauntlet ----------------------------
    g_top = inset_bot - 5.5
    g_bot = g_top - 22
    ax.plot([L + 1, R - 1], [g_top + 1.3, g_top + 1.3], color=RULE, lw=0.45)
    ax.text(L + 1, g_top,
            sp("THE SEVEN-COUNTERPARTY GAUNTLET  ·  F1000 BUYER-SIDE", 3),
            ha="left", va="top",
            fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.text(L + 1, g_top - 1.5,
            "Seven approver chairs in the F1000 procurement room. Each rejects on a different vector. "
            "An agent that does not pre-answer all seven does not ship.",
            ha="left", va="top",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    counterparties = [
        ("01", "INFOSEC",
         "CISO / GRC",
         "Show me your indirect-prompt-injection defense — adaptive red-team, refresh cadence.",
         "10 — 20 wks"),
        ("02", "LEGAL",
         "GC + AI Counsel",
         "Hallucination liability, output-ownership, model-change notice, foundation-model passthrough.",
         "8 — 16 wks"),
        ("03", "PRIVACY",
         "CPO / DPO",
         "Surgical deletion across persistent memory, trajectory logs, and any fine-tuned weights.",
         "6 — 12 wks"),
        ("04", "AI GOVERNANCE",
         "AI Council / CAO",
         "Signed reproducible eval. NIST AI RMF map. Article 14 oversight design. FRIA template.",
         "8 — 16 wks"),
        ("05", "PROCUREMENT",
         "CPO + AI Cat Mgr",
         "Pricing benchmarkable; per-trajectory ceiling; viability through shakeout; exit story.",
         "10 — 24 wks"),
        ("06", "SPONSOR",
         "CRO / CMO / VP CS",
         "Will it hit my number; how fast to value; operator-translation layer to the line manager.",
         "2 — 6 wks"),
        ("07", "ENTERPRISE ARCH",
         "CIO / Chief Arch",
         "OAuth blast radius; reference-architecture conformity; on-call runbook; capacity at 10⁵.",
         "6 — 12 wks"),
    ]
    n = len(counterparties)
    avail = (g_top - 3) - g_bot
    rh = avail / n

    for i, (nm, name, who, q, cycle) in enumerate(counterparties):
        y_top = g_top - 3 - i * rh
        y_bot = y_top - rh
        y_mid = (y_top + y_bot) / 2
        ax.plot([L + 1, R - 1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.3)
        # Number badge
        ax.add_patch(mpatches.Circle((L + 2.0, y_mid), 0.95,
                                      fc=PAPER, ec=VERMILION, lw=0.5))
        ax.text(L + 2.0, y_mid, nm, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=VERMILION)
        # Name (display caps)
        ax.text(L + 4.0, y_mid + 0.7, name, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        # Who (italic serif)
        ax.text(L + 4.0, y_mid - 1.0, who, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=GRAY)
        # Question (serif body)
        ax.text(L + 22, y_mid + 0.15, q, ha="left", va="center",
                fontsize=10, fontname=F_SERIF, color=INK_SOFT)
        # Cycle window
        ax.text(R - 2, y_mid + 0.15, cycle, ha="right", va="center",
                fontsize=10, fontname=F_DMMONO, color=VERDIGRIS)

    # ---- (D) The Seven Updated Bets ------------------------------------
    bets_top = g_bot - 4
    bets_bot = bets_top - 32
    ax.plot([L + 1, R - 1], [bets_top + 1.3, bets_top + 1.3],
            color=RULE, lw=0.45)
    ax.text(L + 1, bets_top,
            sp("THE SEVEN BETS  ·  SEQUENCED  ·  CONVICTION /5", 3),
            ha="left", va="top",
            fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.text(L + 1, bets_top - 1.5,
            "Bet 1 first (claim Process Power) · Bet 2 second (collect equity at a power-holder) · Bet 3 third (compound advisory). "
            "Bets 4–5 fold as Bet 1 modules; Bet 6 is the distribution layer; Bet 7 the long-arc fallback.",
            ha="left", va="top",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    bets = [
        ("1", "PROCUREMENT OPERATING STANDARD", 5, VERMILION,
         "Open Playbook + 30 expert calls + Agent Procurement Rubric · the unclaimed flag at (9, G) OCQ 19"),
        ("2", "VERTICAL AGENT GTM ROLE", 5, VERMILION,
         "Hebbia / Sierra / Rogo NYC anchors · MBB feed-stock activated Feb-Apr 2026 · Q2-Q3 equity window"),
        ("3", "GATEWAY-ADJACENT ADVISORY", 4, OCHRE,
         "Cloudflare AI Gateway primary · Kong / Pomerium secondary · pair-with positioning, not productized servers"),
        ("4", "FINOPS FOR TRAJECTORIES (FOLD)", 4, OCHRE,
         "Per-trajectory FinOps audit · 12-mo window before AWS Bedrock auto-routing bundles · Bet 1 module"),
        ("5", "PERSISTENT MEMORY ARCHITECTURE", 4, OCHRE,
         "L-column anchored: (6, L), (11, L), (12, L) · vendor-neutral architecture audit · Crux 5 dependent"),
        ("6", "OPERATOR TRANSLATION NEWSLETTER", 3, VERDIGRIS,
         "JTBD Job 5 distribution layer · Conclude-phase translation · cross-pollinate Bet 1 downloads"),
        ("7", "VC OPERATING PARTNER", 3, VERDIGRIS,
         "RAAIS / Betaworks / MAD background · principal-to-operator path · primary if Bets 1–3 stall"),
    ]
    nb = len(bets)
    bets_avail = (bets_top - 3.5) - bets_bot
    bh = bets_avail / nb
    for i, (num, name, stars, color, det) in enumerate(bets):
        y_top = bets_top - 3.5 - i * bh
        y_mid = y_top - bh / 2
        ax.plot([L + 1, R - 1], [y_top - bh, y_top - bh],
                color=GRAY_LIGHT, lw=0.3)
        # Bet number (filled circle)
        ax.add_patch(mpatches.Circle((L + 2.0, y_mid + 0.4), 1.1,
                                      fc=color, ec=color, lw=0))
        ax.text(L + 2.0, y_mid + 0.4, num, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=PAPER)
        # Name (display caps)
        ax.text(L + 4.5, y_mid + 1.1, name, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        # Stars: filled / hollow circles
        sx0 = L + 4.5
        for k in range(5):
            cx = sx0 + k * 1.4
            cy = y_mid - 0.8
            if k < stars:
                ax.add_patch(mpatches.Circle((cx, cy), 0.45,
                                             fc=color, ec=color, lw=0))
            else:
                ax.add_patch(mpatches.Circle((cx, cy), 0.45,
                                             fc="none", ec=color, lw=0.4))
        ax.text(sx0 + 7.5, cy, f"{stars}/5",
                ha="left", va="center",
                fontsize=10, fontname=F_DMMONO, color=color)
        # Detail (italic serif)
        ax.text(L + 22, y_mid + 0.4, det, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    # ---- (E) NYC Operator Ranking ---------------------------------------
    ny_top = bets_bot - 4
    ny_bot = ny_top - 12.5
    ax.plot([L + 1, R - 1], [ny_top + 1.3, ny_top + 1.3], color=RULE, lw=0.45)
    ax.text(L + 1, ny_top,
            sp("NYC VERTICAL-AGENT OPERATOR RANKING  ·  ALEX-FIT", 3),
            ha="left", va="top",
            fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.text(L + 1, ny_top - 1.5,
            "Composite of equity asymmetry × power-rent × NYC anchor × Alex profile fit. F4 + F2 agree.",
            ha="left", va="top",
            fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    nyc = [
        ("01", "HEBBIA",  "0.20-0.40% · $250-350K · Mehta + MBB anchor · 2-quarter window",
         "FinServ + MBB · NYC HQ · under-funded ratio 2.5-5% · highest equity asymmetry", VERMILION),
        ("02", "SIERRA",  "0.10-0.25% · $300-400K · Schmidt + Taylor monthly NYC",
         "Process Power on outcome pricing · brand-prestige + cleanest secondary-liquidity", INK_SOFT),
        ("03", "ROGO",    "0.30-0.60% · $250-350K · Tekriwal + banker-fluent gate",
         "Banker copilot · NYC HQ · most equity room of NYC named set", INK_SOFT),
    ]
    nh = (ny_top - 3) - ny_bot
    rh2 = nh / 3 - 0.2
    for i, (rank, name, terms, why, color) in enumerate(nyc):
        y_top = ny_top - 3 - i * (rh2 + 0.2)
        y_mid = y_top - rh2 / 2
        ax.plot([L + 1, R - 1], [y_top - rh2, y_top - rh2],
                color=GRAY_LIGHT, lw=0.3)
        # Rank badge
        ax.add_patch(mpatches.Circle((L + 2.0, y_mid), 1.1,
                                      fc=color, ec=color, lw=0))
        ax.text(L + 2.0, y_mid, rank, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=PAPER)
        # Name caps
        ax.text(L + 4.5, y_mid + 0.9, name, ha="left", va="center",
                fontsize=10.2, fontname=F_DISPLAY, color=color)
        # Terms (mono)
        ax.text(L + 4.5, y_mid - 1.1, terms, ha="left", va="center",
                fontsize=10, fontname=F_DMMONO, color=GRAY)
        # Why (serif italic)
        ax.text(L + 35, y_mid + 0.0, why, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    # ---- (F) The Five Cruxes (bottom strip) ----------------------------
    cy_top = ny_bot - 4
    ax.plot([L + 1, R - 1], [cy_top + 1.3, cy_top + 1.3],
            color=RULE, lw=0.45)
    ax.text(L + 1, cy_top,
            sp("FIVE CRUXES  ·  ANSWER-EVENTS THAT RE-RANK THE MATRIX", 2),
            ha="left", va="top",
            fontsize=10, fontname=F_MONO, color=VERMILION)

    cruxes = [
        ("C1", "ANTHROPIC ARR",
         "$24B vs $30B · Q3 '26",
         "vertical-agent valuation · equity windows compress 20-30% on lower"),
        ("C2", "MCP COMMONS",
         "holds vs silent fork · EOY '26",
         "gateway TAM · Cloudflare / Kong upside if forks; ecosystem if holds"),
        ("C3", "OSWORLD 65%",
         "frontier crosses · Q3 '26",
         "K-column unlocks · Microsoft Sales Copilot wins by default"),
        ("C4", "EU ART. 14 TEETH",
         "enforcement · late '26",
         "Bet 1 TAM 5x range · paper-tiger collapses Bet 1 productized branch"),
        ("C5", "STANDALONE MEMORY",
         "absorbed vs niche · H2 '26",
         "L-column shape · Bet 5 is anchor; Crux already trending niche-only"),
    ]
    cyy = cy_top - 3
    for i, (k, name, when, why) in enumerate(cruxes):
        # 5 across
        x0 = L + 1 + i * ((R - L - 2) / 5)
        # Big circle with crux number
        ax.add_patch(mpatches.Circle((x0 + 1.4, cyy), 1.2,
                                      fc=VERMILION, ec=VERMILION, lw=0))
        ax.text(x0 + 1.4, cyy, k, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=PAPER)
        # Name caps
        ax.text(x0 + 3.3, cyy + 0.9, name, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        # When (mono)
        ax.text(x0 + 3.3, cyy - 0.4, when, ha="left", va="center",
                fontsize=10, fontname=F_DMMONO, color=VERDIGRIS)
        # Why
        ax.text(x0 + 3.3, cyy - 1.6, why, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        render_master(pdf)
    sz_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"Wrote {OUT_PATH}  ·  {sz_kb:.1f} KB")
