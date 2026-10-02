# 01 — Deliverability Fundamentals

Read this once before buying anything. Understanding deliverability is the difference between a working campaign and a campaign where nobody sees your emails.

---

## Why cold email needs its own infrastructure

You cannot send cold email from your main business domain without risking blacklisting that domain's sending reputation. If `youremail@yourcompany.com` gets flagged as spam, your regular business mail — invoices, customer support, quotes — can start landing in spam folders too. This is a career-ending mistake.

**The solution:** Buy throwaway lookalike domains (e.g. `trygrowth.co` when your main is `growth.com`), warm them up, send cold email from those, and rotate across many inboxes. If one gets burned, you throw it away and buy another for $3.

This is how every cold email operator works. It's not a hack, it's the standard.

---

## The anatomy of a cold email send

When you send an email, the receiving server (Gmail, Outlook, Yahoo) makes a spam decision based on:

1. **Sender reputation** — has this domain/IP sent good mail before?
2. **Authentication** — SPF, DKIM, DMARC present and passing?
3. **Content** — does the email look like spam (em dashes, caps, spammy words)?
4. **Engagement** — do recipients open, reply, mark as not spam?
5. **Volume patterns** — is this sender ramping naturally or hitting suddenly?

You control all five. We'll cover each.

---

## SPF, DKIM, DMARC — what they are, why you don't have to touch them

These are DNS records that prove you own the domain you're sending from. They're the difference between "delivered" and "rejected."

- **SPF (Sender Policy Framework)** — says "these specific IPs are allowed to send mail as this domain"
- **DKIM (DomainKeys Identified Mail)** — cryptographic signature that proves the message wasn't tampered with in transit
- **DMARC (Domain-based Message Authentication)** — tells receivers what to do if SPF or DKIM fails (quarantine, reject, report)

**The good news:** Zapmail sets all three automatically when you connect a domain. You don't have to learn DNS editing. This is a huge reason we use Zapmail over rolling your own Google Workspace accounts.

**Verify they're set** (do this after inbox provisioning, before sending):
```bash
dig TXT yourdomain.com                    # should show "v=spf1 ..."
dig TXT _dmarc.yourdomain.com             # should show "v=DMARC1 ..."
```

If either is missing, something went wrong in the Zapmail setup. Re-run the connect step or check the Zapmail UI.

---

## The math of a cold email campaign

Cold email runs on inbox-per-day limits. Violate them and you get flagged.

**Post-warmup sending rate: 30 emails/day/inbox.** That's the safe ceiling for Gmail/Outlook cold sending. Some operators push 50, but 30 is the sensible default.

**Campaign capacity math:**
- 1 inbox × 30/day = 30 sends/day
- 20 domains × 2 inboxes × 30 = **1,200 sends/day**

**How long does a 2,000-lead campaign take?**
- 1,200/day ÷ 2,000 leads = ~1.7 days to finish Email 1
- 4-step sequence × 2,000 = 8,000 total sends
- 8,000 ÷ 1,200 = ~7 days to complete the full sequence

**Scaling:**
- Need more throughput? Buy more inboxes. Never push individual inbox limits up.
- 40 inboxes = 1,200/day. 80 inboxes = 2,400/day. Linear scaling.

---

## Warmup — what, how long, why

New inboxes have zero sending reputation. If you immediately blast 30 cold emails/day from a brand-new inbox, spam filters flag it.

**Warmup** is automated software that sends emails between your inboxes and a pool of other inboxes (Smartlead, Instantly, and most warmup tools have this). The emails look like real conversations — they get opened, replied to, marked as important. This builds a positive sending history before you send real cold email.

**Recommended schedule:**

| Week | Warmup emails/day | Real cold emails/day |
|---|---|---|
| Week 1 | 5-10 | 0 |
| Week 2 | 15-20 | 0 |
| Week 3 | 30 (full) | 5-10 (ramp) |
| Week 4+ | 30 (maintain) | 30 (full cold) |

