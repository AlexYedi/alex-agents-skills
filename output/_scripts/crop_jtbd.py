import pymupdf
from pathlib import Path
ROOT = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output")
THUMB = ROOT / "_scripts" / "verify_thumbs"
doc = pymupdf.open(ROOT / "agents-gtm/AGENTS_GTM_DECISIONS.pdf")
page = doc[3]
w, h = page.rect.width, page.rect.height
clip = pymupdf.Rect(0, h*0.12, w*0.5, h*0.6)
mat = pymupdf.Matrix(200/72, 200/72)
pix = page.get_pixmap(matrix=mat, alpha=False, clip=clip)
pix.save(THUMB / "DECISIONS_p4_jtbd_zoom.png")
print(f"zoom: {pix.width}x{pix.height}")
doc.close()
