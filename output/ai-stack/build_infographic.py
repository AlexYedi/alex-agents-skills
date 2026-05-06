"""
SUBSTRATE — A stratigraphic atlas of the AI stack
Multi-page PDF infographic, museum-quality.
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

# Resolve actual family names from registered files
def fam(filename):
    return fm.FontProperties(fname=os.path.join(FONT_DIR, filename)).get_name()

F_DISPLAY = fam("BigShoulders-Bold.ttf")        # ultra-condensed bold display caps
F_DISPLAY_REG = fam("BigShoulders-Regular.ttf") # condensed regular
F_NARROW = fam("Boldonse-Regular.ttf")          # narrow display
F_SERIF = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT = fam("InstrumentSerif-Italic.ttf")
F_SANS = fam("InstrumentSans-Regular.ttf")
F_SANS_BOLD = fam("InstrumentSans-Bold.ttf")
F_MONO = fam("GeistMono-Regular.ttf")
F_MONO_BOLD = fam("GeistMono-Bold.ttf")
F_PLEX_MONO = fam("IBMPlexMono-Regular.ttf")
F_DMMONO = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42


def sp(text, n=1):
    """Letterspacing helper: insert (n) thin spaces between visible chars."""
    if n <= 0:
        return text
    sep = " " * n  # hairspace approximation
    out = []
    prev = ""
    for ch in text:
        if out:
            out.append(sep)
        out.append(ch)
        prev = ch
    return "".join(out)

# ---------- Palette ----------
PAPER = "#F1E9D6"
INK = "#171210"
INK_SOFT = "#3A2F26"
GRAY = "#7A6E60"
GRAY_LIGHT = "#C9BFA9"
RULE = "#2A211B"
VERMILION = "#A6371F"
VERDIGRIS = "#456C5C"
OCHRE = "#A37425"

# ---------- Page geometry (tabloid portrait, 11 x 17 in) ----------
PAGE_W = 11.0
PAGE_H = 17.0
DPI = 300

OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-stack/AI_STACK_SUBSTRATE.pdf"


def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=DPI, facecolor=PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 154.5)  # 100 wide × proportional
    ax.set_facecolor(PAPER)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def page_frame(ax, plate_no, title_top, subtitle_top, latin, plate_label):
    """Draw the standardized chart frame: margins, depth scale, title block, footer."""
    LEFT = 8.5
    RIGHT = 92.5
    TOP = 148.5
    BOTTOM = 9.5

    # Outer hairline border
    rect = mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                              fill=False, ec=RULE, lw=0.55)
    ax.add_patch(rect)

    # Inner ruled gutters (top/bottom band)
    ax.plot([LEFT, RIGHT], [TOP - 6.0, TOP - 6.0], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 4.5, BOTTOM + 4.5], color=RULE, lw=0.45)

    # Left depth-scale (margin tick rule)
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

    # Title block (top)
    ax.text(LEFT, TOP - 1.0, sp("AN ATLAS OF THE INTELLIGENCE STRATA", 4),
            ha="left", va="top", fontsize=6.0, fontname=F_MONO, color=GRAY,
            )
    ax.text(LEFT, TOP - 1.9, title_top.upper(),
            ha="left", va="top", fontsize=18, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.0, TOP - 2.0, sp(plate_label, 2),
            ha="right", va="top", fontsize=7.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 4.5, subtitle_top,
            ha="left", va="top", fontsize=6.2, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4, latin,
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)

    # Plate number badge (top-right)
    ax.add_patch(mpatches.Circle((RIGHT - 1.4, TOP - 2.0), 1.05, fill=False,
                                 ec=VERMILION, lw=0.6))
    ax.text(RIGHT - 1.4, TOP - 2.0, plate_no, ha="center", va="center",
            fontsize=6.2, fontname=F_MONO_BOLD, color=VERMILION)

    # Footer bar
    ax.text(LEFT, BOTTOM + 3.0, sp("SUBSTRATE — A REFERENCE COMPILATION", 3),
            ha="left", va="top", fontsize=4.6, fontname=F_MONO, color=GRAY,
            )
    ax.text(LEFT, BOTTOM + 1.4, sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, plate_label, ha="right", va="top",
            fontsize=5.4, fontname=F_DMMONO, color=GRAY)
    ax.text(50, BOTTOM + 1.4, "·   ·   ·   ·   ·", ha="center", va="top",
            fontsize=5, fontname=F_MONO, color=GRAY_LIGHT)

    return LEFT, RIGHT, TOP - 6.5, BOTTOM + 4.7


# ---------- Stratum drawing primitives ----------

def stratum(ax, x0, x1, y_top, height, *, num, name, scale, accent=INK_SOFT,
            tagline=None):
    """Draw one stratum: a labeled horizontal register."""
    y_bot = y_top - height
    # Top and bottom hairlines
    ax.plot([x0, x1], [y_top, y_top], color=RULE, lw=0.5)
    ax.plot([x0, x1], [y_bot, y_bot], color=RULE, lw=0.35)

    # Left label column
    label_x_right = x0 + 16.5
    # Numeral
    ax.text(x0 + 0.5, y_top - 1.8, num, ha="left", va="top",
            fontsize=8.5, fontname=F_DMMONO, color=accent, )
    # Stratum name (condensed display caps)
    name_lines = name.split("\n")
    for i, line in enumerate(name_lines):
        ax.text(x0 + 0.5, y_top - 4.0 - i*2.6, line, ha="left", va="top",
                fontsize=10.0, fontname=F_DISPLAY, color=INK)
    # Scale (depth descriptor) — italic latin
    ax.text(x0 + 0.5, y_bot + 1.2, scale, ha="left", va="bottom",
            fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)
    if tagline:
        ax.text(x0 + 0.5, y_bot + 0.0, sp(tagline, 2), ha="left", va="bottom",
                fontsize=4.4, fontname=F_MONO, color=GRAY)

    # Vertical divider between label column and content area
    ax.plot([label_x_right, label_x_right], [y_top - 0.4, y_bot + 0.4],
            color=RULE, lw=0.3, ls=(0, (0.6, 0.9)))
    return label_x_right, y_top, y_bot


def node(ax, x, y, label, sublabel=None, *, dot=True, color=INK):
    if dot:
        ax.add_patch(mpatches.Circle((x, y), 0.32, fc=color, ec=color, lw=0))
    ax.text(x + 0.85, y + 0.05, label, ha="left", va="center",
            fontsize=5.6, fontname=F_SERIF, color=INK)
    if sublabel:
        ax.text(x + 0.85, y - 1.1, sp(sublabel, 1), ha="left", va="center",
                fontsize=4.3, fontname=F_MONO, color=GRAY)


def grid_nodes(ax, items, *, x0, x1, y_top, y_bot, cols=4, color=INK,
               row_h=2.4, top_pad=1.2):
    """Place a grid of nodes. items = list of (label, sublabel|None)."""
    rows = int(np.ceil(len(items) / cols))
    cw = (x1 - x0) / cols
    for i, it in enumerate(items):
        r = i // cols
        c = i % cols
        x = x0 + c * cw + 0.4
        y = y_top - top_pad - r * row_h
        if y - 1.2 < y_bot:
            break
        lbl = it[0] if isinstance(it, tuple) else it
        sub = it[1] if (isinstance(it, tuple) and len(it) > 1) else None
        node(ax, x, y, lbl, sub, color=color)


def hr_band(ax, x0, x1, y, *, label, color=GRAY, dash=False):
    ls = (0, (1.5, 2.0)) if dash else "-"
    ax.plot([x0, x1], [y, y], color=color, lw=0.35, ls=ls)
    ax.text(x0 + 0.4, y + 0.4, sp(label, 2), ha="left", va="bottom",
            fontsize=4.2, fontname=F_MONO, color=color)


def metric_bar(ax, x, y, width, label, value, *, accent=VERMILION):
    """Small annotational metric block — label above, value below the rule."""
    ax.plot([x, x + width], [y, y], color=accent, lw=0.7)
    ax.text(x, y + 0.4, sp(label, 2), ha="left", va="bottom",
            fontsize=4.0, fontname=F_MONO, color=GRAY)
    ax.text(x + width, y - 0.2, value, ha="right", va="top",
            fontsize=8.5, fontname=F_DISPLAY, color=INK)


# ============================================================
# PAGE 1 — Index plate (the full column, abbreviated)
# ============================================================

def page_index(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(
        ax, "I",
        "The Intelligence Stratum",
        "A vertical compilation, from the substrate of electrical generation to the surface of the user interface.",
        "Substratum a generatione electrica usque ad interfaciem hominis · ordo descendens",
        "PLATE I OF VI",
    )
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Big subtitle
    ax.text(inner_x0, TOP - 0.5,
            sp("XIV STRATA · DESCENDING", 4),
            ha="left", va="top", fontsize=8.2, fontname=F_DISPLAY,
            color=VERMILION, )
    ax.plot([inner_x0, inner_x1], [TOP - 2.2, TOP - 2.2], color=RULE, lw=0.4)

    strata = [
        ("XIV", "USER · INTERFACE", "interfaces", "homo sapiens — chat · search · code · agent · voice"),
        ("XIII", "APPLICATION · AGENT", "applications", "harvey · cursor · sierra · perplexity · claude.ai"),
        ("XII",  "ORCHESTRATION", "frameworks", "langgraph · agent sdks · mcp · gateways · evals"),
        ("XI",   "RETRIEVAL · MEMORY", "vectors & graphs", "pinecone · qdrant · weaviate · graphrag · letta"),
        ("X",    "INFERENCE · SERVING", "runtimes", "vllm · sglang · tensorrt-llm · dynamo · mlx"),
        ("IX",   "MODEL · PROVIDERS", "apis", "anthropic · openai · google · meta · mistral · deepseek"),
        ("VIII", "POST-TRAINING", "alignment", "sft · dpo · rlhf · rlaif · grpo · rlvr · thinking"),
        ("VII",  "PRE-TRAINING", "foundation models", "transformer · moe · mamba · diffusion-lm"),
        ("VI",   "DATA · CORPUS", "tokens & images", "common crawl · fineweb · stack v2 · licensed · synthetic"),
        ("V",    "PARALLELISM · KERNELS", "training stack", "fsdp · megatron · deepspeed · jax · triton · flashattn"),
        ("IV",   "FABRIC · NETWORK", "interconnect", "nvlink · infiniband · ultra ethernet · cpo · ualink"),
        ("III",  "COMPUTE · SILICON", "accelerators", "h200 · b200 · b300 · rubin · tpu · trainium · mtia"),
        ("II",   "FACILITY · DATA CENTER", "physical plant", "racks · cdus · pue · liquid cooling · busways"),
        ("I",    "POWER · GRID", "electrical substrate", "ppa · smr · ccgt · transmission · transformer"),
    ]

    # Compute layout
    avail_top = TOP - 3.2
    avail_bot = BOT + 8.0
    avail_h = avail_top - avail_bot
    h = avail_h / len(strata)

    label_w = 16.0  # left label column
    band_x0 = inner_x0
    band_x1 = inner_x1

    for i, (num, name, scale, desc) in enumerate(strata):
        y_top = avail_top - i * h
        y_bot = y_top - h

        # Row dividers
        ax.plot([band_x0, band_x1], [y_top, y_top], color=RULE, lw=0.35)

        # Numeral column
        ax.text(band_x0 + 0.5, (y_top + y_bot)/2 + 0.2, sp(num, 1), ha="left", va="center",
                fontsize=8.0, fontname=F_DMMONO, color=VERMILION)

        # Stratum name
        ax.text(band_x0 + 9.5, (y_top + y_bot)/2 + 0.6, name, ha="left", va="center",
                fontsize=12.5, fontname=F_DISPLAY, color=INK)
        ax.text(band_x0 + 9.5, (y_top + y_bot)/2 - 1.4, scale, ha="left", va="center",
                fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)

        # Mid divider
        ax.plot([band_x0 + label_w + 17.5, band_x0 + label_w + 17.5],
                [y_top - 0.4, y_bot + 0.4], color=RULE, lw=0.25, ls=(0, (0.6, 0.9)))

        # Description
        ax.text(band_x0 + label_w + 19.0, (y_top + y_bot)/2 + 0.2, desc,
                ha="left", va="center", fontsize=6.4, fontname=F_SERIF, color=INK)

        # Right marker
        ax.add_patch(mpatches.Circle((band_x1 - 1.2, (y_top+y_bot)/2 + 0.2),
                                     0.42, fill=False, ec=INK_SOFT, lw=0.4))
        ax.text(band_x1 - 1.2, (y_top + y_bot)/2 + 0.2, str(14 - i),
                ha="center", va="center",
                fontsize=4.6, fontname=F_DMMONO, color=INK_SOFT)

    # Final bottom line
    ax.plot([band_x0, band_x1], [avail_bot, avail_bot], color=RULE, lw=0.5)

    # Footer key
    ax.text(inner_x0, BOT + 6.5, sp("KEY", 3),
            fontsize=5.2, fontname=F_MONO, color=VERMILION, )
    ax.plot([inner_x0, inner_x1], [BOT + 6.0, BOT + 6.0], color=RULE, lw=0.3)
    keys = [
        ("○", "node, defined element"),
        ("•", "active component"),
        ("—", "dependence, ordered flow"),
        ("¶", "sub-stratum, internal partition"),
    ]
    for i, (sym, txt) in enumerate(keys):
        x = inner_x0 + i * 21
        ax.text(x, BOT + 5.0, sym, fontsize=8, fontname=F_SERIF_DISP, color=VERMILION)
        ax.text(x + 1.8, BOT + 5.0, txt, fontsize=5.2, fontname=F_SERIF_IT,
                color=INK_SOFT, va="center")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# Helper to build a content page with multiple strata
# ============================================================

def build_strata_page(pdf, plate_no, plate_label, title, subtitle, latin, layers):
    """
    layers: list of dicts with keys:
      num, name, scale, tagline, items (list of (label, sublabel|None)),
      cols (int), accent_color (str), height_units (relative)
    """
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, plate_no, title, subtitle, latin, plate_label)
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    # Hairline above first stratum
    ax.plot([inner_x0, inner_x1], [TOP - 0.4, TOP - 0.4], color=RULE, lw=0.5)

    # Distribute heights
    total_units = sum(layer.get("h", 1.0) for layer in layers)
    avail = (TOP - 0.4) - (BOT + 0.5)
    y_cursor = TOP - 0.4

    for layer in layers:
        h = avail * (layer.get("h", 1.0) / total_units)
        y_top = y_cursor
        y_bot = y_cursor - h

        label_x_right, _, _ = stratum(
            ax, inner_x0, inner_x1, y_top, h,
            num=layer["num"], name=layer["name"], scale=layer["scale"],
            tagline=layer.get("tagline"),
            accent=layer.get("accent", VERMILION),
        )

        # Optional pre-content subhead
        sub = layer.get("subhead")
        x_content_left = label_x_right + 1.5
        x_content_right = inner_x1 - 1.0

        content_top = y_top - 1.5
        if sub:
            ax.text(x_content_left, content_top, sp(sub, 1), ha="left", va="top",
                    fontsize=4.8, fontname=F_MONO, color=VERMILION)
            ax.plot([x_content_left, x_content_right],
                    [content_top - 1.4, content_top - 1.4], color=RULE, lw=0.3)
            content_top = content_top - 2.4

        # Reserve metric strip if present
        metric_zone = 4.5 if layer.get("metrics") else 0.8

        # Items
        items = layer.get("items", [])
        if items:
            grid_nodes(ax, items, x0=x_content_left, x1=x_content_right,
                       y_top=content_top, y_bot=y_bot + metric_zone,
                       cols=layer.get("cols", 4),
                       row_h=layer.get("row_h", 2.6),
                       color=layer.get("dot_color", INK_SOFT),
                       top_pad=0.0)

        # Optional metric strip at bottom of stratum
        for j, m in enumerate(layer.get("metrics", [])):
            mx = x_content_left + j * 22
            metric_bar(ax, mx, y_bot + 2.0, 18, m[0], m[1],
                       accent=m[2] if len(m) > 2 else VERMILION)

        y_cursor = y_bot

    # Final hairline
    ax.plot([inner_x0, inner_x1], [BOT + 0.5, BOT + 0.5], color=RULE, lw=0.5)

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PAGE 2 — Strata I–II : Power + Facility
# ============================================================

def page_power_facility(pdf):
    layers = [
        {
            "num": "II",
            "name": "FACILITY",
            "scale": "stratum secundum · the data center",
            "tagline": "TIER · PUE · WUE",
            "subhead": "PHYSICAL PLANT · COOLING · POWER DISTRIBUTION",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("White space · slab", "fully populated GB200 ≈ 4,000 lb"),
                ("Gray space", "MEP · 1.2–1.5× white"),
                ("Substation 230/115 kV", "step-down to 34.5 kV"),
                ("MV switchgear", "ring bus · main-tie-main"),
                ("UPS · static (Li-ion)", "double-conversion isolation"),
                ("UPS · rotary (flywheel)", "Hitec · hyperscale tier"),
                ("Rack-level BBU", "Google / Meta pioneer"),
                ("Busway 800–1,400A", "Starline · Universal"),
                ("PDU · in-row · in-rack", "branch distribution"),
                ("Diesel gensets · 2N", "Caterpillar 3 MW units"),
                ("Gas reciprocating", "prime power, AI campuses"),
                ("CRAH · CRAC (legacy)", "<30 kW/rack"),
                ("Rear-door HX", "up to 80 kW/rack"),
                ("Direct-to-chip cold plate", "GB200 · in-rack 250 kW CDU"),
                ("Single-phase immersion", "GRC · Submer · LiquidStack"),
                ("Two-phase immersion", "PFAS retreat 2025"),
                ("Tier I–IV (Uptime)", "AI training trends Tier II–III"),
                ("PUE", "best-in-class 1.10–1.20"),
                ("WUE", "<0.20 L/kWh target"),
                ("OCP · Open Rack v3", "48 V DC · vertical busbar"),
            ],
            "metrics": [
                ("RACK · GB200 NVL72", "132 kW"),
                ("RACK · RUBIN ULTRA KYBER", "≈600 kW"),
                ("BUILD · $/MW IT", "$10–15 M"),
            ],
        },
        {
            "num": "I",
            "name": "POWER",
            "scale": "stratum primum · the electrical substrate",
            "tagline": "PPA · SMR · GRID · TRANSMISSION",
            "subhead": "GENERATION · TRANSMISSION · INTERCONNECTION QUEUE",
            "h": 1.05, "cols": 4, "row_h": 2.5, "accent": VERDIGRIS,
            "items": [
                ("PPA · MSFT–TMI Unit 1", "835 MW · 20-yr · restart 2027"),
                ("PPA · AWS–Susquehanna", "1,920 MW · front-of-meter"),
                ("AWS · X-energy SMR", "5 GW Xe-100 by 2039"),
                ("Google · Kairos KP-FHR", "500 MW · 2030–35"),
                ("Google · Fervo geothermal", "Cape Station 500 MW · UT"),
                ("Meta · Hyperion CCGT", ">7 GW · Entergy LA"),
                ("xAI · Memphis turbines", "≈35 Solar SMT-130 · 16 MW"),
                ("Stargate · Abilene live", "$500B · 4-yr · 10 GW"),
                ("PJM · Dominion zone", "$444.26/MW-day capacity"),
                ("ERCOT · Stargate, Crusoe", "150 GW peak target 2030"),
                ("MISO · Hyperion footprint", "Entergy · MISO South"),
                ("FERC Order 2023", "first-ready first-served"),
                ("BTM · ratepayer cost-shift", "Talen-AWS precedent"),
                ("NuScale VOYGR · 77 MWe", "first NRC-approved SMR"),
                ("X-energy Xe-100 · TRISO", "80 MWe HTGR"),
                ("Kairos KP-FHR · molten salt", "fluoride salt-cooled HTR"),
                ("TerraPower Natrium · WY", "345 MW · sodium fast"),
                ("Holtec · GE BWRX-300", "Westinghouse AP300"),
                ("Transformer lead time", "≈120 wk · power · 2.3 yr"),
                ("Transmission permit horizon", "≈10 yr greenfield"),
            ],
            "metrics": [
                ("DC LOAD · US 2030", "9–17%"),
                ("PJM 25/26 BRA", "+833%"),
                ("INTERCONNECT QUEUE", "≈2,290 GW"),
            ],
        },
    ]
    build_strata_page(
        pdf, "II", "PLATE II OF VI",
        "Power · Facility",
        "The substrate of generation, transmission, transformation; the shell, the loop, the pour.",
        "Stratum I · II — generatio · transmissio · refrigeratio · distributio electrica",
        layers,
    )


# ============================================================
# PAGE 3 — Strata III–V : Compute · Fabric · Parallelism
# ============================================================

def page_compute_fabric(pdf):
    layers = [
        {
            "num": "V",
            "name": "PARALLELISM",
            "scale": "stratum quintum · the training stack",
            "tagline": "FRAMEWORKS · KERNELS · COMPILERS",
            "subhead": "FRAMEWORKS · 4D PARALLELISM · KERNELS",
            "h": 0.78, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("PyTorch · FSDP / FSDP2", "DTensor · sharded params"),
                ("JAX · pjit · shard_map", "Google · TPU pods"),
                ("Megatron-LM / Megatron-Core", "TP+PP+EP · NVIDIA reference"),
                ("DeepSpeed · ZeRO 1/2/3", "Microsoft · MoE all-to-all"),
                ("MaxText · Pax · Praxis", "Gemini-class JAX"),
                ("MindSpore · PaddlePaddle", "Huawei · Baidu"),
                ("Mosaic Composer · LLM Foundry", "Databricks"),
                ("HF Accelerate · TRL", "open-ecosystem default"),
                ("torch.compile · Inductor", "graph capture + fusion"),
                ("XLA · HLO compiler", "JAX / TF AOT"),
                ("OpenAI Triton", "every modern GPU kernel"),
                ("FlashAttention 2 / 3", "75% MFU · FP8"),
                ("ThunderKittens · Mojo", "tile DSL · Modular"),
                ("FlashInfer · vLLM CUDA graphs", "serving kernels"),
                ("NCCL · RCCL · OneCCL", "all-reduce · all-to-all"),
                ("SHARP v4 · in-network reduce", "≈9× collective speedup"),
                ("DP · TP · PP · EP", "4D parallelism"),
                ("Async checkpointing", "Meta: 2.1% wall clock"),
                ("Run:ai / KAI · Slurm / SchedMD", "NVIDIA-owned schedulers"),
                ("Ray · SkyPilot · Determined", "fungible orchestration"),
            ],
        },
        {
            "num": "IV",
            "name": "FABRIC",
            "scale": "stratum quartum · the interconnect",
            "tagline": "NVLINK · INFINIBAND · ETHERNET · OPTICS",
            "subhead": "SCALE-UP · SCALE-OUT · OPTICAL · STORAGE",
            "h": 0.92, "cols": 4, "row_h": 2.55, "accent": VERMILION,
            "items": [
                ("NVLink 4 · Hopper", "900 GB/s · 4th-gen NVSwitch"),
                ("NVLink 5 · Blackwell", "1.8 TB/s · 130 TB/s rack"),
                ("NVLink 6 · Rubin", "≈3.6 TB/s per GPU"),
                ("NVLink 7 · Rubin Ultra", "1.5 PB/s aggregate"),
                ("AMD Infinity Fabric · 8-GPU", "MI300X / MI355X"),
                ("UALink 1.0 · 200 Gbps/lane", "1,024-accel open fabric"),
                ("PCIe Gen5 · Gen6 · Gen7", "32→64→128 GT/s/lane"),
                ("CXL 3.x · CXL 4.0 (Nov 2025)", "memory pooling, KV spill"),
                ("InfiniBand NDR · 400 G", "Quantum-2 QM9700"),
                ("InfiniBand XDR · 800 G", "Quantum-X800 · 144×800"),
                ("Spectrum-X · 51.2 Tb/s", "RoCE adaptive · BlueField"),
                ("Tomahawk 5 · 6 (102.4 Tb/s)", "Broadcom Davisson"),
                ("Cisco Silicon One P200", "51.2 Tb/s · 1,000 km coherent"),
                ("Ultra Ethernet 1.0 · UEC", "open InfiniBand alternative"),
                ("BlueField-3 · BlueField-4", "400→800 Gbps DPU"),
                ("AMD Pensando Pollara 400", "UEC AI NIC"),
                ("AWS Nitro · Intel IPU E2100", "DPU diaspora"),
                ("Pluggable optics 800 G · 1.6 T", "OSFP · QSFP-DD"),
                ("LPO · LRO", "−30–50% module power"),
                ("Co-Packaged Optics · CPO", "Quantum-X Photonics 2025"),
                ("Ayar Labs · Lightmatter", "photonic chiplets · interposer"),
                ("Fat-tree · rail-optimized", "Clos · Dragonfly+"),
                ("GPUDirect Storage · NVMe-oF", "RoCEv2 / IB transport"),
                ("WekaIO · VAST · DDN · Lustre", "parallel FS · 4 TB/s @ Eos"),
            ],
        },
        {
            "num": "III",
            "name": "COMPUTE",
            "scale": "stratum tertium · the silicon",
            "tagline": "GPU · TPU · ASIC · HBM · COWOS",
            "subhead": "ACCELERATORS · MEMORY · FOUNDRY · HOST CPU",
            "h": 1.18, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("NVIDIA H100 · Hopper 4N", "80 GB HBM3 · 700 W"),
                ("NVIDIA H200 · refresh", "141 GB HBM3e · 4.8 TB/s"),
                ("NVIDIA B200 · Blackwell 4NP", "192 GB · 8 TB/s · 1,000 W"),
                ("NVIDIA B300 · Ultra", "288 GB · 1.4 kW · FP4 dense"),
                ("NVIDIA Rubin · NVL144", "HBM4 · 13 TB/s · 2H 2026"),
                ("NVIDIA Rubin Ultra · NVL576", "365 TB · 600 kW · 2027"),
                ("NVIDIA Feynman · Rosa", "CPO native · 2028"),
                ("AMD MI300X · MI325X · MI355X", "288 GB HBM3e · CDNA 4"),
                ("AMD MI400 · Helios", "rack-scale · EPYC Venice"),
                ("Intel Gaudi 3 · Jaguar Shores", "rack-system pivot"),
                ("Google TPU Ironwood (v7)", "192 GB · 9,216-chip pod"),
                ("Google Trillium (v6e)", "transformer-tuned · 256² array"),
                ("Google Axion · Arm CPU", "Neoverse V2"),
                ("AWS Trainium 2", "96 GiB · 1.3 PFLOPS FP8"),
                ("AWS Trainium 3 · 3 nm", "2.52 PFLOPS · 144 GB · MXFP4"),
                ("AWS Inferentia 2", "32 GB · 190 TFLOPS FP16"),
                ("AWS Graviton 4", "96 Neoverse V2"),
                ("MSFT Maia 100 · Maia 200", "216 GB HBM3e · 750 W"),
                ("MSFT Cobalt 100 · Cobalt 200", "Neoverse N2 → V3"),
                ("Meta MTIA v1 · v2 · 300–500", "ranking → training"),
                ("Apple M5 · A19 Pro · Baltra", "MLX · ANE · cloud chip 2027"),
                ("Cerebras WSE-3 · WSE-4", "wafer scale · 900k cores"),
                ("Groq LPU", "deterministic · SRAM-only"),
                ("SambaNova RDU SN40L", "memory-resident large MoE"),
                ("Tenstorrent Wormhole · Blackhole", "RISC-V · open"),
                ("Etched Sohu · transformer ASIC", "Llama 70B claim 500k tok/s"),
                ("d-Matrix · MatX · Lightmatter", "inference / photonic ASICs"),
                ("Qualcomm Cloud AI 100 Ultra", "edge inference 400 TOPS"),
                ("HBM3e · HBM4 · HBM4e", "SK Hynix 62% · Micron 21%"),
                ("CoWoS-S · CoWoS-L · SoIC", "TSMC packaging bottleneck"),
                ("TSMC N4 · N3 · N2 · A16", "leading-edge logic"),
                ("Intel 18A · High-NA EUV", "Foundry comeback · MSFT, DoD"),
                ("Xeon 6 Granite Rapids · Sierra Forest", "128 P / 288 E"),
                ("EPYC 9005 Turin · 9754 Bergamo", "192 cores · default host"),
                ("Grace · Vera · Rosa", "NVIDIA Arm CPUs"),
                ("AmpereOne · Ampere M Polaris", "192 cores → 256 cores"),
            ],
            "metrics": [
                ("NVIDIA AI ACCEL SHARE", "≈80%"),
                ("HBM4 SOURCE · SK HYNIX", "62%"),
                ("CHIP TDP · H100 → R-ULTRA", "0.7 → 3.6 kW"),
            ],
        },
    ]
    build_strata_page(
        pdf, "III", "PLATE III OF VI",
        "Compute · Fabric · Parallelism",
        "The silicon column, the copper-and-photon weave, the orchestration of flops into a coherent gradient.",
        "Stratum III · IV · V — silicium · cuprum · photonum · gradus parallelus quadridimensionalis",
        layers,
    )


# ============================================================
# PAGE 4 — Strata VI–VIII : Data · Pretraining · Post-training
# ============================================================

def page_data_models(pdf):
    layers = [
        {
            "num": "VIII",
            "name": "POST-TRAINING",
            "scale": "stratum octavum · alignment & reasoning",
            "tagline": "SFT · RLHF · CAI · GRPO · RLVR",
            "subhead": "ALIGNMENT METHODS · REASONING · DISTILLATION",
            "h": 0.85, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("SFT · instruction tuning", "LIMA-style: quality > quantity"),
                ("RLHF · PPO + reward model", "InstructGPT lineage"),
                ("DPO · IPO · KTO · ORPO", "preference without RM"),
                ("RLAIF · Constitutional AI", "Anthropic · LLM critic"),
                ("Process Reward Models", "step-level supervision"),
                ("RLVR · verifiable rewards", "math / code / proof"),
                ("GRPO · DeepSeek", "no value net · group-relative"),
                ("R1-Zero · pure-RL reasoning", "no SFT cold start"),
                ("Test-time compute", "o1 / o3 · Claude thinking"),
                ("Adaptive thinking budgets", "64k thinking tokens"),
                ("MCTS · best-of-N · debate", "rollout-based reasoning"),
                ("Distillation · teacher → student", "Behemoth → Maverick"),
                ("Speculative decoding", "EAGLE-3 · 3–6× speedup"),
                ("Chain-of-thought monitorability", "FMF Jan 2026 paper"),
                ("Red team · jailbreak suites", "HarmBench · WMDP · Cybench"),
                ("Auto red-teaming · best-of-N", "GCG attacks"),
            ],
        },
        {
            "num": "VII",
            "name": "PRE-TRAINING",
            "scale": "stratum septimum · the foundation model",
            "tagline": "TRANSFORMER · MOE · MAMBA · DIFFUSION-LM",
            "subhead": "ARCHITECTURE · ATTENTION · POSITION · MULTIMODAL",
            "h": 0.92, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Transformer decoder-only", "the trunk"),
                ("MHA · MQA · GQA", "attention head sharing"),
                ("MLA · DeepSeek V2/V3", "32× KV compression"),
                ("Sliding-window · attention sinks", "Mistral · long context"),
                ("FlashAttention 2/3", "IO-aware kernels · 75% MFU"),
                ("RoPE · YaRN · ALiBi · NoPE", "position encoding"),
                ("Mixtral 8×7B · 8×22B", "open MoE breakthrough"),
                ("DeepSeek V2 · V3 · V4-Pro", "256 routed + shared expert"),
                ("Qwen 2.5 · 3 · 3.5 · QwQ", "Apache 2.0 · thinking toggle"),
                ("Llama 4 Scout · Maverick · Behemoth", "natively multimodal MoE"),
                ("Mistral Large 3 · Codestral · Pixtral", "Apache 2.0 turn"),
                ("Mamba · Mamba-2 · SSM", "linear-time alternatives"),
                ("Jamba · Nemotron Nano 2", "Transformer-Mamba hybrid"),
                ("Mercury · Inception Labs", "diffusion LM · ≈10× faster"),
                ("Vision · ViT · SigLIP 2 · AIM", "Gemma · Janus-Pro"),
                ("Unified multimodal tokenizers", "Chameleon · Show-o"),
                ("Audio · Whisper · Moshi", "full-duplex speech"),
                ("Tokenizer · BPE · SentencePiece", "200k vocab GPT-4o"),
                ("Chinchilla scaling laws", "≈20 tok/param compute-opt"),
                ("Inference-aware overtraining", "Llama 3 · 1,875 tok/param"),
            ],
        },
        {
            "num": "VI",
            "name": "DATA",
            "scale": "stratum sextum · the corpus",
            "tagline": "TOKENS · LICENSING · SYNTHETIC",
            "subhead": "WEB · CODE · BOOKS · MULTIMODAL · SYNTHETIC · LITIGATION",
            "h": 1.1, "cols": 4, "row_h": 2.5, "accent": VERDIGRIS,
            "items": [
                ("Common Crawl · monthly", "raw substrate of web"),
                ("CCNet · Meta", "perplexity-filter pipeline"),
                ("RefinedWeb · Falcon", "web-only matches curated"),
                ("RedPajama-Data v2 · 30T", "84 CC dumps · annotated"),
                ("FineWeb · 15T", "96 CC snapshots · HF"),
                ("FineWeb-Edu · 1.3T", "Llama-3-70B classifier"),
                ("Dolma · AI2 · 3T", "fully documented"),
                ("Nemotron-CC v2 · 1.9T synth", "NVIDIA · ensemble + rephrase"),
                ("The Pile (legacy)", "Books3 flashpoint"),
                ("BigCode · The Stack v2 · 67.5 TB", "SWHID-traceable · opt-out"),
                ("StarCoder2 · 4.3T tokens", "code at scale"),
                ("arXiv · PubMed · S2ORC · OpenAlex", "academic"),
                ("Project Gutenberg · clean", "≈70k public-domain books"),
                ("Books3 · Anna's Archive · LibGen", "litigated shadow corpora"),
                ("CulturaX · mC4 · ROOTS · OSCAR", "multilingual corpora"),
                ("LAION-5B · Re-LAION-5B", "image-text pairs"),
                ("DataComp / CommonPool · 12.8B", "filter-design contest"),
                ("COYO · DOCCI", "alt multimodal"),
                ("Synthetic data · Nemotron-CC", "1.9T synth · Phi · R1 distill"),
                ("Reddit licensing · Google $60M", "OpenAI ≈$70M · Reddit suit"),
                ("AP · Axel Springer · FT · Stack OF", "above-board licensed"),
                ("HarperCollins · Wiley · T&F", "books opt-in"),
                ("Cloudflare default-block · 7/2025", "Pay-Per-Crawl · HTTP 402"),
                ("C2PA · SynthID · watermarks", "provenance / labeling"),
                ("Bartz v. Anthropic · $1.5 B", "largest US copyright recovery"),
                ("NYT v. OpenAI · ongoing", "consolidated SDNY"),
                ("MinHash · LSH · exact dedupe", "Lee 2022 · ≈10× speedup"),
                ("FastText · LLM-as-judge classifiers", "DCLM · FineWeb-Edu"),
                ("DSIR · DoReMi", "domain weighting"),
                ("PII scrubbing · DP-SGD (rare)", "boundary control"),
            ],
            "metrics": [
                ("FRONTIER PRE-TRAIN COST", "$0.5–1 B"),
                ("DEEPSEEK V3 COMPUTE", "$5.6 M"),
                ("BARTZ SETTLEMENT", "$1.5 B"),
            ],
        },
    ]
    build_strata_page(
        pdf, "IV", "PLATE IV OF VI",
        "Data · Pre-training · Post-training",
        "The corpus, the architecture, the alignment — pretraining became a phase, not the destination.",
        "Stratum VI · VII · VIII — corpus · architectura · ratio · alignmentum",
        layers,
    )


# ============================================================
# PAGE 5 — Strata IX–XIV : Models · Inference · Apps · User
# ============================================================

def page_inference_apps(pdf):
    layers = [
        {
            "num": "XIV",
            "name": "USER",
            "scale": "stratum decimum quartum · the human",
            "tagline": "SURFACE · INTENT · LOOP",
            "subhead": "INTERFACES · MODALITIES · WORKFLOWS",
            "h": 0.55, "cols": 4, "row_h": 2.5, "accent": OCHRE,
            "items": [
                ("Chat · text", "ChatGPT 64.5% · Gemini 21.5%"),
                ("Chat · voice", "Advanced Voice · gpt-realtime"),
                ("IDE · pair-programmer", "Cursor · Copilot · Windsurf"),
                ("Terminal agent", "Claude Code · Codex CLI · Devin"),
                ("Browser · agent", "Operator · Mariner · Claude Chrome"),
                ("Computer · screen / kbd / mouse", "Anthropic Computer Use"),
                ("Mobile · on-device", "Apple Intelligence · Gemini Nano"),
                ("API · developer", "Python · TS · Go · Rust SDKs"),
            ],
        },
        {
            "num": "XIII",
            "name": "APPLICATION · AGENT",
            "scale": "stratum decimum tertium · the products",
            "tagline": "VERTICAL · HORIZONTAL · CREATIVE",
            "subhead": "GENERAL · CODING · SEARCH · CX · CREATIVE · VOICE",
            "h": 0.95, "cols": 4, "row_h": 2.55, "accent": VERMILION,
            "items": [
                ("ChatGPT · Claude · Gemini", "general assistants · ~900M WAU"),
                ("Perplexity · You.com · SearchGPT", "$20B · 780M monthly Q"),
                ("MS Copilot · Workspace Gemini", "$30/user · M365 add-on"),
                ("Notion AI · Slack AI · Coda AI", "productivity"),
                ("Granola · Read AI · Mem", "meeting / note assistants"),
                ("Cursor · Windsurf · Cline · Aider", "coding IDE"),
                ("GitHub Copilot · Cody · Tabnine", "incumbent coding"),
                ("Devin · Factory · Augment · Replit Agent", "agentic coding"),
                ("Bolt.new · v0 · Lovable · StackBlitz", "AI app builders"),
                ("Harvey · Hippocratic · Glean", "vertical: legal / health / search"),
                ("Sierra · Decagon · Ema · Cresta", "CX agents · $10B Sierra"),
                ("Midjourney · Flux · Ideogram · Imagen 4", "image generation"),
                ("Sora 2 · Veo 3.1 · Runway · Kling · Pika", "video generation"),
                ("ElevenLabs · Cartesia · Hume · Sesame", "voice / TTS"),
                ("Vapi · Retell · Bland · LiveKit Agents", "voice agent platforms"),
                ("Suno · Udio · Stable Audio", "music gen · WMG settled $500M"),
            ],
        },
        {
            "num": "XII",
            "name": "ORCHESTRATION",
            "scale": "stratum decimum secundum · middleware",
            "tagline": "FRAMEWORK · GATEWAY · EVAL · GUARDRAIL",
            "subhead": "FRAMEWORKS · GATEWAYS · MCP · EVALS · GUARDRAILS",
            "h": 0.85, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("LangChain · LangGraph · LangSmith", "incumbent · Insights Agent"),
                ("LlamaIndex", "RAG · ingestion · query engines"),
                ("DSPy · Stanford · MIPROv2", "declarative · prompt optim."),
                ("TextGrad", "differentiable prompts"),
                ("Haystack · deepset", "European RAG"),
                ("Semantic Kernel + AutoGen", "MS Agent Framework"),
                ("Vercel AI SDK · streamText", "TS-first · agents · MCP"),
                ("Pydantic AI · typed agents", "validation backbone"),
                ("CrewAI · AG2 · Smolagents", "multi-agent + code-exec"),
                ("OpenAI Agents SDK", "handoffs · voice"),
                ("Claude Agent SDK", "MCP-deep · computer use"),
                ("Google ADK", "hierarchical · multi-language"),
                ("Mastra · TS · YC W25", "atop AI SDK · memory · evals"),
                ("MCP · Model Context Protocol", "10k+ servers · AAIF · LF"),
                ("Vercel · Cloudflare · Portkey", "AI gateways"),
                ("Helicone · LiteLLM · Kong AI", "OSS / self-host gateways"),
                ("LangSmith · Langfuse · Arize Phoenix", "tracing / observability"),
                ("Promptfoo (OpenAI) · Braintrust", "evals · regression-block"),
                ("DeepEval · HumanLoop · Galileo", "GenAI evaluation"),
                ("NeMo Guardrails · Guardrails AI", "policy / colang"),
                ("Lakera · Protect AI · Robust I.", "input/output filters"),
                ("Bedrock Guardrails · Azure CS", "hyperscaler-native"),
                ("Outlines · Instructor · XGrammar", "structured generation"),
                ("llguidance · OpenAI SO", "schema-conforming"),
            ],
        },
        {
            "num": "XI",
            "name": "RETRIEVAL · MEMORY",
            "scale": "stratum decimum primum · index",
            "tagline": "DENSE · SPARSE · GRAPH · LONG-TERM",
            "subhead": "VECTORS · GRAPHS · EMBEDDINGS · MEMORY",
            "h": 0.7, "cols": 4, "row_h": 2.5, "accent": VERDIGRIS,
            "items": [
                ("Pinecone · Qdrant · Weaviate", "leading vector DBs"),
                ("Chroma · Milvus · LanceDB", "OSS / scale-out"),
                ("pgvector · Atlas Vector", "DB-integrated"),
                ("Turbopuffer · object-backed", "cheap multi-tenant"),
                ("Voyage 3 · Cohere v4 · OAI v3", "embedding leaders"),
                ("BGE-M3 · Nomic v2 · Jina v5", "OSS embeddings"),
                ("Matryoshka embeddings", "truncatable dimensions"),
                ("Cohere Rerank 4 · Voyage Rerank 2.5", "cross-encoder rerank"),
                ("ColBERT v2 · SPLADE", "late interaction · learned sparse"),
                ("BM25 + dense + RRF", "hybrid retrieval"),
                ("Neo4j · Memgraph · Falkor", "graph DBs"),
                ("Microsoft GraphRAG", "Leiden · community summaries"),
                ("HippoRAG · PathRAG · OG-RAG", "neuro / multi-hop"),
                ("Mem0 · Letta · Zep · Cognee", "long-term memory"),
                ("Knowledge graphs from text", "entity extraction"),
                ("CXL memory pool · KV spill", "100 TiB pools 2025"),
            ],
        },
        {
            "num": "X",
            "name": "INFERENCE",
            "scale": "stratum decimum · serving",
            "tagline": "VLLM · SGLANG · TRT-LLM · DYNAMO",
            "subhead": "RUNTIMES · KV CACHE · QUANT · SPECULATIVE",
            "h": 0.75, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("vLLM · PagedAttention", "PyTorch Foundation · default"),
                ("SGLang · RadixAttention", "85–95% prefix hit · 6× JSON"),
                ("TensorRT-LLM · NIM", "NVIDIA first-party"),
                ("NVIDIA Dynamo · disagg P/D", "fleet OS for inference"),
                ("llama.cpp · GGUF", "consumer / local default"),
                ("MLC-LLM · TVM-based", "Vulkan / Metal / WebGPU"),
                ("PyTorch ExecuTorch 1.0", "50 KB · 12+ backends"),
                ("Apple MLX · MLX-LM", "M5 unified memory · 4× TTFT"),
                ("Ollama · LM Studio · Jan", "consumer wrappers"),
                ("Speculative · EAGLE-3", "3–6× over autoregressive"),
                ("Medusa · Lookahead", "draft-token approaches"),
                ("Quant · FP8 · NVFP4 · MXFP4", "Blackwell production default"),
                ("AWQ · GPTQ · SmoothQuant · GGUF IQ", "weight-only / W8A8"),
                ("Prompt caching · 90% read discount", "Anthropic 5min/1hr"),
                ("Batch APIs · 50% off · 24h", "all major providers"),
                ("KV-cache offload (HBM→DRAM→SSD)", "Dynamo · long-ctx"),
            ],
        },
        {
            "num": "IX",
            "name": "MODEL · PROVIDER",
            "scale": "stratum nonum · the API",
            "tagline": "FRONTIER · OPEN · INFERENCE-AS-A-SERVICE",
            "subhead": "FIRST-PARTY · AGGREGATOR · CUSTOM-SILICON CLOUD",
            "h": 0.65, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Anthropic · Opus 4.6 · Sonnet 4.6", "$5/$25 · $3/$15 · Haiku 4.5"),
                ("OpenAI · GPT-5 · o-series", "router-unified · auto cache"),
                ("Google · Gemini 2.5 Pro · Flash · Deep Think", "Vertex enterprise"),
                ("xAI · Grok 4", "real-time X · Colossus"),
                ("Meta · Llama 4 (open)", "Scout · Maverick · Behemoth"),
                ("DeepSeek V3 · R1 · V4-Pro", "MIT · 1.6T/49B"),
                ("Mistral Large 3 · Codestral · Pixtral", "Apache 2.0"),
                ("Qwen 3.5 · Cohere · GLM · Yi · Reka", "open-weight tier"),
                ("AWS Bedrock · Azure OpenAI · Vertex", "enterprise gateways"),
                ("OpenRouter · Vercel AI Gateway", "aggregator/router"),
                ("Fireworks · Together · Replicate", "inference clouds"),
                ("Modal · Baseten · Lepton · Anyscale", "serverless GPU"),
                ("Cerebras Cloud · 3,000 tok/s", "wafer-scale inference"),
                ("Groq Cloud · 750 tok/s · LPU", "ultra-low latency"),
                ("SambaNova · 580 tok/s 70B · 405B WR", "RDU SN40L"),
                ("DeepInfra · RunPod · Octo", "GPU rental & serverless"),
            ],
            "metrics": [
                ("ANTHROPIC ARR · APR 2026", "$30 B"),
                ("OPENAI ARR · 2026", "$24 B"),
                ("MCP SERVERS LIVE", "10,000+"),
            ],
        },
    ]
    build_strata_page(
        pdf, "V", "PLATE V OF VI",
        "Inference · Application · User",
        "From token to product to person — the path on which the substrate finally surfaces.",
        "Stratum IX–XIV — inferentia · applicatio · agentum · superficies hominis",
        layers,
    )


# ============================================================
# PAGE 6 — Meta layers (Plate VI)
# ============================================================

def page_meta(pdf):
    layers = [
        {
            "num": "M-D",
            "name": "GEOPOLITICS",
            "scale": "meta-stratum · sovereign compute",
            "tagline": "EXPORT · SOVEREIGN AI · TAIWAN",
            "subhead": "EXPORT CONTROLS · SOVEREIGN BUILD · TALENT",
            "h": 0.75, "cols": 4, "row_h": 2.55, "accent": VERDIGRIS,
            "items": [
                ("US export controls · 10²⁵ / 10²⁶ FLOPs", "model registration thresholds"),
                ("H20 saga · halt 4/2025 · revert 7/2025", "≈1M H20 to China 2024"),
                ("Huawei Ascend 910C · 920", "≈60% H100 inference"),
                ("BIS warning · Ascend supply-chain risk", "May 2025"),
                ("TSMC · 90%+ leading-edge logic", "concentration risk"),
                ("TSMC Arizona · $165B US", "AZ + advanced packaging"),
                ("Intel 18A · DoD · MSFT", "domestic foundry comeback"),
                ("ASML High-NA EUV · EXE:5200B", "Intel first commercial"),
                ("Stargate UAE · 1 GW · G42", "OpenAI · Oracle · NVIDIA · SoftBank · Cisco"),
                ("Humain · KSA · 18,000 GB300 / yr", "$10B AMD commit · PIF"),
                ("Mistral · French sovereign tilt", "EU frontier player"),
                ("Falcon · K2 · BharatGPT · Krutrim", "regional sovereign models"),
                ("CHIPS Act · $52B + ITC", "TSMC AZ · Intel · Samsung · Micron"),
                ("Compute as foreign policy", "the new oil-and-steel"),
            ],
        },
        {
            "num": "M-C",
            "name": "ECONOMICS",
            "scale": "meta-stratum · capital flow",
            "tagline": "CAPEX · ARR · DEPRECIATION",
            "subhead": "HYPERSCALER CAPEX · MODEL ARR · SUPPLY CHAIN",
            "h": 0.75, "cols": 4, "row_h": 2.55, "accent": VERMILION,
            "items": [
                ("Hyperscaler capex 2026", "$660–770 B aggregate"),
                ("Amazon · 2026", "≈$200 B"),
                ("Alphabet · 2026", "$175–185 B"),
                ("Meta · 2026", "$115–135 B"),
                ("Microsoft · 2026", "$110–120 B"),
                ("Oracle · 2026", "≈$50 B"),
                ("Stargate · OpenAI · Oracle · SoftBank · MGX", "$500 B / 4 yr / ≈10 GW"),
                ("Amazon FCF · MS proj 2026", "−$17 B (negative)"),
                ("Alphabet FCF · 2026 proj", "↓≈90% to ≈$8 B"),
                ("OpenAI funding round", "≈$40 B at ≈$300 B+"),
                ("Anthropic capital · 2025", ">$13 B raised"),
                ("OpenAI ARR · Apr 2026", "≈$24 B"),
                ("Anthropic ARR · Apr 2026", "$30 B (disputed)"),
                ("CoreWeave backlog", "$66.8 B · Meta 40%"),
                ("GPU depreciation · 2–6 yr range", "Burry: ≈$176 B understated"),
                ("Per-token frontier price · vs 2024", "−4× to −10×"),
                ("Reasoning compute · per query", "100–10,000× simple"),
                ("HBM market · 2026", "≈$58 B · SK 62% · Micron 21%"),
                ("CoWoS-L capacity", "tight through 2027"),
                ("Talent comp · senior frontier", "$1–10 M+ cash + equity"),
            ],
        },
        {
            "num": "M-B",
            "name": "REGULATION",
            "scale": "meta-stratum · governance",
            "tagline": "EU AI ACT · CA SB 53 · COPYRIGHT",
            "subhead": "JURISDICTIONS · COMPLIANCE · LIABILITY",
            "h": 0.75, "cols": 4, "row_h": 2.55, "accent": VERDIGRIS,
            "items": [
                ("EU AI Act · GPAI obligations", "Aug 2, 2025 in force"),
                ("EU · transparency / labeling", "Aug 2, 2026 milestone"),
                ("EU · pre-existing GPAI compliance", "Aug 2, 2027"),
                ("EU · GPAI Code of Practice", "training-summary template"),
                ("US · Biden EO 14110 · rescinded", "Jan 20, 2025"),
                ("US · Trump EO 14179 · Action Plan", "AI Action Plan · July 2025"),
                ("US · NIST AI RMF · ISO 42001", "de facto compliance refs"),
                ("AISI → AI Standards & Innovation", "rebrand under Trump"),
                ("CA SB 53 · Transparency Act", "Jan 1, 2026 effective"),
                ("CA · 10²⁶ FLOPs frontier threshold", "Cal OES incident reporting"),
                ("Texas · Colorado · state laws", "preemption fight"),
                ("UK AI Security Institute", "renamed Feb 14, 2025"),
                ("China · GenAI Service Reg + filing", "CAC algorithm registration"),
                ("Bartz v. Anthropic · $1.5B settlement", "lawful=fair / pirated≠fair"),
                ("NYT v. OpenAI · pretrial", "consolidated SDNY"),
                ("Andersen v. Stability · ongoing", "image-gen lineage"),
                ("TAKE IT DOWN Act · May 19, 2025", "deepfake / NCII federal"),
                ("C2PA · SynthID · watermark mandate", "EU 2026 baseline"),
            ],
        },
        {
            "num": "M-A",
            "name": "SAFETY · ALIGNMENT",
            "scale": "meta-stratum · the conscience",
            "tagline": "RSP · INTERPRETABILITY · MODEL WELFARE",
            "subhead": "POLICY · INTERPRETABILITY · EVAL · WELFARE",
            "h": 0.75, "cols": 4, "row_h": 2.55, "accent": VERMILION,
            "items": [
                ("Anthropic RSP v3.0 · v3.1", "ASL-3 deployed · ASL-4 partial"),
                ("OpenAI Preparedness Framework v2", "High / Critical thresholds"),
                ("DeepMind Frontier Safety Framework", "CCLs · pragmatic interpret."),
                ("Frontier Model Forum · FMF", "Anthropic · GDM · MS · OpenAI"),
                ("Mech interp · circuit tracing · CLT", "Biology of an LLM · 2025"),
                ("SAEs · Anthropic / DeepMind / Apollo", "feature decomposition"),
                ("Constitutional AI · RLAIF · CoT monitor", "Anthropic lineage"),
                ("Scalable oversight · debate · w2s", "research agenda"),
                ("METR · autonomy & RE-Bench", "third-party eval"),
                ("Apollo Research · scheming detect", "o1-preview behaviors"),
                ("Pattern Labs · cyber/CBRN red team", "pre-deployment"),
                ("WMDP · Cybench · persuasion · agentic", "dangerous-cap evals"),
                ("Model welfare · Kyle Fish · Eleos", "Claude consciousness 15–20%"),
                ("Concept injection · introspection", "Lindsey · model psychiatry"),
                ("Adversarial distillation · FMF intel", "April 2026 sharing"),
                ("AAIF · MCP donation · LF directed", "Dec 2025 · governance"),
            ],
        },
    ]
    build_strata_page(
        pdf, "VI", "PLATE VI OF VI",
        "The Field Around the Stack",
        "What governs, finances, regulates, and questions the column above.",
        "Meta-strata A · B · C · D — mores · leges · pecunia · res publica AI",
        layers,
    )


# ============================================================
# Run
# ============================================================

def main():
    with PdfPages(OUT_PATH) as pdf:
        page_index(pdf)
        page_power_facility(pdf)
        page_compute_fabric(pdf)
        page_data_models(pdf)
        page_inference_apps(pdf)
        page_meta(pdf)

        d = pdf.infodict()
        d["Title"] = "SUBSTRATE — An Atlas of the Intelligence Strata"
        d["Author"] = "Compiled for A. Yedi"
        d["Subject"] = "The full AI stack from power grid to end user"
        d["Keywords"] = "AI stack, infographic, atlas, stratigraphy"

    print("Wrote", OUT_PATH)


if __name__ == "__main__":
    main()
