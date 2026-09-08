---
name: consulting-benefits-case
description: >
  Benefits Realization Management (Ward & Daniel, *Benefits Management: How to Increase the
  Business Value of Your IT Investments*, Cranfield School of Management/Wiley, 2006) plus
  Amdahl's Law (1967) as the honesty check on speedup claims. Builds a Benefits Dependency
  Network linking investment objectives to business benefits to business/enabling changes to
  technology enablers, assigns each benefit an owner, measure, and baseline, then deflates every
  per-step automation gain into a realistic end-to-end figure before it goes into an ROI case.
  Use it once the roadmap is sequenced and before you commit to a business case or an
  acceptance bar.
  Triggers - "build the benefits case", "benefits dependency network", "BDN", "benefits
  realization management", "who owns this benefit", "Ward and Daniel", "what's the real ROI",
  "Amdahl's law", "deflate this speedup claim", "how much will automation actually save",
  "the un-automated fraction", "justify this investment", "benefit measures for go-live",
  "will this actually move the number". Produces a Benefits Dependency Network sketch, a
  benefits register (benefit/owner/measure/baseline/target/type), an Amdahl worked calc per
  automation, and a headline ROI.
---

# Benefits Case (Benefits Realization Management, Ward & Daniel + Amdahl's Law)

Benefits Realization Management, as laid out by John Ward and Elizabeth Daniel in *Benefits
Management: How to Increase the Business Value of Your IT Investments* (Cranfield School of
Management/Wiley, 2006), starts from a discipline that most business cases skip: benefits are
never delivered by technology alone. Technology only *enables* benefits; they are realized
through business change, and every benefit needs someone accountable for making that change
happen and for the number it produces. The core tool is the Benefits Dependency Network (BDN),
built right-to-left from investment objectives back through the changes and enablers required to
reach them. Amdahl's Law — Gene Amdahl, "Validity of the Single Processor Approach to Achieving
Large Scale Computing Capabilities," AFIPS Conference Proceedings, 1967 — supplies the arithmetic
that keeps the benefits case honest: no matter how fast you make one step, the fraction of the
process you didn't touch caps how much faster the whole thing gets.

---

## Where this sits in the engagement

This is step 10 of 14, the second step of Phase C (Plan & justify). It takes the economic
baseline from `consulting-cost-time-baseline` (step 3) and the sequenced roadmap from
`consulting-roadmap-sequencing` (step 9) and turns them into a defensible benefits case: which
benefits, owned by whom, measured how, against what baseline, and how much of the claimed
speedup actually survives contact with the un-automated rest of the process. The benefit
measures this skill defines become the acceptance-bar SLOs in `consulting-acceptance-bar` (step
14) — what gets tracked here is what gets held to at go-live and beyond.

---

## When to use this skill

- The roadmap is sequenced and someone is about to ask "so what do we actually get for this."
- A vendor, team, or automation champion has quoted a speedup number ("10x faster") that hasn't been checked against how much of the process it actually touches.
- Leadership needs a business case with named owners and measures, not a benefits list with no accountability.
- You're about to set go-live acceptance thresholds (step 14) and need real target numbers to set them against.
- Multiple automations are competing for investment and you need an honest, comparable end-to-end figure for each.
- A prior initiative's benefits were "assumed" at approval and never checked after go-live — you need a structure that forces a post-implementation review.

---

## The method

### 1. The Benefits Dependency Network (BDN)

Ward & Daniel's BDN is built **right to left**, and every link must hold:

```
INVESTMENT OBJECTIVES  <-  BUSINESS BENEFITS  <-  BUSINESS CHANGES
                                                    (and ENABLING CHANGES)
                                                        <-  IT / TECHNOLOGY ENABLERS
```

- **Investment objectives** — the strategic reasons the investment is being made at all (e.g.,
  "reduce cost-to-serve," "improve cycle-time competitiveness").
- **Business benefits** — the specific, measurable improvements that satisfy an objective. Each
  benefit must trace back to at least one objective; a benefit with no objective is padding.
