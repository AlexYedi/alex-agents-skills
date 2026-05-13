"""
SUBSTRATE · Vol III · MASTER VOLUME
Combines all six deliverables into a single navigable PDF in reading order:
  1. Cover + Navigation guide
  2. Master Plate (the synthesis frontispiece)
  3. Foundation Reference (Report)
  4. Substrate Volume I — Plates I-VI
  5. Decisions Playbook (Addendum)
  6. Substrate Volume II — Plates VII-XI
  7. Living Tracker

Tools: pandoc (docx/md -> html), weasyprint (html -> pdf), pypdf (merge),
matplotlib (cover page in Substrate aesthetic).
"""
import os
import subprocess
import tempfile
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager as fm
from weasyprint import HTML, CSS
from pypdf import PdfWriter, PdfReader

BASE = "/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents"
OUT_PATH = f"{BASE}/AI_AGENTS_MASTER_VOLUME.pdf"

# ---------- Fonts (for the cover page) ----------
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
F_DISPLAY_REG = fam("BigShoulders-Regular.ttf")
F_SERIF = fam("CrimsonPro-Regular.ttf")
F_SERIF_IT = fam("CrimsonPro-Italic.ttf")
F_SERIF_DISP = fam("InstrumentSerif-Regular.ttf")
F_SERIF_DISP_IT = fam("InstrumentSerif-Italic.ttf")
F_MONO = fam("GeistMono-Regular.ttf")
F_MONO_BOLD = fam("GeistMono-Bold.ttf")
F_DMMONO = fam("DMMono-Regular.ttf")

mpl.rcParams["pdf.fonttype"] = 42

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
# COVER + NAVIGATION GUIDE (2 pages, matplotlib)
# ============================================================

