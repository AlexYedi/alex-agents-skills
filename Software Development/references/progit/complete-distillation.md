# Pro Git — Complete Distillation

> All-encompassing single-document view of *Pro Git* (Scott Chacon & Ben Straub).
> Use this when you want everything from this book in one place — including
> what's *not* surfaced in individual skills, redundancies with existing repo
> coverage, and a recommended reading order.

---

## 1. Source Identification

- **Title:** Pro Git
- **Authors:** Scott Chacon and Ben Straub
- **Edition:** 2nd Edition (Apress, 2014) + ongoing updates as Git itself evolves
- **Source format:** Open-source book (CC BY-NC-SA 3.0). Web at git-scm.com/book.
- **Pages distilled:** ~501 (full book; index/appendix excluded from skill scope)
- **Distilled in this repo:** 2026-04-29
- **Distillation chunks:** 5 (10–100, 100–200, 200–300, 300–400, 400–501)
- **Chunks promoted to skills:** 3 (sec_10_100, sec_100_200, sec_200_300)

---

## 2. Executive Summary

*Pro Git* is the canonical reference for Git, written by GitHub's co-founder
and a long-time Git educator. The book's distinctive contribution is its
**model-first pedagogy**: rather than a command tutorial, it teaches Git's
data model (snapshots, content-addressable storage, the three-stage workflow)
first, then layers commands on top. Once the model clicks, every command is
predictable.

**Why it matters now (2026):** Git has won. Every developer encounters it.
The model in this book is unchanged from 2009 to today. Force-pushing,
rebasing, and PR workflows still trip up senior engineers because the
underlying mental model wasn't established. Pro Git remains the cure — and
its open-source status means it ages with Git itself.

---

## 3. The Big Takeaways

1. **Snapshots, not deltas.** Git stores full snapshots, not file-by-file changes. Internalizing this single fact unlocks branches, merges, resets, and reverts.

2. **Three-stage workflow.** Working tree → Index (staging) → Repository. The staging area is not optional ceremony — it's how atomic commits become possible.

3. **Local-first.** Almost every Git operation is local. History browsing, diffing, branching, committing — no network. This makes Git *feel* fast.

4. **Content-addressable integrity.** Every object is keyed by SHA-1 of its content. Tampering is detectable. Identity is automatic.

5. **The reflog is the safety net.** Almost nothing is truly lost for ~90 days. Knowing this changes risk tolerance — try the destructive command, recover via reflog if needed.

6. **Public commits are immutable.** The single rule that prevents 90% of "Git destroyed our team" stories. Once pushed and seen, treat as fixed. Use `git revert`, never `git push --force`.

7. **Branches are pointers, not copies.** Creating a branch is a pointer write. There is no penalty for branching for any reason, ever.

8. **Workflow taxonomy:** Centralized → Integration-Manager → Dictator-Lieutenants → GitHub Flow. Pick deliberately by team size, trust model, and review needs.

9. **Rebase locally, merge publicly.** Clean before sharing. Preserve integration record at the merge point.

10. **Git is plumbing + porcelain.** Daily work uses porcelain (`git commit`, `git push`). Scripts and customization use plumbing (`git hash-object`, `git update-ref`). The split is a UNIX-philosophy strength.

---

## 4. Skills Derived from This Book

| Skill | When to use it |
|---|---|
| [`git-fundamentals-and-workflow`](../../git-fundamentals-and-workflow/SKILL.md) | Onboarding to Git, debugging confusing state, transitioning a team from CVCS, reasoning about HEAD/index/working-tree |
| [`git-collaboration-workflows`](../../git-collaboration-workflows/SKILL.md) | Choosing a branching strategy, deciding rebase-vs-merge, contributing to open-source, setting team commit-message standards |
| [`git-power-user-techniques`](../../git-power-user-techniques/SKILL.md) | Cleaning history before PR, splitting commits, recovering from a botched merge, advanced merging, bisect, rerere |

---

## 5. Frameworks Index

See `frameworks.md` in this directory for full definitions. Catalog covers:

