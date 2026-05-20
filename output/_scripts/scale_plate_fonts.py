"""
Scale fonts and page dimensions across all plate-build scripts.

Rules:
  - matplotlib `fontsize=N` (int or float)  -> max(10.0, round(N*1.2, 1))
  - CSS `font-size: Npt`                    -> max(10.0, round(N*1.2, 1))pt
  - `PAGE_W` / `PAGE_H` numeric literals    -> multiplied by PAGE_SCALE (default 1.4)
  - `figsize=(W, H)` numeric literals       -> multiplied by PAGE_SCALE
  - `page_w` / `page_h` default args        -> multiplied by PAGE_SCALE

Idempotent: re-running on already-scaled files won't change them again,
because the floor and the multiplier together yield a stable fixed point
once values are >= the new floor and have been multiplied once.  We track
that with a sentinel comment `# plate-fonts-scaled-v1` at the top of each
file.  Files bearing the sentinel are skipped.

Usage:
    python output/_scripts/scale_plate_fonts.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output")

TARGETS = [
    "ai-agents/build_master_plate.py",
    "ai-agents/build_master_volume.py",
    "ai-agents/build_substrate.py",
    "ai-agents/build_substrate_vol2.py",
    "agents-gtm/build_matrix_plate.py",
    "agents-gtm/build_master_plate.py",
    "agents-gtm/build_substrate.py",
    "agents-gtm/build_decisions.py",
]

SENTINEL = "# plate-fonts-scaled-v1"

FONT_FLOOR = 10.0
FONT_MULT = 1.2
PAGE_SCALE = 1.4


def scaled_font(v: float) -> float:
    return max(FONT_FLOOR, round(v * FONT_MULT, 1))


def scaled_page(v: float) -> float:
    return round(v * PAGE_SCALE, 2)


def fmt(v: float) -> str:
    """Render with no trailing zeros, no unnecessary decimal."""
    if v == int(v):
        return str(int(v))
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s


# --- regexes -----------------------------------------------------------------
RX_MPL = re.compile(r"\bfontsize\s*=\s*(\d+(?:\.\d+)?)")
RX_CSS = re.compile(r"font-size:\s*(\d+(?:\.\d+)?)\s*pt")
RX_PAGE_W = re.compile(r"^(PAGE_W\s*=\s*)(\d+(?:\.\d+)?)", re.MULTILINE)
RX_PAGE_H = re.compile(r"^(PAGE_H\s*=\s*)(\d+(?:\.\d+)?)", re.MULTILINE)
# Inline pair: PAGE_W, PAGE_H = a, b
RX_PAGE_PAIR = re.compile(
    r"^(PAGE_W\s*,\s*PAGE_H\s*=\s*)(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)",
    re.MULTILINE,
)
# Local assignments inside fn bodies: indented "PAGE_W = 17.0"
RX_PAGE_W_INDENT = re.compile(r"^(\s+PAGE_W\s*=\s*)(\d+(?:\.\d+)?)", re.MULTILINE)
RX_PAGE_H_INDENT = re.compile(r"^(\s+PAGE_H\s*=\s*)(\d+(?:\.\d+)?)", re.MULTILINE)
# Inline figsize=(W, H) literal
RX_FIGSIZE = re.compile(
    r"figsize\s*=\s*\(\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*\)"
)
# Function default args: page_w=11.0, page_h=17.0
RX_PAGE_KW = re.compile(
    r"(\bpage_[wh]\s*=\s*)(\d+(?:\.\d+)?)"
)


def transform(text: str) -> tuple[str, dict[str, int]]:
    counts = {"fontsize": 0, "css_font": 0, "page_dim": 0, "figsize": 0}

    def sub_font_mpl(m: re.Match) -> str:
        counts["fontsize"] += 1
        v = float(m.group(1))
        return f"fontsize={fmt(scaled_font(v))}"

    def sub_font_css(m: re.Match) -> str:
        counts["css_font"] += 1
        v = float(m.group(1))
        return f"font-size: {fmt(scaled_font(v))}pt"

    def sub_page_pair(m: re.Match) -> str:
        counts["page_dim"] += 2
        a, b = float(m.group(2)), float(m.group(3))
        return f"{m.group(1)}{fmt(scaled_page(a))}, {fmt(scaled_page(b))}"

    def sub_page_w(m: re.Match) -> str:
        counts["page_dim"] += 1
        return f"{m.group(1)}{fmt(scaled_page(float(m.group(2))))}"

    def sub_figsize(m: re.Match) -> str:
        counts["figsize"] += 1
        a, b = float(m.group(1)), float(m.group(2))
        return f"figsize=({fmt(scaled_page(a))}, {fmt(scaled_page(b))})"

    def sub_page_kw(m: re.Match) -> str:
        counts["page_dim"] += 1
        return f"{m.group(1)}{fmt(scaled_page(float(m.group(2))))}"

    # Order: page_pair first (consumes both on one line), then singletons.
    text = RX_PAGE_PAIR.sub(sub_page_pair, text)
    text = RX_PAGE_W.sub(sub_page_w, text)
    text = RX_PAGE_H.sub(sub_page_w, text)
    text = RX_PAGE_W_INDENT.sub(sub_page_w, text)
    text = RX_PAGE_H_INDENT.sub(sub_page_w, text)
    text = RX_FIGSIZE.sub(sub_figsize, text)
    text = RX_PAGE_KW.sub(sub_page_kw, text)
    text = RX_MPL.sub(sub_font_mpl, text)
    text = RX_CSS.sub(sub_font_css, text)
    return text, counts


def main() -> int:
    summary = []
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            print(f"!! MISSING: {path}")
            continue
        src = path.read_text(encoding="utf-8")
        if SENTINEL in src:
            print(f".. SKIP (already scaled): {rel}")
            continue
        new, counts = transform(src)
        # add sentinel after the module docstring or at top
        # find end of docstring if present
        m = re.match(r'^("""[\s\S]*?""")\s*\n', new)
        if m:
            new = new[: m.end()] + SENTINEL + "\n" + new[m.end():]
        else:
            new = SENTINEL + "\n" + new
        path.write_text(new, encoding="utf-8")
        summary.append((rel, counts))
        print(
            f"OK {rel}: fontsize={counts['fontsize']} css={counts['css_font']} "
            f"page_dim={counts['page_dim']} figsize={counts['figsize']}"
        )

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
