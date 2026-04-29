# Pro Git — Additional Expert Notes

> Best practices, advice, and worked patterns from *Pro Git* (Chacon & Straub) that
> are too detailed for the action-focused skill files but worth keeping accessible.

---

## About the Authors

**Scott Chacon** — Co-founder of GitHub. Former CIO of GitHub. Chacon wrote
the original *Pro Git* (1st edition, 2009) and grew it into the canonical Git
reference. His perspective is grounded in operating Git at scale (GitHub) and
teaching Git to many thousands of newcomers.

**Ben Straub** — Co-author of the 2nd edition (2014) and current maintainers'
edition. Long-time Git consultant and developer educator. Straub focuses on
the developer-experience side: making the data model legible, making advanced
techniques approachable.

**Voice characteristics:**
- Mental-model-first. Both authors lead with *why* before *how*.
- Iterative reveal. Chapter 1 introduces concepts again, deeper, in Chapter 7.
- Pragmatic. They acknowledge anti-patterns ("you'll do this; don't") without moralizing.
- Hardware-aware. They cite the SHA-1 design and packfiles to ground abstractions.
- The book is open-source and updates with Git itself. The advice ages well because the model is stable.

---

## Foundational Mindset Shifts

Before any commands make sense, four shifts must happen:

### 1. Snapshots, not deltas

Most VCS users come from a "track changes" model. Git's data model is "store
the state of the project at this moment." Once this clicks, branching and
merging stop feeling weird. The merge base is automatic. Branches are pointers.
Reverts are just pointing at an earlier snapshot.

### 2. Local-first

`git log`, `git diff`, `git checkout`, `git commit` — none of these touch the
network. Coming from CVS / SVN / Perforce, this feels uncanny. The implication:
work fluently offline, in flight, on bad WiFi.

### 3. The reflog is your safety net

Every move HEAD makes is logged for ~90 days. Almost nothing is truly lost.
Knowing this changes risk tolerance — try the destructive command, then recover
if it didn't do what you wanted.

### 4. Public commits are immutable

Once a commit has been seen by another repository, treat it as fixed. If you
want to undo, write a new commit (`revert`). Never rewrite. This single rule
prevents 90% of "Git destroyed my team's work" stories.

---

## Best Practices, Organized by Topic

### Getting started on a new machine

1. Identity: `user.name`, `user.email`. Without these, Git refuses to commit.
2. Editor: `core.editor`. Pick one you'll be happy in for commit messages and rebase TODOs.
3. Default branch: `init.defaultBranch=main` (or your team standard).
4. Pull strategy: `pull.rebase=true|false|only`. Set explicitly.
5. Credential helper: `credential.helper=osxkeychain` (macOS), `manager-core` (Windows), `cache` (Linux).
6. Color: `color.ui=auto`. Default in modern Git, but verify.

### Repository hygiene

- Top-level `.gitignore` for language/framework files; keep it tight.
- Per-developer `.gitignore_global` for IDE files (e.g., `.vscode/`, `.idea/`).
- One CONTRIBUTING.md describing branching, message conventions, PR expectations.
- `.gitattributes` for line endings (`* text=auto eol=lf`) and binary file flags.
- Use Git LFS for large binary files; don't put video, large images, or compiled artifacts in plain Git.

### Commit hygiene

- One logical change per commit. If "and" appears in the subject line, you probably should split.
- Subject in imperative mood, max 50 chars. Body wraps at 72.
- Reference issues by URL (`Fixes: https://github.com/.../issues/42`) — readable in any tool.
- Use `Co-authored-by:` footers for pair-programmed commits. GitHub renders both authors.
- Sign commits (`commit.gpgsign=true` or `gpg.format=ssh` with an SSH signing key). Increasingly expected by serious projects.

### Branch hygiene

- Delete merged branches promptly (or auto-delete on PR merge).
- Keep `main` deployable. Never push directly to `main` — branch protection enforces this.
- Topic branches: short-lived (days, not weeks). For longer work, use feature flags + small merges to `main`.
- Tags for releases (`v1.2.3`), annotated (`-a`) with a message — they survive in `git log`.

### Workflow choice

- Solo project: GitHub Flow (still useful — branches per change keep history clean).
- Small team: GitHub Flow + branch protection + 1 reviewer required.
- Open source: Integration-Manager workflow (PR-based contribution).
- Hierarchical mega-project: Dictator-Lieutenants. You probably aren't this team.
- Avoid git-flow's `develop`/`release`/`hotfix` branches unless you have a real release-branch reason. For most product teams, GitHub Flow is sufficient and simpler.

### Pull request hygiene