def build_cover_pdf(out_path):
    PAGE_W, PAGE_H = 8.5, 11.0  # Letter — matches the prose pages
    with PdfPages(out_path) as pdf:
        # ----- COVER -----
        fig = plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=PAPER)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 100); ax.set_ylim(0, 130)
        ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

        # Border
        ax.add_patch(mpatches.Rectangle((6, 6), 88, 118, fill=False, ec=RULE, lw=0.6))

        # Eyebrow
        ax.text(50, 100, sp("AN ATLAS OF THE AGENT STRATA", 4),
                ha="center", va="center", fontsize=7, fontname=F_MONO, color=GRAY)
        ax.plot([20, 80], [97, 97], color=RULE, lw=0.4)

        # Title
        ax.text(50, 85, "THE AGENT, SEEN WHOLE",
                ha="center", va="center", fontsize=32, fontname=F_DISPLAY, color=INK)
        ax.text(50, 78, "A Master Volume",
                ha="center", va="center", fontsize=14, fontname=F_SERIF_DISP_IT, color=INK_SOFT)
        ax.plot([35, 65], [73, 73], color=VERMILION, lw=0.8)

        # Subtitle
        ax.text(50, 67, "Volume III · the agent layer unfolded as ten sub-strata plus four wrapping meta-strata.",
                ha="center", va="center", fontsize=9, fontname=F_SERIF_IT, color=INK_SOFT, wrap=True)
        ax.text(50, 63, "Seven artifacts in one bound order — frontispiece, foundation, decisions, plates, tracker.",
                ha="center", va="center", fontsize=9, fontname=F_SERIF_IT, color=INK_SOFT, wrap=True)

        # Center mark
        ax.add_patch(mpatches.Circle((50, 45), 8, fill=False, ec=VERMILION, lw=0.7))
        ax.text(50, 45, "M", ha="center", va="center",
                fontsize=24, fontname=F_DISPLAY, color=VERMILION)

        # Compiled-for
        ax.text(50, 26, "Compiled for A. Yedi",
                ha="center", va="center", fontsize=11, fontname=F_SERIF_DISP_IT, color=INK)
        ax.text(50, 22, "Cycle MMXXVI · Revision I · 2026-05-12",
                ha="center", va="center", fontsize=8, fontname=F_DMMONO, color=GRAY)

        # Footer
        ax.text(50, 12, sp("SUBSTRATE · VOLUME III · MASTER VOLUME", 3),
                ha="center", va="center", fontsize=6, fontname=F_MONO, color=GRAY)

        pdf.savefig(fig, facecolor=PAPER)
        plt.close(fig)

        # ----- NAVIGATION GUIDE -----
        fig = plt.figure(figsize=(PAGE_W, PAGE_H), facecolor=PAPER)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 100); ax.set_ylim(0, 130)
        ax.set_facecolor(PAPER); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

        ax.add_patch(mpatches.Rectangle((6, 6), 88, 118, fill=False, ec=RULE, lw=0.6))

        # Header
        ax.text(10, 120, sp("READING GUIDE", 3),
                ha="left", va="center", fontsize=8, fontname=F_MONO, color=VERMILION)
        ax.text(10, 115, "How to navigate this volume",
                ha="left", va="center", fontsize=18, fontname=F_DISPLAY, color=INK)
        ax.plot([10, 90], [111, 111], color=RULE, lw=0.4)

        # Reading order — sequential
        ax.text(10, 106, sp("A · SEQUENTIAL READ (FULL CYCLE)", 2),
                ha="left", va="center", fontsize=7, fontname=F_MONO, color=VERMILION)
        seq = [
            ("01", "Cover + this guide", "1–2"),
            ("02", "Master Plate · the synthesis frontispiece", "3"),
            ("03", "Foundation Reference · the descriptive layer (~10,000 words)", "4–"),
            ("04", "Substrate Volume I · Plates I–VI · the visual atlas", "—"),
            ("05", "Decisions Playbook · framework analyses + 7 Bets refreshed (~17,000 words)", "—"),
            ("06", "Substrate Volume II · Plates VII–XI · framework plates", "—"),
            ("07", "Living Tracker · the working surface", "—"),
        ]
        for i, (num, label, pgs) in enumerate(seq):
            y = 101 - i * 4
            ax.text(11, y, num, ha="left", va="center",
                    fontsize=7, fontname=F_DMMONO, color=VERMILION)
            ax.text(17, y, label, ha="left", va="center",
                    fontsize=9, fontname=F_SERIF, color=INK)

        # Reading order — speed read
        ax.plot([10, 90], [70, 70], color=RULE, lw=0.4)
        ax.text(10, 67, sp("B · NINETY-MINUTE SPEED READ", 2),
                ha="left", va="center", fontsize=7, fontname=F_MONO, color=VERMILION)
        ax.text(10, 63,
                "If you cannot read the volume cover-to-cover, take this path. Total ~90 min.",
                ha="left", va="center", fontsize=8, fontname=F_SERIF_IT, color=INK_SOFT)

        speed = [
            ("5 min", "Master Plate — the whole synthesis on one page"),
            ("10 min", "Tracker Section A — the 7 Bets refreshed (Vol III deltas annotated)"),
            ("20 min", "Addendum Part XI — Synthesis with full Bet rewrites, Risks, Cruxes"),
            ("15 min", "Addendum Part XIII — the Agent-Specific Procurement Rubric"),
            ("10 min", "Substrate Plate I (index) + Plate V (vertical products)"),
            ("10 min", "Report Executive Summary — five forces structuring the agent layer"),
            ("20 min", "Skim the rest as you act on the 6/12/18-Month Action Map (Addendum Part XII)"),
        ]
        for i, (time, label) in enumerate(speed):
            y = 58 - i * 3.5
            ax.text(11, y, time, ha="left", va="center",
                    fontsize=7, fontname=F_DMMONO, color=OCHRE)
            ax.text(22, y, label, ha="left", va="center",
                    fontsize=8.5, fontname=F_SERIF, color=INK)

        # The Volume III delta in one line
        ax.plot([10, 90], [28, 28], color=RULE, lw=0.4)
        ax.text(10, 25, sp("THE VOL III DELTA (ONE LINE)", 2),
                ha="left", va="center", fontsize=7, fontname=F_MONO, color=VERMILION)
        ax.text(10, 21,
                "Bet #1 sequenced first (claim Process Power) · Bet #2 second (collect equity)",
                ha="left", va="center", fontsize=9, fontname=F_SERIF_DISP, color=INK)
        ax.text(10, 18,
                "· Bet #3 third (compound as advisory) · Bets 4–5 fold into #1 as modules.",
                ha="left", va="center", fontsize=9, fontname=F_SERIF_DISP, color=INK)

        # Footer
        ax.text(50, 10, sp("SUBSTRATE · VOLUME III · MASTER VOLUME", 3),
                ha="center", va="center", fontsize=6, fontname=F_MONO, color=GRAY)

        pdf.savefig(fig, facecolor=PAPER)
        plt.close(fig)


