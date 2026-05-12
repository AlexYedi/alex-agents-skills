"""
SUBSTRATE · Volume III — A stratigraphic atlas of the AGENT LAYER.
Six plates: index, 4 sub-stratum pages, 1 meta-stratum page.
Mirrors the aesthetic of Volume I (ink-on-cream, hairline rules,
vermilion / verdigris / ochre accents, condensed display caps,
monospace marginalia, depth-scale ticks).
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
if os.path.isdir(FONT_DIR):
    for fp in os.listdir(FONT_DIR):
        if fp.endswith((".ttf", ".otf")):
            fm.fontManager.addfont(os.path.join(FONT_DIR, fp))

def fam(filename):
    path = os.path.join(FONT_DIR, filename)
    if os.path.isfile(path):
        return fm.FontProperties(fname=path).get_name()
    return "DejaVu Sans"  # fallback

F_DISPLAY = fam("BigShoulders-Bold.ttf")
F_DISPLAY_REG = fam("BigShoulders-Regular.ttf")
F_NARROW = fam("Boldonse-Regular.ttf")
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
    if n <= 0:
        return text
    sep = " " * n
    out = []
    for ch in text:
        if out:
            out.append(sep)
        out.append(ch)
    return "".join(out)


# ---------- Palette (Substrate v1) ----------
PAPER = "#F1E9D6"
INK = "#171210"
INK_SOFT = "#3A2F26"
GRAY = "#7A6E60"
GRAY_LIGHT = "#C9BFA9"
RULE = "#2A211B"
VERMILION = "#A6371F"
VERDIGRIS = "#456C5C"
OCHRE = "#A37425"

# ---------- Geometry (tabloid portrait) ----------
PAGE_W = 11.0
PAGE_H = 17.0
DPI = 300
OUT_PATH = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents/AI_AGENTS_SUBSTRATE.pdf"


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
    LEFT = 8.5
    RIGHT = 92.5
    TOP = 148.5
    BOTTOM = 9.5

    rect = mpatches.Rectangle((LEFT, BOTTOM), RIGHT - LEFT, TOP - BOTTOM,
                              fill=False, ec=RULE, lw=0.55)
    ax.add_patch(rect)
    ax.plot([LEFT, RIGHT], [TOP - 6.0, TOP - 6.0], color=RULE, lw=0.45)
    ax.plot([LEFT, RIGHT], [BOTTOM + 4.5, BOTTOM + 4.5], color=RULE, lw=0.45)

    # Left depth scale
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

    ax.text(LEFT, TOP - 1.0, sp("AN ATLAS OF THE AGENT STRATA", 4),
            ha="left", va="top", fontsize=6.0, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, TOP - 1.9, title_top.upper(),
            ha="left", va="top", fontsize=18, fontname=F_DISPLAY, color=INK)
    ax.text(RIGHT - 4.0, TOP - 2.0, sp(plate_label, 2),
            ha="right", va="top", fontsize=7.5, fontname=F_DISPLAY_REG, color=INK_SOFT)
    ax.text(LEFT, TOP - 4.5, subtitle_top,
            ha="left", va="top", fontsize=6.2, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
    ax.text(LEFT, TOP - 5.4, latin,
            ha="left", va="top", fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)

    ax.add_patch(mpatches.Circle((RIGHT - 1.4, TOP - 2.0), 1.05, fill=False,
                                 ec=VERMILION, lw=0.6))
    ax.text(RIGHT - 1.4, TOP - 2.0, plate_no, ha="center", va="center",
            fontsize=6.2, fontname=F_MONO_BOLD, color=VERMILION)

    ax.text(LEFT, BOTTOM + 3.0, sp("SUBSTRATE · VOL III · THE AGENT LAYER", 3),
            ha="left", va="top", fontsize=4.6, fontname=F_MONO, color=GRAY)
    ax.text(LEFT, BOTTOM + 1.4, sp("Compiled for A. Yedi · Cycle MMXXVI · Rev. I", 2),
            ha="left", va="top", fontsize=5.2, fontname=F_SERIF_DISP_IT, color=GRAY)
    ax.text(RIGHT, BOTTOM + 1.4, plate_label, ha="right", va="top",
            fontsize=5.4, fontname=F_DMMONO, color=GRAY)
    ax.text(50, BOTTOM + 1.4, "·   ·   ·   ·   ·", ha="center", va="top",
            fontsize=5, fontname=F_MONO, color=GRAY_LIGHT)

    return LEFT, RIGHT, TOP - 6.5, BOTTOM + 4.7


def stratum(ax, x0, x1, y_top, height, *, num, name, scale, accent=INK_SOFT, tagline=None):
    y_bot = y_top - height
    ax.plot([x0, x1], [y_top, y_top], color=RULE, lw=0.5)
    ax.plot([x0, x1], [y_bot, y_bot], color=RULE, lw=0.35)
    label_x_right = x0 + 16.5
    ax.text(x0 + 0.5, y_top - 1.8, num, ha="left", va="top",
            fontsize=8.5, fontname=F_DMMONO, color=accent)
    for i, line in enumerate(name.split("\n")):
        ax.text(x0 + 0.5, y_top - 4.0 - i*2.6, line, ha="left", va="top",
                fontsize=10.0, fontname=F_DISPLAY, color=INK)
    ax.text(x0 + 0.5, y_bot + 1.2, scale, ha="left", va="bottom",
            fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)
    if tagline:
        ax.text(x0 + 0.5, y_bot + 0.0, sp(tagline, 2), ha="left", va="bottom",
                fontsize=4.4, fontname=F_MONO, color=GRAY)
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


def metric_bar(ax, x, y, width, label, value, *, accent=VERMILION):
    ax.plot([x, x + width], [y, y], color=accent, lw=0.7)
    ax.text(x, y + 0.4, sp(label, 2), ha="left", va="bottom",
            fontsize=4.0, fontname=F_MONO, color=GRAY)
    ax.text(x + width, y - 0.2, value, ha="right", va="top",
            fontsize=8.5, fontname=F_DISPLAY, color=INK)


def build_strata_page(pdf, plate_no, plate_label, title, subtitle, latin, layers):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(ax, plate_no, title, subtitle, latin, plate_label)
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0
    ax.plot([inner_x0, inner_x1], [TOP - 0.4, TOP - 0.4], color=RULE, lw=0.5)

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
        metric_zone = 4.5 if layer.get("metrics") else 0.8
        items = layer.get("items", [])
        if items:
            grid_nodes(ax, items, x0=x_content_left, x1=x_content_right,
                       y_top=content_top, y_bot=y_bot + metric_zone,
                       cols=layer.get("cols", 4),
                       row_h=layer.get("row_h", 2.6),
                       color=layer.get("dot_color", INK_SOFT),
                       top_pad=0.0)
        for j, m in enumerate(layer.get("metrics", [])):
            mx = x_content_left + j * 22
            metric_bar(ax, mx, y_bot + 2.0, 18, m[0], m[1],
                       accent=m[2] if len(m) > 2 else VERMILION)
        y_cursor = y_bot

    ax.plot([inner_x0, inner_x1], [BOT + 0.5, BOT + 0.5], color=RULE, lw=0.5)
    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PAGE 1 — INDEX PLATE (the agent column)
# ============================================================

def page_index(pdf):
    fig, ax = new_page()
    L, R, TOP, BOT = page_frame(
        ax, "I",
        "The Agent Column",
        "A higher-resolution zoom into Stratum XIII of the parent atlas — the agent layer unfolded as ten sub-strata plus four wrapping meta-strata.",
        "Stratum agenticum — denso compositum, ordo descendens, gradibus decem cum quattuor strata circumdantia",
        "PLATE I OF VI",
    )
    inner_x0 = L + 1.0
    inner_x1 = R - 1.0

    ax.text(inner_x0, TOP - 0.5,
            sp("X SUB-STRATA · IV META · DESCENDING", 3),
            ha="left", va="top", fontsize=8.2, fontname=F_DISPLAY, color=VERMILION)
    ax.plot([inner_x0, inner_x1], [TOP - 2.2, TOP - 2.2], color=RULE, lw=0.4)

    strata = [
        ("X", "END-USER · SURFACE", "form factors", "chat · cli · ide · trigger · slack · whatsapp · voice · ar"),
        ("IX", "VERTICAL · PRODUCTS", "productized agents", "sierra · decagon · glean · harvey · hippocratic · clay · rogo"),
        ("VIII", "RUNTIME · SAFETY", "tool-boundary defense", "lakera · nemo · llama-guard · bedrock · purview"),
        ("VII", "EVAL · OBSERVABILITY", "trajectory analytics", "braintrust · langsmith · langfuse · arize · galileo · inspect"),
        ("VI", "ACTION · SURFACES", "agent reaches into world", "e2b · modal · browserbase · computer-use · vapi"),
        ("V", "PLANNING · REASONING", "cognition loop", "react · planner-executor · o-series · extended-thinking"),
        ("IV", "MEMORY · STATE", "persistence", "mem0 · letta · zep · graphrag · lab-native"),
        ("III", "TOOL · PROTOCOL", "interface to world", "mcp · function calling · gateways · a2a"),
        ("II", "AGENT · RUNTIMES", "harness", "claude agent sdk · openai agents · adk · langgraph · mastra"),
        ("I", "FOUNDATION · CAPABILITY", "the agentic delta", "claude · gpt-5 · gemini · deepseek · tau · swe · osworld"),
    ]

    meta = [
        ("A", "CAPABILITY · SAFETY", "asl · preparedness · frontier · aisi · metr"),
        ("B", "REGULATION", "eu ai act · ca sb 53 · sectoral · bartz · nyt"),
        ("C", "ECONOMICS", "per-task · outcome pricing · finops"),
        ("D", "GEOPOLITICS", "sovereign agents · export controls · jurisdiction"),
    ]

    # Sub-strata column
    avail_top = TOP - 3.2
    avail_bot = BOT + 22.0
    avail_h = avail_top - avail_bot
    h = avail_h / len(strata)

    label_w = 16.0
    band_x0 = inner_x0
    band_x1 = inner_x1

    for i, (num, name, scale, desc) in enumerate(strata):
        y_top = avail_top - i * h
        y_bot = y_top - h
        ax.plot([band_x0, band_x1], [y_top, y_top], color=RULE, lw=0.35)
        ax.text(band_x0 + 0.5, (y_top + y_bot)/2 + 0.2, sp(num, 1), ha="left", va="center",
                fontsize=8.0, fontname=F_DMMONO, color=VERMILION)
        ax.text(band_x0 + 9.5, (y_top + y_bot)/2 + 0.6, name, ha="left", va="center",
                fontsize=12.5, fontname=F_DISPLAY, color=INK)
        ax.text(band_x0 + 9.5, (y_top + y_bot)/2 - 1.4, scale, ha="left", va="center",
                fontsize=5.0, fontname=F_SERIF_IT, color=GRAY)
        ax.plot([band_x0 + label_w + 17.5, band_x0 + label_w + 17.5],
                [y_top - 0.4, y_bot + 0.4], color=RULE, lw=0.25, ls=(0, (0.6, 0.9)))
        ax.text(band_x0 + label_w + 19.0, (y_top + y_bot)/2 + 0.2, desc,
                ha="left", va="center", fontsize=6.4, fontname=F_SERIF, color=INK)
        ax.add_patch(mpatches.Circle((band_x1 - 1.2, (y_top+y_bot)/2 + 0.2),
                                     0.42, fill=False, ec=INK_SOFT, lw=0.4))
        ax.text(band_x1 - 1.2, (y_top + y_bot)/2 + 0.2, str(10 - i),
                ha="center", va="center",
                fontsize=4.6, fontname=F_DMMONO, color=INK_SOFT)

    ax.plot([band_x0, band_x1], [avail_bot, avail_bot], color=RULE, lw=0.5)

    # Meta strata strip (4 horizontal bands below)
    meta_top = avail_bot - 1.0
    meta_bot = BOT + 8.0
    meta_h = (meta_top - meta_bot) / 4
    ax.text(band_x0, meta_top + 0.4, sp("META · WRAPPING FORCES", 3),
            ha="left", va="bottom",
            fontsize=5.4, fontname=F_MONO, color=VERDIGRIS)
    for i, (let, name, desc) in enumerate(meta):
        y_top = meta_top - i * meta_h
        y_bot = y_top - meta_h
        ax.plot([band_x0, band_x1], [y_top, y_top], color=RULE, lw=0.3)
        ax.text(band_x0 + 0.5, (y_top + y_bot)/2 + 0.2, let, ha="left", va="center",
                fontsize=7.5, fontname=F_DMMONO, color=VERDIGRIS)
        ax.text(band_x0 + 4.5, (y_top + y_bot)/2 + 0.2, name, ha="left", va="center",
                fontsize=8.5, fontname=F_DISPLAY, color=INK_SOFT)
        ax.text(band_x0 + label_w + 19.0, (y_top + y_bot)/2 + 0.2, desc,
                ha="left", va="center", fontsize=5.8, fontname=F_SERIF_IT, color=GRAY)
    ax.plot([band_x0, band_x1], [meta_bot, meta_bot], color=RULE, lw=0.4)

    # Footer key
    ax.text(inner_x0, BOT + 6.5, sp("KEY", 3),
            fontsize=5.2, fontname=F_MONO, color=VERMILION)
    ax.plot([inner_x0, inner_x1], [BOT + 6.0, BOT + 6.0], color=RULE, lw=0.3)
    keys = [
        ("○", "sub-stratum"),
        ("•", "component"),
        ("¶", "meta-stratum"),
        ("—", "dependency"),
    ]
    for i, (sym, txt) in enumerate(keys):
        x = inner_x0 + i * 21
        ax.text(x, BOT + 5.0, sym, fontsize=8, fontname=F_SERIF_DISP, color=VERMILION)
        ax.text(x + 1.8, BOT + 5.0, txt, fontsize=5.2, fontname=F_SERIF_IT,
                color=INK_SOFT, va="center")

    pdf.savefig(fig, dpi=DPI, facecolor=PAPER)
    plt.close(fig)


# ============================================================
# PAGE 2 — Strata I–III · The Capability Substrate
# ============================================================

def page_capability_substrate(pdf):
    layers = [
        {
            "num": "III",
            "name": "TOOL · PROTOCOL",
            "scale": "stratum tertium · the joint to the world",
            "tagline": "MCP · JSON-RPC · GATEWAYS",
            "subhead": "MODEL CONTEXT PROTOCOL · ADOPTION · FORK VECTORS",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("MCP — Anthropic Nov '24", "JSON-RPC; Py + TS SDKs"),
                ("OpenAI adoption — Mar '25", "Agents SDK · Responses API"),
                ("Google adoption — Apr '25", "Gemini · Vertex AI · A2A"),
                ("Microsoft adoption — May '25", "Copilot Studio · SK"),
                ("Hugging Face — Jun '25", "MCP-compatible Spaces"),
                ("Linux Foundation — Dec '25", "Agentic AI Foundation"),
                ("Registry · ~11.4K servers", "Apr '26 LF stats"),
                ("Cloudflare Workers AI MCP", "Dec '24 · gateway"),
                ("Kong MCP Gateway", "GA Jul '25 · F500 logos"),
                ("Pomerium identity proxy", "May '25"),
                ("Function calling (legacy)", "OpenAI Jun '23"),
                ("Structured outputs", "OpenAI Aug '24"),
                ("Stripe MCP", "first-party · canonical"),
                ("Linear · Cloudflare MCP", "first-party tier"),
                ("GitHub MCP", "MSFT canonical"),
                ("A2A protocol — Apr '25", "agent-to-agent (Google)"),
                ("Fork vector — proprietary tool calls", "OAI latency wins"),
                ("Fork vector — quality split", "long tail abandonware"),
            ],
            "metrics": [
                ("REGISTRY · MAY '26", "~11.4K"),
                ("HYPERSCALERS COMMITTED", "4 / 4"),
                ("GATEWAY CATEGORY", "GA"),
            ],
        },
        {
            "num": "II",
            "name": "RUNTIMES",
            "scale": "stratum secundum · the harness",
            "tagline": "SDK · LOOP · SUB-AGENTS",
            "subhead": "AGENT RUNTIMES · HARNESSES · ORCHESTRATORS",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Claude Agent SDK", "Sep '25 · sub-agents · skills"),
                ("OpenAI Agents SDK", "Mar '25 · handoffs"),
                ("Google ADK", "Apr '25 · Vertex Agent Engine"),
                ("LangGraph 1.0", "GA Oct '25 · production"),
                ("LangSmith", "obs layer · margin lives here"),
                ("Mastra", "TypeScript · YC W24 · Vercel"),
                ("Pydantic AI", "typed validation · Logfire"),
                ("CrewAI", "multi-agent · $18M Oct '24"),
                ("Smolagents (HF)", "minimalist · Dec '24"),
                ("AutoGen / AG2", "MSR + community fork"),
                ("DSPy · BAML", "compile-time / IR layer"),
                ("Inspect AI (UK AISI)", "eval framework · OSS"),
                ("Mistral Agents API", "May '25 · EU"),
                ("Manus AI (CN)", "Butterfly Effect · viral '25"),
                ("Sarvam AI (IN)", "Q1 '26"),
                ("Aleph Alpha", "compliance-first · DE"),
            ],
            "metrics": [
                ("SHIPPED · LAST 14 MO", "4 SDKs"),
                ("LANGGRAPH ARR", "$40–60M (inf)"),
                ("RUNTIME GROSS MARGIN", "THINNEST"),
            ],
        },
        {
            "num": "I",
            "name": "FOUNDATION · CAPABILITY",
            "scale": "stratum primum · the agentic delta",
            "tagline": "TAU · SWE · OSWORLD · BROWSECOMP",
            "subhead": "AGENTIC CAPABILITY DELTAS · NOT PROVIDER ECONOMICS",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Claude Opus 4.5", "Nov '25 · 82.8% SWE-V"),
                ("Claude Sonnet 4.5", "interactive executor"),
                ("GPT-5 / 5.1 thinking", "~80% SWE-V w/ tools"),
                ("ChatGPT Agent", "Operator+DR · OSWorld claim"),
                ("Gemini 2.5 Pro Deep Think", "GAIA ~70 · BrowseComp ~50"),
                ("Project Mariner", "GA Apr '26 · OSWorld ~38%"),
                ("DeepSeek R1 / R2", "open weights · mid-50s SWE"),
                ("Qwen QwQ / Qwen3", "RLVR · open · CN"),
                ("Kimi K1.5 / K2", "long-context CN · Moonshot"),
                ("Meta Llama 4", "Apr '25 · –10–15 pts vs frontier"),
                ("Anthropic sub-agents", "fresh-ctx children · 6mo lead"),
                ("Reasoning regression", "context degr. past 32K tokens"),
                ("Error compounding ceiling", "0.95^20 ≈ 36%"),
                ("Computer-use ceiling", "OSWorld ~50% vs human 72%"),
                ("Extended thinking 64K", "interactive vs back-office split"),
                ("Tool use in thinking", "Claude 4.5 · GPT-5 · Deep Think"),
            ],
            "metrics": [
                ("SWE-BENCH VERIFIED", "82.8%"),
                ("OSWORLD (MAY '26)", "~50%"),
                ("REASONING-MODEL TIERS", "9"),
            ],
        },
    ]
    build_strata_page(
        pdf, "II", "PLATE II OF VI",
        "Capability · Substrate",
        "Strata I–III · the model, the runtime, the protocol — the geological basement on which every agent runs.",
        "Stratum primum, secundum, tertium · capacitas, harnesia, protocollum tooluse",
        layers,
    )


# ============================================================
# PAGE 3 — Strata IV–V · The Loops of Cognition
# ============================================================

def page_cognition_loops(pdf):
    layers = [
        {
            "num": "V",
            "name": "PLANNING · REASONING",
            "scale": "stratum quintum · the inner loop",
            "tagline": "REACT · PLANNER-EXECUTOR · TTC",
            "subhead": "WHAT SURVIVED · TEST-TIME COMPUTE · ECONOMICS",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("ReAct (Yao Oct '22)", "still dominant 2026 loop"),
                ("Plan-and-Solve (May '23)", "prompting · alive"),
                ("Tree-of-Thoughts (May '23)", "lab curiosity · rare prod"),
                ("Reflexion (Mar '23)", "verifier sub-agent · alive"),
                ("AutoGPT / BabyAGI", "dead in prod · idea survived"),
                ("Planner-executor split", "durable architectural idea"),
                ("Meta-planning / hierarchical", "emerging 2025–26"),
                ("o1 / o3 (Sep–Dec '24)", "reasoning model tier opens"),
                ("Claude extended thinking", "Feb '25 · 64K budgets"),
                ("Gemini Deep Think (May '25)", "super-linear on hard"),
                ("DeepSeek R1 / R1-Zero", "Jan '25 · pure RLVR"),
                ("Qwen QwQ-32B · Kimi K1.5", "open reasoning"),
                ("Tool use IN thinking", "outer ReAct collapses"),
                ("`reasoning_effort` knob", "OpenAI · buyer-controlled"),
                ("PRM (Lightman May '23)", "in-model · not exposed"),
                ("GRPO at trajectory", "DeepSeek · default RL"),
            ],
            "metrics": [
                ("CX TRAJECTORY · TOKENS", "4–25K"),
                ("CODE AGENT · TOKENS", "30–250K"),
                ("DEEP RESEARCH · TOKENS", "0.5–5M"),
            ],
        },
        {
            "num": "IV",
            "name": "MEMORY · STATE",
            "scale": "stratum quartum · persistence",
            "tagline": "EPISODIC · SEMANTIC · PROCEDURAL",
            "subhead": "STANDALONE OR ABSORBED · COMPLIANCE WEDGE",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Mem0 (YC W24)", "$24M A Dec '25 · 40K stars"),
                ("Letta (MemGPT)", "$10M seed · A rumored '26"),
                ("Zep — Graphiti", "$15M A Feb '25 · HIPAA"),
                ("Cognee", "OSS pipeline · seed Dec '24"),
                ("Microsoft GraphRAG", "Apr '24 paper · Jul '24 OSS"),
                ("LightRAG (HKU)", "Oct '24 · cheaper graph"),
                ("HippoRAG · PathRAG · OG-RAG", "research-only"),
                ("MemoryOS (Tsinghua)", "Sep '25 paper · CN"),
                ("ChatGPT memory", "Apr '24 paid · Sep '24 free"),
                ("Claude Projects memory", "GA Apr '26"),
                ("Gemini personalization", "GA Mar '26"),
                ("Working memory (LangGraph)", "engineering not category"),
                ("Procurement — Article 17", "Mem0 forget API Feb '26"),
                ("HIPAA story (Zep)", "Athelas · F500 health"),
                ("Contextual integrity", "Nissenbaum · no vendor"),
                ("Falsifiability test", "70% pitches = RAG + writes"),
            ],
            "metrics": [
                ("STANDALONE CEILING (INF)", "$200–400M"),
                ("LAB MEMORY MAU", "~800M"),
                ("CRUX #5 (INHERITED)", "OPEN"),
            ],
        },
    ]
    build_strata_page(
        pdf, "III", "PLATE III OF VI",
        "Cognition · Loops",
        "Strata IV–V · the inner cognition of the working agent — what it remembers and how it plans the next step.",
        "Stratum quartum et quintum · memoria et ratiocinatio · circuitus interni",
        layers,
    )


# ============================================================
# PAGE 4 — Strata VI–VIII · Action and Defense
# ============================================================

def page_action_defense(pdf):
    layers = [
        {
            "num": "VIII",
            "name": "RUNTIME · SAFETY",
            "scale": "stratum octavum · the tool boundary",
            "tagline": "PI · ACTION GATES · SANDBOXING",
            "subhead": "GUARDRAILS · INJECTION DEFENSE · BUNDLING",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Lakera (Guard · Red)", "Series A '23 · B Q4 '25"),
                ("Protect AI · to Palo Alto", "~$700M Q3 '25 · the bell"),
                ("Robust Intelligence · to Cisco", "Aug '24 · AI Defense"),
                ("HiddenLayer", "$50M B Mar '24"),
                ("Apex Security", "Sequoia seed Mar '24"),
                ("CalypsoAI", "$23M B · federal angle"),
                ("Cranium", "KPMG spin · GRC-leaning"),
                ("AWS Bedrock Guardrails", "Apr '24 · Auto Reasoning"),
                ("Purview AI Hub · Defender", "MSFT Ignite Nov '24"),
                ("Vertex AI Model Armor", "Cloud Next '24"),
                ("NeMo Guardrails 1.0", "GA Apr '26 · OSS"),
                ("Llama Guard 3 · Prompt Guard 2", "Meta open weights"),
                ("Promptfoo (now OAI)", "red-team OSS · Sep '25"),
                ("Garak (NVIDIA OSS)", "vulnerability scanner"),
                ("EchoLeak CVE class", "Mar '26 · indirect PI"),
                ("Constitutional classifiers", "Anthropic · baked in"),
            ],
            "metrics": [
                ("PURE-PLAYS ABSORBED", "18 MO"),
                ("INDIRECT PI", "UNSOLVED"),
                ("DEFENSE STACK · LAYERS", "5"),
            ],
        },
        {
            "num": "VII",
            "name": "EVAL · OBSERVABILITY",
            "scale": "stratum septimum · trajectory analytics",
            "tagline": "TRAJECTORY · REPLAY · ONLINE",
            "subhead": "AGENT EVAL · OBS · BENCHMARKS",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Braintrust", "$36M A · B rumored '26"),
                ("LangSmith / LangChain", "$25M C · LangGraph 1.0"),
                ("Langfuse", "OSS · YC W23 · EU choice"),
                ("Arize Phoenix / AX", "$70M C Dec '24"),
                ("Galileo", "$45M B · C reported Apr '26"),
                ("HumanLoop", "UK · FSI"),
                ("Patronus AI · Lynx · Glider", "$17M A · defensible judge"),
                ("Comet Opik · DeepEval", "OSS · pytest-style"),
                ("AgentOps", "CrewAI / AutoGen ecosystem"),
                ("Helicone · proxy", "losing as native matures"),
                ("Promptfoo (acq OAI)", "Sep '25 · neutrality gone"),
                ("Inspect AI (UK AISI)", "EU AI Act conformity"),
                ("METR · time-horizon", "Mar '25 · cite not procure"),
                ("TAU-bench / tau-2", "Sierra-co · CX proxy"),
                ("SWE-Bench Verified · Live", "code agency · ~75–80%"),
                ("OSWorld · WebArena · GAIA", "computer/web/research"),
            ],
            "metrics": [
                ("OTEL GENAI CONVENTIONS", "JAN '26 GA"),
                ("CONSOLIDATION (2027)", "PARTIAL"),
                ("PROCUREMENT GAP", "OPEN"),
            ],
        },
        {
            "num": "VI",
            "name": "ACTION · SURFACES",
            "scale": "stratum sextum · agent reaches into world",
            "tagline": "SANDBOX · BROWSER · COMPUTER · VOICE",
            "subhead": "SANDBOXED CODE · BROWSER · COMPUTER · VOICE OUTBOUND",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("E2B", "OSS-core · ~$15–25M ARR"),
                ("Modal", "agent-workload pivot · >$50M"),
                ("Daytona", "newer · price-aggressive"),
                ("Vercel Sandbox", "GA Jan '26 · Firecracker"),
                ("Replit Agent sandbox", "bundled · prosumer"),
                ("HF Spaces · Codespaces", "ad-hoc · weaker fit"),
                ("Browserbase + Stagehand", ">$50M ARR Q1 '26"),
                ("Browserless · Skyvern", "incumbent · OSS"),
                ("Playwright + AI", "the boring baseline"),
                ("Anchor · Hyperbrowser", "MCP-compat 2025"),
                ("Anthropic Computer Use", "Oct '24 · Claude for Chrome"),
                ("ChatGPT Agent", "Operator rebrand mid '25"),
                ("Google Project Mariner", "GA Apr '26 · Gemini Ent"),
                ("MSFT Copilot Vision", "Windows-native"),
                ("Vapi · Retell · Bland", "voice trio · $20M+ ARR ea"),
                ("LiveKit Agents", "WebRTC substrate"),
                ("ElevenLabs Conv. AI", "voice up-stack"),
                ("Cartesia Sonic-2", "~40ms first-byte"),
                ("Deepgram Nova-3", "ASR · accent"),
                ("Twilio · Telnyx · LiveKit Cloud", "telephony"),
            ],
            "metrics": [
                ("VOICE-TO-VOICE FLOOR", "500–800ms"),
                ("SANDBOX TIMELINE", "18–24 MO"),
                ("CU PRODUCTION", "NO"),
            ],
        },
    ]
    build_strata_page(
        pdf, "IV", "PLATE IV OF VI",
        "Action · Defense",
        "Strata VI–VIII · where the agent reaches into the world, how we observe that it did the right thing, and what defends when it does not.",
        "Stratum sextum, septimum, octavum · operatio, observatio, custodia",
        layers,
    )


# ============================================================
# PAGE 5 — Strata IX–X · The Productized Layer
# ============================================================

def page_productized(pdf):
    layers = [
        {
            "num": "X",
            "name": "END-USER · SURFACES",
            "scale": "stratum decimum · form factor",
            "tagline": "BUYER · THREAT · ADOPTION",
            "subhead": "TWELVE FORM FACTORS · THE BINDING CONSTRAINT",
            "h": 1.0, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Chat — web/desktop", "ChatGPT 800M WAU · plateau"),
                ("Chat — mobile/on-device", "Apple Intelligence slot"),
                ("CLI / terminal", "Claude Code ~$500M RR"),
                ("In-IDE inline", "Cursor · Copilot · Windsurf"),
                ("Agentic trigger", "n8n · Zapier · cron · Art. 14"),
                ("In-browser sidebar", "Claude for Chrome · Comet 5M"),
                ("Embedded in SaaS", "Copilot 365 ~30M seats"),
                ("Slack / Teams · headless", "Glean wedge"),
                ("WhatsApp · SMS · email", "Meta API Jan '26 · 2.9B"),
                ("Voice — inbound", "Advanced Voice · AirPods"),
                ("Wearable · AR · ambient", "Ray-Ban >2M · Plaud >1M"),
                ("Computer use (UX)", "watched only · no reg ent"),
                ("API · SDK · no-UI", "2/3 OAI rev · majority Anthropic"),
                ("WhatsApp Business API", "Jan '26 · GLOBAL MAJORITY"),
                ("Coze on Feishu · WeChat", "CN parallel-track"),
                ("Manus · Yellow.ai · Haptik", "non-US agent surfaces"),
                ("Pew chat-churn 41%", "Jan '26 · 'chat solved' = SF"),
                ("Anthropic mobile gap", "no AI slot · no voice"),
            ],
            "metrics": [
                ("MICROSOFT COPILOT ARR", "$5B+"),
                ("WHATSAPP MAU", "2.9B"),
                ("BINDING CONSTRAINT", "FORM"),
            ],
        },
        {
            "num": "IX",
            "name": "VERTICAL · PRODUCTS",
            "scale": "stratum nonum · productized agents",
            "tagline": "CX · CODE · LEGAL · HEALTH · FINANCE",
            "subhead": "ENTERPRISE REVENUE LAYER · BUYING MOTION BY DOMAIN",
            "h": 1.2, "cols": 4, "row_h": 2.5, "accent": VERMILION,
            "items": [
                ("Sierra — $175M+ ARR", "$10B (Mar '26) · NYC dual"),
                ("Decagon — $80M+", "$4.5B Sep '25 · NYC/SF"),
                ("Glean — $300M+", "$7.2B Sep '25 · NYC growing"),
                ("Harvey — $100M+", "$5B Feb '26 · NYC office"),
                ("Hippocratic — $50M+", "$2B Feb '26 · NYC HQ"),
                ("Augment Code — $40M", "$977M Nov '25 · enterprise"),
                ("Cursor — $500M RR", "$9.9B Jul '25 · IDE leader"),
                ("Cognition (Devin)", "$3B Codeium absorbed Mar '26"),
                ("Replit Agent — $150M", "$3B Sep '25 · prosumer"),
                ("Lovable — $80M Q1'26", "fastest EU SaaS · Stockholm"),
                ("Abridge — $120M+", "$2.75B Jun '25 · scribe"),
                ("Hebbia — $50M+", "NYC HQ · ex-2Sigma · raise"),
                ("Clay — $80M+", "NYC HQ · $1.5B Jan '26"),
                ("Rogo — $30M+", "NYC HQ · $400M Jan '26"),
                ("Ramp AI org", "$13B · NYC · $20B raise rumor"),
                ("Runway — $100M+", "NYC Chelsea · creative"),
                ("ElevenLabs — $200M+", "voice platform · $3.3B"),
                ("Cresta · Ada · Intercom Fin", "CX maturing/stalling"),
                ("Parloa · PolyAI · Regal", "EU/UK + NYC sales voice"),
                ("EvenUp · Eve · Spellbook", "legal long tail"),
                ("11x · Artisan · AiSDR", "synthetic SDR · 11x flat"),
                ("Mistral Le Chat Ent.", "€600M Mar '26 · EU sovereign"),
            ],
            "metrics": [
                ("WINNER-TAKE-MOST SEGMENTS", "3 / 9"),
                ("BET #2 NYC TARGETS", "10+"),
                ("OUTCOME PRICING (TAYLOR)", "CX ONLY"),
            ],
        },
    ]
    build_strata_page(
        pdf, "V", "PLATE V OF VI",
        "Productized · Layer",
        "Strata IX–X · where enterprise revenue lands and where the human meets the agent — the productized application and its surface.",
        "Stratum nonum et decimum · productum agenticum et facies hominis",
        layers,
    )


# ============================================================
# PAGE 6 — Meta-Strata · Wrapping Forces
# ============================================================

def page_meta(pdf):
    layers = [
        {
            "num": "D",
            "name": "GEOPOLITICS",
            "scale": "meta · sovereign agents",
            "tagline": "SOVEREIGN · EXPORT · JURISDICTION",
            "subhead": "WHERE AGENTS RUN · EXPORT CONTROLS · SIT-CONTROLS",
            "h": 1.0, "cols": 4, "row_h": 2.6, "accent": VERDIGRIS, "dot_color": VERDIGRIS,
            "items": [
                ("Mistral Le Chat Ent.", "€600M @ €11B Mar '26"),
                ("G42 · Falcon · UAE", "Humain ties · sovereign AI"),
                ("Humain (KSA)", "MI300/350 commits · $10B"),
                ("Sarvam AI (IN)", "$41M · Q1 '26 raise rumor"),
                ("Krutrim (Ola IN)", "$50M · political tailwind"),
                ("Manus (CN)", "Butterfly · $500M rumor"),
                ("Coze on Feishu", "ByteDance · parallel-track"),
                ("WeChat Mini-Programs", "agentic Q2 '26"),
                ("US Commerce auth — Nov '25", "G42 + Humain chips"),
                ("Agent-capability export rule", "2026–27 regulatory front"),
                ("EU residency lever", "AI Act + GDPR + Schrems II"),
                ("Trajectory siting", "where memory + actions reside"),
            ],
        },
        {
            "num": "C",
            "name": "ECONOMICS",
            "scale": "meta · the inversion",
            "tagline": "PER-TASK · OUTCOME · FINOPS",
            "subhead": "FROM PER-TOKEN TO PER-TASK · OUTCOME PRICING",
            "h": 1.0, "cols": 4, "row_h": 2.6, "accent": OCHRE, "dot_color": OCHRE,
            "items": [
                ("Token price · –4× / –10×", "Q1 '24 to Q1 '26"),
                ("CX trajectory · 4–25K tok", "~$0.02–$0.30 / task"),
                ("Code agent · 30–250K tok", "~$0.20–$3 / task"),
                ("Deep research · 0.5–5M tok", "~$1–$20 / task"),
                ("Planner-executor split", "70–85% on cheap tier"),
                ("Vercel AI Gateway routing", "first-class · GA '26"),
                ("AWS Bedrock · OpenRouter", "tier routing standard"),
                ("Outcome pricing — CX", "per-resolution · $1–4 (Taylor)"),
                ("Outcome — healthcare", "per-encounter · per-call $9/hr"),
                ("Per-seat survivors", "code · knowledge · finance"),
                ("FinOps for Tokens (Bet #4)", "12–18 mo window"),
                ("Hyperscaler bundling", "Bedrock auto-optim threat"),
            ],
        },
        {
            "num": "B",
            "name": "REGULATION",
            "scale": "meta · the gauntlet",
            "tagline": "EU AI ACT · CA SB 53 · SECTORAL",
            "subhead": "EU ARTICLE 14 · CA SB 53 · BARTZ · SECTORAL",
            "h": 1.0, "cols": 4, "row_h": 2.6, "accent": VERMILION, "dot_color": VERMILION,
            "items": [
                ("EU AI Act · Art. 55 GPAI", "enforceable Aug 2 '25"),
                ("EU AI Act · Art. 14 oversight", "draft Apr '26 · agentic"),
                ("EU AI Act · conformity drafts", "Feb '26 · Inspect AI cited"),
                ("CA SB 53 frontier disclosure", "effective Jan 1 '26"),
                ("NY S5641 · state-level", "advancing 2026"),
                ("Trump Dec '25 preemption EO", "courts through '26–'27"),
                ("Bartz v. Anthropic", "$1.5B training-data settle"),
                ("NYT v. OpenAI", "vendor terms repricing"),
                ("FINRA · OCC · BD rules", "finance agent fence"),
                ("HIPAA · FDA SaMD", "health agent fence"),
                ("TCPA · state consent", "voice agent fence"),
                ("EU AI Office", "structural regulator"),
            ],
        },
        {
            "num": "A",
            "name": "CAPABILITY · SAFETY",
            "scale": "meta · the deploy gate",
            "tagline": "ASL · PREPAREDNESS · FRONTIER",
            "subhead": "LAB-SIDE SAFETY REGIMES · EVAL INSTITUTES",
            "h": 1.0, "cols": 4, "row_h": 2.6, "accent": VERMILION, "dot_color": VERMILION,
            "items": [
                ("Anthropic ASL framework", "ASL-3 Opus 4 May '25"),
                ("Anthropic RSP — Nov '24", "binding policy"),
                ("OpenAI Preparedness Framework", "tracked categories"),
                ("Preparedness adjustment clause", "Risk #3 · open question"),
                ("Google Frontier Safety", "May '24 · maturing"),
                ("DeepMind capability evals", "auto-replication · cyber"),
                ("UK AISI", "Nov '23 · Inspect framework"),
                ("US AISI (post-restruct)", "early '26 · narrower scope"),
                ("METR (research org)", "time-horizon · 7-mo doubling"),
                ("EU AI Office", "regulatory counterpart"),
                ("ASL-4 capability emergence", "2026–27 question"),
                ("Model cards for agents", "in-flight standardization"),
            ],
        },
    ]
    build_strata_page(
        pdf, "VI", "PLATE VI OF VI",
        "Meta · Wrapping Forces",
        "Meta A–D · the four forces that wrap the agent layer: capability-safety regimes, regulation, economics, geopolitics.",
        "Quattuor stratorum meta · circumscribunt agenticam stratam",
        layers,
    )


# ============================================================
# Build
# ============================================================

if __name__ == "__main__":
    with PdfPages(OUT_PATH) as pdf:
        page_index(pdf)
        page_capability_substrate(pdf)
        page_cognition_loops(pdf)
        page_action_defense(pdf)
        page_productized(pdf)
        page_meta(pdf)

    size_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"Wrote {OUT_PATH} · {size_kb:.1f} KB")
