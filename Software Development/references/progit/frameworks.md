# Pro Git — Frameworks Catalog

Catalog of every named framework, pattern, and workflow described in *Pro Git*
(Chacon & Straub). Use this as a lookup when you encounter a name in a PR
discussion, doc, or commit message and want a precise definition.

---

## Index (Alphabetical)

| Name | Section | Purpose |
|---|---|---|
| Centralized Workflow | Distributed Workflows | Single hub, all devs push/pull |
| Content-Addressable Filesystem | Internals | Storage by SHA-1 of content |
| DAG (Directed Acyclic Graph) | Internals | Underlying commit graph model |
| Delta-based Storage (legacy) | Foundations | What CVS/SVN/Perforce do; not Git |
| Detached HEAD | Branching | HEAD points at a commit, not a branch |
| Dictator-and-Lieutenants Workflow | Distributed Workflows | Hierarchical large-project model |
| Distributed Version Control (DVCS) | Foundations | Every clone is a full repo |
| Email Patch Workflow | Distributed Workflows | format-patch + send-email contribution |
| Fast-Forward Merge | Branching | Move branch pointer forward, no merge commit |
| Filter-Branch / Filter-Repo | History Rewriting | Rewrite many commits at once |
| GitHub Flow | Distributed Workflows | Branch → PR → merge → deploy |
| Hooks | Customization | Scripts triggered by Git events |
| Integration-Manager Workflow | Distributed Workflows | Maintainer pulls from contributor forks |
| Interactive Rebase | History Rewriting | Edit a series of commits |
| Interactive Staging | Daily Workflow | Stage hunks selectively |
| Merge Workflow | Branching | Combine via merge commit |
| Object Database | Internals | Blobs, trees, commits, tags by SHA |
| Packfiles | Internals | Compressed object storage |
| Plumbing vs Porcelain | Internals | Low-level vs user-facing commands |
| Pull Request as Iterative Patch | Distributed Workflows | Push fixups instead of replacing |
| Pull Request Refs | GitHub | `refs/pull/N/head` and `/merge` |
| Rebase Workflow | Branching | Replay commits onto new base |
| Recursive Merge Strategy | Advanced Merging | Default 3-way merge |
| Reflog | Recovery | Local log of HEAD movements |
| Remote-Tracking Branches | Foundations | Local cache of server state |
| Rerere (Reuse Recorded Resolution) | Advanced Merging | Auto-apply prior conflict resolutions |
| Reset Demystified (Three-Tree Model) | Internals | HEAD / Index / Working Tree |
| Revision Selection Grammar | Daily Workflow | SHA, refs, ancestry, ranges |
| Snapshot-Based Storage | Foundations | Git's data model |
| Squash Merge | Branching | Combine all topic-branch commits into one |
| Submodules | Customization | Git repos inside Git repos |
| Subtree Merge | Advanced Merging | Merge another project as subdirectory |
| Three-Stage Workflow | Foundations | Working tree → Index → Repository |
| Topic Branches Pattern | Branching | Short-lived branches per logical change |
| Tracking Branches | Foundations | Local branch with upstream link |

---

## Framework Catalog (Detailed)

### Centralized Workflow
**Origin:** CVCS pattern adapted to Git (Chapter 5).
**Structure:** All developers clone from one canonical repo, work locally, push back. First-push wins; subsequent pushers must fetch + integrate.
**When to apply:** Small co-located teams. High trust. No need for review gates.
**Cross-refs:** Contrasts with Integration-Manager and Dictator-Lieutenants.
**Caveats:** Doesn't enforce review or branch protection. Rare in modern teams; default has shifted to GitHub Flow.

### Content-Addressable Filesystem
**Origin:** Git's design (Chapter 10).
**Structure:** Storage by hash of content; same content always has the same key. Git's `.git/objects/` is a content-addressed key-value store.
**When to apply:** Always. It's how Git works under the hood. Read about it to understand why operations are fast and why integrity is automatic.
**Cross-refs:** SHA-1 hashes, Object Database, Plumbing vs Porcelain.
**Caveats:** SHA-1 (vs SHA-256) — Git is migrating to SHA-256 but most repos remain SHA-1.

