---
name: the-meddpicc-enterprise-deal-desk
description: Run enterprise deals through a MEDDPICC qualification pass and produce the business case. Use this skill when Alex says "MEDDPICC this deal", "deal desk on [account]", "qualify [opportunity]", "where's the gap on [account]", "business case for [deal]", or "what's missing to close X". Triggers on enterprise opportunities being evaluated for forecast, stalled deals needing diagnosis, or when a champion asks for a business-case artifact. Produces the MEDDPICC scorecard (Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition), the gap list, and a business-case draft.
---

# The MEDDPICC Enterprise Deal Desk

<!-- SKELETON — fill in with the actual authored content. Structure below is a
starting scaffold based on the README description. -->

Qualify an enterprise deal through MEDDPICC, surface the gaps, and produce the
business-case artifact the champion can circulate internally.

## Inputs

- Account / opportunity name.
- Whatever context Alex has: call notes, CRM fields, email threads, champion
  conversations.

## Workflow

1. For each MEDDPICC letter, extract what's known and what's missing:
   - **M**etrics — the quantified outcome the buyer will commit to.
   - **E**conomic buyer — named, reachable, aware of the deal.
   - **D**ecision criteria — written, shared, owned.
   - **D**ecision process — steps, stakeholders, timeline.
   - **P**aper process — legal, procurement, security review.
   - **I**dentify pain — the specific, quantified problem.
   - **C**hampion — tested, coached, willing to spend political capital.
   - **C**ompetition — named alternatives including status quo and in-house build.
2. Score each letter 0-3. Total out of 24.
3. List the top 3 gaps by deal-impact, not alphabetical order.
4. Draft the business case: problem, quantified impact, proposed solution,
   measurable outcome, investment, risk/return.
5. Recommend the next 1-2 actions per gap.

## Outputs

- MEDDPICC scorecard.
- Gap list with owner and next action.
- Business-case draft (1-2 pages).

## When NOT to trigger

- SMB deals where MEDDPICC is overkill.
- Pure discovery calls — qualification comes after discovery.
- Post-close handoffs — different artifact.

## Specialized agents

- `agents/content-companion.md` — MEDDPICC-voiced drafter for
  Champion Packs, Business Cases, MAPs, EB-meeting prep docs,
  Pre-mortem briefs, Paper Process kickoff emails, Forecast-call
  deal narratives, Champion Test asks, calibrated discovery
  questions, and deal-review one-pagers. Pulls every output
  through the gap-explicit review checklist and the score-
  citation pattern. Refuses to ship optimism inflation, Champion
  inflation, or unproven Metric claims.
