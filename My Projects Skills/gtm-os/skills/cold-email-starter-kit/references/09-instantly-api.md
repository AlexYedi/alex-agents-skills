# 09 — Instantly API Reference

Full Instantly v2 endpoint reference. Written from Instantly's public OpenAPI spec (https://developer.instantly.ai/llms.txt).

## Quickstart

```bash
# Create a campaign, add leads, launch — end-to-end
npx tsx scripts/instantly-create-campaign.ts \
  --name "My First Campaign" \
  --sequence sequence.json \
  --leads leads.csv
```

See `scripts/instantly-create-campaign.ts`, `scripts/instantly-add-leads.ts`, and `scripts/instantly-pull-analytics.ts` for working end-to-end examples.

---

## Authentication

```
Authorization: Bearer {INSTANTLY_API_KEY}
```

Base URL: `https://api.instantly.ai`
Env var: `$INSTANTLY_API_KEY`

**Important:** Instantly uses **Bearer tokens** in a header, NOT query-param auth like Smartlead. If you see 401s, check that your header is exactly `Authorization: Bearer {key}` (not `Token {key}`, not `API-Key: {key}`).

---

## Rate Limiting

Documented rate limits:
- `GET /api/v2/emails` → **20 requests/min** (tightest limit — be careful)
- `POST /api/v2/emails/test` → 10 requests/min
- AI label prediction endpoint → 500 requests / 30 days (monthly quota, not per-minute)
- Everything else → not explicitly documented; use exponential backoff on 429

Recommended pattern: start with 10 rps concurrency, back off to 1 rps on 429, never retry past 5 attempts.

---

## TypeScript client pattern

```typescript
const INSTANTLY_API = "https://api.instantly.ai";
const API_KEY = process.env.INSTANTLY_API_KEY;

async function instantlyFetch(path: string, init: RequestInit = {}): Promise<Response> {
  const res = await fetch(`${INSTANTLY_API}${path}`, {
    ...init,
    headers: {
      "Authorization": `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
      ...init.headers,
    },
  });
  if (res.status === 429 || res.status >= 500) {
    // exponential backoff retry
    await new Promise(r => setTimeout(r, 1000 * Math.pow(2, (init as any)._attempt || 0)));
    return instantlyFetch(path, { ...init, _attempt: ((init as any)._attempt || 0) + 1 } as any);
  }
  return res;
}
```

---

## Endpoint reference

### Account Management (email sending accounts)

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/accounts` | Create new email account |
| `GET` | `/api/v2/accounts` | List all accounts |
| `GET` | `/api/v2/accounts/{id}` | Get account details |
| `PATCH` | `/api/v2/accounts/{id}` | Update config (warmup, daily limit, etc.) |
| `DELETE` | `/api/v2/accounts/{id}` | Remove account |
| `POST` | `/api/v2/accounts/{id}/pause` | Pause sending |
| `POST` | `/api/v2/accounts/{id}/resume` | Resume sending |
| `POST` | `/api/v2/accounts/{id}/mark-as-fixed` | Mark sending issue as resolved |
| `POST` | `/api/v2/accounts/disable-warmup` | Disable warmup (async job) |
| `POST` | `/api/v2/accounts/enable-warmup` | Enable warmup (async job) |
| `POST` | `/api/v2/accounts/move-between-workspaces` | Transfer accounts across workspaces |
| `GET` | `/api/v2/accounts/{id}/test-vitals` | Health check |
| `GET` | `/api/v2/accounts/{id}/custom-tracking-domain` | Check custom domain status |

