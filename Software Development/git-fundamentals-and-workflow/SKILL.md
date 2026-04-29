---
name: git-fundamentals-and-workflow
description: >
  Apply Git's foundational mental model — snapshots not deltas, three-stage
  workflow (modified → staged → committed), local-first operations, and
  content-addressable storage. Use when onboarding to Git, debugging confusing
  state, deciding what to stage vs commit, or transitioning a team from a
  centralized VCS (CVS, SVN, Perforce) to Git. Triggers: "explain Git's data
  model", "why is git showing this state", "stage vs commit confusion",
  "moving from SVN to Git", "what's HEAD really", "Git basics for new dev".
  Produces a clear mental model and the exact commands for the 80% of daily
  Git workflow.
---

# Git Fundamentals and Workflow

You apply the Pro Git foundational mental model: Git stores **snapshots, not
deltas**. Every commit is a full picture of the project tree, content-addressed
by SHA-1, and integrated through a three-stage workflow. Mastering this model
prevents 80% of the confusion that pulls developers in from CVCS backgrounds.

---

## When to Use This Skill

- Explaining Git to someone with CVS / SVN / Perforce background
- Debugging "why is Git in this state" with files appearing unexpectedly modified or staged
- Deciding what belongs in a single commit vs what should be split
- Understanding why a `git reset` or `git checkout` did what it did
- Setting up a brand-new repo with sensible defaults from day 1

---

## The Core Mental Model

### Snapshots, Not Deltas

Most VCSs (CVS, SVN, Perforce) store **changes per file** over time. Git stores
**a snapshot of every file** at every commit. Unchanged files are stored as
links to the prior identical blob — efficient, but conceptually a full picture.

**Why this matters:** branching is cheap (just a pointer to a commit), merging
is reliable (the merge base is computable from the commit graph), and history
manipulation works by rewriting pointers, not patching deltas.

### The Three Sections + Three States

```
WORKING TREE  ────add────►  STAGING AREA (Index)  ────commit────►  GIT DIRECTORY
   (files you edit)         (next commit's content)              (.git, the database)

State of any file:
  modified  =  changed in working tree, not staged
  staged    =  added to index, will be in next commit
  committed =  in the database, immutable
```

### Local-First

Almost every Git operation is local. History browsing, diffs, log searches,
branch operations — all read your local `.git`. Network only happens on
`fetch`, `pull`, `push`, `clone`. This is why Git feels orders of magnitude
faster than CVCS for everyday work.

### Content-Addressable

Every object (blob, tree, commit, tag) is keyed by a SHA-1 hash of its content.
You can't change content without the hash changing. This guarantees integrity:
the system detects corruption automatically.

---

## The 80% Daily Workflow

```bash
# Inspect state
git status                    # what's modified, staged, branch, tracking
git diff                      # working tree vs staging
git diff --staged             # staging vs last commit (alias: --cached)
git log --oneline -20         # recent history

# Stage + commit
git add <file>                # stage specific file
git add -p                    # stage hunks interactively (very useful)
git commit -m "Subject"       # commit staged
git commit --amend            # amend the last commit (LOCAL ONLY)

# Move/Compare/Discard
git restore <file>            # discard working tree changes (was: checkout --)
git restore --staged <file>   # unstage (was: reset HEAD)
git checkout <branch>         # switch branch (snapshot of working tree changes)

# Sync
git fetch                     # update remote-tracking refs only
git pull                      # fetch + merge (or rebase, see below)
git push                      # send local commits to remote
```

---

## Principles

- **Commit early, commit often, locally.** Local commits are free. Squash later if needed.
- **Stage selectively.** A commit should be one logical change. Use `git add -p` to split unrelated changes in the same file across commits.
- **Never rewrite published history.** Amending or rebasing commits already pushed forces collaborators to redo their work. Treat published commits as immutable.
- **Branches are pointers, not copies.** Creating a branch is instantaneous. There's no penalty for branching for tiny experiments.
- **Fetch before push.** Always know what's upstream before pushing. `git fetch` is cheap and catches divergence early.
- **Trust SHA-1 integrity.** Refer to commits by short SHA when describing them in PRs, issues, or chat. They're stable forever (within a repo).

---

## Anti-Patterns

### Using Git as a Backup System Only

**Looks like:** Single `master` branch, commits with messages like "WIP", "more changes". No branching. Force-push when things go wrong.

**Why it fails:** Loses Git's value. Branching is the killer feature; forcing the snapshot model into "save game" usage wastes it.

**The fix:** Even solo work benefits from topic branches. Use them.

### Mental Model Stuck on Deltas

**Looks like:** Confusion when `git checkout <branch>` makes "untracked" files appear or disappear. Treating each commit as "the changes I made" rather than "the state of the project at that moment".

**Why it fails:** Predictions about Git's behavior are wrong. Reset, checkout, and merge don't make sense.

**The fix:** Internalize that every commit is a full snapshot. The diff you see is computed; it's not what's stored.

### Big Bang Commits

**Looks like:** Days of work in a single commit. Message: "implemented feature X". Hundreds of files changed.

