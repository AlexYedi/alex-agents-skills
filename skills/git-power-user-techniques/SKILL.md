---
name: git-power-user-techniques
description: >
  Apply Git's advanced techniques: interactive staging, history rewriting,
  the three-tree reset model, advanced merging strategies (recursive, ours,
  theirs, subtree, rerere), and the full revision-selection grammar (SHA,
  refs, ancestry, ranges). Use when crafting clean commits from messy work,
  rewriting local history before pushing, recovering from a tangled merge,
  selecting commits for cherry-pick / bisect / log filtering, or reasoning
  about what a `git reset` actually did. Triggers: "rewrite history", "split
  a commit", "interactive rebase", "git reset confused me", "merge
  conflicts keep recurring", "cherry-pick a range", "what does HEAD~3 mean",
  "reuse recorded resolution", "stash with patches".
---

# Git Power-User Techniques

You apply Pro Git's advanced techniques: interactive staging, history
rewriting (with the immutability rule), the **three-tree reset model**,
advanced merging strategies (including `rerere` for repeating conflicts),
and the full revision-selection grammar. These are the tools that take
Git from "I can commit" to "I can shape history precisely."

---

## When to Use This Skill

- Cleaning up a messy local branch before opening a PR
- Splitting a too-big commit into atomic logical commits
- Recovering from a botched merge or rebase (without losing work)
- Reasoning about what a specific `git reset` flag actually changed
- Cherry-picking a range of commits across branches
- Filtering `git log` to find a specific change
- Dealing with the same merge conflict appearing on every rebase

---

## The Three-Tree Model (Reset Demystified)

Every Git operation operates on three trees:

```
HEAD              →  the last commit snapshot you're on
INDEX (staging)   →  the proposed next commit
WORKING TREE      →  files actually on disk
```

`git reset` changes which trees get updated:

| Command | HEAD | Index | Working tree | Effect |
|---|---|---|---|---|
| `git reset --soft <commit>` | ✓ moves | unchanged | unchanged | Move HEAD only; staged changes preserved (good for "redo last commit") |
| `git reset [--mixed] <commit>` (default) | ✓ moves | ✓ matches HEAD | unchanged | Unstages but preserves working changes |
| `git reset --hard <commit>` | ✓ moves | ✓ matches HEAD | ✓ matches HEAD | **Destructive.** Working tree is overwritten. |

**Mental shortcut:**
- `--soft`: I want to redo the commit, keep staging
- `--mixed`: I want to redo the commit and the staging
- `--hard`: I want everything to look like that commit. Discard everything else.

**Recovery from `--hard`:** `git reflog` → find the prior HEAD → `git reset --hard <reflog-sha>`. The reflog keeps ~90 days of HEAD movements.

---

## Interactive Staging — Crafting Atomic Commits

```bash
# Hunk-by-hunk staging (the workhorse)
git add -p                  # for each hunk: y/n/s (split)/q/?/

# Top-level interactive menu (status, update, revert, add untracked, patch)
git add -i

# Stash hunks selectively
git stash --patch
git stash --keep-index      # stash unstaged, keep what's staged
git stash --include-untracked  # also stash new files
```

**Worked pattern — splitting unrelated work:**

```bash
git status                  # 5 files modified across two unrelated changes
git add -p file1.py         # stage hunks for change A only
git commit -m "Change A: descriptive subject"
git add -p file1.py         # remaining hunks (change B)
git add file2.py            # all of file2 belongs to change B
git commit -m "Change B: descriptive subject"
```

---

## History Rewriting (Local Only)

> **Hard rule:** Never rewrite history that has been pushed where others might have it.
> If you must, coordinate explicitly. `--force-with-lease`, never raw `--force`.

### `git commit --amend`

Replace the previous commit. New SHA. Useful for:
- Adding a forgotten file: `git add forgot.py && git commit --amend --no-edit`
- Fixing a typo in the message: `git commit --amend`

### Interactive rebase: the all-purpose history editor

```bash
git rebase -i HEAD~5         # edit last 5 commits
git rebase -i origin/main    # edit everything since main diverged
```

