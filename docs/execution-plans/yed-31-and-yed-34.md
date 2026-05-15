# Execution plan — YED-31 (skill migration waves) + YED-34 (orphan agents/commands audit)

Drafted 2026-05-15. Paused before execution. Two related tickets that together finish the alex-agents-skills plugin-ification arc started in YED-28.

## Where we left off (state as of pause)

Shipped to main:

| Ticket | What | Plugin version after |
|---|---|---|
| YED-26 | SessionStart Linear-priorities hook | n/a (hook lives in `~/.claude/hooks/`) |
| YED-27 | Repo-touch nudge (Hook A) + v2-trigger logging (Hook B) | n/a |
| YED-28 | 15-skill MVP plugin (`alex`) installed at user scope | 0.1.0 |
| YED-29 | Promoted SessionStart + Hook A to user scope; Hook B stays at Empire State | n/a |
| YED-32 | Deleted `GTM/Marketing/intent-signal-orchestration/` (byte-identical duplicate of Growth) | 0.1.0 |
| YED-33 | 5 agents promoted to `agents/<name>.md`; manifest declares them | 0.2.0 |
| YED-35 | `scripts/install-git-hooks.sh` + working post-commit hook (auto `claude plugin update`) | 0.2.0 |

Still in backlog:
- **YED-31** — migrate the remaining ~205 skills (this plan)
- **YED-34** — audit ~50 nested `agents/` and `commands/` dirs (this plan)
- **YED-30** — canonical CLAUDE.md fragment + new-project starter kit (unblocked but not in this plan)

## Operating context to assume on resumption

