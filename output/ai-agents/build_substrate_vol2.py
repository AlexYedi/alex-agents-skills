"""
SUBSTRATE · Vol III · Volume II of Plates (Plates VII–XI).
Agent-layer OCQ heat map, Wardley map, 7 Powers grid, JTBD canvas, Action portfolio.
"""
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
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
    return "DejaVu Sans"

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
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents/AI_AGENTS_SUBSTRATE_VOL2.pdf"


def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 154.5)
    ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax, plate_no, title_top, subtitle_top, latin, plate_label):
    LEFT = 8.5; RIGHT = 92.5; TOP = 148.5; BOTTOM = 9.5
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.55))
    ax.plot([LEFT, RIGHT], [TOP - 6.0, TOP - 6.0], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 4.5, BOTTOM + 4.5], color=RULE, lw=0.45)
    ax.plot([LEFT - 2.6, LEFT - 2.6], [BOTTOM + 4.5, TOP - 6.0], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 4.5, TOP - 6.0, 28)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([LEFT - 2.6 - (1.0 if long else 0.5), LEFT - 2.6], [y, y], color=RULE, lw=0.35)
        if long:
            ax.text(LEFT - 4.1, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=4.4, fontname=F_DMMONO, color=GRAY)
    ax.text(LEFT, TOP - 1.0, sp("AN ATLAS OF THE AGENT STRATA  ·  VOLUME II", 4),
            ha="left", va="top", fontsize=6.0, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 1.9, title_top.upper(),
            ha="left", va="top", fontsize=18, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.0, TOP - 2.0, sp(plate_label, 2),
            ha="right", va="top", fontsize=7.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 4.5, subtitle_top,
            ha="left", va="top", fontsize=6.2, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4, latin,
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)
    ax.add_patch(mpatches.Circle((RIGHT - 1.4, TOP - 2.0), 1.05, fill=False, ec=VERMILION, lw=0.6))
    ax.text(RIGHT - 1.4, TOP - 2.0, plate_no, ha="center", va="center",
            fontsize=6.2, fontname=F_MONO_BOLD, color=VERMILION)
    ax.text(LEFT, BOTTOM + 3.0, sp("SUBSTRATE  ·  VOL III  ·  DECISIONS PLAYBOOK", 3),
            ha="left", va="top", fontsize=4.6, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.4, sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, plate_label, ha="right", va="top",
            fontsize=5.4, fontname=F_DMMONO, color=GRAY)
    return LEFT, RIGHT, TOP - 6.5, BOTTOM + 4.7


# ============================================================
# PLATE VII — OCQ HEAT MAP (agent layer: 10 sub + 4 meta)
# ============================================================

