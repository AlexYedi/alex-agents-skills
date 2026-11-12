# Plugin evals

A regression check for the `alex` plugin, run with Claude Code's built-in eval runner (`claude plugin eval`, docs: https://code.claude.com/docs/en/plugin-evals.md).

Each case is a prompt a real session would send, plus graders:
- `fires.md` checks that the intended skill loaded (`tool_used: Skill`). In the default two-arm run (with the plugin, and without it) this is a plugin-fired indicator, not part of the score.
- `quality.md` is an LLM-judged rubric for the answer. The report shows the score with and without the plugin, so it measures what the skill adds.
- `no-skill-for-trivia` guards the other direction: an over-eager skill description that loads on a trivial question fails it.

Run it from this repo:

```bash
claude plugin eval . --trust-plugin --runs 1 --no-publish   # quick check, about 10 agent runs
claude plugin eval .                                         # full: 3 runs per case, both arms
claude plugin eval . --case cto-architect-fires              # one case
```

**Gotcha (seen 2026-11-12):** the runner refuses to start if any file in the plugin has a second hard link. A failed run keeps its sandbox in `/private/tmp/e-*`, and that sandbox hard-links the plugin's files, including old results under `evals/results/`. The next run then fails every case in about 2 seconds with "has more than one hard link". To avoid it, write results outside the repo with `--output-dir "$TMPDIR/plugin-eval" --report "$TMPDIR/plugin-eval/report.html"`. If it happens anyway, delete `evals/results/` and re-copy the linked files (`find . -type f -links +1 -not -path './.git/*'` lists them).

## First run (2026-11-12, 1 run per case, both arms, $2.19)

| Case | Skill fired? | Score with / without plugin |
|---|---|---|
| karpathy-coder-fires | yes | 1.00 / 0.00 (the skill is what made the answer pass) |
| trade-off-analysis-fires | yes | 1.00 / 1.00 |
| cto-architect-fires | **no**, despite "CTO hat on … how should I architect this" | 1.00 / 1.00 |
| pre-mortem-fires | **no**, despite "run a pre-mortem" | 1.00 / 1.00 |
| no-skill-for-trivia | no (correct) | 1.00 / 1.00 |

One run per case is a smoke signal, not a measurement. Run the full 3 before changing a skill description on the strength of it.

## Full run (2026-11-12, 3 runs per case, both arms)

| Case | Skill fired (with plugin) | Score with / without plugin |
|---|---|---|
| karpathy-coder-fires | 3 of 3 | 1.00 / 1.00 (after the grader fix below) |
| cto-architect-fires | 0 of 3 (0 of 7 across both days) | 1.00 / 1.00 |
| pre-mortem-fires | 0 of 3 | 1.00 / 1.00 |

What the traces show (`--keep-temp`, then read `out/trace.jsonl` in the kept sandbox):
- **cto-architect loses to a built-in skill.** The prompt asks for a tool that tags posts by theme, which is LLM work, so the session loads the bundled `claude-api` skill instead. Its description tells the model to read it first for anything LLM-shaped. Expect the same in real sessions whenever a build involves a model.
- **pre-mortem loads nothing.** The model writes a competent pre-mortem directly and passes the rubric without the skill.
- **Rewriting both descriptions to lead with their trigger phrases changed nothing** (0 of 3 each), so the rewrite was not shipped. Neither skill adds measurable value on these prompts; the open question is whether their extra content (Alex's stack rules, the FMEA scoring table) matters enough to invoke them explicitly.
- **The karpathy-coder grader was too strict.** All answers said "overcomplicated, revert", but the judge failed any answer that also said what to do if a second pricing rule appears later. The rubric now allows that conditional note.

Runner notes: `--case` keeps only the last value, so run one case per command. If the checkout picks up hard links you can't explain, run against a plain copy (`rsync -a --exclude .git . "$TMPDIR/plugin-copy/"`).

Add a case when a skill's description changes or a skill misfires in a real session: copy a folder, change the prompt and the skill name in `fires.md`. Results land in `evals/results/` (gitignored).