### Campaigns

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/campaigns` | Create a new campaign |
| `GET` | `/api/v2/campaigns` | List all campaigns |
| `GET` | `/api/v2/campaigns/{id}` | Get campaign details |
| `PATCH` | `/api/v2/campaigns/{id}` | Update campaign |
| `DELETE` | `/api/v2/campaigns/{id}` | Delete campaign |
| `POST` | `/api/v2/campaigns/{id}/activate` | Start or resume |
| `POST` | `/api/v2/campaigns/{id}/pause` | Pause |
| `POST` | `/api/v2/campaigns/{id}/duplicate` | Clone config |
| `POST` | `/api/v2/campaigns/{id}/share` | Enable 7-day shareable link |
| `POST` | `/api/v2/campaigns/from-shared` | Create from shared template |
| `POST` | `/api/v2/campaigns/{id}/variables` | Add dynamic variables |
| `GET` | `/api/v2/campaigns/{id}/export` | Export as JSON |
| `GET` | `/api/v2/campaigns/search-by-email` | Find campaigns containing a lead email |
| `GET` | `/api/v2/campaigns/count-launched` | Count active campaigns |

### Campaign Analytics

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/v2/campaigns/analytics` | Single or batch campaign metrics |
| `GET` | `/api/v2/campaigns/analytics/overview` | High-level summary across all campaigns |
| `GET` | `/api/v2/campaigns/analytics/daily` | Daily performance breakdown |
| `GET` | `/api/v2/campaigns/{id}/analytics/steps` | Per-step metrics within a sequence |
| `GET` | `/api/v2/campaigns/{id}/sending-status` | Diagnose sending issues |

### Subsequences (branching follow-ups — Instantly-exclusive)

Subsequences are Instantly's killer feature: branch your follow-ups based on reply category. For example, positive reply → subsequence A (booking flow), OOO reply → subsequence B (reschedule flow).

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/subsequences` | Create subsequence |
| `GET` | `/api/v2/subsequences` | List subsequences |
| `GET` | `/api/v2/subsequences/{id}` | Get details |
| `PATCH` | `/api/v2/subsequences/{id}` | Update |
| `DELETE` | `/api/v2/subsequences/{id}` | Remove |
| `POST` | `/api/v2/subsequences/{id}/pause` | Pause execution |
| `POST` | `/api/v2/subsequences/{id}/resume` | Resume |
| `POST` | `/api/v2/subsequences/{id}/duplicate` | Clone |
| `GET` | `/api/v2/subsequences/{id}/sending-status` | Health |

### Lead Management

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/leads` | Create individual lead |
| `GET` | `/api/v2/leads/{id}` | Get lead |
| `PATCH` | `/api/v2/leads/{id}` | Update lead |
| `DELETE` | `/api/v2/leads/{id}` | Delete lead |
| `POST` | `/api/v2/leads/list` | Query leads with filters |
| `POST` | `/api/v2/leads/bulk-create` | **Add up to 1,000 leads in one request** |
| `POST` | `/api/v2/leads/bulk-delete` | Bulk delete |
| `POST` | `/api/v2/leads/bulk-assign` | Assign leads to team members |
| `POST` | `/api/v2/leads/{id}/merge` | Merge two lead records |
| `POST` | `/api/v2/leads/{id}/move` | Move between campaigns/lists |
| `POST` | `/api/v2/leads/{id}/subsequence/move` | Enroll in subsequence |
| `POST` | `/api/v2/leads/{id}/subsequence/remove` | Unenroll |
| `PATCH` | `/api/v2/leads/{id}/interest-status` | Update engagement (interested/not interested/meeting booked) |

### Lead Lists + Labels

| Method | Path | Purpose |
|---|---|---|
| `POST/GET/PATCH/DELETE` | `/api/v2/lead-lists[/{id}]` | CRUD on lead containers |
| `GET` | `/api/v2/lead-lists/{id}/verification-stats` | Email validation summary |
| `POST/GET/PATCH/DELETE` | `/api/v2/lead-labels[/{id}]` | CRUD on labels |
| `POST` | `/api/v2/lead-labels/test-ai-prediction` | Preview AI auto-tagging (quota: 500/month) |