- One PR per logical change. Don't bundle.
- PR description: what, why, how to test. Link to the issue.
- Prefer fixup-commits during review (don't force-push every revision). Squash on merge if your team's policy.
- After approval, the merger is responsible for choosing merge / squash / rebase. Be consistent at the team level.

### Conflict resolution

- `git mergetool` if you've configured one (vimdiff, kdiff3, VS Code, etc.).
- `git checkout --ours <file>` / `--theirs <file>` to take one side wholesale.
- `rerere` for repeating conflicts in long-lived branches.
- For 3-way merge clarity: `git config merge.conflictStyle diff3` shows the common ancestor block. Hugely helpful.

---

## Specific Advice with Rationale

### Always `git fetch` before `git push`

The push will fail anyway if the remote has changes you don't have locally.
Fetching first makes the divergence visible — you decide whether to merge or
rebase. Pushing first then handling the rejection is a worse experience.

### Use `git switch` and `git restore` over `git checkout`

`git checkout` is overloaded — it switches branches, restores files, and
detaches HEAD. The newer `git switch` and `git restore` (Git 2.23+) split
those responsibilities. Use them; the intent is clearer.

### Configure `pull.rebase` explicitly

Modern Git nags about this. Picking a default ends the nagging:
- `pull.rebase=true` — clean linear history, but requires the team to understand rebase
- `pull.rebase=false` — merge by default; safer for teams not yet rebase-fluent
- `pull.rebase=only` — fast-forward only; refuses to create a merge commit. Forces you to rebase explicitly.

### Use `--force-with-lease`, never raw `--force`

`--force-with-lease` checks that the upstream is what you last saw. If a
colleague pushed in the meantime, the lease fails — you're protected from
silently overwriting their work. Configure as default:

```bash
git config --global alias.pushf "push --force-with-lease"
```

Then `git pushf` does the right thing every time.

### Configure `merge.conflictStyle=diff3`

The default merge conflict shows your version and their version. `diff3` adds
the common ancestor. This is dramatically more useful for understanding
*why* a conflict happened.

### Sign commits with SSH keys (Git 2.34+)

GPG signing is fragile (key management, expiration, OS-specific tooling).
SSH signing reuses the key you already use to authenticate. GitHub, GitLab,
and others accept it. Configure:

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

### Never trust `git stash` for long-term storage

Stashes decay. A 3-week-old stash is forgotten. If work is worth keeping,
make a branch (`git stash branch <name>`).

### `git log --oneline --graph --decorate --all` is the cheat code

Shows every branch, the merge graph, where HEAD and remotes are. Alias it.
This is the single most useful read-only Git command.

```bash
git config --global alias.lg "log --oneline --graph --decorate --all"
```

### When confused, `git reflog` first

Before reaching for backup, before panicking — `git reflog`. 90 days of HEAD
history. The thing you "lost" is almost always there.

---

## Worked Examples

### Recovering from a botched rebase

```bash
# Started a rebase, resolved conflicts, but the result is wrong.
# You haven't pushed yet.

git reflog
# 1a2b3c HEAD@{0}: rebase finished (this is the bad state)
# 4d5e6f HEAD@{1}: rebase: replaying conflict
# 7g8h9i HEAD@{2}: rebase: starting
# 0j1k2l HEAD@{3}: checkout: moving from main to feature/x
# m3n4o5 HEAD@{4}: commit: last good commit before rebase

git reset --hard m3n4o5         # back to before the rebase
# Working tree is restored to that snapshot.
# Reflog still has m3n4o5 even after the reset; if THIS reset is wrong,
# you can reset --hard to it.
```

### Cherry-picking a fix from main into a release branch

```bash
git checkout release/v2.1
git cherry-pick <sha-of-fix-on-main>
# Conflicts? Resolve, git add, git cherry-pick --continue.
git push origin release/v2.1
```

### Splitting a 200-line "fix" into 3 logical commits

```bash
# On your branch, the last commit does too much.
git reset HEAD^                  # un-commit, keep working tree
git status                       # see all the changes spread across files
git add -p file1.py              # stage hunks for change A
git add file2.py                 # all of file2 is change A
git commit -m "Change A: descriptive subject"

git add -p file1.py              # remaining hunks (change B)
git commit -m "Change B: descriptive subject"

git add file3.py                 # change C
git commit -m "Change C: descriptive subject"
```

### Bisecting an automated regression

```bash
git bisect start
git bisect bad HEAD              # current is broken
git bisect good v1.4.0           # this version was fine
git bisect run pytest tests/test_login.py::test_oauth_redirect
# Git checks out commits, runs the test on each, converges.
# Output: <sha> is the first bad commit
git bisect reset
```

5 minutes of setup → first-bad-commit identified across 80 commits in a few seconds of CPU.

### Email-patch contribution to a kernel-style project

```bash
# On your topic branch:
git rebase -i origin/main         # clean it up first
git format-patch origin/main      # produces 0001-…patch, 0002-…patch
# Review the patches; they include subject + body from your commits.

git send-email --to=upstream@list.example.org --cc=maintainer@example.org *.patch
# Or use git imap-send if SMTP is unavailable.
```

The maintainer applies with `git am *.patch` and your authorship is preserved.

---

## Anti-Patterns Deeper Than the Skill Files

### Treating `master`/`main` as a personal branch

Direct pushes. Force-pushes. Amend on `main`. Each of these has nuked teams.
Branch protection is the technical fix; team education is the cultural fix.

### Cargo-culting git-flow

Many teams adopted git-flow (Vincent Driessen's blog post from 2010) without
needing release branches. The result: ceremonial complexity for no gain.
Adopt the simplest workflow that fits your release cadence. For continuous
delivery, GitHub Flow is sufficient.

### Squashing everything to one commit per PR, always

Squash-merge is great when your topic branch was messy. But for a logical
series of 4 atomic commits that each compile and test, squashing erases the
detail. Some teams ship merge commits to preserve series; some squash. Pick
one and document it.

### Reaching for `--force` instinctively

Almost every situation where you want `--force` is solvable with
`--force-with-lease`. Train the muscle memory.

### Using submodules for everything that's "shared"

Submodules are slow, awkward, and rot. Pin a dependency via your package
manager. Use submodules only when you genuinely need a Git tree inside another
Git tree (rare).

### Long-running stashes as task management

Stashes aren't tasks. If you're parking work for a day, stash. For longer,
make a branch.

### Rebasing every PR before merging just because

If your team uses merge-commits or squash-merges on PR, the pre-merge rebase
adds nothing for the recipient. It's only useful when the topic branch's
commit history will land on `main` as-is.

### Mixing whitespace cleanup with logic changes

Reviewers can't tell what changed. Do whitespace as a separate commit (or PR)
that everyone agrees on. Many teams enforce this with a `.editorconfig` and a
pre-commit hook so whitespace is consistent automatically.

---

## Process Wisdom

### Commit early, commit often, locally

Local commits are free. Even messy. You can always `git rebase -i` to clean
them up before sharing. The worst Git failure mode is "I lost a day's work
because I hadn't committed."

### Branch for everything, even tiny changes

A topic branch for a 3-line typo fix is not overkill. It's protection: if
the change is wrong, you don't taint `main`. The cost of branching is zero;
the cost of polluting `main` is non-zero.

### Review your own diff before committing

`git diff --staged` before `git commit`. Catches accidental changes (a
debug print left in, a config tweaked while testing). Quality beats velocity
here.

### Read every conflict marker

Don't just delete `<<<<<<< HEAD` and `=======` lines mechanically. Understand
what each side did. `merge.conflictStyle=diff3` shows you the common ancestor —
use it.

### Tag your releases

Annotated tags (`git tag -a v1.0 -m "Initial release"`) survive in history.
They're how `git describe` works. They're how you `git checkout v1.0` to
reproduce a customer's environment six months later.

### Maintain a CHANGELOG.md, generated or hand-written

`git log` is for engineers. CHANGELOG.md is for users. They're different
audiences. Either commit it manually with each release, or generate from
conventional commits with a tool — but don't ask users to read git log.

---

## Career / Context Wisdom

### Git fluency is a leverage skill

Senior engineers reach for advanced Git constantly: bisecting regressions,
splitting commits before review, cherry-picking hotfixes across versions.
The 80% workflow gets you contributing. The advanced 20% multiplies your
effectiveness in everything from code review to incident response.

### Read other people's commits

`git log --author="<senior-engineer>" --reverse --since="6 months ago"` —
study how they structure commits, write messages, name branches. The best
teachers are often colleagues' commits, not blog posts.

### Contribute to an open-source project to learn distributed Git

Patches via email, fork-and-PR via GitHub, both teach the workflows by
forcing you to operate at a distance. You can't ask the maintainer to fix
your branch; you have to make it merge cleanly yourself.

### Don't optimize Git config until you know your needs

Resist the urge to adopt every dotfile someone shared. Understand what each
setting does (the Pro Git references work — read the chapter, not just the
gist). Your `.gitconfig` should reflect your workflow, not someone else's.

### Lean on the porcelain; explore the plumbing when curious

Most users only need porcelain (`git commit`, `git push`, etc.). Pro Git
Chapter 10 (Git internals) is fascinating but not required for daily work.
Read it once for the mental model, refer back when scripting.

---

## When to Apply These Practices

- Setting up a new repo or onboarding a new team → see `git-fundamentals-and-workflow`
- Choosing branching/merging strategy or PR conventions → see `git-collaboration-workflows`
- Cleaning history, recovering from mistakes, advanced merging → see `git-power-user-techniques`
- Need a framework name fast → see `frameworks.md` in this directory
- Want the consolidated single-doc view → see `complete-distillation.md`

Source: *Pro Git* (Chacon & Straub, 2nd Edition + ongoing updates).