- Centralized / Integration-Manager / Dictator-Lieutenants / GitHub Flow workflows
- Three-Stage Workflow, Snapshot-Based Storage, Content-Addressable Filesystem
- Topic Branches, Tracking Branches, Remote-Tracking Branches, Detached HEAD
- Merge Workflow, Rebase Workflow, Fast-Forward, Recursive, Subtree, Squash, Rerere
- Interactive Staging, Interactive Rebase, Filter-Branch/Repo, History Rewriting
- Reset Demystified (Three-Tree Model), Reflog, Revision Selection Grammar
- Pull Request Refs, Pull Request as Iterative Patch, Email Patch Workflow
- Hooks, Submodules, Plumbing vs Porcelain

---

## 6. Best Practices Index

See `additional-experts.md` in this directory. Topics include:

- New-machine setup checklist
- Repository hygiene (.gitignore, .gitattributes, LFS, signing)
- Commit hygiene (atomic commits, message format, co-authored-by)
- Branch hygiene (deletion after merge, naming conventions, length)
- Workflow choice by team size and project type
- PR hygiene (one PR per change, fixup commits, squash policy)
- Conflict resolution (mergetool, ours/theirs, rerere, diff3 conflict style)
- Specific advice with rationale (force-with-lease, switch/restore, signing keys, etc.)
- Worked examples (rebase recovery, cherry-pick, splitting commits, bisect, email patches)

---

## 7. Decision Rules Consolidated

From all three skills, every named decision rule:

| Condition | Action |
|---|---|
| Coming from SVN/CVS | Read Pro Git Ch. 1. Internalize snapshots before commands. |
| Setting up a new repo | Configure user.name/email, default branch, pull policy first |
| Switching to a new task | New topic branch off `main` |
| Multiple unrelated edits in one file | `git add -p` to stage hunks separately |
| Need to fix the last commit | `git commit --amend` (LOCAL ONLY) |
| Rebasing your private branch | OK; use `--force-with-lease` |
| Considering rebasing a shared branch | DON'T. Use `git revert` instead. |
| `git pull` produces ugly merge commits | Set `pull.rebase=true` |
| Lost a commit | `git reflog`. Almost nothing is gone for 90 days. |
| `git reset --hard` about to destroy work | `git stash` first |
| Branch protection on `main` | Require PR + review. Block direct push. |
| Long-running feature | Feature flags + small merges. Avoid long-lived branches. |
| Cherry-pick range A..B inclusive | `git cherry-pick A^..B` |
| Same conflict every rebase | Enable `rerere` |
| Unknown bug in last 50 commits | `git bisect run <test>` |
| Need to share WIP for review | Push branch, draft PR. Don't merge to main. |
| Solo project with continuous deploy | GitHub Flow + branch protection on `main` |
| Open-source contribution | Integration-Manager (PR-based) + CONTRIBUTING.md |
| Force-pushing publicly | Coordinate first. Always `--force-with-lease`. |
| New developer onboarding | Lead with the model, not commands. |

---

## 8. Anti-Patterns Consolidated

- Using Git as a backup system only (single branch, "WIP" commits)
- Mental model stuck on deltas (confusion when checkout makes files appear/disappear)
- Big-bang commits (entire feature in one commit)
- Force-pushing to shared branches
- Force-pushing without `--force-with-lease`
- Deleting unmerged branches with `-D` without verifying
- Long-lived feature branches (weeks of integration debt)
- Pulling without knowing what's upstream
- Mixing unrelated changes in one commit
- "PR as a static patch" (force-pushing entire new branch instead of fixup commits)
- Vague subject lines ("fix bug", "WIP", "more changes")
- Treating `master`/`main` as a personal branch
- Cargo-culting git-flow when GitHub Flow suffices
- Reaching for `--force` instinctively
- Submodules for everything that's "shared"
- Long-running stashes as task management
- Rebasing every PR before merging just because
- Mixing whitespace cleanup with logic changes
- Rebasing public commits
- `git reset --hard` without stashing first
- Merging main into topic branch repeatedly (clutters history)

---

## 9. Worked Examples Pointer

