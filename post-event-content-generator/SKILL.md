---
name: post-event-content-generator
description: >
  Generates the full post-event content and outreach output once Alex has raw event material to work from — voice notes, Granola transcripts, contact names, or even a quick freeform recap. Use this skill when Alex is ready to produce: contact bucket sorting, outreach DM drafts (per bucket), a LinkedIn comment draft, and a LinkedIn post draft. This skill executes the content generation step; content-correspondent provides the strategic foundation and full framework. Triggers include: "draft my follow-ups from last night", "write the post from [event]", "I have my Wispr notes, let's go", "sort these contacts and draft outreach", or any request to turn raw event input into ready-to-send content. Also use when Alex asks for a pattern post across multiple events, an audience-segmented angle, or help tracking what's landing.
---

# Post-Event Content Generator

This skill takes raw event input and produces ready-to-use output across both tracks: private outreach and public content. It is the execution layer of the post-event system. The strategic foundation — the field reporter frame, the two-track mental model, the closed loop theory — lives in the `content-correspondent` skill. This skill is where that theory becomes drafts.

**Input formats accepted:**
- Wispr Flow voice note transcript (paste in)
- Granola session notes or transcript
- Freeform recap ("I met X, they said Y, the room felt Z")
- Just an event name + a few names (sparse mode — see below)

**Output produced every time:**
1. Contact sort (bucket A/B/C/D with brief rationale)
2. Outreach DM drafts (one per relevant contact, copy-paste ready)
3. Tier 1 LinkedIn comment draft (for host/speaker post)
4. Tier 2 LinkedIn post draft (150–300 words, field dispatch format)

Lean toward opinionated and specific over safe and hedged. Alex reviews everything. A draft with genuine voice that's 80% right is more useful than a technically correct draft that sounds like a marketing bot.

---

## Contact Sorting

Before writing anything, sort contacts into buckets. Brief rationale per person — don't over-explain.

| Bucket | Who | Timing |
|--------|-----|--------|
| A — High Signal | Founders, hiring managers at target companies, investors | 24h |
| B — Peer Builders | AEs/CS/AM peers making the same AI+GTM transition | 48h |
| C — Interesting Stranger | Real conversation, no obvious immediate mutual value | 72h |
| D — Room Presence | Noticed but didn't connect 1:1 | Public engagement only |

---

## Outreach DM Templates

**The non-negotiable:** every message contains a specific callback to something said, built, or shared in person. Generic openers are deleted. The formula is: **Callback → POV → Forward Motion**.

**No CTA on first touch for Bucket A.** The goal of message 1 is to earn a response. The ask comes after they engage.

**Bucket A — Hiring Manager:**
> "[Name] — really enjoyed our conversation about [specific topic]. Your point about [specific thing] is something I've been wrestling with too — I've been approaching it by [brief relevant POV]. If you'd find it useful, happy to share what I've been seeing from [relevant angle]. Either way, glad we connected."

**Bucket A — Founder:**
> "[Name] — the [specific product/problem] angle you described is one I keep coming back to. One thing I didn't mention on the night: [relevant observation or customer pattern]. Curious whether [specific question based on something they said]. No agenda — it's just a genuinely interesting problem."

**Bucket A — Investor:**
> "[Name] — enjoyed the conversation about [thesis area]. Your framing of [specific thing] was sharp — it maps to something I've been watching closely on the [GTM/sales/enterprise buyer] side. Would be interested to continue that conversation sometime."

**Bucket B — Peer Builder:**
> "[Name] — good to connect last night. The way you're thinking about [specific thing] is solid — I've been working through a similar problem around [your angle]. I'm going to write something about [topic] this week — I'll tag you if it connects to what you're doing. And if you publish anything on [relevant topic], send it my way."

**Bucket C — Interesting Stranger:**
> "Hi [name] — we crossed paths at [event] and your take on [specific thing] stuck with me. I'm in the [AI + GTM/enterprise sales] space and often write about [adjacent topic]. Would be glad to stay connected."

---

## LinkedIn Comment Draft (Tier 1)

Target: the host's or speaker's LinkedIn post about the event. Aim for same night or next morning. A sharp comment on a high-reach post surfaces Alex to everyone who sees it — including people in the room he didn't meet.

