# 07 — Enrichment Library

Optional enrichments that add personalization data to your leads after list building. All run as standalone scripts — no external database required.

---

## When do you actually need enrichment?

**Skip this entirely for your first campaign.** Seriously. Ship a plain campaign first, get baseline metrics, then add enrichment.

Use enrichment when:
- Your copy references specific data (`{{ai_customer_type}}`, `{{nearby_restaurant}}`, `{{recent_news}}`)
- You've shipped 1+ campaigns without AI and want to measure lift
- You're doing hyper-personalized premium outreach

Don't use enrichment when:
- You're sending a simple static campaign
- You're in your first month of cold email
- Your targeting is already narrow enough that personalization is noise

---

## How enrichments work

Each enrichment:
1. Reads a CSV of leads
2. Calls an external API (rate-limited)
3. Writes an enriched CSV with new columns
4. Fails gracefully on individual bad rows — never crashes the batch

Run order: always email finding first (Prospeo), then enrichments in sequence:
```bash
npx tsx scripts/enrichments/ai-company-analysis.ts --input leads.csv --output leads-v1.csv
npx tsx scripts/enrichments/company-phone.ts --input leads-v1.csv --output leads-v2.csv
npx tsx scripts/enrichments/company-news.ts --input leads-v2.csv --output leads-final.csv
```

---

## The 5 enrichments

### 1. Company phone finder

**Script:** `scripts/enrichments/company-phone.ts`
**API:** Blitz `/api/enrichment/company`
**Signup:** https://blitz.us/
**Cost:** ~$15 per 1,000 leads (~$50/mo small tier)
**Rate limit:** 30 requests/second
**Adds column:** `company_phone`

**Use case:** "I saw the number for {{company_name}} but figured email would be easier." Adds legitimacy — you've clearly done research.

**Run:**
```bash
npx tsx scripts/enrichments/company-phone.ts \
  --input leads.csv \
  --output leads-with-phone.csv
```

**Failure modes:**
- Blitz doesn't have the company → writes empty string, continues
- Rate limit 429 → exponential backoff
- Auth error → exits 1 with clear message

---

### 2. AI company analysis (GPT-4o-mini)

**Script:** `scripts/enrichments/ai-company-analysis.ts`
**API:** OpenRouter (via `openai/gpt-4o-mini`)
**Signup:** https://openrouter.ai/
**Cost:** ~$0.15 per 1,000 leads (roughly one-fifth of a cent per lead)
**Rate limit:** 50 requests/second
**Adds columns:** `ai_company_summary`, `ai_industry_category`, `ai_customer_type`, `ai_company_mission`

**Use case:** Enables `{{ai_*}}` variables in your copy. "So you can focus on {{ai_company_mission}}..." type lines.

**What the AI sees:** Company name, domain, headcount, LinkedIn description (from Prospeo data).
**What it returns:** One-sentence summary, industry vertical, customer type, company mission.

**Run:**
```bash
npx tsx scripts/enrichments/ai-company-analysis.ts \
  --input leads.csv \
  --output leads-ai.csv \
  --model openai/gpt-4o-mini
```

**Model choices (cost vs quality):**
- `openai/gpt-4o-mini` — default, fast, cheap
- `openai/gpt-4.1-nano` — even cheaper, slightly less reliable
- `anthropic/claude-haiku-4-5` — higher quality, 2-3× cost
- `openai/gpt-4o` — overkill for this task, don't use

**Failure modes:**
- Non-JSON response from the model → logs warning, writes nulls, continues
- Rate limit → backs off
- API error → continues with next lead

---

### 3. Company news (OpenWebNinja via RapidAPI)

**Script:** `scripts/enrichments/company-news.ts`
**API:** OpenWebNinja Google Search (via RapidAPI)
**Signup:** https://rapidapi.com/ → search "OpenWebNinja"
**Cost:** $10-25 per month depending on volume tier
**Rate limit:** 10 requests/second
**Adds columns:** `recent_news_title`, `recent_news_url`, `recent_news_date`, `recent_news_snippet`

**Use case:** Personalized first lines: "Saw your announcement about {{recent_news_title}}..."

**How it works:**
1. Searches Google for `"{company_name}" news OR blog OR case study` in the last 90 days
2. Filters out political, personal, and job-posting results (blocklist built-in)
3. Returns the top 3 articles per company

