#!/usr/bin/env python3
"""
Extract chapter text from a text-extractable PDF.

Two modes:

  by-pages: Extract a specific page range (most reliable)
    python3 extract_chapter.py <pdf> --pages 12-34 --out /tmp/chunk.txt

  by-toc: Detect chapters via heading patterns and extract one
    python3 extract_chapter.py <pdf> --toc            (list detected chapters)
    python3 extract_chapter.py <pdf> --chapter 7 --out /tmp/chunk.txt

  full: Extract entire PDF as one chunk (small books or screening)
    python3 extract_chapter.py <pdf> --full --out /tmp/all.txt

Requires the PDF to have an OCR text layer. Run scripts/ocr_pdf.py first
on image-based PDFs.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import pypdf
except ImportError:
    sys.exit("ERROR: pypdf not installed. Run `pip3 install pypdf`.")


# Heading patterns common to O'Reilly + similar technical books.
CHAPTER_PATTERNS = [
    re.compile(r"^\s*Chapter\s+(\d+)[\.\s:]+(.+?)$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*CHAPTER\s+(\d+)\s*$", re.MULTILINE),
    re.compile(r"^\s*(\d+)\.\s+([A-Z][A-Za-z\s]+)$", re.MULTILINE),
]


def open_pdf(path: Path) -> pypdf.PdfReader:
    if not path.exists():
        sys.exit(f"ERROR: PDF not found: {path}")
    try:
        return pypdf.PdfReader(str(path))
    except Exception as e:
        sys.exit(f"ERROR: failed to open PDF: {e}")


def parse_page_range(spec: str, max_page: int) -> list[int]:
    """Parse '1-5' or '7' into 0-indexed page numbers."""
    if "-" in spec:
        a, b = spec.split("-", 1)
        start, end = int(a), int(b)
    else:
        start = end = int(spec)
    if start < 1 or end > max_page or start > end:
        sys.exit(f"ERROR: invalid page range {spec} (PDF has {max_page} pages)")
    return list(range(start - 1, end))


def extract_pages(reader: pypdf.PdfReader, page_indexes: list[int]) -> str:
    parts = []
    for idx in page_indexes:
        try:
            text = reader.pages[idx].extract_text() or ""
        except Exception as e:
            print(f"  warn: page {idx + 1} extract failed: {e}", file=sys.stderr)
            text = ""
        parts.append(text)
    return "\n\n".join(p.strip() for p in parts if p.strip())


def detect_chapters(reader: pypdf.PdfReader) -> list[dict]:
    """Walk pages, find chapter heading hits, return [{num, title, start_page}]."""
    chapters = []
    seen_nums = set()
    for page_idx, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception:
            continue
        for pat in CHAPTER_PATTERNS:
            for m in pat.finditer(text):
                groups = m.groups()
                num_str = groups[0]
                title = groups[1].strip() if len(groups) > 1 else f"Chapter {num_str}"
                try:
                    num = int(num_str)
                except ValueError:
                    continue
                if num in seen_nums:
                    continue
                seen_nums.add(num)
                chapters.append({
                    "num": num,
                    "title": title,
                    "start_page": page_idx + 1,  # 1-indexed for display
                })
                break
    chapters.sort(key=lambda c: c["num"])
    return chapters


def cmd_pages(args):
    reader = open_pdf(Path(args.pdf))
    pages = parse_page_range(args.pages, len(reader.pages))
    text = extract_pages(reader, pages)
    write_or_print(text, args.out)


def cmd_toc(args):
    reader = open_pdf(Path(args.pdf))
    chapters = detect_chapters(reader)
    if not chapters:
        print("No chapters detected. Try --pages mode instead.", file=sys.stderr)
        sys.exit(2)
    print(f"Detected {len(chapters)} chapters in {args.pdf}:")
    for c in chapters:
        print(f"  {c['num']:>3}. {c['title']:<60} (page {c['start_page']})")


def cmd_chapter(args):
    reader = open_pdf(Path(args.pdf))
    chapters = detect_chapters(reader)
    target = next((c for c in chapters if c["num"] == args.chapter), None)
    if not target:
        sys.exit(f"ERROR: chapter {args.chapter} not detected. Run --toc to list.")

    next_chapter = next((c for c in chapters if c["num"] == args.chapter + 1), None)
    end_page = next_chapter["start_page"] - 1 if next_chapter else len(reader.pages)
    pages = list(range(target["start_page"] - 1, end_page))

    print(f"Chapter {target['num']}: {target['title']}", file=sys.stderr)
    print(f"  pages {target['start_page']}-{end_page} ({len(pages)} pages)", file=sys.stderr)

    text = extract_pages(reader, pages)
    write_or_print(text, args.out)


def cmd_full(args):
    reader = open_pdf(Path(args.pdf))
    pages = list(range(len(reader.pages)))
    text = extract_pages(reader, pages)
    write_or_print(text, args.out)


def write_or_print(text: str, out_path: str | None):
    if out_path:
        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        chars = len(text)
        print(f"OK: wrote {chars:,} chars to {out_path}")
    else:
        print(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", help="Path to text-extractable PDF")
    parser.add_argument("--pages", help="Page range, e.g. '12-34' or '7'")
    parser.add_argument("--toc", action="store_true",
                        help="List detected chapters and exit")
    parser.add_argument("--chapter", type=int, help="Extract chapter by number")
    parser.add_argument("--full", action="store_true",
                        help="Extract entire PDF as one chunk")
    parser.add_argument("--out", help="Write to file (default stdout)")
    args = parser.parse_args()

    modes = sum(bool(x) for x in [args.pages, args.toc, args.chapter, args.full])
    if modes != 1:
        parser.error("Specify exactly one of: --pages, --toc, --chapter, --full")

    if args.pages:
        cmd_pages(args)
    elif args.toc:
        cmd_toc(args)
    elif args.chapter:
        cmd_chapter(args)
    elif args.full:
        cmd_full(args)


if __name__ == "__main__":
    main()
