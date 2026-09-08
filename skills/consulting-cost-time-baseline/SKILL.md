---
name: consulting-cost-time-baseline
description: >
  Time-Driven Activity-Based Costing (Kaplan & Anderson, Harvard Business Review, Nov 2004;
  Harvard Business School Press, 2007). Puts a defensible cost and time figure on every step of
  a bounded, mined process by estimating just two parameters — a capacity cost rate and unit
  time equations — instead of running a full activity survey. Use it once a process is scoped
  and its real variants are known, and you need to know what the process actually costs, where
  time goes, and how much capacity sits idle.
  Triggers - "how much does this process cost", "time-driven ABC", "TDABC", "cost per case",
  "cost the process", "what's the capacity cost rate", "how much idle capacity do we have",
  "cost and time baseline", "activity-based costing without the survey", "price out this
  workflow", "what does this step cost us", "unused capacity". Produces a capacity-cost-rate
  worksheet plus a per-step cost/time table with total process cost, cost per case, and
  unused-capacity figure.
---

# Cost and Time Baseline (Time-Driven Activity-Based Costing, Kaplan & Anderson, HBR, 2004)

Time-Driven Activity-Based Costing (TDABC) fixes the fatal flaw of classic Activity-Based
Costing: the survey burden. Classic ABC asks every employee to estimate what percentage of
their time goes to each activity — expensive to collect, quickly stale, and biased toward
100% utilization (nobody reports idle time). Kaplan and Anderson's fix, laid out in "Time-Driven
Activity-Based Costing" (Harvard Business Review, November 2004) and expanded in their 2007
book of the same name (Harvard Business School Press), replaces the survey with two directly
estimable parameters: a capacity cost rate per resource pool, and the unit time each activity
actually consumes. Multiply the two and you have defensible activity cost — and, as a
byproduct, a clean measure of unused capacity that a activity survey can never produce, because
survey respondents always allocate themselves to 100%.

---

## Where this sits in the engagement

This is step 3 of 14, the last step of Phase A (Discovery) before tacit-work elicitation. It
takes the bounded process from `consulting-boundary-setting` (step 1) and the actual, mined
process and variants from `consulting-process-recovery` (step 2) and puts a cost and time
number on every step. The result is the economic baseline: `consulting-benefits-case` (step 10)
measures automation savings against it, and `consulting-constraint-analysis` (step 8) uses it
to find where the money and time actually sit in the process.

---

## When to use this skill

- You have a scoped process (SIPOC/VSM) and its real, mined variants, and now need to know what it costs.
- Leadership wants a business case and asks "where's the money" before you can answer.
- You need a defensible cost-per-case figure without running a multi-week activity survey.
- You suspect significant idle or unused capacity in a resource pool but have no way to prove it.
- Process variants (rush vs. standard, new vs. existing customer, simple vs. complex) make a single average cost misleading.
- You're about to feed `consulting-constraint-analysis` or `consulting-benefits-case` and they need real numbers, not guesses.

---

## The method

TDABC estimates exactly two parameters per resource pool and activity — nothing else.

**1. Capacity Cost Rate**

```
Capacity Cost Rate = Cost of Capacity Supplied / Practical Capacity of Resources Supplied
```

- *Cost of capacity supplied*: the total cost of the resource pool for the period (salaries,
  benefits, supervision, occupancy, equipment, systems — all costs of having the resource
  available), NOT the cost of what it actually produced.
- *Practical capacity*: the time resources are actually available to do productive work, not
  their theoretical 100%. Practical capacity is roughly **80–85% of theoretical capacity** —
  subtract breaks, training, meetings, maintenance, and unavoidable downtime from the
  theoretical total (e.g., a 40-hour week, minus the above, nets to practical capacity).
- Units are money per time unit — e.g., $/minute or $/hour — so it can be multiplied directly
  against a duration.

**2. Unit Times, via Time Equations**

Instead of surveying "what % of your time goes to activity X," estimate directly how long each
activity/transaction takes. Where a single average would hide real variation, use a **time
equation**:

```
Time = beta0 + beta1*X1 + beta2*X2 + ... + betaN*XN
```

- `beta0` is the base time for the standard case.
- Each `beta_i*X_i` term adds (or the driver value implies) extra time for a condition that
  makes the case take longer — new vs. existing customer, standard vs. expedited, simple vs.
  complex, number of line items, etc.
- One time equation replaces what classic ABC would need a separate survey question — and a
  separate cost pool — for every variant. This is what lets TDABC absorb the variants surfaced
  by process mining (step 2) into a single model instead of one cost per variant.

**3. Cost of an Activity**

```
Cost of Activity = Capacity Cost Rate x Time Consumed
```

Sum activity costs across the process to get total process cost; divide by case volume for
cost per case.

**4. The Killer Output: Unused (Idle) Capacity**