# ============================================================
# UNIFIED CSS — applied to all prose conversions
# ============================================================

UNIFIED_CSS = """
@page {
  size: letter;
  margin: 0.85in 0.85in 0.85in 0.85in;
  @top-right {
    content: "SUBSTRATE · VOLUME III";
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7pt;
    color: #6E6356;
    letter-spacing: 0.08em;
  }
  @bottom-center {
    content: counter(page);
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8pt;
    color: #6E6356;
  }
}

body {
  font-family: Calibri, 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 11pt;
  line-height: 1.55;
  color: #1A1410;
  background: #F1E9D6;
}

h1 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 22pt;
  font-weight: 700;
  color: #1A1410;
  page-break-before: always;
  page-break-after: avoid;
  border-bottom: 1.2pt solid #A6371F;
  padding-bottom: 6pt;
  margin-top: 18pt;
  margin-bottom: 14pt;
}
h1:first-of-type {
  page-break-before: auto;
}

h2 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 16pt;
  font-weight: 700;
  color: #1A1410;
  margin-top: 18pt;
  margin-bottom: 8pt;
  page-break-after: avoid;
}

h3 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 12.5pt;
  font-weight: 700;
  color: #A6371F;
  margin-top: 14pt;
  margin-bottom: 6pt;
  page-break-after: avoid;
}

h4, h5, h6 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 11pt;
  font-weight: 700;
  color: #3A2F26;
  margin-top: 12pt;
  margin-bottom: 4pt;
}

p {
  margin: 0 0 7pt 0;
  text-align: justify;
  text-justify: inter-word;
  orphans: 2;
  widows: 2;
}

strong, b { font-weight: 700; color: #1A1410; }
em, i { font-style: italic; color: #3A2F26; }

ul, ol {
  margin: 4pt 0 8pt 0;
  padding-left: 22pt;
}
li {
  margin-bottom: 3pt;
  line-height: 1.45;
}

blockquote {
  margin: 8pt 16pt;
  padding-left: 10pt;
  border-left: 2pt solid #A6371F;
  color: #3A2F26;
  font-style: italic;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 10pt 0;
  font-size: 9.5pt;
}
th, td {
  border: 0.4pt solid #6E6356;
  padding: 4pt 6pt;
  text-align: left;
  vertical-align: top;
}
th {
  background: #E4DCC4;
  font-weight: 700;
  color: #1A1410;
  font-family: Georgia, serif;
}

code, pre {
  font-family: 'Consolas', 'Courier New', monospace;
  font-size: 9.5pt;
  color: #3A2F26;
}
pre {
  background: #E4DCC4;
  padding: 6pt;
  border-left: 2pt solid #A37425;
}

hr {
  border: none;
  border-top: 0.6pt solid #A6371F;
  margin: 10pt 0;
}

/* Section header style for the part dividers we inject */
.section-divider {
  page-break-before: always;
  text-align: center;
  margin-top: 2in;
}
.section-divider .eyebrow {
  font-family: 'Consolas', monospace;
  font-size: 8pt;
  letter-spacing: 0.32em;
  color: #A6371F;
  text-transform: uppercase;
}
.section-divider .title {
  font-family: Georgia, serif;
  font-size: 28pt;
  font-weight: 700;
  color: #1A1410;
  margin: 16pt 0 8pt 0;
}
.section-divider .subtitle {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 12pt;
  color: #6E6356;
}
.section-divider .badge {
  font-family: 'Consolas', monospace;
  font-size: 9pt;
  letter-spacing: 0.2em;
  color: #A6371F;
  margin-top: 24pt;
}
"""

