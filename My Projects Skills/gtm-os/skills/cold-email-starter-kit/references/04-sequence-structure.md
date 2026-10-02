# 04 — Sequence Structure

How to structure a multi-step cold email sequence. Covers timing, threading, A/B testing, and spintax.

Read `03-campaign-copywriting.md` first. This file is about *how the emails fit together*, not how to write them.

---

## How many emails in a sequence?

**4 is the sweet spot.** More than 4 starts to feel spammy. Fewer than 3 leaves reply potential on the table.

The reply curve across 4 emails typically looks like:
- Email 1: ~35% of total replies
- Email 2: ~30%
- Email 3: ~20%
- Email 4: ~15%

Meaning: **if you stop at Email 1, you're leaving 65% of your replies on the table.** Follow-ups are where the volume is.

---

## Timing

| Step | Day | Subject | Threading |
|---|---|---|---|
| Email 1 | Day 0 | New subject | New thread |
| Email 2 | Day 3-4 | NONE (blank) | Reply to Email 1 thread |
| Email 3 | Day 7-8 | New subject | New thread |
| Email 4 | Day 11-12 | New subject OR in-thread | Your choice |

**Why the gap increases:** recipients who haven't replied by Day 7 are probably saving it or ignoring it. Longer gaps reduce annoyance.

**Weekends:** skip them. Business hours in recipient's timezone only.

**Timezone:** set your sending schedule based on the recipient's timezone, not yours. Both platforms support this.

---

## Threading — when to reply into an existing thread vs. start fresh

**Thread (reply to Email 1):**
- Email 2 → threads (leave subject blank, platform auto-threads)
- Keeps the conversation together in recipient's inbox
- Good for "bump" style follow-ups

**New thread:**
- Email 1 → always new thread
- Email 3 → always new thread (buried threads don't get seen)
- Email 4 → your call

**Why Email 3 resets:** by Day 7, Email 1's thread is buried 20 emails deep. Starting fresh with a new subject gives your Email 3 a chance to be seen.

---

## A/B testing

Both Smartlead and Instantly support variant testing inside a single sequence. Send Variant A to 33% of leads, B to 33%, C to 33%. After 2-3 days, keep the winner for the rest of the campaign.

### What to test (in order of priority)

1. **Subject line** — biggest impact on open rate
2. **First line** — biggest impact on reply rate
3. **CTA** — impact on response quality
4. **Whole body** — only when you have a fundamentally different angle

### Rules

- **Test one thing at a time.** If you change subject + first line + CTA simultaneously, you don't know which caused the lift.
- **Minimum 500 sends per variant** before drawing conclusions. Less than that is noise.
- **Keep the winner, discard the loser.** Don't be sentimental.
- **Don't run 5 variants at once.** 2-3 is the practical max.

### Example variant test

Same body, 3 different subjects:
- **A**: "question for {{first_name}}"
- **B**: "{{company_name}} equipment"
- **C**: "Ever chase renters to pay on time?"

After 1,500 sends (500 per variant), whichever has the highest reply rate wins.

---

## Spintax for deliverability

**What it is:** Syntax like `{Hi|Hey|Hello}` that expands randomly per send.

**Why it matters:** Gmail and Outlook have pattern-matching spam filters. If you send 2,000 identical emails, they fingerprint you and start flagging. Spintax makes every email slightly different, defeating the fingerprinting.

**Where to use it:**
- Greeting: `{Hi|Hey|Hello} {{first_name}}`
- Subject: `{question for|quick question for|curious about} {{first_name}}` (lowercase q)
- First line connector: `{Saw|Noticed|Spotted} {{company_name}} on {{source}}`
- CTA: `{Worth a look|Worth exploring|Worth a quick chat}?`

**Syntax:** Both Smartlead and Instantly accept `{option1|option2|option3}`. They expand independently per send.

**Don't overdo it.** 3-5 spintax points per email is enough. Every word spintax'd = unnatural.

---

## When to use AI-generated variables

See `03-campaign-copywriting.md` → "AI Personalization Decision Framework" for the full logic.

Quick rule: **only use `{{ai_*}}` variables when your product's value changes based on what the recipient does.**

- ✅ "So you can focus on {{ai_company_mission}}..." (SaaS company — different missions need different messaging)
- ❌ "We help you clean {{ai_product_type}}..." (cleaning company — same service regardless of what they sell)

---

## Example 4-step sequence (complete, copy-pasteable)

This is a full sequence for a hypothetical SaaS cold outbound tool. Adapt to your product.

### Email 1 — Day 0
**Subject**: `question for {{first_name}}`

```
{{first_name}}, {saw|noticed} {{company_name}} {is|appears to be} selling to {{ai_customer_type}}.

We built a cold outbound tool that {pulls|finds} verified decision-makers and writes first lines based on their LinkedIn. {Acme Corp|Lemlist|Apollo} saw a 4.7x increase in pipeline after switching.

{Worth a look|Worth exploring}?

Jane
```

### Email 2 — Day 3 (threaded, blank subject)
**Subject**: *(blank — threads to Email 1)*

```
{{first_name}}, from my experience, most {VP Sales|Head of Sales|sales leaders} are focused on {pipeline velocity|deal volume|rep efficiency}.

{If that's you|If that sounds familiar}, we make a tool that {cuts prospecting time in half|doubles rep output|replaces 3 SaaS subscriptions}.

Is {pipeline|rep efficiency} on your radar?

Jane
```

### Email 3 — Day 7 (new thread, new subject)
**Subject**: `SaaS case study`

```
{{first_name}}, quick story.

{A|One} SaaS company {like yours|in your space} was spending $8K/month across 4 outbound tools. Their SDRs were drowning in tabs.

We consolidated them into one tool. Result: {40% faster|half the time} per prospect, same output, saved $6K/month.

Given what {{company_name}} does, {figured|thought} this might be relevant.

Worth a quick chat?

Jane
```

### Email 4 — Day 11 (final, threaded or new)
**Subject**: `show and tell` *(or blank to thread)*

```
{{first_name}}, last email from me.

I figured you sell to customers like {{ai_customer_type}}. I went ahead and pulled 5 of them off LinkedIn for you using our system. No human wrote this email.

{{lead_example_1}}, {{linkedin_1}}, {{email_1}}
{{lead_example_2}}, {{linkedin_2}}, {{email_2}}
{{lead_example_3}}, {{linkedin_3}}, {{email_3}}

Want to see a video of how I did this automatically?

Jane
```

### Variables used

| Variable | Source | Example |
|---|---|---|
| `{{first_name}}` | Prospeo | "Sarah" |
| `{{company_name}}` | Prospeo | "Acme Inc" |
| `{{ai_customer_type}}` | OpenRouter enrichment | "B2B SaaS buyers" |
| `{{lead_example_*}}` | Custom scripted enrichment | "Maya Chen, VP Product" |

---

## Launching the sequence

1. Write all 4 emails in your platform (Smartlead or Instantly)
2. Add delays between steps (0, 3, 7, 11 days)
3. Mark Email 2 to thread with Email 1 (blank subject)
4. Mark Emails 3 and 4 as new thread
5. Preview on 5 real leads to make sure variables resolve (no `{{undefined}}`)
6. Send a test to yourself first
7. Run the launch checklist in `12-launch-checklist.md`
8. Hit start

Done. Now wait 11 days before drawing any conclusions — the sequence has to fully run before you can judge it.
