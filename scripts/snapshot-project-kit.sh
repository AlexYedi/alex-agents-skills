#!/usr/bin/env bash
# Snapshot a project repo's committed .claude kit into "My Projects Skills/<name>/".
# Archive copies are portable and versioned here but NOT plugin-loaded — only
# skills/ at this repo's root is auto-discovered.
#
# Usage: scripts/snapshot-project-kit.sh <project-repo-path> <archive-name>
# Re-run any time to refresh; it replaces the snapshot with the project's HEAD.
set -euo pipefail

src="${1:?project repo path}"; name="${2:?archive name}"
root="$(cd "$(dirname "$0")/.." && pwd)"
dest="$root/My Projects Skills/$name"
subdirs=(skills commands agents references hooks scripts)

sha="$(git -C "$src" rev-parse --short HEAD)"
remote="$(git -C "$src" remote get-url origin 2>/dev/null || echo 'local')"

present=()
for d in "${subdirs[@]}"; do
  [ -n "$(git -C "$src" ls-files ".claude/$d" | head -1)" ] && present+=(".claude/$d")
done
[ ${#present[@]} -gt 0 ] || { echo "no committed .claude kit in $src" >&2; exit 1; }

tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
git -C "$src" archive HEAD "${present[@]}" | tar -x -C "$tmp"

mkdir -p "$dest"
for p in "${present[@]}"; do
  d="${p#.claude/}"; rm -rf "$dest/$d"; cp -R "$tmp/$p" "$dest/$d"
done

cat > "$dest/README.md" <<MD
# $name — archived project kit (not auto-loaded)

Snapshot of the committed \`.claude/\` kit from **$remote** at commit \`$sha\` ($(date +%F)).

- **Source of truth is the project repo**, not this copy. Edit there, then refresh:
  \`scripts/snapshot-project-kit.sh <path-to-repo> $name\`
- **Not plugin-loaded.** Only \`skills/\` at the alex-agents-skills root is auto-discovered,
  so nothing here fires in Claude sessions. It exists so the kit is portable and versioned
  alongside the general skill library.
- Contents: $(printf '%s ' "${present[@]#.claude/}")
- Paths inside these files (e.g. \`.claude/references/...\`) are relative to the project repo.
MD
echo "snapshotted $remote@$sha -> My Projects Skills/$name ($(find "$dest" -type f | wc -l | tr -d ' ') files)"
