# Additional Experts: Building AI-Powered Products

**Source:** *Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management* by Marily Nika, PhD

This reference captures the best practices, advice, and examples that an
experienced AI Product Manager would draw on when guiding a team through
AI product development. Use this alongside the action-focused skills in
`Product/ai-*/SKILL.md`.

---

## About the Expert

**Marily Nika, PhD** is a recognized AI product leader with experience at
Google and Meta on AI-powered consumer products. Her expertise sits at the
intersection of AI/ML, product management, and bringing novel technology to
market. The book reflects her experience shipping AI products in both
0-to-1 (research-led) and 1-to-n (product-enhancement) contexts.

The voice is practical, opinionated, and grounded in real teams. When she
says "back your hunches with data," it's because she's lost battles where
unbacked hunches got rejected — not because it's a generic platitude.

---

## Foundational Best Practices

### Treat AI as a probabilistic system, not deterministic software

The single most important mental shift for PMs entering AI work. Traditional
software is "if input X, output Y." AI products operate on predictions, not
certainties. Every output carries uncertainty.

**Practical implications:**
- Set stakeholder expectations early about confidence ranges, not absolute outcomes
- Show users confidence scores or warnings where stakes are meaningful
- Build feedback loops that handle the uncertain cases (escalation, human review)
- Balance accuracy against speed and cost — not all three can be maximized

### Data is the heart of AI — design data strategy alongside product strategy

Most product teams treat data as engineering infrastructure. AI PMs must own
data strategy as a first-class product concern.

**Specific advice:**
- Audit data quality before promising AI features. Volume alone is insufficient — diversity and relevance matter more.
- Build workflows for sourcing, cleansing, and validating data continuously
- Privacy-protective techniques (differential privacy, federated learning) are now standard — design them in, not bolted on
- "If obtaining quality data is impossible, AI might not be the path forward" — be willing to say this to leadership

### Plan for model drift from day one

AI products are not "ship and forget." Models degrade as the world they were
trained on changes. Treat AI products as continuously evolving systems.

**Operational requirements:**
- Model retraining schedule (cadence depends on use case — daily for fraud detection, monthly for content recommendations)
- Active learning frameworks where user feedback flows back into training data
- Mechanisms to correct outputs in production (user-flagged errors, override capability)
- Monitoring on input distribution shift — when production inputs diverge from training distribution, retrain

### Invest in interpretability and explainability before regulators demand it

The regulatory landscape is tightening fast (EU AI Act, sector-specific rules
in healthcare/finance). Building explainability later costs 10x what building
it from the start does.

**Tools and practices:**
- SHAP, LIME, InterpretML for explaining individual predictions
- Document the model's training data lineage (audit trail)
- Provide users with plain-language explanations for consequential decisions
- Have a compliance review process for any model touching regulated data

### Define decision boundaries explicitly

AI systems can recommend or decide — and the line between these matters.
High-stakes domains (healthcare, finance, hiring) require explicit
decisions about where automation stops and human judgment begins.

**Decision matrix:**

| Stakes | Reversibility | Recommended autonomy |
|---|---|---|
| Low | High | Full automation OK |
| Low | Low | Suggestion + user confirms |
| High | High | Approval gate (human reviews before commit) |
| High | Low | Human decides; AI assists |

---

## The 0-to-1 vs 1-to-n Distinction (Practical Application)

The most important categorization Nika makes. Treating both as the same kind
of work leads to mismatched timelines, team composition, and expectations.

### Working on 0-to-1 AI Products (real-world advice)