def section_divider_html(eyebrow, title, subtitle, badge):
    return f"""
<!DOCTYPE html>
<html><head><meta charset="utf-8"></head><body>
<div class="section-divider">
  <div class="eyebrow">{eyebrow}</div>
  <div class="title">{title}</div>
  <div class="subtitle">{subtitle}</div>
  <div class="badge">{badge}</div>
</div>
</body></html>
"""


# ============================================================
# PROSE CONVERSION — pandoc -> HTML -> weasyprint -> PDF
# ============================================================

def convert_to_pdf(src_path, out_pdf, title=None):
    """Convert a docx or markdown file to a styled PDF using pandoc + weasyprint."""
    # 1. pandoc to HTML body
    cmd = ["pandoc", src_path, "-t", "html5", "--no-highlight", "--wrap=none"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    body_html = result.stdout

    # 2. Wrap with full HTML + our unified CSS
    full_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title or 'Document'}</title></head>
<body>
{body_html}
</body></html>"""

    # 3. Render with weasyprint
    HTML(string=full_html, base_url=BASE).write_pdf(
        out_pdf,
        stylesheets=[CSS(string=UNIFIED_CSS)]
    )

def divider_to_pdf(eyebrow, title, subtitle, badge, out_pdf):
    html = section_divider_html(eyebrow, title, subtitle, badge)
    HTML(string=html).write_pdf(out_pdf, stylesheets=[CSS(string=UNIFIED_CSS)])


# ============================================================
# BUILD
# ============================================================

def main():
    tmp = tempfile.mkdtemp(prefix="ai_agents_master_")
    print(f"Tmp dir: {tmp}")

    # 1. Cover + navigation guide
    cover_pdf = f"{tmp}/00_cover.pdf"
    print("Building cover + navigation...")
    build_cover_pdf(cover_pdf)

    # 2. Master Plate (already exists)
    master_plate_pdf = f"{BASE}/AI_AGENTS_MASTER_PLATE.pdf"

    # 3. Foundation Reference + divider
    print("Converting Foundation Reference...")
    report_divider = f"{tmp}/02_divider_report.pdf"
    divider_to_pdf(
        "AN ATLAS OF THE AGENT STRATA",
        "The Foundation Reference",
        "Volume III · the descriptive layer · ten sub-strata plus four wrapping meta-strata",
        "Section II of VII",
        report_divider
    )
    report_pdf = f"{tmp}/03_report.pdf"
    convert_to_pdf(f"{BASE}/AI_AGENTS_REPORT.docx", report_pdf, title="Foundation Reference")

    # 4. Substrate Plates I-VI (already exists)
    substrate_pdf = f"{BASE}/AI_AGENTS_SUBSTRATE.pdf"
    substrate_divider = f"{tmp}/04_divider_substrate1.pdf"
    divider_to_pdf(
        "VISUAL ATLAS",
        "Substrate · Volume I",
        "Plates I–VI · the agent column · index + sub-strata + meta",
        "Section III of VII",
        substrate_divider
    )

    # 5. Decisions Playbook
    print("Converting Decisions Playbook...")
    addendum_divider = f"{tmp}/06_divider_addendum.pdf"
    divider_to_pdf(
        "FRAMEWORK ANALYSES + DECISIONS",
        "The Decisions Playbook",
        "Volume III · five frameworks · seven Bets refreshed · five Risks · five Cruxes",
        "Section IV of VII",
        addendum_divider
    )
    addendum_pdf = f"{tmp}/07_addendum.pdf"
    convert_to_pdf(f"{BASE}/AI_AGENTS_ADDENDUM.docx", addendum_pdf, title="Decisions Playbook")

    # 6. Substrate Plates VII-XI (already exists)
    substrate2_pdf = f"{BASE}/AI_AGENTS_SUBSTRATE_VOL2.pdf"
    substrate2_divider = f"{tmp}/08_divider_substrate2.pdf"
    divider_to_pdf(
        "VISUAL ATLAS",
        "Substrate · Volume II",
        "Plates VII–XI · OCQ heat · Wardley · 7 Powers · JTBD · Action Portfolio",
        "Section V of VII",
        substrate2_divider
    )

    # 7. Living Tracker
    print("Converting Living Tracker...")
    tracker_divider = f"{tmp}/10_divider_tracker.pdf"
    divider_to_pdf(
        "THE WORKING SURFACE",
        "The Living Tracker",
        "Volume III · seven Bets · talent + capital flow · cruxes · risks",
        "Section VI of VII",
        tracker_divider
    )
    tracker_pdf = f"{tmp}/11_tracker.pdf"
    convert_to_pdf(f"{BASE}/AI_AGENTS_TRACKER.md", tracker_pdf, title="Living Tracker")

    # Master Plate divider
    masterplate_divider = f"{tmp}/01_divider_master.pdf"
    divider_to_pdf(
        "THE SYNTHESIS",
        "Master Plate",
        "Volume III · the agent layer as a single connected system",
        "Section I of VII",
        masterplate_divider
    )

    # 8. MERGE all PDFs in reading order
    print("Merging into Master Volume...")
    order = [
        cover_pdf,              # Cover + Navigation
        masterplate_divider,    # § I
        master_plate_pdf,
        report_divider,         # § II
        report_pdf,
        substrate_divider,      # § III
        substrate_pdf,
        addendum_divider,       # § IV
        addendum_pdf,
        substrate2_divider,     # § V
        substrate2_pdf,
        tracker_divider,        # § VI
        tracker_pdf,
    ]

    writer = PdfWriter()
    page_counts = []
    for path in order:
        reader = PdfReader(path)
        n = len(reader.pages)
        page_counts.append((os.path.basename(path), n))
        for page in reader.pages:
            writer.add_page(page)

    # Add a bookmark/outline structure
    page_idx = 0
    bookmarks = [
        ("Cover · Navigation", 0, 2),
        ("§ I — Master Plate", 2, 2),
        ("§ II — Foundation Reference (Report)", 4, None),
        ("§ III — Substrate Plates I–VI", None, 6),
        ("§ IV — Decisions Playbook (Addendum)", None, None),
        ("§ V — Substrate Plates VII–XI", None, 5),
        ("§ VI — Living Tracker", None, None),
    ]
    # Cumulative page counts
    cum = 0
    bookmark_starts = []
    for name, n in page_counts:
        bookmark_starts.append((name, cum))
        cum += n

    # Build outline: pair section dividers with their starts
    # Section dividers come at indexes: 1, 3, 5, 7, 9, 11
    section_indexes = [
        ("Cover · Navigation", 0),
        ("I · Master Plate", 1),
        ("II · Foundation Reference (Report)", 3),
        ("III · Substrate Plates I–VI", 5),
        ("IV · Decisions Playbook (Addendum)", 7),
        ("V · Substrate Plates VII–XI", 9),
        ("VI · Living Tracker", 11),
    ]
    for title, idx in section_indexes:
        if idx < len(bookmark_starts):
            page = bookmark_starts[idx][1]
            writer.add_outline_item(title, page)

    with open(OUT_PATH, "wb") as f:
        writer.write(f)

    total_pages = sum(n for _, n in page_counts)
    size_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"\nWrote {OUT_PATH}")
    print(f"  · {total_pages} pages, {size_kb:.1f} KB")
    print("\nSection breakdown:")
    for name, n in page_counts:
        print(f"    {name:40s} {n:4d} pp")


if __name__ == "__main__":
    main()