**Run:**
```bash
npx tsx scripts/enrichments/company-news.ts \
  --input leads.csv \
  --output leads-news.csv \
  --days 90
```

**Why 90 days:** Older news feels stale. Newer = more credible you did real research.

**Failure modes:**
- No news found → writes empty columns, continues (~30% of leads)
- Blocked domain (competitor, blocklist) → skipped
- Rate limit → backoff

---

### 4. Nearby business (RapidAPI Maps)

**Script:** `scripts/enrichments/nearby-business.ts` (advanced, not in default install)
**API:** RapidAPI Maps Data
**Cost:** ~$5 per 1,000 leads
**Rate limit:** 2 requests/second (slow — plan for this)
**Adds columns:** `nearby_business_name`, `nearby_business_type`, `nearby_business_rating`

**Use case:** Hyper-local personalization. "P.S. I saw Morton's across the street from your office, looks solid."

**Requires:** Lead data already has `lat`/`lng` coordinates (enrichment-first via Google Maps). Not applicable if you got leads from Prospeo (no location coordinates). Mostly used for local business campaigns sourced from Google Maps directly.

**Skip unless:** You're doing local SMB outreach to specific store locations.

---

### 5. LinkedIn profile scrape

> **[gtm-os local]** Script removed from this repo: it depends on a LinkedIn scraper, which gtm-os's locked ethics rule forbids (no LinkedIn/X scraping).

**Script:** `scripts/enrichments/linkedin-profile.ts` (removed)
**API:** RapidAPI LinkedIn Bulk Scraper
**Signup:** https://rapidapi.com/ → search "LinkedIn Bulk Scraper"
**Cost:** $25-75 per month
**Rate limit:** 5 requests/second
**Adds columns:** `linkedin_headline`, `linkedin_about`, `linkedin_tenure_years`, `linkedin_recent_post_topic`

**Use case:** Deep personalization from LinkedIn activity. "Saw your post about {{recent_post_topic}}..."

**Warning:** LinkedIn's terms prohibit scraping. Using this is a legal gray area. You're responsible for your own compliance. Consider alternatives (Prospeo already returns some LinkedIn data, OpenWebNinja finds their posts via Google).

**Run:**
```bash
npx tsx scripts/enrichments/linkedin-profile.ts \
  --input leads.csv \
  --output leads-linkedin.csv
```

---

## Enrichment output format

All enrichments append new columns to your CSV. After running all 3 default enrichments (AI, phone, news), your CSV has these added columns:

| Column | Source | Example |
|---|---|---|
| `ai_company_summary` | GPT-4o-mini | "B2B SaaS platform for field service teams" |
| `ai_industry_category` | GPT-4o-mini | "field service management" |
| `ai_customer_type` | GPT-4o-mini | "HVAC contractors and plumbers" |
| `ai_company_mission` | GPT-4o-mini | "helping field techs do better work" |
| `company_phone` | Blitz | "+1-555-0123" |
| `recent_news_title` | OpenWebNinja | "Acme Inc raises $12M Series A" |
| `recent_news_url` | OpenWebNinja | "https://techcrunch.com/..." |
| `recent_news_date` | OpenWebNinja | "2026-03-14" |
| `recent_news_snippet` | OpenWebNinja | "Acme Inc announced today..." |

These columns map directly to Smartlead/Instantly custom variables. In your email: `{{ai_customer_type}}`, `{{recent_news_title}}`, etc.

---

## Beginner recommendation

**Your first 3 campaigns:** skip all enrichment.
**Your 4th campaign:** add only AI company analysis (cheapest, biggest impact).
**Your 5th+:** layer in news + phone if your niche benefits.

Never pay for enrichment you can't directly trace to a reply-rate lift in your data.

---

## Cost efficiency tip

Always run enrichment AFTER email finding. Enriching leads without valid emails wastes API credits. The `email-waterfall` pattern (check cache → find email → enrich valid rows only) is standard.

---

## Fallback logic

Every enrichment script:
1. Wraps each API call in try/catch
2. Writes `null` for failed rows
3. Logs failures to `{script}-errors.csv` for later retry
4. Prints a summary at the end: `X enriched, Y failed, Z skipped`

You can re-run any enrichment on just the failed rows by feeding the errors CSV back in as input.