```
Unused Capacity = (Practical Capacity - Capacity Actually Used) x Capacity Cost Rate
```

Because capacity supplied is measured independently of time actually used on activities, TDABC
is the only ABC variant that can show idle/unused capacity directly — the gap between what you
pay for and what the process consumes. It also naturally prices the cost of complexity: a
variant with many small correction terms in its time equation costs visibly more than the
standard case, and low-volume/high-variation variants show up as disproportionately expensive
per case. This unused-capacity figure is exactly what sizes an automation's addressable cost:
capacity you're already paying for but not using productively is not "savings" from
automation — it is capacity you can either reclaim (headcount, redeployment) or grow into
without adding cost.

---

## Workflow (what you do when invoked)

1. **List resource pools.** Enumerate every resource pool that touches the bounded process from
   step 1 (people, teams, systems, equipment) and pull its supplied cost for the period
   (fully loaded: salary, benefits, overhead, systems, occupancy).
2. **Compute practical capacity and rate.** For each pool, establish theoretical capacity (e.g.,
   FTE-hours per period), apply the 80–85% practical-capacity haircut, and divide supplied cost
   by practical capacity to get the capacity cost rate ($/minute or $/hour).
3. **Estimate unit times per activity.** Walk the VSM steps (step 1) and the variants mined in
   step 2. Where variants genuinely differ in duration, build a time equation
   (`beta0 + beta1*X1 + ...`) rather than a single average; where they don't, use one flat time.
4. **Multiply rate x time.** Compute cost per activity, per step, and roll up to cost per case
   and total process cost across the modeled volume.
5. **Expose unused capacity.** Compare practical capacity supplied against capacity actually
   consumed by the process for each resource pool; compute the idle-capacity cost. Flag any
   pool where this is material — it's a signal for both `consulting-constraint-analysis` and
   the benefits case.
6. **Hand off the baseline.** Package the capacity-cost-rate worksheet and the per-step
   cost/time table as the economic baseline feeding `consulting-benefits-case` (savings are
   measured against these numbers) and `consulting-constraint-analysis` (bottleneck-hunting
   starts from where the cost/time actually is).

---

## Deliverable & templates

**Capacity-cost-rate worksheet**

| Resource pool | Cost of capacity supplied (period) | Theoretical capacity | Practical capacity (~80–85%) | Capacity cost rate ($/min) |
|---|---|---|---|---|
| e.g. AP Clerks | | | | |
| e.g. Approval System | | | | |

**Per-step cost/time table**

| Activity (VSM step) | Driver / time equation | Minutes (per case) | Capacity cost rate | Cost per case |
|---|---|---|---|---|
| e.g. Validate invoice | `beta0 = 4 min; +2 min if new vendor` | 4–6 | $0.85/min | $3.40–$5.10 |
| ... | | | | |

**Roll-up**

```
Total process cost (period)   = sum of activity costs x volume
Cost per case                 = total process cost / case volume
Unused capacity (per pool)    = (practical capacity - capacity used) x capacity cost rate
```

---

## Pitfalls

- **Using theoretical (not practical) capacity.** This understates the rate and hides idle
  capacity — always haircut to ~80–85%.
- **Averaging away real variation.** Forcing one flat unit time across genuinely different
  variants (rush vs. standard, simple vs. complex) produces a misleading average cost; use a
  time equation instead.
- **Costing what was produced, not what was supplied.** Capacity cost rate must use the cost of
  capacity supplied (the resource pool's full cost), not an allocated cost of output — that's
  circular.
- **Skipping the unused-capacity step.** It's the reason to use TDABC over classic ABC; omitting
  it leaves the automation business case with no addressable-cost number to point at.
- **Eyeballing unit times instead of observing them.** Guessed durations are no better than
  survey-driven estimates that don't hold up under scrutiny — always ground unit times in actual
  observation or system timestamps where available, especially those recovered in step 2.
- **Letting time equations sprawl.** A time equation with a dozen driver terms is no easier to
  maintain than a full ABC survey — keep it to the handful of drivers that genuinely explain
  variation, informed by the variants process mining actually surfaced.

---

## Related

- **In-suite** — `consulting-boundary-setting` (step 1, upstream): supplies the scoped VSM steps this skill costs and times. `consulting-process-recovery` (step 2, upstream): supplies the real variants that drive the time equations. `consulting-benefits-case` (step 10, downstream): measures automation savings against this cost/time baseline. `consulting-constraint-analysis` (step 8, downstream): uses the cost/time table to help locate the actual bottleneck.
- **Elsewhere in the library** — `creating-financial-models`, `capacity-modeling`, `variance-analysis`.
- **References** — Kaplan, R. S. & Anderson, S. R., "Time-Driven Activity-Based Costing," *Harvard Business Review*, November 2004; *Time-Driven Activity-Based Costing* (Kaplan & Anderson, Harvard Business School Press, 2007).