**Minimum: 2 weeks warmup.** 3-4 weeks is better.

Both Smartlead and Instantly have built-in warmup. Enable it the moment you create an inbox. Zapmail inboxes are auto-connected to both platforms' warmup during export.

---

## Domain strategy

**Rule 1: Buy many domains, not one.**

Start with 10-20 cheap domains. Reason: if one gets burned (blacklisted, high spam complaints), you throw it away and the rest keep sending. With only 1 domain, one bad week ends your whole operation.

**Rule 2: Use reputable, trusted TLDs.**

Stick to `.com` or `.co` for cold email. Recipients pattern-match on TLD in under a second — `.com` and `.co` pass that test, weirder TLDs don't.

| TLD | Cost | Use? |
|---|---|---|
| `.com` | ~$10-14 | **Yes — primary recommendation.** Highest trust, best deliverability. |
| `.co` | ~$8-30 | **Yes — secondary.** Looks professional, often available when .com is taken. |
| `.net` | ~$12 | OK. Slightly less trusted than .com but fine. |
| `.org` | ~$10 | OK for nonprofit/association-adjacent businesses; otherwise looks odd. |
| `.io` | ~$30+ | Expensive. Trusted in tech circles but overpriced for throwaway sending domains. |
| `.info` | ~$3 | Avoid for external recipients — lower inbox trust. Cheap for internal/test only. |
| `.xyz`, `.click`, `.top`, `.loan`, `.buzz` | cheap | **No** — these are heavily spam-flagged. Do not use. |

Default to `.com`. If your preferred .com is taken, go `.co`. Stay away from everything else.

**Rule 3: Pick lookalike patterns, not random names.**

Your sending domain should be plausibly related to your real company. If your main is `growth.com`, good lookalikes are:
- `trygrowth.co`
- `getgrowth.co`
- `growthhq.com` (if available)
- `growth-co.com`
- `hellogrowth.co`

Bad: `qztop9.xyz`, `mail-sender-pro.click`. These scream spam.

**Rule 4: Max 2 inboxes per domain.**

3+ inboxes per domain hurts reputation. 2 is the sweet spot — you can use `firstname@` and `firstnamelastname@` patterns.

---

## Inbox rotation

Both Smartlead and Instantly automatically rotate sends across your inbox pool. This is good — never send all 2,000 leads from one inbox. If one gets rate-limited or flagged, the rest keep sending.

Don't override the auto-rotation unless you know exactly why.

---

## When reputation is burned

Signs your inbox/domain is in trouble:
- **Open rate < 20%** (normal is 40-60%)
- **Bounce rate > 5%** (normal is < 3%)
- **Blacklist hit** (check MXToolbox: https://mxtoolbox.com/blacklists.aspx)
- **Gmail/Outlook show warning banner** on delivered mail
- **Reply rate drops to near-zero** for no obvious reason

**What to do:**
1. Pause sending from that domain immediately
2. Don't try to "save" it — you can't resurrect a burned domain
3. Warm a replacement
4. Investigate *why* (bad list? bad copy? over-sending?)

This is why we buy 20 domains, not 1.

---

## Pre-launch deliverability check

Before your first real send, do this:

1. **DNS verification** — `dig TXT yourdomain.com` shows SPF, `dig TXT _dmarc.yourdomain.com` shows DMARC
2. **Test send to yourself** — personal Gmail AND personal Outlook. Both should land in **primary inbox**, not spam/promotions
3. **Test send to a buddy** — have a friend at a different domain receive one and tell you where it landed
4. **MXToolbox blacklist check** — https://mxtoolbox.com/blacklists.aspx → paste your sending domain → should show no listings
5. **Read `references/12-launch-checklist.md`** — it's the full pre-flight QA

---

## Bottom line

Deliverability is 80% infrastructure (domains, warmup, DNS) and 20% content (copy, subject lines). Most beginners obsess over subject lines. Obsess over infrastructure first. Great copy from a burned domain still lands in spam.
