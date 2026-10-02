# 10 — Reply Handling

What to do when replies start coming in. This is where campaigns turn into revenue.

---

## Reply categories

Every cold email reply falls into one of 6 buckets:

| Category | Signal | Action |
|---|---|---|
| **Positive** | "Yes", "tell me more", "let's chat", asks a question, shares availability | Reply within 30 min, human-written, book the call |
| **Negative** | "Not interested", "remove me", "stop emailing", "we use X already" | Gracefully accept, mark as not-interested, don't argue |
| **Out of Office (OOO)** | Auto-reply, "returning on X", "away until Y" | Reschedule the rest of their sequence for after return date |
| **Wrong person** | "I don't handle this", "talk to X instead" | Thank them, ask for the right contact, exit politely |
| **Unsubscribe** | "Unsubscribe", "remove", explicit opt-out | Immediately block across all campaigns, confirm with one-line reply |
| **Bounce** | Mailer-daemon, "address not found", hard bounce | Pause this address, investigate inbox reputation if > 5% bounce rate |

Both Smartlead and Instantly have built-in AI reply categorization. Enable it; it's accurate ~90% of the time.

---

## What to do with each

### Positive reply

**Goal:** Convert to a booked meeting within 24 hours.

**Speed matters.** A reply within 30 minutes of receipt looks 10x more human and increases booking rates significantly. Set up mobile notifications from your master inbox.

**Template (positive, interested):**
```
{{first_name}}, appreciate the quick reply.

Does [day/time] or [day/time] work for a 15-min call?

If easier, here's my calendar: [booking link]

— [your name]
```

**Rules:**
- Write it yourself, don't reuse AI templates
- Keep it shorter than the original email
- Offer 2 specific times, not "whenever works"
- Include a calendar link as fallback

### Negative reply

**Goal:** Exit gracefully. Preserve the relationship for 6-12 months from now.

**Never:**
- Argue ("but did you consider...")
- Counter-pitch ("well, maybe this other product...")
- Guilt-trip ("I just spent 2 hours researching you...")
- Send more to this person

**Do:**
- One short acknowledgment reply
- Move the lead to "not interested" status
- Exit the sequence

**Template:**
```
Got it, appreciate the direct reply. I'll stop reaching out.

If priorities shift in 6 months, feel free to respond to this thread.

— [your name]
```

### Out of Office (OOO)

**Goal:** Reschedule future sends for after their return.

Most platforms auto-detect OOO. If yours does, it'll automatically pause future steps until the return date and resume.

**If manual:**
1. Read the OOO message for a return date
2. Edit the lead's next send date to return_date + 1 day
3. Let the sequence continue

Never reply to an OOO. It's not a rejection, just a pause.

### Wrong person

**Goal:** Get the right contact, exit politely.

**Template:**
```
Thanks for the redirect. Could you share who handles [thing] at {{company_name}}, and I'll reach out to them directly?

Appreciate your time.

— [your name]
```

If they share a contact: add that contact as a new lead in a different campaign (or the same one if appropriate), remove the current person, exit.

### Unsubscribe

**Goal:** Honor the request immediately, log it, move on.

**Practical rule:** do it same-day. Same-day comfortably beats CAN-SPAM (10 business days) and GDPR (immediate).

**Steps:**
1. Add their email to the block list (both Smartlead `/domain-block-list` and Instantly `/block-list-entries` support this)
2. Suppress across ALL your campaigns, not just this one
3. Reply with one-line confirmation:
   ```
   Done, you're removed. Sorry for the intrusion.
   ```
4. Don't add justifications, apologies, or retargeting attempts

### Bounce

**Goal:** Identify if this is a single bad address or a reputation issue.

**If bounce rate < 3%**: normal, expected, nothing to do. Bad addresses happen.

**If bounce rate > 5%**: something's wrong. Options:
- Bad list (emails weren't verified) → re-verify with MillionVerifier before next campaign
- Inbox reputation issue → pause sending from that inbox, investigate
- Domain reputation issue → pause the whole domain, check MXToolbox

---

## The 30-second rule

Replies that sit for hours go cold. The difference between a 2-minute response and a 2-hour response is ~5x in booking rate.

**Set up:**
- Desktop notifications from your sending platform
- Mobile app notifications (Smartlead and Instantly both have mobile apps)
- A "positive reply" webhook → Slack/SMS alert
- Dedicated "prospect replies" notification sound so you know it's urgent

**Your workflow:**
- Notification fires → open master inbox
- 5 seconds: read the reply
- 30 seconds: write a personal response
- 1 minute: hit send

If you're in a meeting and can't respond in 30 min, note it and reply within 2 hours max.

---

## Master inbox vs. individual inbox login

**Always use the master inbox.**

- Smartlead: "Master Inbox" tab — shows replies from all 40 inboxes in one view
- Instantly: "Unibox" — same concept

Never log into 40 individual Gmail accounts. You'll burn out in a week. The whole point of running 40 inboxes is that they're invisible to you — you just read replies from a unified feed.

---

## Automation: AI reply categorization

Both platforms offer AI that auto-labels replies as Interested / Not Interested / OOO / Wrong Person. Enable it.

**Smartlead:** Campaign Settings → AI Categorization → Enable.
**Instantly:** Lead Labels → Enable AI Prediction on default labels (monthly quota: 500/30d).

Combined with a webhook, you can automate:
- Positive reply → Slack notification with customer details + quick-reply template
- Negative reply → auto-mark as not-interested, no notification
- OOO → auto-reschedule, no notification
- Wrong person → notification to manually redirect

---

## Weekly inbox review (always do this)

Every Monday morning:

1. Review **all** positive replies from last week
2. Review **manually** 10-20 AI-categorized replies to check accuracy
3. If AI is mis-categorizing, retrain (both platforms let you provide feedback)
4. Archive handled threads
5. Note patterns: same objection repeated → rewrite your copy to address it

Never let replies sit unread for more than a weekend.

---

## Common mistakes

1. **Replying from a branded account** — reply from the same inbox the cold email came from. Consistency matters for deliverability.
2. **Over-responding** — long, flowery responses feel salesy. Keep replies shorter than the original email.
3. **Ignoring unsubscribes** — block immediately, across every campaign. It's also the right thing to do.
4. **Taking offense at negatives** — "no" isn't personal. Exit gracefully, move on.
5. **Not booking the call fast enough** — positive replies that sit for 24+ hours lose 50% of their booking potential.
6. **Replying with a calendar link only** — offer 2 specific times first, calendar as fallback. Calendar-first feels lazy.
