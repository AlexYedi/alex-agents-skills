# 13 — Troubleshooting

Symptom → cause → fix matrix. Start here when something breaks.

---

## Error matrix

| Symptom | Likely cause | Fix |
|---|---|---|
| Bounce rate > 5% | Bad list quality | Re-verify the list with MillionVerifier before next send |
| Bounce rate > 10% | Blacklist hit or very bad list | Pause immediately. Check MXToolbox. Throw away the list or domain. |
| Open rate < 30% | Deliverability / reputation issue | Check SPF/DKIM/DMARC, pause that inbox, warm a replacement |
| Open rate 30-40% | Subject line is weak | Rewrite subjects, A/B test |
| Reply rate 0% after 500+ sends | Copy is off | Rewrite first line, re-run QA checklist |
| Emails landing in spam | Missing SPF/DKIM/DMARC OR reputation burned | Re-verify DNS, pause + warm replacement |
| Gmail shows "via" warning | Sender domain doesn't match from address | Check your sending domain config |
| "Invalid API key" (Smartlead) | Wrong/expired key, or using sub-client key without `client_id` | Regenerate from Smartlead Settings → API Keys |
| "401 Unauthorized" (Instantly) | Wrong Bearer token format | Header must be exactly `Authorization: Bearer {key}` |
| Dynadot "IP_NOT_ALLOWED" | IP not whitelisted | Add current IP at Tools → API → Whitelist |
| Dynadot "NS_MISMATCH" on connect | NS propagation not done | Wait 15-20 min, retry |
| Zapmail "DOMAIN_NOT_CONNECTED" | Connect step skipped or failed | Re-run connect, wait, poll `/domains/assignable` |
| Zapmail "INBOX_PROVISION_PENDING" | Normal — 4-6 hour wait | Come back later, it's provisioning |
| Zapmail export returns 0 mailboxes | Status filter mismatch | Always filter by `status: "ACTIVE"`, not "IN_PROGRESS" |
| Zapmail batch inbox returns 400 | One mailbox already exists | Retry failed domains individually |
| Rate limit 429 (any API) | Too many requests | Exponential backoff (1s → 2s → 4s → 8s → 16s) |
| Prospeo returns 0 results | Filters too strict | Remove one filter at a time; drop "of" from titles; add synonyms |
| Prospeo "INSUFFICIENT_CREDITS" | Out of credits | Top up on Prospeo dashboard |
| Smartlead "Duplicate lead" | Email already in campaign | Use `?ignore_duplicate=true` or dedupe first |
| Instantly `bulk-create` fails | Over 1000 leads per call | Split into batches of 1000 |
| Variables show literal `{{var}}` in sent emails | CSV column name doesn't match variable | Column names must exactly match: `first_name`, `company_name`, `ai_customer_type`, etc. |
| High open rate but 0 replies | CTA is too high-effort or copy lacks specificity | Shorten CTA to 5 words or less, add specific research signal |

---

## Diagnostic commands

Run these when something feels off:

### DNS verification
```bash
dig TXT yourdomain.com             # should show SPF
dig TXT _dmarc.yourdomain.com      # should show DMARC
dig MX yourdomain.com              # should point to Zapmail MX
```

### Auth verification
```bash
# Smartlead auth test
curl -I "https://server.smartlead.ai/api/v1/campaigns?api_key=$SMARTLEAD_API_KEY"
# Should return 200

# Instantly auth test
curl -H "Authorization: Bearer $INSTANTLY_API_KEY" "https://api.instantly.ai/api/v2/workspace"
# Should return 200 with workspace details

# Dynadot auth test
curl "https://api.dynadot.com/api3.json?key=$DYNADOT_API_KEY&command=account_info"
# Should return wallet balance

# Zapmail auth test
curl -H "x-auth-zapmail: $ZAPMAIL_API_KEY" "https://api.zapmail.ai/api/v2/domains/assignable?limit=5&page=1"
# Should return a list of domains (possibly empty)

# Prospeo auth test
curl -X POST "https://api.prospeo.io/search-person" \
  -H "X-KEY: $PROSPEO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page":1,"filters":{"person_location_search":{"include":["California, United States #US"]}}}'
# Should return results
```

