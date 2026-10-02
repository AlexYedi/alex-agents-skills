# 11 — Legal Compliance

A short overview of cold email law. Skim it once; no need to memorize.

**Not legal advice.** This is a summary based on publicly available guidance. For your specific situation, consult a lawyer — especially if you're in a regulated space (healthcare, finance, EU consumers, anything beyond small-scale B2B).

---

## CAN-SPAM (USA)

The US law governing commercial email. Most cold email is straightforward to comply with.

### What CAN-SPAM asks for

A compliant cold email generally has:

1. **Truthful sender identity** — the "From" name and email match a real person/organization.
2. **Non-deceptive subject line** — don't write "Re: your inquiry" if they never inquired.
3. **Identification as an ad** — can be implicit (the email itself makes clear it's solicitation), not explicit.
4. **Physical mailing address** — a real business address, or a PO box, in the footer.
5. **Unsubscribe mechanism** — a clear way to opt out, honored within 10 business days.
6. **Opt-out honored** — once someone unsubscribes, don't email them again. Apply it across all your campaigns.

### What CAN-SPAM does NOT require

- Prior consent (unlike GDPR)
- Double opt-in
- B2B limitations (you can legally cold email businesses without consent)

### How to comply (in your email)

Every email should have a footer like:
```
— Jane Doe
Acme Inc, 123 Main St, Anytown, CA 94105

If you'd rather not hear from me, just reply "unsubscribe".
```

Or a hyperlinked unsubscribe:
```
Don't want these? [Unsubscribe]
```

Both Smartlead and Instantly can inject this automatically. Use it.

---

## GDPR (EU)

The EU data protection regulation. Stricter than CAN-SPAM, especially around consumer addresses.

### The short version

**B2B cold email to EU recipients is generally legal** under GDPR's "legitimate interest" clause, provided:

1. **The email is relevant to their job role.** You can email a VP of Sales about sales tools. You cannot email them about car insurance.
2. **They can easily opt out.** Unsubscribe link in every email, honored immediately.
3. **You have a clear lawful basis** documented internally ("legitimate interest for B2B outreach about [your product category]").
4. **You respect their rights** — if they ask for data deletion, you do it.
5. **Your privacy notice is accessible** — link in email footer to your privacy policy.

### What GDPR prohibits

- **Emailing EU consumers** (personal addresses, gmail.com, hotmail.com, etc. when the person is in the EU and not in a business role). Hard no.
- **Buying lists** without documented lawful basis.
- **Hiding your identity** or using fake names.
- **Ignoring "right to be forgotten"** requests. When an EU recipient asks you to delete their data, you have 30 days to comply.

### DPO contact

If you send to EU recipients at scale, include a DPO (Data Protection Officer) contact email in your privacy policy. For small operations, your regular "legal@yourcompany.com" works.

---

## CASL (Canada)

Canadian Anti-Spam Legislation. Stricter than CAN-SPAM around consent.

### Key difference from CAN-SPAM

CASL requires **consent** (express or implied). For cold email, you rely on **implied consent** from "business relationship" rules:

- **Implied consent (24 months)**: They're a published business contact (their email is on their company website, LinkedIn, etc.) AND your message is relevant to their business role.
- **Express consent**: Explicit opt-in — not applicable for cold email.

### How to comply (Canadian recipients)

1. Send only to published business email addresses (from public websites, not scraped personal addresses)
2. Your email MUST be relevant to their business role
3. Include unsubscribe link
4. Physical address in footer
5. Sender identity clear and truthful

### If in doubt

If you're unsure whether a Canadian recipient qualifies for implied consent, skip them.

---

## Other regions

- **UK (PECR + UK GDPR)** — same as EU GDPR for most practical purposes. B2B cold email is legal with legitimate interest; consumers are off-limits.
- **Australia (Spam Act 2003)** — requires "consent" which can be inferred from a business relationship or published contact. Similar to CASL.
- **Brazil (LGPD)**, **Singapore (PDPA)**, **India (IT Rules)** — various levels of strictness. If you're sending at scale in any of these, research the specific law.

---

## Unsubscribe requirements (summary table)

| Region | Unsubscribe required? | Honor deadline |
|---|---|---|
| USA (CAN-SPAM) | Yes | 10 business days |
| EU (GDPR) | Yes | Immediately |
| Canada (CASL) | Yes | 10 business days |
| UK (PECR) | Yes | Immediately |
| Australia (Spam Act) | Yes | 5 business days |

**Practical rule:** honor all unsubscribes within 24 hours. That's safer than any legal minimum and good practice anyway.

---

## Physical address requirement

CAN-SPAM, CASL, and some EU rules require a physical mailing address in every email.

**Options:**
- Your actual business address (if you're comfortable publishing it)
- **A PO box** ($10-30/month from USPS)
- **A virtual office / mailbox** — iPostal1 (~$10/mo), Earth Class Mail (~$20/mo), Anytime Mailbox (~$10/mo)

It's a small thing that quietly satisfies CAN-SPAM, CASL, and a few EU rules in one line.

---

## Things to avoid

1. **Skip purchased lists from random sellers.** Prospeo/Apollo/etc. are clean. Cheap "$99 lead packs" are scraped data that will hurt your domain reputation.
2. **Skip consumer addresses in the EU.** B2B is fine; personal addresses aren't.
3. **Skip student / .edu addresses for minors.** Filter universities that still use student emails.
4. **Skip government addresses (.gov, .mil).** Some agencies escalate to IT.
5. **Don't scrape Facebook, Instagram, personal Twitter, or TikTok for emails** — terms of service + privacy laws.
6. **Don't email healthcare providers about patient data** — HIPAA is its own layer.
7. **Don't auto-bcc your boss** — if they show up in "To" unexpectedly, it looks unprofessional.
8. **Don't spoof From addresses.** Send only from domains you own.
9. **Honor unsubscribes permanently** — once removed, stay removed across every campaign.
10. **Include a physical address in the footer.** Easy to set once and forget.

---

## Your pre-launch legal checklist

Before your first campaign ships, confirm:

- [ ] Sender name is real
- [ ] From email matches sending domain
- [ ] Physical address is in footer (real or PO box)
- [ ] Unsubscribe link/reply instruction is in every email
- [ ] Privacy policy exists and is linked (if sending to EU/UK)
- [ ] Your list is from a legitimate source (Prospeo, Apollo, Blitz, Clay, LinkedIn scraper you own)
- [ ] You're not emailing consumer addresses in GDPR regions
- [ ] You're not emailing .gov / .mil / .edu
- [ ] Your block list is wired up and honors unsubscribes across campaigns
- [ ] You have a process to honor "right to be forgotten" requests within 30 days

If all checked: ship.

---

## If you get a complaint

1. **Stay calm.** Most complaints are non-escalating.
2. **Respond within 24 hours** acknowledging receipt.
3. **Remove them from all campaigns immediately.**
4. **Document** the complaint and your response.
5. **If they threaten legal action:** stop responding, consult a lawyer.

Most "unsubscribe or I'll sue" emails are noise. But some are real. Take every one seriously.

---

## When to consult a lawyer

- You're sending > 100K emails/month
- You have EU / UK recipients at scale
- You're in healthcare, finance, insurance, or legal
- You received a cease & desist
- You're considering a purchased list
- You're unsure about anything above

A short compliance review before your first big campaign is usually a good investment if any of these apply.
