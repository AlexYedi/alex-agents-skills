import pymupdf
from pathlib import Path
ROOT = Path("/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output")
THUMB = ROOT / "_scripts" / "verify_thumbs"
doc = pymupdf.open(ROOT / "agents-gtm/AGENTS_GTM_DECISIONS.pdf")
page = doc[1]
w, h = page.rect.width, page.rect.height
# Crop the dense upper-middle Pioneer / Settler region (left half, top 60%)
clip = pymupdf.Rect(0, 0, w*0.55, h*0.55)
mat = pymupdf.Matrix(200/72, 200/72)
pix = page.get_pixmap(matrix=mat, alpha=False, clip=clip)
pix.save(THUMB / "DECISIONS_p2_topleft_zoom.png")
print(f"crop: {pix.width}x{pix.height}")
# Also crop a more focused region around the dense Genesis cluster
clip2 = pymupdf.Rect(w*0.20, h*0.08, w*0.55, h*0.45)
pix2 = page.get_pixmap(matrix=mat, alpha=False, clip=clip2)
pix2.save(THUMB / "DECISIONS_p2_genesis_zoom.png")
print(f"zoom: {pix2.width}x{pix2.height}")
doc.close()