### Email / Unibox (unified inbox)

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/v2/emails` | List emails (**20/min rate limit**) |
| `GET` | `/api/v2/emails/{id}` | Get email |
| `PATCH` | `/api/v2/emails/{id}` | Update metadata |
| `DELETE` | `/api/v2/emails/{id}` | Delete |
| `POST` | `/api/v2/emails/{id}/reply` | Send threaded reply |
| `POST` | `/api/v2/emails/{id}/forward` | Forward |
| `POST` | `/api/v2/emails/test` | Send test email (10/min limit) |
| `POST` | `/api/v2/emails/mark-thread-read` | Mark thread as read |
| `GET` | `/api/v2/emails/unread-count` | Get unread count |

### Email Verification

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/email-verification` | Verify single email |
| `GET` | `/api/v2/email-verification/{email}` | Check cached verification status |

### Block Lists (suppression)

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/block-list-entries` | Add entry |
| `GET` | `/api/v2/block-list-entries` | List |
| `GET` | `/api/v2/block-list-entries/{id}` | Get |
| `PATCH` | `/api/v2/block-list-entries/{id}` | Update |
| `DELETE` | `/api/v2/block-list-entries/{id}` | Remove |
| `POST` | `/api/v2/block-list-entries/bulk-create` | Bulk add |
| `POST` | `/api/v2/block-list-entries/bulk-delete` | Bulk remove |
| `POST` | `/api/v2/block-list-entries/delete-all` | Clear entire list |
| `GET` | `/api/v2/block-list-entries/export` | Download as CSV |

### Webhooks

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/webhooks` | Create webhook subscription |
| `GET` | `/api/v2/webhooks` | List all webhooks |
| `GET` | `/api/v2/webhooks/{id}` | Get details |
| `PATCH` | `/api/v2/webhooks/{id}` | Update settings |
| `DELETE` | `/api/v2/webhooks/{id}` | Remove |
| `POST` | `/api/v2/webhooks/{id}/test` | Fire test payload |
| `POST` | `/api/v2/webhooks/{id}/resume` | Re-enable after failures |
| `GET` | `/api/v2/webhooks/event-types` | List available event triggers |
| `GET` | `/api/v2/webhook-events[/{id}]` | Event history |
| `GET` | `/api/v2/webhook-events/overview` | Success/failure rates |
| `GET` | `/api/v2/webhook-events/overview-by-date` | Daily metrics |

### Inbox Placement Testing (Instantly-exclusive deliverability tool)

| Method | Path | Purpose |
|---|---|---|
| `POST/GET/PATCH/DELETE` | `/api/v2/inbox-placement-tests[/{id}]` | CRUD on deliverability tests |
| `GET` | `/api/v2/inbox-placement-tests/esp-options` | Available ESP (Gmail/Outlook/etc.) options |
| `GET` | `/api/v2/inbox-placement-analytics[/{id}]` | Test results |
| `GET` | `/api/v2/inbox-placement-analytics/by-date` | Time series |
| `GET` | `/api/v2/inbox-placement-analytics/{id}/insights` | Deliverability diagnosis |
| `POST` | `/api/v2/inbox-placement-analytics/by-test-ids` | Batch aggregation |
| `GET` | `/api/v2/inbox-placement-reports[/{id}]` | Blacklist + spam score details |

**Use case:** Before launching a real campaign, run a placement test to confirm your inboxes are landing in primary inbox (not spam/promotions) across Gmail, Outlook, Yahoo.