| Example | Where |
|---|---|
| Onboarding a developer from SVN | `git-fundamentals-and-workflow` |
| Three-person team adopting GitHub Flow | `git-collaboration-workflows` |
| Cleaning a messy topic branch | `git-power-user-techniques` |
| Recovering from a botched rebase | `additional-experts.md` |
| Cherry-picking a fix from main into release branch | `additional-experts.md` |
| Splitting a 200-line commit into 3 logical commits | `additional-experts.md` |
| Bisecting an automated regression | `additional-experts.md` |
| Email-patch contribution to kernel-style project | `additional-experts.md` |

---

## 10. Notable Content NOT in Skill Files

These topics from Pro Git scored "skim" or "skip" during triage but are worth
knowing they exist:

### Server administration (Chapter 4)

- Setting up your own Git server (HTTP, SSH, Git protocols)
- Smart vs Dumb HTTP transport
- Hosted alternatives (GitHub, GitLab, Bitbucket, Gitea, Codeberg, etc.)
- Why most teams should not self-host (operational burden vs platform value)

**Why deferred:** Self-hosting is a niche choice in 2026. Most teams use a hosted platform. The chapter is useful if you're building a private compliance-driven environment.

### Git internals (Chapter 10)

- Object types: blob, tree, commit, tag
- The `.git/` directory layout (HEAD, refs, objects, packed-refs)
- Packfiles and delta compression on the wire
- The `git fsck` and `git gc` operations
- Refspecs and the refs namespace

**Why deferred:** Fascinating but rarely actionable. Read once if you want to understand how `git push` actually transmits data, or if you're writing a Git tool.

### Subversion bridge (`git svn`) (Chapter 9)

- Using Git as a Subversion client
- Migrating an SVN repository to Git
- Bidirectional sync caveats

**Why deferred:** Niche. Useful only if you're stuck working with an SVN server. Migration tools have largely moved on (`svn2git`, `subgit`).

### Customization (Chapter 8 in detail)