- **Business changes** — the new ways of working, roles, policies, or processes people must
  actually adopt for the benefit to occur. **Enabling changes** are the prerequisite changes
  (new skills, org structure, data cleanup) that must happen before the business change can
  take hold.
- **IT/technology enablers** — the automation, tool, or system capability being built. It
  enables the business change; it does not, by itself, produce the benefit.

The discipline's central truth: **benefits are realized only through business change, never by
delivering the technology alone.** A BDN with a technology enabler and no business change
attached to it is a warning sign, not a benefit.

### 2. Owner, measure, baseline — for every benefit

Every benefit in the network carries three fields, non-negotiable:

- **Benefit owner** — a named individual accountable for the benefit occurring, not the project
  team that delivered the technology.
- **Measure** — the specific metric that will demonstrate the benefit, defined precisely enough
  to be tracked after go-live.
- **Baseline** — the pre-change value of that measure, taken directly from the cost/time
  baseline built in `consulting-cost-time-baseline` (step 3). No baseline, no credible benefit.

### 3. Classify each benefit by measurability

| Type | Definition |
|---|---|
| **Financial** | Can be expressed directly in monetary terms with an agreed calculation (e.g., $ saved per case). |
| **Quantifiable** | Can be measured numerically, and a monetary value could plausibly be estimated, but isn't formally financial (e.g., cases processed per FTE-day). |
| **Measurable** | Can be measured, but there is no agreed way to convert it to money or a single number others would sign off on (e.g., customer satisfaction score). |
| **Observable** | Judged by agreed criteria but not directly measured, by consensus among relevant stakeholders (e.g., "decisions feel more consistent"). |

Classify honestly. Overclaiming an observable benefit as financial is the fastest way to lose
credibility with whoever signs the business case.

### 4. Amdahl's Law — the honesty check on speedup

```
S = 1 / ( (1 - p) + p/s )
```

- `p` = the **fraction** of total work/cycle time the automation improves.
- `s` = the **speedup** applied to that fraction.
- `S` = the overall, end-to-end speedup actually achieved.

As `s -> infinity`, `S -> 1 / (1 - p)`: **the un-automated fraction caps the end-to-end gain**,
no matter how fast the automated piece runs.

**Worked example.** Automate a step that is 30% of cycle time (`p = 0.3`). Even with a perfect,
instantaneous automation (`s -> infinity`):

```
S -> 1 / (1 - 0.3) = 1 / 0.7 ~= 1.43x
```

A "10x faster" automation on a step that's 30% of the process delivers roughly a 1.4x
end-to-end speedup — not 10x. Use Amdahl to deflate inflated ROI claims, and to steer automation
investment toward the **largest-p** steps: the ones already flagged by the cost/time baseline
(step 3) and the bottleneck found in `consulting-constraint-analysis` (step 8). Automating a
small-p step, however dramatically, barely moves the end-to-end number.

---

## Workflow (what you do when invoked)

1. **State the investment objectives.** Pull them from the engagement's stated strategic
   rationale — write 2–4 crisp objectives the whole case will trace back to.
2. **Build the BDN right to left.** For each objective, map the business benefits that would
   satisfy it; for each benefit, map the business changes (and enabling changes) required; for
   each change, map the technology enabler from the roadmap (step 9) that makes it possible.
   Sketch it as columns, objectives on the right, enablers on the left.
3. **Assign owner, measure, baseline, and type per benefit.** Pull baselines directly from step
   3's cost/time table. Classify each benefit as financial, quantifiable, measurable, or
   observable — don't round up.
4. **Apply Amdahl's Law to every automation.** For each technology enabler in the roadmap,
   estimate `p` (its share of total cycle time, from step 3) and `s` (the speedup on that
   share), and compute the realistic end-to-end `S`. Flag any benefit whose claimed savings
   assume `s` alone, ignoring `p`.
5. **Total into the benefits case and headline ROI.** Roll the deflated, per-automation
   end-to-end gains into a total benefits figure and a headline ROI, built only from
   financial/quantifiable benefits with a stated calculation.