**Context:** Early-stage startup, or research-led team in a big company
(e.g., Adobe/Pinterest/Nextdoor's recent LLM PM hires).

**Practical realities:**
- You don't know who the user is or even if there will be one. Embrace ambiguity; it's not a bug.
- Hypothesis-and-test cycles are the work, not a phase before the work
- Collaboration with AI researchers is critical — they understand the model's actual capabilities (and limits)
- "Each experiment's feedback cycle is geared toward refining the AI solution to fill market gaps"
- Be ready to start over from scratch on hypothesis failures — sunk cost reasoning kills 0-to-1 products

**Anecdotal example (from book):** Working at an early speech recognition team
designing devices that could understand a wide variety of accents. The work
was "wrangling enormous datasets, refining algorithms, and spending months
trying to figure out how to embed this technology into user-facing products."
The market wasn't proven; the technology was novel; the user wasn't defined.

### Working on 1-to-n AI Products (real-world advice)

**Context:** Established company adding AI to existing products (Netflix
recommendations, Amazon Prime Video optimization, Spotify's AI DJ).

**Practical realities:**
- You have product-market fit on the underlying product — your job is enhancement, not validation
- Start from existing user pain points; don't invent new ones
- Data signal is your best friend — usage logs reveal where AI can help
- Concrete examples (from book):
  - Sophisticated recommendation systems that learn user viewing patterns
  - Dynamic streaming quality optimization
  - Automated content moderation
- The win is in the unit metrics: minutes-watched, click-through, retention by cohort

---

## The AIPDL in Practice (Worked Examples and Caveats)

### Stage-by-stage practical advice

**Ideation stage:**
- Time-block 3-4 hours for in-depth brainstorming sessions with team
- Mute notifications during brainstorming — AI ideas need warm-up time
- Ask team for: current projects, aspirational projects, moonshot ideas
- Pick top 10% of ideas by value to key user segments

**Brainstorming dos and don'ts (verbatim from book):**

DOs:
- Solve the right problem (validate user pain before solutioning)
- Understand impact of each feature on existing features
- Bring diverse perspectives (data science, UX, ethics, domain expertise — pick 4-5 core members)
- Use the customer-product engagement lens (e.g., Starbucks app pickup-time prediction)

DON'Ts:
- Fall into the "shiny AI object" trap (don't ship just because the tech is cool)
- Talk about a "hunch" — back proposals with data on similar past implementations and ROI
- Skip impact analysis on existing features

**Opportunity stage:**
- Use Van Westendorp Pricing Model alongside surveys for willingness-to-pay
- Use AI tools for market research (Komo, You.com mentioned in book)
- For larger companies: partner with in-house UX researcher
- For startups: outsource via Upwork or use direct user-feedback platforms

**Concept/Prototype stage:**
- AI MVPs differ from software MVPs — they must add immediate value (not just promise it)
- Hardcode behavior for non-essential paths (e.g., chatbot predefined responses for common queries) while training only the differentiating capability
- Demonstrate low-effort integration via API or sample integration layer
- Use small high-quality domain dataset to showcase domain expertise

**Testing & Analysis stage:**
- Achieve Minimum Viable Quality (MVQ) before proceeding to rollout
- MVQ threshold depends on use case (medical needs higher than entertainment)
- Eventually, no metrics will perfectly capture whether the model is "ready" — human judgment must close the gap

**Rollout stage:**
- Marketing strategies should build synergies between promotional activities
- Schedule events along a predetermined timeline
- Continuously evaluate accuracy and performance post-deployment
- Schedule maintenance checks; AI features need ongoing care, not just initial shipping

---

## Strategic Thinking Best Practices

### Build vs Buy: practical decision-making

Nika treats this as one of the most consequential strategic decisions an AI
PM makes.

**Specific guidance:**
- Map AI capabilities to mission and identify specific user pain
- "Don't use AI if you can't get good data" — be willing to walk away
- Before AI: evaluate non-AI alternatives (rule-based systems, automation scripts)
- "Sometimes the answer is yes, and that's OK" — non-AI solutions are valid
- Acquisition warning: companies acquire startups with great tech but later have to rewrite all the code due to incompatibility — assess fit early

### Synthetic data: when it works and when it doesn't

**Best practice (from book):**
- Use synthetic data for sensitive information, rare scenarios, early development
- Tesla's example: synthetic scenarios for rare edge cases + real-world driving data for common scenarios
- Validation gate: synthetic data must maintain statistical properties of real data
- "Always validate your synthetic data against real samples when possible"
- "Keep checking that your model's performance holds up in real-world conditions"

**Caveat:** Generating good synthetic data is an art. Bad synthetic data
introduces accidental patterns that bias the model. This is hard to detect
on aggregate metrics; it surfaces on slice-based analysis.

### Fine-tune vs RAG vs Grounding (practical selection)

**Fine-tuning:**
- Best for narrow, stable, high-precision tasks (content moderation, fraud detection, medical diagnostics)
- Example from book: social media platforms fine-tune for hate speech detection
- Resource-intensive: substantial labeled data + compute
- Example: audio streaming services fine-tune for personalized recommendations

**RAG:**
- Best for dynamic, information-heavy contexts (news, market trends, internal docs)
- Information changes frequently → fine-tuning is too slow → RAG fits
- Implementation: vector store + retrieval mechanism + LLM that consumes retrieved context

**Grounding (prompt engineering):**
- Best for rapid iteration during product experimentation
- "Where changes need to be made quickly without retraining the model"
- Lightweight; cheap; fast
- The right tool when you're still in pre-MVQ exploration

---

## OKRs and Metrics: Best Practices

### The "no single metric" rule

Nika is firm: any single AI metric will mislead. The blend matters more than
any individual metric.

**Specific advice for setting AI OKRs:**
- Always include at least one metric from each bucket (Product Health, System Health, AI Proxy)
- Add a North Star above the buckets
- Add 2-3 guardrails as hard floors (not goals)
- Make every KR SMART (Specific, Measurable, Achievable, Relevant, Time-bound)

### Concrete metric examples by domain

**Recommendation systems:**
- North Star: monthly active recommendations clicked per user
- Product Health: retention curve, session length
- System Health: p99 latency, infra cost per recommendation
- AI Proxy: top-N accuracy, click-through rate on top-1
- Guardrails: irrelevance complaints, filter bubble metrics

**Conversational agents:**
- North Star: % tickets auto-resolved without escalation
- Product Health: CSAT, resolution time
- System Health: response latency, uptime
- AI Proxy: intent classification accuracy
- Guardrails: hallucination rate, escalation-after-AI complaint rate

**Content generation:**
- North Star: user-generated content shipped per week using AI
- Product Health: completion rate, edit distance from AI output to final
- System Health: time-to-first-token, total generation time
- AI Proxy: quality score from human eval
- Guardrails: factual error rate, brand voice consistency

### The "context matters" rule

"There is no one-size-fits-all recipe" — Nika repeats this throughout the book.
Templates are starting points, not endings. Customize for your product type,
user expectations, and problem characteristics.

---

## Agent Design: Practical Wisdom

### Defining autonomy explicitly

Nika treats this as the dominant strategic choice in agent design. Most agent
failures trace to unclear autonomy boundaries — agents either too cautious
(low value) or runaway (catastrophic errors).

**Practical decision framework:**

| Autonomy level | When to use | Example |
|---|---|---|
| Assistance | New agent, regulated domain | Code completion |
| Suggestion | User-edits-and-ships flows | Email draft suggestions |
| Approval gate | Consequential actions | Auto-payment requires user approval |
| Co-pilot | User present, agent acts with confirmation | GitHub Copilot |
| Full automation | Stable scope, measured reliability | Background email categorization |

**Best practice:** Start narrow. Earn autonomy by demonstrating reliability.
Define the criteria to graduate (e.g., "95% task completion across 10K runs"
before expanding scope).

### UI patterns: matching the surface to the task

**Side Panel pattern:**
- Best for: continuous assistance during workflow
- Example: Microsoft Copilot in Word/Excel
- Advantage: persistent, contextual, doesn't disrupt flow
- Risk: takes screen real estate

**Floating Bubble pattern:**
- Best for: reactive help, summoned occasionally
- Example: in-app chat widgets
- Advantage: low visual cost
- Risk: discoverability — users might not know it's there

**Dedicated Chat Interface:**
- Best for: complex multi-turn tasks
- Example: ChatGPT, Claude.ai
- Advantage: full conversational space
- Risk: pulls user out of their working context

**Integrated UI:**
- Best for: specialized assistance inside existing flow
- Example: GitHub Copilot inline suggestions
- Advantage: zero disruption, very high adoption
- Risk: requires deep product integration

**Collaborative Browser Interface:**
- Best for: agent operates in user's environment with takeover
- Example: Browser agents (Anthropic Computer Use)
- Advantage: agent can do anything user can do
- Risk: high — observation/control gap is unpredictable

### Anti-patterns Nika specifically calls out

**Glorified Chatbots:**
- Marketing claims of "agentic AI" but actually script-following chatbots with predefined responses
- Why it's bad: users discover limits in first session, lose trust permanently, brand damage
- The fix: build true agency (decision-making, tool use, planning) or call it a chatbot

**Over-Automation:**
- Excessive autonomy without human oversight
- Why it's bad: failures at scale = failures at scale (one bug → thousands of incidents)
- The fix: graduated autonomy with measured reliability

---

## Process Wisdom

### Stakeholder management for AI products

AI products attract scrutiny from leadership in ways traditional features don't.
Practical advice for AI PMs working with execs:

- **Set expectations on probabilistic nature explicitly** — execs default to deterministic mental models
- **Translate ML metrics to business metrics** — "98% accuracy" means nothing; "$2M saved in support tickets" means everything
- **Pre-empt the "why didn't AI catch this case" question** — every error becomes a stakeholder concern
- **Document the cost-benefit** — AI features cost 5-10x more than typical features; defend the investment
- **Plan for the "when will this be 100%" question** — it never will be; help leadership understand asymptotic improvement curves

### Cross-functional team composition for AI products

The book emphasizes that AI PM success depends on working with these stakeholders:

| Function | What they bring |
|---|---|
| ML scientists | Model building, capability assessment |
| Red/blue teams | Security testing, adversarial evaluation |
| MLOps | Deployment infrastructure, monitoring |
| Program managers | Timeline coordination, resource allocation |
| DataOps | Data collection, cleaning, regulatory compliance (GDPR) |
| Developers | Architectural integration of AI components |
| Testers | Functional evaluation, edge case identification |
| UX research | Insight gathering, user need validation |
| Content specialists | Clarity, branding, prompt engineering |
| Product marketing | Value proposition, go-to-market |
| Sales | Customer feedback, pitch refinement |
| Vendors/OEMs | Specialized components or services |
| Consultants/research institutions | Advanced knowledge, innovation |

For each AI initiative, identify which subset matters and engage them early.

---

## Career Wisdom for AI PMs

### The career ladder (conceptual)

Nika defines AI PM levels (the actual rungs vary by company):

- **Levels 4-5 (Execution):** Day-to-day model performance monitoring, OKR setting, identifying product-market fit
- **Levels 6-7 (Mid-level):** Defining product requirements, prioritizing roadmaps, multi-year AI product visions, ML infrastructure strategy
- **Levels 8+ (Strategic Leadership):** Aligning AI products with overall business strategy, AI portfolio management, governance/ethics/compliance
- **Levels 9+ (Top Executive):** Company-wide AI vision at scale, embedding AI across all units, multi-billion-dollar investments, responsible AI governance

### Skill set buckets

What AI PMs need to be good at, organized into four buckets:

**Core PM craft:** User segmentation, pain identification, ideation, RICE
prioritization, roadmapping, KPI/North Star setting

**Engineering foundations:** Software development methodologies (Agile/Waterfall),
working with code, version control, testing frameworks, system architecture,
APIs, AI infrastructure (cloud platforms, edge AI)

**Leadership/collaboration:** Experimentation mindset, creativity, stakeholder
alignment, communication, leadership, analytical thinking, storytelling, empathy

**AI lifecycle awareness:** Understanding AI/GenAI capabilities, prompt engineering,
model training (MLOps), LLMs/fine-tuning, productionization, DataOps,
evaluation/adversarial testing, ethics/compliance, emerging trends (multimodal, agentic)

---

## When to Apply These Practices

This expert reference complements the action-focused skills:

- For lifecycle decisions → also see `ai-product-development-lifecycle/SKILL.md`
- For build vs buy → also see `ai-build-vs-buy-and-model-adaptation/SKILL.md`
- For metrics and OKRs → also see `ai-product-okrs-and-metrics/SKILL.md`
- For agent design → also see `ai-agent-design-patterns/SKILL.md`
- For frameworks catalog → see `frameworks.md` in this folder

When facing a novel AI PM situation not covered by the skills, browse this
reference for adjacent practical wisdom that might apply.
