#!/usr/bin/env tsx
// Add leads to an existing Instantly campaign. Batches of 1000.
// Run: npx tsx scripts/instantly-add-leads.ts --campaign-id abc123 --leads leads.csv

import { env, required, parseArgs, readCsv, writeCsv, retry } from "./_lib.ts";

const API = "https://api.instantly.ai";

async function main() {
  const { flags } = parseArgs();
  const campaignId = flags["campaign-id"] as string;
  const leadsFile = (flags.leads as string) || "leads.csv";
  if (!campaignId) { console.error("Usage: --campaign-id <id> --leads leads.csv"); process.exit(1); }

  const key = required("INSTANTLY_API_KEY");
  const leads = readCsv(leadsFile);
  console.log(`Adding ${leads.length} leads to Instantly campaign ${campaignId}...`);

  let added = 0, failed = 0;
  const failedRows: any[] = [];

  for (let i = 0; i < leads.length; i += 1000) {
    const batch = leads.slice(i, i + 1000).map(l => ({
      email: l.email,
      first_name: l.first_name,
      last_name: l.last_name,
      company_name: l.company_name,
      custom_variables: {
        company_domain: l.company_domain,
        role_title: l.role_title,
        ai_customer_type: l.ai_customer_type || "",
        ai_company_mission: l.ai_company_mission || "",
        recent_news_title: l.recent_news_title || "",
        company_phone: l.company_phone || "",
      },
    }));
    try {
      const res = await retry(() => fetch(`${API}/api/v2/leads/bulk-create`, {
        method: "POST",
        headers: { "Authorization": `Bearer ${key}`, "Content-Type": "application/json" },
        body: JSON.stringify({ campaign: campaignId, leads: batch }),
      }));
      if (res.ok) {
        added += batch.length;
      } else {
        failed += batch.length;
        failedRows.push(...leads.slice(i, i + 1000));
      }
    } catch (e: any) {
      failed += batch.length;
      failedRows.push(...leads.slice(i, i + 1000));
    }
    process.stdout.write(`  processed ${Math.min(i + 1000, leads.length)}/${leads.length}\r`);
  }
  console.log();

  if (failedRows.length > 0) writeCsv("failed-leads.csv", failedRows);

  console.log(`\n✅ Added: ${added}`);
  console.log(`❌ Failed: ${failed}`);
  if (failed > 0) console.log("Failed rows saved to failed-leads.csv for retry.");
}

main().catch(e => { console.error(e); process.exit(1); });
