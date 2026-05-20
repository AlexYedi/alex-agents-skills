#!/usr/bin/env bash
# Build AI_AGENTS_MASTER.epub from chapters/*.md + plates/*.svg
# Run from the ai-agents-v2/ directory: bash build_epub.sh

set -euo pipefail

cd "$(dirname "$0")"

OUTPUT="AI_AGENTS_MASTER.epub"

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
    --metadata title="AI Agents Master" \
    --metadata subtitle="Volume III · Zooming the agent layer" \
    --metadata author="Alex Yedi" \
    --metadata date="$(date +%Y-%m-%d)" \
    --metadata lang="en-US" \
    --metadata description="Volume III: 14 agent sub-strata, refreshed bets, agent-specific procurement rubric, sub-tracker feeding Volume I."

if [[ -f "$OUTPUT" ]]; then
    SIZE=$(du -h "$OUTPUT" | awk '{print $1}')
    echo "OK: $OUTPUT built ($SIZE)"
    echo "    Open with: open '$OUTPUT'"
else
    echo "ERROR: build failed" >&2
    exit 1
fi
