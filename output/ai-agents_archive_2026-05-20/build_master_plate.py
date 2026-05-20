"""
SUBSTRATE · Vol III · Master Plate (Plate M).
The agent layer as a single connected system — strata, flows, feedback loops,
binding constraints, wrapping meta-forces, and the seven Bets sequenced.
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
GRAY_FAINT = "#E4DCC4"
RULE = "#2A211B"
VERMILION = "#A6371F"
VERDIGRIS = "#456C5C"
OCHRE = "#A37425"
INDIGO = "#3D4A6B"

PAGE_W, PAGE_H = 15.4, 23.8
DPI = 300
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents/AI_AGENTS_MASTER_PLATE.pdf"


def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 154.5)
    ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax):
    LEFT, RIGHT, TOP, BOTTOM = 6.0, 94.0, 149.5, 7.5
    ax.add_patch(mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                                    fill=False, ec=RULE, lw=0.55))
    ax.plot([LEFT, RIGHT], [TOP - 7.5, TOP - 7.5], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 5.0, BOTTOM + 5.0], color=RULE, lw=0.45)
    # Margin tick rule
    ax.plot([LEFT - 2.6, LEFT - 2.6], [BOTTOM + 5.0, TOP - 7.5], color=RULE, lw=0.4)
    ys = np.linspace(BOTTOM + 5.0, TOP - 7.5, 28)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([LEFT - 2.6 - (1.0 if long else 0.5), LEFT - 2.6], [y, y], color=RULE, lw=0.35)
        if long:
            ax.text(LEFT - 4.1, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=10, fontname=F_DMMONO, color=GRAY)
    # Title block
    ax.text(LEFT, TOP - 1.4, sp("AN ATLAS OF THE AGENT STRATA  ·  MASTER SECTION", 4),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 2.6, "THE AGENT, SEEN WHOLE",
            ha="left", va="top", fontsize=26.4, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.0, TOP - 2.8, sp("MASTER PLATE", 2),
            ha="right", va="top", fontsize=10, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4,
            "Ten sub-strata · four wrapping forces · cross-layer flows · binding constraints · sequenced Bets — the agent layer as a single connected system.",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 6.5,
            "Stratum agenticum tota machina · quomodo strata simul operentur",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_IT, color=GRAY)
    # Plate badge — use 'M' since Big Shoulders lacks Omega
    ax.add_patch(mpatches.Circle((RIGHT - 1.6, TOP - 2.6), 1.1, fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 1.6, TOP - 2.6, "M", ha="center", va="center",
            fontsize=10, fontname=F_MONO_BOLD, color=VERMILION)
    # Footer
    ax.text(LEFT, BOTTOM + 3.0, sp("SUBSTRATE  ·  VOL III  ·  MASTER PLATE", 3),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.4, sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=10, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, sp("MASTER", 2), ha="right", va="top",
            fontsize=10, fontname=F_DMMONO, color=GRAY)
    return LEFT, RIGHT, TOP - 7.5, BOTTOM + 5.0


def curved_flow(ax, x0, y0, x1, y1, color=GRAY, lw=0.5, alpha=0.65, label=None,
                ctrl_offset=12, label_offset=0.6):
    """Draw a smooth Bezier-like curve from (x0,y0) to (x1,y1)."""
    cx = (x0 + x1) / 2 + ctrl_offset
    cy = (y0 + y1) / 2
    verts = [(x0, y0), (cx, cy), (x1, y1)]
    codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
    path = Path(verts, codes)
    patch = mpatches.PathPatch(path, fill=False, ec=color, lw=lw, alpha=alpha)
    ax.add_patch(patch)
    if label:
        ax.text(cx + label_offset, cy, label, fontsize=10, fontname=F_SERIF_IT,
                color=color, va="center", alpha=0.9)


def page_master(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax)

    # ---------- Layout zones ----------
    col_x0 = L + 8                     # central stack starts here
    col_x1 = col_x0 + 38               # central stack ends here
    constraint_x = L + 1               # left margin column
    bet_x0 = col_x1 + 14               # bets column
    bet_x1 = R - 1.5

    # Meta-strata wrapping band (drawn as faint background panels around the column)
    meta_band_top = TOP - 1
    meta_band_bot = BOT + 26
    ax.add_patch(mpatches.Rectangle((col_x0 - 4, meta_band_bot),
                                     col_x1 - col_x0 + 8, meta_band_top - meta_band_bot,
                                     fc=GRAY_FAINT, ec=GRAY_LIGHT, lw=0.4, alpha=0.55))

    # ---------- The agent column ----------
    strata = [
        ("X",    "END-USER · SURFACES",     "form factor binds enterprise adoption · WhatsApp = global majority"),
        ("IX",   "VERTICAL · PRODUCTS",     "Sierra · Decagon · Glean · Harvey · Hippocratic · Hebbia · Rogo · Clay"),
        ("VIII", "RUNTIME · SAFETY",        "indirect prompt injection unsolved · mostly absorbed by hyperscalers"),
        ("VII",  "EVAL · OBSERVABILITY",    "signed reproducible reports = unclaimed flag · OTel GenAI Jan '26"),
        ("VI",   "ACTION · SURFACES",       "sandbox · browser · computer · voice · operational layer holds margin"),
        ("V",    "PLANNING · REASONING",    "ReAct + planner-executor + verifier · 70–85% tokens on cheap tier"),
        ("IV",   "MEMORY · STATE",          "RAG with writes · consumer absorbed · compliance niche"),
        ("III",  "TOOL · PROTOCOL",         "MCP spec held · experience fragmenting · gateways durable"),
        ("II",   "AGENT · RUNTIMES",        "thinnest gross-margin layer · splitting along the model spine"),
        ("I",    "FOUNDATION · CAPABILITY", "OSWorld ~50 · per-step ~99% gates unattended autonomous"),
    ]
    n = len(strata)
    avail = (TOP - 5) - (BOT + 32)
    h = avail / n
    label_w = 18

    for i, (num, name, tagline) in enumerate(strata):
        y_top = TOP - 5 - i * h
        y_bot = y_top - h
        y_mid = (y_top + y_bot) / 2

        ax.plot([col_x0, col_x1], [y_top, y_top], color=RULE, lw=0.45)
        ax.plot([col_x0, col_x1], [y_bot, y_bot], color=RULE, lw=0.3)

        # Roman numeral
        ax.text(col_x0 + 0.6, y_mid + 0.4, num, ha="left", va="center",
                fontsize=10.2, fontname=F_DMMONO, color=VERMILION)
        # Stratum name
        ax.text(col_x0 + 5.8, y_mid + 0.8, name, ha="left", va="center",
                fontsize=10.2, fontname=F_DISPLAY, color=INK)
        # Tagline (italic)
        ax.text(col_x0 + 5.8, y_mid - 1.4, tagline, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # ---------- Cross-layer flows (Bezier arcs to the right) ----------
    # Flow positions (y) for each stratum
    flow_ys = {}
    for i, (num, _, _) in enumerate(strata):
        flow_ys[num] = TOP - 5 - i * h - h / 2

    flows = [
        # (from_num, to_num, label, color)
        ("VI", "VIII", "tool returns -> injection vector", VERMILION),
        ("III", "VI", "MCP -> tool surface", OCHRE),
        ("II", "I", "harness -> model coupling", GRAY),
        ("V", "I", "reasoning -> trajectory", VERDIGRIS),
        ("IX", "VI", "vertical -> action surface", OCHRE),
        ("IX", "VII", "vertical -> trajectory eval", VERDIGRIS),
        ("X", "IX", "form factor gates vertical buyer", VERMILION),
        ("IV", "I", "memory -> RL trajectory data", OCHRE),
        ("VIII", "VII", "guardrail -> eval surface", GRAY),
        ("I", "IX", "model walks up-stack (encroach)", VERMILION),
    ]
    for from_num, to_num, label, color in flows:
        y0 = flow_ys[from_num]
        y1 = flow_ys[to_num]
        x0 = col_x1 + 0.3
        x1 = col_x1 + 0.3
        # Use varying control offsets to spread the arcs
        ctrl = 4 + abs(y1 - y0) * 0.18
        curved_flow(ax, x0, y0, x1, y1, color=color, lw=0.5, alpha=0.5,
                    ctrl_offset=ctrl, label=label, label_offset=0.4)

    # ---------- Binding constraints (left side) ----------
    bc_top = TOP - 5
    ax.text(constraint_x, bc_top, sp("BINDING CONSTRAINTS", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.plot([constraint_x, constraint_x + 6], [bc_top - 0.8, bc_top - 0.8],
            color=RULE, lw=0.3)

    constraints = [
        ("I",  "per-step ~99%", "computer-use ceiling"),
        ("I",  "ctx > 32K", "reasoning regression"),
        ("III", "MCP forks", "spec held / experience splits"),
        ("VI", "OSWorld ~50%", "unattended autonomy gates"),
        ("VIII", "indirect PI", "unsolved across all vendors"),
        ("VII", "no signed reports", "procurement-readiness gap"),
        ("IX", "lab walk-up", "encroaches Sierra / Glean wedge"),
        ("X",  "form factor", "CISO + buyer + threat-model"),
        ("M-A", "ASL framework", "not in EU code / NIST / ISO"),
        ("M-B", "EU Art. 14", "agentic triggers caught"),
        ("M-C", "token price", "decline outpaces optim"),
        ("M-D", "sovereign", "data residency lever"),
    ]
    for i, (s, c, why) in enumerate(constraints):
        y = bc_top - 2.5 - i * 4.2
        ax.add_patch(mpatches.Circle((constraint_x + 0.4, y + 0.5), 0.7,
                                     fc=PAPER, ec=VERMILION, lw=0.5))
        ax.text(constraint_x + 0.4, y + 0.5, s, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=VERMILION)
        ax.text(constraint_x + 1.8, y + 1.0, c, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        ax.text(constraint_x + 1.8, y - 0.5, why, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=GRAY)

    # ---------- The Seven Bets sequenced (right side) ----------
    bet_top = TOP - 5
    ax.text(bet_x0, bet_top, sp("SEVEN BETS · SEQUENCED", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    ax.text(bet_x0, bet_top - 1.8,
            "Bet #1 first (claim Process Power) · Bet #2 second (collect equity) · Bet #3 third (compound)",
            ha="left", va="top", fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)
    ax.plot([bet_x0, bet_x1], [bet_top - 2.6, bet_top - 2.6], color=RULE, lw=0.3)

    bets = [
        ("1", "PROCUREMENT OPERATING STANDARD",
            "5 / 5", VERMILION,
            "open Playbook · 30 expert calls · Agent Procurement Rubric · the unclaimed flag at Meta-B"),
        ("2", "VERTICAL AGENT GTM ROLE",
            "5 / 5", VERMILION,
            "Sierra · Decagon · Glean · Harvey · Hippocratic · Hebbia · Rogo · Clay · Ramp · Runway · NYC peak Q2-Q3 '26"),
        ("3", "MCP-NATIVE PRACTICE (reframed)",
            "4 / 5", OCHRE,
            "advisory + gateway-adjacent · pair with Cloudflare / Kong / Pomerium · not productized servers"),
        ("4", "FINOPS FOR TRAJECTORIES",
            "4 / 5", OCHRE,
            "planner-executor audit · 12-mo window before Bedrock auto-routes · fold into Bet #1 module"),
        ("5", "RAG + MEMORY ARCHITECTURE",
            "4 / 5", OCHRE,
            "vendor-neutral architecture audit · memory architecture as service line · Crux #5 absorbed/niche"),
        ("6", "OPERATOR TRANSLATION NEWSLETTER",
            "3 / 5", VERDIGRIS,
            "Job 5 distribution layer · Conclude-phase translation · cross-pollinate Bet #1 downloads"),
        ("7", "VC OPERATING PARTNER",
            "3 / 5", VERDIGRIS,
            "long-arc fallback · principal-to-operator path active · primary if Bets 1-3 stall"),
    ]
    nb = len(bets)
    bet_avail = (TOP - 5 - 4) - (BOT + 32)
    bh = bet_avail / nb

    for i, (num, name, score, color, detail) in enumerate(bets):
        y_top = TOP - 5 - 4 - i * bh
        y_bot = y_top - bh
        y_mid = (y_top + y_bot) / 2
        ax.plot([bet_x0, bet_x1], [y_bot, y_bot], color=GRAY_LIGHT, lw=0.3)
        ax.add_patch(mpatches.Circle((bet_x0 + 1.2, y_mid + 0.5), 1.0,
                                     fc=color, ec=color, lw=0))
        ax.text(bet_x0 + 1.2, y_mid + 0.5, num, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=PAPER)
        ax.text(bet_x0 + 3.2, y_mid + 1.0, name, ha="left", va="center",
                fontsize=10, fontname=F_DISPLAY, color=INK)
        ax.text(bet_x0 + 3.2, y_mid - 0.5, score, ha="left", va="center",
                fontsize=10, fontname=F_DMMONO, color=color)
        ax.text(bet_x0 + 14, y_mid + 0.3, detail, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    # ---------- META-STRATA wrapping band (bottom) ----------
    meta_y = BOT + 17
    ax.plot([L + 1, R - 1], [meta_y + 1.2, meta_y + 1.2], color=RULE, lw=0.4)
    ax.text(L + 1, meta_y, sp("FOUR WRAPPING META-FORCES", 3),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERDIGRIS)
    meta = [
        ("META-A", "CAPABILITY SAFETY",
         "ASL · Preparedness · Frontier · METR · AISI", VERMILION),
        ("META-B", "REGULATION",
         "EU AI Act Art.14 · CA SB 53 · sectoral · Bartz · NYT", OCHRE),
        ("META-C", "ECONOMICS",
         "per-task · outcome pricing · planner-executor · FinOps", OCHRE),
        ("META-D", "GEOPOLITICS",
         "sovereign agents · export controls · jurisdictional siting", VERDIGRIS),
    ]
    for i, (k, name, blurb, color) in enumerate(meta):
        x = L + 1 + i * 23
        ax.add_patch(mpatches.Rectangle((x, meta_y - 7.5), 22, 5.5,
                                         fc=PAPER, ec=color, lw=0.4))
        ax.text(x + 0.8, meta_y - 2.5, k, fontsize=10, fontname=F_DMMONO,
                color=color, va="center")
        ax.text(x + 0.8, meta_y - 4.0, name, fontsize=10, fontname=F_DISPLAY,
                color=INK, va="center")
        ax.text(x + 0.8, meta_y - 6.0, blurb, fontsize=10, fontname=F_SERIF_IT,
                color=INK_SOFT, va="center")

    # ---------- CRUXES (bottom strip) ----------
    cy = BOT + 7.5
    ax.text(L + 1, cy, sp("FIVE CRUXES · ANSWER-EVENTS THAT RE-RANK EVERYTHING", 2),
            ha="left", va="top", fontsize=10, fontname=F_MONO, color=VERMILION)
    cruxes = [
        ("C1", "Anthropic ARR · $24B vs $30B · Q3 '26"),
        ("C2", "MCP commons vs silent fork · EOY '26"),
        ("C3", "OSWorld 65% on frontier · Q3 '26"),
        ("C4", "EU AI Act Art. 14 teeth · late '26"),
        ("C5", "Standalone memory · absorbed vs niche · H2 '26"),
    ]
    for i, (k, txt) in enumerate(cruxes):
        x = L + 1 + i * 18
        ax.add_patch(mpatches.Circle((x + 0.6, cy - 2.2), 0.8, fc=VERMILION, ec=VERMILION, lw=0))
        ax.text(x + 0.6, cy - 2.2, k, ha="center", va="center",
                fontsize=10, fontname=F_DMMONO, color=PAPER)
        ax.text(x + 2.2, cy - 2.2, txt, ha="left", va="center",
                fontsize=10, fontname=F_SERIF_IT, color=INK_SOFT)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        page_master(pdf)
    print(f"Wrote {OUT_PATH} · {os.path.getsize(OUT_PATH)/1024:.1f} KB")
