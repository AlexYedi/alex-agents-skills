# Chapter 0 — Frame

## Why this exists

This workbook is the operating substrate for the next 18 months of Alex's strategic bets. It exists because the prior artifacts — `AI_STACK_REPORT.docx`, `AI_STACK_ADDENDUM.docx`, `OCQ_TRACKER.md`, and the two HANDOVER briefs, plus twelve unreadable matplotlib plates — had crossed the line from reference into clutter. Four documents in three registers, with overlapping content and divergent numbering, do not get re-opened on a Tuesday morning when a Linear ticket or a Sierra recruiter pushes the question "what do I actually believe this month?" An operating substrate has to be one file, scannable in the order you scan it, with the update cadence written into it.

The consolidation collapses that pile to one editable markdown source plus a regenerable EPUB. Educational density replaces literary register; five plates that carry information prose cannot replaces twelve that decorate. The "Substrate" visual philosophy from the original pile is archived — useful as a thinking exercise once, not as a daily surface. Public-facing artifacts (the eventual newsletter, conference deck, advisory one-pager) come later, off a different surface. This is internal substrate: written for one reader, updated by one owner, sharable when useful, but not optimized for that case.

The split between source and export matters. Markdown is canonical and edited directly. EPUB is regenerable via pandoc and reflows on phone, Kindle, or e-reader for the read-anywhere case. Plates are SVG, regenerated from `plates/build_plates.py`. The spec (`_spec.md`) defines the taxonomy. Nothing in the workbook is hand-formatted in a way that breaks if the source moves.

## Alex's profile (in 5 lines)

- 12 years enterprise B2B sales and GTM — SaaS through procurement gauntlets at Meltwater, Bazaarvoice, and Cohley; ICP-led motion across F1000 marketing, legal, and InfoSec counterparties.
- AI-builder track since 2023 — shipping with Claude, the AI SDK, n8n, Supabase, Vercel, Cursor, Linear, PostHog; published skills, agent stacks, and the substrate this workbook lives in.
- NYC-based; active senior search across vertical-agent GTM leadership roles (Sierra, Decagon, Glean, Harvey, Hippocratic, Augment) plus advisory and operator-partner paths.
- The unique combination: commercial fluency the AI labs lack + AI-builder fluency the enterprise sales bench lacks + buyer-side procurement scar tissue most NYC GTM talent does not carry.
- 18-month bet horizon — May 2026 to late 2027; the workbook is sized to that window, then will be re-versioned.

## The thesis (in one sentence)

The highest-leverage opportunity for someone with twelve years of enterprise B2B fluency, growing AI-builder skill, NYC location, and an active job search is to plant a flag at the intersection of enterprise AI procurement, vertical agent go-to-market, and operator translation — three positions that compound, that all five frameworks converge on, and that a senior practitioner with this exact profile is one of fewer than fifty people structurally able to occupy.

## How to read this workbook

The workbook is structured for several reading paths. Pick the one that matches the moment.

- **Full cover-to-cover read (~2 hours).** Ch 0 → Ch 6. Use once on first contact, and again at each twice-yearly major refresh (Ch 5 §5.4). The order is the reasoning path: substrate → frameworks → bets → tracker → rituals → appendix.
- **Framework-only refresh (~30 min).** Ch 2 alone. Use when a new opportunity, role, or company crosses the desk and you want to score it cleanly — OCQ lens, Wardley position, 7 Powers inventory, JTBD job mapping. The lens definitions in Ch 2 §2.1 are the canonical scoring rubric.
- **Decision update (~20 min monthly).** Ch 3 bet status + Ch 4 tracker tables. Use during the monthly conviction ritual (Ch 5 §5.2). Re-rate the seven bets, mark which leading indicators moved, log any crux that fired (Ch 4 §4.8).
- **Weekly reflection (~10 min).** Ch 5 §5.1 prompts only. Three short questions; about two minutes each. The point is not depth, it is repetition.
- **Onboarding a new helper or briefing a friend (~20 min).** Ch 0 + the Ch 3 summary tables. The Frame chapter is short on purpose so it can be handed to someone — recruiter, advisor, founder, downstream Claude session — without the rest of the apparatus.