### Detached HEAD
**Origin:** Git internals (Chapter 1, deeper in Chapter 7).
**Structure:** HEAD pointing directly at a commit (e.g., `HEAD → 1a2b3c4`) rather than a branch. Happens after `git checkout <sha>` or `git checkout v1.0`.
**When to apply:** Inspecting historical state. Building a release artifact from a tag.
**Cross-refs:** Reflog (commits made in detached HEAD are reachable only via reflog).
**Caveats:** Commits made in detached HEAD aren't on any branch. Create a branch (`git switch -c rescue`) before committing.

### Dictator-and-Lieutenants Workflow
**Origin:** Linus Torvalds, Linux kernel project (Chapter 5).
**Structure:** Hierarchical. Subsystem maintainers ("lieutenants") merge contributions in their area. Project lead ("dictator") merges from lieutenants. Reference repo is the dictator's tree.
**When to apply:** Very large projects with subsystem ownership and high contribution volume.
**Cross-refs:** Integration-Manager (a degenerate single-tier version).
**Caveats:** Overkill for most projects. The structure scales but adds latency.

### Distributed Version Control (DVCS)
**Origin:** Foundational concept (Chapter 1).
**Structure:** Every clone is a full repository including history. No required central server.
**When to apply:** Always; it's Git's nature.
**Cross-refs:** Local-first operations, Three-Stage Workflow.
**Caveats:** Most teams still use a central server (GitHub, GitLab, etc.) by convention. The DVCS property is what makes resilience and offline work possible.

### Fast-Forward Merge
**Origin:** Branching mechanics (Chapter 3).
**Structure:** When the merge target branch is a direct ancestor of the source, Git just moves the pointer forward — no new merge commit.
**When to apply:** Default for short topic branches. Faster, cleaner history.
**Cross-refs:** Recursive Merge, Squash Merge.
**Caveats:** Loses topic-branch identity. Use `--no-ff` if you want an explicit merge commit to mark integration.

### GitHub Flow
**Origin:** Scott Chacon's 2011 blog post; canonized in Pro Git Chapter 6.
**Structure:** (1) Branch from `main`, (2) commit, (3) PR, (4) discuss/review, (5) deploy from branch (optional), (6) merge to `main`. `main` is always deployable.
**When to apply:** Most product teams. Continuous delivery contexts.
**Cross-refs:** Topic Branches, Pull Request as Iterative Patch.
**Caveats:** Requires a culture of `main` always being deployable — feature flags or trunk-based development practices help.

### Hooks
**Origin:** Git extensibility (Chapter 8).
**Structure:** Scripts in `.git/hooks/` triggered by events: `pre-commit`, `commit-msg`, `pre-push`, `post-receive`, etc. Server-side and client-side variants.
**When to apply:** Enforcing local checks (lint, tests, message format) before commits/pushes. Server-side enforcement of policies.
**Cross-refs:** pre-commit framework (third-party but recommended for managing hooks across a team).
**Caveats:** Client-side hooks aren't shared by `git clone` — they live in `.git/`, which isn't committed. Use a tool like `pre-commit` (Python) or `husky` (Node) to install hooks consistently.

### Integration-Manager Workflow
**Origin:** Open-source contribution pattern (Chapter 5).
**Structure:** Contributor forks the canonical repo, pushes work to their fork, requests the maintainer pull from the fork. Maintainer reviews + merges.
**When to apply:** Open-source projects, internal projects with strict review gating. The default for GitHub/GitLab/Gitea/Codeberg.
**Cross-refs:** GitHub Flow (a specific implementation).
**Caveats:** Requires hosting that supports forks + PRs. For email-based projects, see Email Patch Workflow instead.

### Interactive Rebase
**Origin:** Git history-rewriting tooling (Chapter 7).
**Structure:** `git rebase -i <upstream>`. Editor opens with one line per commit. Mark lines with `pick`/`reword`/`edit`/`squash`/`fixup`/`drop`/`exec`. Commits are replayed with your edits.
**When to apply:** Cleaning a topic branch before opening a PR. Squashing WIP commits. Splitting a too-big commit. Reordering commits to improve logical flow.
**Cross-refs:** Filter-Branch (heavier-duty rewriting), Reflog (safety net).
**Caveats:** Local commits only. Never rebase published commits.

