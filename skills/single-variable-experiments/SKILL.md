---
name: single-variable-experiments
description: The discipline of isolating one variable per experiment so results are actually attributable. Defines experiment types (input-only, treatment-only, combined), confidence weighting based on what was held fixed, minimum sample sizes, and success criteria. Use when the user wants to test a change, compare variants, improve a campaign or funnel, or interpret an experiment whose result they can't explain. Prevents the most common learning-loop failure — changing several things at once and losing all signal. Worked examples are cold email (list / copy / offer); the discipline applies to any iterative test. For hypothesis templates, guardrails, and measurement-plan scaffolding, see `experiment-design-kit`.
---

# Single-Variable Experiments

If you change several things at once, you learn nothing. This skill forces you to isolate one variable per experiment so you can actually attribute the result.

The worked examples below are cold email — list, copy, and offer are the three variables — but the discipline is domain-general. Substitute your own variables (pricing tier / landing page / audience, model / prompt / retrieval, channel / creative / segment) and the framework holds.

## Why this exists

Most cold email operators run "throw-everything" experiments. Campaign 1 gets a new list, new copy, and a new offer. It works better. They declare victory. But they can't tell you WHY — was it the list? The copy? The offer?

Then campaign 2 changes all three again. Regression. Nobody knows why.

This skill is the antidote: plan each experiment around ONE variable, keep everything else constant, and confidence-weight the results.

## The three experiment types

