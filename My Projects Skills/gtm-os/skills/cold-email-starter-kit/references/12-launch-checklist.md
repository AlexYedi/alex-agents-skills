# 12 — Launch Checklist

Run through this list before pressing "Start campaign." It's the difference between a clean launch and a burned domain.

---

## Sender identity

- [ ] **From name** is a real person (not "info", "sales", "team")
- [ ] **From email** domain matches the sending domain (not a mix)
- [ ] **Reply-to** goes somewhere you actually monitor
- [ ] **Signature** includes your name, company, and physical address
- [ ] **Signature** does NOT include a logo image (tracking pixel risk)

---

## Compliance

- [ ] **Unsubscribe link** OR unsubscribe instruction in every email
- [ ] **Physical mailing address** in footer (real or PO box)
- [ ] **Privacy policy link** (if sending to EU/UK/Canada)
- [ ] **List source is legitimate** (Prospeo, Apollo, Blitz — not random lead sellers)
- [ ] **Block list / suppression list** loaded from prior campaigns

See `references/11-legal-compliance.md` for the legal details.

---

## Deliverability infrastructure

- [ ] **SPF** record set on every sending domain — verify: `dig TXT yourdomain.com` shows `v=spf1 ...`
- [ ] **DKIM** record set — verify in Zapmail dashboard or with `dig TXT selector._domainkey.yourdomain.com`
- [ ] **DMARC** record set — verify: `dig TXT _dmarc.yourdomain.com` shows `v=DMARC1 ...`
- [ ] **All inboxes warmed** for at least 2 weeks
- [ ] **No blacklist hits** — check https://mxtoolbox.com/blacklists.aspx for your sending domain
- [ ] **Test sends landed in primary inbox** (not spam, not promotions) at personal Gmail AND personal Outlook

---

## Copy quality

- [ ] **Run through QA checklist** in `03-campaign-copywriting.md`
- [ ] **No em dashes (—)** anywhere — Gmail flags these
- [ ] **No banned phrases** ("I hope this finds you well", "Quick question", "Curious")
- [ ] **Word count 50-90** per email (or justified up to 125 with strong AI personalization)
- [ ] **4-step sequence** with proper delays (Day 0, 3-4, 7-8, 11-12)
- [ ] **Email 2 threads** (blank subject), Email 3 is a new thread (new subject)
- [ ] **Spintax** applied to subject, first line, and CTA (3-5 spin points per email)
- [ ] **All variables resolved** on a 5-lead preview (no literal `{{first_name}}` leaking through)
- [ ] **Subject lines are 2-4 words** OR a whole-offer subject — not "Curious" or "Quick question"

---

## Lead list

- [ ] **Deduplicated** (no email appears twice)
- [ ] **Email-verified** via MillionVerifier or similar — aim for < 3% predicted bounce rate
- [ ] **Bad-title filter applied** (remove "assistant", "intern", "student" unless targeted)
- [ ] **Excluded domains** list honored (your competitors, existing customers, past unsubscribes)
- [ ] **All required variables populated** (first_name, company_name, etc.) — rows missing required vars should be filtered out
- [ ] **Tested on 5 preview leads** before full upload

---

## Sending configuration

- [ ] **Daily send limit**: 30/inbox (never more)
- [ ] **Schedule**: Business hours in recipient's timezone
- [ ] **Schedule**: Weekdays only (skip Saturday + Sunday)
- [ ] **Inbox rotation**: enabled (default on both platforms)
- [ ] **Tracking links**: enabled if you want open/click data (note: affects deliverability slightly)
- [ ] **Unsubscribe tracking**: enabled
- [ ] **Bounce pause**: enabled (auto-pause leads that bounce)
- [ ] **Reply pause**: enabled (stop sequence on reply)

---

## Monitoring setup

- [ ] **Master inbox** (Smartlead) or **Unibox** (Instantly) has mobile notifications enabled
- [ ] **AI reply categorization** enabled
- [ ] **Webhook for positive replies** wired to Slack/SMS/email if you want real-time alerts
- [ ] **Analytics pull schedule** set up (daily or weekly CSV via `scripts/*-pull-analytics.ts`)
- [ ] **Reply templates** ready (positive, negative, OOO, wrong person, unsubscribe)

---

## Final test

- [ ] **Send to yourself** — preview one email in the sequence, check how it looks in your own Gmail/Outlook
- [ ] **Check preview text** — the first 50-100 chars are what appears in the inbox preview. They should be compelling.
- [ ] **Check rendering** — does it look natural, not over-formatted?
- [ ] **Reply to yourself** — verify your reply routing works and lands in the master inbox
- [ ] **Test unsubscribe** — click the unsubscribe link from a test send, verify the block list is updated

---

## Go/no-go

If all above are ✅, hit "Start."

If even one is ❌, fix it first. Most launch-day failures come from skipping checklist items.

---

## Post-launch monitoring (day 1)

After hitting start, check back in 2-4 hours:

- **Sent count** matches expected (daily limit × active inboxes)
- **Bounce rate** < 5% (if higher, pause immediately and investigate)
- **Error count** is 0 — sending platform shows no auth/config errors
- **First replies** if any — respond immediately

Then check again at end of day 1, day 2, day 3. After that, weekly is enough unless something looks wrong.

---

## Expected first-campaign metrics

Don't panic if your first campaign's numbers look different from what "experts" claim online. Realistic ranges:

| Metric | Poor | OK | Good | Excellent |
|---|---|---|---|---|
| Open rate | < 30% | 30-45% | 45-60% | > 60% |
| Reply rate | < 1% | 1-3% | 3-5% | > 5% |
| Positive reply rate | < 0.3% | 0.3-1% | 1-2% | > 2% |
| Bounce rate | > 5% | 3-5% | 1-3% | < 1% |

If you're in "OK" or better across all four metrics on your first campaign, you shipped a successful first campaign.
