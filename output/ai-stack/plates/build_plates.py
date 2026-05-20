"""
AI_STACK_MASTER — Plate generator
=================================
Generates 5 SVG plates that accompany AI_STACK_MASTER.
Educational, NOT aesthetic. Black on white, one accent color (dark blue #1d4ed8).

Run from ai-stack-v2/ directory:
    python plates/build_plates.py

Output: plates/01_substrate_column.svg ... plates/05_cross_stratum_flows.svg
"""

import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
from matplotlib.lines import Line2D
import numpy as np

# -----------------------------------------------------------------------------
# Global style — binding per spec §8
# -----------------------------------------------------------------------------
ACCENT = "#1d4ed8"          # one accent color (saturated dark blue)
ACCENT_LIGHT = "#93c5fd"    # only used in heatmap gradient (a single hue)
BLACK = "#000000"
GRAY_MED = "#6b7280"
GRAY_LIGHT = "#d1d5db"
WHITE = "#ffffff"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["svg.fonttype"] = "none"   # keep text as text in SVG
plt.rcParams["axes.edgecolor"] = BLACK
plt.rcParams["axes.linewidth"] = 0.5
plt.rcParams["pdf.fonttype"] = 42

# Page sizes (inches). Letter portrait.
PAGE_W = 8.5
PAGE_H = 11.0

PLATES_DIR = Path(__file__).parent

# -----------------------------------------------------------------------------
# Canonical data (matches Ch 1, Ch 2, Ch 3)
# -----------------------------------------------------------------------------

# 14 primary strata + the joined XI–XII row. We render top-to-bottom I -> XIV.
# Each entry: (roman, name, evo_stage, binding_short)
STRATA = [
    ("I",     "POWER",                "Commodity/Utility",  "Transformers 130wk lead, 30% deficit"),
    ("II",    "FACILITY",             "Product",            "Liquid-cooling retrofit, WUE <0.20 L/kWh"),
    ("III",   "COMPUTE",              "Product",            "HBM4 / CoWoS-L 75-80 KWPM"),
    ("IV",    "FABRIC",               "Product",            "Optics + UALink silicon gap"),
    ("V",     "PARALLELISM",          "Product",            "Systems-talent thin; checkpoint loss"),
    ("VI",    "DATA",                 "Product",            "Copyright + Cloudflare 402 + provenance"),
    ("VII",   "PRETRAINING",          "Custom-Built",       "$1B+ run cost; 6-lab oligopoly"),
    ("VIII",  "POST-TRAINING",        "Custom-Built",       "RLVR verifier coverage limited"),
    ("IX",    "MODEL PROVIDERS",      "Product",            "Per-token 4-10x compression"),
    ("X",     "INFERENCE ENGINES",    "Product",            "KV-cache / FP4 long-context"),
    # combined row for XI-XII
    ("XI-XII", "RETRIEVAL, MEMORY, ORCHESTRATION", "Custom-Built", "MCP commons-or-fork; memory absorption"),
    ("XIII",  "APPLICATION LAYER",    "Custom-Built",       "Enterprise procurement cycle (Job 4)"),
    ("XIV",   "THE USER",             "Product",            "Default-distribution risk; battery/thermal"),
]

# Meta-strata — render as vertical bands on the right margin
META = [
    ("META-A",  "SAFETY"),
    ("META-B",  "REGULATION"),
    ("META-C",  "ECONOMICS"),
    ("META-D",  "GEOPOLITICS"),
]

# -----------------------------------------------------------------------------
# OCQ scores (verbatim from Ch 2 §2.1) — 18 rows
# Row = (label, Opportunity, Challenge, OpenQuestion). Scores /15.
# -----------------------------------------------------------------------------
OCQ = [
    ("I — Power",                 13, 13, 12),
    ("II — Facility",             15, 11, 11),
    ("III — Compute",             13, 14, 14),
    ("IV — Fabric",               13, 12, 12),
    ("V — Parallelism",           15, 11, 14),
    ("VI — Data",                 15, 10, 13),
    ("VII — Pretraining",         12, 12, 11),
    ("VIII — Post-training",      13, 12, 13),
    ("IX — Model Providers",      15, 13, 14),
    ("X — Inference Engines",     15, 11, 13),
    ("XI — Retrieval & Memory",   15, 11, 15),
    ("XII — Orchestration",       15, 12, 14),
    ("XIII — Application Layer",  15, 11, 13),
    ("XIV — The User",            13, 10, 13),
    ("Meta-A — Safety",           12, 11, 13),
    ("Meta-B — Regulation",       15, 12, 15),
    ("Meta-C — Economics",        15, 10, 14),
    ("Meta-D — Geopolitics",      13, 12, 12),
]