### Interactive Staging (`git add -p`)
**Origin:** Granular staging tools (Chapter 7).
**Structure:** Iterates hunks of changes. For each: `y`/`n`/`s` (split)/`q`/`?`. Lets you stage logical pieces of a file separately.
**When to apply:** Splitting unrelated changes that share a file. Crafting atomic commits. Reviewing your own work hunk-by-hunk before committing.
**Cross-refs:** `git add -i` (top-level interactive menu), `git stash --patch`.
**Caveats:** Slows you down on simple cases. Worth the time for complex commits; overkill for a one-line fix.

### Merge Workflow
**Origin:** Default Git integration model (Chapter 3).
**Structure:** `git merge <branch>`. Creates a merge commit (unless fast-forward possible) recording the integration of two histories.
**When to apply:** Default for integrating shared branches. Preserves history of when/where work was integrated.
**Cross-refs:** Rebase Workflow (alternative; linearizes history).
**Caveats:** Many merge commits make `main` history dense. Use `--first-parent` in log to filter.

### Plumbing vs Porcelain
**Origin:** UNIX philosophy applied to Git (Chapter 10).
**Structure:** Porcelain commands are user-facing (`git commit`, `git pull`). Plumbing commands are low-level scriptable primitives (`git hash-object`, `git update-ref`, `git read-tree`).
**When to apply:** Porcelain for daily work. Plumbing for scripts, custom tooling, and understanding internals.
**Cross-refs:** Hooks (often script porcelain or plumbing).
**Caveats:** Plumbing is stable across versions; porcelain output may change. For scripts, prefer plumbing.

### Pull Request as Iterative Patch
**Origin:** Modern PR-based collaboration (Chapter 6).
**Structure:** A PR is a long-lived branch + thread. You push fixup commits in response to review feedback rather than re-submitting a "v2" patch. Reviewers see the conversation linearly.
**When to apply:** Any PR-based workflow.
**Cross-refs:** Email Patch Workflow (the older, static-patch alternative).
**Caveats:** Squash-merge erases the iterative history on `main`. Some teams prefer merge-commits to preserve the conversation in `git log`.

### Pull Request Refs
**Origin:** GitHub-specific Git extension (Chapter 6).
**Structure:** PRs are exposed server-side as `refs/pull/<N>/head` (the PR branch tip) and `refs/pull/<N>/merge` (a synthetic merge with target). Fetch them locally with `git fetch origin pull/<N>/head:pr-<N>`.
**When to apply:** Reviewing or testing a PR locally without a contributor's repo as a remote.
**Cross-refs:** Integration-Manager Workflow.
**Caveats:** GitHub-specific; GitLab uses different naming (`refs/merge-requests/`).

### Rebase Workflow
**Origin:** Linear-history advocates; covered in Chapter 3.
**Structure:** `git rebase <upstream>` replays your commits onto the latest upstream tip, producing a linear history with no merge commit.
**When to apply:** Cleaning topic branches before merging. Maintaining linear history on `main` (with squash-merge or merge-rebase). Also: `git pull --rebase` to avoid noisy merge commits when pulling.
**Cross-refs:** Merge Workflow, Interactive Rebase.
**Caveats:** **Never rebase published commits.** Force-push is required after a rebase, and only safe for branches you own.

### Recursive Merge Strategy
**Origin:** Default Git merge algorithm (Chapter 7).
**Structure:** Standard 3-way merge using common ancestor + both tips. Detects conflicts at the line level. Variants: `-X ours`, `-X theirs` to auto-resolve in one direction.
**When to apply:** The default. You don't choose it explicitly.
**Cross-refs:** Subtree, Octopus (very rare), Resolve.
**Caveats:** With multiple common ancestors, recursive recurses to find a synthetic merge base. Usually invisible; can produce surprising results in pathological histories.

