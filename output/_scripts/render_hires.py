import pymupdf
from pathlib import Path
ROOT = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output")
THUMB = ROOT / "_scripts" / "verify_thumbs"
# Render at higher DPI, crop region of interest
doc = pymupdf.open(ROOT / "agents-gtm/AGENTS_GTM_DECISIONS.pdf")
page = doc[1]  # Wardley
mat = pymupdf.Matrix(200/72, 200/72)
pix = page.get_pixmap(matrix=mat, alpha=False)
pix.save(THUMB / "DECISIONS_p2_200dpi.png")
print(f"size: {pix.width}x{pix.height}")
doc.close()
