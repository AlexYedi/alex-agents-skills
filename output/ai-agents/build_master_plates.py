"""
SUBSTRATE · Vol III · MASTER PLATES
A clean PDF of just the plates in the correct order they should be experienced:
  1. Cover
  2. Plate M — Master Plate (the agent seen whole · synthesis frontispiece)
  3. Plates I–VI — Substrate Vol I · the agent column (sub-strata + meta)
  4. Plates VII–XI — Substrate Vol II · framework plates

No prose pages — the plates stand on their own at their native size and aesthetic.
"""
import os
import tempfile
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
from pypdf import PdfWriter, PdfReader

BASE = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents"
OUT_PATH = f"{BASE}/AI_AGENTS_MASTER_PLATES.pdf"

# ---------- Fonts ----------
FONT_DIR = "/Users/sameoldexpressions/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/f85326cc-c479-4349-956a-d3d47e404d0b/d1370235-0ed8-47e6-859d-0bec833074a3/skills/canvas-design/canvas-fonts"
if os.path.isdir(FONT_DIR):
    for fp in os.listdir(FONT_DIR):
        if fp.endswith((".ttf", ".otf")):
            fm.fontManager.addfont(os.path.join(FONT_DIR, fp))

def fam(filename, fallback="DejaVu Sans"):
    path = os.path.join(FONT_DIR, filename)
    if os.path.isfile(path):
        return fm.FontProperties(fname=path).get_name()
    return fallback

F_DISPLAY = fam("BigShoulders-Bold.ttf")
F_SERIF = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT = fam("InstrumentSerif-Italic.ttf")
F_MONO = fam("GeistMono-Regular.ttf")
F_DMMONO = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42

# ---------- Palette ----------
PAPER = "#F1E9D6"
INK = "#171210"
INK_SOFT = "#3A2F26"
GRAY = "#7A6E60"
RULE = "#2A211B"
VERMILION = "#A6371F"
OCHRE = "#A37425"

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


# ============================================================
# COVER + CONTENTS PAGE
# ============================================================

