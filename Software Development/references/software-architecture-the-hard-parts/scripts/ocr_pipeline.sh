#!/usr/bin/env bash
# OCR pipeline for image-only PDFs of Software Architecture: The Hard Parts.
#
# The source PDF distributed to Alex is image-only (Kindle screenshots, ~225MB,
# no embedded text). This script makes it searchable + extracts plaintext for
# distillation work.
#
# Outputs land in output/hard-parts-ocr/ at the repo root and are gitignored.
#
# Requirements (install via Homebrew on macOS):
#   brew install ocrmypdf tesseract poppler
#
# Usage:
#   ./ocr_pipeline.sh <path-to-source-pdf>
#
# Typical runtime: 15-30 min for ~330 image pages on Apple Silicon.

set -euo pipefail

SOURCE_PDF="${1:-}"

if [[ -z "$SOURCE_PDF" ]]; then
  echo "usage: $0 <path-to-source-pdf>" >&2
  exit 1
fi

if [[ ! -f "$SOURCE_PDF" ]]; then
  echo "source pdf not found: $SOURCE_PDF" >&2
  exit 1
fi

# Resolve repo root (this script lives at
# Software Development/references/software-architecture-the-hard-parts/scripts/ocr_pipeline.sh).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
OUT_DIR="$REPO_ROOT/output/hard-parts-ocr"

mkdir -p "$OUT_DIR"

OCR_PDF="$OUT_DIR/hard-parts-ocr.pdf"
PLAINTEXT="$OUT_DIR/hard-parts.txt"
LOGFILE="$OUT_DIR/ocr.log"

echo "OCR started at $(date)" | tee "$LOGFILE"
echo "source: $SOURCE_PDF" | tee -a "$LOGFILE"
echo "output dir: $OUT_DIR" | tee -a "$LOGFILE"

# --skip-text     : pages already containing text are passed through
# --optimize 0    : don't bother compressing (we'll throw the PDF away)
# --jobs 4        : 4-way parallelism — tune to your machine
# --language eng  : English text
ocrmypdf \
  --output-type pdf \
  --optimize 0 \
  --skip-text \
  --jobs 4 \
  --language eng \
  "$SOURCE_PDF" \
  "$OCR_PDF" \
  >>"$LOGFILE" 2>&1

# Extract plaintext with column layout preserved (most reliable for Kindle screenshots).
pdftotext -layout "$OCR_PDF" "$PLAINTEXT"

echo "OCR done at $(date)" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"
echo "outputs:" | tee -a "$LOGFILE"
echo "  $OCR_PDF  ($(du -h "$OCR_PDF" | cut -f1))" | tee -a "$LOGFILE"
echo "  $PLAINTEXT  ($(wc -l <"$PLAINTEXT" | tr -d ' ') lines)" | tee -a "$LOGFILE"
echo "  $LOGFILE" | tee -a "$LOGFILE"
