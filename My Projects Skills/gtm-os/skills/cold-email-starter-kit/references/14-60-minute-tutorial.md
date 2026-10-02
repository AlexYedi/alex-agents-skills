# 14 — The 60-Minute First Campaign Tutorial

This is a literal, step-by-step walkthrough. Follow it exactly. At the end you'll have a real campaign sending real emails.

**Assumptions:**
- You installed this skill at `<repo>/skills/cold-email-starter-kit/`
- You have Node.js 20+ and `tsx` installed
- You have a product or service to sell
- You have ~$200 and a credit card
- You have a website (doesn't need to be fancy)

**What you'll spend:** ~$186 month 1, ~$126/month recurring.

**Total wall-clock time:** ~60 minutes of active work + ~6 hours of waiting (DNS propagation, inbox provisioning). The wait is unavoidable.

---

## Day 1 — Active work: ~45 minutes

### Minute 0-10: Sign up for accounts

Open 5 browser tabs and sign up at each:

1. **Dynadot** — https://www.dynadot.com/account/signup.html
   - After signup, top up wallet: Tools → Account → Add Funds → $100
   - Tools → API → Enable API Access → **copy the API key**
   - Tools → API → IP Whitelist → paste your IP from https://whatismyip.com

2. **Zapmail** — https://zapmail.ai/
   - After signup: Settings → API → **copy the API token**

3. **Prospeo** — https://prospeo.io/
   - After signup, buy Starter credits (~$49 for 1,000)
   - Dashboard → Integrations → API → **copy the API key**

4. **Smartlead** — https://app.smartlead.ai/auth/sign-up (recommended for beginners)
   - Or Instantly: https://app.instantly.ai/signup (if you want more features)
   - After signup: Settings → API Keys → Create new → **copy the key**

5. **(Optional, skip for first campaign)** OpenRouter, Blitz, RapidAPI — for enrichment later

---

### Minute 10-12: Configure `.env`

```bash
cd <repo>/skills/cold-email-starter-kit
cp .env.example .env
# open .env in your editor
```

Paste the keys you collected. Save.

---

### Minute 12-14: Verify credentials

```bash
npx tsx scripts/verify-credentials.ts
```

Expected:
```
Service       Status  Notes
Dynadot       ✅      Wallet: $127.50
Zapmail       ✅      0 domains, 0 inboxes
Prospeo       ✅      1000 credits
Smartlead     ✅      0 campaigns
Instantly     ⚠️       Not configured (optional)
```

If anything is ❌, fix before continuing. See `13-troubleshooting.md` for auth issues.

---

### Minute 14-20: Generate campaign strategy

In a Claude Code session (could be this one), say:

```
Use the campaign-strategy skill. My website is https://YOUR-WEBSITE.com
```

Claude reads your site, analyzes case studies, and generates 15-20 campaign ideas.

**For your first campaign**, pick the **Creative Ideas** campaign (always included). It's the safest starter because:
- Works with broad targeting
- No complex enrichment required
- Proven across virtually all industries

---

### Minute 20-30: Write the copy

Still in Claude Code:

```
Use the campaign-copywriting skill. I picked the Creative Ideas campaign from the strategy output.
```

Claude walks you through 4 confirmation steps:
1. Campaign direction (target, pain, value prop)
2. Subject line + first line options (pick one)
3. Body structure (case study, CTA, variables)
4. Final copy with all variants

Save the output to `sequence.json` (or copy the 4 emails somewhere you can paste later).

**Tip:** For your first campaign, keep it simple. No AI personalization variables. Static copy only. You can add sophistication later.

---

### Minute 30-35: Buy domains

```bash
# Step 1: generate candidates
npx tsx scripts/dynadot-generate-domains.ts \
  --brand YOURBRAND \
  --count 20 \
  --tld com

# Review the list printed (you'll see ~20 available .com domains with prices)
# If most .coms are taken, re-run with --tld co as fallback.

# Step 2: purchase
npx tsx scripts/dynadot-bulk-purchase.ts \
  --list generated-domains.csv
```

You'll see:
```
About to purchase 20 .com domains for $240.00. Your wallet: $300.00. Confirm? (y/N)
```

Type `y`. Script buys them one by one and logs results to `purchased-domains.csv`.

---

### Minute 35-36: Start DNS switch and walk away

```bash
npx tsx scripts/zapmail-full-setup.ts \
  --domains purchased-domains.csv \
  --first-name "Jane" \
  --last-name "Doe" \
  --inboxes-per-domain 2 \
  --platform smartlead
```

This kicks off the 4-phase workflow:
1. Dynadot NS switch (1 minute)
2. Wait 20 minutes for DNS
3. Zapmail connect (1 minute)
4. Poll assignable (5-15 minutes)
5. Create inboxes (1 minute)
6. Wait 4-6 hours for provisioning
7. Export to Smartlead (1 minute)

**The script runs non-interactively and uses `caffeinate` (on macOS) to prevent sleep.** You can minimize the terminal and come back later. A macOS notification fires when it finishes.

---

### Minute 36-45: Pull a lead list

While inboxes are provisioning, get your lead list ready.

Pick a simple target. Example: "VP of Sales at US SaaS companies, 50-200 employees":

```bash
npx tsx scripts/prospeo-full-export.ts \
  --title "VP Sales" \
  --title "Vice President Sales" \
  --title "Head of Sales" \
  --location "United States" \
  --headcount-min 50 \
  --headcount-max 200 \
  --industry "Software Development" \
  --industry "Computer Software" \
  --limit 2000 \
  --output leads.csv
```

**Tip:** Drop "of" from titles (Eric's rule — improves match rate). Always include synonym titles.

You'll see:
```
Found 4,821 matches. Will pull top 2000 (costs ~2000 credits). Confirm? (y/N)
```

Type `y`. Script pulls leads page by page. Takes 2-3 minutes.

---

### Minute 45: You're done with active work for Day 1

Make coffee. Your inboxes are provisioning for 4-6 hours.

---

## Day 1 — Passive wait: ~6 hours

Zapmail is provisioning your 40 inboxes. You'll get a macOS notification when complete. In the meantime:
- Read `01-deliverability-fundamentals.md` to understand what's happening
- Read `10-reply-handling.md` so you're ready when replies come in

---

## Day 2 — Launch: ~15 minutes

### Minute 0-5: Verify inboxes provisioned

```bash
smartlead email-accounts list
# Should show 40 accounts, all with warmup_status=ACTIVE
```

If any show `IN_PROGRESS`, wait another hour and check again.

---

### Minute 5-10: Upload to Smartlead

```bash
npx tsx scripts/smartlead-create-campaign.ts \
  --name "My First Campaign" \
  --sequence sequence.json \
  --leads leads.csv
```

Script creates the campaign, saves your sequence, attaches all 40 email accounts, adds leads in batches of 100, and prints:

```
✅ Campaign created: https://app.smartlead.ai/campaigns/12345
   - 2000 leads added
   - 40 email accounts attached
   - 4-step sequence saved
   - Status: DRAFT

Next: Visit the URL, run the launch checklist, hit Start.
```

---

### Minute 10-15: Run launch checklist

Open the Smartlead URL. Walk through `references/12-launch-checklist.md` item by item in the Smartlead UI:

- Sender identity — ✓
- Unsubscribe link — ✓
- Physical address in footer — ✓
- SPF/DKIM/DMARC on all domains — ✓ (verify with `dig`)
- Warmup status — ✓ (should be ACTIVE on all)
- Schedule: M-F business hours — ✓
- Daily limit: 30/inbox — ✓
- Test send to yourself — ✓

Send one email to yourself as a final sanity check. Make sure it lands in your primary inbox.

---

### Minute 15: Hit Start

Campaign begins sending. You're officially running cold email.

---

## Day 2+ — Monitor

### End of Day 2 (4-6 hours after launch)

```bash
npx tsx scripts/smartlead-pull-analytics.ts --campaign-id 12345 --csv
```

Expected by end of day 1:
- Sent: ~1,000-1,200 (whatever your daily cap × inboxes allows)
- Bounce rate: < 3%
- Open rate: still catching up, meaningful numbers come after 24h
- Replies: 0-5

---

### Day 3-4

Email 2 starts going out (Day 3 threaded follow-up).
First replies should start appearing. Read `10-reply-handling.md`.

---

### Day 7-8

Email 3 goes out (new thread, different angle).
By now you should have 10-40 replies to process.

---

### Day 11-14

Email 4 goes out (final).
Campaign wraps up around Day 15.

---

### Expected full-sequence metrics

For a 2,000-lead campaign with decent targeting and copy:

- **Total sent**: ~8,000 (2K leads × 4 steps)
- **Open rate**: 40-60%
- **Reply rate**: 1-3% (20-60 replies)
- **Positive reply rate**: 0.3-1% (6-20 meetings worth booking)
- **Bounce rate**: < 3%

If you're in those ranges on your first campaign, **you shipped a successful first campaign.**

---

## Common first-campaign problems

| Problem | Fix |
|---|---|
| 0 replies by Day 3 | Normal — most replies come in Email 2-3 |
| High bounce on Day 1 | Pause, re-verify list, resume |
| Landing in spam | Check SPF/DKIM/DMARC, check blacklists |
| Positive reply came, don't know what to say | `10-reply-handling.md` has templates |
| Negative reply | Accept gracefully, move on — `10-reply-handling.md` |
| Unsubscribe | Immediately add to block list — `11-legal-compliance.md` |

---

## After your first campaign

1. **Export analytics** to CSV for record-keeping
2. **Write a retro** — what worked, what didn't, what surprised you
3. **Rewrite your worst variant** — improve based on what you learned
4. **Launch campaign #2** — same infrastructure, different targeting or copy
5. **Add enrichment** — layer in `{{ai_customer_type}}` variables for more personalization (see `07-enrichment-library.md`)

The first campaign is just the beginning. The compounding benefit comes from running 5-10 campaigns with the same infrastructure, learning from each one.