### A. List-only experiment
- **What varies:** the list (targeting criteria)
- **What stays fixed:** copy, offer, sending infrastructure, sequence timing
- **What you learn:** whether this segment is a better fit than the baseline
- **Confidence on learnings:** HIGH on targeting, LOW on copy (because copy wasn't tested)

### B. Copy-only experiment
- **What varies:** the copy (subject, body, sequence, or A/B variant)
- **What stays fixed:** list, offer, infrastructure
- **What you learn:** whether this copy resonates with this audience
- **Confidence on learnings:** HIGH on copy, LOW on targeting

### C. Combined experiment (use sparingly)
- **What varies:** list AND copy (and sometimes offer)
- **What stays fixed:** only infrastructure
- **When to use:** launching a whole new campaign for a new ICP. You can't isolate because everything is new.
- **Confidence on learnings:** MEDIUM on everything. Use as hypothesis-generation, not conclusion.

## The Framework

### Step 1: Name your hypothesis

Every experiment starts with a one-sentence hypothesis:

> "Targeting Heads of Marketing at 50-200 person B2B SaaS companies will get a higher positive reply rate than our current VP Sales baseline, because [reason]."

Or:

> "Leading with a question about their recent product launch will get a higher reply rate than our current benefit-focused opener, because [reason]."

If you can't write the hypothesis in one sentence, you don't understand the experiment yet. Go back.

### Step 2: Identify the single variable

Write down exactly what changes and what stays the same.

```
Variable: Target job title
Change: "VP Sales" → "Head of Marketing"

Constants:
- Industry filter: unchanged
- Headcount: unchanged
- Geography: unchanged
- Copy: unchanged (same 4-step sequence)
- Offer: unchanged (same lead magnet)
- Sending infrastructure: unchanged (same 20 domains, 40 inboxes)
- Send schedule: unchanged
```

If ANY constant is actually changing, stop. Either lock it down, or reclassify as a combined experiment.

### Baseline sanity check — the 1% rule

Before running any experiment, confirm your baseline is healthy: **overall reply rate ≥1% after 200+ sends.** If your baseline is below 1% after 200 sends, the problem isn't your experiment — your infrastructure or copy is already broken. Run `/email-deliverability-audit` first.

Running an experiment on a broken baseline is wasted effort: you'll learn that "both arms are bad," not "which arm wins."

### Step 3: Calculate minimum sample size

The smaller your effect, the more leads you need. Use these rough rules for cold email:

| Current baseline | Expected lift | Minimum sends per arm |
|---|---|---|
| 1% positive reply rate | 2x (1% → 2%) | ~500 |
| 1% positive reply rate | 1.5x (1% → 1.5%) | ~2,000 |
| 1% positive reply rate | 1.2x (1% → 1.2%) | ~10,000 |
| 2% positive reply rate | 2x (2% → 4%) | ~250 |
| 2% positive reply rate | 1.5x (2% → 3%) | ~1,000 |

Rule of thumb: **if your test has fewer than 500 sends per arm, you can't tell signal from noise.**

For most beginners, 2,000 sends per arm is the right default.

### Step 4: Build the success criteria up front

Before launching, write:

```
Success = positive reply rate > X% (our current baseline is Y%)
Failure = positive reply rate < Z%
Inconclusive = between X and Z
Required sample: at least N sends per arm, reported after day 21 of sequence
```

Decide now — not after seeing the data. This prevents "oh we learned something else instead" rationalization.

### Step 5: Launch both arms simultaneously

Same day, same sending infrastructure split, same sequence. If your control arm sends Monday and your variant arm sends Thursday, day-of-week effects will confound the test.

Best practice in Smartlead/Instantly: create two campaigns, assign each half of your inboxes, launch at the exact same time, same schedule.

### Step 6: Measure at day 21

Wait until the full sequence (typically Day 0, 3, 7, 11 + reply grace period) has finished for ALL leads. Measuring earlier biases toward the first email's reply rate.

Pull metrics per arm (in a GTM pipeline this is a reply-scoring step; substitute your own measurement source):
- Total sent (per arm)
- Total replies (per arm)
- Positive replies (per arm, classified by Claude)
- Positive reply rate = positive replies / total sent

Secondary metrics (report but don't optimize for):
- Overall reply rate (positive replies / total sent is primary, but this shows raw engagement)
- Open rate (if available)
- Bounce rate (sanity check — if one arm bounces more, your list is bad, not your copy)

### Step 7: Weight the learnings

Use this framework when reporting:

```
Experiment: <name>
Type: List-only | Copy-only | Combined
Variable: <what changed>

Result: <winner name> at <positive reply rate>% vs <baseline>%
Confidence: HIGH | MEDIUM | LOW (based on experiment type + sample size)

Learnings (by confidence):
  HIGH confidence:
    - <thing you can trust>
  MEDIUM confidence:
    - <thing that looks good but needs replication>
  LOW confidence:
    - <thing you're speculating about>
```

HIGH only if: experiment type isolates the variable AND sample size meets the minimum.

### Step 8: Decide what to do with the result

- **Winner by ≥20% lift, HIGH confidence:** adopt as new baseline. Document. Move to next experiment.
- **Winner by 10-20% lift, HIGH confidence:** run a replication experiment with fresh leads. If it wins again, adopt.
- **Winner by <10% lift:** inconclusive. Run bigger next time or drop.
- **Loser:** document WHY you think it lost. Don't just move on — the loss is a learning.
- **Combined experiment winner:** do NOT adopt as a new baseline. Instead, split into single-variable follow-ups to figure out which part actually drove the lift.

## What NOT to experiment on (at first)

If you're just starting out, **don't experiment at all** until you have a baseline from a single shipped campaign running for 3 weeks. You need a control before you can run tests.

Once you have a baseline, the priority order of experiments is usually:
1. **List** (biggest impact — bad list kills any copy)
2. **Offer / lead magnet** (second biggest — "book a call" vs a real magnet)
3. **Subject line** (cheap to test, drives open rate)
4. **Opener / first line** (after subject, the big lever)
5. **CTA** (how you end the email)
6. **Sequence timing** (Day 3 vs Day 2 follow-up)
7. **Sequence length** (4-step vs 6-step)

Don't jump to step 6 when step 1 is broken.

## Common mistakes

- **A/B testing inside one campaign.** Smartlead's A/B variant feature mixes the data — fine for small copy tweaks, terrible for hypothesis testing. Use TWO campaigns for real isolation.
- **"I'll test 3 things at once."** You'll learn nothing.
- **Calling it early.** Wait 21 days minimum. Cold email replies trickle in over weeks.
- **Changing infrastructure mid-test.** If one arm uses new domains and one uses old, deliverability skews everything.
- **Ignoring bounce rate.** If variant's bounce rate is 2x control, the list is bad — not the copy. Disqualify the test.

## Output: experiment plan file

At the end of planning, write to:

```
~/cold-email-ai-skills/profiles/<business-slug>/experiments/YYYY-MM-DD-<name>.yaml
```

Schema:

```yaml
experiment:
  name: <short name>
  hypothesis: <one sentence>
  type: list-only | copy-only | combined
  variable: <what changes>
  constants: <list of what stays fixed>

success_criteria:
  positive_reply_rate_target: <float>
  baseline: <float>
  minimum_sends_per_arm: <int>
  measurement_date: <YYYY-MM-DD>

arms:
  control:
    smartlead_campaign_id: <tbd until launch>
    description: <what's in the control>
  variant:
    smartlead_campaign_id: <tbd until launch>
    description: <what's in the variant>

results: <empty until day 21>
  control_positive_reply_rate: null
  variant_positive_reply_rate: null
  winner: null
  confidence: null
  decision: null
```

## What to do next

**Launch the planned experiment** through whatever system owns the change — a campaign tool, a feature flag, a deploy, a prompt version.

**Then respect the measurement window before evaluating.** Lagging metrics need time to stabilize; reading them early is how a null result gets mistaken for a win. In cold email that window is ~21 days for reply rate. Pick the equivalent for your metric and write it down *before* you launch, so you can't shorten it once you're curious.

**Check you can actually detect the effect you care about.** If your arms are too small, a real effect and no effect look identical. The cold-email rule of thumb is 2,000+ leads per arm to see normal-sized differences — compute the equivalent for your metric's base rate and expected lift rather than borrowing that number directly. If you can't reach it, either widen the test or accept the result as directional only.

## Related skills

- `experiment-design-kit` — hypothesis templates, guardrails, and measurement-plan scaffolding to pair with this discipline
- `approval-loop-fanout` — if the thing being tested is a generation prompt applied across a batch
- `hypothesis-library` — reusable hypotheses to draw candidates from
- `systems-thinking` — when a confounded result points at a feedback loop rather than a variable

## Note on provenance

Built for cold-email experimentation, which is why the worked examples use list / copy / offer and the sample-size and timing numbers are email-specific. The isolation discipline and confidence weighting are the transferable parts.