### Reflog
**Origin:** Git's safety net mechanism (Chapter 2 and 7).
**Structure:** Local log of every HEAD movement (commits, checkouts, resets, pulls). Stored in `.git/logs/HEAD`. Default retention 90 days for reachable commits, 30 for unreachable.
**When to apply:** Recovering "lost" commits. Diagnosing what happened during a confusing rebase or reset. Time-travel debugging (`HEAD@{2.hours.ago}`).
**Cross-refs:** Detached HEAD, Reset Demystified.
**Caveats:** Local only — clone doesn't carry your reflog. If you destroy work and don't recover within 30-90 days, it's gone.

### Remote-Tracking Branches
**Origin:** Distributed branching model (Chapter 3).
**Structure:** Local refs of the form `refs/remotes/<remote>/<branch>`, e.g., `origin/main`. They mirror the server's branches as of your last fetch. Read-only locally — you can't `git checkout origin/main` and commit; you'd be in detached HEAD.
**When to apply:** Comparing local work to upstream. `git log HEAD..origin/main` shows what's about to be pulled in.
**Cross-refs:** Tracking Branches (a local branch with an upstream link).
**Caveats:** They aren't live — they update on `git fetch`. Don't confuse "out of date locally" with "the branch was deleted upstream."

### Rerere (Reuse Recorded Resolution)
**Origin:** Conflict-resolution caching (Chapter 7).
**Structure:** When enabled, Git records how you resolved a conflict. When the same conflict appears again (e.g., on subsequent rebases), Git auto-applies the prior resolution.
**When to apply:** Long-running branches that periodically pull `main` and hit the same conflicts each time.
**Cross-refs:** Advanced Merging Strategies.
**Caveats:** Only triggers on identical conflicts. Whitespace differences defeat it. Treat as a help, not a guarantee.

### Reset Demystified (Three-Tree Model)
**Origin:** Pro Git Chapter 7 (the most-cited section in the book).
**Structure:** HEAD (last commit) / Index (staging) / Working Tree (files on disk). `git reset` flags select which trees to update:
- `--soft` → HEAD only
- `--mixed` → HEAD + Index (default)
- `--hard` → HEAD + Index + Working Tree (destructive)
**When to apply:** Any time you're confused about what `git reset` will do.
**Cross-refs:** Reflog (recovery from `--hard`).
**Caveats:** Working tree changes destroyed by `--hard` aren't in the reflog. Stash first.

### Revision Selection Grammar
**Origin:** Git's expressive ref language (Chapter 7).
**Structure:**
- `<sha>` — full or abbreviated
- `HEAD~N`, `HEAD^`, `HEAD^N` — ancestry
- `HEAD@{N}`, `HEAD@{2.hours.ago}` — reflog
- `<branch>@{upstream}` — tracked branch
- `A..B`, `A...B` — ranges
- `:/<text>` — most recent message starting with text
**When to apply:** Cherry-picking, log filtering, comparing branches, diff selection.
**Cross-refs:** Revision walking under the hood.
**Caveats:** `HEAD~3` (graph distance) ≠ `HEAD@{3}` (reflog position). Two different concepts.

### Snapshot-Based Storage
**Origin:** Git's foundational data model (Chapter 1).
**Structure:** Each commit is a tree object pointing at blobs (file contents). Unchanged files reference the same blob; only changes write new blobs. Conceptually a snapshot; physically deduplicated.
**When to apply:** Always. Internalize this before any commands make sense.
**Cross-refs:** Content-Addressable Filesystem, Object Database.
**Caveats:** Different from CVS/SVN/Perforce delta-based storage. Cargo-culting CVCS habits leads to confusion.

### Submodules
**Origin:** Git's mechanism for nested repositories (Chapter 7).
**Structure:** A pointer to a specific commit in another repository, recorded in `.gitmodules`. The submodule's content lives in a subdirectory but is its own repo.
**When to apply:** Genuinely needing another repository's history embedded — e.g., a vendor library with its own version history that you want to track at the commit level.
**Cross-refs:** Subtree Merge (an alternative).
**Caveats:** Submodules are awkward — they require explicit init/update, can detach HEAD silently, and confuse newcomers. Prefer package managers when possible.

