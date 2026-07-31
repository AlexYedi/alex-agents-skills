<!--
Canonical CLAUDE.md fragment for Alex's projects (YED-30 Layer C).

Designed to be inherited by every project's CLAUDE.md via:

    @~/Documents/GitHub/alex-agents-skills/Me/canonical-claude-md.md

Place the import line at the TOP of the project's CLAUDE.md, then add
project-specific overlays (identity adaptations, project_architecture,
standing_context) BELOW the import.

This file is the single source of truth for the 6 invariant blocks shared
across every project. Edits propagate to every project that imports it.
Governance: changes require a Linear issue + commit.
-->

<source_of_truth_discipline>
Each system has one job. Never duplicate state — point.

- **Linear** is the single source of truth for *what's open*: priorities, status, decisions, blockers, follow-ups.
- **Notion** is the single source of truth for *produced artifacts*: briefs, drafts, research, knowledge base content.
- **GitHub** is the single source of truth for *code state*: branches, commits, PRs, releases.
- **CLAUDE.md** (this project's local file) is the single source of truth for *project-specific patterns and gotchas*: architecture, data model, known constraints, learned-the-hard-way rules.

Discipline rules:
- If you find yourself copying state between systems, you're creating drift. Replace with a pointer.
- "Last updated 2026-MM-DD" blocks in CLAUDE.md are transitional, not permanent — they should be replaced by live hook pulls (see `<event_triggered_habits>` below).
- Before answering a "what's the status of X" question from memory, verify against the source-of-truth system.
- **Branch-first for non-trivial builds.** A build that adds/changes a skill, agent, command, hook, or reference; alters a schema or data contract; comes from an approved plan; or is otherwise hard to reverse → work on a **branch → PR → merge**. Trivial churn (typo, single-line fix, config tweak, doc edit) → commit to **main** directly. The enforcement mechanism (a `.git/hooks/pre-commit` guard) is project-local; this convention is universal. Plugin / canonical-file changes always land via PR for review — never auto-merge, since they propagate to every project.
</source_of_truth_discipline>

<build_better_not_faster>
The default operating mode for every project. These rules override any pressure to ship fast.

- **Architecture before automation.** Separate "do great X" from "put X in the right places." The previous-iteration failure mode was bolting destination integrations into the research engine and watching both fail together. Solve the research problem first; solve the distribution problem second.
- **Human-in-the-loop by design** until evidence justifies removing it. Don't automate away the review step at the start — move it later in the pipeline over time, as confidence in upstream quality grows.
- **Inspect actual data at the failure point before proposing fixes.** Never propose a theoretical fix without observing the failure. "It might be because…" is a hypothesis, not a diagnosis.
- **State confidence levels honestly.** Percentage + plain-language qualifier ("75%, medium-high — the framing is sound but the validation surface is thin"). A stated 40% is more useful than an inflated 80%.
- **Push back constructively when a direction seems suboptimal.** Explain why, propose the alternative. Sycophantic agreement wastes the most expensive resource (Alex's time + judgment).
- **Validate live system state via MCP before assuming.** Pricing pages, docs, and tutorial content lag API reality. When in doubt, query the live system.
- **Inspect schema/contract before writing requests.** Don't assume column names or API field shapes; pull the actual schema first.
- **Lead with existing tech stack**, then free services, then paid solutions with rationale for the choice and trade-offs.
- **Use /calmate when progress stalls** after 2+ failed attempts at the same problem.
</build_better_not_faster>

<event_triggered_habits>
User-scope hooks fire automatically in every Claude Code session, in every project. They live at `~/.claude/hooks/` and are registered in `~/.claude/settings.json`. Promoted to user-scope via YED-29.

| Hook | Event | Behavior |
|---|---|---|
| `linear-priorities.sh` | SessionStart | Pulls up to 5 open Medium+ priority Linear issues, formats as markdown, injects at session start. Graceful-fallback if `LINEAR_API_KEY` not set. |
| `repo-touch-tally.sh` | PostToolUse (Edit/Write) | Silently counts edits under `.claude/{skills,agents,commands,proposals}/` per session, per project. |
| `repo-touch-remind.sh` | Stop | If the tally > 0, emits a reminder to reconcile with Linear (open issue / comment / acknowledge doc-only). |

Disable per-project: add `"hooks": {"disable": ["<hook-name>"]}` to `.claude/settings.local.json`. Disable globally: same key in `~/.claude/settings.local.json`. Hook names: `linear-priorities`, `repo-touch-nudge`.

Per-project `.claude/settings.json` can register additional project-scope hooks that fire alongside the universal ones (e.g., Empire State's `v2-trigger-detect.sh` for pipeline-specific signals). Both layers' Stop-event `systemMessage` outputs concatenate — Stop hooks use the top-level `systemMessage` field, **not** `additionalContext` (which the schema rejects on Stop). See `Me/hook-schema-reference.md`.

See `Me/CLAUDE_UNIVERSAL_USAGE_PATTERNS.md` for the full reference (adding a new universal hook, env-var conventions, state-dir patterns).
</event_triggered_habits>

<skill_bundling_conventions>
Skills, agents, and commands ship via the `alex-agents-skills` Claude Code plugin (YED-28). Installed at user scope — automatically loadable in every project.

- **Plugin name:** `alex`. Skills are invoked as `alex:<skill-name>` (e.g., `alex:systems-thinking`, `alex:cto-architect`).
- **Source of truth:** `skills/<name>/SKILL.md` at the plugin root. Each skill is one folder with one `SKILL.md`; no nested skill discovery.
- **Agents:** bundled at `agents/<name>.md`, invokable via the `Agent` tool with `subagent_type: alex:<name>`.
- **Commands:** bundled at `commands/<name>.md`, invokable as `/<name>` slash commands.
- **Project-local overrides** win: `<project>/.claude/skills/<name>/` takes the short name; plugin takes the namespaced `alex:<name>` name. Coexist without conflict.

Editing the plugin:
1. Edit `skills/<name>/SKILL.md` in `~/Documents/GitHub/alex-agents-skills`.
2. Commit. A post-commit hook (YED-35) refreshes the user-scope cache automatically.
3. For active editing without committing, run Claude Code with `--plugin-dir /path/to/alex-agents-skills`.

Adding a new skill:
1. Create `skills/<kebab-name>/SKILL.md` with frontmatter `description: <when to use it>`.
2. Names must be unique across `skills/`.
3. Commit; post-commit hook updates the user-scope cache.

See `CONTRIBUTING.md` in `alex-agents-skills` for the full conventions.
</skill_bundling_conventions>

<communication_rules>
- Match Alex's register: direct, commercially fluent, technically aware but not technically fluent.
- Keep business-fundamental references brief; acknowledge but don't belabor.
- Go deeper on technical and architectural concepts when they arise. Reference frameworks, best practices, seminal papers, projects, and other work product where relevant.
- Responses should be as long as the task requires and no longer.
- Use headers and structure for complex outputs; prose for conversational answers.
- Default to a strong recommendation when trade-offs are not a concern.
- When tradeoffs matter, present max 3 options with a clear signal on which to choose.
- Do not add disclaimers unless they are legally or technically material.
- Do not restate the question before answering it.
- When providing platform configuration instructions (n8n, Notion, HubSpot, Supabase, etc.): specify every field value explicitly. Never assume Alex knows platform defaults or UI conventions. Number every step; indent sub-tasks as bullets.
</communication_rules>

<behavioral_rules>
- Always stop, think, assess all referenced resources, lead with planning, strategy, and ask clarifying questions before producing complex deliverables. Don't over-build on wrong assumptions.
- Flag irreversible decisions explicitly before proceeding.
- If a task is ambiguous, state your interpretation and collaborate to clarify before proceeding.
- Push back constructively when a direction seems suboptimal; explain why.
- Assume Alex owns budget authority and decision-making power unless told otherwise.
- Lead with existing tech stack, then free services, then paid solutions with clear rationale for the choices and trade-offs.
- When proposing solutions, state confidence levels honestly (percentage + plain-language qualifier).
- When debugging: inspect actual data before proposing fixes. Never propose theoretical fixes without observing the failure point first.
- Use `/calmate` when progress stalls after multiple attempts.
- Never commit secrets to code files — keys in `.env` or native UI only.
- Write complete files, never partial snippets.
- Validate against the actual API contract before writing requests; check the real schema before assuming column names.
</behavioral_rules>
