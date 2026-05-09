"""
SUBSTRATE — Volume II
Plates VII-XI: OCQ heat map, Wardley map, 7 Powers grid, JTBD canvas, Action portfolio.
Same aesthetic as the original 6 plates.
"""
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
import numpy as np

# ---------- Fonts ----------
FONT_DIR = "/Users/sameoldexpressions/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/f85326cc-c479-4349-956a-d3d47e404d0b/d1370235-0ed8-47e6-859d-0bec833074a3/skills/canvas-design/canvas-fonts"
for fp in os.listdir(FONT_DIR):
    if fp.endswith((".ttf", ".otf")):
        fm.fontManager.addfont(os.path.join(FONT_DIR, fp))

def fam(filename):
    return fm.FontProperties(fname=os.path.join(FONT_DIR, filename)).get_name()

F_DISPLAY = fam("BigShoulders-Bold.ttf")
F_DISPLAY_REG = fam("BigShoulders-Regular.ttf")
F_SERIF = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT = fam("InstrumentSerif-Italic.ttf")
F_MONO = fam("GeistMono-Regular.ttf")
F_MONO_BOLD = fam("GeistMono-Bold.ttf")
F_DMMONO = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42

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

# ---------- Palette (matches Vol I) ----------
PAPER = "#F1E9D6"
INK = "#171210"
INK_SOFT = "#3A2F26"
GRAY = "#7A6E60"
GRAY_LIGHT = "#C9BFA9"
RULE = "#2A211B"
VERMILION = "#A6371F"
VERDIGRIS = "#456C5C"
OCHRE = "#A37425"

PAGE_W, PAGE_H = 11.0, 17.0
DPI = 300

OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-stack/AI_STACK_SUBSTRATE_VOL2.pdf"