def build_cover_pdf(out_path):
    PAGE_W, PAGE_H = 11.0, 17.0  # Tabloid portrait — matches plate orientation
    with PdfPages(out_path) as pdf:
        # ----- COVER -----
        fig = plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=PAPER)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 110); ax.set_ylim(0, 170)
        ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

        ax.add_patch(mpatches.Rectangle((6, 6), 98, 158, fill=False, ec=RULE, lw=0.6))

        ax.text(55, 140, sp("AN ATLAS OF THE AGENT STRATA", 4),
                ha="center", va="center", fontsize=8, fontname=F_MONO, color=GRAY)
        ax.plot([25, 85], [135, 135], color=RULE, lw=0.4)

        ax.text(55, 115, "THE AGENT,\nSEEN WHOLE",
                ha="center", va="center", fontsize=44, fontname=F_DISPLAY, color=INK,
                linespacing=0.95)
        ax.text(55, 95, "The Plates",
                ha="center", va="center", fontsize=22, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
        ax.plot([42, 68], [89, 89], color=VERMILION, lw=0.8)

        ax.text(55, 82,
                "Twelve plates in the order they should be experienced —",
                ha="center", va="center", fontsize=11, fontname=F_SERIF_IT, color=INK_SOFT)
        ax.text(55, 78,
                "synthesis first, then the agent column, then the frameworks.",
                ha="center", va="center", fontsize=11, fontname=F_SERIF_IT, color=INK_SOFT)

        ax.add_patch(mpatches.Circle((55, 55), 7, fill=False, ec=VERMILION, lw=0.7))
        ax.text(55, 55, "M", ha="center", va="center",
                fontsize=22, fontname=F_DISPLAY, color=VERMILION)

        ax.text(55, 30, "Compiled for A. Yedi · Cycle MMXXVI · Revision I",
                ha="center", va="center", fontsize=11, fontname=F_SERIF_DISP_IT, color=INK)
        ax.text(55, 25, "2026-05-14",
                ha="center", va="center", fontsize=8.5, fontname=F_DMMONO, color=GRAY)

        ax.text(55, 12, sp("SUBSTRATE · VOLUME III · MASTER PLATES", 3),
                ha="center", va="center", fontsize=6.5, fontname=F_MONO, color=GRAY)

        pdf.savefig(fig, facecolor=PAPER)
        plt.close(fig)

        # ----- CONTENTS PAGE -----
        fig = plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=PAPER)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 110); ax.set_ylim(0, 170)
        ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

        ax.add_patch(mpatches.Rectangle((6, 6), 98, 158, fill=False, ec=RULE, lw=0.6))

        ax.text(10, 156, sp("CONTENTS", 3),
                ha="left", va="center", fontsize=9, fontname=F_MONO, color=VERMILION)
        ax.text(10, 148, "Twelve plates in the order they should be read",
                ha="left", va="center", fontsize=22, fontname=F_DISPLAY, color=INK)
        ax.plot([10, 100], [142, 142], color=RULE, lw=0.5)

        # Section I — The Synthesis Frontispiece
        ax.text(10, 134, sp("§ I — THE SYNTHESIS", 2),
                ha="left", va="center", fontsize=8, fontname=F_MONO, color=VERMILION)
        ax.text(12, 126, "M", ha="left", va="center",
                fontsize=15, fontname=F_DISPLAY, color=VERMILION)
        ax.text(20, 127, "Master Plate · The agent layer as a single connected system",
                ha="left", va="center", fontsize=12, fontname=F_SERIF, color=INK)
        ax.text(20, 122, "Begin here — every later plate is a zoom into one quadrant of this one.",
                ha="left", va="center", fontsize=10, fontname=F_SERIF_IT, color=GRAY)

        ax.plot([10, 100], [115, 115], color=RULE, lw=0.3, alpha=0.5)

        # Section II — The Agent Column (Sub-Strata)
        ax.text(10, 108, sp("§ II — THE AGENT COLUMN · SUBSTRATE VOL I", 2),
                ha="left", va="center", fontsize=8, fontname=F_MONO, color=VERMILION)
        col_plates = [
            ("I",   "Index of the agent column — the ten sub-strata + four meta"),
            ("II",  "The cognition loop — perceive · plan · act · reflect"),
            ("III", "Memory and state — short-term, episodic, long-term, shared"),
            ("IV",  "Action surfaces — tool use, web, code, computer, voice"),
            ("V",   "Vertical products — where the agent meets the buyer"),
            ("VI",  "Evaluation, observability, safety — the meta-strata"),
        ]
        y0 = 100
        for i, (num, label) in enumerate(col_plates):
            y = y0 - i * 5.5
            ax.text(12, y, num, ha="left", va="center",
                    fontsize=11, fontname=F_DMMONO, color=OCHRE)
            ax.text(22, y, label, ha="left", va="center",
                    fontsize=11, fontname=F_SERIF, color=INK)

        ax.plot([10, 100], [62, 62], color=RULE, lw=0.3, alpha=0.5)

        # Section III — The Framework Plates
        ax.text(10, 55, sp("§ III — THE FRAMEWORK PLATES · SUBSTRATE VOL II", 2),
                ha="left", va="center", fontsize=8, fontname=F_MONO, color=VERMILION)
        fw_plates = [
            ("VII",  "OCQ heat map — opportunities, challenges, open questions"),
            ("VIII", "Wardley map — evolution of every component, claimable flags"),
            ("IX",   "Helmer's 7 Powers — which powers compound at the agent layer"),
            ("X",    "JTBD — the six ecosystem-level jobs the agent layer performs"),
            ("XI",   "Action Portfolio — the seven Bets refreshed, sequenced, sized"),
        ]
        y0 = 47
        for i, (num, label) in enumerate(fw_plates):
            y = y0 - i * 5.5
            ax.text(12, y, num, ha="left", va="center",
                    fontsize=11, fontname=F_DMMONO, color=OCHRE)
            ax.text(22, y, label, ha="left", va="center",
                    fontsize=11, fontname=F_SERIF, color=INK)

        ax.text(55, 12, sp("SUBSTRATE · VOLUME III · MASTER PLATES", 3),
                ha="center", va="center", fontsize=6.5, fontname=F_MONO, color=GRAY)

        pdf.savefig(fig, facecolor=PAPER)
        plt.close(fig)