### SuperSearch Enrichment (Instantly's built-in lead enrichment)

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/enrichments` | Create enrichment job |
| `POST` | `/api/v2/enrichments/ai` | Create AI-powered enrichment |
| `POST` | `/api/v2/enrichments/supersearch` | Enrich via SuperSearch (Instantly's lead DB) |
| `GET` | `/api/v2/enrichments/{id}` | Get job details |
| `GET` | `/api/v2/enrichments/ai/{resource_id}` | Fetch AI enrichment config |
| `GET` | `/api/v2/enrichments/history` | Enrichment timeline |
| `POST` | `/api/v2/enrichments/count-leads` | Estimate lead availability |
| `POST` | `/api/v2/enrichments/preview-leads` | Sample without enriching |
| `POST` | `/api/v2/enrichments/{id}/run` | Execute |
| `PATCH` | `/api/v2/enrichments/{id}/settings` | Adjust auto-update rules |

Note: SuperSearch overlaps with Prospeo + our enrichment scripts. You can use either path. SuperSearch is more integrated; Prospeo is more flexible and cheaper.

### OAuth Account Connection

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/oauth/google/initialize` | Start Google OAuth flow |
| `POST` | `/api/v2/oauth/microsoft/initialize` | Start Microsoft OAuth flow |
| `GET` | `/api/v2/oauth/{session_id}/status` | Poll for completion |

OAuth is async. Initialize, then poll status until the user completes the grant.

### Workspace + Team

| Method | Path | Purpose |
|---|---|---|
| `GET/PATCH` | `/api/v2/workspace` | Current workspace info |
| `POST` | `/api/v2/workspace/change-owner` | Transfer ownership |
| `POST/GET/DELETE` | `/api/v2/workspace/agency-domain` | Custom agency domain |
| `POST/GET/PATCH/DELETE` | `/api/v2/workspace-members[/{id}]` | Team management |
| `POST/GET/DELETE` | `/api/v2/workspace-group-members[/{id}]` | Multi-workspace groups |
| `GET` | `/api/v2/workspace-group-members/admin` | Admin workspace info |
| `GET` | `/api/v2/workspace-billing/plan` | Plan details |
| `GET` | `/api/v2/workspace-billing/subscription` | Billing info |

### DFY Email Accounts (Instantly's done-for-you inbox orders)

Alternative to Zapmail — Instantly can order and set up inboxes for you.

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/dfy-email-account-orders` | Order inboxes |
| `GET` | `/api/v2/dfy-email-account-orders` | List orders |
| `DELETE` | `/api/v2/dfy-email-account-orders/{id}` | Cancel order |
| `GET` | `/api/v2/dfy-email-account-orders/ordered-accounts` | View provisioned accounts |
| `POST` | `/api/v2/dfy-email-account-orders/check-domains` | Check availability |
| `POST` | `/api/v2/dfy-email-account-orders/generate-domains` | Suggest domains |
| `GET` | `/api/v2/dfy-email-account-orders/prewarmed-domains` | List pre-warmed options |

### API Keys + Audit

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v2/api-keys` | Create new API key |
| `GET` | `/api/v2/api-keys` | List active keys |
| `DELETE` | `/api/v2/api-keys/{id}` | Revoke |
| `GET` | `/api/v2/audit-logs` | Activity history |

