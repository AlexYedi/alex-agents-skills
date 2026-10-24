# alex-agents-skills

This repo is the `alex` Claude Code plugin. Every repo's sessions load it from a release clone (`~/Documents/GitHub/alex-agents-skills-release`) that tracks this dev clone's `main`.

- The dev clone's checkout stays on `main`. Never switch it to another branch.
- Branch work lives in worktrees cut from `origin/main`: `git worktree add ../alex-agents-skills-wt-<name> -b alex/<name> origin/main`.
- Any skill, agent, command or manifest change goes Branch → PR → merge.
- Test a branch with `claude --plugin-dir <worktree path>`.
- After merging, `git pull` on `main` in the dev clone is what ships it (the git hooks fast-forward the release clone and reinstall the plugin).
- See `CONTRIBUTING.md` for setup and layout.