**"Yes, And" format:** add a new dimension, counterpoint, or specific observation. Not "great event!" — something that sounds like a person with a POV.

> "The [specific point they made] is something I've been watching play out in [your specific context]. What I'd add from the enterprise/GTM side: [your observation]. Curious whether others in the room saw [specific dynamic] the same way."

---

## LinkedIn Post Draft (Tier 2)

**Format:** 150–300 words. Field dispatch. The event is the news hook; the take is the substance.

**Structure:**
1. **Hook** — 1 sentence. Stops the scroll. Never opens with "I attended X and here's what I learned."
2. **Setup** — 2–3 sentences. What was the room, who was there, what was the tension or theme.
3. **The Take** — 3–4 sentences. Specific POV. A tension or counterpoint that makes people think.
4. **Invitation** — 1–2 sentences. A specific question that reveals something about the reader when they answer it.
5. **Optional tag** — 1–2 people from the event, only if earned (e.g., "as [name] said last night...").

**Hook examples that work:**
- "The best thing I heard at last night's PMF x AI event wasn't about AI."
- "Talked to 8 founders last night. The ones building something real all said the same thing about [X]."
- "I've been to 20 of these NYC AI events. Last night was different."

**Closing question examples that work:**
- "Is the translation layer between infra builders and enterprise buyers a person, a process, or eventually a product?"
- "At what point does 'AI-native' stop being a differentiator and start being table stakes for enterprise buyers?"

### Audience-Specific Angles

Pick one per event. Vary across events to test which resonates.

| Audience | Angle | Hook Style |
|----------|-------|------------|
| Founders & Builders | "What I observed about [problem/market] from the inside" | "The founders who are actually gaining traction all share one counterintuitive habit..." |
| Execs & Hiring Managers | "What talent dynamics in this scene tell you about the market" | "I've noticed the best enterprise AI hires I keep meeting are all coming from [unexpected background]..." |
| Peers (AEs, CS, AM in transition) | "What I'm learning from builders about how our jobs are changing" | "Honest admission: I came expecting to ask questions. I left feeling like the one who should be building." |
| General Tech/AI Audience | "Signal from the NYC AI scene — what's real vs. noise" | "Everyone talks about AI GTM. Last night I was in a room of 60 people actually doing it. Here's the gap." |

---

## Sparse Input Mode

If Alex provides just an event name and a few contact names with no detail, ask exactly three things — no more:

1. Who are the 1–2 most important people you met, and what did they say?
2. What was the single sharpest thing you took away from the room?
3. Was there any tension, disagreement, or surprise?

Produce from whatever comes back. Don't wait for perfect input.

---

## The Closed Loop (activate both tracks together)

Always produce the post and the DM drafts in the same session. The post gives the DM something to point to; the DM activates the post.

```
Post published
    → Tag 1-2 Bucket B peers in the post
    → DM Bucket A: "I wrote something based on what we discussed — curious your take"
    → Their engagement surfaces Alex to their network
    → New connections comment → warm context for future outreach
    → LOOP
```

---

## Calibration Signals (first 30 days)

Variation is more valuable than optimization right now. The data from real sends is what tunes the system.

| Signal | Kill Sign | Green Sign |
|--------|-----------|------------|
| Post impressions in first 2h | <200, no comments | >500 + 3+ substantive comments |
| Comments vs. Likes ratio | All likes, no comments | Comments + tags + reposts |
| Bucket A DM response rate | <20% | >40% |
| Tagged person engagement | No response | Tagged person comments or shares |
| Best post timing | Monday AM or Friday PM | Tuesday–Thursday AM |

---

## Execution Timing

**Within 2 hours of getting home:**
- Classify contacts into buckets
- Draft Bucket A and B outreach while memory is live
- Write one sentence: "The one thing I'd post about tonight is ___"

**Next morning:**
- Send queued DMs
- Publish post using last night's sentence as the hook seed
- Pull speaker quotes from Granola transcript if available

---

## Progressive Rollout

- **Week 1–4**: Master the 24-hour post. Every event, every time.
- **Week 5–8**: Add same-night comment + Bucket A/B outreach.
- **Week 9+**: Layer in the pattern post; start the newsletter thesis.

Consistency at one tier beats sporadic brilliance across all four.