# -----------------------------------------------------------------------------
# Wardley map components (Ch 2 §2.2 + Ch 1 named players)
# Each: (label, evolution_x [0-1], value_chain_y [0-1])
#   evolution: 0=Genesis, 0.33=Custom-Built, 0.67=Product, 1=Commodity/Utility
#   value chain: 0=invisible substrate, 1=user-visible
# -----------------------------------------------------------------------------
WARDLEY = [
    # USER & APP LAYER (top, visible)
    ("Sierra",                    0.40, 0.96),
    ("Decagon",                   0.42, 0.94),
    ("Harvey",                    0.40, 0.92),
    ("Glean",                     0.55, 0.92),
    ("Cursor",                    0.70, 0.94),
    ("ChatGPT",                   0.78, 0.97),
    ("Claude Code",               0.62, 0.95),
    ("Apple Intelligence",        0.45, 0.88),
    # ORCHESTRATION / MIDDLEWARE
    ("MCP",                       0.48, 0.78),
    ("LangGraph",                 0.55, 0.76),
    ("Vercel AI SDK",             0.62, 0.78),
    ("OpenAI Agents SDK",         0.45, 0.74),
    ("Mastra",                    0.30, 0.76),
    ("Computer-use agents",       0.18, 0.82),
    # RETRIEVAL / MEMORY
    ("pgvector",                  0.82, 0.66),
    ("Pinecone",                  0.65, 0.68),
    ("Qdrant",                    0.60, 0.66),
    ("Mem0 / Letta",              0.22, 0.70),
    ("GraphRAG",                  0.20, 0.64),
    # MODEL PROVIDERS
    ("Anthropic",                 0.68, 0.58),
    ("OpenAI",                    0.72, 0.60),
    ("Google Vertex",             0.72, 0.56),
    ("Vercel AI Gateway",         0.85, 0.54),
    # INFERENCE ENGINES
    ("vLLM",                      0.78, 0.46),
    ("SGLang",                    0.70, 0.46),
    ("TensorRT-LLM",              0.72, 0.44),
    ("NVIDIA Dynamo",             0.45, 0.42),
    ("Groq / Cerebras",           0.30, 0.44),
    # PRE / POST TRAINING
    ("Llama / Qwen open-weight",  0.55, 0.36),
    ("RLVR / GRPO",               0.35, 0.34),
    ("Frontier pretrain (GPT-5/Opus 4.5)", 0.30, 0.38),
    # DATA
    ("Common Crawl",              0.92, 0.28),
    ("Licensed corpora",          0.50, 0.26),
    ("Synthetic data",            0.30, 0.24),
    # FABRIC
    ("InfiniBand / Ethernet",     0.78, 0.18),
    ("NVLink",                    0.40, 0.16),
    ("UALink",                    0.10, 0.20),
    ("CPO / Optics",              0.22, 0.14),
    # COMPUTE
    ("NVIDIA Blackwell",          0.70, 0.10),
    ("AMD MI355X",                0.40, 0.08),
    ("TPU v7 Ironwood",           0.45, 0.10),
    ("Rubin Ultra (Kyber)",       0.18, 0.08),
    # FACILITY & POWER
    ("Hyperscale DC",             0.75, 0.04),
    ("Stargate / Hyperion",       0.35, 0.04),
    ("Grid power",                0.98, 0.02),
    ("SMR (Kairos / X-energy)",   0.08, 0.02),
]

# 5 punctuated equilibria — arrows on the Wardley map (Ch 2 §2.2)
# (label_match, dx — how far rightward)
WARDLEY_ARROWS = [
    ("MCP",                  0.20),  # late-Custom -> Product H1 2026
    ("Computer-use agents",  0.18),  # Genesis -> Custom-Built mid-late 2026
    ("Rubin Ultra (Kyber)",  0.18),  # HBM4 + CoWoS-L Custom -> Product
    ("Vercel AI Gateway",    0.10),  # Product -> Commodity through 2026
    ("Mem0 / Letta",         0.15),  # voice / memory crossing
]

# Dependency lines (top-down) — 5-8 key relationships
WARDLEY_DEPS = [
    ("Sierra",          "Anthropic"),
    ("Decagon",         "OpenAI"),
    ("Cursor",          "Anthropic"),
    ("Anthropic",       "vLLM"),
    ("vLLM",            "NVIDIA Blackwell"),
    ("NVIDIA Blackwell","Hyperscale DC"),
    ("Hyperscale DC",   "Grid power"),
    ("MCP",             "Anthropic"),
]

# -----------------------------------------------------------------------------
# Powers x Layer Grid (Ch 2 §2.3)
# Status codes: "F" = filled (held), "S" = strengthening (accent filled),
#               "E" = eroding (outline), ""  = absent
# Optional holder note in parentheses (kept very short).
# Columns: Scale / Network / CounterPos / Switching / Branding / Cornered / Process
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