def plate_vii(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "VII", "OCQ Heat Map · Agent",
        "Fourteen agent strata × three lenses · scored opportunity, challenge, open question.",
        "Stratum agenticum × instrumentum analyticum · conviction across the column",
        "PLATE VII OF XI")
    ix0, ix1 = L + 1.0, R - 1.0

    # Agent strata (descending: X = end-user surface, I = foundation)
    strata = [
        ("X",    "END-USER · SURFACES",     [13, 12, 13], [12, 11], [12, 13]),
        ("IX",   "VERTICAL · PRODUCTS",     [15, 13, 12], [13, 11], [15, 13]),
        ("VIII", "RUNTIME · SAFETY",        [12, 10, 11], [13, 13], [10, 12]),
        ("VII",  "EVAL · OBSERVABILITY",    [14, 11, 10], [13, 13], [12, 13]),
        ("VI",   "ACTION · SURFACES",       [13, 12, 13], [12, 11], [14, 11]),
        ("V",    "PLANNING · REASONING",    [15, 13, 11], [13, 11], [12, 12]),
        ("IV",   "MEMORY · STATE",          [13, 13, 11], [12, 11], [11, 12]),
        ("III",  "TOOL · PROTOCOL",         [13, 13, 11], [12, 13], [14, 12]),
        ("II",   "AGENT · RUNTIMES",        [12, 12, 12], [12, 11], [11, 9]),
        ("I",    "FOUNDATION · CAPABILITY", [13, 13, 13], [13, 12], [14, 11]),
        ("M-A",  "CAPABILITY · SAFETY",     [11, 9, 10],  [11, 9],  [11, 12]),
        ("M-B",  "REGULATION",              [13, 12, 12], [12, 11], [13, 14]),
        ("M-C",  "ECONOMICS",               [15, 12, 11], [13, 12], [13, 13]),
        ("M-D",  "GEOPOLITICS",             [11, 10, 9],  [9, 8],   [11, 11]),
    ]

    row_h = (TOP - BOT - 6) / len(strata)
    label_x_right = ix0 + 17

    band_y = TOP - 0.5
    ax.text(ix0, band_y, sp("STRATUM", 2),
            fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
    titles = ["OPPORTUNITY", "CHALLENGE", "OPEN QUESTION"]
    colors = [VERMILION, OCHRE, VERDIGRIS]
    cw = (ix1 - label_x_right - 1.5) / 3
    for i, (t, c) in enumerate(zip(titles, colors)):
        cx = label_x_right + 1.5 + i * cw + cw / 2
        ax.text(cx, band_y, sp(t, 2),
                fontsize=5.5, fontname=F_MONO, color=c, va="top", ha="center")
    ax.plot([ix0, ix1], [TOP - 2.4, TOP - 2.4], color=RULE, lw=0.5)

    for i, (num, name, opps, chals, qs) in enumerate(strata):
        y_top = TOP - 3.5 - i * row_h
        y_mid = y_top - row_h / 2
        y_bot = y_top - row_h
        ax.plot([ix0, ix1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.3)
        ax.text(ix0 + 0.3, y_mid, num, fontsize=6.5, fontname=F_DMMONO,
                color=VERMILION, va="center")
        ax.text(ix0 + 4.2, y_mid, name, fontsize=8, fontname=F_DISPLAY,
                color=INK, va="center")
        for col, (scores, color) in enumerate(zip([opps, chals, qs], colors)):
            cx0 = label_x_right + 1.5 + col * cw
            for j, score in enumerate(scores):
                dx = cx0 + (j + 0.5) * (cw / 3)
                radius = 0.35 + (score - 8) * 0.12
                ax.add_patch(mpatches.Circle((dx, y_mid + 0.2), radius,
                                              fc=color, ec=color, lw=0, alpha=0.85))
                ax.text(dx, y_mid - 1.3, str(score),
                        fontsize=4.3, fontname=F_DMMONO, color=GRAY, ha="center", va="center")

    leg_y = BOT + 6.5
    ax.plot([ix0, ix1], [leg_y + 1.0, leg_y + 1.0], color=RULE, lw=0.4)
    ax.text(ix0, leg_y, sp("LEGEND", 2),
            fontsize=5, fontname=F_MONO, color=VERMILION, va="top")
    ax.text(ix0, leg_y - 1.6,
            "Each dot = one top entry in that lens for that stratum. Diameter scales with composite score (out of 15).",
            fontsize=5, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
    ax.text(ix0, leg_y - 2.7,
            "Opportunity = Confidence × Time-to-Monetize × Claimability. Challenge = Severity × Probability × Exposure. Open Question = Decidability × Asymmetry × Bet-size.",
            fontsize=5, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE VIII — WARDLEY MAP (agent stack)
# ============================================================

def plate_viii(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "VIII", "Wardley Map · Agent Stack",
        "Four anchored agent user-needs · dependencies cascading · evolution stage along the X-axis.",
        "Cartographia agenticum · stage of evolution in 2025–2026",
        "PLATE VIII OF XI")
    ix0, ix1 = L + 1.0, R - 1.0

    mx0, mx1 = ix0 + 4, ix1 - 1
    my0, my1 = BOT + 8, TOP - 4
    sw = (mx1 - mx0) / 4
    stages = ["GENESIS", "CUSTOM-BUILT", "PRODUCT", "COMMODITY"]
    scolors = [VERMILION, OCHRE, VERDIGRIS, GRAY]
    for i, (s, c) in enumerate(zip(stages, scolors)):
        sx = mx0 + i * sw
        ax.plot([sx, sx], [my0, my1], color=GRAY_LIGHT, lw=0.4, ls=(0, (1, 2)))
        ax.text(sx + sw/2, my0 - 1.5, sp(s, 2),
                fontsize=5.5, fontname=F_MONO, color=c, ha="center", va="top")
    ax.plot([mx1, mx1], [my0, my1], color=GRAY_LIGHT, lw=0.4, ls=(0, (1, 2)))

    ax.plot([mx0, mx0], [my0, my1], color=RULE, lw=0.6)
    ax.plot([mx0, mx1], [my0, my0], color=RULE, lw=0.6)
    ax.text(mx0 - 1.5, my1, "USER", fontsize=7, fontname=F_DISPLAY,
            color=INK, ha="right", va="top", rotation=90)
    ax.text(mx0 - 1.5, my0 + 0.5, "FOUNDATION", fontsize=7, fontname=F_DISPLAY,
            color=INK, ha="right", va="bottom", rotation=90)
    ax.text(mx0, my1 + 0.7, sp("VISIBILITY (up)", 2),
            fontsize=5, fontname=F_MONO, color=GRAY, va="bottom")
    ax.text(mx1, my0 - 4, sp("EVOLUTION (right)", 2),
            fontsize=5, fontname=F_MONO, color=GRAY, ha="right", va="top")

    # Components (x: 0..4 across stages, y: 0..1 visibility)
    components = [
        # Anchored user needs (top, near user)
        ("Deep research", 2.5, 0.97, INK),
        ("Back-office workflow", 0.9, 0.93, INK),
        ("CX resolution + voice", 2.0, 0.92, INK),
        ("Code change merge", 2.5, 0.95, INK),
        # End-user surfaces (X)
        ("Chat web / mobile", 2.9, 0.86, VERDIGRIS),
        ("CLI · IDE inline", 2.7, 0.84, VERDIGRIS),
        ("Embedded SaaS (Copilot)", 2.8, 0.81, VERDIGRIS),
        ("Slack · WhatsApp agents", 1.8, 0.79, OCHRE),
        ("Voice inbound", 1.9, 0.76, OCHRE),
        ("Computer-use UX", 0.7, 0.83, VERMILION),
        ("Wearable · AR", 0.5, 0.74, VERMILION),
        # Vertical products (IX)
        ("Sierra · Decagon (CX)", 1.9, 0.71, VERDIGRIS),
        ("Glean (knowledge)", 2.1, 0.69, VERDIGRIS),
        ("Harvey (legal)", 1.7, 0.67, OCHRE),
        ("Hippocratic · Abridge", 1.7, 0.65, OCHRE),
        ("Hebbia · Rogo (fin / KW)", 1.6, 0.63, OCHRE),
        ("Mistral Le Chat Ent.", 1.5, 0.61, OCHRE),
        # Eval / obs / safety (VII, VIII)
        ("Procurement-grade audit", 0.4, 0.55, VERMILION),
        ("Braintrust · LangSmith", 2.0, 0.53, OCHRE),
        ("Lakera · NeMo · L-Guard", 2.1, 0.51, OCHRE),
        ("OTel GenAI", 2.8, 0.49, VERDIGRIS),
        # Action surfaces (VI)
        ("Browserbase + Stagehand", 2.5, 0.45, VERDIGRIS),
        ("E2B · Modal · V-Sandbox", 2.7, 0.43, VERDIGRIS),
        ("LiveKit · Cartesia · Twilio", 2.9, 0.41, VERDIGRIS),
        ("Vapi · Retell (orch)", 1.9, 0.43, OCHRE),
        # Memory / planning (IV, V)
        ("Lab-native memory", 2.0, 0.37, OCHRE),
        ("Mem0 · Letta · Zep", 0.8, 0.35, VERMILION),
        ("Planner-executor split", 2.7, 0.33, VERDIGRIS),
        ("Reasoning models", 2.5, 0.31, VERDIGRIS),
        # Runtimes / protocol (II, III)
        ("Claude / OAI / Google SDKs", 1.9, 0.27, OCHRE),
        ("LangGraph 1.0", 2.4, 0.25, VERDIGRIS),
        ("MCP spec", 2.6, 0.23, VERDIGRIS),
        ("MCP gateways", 1.8, 0.21, OCHRE),
        ("A2A", 0.4, 0.19, VERMILION),
        # Foundation (I)
        ("Frontier model agentic capability", 2.0, 0.13, VERDIGRIS),
        ("Open-weight reasoners (R2 / Qwen3)", 1.4, 0.11, OCHRE),
        ("Computer-use ceiling (OSWorld)", 0.7, 0.09, VERMILION),
    ]
    for label, sx, sy, color in components:
        x = mx0 + sx * sw
        y = my0 + sy * (my1 - my0)
        ax.add_patch(mpatches.Circle((x, y), 0.45, fc=color, ec=color, lw=0, alpha=0.85))
        ax.text(x + 0.7, y, label, fontsize=4.4, fontname=F_SERIF, color=INK, va="center")

    # Punctuated equilibria callout
    pe_y = BOT + 5.5
    ax.text(ix0, pe_y, sp("PUNCTUATED EQUILIBRIA · 2026–2027", 3),
            fontsize=5.2, fontname=F_MONO, color=VERMILION, va="top")
    ax.plot([ix0, ix1], [pe_y - 0.8, pe_y - 0.8], color=RULE, lw=0.3)
    pe = [
        "1 · MCP gateways · Custom → Product · H2 '26",
        "2 · Computer use · Genesis → Custom · mid-late '26",
        "3 · Voice substrate · Product → Commodity · mid-late '26",
        "4 · Memory · forced binary · H2 '26",
        "5 · Procurement-grade controls · Genesis → Custom · Q4 '26",
        "6 · Eval / obs consolidation · Q4 '26 – H1 '27",
        "7 · Foundation labs walking up-stack · continuous",
    ]
    for i, t in enumerate(pe):
        x = ix0 + (i % 4) * (ix1 - ix0) / 4
        y = pe_y - 2.2 - (i // 4) * 1.6
        ax.text(x, y, t, fontsize=4.6, fontname=F_SERIF, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE IX — 7 POWERS GRID
# ============================================================

def plate_ix(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "IX", "7 Powers · Agent",
        "Per-stratum mapping of the seven Helmer powers · who holds them · direction of travel.",
        "Septem potestates Helmeri applicatae stratis agenticis",
        "PLATE IX OF XI")
    ix0, ix1 = L + 1.0, R - 1.0

    powers = ["Scale", "Network", "Counter-Pos.", "Switching", "Brand", "Cornered", "Process"]
    strata = [
        ("X",   "END-USER SURF.",     [".", "·", "○", "●", "○", "●", "○"], "MSFT Copilot · Apple AI · WhatsApp"),
        ("IX",  "VERTICAL PROD.",     ["·", "○", "·", "●", "○", "·", "●"], "Sierra · Harvey · Glean · Hippocratic"),
        ("VIII","RUNTIME SAFETY",     [".", "·", "·", "○", "○", "·", "·"], "Lakera niche; mostly absorbed"),
        ("VII", "EVAL / OBS",         [".", ".", "·", "○", "○", ".", "○"], "LangSmith · Braintrust · Inspect AI"),
        ("VI",  "ACTION SURF.",       ["○", "·", "·", "○", "·", "○", "·"], "LiveKit (CR) · Browserbase (SC)"),
        ("V",   "PLANNING / RES.",    [".", ".", ".", ".", ".", "○", "●"], "Inside labs only"),
        ("IV",  "MEMORY / STATE",     [".", ".", "·", "○", "·", ".", "·"], "Zep compliance niche"),
        ("III", "TOOL / PROTOCOL",    [".", "●", "●", "○", ".", ".", "·"], "MCP gateways · Anthropic CP win"),
        ("II",  "AGENT RUNTIMES",     [".", ".", ".", ".", ".", ".", "."], "Thinnest layer · no powers"),
        ("I",   "FOUND. CAPABILITY",  [".", "·", "·", "○", "○", "●", "●"], "Anthropic / OAI / Google · talent CR"),
        ("M-A", "CAP. SAFETY",        [".", ".", "·", "○", "●", "●", "●"], "Anthropic ASL most defensible"),
        ("M-B", "REGULATION",         [".", ".", "●", "○", ".", "●", "●"], "Mistral CP · Palantir · Bet #1"),
        ("M-C", "ECONOMICS",          ["●", ".", ".", "·", ".", ".", "·"], "Hyperscaler scale only"),
        ("M-D", "GEOPOLITICS",        [".", ".", "●", "·", ".", "●", "·"], "Mistral · Manus (CN data CR)"),
    ]

    # Header
    label_w = 20
    cell_w = (ix1 - ix0 - label_w - 28) / len(powers)
    band_y = TOP - 0.5
    ax.text(ix0, band_y, sp("STRATUM", 2),
            fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
    for i, pw in enumerate(powers):
        x = ix0 + label_w + i * cell_w + cell_w / 2
        ax.text(x, band_y, sp(pw.upper(), 1),
                fontsize=4.5, fontname=F_MONO, color=VERMILION, va="top", ha="center", rotation=20)
    ax.text(ix0 + label_w + 7 * cell_w + 2, band_y, sp("HOLDERS", 2),
            fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
    ax.plot([ix0, ix1], [TOP - 3.0, TOP - 3.0], color=RULE, lw=0.5)

    row_h = (TOP - 4 - BOT - 8) / len(strata)
    for i, (num, name, marks, holders) in enumerate(strata):
        y = TOP - 4 - (i + 0.5) * row_h
        ax.plot([ix0, ix1], [y - row_h/2, y - row_h/2], color=GRAY_LIGHT, lw=0.3)
        ax.text(ix0 + 0.3, y, num, fontsize=6, fontname=F_DMMONO, color=VERMILION, va="center")
        ax.text(ix0 + 4, y, name, fontsize=6.6, fontname=F_DISPLAY, color=INK, va="center")
        for j, mark in enumerate(marks):
            x = ix0 + label_w + j * cell_w + cell_w / 2
            if mark == "●":
                ax.add_patch(mpatches.Circle((x, y), 0.55, fc=VERMILION, ec=VERMILION, lw=0))
            elif mark == "○":
                ax.add_patch(mpatches.Circle((x, y), 0.45, fc="none", ec=INK_SOFT, lw=0.6))
            elif mark == "·":
                ax.add_patch(mpatches.Circle((x, y), 0.18, fc=GRAY, ec=GRAY, lw=0))
            # else "." = nothing
        ax.text(ix0 + label_w + 7 * cell_w + 2, y, holders,
                fontsize=4.6, fontname=F_SERIF_IT, color=INK_SOFT, va="center")

    # Legend
    leg_y = BOT + 6.5
    ax.plot([ix0, ix1], [leg_y + 1.0, leg_y + 1.0], color=RULE, lw=0.4)
    ax.text(ix0, leg_y, sp("LEGEND  ·  POWERS", 2),
            fontsize=5, fontname=F_MONO, color=VERMILION, va="top")
    # Legend drawn as actual shapes (text glyphs missing in serif italic)
    legend_pos = [(0, "filled", "strong & durable", VERMILION),
                  (18, "outline", "present, partial", INK_SOFT),
                  (36, "small-dot", "weak", GRAY),
                  (54, "none", "absent", GRAY_LIGHT)]
    for offset, shape, txt, c in legend_pos:
        cx = ix0 + offset
        cy = leg_y - 1.6
        if shape == "filled":
            ax.add_patch(mpatches.Circle((cx, cy), 0.55, fc=c, ec=c, lw=0))
        elif shape == "outline":
            ax.add_patch(mpatches.Circle((cx, cy), 0.45, fc="none", ec=c, lw=0.6))
        elif shape == "small-dot":
            ax.add_patch(mpatches.Circle((cx, cy), 0.18, fc=c, ec=c, lw=0))
        # else nothing for "absent"
        ax.text(cx + 1.4, cy, txt, fontsize=5, fontname=F_SERIF_IT, color=INK_SOFT, va="center")
    ax.text(ix0, leg_y - 3.0,
            "Discipline: mindshare is not a power. ARR is not a power. A power requires benefit + barrier.",
            fontsize=4.8, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE X — JTBD CANVAS (7 jobs × 8 phases)
# ============================================================

def plate_x(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "X", "JTBD Canvas · Agent",
        "Seven ecosystem-level jobs the agent stack is hired for · Ulwick eight-phase map · Conclude is universally unserved.",
        "Septem opera quaesita · phases octo · Concludere universaliter desertum",
        "PLATE X OF XI")
    ix0, ix1 = L + 1.0, R - 1.0

    phases = ["Define", "Locate", "Prepare", "Confirm", "Execute", "Monitor", "Modify", "Conclude"]
    # Heat: 0=well-served (light), 1=partial, 2=under-served (dark)
    jobs = [
        ("J1", "Back-office task unattended",   [2, 1, 1, 2, 1, 1, 2, 2]),
        ("J2", "CX resolution + escalation",    [1, 1, 2, 1, 0, 1, 2, 2]),
        ("J3", "Code change · review · merge",  [2, 1, 1, 2, 0, 1, 1, 2]),
        ("J4", "Operate a SaaS for the user",   [1, 1, 2, 2, 1, 2, 1, 2]),
        ("J5", "Stay current · act on change",  [1, 1, 1, 2, 1, 2, 2, 2]),
        ("J6", "Pass procurement gauntlet",     [2, 1, 2, 2, 2, 2, 2, 2]),
        ("J7", "Ramp a new-role agent-pair",    [2, 2, 2, 2, 1, 2, 2, 2]),
    ]

    label_w = 28
    cell_w = (ix1 - ix0 - label_w) / len(phases)
    band_y = TOP - 0.5
    ax.text(ix0, band_y, sp("JOB", 2),
            fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
    for i, ph in enumerate(phases):
        x = ix0 + label_w + i * cell_w + cell_w / 2
        ax.text(x, band_y, sp(ph.upper(), 1),
                fontsize=4.8, fontname=F_MONO, color=VERMILION, va="top", ha="center", rotation=20)
    ax.plot([ix0, ix1], [TOP - 3.0, TOP - 3.0], color=RULE, lw=0.5)

    row_h = (TOP - 4 - BOT - 18) / len(jobs)
    palette = ["#E4D8B6", OCHRE, VERMILION]  # well / partial / under
    for i, (num, name, heat) in enumerate(jobs):
        y_top = TOP - 4 - i * row_h
        y_mid = y_top - row_h / 2
        y_bot = y_top - row_h
        ax.plot([ix0, ix1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.3)
        ax.text(ix0 + 0.3, y_mid, num, fontsize=6.5, fontname=F_DMMONO,
                color=VERMILION, va="center")
        ax.text(ix0 + 4, y_mid, name, fontsize=6.5, fontname=F_DISPLAY, color=INK, va="center")
        for j, h in enumerate(heat):
            x = ix0 + label_w + j * cell_w
            ax.add_patch(mpatches.Rectangle((x + 0.5, y_bot + 0.5), cell_w - 1, row_h - 1,
                                            fc=palette[h], ec=INK_SOFT, lw=0.3, alpha=0.85))

    # Synthesis box
    sy = BOT + 12
    ax.plot([ix0, ix1], [sy + 1.2, sy + 1.2], color=RULE, lw=0.4)
    ax.text(ix0, sy, sp("UNDER-SERVED PATTERNS (CROSS-JOB)", 3),
            fontsize=5.2, fontname=F_MONO, color=VERMILION, va="top")
    bullets = [
        "1 · Conclude is universally unserved — signed evidence, warm handoff, provenance, change-log, decision-routing, agent taper",
        "2 · Modify by a non-engineer — replay UIs for engineers exist; cockpit UIs for line managers / CX leads / FP&A do not",
        "3 · Confirm (pre-flight) — PRMs internal at labs but not exposed to buyers; the difference between $25K and $250K ACV",
    ]
    for i, t in enumerate(bullets):
        ax.text(ix0, sy - 2.0 - i * 1.5, t, fontsize=5,
                fontname=F_SERIF, color=INK, va="top")

    over = [
        "Over-served · Execute on code (14+ funded); Locate / knowledge-search (consolidating to 2–3); Execute on inbound chat.",
    ]
    for i, t in enumerate(over):
        ax.text(ix0, sy - 7.5 - i * 1.5, t, fontsize=5,
                fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    # Legend
    leg_y = BOT + 5.5
    ax.text(ix0, leg_y, sp("HEAT MAP", 2),
            fontsize=5, fontname=F_MONO, color=VERMILION, va="top")
    legend = [("well-served", "#E4D8B6"), ("partial", OCHRE), ("under-served", VERMILION)]
    for i, (txt, col) in enumerate(legend):
        x = ix0 + i * 22
        ax.add_patch(mpatches.Rectangle((x, leg_y - 2.3), 2, 1, fc=col, ec=INK_SOFT, lw=0.3))
        ax.text(x + 2.5, leg_y - 1.8, txt, fontsize=5, fontname=F_SERIF_IT,
                color=INK_SOFT, va="center")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PLATE XI — ACTION PORTFOLIO (6/12/18 month)
# ============================================================

def plate_xi(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, "XI", "Action Portfolio · 6 / 12 / 18",
        "Seven refreshed Bets sequenced across three windows. Bet #1 first (claim power) · Bet #2 second (collect equity) · Bet #3 third (compound).",
        "Septem electa per tres fenestras temporis · ordo agendi",
        "PLATE XI OF XI")
    ix0, ix1 = L + 1.0, R - 1.0

    bets = [
        ("1", "Procurement Operating Standard", "5 / 5", VERMILION,
            ["Publish open Playbook (wk 12)", "30 expert interviews", "AI Gov sign-off audit"],
            ["3–5 paid engagements", "Procurement Audit reports", "Article 14 playbook"],
            ["SaaS productization decision", "$250–500K annual rev", "Three-product bundle"]),
        ("2", "Vertical Agent GTM Role", "5 / 5", VERMILION,
            ["NYC search · 10 targets", "Time offer before up-round", "Consulting alumni pipeline"],
            ["Sign at chosen vertical", "Close Confirm + Conclude gap", "Anthropic ARR resolution"],
            ["Deliver job · vertical", "Compound from inside", "Re-rank by Crux #1 outcome"]),
        ("3", "MCP-Native Practice", "4 / 5", OCHRE,
            ["Audit 10 SaaS · gateway pair", "Pair w/ Cloudflare · Kong", "Reframe to advisory"],
            ["Productize or sustain advisory", "Gateway-adjacent positioning", "Watch fork Crux #2"],
            ["Compound · advisory + Playbook", "Decide on platform vs. practice", ""]),
        ("4", "FinOps for Trajectories", "4 / 5", OCHRE,
            ["Free first audit · 5 cos", "Case study", "Per-trajectory rubric"],
            ["Fold into Bet #1 module", "Decide scale or absorb", ""],
            ["Decay window honest", "Bedrock auto-routing watch", ""]),
        ("5", "RAG + Memory Architecture", "4 / 5", OCHRE,
            ["Bundle as audit", "Memory architecture line", "Vendor-neutral guidance"],
            ["3 architecture audits", "Three-product practice", ""],
            ["Sustain · selective", "Track CRUX #5", ""]),
        ("6", "Operator Newsletter", "3 / 5", VERDIGRIS,
            ["Kit v1 · wk 4", "Cadence decision · wk 8", "JTBD Job 5 angle"],
            ["5K subs / 3 inbound · or kill", "Conclude-phase translation", ""],
            ["Sustain · paid tier", "Distribution layer for #1–#3", ""]),
        ("7", "VC Operating Partner", "3 / 5", VERDIGRIS,
            ["Background networking", "RAAIS · Betaworks · MAD", "No applications"],
            ["3 NYC funds · relationships", "Watch principal→operator", ""],
            ["Primary path if 1–3 stall", "Active applications Q4 '26", ""]),
    ]

    # Columns: Bet | 0–6 | 6–12 | 12–18
    label_w = 30
    col_w = (ix1 - ix0 - label_w) / 3
    band_y = TOP - 0.5
    ax.text(ix0, band_y, sp("BET", 2),
            fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
    headers = ["MONTHS 0–6 · PLANT", "MONTHS 6–12 · COMMIT", "MONTHS 12–18 · COMPOUND"]
    for i, h in enumerate(headers):
        x = ix0 + label_w + i * col_w + col_w / 2
        ax.text(x, band_y, sp(h, 1),
                fontsize=5.0, fontname=F_MONO, color=VERMILION, va="top", ha="center")
    ax.plot([ix0, ix1], [TOP - 3.0, TOP - 3.0], color=RULE, lw=0.5)

    row_h = (TOP - 4 - BOT - 18) / len(bets)
    for i, (num, name, stars, color, c1, c2, c3) in enumerate(bets):
        y_top = TOP - 4 - i * row_h
        y_mid = y_top - row_h / 2
        y_bot = y_top - row_h
        ax.plot([ix0, ix1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.3)
        # Bet number badge
        ax.add_patch(mpatches.Circle((ix0 + 1.2, y_mid), 1.1, fc=color, ec=color, lw=0))
        ax.text(ix0 + 1.2, y_mid, num, fontsize=7, fontname=F_DMMONO,
                color=PAPER, ha="center", va="center")
        # Bet name + stars
        ax.text(ix0 + 3.5, y_mid + 0.8, name, fontsize=6.5, fontname=F_DISPLAY,
                color=INK, va="center")
        ax.text(ix0 + 3.5, y_mid - 1.2, stars, fontsize=5.5, fontname=F_SERIF_DISP,
                color=color, va="center")
        # Column content
        for col, items in enumerate([c1, c2, c3]):
            x = ix0 + label_w + col * col_w + 0.5
            for k, it in enumerate(items):
                if not it:
                    continue
                ax.add_patch(mpatches.Circle((x + 0.4, y_mid + 1.5 - k * 1.5), 0.18,
                                              fc=color, ec=color, lw=0))
                ax.text(x + 1.2, y_mid + 1.5 - k * 1.5, it,
                        fontsize=4.6, fontname=F_SERIF, color=INK_SOFT, va="center")

    # Sequencing callout
    sy = BOT + 12
    ax.plot([ix0, ix1], [sy + 1.2, sy + 1.2], color=RULE, lw=0.4)
    ax.text(ix0, sy, sp("SEQUENCING · THE VOL III DELTA", 3),
            fontsize=5.2, fontname=F_MONO, color=VERMILION, va="top")
    ax.text(ix0, sy - 2,
            "The five-framework convergence reorders the prior addendum: Bet #1 first (claim Process Power at Meta-B), Bet #2 second (collect equity at a power-holder), Bet #3 third (advisory practice compounding from both). Bets 4–5 fold into Bet #1 as modules; Bet #6 is the distribution layer; Bet #7 the long-arc fallback.",
            fontsize=5, fontname=F_SERIF, color=INK, va="top", wrap=True)

    # Footer cruxes
    cy = BOT + 5.5
    ax.text(ix0, cy, sp("CRUXES THAT RE-RANK EVERYTHING", 2),
            fontsize=5, fontname=F_MONO, color=VERMILION, va="top")
    cruxes = [
        "C1 · Anthropic ARR $24B vs $30B · Q3 '26",
        "C2 · MCP commons vs fork · EOY '26",
        "C3 · OSWorld 65% on frontier · Q3 '26",
        "C4 · EU AI Act Article 14 teeth · late '26",
        "C5 · Standalone memory absorbed vs niche · H2 '26",
    ]
    for i, c in enumerate(cruxes):
        x = ix0 + (i % 3) * (ix1 - ix0) / 3
        y = cy - 1.6 - (i // 3) * 1.4
        ax.text(x, y, c, fontsize=4.8, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# Build
# ============================================================

if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        plate_vii(pdf)
        plate_viii(pdf)
        plate_ix(pdf)
        plate_x(pdf)
        plate_xi(pdf)
    print(f"Wrote {OUT_PATH} · {os.path.getsize(OUT_PATH)/1024:.1f} KB")
