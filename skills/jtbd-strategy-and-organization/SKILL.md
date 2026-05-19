---
name: jtbd-strategy-and-organization
description: >
  Apply JTBD to strategy and organization: Ulwick's Growth Strategy Matrix
  (better/worse × cheaper/expensive), Ansoff Matrix, Surviving Disruption
  Canvas (Christensen), Diffusion of Innovations (Rogers' 5 heuristics),
  Fogg Behavior Model (Motivation × Ability × Prompts), Arenas based on
  jobs (Rita McGrath), Shared Value (Porter & Kramer), organizing teams
  around jobs (Spotify-inspired squads), customer onboarding into the job,
  cancellation interviews, support reframed as job-resolution. Use when
  setting product strategy with JTBD lens, organizing teams around customer
  outcomes, designing onboarding for job completion, or reducing churn.
  Triggers: "JTBD growth strategy", "Ansoff matrix", "Surviving Disruption",
  "Diffusion of Innovations", "Fogg Behavior Model", "organize around
  jobs", "onboard into the job", "JTBD support strategy". Produces a
  strategic / organizational application of JTBD.
---

# JTBD Strategy and Organization

You apply Jim Kalbach's strategic and organizational chapters of *The
Jobs to be Done Playbook*: JTBD isn't just for research — it's a substrate
that aligns product strategy, marketing, support, onboarding, and team
organization around the customer's actual progress.

---

## When to Use This Skill

- Setting product strategy through a JTBD lens
- Organizing teams around customer jobs (vs feature areas)
- Designing onboarding that drives customers to job completion
- Reducing churn via job-aligned support
- Identifying disruption threats and defenses
- Predicting adoption of a new product/feature
- Reframing competition (solution-agnostic)

---

## JTBD Growth Strategy Matrix (Tony Ulwick)

```
                     Gets job done...
                BETTER           WORSE
              ┌────────┬─────────┐
   COSTS     │  GROW   │ DROP    │
   MORE      │ Premium │ "Why    │
              │         │ exist?" │
              ├─────────┼─────────┤
   COSTS     │  WIN    │ DEFEND  │
   LESS      │ Disrupt │ Churn   │
              │         │ risk    │
              └─────────┴─────────┘
```

| Quadrant | Strategy |
|---|---|
| **WIN** (better + cheaper) | Disruption. Rare; if real, dominate. |
| **GROW** (better + expensive) | Premium positioning. Justify price via outcome. |
| **DEFEND** (worse + cheaper) | Survive on cost; vulnerable to disruption. |
| **DROP** (worse + expensive) | Existential question — why does the product exist? |

**Use when:** Comparing your offering against competition on a job-by-job basis. Different jobs may put you in different quadrants.

---

## Ansoff Matrix (Classical)

```
                Existing market    New market
              ┌────────────────┬─────────────┐
EXISTING     │ Market         │ Market       │
PRODUCT      │ Penetration    │ Development  │
              ├────────────────┼─────────────┤
NEW          │ Product        │ Diversifi-   │
PRODUCT      │ Development    │ cation       │
              └────────────────┴─────────────┘
```

**JTBD layer:**
- "Existing market" = same job performers
- "New market" = new job performers (potentially same job)
- "Existing product" = same solution
- "New product" = new solution (same job or new job)

**Riskiest:** Diversification (new product, new market). JTBD reframes: same job in adjacent contexts is less risky than truly new job in new market.

---

## Surviving Disruption Canvas (Christensen)

A canvas (from *Surviving Disruption*) that identifies:
- Jobs overlapping with low-quality competition (you may be over-serving)
- Disruption barriers you're relying on (do they hold?)
- Your defensible asymmetries

**When valuable:** Mature product. Low-end disruptors emerging. Need to assess threat.

---

## Diffusion of Innovations (Everett Rogers)

Five heuristics that predict adoption rate:

| Heuristic | Question | Drives adoption? |
|---|---|---|
| **Relative advantage** | Does it solve the job better than current? | Yes |
| **Compatibility** | Does it fit existing values, experiences, infrastructure? | Yes |
| **Complexity** | How hard to understand and use? | NO |
| **Trialability** | Can users try without commitment? | Yes (low barrier) |
| **Observability** | Can others see results? | Yes |

**JTBD application:** When evaluating a new offering's adoption, score each heuristic. Low scores = friction; design to address.

---

## Fogg Behavior Model

```
          Behavior = Motivation × Ability × Prompt

If any one is zero, no behavior happens.
```

| Element | What it requires |
|---|---|
| **Motivation** | The customer wants the outcome (the job is real) |
| **Ability** | The customer can actually do it (low friction) |
| **Prompt** | The customer is reminded / triggered at the right moment |

**JTBD usage:**
- Motivation = job exists; tied to Push of situation
- Ability = product makes job easy to complete
- Prompt = surface the action when relevant context occurs

**Diagnostic:** A feature underused? Check which of M/A/P is missing. Often it's prompts (right thing, wrong time).

---

## Arenas Based on Jobs (Rita McGrath)

McGrath argues that traditional industry boundaries are obsolete. Markets are defined by **outcomes customers seek**, not industry classifications.

**Example:** "Get to work each day."
- Old industry frame: car-makers compete with car-makers
- Arena frame: cars vs subway vs bike vs work-from-home vs ride-share

**JTBD lens:** Solution-agnostic competition is the rule. Map your Arena by the job, not your category.

---

## Shared Value (Porter & Kramer)

Revenue creation linked to social benefit. Companies fit into the customer's broader life context.

**JTBD overlap:** When you design for the job in context, you naturally consider broader impact. A product that wins the job and improves customer's broader life beats one that only wins the job.

---

## Organizing Teams Around Jobs

Inspired by Spotify's tribes/squads model. **Align teams to customer jobs**, not functional silos.

```
TRADITIONAL                       JTBD-ALIGNED

[Frontend Team]                   [Job: Onboard team]
[Backend Team]                       — Designer
[Mobile Team]                        — Frontend dev
[QA Team]                            — Backend dev
                                     — PM
                                     — UX Researcher
                                  
                                  [Job: Migrate-data team]
                                  [Job: Run-recurring-reports team]
```

**Pros:** Each team owns customer outcomes end-to-end. Faster value delivery. Clear accountability.

**Cons:** Needs strong technical platform (or duplication). Cross-job coordination required for shared infra.

**Practical hybrid:** Squads aligned to jobs; chapters/guilds for technical disciplines (frontend chapter, backend chapter, etc.). Spotify's actual model.

---

## Customer Onboarding Into the Job

Don't onboard customers into the **product**. Onboard them into the **job**.

| Bad onboarding | Good onboarding |
|---|---|
| "Here are 12 features. Click around!" | "First, let's complete your first $JOB. We'll show 3 features along the way." |
| Tutorial focused on UI | Tutorial focused on outcome |
| Ends at "you've completed setup" | Ends at "you've achieved $OUTCOME for the first time" |

**Time to Value (TTV)** = time from signup to first job completion. Measure it. Optimize it.

**Sequence:**
1. Identify what customers struggle with most (Switch interviews of churned trial users)
2. Close the biggest knowledge gap first
3. Demonstrate solution capabilities while completing the job
4. Reach a "first success" moment within the first session if possible

---

## Cancellation as Job Mismatch

**Reframe churn:** Customers cancel when their job changes (new context, new performer) or when your product no longer wins their job.

**Reduce churn via:**
- Inverted Switch interviews on cancellers (see fundamentals skill)
- Onboarding designed for job completion (not feature exploration)
- Account management focused on outcomes ("did the job get done last quarter?")
- Surface job-completion metrics to customers (recurring proof of value)

**Maximize retention** by:
- Ongoing job-completion conversations
- Pre-emptive identification of accounts with job-mismatch signals
- Proactive outreach when usage patterns suggest the job has shifted

---

## Support Reframed

Traditional support: fix product issues.
JTBD support: **help customers complete their job.**

**Listen for the job:**
- Customer asks "how do I export to PDF?" — what job? Probably "share results with someone external."
- Don't just answer the literal question. Confirm the job. Maybe a different feature serves the job better.

**Resolution criterion:** Job done, not ticket closed.

**Result:** Higher CSAT; more product education; identification of feature gaps.

---

## Principles

- **JTBD is a substrate, not a research method.** It runs through strategy, marketing, product, support, org design.
- **Solution-agnostic competition.** Map by job, not category.
- **Teams align to jobs, not functions** (where possible).
- **Onboard into the job, not the product.**
- **Time to Value is a key metric.** Measure; optimize.
- **Listen for the job in support tickets.**
- **Cancellation = job mismatch.** Diagnose accordingly.
- **Adoption requires: relative advantage + compatibility + low complexity + trialability + observability.**
- **Behavior = Motivation × Ability × Prompt.** All three.

---

## Anti-Patterns

### JTBD Research Without Strategic Application

**Looks like:** Run JTBD interviews. File the report. Roadmap unaffected.

**Why it fails:** Insights without application don't compound.

**The fix:** Tie research to specific strategic decisions. ODI Opportunity Map → roadmap; Switch findings → onboarding redesign; Cancellation interviews → retention strategy.

### Design Thinking Only

**Looks like:** Adopt design thinking; expect transformation.

**Why it fails:** Without organizational practice change, design thinking yields beautiful artifacts no one acts on.

**The fix:** Combine design thinking with JTBD as the substrate. Aligns research, strategy, and execution.

### Cutting Corners on Needs Analysis

**Looks like:** "We don't have time for full ODI." 5 chats; everyone declares understanding.

**Why it fails:** Inconclusive findings; speculation; missed opportunities.

**The fix:** Right-size the rigor to the stakes. High-stakes innovation deserves full ODI.

### Demographic-Based Personas

**Looks like:** "Marketing Mary, 35-44, suburban..." with no job articulation.

**Why it fails:** Doesn't predict behavior or guide decisions.

**The fix:** Goal-based personas. Demographics for media targeting; jobs for design.

### Onboarding That's a Feature Tour

**Looks like:** "Here are all our features! Try them!"

**Why it fails:** Customer's job is forgotten. Time to Value extended. Drop-off.

**The fix:** Onboard into the customer's first job. Show only the features needed for that. Defer the rest.

### Support That Closes Tickets, Not Jobs

**Looks like:** SLA on response time. Resolution = ticket closed.

**Why it fails:** Ticket can be closed without job done.

**The fix:** Resolution = job done. Track. CSAT after the customer's outcome occurs, not after the ticket closes.

### Functional Silos Slowing Job Delivery

**Looks like:** Frontend + Backend + Mobile + DevOps all separate. Every job needs all of them. Coordination overhead enormous.

**Why it fails:** Slow value delivery; ownership unclear.

**The fix:** Squads aligned to jobs. Chapters for technical discipline expertise. Spotify-style.

### Innovation Roadmap Driven by Loudest Customer

**Looks like:** Roadmap = sum of feature requests from biggest customers.

**Why it fails:** Big customers may not be representative; their requests are solutions, not jobs.

**The fix:** ODI Opportunity Map drives roadmap. Big customers' requests are inputs; underserved outcomes are the directives.

---

## Decision Rules

| Situation | Action |
|---|---|
| Strategic positioning vs competition | Map jobs; place self in JTBD Growth Matrix |
| Adjacency exploration | Ansoff with JTBD lens — same job, different market |
| Disruption threat from low-end | Surviving Disruption Canvas |
| Predicting adoption | Score Diffusion of Innovations heuristics |
| Feature underused | Diagnose Fogg model — Motivation, Ability, Prompt? |
| Defining the market | Arenas (McGrath) — by job, not industry |
| Org design | Squads aligned to jobs; chapters for technical discipline |
| Onboarding flow | Anchor on first job completion; minimize TTV |
| Reducing churn | Inverted Switch interviews; identify job-mismatch patterns |
| Support strategy | Train on job-listening; resolution = job done |
| Tackling churn from "didn't use enough" | Job-completion metrics surfaced to customers; account management focused on outcomes |
| Product roadmap | Drive from underserved outcomes (ODI), not feature requests |
| Marketing positioning | Sell job completion, not features |
| Big enterprise customer demanding feature | Probe job; alternative solutions might serve better |

---

## Worked Example: Reorganizing a Product Team Around Jobs

**Context:** B2B SaaS, 60-person product org. Functional silos (Frontend, Backend, Mobile, QA, DevOps). Ship velocity slow. Cross-team coordination frustrating.

**Diagnosis:** Functional org optimizes for technical specialization. Customer outcomes require all functions. Coordination tax is enormous.

**Reorganization plan:**

| Job (from customer research) | Squad |
|---|---|
| "Onboard a new team to our platform" | Onboarding Squad |
| "Migrate data from competitor" | Migration Squad |
| "Run recurring reports" | Reporting Squad |
| "Integrate with our existing tools" | Integrations Squad |
| "Get help when stuck" | Support Experience Squad |

Each squad: Designer + Frontend + Backend + Mobile (if applicable) + PM + UX researcher.

**Cross-cutting chapters:**
- Frontend Chapter (frontend devs across squads)
- Backend Chapter
- Design Chapter
- Etc.

**Result:** 6 months in, ship velocity up 40%. Each squad owns end-to-end outcomes. Cross-squad coordination needed for shared infra; addressed via a Platform Squad.

**Lesson:** Functional silos are technical specialization optimized; squads are customer outcome optimized. For most B2B/B2C SaaS, squads win once the team scales beyond ~30 engineers.

---

## Gotchas

- **Squad model needs strong platform investment.** Otherwise duplication kills velocity.
- **Spotify model is often misunderstood.** Spotify themselves moved beyond it. Use as inspiration, not gospel.
- **JTBD-driven roadmap can frustrate execs** who want feature lists.
- **Support team transformation is hard.** Listening for the job requires training and culture shift.
- **Onboarding redesign is high-leverage.** Often the single biggest churn lever.
- **Time to Value depends on definition.** "First Login" is not job completion.
- **Diffusion of Innovations applies to internal adoption too.** New tooling within your company succeeds via the 5 heuristics.
- **Fogg model + JTBD pairs well.** Job = motivation; product = ability; UI/notifications = prompts.

---

## Further Reading

- *The Jobs to be Done Playbook* by Jim Kalbach
- *Surviving Disruption* by Christensen + Wessel
- *Diffusion of Innovations* by Everett Rogers
- *Tiny Habits* by BJ Fogg (Behavior Model)
- *The End of Competitive Advantage* by Rita Gunther McGrath (Arenas)
- *Team Topologies* by Skelton & Pais (squad organization)
- See `jtbd-fundamentals-and-interviewing` for upstream research methods
- See `outcome-driven-innovation-and-job-mapping` for ODI prioritization

Source: *The Jobs to be Done Playbook* (Kalbach), strategic + organizational chapters.
