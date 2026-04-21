---
name: post-event-content-generator
description: Turn raw event notes into a shipped LinkedIn post plus the speaker/host DMs that ride on it. Use this skill when Alex says "write the post from [event]", "here are my notes from [event]", "post-event content for X", "draft the recap and DMs", or dumps raw notes and asks for the deliverable. Triggers on unstructured event notes, brief dumps, or a Notion Event page that has been attended (Last Attended populated). Produces a single-event post in Alex's documentarian voice plus per-speaker/host DMs. If two recent briefs meet the synthesis trigger, flags the opportunity for `pattern-synthesis` rather than generating a synthesis here.
---

# Post-Event Content Generator

<!-- SKELETON — fill in with the actual authored content. Structure below is a
starting scaffold based on the README description. -->

Turn raw post-event notes into a shipped single-event LinkedIn post plus the
per-speaker/host DMs.

## Inputs

- Raw notes (dump, bullets, voice memo transcript) OR a Notion Event page with
  post-attendance fields populated.
- Optional: Alex's preferred angle ("lead with the demo", "contrast with last
  week's event", etc.).

## Workflow

1. Resolve the event in Notion. Capture speakers, hosts, topics, companies.
2. Extract the 2-3 load-bearing moments from the notes (a quote, a demo, a
   specific claim).
3. Check the synthesis trigger: if another brief within 7 days forms an opposing
   thesis, flag for `pattern-synthesis` and stop.
4. Draft 2 post variants in Alex's voice: one lead-with-claim, one
   lead-with-detail.
5. Draft per-speaker/host DMs (60-100 words each) referencing a specific
   contribution.
6. Write to Notion Content Drafts with the correct schema.

## Outputs

- 2 post variants.
- Per-person DMs.
- Notion Content Draft URL.

## When NOT to trigger

- Two-event synthesis — use `pattern-synthesis`.
- Pre-event content — use `pre-event-content`.
- Pure recap without a thesis — offer recap format instead.

## Voice rules

Inherit from the project style guide. Name names. No throat-clearing. First
person singular. Specific over clever.
