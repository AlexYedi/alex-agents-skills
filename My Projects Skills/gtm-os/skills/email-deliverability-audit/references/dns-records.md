# DNS Records for Cold Email Deliverability

Three records every sending domain needs: **SPF, DKIM, DMARC**. Miss any one and your deliverability suffers.

## SPF (Sender Policy Framework)

Declares which servers are allowed to send mail on behalf of your domain.

**Record type:** TXT
**Host:** `@` (the bare domain, e.g. `example.com`)
**Value format:**
```
v=spf1 include:<provider> ~all
```

### Examples

| Provider | SPF value |
|---|---|
| Zapmail | `v=spf1 include:_spf.zapmail.com ~all` |
| Google Workspace | `v=spf1 include:_spf.google.com ~all` |
| Microsoft 365 | `v=spf1 include:spf.protection.outlook.com ~all` |
| SendGrid | `v=spf1 include:sendgrid.net ~all` |

### Strictness modifiers

- `~all` (soft fail) — emails that fail get marked suspicious but usually still delivered. **Default for new domains.**
- `-all` (hard fail) — emails that fail get rejected. **Only use after weeks of clean mail.**
- `+all` — allows any sender. **NEVER use. Makes SPF useless.**
- `?all` — neutral. Same as no SPF.

### Verify
```bash
dig TXT example.com +short | grep spf1
```

## DKIM (DomainKeys Identified Mail)

Cryptographic signature that proves the email wasn't modified in transit.

**Record type:** TXT
**Host:** `<selector>._domainkey` — the selector varies by provider, see below. Never assume `default`.
**Value:** Long public key provided by your sending provider. Looks like:
```
v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC...
```

### ⛔ There is no single DKIM selector — check all of them

Checking only `default._domainkey` is the most damaging DNS mistake in a cold email audit. It
marks an entire healthy fleet "missing DKIM", routes genuinely burned domains to "fix your auth",
and buys you a week of republishing records that already exist while the burned domain keeps
sending.

DKIM is present if **any** of these resolves:

```bash
dig TXT   google._domainkey.example.com    +short   # Google / Gmail-backed providers — the common one
dig CNAME selector1._domainkey.example.com +short   # Microsoft 365 — a CNAME, not a TXT
dig CNAME selector2._domainkey.example.com +short   # Microsoft 365, second key
dig TXT   default._domainkey.example.com   +short   # generic fallback, frequently EMPTY
```

⚠️ **For the Microsoft selectors, accept the CNAME itself as proof.** A `dig TXT
selector1._domainkey.example.com` returns nothing even when DKIM is configured correctly — the
record is a CNAME pointing at `selector1._domainkey.outlook.com`.

Verified live on two real sending domains: a Gmail-backed domain published at `google._domainkey`
(TXT), a Microsoft-backed one at `selector1._domainkey` (CNAME), and `default._domainkey` was
**empty on both**.

`scripts/check-domain-auth.ts` tries all four and reports which one resolved in the
`dkim_selector` column. Pass `--dkim-selector=XYZ` to add a provider-specific one.

### Why it's often missing
- Domain wasn't connected through the sending provider's onboarding flow
- Selector published on old provider, domain migrated without re-publishing
- Propagation not yet complete (wait up to 48h after setup)

## DMARC (Domain-based Message Authentication, Reporting and Conformance)

Tells receiving servers what to do with emails that fail SPF/DKIM, and where to send reports.

**Record type:** TXT
**Host:** `_dmarc`
**Minimum value:**
```
v=DMARC1; p=none; rua=mailto:dmarc@example.com
```

### Policy levels

- `p=none` — monitor only. Failing emails still delivered. Reports sent to `rua=` address. **Start here.**
- `p=quarantine` — failing emails go to spam. **Upgrade to this after 1-2 weeks of clean `rua=` reports.**
- `p=reject` — failing emails bounced. **Strictest. Use only after 30+ days confirmed clean.**

### Additional tags

```
v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com; ruf=mailto:forensic@example.com; pct=100; adkim=r; aspf=r
```

- `rua` — aggregate reports (daily summary). Set this.
- `ruf` — forensic reports (per-failure detail). Optional, gets noisy.
- `pct` — percentage of failing mail to apply policy to. Start at 100.
- `adkim=r|s` — DKIM alignment mode. `r` = relaxed (subdomain OK), `s` = strict.
- `aspf=r|s` — SPF alignment mode. Same as above.

### Verify
```bash
dig TXT _dmarc.example.com +short
```

## Checklist for a new domain

1. **Day 0 — registration:** point nameservers to your sending provider (e.g., Zapmail)
2. **Day 0-1 — DNS propagation:** wait 20 min - 48h for records to appear
3. **Day 1 — verify all three:**
   ```bash
   dig TXT example.com +short
   dig TXT   google._domainkey.example.com    +short   # or...
   dig CNAME selector1._domainkey.example.com +short   # ...or selector2, or default
   dig TXT _dmarc.example.com +short
   ```
4. **Day 1-14 — warmup:** DMARC `p=none`, SPF `~all`. Warm inboxes slowly.
5. **Day 14 — tighten DMARC:** switch to `p=quarantine` if aggregate reports are clean.
6. **Day 30+ — optional reject:** switch to `p=reject` if you're confident no legitimate mail will fail.

## Common failure patterns

| Symptom | Likely cause |
|---|---|
| SPF present but marked soft-fail in DMARC reports | SPF `include:` list missing your provider |
| DKIM signature in email but DMARC still fails | From-domain doesn't match DKIM-signing domain (alignment issue) |
| DMARC reports show failures from your own sending | DKIM selector moved or expired |
| Emails landing in spam despite all 3 passing | Domain reputation issue — content/behavior, not auth |
| Brand-new domain, all auth fails | DNS propagation still in progress, wait 48h |

## How Zapmail handles this

Zapmail's onboarding flow typically publishes SPF, DKIM, and DMARC (`p=none`) automatically when you connect a domain to them. If any are missing:
- Re-run Zapmail's "verify domain" wizard
- Check the nameservers actually point to Zapmail
- Wait longer for DNS propagation

If you need more control, switch to "custom DNS" mode in Zapmail and publish records manually at your registrar.