### Subtree Merge
**Origin:** Merging projects as subdirectories (Chapter 7).
**Structure:** `git merge -s subtree --allow-unrelated-histories <other-repo>` — merges another project into a subdirectory of yours, preserving combined history.
**When to apply:** Combining two repos into one. Embedding an external library you'll modify.
**Cross-refs:** Submodules (alternative; pointer-based instead of merged).
**Caveats:** Pulling updates from upstream requires `git subtree pull` — non-obvious. Many teams find it more confusing than submodules.

### Three-Stage Workflow
**Origin:** Git's central daily-use model (Chapter 1).
**Structure:** Working Tree → Staging Area (Index) → Repository. Files are modified, then staged (`git add`), then committed (`git commit`).
**When to apply:** Every commit. The discipline of staging selectively is what makes atomic commits possible.
**Cross-refs:** Interactive Staging (`git add -p`).
**Caveats:** Staging adds a step beyond CVS/SVN's "modify then commit" — easy to skip with `git commit -a` but you lose selectivity.

### Topic Branches Pattern
**Origin:** Branching best practice (Chapter 3).
**Structure:** Short-lived branch per logical change, named descriptively (`feature/login-redirect`, `fix/null-pointer-in-checkout`). Created off a stable base (`main`), merged back when complete.
**When to apply:** Every change. Even one-line fixes deserve their own branch.
**Cross-refs:** GitHub Flow (canonical container for topic branches).
**Caveats:** Long-lived topic branches accumulate integration debt. Aim for days, not weeks.

### Tracking Branches
**Origin:** Local-to-remote relationship (Chapter 3).
**Structure:** A local branch with an explicit upstream (`branch.<name>.remote` and `branch.<name>.merge`). `git status` shows ahead/behind counts. Created via `git checkout -b feature origin/feature` or `--track`.
**When to apply:** Any branch you intend to sync with a remote.
**Cross-refs:** Remote-Tracking Branches.
**Caveats:** Not the same thing as remote-tracking branches. The tracking branch is local; the remote-tracking branch is the local cache of the server.

---

## Cross-Reference Map

```
                           SNAPSHOT-BASED STORAGE
                                    │
                                    ▼
                       CONTENT-ADDRESSABLE FILESYSTEM
                                    │
                              ┌─────┴─────┐
                              │           │
                              ▼           ▼
                       OBJECT DATABASE   PACKFILES
                              │
                              ▼
                          DAG of commits
                              │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
  THREE-STAGE WORKFLOW    BRANCHES           HISTORY REWRITING
        │                      │                      │
   Working Tree            Topic Branches      Interactive Rebase
   Index (Staging)         Tracking Branches   Filter-Branch/Repo
   Repository              Remote-Tracking     git commit --amend
        │                      │                      │
        ▼                      ▼                      ▼
  INTERACTIVE STAGING     COLLABORATION         RESET DEMYSTIFIED
  (git add -p)            WORKFLOWS:            (Three-Tree Model)
                          - Centralized                │
                          - Integration-Mgr            ▼
                          - Dictator-Lts          REFLOG
                          - GitHub Flow         (safety net)


       MERGE FAMILY                              SAFETY NET
            │                                         │
   ┌────────┼─────────┐                  ┌───────────┴────────┐
   ▼        ▼         ▼                  ▼                    ▼
 Recursive  Subtree   Squash         Reflog              Detached HEAD
 (default)            Merge        (HEAD log)         (recoverable via reflog)
   │
   ├─ Fast-Forward (no merge commit)
   ├─ -X ours / -X theirs (auto-resolve)
   ├─ -s ours (fake merge)
   └─ Rerere (auto-replay resolutions)


   REVISION GRAMMAR              GITHUB INTEGRATIONS
        │                                │
   <sha>, HEAD~N                  Pull Request Refs
   HEAD@{N}                       Mentions/Notifications
   A..B, A...B                    Pull Request as Iterative Patch
   :/<text>                       (Fork → PR → review → merge)
```

---

## How to Use This Catalog

- **You see a name in a PR or commit message and want a definition** → look up here.
- **You're choosing between two related techniques** → find both in the alphabetical index, compare cross-refs.
- **You're learning Git deeply** → read Pro Git linearly. Use this catalog to refresh names later.
- **You're teaching Git** → use the index as a vocabulary checklist for what a learner should be able to define.

Source: *Pro Git* (Chacon & Straub, 2nd Edition).
