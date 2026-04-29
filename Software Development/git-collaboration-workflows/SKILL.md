---
name: git-collaboration-workflows
description: >
  Pick and operate the right Git collaboration model — Centralized,
  Integration-Manager, Dictator-Lieutenants, or GitHub Flow — and apply the
  rebase-vs-merge rule, topic branch hygiene, and commit message standards.
  Use when setting up a new repo's branching strategy, deciding rebase vs
  merge for a team, reviewing PR practices, contributing to an open-source
  project via patches or PRs, or scaling a solo project into a team workflow.
  Triggers: "rebase or merge", "branching strategy", "GitHub Flow vs git-flow",
  "should we squash merge", "open-source contribution etiquette", "topic
  branches", "commit message conventions". Produces a chosen workflow with
  command sequences and policy guidance.
---

# Git Collaboration Workflows

You apply Pro Git's distributed workflow taxonomy: **Centralized**,
**Integration-Manager**, **Dictator-and-Lieutenants**, and **GitHub Flow**.
You pick a workflow that matches team size and trust model, enforce the
golden rebase rule, and make commit messages do their job.

---

## When to Use This Skill

- Choosing a branching strategy for a new team or project
- Debugging why merges keep producing merge-commit clutter (or, conversely, lose history)
- Setting commit-message and topic-branch conventions
- Onboarding contributors to an open-source project
- Deciding rebase vs merge as a default pull policy

---

## The Four Workflows

### 1. Centralized

```
        ┌──── Developer A ────┐
HUB ◄──►│                     │
        └──── Developer B ────┘
```

**Mechanics:** Everyone clones from one central repo, fetches, integrates locally, pushes back.

**When:** Small co-located teams. Trust is high. No need for review gates.

**Constraint:** Everyone must `fetch` and integrate before pushing — first push wins, second push is rejected until they pull.

### 2. Integration-Manager

```
Contributor ──fork──► Personal Public Repo ──pull request──► Maintainer
                                                                   │
                                                                   ▼
                                                          Canonical "Blessed" Repo
```

**Mechanics:** Contributors don't push directly. They fork (server-side or via remote), push to their fork, request the maintainer pull from there.

**When:** Open-source projects, internal projects with strong gating, anywhere "review before merge" is required. This is the GitHub/GitLab default.

### 3. Dictator-and-Lieutenants

```
Developers ──► Lieutenants ──► Benevolent Dictator ──► Reference Repo
              (one per area)
```

**Mechanics:** Hierarchical. Lieutenants merge their area's contributions; the dictator merges from lieutenants. Used for the Linux kernel.

**When:** Very large projects with subsystem maintainers. Probably not your project.

### 4. GitHub Flow (the modern default)

```
1. Branch from main
2. Add commits
3. Open Pull Request
4. Discuss, review
5. Deploy from branch (optional)
6. Merge to main → deploy main
```

**Mechanics:** Simpler than git-flow. Main is always deployable. Topic branches → PRs → merge to main.

**When:** Most product teams. Continuous delivery. No long-lived release branches needed.

---

## The Golden Rebase Rule

> **Never rebase commits that have left your local repository.**

| Situation | Rebase? | Why |
|---|---|---|
| Your local feature branch, no one else has it | YES | Cleans history before sharing |
| Your feature branch, you pushed for backup but no one else has cloned | YES (use `--force-with-lease`) | Still effectively yours |
| Your feature branch, a colleague has it pulled | NO (or coordinate) | They lose their work or get confused |
| `main` or any shared branch | NO | Catastrophic for the team |
| You see force-pushed upstream commits | `git pull --rebase` | Replays your unique work on top of their new history |

**Why rebase at all?** Linear history is easier to bisect, cherry-pick, and reason about. The history you ship to `main` is communication — clean it.

**Why merge sometimes?** Preserves the actual chronology. For long-running collaborative branches, the merge commit captures the integration moment.

---

## Rebase vs Merge — Pick Your Default

| Default | Use case | Trade-off |
|---|---|---|
| `git pull --rebase` (rebase by default) | Teams that value linear history; mostly small features merged in clean topic branches | If you forget the rule and rebase a shared branch, you cause pain |
| `git pull` (merge by default) | Larger teams; long-running feature branches; explicit merge-commits as audit trail | History becomes a "diamond" with many merge commits — harder to bisect cleanly |
| **Squash-merge on PR** (GitHub-flow-friendly) | Each PR becomes one commit on `main` | History on `main` is clean; on the topic branch you can be messy |

