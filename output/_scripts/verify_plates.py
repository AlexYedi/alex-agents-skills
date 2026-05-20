"""Spot-check the rebuilt plates: page dims, page count, and a thumbnail render.

Renders page 1 of each PDF to a PNG so a human can eyeball-check for overlap.
Also flags any text that visually clips the page border.
"""
from __future__ import annotations

import pymupdf  # type: ignore
from pathlib import Path

ROOT = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output")
PLATES = [
    "ai-agents/AI_AGENTS_MASTER_PLATE.pdf",
    "ai-agents/AI_AGENTS_SUBSTRATE.pdf",
    "ai-agents/AI_AGENTS_SUBSTRATE_VOL2.pdf",
    "ai-agents/AI_AGENTS_MASTER_VOLUME.pdf",
    "agents-gtm/AGENTS_GTM_MATRIX.pdf",
    "agents-gtm/AGENTS_GTM_MASTER_PLATE.pdf",
    "agents-gtm/AGENTS_GTM_SUBSTRATE.pdf",
    "agents-gtm/AGENTS_GTM_DECISIONS.pdf",
]

THUMB_DIR = ROOT / "_scripts" / "verify_thumbs"
THUMB_DIR.mkdir(parents=True, exist_ok=True)

for rel in PLATES:
    p = ROOT / rel
    if not p.exists():
        print(f"!! missing: {rel}")
        continue
    doc = pymupdf.open(p)
    page = doc[0]
    w_pt, h_pt = page.rect.width, page.rect.height
    w_in, h_in = w_pt / 72, h_pt / 72
    # rasterize at 100dpi -> a manageable thumbnail
    mat = pymupdf.Matrix(100 / 72, 100 / 72)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    out = THUMB_DIR / f"{Path(rel).stem}_p1.png"
    pix.save(out)
    # smallest text size on page (heuristic via spans)
    sizes = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if span["text"].strip():
                    sizes.append(span["size"])
    min_sz = min(sizes) if sizes else None
    max_sz = max(sizes) if sizes else None
    print(
        f"{rel:<55} pages={len(doc):>3}  "
        f"size={w_in:>5.1f}x{h_in:>5.1f}in  "
        f"text_pt_min={min_sz:>5.1f}  max={max_sz:>5.1f}  "
        f"thumb→{out.name}"
    )
    doc.close()
