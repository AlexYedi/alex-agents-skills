#!/usr/bin/env bash
# Install local git hooks for alex-agents-skills development.
# Issue: YED-35
#
# This script is opt-in. Run once per clone (re-run to upgrade the hooks):
#   bash scripts/install-git-hooks.sh
#
# What it installs — the same hook body under three names, so the user-scope
# plugin tracks this repo however HEAD moves:
#   post-commit   — after you commit locally
#   post-merge    — after `git pull` / `git merge` (e.g. a PR merged on GitHub)
#   post-rewrite  — after `git pull --rebase` / `git commit --amend`
#
# Why reinstall instead of `claude plugin update`: update is a no-op unless the
# version in .claude-plugin/plugin.json changes, so ordinary skill edits never
# propagated. The hook uninstalls and reinstalls (keeping plugin data), which
# copies the repo's current state regardless of version. It skips the work when
# the last successful install (stamped in .git/) is already HEAD.
#
# Git hooks live in .git/hooks/ which is local (not tracked). That's why this
# is a one-time setup script rather than a tracked hook file.

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
  echo "ERROR: not inside a git repository" >&2
  exit 1
}

HOOKS=(post-commit post-merge post-rewrite)
MARKER="alex-agents-skills auto-update"

for h in "${HOOKS[@]}"; do
  p="$REPO_ROOT/.git/hooks/$h"
  if [ -f "$p" ] && ! grep -q "$MARKER" "$p" 2>/dev/null; then
    echo "ERROR: a $h hook already exists and is not ours:" >&2
    echo "  $p" >&2
    echo "Refusing to overwrite. Move/inspect the existing hook, then re-run." >&2
    exit 1
  fi
done

for h in "${HOOKS[@]}"; do
  p="$REPO_ROOT/.git/hooks/$h"
  cat > "$p" <<'HOOK_EOF'
#!/usr/bin/env bash
# alex-agents-skills auto-update hook (YED-35)
# Reinstalls the user-scope plugin so this repo's current state reaches every
# new session. Runs in the background, fully detached, never blocks git.

command -v claude >/dev/null 2>&1 || exit 0

PLUGIN="alex@alex-agents-skills"
HOOK_NAME="$(basename "$0")"
HEAD_SHA="$(git rev-parse HEAD 2>/dev/null)"
LOG_FILE="${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log"
LOCK_DIR="${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.lock"
# Our own record of the last commit successfully installed. The gitCommitSha
# in installed_plugins.json is not reliably updated for directory sources.
STAMP="$(git rev-parse --absolute-git-dir)/alex-plugin-installed-sha"

(
  {
    # One refresh at a time. `git commit --amend` fires post-commit AND
    # post-rewrite together; the second waits here, then sees the stamp and skips.
    got=0
    for _ in $(seq 1 60); do mkdir "$LOCK_DIR" 2>/dev/null && { got=1; break; }; sleep 2; done
    echo "----"
    echo "$HOOK_NAME $* @ $(date -u +%Y-%m-%dT%H:%M:%SZ) — HEAD ${HEAD_SHA:0:7}"
    [ "$got" = 1 ] || { echo "lock busy for 2 min — skipping"; exit 0; }
    trap 'rmdir "$LOCK_DIR" 2>/dev/null' EXIT

    installed="$(cat "$STAMP" 2>/dev/null)"

    if [ -n "$installed" ] && [ "$installed" = "$HEAD_SHA" ]; then
      echo "already at HEAD — nothing to do"
      exit 0
    fi

    echo "installed ${installed:0:7} != HEAD — reinstalling"
    claude plugin uninstall "$PLUGIN" --scope user --keep-data 2>&1
    if claude plugin install "$PLUGIN" --scope user 2>&1 \
       || { echo "install failed — retrying once"; sleep 3; claude plugin install "$PLUGIN" --scope user 2>&1; }; then
      echo "$HEAD_SHA" > "$STAMP"
    else
      rm -f "$STAMP"
      echo "!! INSTALL FAILED — plugin is NOT installed. Run: claude plugin install $PLUGIN --scope user"
      exit 1
    fi
    echo "done — restart Claude Code sessions to pick it up"
  } >> "$LOG_FILE" 2>&1
) &
disown 2>/dev/null || true

exit 0
HOOK_EOF
  chmod +x "$p"
  echo "Installed: $p"
done

echo ""
echo "Test it:"
echo "  - Commit, pull, or rebase, then check the log: tail \"\${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log\""
echo ""
echo "Remove them:"
echo "  rm \"$REPO_ROOT/.git/hooks/\"{post-commit,post-merge,post-rewrite}"