Opens an editor with one line per commit. Available actions:

| Action | Effect |
|---|---|
| `pick` | Keep as-is (default) |
| `reword` | Edit message only |
| `edit` | Stop after replaying; you can amend, then `git rebase --continue` |
| `squash` | Combine into the prior commit; keep both messages |
| `fixup` | Like squash, but discard this commit's message |
| `drop` | Delete the commit |
| `exec` | Run a shell command (e.g., `--exec "make test"` to verify each commit) |

### Splitting a commit

```bash
git rebase -i HEAD~3                    # mark target commit as 'edit'
# rebase pauses
git reset HEAD^                         # un-commit, working tree intact
git add -p && git commit                # stage + commit logical part 1
git add -p && git commit                # stage + commit logical part 2
git rebase --continue
```

### Reordering commits

In the interactive editor, swap line order. Replay applies them in new order.
Conflicts may surface — resolve with `git rebase --continue`.

### `filter-branch` / `git filter-repo`

For scrubbing secrets accidentally committed long ago, or rewriting paths.
**`filter-repo` is preferred** (third-party but recommended over `filter-branch`).

```bash
git filter-repo --path secret.txt --invert-paths   # remove file from all history
```

After running: force-push (if branch is yours) and rotate the secret regardless.

---

## Revision Selection Grammar

You can refer to a commit (or a range) in many ways:

| Form | Means |
|---|---|
| `<sha>` (full or short) | That exact commit. 7 chars usually unambiguous. |
| `HEAD` | Where you are now |
| `<branch>` | Tip of the branch |
| `<tag>` | The tagged commit |
| `HEAD~3` | 3 commits back, first parent each step |
| `HEAD^` | Same as `HEAD~1` |
| `HEAD^2` | Second parent (in a merge commit) |
| `HEAD@{2.hours.ago}` | What HEAD pointed to 2 hours ago (reflog-based) |
| `HEAD@{N}` | Reflog entry N |
| `<branch>@{upstream}` | The remote-tracking branch (often `origin/main`) |
| `master..experiment` | Commits in `experiment` not in `master` |
| `master...experiment` | Symmetric difference (commits in either, not both) |
| `:/<text>` | Most recent commit whose message starts with `<text>` |

**Practical uses:**

```bash
# Diff your branch against main
git diff main...HEAD

# Show what's about to be pushed
git log @{upstream}..HEAD

# Cherry-pick a range
git cherry-pick A^..B           # commits from A through B inclusive

# Show last week's commits by you
git log --author="$(git config user.email)" --since="1 week ago"

# Find first commit mentioning "checkout"
git log --grep=checkout --reverse | head
```

---

## Advanced Merging Strategies

### Strategy options

| Command | Behavior |
|---|---|
| `git merge feature` | Default: recursive merge. Creates a merge commit. |
| `git merge --ff-only feature` | Only merge if it's a fast-forward (no merge commit). |
| `git merge --no-ff feature` | Force a merge commit even if FF was possible (preserves topic-branch identity). |
| `git merge -s ours feature` | "Fake merge" — record the merge but discard `feature`'s changes entirely. Used for record-keeping. |
| `git merge -X ours feature` | Recursive but prefer our side on conflicts (no manual resolution). |
| `git merge -X theirs feature` | Recursive but prefer their side on conflicts. |
| `git merge --squash feature` | Squash all of `feature` into one staged change; you commit. No merge ancestry. |
| `git merge -s subtree feature` | Subtree merge — merge a project as a subdirectory of yours. |

### `rerere` — Reuse Recorded Resolution

For long-running branches, the same merge conflict can recur on every rebase
or merge cycle. `rerere` records your resolution once and reapplies it.

```bash
git config --global rerere.enabled true
# Now every conflict you resolve is remembered.
# Next time the same conflict appears: auto-resolved.
```

**Use case:** A long-running feature branch that you periodically merge `main` into. The same trio of files conflicts each time. `rerere` resolves them automatically after the first manual fix.

