---
name: toolbox
description: >
  Your tool wall — list every slash command, skill, and agent in the CURRENT project,
  one scannable line each (name · what-it's-for · args), scanned live from frontmatter
  so it never drifts. Use when you've built enough that you forget what you have, when
  onboarding to a project's `.claude/` kit, or when you ask "what commands/skills/agents
  do I have here", "what's in my toolbox", "list my tools", "what can I run". Optional
  keyword to filter, or `plugins <keyword>` to search the alex-plugin skills library.
tools: Bash, Read
---

# toolbox — what's at your fingertips

Solves the "I built so much I forget what I have" problem. The catalog is **generated live** from the
`description` frontmatter in the current project's `.claude/{commands,skills,agents}` — there is no separate
list to maintain, so it can never go stale. Lead with the **project-local** kit; the `alex`-plugin skills
library is a filterable appendix.

## Modes (from `$ARGUMENTS`)
- **no args** → the full project-local catalog, grouped by type.
- **a keyword** (e.g. `content`, `research`, `deploy`) → filter project-local entries whose name/description
  matches (case-insensitive).
- **`plugins <keyword>`** → search the `alex`-plugin skills (`~/Documents/GitHub/alex-agents-skills/skills/`)
  by keyword and list matches (never dump the whole library).

## Step 1 — Scan the frontmatter (live)
Runs against the current project (`$CLAUDE_PROJECT_DIR`, falling back to the working dir). Extracts
name · description · args for every project-local command, skill, and agent:

```bash
cd "${CLAUDE_PROJECT_DIR:-$PWD}"
python3 - <<'PY'
import glob, os, re
def fm(p):
    t = open(p).read(); m = re.match(r'^---\n(.*?)\n---', t, re.S); return m.group(1) if m else ''
def field(block, key):
    lines = block.split('\n')
    for i, l in enumerate(lines):
        m = re.match(rf'^{key}:\s*(.*)$', l)
        if not m: continue
        v = m.group(1).strip()
        # seed with the inline value (unless it's a folded/block/empty marker), then append any
        # continuation lines — covers single-line, folded '>', block '|', AND wrapped plain scalars.
        parts = [] if v in ('>', '|', '>-', '|-', '') else [v.strip('"').strip("'")]
        for j in range(i + 1, len(lines)):
            if re.match(r'^[A-Za-z_-]+:', lines[j]): break   # next top-level key at col 0
            if lines[j].strip(): parts.append(lines[j].strip())
        return ' '.join(parts).strip()
    return ''
def emit(kind, name, desc, args=''):
    print(f"{kind}\t{name}\t{' '.join(desc.split())[:160]}\t{args}")
for p in sorted(glob.glob('.claude/commands/*.md')):
    b = fm(p); emit('command', '/' + os.path.basename(p)[:-3], field(b, 'description'), field(b, 'argument-hint'))
for p in sorted(glob.glob('.claude/skills/*/SKILL.md')):
    b = fm(p); emit('skill', field(b, 'name') or os.path.basename(os.path.dirname(p)), field(b, 'description'))
for p in sorted(glob.glob('.claude/agents/**/*.md', recursive=True)):
    b = fm(p); emit('agent', field(b, 'name') or os.path.basename(p)[:-3], field(b, 'description'))
PY
```
(Robust YAML-ish parse — handles folded `>` / block `|` / wrapped multi-line descriptions, so nothing
renders truncated. If the project keeps loose skills as `.claude/skills/*.md` instead of folders, add a
second glob for those.)

For `plugins <keyword>` mode instead run:
```bash
grep -rl -i "<keyword>" ~/Documents/GitHub/alex-agents-skills/skills/*/SKILL.md 2>/dev/null | while read -r f; do
  n=$(awk '/^name:/{sub(/^name: */,"");print;exit}' "$f")
  d=$(awk '/^description:/{sub(/^description: */,"");gsub(/^"|"$/,"");print;exit}' "$f")
  printf 'alex:%s — %s\n' "$n" "$(echo "$d" | cut -c1-100)"
done | head -40
```

## Step 2 — Group & present
Group the scanned rows **by type** — three sections, in this order:

1. **Commands** (`/name`, typed directly)
2. **Skills** (invoked by name or auto-triggered)
3. **Agents** (invoked by commands/workflows, not typed directly — list compactly)

Within each section, present each entry as a **single scannable line**:
`` `name` `` — *use-when* (tighten the description into a ≤12-word "reach for this when…") — `args` if any.

Open with a one-line count (`N commands · M skills · K agents`). Keep it dense and skimmable — this is a
menu, not documentation. **Do not invent tools; only list what the scan returned.** Close with the pointer:
*"Filter with `toolbox <keyword>`; search the plugin library with `toolbox plugins <keyword>`."*

**Optional — proactivity tier.** If the project documents an invocation-proactivity convention (e.g. a
CLAUDE.md rule for whether a tool auto-fires), tag each entry with the project's tiers so the catalog also
answers "will it run on its own?" Skip this in projects that have no such convention — it is not universal.

## Notes
- **Freshness by design:** re-scans every run, so newly-added commands/skills/agents appear automatically —
  no upkeep, no drift.
- **Static snapshot (optional):** a project that wants a browsable/shareable catalog (e.g. a dashboard page)
  can serialize this scan to JSON and commit it, regenerating on change. The live scan is always the source
  of truth; any committed snapshot is a convenience copy.
