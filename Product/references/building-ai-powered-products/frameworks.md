# Frameworks: Building AI-Powered Products

**Source:** *Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management* by Marily Nika, PhD

A catalog of every framework introduced or applied in this book, with structure,
when-to-apply, and cross-references between frameworks. Use this when:
- You vaguely remember a framework name and need its structure
- You're applying one framework and want to know what else combines well with it
- You're choosing between framework variants

---

## Framework Index (Alphabetical)

| Framework | Domain | When to apply |
|---|---|---|
| AIPDL (AI Product Development Lifecycle) | Product process | Any AI product effort |
| AI Algorithms Map | Domain modeling | Mapping technology to use cases |
| AI MVP Requirements | Validation | Building first AI product iteration |
| AI PM Career Ladder | Career planning | Self-assessment, hiring rubrics |
| AI PM Skill Set Buckets | Skill development | Personal growth roadmapping |
| AI Product Metric Blend | Measurement | Setting OKRs and dashboards |
| AI Superpowers (Capability taxonomy) | Ideation | Mapping AI capabilities to user pains |
| Agent Type Taxonomy | Agent architecture | Choosing agent class for a use case |
| Agent UI Patterns | Agent UX | Designing agent surfaces |
| Autonomy Spectrum | Agent governance | Defining where on the spectrum to operate |
| Build-versus-Buy Decision Matrix | Strategic decisions | Architecture and resourcing choices |
| Cross-Functional Collaboration Model | Team design | Cross-functional setup for AI products |
| Direct vs Indirect Monetization | Go-to-market | Pricing decisions for AI features |
| Hybrid Approach (Build + Buy) | Strategic decisions | When pure build or pure buy doesn't fit |
| Innovator's Dilemma (Christensen) | Strategic positioning | Disruptive vs sustaining innovation calls |
| Model Adaptation Methods | Technical approach | Fine-tune / RAG / Grounding selection |
| Monetization Strategies | Go-to-market | Direct vs indirect framing |
| North Star Metric (for AI) | Measurement | Picking the single core KPI |
| OKR Framework for AI Products | Goal-setting | Quarterly/annual goal cycles |
| Product-Market Fit Three Pillars | Validation | Opportunity-stage gating |
| Product Review Template | Stakeholder management | Leadership reviews and decisions |
| Proactivity vs Reactivity | Agent design | Defining agent activation triggers |
| RICE Framework | Prioritization | Feature backlog ranking |
| Six-Step Trade Space Guide | Trade-off analysis | Cross-functional priority alignment |
| Synthetic vs Real-World Data Strategy | Data strategy | Choosing data sourcing approach |
| Trade Space (Concept) | Trade-off analysis | Visualizing competing constraints |

---

## Framework Catalog (Detailed)

### AIPDL (AI Product Development Lifecycle)

**Originator:** Marily Nika (this book)

**Structure:** Five iterative stages:
1. Ideation — develop initial concept; identify AI features for target user segment
2. Opportunity — validate the three PMF pillars
3. Concept/Prototype — build AI MVP; achieve Minimum Viable Quality (MVQ)
4. Testing & Analysis — gather feedback; validate ethics; measure
5. Rollout — launch + post-deployment monitoring

**Reiteration rule:** Reiterate from any stage as needed; only proceed past
Concept/Prototype after achieving MVQ.

**Cross-references:**
- Uses **RICE** in the Ideation stage
- Uses **PMF Three Pillars** in the Opportunity stage
- Uses **AI MVP Requirements** in the Concept/Prototype stage
- Uses **AI Product Metric Blend** in Testing & Analysis and Rollout

**When to apply:** Any AI/ML product effort. Differs from traditional SDLC because
the data + model + evaluation loop is part of the product, not just code.

---

### RICE Framework (applied to AI features)

**Originator:** Standard PM tool, applied to AI in this book

**Structure:**
- **Reach:** Number of users affected within a time window
- **Impact:** Effect on key metrics (3=high, 2=medium, 1=low, 0.5=minimal)
- **Confidence:** Certainty in your estimates (% backed by data)
- **Effort:** Total work in person-months

**Formula:** `RICE = (Reach × Impact × Confidence) / Effort`

