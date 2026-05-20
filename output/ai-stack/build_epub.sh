#!/usr/bin/env bash
# Build AI_STACK_MASTER.epub from chapters/*.md + plates/*.svg
# Run from the ai-stack-v2/ directory: bash build_epub.sh

set -euo pipefail

cd "$(dirname "$0")"

OUTPUT="AI_STACK_MASTER.epub"
TITLE_FILE="chapters/_title.md"

# Chapter order — drives reading flow
CHAPTERS=(
    "chapters/_title.md"
    "chapters/00_frame.md"
    "chapters/01_substrate.md"
    "chapters/02_frameworks.md"
    "chapters/03_bets_risks_cruxes.md"
    "chapters/04_tracker.md"
    "chapters/05_rituals.md"
    "chapters/06_appendix.md"
)

# Verify every chapter exists before building
for ch in "${CHAPTERS[@]}"; do
    if [[ ! -f "$ch" ]]; then
        echo "ERROR: missing chapter $ch" >&2
        exit 1
    fi
done

# Verify all 5 plates exist
for plate in plates/0{1..5}_*.svg; do
    if [[ ! -f "$plate" ]]; then
        echo "ERROR: missing plate $plate" >&2
        exit 1
    fi
done

echo "Building $OUTPUT from ${#CHAPTERS[@]} chapters + 5 plates..."

pandoc \
    "${CHAPTERS[@]}" \
    --from markdown \
    --to epub3 \
    --output "$OUTPUT" \
    --toc \
    --toc-depth=2 \
    --split-level=1 \
    --metadata title="AI Stack Master" \
    --metadata subtitle="An operating workbook for the 2026–2027 thesis" \
    --metadata author="Alex Yedi" \
    --metadata date="$(date +%Y-%m-%d)" \
    --metadata lang="en-US" \
    --metadata description="Operating workbook: 18-stratum AI stack, five framework lenses, seven bets, five risks, five cruxes, living tracker, and the rituals to keep them current."

# Verify build
if [[ -f "$OUTPUT" ]]; then
    SIZE=$(du -h "$OUTPUT" | awk '{print $1}')
    echo "OK: $OUTPUT built ($SIZE)"
    echo "    Open with: open '$OUTPUT'  (macOS Books) or your EPUB reader of choice."
else
    echo "ERROR: build failed — $OUTPUT not produced" >&2
    exit 1
fi
