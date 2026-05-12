"""
SUBSTRATE — Master Section (Plate Ω)
The whole stack with cross-layer flows, feedback loops, binding constraints,
and the wrapping meta-forces.
"""
import os
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.path import Path
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
import numpy as np

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

PAGE_W, PAGE_H = 11.0, 17.0
DPI = 300

OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-stack/AI_STACK_MASTER_PLATE.pdf"


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


def page_frame(ax):
    LEFT, RIGHT, TOP, BOTTOM = 6.0, 94.0, 149.5, 7.5
    rect = mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                              fill=False, ec=RULE, lw=0.55)
    ax.add_patch(rect)
    ax.plot([LEFT, RIGHT], [TOP - 7.5, TOP - 7.5], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 5.0, BOTTOM + 5.0], color=RULE, lw=0.45)

    # Margin tick rule (left)
    ax.plot([LEFT - 2.6, LEFT - 2.6], [BOTTOM + 5.0, TOP - 7.5], color=RULE, lw=0.4)
    n_ticks = 28
    ys = np.linspace(BOTTOM + 5.0, TOP - 7.5, n_ticks)
    for i, y in enumerate(ys):
        long = (i % 5 == 0)
        ax.plot([LEFT - 2.6 - (1.0 if long else 0.5), LEFT - 2.6], [y, y],
                color=RULE, lw=0.35)
        if long:
            ax.text(LEFT - 4.1, y, f"{i*5:02d}", ha="right", va="center",
                    fontsize=4.4, fontname=F_DMMONO, color=GRAY)

    # Title block
    ax.text(LEFT, TOP - 1.4, sp("AN ATLAS OF THE INTELLIGENCE STRATA  ·  MASTER SECTION", 4),
            ha="left", va="top", fontsize=6.0, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 2.6, "THE WHOLE STACK",
            ha="left", va="top", fontsize=22, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.0, TOP - 2.8, sp("MASTER PLATE", 2),
            ha="right", va="top", fontsize=7.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4,
            "Orchestration · entanglement · feedback loops · binding constraints — the AI stack as a single connected system.",
            ha="left", va="top", fontsize=6.5, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 6.5,
            "Tota machina mentis artificialis · quomodo strata simul operentur",
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)

    # Plate badge (use M for Master since Big Shoulders lacks Omega glyph)
    ax.add_patch(mpatches.Circle((RIGHT - 1.6, TOP - 2.6), 1.1, fill=False, ec=VERMILION, lw=0.7))
    ax.text(RIGHT - 1.6, TOP - 2.6, "M", ha="center", va="center",
            fontsize=8, fontname=F_MONO_BOLD, color=VERMILION)

    # Footer
    ax.text(LEFT, BOTTOM + 3.4, sp("SUBSTRATE  ·  MASTER PLATE  ·  THE WHOLE STACK", 3),
            ha="left", va="top", fontsize=4.8, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.8, sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.8, "MASTER PLATE", ha="right", va="top",
            fontsize=5.4, fontname=F_DMMONO, color=GRAY)

    return LEFT, RIGHT, TOP - 8.0, BOTTOM + 5.3


def curved_arrow(ax, p_start, p_end, p_control, color, lw=0.6, alpha=0.7,
                 arrow_size=1.0, label=None, label_offset=(0, 0), label_color=None):
    """Draw a curved arrow with optional label."""
    verts = [p_start, p_control, p_end]
    codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
    path = Path(verts, codes)
    patch = mpatches.PathPatch(path, fc='none', ec=color, lw=lw, alpha=alpha)
    ax.add_patch(patch)
    # Arrow head
    # Direction at end: from control to end
    dx = p_end[0] - p_control[0]
    dy = p_end[1] - p_control[1]
    L = np.sqrt(dx*dx + dy*dy) or 1
    dx, dy = dx/L, dy/L
    # Perpendicular
    px, py = -dy, dx
    a1 = (p_end[0] - dx*arrow_size + px*arrow_size*0.5,
          p_end[1] - dy*arrow_size + py*arrow_size*0.5)
    a2 = (p_end[0] - dx*arrow_size - px*arrow_size*0.5,
          p_end[1] - dy*arrow_size - py*arrow_size*0.5)
    ax.add_patch(mpatches.Polygon([p_end, a1, a2], closed=True,
                                    fc=color, ec=color, alpha=alpha))
    if label:
        # Label at midpoint of control
        lx = p_control[0] + label_offset[0]
        ly = p_control[1] + label_offset[1]
        ax.text(lx, ly, label, fontsize=4.6, fontname=F_MONO,
                color=label_color or color, alpha=0.95,
                ha="center", va="center")


