"""
AI_AGENTS_MASTER (Volume III) — Plate generator
================================================
Generates 5 SVG plates that accompany AI_AGENTS_MASTER Volume III.
Educational, NOT aesthetic. Black on white, one accent color (#1d4ed8).
Visual continuity with Volume I plates (output/ai-stack/plates/build_plates.py).

Run from ai-agents-v2/ directory:
    python plates/build_plates.py

Output:
    plates/01_agent_substrate_column.svg
    plates/02_agent_ocq_heatmap.svg
    plates/03_agent_wardley_map.svg
    plates/04_agent_powers_grid.svg
    plates/05_agent_cross_substratum_flows.svg
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np

# -----------------------------------------------------------------------------
# Global style — binding per V1 §8 (visual continuity)
# -----------------------------------------------------------------------------
ACCENT = "#1d4ed8"          # one accent color (saturated dark blue)
BLACK = "#000000"
GRAY_MED = "#6b7280"
GRAY_LIGHT = "#d1d5db"
WHITE = "#ffffff"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["axes.edgecolor"] = BLACK
plt.rcParams["axes.linewidth"] = 0.5
plt.rcParams["pdf.fonttype"] = 42

# Page sizes (inches). Letter portrait.
PAGE_W = 8.5
PAGE_H = 11.0

PLATES_DIR = Path(__file__).parent

# -----------------------------------------------------------------------------
# Canonical data — sourced from Ch 1, Ch 2, Ch 3 (May 2026)
# -----------------------------------------------------------------------------

# Plate 1 — 10 numbered agent sub-strata + 4 meta.
# (roman, name, evo_stage, binding_short)
AGENT_STRATA = [
    ("I",    "FOUNDATION MODELS",            "Custom-Built",       "Per-step reliability ceiling; OSWorld 50-55%"),
    ("II",   "AGENT RUNTIMES / SDKs",        "Product",            "Thin margin; switching cost <1 quarter"),
    ("III",  "TOOL USE / MCP",               "Product",            "Spec held; experience forking (4 vectors)"),
    ("IV",   "MEMORY & STATE",               "Genesis/Custom",     "Lab absorption; deletion auditability"),
    ("V",    "PLANNING & TEST-TIME COMPUTE", "Product",            "Thinking econ; 5-12x cost for 3-10pt gain"),
    ("VI",   "ACTION SURFACES",              "Genesis/Custom",     "Computer-use OSWorld coin flip"),
    ("VII",  "EVAL & OBSERVABILITY",         "Custom-Built",       "No turnkey signed eval reports"),
    ("VIII", "RUNTIME SAFETY / GUARDRAILS",  "Custom-Built",       "Indirect prompt injection unsolved"),
    ("IX",   "VERTICAL AGENT PRODUCTS",      "Custom-Built",       "Foundation-lab walk-up-stack pressure"),
    ("X",    "END-USER SURFACES",            "Product",            "Form factor outranks capability for adoption"),
]

# Meta-strata — vertical bands on right margin
AGENT_META = [
    ("META-A", "SAFETY"),
    ("META-B", "REGULATION"),
    ("META-C", "ECONOMICS"),
    ("META-D", "GEOPOLITICS"),
]

# -----------------------------------------------------------------------------
# Plate 2 — Agent OCQ scores (verbatim from Ch 2 §2.1)
# Row = (label, Opportunity, Challenge, OpenQuestion). Scores /15.
# -----------------------------------------------------------------------------
AGENT_OCQ = [
    ("I — Foundation Models",         13, 12, 13),
    ("II — Agent Runtimes",           14, 11, 11),
    ("III — Tool Use / MCP",          12, 12, 14),
    ("IV — Memory & State",           13, 10, 10),
    ("V — Planning / TTC",            15, 13, 11),
    ("VI — Action Surfaces",          14, 11, 10),
    ("VII — Eval & Observability",    14, 11, 12),
    ("VIII — Runtime Safety",         13, 11, 12),
    ("IX — Vertical Products",        13, 11, 14),
    ("X — End-User Surfaces",         12, 11, 13),
    ("Meta-A — Safety Regimes",       12, 10, 13),
    ("Meta-B — Regulation",           13, 11, 14),
    ("Meta-C — Economics",            13, 14, 12),
    ("Meta-D — Geopolitics",          11, 12, 11),
]

# -----------------------------------------------------------------------------
# Plate 3 — Wardley map components (Ch 2 §2.2 + Ch 1 named players)
# (label, evolution_x [0-1], value_chain_y [0-1])
#   evolution: 0=Genesis, 0.33=Custom-Built, 0.67=Product, 1=Commodity
#   value chain: 0=invisible substrate, 1=user-visible
# -----------------------------------------------------------------------------
AGENT_WARDLEY = [
    # USER-VISIBLE / VERTICAL AGENT PRODUCTS (top)
    ("Sierra",                  0.42, 0.96),
    ("Decagon",                 0.44, 0.93),
    ("Harvey",                  0.36, 0.90),
    ("Hippocratic",             0.34, 0.87),
    ("Abridge",                 0.36, 0.84),
    ("Glean",                   0.55, 0.93),
    ("Hebbia",                  0.40, 0.89),
    ("Rogo",                    0.32, 0.86),
    ("Clay",                    0.46, 0.83),
    ("Cursor",                  0.66, 0.94),
    ("Claude Code",             0.60, 0.96),
    ("Cognition Devin",         0.40, 0.92),
    ("Augment",                 0.46, 0.89),
    ("ChatGPT Agent",           0.62, 0.86),
    ("Mistral Le Chat",         0.32, 0.82),
    ("ElevenLabs",              0.66, 0.84),
    ("Runway",                  0.60, 0.81),
    # END-USER SURFACES
    ("M365 Copilot",            0.78, 0.79),
    ("Apple Intelligence",      0.50, 0.76),
    ("Claude for Chrome",       0.28, 0.78),
    ("Comet (Perplexity)",      0.46, 0.76),
    # RUNTIMES / SDKs
    ("Claude Agent SDK",        0.55, 0.68),
    ("OpenAI Agents SDK",       0.58, 0.66),
    ("LangGraph 1.0",           0.70, 0.66),
    ("Google ADK",              0.50, 0.64),
    ("Mastra",                  0.35, 0.66),
    # ACTION SURFACES
    ("Browserbase",             0.66, 0.58),
    ("Vercel Sandbox",          0.72, 0.56),
    ("E2B / Modal",             0.70, 0.54),
    ("Vapi / Retell",           0.46, 0.58),
    ("LiveKit + Cartesia",      0.74, 0.52),
    ("Computer Use (Claude)",   0.16, 0.62),
    # EVAL / OBSERVABILITY
    ("LangSmith",               0.62, 0.46),
    ("Braintrust",              0.55, 0.46),
    ("Langfuse",                0.58, 0.44),
    ("Inspect AI (UK AISI)",    0.32, 0.42),
    # RUNTIME SAFETY
    ("Lakera",                  0.50, 0.40),
    ("NeMo Guardrails",         0.70, 0.38),
    ("Llama Guard 3",           0.78, 0.36),
    # MEMORY
    ("Mem0",                    0.22, 0.34),
    ("Letta",                   0.18, 0.32),
    ("Zep / Graphiti",          0.30, 0.34),
    ("GraphRAG (MS)",           0.26, 0.30),
    ("Claude Projects memory",  0.50, 0.32),
    # TOOL USE / MCP
    ("MCP spec (LF)",           0.66, 0.24),
    ("Cloudflare MCP",          0.46, 0.22),
    ("Kong MCP Gateway",        0.50, 0.20),
    ("Pomerium",                0.42, 0.20),
    ("A2A (Google)",            0.10, 0.22),
    # FOUNDATION MODELS (invisible substrate)
    ("Anthropic Claude Opus",   0.55, 0.10),
    ("OpenAI GPT-5",            0.60, 0.08),
    ("Google Gemini Deep Think",0.58, 0.06),
    ("DeepSeek R2",             0.38, 0.06),
    ("Llama 4",                 0.74, 0.04),
    # PROCUREMENT-GRADE CONTROLS (cross-cutting, Genesis)
    ("Procurement-grade controls (unclaimed)", 0.06, 0.50),
]

# 6 punctuated equilibria — arrows on the Wardley map (Ch 2 §2.2)
AGENT_WARDLEY_ARROWS = [
    ("Kong MCP Gateway",                0.18),  # gateways Custom -> Product H2 2026
    ("Computer Use (Claude)",           0.18),  # Genesis -> Custom mid-late 2026
    ("LiveKit + Cartesia",              0.14),  # voice substrate Product -> Commodity
    ("Procurement-grade controls (unclaimed)", 0.16),  # Genesis -> Custom Q4 2026
    ("Braintrust",                      0.12),  # eval/obs consolidation
    ("ChatGPT Agent",                   0.12),  # foundation labs walking up-stack
]

# Dependency lines (light gray) — 8 key relationships
AGENT_WARDLEY_DEPS = [
    ("Sierra",              "Anthropic Claude Opus"),
    ("Cursor",              "Anthropic Claude Opus"),
    ("Claude Code",         "Anthropic Claude Opus"),
    ("Decagon",             "OpenAI GPT-5"),
    ("Sierra",              "Claude Agent SDK"),
    ("Claude Agent SDK",    "MCP spec (LF)"),
    ("MCP spec (LF)",       "Kong MCP Gateway"),
    ("Browserbase",         "Vercel Sandbox"),
]

# -----------------------------------------------------------------------------
# Plate 4 — Agent Powers x Sub-Stratum Grid (Ch 2 §2.3)
# Status codes: "F" = held filled, "S" = strengthening (accent), "E" = eroding (outline), "" = absent
# Columns: Scale / Network / Counter-Pos / Switching / Branding / Cornered / Process
# -----------------------------------------------------------------------------
AGENT_POWERS_COLS = [
    "Scale\nEconomies",
    "Network\nEconomies",
    "Counter-\nPositioning",
    "Switching\nCosts",
    "Branding",
    "Cornered\nResource",
    "Process\nPower",
]

# rows: (label, Scale, Net, CP, Sw, Br, CR, Pr, holder)
AGENT_POWERS = [
    ("I — Foundation Models",       "F",  "",   "",   "F",  "F",  "F",  "S",  "Anthropic / OpenAI / GDM"),
    ("II — Agent Runtimes",         "",   "",   "",   "E",  "E",  "",   "",   "(no durable holder)"),
    ("III — Tool Use / MCP",        "",   "S",  "F",  "S",  "F",  "",   "",   "Anthropic (CP); Cloudflare/Kong/Pomerium"),
    ("IV — Memory & State",         "",   "",   "",   "E",  "E",  "",   "F",  "Zep (compliance niche)"),
    ("V — Planning / TTC",          "",   "",   "",   "",   "",   "",   "F",  "Lab-internal (RLVR/GRPO)"),
    ("VI — Action Surfaces",        "F",  "",   "",   "F",  "",   "F",  "F",  "Browserbase / LiveKit"),
    ("VII — Eval & Observability",  "",   "",   "",   "F",  "F",  "",   "S",  "LangSmith / Braintrust / Lakera"),
    ("VIII — Runtime Safety",       "",   "",   "",   "E",  "F",  "",   "",   "Lakera (model-neutral)"),
    ("IX — Vertical Products",      "",   "F",  "",   "F",  "F",  "F",  "F",  "Sierra / Harvey / Glean / Hippocratic"),
    ("X — End-User Surfaces",       "F",  "F",  "",   "F",  "F",  "F",  "",   "Microsoft / Apple / Meta WhatsApp"),
    ("Meta-A — Safety Regimes",     "",   "",   "",   "",   "F",  "F",  "F",  "Anthropic (most defensible)"),
    ("Meta-B — Regulation",         "",   "",   "F",  "",   "",   "F",  "F",  "Palantir / Mistral (EU CP)"),
    ("Meta-C — Economics",          "F",  "",   "",   "E",  "",   "",   "",   "Hyperscalers (Scale)"),
    ("Meta-D — Geopolitics",        "",   "",   "F",  "",   "",   "F",  "",   "Mistral / Sarvam / Manus"),
]

# -----------------------------------------------------------------------------
# Plate 5 — Cross-Sub-Stratum Flows (Ch 3 §3.6 + Ch 1 binding constraints + 5 Risks)
# 10 numbered sub-strata as nodes (no meta to keep readable).
# -----------------------------------------------------------------------------
FLOW_STRATA_LABELS = [
    "I  Foundation Models",
    "II  Agent Runtimes",
    "III  Tool Use / MCP",
    "IV  Memory & State",
    "V  Planning / TTC",
    "VI  Action Surfaces",
    "VII  Eval & Observability",
    "VIII  Runtime Safety",
    "IX  Vertical Products",
    "X  End-User Surfaces",
]

# Dependency edges (light gray, thin) — sub-stratum -> sub-stratum it gates
FLOW_DEPS = [
    ("I  Foundation Models",        "II  Agent Runtimes"),
    ("II  Agent Runtimes",          "III  Tool Use / MCP"),
    ("II  Agent Runtimes",          "IV  Memory & State"),
    ("II  Agent Runtimes",          "V  Planning / TTC"),
    ("III  Tool Use / MCP",         "VI  Action Surfaces"),
    ("VI  Action Surfaces",         "IX  Vertical Products"),
    ("VIII  Runtime Safety",        "IX  Vertical Products"),
    ("IX  Vertical Products",       "X  End-User Surfaces"),
]

# Risk propagation paths (accent, thick) — risk# -> strata it threatens
# 5 Risks from Ch 3 §3.2 (agent-layer framing)
FLOW_RISKS = [
    ("R1", "Foundation labs walk up-stack",  ["I  Foundation Models", "IX  Vertical Products"]),
    ("R2", "MCP silent fork (Responses-API)", ["III  Tool Use / MCP", "VI  Action Surfaces"]),
    ("R3", "Anthropic ARR resolution",        ["IX  Vertical Products"]),
    ("R4", "Hyperscaler bundling",            ["V  Planning / TTC", "VII  Eval & Observability", "VIII  Runtime Safety"]),
    ("R5", "EU AI Act paper-tiger outcome",   ["VII  Eval & Observability", "IX  Vertical Products"]),
]

# Bet coupling clusters (dotted accent) — from Ch 3 §3.6
# - Bet #1 + #4 + #5 + Procurement Rubric: shared buyer at VII, VIII, IX
# - Bet #2 + Crux #1 (Anthropic ARR): pressure on IX
FLOW_COUPLINGS = [
    ("Bet #1 + #4 + #5 + Procurement Rubric (shared F1000 buyer)",
        [("VII  Eval & Observability", "VIII  Runtime Safety"),
         ("VIII  Runtime Safety",      "IX  Vertical Products")]),
    ("Bet #2 + Crux #1 (Anthropic ARR -> vertical valuations)",
        [("I  Foundation Models",       "IX  Vertical Products")]),
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
# Plate 1 — Agent Substrate Column
# =============================================================================

def build_agent_substrate_column():
    fig = _new_fig()
    ax = fig.add_axes([0.06, 0.04, 0.88, 0.92])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13.5)
    ax.set_axis_off()

    # Title + subtitle
    ax.text(0, 13.2, "Plate 1 — The Agent Sub-Strata Column",
            fontsize=16, fontweight="bold", color=BLACK, ha="left", va="top")
    ax.text(0, 12.85, "Volume III  ·  10 sub-strata + 4 meta  ·  zoomed from V1 Stratum XIII.",
            fontsize=10, color=BLACK, ha="left", va="top")

    # Column header: AGENT LAYER (V1 Stratum XIII)
    ax.text(0, 12.40, "AGENT LAYER  (V1 Stratum XIII)",
            fontsize=9.5, fontweight="bold", color=ACCENT, ha="left", va="top")

    # Layout: 10 sub-stratum rows
    n = len(AGENT_STRATA)
    top_y = 12.10
    bottom_y = 1.4
    row_h = (top_y - bottom_y) / n

    # Right margin reserved for meta-strata bands
    col_x0 = 0.0
    col_x1 = 7.0
    meta_x0 = 7.15
    meta_x1 = 10.0

    for i, (roman, name, evo, binding) in enumerate(AGENT_STRATA):
        y_top = top_y - i * row_h
        y_bot = y_top - row_h
        y_mid = (y_top + y_bot) / 2

        # row separator
        ax.plot([col_x0, col_x1], [y_bot, y_bot], color=GRAY_LIGHT, linewidth=0.4)

        # Roman numeral
        ax.text(col_x0 + 0.1, y_mid + 0.05, roman,
                fontsize=11, fontweight="bold", color=BLACK,
                ha="left", va="center", family="monospace")

        # Stratum name
        ax.text(col_x0 + 1.0, y_mid + 0.18, name,
                fontsize=11, fontweight="bold", color=BLACK,
                ha="left", va="center")

        # Binding-constraint tag
        ax.text(col_x0 + 1.0, y_mid - 0.22, binding,
                fontsize=7.5, color=GRAY_MED, ha="left", va="center", style="italic")

        # Evolution-stage tag (right)
        ax.text(col_x1 - 0.1, y_mid + 0.05, evo,
                fontsize=8, color=BLACK, ha="right", va="center")

    # Top border
    ax.plot([col_x0, col_x1], [top_y, top_y], color=BLACK, linewidth=0.7)

    # ----- META BANDS -----
    n_meta = len(AGENT_META)
    band_w = (meta_x1 - meta_x0) / n_meta
    band_top = top_y
    band_bot = bottom_y - 0.2

    for j, (code, name) in enumerate(AGENT_META):
        bx = meta_x0 + j * band_w
        rect = Rectangle((bx, band_bot), band_w * 0.9, band_top - band_bot,
                         facecolor=WHITE, edgecolor=BLACK, linewidth=0.7)
        ax.add_patch(rect)
        cx = bx + band_w * 0.45
        cy = (band_top + band_bot) / 2
        ax.text(cx, cy, f"{code}  ·  {name}",
                fontsize=9.5, fontweight="bold", color=BLACK,
                ha="center", va="center", rotation=90)

    # Header line above meta bands
    ax.text(meta_x0, top_y + 0.18, "META-STRATA (wrap the agent stack)",
            fontsize=8, color=BLACK, ha="left", va="bottom", fontweight="bold")

    # Legend / key (bottom)
    ax.text(0, 1.05,
            "Read top to bottom: ascending dependency. Stratum I gates everything above; Stratum X is closest to the buyer.",
            fontsize=7.5, color=BLACK, ha="left", va="top")
    ax.text(0, 0.75,
            "Evolution stage follows Wardley: Genesis (novel) -> Custom-Built (recipe known) -> Product (vendor market) -> Commodity/Utility (rentable).",
            fontsize=7.5, color=BLACK, ha="left", va="top")
    ax.text(0, 0.45,
            "Binding constraint = what limits scaling at this sub-stratum in May 2026 (one short tag per row).",
            fontsize=7.5, color=BLACK, ha="left", va="top")

    _source_caption(ax, "Source: AI_AGENTS_MASTER Ch 1 §I-X and §Meta-A-D.", x=0.0, y=0.01)

    _save(fig, PLATES_DIR / "01_agent_substrate_column.svg")


# =============================================================================
# Plate 2 — Agent OCQ Heatmap
# =============================================================================

def build_agent_ocq_heatmap():
    fig = _new_fig()
    ax = fig.add_axes([0.30, 0.10, 0.55, 0.78])

    n_rows = len(AGENT_OCQ)
    cols = ["Opportunity", "Challenge", "Open Question"]
    n_cols = 3

    data = np.array([[r[1], r[2], r[3]] for r in AGENT_OCQ], dtype=float)
    row_labels = [r[0] for r in AGENT_OCQ]

    # Single-hue gradient white -> ACCENT (#1d4ed8). Scale 0..15.
    def shade_for(score):
        t = score / 15.0
        r0, g0, b0 = 1.0, 1.0, 1.0
        r1, g1, b1 = 29/255.0, 78/255.0, 216/255.0
        return (r0 + (r1 - r0) * t, g0 + (g1 - g0) * t, b0 + (b1 - b0) * t)

    for i in range(n_rows):
        for j in range(n_cols):
            score = data[i, j]
            color = shade_for(score)
            rect = Rectangle((j, n_rows - i - 1), 1, 1,
                             facecolor=color, edgecolor=BLACK, linewidth=0.4)
            ax.add_patch(rect)
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
    fig.text(0.06, 0.94, "Plate 2 — Agent OCQ Heatmap",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.915, "Volume III  ·  Opportunity / Challenge / Open Question per agent sub-stratum.",
             fontsize=10, color=BLACK, ha="left")
    fig.text(0.06, 0.895, "Score out of 15. Darker cell = higher intensity.",
             fontsize=9, color=BLACK, ha="left")

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
    for k in [0, 5, 10, 15]:
        leg_ax.text(k + 0.5, -0.5, str(k), ha="center", va="top", fontsize=7.5, color=BLACK)
    leg_ax.text(8, 1.7, "Score (0-15) — darker = higher", ha="center", va="bottom",
                fontsize=8, color=BLACK)

    fig.text(0.06, 0.01, "Source: AI_AGENTS_MASTER Ch 2 §2.1.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "02_agent_ocq_heatmap.svg")


# =============================================================================
# Plate 3 — Agent Wardley Map
# =============================================================================

def build_agent_wardley_map():
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

    # Lookup
    comp_pos = {c[0]: (c[1], c[2]) for c in AGENT_WARDLEY}

    # Dependency lines (light gray)
    for src, dst in AGENT_WARDLEY_DEPS:
        if src in comp_pos and dst in comp_pos:
            x1, y1 = comp_pos[src]
            x2, y2 = comp_pos[dst]
            ax.plot([x1, x2], [y1, y2], color=GRAY_LIGHT, linewidth=0.7, zorder=1)

    # Plot components
    for label, x, y in AGENT_WARDLEY:
        ax.scatter([x], [y], s=20, color=BLACK, zorder=3)
        ax.text(x + 0.010, y, label, fontsize=7, color=BLACK,
                ha="left", va="center", zorder=4)

    # Punctuated equilibria arrows (accent)
    for label, dx in AGENT_WARDLEY_ARROWS:
        if label in comp_pos:
            x, y = comp_pos[label]
            ax.annotate("", xy=(min(x + dx, 0.98), y), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.8), zorder=5)

    # Title + subtitle
    fig.text(0.07, 0.94, "Plate 3 — Wardley Map of the Agent Stack",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.07, 0.915, "Volume III  ·  Components positioned by evolution x value chain. Arrows: 2026-2027 movement.",
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

    fig.text(0.07, 0.01, "Source: AI_AGENTS_MASTER Ch 2 §2.2 and Ch 1 named players.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "03_agent_wardley_map.svg")


# =============================================================================
# Plate 4 — Agent Powers x Sub-Stratum Grid
# =============================================================================

def build_agent_powers_grid():
    fig = _new_fig()
    ax = fig.add_axes([0.27, 0.08, 0.68, 0.82])

    n_rows = len(AGENT_POWERS)
    n_cols = len(AGENT_POWERS_COLS)
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows + 0.6)
    ax.set_aspect("equal")
    ax.set_axis_off()

    # Header cells
    for j, c in enumerate(AGENT_POWERS_COLS):
        ax.text(j + 0.5, n_rows + 0.30, c,
                ha="center", va="bottom", fontsize=8.5, fontweight="bold", color=BLACK)

    # Cells + markers
    for i, row in enumerate(AGENT_POWERS):
        label = row[0]
        statuses = row[1:8]
        holder = row[8] if len(row) > 8 else ""

        # row label
        ax.text(-0.12, n_rows - i - 1 + 0.5, label,
                ha="right", va="center", fontsize=8, color=BLACK)

        # holder annotation
        if holder:
            ax.text(n_cols + 0.08, n_rows - i - 1 + 0.5, holder,
                    ha="left", va="center", fontsize=6.5, color=GRAY_MED, style="italic")

        for j, st in enumerate(statuses):
            cx = j + 0.5
            cy = n_rows - i - 1 + 0.5
            rect = Rectangle((j, n_rows - i - 1), 1, 1,
                             facecolor=WHITE, edgecolor=GRAY_LIGHT, linewidth=0.3)
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
    fig.text(0.06, 0.94, "Plate 4 — Powers x Agent Sub-Stratum",
             fontsize=16, fontweight="bold", color=BLACK, ha="left")
    fig.text(0.06, 0.915, "Volume III  ·  Helmer's 7 Powers across 14 agent sub-strata.",
             fontsize=10, color=BLACK, ha="left")
    fig.text(0.06, 0.895, "Filled = held; accent (blue) = strengthening; outline = eroding.",
             fontsize=9, color=BLACK, ha="left")

    # Legend (bottom)
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

    fig.text(0.06, 0.005, "Source: AI_AGENTS_MASTER Ch 2 §2.3.",
             fontsize=7, color=GRAY_MED, ha="left", style="italic")

    _save(fig, PLATES_DIR / "04_agent_powers_grid.svg")


# =============================================================================
# Plate 5 — Agent Cross-Sub-Stratum Flows
# =============================================================================

def build_agent_cross_substratum_flows():
    fig = _new_fig()
    ax = fig.add_axes([0.05, 0.06, 0.90, 0.86])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13.5)
    ax.set_axis_off()

    # Title + subtitle
    ax.text(0, 13.2, "Plate 5 — Cross-Sub-Stratum Flows",
            fontsize=16, fontweight="bold", color=BLACK, ha="left", va="top")
    ax.text(0, 12.85, "Volume III  ·  Dependencies (gray), risk propagation (blue thick), bet coupling (blue dotted).",
            fontsize=10, color=BLACK, ha="left", va="top")

    # Lay out 10 sub-stratum nodes in a vertical column
    n = len(FLOW_STRATA_LABELS)
    top_y = 12.0
    bot_y = 1.6
    step = (top_y - bot_y) / (n - 1)
    node_x = 2.4
    node_w = 3.8
    node_h = 0.55

    node_pos = {}
    for i, lbl in enumerate(FLOW_STRATA_LABELS):
        y = top_y - i * step
        node_pos[lbl] = (node_x, y)
        rect = Rectangle((node_x - node_w/2, y - node_h/2), node_w, node_h,
                         facecolor=WHITE, edgecolor=BLACK, linewidth=0.7, zorder=3)
        ax.add_patch(rect)
        ax.text(node_x, y, lbl, ha="center", va="center", fontsize=8.5,
                fontweight="bold", color=BLACK, zorder=4)

    # Dependency edges (light gray, to the LEFT of the column)
    for src, dst in FLOW_DEPS:
        if src in node_pos and dst in node_pos:
            x1, y1 = node_pos[src]
            x2, y2 = node_pos[dst]
            # Curved arrow on the left side
            arrow = FancyArrowPatch(
                (x1 - node_w/2, y1), (x2 - node_w/2, y2),
                arrowstyle="->", color=GRAY_LIGHT, lw=1.0,
                mutation_scale=10,
                connectionstyle="arc3,rad=0.20",
                zorder=2,
            )
            ax.add_patch(arrow)

    # Risk propagation paths (accent, thick) — right side
    risk_anchor_x = node_x + node_w/2 + 1.5
    risk_anchor_y_top = 11.6
    risk_anchor_dy = 0.55

    for k, (rid, rlabel, strata) in enumerate(FLOW_RISKS):
        ay = risk_anchor_y_top - k * risk_anchor_dy
        rect = Rectangle((risk_anchor_x, ay - 0.22), 4.7, 0.44,
                         facecolor=WHITE, edgecolor=ACCENT, linewidth=1.2, zorder=3)
        ax.add_patch(rect)
        ax.text(risk_anchor_x + 0.1, ay, f"{rid}  {rlabel}",
                fontsize=8, fontweight="bold", color=ACCENT,
                ha="left", va="center", zorder=4)

        for s in strata:
            if s in node_pos:
                sx, sy = node_pos[s]
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

    # Bet-coupling lines (dotted accent) below the risks
    coupling_y_top = 7.6
    coupling_dy = 0.55
    for ci, (clabel, edges) in enumerate(FLOW_COUPLINGS):
        ly = coupling_y_top - ci * coupling_dy
        rect = Rectangle((risk_anchor_x, ly - 0.22), 4.7, 0.44,
                         facecolor=WHITE, edgecolor=ACCENT, linewidth=1.0,
                         linestyle="--", zorder=3)
        ax.add_patch(rect)
        ax.text(risk_anchor_x + 0.1, ly, clabel,
                fontsize=7.5, fontweight="bold", color=ACCENT,
                ha="left", va="center", zorder=4)

        # Dotted accent connectors between strata pairs (on the right side of column)
        for s1, s2 in edges:
            if s1 in node_pos and s2 in node_pos:
                x1, y1 = node_pos[s1]
                x2, y2 = node_pos[s2]
                conn_x = node_x + node_w/2 + 0.25
                # Vertical dotted line
                ax.plot([conn_x, conn_x], [y1, y2],
                        color=ACCENT, linewidth=1.4, linestyle=":", zorder=2)
                # Tie-bars to each node
                ax.plot([node_x + node_w/2, conn_x], [y1, y1],
                        color=ACCENT, linewidth=1.4, linestyle=":", zorder=2)
                ax.plot([node_x + node_w/2, conn_x], [y2, y2],
                        color=ACCENT, linewidth=1.4, linestyle=":", zorder=2)

    # Legend
    leg_y = 1.0
    ax.annotate("", xy=(1.1, leg_y), xytext=(0.4, leg_y),
                arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT, lw=1.2))
    ax.text(1.2, leg_y, "Dependency", fontsize=8, color=BLACK, ha="left", va="center")

    arrow = FancyArrowPatch((3.0, leg_y), (3.7, leg_y),
                            arrowstyle="->", color=ACCENT, lw=1.6, mutation_scale=12)
    ax.add_patch(arrow)
    ax.text(3.8, leg_y, "Risk propagation", fontsize=8, color=BLACK, ha="left", va="center")

    ax.plot([6.0, 6.7], [leg_y, leg_y], color=ACCENT, linewidth=1.4, linestyle=":")
    ax.text(6.8, leg_y, "Bet coupling", fontsize=8, color=BLACK, ha="left", va="center")

    # Source caption
    ax.text(0, 0.3, "Source: AI_AGENTS_MASTER Ch 3 §3.6, Ch 1 binding constraints, and Ch 3 §3.2 (5 Risks).",
            fontsize=7, color=GRAY_MED, ha="left", va="bottom", style="italic")

    _save(fig, PLATES_DIR / "05_agent_cross_substratum_flows.svg")


# =============================================================================
# main
# =============================================================================

def main():
    PLATES_DIR.mkdir(parents=True, exist_ok=True)
    build_agent_substrate_column()
    build_agent_ocq_heatmap()
    build_agent_wardley_map()
    build_agent_powers_grid()
    build_agent_cross_substratum_flows()
    print("Generated:")
    for p in sorted(PLATES_DIR.glob("0*.svg")):
        print(f"  {p}  ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