**Set policy at the team level**, not per-developer. Inconsistent pull policies cause divergence pain.

---

## Topic Branch Hygiene

Topic branches isolate one logical change. They're cheap. Use them.

```bash
# Off main, named for the work
git checkout main && git pull
git checkout -b feature/<short-description>
# … work, commit …
git push -u origin feature/<short-description>
# Open PR
```

**Naming conventions (pick one and stick to it):**
- `feature/`, `fix/`, `chore/`, `docs/` prefixes
- Or per-developer: `<initials>/<topic>` (e.g., `ay/checkout-flow`)
- Avoid issue-tracker IDs only (`PROJ-1234`) — unreadable in `git branch -vv`

**Pre-PR cleanup checklist:**
1. `git rebase -i origin/main` — squash WIP commits, fix typos in messages
2. Make sure the branch passes tests at every commit (use `git rebase --exec "<test cmd>"`)
3. `git push --force-with-lease` after rebasing
4. Title the PR with the eventual commit message (squash-merge friendly)

---

## Commit Message Standards

The Pro Git / kernel-style standard:

```
Subject: imperative, max 50 characters

Body explaining motivation: why this change. Contrast with the
previous behavior. Wrap at 72 characters. Reference issues by
URL or short ID, not "see PR".

Use bullets if helpful:
- Item one with a complete thought
- Item two

Footer:
Fixes: #1234
Co-authored-by: Name <email>
```

**Hard rules:**
- Subject line is **imperative mood** ("Add user logout" not "Added user logout" or "Adds user logout")
- Subject < 50 chars. If you can't, the commit is too big.
- Blank line between subject and body
- Body wraps at 72 chars (preserves readability in `git log` and email clients)

**Why this exists:** Git tools assume this format. `git log --oneline` shows the subject. `git format-patch` produces email-ready patches. `gitk` and GitHub render the body. Following the format makes your work navigable.

---

## Patch-Based Contribution (Email Workflow)

Some open-source projects (Linux kernel, Git itself) use email patches, not PRs.

```bash
# Generate patch series from your topic branch
git format-patch origin/main -o /tmp/patches

# Review (and edit message text if needed)
ls /tmp/patches
# 0001-Add-frobnicate.patch
# 0002-Frobnicate-tests.patch

# Send via configured SMTP
git send-email --to=upstream-list@example.org /tmp/patches
```

**Reverse:** to apply a series someone sent:
```bash
git am /path/to/patches/*.patch
```

---

## Principles

- **Fetch before push.** Always. Cheap, prevents surprises, clarifies divergence.
- **Topic branches for everything**, even one-line fixes. Nothing direct on `main`.
- **One logical change per commit.** A commit should be revertible without losing unrelated work.
- **Public commits are immutable.** Once pushed and seen, treat as fixed. Use revert, not rewrite.
- **Document the workflow in CONTRIBUTING.md.** Don't make contributors guess your branching policy.
- **Coordinate force-pushes.** If unavoidable, announce in chat. `--force-with-lease` always.
- **Rebase locally, merge publicly.** Clean before sharing; preserve integration record at the merge point.

---

## Anti-Patterns

### Long-Lived Feature Branches

**Looks like:** `feature/big-rewrite` lives 3 months while `main` accumulates changes. Eventual merge is a week of conflict resolution.

**Why it fails:** Integration cost is exponential in branch age. Conflicts compound silently.

**The fix:** Break the work into smaller increments. Use feature flags to ship incomplete code that's hidden until ready. Merge to `main` weekly at minimum.

### Force-Push to `main` (or any shared branch)

**Looks like:** "I rebased main to clean up, then force-pushed."

**Why it fails:** Anyone with the old `main` loses work. Reflog recovery is possible but tedious. Trust evaporates.

**The fix:** Treat `main` as append-only. Use `git revert` to undo. Educate the team that this is a hard rule.

### Pull Without Knowing What's Upstream

**Looks like:** `git pull` blindly. Surprise merge commits. Or surprise rebase replays of your local work.

**Why it fails:** You don't see what's incoming until it's already integrated.

**The fix:** `git fetch` then inspect (`git log HEAD..origin/main`). Decide merge vs rebase deliberately.

### Mixing Unrelated Changes in One Commit

**Looks like:** A commit titled "fix login bug + tweak header CSS + update README"