### Aborting and starting over

```bash
git merge --abort           # cleanly bail out of a merge in progress
git rebase --abort          # cleanly bail out of a rebase in progress
git cherry-pick --abort     # likewise

# Or, after committing the wrong merge result:
git reset --hard HEAD@{1}   # back to before the merge (HEAD@{1} = previous HEAD)
```

---

## Bisect — Binary Search for Regressions

```bash
git bisect start
git bisect bad              # current commit is broken
git bisect good v1.4        # this old version was fine
# Git checks out the midpoint
# Test, then mark:
git bisect good             # OR git bisect bad
# repeat... Git converges to the first bad commit

git bisect reset            # done; back to where you were
```

Automate with `git bisect run <command>` — exit 0 = good, non-zero = bad. Bisect runs to completion without you.

---

## Stash Patterns

```bash
git stash                       # stash everything tracked
git stash --include-untracked   # also stash new files
git stash --keep-index          # stash only unstaged (preserve staging)
git stash --patch               # interactively pick hunks to stash
git stash list
git stash show -p stash@{0}     # show patch
git stash pop                   # apply + drop top stash
git stash apply stash@{2}       # apply specific stash, keep it on the list
git stash drop stash@{0}
git stash branch <new-branch>   # turn a stash into a branch (useful if main moved)
```

---

## Principles

- **History is communication.** Clean it before sharing. Rebase locally, merge publicly.
- **Reflog is your safety net.** Almost nothing is truly lost for ~90 days. Know how to use it before you need it.
- **Atomic commits.** Each commit should compile, pass tests, and be revertible alone.
- **Use `--force-with-lease`, never raw `--force`.** Protects against overwriting unseen upstream.
- **Don't fear interactive rebase.** It's the best history editor available; the safety net (reflog) makes mistakes recoverable.
- **`rerere` for repeating conflicts.** Once you've resolved a conflict the right way, let Git do it for you next time.
- **`git bisect run`** is dramatically underused. A 5-minute setup finds bugs in 60-commit ranges in seconds.

---

## Anti-Patterns

### Force-Pushing Without `--force-with-lease`

**Looks like:** `git push --force` after rebase.

**Why it fails:** If a colleague pushed in between your fetch and your push, their work is silently lost.

**The fix:** `git push --force-with-lease`. Refuses to overwrite if the upstream isn't what you last saw.

### `git reset --hard` Without Stashing First

**Looks like:** "Let me discard everything and start over." `git reset --hard origin/main`. Working tree changes vanish.

**Why it fails:** Working-tree changes are gone. Reflog won't bring them back (it tracks HEAD, not working tree).

**The fix:** `git stash` (or `git stash -u` for untracked files) first. Reset. Then decide whether to pop the stash.

### Rebasing Public Commits

**Looks like:** `git rebase -i origin/main` followed by force-push.

**Why it fails:** If anyone has pulled, they now have orphaned commits. Trust evaporates.

**The fix:** Only rebase commits you've kept local. If you must rewrite published history, coordinate in chat first and use `--force-with-lease`.

### Long-Lived Stash

**Looks like:** `git stash` from three weeks ago. Five stashes deep. Forgot what's in them.

**Why it fails:** Stash list rots. You can't tell what each stash is, and they decay context.

**The fix:** Use stash for short-term context-switches. For longer parking, create a branch (`git stash branch <name>`).

### Merging Main Into Topic Branch Repeatedly

**Looks like:** `git merge main` into `feature/x` weekly, producing a tangle of merge commits.

**Why it fails:** Topic branch's history becomes a noise of "merge main into …" commits. Can't tell which commits are the actual feature.

**The fix:** `git rebase main` (if branch is private) or merge once just before opening the PR. Or use squash-merge so the noise dies on `main`.

---

## Decision Rules