- Hook scripts (`pre-commit`, `commit-msg`, `pre-push`, `post-receive`)
- The `pre-commit` framework (Python tool, not the same as Git's pre-commit hook)
- Custom merge drivers and diff drivers (e.g., for binary or generated files)
- Attribute-based handling via `.gitattributes`

**Why deferred:** Hooks are a rabbit hole. The skill files mention them; the chapter goes deep. Read when you have a specific hook to write.

### Git in other VCSs (Chapter 9 — Mercurial, Perforce, Subversion bridges)

- `git-remote-hg` for Mercurial
- `git-p4` and Perforce Git Fusion
- Considerations migrating between systems

**Why deferred:** Most readers will never use these. Worth knowing they exist.

### Plumbing commands (Chapter 10)

- `git hash-object`, `git cat-file`, `git update-ref`, `git symbolic-ref`
- `git read-tree`, `git write-tree`, `git commit-tree`
- `git ls-files`, `git ls-tree`
- Refspecs in detail

**Why deferred:** Useful for scripting. Rare in daily work. If you're writing custom Git tooling, read this chapter carefully.

### libgit2 / JGit (Appendix B)

- Embedding Git functionality in applications
- Language bindings: Rugged (Ruby), pygit2 (Python), LibGit2Sharp (.NET), JGit (Java), go-git (Go), Dulwich (pure Python)

**Why deferred:** Highly specialized. Relevant if you're building Git tooling, IDE integrations, or platform features.

### IDE integrations (Appendix A)

- Git in Visual Studio, JetBrains IDEs, Eclipse
- GUI clients: Git Kraken, Tower, GitX, GitHub Desktop
- Shell prompt integrations (vcs_info, posh-git, oh-my-zsh's git plugin)

**Why deferred:** Tooling preference. Worth a skim if you want to explore alternatives, but most developers settle on one and stay.

---

## 11. Redundancy with Existing Repo Coverage

Mapping Pro Git topics to skills already in alex-agents-skills/:

| Topic | Existing repo coverage | Relationship |
|---|---|---|
| Iterative engineering practices (TDD, CI, CD) | `Software Development/iterative-engineering-practices/` (from *Modern Software Engineering*) | **Adjacent.** Pro Git underlies the practical "how do we do CI" — but the *why* of CI is in MSE. Read together. |
| Architecture decision making | `Software Development/architecture-characteristics-and-tradeoffs/` (from *Fundamentals of Software Architecture*) | **No overlap.** Architecture is design-level; Git is implementation-level. |
| Testing strategy | `Software Development/iterative-engineering-practices/` | **Adjacent.** Iterative practices reference Git; this skill set details the Git side. |
| Code review | Spread across `engineering:code-review` skill | **Complementary.** Code review skills assume PR mechanics; this distillation provides the mechanics. |

**Net assessment:** No direct overlap. Pro Git skills add a missing layer (version-control mechanics) underneath existing engineering practice skills.

---

## 12. Recommended Reading Order

For someone new to Git or coming from a CVCS:

1. **`git-fundamentals-and-workflow`** — establishes the model. Read this first; everything depends on it.
2. **`additional-experts.md`** sections "Foundational Mindset Shifts" and "Best Practices: Getting started on a new machine" + "Repository hygiene"
3. **`git-collaboration-workflows`** — once you can commit confidently, learn how teams use Git
4. **`additional-experts.md`** sections "Best Practices: Workflow choice" + "Pull request hygiene" + "Conflict resolution"
5. **`git-power-user-techniques`** — once you're comfortable with daily and team workflows, learn to shape history precisely
6. **`additional-experts.md`** sections "Worked Examples" (read all) + "Anti-Patterns Deeper Than Skill Files"
7. **`frameworks.md`** — refer to as needed; not for linear reading

For an experienced Git user who wants the model articulated:
1. `git-fundamentals-and-workflow`
2. `git-power-user-techniques`
3. Pro Git Chapter 7 directly, then Chapter 10

For a team setting up a new repo's policies:
1. `git-collaboration-workflows`
2. `additional-experts.md` "Workflow choice" + "Best Practices: Branch hygiene"
3. Document the chosen workflow in CONTRIBUTING.md

---

## 13. Routing Guide — When to Invoke Which Skill

| User says / asks | Invoke |
|---|---|
| "Explain Git to me" / "I'm new to Git" | `git-fundamentals-and-workflow` |
| "Why is git showing this state" / "I'm confused about HEAD" | `git-fundamentals-and-workflow` |
| "Should I rebase or merge" | `git-collaboration-workflows` |
| "What's the right branching strategy" / "Do we need git-flow" | `git-collaboration-workflows` |
| "Help me write good commit messages" | `git-collaboration-workflows` |
| "Set up branch protection / PR policy" | `git-collaboration-workflows` |
| "I need to clean up this branch before opening a PR" | `git-power-user-techniques` |
| "I want to split this commit" | `git-power-user-techniques` |
| "I lost a commit" / "git reset destroyed my work" | `git-power-user-techniques` (reflog section) |
| "Same merge conflict every rebase" | `git-power-user-techniques` (rerere) |
| "There's a regression somewhere in the last 50 commits" | `git-power-user-techniques` (bisect) |
| "Cherry-pick a range" / "What does HEAD~3 mean" | `git-power-user-techniques` (revision grammar) |

If the question is about Git AND another topic (e.g., "what testing strategy with Git"), invoke the Git skill *and* the other skill — they layer.

---

## Appendix: Distillation Notes

- **Chunks promoted to skills:** sec_10_100 (foundations), sec_100_200 (workflows), sec_200_300 (power-user techniques)
- **Chunks scored "skim":** sec_300_400 (submodules, line endings, credentials, Subversion bridge — niche)
- **Chunks scored "defer":** sec_400_501 (internals, libgit2, IDE clients — fascinating but not action-focused)

The skipped chapters aren't bad — they're either niche or descriptive. Their content is summarized in section 10 above so it's not lost.

**Distillation persona:** anthropic-skills:cto-architect (treating Git as engineering infrastructure to be designed, taught, and operated, not just used)

Source: *Pro Git* (Chacon & Straub, 2nd Edition + ongoing updates), distilled 2026-04-29.