**AI-specific adjustment:** Confidence weighting matters more in AI than in
typical features, because data and algorithm feasibility are often unknown
at ideation. A high-Confidence feature is one where similar implementations
have shipped before.

**Cross-references:**
- Used inside **AIPDL Ideation stage**
- Confidence column reveals **Hunch-Driven Pitching** anti-pattern (see additional-experts.md)

---

### Product-Market Fit Three Pillars

**Originator:** Andreessen-derived, applied to AI in this book

**Structure:** Three simultaneous criteria, all required:

| Pillar | Validation method |
|---|---|
| Business Viability | Market sizing, competitive analysis, ROI estimation, regulatory audit (GDPR/EU AI Act/HIPAA) |
| Technical Feasibility | Engineering review, data availability check, compute cost estimation |
| User Desirability | Surveys, interviews, MVP A/B testing, Van Westendorp Pricing Model |

**Visual:** Three intersecting circles; PMF only at the intersection of all three.

**Cross-references:**
- Validation gate at **AIPDL Opportunity stage**
- Revisited during **AIPDL Testing & Analysis stage**

---

### AI MVP Requirements (4-part contract)

**Originator:** Marily Nika (extending Eric Ries's MVP)

**Structure:** An AI MVP must satisfy all 4:
1. **Demonstrate low-effort integration** with existing systems (API, sample integration layer)
2. **Showcase domain-specific expertise** via a small but high-quality dataset relevant to target vertical
3. **Add value from day one** — operational efficiency, personalization, or actionable insights from the start
4. **Include a feedback loop** demonstrating learning (e.g., capturing which recommendations users click)

**Cross-references:**
- Used at **AIPDL Concept/Prototype stage**
- Differs from software MVP (Eric Ries) — software MVPs can promise value; AI MVPs must deliver from day one

**Hardcoding allowance:** Hardcode un-essential paths (e.g., predefined chatbot
responses for common queries) while training only the differentiating capability.

---

### AI Product Metric Blend

**Originator:** Marily Nika (this book)

**Structure:** Three metric buckets + 1 North Star + 2-3 Guardrails:

```
                    NORTH STAR (1)
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
   PRODUCT HEALTH    SYSTEM HEALTH      AI PROXY
   (engagement,      (latency, uptime,  (accuracy,
    retention,        error rate,        precision/recall,
    NPS)              cost/req)          drift)

       └─────────── GUARDRAILS (2-3) ──────────┘
       (complaint rate, p99 latency, bias signals)
```

**Cross-references:**
- Realized through the **AI Product OKR Framework**
- Combines with **North Star Metric (for AI)** at the top

---

### AI Product OKR Framework

**Originator:** Marily Nika (this book)

**Structure:** Each OKR includes:
- 1 metric from each of the three buckets (Product Health, System Health, AI Proxy)
- 1 North Star
- 2-3 Guardrails (hard floors, not goals)
- All KRs must be SMART (Specific, Measurable, Achievable, Relevant, Time-bound)

**Cross-references:**
- Operationalizes the **AI Product Metric Blend**
- Quarterly/annual cadence

---

### Build-versus-Buy Decision Matrix

**Originator:** Standard PM/architecture tool, with AI-specific factors

**Structure:** Score 7 factors:
1. Core competency — is AI central to value prop?
2. Resources/expertise — do you have ML talent + data + 2yr budget?
3. Time to market — urgency?
4. Cost — upfront and ongoing?
5. Risk — regulatory, IP, quality?
6. Data privacy — can you use third-party processing?
7. Competitive differentiation — is the AI capability your moat?

**Decision logic:**
- Build wins on capability + resources + differentiation
- Buy wins on speed + cost + non-differentiation
- **Hybrid Approach** is the answer when factors split

**Cross-references:**
- Combines with **Hybrid Approach** for split decisions
- Strategic decision often made at **AIPDL Ideation/Opportunity intersection**

---

### Hybrid Approach (Build + Buy)

**Originator:** Marily Nika (this book)

**Structure:** Build core differentiating AI in-house; leverage third-party
solutions for non-essential or supplementary capabilities.

**Examples (from book and common practice):**
- Health-tech: build proprietary diagnostic models in-house; use OpenAI for chat support
- E-commerce: build custom recommendation engine; use commercial NER for product tagging

**When to apply:** When Build vs Buy factors split between build and buy
across different capabilities.

---

### Synthetic vs Real-World Data Strategy

**Originator:** This book (illustrated by Tesla's autonomous driving)

**Structure:** Decision framework for data sourcing:

| Use case | Strategy |
|---|---|
| Sensitive data (PHI, PII, financial) | Synthetic for development, real for production validation |
| Rare scenarios / edge cases | Synthetic to fill the long tail |
| High-stakes decisions (medical, autonomous) | Both — real for fidelity, synthetic for edge case coverage |
| Behavior nuance critical (recommendations, NLP) | Real-world primary; synthetic only as supplement |

**Validation gate:** Synthetic data must maintain statistical properties of
real data; no accidental bias patterns introduced.

**Cross-references:**
- Inputs to the **Model Adaptation Methods** decision (data availability affects fine-tuning vs RAG)
- Discussed in **AIPDL Concept/Prototype stage**

---

### Model Adaptation Methods (Fine-tuning vs RAG vs Grounding)

**Originator:** This book's framing of three industry-standard techniques

**Structure:** Three methods, choose based on accuracy needs vs flexibility:

| Method | Mechanism | Best for | Cost | Iteration speed |
|---|---|---|---|---|
| Fine-tuning | Train pretrained model on specific dataset | Stable narrow tasks needing high precision | High | Slow |
| RAG (Retrieval-Augmented Generation) | Retrieve relevant info at inference | Dynamic info that changes frequently | Medium | Medium |
| Grounding (prompt engineering) | Lightweight adjustments via prompt | Rapid experimentation, pre-MVQ | Low | Fast |

**Decision tree:**
- Information changes frequently? → **RAG**
- Stable narrow task, high precision? → **Fine-tune**
- Pre-MVQ exploration? → **Grounding**

---

### Innovator's Dilemma (applied to AI)

**Originator:** Clayton Christensen, *The Innovator's Dilemma* (Harvard Business Review Press, 1997)

**Structure:**
- **Sustaining innovation:** Improving existing products with AI for current customers (incumbents do this well)
- **Disruptive innovation:** New AI capability that initially looks worse but redefines the market

**Trap:** Today's weak AI model can become tomorrow's dominant standard.
Incumbents kill disruptive AI projects because they underperform on current metrics.

**Detection signal:** Internal critiques like "the AI is less accurate than our
current approach" or "users don't ask for this" — exactly the patterns Christensen described.

**Caveat:** Distinguish *promising-but-immature* from *fundamentally-flawed*.
Not every weak model is disruptive.

**Cross-references:**
- Applied in **Build-versus-Buy** decisions (build for disruptive even when sustaining looks safer)

---

### Direct vs Indirect Monetization

**Originator:** This book

**Structure:**

| Strategy | Mechanism | When to use |
|---|---|---|
| Direct | Charge separately, bundle with price increase, or sell standalone | Strong willingness-to-pay signal; high compute cost; clear added value |
| Indirect | Integrate into existing packages without altering price | Goal is adoption/retention; AI capability still maturing; want to refine before pricing |

**Cross-references:**
- Used at **AIPDL Rollout stage**
- Decision driven by data from **PMF Three Pillars** validation

---

### AI Superpowers (Capability Taxonomy)

**Originator:** This book

**Structure:** Map AI capabilities to user pain. Categories:
- Automating workflows (smarter automation, contextual factors)
- Creative collaboration (brainstorming, idea generation, music/writing/art assistance)
- Immersive and interactive spaces (dynamic adaptive environments)
- Error detection and mitigation (process / content quality)
- Reasoning and intent understanding (interpreting vague/ambiguous user inputs)
- Multimodality (text + audio + images + video)
- Humanlike conversation (natural engaging dialog)

**Cross-references:**
- Used in **AIPDL Ideation stage**
- Inputs to **Agent Type Taxonomy** when designing capability-driven agents

---

### Agent Type Taxonomy

**Originator:** This book, applying classical AI agent theory

**Structure:** Four agent archetypes:
1. **Simple Reflex** — if/then rules, no memory or learning
2. **Goal-Based** — selects options to accomplish defined objectives
3. **Utility-Based** — optimizes a specific metric
4. **General-Purpose** — has internal world model, adapts across domains

**Decision rules:**
- Task-specific with clear if/then logic → Simple Reflex
- Multi-step planning toward objective → Goal-Based
- Optimize a specific metric → Utility-Based
- Multi-domain adaptive behavior → General-Purpose (e.g., LLM-based)

**Cross-references:**
- Combines with **Agent UI Patterns**, **Autonomy Spectrum**, **Proactivity vs Reactivity** for full agent design

---

### Agent UI Patterns

**Originator:** This book

**Structure:** Five common surfaces:

| Pattern | Visibility | Best for |
|---|---|---|
| Side Panel | Always visible, contextual | Continuous assistance during workflow |
| Floating Bubble | Movable icon, summoned by user | Reactive help that doesn't dominate |
| Dedicated Chat Interface | Full conversational space | Complex multi-turn tasks |
| Integrated UI | Seamlessly embedded | Specialized assistance inside existing flow |
| Collaborative Browser Interface | Blends agent autonomy with manual control | Agent operates in user environment |

**Examples (from book and broader practice):**
- Side Panel: Microsoft Copilot in Word/Excel
- Floating Bubble: in-app chat widgets
- Dedicated Chat: ChatGPT, Claude.ai
- Integrated UI: GitHub Copilot inline suggestions
- Collaborative Browser: Browser agents (Anthropic Computer Use)

---

### Autonomy Spectrum

**Originator:** This book

**Structure:** Range from suggestion-only to full automation:

```
[Assistance]──[Suggestion]──[Approval]──[Co-pilot]──[Full Automation]
```

| Level | When to use | Risk profile |
|---|---|---|
| Assistance | New agent, regulated domain | Low |
| Suggestion | Agent provides drafts, user edits and ships | Low |
| Approval | Agent proposes; user approves before execution | Medium |
| Co-pilot | Agent acts on user's behalf with confirmation | Medium-High |
| Full Automation | End-to-end execution | High |

**Default principle:** Graduated autonomy. Start narrow; earn trust by measuring reliability.

---

### Proactivity vs Reactivity

**Originator:** This book

**Structure:**
- **Proactive:** Agent initiates based on context, behavior, or schedule
- **Reactive:** Agent responds only to explicit user invocation

**Default:** Reactive. Earn proactivity by demonstrating value reactively first.

---

### Trade Space (Concept)

**Originator:** This book

**Structure:** A dynamic, shifting landscape of trade-offs unique to a product's
market and organizational goals. Visualized as intersecting constraints defining
a solution space.

**Companion framework:** **Six-Step Trade Space Guide**

---

### Six-Step Trade Space Guide

**Originator:** This book

**Structure:**
1. Identify key factors
2. Rank priorities
3. Map interdependencies
4. Visualize the space
5. Test different scenarios
6. Iterate/adjust based on new information

**When to apply:** Cross-functional priority alignment when multiple stakeholders
have competing demands (quality vs speed, cost vs performance, etc.)

---

### Cross-Functional Collaboration Model

**Originator:** This book

**Structure:** Stakeholder groups required to bring AI products to market:

| Group | Roles |
|---|---|
| AI/ML Teams | ML scientists, red/blue teams, MLOps |
| Operations Teams | Program managers, DataOps |
| Engineering Teams | Developers, testers, data engineers, technical PMs |
| UX Teams | User researchers, UX developers/designers, content specialists |
| Business Teams | Product marketing, sales, partnerships |
| Third-Party Stakeholders | Vendors/OEMs, consultants, research institutions |

**When to apply:** Initial team formation for an AI product; resource planning;
identifying gaps in the team.

---

### AI PM Career Ladder

**Originator:** This book

**Structure (conceptual; actual rungs vary by company):**
- Levels 4-5: Execution-level (day-to-day model performance, OKRs)
- Levels 6-7: AI/ML Product Management (roadmaps, multi-year visions, ML infra strategy)
- Levels 8+: Strategic Leadership (portfolio management, governance, ethics)
- Levels 9+: Top Executive (company-wide AI vision, multi-billion-dollar investments)

**When to apply:** Career planning, hiring rubrics, role scoping.

---

### AI PM Skill Set Buckets

**Originator:** This book

**Structure:** Four skill buckets:

1. **Core PM craft** — user segments, RICE, roadmapping, KPIs/North Star
2. **Engineering foundations** — SDLC, version control, APIs, AI infrastructure
3. **Leadership/collaboration** — experimentation mindset, communication, storytelling
4. **AI lifecycle awareness** — prompt engineering, MLOps, fine-tuning, evals, ethics

**When to apply:** Self-assessment, hiring rubric design, identifying skill gaps.

---

### Product Review Template

**Originator:** This book

**Structure:** Collaborative document for leadership reviews:
- Executive summary with multiple options
- Pros/cons analysis (using + and - symbols)
- Recommendation justification
- Cross-functional alignment on strategic priorities

**When to apply:** Stakeholder reviews where leadership needs to make a decision
between alternatives.

---

### AI Algorithms Map

**Originator:** This book

**Structure:** Conceptual framework categorizing AI technologies:
- **Learning Methods:** Supervised, Self-supervised, Unsupervised, Reinforcement
- **Algorithms/Models:** specific model architectures
- **Applications:** functional uses
- **Use Cases:** business/user-facing applications

**When to apply:** Mapping technology convergence to real-world impacts;
explaining the AI landscape to non-technical stakeholders.

---

## Cross-Reference Map (which frameworks combine)

```
                   ┌──────────────────┐
                   │      AIPDL       │ (top-level lifecycle)
                   └────────┬─────────┘
                            │ uses at each stage:
        ┌──────────┬────────┴────────┬─────────────────┐
        ▼          ▼                 ▼                 ▼
    ┌──────┐  ┌────────┐      ┌─────────┐       ┌─────────┐
    │ RICE │  │  PMF   │      │ AI MVP  │       │ Metric  │
    │      │  │ 3 Pill.│      │ Reqs.   │       │ Blend   │
    └──────┘  └────────┘      └─────────┘       └────┬────┘
                                                      │
                                                      ▼
                                              ┌───────────────┐
                                              │ OKR Framework │
                                              └───────────────┘

  Strategic decisions:
  ┌────────────────┐    ┌──────────────┐    ┌────────────────┐
  │ Build vs Buy   │ ←→ │  Hybrid      │    │ Innovator's    │
  │ Decision Matrix│    │  Approach    │    │ Dilemma        │
  └────────┬───────┘    └──────────────┘    └────────────────┘
           │
           ▼
  ┌────────────────┐    ┌────────────────┐
  │ Synthetic vs   │ ←→ │ Model          │
  │ Real-World Data│    │ Adaptation     │
  │ Strategy       │    │ Methods        │
  └────────────────┘    └────────────────┘

  Agent design (compose all four):
  ┌────────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
  │ Agent Type     │ ←→ │ Agent UI     │ ←→ │ Autonomy     │ ←→ │ Proactivity  │
  │ Taxonomy       │    │ Patterns     │    │ Spectrum     │    │ vs Reactivity│
  └────────────────┘    └──────────────┘    └──────────────┘    └──────────────┘

  Trade-off and team:
  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐
  │ Trade Space    │ ←→ │ 6-Step Trade   │    │ Cross-Functional│
  │                │    │ Space Guide    │    │ Collaboration   │
  └────────────────┘    └────────────────┘    └────────────────┘

  Career and skills:
  ┌────────────────┐    ┌────────────────┐
  │ AI PM Career   │ ←→ │ AI PM Skill    │
  │ Ladder         │    │ Set Buckets    │
  └────────────────┘    └────────────────┘
```

---

## How to use this catalog

- **Vaguely remember a name?** Browse the alphabetical index
- **Picking a framework for a specific decision?** Search by domain
- **Already using one and want to know what combines well?** Check the cross-reference map
- **Need depth on a specific framework?** See the detailed catalog above
- **Need expert advice on applying these?** See `additional-experts.md` in this folder