- Plugin name: `alex`. Skill invocation: `alex:<name>`. Agent subagent_type: `alex:<name>`.
- Plugin manifest: `.claude-plugin/plugin.json` (skills auto-discovered from `skills/<name>/SKILL.md`; agents explicitly listed in the `agents` array).
- Plugin source-of-truth: this repo. User-scope install caches at `~/.claude/plugins/cache/alex-agents-skills/alex/<version>/`.
- Post-commit hook is live: `claude plugin update alex@alex-agents-skills` runs in background after every commit. Log at `${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log`. No manual update needed.
- Workflow pattern observed during YED-28 through YED-33: Claude commits to a branch; user opens + merges PRs (sometimes ahead of the branch's final state, so Claude should announce when a branch is "fully done" before requesting PR).

## YED-31 — Migrate remaining ~205 skills

### Pattern recap

- Plugin-discoverable: `skills/<name>/SKILL.md` at repo root. FLAT — one level deep. No nested subdirectory discovery.
- Archive: everything in domain folders (`Product/`, `Software Development/`, `GTM/`, etc.). Not plugin-loaded.
- Migration = `git mv <domain>/<skill>/ skills/<skill>/`. Preserves history.
- Umbrella skills (folders containing nested `skills/`): atomic sub-skills move out individually to plugin root; the umbrella shell (with its `agents/` and `commands/` dirs) becomes a YED-34 candidate.
- Skills with `references/` subdirs travel with the skill — the plugin loader walks the skill's own directory.

### Wave structure (5 waves, one PR each)

#### Wave 2a — Product remaining (~22 skills)

Domain folder: `Product/`. After YED-28 MVP migrated 11 Product skills, these remain:

```
ai-agent-design-patterns
ai-build-vs-buy-and-model-adaptation
ai-product-development-lifecycle
ai-product-okrs-and-metrics
behavioral-product-design
causal-decision-modeling
decision-intelligence-fundamentals
decision-simulation-and-monitoring
jtbd-fundamentals-and-interviewing
jtbd-strategy-and-organization
measuring-product-market-fit
organizational-design
outcome-driven-innovation-and-job-mapping
platform-infrastructure
platform-strategy
product-led-sales
product-operations
product-taste-intuition
```

Plus from umbrellas (still need migration):
- `product-launch-orchestration/skills/war-room-ops` (the other 2, `launch-tiering` and `risk-playbooks`, already migrated)
- `product-led-growth/skills/{in-app-messaging-kit,onboarding-blueprint,pql-framework,usage-health-scorecard}`

Umbrella shells left behind for YED-34: `product-launch-orchestration/{agents,commands}/`, `product-led-growth/{agents,commands}/`.

**Estimated effort:** ~3 hours. Low collision risk.

#### Wave 2b — Software Development (~40 skills)

Domain folder: `Software Development/`. After YED-28 MVP migrated 3, the remaining ~40 are listed in domain folder (cto-architect, karpathy-coder, iterative-engineering-practices already moved).

Notable subfolders:
- `technical-writing/skills/{api-style-guide,doc-requirements-matrix,quality-review-checklist,versioning-dashboard}` — umbrella with agents/commands shells
- All other Software Development skills are flat (no umbrellas)

**Estimated effort:** ~5 hours. Low-medium collision risk. References subdirs are heavier here (some skills have 7-15 reference files derived from "Foundations of Scalable Systems" and "Hard Parts" books).

#### Wave 2c — GTM (~80 skills) ⚠️ LARGEST

Domain folder: `GTM/`. Subdivided heavily:
- `CS_Post_Sale/` — account-management (umbrella, 4 subskills), customer-success (umbrella, 4 subskills), retention-engagement (flat)
- `Growth/` — many umbrellas (Growth Strategist, growth-experiments, intent-signal-orchestration, lead-nurture-orchestration, signal-scoring) + flat skills + cold-email/icp-research subfolders
- `Marketing/` — many umbrellas (abm-orchestration, campaign-analytics, campaign-orchestration, copywriting, customer-analytics, customer-journey-orchestration, customer-marketing, marketing-analytics, marketing-automation, social-media-marketing, social-scheduler-orchestration) + flat skills
- `RevOps/` — revenue-analytics (umbrella), revenue-forecasting-pipeline (umbrella) + 3 flat skills
- `Sales/` — building-sales-team (umbrella with weird structure: has SKILL.md AND subfolders), enterprise-sales (umbrella), sales-coaching (umbrella), sales-enablement (umbrella), sales-intelligence (umbrella), Sales-Methodology-Skills (umbrella with 3 named subskills), sales-operations (umbrella), sales-pipeline (umbrella), sales-compensation (flat), sales-qualification (flat)
- `partnership-bd/` (flat)

Recommended sub-batching: ship as **5 sub-PRs** (one per GTM subdomain — CS_Post_Sale, Growth, Marketing, RevOps, Sales+partnership-bd) rather than one mega-PR. Reduces blast radius.

**Collision watchpoints:** name collisions likely between Growth and Marketing (the intent-signal-orchestration case was already cleaned up in YED-32, but check others like `signal-intel`, `personalization`, `segmentation-framework`). Pre-flight script: enumerate `find GTM -path '*/skills/*/SKILL.md' -printf '%h\n' | xargs basename | sort | uniq -d`.

**Estimated effort:** ~6-8 hours total, split across the sub-batches.

#### Wave 2d — Data Engineering (~20 skills)

Domain folder: `Data Engineering/`. Structure:
- `architecture/` — 6 flat skills
- `databases/` — `database-designer` (flat)
- `governance-and-quality/` — 2 flat skills
- `pipelines/analytics-pipeline-orchestration/skills/{instrumentation,quality-gates,visualization-patterns}` (umbrella)
- `pipelines/enrichment-pipeline/skills/{firmographic-analysis,identity-resolution,provider-scorecard,signal-taxonomy,validation-rulebook,waterfall-blueprint}` (umbrella)
- `retrieval/` — 4 flat skills
- `playbooks/` — reference docs (NOT skills, leave alone)
- `references/` — reference docs (NOT skills, leave alone)

Plus a `data-quality-auditor` skill in `governance-and-quality/` has its own `.claude-plugin/plugin.json` (weird — leftover from an earlier attempt to plugin-ify it standalone). Need to decide: keep as nested plugin or absorb into the main `alex` plugin. Recommend: absorb, delete the nested `.claude-plugin/`.

**Estimated effort:** ~2 hours.

#### Wave 2e — Long tail (~25 skills across 3 domains)

- `Evals, Harness, & Observability/` — 8 flat skills (`ai-evals`, `eval-harness`, `evaluating-new-technology`, `evaluating-trade-offs`, `managing-tech-debt`, `observability-designer`, `tdd-workflow`, `usability-testing`)
- `Organizational Leadership/` — 8 flat skills (`cross-functional-collaboration`, `delegating-work`, `organizational-transformation`, `post-mortems-retrospectives`, `problem-definition`, `running-decision-processes`, `setting-okrs-goals`, `stakeholder-alignment`)
- `Research, Financial Modeling, and Market Analysis/` — `statistical-analyst` (flat) + 4 business-intelligence subskills + 4 competitive-intelligence subskills + 4 market-research subskills + `Content Transformations/book-distiller/` (skill with multi-stage pipeline)

Note: book-distiller has 3 `*-prompt.md` files inside its `references/` — these are skill-internal reference files, NOT agent prompts. Leave them in place.

**Estimated effort:** ~2-3 hours.

### Per-wave checklist (ritual)

```
1. Pre-flight collision audit:
   find skills -maxdepth 1 -mindepth 1 -type d | xargs -n1 basename | sort > /tmp/existing-skills.txt
   <enumerate candidate names from this wave> | sort > /tmp/candidate-skills.txt
   comm -12 /tmp/existing-skills.txt /tmp/candidate-skills.txt   # collisions
2. For each collision: diff the two files. If byte-identical → dedupe. If distinct → decide prefix.
3. Branch: alex/yed-31-wave-{2a|2b|2c-{cs|growth|marketing|revops|sales}|2d|2e}
4. git mv each atomic skill folder. Use `git mv` not cp+rm; preserves history.
5. For any cross-references in OTHER SKILL.md files pointing to OLD paths, update them.
   grep -rl "<old-path>" --include="*.md"
6. Validate locally: claude --plugin-dir . --print "List all alex:* skills, count only."
7. Commit. Post-commit hook will fire claude plugin update.
8. Push, open PR, announce "fully done" before requesting merge.
9. After merge: smoke-test in a real session (fresh `claude` in Empire State or gtm-os).
```

### Risks + mitigations

- **Hidden collisions** — mitigation: the pre-flight `comm` step in the checklist.
- **Cross-reference breakage** — mitigation: grep step before mv.
- **References subdirs bloat plugin context** — currently each skill's SKILL.md is what loads into context; references are read on demand. So bloat is bounded. But if a skill has 15 ref files, consider whether they should live in a non-loaded `docs/` instead. Decide per skill; default is "keep them with the skill."
- **Umbrella SKILL.md (some umbrellas have one)** — these are orchestrator skills that reference their sub-skills. After unwinding, the umbrella SKILL.md may have broken `skills/<sub>/SKILL.md` references. Two options: (a) move the umbrella SKILL.md to `skills/<umbrella-name>/SKILL.md` and update its internal refs to point to new flat locations; (b) absorb umbrella SKILL.md content into a top-level `references/<umbrella-name>.md` and don't migrate it as a skill. Pick per-umbrella in the wave.

### Rollback strategy

Per-wave PRs make rollback granular. If a wave produces regressions:
1. `git revert` the merge commit on main.
2. Run `claude plugin update alex@alex-agents-skills` — cache returns to prior version.
3. Re-do the wave from a clean branch.

---

## YED-34 — Audit ~50 nested `agents/` and `commands/` dirs

### Trigger

After YED-31 migrates the atomic skills out of umbrellas, the umbrella shells remain — typically:
```
<old-domain>/<umbrella>/
├── agents/<name>.md     (orphan content — not plugin-loaded)
├── commands/<name>.md   (orphan content — not plugin-loaded)
└── (skills/ subdir is now empty or removed after wave migration)
```

Plus the known orphan: `GTM/Sales/sales-operations/sales-strategy-consultant-prompt.md`.

### Inventory step (do this first, before any decisions)

Script to enumerate everything:
```bash
find . -type d \( -name agents -o -name commands \) \
  -not -path "./.git/*" \
  -not -path "./agents" \
  -not -path "./commands" \
  -not -path "./skills/*/references/*" \
  | while read dir; do
      echo "=== $dir ==="
      ls "$dir"
    done > /tmp/yed-34-inventory.txt
```

Produces a table to drive decisions per dir.

### Decision framework (per nested dir)

Four categories, applied per file inside each dir:

- **(a) Promote to plugin root** — the agent/command is genuinely useful and cross-project. Move to `agents/<umbrella>-<name>.md` or `commands/<umbrella>-<name>.md`. Use umbrella prefix to avoid collisions. List in `plugin.json`.
- **(b) Drop** — content is stale, redundant with an existing skill, or trial-balloon work that didn't take. `git rm`.
- **(c) Fold into SKILL.md** — agent/command content is really part of one skill's instructions. Merge it into that skill's SKILL.md body, then `git rm` the original.
- **(d) Promote to skill** — the file is actually a skill mislabeled as agent/command. Convert frontmatter, move to `skills/<name>/SKILL.md`.

### Orphan tracker

| File | Category | Reasoning |
|---|---|---|
| `GTM/Sales/sales-operations/sales-strategy-consultant-prompt.md` | TBD on audit | Discovered in YED-33. Likely (a) promote as `agents/sales-strategy-consultant.md`, but defer until full inventory. |

### Ordering vs YED-31

**Recommended: YED-31 first, then YED-34.** Reasoning:
1. YED-31 dissolves the umbrella concept by moving atomic skills out. What remains in `<old-domain>/<umbrella>/` is purely orphan content.
2. YED-34 then has a smaller, cleaner audit scope: just the orphan files, no entangled active skills.
3. If we interleaved (per-wave YED-34), we'd be making editorial decisions about content that we haven't yet seen in its final flat context.

### Effort

~3-5 hours after YED-31 completes. The audit is bounded; most decisions will be (b) drop or (c) fold, with (a) promote reserved for the ~5-10 genuinely valuable ones.

### Linear sub-structure

YED-34 stays single-issue. The work is one focused audit pass, not a multi-wave migration.

---

## Linear ticket organization (proposed)

Optional refinement to make progress trackable in Linear:

- **YED-31** stays as parent. Update its description to point to this plan.
- Create 5 sub-issues blocking YED-31:
  - YED-31a Wave 2a — Product remaining
  - YED-31b Wave 2b — Software Development
  - YED-31c Wave 2c — GTM (further split into 5 sub-PRs in execution, but one Linear issue)
  - YED-31d Wave 2d — Data Engineering
  - YED-31e Wave 2e — Long tail
- **YED-34** stays as-is, blocked by YED-31.

Alternative: keep YED-31 single-issue and use the in-issue checklist. Less Linear ceremony, more conversation context in one ticket.

## Open decisions to resolve before resumption

1. **Linear sub-tickets for YED-31 waves — yes or no?** (Affects how progress is reported.)
2. **GTM wave priority order.** Default is alphabetical (CS → Growth → Marketing → RevOps → Sales). If Sales is more relevant to active work (job-search), swap to Sales-first.
3. **References-subdir bloat policy.** Skills with 7+ reference files: keep all with skill, or selectively cull? Suggested default: keep all unless skill body explicitly says they're outdated.
4. **Umbrella SKILL.md handling.** Some umbrellas (e.g., `building-sales-team`, `cto-architect`-pre-migration-pattern) have their own SKILL.md plus a nested `skills/` directory. Default: promote umbrella SKILL.md as a top-level skill, then promote its sub-skills also as top-level. Two skills come out of one umbrella.
5. **Nested `data-quality-auditor` plugin manifest** (in `Data Engineering/governance-and-quality/data-quality-auditor/.claude-plugin/plugin.json`). Absorb into main `alex` plugin (recommended) or surface as a question.
6. **YED-34 promotion-name convention.** When promoting nested agents to plugin root: `agents/<umbrella>-<name>.md` (e.g., `agents/abm-orchestration-intent-analyst.md`)? Or strip umbrella and use `agents/<name>.md` only when no collision? Default: include umbrella prefix to make provenance clear and prevent future collisions.

## Estimated total effort

| Wave | Skills | Hours |
|---|---|---|
| 2a Product | ~22 | 3 |
| 2b Software Development | ~40 | 5 |
| 2c GTM (5 sub-PRs) | ~80 | 6-8 |
| 2d Data Engineering | ~20 | 2 |
| 2e Long tail | ~25 | 2-3 |
| **YED-31 total** | **~187** | **18-21** |
| YED-34 audit | ~50 nested dirs + orphan | 3-5 |
| **Combined** | | **21-26 hours** |

Spread across ~6-10 working sessions depending on focus blocks.

## Workflow notes for resumption

- Auto-update hook is live. Every commit on this repo updates the user-scope plugin cache in the background. No manual `claude plugin update` needed unless investigating the log at `${TMPDIR:-/tmp}/alex-agents-skills-plugin-update.log`.
- Don't open PRs until I explicitly say "branch is fully done." (Lesson from YED-33: opening a PR while commits were still landing led to a partial merge.)
- For pre-flight validation, prefer `claude --plugin-dir /Users/sameoldexpressions/Documents/GitHub/alex-agents-skills --print "..."` from `/tmp` — neutral cwd, no project-local skill interference.
- Linear status updates happen at PR merge (status: Done) — not at branch creation (status: In Progress). YED-33 confusion came from updating Linear before the merge actually reflected the work.
