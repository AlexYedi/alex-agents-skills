# Cross-provider LLM-as-judge — quorum design + provider gotchas

A reusable design for an **LLM-as-judge that resists self-preference**, plus the API gotchas of adding a
second provider. Use when a Claude judge scores work that Claude (or a Claude subagent) produced — the
unclosed risk is **judge circularity**: a model rating its own family's output. A judge from a *different
provider* is the concrete mitigation.

## Two seats — house-aware + independent

| Seat | Model | Role | Cost |
|---|---|---|---|
| **House-aware** | a Claude model (e.g. Sonnet) via the `Agent` tool | knows the project's conventions | subscription — no marginal `$` |
| **Independent** | a different provider (e.g. Google `gemini-pro-latest`) via a shell adapter (curl) | catches the house model's blind spots | metered API key (~cents/run) |

Notes: use a *mid/strong* model for each seat, not the cheapest — a too-weak independent seat produces
noisy disagreements. Avoid same-family judge-of-judge (amplifies self-preference); avoid a too-large seat
(quota-heavy for marginal gain).

## Scope the vote by competence (not naïve 50/50)
Both seats score all criteria, but weight their votes by where each is credible:
- **Provider-neutral criteria** (correctness, completeness) → the independent seat carries **full weight** —
  this is where cross-provider catches blind spots.
- **House-specific criteria** (convention adherence, house anti-patterns) → the house-aware seat retains
  **primary** judgment; the independent seat lacks native project context and votes advisory-only (unless
  heavily briefed). Give both seats the *same* rubric + per-artifact context (apples-to-apples), plus a
  house-context primer for the convention criteria.

## Resolve without a model tiebreak (it would be circular)
A disputant can't adjudicate its own split, and a correlated third model isn't independent. So:
- **Agree** (both pass / both flag) → **auto-verdict**, high confidence, no human.
- **Disagree** + human in the loop → **escalate to the human** (the only independent tiebreaker). Surface
  **both seats' per-criterion reasoning side-by-side**, divergent criterion highlighted → a ~15-second call.
- **Disagree** + autonomous/batch → **fail-safe to FLAG** ("review before done", non-destructive) and queue
  the split for later human review. **Never auto-resolve a split with a correlated model.**
- The disagreement set is the highest-value output — it's where the judge is least trustworthy.

## Run-log discipline (own the contract, rent the platform)
Keep one stable log schema across seats; add rather than restructure. Useful fields: `judge_model` **plus
the resolved model version** from the API response (since `-latest` aliases shift — preserves calibration
traceability); `calibration_set` = `backfill` vs `prospective` (report agreement **separately and
combined**, so a clean prospective signal isn't inflated by a correlated backfill); and a `quorum` record
`{seatA:{verdict,score}, seatB:{verdict,score}, agree, resolution: auto|escalated|failsafe_flag,
final_verdict, human_ack}`. Compute the quorum as a **separate additive record** — no seat needs the
other's result at write time (avoids an order dependency the adapter can't satisfy).

## Calibration to retire "provisional"
- **Backfill** (fast): run the independent seat on already-human-acked artifact *states*; report
  independent-vs-human + inter-judge agreement + the disagreement set. Correlated with the original labels —
  a sanity pass, not proof.
- **Prospective** (clean): every new judgment runs both seats on a fresh, held-out artifact; the human acks
  once; agreement accrues on independent work. **This is what actually earns trust** — target ≥80%
  independent-vs-human across ~15+ prospective runs.

## Gemini API gotchas (learned wiring the independent seat)
1. **Gemini Pro is a thinking model** — set `generationConfig.maxOutputTokens` generously (~8000) or
   reasoning tokens starve the JSON verdict (a tiny cap returns empty). Prefer
   `responseMimeType: application/json` + a response schema to force clean structured output.
2. **Model-id churn is fast** — pinned preview ids deprecate within weeks. Use `gemini-pro-latest` and
   **record the resolved version per run**; don't hardcode a soon-dead preview id.
3. **Key hygiene** — source it from `.env`, pass via the `x-goog-api-key` header, never echo the command
   with the key inline.
4. **Free tier ≠ Pro** — the Pro model needs billing enabled; a free key silently caps you to a weak
   model. If billing lapses, **surface it** — don't silently fall back to a weaker judge.
5. **Cost is negligible at judge volume** — a few cents per run; the Claude seat stays subscription-free.
