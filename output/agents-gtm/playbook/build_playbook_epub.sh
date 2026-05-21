#!/usr/bin/env bash
# Build AI_VENDOR_PROCUREMENT_PLAYBOOK.epub from playbook/*.md
# Run from the playbook/ directory OR from agents-gtm-v2/: bash playbook/build_playbook_epub.sh

set -euo pipefail

cd "$(dirname "$0")/.."

OUTPUT="AI_VENDOR_PROCUREMENT_PLAYBOOK.epub"

CHAPTERS=(
    "playbook/_title.md"
    "playbook/PLAYBOOK_part_A.md"
    "playbook/PLAYBOOK_part_B.md"
    "playbook/PLAYBOOK_part_C.md"
)

for ch in "${CHAPTERS[@]}"; do
    if [[ ! -f "$ch" ]]; then
        echo "ERROR: missing chapter $ch" >&2
        exit 1
    fi
done

echo "Building $OUTPUT from ${#CHAPTERS[@]} files..."

pandoc \
    "${CHAPTERS[@]}" \
    --from markdown \
    --to epub3 \
    --output "$OUTPUT" \
    --toc \
    --toc-depth=2 \
    --split-level=1 \
    --metadata title="The AI Vendor Procurement Playbook" \
    --metadata subtitle="A reference for F1000 AI council buyers" \
    --metadata author="Alex Yedi" \
    --metadata date="$(date +%Y-%m-%d)" \
    --metadata lang="en-US"

if [[ -f "$OUTPUT" ]]; then
    SIZE=$(du -h "$OUTPUT" | awk '{print $1}')
    echo "OK: $OUTPUT built ($SIZE)"
else
    echo "ERROR: build failed" >&2
    exit 1
fi