**Why it fails:** Can't revert one without the others. Bisect blames a hunk that's not the regression. Code review is harder.

**The fix:** `git add -p` and `git commit --interactive` to split. Three commits, one revertible each.

### "PR as a Static Patch"

**Looks like:** Open PR, get review comments, force-push entirely new branch with a "v2" name.

**Why it fails:** Loses the conversation thread. Reviewers can't see what you changed in response to feedback.

**The fix:** Push fixup commits to the same branch. After approval, optionally squash on merge.

### Subject Lines That Don't Say What

**Looks like:** "fix bug", "update", "WIP", "more changes"

**Why it fails:** `git log --oneline` is unreadable. Future you can't find anything.

**The fix:** Imperative subject naming the change. "Add CSV export to reports view" not "fix bug".

---

## Decision Rules

| Condition | Action |
|---|---|
| New repo, small team (< 10 devs), continuous delivery | GitHub Flow + squash-merge on PR |
| New repo, > 10 devs, structured release cadence | GitHub Flow with release branches off `main` for hotfixes |
| Open-source project | Integration-Manager (PR-based) + CONTRIBUTING.md |
| Linux-kernel-style large hierarchical project | Dictator-Lieutenants (don't reinvent this for your team) |
| Branch is yours, hasn't been pushed | Rebase freely to clean up |
| Branch is yours, was pushed but no one else has cloned | Rebase + `--force-with-lease` |
| Branch is yours, others have cloned | Don't rebase. Add fixup commits. Squash on merge. |
| `main` or any shared branch | Never rebase. Use `git revert` to undo. |
| Inheriting force-pushed upstream | `git pull --rebase` to replay your unique commits |
| Need to share WIP for review | Push branch, open draft PR. Don't merge to main. |
| Conflict-prone long-running feature | Merge `main` into the feature branch weekly to keep up |
| Feature is too big to ship | Feature flag + merge incomplete code to main. Long-lived branches lose. |

---

## Worked Example: A Three-Person Team Adopting GitHub Flow

**Starting point:** Three devs, one repo, everyone pushing to `main`. Frequent push rejections. No reviews.

**Steps:**

| Step | Action | Why |
|---|---|---|
| 1 | Branch protection on `main`: require PR, require 1 approval | Forces topic-branch workflow without yelling at people |
| 2 | Document branch naming: `feature/`, `fix/`, `chore/` | Consistency in `git branch` output |
| 3 | Establish commit message rules in CONTRIBUTING.md | New devs see expectations on day 1 |
| 4 | Default merge strategy: squash-merge | Linear `main` history; messy topic branches don't matter |
| 5 | Default pull policy: `git pull --rebase` | Avoid noisy merge commits when pulling main |
| 6 | Auto-delete branches after merge | Repository stays tidy |
| 7 | CI runs on every PR, blocks merge if red | Catches regressions before main |

**Result:** Three weeks in, push rejections gone. PR conversations are the norm. `git log --oneline main` is readable.

**Lesson:** Workflow is enforced by branch protection + automation, not by reminders. Make the easy path the right path.

---

## Gotchas

- **`git pull` defaults vary by version.** Recent Git asks you to set `pull.rebase`. Set it explicitly in `~/.gitconfig`.
- **Squash-merge erases the topic branch's commit history.** That's usually fine on `main`, but it means rebase work on the topic branch was for nothing — it gets squashed away. Save it for the topic branch's own log if it matters.
- **Merge commits look messy in linear views.** `git log --oneline --graph` is your friend. `git log --no-merges` filters them out.
- **`git rebase --onto X Y Z`** is the surgical form: take commits between Y and Z, replay onto X. Useful for moving work to a different base branch.
- **`git format-patch` includes from-line metadata.** Don't strip headers manually; `git am` needs them.
- **`--force-with-lease` ≠ `--force`.** Lease checks the upstream is what you saw last. If someone else pushed, you get a polite refusal instead of clobbering them.
- **`origin/HEAD` may point at the wrong default branch** after a repo renames `master` → `main`. Update with `git remote set-head origin -a`.

---

## Further Reading

- *Pro Git* (Chacon & Straub), Chapters 5–6 — distributed workflows and GitHub
- See `git-fundamentals-and-workflow` for the underlying data model
- See `git-power-user-techniques` for rebase, history rewriting, and advanced merging

Source: *Pro Git* (Chacon & Straub), Chapters 5 (Distributed Git) and 6 (GitHub).
