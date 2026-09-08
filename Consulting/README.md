# Consulting Suite

A cross-linked **AI / automation transformation engagement**, run the way a top-tier
consultancy would — 14 skills, each one rigorous, academically-grounded method with an
operational workflow and a concrete deliverable.

> **This folder is a human-browsable index only.** The skills themselves live flat under
> [`../skills/`](../skills/) because Claude Code discovers skills only at
> `skills/<name>/SKILL.md` (one level deep — a nested `Consulting/` subfolder would **not**
> load). The shared `consulting-` name prefix is the grouping mechanism: the 14 cluster
> together in listings and in `alex:toolbox`, and invoke as `alex:consulting-<name>`.

## The engagement, end to end

The suite runs as a pipeline. Each step consumes the one(s) before it and feeds the ones after.

### Phase A — Understand the work (Discovery)

| # | Skill | Method | Source |
|---|-------|--------|--------|
| 1 | [`consulting-boundary-setting`](../skills/consulting-boundary-setting/SKILL.md) | SIPOC + Value Stream Mapping | Rother & Shook, *Learning to See* (1999) |
| 2 | [`consulting-process-recovery`](../skills/consulting-process-recovery/SKILL.md) | Process Mining (de facto vs de jure) | van der Aalst; IEEE Process Mining Manifesto (2011) |
| 3 | [`consulting-cost-time-baseline`](../skills/consulting-cost-time-baseline/SKILL.md) | Time-Driven Activity-Based Costing | Kaplan & Anderson, HBR (2004) |
| 4 | [`consulting-tacit-work-elicitation`](../skills/consulting-tacit-work-elicitation/SKILL.md) | Critical Incident Technique + Contextual Inquiry | Flanagan (1954); Beyer & Holtzblatt (1998) |

### Phase B — Analyze & target (Diagnosis)

| # | Skill | Method | Source |
|---|-------|--------|--------|
| 5 | [`consulting-task-decomposition`](../skills/consulting-task-decomposition/SKILL.md) | Task-based framework (routine × cognitive) | Autor, Levy & Murnane, QJE (2003) |
| 6 | [`consulting-ai-suitability-scoring`](../skills/consulting-ai-suitability-scoring/SKILL.md) | SML rubric | Brynjolfsson & Mitchell, *Science* (2017); Brynjolfsson, Mitchell & Rock (2018) |
| 7 | [`consulting-automation-design`](../skills/consulting-automation-design/SKILL.md) | Levels of Automation + 4-stage model | Sheridan & Verplank (1978); Parasuraman, Sheridan & Wickens (2000) |
| 8 | [`consulting-constraint-analysis`](../skills/consulting-constraint-analysis/SKILL.md) | Theory of Constraints (Five Focusing Steps) | Goldratt, *The Goal* (1984) |

### Phase C — Plan & justify (Roadmap & case)

| # | Skill | Method | Source |
|---|-------|--------|--------|
| 9 | [`consulting-roadmap-sequencing`](../skills/consulting-roadmap-sequencing/SKILL.md) | Weighted Shortest Job First (CoD ÷ job size) | Reinertsen, *Product Development Flow* (2009) |
| 10 | [`consulting-benefits-case`](../skills/consulting-benefits-case/SKILL.md) | Benefits Realization Management + Amdahl's Law | Ward & Daniel (2006); Amdahl (1967) |

### Phase D — Specify & build safely (Delivery contracts)

| # | Skill | Method | Source |
|---|-------|--------|--------|
| 11 | [`consulting-behaviour-specification`](../skills/consulting-behaviour-specification/SKILL.md) | Given-When-Then + requirement quality bar | North (2006); ISO/IEC/IEEE 29148:2018 |
| 12 | [`consulting-agent-contract`](../skills/consulting-agent-contract/SKILL.md) | Design by Contract + Hoare logic | Meyer (1986); Hoare, CACM (1969) |
| 13 | [`consulting-failure-design`](../skills/consulting-failure-design/SKILL.md) | FMEA + Pre-Mortem | MIL-STD-1629A / AIAG-VDA; Klein, HBR (2007) |
| 14 | [`consulting-acceptance-bar`](../skills/consulting-acceptance-bar/SKILL.md) | Service Levels & Error Budgets | Beyer, Jones, Petoff & Murphy, *Site Reliability Engineering* (2016) |

## How the pipeline flows

```
A. Understand          B. Analyze & target        C. Plan & justify      D. Specify & build safely
─────────────          ───────────────────        ─────────────────      ─────────────────────────
1 boundary-setting ──┬─▶ 5 task-decomposition ──▶ 6 ai-suitability ──▶ 7 automation-design ──┐
2 process-recovery ──┤                                                                        │
3 cost-time-baseline ┤                            8 constraint-analysis ◀────────────────────┘
4 tacit-elicitation ─┘                                     │
                                                           ▼
                                          9 roadmap-sequencing ⇄ 10 benefits-case
                                                                       │
                        11 behaviour-spec ─▶ 12 agent-contract ─▶ 13 failure-design ─▶ 14 acceptance-bar
                                                                                              │
                                                                       (SLOs close the loop to 10)
```

- **1** bounds the process and hands the as-is picture to **2–4**.
- **2** recovers the real process; **3** prices it; **4** captures the tacit work — together they feed diagnosis.
- **5** breaks the work into tasks, **6** scores each for AI suitability, **7** designs the human–machine split, **8** checks it all targets the true bottleneck.
- **9** sequences the initiatives by economic value; **10** builds the benefits case (Amdahl keeps it honest).
- **11–14** turn the chosen automation into precise behaviour, a formal contract, a failure design, and a go-live acceptance bar whose SLOs trace back to the benefits case.

## Using them

Invoke any step directly, e.g. `alex:consulting-boundary-setting`, or walk the whole engagement
A → D. Each skill also cross-links to relevant standing library skills (e.g.
`consulting-constraint-analysis` ↔ `systems-thinking`, `consulting-agent-contract` ↔
`agent-memory-and-guardrails`, `consulting-acceptance-bar` ↔ `observability-designer`).

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for how skills are discovered, added, and released.
