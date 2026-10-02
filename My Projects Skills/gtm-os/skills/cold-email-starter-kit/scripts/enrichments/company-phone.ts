#!/usr/bin/env tsx
// Enrich leads with company phone via Blitz API.
// Run: npx tsx scripts/enrichments/company-phone.ts --input leads.csv --output leads-with-phone.csv

import { env, required, parseArgs, readCsv, writeCsv, createQueue, retry } from "../_lib.ts";

async function main() {
  const { flags } = parseArgs();
  const input = (flags.input as string) || "leads.csv";
  const output = (flags.output as string) || "leads-with-phone.csv";

  const blitzKey = required("BLITZ_API_KEY");
  const blitzBase = env.BLITZ_BASE_URL || "https://api.blitz.us";

  const leads = readCsv(input);
  console.log(`Enriching ${leads.length} leads with company phones via Blitz...`);

  const queue = createQueue(10);
  const errors: any[] = [];
  let enriched = 0;

  const enriched_rows = await Promise.all(leads.map(lead => queue.add(async () => {
    if (!lead.company_domain) return { ...lead, company_phone: "" };
    try {
      const res = await retry(() => fetch(`${blitzBase}/api/enrichment/company`, {
        method: "POST",
        headers: { "Authorization": `Bearer ${blitzKey}`, "Content-Type": "application/json" },
        body: JSON.stringify({ domain: lead.company_domain }),
      }));
      if (!res.ok) {
        errors.push({ email: lead.email, domain: lead.company_domain, error: `HTTP ${res.status}` });
        return { ...lead, company_phone: "" };
      }
      const j: any = await res.json();
      const phone = j?.company?.phone || "";
      if (phone) enriched++;
      return { ...lead, company_phone: phone };
    } catch (e: any) {
      errors.push({ email: lead.email, domain: lead.company_domain, error: e.message });
      return { ...lead, company_phone: "" };
    }
  })));

  writeCsv(output, enriched_rows);
  if (errors.length > 0) writeCsv("company-phone-errors.csv", errors);

  console.log(`\n✅ Enriched ${enriched}/${leads.length} with phones (${errors.length} errors)`);
  console.log(`Saved to ${output}`);
}

main().catch(e => { console.error(e); process.exit(1); });