# Order rows top-to-bottom I..XIV then Meta-A..D (matches OCQ order)
POWERS = [
    # row label,        Scale, Net,  CP,   Sw,   Br,   CR,   Pr,   holder (short, optional)
    ("I — Power",        "S",  "",   "",   "",   "",   "F",  "F",  "Constellation/Vistra/Talen"),
    ("II — Facility",    "F",  "",   "",   "F",  "",   "F",  "",   "Equinix/DLR/QTS"),
    ("III — Compute",    "F",  "",   "",   "F",  "F",  "F",  "F",  "NVIDIA"),
    ("IV — Fabric",      "",   "",   "S",  "",   "",   "F",  "F",  "NVIDIA / Broadcom"),
    ("V — Parallelism",  "",   "F",  "",   "",   "",   "F",  "F",  "Frontier labs"),
    ("VI — Data",        "",   "",   "F",  "F",  "",   "F",  "",   "Reddit/YT/GH/Bloomberg"),
    ("VII — Pretraining","F",  "",   "S",  "",   "F",  "F",  "F",  "Anthropic/OpenAI/GDM"),
    ("VIII — Post-train","",   "",   "",   "F",  "",   "F",  "F",  "Anthropic CAI; Scale"),
    ("IX — Model Prov.", "E",  "F",  "",   "E",  "F",  "",   "",   "OpenAI/Anthropic"),
    ("X — Inference",    "",   "F",  "",   "",   "",   "F",  "F",  "Groq/Together/vLLM"),
    ("XI — Retrieval",   "",   "",   "",   "E",  "E",  "",   "F",  "Turbopuffer/MongoDB"),
    ("XII — Orchestr.",  "",   "S",  "S",  "F",  "S",  "",   "",   "MCP / Vercel AI SDK"),
    ("XIII — Application","",  "S",  "",   "F",  "F",  "",   "F",  "Sierra/Decagon/Harvey/Glean"),
    ("XIV — The User",   "",   "F",  "",   "F",  "F",  "F",  "",   "Apple / Google duopoly"),
    ("Meta-A — Safety",  "",   "",   "",   "",   "F",  "F",  "F",  "Anthropic"),
    ("Meta-B — Regul.",  "",   "",   "F",  "",   "",   "F",  "F",  "Palantir / GovCloud"),
    ("Meta-C — Econ.",   "F",  "",   "",   "",   "",   "F",  "",   "Hyperscaler balance sheets"),
    ("Meta-D — Geo.",    "",   "",   "F",  "",   "",   "F",  "",   "TSMC / ASML / SK Hynix"),
]

# -----------------------------------------------------------------------------
# Cross-stratum flows (Ch 3 §3.5 + Ch 1 binding constraints)
# Strata I..XIV positioned around a vertical column with labels.
# We draw:
#   - dependency edges (light gray)
#   - risk-propagation paths (accent, thick)
#   - bet coupling lines (accent, dotted)
# -----------------------------------------------------------------------------

# Strata positions for the flow graph (we lay them out as a vertical column on the left,
# bets/risks on the right). Order matches I..XIV including combined XI-XII.
FLOW_STRATA_LABELS = [
    "I  Power",
    "II  Facility",
    "III  Compute",
    "IV  Fabric",
    "V  Parallelism",
    "VI  Data",
    "VII  Pretraining",
    "VIII  Post-training",
    "IX  Model Providers",
    "X  Inference",
    "XI-XII  Retrieval/Memory/Orch.",
    "XIII  Application",
    "XIV  The User",
]

# Dependency edges (light gray) — stratum -> stratum it gates
FLOW_DEPS = [
    ("I  Power",                "II  Facility"),
    ("II  Facility",            "III  Compute"),
    ("III  Compute",            "IV  Fabric"),
    ("IV  Fabric",              "V  Parallelism"),
    ("VI  Data",                "VII  Pretraining"),
    ("VII  Pretraining",        "VIII  Post-training"),
    ("VIII  Post-training",     "IX  Model Providers"),
    ("IX  Model Providers",     "X  Inference"),
    ("X  Inference",            "XI-XII  Retrieval/Memory/Orch."),
    ("XI-XII  Retrieval/Memory/Orch.", "XIII  Application"),
    ("XIII  Application",       "XIV  The User"),
]

# Risk propagation paths (accent, thick) — risk# -> strata it threatens
# (risk_id, [list of strata it threatens])
FLOW_RISKS = [
    ("R1", "HBM4/CoWoS-L slip",        ["III  Compute", "IV  Fabric", "VII  Pretraining"]),
    ("R2", "Hyperscaler FCF reckoning",["IX  Model Providers", "XIII  Application"]),
    ("R3", "OpenAI Preparedness clause",["VIII  Post-training", "IX  Model Providers"]),
    ("R4", "Federal preemption (Meta-B)",["IX  Model Providers", "XIII  Application"]),
    ("R5", "Foundation labs walk up-stack",["XIII  Application", "IX  Model Providers"]),
]