### Blacklist check
- https://mxtoolbox.com/blacklists.aspx → enter your sending domain
- https://www.mail-tester.com → send a test email, get a deliverability score

---

## "I don't know where to start" flow

Follow this decision tree when you're stuck:

1. **Is it a config error?** (401/403 responses, missing env var) → Re-check `.env`, run `scripts/verify-credentials.ts`
2. **Is it a deliverability issue?** (low opens, spam folder) → Read `01-deliverability-fundamentals.md`, check DNS + blacklists
3. **Is it a copy issue?** (opens are fine, no replies) → Re-run QA checklist in `03-campaign-copywriting.md`
4. **Is it a list issue?** (high bounces, no engagement) → Re-verify list, review `06-list-building-prospeo.md` filters
5. **Is it a sequence issue?** (engagement drops off after email 1) → Review `04-sequence-structure.md`, check that follow-ups are meaningfully different from email 1
6. **Still stuck?** Post redacted details to r/coldemail or r/salesdevelopment

---

## Specific problems

### "I bought domains but Dynadot says my IP isn't whitelisted"

Dynadot is strict about this. Steps:
1. Go to https://whatismyip.com — note your current IP
2. Dynadot → Tools → API → IP Whitelist → Add
3. Wait 60 seconds
4. Retry

If your IP changes often (mobile hotspot, VPN), whitelist a /24 subnet range or use a dedicated server.

### "Emails land in spam despite warmup"

Possible causes:
1. **Em dashes in copy** — remove ALL `—` characters
2. **Spammy words** — "guaranteed", "free", "winner", "urgent" trigger filters
3. **Single-word sender names** — "Jane" looks more human than "Sales"
4. **Too much HTML** — stick to plain-text formatting
5. **Old reputation** — burned domains can't be saved, warm a replacement
6. **List is full of dead addresses** — re-verify with MillionVerifier

Use https://www.mail-tester.com to score your email. Target: 9/10 or higher.

### "My master inbox is empty but the campaign says replies"

Check that your reply-to address matches the sending domain. If you set `reply_to: jane@different-domain.com`, replies route there instead of the master inbox.

### "Instantly API returns 401"

- Verify exact header: `Authorization: Bearer XXX` (capital B in Bearer)
- Check that your API key is from Instantly v2 (not v1 — v1 is deprecated)
- Check that your workspace hasn't run out of API quota

### "Smartlead `POST /campaigns/{id}/leads` returns 400"

Common causes:
- Missing required fields (email is always required)
- Body format wrong — should be `{ "lead_list": [...] }`, not `[...]`
- Batch too big — cap at 100 per call
- `client_id` mismatch if using sub-client key

### "Zapmail says my domain isn't assignable"

- Did you wait 15+ minutes after NS switch? DNS propagation takes time.
- Did the connect step succeed? Re-run if unsure.
- Is the domain status "IN_PROGRESS"? That means it's still verifying. Poll every 5 minutes.

---

## When to throw in the towel (and start over)

Some problems aren't worth debugging. Throw away and restart when:

- A domain is on 3+ blacklists
- Open rate stays below 20% after trying everything
- Bounce rate stays above 8% with a re-verified list
- An API key has been leaked (regenerate immediately)

Cold email infrastructure is disposable. A domain costs $3. Your time is worth more than preserving a burned sender.

---

## Getting help

1. **Re-read** the specific reference file for what you're doing (e.g., `05-domain-and-inbox-setup.md` for inbox issues)
2. **Search** the platform's documentation — Smartlead Help Center, Instantly docs
3. **r/coldemail** — active community, helpful for general questions
4. **Smartlead / Instantly Slack communities** — official channels with engineers
5. **Paid**: Pick a cold email consultant for 1 hour of help ($100-300). Cheaper than wasting a week debugging.