# ============================================================
# SECTION DIVIDER PAGES
# ============================================================

def build_divider_pdf(out_path, eyebrow, title, subtitle, badge):
    PAGE_W, PAGE_H = 11.0, 17.0
    with PdfPages(out_path) as pdf:
        fig = plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=PAPER)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 110); ax.set_ylim(0, 170)
        ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

        ax.add_patch(mpatches.Rectangle((6, 6), 98, 158, fill=False, ec=RULE, lw=0.6))

        ax.text(55, 100, sp(eyebrow, 3),
                ha="center", va="center", fontsize=9, fontname=F_MONO, color=VERMILION)
        ax.plot([35, 75], [94, 94], color=RULE, lw=0.5)
        ax.text(55, 85, title,
                ha="center", va="center", fontsize=36, fontname=F_DISPLAY, color=INK)
        ax.text(55, 75, subtitle,
                ha="center", va="center", fontsize=14, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
        ax.text(55, 55, badge,
                ha="center", va="center", fontsize=11, fontname=F_DMMONO, color=VERMILION)

        ax.text(55, 12, sp("SUBSTRATE · VOLUME III · MASTER PLATES", 3),
                ha="center", va="center", fontsize=6.5, fontname=F_MONO, color=GRAY)

        pdf.savefig(fig, facecolor=PAPER)
        plt.close(fig)


# ============================================================
# BUILD
# ============================================================

def main():
    tmp = tempfile.mkdtemp(prefix="ai_agents_plates_")
    print(f"Tmp dir: {tmp}")

    cover_pdf = f"{tmp}/00_cover.pdf"
    print("Building cover + contents...")
    build_cover_pdf(cover_pdf)

    div_m = f"{tmp}/01_div_master.pdf"
    build_divider_pdf(div_m,
        "THE SYNTHESIS FRONTISPIECE",
        "Master Plate",
        "Begin here · the agent seen whole",
        "§ I of III")

    div_col = f"{tmp}/02_div_column.pdf"
    build_divider_pdf(div_col,
        "THE AGENT COLUMN",
        "Plates I–VI",
        "Sub-strata + the meta · the agent layer unfolded",
        "§ II of III")

    div_fw = f"{tmp}/03_div_framework.pdf"
    build_divider_pdf(div_fw,
        "THE FRAMEWORK PLATES",
        "Plates VII–XI",
        "OCQ · Wardley · 7 Powers · JTBD · Action Portfolio",
        "§ III of III")

    # Source plates
    master_plate = f"{BASE}/AI_AGENTS_MASTER_PLATE.pdf"
    substrate_vol1 = f"{BASE}/AI_AGENTS_SUBSTRATE.pdf"
    substrate_vol2 = f"{BASE}/AI_AGENTS_SUBSTRATE_VOL2.pdf"

    # Merge in experience order
    print("Merging plates in experience order...")
    order = [
        (cover_pdf, "Cover · Contents"),
        (div_m, "§ I — Synthesis Frontispiece"),
        (master_plate, "Plate M · Master"),
        (div_col, "§ II — Agent Column"),
        (substrate_vol1, "Plates I–VI"),
        (div_fw, "§ III — Framework Plates"),
        (substrate_vol2, "Plates VII–XI"),
    ]

    writer = PdfWriter()
    page_idx = 0
    bookmarks = []
    for path, name in order:
        reader = PdfReader(path)
        n = len(reader.pages)
        bookmarks.append((name, page_idx))
        for page in reader.pages:
            writer.add_page(page)
        page_idx += n

    # Add outline
    for title, idx in bookmarks:
        writer.add_outline_item(title, idx)

    with open(OUT_PATH, "wb") as f:
        writer.write(f)

    total = page_idx
    size_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"\nWrote {OUT_PATH}")
    print(f"  · {total} pages, {size_kb:.1f} KB")
    for name, idx in bookmarks:
        print(f"    p.{idx+1:3d}  {name}")


if __name__ == "__main__":
    main()