Markdown is canonical. The EPUB is regenerable via pandoc (`build_epub.sh`). Edit `chapters/*.md` directly; never edit the EPUB. The spec (`_spec.md`) holds the taxonomy — strata numbering, OCQ lens definitions, the seven bets, the five cruxes, the five risks. If anything in a chapter contradicts the spec, the spec wins; bump the spec version and propagate. The full update protocol — what changes when, who owns it — lives in Ch 6 §6.4.

## What's in each chapter

1. **Ch 0 — Frame.** This chapter. Profile, thesis, reading paths. Re-read at each major refresh.
2. **Ch 1 — The Substrate.** The 18 strata (I–XIV plus Meta A–D) at the depth a senior practitioner uses to make decisions. Read top-to-bottom once; afterward, jump to the stratum a buyer, interviewer, or roadmap is probing.
3. **Ch 2 — Framework Lenses.** Five frameworks: OCQ × Layer Matrix, Wardley Mapping, Helmer's 7 Powers, Ecosystem JTBD, Talent & Capital Flow. Use to score one new opportunity, place one new player, or stress-test a bet.
4. **Ch 3 — Big Bets, Risks, Cruxes.** The 7 Big Bets (hypothesis, falsifiability, conviction, next action), the 5 Structural Risks, the 5 Cruxes, and the 6/12/18-month Action Map. Use monthly during the conviction ritual.
5. **Ch 4 — Operating Tracker.** Living tracker: bet status, senior talent moves, capital events, ARR watchlist, NYC snapshot, crux status, risk status, update log. Bi-weekly and monthly updates land here.
6. **Ch 5 — Operating Rituals.** Weekly reflection prompts, monthly conviction ritual, quarterly deep review, twice-yearly major refresh. Use as a calendar.
7. **Ch 6 — Appendix.** Glossary, sources, methodology, update protocol, change log. Reference, not narrative.

## Pointers to companion artifacts

- **`_spec.md`** — canonical taxonomy. Strata numbering, OCQ lens definitions, bet list, crux list, glossary, update protocol. Read once; revisit when something contradicts.
- **`plates/*.svg`** — five visual companions. Plate 1 Substrate Column (Ch 1 key), Plate 2 OCQ Heatmap (Ch 2 §2.1), Plate 3 Wardley Map (Ch 2 §2.2), Plate 4 Powers × Layer Grid (Ch 2 §2.3), Plate 5 Cross-Stratum Flows (Ch 3 bet coupling and risk propagation). Each earns its place because the information is positional, comparative, or graph-shaped — not because it is decorative.
- **`_archive/`** — original HANDOVER docs, design philosophy, the prior matplotlib plates. Kept for downstream Claude sessions and audit; not part of the live workbook. Read only if you are reconstructing the lineage.
- **`_extract/`** — raw text extracts from the original `.docx` files. Source material for the chapter writers, not for direct reading. Treat as a quarry, not a finished surface.
- **Downstream artifacts.** `output/ai-agents/` (Volume III: the agent-layer deep dive, agent-specific tracker, agent-layer bet deltas) and `output/agents-gtm/` (Volume IV: the GTM playbook for vertical-agent companies). This workbook is Volume I/II — the foundation layer the downstream volumes build on. The Vol III addendum at the top of Ch 4 lists the deltas the agent-layer work has already pushed back.

## Apply

In one sentence, write your thesis for the next 18 months. If you cannot write it, you are not yet ready to operate against the bets in Ch 3 — re-read this chapter's §thesis and try again. If you can, save the sentence somewhere visible: pinned note, Linear profile, whiteboard. Re-read it monthly during the conviction ritual (Ch 5 §5.2). If the sentence has changed, that is a signal worth examining before re-rating the bets — what moved, and is the new sentence load-bearing or rationalization?
