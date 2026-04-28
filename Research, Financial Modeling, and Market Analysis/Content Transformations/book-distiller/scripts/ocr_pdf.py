#!/usr/bin/env python3
"""
OCR wrapper for the book-distiller pipeline.

Wraps `ocrmypdf` to convert image-based PDFs (e.g., screen captures) into
text-extractable PDFs. After running this, pypdf can read the output.

Usage:
  python3 ocr_pdf.py <input.pdf> <output.pdf>
  python3 ocr_pdf.py <input.pdf> <output.pdf> --jobs 8

Defaults:
  --output-type pdf    (preserves layout, smaller than pdfa)
  --skip-text          (skip pages that already have text — idempotent)
  --jobs 4             (parallel page workers)

Exits non-zero on failure. Prints output PDF path on success.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Input PDF path")
    parser.add_argument("output", help="Output PDF path (text-extractable)")
    parser.add_argument("--jobs", type=int, default=4,
                        help="Parallel page workers (default 4)")
    parser.add_argument("--language", default="eng",
                        help="Tesseract language code (default eng)")
    parser.add_argument("--force", action="store_true",
                        help="Re-OCR even if output exists")
    args = parser.parse_args()

    if not shutil.which("ocrmypdf"):
        sys.exit("ERROR: ocrmypdf not on PATH. Run `brew install ocrmypdf`.")

    in_path = Path(args.input).expanduser().resolve()
    out_path = Path(args.output).expanduser().resolve()

    if not in_path.exists():
        sys.exit(f"ERROR: input not found: {in_path}")

    if out_path.exists() and not args.force:
        print(f"OK: output already exists at {out_path} (use --force to re-run)")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ocrmypdf",
        "--output-type", "pdf",
        "--skip-text",
        "--jobs", str(args.jobs),
        "--language", args.language,
        str(in_path),
        str(out_path),
    ]
    print(f"Running: {' '.join(cmd)}", file=sys.stderr)
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(f"ERROR: ocrmypdf exited {result.returncode}")
    print(f"OK: wrote {out_path}")


if __name__ == "__main__":
    main()