# Bet coupling clusters (dotted accent)
# Bets are not on the graph as nodes — we draw coupling annotations between strata they
# all touch, to keep the graph readable. Per Ch 3 §3.5:
#   - #1, #4, #5 share buyer (procurement officer): IX, X, XI-XII
#   - #1, #2, #6 platform compound: IX, XIII
FLOW_COUPLINGS = [
    ("Bet #1-#4-#5 (shared buyer)",
        [("IX  Model Providers", "X  Inference"),
         ("X  Inference", "XI-XII  Retrieval/Memory/Orch.")]),
    ("Bet #1-#2-#6 (platform compound)",
        [("IX  Model Providers", "XIII  Application")]),
]


# =============================================================================
# Helpers
# =============================================================================

def _new_fig(landscape=False):
    if landscape:
        return plt.figure(figsize=(PAGE_H, PAGE_W), facecolor=WHITE)
    return plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=WHITE)


def _save(fig, path):
    fig.savefig(path, format="svg", bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


def _source_caption(ax, text, x=0.02, y=0.005):
    ax.text(x, y, text, transform=ax.transAxes,
            fontsize=7, color=GRAY_MED, ha="left", va="bottom", style="italic")


# =============================================================================
# Plate 1 — Substrate Column
# =============================================================================

def build_substrate_column():
    fig = _new_fig()
    ax = fig.add_axes([0.06, 0.04, 0.88, 0.92])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13.5)
    ax.set_axis_off()

    # Title + subtitle
    ax.text(0, 13.2, "Plate 1 — The Substrate Column",
            fontsize=16, fontweight="bold", color=BLACK, ha="left", va="top")
    ax.text(0, 12.85, "14 strata + 4 meta. Read top to bottom: ascending dependency.",
            fontsize=10, color=BLACK, ha="left", va="top")

    # Layout: 13 rows (combined XI-XII), occupy y from 12.2 down to 1.2 -> ~0.85/row
    n = len(STRATA)
    top_y = 12.2
    bottom_y = 1.2
    row_h = (top_y - bottom_y) / n

    # Right margin reserved for meta-strata bands
    col_x0 = 0.0      # left edge of stratum block
    col_x1 = 7.0      # right edge of stratum block (before meta bands)
    meta_x0 = 7.15
    meta_x1 = 10.0

    for i, (roman, name, evo, binding) in enumerate(STRATA):
        y_top = top_y - i * row_h
        y_bot = y_top - row_h
        y_mid = (y_top + y_bot) / 2

        # row separator (thin)
        ax.plot([col_x0, col_x1], [y_bot, y_bot], color=GRAY_LIGHT, linewidth=0.4)

        # Roman numeral (left, monospace-ish)
        ax.text(col_x0 + 0.1, y_mid + 0.05, roman,
                fontsize=11, fontweight="bold", color=BLACK,
                ha="left", va="center", family="monospace")

        # Stratum name (large, all-caps)
        ax.text(col_x0 + 1.0, y_mid + 0.15, name,
                fontsize=11.5, fontweight="bold", color=BLACK,
                ha="left", va="center")

        # Binding-constraint tag (smaller, under name)
        ax.text(col_x0 + 1.0, y_mid - 0.22, binding,
                fontsize=7.5, color=GRAY_MED, ha="left", va="center", style="italic")

        # Evolution-stage tag (right)
        ax.text(col_x1 - 0.1, y_mid + 0.05, evo,
                fontsize=8, color=BLACK, ha="right", va="center")

    # Top border
    ax.plot([col_x0, col_x1], [top_y, top_y], color=BLACK, linewidth=0.7)

    # ----- META BANDS -----
    n_meta = len(META)
    band_w = (meta_x1 - meta_x0) / n_meta
    band_top = top_y
    band_bot = bottom_y - 0.4

    for j, (code, name) in enumerate(META):
        bx = meta_x0 + j * band_w
        # Outline band
        rect = Rectangle((bx, band_bot), band_w * 0.9, band_top - band_bot,
                         facecolor=WHITE, edgecolor=BLACK, linewidth=0.7)
        ax.add_patch(rect)
        # Rotated label centered in the band
        cx = bx + band_w * 0.45
        cy = (band_top + band_bot) / 2
        ax.text(cx, cy, f"{code}  ·  {name}",
                fontsize=9.5, fontweight="bold", color=BLACK,
                ha="center", va="center", rotation=90)

    # Header line above meta bands
    ax.text(meta_x0, top_y + 0.18, "META-STRATA (wrap the whole column)",
            fontsize=8, color=BLACK, ha="left", va="bottom", fontweight="bold")

    # Legend / key (bottom)
    ax.text(0, 0.85,
            "Evolution stage notation follows Wardley: Genesis (novel) -> Custom-Built (recipe known) -> Product (vendor market) -> Commodity/Utility (rentable).",
            fontsize=7.5, color=BLACK, ha="left", va="top")
    ax.text(0, 0.55,
            "Binding constraint = what limits scaling at this layer in 2026 (one short tag per row).",
            fontsize=7.5, color=BLACK, ha="left", va="top")

    _source_caption(ax, "Source: AI_STACK_MASTER Ch 1 §I–XIV and §Meta-A–D.", x=0.0, y=0.01)

    _save(fig, PLATES_DIR / "01_substrate_column.svg")


