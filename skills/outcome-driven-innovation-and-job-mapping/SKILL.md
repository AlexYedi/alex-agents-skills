---
name: outcome-driven-innovation-and-job-mapping
description: >
  Apply Outcome-Driven Innovation (ODI, Tony Ulwick) and Job Mapping (Lance
  Bettencourt + Anthony Ulwick): identify the main job, build the 8-phase
  Job Map (Define → Locate → Prepare → Confirm → Execute → Monitor → Modify
  → Conclude), write desired outcome statements (direction + unit + object
  + context), prioritize underserved outcomes, write Job Stories ("When
  [situation], I want [motivation], so I can [outcome]"), apply Job Stories
  Canvas, JTBD Canvas, Value Proposition Canvas. Use when running
  innovation prioritization, mapping a customer's complete job, writing
  precise opportunity statements, or building product specs from JTBD.
  Triggers: "Outcome-Driven Innovation", "ODI", "Tony Ulwick",
  "job map 8 phases", "desired outcome statement", "Job Stories", "JTBD
  Canvas", "Value Proposition Canvas". Produces a job map + prioritized
  outcomes + job stories.
---

# Outcome-Driven Innovation and Job Mapping

You apply Tony Ulwick's *Outcome-Driven Innovation* methodology with
Lance Bettencourt's Job Map: structured, repeatable innovation by mapping
the customer's main job, identifying every desired outcome, and
prioritizing where the gap between importance and current satisfaction is largest.

---

## When to Use This Skill

- Running an innovation initiative needing rigor (not "let's brainstorm features")
- Mapping a customer's complete job for product or service design
- Writing opportunity statements precise enough to guide engineering
- Prioritizing where to invest in product improvements
- Translating JTBD interviews into actionable specs
- Differentiating against competitors via underserved-need analysis

---

## ODI in Four Phases

```
1. IDENTIFY THE JOB    → What's the main functional job?
2. CREATE A JOB MAP    → Break it into the standard 8 phases
3. DEFINE OUTCOMES     → Desired outcome statements per phase
4. QUANTIFY THE MARKET → Survey to score importance + satisfaction
                          → Prioritize underserved outcomes
```

ODI is high-effort. It's the rigorous method. Use it when stakes warrant the investment.

---

## The 8-Phase Job Map

```
DEFINE → LOCATE → PREPARE → CONFIRM → EXECUTE → MONITOR → MODIFY → CONCLUDE
```

| Phase | What the customer does | Example (gardening) |
|---|---|---|
| **Define** | Determine objectives, plan approach | "Decide what to plant this season" |
| **Locate** | Gather inputs and tools | "Acquire seeds, soil, gear" |
| **Prepare** | Set up environment | "Till soil, prepare beds" |
| **Confirm** | Verify readiness | "Check weather forecast, soil pH" |
| **Execute** | Perform the core activity | "Plant seeds" |
| **Monitor** | Assess progress | "Check growth daily, look for pests" |
| **Modify** | Adjust based on monitoring | "Add water, fertilizer, prune" |
| **Conclude** | Wrap up; finalize | "Harvest, store, plan for next season" |

**Customers experience friction in each phase.** Innovation opportunities live in identifying which phases are underserved.

---

## Desired Outcome Statements

A precise format for opportunities. Four elements:

```
Minimize | Increase     [Direction]
the time it takes        [Unit of Measure]
to identify which seeds  [Object of the need]
will thrive in my soil   [Context]
type and climate
```

**Each element is required:**

| Element | Purpose |
|---|---|
| Direction | Minimize / Increase / Eliminate (gives the goal) |
| Unit of Measure | Time, frequency, distance, cost (makes it measurable) |
| Object of the need | What's being measured (must be objective) |
| Context | When/where/who (specific situation) |

**Why this format:** Vague statements ("better seed selection") can't be tested. Precise statements ("minimize the time to identify which seeds will thrive given my zip code") can be quantified.

### Outcome Statement Examples

| Domain | Outcome statement |
|---|---|
| Online tax filing | Minimize the time it takes to determine which deductions apply given my employment situation |
| Streaming TV | Increase the likelihood of finding content I'll enjoy given my mood |
| B2B SaaS onboarding | Minimize the time from signup to my first measurable success |
| Restaurant booking | Increase the likelihood that the table will be ready when I arrive |

---

## Quantifying the Market

After collecting desired outcomes (typically 50-150 per main job), survey actual job performers:

- **Importance:** "How important is this outcome to you?" (1-10)
- **Satisfaction:** "How satisfied are you with how well it's met today?" (1-10)

Compute **opportunity score:**

```
Opportunity = Importance + max(Importance - Satisfaction, 0)
```

| Importance | Satisfaction | Opportunity | Status |
|---|---|---|---|
| 9 | 9 | 9 | Met (low opportunity) |
| 9 | 3 | 15 | **Underserved (high opportunity)** |
| 3 | 9 | 3 | Overserved (cost-cut opportunity) |
| 3 | 3 | 3 | Low-priority |

**Underserved outcomes are where innovation pays off.** Overserved are where you can simplify / cut features without losing value.

---

## Job Stories

A user-story format **derived from JTBD**, replacing generic "As a user, I want..." with situation-aware framing.

```
When [SITUATION],
I want to [MOTIVATION],
so I can [EXPECTED OUTCOME].
```

### Examples

**Generic user story:**
> "As a user, I want to filter the dashboard."

**Job Story:**
> "When I'm reviewing weekly performance and the meeting starts in 5 minutes, I want to filter the dashboard to my own team's metrics, so I can focus the discussion on what we control."

The job story:
- Anchors the situation (timing, urgency)
- Names the motivation (the job)
- States the desired outcome (success criterion)

### When to use Job Stories vs Desired Outcomes

| Format | When |
|---|---|
| **Desired outcome statement** | Innovation prioritization; survey-based scoring |
| **Job Story** | Engineering brief; sprint planning; design discussion |

They compose. Outcome statements drive prioritization; job stories operationalize.

---

## JTBD Canvas (Daniel Silverstein-inspired)

A one-pager that splits a job into its components:

```
┌────────────────────────────────────────┐
│ JOB:                                    │
│ "When ..., I want to ..., so I can ..."│
├──────────────────┬─────────────────────┤
│ Functional needs │ Emotional needs     │
│                  │                     │
│ - ...            │ - ...               │
│ - ...            │ - ...               │
├──────────────────┴─────────────────────┤
│ Job Performer: ...                      │
│ Context / Situation: ...                │
│ Forces (Push, Pull, Anxiety, Habit): ...│
└─────────────────────────────────────────┘
```

**When:** Aligning a small team on a specific job before sprint work.

---

## Value Proposition Canvas (Strategyzer)

Alexander Osterwalder + Yves Pigneur's tool. Aligns:

```
[Customer Profile]                        [Value Map]
                                         
Customer Jobs   ◄─matches──► Pain Relievers
Pains           ◄─matches──► Gain Creators
Gains           ◄─matches──► Products & Services
```

**JTBD usage:** The "Customer Jobs" section of the canvas comes directly from JTBD interviews. Pains and Gains are layered on top.

---

## Hypothesis Progression Framework (HPF)

Travis Lowdermilk + Jessica Rich's four-stage model from *The Customer-Driven Playbook*:

```
1. Customer hypothesis    — Who is the customer? What's their job?
2. Problem hypothesis     — What problem are we solving for them?
3. Concept hypothesis     — What solution might solve the problem?
4. Feature hypothesis     — What features would make the solution work?
```

Each stage is **tested before moving on.** Failing tests means going back, not skipping forward.

---

## Goal-Driven Personas (Alan Cooper)

Personas defined by:
- Goal/job-based behavior variables (not demographics)
- Specific, observable, varying across users

**Example:**
- "Wants to organize finances for tax season" (job-based) ✓
- "35-44, suburban, college-educated" (demographics) ✗

**Why:** Demographics correlate with jobs imperfectly. A 25-year-old and a 65-year-old can share a job ("simplify tax filing") and need the same product affordances.

---

## Consumption Journey Maps

Distinct from Job Maps. Job Map covers **the main job**. Consumption Journey covers **interactions with your specific solution**.

```
Find → Decide → Acquire → Set up → Use → Renew/leave
```

**Use both:**
- Job Map for "what's the customer trying to do overall"
- Consumption Journey for "how is our specific product helping or hindering"

---

## Principles

- **Customer Jobs are stable; solutions evolve.** Map jobs once; reuse over years.
- **Functional first.** Don't layer emotional/social before solving the functional job.
- **Outcomes are measurable.** Direction + unit + object + context.
- **Underserved outcomes are innovation gold.** Importance high; satisfaction low.
- **Overserved outcomes are simplification opportunities.**
- **Job stories operationalize; outcome statements prioritize.**
- **Goal-based personas, not demographic.**
- **Hypothesis-test before building.**
- **Consumption journey ≠ job map.** Use both.

---

## Anti-Patterns

### Cutting Corners on Needs Analysis

**Looks like:** "We've talked to a few customers; we know what they need." 12-15 informal chats; no rigorous methodology.

**Why it fails:** Inconclusive findings; speculation; missed needs.

**The fix:** Full ODI process for high-stakes innovation. Or at least 30-50 jobs interviews before claiming you understand the job.

### Vague Outcome Statements

**Looks like:** "Better customer experience." "Easier onboarding." "Faster support."

**Why it fails:** Untestable, unprioritizable, doesn't drive design.

**The fix:** Direction + unit + object + context. Every outcome statement has all four.

### Generic User Stories Without Context

**Looks like:** "As a user, I want to filter the list, so I can find items."

**Why it fails:** Doesn't anchor situation. Loses the why.

**The fix:** Job Story format with situation, motivation, outcome.

### One Job Map for Everyone

**Looks like:** Single Job Map applied to all customer segments.

**Why it fails:** Different segments may have different jobs, or the same job in different contexts.

**The fix:** Job Map per segment if jobs differ. Or per main job if you serve multiple.

### Personas Decorated With Stock Photos

**Looks like:** "Marketing Mary" — name, photo, hobbies, age, salary. No job articulation.

**Why it fails:** Decorative. Doesn't predict behavior or guide design.

**The fix:** Goal-based personas. Lead with the job, not the photo.

### Surveying Importance Without Satisfaction

**Looks like:** "Rate the importance of these outcomes." Score "all important." No prioritization.

**Why it fails:** Importance alone doesn't surface opportunity.

**The fix:** Importance × Satisfaction. Underserved (high importance, low satisfaction) is the opportunity.

### Skipping the Job Map

**Looks like:** Going straight from "main job" to "feature ideas."

**Why it fails:** Misses phase-by-phase opportunities. Innovation lives in specific phases.

**The fix:** Always map the 8 phases. Outcomes per phase.

### Static ODI Output

**Looks like:** ODI study completed once; outputs filed. Reused without updating.

**Why it fails:** Customer jobs and contexts evolve.

**The fix:** Re-interview annually; refresh outcome scoring; track shifts.

---

## Decision Rules

| Situation | Action |
|---|---|
| High-stakes innovation | Full ODI methodology |
| Engineering brief | Job Stories with situation/motivation/outcome |
| Innovation prioritization | Desired Outcome Statements + Importance × Satisfaction survey |
| Feature ideation | Anchor on underserved outcomes from prior survey |
| Sprint planning | Job Stories per ticket |
| Persona work | Goal-based; not demographic |
| Mapping a complex job | 8-phase Job Map |
| Aligning small team on a job | JTBD Canvas one-pager |
| Building product positioning | Value Proposition Canvas |
| Hypothesis-driven product | HPF (Customer → Problem → Concept → Feature) |
| Find vs use vs renew flow | Consumption Journey Map (separate from Job Map) |
| "Better X" outcome statement | Refine to direction + unit + object + context |
| Same job for two segments | Confirm; might be different jobs requiring different products |
| ODI feels too heavy | Use lighter Job Stories + Switch interviews; reserve full ODI for major bets |

---

## Worked Example: ODI for a B2B Procurement SaaS

**Context:** Procurement SaaS company. Want to prioritize next year's product investment. Heavy ODI investment justified.

**Process:**

| Phase | Activity |
|---|---|
| 1. Identify Job | Jobs interviews with 30 procurement managers. Main job: "Get the right goods/services purchased on time at the right price." |
| 2. Job Map | 8 phases mapped. Define = "Determine what to buy." Conclude = "Confirm receipt and invoice." |
| 3. Define Outcomes | 87 desired outcomes statements collected across phases (e.g., "Minimize the time to identify approved suppliers for a category given my company's policies"). |
| 4. Quantify | Survey of 200 procurement managers. Score Importance + Satisfaction. |

**Top underserved outcomes (opportunity score):**

| Outcome | Importance | Satisfaction | Opportunity |
|---|---|---|---|
| Minimize time to identify approved suppliers in policy compliance | 9.2 | 4.1 | 14.3 |
| Minimize likelihood of duplicate purchase orders | 8.8 | 5.5 | 12.1 |
| Increase visibility into spend by category | 9.0 | 6.5 | 11.5 |

**Top overserved outcomes (simplification candidates):**

| Outcome | Importance | Satisfaction | Opportunity |
|---|---|---|---|
| Generate procurement reports for finance department | 4.0 | 9.5 | 4.0 |
| Print purchase orders | 2.5 | 9.5 | 2.5 |

**Action plan:**
- Invest in supplier discovery + policy match (top opportunity)
- Build duplicate-PO detection
- Improve spend visibility dashboards
- Cut investment in reporting tools (overserved)
- Sunset print-PO feature (overserved + low importance)

**Result:** Following year's roadmap is data-driven. Marketing can target "supplier discovery friction" — a real customer pain.

**Lesson:** ODI is heavy upfront, but pays off in years of clearer prioritization. The opportunity-score map is the most valuable artifact a product team can have.

---

## Gotchas

- **ODI is expensive.** Full study can be $100K+ with consultants. Worth it for major innovation; overkill for incremental.
- **50+ outcomes per job is normal.** Don't truncate to 10 — you'll miss the underserved.
- **Survey panel quality matters.** Job performers must be real, recent, and representative.
- **Importance scores often cluster high.** Differentiate with satisfaction.
- **Different segments may have different opportunity maps.** Segment by job, not demographics.
- **Outcome statements take practice.** Direction + unit + object + context isn't intuitive at first.
- **Job Stories without situation are just user stories.** The "When..." is essential.
- **Job Map ≠ workflow.** Job Map is what the customer is trying to accomplish; workflow is your product's flow. They differ.
- **Tony Ulwick's books and Strategyn are the canonical ODI source.** Lots of consultants offer "ODI-lite"; verify rigor.

---

## Further Reading

- *Jobs to Be Done: Theory to Practice* by Tony Ulwick (canonical ODI)
- *What Customers Want* by Tony Ulwick (earlier ODI articulation)
- *The Jobs to be Done Playbook* by Jim Kalbach (broader JTBD overview)
- *The Customer-Driven Playbook* by Lowdermilk + Rich (HPF)
- *Value Proposition Design* by Osterwalder et al.
- See `jtbd-fundamentals-and-interviewing` for the upstream interview methodology
- See `jtbd-strategy-and-organization` for applying ODI to strategy + org

Source: *The Jobs to be Done Playbook* (Kalbach) + ODI references.