**Why it fails:** Bisect can't pinpoint a regression. Reviews are impossible. Reverts are all-or-nothing.

**The fix:** Atomic commits. Each commit should compile, pass tests, and be revertible independently.

### Force-Push to Shared Branches

**Looks like:** Rebasing `main` after a colleague's commits are already there, then `git push --force`.

**Why it fails:** Anyone with the old history loses their commits or has to recover via reflog. In team workflows, this is destructive.

**The fix:** Only force-push to your personal feature branches. Use `--force-with-lease` even there to prevent overwriting unseen upstream work.

### Deleting Unmerged Branches with `-D`

**Looks like:** `git branch -D feature` to "clean up", losing work that wasn't merged.

**Why it fails:** Git refuses with `-d` for a reason — the branch has unmerged commits.

**The fix:** Verify `git log <branch> --not main` first. Only use `-D` if you're certain the work is discarded.

---

## Decision Rules

| Situation | Action |
|---|---|
| Switching context to a new task | New topic branch off `main`. Don't pile work on one branch. |
| Multiple unrelated edits in one file | `git add -p` to stage hunks separately into different commits |
| Made the last commit too early | `git commit --amend` (local only) |
| Pushed a commit with a typo in the message | Don't amend — write a new commit with the fix, or accept it |
| Want to share work-in-progress | Push the topic branch; don't merge to `main` early |
| Coming from SVN/CVS background | Read Chapter 1 of Pro Git. Internalize snapshots before commands. |
| Cloning a fresh repo | Configure `user.name`, `user.email`, and `core.editor` first |
| About to run `git reset --hard` | Stash or branch first. Hard reset is unrecoverable from working tree. |
| Need to undo a public commit | `git revert <sha>` (creates inverse commit). Don't rewrite. |
| Lost a commit somehow | `git reflog`. Almost nothing is truly gone for 90 days. |

---

## Worked Example: Onboarding a Developer From SVN

**Context:** New hire used Subversion for 8 years. Confused after first day in Git.

| Day | Concept introduced | Why first |
|---|---|---|
| 1 | Three-stage workflow (working / staging / committed) | Removes the SVN "modify-then-commit" assumption |
| 1 | `git status` as primary diagnostic | Replaces `svn status`; teaches new vocabulary |
| 2 | Snapshots not deltas | Reframes the data model; everything else flows from this |
| 2 | Local-first operations | Explains why Git feels different (and faster) |
| 3 | Branching = pointer to a commit | Cheap branches make topic-branch workflow viable |
| 3 | Remote-tracking branches (`origin/main`) | Distinguishes local view from server view |
| 4 | `git add -p` to split changes | Teaches selective staging discipline |
| 5 | `git commit --amend` (local only) | First exposure to history rewriting + its constraint |
| 6 | `git pull --rebase` vs `git pull` | Where the SVN-trained dev's reflexes need updating |
| 7 | `git reflog` as the safety net | Eliminates fear of irreversible mistakes |

**Lesson:** Lead with the model, not the commands. SVN-trained devs who learn
commands first stay confused for months. The model unlocks the commands.

---

## Gotchas

- **`git checkout <file>` discarded my work!** It overwrote your working-tree changes with the staged or committed version. There's no recycle bin. Use `git restore` (Git 2.23+) which is the same operation but with a clearer name.
- **`HEAD` is not the latest commit on `main`.** It's wherever you currently are. After `git checkout <sha>`, HEAD points at that sha (detached HEAD state).
- **Detached HEAD is fine, briefly.** Inspecting an old commit is normal. Just don't make commits there without creating a branch first — they'll be reachable only from reflog.
- **`origin/main` is your local cache of what was on the server when you last fetched.** It's not live. `git fetch` updates it.
- **`git pull` is `git fetch` + `git merge`** (or rebase). Two operations. Knowing the components makes pull failures debuggable.
- **`.git/` is the entire database.** Lose `.git/`, lose everything. Back up or push regularly.
- **SHA-1 collisions are not a practical concern.** A short SHA (7 chars) is unambiguous in 99.9% of repos. Git tells you when it isn't.

---

## Initial Setup Checklist

```bash
# Identity (required for commits)
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"

# Editor (used for commit messages, rebase, etc.)
git config --global core.editor "code --wait"   # or vim, nvim, etc.

# Default branch name for new repos
git config --global init.defaultBranch main

# Pull strategy (avoid the prompt every time)
git config --global pull.rebase false   # or 'true' for rebase, 'only' for FF-only

# Useful aliases
git config --global alias.st  status
git config --global alias.lg  "log --oneline --graph --decorate"
git config --global alias.unstage "restore --staged"
```

---

## Further Reading

- *Pro Git* (Chacon & Straub), Chapters 1–2 — the canonical conceptual reference
- See `git-collaboration-workflows` skill for distributed collaboration patterns
- See `git-power-user-techniques` skill for interactive staging, history rewriting, advanced merging

Source: *Pro Git* (Chacon & Straub), Chapters 1–3.