# =============================================================================
# Plate 2 — OCQ Heatmap
# =============================================================================

def build_ocq_heatmap():
    fig = _new_fig()
    ax = fig.add_axes([0.30, 0.10, 0.55, 0.78])

    n_rows = len(OCQ)
    cols = ["Opportunity", "Challenge", "Open Question"]
    n_cols = 3

    data = np.array([[r[1], r[2], r[3]] for r in OCQ], dtype=float)
    row_labels = [r[0] for r in OCQ]

    # Single-hue gradient white -> ACCENT (#1d4ed8). Scale 0..15.
    # We map a 0..15 score to alpha 0..1 over the accent.
    def shade_for(score):
        t = score / 15.0
        # Linear blend white -> ACCENT
        # white = (1,1,1), accent rgb = (29,78,216) -> normalized
        r0, g0, b0 = 1.0, 1.0, 1.0
        r1, g1, b1 = 29/255.0, 78/255.0, 216/255.0
        return (r0 + (r1 - r0) * t, g0 + (g1 - g0) * t, b0 + (b1 - b0) * t)

    # Build cells
    for i in range(n_rows):
        for j in range(n_cols):
            score = data[i, j]
            color = shade_for(score)
            rect = Rectangle((j, n_rows - i - 1), 1, 1,
                             facecolor=color, edgecolor=BLACK, linewidth=0.4)
            ax.add_patch(rect)
            # Numeric label — contrast: dark text below ~8, white above
            txt_color = WHITE if score >= 11 else BLACK
            ax.text(j + 0.5, n_rows - i - 1 + 0.5, f"{int(score)}",
                    ha="center", va="center", fontsize=9, fontweight="bold",
                    color=txt_color)

    # Row labels
    for i, lbl in enumerate(row_labels):
        ax.text(-0.15, n_rows - i - 1 + 0.5, lbl,
                ha="right", va="center", fontsize=8.5, color=BLACK)

    # Column labels (top)
    for j, c in enumerate(cols):
        ax.text(j + 0.5, n_rows + 0.25, c,
                ha="center", va="bottom", fontsize=10, fontweight="bold", color=BLACK)

    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows + 0.6)
    ax.set_aspect("equal")
    ax.set_axis_off()

    # Title (above the grid, on the figure)
    fig.text(0.06, 0.94, "Plate 2 — OCQ Heatmap",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.915, "Opportunity / Challenge / Open Question. Score out of 15.",
             fontsize=10, color=BLACK, ha="left")

    # Legend — score scale (color ramp at bottom)
    leg_ax = fig.add_axes([0.30, 0.05, 0.55, 0.025])
    steps = 16
    for k in range(steps):
        c = shade_for(k)
        leg_ax.add_patch(Rectangle((k, 0), 1, 1, facecolor=c,
                                   edgecolor=BLACK, linewidth=0.3))
    leg_ax.set_xlim(0, steps)
    leg_ax.set_ylim(0, 1)
    leg_ax.set_axis_off()
    # tick labels
    for k in [0, 5, 10, 15]:
        leg_ax.text(k + 0.5, -0.5, str(k), ha="center", va="top", fontsize=7.5, color=BLACK)
    leg_ax.text(8, 1.7, "Score (0–15) — darker = higher", ha="center", va="bottom",
                fontsize=8, color=BLACK)

    # Source caption
    fig.text(0.06, 0.01, "Source: AI_STACK_MASTER Ch 2 §2.1.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "02_ocq_heatmap.svg")


# =============================================================================
# Plate 3 — Wardley Map
# =============================================================================

def build_wardley_map():
    # Landscape layout reads better for a 2D map
    fig = plt.figure(figsize=(PAGE_H, PAGE_W), facecolor=WHITE)  # 11 x 8.5

    ax = fig.add_axes([0.07, 0.10, 0.88, 0.78])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()

    # Background grid: 4 evolution columns
    boundaries = [0.0, 0.25, 0.50, 0.75, 1.0]
    stage_labels = ["Genesis", "Custom-Built", "Product", "Commodity/Utility"]
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
        ax.text(cx, -0.04, lbl, ha="center", va="top", fontsize=9, color=BLACK)

    # Evolution arrow under axis
    ax.annotate("", xy=(0.98, -0.085), xytext=(0.02, -0.085),
                arrowprops=dict(arrowstyle="->", color=BLACK, lw=0.7))
    ax.text(0.5, -0.105, "Evolution", ha="center", va="top", fontsize=8, color=BLACK)

    # Y axis label
    ax.text(-0.04, 0.5, "Value Chain  (invisible substrate -> user-visible)",
            rotation=90, ha="center", va="center", fontsize=9, color=BLACK)

    # Build a lookup for arrows + deps
    comp_pos = {c[0]: (c[1], c[2]) for c in WARDLEY}

    # Dependency lines (light gray)
    for src, dst in WARDLEY_DEPS:
        if src in comp_pos and dst in comp_pos:
            x1, y1 = comp_pos[src]
            x2, y2 = comp_pos[dst]
            ax.plot([x1, x2], [y1, y2], color=GRAY_LIGHT, linewidth=0.7, zorder=1)

    # Plot components (small filled black circles)
    for label, x, y in WARDLEY:
        ax.scatter([x], [y], s=22, color=BLACK, zorder=3)
        # Offset label to the right of dot
        ax.text(x + 0.012, y, label, fontsize=7.5, color=BLACK,
                ha="left", va="center", zorder=4)

    # Punctuated equilibria arrows (accent)
    for label, dx in WARDLEY_ARROWS:
        if label in comp_pos:
            x, y = comp_pos[label]
            ax.annotate("", xy=(min(x + dx, 0.98), y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.8), zorder=5)

    # Title + subtitle
    fig.text(0.07, 0.94, "Plate 3 — Wardley Map of the AI Stack",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.07, 0.915, "Components placed by evolution stage and value-chain position. Arrows: 2026–2027 movement.",
             fontsize=10, color=BLACK, ha="left")

    # Legend (top-right area)
    leg_x = 0.78
    leg_y = 0.96
    leg_lines = [
        ("Component",       BLACK, "scatter"),
        ("Dependency",      GRAY_LIGHT, "line"),
        ("Evolution arrow", ACCENT, "arrow"),
    ]
    for i, (txt, col, kind) in enumerate(leg_lines):
        y = leg_y - i * 0.025
        if kind == "scatter":
            fig.text(leg_x + 0.012, y, txt, fontsize=8, color=BLACK, ha="left", va="center")
            fig.add_artist(plt.Circle((leg_x, y), 0.004, color=col, transform=fig.transFigure))
        elif kind == "line":
            fig.add_artist(Line2D([leg_x - 0.005, leg_x + 0.012], [y, y],
                                  color=col, lw=1.2, transform=fig.transFigure))
            fig.text(leg_x + 0.018, y, txt, fontsize=8, color=BLACK, ha="left", va="center")
        elif kind == "arrow":
            fig.add_artist(FancyArrowPatch((leg_x - 0.005, y), (leg_x + 0.012, y),
                                           arrowstyle="->", color=col, lw=1.6,
                                           mutation_scale=10, transform=fig.transFigure))
            fig.text(leg_x + 0.018, y, txt, fontsize=8, color=BLACK, ha="left", va="center")

    fig.text(0.07, 0.01, "Source: AI_STACK_MASTER Ch 2 §2.2 and Ch 1 named players.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "03_wardley_map.svg")


# =============================================================================
# Plate 4 — 7 Powers x Layer Grid
# =============================================================================

def build_powers_grid():
    fig = _new_fig()
    ax = fig.add_axes([0.27, 0.08, 0.68, 0.82])

    n_rows = len(POWERS)
    n_cols = len(POWERS_COLS)
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows + 0.6)
    ax.set_aspect("equal")
    ax.set_axis_off()

    # Header cells
    for j, c in enumerate(POWERS_COLS):
        ax.text(j + 0.5, n_rows + 0.30, c,
                ha="center", va="bottom", fontsize=8.5, fontweight="bold", color=BLACK)

    # Cells + markers
    for i, row in enumerate(POWERS):
        label = row[0]
        statuses = row[1:8]
        holder = row[8] if len(row) > 8 else ""

        # row label
        ax.text(-0.12, n_rows - i - 1 + 0.5, label,
                ha="right", va="center", fontsize=8, color=BLACK)

        # holder annotation on right side (very small)
        if holder:
            ax.text(n_cols + 0.08, n_rows - i - 1 + 0.5, holder,
                    ha="left", va="center", fontsize=6.5, color=GRAY_MED, style="italic")

        for j, st in enumerate(statuses):
            cx = j + 0.5
            cy = n_rows - i - 1 + 0.5
            # cell border
            rect = Rectangle((j, n_rows - i - 1), 1, 1,
                             facecolor=WHITE, edgecolor=GRAY_LIGHT, linewidth=0.3)
            ax.add_patch(rect)
            # marker
            if st == "F":
                ax.scatter([cx], [cy], s=70, color=BLACK, zorder=3)
            elif st == "S":
                ax.scatter([cx], [cy], s=80, color=ACCENT, zorder=3, edgecolors=BLACK, linewidths=0.6)
            elif st == "E":
                ax.scatter([cx], [cy], s=70, facecolors="none",
                           edgecolors=BLACK, linewidths=1.0, zorder=3)
            # else blank

    # Title + subtitle
    fig.text(0.06, 0.94, "Plate 4 — Powers x Layer Grid",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.915, "Helmer's 7 Powers across the 18-stratum stack.",
             fontsize=10, color=BLACK, ha="left")
    fig.text(0.06, 0.895, "Filled = held; accent (blue) = strengthening; outline = eroding.",
             fontsize=9, color=BLACK, ha="left")

    # Legend (bottom, inside figure space)
    leg_ax = fig.add_axes([0.27, 0.03, 0.68, 0.04])
    leg_ax.set_xlim(0, 10)
    leg_ax.set_ylim(0, 1)
    leg_ax.set_axis_off()

    leg_ax.scatter([0.3], [0.5], s=70, color=BLACK)
    leg_ax.text(0.55, 0.5, "Held (filled)", fontsize=8, va="center", color=BLACK)

    leg_ax.scatter([2.5], [0.5], s=80, color=ACCENT, edgecolors=BLACK, linewidths=0.6)
    leg_ax.text(2.8, 0.5, "Strengthening (accent)", fontsize=8, va="center", color=BLACK)

    leg_ax.scatter([5.5], [0.5], s=70, facecolors="none", edgecolors=BLACK, linewidths=1.0)
    leg_ax.text(5.8, 0.5, "Eroding (outline)", fontsize=8, va="center", color=BLACK)

    leg_ax.text(8.0, 0.5, "Blank = absent", fontsize=8, va="center", color=BLACK)

    fig.text(0.06, 0.005, "Source: AI_STACK_MASTER Ch 2 §2.3.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "04_powers_layer_grid.svg")


# =============================================================================
# Plate 5 — Cross-Stratum Flows
# =============================================================================

def build_cross_stratum_flows():
    fig = _new_fig()
    ax = fig.add_axes([0.05, 0.06, 0.90, 0.86])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13.5)
    ax.set_axis_off()

    # Title + subtitle
    ax.text(0, 13.2, "Plate 5 — Cross-Stratum Flows",
            fontsize=16, fontweight="bold", color=BLACK, ha="left", va="top")
    ax.text(0, 12.85, "Dependencies (gray), risk propagation (blue thick), bet coupling (blue dotted).",
            fontsize=10, color=BLACK, ha="left", va="top")

    # Lay out 13 stratum nodes in a vertical column on the left
    n = len(FLOW_STRATA_LABELS)
    top_y = 12.0
    bot_y = 1.5
    step = (top_y - bot_y) / (n - 1)
    node_x = 2.4
    node_w = 3.6
    node_h = 0.55

    node_pos = {}
    for i, lbl in enumerate(FLOW_STRATA_LABELS):
        y = top_y - i * step
        node_pos[lbl] = (node_x, y)
        # node box
        rect = Rectangle((node_x - node_w/2, y - node_h/2), node_w, node_h,
                         facecolor=WHITE, edgecolor=BLACK, linewidth=0.7, zorder=3)
        ax.add_patch(rect)
        ax.text(node_x, y, lbl, ha="center", va="center", fontsize=8.5,
                fontweight="bold", color=BLACK, zorder=4)

    # Dependency edges (light gray, vertical, slightly to the left of the column)
    dep_x = node_x - node_w/2 - 0.25
    for src, dst in FLOW_DEPS:
        if src in node_pos and dst in node_pos:
            x1, y1 = node_pos[src]
            x2, y2 = node_pos[dst]
            # Draw a small "U" on the left
            ax.annotate("", xy=(x2 - node_w/2, y2), xytext=(x1 - node_w/2, y1),
                        arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT, lw=1.2),
                        zorder=2)

    # Risk propagation paths (accent, thick) — draw on the right side
    risk_x_base = node_x + node_w/2 + 0.6
    risk_offsets = [0.0, 0.35, 0.70, 1.05, 1.40]  # one per risk

    # We'll list risks vertically at the top-right with short labels and
    # draw thick accent arrows from a risk anchor to each threatened stratum.
    risk_anchor_x = node_x + node_w/2 + 2.0
    risk_anchor_y_top = 11.5
    risk_anchor_dy = 0.55

    for k, (rid, rlabel, strata) in enumerate(FLOW_RISKS):
        ay = risk_anchor_y_top - k * risk_anchor_dy
        # Risk anchor label box
        rect = Rectangle((risk_anchor_x, ay - 0.22), 4.5, 0.44,
                         facecolor=WHITE, edgecolor=ACCENT, linewidth=1.2, zorder=3)
        ax.add_patch(rect)
        ax.text(risk_anchor_x + 0.1, ay, f"{rid}  {rlabel}",
                fontsize=8, fontweight="bold", color=ACCENT,
                ha="left", va="center", zorder=4)

        # Draw thick accent arrows from the anchor's left edge to each threatened stratum
        for s in strata:
            if s in node_pos:
                sx, sy = node_pos[s]
                # arrow target: right edge of stratum box
                target_x = sx + node_w/2 + 0.04
                target_y = sy
                src_x = risk_anchor_x - 0.02
                src_y = ay
                arrow = FancyArrowPatch((src_x, src_y), (target_x, target_y),
                                        arrowstyle="->",
                                        color=ACCENT,
                                        linewidth=1.6,
                                        mutation_scale=12,
                                        connectionstyle="arc3,rad=-0.15",
                                        zorder=2.5,
                                        alpha=0.85)
                ax.add_patch(arrow)

    # Bet-coupling lines (dotted accent)
    # Draw between strata along the inner column with a dotted style
    coupling_label_y = 6.0
    for ci, (clabel, edges) in enumerate(FLOW_COUPLINGS):
        # Label position: stack below risks
        ly = 4.0 - ci * 0.45
        # Coupling label badge
        rect = Rectangle((risk_anchor_x, ly - 0.22), 4.5, 0.44,
                         facecolor=WHITE, edgecolor=ACCENT, linewidth=1.0,
                         linestyle="--", zorder=3)
        ax.add_patch(rect)
        ax.text(risk_anchor_x + 0.1, ly, clabel,
                fontsize=8, fontweight="bold", color=ACCENT,
                ha="left", va="center", zorder=4)

        # Dotted accent connectors between strata pairs (on the inner side of column)
        for s1, s2 in edges:
            if s1 in node_pos and s2 in node_pos:
                x1, y1 = node_pos[s1]
                x2, y2 = node_pos[s2]
                ax.plot([x1 + node_w/2 + 0.1, x1 + node_w/2 + 0.1],
                        [y1, y2],
                        color=ACCENT, linewidth=1.4, linestyle=":", zorder=2)
                # short tie-bars
                ax.plot([x1 + node_w/2 - 0.02, x1 + node_w/2 + 0.1], [y1, y1],
                        color=ACCENT, linewidth=1.4, linestyle=":", zorder=2)
                ax.plot([x2 + node_w/2 - 0.02, x2 + node_w/2 + 0.1], [y2, y2],
                        color=ACCENT, linewidth=1.4, linestyle=":", zorder=2)

    # Legend
    leg_y = 1.0
    # Dependency
    ax.annotate("", xy=(1.1, leg_y), xytext=(0.4, leg_y),
                arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT, lw=1.2))
    ax.text(1.2, leg_y, "Dependency", fontsize=8, color=BLACK, ha="left", va="center")

    # Risk
    arrow = FancyArrowPatch((3.5, leg_y), (4.2, leg_y),
                            arrowstyle="->", color=ACCENT, lw=1.6, mutation_scale=12)
    ax.add_patch(arrow)
    ax.text(4.3, leg_y, "Risk propagation", fontsize=8, color=BLACK, ha="left", va="center")

    # Bet coupling
    ax.plot([6.3, 7.0], [leg_y, leg_y], color=ACCENT, linewidth=1.4, linestyle=":")
    ax.text(7.1, leg_y, "Bet coupling", fontsize=8, color=BLACK, ha="left", va="center")

    # Source caption
    ax.text(0, 0.3, "Source: AI_STACK_MASTER Ch 3 §3.2, §3.5 and Ch 1 binding constraints.",
            fontsize=7, color=GRAY_MED, ha="left", va="bottom", style="italic")

    _save(fig, PLATES_DIR / "05_cross_stratum_flows.svg")


# =============================================================================
# main
# =============================================================================

def main():
    PLATES_DIR.mkdir(parents=True, exist_ok=True)
    build_substrate_column()
    build_ocq_heatmap()
    build_wardley_map()
    build_powers_grid()
    build_cross_stratum_flows()
    print("Generated:")
    for p in sorted(PLATES_DIR.glob("0*.svg")):
        print(f"  {p}  ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