6. **Hand off and schedule realization review.** Package the benefit measures for
   `consulting-acceptance-bar` (step 14) to convert into go-live SLOs, and set a date for the
   post-go-live realization review — benefits are tracked after go-live, never assumed at
   approval.

---

## Deliverable & templates

**Benefits Dependency Network (sketch)**

```
INVESTMENT OBJECTIVES        BUSINESS BENEFITS          BUSINESS / ENABLING CHANGES        IT / TECHNOLOGY ENABLERS
--------------------------   ------------------------   ---------------------------------   -------------------------
e.g. Reduce cost-to-serve <- e.g. Lower cost per case <- e.g. New exception-handling role  <- e.g. Automated
                                                          (enabling: staff retraining)          invoice-matching tool
e.g. Improve cycle-time   <- e.g. Faster case turnaround <- e.g. New SLA-driven routing     <- e.g. Workflow
   competitiveness                                          policy                             orchestration enabler
```

**Benefits register**

| Benefit | Owner | Measure | Baseline (step 3) | Target | Type |
|---|---|---|---|---|---|
| e.g. Lower cost per case | e.g. AP Manager | $/case processed | e.g. $5.10/case | e.g. $3.20/case | Financial |
| e.g. Faster case turnaround | e.g. Ops Lead | Median cycle time | e.g. 4.2 days | e.g. 2.5 days | Quantifiable |
| e.g. More consistent exception handling | e.g. Team Lead | Stakeholder consensus rating | e.g. n/a (new) | e.g. "consistent" per review | Observable |

**Amdahl worked calc (per automation)**

| Automation | p (fraction of cycle time) | s (speedup on that fraction) | End-to-end S = 1/((1-p)+p/s) | Vendor/claimed speedup | Verdict |
|---|---|---|---|---|---|
| e.g. Automated invoice matching | 0.30 | 10x | ~1.37x | "10x faster" | Deflated: real gain ~1.37x, not 10x |

**Headline ROI**

```
Total annual benefit  = sum(deflated per-automation savings, financial + quantifiable only)
Total investment cost = build + run cost across the roadmap (step 9)
ROI                   = (Total annual benefit - Total investment cost) / Total investment cost
Realization review date: <set post-go-live checkpoint>
```

---

## Pitfalls

- **Claiming the technology delivers the benefit.** If a benefit has no business change (and,
  where needed, enabling change) attached, the technology alone will not produce it — the BDN
  link is broken.
- **No baseline, no benefit.** A target with no baseline from step 3 is a guess dressed up as a
  number; refuse to carry it into the ROI.
- **Rounding a measurable or observable benefit up to financial.** This is the single fastest
  way to lose credibility with whoever approves the business case — classify honestly.
- **Quoting vendor/step-level speedup as the end-to-end number.** A "10x faster" automation on a
  30%-of-cycle-time step is a ~1.4x end-to-end gain — always run it through Amdahl before it
  goes into ROI.
- **Automating the smallest-p step because it's easiest.** It flatters the demo and barely moves
  the total; prioritize by `p`, cross-checked against the bottleneck from step 8.
- **Treating approval as realization.** Benefits are tracked after go-live, not assumed at
  sign-off — a benefits case with no scheduled post-implementation review is unfinished.

---

## Related

- **In-suite** — `consulting-cost-time-baseline` (step 3, upstream): supplies the baselines every benefit measure is set against. `consulting-roadmap-sequencing` (step 9, upstream/pairs): supplies the sequenced initiatives that populate the BDN's technology enablers. `consulting-acceptance-bar` (step 14, downstream): converts this skill's benefit measures into go-live SLOs and error budgets.
- **Elsewhere in the library** — `creating-financial-models`, `roi-benchmark-library`, `board-readiness-kit`.
- **References** — Ward, J. & Daniel, E., *Benefits Management: How to Increase the Business Value of Your IT Investments* (Cranfield School of Management/Wiley, 2006); Amdahl, G. M., "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities," *AFIPS Conference Proceedings*, 1967.