def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 154.5)
    ax.set_facecolor(PAPER)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax, plate_no, title_top, subtitle_top, latin, plate_label):
    LEFT = 8.5; RIGHT = 92.5; TOP = 148.5; BOTTOM = 9.5
    rect = mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                              fill=False, ec=RULE, lw=0.55)
    ax.add_patch(rect)
    ax.plot([LEFT, RIGHT], [TOP - 6.0, TOP - 6.0], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 4.5, BOTTOM + 4.5], color=RULE, lw=0.45)

    # Depth scale
    ax.plot([LEFT - 2.6, LEFT - 2.6], [BOTTOM + 4.5, TOP - 6.0], color=RULE, lw=0.4)
    n_ticks = 28
    ys = np.linspace(BOTTOM + 4.5, TOP - 6.0, n_ticks)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([LEFT - 2.6 - (1.0 if long else 0.5), LEFT - 2.6], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(LEFT - 4.1, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=4.4, fontname=F_DMMONO, color=GRAY)

    # Title
    ax.text(LEFT, TOP - 1.0, sp("AN ATLAS OF THE INTELLIGENCE STRATA  ·  VOLUME II", 4),
            ha="left", va="top", fontsize=6.0, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 1.9, title_top.upper(),
            ha="left", va="top", fontsize=18, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.0, TOP - 2.0, sp(plate_label, 2),
            ha="right", va="top", fontsize=7.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 4.5, subtitle_top,
            ha="left", va="top", fontsize=6.2, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4, latin,
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)

    # Plate badge
    ax.add_patch(mpatches.Circle((RIGHT - 1.4, TOP - 2.0), 1.05, fill=False, ec=VERMILION, lw=0.6))
    ax.text(RIGHT - 1.4, TOP - 2.0, plate_no, ha="center", va="center",
            fontsize=6.2, fontname=F_MONO_BOLD, color=VERMILION)

    # Footer
    ax.text(LEFT, BOTTOM + 3.0, sp("SUBSTRATE  ·  VOLUME II  ·  DECISIONS PLAYBOOK", 3),
            ha="left", va="top", fontsize=4.6, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.4, sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, plate_label, ha="right", va="top",
            fontsize=5.4, fontname=F_DMMONO, color=GRAY)

    return LEFT, RIGHT, TOP - 6.5, BOTTOM + 4.7


# ============================================================
# PLATE VII — OCQ HEAT MAP
# ============================================================

def plate_vii_ocq_heat(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "VII", "The OCQ Heat Map",
        "Eighteen strata × three lenses · scored opportunity, challenge, open question.",
        "Stratum × instrumentum analyticum — convergence of conviction across the column",
        "PLATE VII OF XI")
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Strata data — ordered top (high) to bottom (low) like SUBSTRATE original
    strata = [
        ("XIV",  "USER",                   [12, 13, 11], [10, 9],   [13, 12]),
        ("XIII", "APPLICATION · AGENT",    [15, 15, 13], [11, 11],  [13, 12]),
        ("XII",  "ORCHESTRATION",          [15, 14, 13], [12, 10],  [14, 11]),
        ("XI",   "RETRIEVAL · MEMORY",     [15, 13, 11], [11, 10],  [15, 12]),
        ("X",    "INFERENCE",              [15, 13, 11], [12, 11],  [12, 13]),
        ("IX",   "MODEL · PROVIDERS",      [15, 13, 15], [13, 12],  [14, 13]),
        ("VIII", "POST-TRAINING",          [12, 13, 13], [10, 12],  [13, 13]),
        ("VII",  "PRE-TRAINING",           [12, 11, 12], [12, 9],   [11, 11]),
        ("VI",   "DATA · CORPUS",          [15, 12, 11], [10, 10],  [13, 13]),
        ("V",    "PARALLELISM",            [13, 15, 13], [11, 10],  [14, 14]),
        ("IV",   "FABRIC",                 [13, 10, 10], [12, 9],   [12, 9]),
        ("III",  "COMPUTE",                [13, 13, 11], [14, 13],  [14, 13]),
        ("II",   "FACILITY",               [15, 15, 11], [11, 10],  [11, 9]),
        ("I",    "POWER",                  [13, 12, 11], [13, 11],  [11, 12]),
        ("M-A",  "SAFETY · ALIGNMENT",     [12, 9, 11],  [11, 10],  [10, 13]),
        ("M-B",  "REGULATION",             [15, 13, 13], [12, 10],  [15, 12]),
        ("M-C",  "ECONOMICS",              [15, 14, 14], [10, 10],  [14, 13]),
        ("M-D",  "GEOPOLITICS",            [12, 13, 13], [12, 10],  [12, 12]),
    ]

    # Layout - left labels, then 3 columns (O / C / Q) with cells
    row_h = (TOP - BOT - 6) / len(strata)
    label_x_right = inner_x0 + 17

    # Header band
    band_y = TOP - 0.5
    ax.text(inner_x0, band_y, sp("STRATUM", 2),
            fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")

    col_titles = ["OPPORTUNITY", "CHALLENGE", "OPEN QUESTION"]
    col_colors = [VERMILION, OCHRE, VERDIGRIS]
    col_widths = (inner_x1 - label_x_right - 1.5) / 3
    for i, (title, color) in enumerate(zip(col_titles, col_colors)):
        cx = label_x_right + 1.5 + i * col_widths + col_widths / 2
        ax.text(cx, band_y, sp(title, 2),
                fontsize=5.5, fontname=F_MONO, color=color, va="top", ha="center")

    ax.plot([inner_x0, inner_x1], [TOP - 2.4, TOP - 2.4], color=RULE, lw=0.5)

    # Rows
    for i, (num, name, opps, chals, qs) in enumerate(strata):
        y_top = TOP - 3.5 - i * row_h
        y_mid = y_top - row_h / 2
        y_bot = y_top - row_h

        ax.plot([inner_x0, inner_x1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.3)
        ax.text(inner_x0 + 0.3, y_mid, num, fontsize=6.5, fontname=F_DMMONO,
                color=VERMILION, va="center")
        ax.text(inner_x0 + 4.2, y_mid, name, fontsize=8, fontname=F_DISPLAY,
                color=INK, va="center")

        # 3 cells per row - each cell shows 3 dots for top entries (size = score/15)
        for col, (scores, color) in enumerate(zip([opps, chals, qs], col_colors)):
            cx0 = label_x_right + 1.5 + col * col_widths
            for j, score in enumerate(scores):
                dx = cx0 + (j + 0.5) * (col_widths / 3)
                # dot size by score
                radius = 0.35 + (score - 8) * 0.12
                ax.add_patch(mpatches.Circle((dx, y_mid + 0.2), radius,
                                              fc=color, ec=color, lw=0, alpha=0.85))
                ax.text(dx, y_mid - 1.3, str(score),
                        fontsize=4.3, fontname=F_DMMONO, color=GRAY, ha="center", va="center")

    # Legend at bottom
    leg_y = BOT + 6.5
    ax.plot([inner_x0, inner_x1], [leg_y + 1.0, leg_y + 1.0], color=RULE, lw=0.4)
    ax.text(inner_x0, leg_y, sp("LEGEND", 2),
            fontsize=5, fontname=F_MONO, color=VERMILION, va="top")
    ax.text(inner_x0, leg_y - 1.6,
            "Each dot = one of the top entries in that lens for that stratum.  Diameter scales with composite score (out of 15).",
            fontsize=5, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
    ax.text(inner_x0, leg_y - 2.7,
            "Opportunity = Confidence × Time-to-monetize × Claimability for Alex.   Challenge = Severity × Probability × Alex exposure.   Open Question = Decidability × Asymmetry × Bet-size.",
            fontsize=5, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE VIII — WARDLEY MAP
# ============================================================

def plate_viii_wardley(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "VIII", "Wardley Map of the Stack",
        "User-need at top → dependencies cascading to foundations · evolution stage on the X-axis.",
        "Cartographia secundum Wardley — situs in evolutione",
        "PLATE VIII OF XI")
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Define grid
    map_x0 = inner_x0 + 4
    map_x1 = inner_x1 - 1
    map_y0 = BOT + 8
    map_y1 = TOP - 4

    # X-axis: evolution stages
    stage_w = (map_x1 - map_x0) / 4
    stages = ["GENESIS", "CUSTOM-BUILT", "PRODUCT", "COMMODITY"]
    stage_colors = [VERMILION, OCHRE, VERDIGRIS, GRAY]
    for i, (s, c) in enumerate(zip(stages, stage_colors)):
        sx = map_x0 + i * stage_w
        ax.plot([sx, sx], [map_y0, map_y1], color=GRAY_LIGHT, lw=0.4, ls=(0, (1, 2)))
        ax.text(sx + stage_w/2, map_y0 - 1.5, sp(s, 2),
                fontsize=5.5, fontname=F_MONO, color=c, ha="center", va="top")
    ax.plot([map_x1, map_x1], [map_y0, map_y1], color=GRAY_LIGHT, lw=0.4, ls=(0, (1, 2)))

    # Y-axis: visibility
    ax.plot([map_x0, map_x0], [map_y0, map_y1], color=RULE, lw=0.6)
    ax.plot([map_x0, map_x1], [map_y0, map_y0], color=RULE, lw=0.6)
    ax.text(map_x0 - 1.5, map_y1, "USER", fontsize=7, fontname=F_DISPLAY,
            color=INK, ha="right", va="top", rotation=90)
    ax.text(map_x0 - 1.5, map_y0 + 0.5, "FOUNDATION", fontsize=7, fontname=F_DISPLAY,
            color=INK, ha="right", va="bottom", rotation=90)

    # Axis labels
    ax.text(map_x0, map_y1 + 0.7, sp("VISIBILITY  ↑", 2),
            fontsize=5, fontname=F_MONO, color=GRAY, va="bottom")
    ax.text(map_x1, map_y0 - 4, sp("EVOLUTION  →", 2),
            fontsize=5, fontname=F_MONO, color=GRAY, ha="right", va="top")

    # Components: (label, x_stage_index 0-3 + fraction, y_visibility 0-1, color)
    # y_visibility: 1.0 = user, 0.0 = foundation
    components = [
        # User-need anchors (top)
        ("Knowledge work AI", 2.4, 0.97, INK),
        ("Computer-use agents", 0.6, 0.93, INK),
        ("Voice / CX agents", 2.0, 0.88, INK),
        ("Vertical agents", 2.3, 0.92, INK),
        # Application
        ("Sierra · Decagon · Glean", 1.8, 0.85, VERDIGRIS),
        ("Harvey · Hippocratic", 1.7, 0.82, VERDIGRIS),
        ("Cursor · Lovable · v0", 2.5, 0.83, VERDIGRIS),
        ("Operator · Mariner", 0.7, 0.86, VERMILION),
        ("Vapi · Retell", 2.0, 0.78, VERDIGRIS),
        # Orchestration
        ("MCP", 1.9, 0.72, OCHRE),
        ("LangGraph · Agent SDKs", 1.5, 0.68, VERDIGRIS),
        ("AI Gateways", 2.8, 0.66, VERDIGRIS),
        ("Eval / Obs (LangSmith…)", 1.7, 0.62, VERDIGRIS),
        # Memory / retrieval
        ("Mem0 · Letta · Zep", 0.8, 0.58, VERMILION),
        ("GraphRAG", 0.6, 0.55, VERMILION),
        ("Pinecone · Qdrant · pgvector", 2.7, 0.53, VERDIGRIS),
        ("Embeddings · Rerankers", 2.6, 0.49, VERDIGRIS),
        # Inference
        ("vLLM · SGLang", 2.8, 0.44, VERDIGRIS),
        ("NVIDIA Dynamo", 1.6, 0.41, VERDIGRIS),
        ("Apple MLX · ExecuTorch", 1.4, 0.38, OCHRE),
        # Models
        ("Frontier LLMs (Claude, GPT, Gemini)", 1.9, 0.35, VERDIGRIS),
        ("Open-weight LLMs (Llama 4, Qwen, DSV4)", 2.4, 0.32, VERDIGRIS),
        # Training
        ("RLVR · GRPO · Constitutional AI", 1.4, 0.27, OCHRE),
        ("PyTorch · Megatron · JAX", 2.7, 0.25, GRAY),
        # Data
        ("Common Crawl · FineWeb", 2.8, 0.21, GRAY),
        ("Licensed corpora (Reddit, FT, Reuters)", 1.8, 0.19, OCHRE),
        ("Synthetic data", 1.0, 0.17, VERMILION),
        # Compute
        ("H200 · B200 · GB300 NVL72", 2.2, 0.13, VERDIGRIS),
        ("HBM3e / HBM4", 1.5, 0.10, OCHRE),
        ("CoWoS-L packaging", 1.2, 0.08, OCHRE),
        # Networking
        ("NVLink · InfiniBand · 800G Ethernet", 2.3, 0.05, VERDIGRIS),
        # Power
        ("PPAs · Gas · SMR (Genesis)", 0.8, 0.02, VERMILION),
        ("Grid / Transmission", 3.7, 0.01, GRAY),
    ]
    for (label, x_idx, y_vis, color) in components:
        x = map_x0 + x_idx * stage_w
        y = map_y0 + y_vis * (map_y1 - map_y0)
        ax.add_patch(mpatches.Circle((x, y), 0.42, fc=color, ec=color, lw=0))
        # Label position - alternate sides to reduce collisions
        ax.text(x + 0.7, y + 0.05, label, fontsize=4.6, fontname=F_SERIF, color=INK,
                va="center", ha="left")

    # Strategic quadrant zones (subtle bg shade with labels)
    # PIONEER
    ax.text(map_x0 + stage_w * 0.5, map_y1 - 1.0, sp("PIONEER", 1),
            fontsize=8, fontname=F_DISPLAY, color=VERMILION, ha="center", alpha=0.7)
    ax.text(map_x0 + stage_w * 0.5, map_y1 - 2.2, "build · write · observe", fontsize=4.2,
            fontname=F_SERIF_IT, color=GRAY, ha="center", alpha=0.7)
    # SETTLE
    ax.text(map_x0 + stage_w * 1.5, map_y1 - 1.0, sp("SETTLE", 1),
            fontsize=8, fontname=F_DISPLAY, color=OCHRE, ha="center", alpha=0.7)
    ax.text(map_x0 + stage_w * 1.5, map_y1 - 2.2, "productize · the build sweet spot", fontsize=4.2,
            fontname=F_SERIF_IT, color=GRAY, ha="center", alpha=0.7)
    # CONSUME
    ax.text(map_x0 + stage_w * 2.5, map_y1 - 1.0, sp("CONSUME", 1),
            fontsize=8, fontname=F_DISPLAY, color=VERDIGRIS, ha="center", alpha=0.7)
    ax.text(map_x0 + stage_w * 2.5, map_y1 - 2.2, "buy · integrate · do not build", fontsize=4.2,
            fontname=F_SERIF_IT, color=GRAY, ha="center", alpha=0.7)
    # UTILITY
    ax.text(map_x0 + stage_w * 3.5, map_y1 - 1.0, sp("UTILITY", 1),
            fontsize=8, fontname=F_DISPLAY, color=GRAY, ha="center", alpha=0.7)
    ax.text(map_x0 + stage_w * 3.5, map_y1 - 2.2, "invisible plumbing", fontsize=4.2,
            fontname=F_SERIF_IT, color=GRAY, ha="center", alpha=0.7)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE IX — 7 POWERS GRID
# ============================================================

def plate_ix_powers(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "IX", "The 7 Powers Grid",
        "Eighteen strata × seven powers (Helmer) · who holds, where it strengthens or erodes.",
        "Imperia durabilia secundum Helmer — quae perdurant et quae cessant",
        "PLATE IX OF XI")
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # 7 Powers
    powers = ["SCALE", "NETWORK", "COUNTER-POS.", "SWITCH-COSTS", "BRAND", "CORNER-RES.", "PROCESS"]

    # Strata + presence map (1 = strong, 0.5 = partial, 0 = absent)
    # [Scale, Network, Counter, Switch, Brand, Cornered, Process]
    strata = [
        ("XIV USER",                   [1, 0.5, 0, 1, 1, 1, 0.5]),
        ("XIII APP / AGENT",           [0.5, 1, 0.5, 1, 1, 0.5, 1]),
        ("XII ORCHESTRATION / MCP",    [0.5, 1, 1, 0.5, 0.5, 0, 0.5]),
        ("XI RETRIEVAL / MEMORY",      [0, 0.5, 0, 0.5, 0.5, 0, 0.5]),
        ("X INFERENCE",                [0.5, 0.5, 0, 0, 0, 0.5, 1]),
        ("IX MODEL PROVIDERS",         [1, 0.5, 0, 0.5, 1, 0.5, 0.5]),
        ("VIII POST-TRAINING",         [0, 0, 0, 0.5, 0, 1, 1]),
        ("VII PRE-TRAINING",           [1, 0.5, 0.5, 0, 1, 1, 1]),
        ("VI DATA",                    [0, 0, 0.5, 0.5, 0.5, 1, 0.5]),
        ("V PARALLELISM",              [0, 1, 0, 0, 0, 1, 1]),
        ("IV FABRIC",                  [0.5, 0, 0.5, 1, 0, 1, 1]),
        ("III COMPUTE (NVIDIA et al)", [1, 0, 0, 1, 1, 1, 1]),
        ("II FACILITY",                [1, 0, 0, 1, 0, 1, 0.5]),
        ("I POWER",                    [1, 0, 0, 0, 0, 1, 1]),
        ("M-A SAFETY (Anthropic)",     [0, 0, 0, 0, 1, 1, 1]),
        ("M-B REGULATION / COMPLIANCE",[0, 0, 1, 1, 0, 1, 1]),
        ("M-C ECONOMICS / CAPITAL",    [1, 0, 0, 0, 0, 1, 0]),
        ("M-D GEOPOLITICS",            [0.5, 0, 1, 0, 0, 1, 0.5]),
    ]

    # Layout
    label_w = 28
    grid_x0 = inner_x0 + label_w
    grid_x1 = inner_x1 - 1
    cell_w = (grid_x1 - grid_x0) / 7
    grid_y0 = BOT + 6
    grid_y1 = TOP - 5
    cell_h = (grid_y1 - grid_y0) / len(strata)

    # Header
    for i, p in enumerate(powers):
        cx = grid_x0 + (i + 0.5) * cell_w
        ax.text(cx, grid_y1 + 1.5, sp(p, 1), fontsize=5, fontname=F_MONO,
                color=VERMILION, ha="center", va="bottom")
    ax.plot([inner_x0, inner_x1], [grid_y1 + 0.6, grid_y1 + 0.6], color=RULE, lw=0.5)
    ax.plot([grid_x0, grid_x0], [grid_y0, grid_y1 + 0.6], color=RULE, lw=0.4)

    # Rows
    for r, (name, presence) in enumerate(strata):
        y_top = grid_y1 - r * cell_h
        y_mid = y_top - cell_h / 2
        y_bot = y_top - cell_h
        ax.plot([inner_x0, inner_x1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.25)
        ax.text(inner_x0, y_mid, name, fontsize=6, fontname=F_DISPLAY_REG,
                color=INK, va="center")
        for c, val in enumerate(presence):
            cx = grid_x0 + (c + 0.5) * cell_w
            if val == 1:
                ax.add_patch(mpatches.Circle((cx, y_mid), 0.85,
                                              fc=VERMILION, ec=VERMILION, lw=0))
            elif val == 0.5:
                ax.add_patch(mpatches.Circle((cx, y_mid), 0.85,
                                              fc='none', ec=OCHRE, lw=0.6))
            else:
                ax.plot([cx - 0.3, cx + 0.3], [y_mid, y_mid], color=GRAY_LIGHT, lw=0.4)

    # Legend
    leg_y = BOT + 4
    ax.plot([inner_x0, inner_x1], [leg_y + 0.6, leg_y + 0.6], color=RULE, lw=0.4)
    ax.add_patch(mpatches.Circle((inner_x0 + 1, leg_y - 0.5), 0.6, fc=VERMILION, ec=VERMILION, lw=0))
    ax.text(inner_x0 + 2, leg_y - 0.5, "Strong / present", fontsize=5, fontname=F_SERIF_IT,
            color=INK_SOFT, va="center")
    ax.add_patch(mpatches.Circle((inner_x0 + 25, leg_y - 0.5), 0.6, fc='none', ec=OCHRE, lw=0.6))
    ax.text(inner_x0 + 26, leg_y - 0.5, "Partial / contested", fontsize=5, fontname=F_SERIF_IT,
            color=INK_SOFT, va="center")
    ax.plot([inner_x0 + 50, inner_x0 + 51], [leg_y - 0.5, leg_y - 0.5], color=GRAY_LIGHT, lw=0.5)
    ax.text(inner_x0 + 52, leg_y - 0.5, "Absent / cyclical", fontsize=5, fontname=F_SERIF_IT,
            color=INK_SOFT, va="center")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE X — ECOSYSTEM JTBD CANVAS
# ============================================================

def plate_x_jtbd(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "X", "Ecosystem JTBD Canvas",
        "Six top-down jobs · 8-phase maps · top underserved outcomes per job.",
        "Officia ab usuario adsumpta — quae officia stratum totum implere debet, ubi deficit",
        "PLATE X OF XI")
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Six jobs - we'll lay out as 2 columns × 3 rows of cards
    jobs = [
        {
            "id": "1",
            "name": "RUN AN AI-LEVERAGED\nENTERPRISE SALES MOTION",
            "color": OCHRE,
            "underserved": [
                ("Detecting AI-generated outreach", 7),
                ("Mapping the buying committee", 7),
                ("Diagnosing a stalling deal", 6),
            ],
            "hook": "Buying-committee graph tool · n8n + Claude + Supabase",
        },
        {
            "id": "2",
            "name": "BUILD · SHIP · ITERATE\nAI-NATIVE PRODUCT (1-10 PERSON)",
            "color": OCHRE,
            "underserved": [
                ("Eval design that catches real failures", 8),
                ("Causal attribution of bad outputs", 8),
                ("Model migration without regression", 6),
            ],
            "hook": "Eval-design service · public build log",
        },
        {
            "id": "3",
            "name": "STAY CURRENT ON THE\nAI ECOSYSTEM AND ACT",
            "color": OCHRE,
            "underserved": [
                ("Translating 'X shipped' into 'I should change Y'", 7),
                ("Acting on signal vs. hype", 6),
                ("Personal taxonomy that survives evolution", 6),
            ],
            "hook": "Operator's translation newsletter",
        },
        {
            "id": "4",
            "name": "PASS ENTERPRISE AI\nPROCUREMENT  ★ PRIORITY",
            "color": VERMILION,
            "underserved": [
                ("AI-specific contract addendum negotiation", 8),
                ("Mapping the buyer's AI governance org", 8),
                ("Capturing precedent across deals", 8),
            ],
            "hook": "The Enterprise AI Vendor Procurement Playbook",
        },
        {
            "id": "5",
            "name": "RECRUIT · EVALUATE · RAMP\nAI-NATIVE TALENT",
            "color": OCHRE,
            "underserved": [
                ("Filtering for verifiable AI-native experience", 7),
                ("Screening builders vs. prompters", 7),
                ("Role re-specification cadence", 6),
            ],
            "hook": "Screening rubric for AI-native commercial roles",
        },
        {
            "id": "6",
            "name": "GOVERN AI USAGE\nACROSS THE ENTERPRISE",
            "color": OCHRE,
            "underserved": [
                ("Shadow AI discovery", 7),
                ("Low-friction enforcement", 7),
                ("Board-ready usage reporting", 6),
            ],
            "hook": "Board-ready AI usage scorecard · 90-day baseline",
        },
    ]

    # Layout 2 cols × 3 rows
    cols = 2
    rows = 3
    avail_w = inner_x1 - inner_x0
    avail_h = (TOP - BOT) - 4
    card_w = avail_w / cols - 1
    card_h = avail_h / rows - 1.5
    base_y = TOP - 2.0

    for i, job in enumerate(jobs):
        col = i % cols
        row = i // cols
        x0 = inner_x0 + col * (card_w + 1)
        y_top = base_y - row * (card_h + 1.5)
        y_bot = y_top - card_h

        # Card border
        ax.add_patch(mpatches.Rectangle((x0, y_bot), card_w, card_h,
                                          fill=False, ec=RULE, lw=0.45))

        # Job ID badge
        ax.add_patch(mpatches.Circle((x0 + 1.0, y_top - 1.0), 0.7,
                                       fc=job["color"], ec=job["color"], lw=0))
        ax.text(x0 + 1.0, y_top - 1.0, job["id"], fontsize=7, fontname=F_MONO_BOLD,
                color=PAPER, ha="center", va="center")

        # Job title
        for li, line in enumerate(job["name"].split("\n")):
            ax.text(x0 + 2.2, y_top - 0.7 - li * 1.6, line, fontsize=8.5,
                    fontname=F_DISPLAY, color=INK, va="top")

        # Divider
        ax.plot([x0 + 0.5, x0 + card_w - 0.5], [y_top - 4.0, y_top - 4.0],
                color=RULE, lw=0.3)

        # Underserved outcomes
        ax.text(x0 + 0.6, y_top - 4.7, sp("UNDERSERVED OUTCOMES", 1),
                fontsize=4.5, fontname=F_MONO, color=VERMILION, va="top")
        for j, (outcome, gap) in enumerate(job["underserved"]):
            ay = y_top - 6.0 - j * 1.6
            # Gap circle
            ax.add_patch(mpatches.Circle((x0 + 1.0, ay), 0.5,
                                          fc=VERMILION if gap >= 7 else OCHRE,
                                          ec=VERMILION if gap >= 7 else OCHRE, lw=0))
            ax.text(x0 + 1.0, ay, str(gap), fontsize=4.6, fontname=F_MONO_BOLD,
                    color=PAPER, ha="center", va="center")
            ax.text(x0 + 1.9, ay, outcome, fontsize=5, fontname=F_SERIF, color=INK, va="center")

        # Action hook at bottom
        hook_y = y_bot + 1.0
        ax.plot([x0 + 0.5, x0 + card_w - 0.5], [hook_y + 1.5, hook_y + 1.5],
                color=RULE, lw=0.3)
        ax.text(x0 + 0.6, hook_y + 0.8, sp("ACTION HOOK", 1),
                fontsize=4.3, fontname=F_MONO, color=VERDIGRIS, va="top")
        ax.text(x0 + 0.6, hook_y - 0.2, job["hook"], fontsize=5,
                fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE XI — ALEX'S ACTION PORTFOLIO
# ============================================================

def plate_xi_action(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "XI", "The Action Portfolio",
        "Seven ranked bets · 6 / 12 / 18-month sequencing · cruxes and risks.",
        "Portfolium consilii — septem pignora, quinque pericula, quinque quaestiones",
        "PLATE XI OF XI")
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # SECTION 1: 7 Big Bets at top
    section_top = TOP - 1.0
    ax.text(inner_x0, section_top, sp("THE 7 BIG BETS  ·  RANKED", 3),
            fontsize=6.2, fontname=F_MONO, color=VERMILION, va="top")
    ax.plot([inner_x0, inner_x1], [section_top - 2.0, section_top - 2.0],
            color=RULE, lw=0.5)

    # Conviction encoded as filled-circle count (5 max)
    bets = [
        ("1", "Enterprise AI Procurement Playbook + Practice", 5, "Convergence across 5/5 frameworks · 90-day flag-plant", VERMILION),
        ("2", "Vertical Agent GTM Leadership Role (NYC)", 5, "Sierra · Decagon · Glean · Harvey · Hippocratic · Augment", VERMILION),
        ("3", "MCP-Native Enterprise Integration Practice", 4, "Gated on Crux 3 · Q2-Q4 2026 window", OCHRE),
        ("4", "Inference Cost Optimization (FinOps for Tokens)", 4, "12-18mo decay · highest velocity-to-cash", OCHRE),
        ("5", "Enterprise RAG Architecture Practice", 4, "Compounds with #1 and #4 · same buyer", OCHRE),
        ("6", "Operator's Translation Newsletter", 3, "Lowest cost-to-start · positioning flywheel", VERDIGRIS),
        ("7", "VC Operating Partner / Platform Path", 3, "Long-arc fallback · activates if 1+2 stall", VERDIGRIS),
    ]

    bet_y = section_top - 3.5
    bet_h = 4.0
    for i, (num, name, conv, sub, color) in enumerate(bets):
        y_top = bet_y - i * bet_h
        y_mid = y_top - bet_h/2 + 0.3
        ax.add_patch(mpatches.Circle((inner_x0 + 1.5, y_mid), 1.4,
                                       fc=color, ec=color, lw=0))
        ax.text(inner_x0 + 1.5, y_mid + 0.1, num, fontsize=11, fontname=F_MONO_BOLD,
                color=PAPER, ha="center", va="center")
        ax.text(inner_x0 + 4, y_mid + 0.9, name, fontsize=10,
                fontname=F_DISPLAY, color=INK, va="center")
        # Conviction dots (filled = conv, unfilled = 5-conv)
        for k in range(5):
            cx_dot = inner_x1 - 0.5 - (4 - k) * 1.2
            if k < conv:
                ax.add_patch(mpatches.Circle((cx_dot, y_mid + 0.9), 0.35,
                                              fc=color, ec=color, lw=0))
            else:
                ax.add_patch(mpatches.Circle((cx_dot, y_mid + 0.9), 0.35,
                                              fc='none', ec=color, lw=0.5))
        ax.text(inner_x0 + 4, y_mid - 1.0, sub, fontsize=5.5,
                fontname=F_SERIF_IT, color=INK_SOFT, va="center")
        if i < len(bets) - 1:
            ax.plot([inner_x0 + 0.5, inner_x1 - 0.5], [y_top - bet_h, y_top - bet_h],
                    color=GRAY_LIGHT, lw=0.3)

    # SECTION 2: 6/12/18-month timeline
    timeline_top = bet_y - len(bets) * bet_h - 2.5
    ax.text(inner_x0, timeline_top, sp("6 · 12 · 18-MONTH SEQUENCING", 3),
            fontsize=6.2, fontname=F_MONO, color=VERMILION, va="top")
    ax.plot([inner_x0, inner_x1], [timeline_top - 2.0, timeline_top - 2.0],
            color=RULE, lw=0.5)

    # 3 columns
    col_w = (inner_x1 - inner_x0) / 3
    phases = [
        {
            "title": "MONTHS 0–6",
            "subtitle": "Plant flags · cheap experiments",
            "color": VERMILION,
            "items": [
                "Outline + publish Procurement Playbook (90 days)",
                "Active job search: Sierra · Decagon · Glean · Harvey · Hippocratic · Augment",
                "5 free FinOps audits → 2 paid retainers",
                "Translation newsletter weekly",
                "Network: RAAIS · AI Tinkerers · Betaworks · FirstMark MAD",
                "2 high-signal conversations / week, logged",
            ],
        },
        {
            "title": "MONTHS 6–12",
            "subtitle": "Commit · path A / B / C",
            "color": OCHRE,
            "items": [
                "Path A: take vertical-agent role if offer in band",
                "Path B: productize procurement-readiness SaaS",
                "Path C: activate VC Operating Partner outreach",
                "Bet 3 (MCP) gating check at month 6 (Crux 3)",
                "Ship 3 production MCP servers if commons holds",
                "Continue newsletter as flywheel",
            ],
        },
        {
            "title": "MONTHS 12–18",
            "subtitle": "Compound · decide longer arc",
            "color": VERDIGRIS,
            "items": [
                "Public voice: inbound > outbound threshold",
                "One canonical phrase / framework attributable",
                "Decide: Path A (GTM exec) · Path B (advisory + SaaS) · Path D (C-level)",
                "Optional Sovereign-AI niche: 1 trip + 1 essay / quarter",
                "Quarterly check-in template against tracker",
                "Subtraction: kill one bet quarterly",
            ],
        },
    ]
    for i, phase in enumerate(phases):
        x0 = inner_x0 + i * col_w + 0.4
        col_top = timeline_top - 2.8
        # Phase header
        ax.text(x0, col_top, sp(phase["title"], 1),
                fontsize=7, fontname=F_DISPLAY, color=phase["color"], va="top")
        ax.text(x0, col_top - 1.3, phase["subtitle"],
                fontsize=4.8, fontname=F_SERIF_DISP_IT, color=GRAY, va="top")
        ax.plot([x0, x0 + col_w - 1], [col_top - 2.0, col_top - 2.0],
                color=phase["color"], lw=0.5)
        # Items
        for j, item in enumerate(phase["items"]):
            iy = col_top - 3.0 - j * 1.7
            ax.add_patch(mpatches.Circle((x0 + 0.3, iy), 0.25,
                                          fc=phase["color"], ec=phase["color"], lw=0))
            # Text wrap manually for narrow column
            words = item.split()
            lines = []
            curr = ""
            for w in words:
                test = curr + (" " if curr else "") + w
                if len(test) > 38:
                    if curr:
                        lines.append(curr)
                    curr = w
                else:
                    curr = test
            if curr:
                lines.append(curr)
            for li, line in enumerate(lines):
                ax.text(x0 + 0.9, iy - li * 0.95, line, fontsize=5,
                        fontname=F_SERIF, color=INK, va="center")

    # SECTION 3: Cruxes + Risks side-by-side at bottom
    bottom_top = timeline_top - 2.0 - 1.0 - 18  # estimate after phases
    bottom_top = BOT + 26  # fixed position from bottom
    half_x = (inner_x0 + inner_x1) / 2

    ax.text(inner_x0, bottom_top, sp("THE 5 CRUXES", 3),
            fontsize=5.8, fontname=F_MONO, color=VERDIGRIS, va="top")
    ax.plot([inner_x0, half_x - 1.5], [bottom_top - 1.5, bottom_top - 1.5],
            color=RULE, lw=0.4)
    cruxes = [
        ("Anthropic ARR — $24B or $30B?", "Q2-Q3 2026"),
        ("Inference compute — 10x or flat?", "Q4 2026"),
        ("MCP — commons or fork?", "H2 2026"),
        ("EU AI Act — teeth or paper tiger?", "late 2026"),
        ("Long-term memory — standalone or absorbed?", "12-18mo"),
    ]
    for i, (q, when) in enumerate(cruxes):
        y = bottom_top - 2.6 - i * 2.5
        ax.add_patch(mpatches.Circle((inner_x0 + 0.4, y), 0.3, fc=VERDIGRIS, ec=VERDIGRIS, lw=0))
        ax.text(inner_x0 + 1.0, y, q, fontsize=5.5, fontname=F_SERIF, color=INK, va="center")
        ax.text(inner_x0 + 1.0, y - 1.0, when, fontsize=4.4, fontname=F_DMMONO, color=GRAY, va="center")

    ax.text(half_x + 1, bottom_top, sp("THE 5 STRUCTURAL RISKS", 3),
            fontsize=5.8, fontname=F_MONO, color=VERMILION, va="top")
    ax.plot([half_x + 1, inner_x1], [bottom_top - 1.5, bottom_top - 1.5],
            color=RULE, lw=0.4)
    risks = [
        ("HBM4 / CoWoS-L slip", "ramp telemetry"),
        ("Hyperscaler FCF reckoning", "Q3-Q4 2026"),
        ("OpenAI Preparedness adjustment-clause", "any time"),
        ("Federal preemption volatility", "2026-27 court rulings"),
        ("Foundation labs walking up-stack", "Connectors / Skills releases"),
    ]
    for i, (r, watch) in enumerate(risks):
        y = bottom_top - 2.6 - i * 2.5
        ax.add_patch(mpatches.Circle((half_x + 1.4, y), 0.3, fc=VERMILION, ec=VERMILION, lw=0))
        ax.text(half_x + 2.0, y, r, fontsize=5.5, fontname=F_SERIF, color=INK, va="center")
        ax.text(half_x + 2.0, y - 1.0, "Watch: " + watch, fontsize=4.4, fontname=F_DMMONO, color=GRAY, va="center")

    # Closing thesis at very bottom
    ax.plot([inner_x0, inner_x1], [BOT + 10.5, BOT + 10.5], color=RULE, lw=0.5)
    ax.text(inner_x0, BOT + 9.5, sp("THESIS", 3),
            fontsize=5, fontname=F_MONO, color=VERMILION, va="top")
    ax.text(inner_x0, BOT + 8.0,
            "Plant a flag at the intersection of enterprise AI procurement, vertical agent GTM, and operator translation —",
            fontsize=5.5, fontname=F_SERIF_DISP_IT, color=INK, va="top")
    ax.text(inner_x0, BOT + 7.0,
            "three positions that compound, that the frameworks all converge on, and that this profile is",
            fontsize=5.5, fontname=F_SERIF_DISP_IT, color=INK, va="top")
    ax.text(inner_x0, BOT + 6.0,
            "one of fewer than fifty people on Earth structurally able to occupy.   That position is yours to claim.",
            fontsize=5.5, fontname=F_SERIF_DISP_IT, color=INK, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# Run
# ============================================================

def main():
    with PdfPages(OUT_PATH) as pdf:
        plate_vii_ocq_heat(pdf)
        plate_viii_wardley(pdf)
        plate_ix_powers(pdf)
        plate_x_jtbd(pdf)
        plate_xi_action(pdf)

        d = pdf.infodict()
        d["Title"] = "SUBSTRATE Vol II — Plates VII–XI"
        d["Author"] = "Compiled for A. Yedi"
        d["Subject"] = "Decisions playbook visual atlas (companion to Vol I)"

    print("Wrote", OUT_PATH)


if __name__ == "__main__":
    main()