def main():
    with PdfPages(OUT_PATH) as pdf:
        fig, ax = new_page()
        L, R, TOP, BOT = page_frame(ax)

        # ========== Layout ==========
        # The stack column sits in the middle-left. Left rail must clear col_x0.
        col_x0 = 24.0
        col_x1 = 60.0
        col_top = TOP - 2.0
        col_bot = BOT + 16.0   # leave room for meta-strata band at bottom

        # 14 strata bands, top (XIV) to bottom (I)
        strata = [
            ("XIV",  "USER",                "homo · chat · search · code · agent · voice"),
            ("XIII", "APPLICATION · AGENT", "Sierra · Cursor · Harvey · ChatGPT · Glean"),
            ("XII",  "ORCHESTRATION",       "MCP · LangGraph · Agent SDKs · gateways"),
            ("XI",   "RETRIEVAL · MEMORY",  "vector DBs · embeddings · rerankers · memory"),
            ("X",    "INFERENCE",           "vLLM · SGLang · Dynamo · MLX · quantization"),
            ("IX",   "MODEL · PROVIDERS",   "Anthropic · OpenAI · Google · DeepSeek · Mistral"),
            ("VIII", "POST-TRAINING",       "SFT · DPO · RLHF · RLVR · GRPO · CoT"),
            ("VII",  "PRE-TRAINING",        "Transformer · MoE · MLA · Mamba · diffusion-LM"),
            ("VI",   "DATA · CORPUS",       "CommonCrawl · FineWeb · licensed · synthetic"),
            ("V",    "PARALLELISM",         "FSDP · Megatron · DeepSpeed · JAX · Triton"),
            ("IV",   "FABRIC",              "NVLink · InfiniBand · UEC · 800G · CPO"),
            ("III",  "COMPUTE",             "H200 · B200 · GB300 · TPU · HBM · CoWoS"),
            ("II",   "FACILITY",            "racks · liquid cooling · busways · PUE · WUE"),
            ("I",    "POWER",               "PPA · SMR · gas · transformer · transmission"),
        ]
        n = len(strata)
        band_h = (col_top - col_bot) / n

        # Wardley stage per stratum: 0 = Genesis (vermilion), 1 = Custom (ochre),
        # 2 = Product (verdigris), 3 = Commodity (gray)
        wardley_stage = {
            "XIV": 3, "XIII": 2, "XII": 1, "XI": 2, "X": 2, "IX": 2,
            "VIII": 1, "VII": 2, "VI": 2, "V": 2, "IV": 2, "III": 2,
            "II": 2, "I": 3,
        }
        stage_color = {0: VERMILION, 1: OCHRE, 2: VERDIGRIS, 3: GRAY}
        stage_letter = {0: "G", 1: "C", 2: "P", 3: "U"}

        # Draw strata
        band_centers = {}
        for i, (num, name, comp) in enumerate(strata):
            y_top = col_top - i * band_h
            y_bot = y_top - band_h
            y_mid = (y_top + y_bot) / 2
            band_centers[num] = y_mid

            # Faint tint by Wardley stage
            tint = stage_color[wardley_stage[num]]
            ax.add_patch(mpatches.Rectangle((col_x0, y_bot + 0.1),
                                              col_x1 - col_x0,
                                              band_h - 0.2,
                                              fc=tint, ec='none', alpha=0.05))

            # Top/bottom rule
            ax.plot([col_x0, col_x1], [y_top, y_top], color=RULE, lw=0.4)

            # Numeral column
            ax.text(col_x0 + 0.5, y_mid + 0.3, num, ha="left", va="center",
                    fontsize=6.5, fontname=F_DMMONO, color=VERMILION)

            # Name in display caps
            ax.text(col_x0 + 5.5, y_mid + 0.6, name, ha="left", va="center",
                    fontsize=8.5, fontname=F_DISPLAY, color=INK)

            # Components in serif
            ax.text(col_x0 + 5.5, y_mid - 1.0, comp, ha="left", va="center",
                    fontsize=4.5, fontname=F_SERIF_IT, color=INK_SOFT)

            # Wardley stage chip on the right inside the band
            chip_x = col_x1 - 1.8
            ax.add_patch(mpatches.Circle((chip_x, y_mid + 0.3), 0.55,
                                          fc=tint, ec=tint, lw=0, alpha=0.7))
            ax.text(chip_x, y_mid + 0.3, stage_letter[wardley_stage[num]],
                    ha="center", va="center", fontsize=4.5,
                    fontname=F_MONO_BOLD, color=PAPER)

        # Closing rule at bottom of column
        ax.plot([col_x0, col_x1], [col_bot, col_bot], color=RULE, lw=0.5)
        ax.plot([col_x0, col_x0], [col_top, col_bot], color=RULE, lw=0.5)
        ax.plot([col_x1, col_x1], [col_top, col_bot], color=RULE, lw=0.5)

        # ========== Left rail: BINDING CONSTRAINTS ==========
        rail_left_x = L + 2.0
        rail_left_w = col_x0 - rail_left_x - 1.5   # ~16.5 units of clear label space
        label_right_edge = col_x0 - 1.0
        # Header
        ax.text(rail_left_x, col_top, sp("BINDING", 1),
                fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
        ax.text(rail_left_x, col_top - 1.0, sp("CONSTRAINTS", 1),
                fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
        ax.plot([rail_left_x, label_right_edge],
                [col_top - 2.3, col_top - 2.3], color=VERMILION, lw=0.4)

        # Constraint pins — staggered so multiple constraints per stratum do not overlap
        # Each entry: (stratum, name, detail, vertical_offset_from_band_center)
        constraints = [
            ("III", "HBM4",            "SK Hynix 62% · 2026 pre-booked",  +1.5),
            ("III", "CoWoS-L pkg",     "TSMC bottleneck · ≈100 KWPM",     -1.5),
            ("II",  "Transformers",    "≈120 wk lead · Wood Mackenzie",    0.0),
            ("I",   "Interconnect q",  "≈2,290 GW · 4–7 yr backlog",      +1.3),
            ("I",   "Power perms",     "permitting >10 yr greenfield",    -1.3),
            ("VI",  "Licensed data",   "Bartz $1.5 B · CF default-block",  0.0),
            ("VIII","Alignment talent","≈200 senior researchers",          0.0),
            ("V",   "Frontier ML team","fewer than 50 shipped >100B",      0.0),
            ("XII", "MCP convergence", "Crux 3 · H2 2026",                 0.0),
        ]
        for num, name, detail, dy in constraints:
            y = band_centers[num] + dy
            # Pin on the column edge
            pin_x = col_x0 - 0.25
            ax.add_patch(mpatches.Circle((pin_x, y), 0.32,
                                          fc=VERMILION, ec=VERMILION, lw=0))
            # Short connector line from label area to pin
            ax.plot([label_right_edge + 0.2, pin_x - 0.4], [y, y],
                    color=VERMILION, lw=0.3, alpha=0.6)
            # Label: name above the line, detail below
            ax.text(label_right_edge, y + 0.3, name, fontsize=4.7,
                    fontname=F_DISPLAY_REG, color=INK, ha="right", va="bottom")
            ax.text(label_right_edge, y - 0.3, detail, fontsize=3.5,
                    fontname=F_SERIF_IT, color=GRAY, ha="right", va="top")

        # ========== Right rail: FLOWS & ENTANGLEMENTS ==========
        # The right rail is reorganised into two compact sections:
        #   (A) directional flows — two short labeled arrows side by side
        #   (B) the feedback-loops legend — five named loops
        # Both are squeezed into the upper-right area, leaving the lower-right
        # for an "interplay summary" box.

        rail_right_x = col_x1 + 7.0   # leave room for data-flywheel curve labels
        rail_right_w = R - rail_right_x - 1.5

        # (A) DIRECTIONAL FLOWS — compact, two short arrows
        flow_top = col_top
        ax.text(rail_right_x, flow_top, sp("DIRECTIONAL FLOWS", 1),
                fontsize=5.5, fontname=F_MONO, color=VERDIGRIS, va="top")
        ax.plot([rail_right_x, R - 1.5], [flow_top - 1.5, flow_top - 1.5],
                color=VERDIGRIS, lw=0.4)

        flow_y_top = flow_top - 3.2
        flow_y_bot = flow_y_top - 12.0   # much shorter

        # Capital flow DOWN
        cf_x = rail_right_x + 1.2
        ax.annotate('', xy=(cf_x, flow_y_bot), xytext=(cf_x, flow_y_top),
                    arrowprops=dict(arrowstyle='-|>', color=VERMILION,
                                    lw=1.4, alpha=0.9))
        ax.text(cf_x + 0.9, flow_y_top - 0.2, "CAPITAL ↓",
                fontsize=5.8, fontname=F_DISPLAY, color=VERMILION, va="top")
        ax.text(cf_x + 0.9, flow_y_top - 2.0,
                "user payments → app revenue →",
                fontsize=4.0, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
        ax.text(cf_x + 0.9, flow_y_top - 2.9,
                "API spend → inference cost →",
                fontsize=4.0, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
        ax.text(cf_x + 0.9, flow_y_top - 3.8,
                "compute capex → PPA → grid",
                fontsize=4.0, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
        ax.text(cf_x + 0.9, flow_y_top - 5.4,
                "$660–770 B / yr aggregate 2026",
                fontsize=4.0, fontname=F_MONO_BOLD, color=VERMILION, va="top")

        # Capability flow UP
        cap_x = rail_right_x + 1.2
        cap_y_top = flow_y_top - 6.8
        cap_y_bot = flow_y_bot
        ax.annotate('', xy=(cap_x, cap_y_top), xytext=(cap_x, cap_y_bot),
                    arrowprops=dict(arrowstyle='-|>', color=VERDIGRIS,
                                    lw=1.4, alpha=0.9))
        ax.text(cap_x + 0.9, cap_y_top - 0.2, "CAPABILITY ↑",
                fontsize=5.8, fontname=F_DISPLAY, color=VERDIGRIS, va="top")
        ax.text(cap_x + 0.9, cap_y_top - 2.0,
                "MWh → FLOPs → tokens → weights",
                fontsize=4.0, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
        ax.text(cap_x + 0.9, cap_y_top - 2.9,
                "→ API → tool calls → apps → work",
                fontsize=4.0, fontname=F_SERIF_IT, color=INK_SOFT, va="top")
        ax.text(cap_x + 0.9, cap_y_top - 4.4,
                "the value cascade",
                fontsize=4.0, fontname=F_MONO_BOLD, color=VERDIGRIS, va="top")

        # (B) FEEDBACK LOOPS
        loop_top = flow_y_bot - 3.5
        ax.text(rail_right_x, loop_top, sp("THE FEEDBACK LOOPS", 1),
                fontsize=5.5, fontname=F_MONO, color=OCHRE, va="top")
        ax.plot([rail_right_x, R - 1.5], [loop_top - 1.5, loop_top - 1.5],
                color=OCHRE, lw=0.4)

        loops = [
            ("●", "DATA FLYWHEEL",
             "XIV → VI → VII → IX → XIII → XIV   ·   user outputs become training data, retrain models, redeploy in apps, attract more users."),
            ("●", "EVAL FEEDBACK",
             "XIII → XII (eval) → VIII → IX → XIII   ·   production failures feed into eval datasets, drive post-training updates."),
            ("●", "COST PRESSURE",
             "III (HBM, CoWoS) → IX (token price) → X (inference econ) → XIII (app margin)   ·   silicon supply propagates upward through pricing."),
            ("●", "MCP JUNCTION",
             "XII connects horizontally to XI (memory), IX (models), XIII (apps), and the user's external systems — protocol-level glue."),
            ("●", "AGENT LOOP",
             "XIV → XIII → XII (tools) → external system → XII → XIII → XIV   ·   user delegates a task, the agent acts on the world, returns result."),
        ]
        # Tighter spacing; right-rail is narrower so wrap at ~38 chars
        for i, (mk, title, body) in enumerate(loops):
            y = loop_top - 2.6 - i * 5.6
            ax.add_patch(mpatches.Circle((rail_right_x + 0.3, y), 0.35,
                                          fc=OCHRE, ec=OCHRE, lw=0))
            ax.text(rail_right_x + 1.0, y + 0.2, title,
                    fontsize=5.4, fontname=F_DISPLAY, color=INK, va="center")
            words = body.split()
            lines = []
            cur = ""
            for w in words:
                test = (cur + " " + w).strip()
                if len(test) > 38:
                    if cur:
                        lines.append(cur)
                    cur = w
                else:
                    cur = test
            if cur:
                lines.append(cur)
            for li, ln in enumerate(lines[:4]):  # cap at 4 lines per loop
                ax.text(rail_right_x + 1.0, y - 1.0 - li * 0.95, ln,
                        fontsize=4.0, fontname=F_SERIF_IT, color=INK_SOFT, va="center")

        # (C) THE INTERPLAY IN ONE SENTENCE
        thesis_top = loop_top - 3.0 - len(loops) * 5.6 - 1.5
        ax.text(rail_right_x, thesis_top, sp("THE INTERPLAY · IN ONE SENTENCE", 1),
                fontsize=5.0, fontname=F_MONO, color=VERMILION, va="top")
        ax.plot([rail_right_x, R - 1.5], [thesis_top - 1.3, thesis_top - 1.3],
                color=VERMILION, lw=0.4)

        thesis_lines = [
            "Power and packaging set the",
            "ceiling. Compute and fabric set the",
            "shape. Data and post-training set",
            "the quality. Inference and serving",
            "set the price. Orchestration sets",
            "the surface. Application sets the",
            "value. The user closes the loop —",
            "and the loop, closed, feeds every",
            "layer beneath.",
        ]
        for i, line in enumerate(thesis_lines):
            ax.text(rail_right_x, thesis_top - 2.6 - i * 1.15, line,
                    fontsize=4.6, fontname=F_SERIF_DISP_IT,
                    color=INK, va="top")

        # ========== Cross-layer flow lines drawn on the column itself ==========
        # We draw a few key cross-layer arrows directly through / alongside the column
        # to make the entanglements visible.

        # We draw cross-layer flow arcs in a dedicated channel between the column
        # and the right rail. Channel runs from col_x1 to about col_x1+3.5.
        codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
        channel_w = 3.5

        # 1) Data flywheel — User (XIV) down to Data (VI) on the right side
        y_xiv = band_centers["XIV"]
        y_vi = band_centers["VI"]
        verts = [(col_x1 + 0.2, y_xiv),
                 (col_x1 + channel_w, (y_xiv + y_vi) / 2),
                 (col_x1 + 0.2, y_vi)]
        ax.add_patch(mpatches.PathPatch(Path(verts, codes), fc='none',
                                          ec=OCHRE, lw=0.9, alpha=0.85))
        ax.annotate('', xy=(col_x1 + 0.2, y_vi), xytext=(col_x1 + 1.0, y_vi + 1.8),
                    arrowprops=dict(arrowstyle='-|>', color=OCHRE, lw=0.9, alpha=0.9))
        # Label aligned with the curve's bulge
        ax.text(col_x1 + channel_w + 0.2, (y_xiv + y_vi) / 2 + 0.5,
                "DATA", fontsize=4.6, fontname=F_MONO_BOLD,
                color=OCHRE, va="center", ha="left")
        ax.text(col_x1 + channel_w + 0.2, (y_xiv + y_vi) / 2 - 0.5,
                "FLYWHEEL", fontsize=4.6, fontname=F_MONO_BOLD,
                color=OCHRE, va="center", ha="left")

        # 2) Eval feedback — Application (XIII) down to Post-training (VIII)
        y_xiii = band_centers["XIII"]
        y_viii = band_centers["VIII"]
        verts = [(col_x1 + 0.2, y_xiii),
                 (col_x1 + channel_w * 0.55, (y_xiii + y_viii) / 2),
                 (col_x1 + 0.2, y_viii)]
        ax.add_patch(mpatches.PathPatch(Path(verts, codes), fc='none',
                                          ec=VERDIGRIS, lw=0.7, alpha=0.85))
        ax.annotate('', xy=(col_x1 + 0.2, y_viii), xytext=(col_x1 + 0.7, y_viii + 1.2),
                    arrowprops=dict(arrowstyle='-|>', color=VERDIGRIS, lw=0.8, alpha=0.9))
        ax.text(col_x1 + channel_w * 0.55 + 0.2, (y_xiii + y_viii) / 2,
                "EVAL", fontsize=4.4, fontname=F_MONO_BOLD,
                color=VERDIGRIS, va="center", ha="left")

        # 3) MCP junction at XII — annotated on the left of the column
        y_xii = band_centers["XII"]
        ax.annotate('', xy=(col_x0 - 0.3, y_xii), xytext=(col_x0 - 2.4, y_xii),
                    arrowprops=dict(arrowstyle='<|-|>', color=INDIGO, lw=0.7, alpha=0.85))
        ax.text(col_x0 - 2.7, y_xii + 0.4, "MCP",
                fontsize=4.6, fontname=F_MONO_BOLD, color=INDIGO, ha="right", va="bottom")
        ax.text(col_x0 - 2.7, y_xii - 0.4, "junction",
                fontsize=3.6, fontname=F_SERIF_IT, color=INDIGO, ha="right", va="top")

        # Cost-pressure cascade arrow REMOVED from this position to avoid clutter;
        # the COST PRESSURE feedback loop is already named in the right rail list.

        # ========== Bottom band: META-STRATA AS FORCES ==========
        meta_top = col_bot - 1.5
        meta_bot = BOT + 6.5
        meta_h = meta_top - meta_bot
        meta_x0 = L + 1.5
        meta_x1 = R - 1.5
        meta_w = (meta_x1 - meta_x0) / 4

        # Section header
        ax.text(meta_x0, meta_top + 1.5, sp("FORCES ACTING ON THE WHOLE STACK  ·  META-STRATA", 2),
                fontsize=5.5, fontname=F_MONO, color=VERMILION, va="top")
        ax.plot([meta_x0, meta_x1], [meta_top + 0.4, meta_top + 0.4],
                color=VERMILION, lw=0.5)

        metas = [
            ("M-A", "SAFETY · ALIGNMENT", VERMILION,
             "Anthropic RSP v3.1 · ASL-3 deployed · ASL-4 partial · Constitutional AI · interpretability · model welfare"),
            ("M-B", "REGULATION",         OCHRE,
             "EU AI Act GPAI 8/2025 · transparency 8/2026 · CA SB 53 · TAKE IT DOWN · C2PA · Bartz $1.5B"),
            ("M-C", "ECONOMICS",          VERDIGRIS,
             "Hyperscaler capex $660–770 B / yr · Stargate $500 B · Anthropic ARR $24–30 B · margin compression"),
            ("M-D", "GEOPOLITICS",        INDIGO,
             "TSMC 90% lead logic · H20 / B30A export saga · Stargate UAE 1 GW · Humain KSA · sovereign AI"),
        ]
        for i, (num, name, color, detail) in enumerate(metas):
            mx0 = meta_x0 + i * meta_w
            mx1 = mx0 + meta_w - 0.6
            mid_y = (meta_top + meta_bot) / 2

            # Card border
            ax.add_patch(mpatches.Rectangle((mx0, meta_bot), meta_w - 0.6, meta_h,
                                              fill=False, ec=color, lw=0.4))

            # Up-arrow pointing toward the column (force acting upward)
            arrow_x = mx0 + (meta_w - 0.6) / 2
            ax.annotate('', xy=(arrow_x, meta_top + 0.3), xytext=(arrow_x, meta_top - 0.6),
                        arrowprops=dict(arrowstyle='-|>', color=color, lw=0.6, alpha=0.7))

            # Numeral
            ax.text(mx0 + 0.8, meta_top - 1.0, num, fontsize=6,
                    fontname=F_DMMONO, color=color, va="top")
            # Name
            ax.text(mx0 + 0.8, meta_top - 2.6, name, fontsize=7.5,
                    fontname=F_DISPLAY, color=INK, va="top")
            # Detail (wrap)
            words = detail.split()
            lines = []
            cur = ""
            for w in words:
                test = (cur + " " + w).strip()
                if len(test) > 32:
                    if cur:
                        lines.append(cur)
                    cur = w
                else:
                    cur = test
            if cur:
                lines.append(cur)
            for li, ln in enumerate(lines):
                ax.text(mx0 + 0.8, meta_top - 4.2 - li * 1.1, ln,
                        fontsize=4.2, fontname=F_SERIF_IT, color=INK_SOFT, va="top")

        # ========== Top legend strip ==========
        legend_y = TOP - 0.6
        # Wardley stage chips legend
        leg_items = [
            ("G", VERMILION, "Genesis"),
            ("C", OCHRE,     "Custom"),
            ("P", VERDIGRIS, "Product"),
            ("U", GRAY,      "Commodity"),
        ]
        lx0 = R - 36
        ax.text(lx0 - 1, legend_y, sp("WARDLEY STAGE", 1),
                fontsize=4.4, fontname=F_MONO, color=GRAY, ha="right", va="center")
        for i, (letter, color, desc) in enumerate(leg_items):
            cx = lx0 + i * 8.0
            ax.add_patch(mpatches.Circle((cx, legend_y), 0.55,
                                           fc=color, ec=color, lw=0, alpha=0.7))
            ax.text(cx, legend_y, letter, ha="center", va="center",
                    fontsize=4.4, fontname=F_MONO_BOLD, color=PAPER)
            ax.text(cx + 0.9, legend_y, desc, ha="left", va="center",
                    fontsize=4.0, fontname=F_SERIF_IT, color=GRAY)

        # ========== Save ==========
        pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
        plt.close(fig)

        d = pdf.infodict()
        d["Title"] = "SUBSTRATE — Master Plate"
        d["Author"] = "Compiled for A. Yedi"
        d["Subject"] = "The whole AI stack as a single connected system"

    print("Wrote", OUT_PATH)


if __name__ == "__main__":
    main()
