#!/usr/bin/env bash
# Install local git hooks for alex-agents-skills development.
# Issue: YED-35
#
# This script is opt-in. Run once per clone:
#   bash scripts/install-git-hooks.sh
#
# What it installs:
#   .git/hooks/post-commit — refreshes the user-scope plugin cache after every
#   commit by running `claude plugin update alex@alex-agents-skills` in the
#   background. Removes the "did I forget to run update?" friction.
#
# Git hooks live in .git/hooks/ which is local (not tracked). That's why this
# is a one-time setup script rather than a tracked hook file.

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
  echo "ERROR: not inside a git repository" >&2
  exit 1
}

HOOK_PATH="$REPO_ROOT/.git/hooks/post-commit"

if [ -f "$HOOK_PATH" ] && ! grep -q "alex-agents-skills auto-update" "$HOOK_PATH" 2>/dev/null; then
  echo "WARNING: a post-commit hook already exists and is not ours:"
  echo "  $HOOK_PATH"
  echo "Refusing to overwrite. Move/inspect the existing hook, then re-run." >&2
  exit 1
fi

cat > "$HOOK_PATH" <<'HOOK_EOF'
#!/usr/bin/env bash
# alex-agents-skills auto-update post-commit hook (YED-35)
# Refreshes the user-scope plugin cache so edits propagate to all sessions.
# Runs in the background, fully detached, never blocks the commit.

# Skip silently if claude CLI is not installed.
command -v claude >/dev/null 2>&1 || exit 0

LOG_FILE="${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log"

(
  {
    echo "----"
    echo "post-commit @ $(date -u +%Y-%m-%dT%H:%M:%SZ) — running claude plugin update"
    claude plugin update alex@alex-agents-skills 2>&1
  } >> "$LOG_FILE" 2>&1
) &
disown 2>/dev/null || true

exit 0
HOOK_EOF

chmod +x "$HOOK_PATH"

echo "Installed: $HOOK_PATH"
echo ""
echo "Test it:"
echo "  - Make any edit, commit, then check the log: tail \"\${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log\""
echo ""
echo "Remove it:"
echo "  rm \"$HOOK_PATH\""