### Background Jobs

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/v2/background-jobs` | List async jobs |
| `GET` | `/api/v2/background-jobs/{id}` | Poll job status |

Used when an operation (warmup toggle, bulk import) runs async. Poll until complete.

### Custom Tags, CRM

| Method | Path | Purpose |
|---|---|---|
| `POST/GET/PATCH/DELETE` | `/api/v2/custom-tags[/{id}]` | Tag management |
| `POST` | `/api/v2/custom-tags/assign` | Apply tags |
| `GET` | `/api/v2/crm/phone-numbers` | List phone numbers |
| `DELETE` | `/api/v2/crm/phone-numbers/{id}` | Remove |
| `GET` | `/api/v2/account-campaign-mappings/{email}` | Find campaigns by account email |

---

## Smartlead ↔ Instantly parity table

If you're coming from Smartlead, here's how common operations map:

| Operation | Smartlead | Instantly |
|---|---|---|
| Auth | `?api_key=` query | `Authorization: Bearer` header |
| Create campaign | `POST /campaigns/create` | `POST /api/v2/campaigns` |
| Add leads | `POST /campaigns/{id}/leads` (100/batch) | `POST /api/v2/leads/bulk-create` (1000/batch) |
| Update sequence | `POST /campaigns/{id}/sequences` | `PATCH /api/v2/campaigns/{id}` (include `sequences` field) |
| Update settings | `POST /campaigns/{id}/settings` | `PATCH /api/v2/campaigns/{id}` |
| Pull analytics | `GET /analytics/day-wise-overall-stats` | `GET /api/v2/campaigns/analytics/daily` |
| List email accounts | `GET /email-accounts` | `GET /api/v2/accounts` |
| Create email account | `POST /email-accounts/save` | `POST /api/v2/accounts` |
| Master inbox / unibox | `POST /master-inbox/inbox-replies` | `GET /api/v2/emails` (20/min limit) |
| Register webhook | `POST /campaigns/{id}/webhooks` | `POST /api/v2/webhooks` |
| Start campaign | `POST /campaigns/{id}/status` body `{"status": "START"}` | `POST /api/v2/campaigns/{id}/activate` |

---

## Instantly-exclusive features worth knowing about

1. **Subsequences** — Branch your follow-ups by reply category. If someone says "wrong person", auto-enroll in a subsequence that asks for the right contact.
2. **Inbox placement testing** — Before launch, test where your emails land (primary/promotions/spam) across Gmail, Outlook, Yahoo. No Smartlead equivalent.
3. **SuperSearch enrichment** — Built-in lead database with AI-enhanced enrichment. Competes with Prospeo.
4. **DFY email accounts** — Order pre-warmed inboxes directly from Instantly. Alternative to Zapmail.
5. **Lead labels with AI prediction** — AI auto-classifies leads (interested, not interested, etc.) into custom labels.

---

## Gotchas

1. **Bearer token, not query param.** Common mistake coming from Smartlead.
2. **`/api/v2/emails` list endpoint is rate-limited to 20/min.** Use webhooks for real-time inbox monitoring instead of polling.
3. **`bulk-create` caps at 1,000 leads per request.** If you're uploading 2,000, split into 2 requests.
4. **OAuth is async.** Don't block — initialize, then poll `/oauth/{session_id}/status`.
5. **AI label prediction has a monthly quota (500/30d), not per-minute.** Plan accordingly.
6. **Background jobs need polling.** Enable warmup, disable warmup, and bulk ops all return a job ID. Poll `/api/v2/background-jobs/{id}` until done.
7. **Subsequence enrollment vs. move:** `subsequence/move` enrolls a lead into a subsequence; `subsequence/remove` unenrolls. Don't confuse with `leads/{id}/move` which moves across campaigns.
8. **Account pause is soft.** Paused accounts still exist and count against your plan; delete to actually remove.

---

## Minimal create-campaign example

```typescript
// 1. Create campaign
const campaignRes = await instantlyFetch("/api/v2/campaigns", {
  method: "POST",
  body: JSON.stringify({
    name: "My First Campaign",
    email_list: ["abc123", "def456"],  // account IDs from GET /api/v2/accounts
    sequences: [
      {
        steps: [
          { delay: 0, subject: "question for {{firstName}}", body: "..." },
          { delay: 3, subject: "", body: "..." },  // blank subject = thread
          { delay: 7, subject: "SaaS case study", body: "..." },
          { delay: 11, subject: "show and tell", body: "..." },
        ],
      },
    ],
  }),
});
const { id: campaignId } = await campaignRes.json();

// 2. Bulk add leads
const leadsRes = await instantlyFetch("/api/v2/leads/bulk-create", {
  method: "POST",
  body: JSON.stringify({
    campaign: campaignId,
    leads: leads.slice(0, 1000),  // up to 1000 per call
  }),
});

// 3. Activate
await instantlyFetch(`/api/v2/campaigns/${campaignId}/activate`, { method: "POST" });

// 4. Pull daily analytics later
const statsRes = await instantlyFetch(
  `/api/v2/campaigns/analytics/daily?campaign_id=${campaignId}&start_date=2026-04-01&end_date=2026-04-30`
);
```
