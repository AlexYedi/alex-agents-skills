#!/usr/bin/env bash
# Build AGENTS_GTM_MASTER.epub from chapters/*.md + plates/*.svg
# Run from the agents-gtm-v2/ directory: bash build_epub.sh
# (For the playbook EPUB, run bash playbook/build_playbook_epub.sh — separate artifact)

set -euo pipefail

cd "$(dirname "$0")"

OUTPUT="AGENTS_GTM_MASTER.epub"

CHAPTERS=(
    "chapters/_title.md"
    "chapters/00_frame.md"
    "chapters/01_cell_matrix.md"
    "chapters/02_frameworks.md"
    "chapters/03_bets_risks_cruxes.md"
    "chapters/04_tracker.md"
    "chapters/05_rituals.md"
    "chapters/06_appendix.md"
)

for ch in "${CHAPTERS[@]}"; do
    if [[ ! -f "$ch" ]]; then
        echo "ERROR: missing chapter $ch" >&2
        exit 1
    fi
done

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
    --metadata title="AI Agents × GTM Master" \
    --metadata subtitle="Volume IV · Cell-resolution" \
    --metadata author="Alex Yedi" \
    --metadata date="$(date +%Y-%m-%d)" \
    --metadata lang="en-US" \
    --metadata description="Volume IV: 156-cell agent × GTM matrix, refreshed bets, agent-specific procurement rubric, sub-tracker feeding V1 + V3."

if [[ -f "$OUTPUT" ]]; then
    SIZE=$(du -h "$OUTPUT" | awk '{print $1}')
    echo "OK: $OUTPUT built ($SIZE)"
    echo "    Open with: open '$OUTPUT'"
    echo "    Companion: AI_VENDOR_PROCUREMENT_PLAYBOOK.epub (built separately via playbook/build_playbook_epub.sh)"
else
    echo "ERROR: build failed" >&2
    exit 1
fi
