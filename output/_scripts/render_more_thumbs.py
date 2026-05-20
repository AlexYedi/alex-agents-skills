import pymupdf
from pathlib import Path
ROOT = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output")
THUMB = ROOT / "_scripts" / "verify_thumbs"
# Render additional pages from multi-page PDFs for inspection
TARGETS = [
    ("agents-gtm/AGENTS_GTM_DECISIONS.pdf", [1, 2, 3, 4]),  # Wardley, 7Powers, JTBD, ActionMap
    ("agents-gtm/AGENTS_GTM_SUBSTRATE.pdf", [0, 1, 2, 3, 4]),
    ("ai-agents/AI_AGENTS_SUBSTRATE.pdf", [0, 1, 2, 3, 4, 5]),
    ("ai-agents/AI_AGENTS_SUBSTRATE_VOL2.pdf", [0, 1, 2, 3, 4]),
]
for rel, pages in TARGETS:
    doc = pymupdf.open(ROOT / rel)
    for pi in pages:
        if pi >= len(doc): continue
        mat = pymupdf.Matrix(110/72, 110/72)
        pix = doc[pi].get_pixmap(matrix=mat, alpha=False)
        out = THUMB / f"{Path(rel).stem}_p{pi+1}.png"
        pix.save(out)
        print(f"wrote {out.name}")
    doc.close()