| Situation | Action |
|---|---|
| Last commit needs a small fix | `git commit --amend` (local only) |
| Last commit needs a big fix | New commit; squash later if desired |
| Need to rewrite messages on last 5 commits | `git rebase -i HEAD~5`, mark `reword` |
| Need to split a commit | `git rebase -i`, mark `edit`, `git reset HEAD^`, re-stage in chunks |
| Need to drop a commit | `git rebase -i`, mark `drop` |
| Working tree is a mess, want to start over | `git stash` first, then `git reset --hard` |
| Lost a commit | `git reflog` → `git reset --hard <sha>` |
| Same conflict every rebase | `git config --global rerere.enabled true` |
| Bug introduced sometime in last 50 commits | `git bisect start && git bisect run <test>` |
| Want to preview merge result | `git merge --no-commit --no-ff <branch>`, inspect, `git merge --abort` |
| Cherry-pick range A..B | `git cherry-pick A^..B` (note `A^` for inclusive) |
| Pulling produces ugly merges | Set `pull.rebase=true` and use `--force-with-lease` for public branches |

---

## Worked Example: Cleaning a Messy Topic Branch

**Starting point:** 8 commits on `feature/dashboard`, including 3 "WIP" commits, a typo fix, and one commit that does two unrelated things.

**Goal:** Open a PR with 4 logical commits, each tested.

```bash
git rebase -i origin/main
# Editor opens with:
#   pick a1b2c3 Add dashboard route
#   pick d4e5f6 WIP
#   pick a7b8c9 Add dashboard tests
#   pick c1d2e3 WIP fix typos
#   pick e4f5g6 Add chart component + fix unrelated CSS bug
#   pick b7c8d9 WIP
#   pick f1e2d3 Add filters to dashboard
#   pick 2a3b4c WIP last attempt

# Edit to:
#   pick a1b2c3 Add dashboard route
#   fixup d4e5f6 WIP
#   pick a7b8c9 Add dashboard tests
#   fixup c1d2e3 WIP fix typos
#   edit e4f5g6 Add chart component + fix unrelated CSS bug
#   reword f1e2d3 Add filters to dashboard      # rename to "Add filter UI to dashboard"
#   fixup 2a3b4c WIP last attempt
#   drop  b7c8d9 WIP                            # this one was abandoned

# Save. Rebase pauses at 'edit' for the chart-component commit.
git reset HEAD^
git add -p   # stage chart-component changes
git commit -m "Add chart component to dashboard"
git add -p   # stage CSS-bug fix
git commit -m "Fix nav alignment on small screens"
git rebase --continue
# Conflicts? Resolve, git rebase --continue.
# After completion:
git push --force-with-lease
```

**Result:** Topic branch is now 4 clean commits. PR reviewers see the logical progression, not the WIP detritus.

---

## Gotchas

- **Reflog is local only.** Cloning a repo doesn't copy your reflog. If a commit is "lost" upstream, only the person who lost it locally can recover it.
- **`HEAD@{N}` is reflog position N**, not "N commits ago". `HEAD~N` is "N commits ago by graph". Different things.
- **Detached HEAD commits aren't in any branch.** They're reachable only via reflog. Create a branch (`git switch -c rescue`) to keep them.
- **Squash-merge erases the topic branch's commit ancestry from `main`'s perspective.** If you bisect on `main`, the squashed commit is one giant changeset.
- **Cherry-picking creates a new commit with a new SHA.** The original commit on the source branch is unchanged.
- **`git revert` of a merge commit needs `-m 1`** (or `-m 2`) to specify which parent to keep as mainline. Otherwise Git refuses.
- **`rerere` only triggers on identical conflicts.** A whitespace difference can defeat it. Use it as a help, not a guarantee.
- **`filter-branch` is deprecated**; use `git filter-repo`. The latter is faster, safer, and the maintainers recommend it.

---

## Further Reading

- *Pro Git* (Chacon & Straub), Chapter 7 — advanced commands, reset demystified, advanced merging
- See `git-fundamentals-and-workflow` for the underlying snapshot/SHA model
- See `git-collaboration-workflows` for the rebase-vs-merge decision in team contexts

Source: *Pro Git* (Chacon & Straub), Chapter 7 (Git Tools), section on Reset Demystified, Advanced Merging.
