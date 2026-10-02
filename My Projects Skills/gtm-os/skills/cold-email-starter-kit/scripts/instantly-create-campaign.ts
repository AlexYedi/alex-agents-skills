#!/usr/bin/env tsx
// End-to-end Instantly campaign creation: create → add leads → activate.
// Run: npx tsx scripts/instantly-create-campaign.ts --name "My First" --sequence sequence.json --leads leads.csv

import { env, required, parseArgs, readCsv, retry } from "./_lib.ts";
import fs from "node:fs";

const API = "https://api.instantly.ai";

async function instantlyFetch(path: string, init: RequestInit = {}, key: string): Promise<any> {
  const res = await retry(() => fetch(`${API}${path}`, {
    ...init,
    headers: {
      "Authorization": `Bearer ${key}`,
      "Content-Type": "application/json",
      ...(init.headers as any),
    },
  }));
  if (!res.ok) throw new Error(`Instantly ${path} → ${res.status}: ${await res.text()}`);
  return await res.json();
}

async function main() {
  const { flags } = parseArgs();
  const name = (flags.name as string) || `Campaign ${new Date().toISOString().slice(0, 10)}`;
  const sequenceFile = (flags.sequence as string) || "sequence.json";
  const leadsFile = (flags.leads as string) || "leads.csv";
  const autoActivate = !!flags["auto-activate"];

  const key = required("INSTANTLY_API_KEY");

  // 1. Fetch warmed accounts
  console.log("Fetching email accounts...");
  const accountsResp = await instantlyFetch("/api/v2/accounts?limit=200", {}, key);
  const accounts = Array.isArray(accountsResp?.data) ? accountsResp.data : (accountsResp?.data || []);
  const accountEmails = accounts.map((a: any) => a.email).filter(Boolean);
  console.log(`Found ${accountEmails.length} accounts.`);

  // 2. Load sequence
  let sequences: any[] = [];
  if (fs.existsSync(sequenceFile)) {
    sequences = JSON.parse(fs.readFileSync(sequenceFile, "utf8"));
    if (!Array.isArray(sequences)) sequences = [sequences];
  }

  // 3. Create campaign
  console.log(`Creating campaign "${name}"...`);
  const payload: any = {
    name,
    email_list: accountEmails,
    sequences,
    daily_limit: 30,
    campaign_schedule: {
      schedules: [{
        name: "Business hours",
        timing: { from: "09:00", to: "17:00" },
        days: { "1": true, "2": true, "3": true, "4": true, "5": true, "0": false, "6": false },
        timezone: "America/New_York",
      }],
    },
  };
  const created = await instantlyFetch("/api/v2/campaigns", {
    method: "POST",
    body: JSON.stringify(payload),
  }, key);
  const campaignId = created?.id;
  if (!campaignId) throw new Error(`Campaign create failed: ${JSON.stringify(created).slice(0, 300)}`);
  console.log(`✅ Campaign created: ${campaignId}`);

  // 4. Add leads in batches of 1000
  if (fs.existsSync(leadsFile)) {
    const leads = readCsv(leadsFile);
    console.log(`Adding ${leads.length} leads in batches of 1000...`);
    let added = 0;
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
        await instantlyFetch("/api/v2/leads/bulk-create", {
          method: "POST",
          body: JSON.stringify({ campaign: campaignId, leads: batch }),
        }, key);
        added += batch.length;
        process.stdout.write(`  ${added}/${leads.length}\r`);
      } catch (e: any) {
        console.warn(`\n  batch ${i}-${i + 1000} failed: ${e.message}`);
      }
    }
    console.log(`\n✅ Added ${added} leads.`);
  }

  // 5. Activate (optional)
  if (autoActivate) {
    console.log("Activating campaign...");
    await instantlyFetch(`/api/v2/campaigns/${campaignId}/activate`, { method: "POST" }, key);
    console.log("✅ Campaign ACTIVE.");
  }

  console.log();
  console.log(`✅ Campaign ready: https://app.instantly.ai/app/campaign/${campaignId}`);
  if (!autoActivate) console.log("   Review in the UI, then activate manually (or re-run with --auto-activate).");
}

main().catch(e => { console.error(e); process.exit(1); });
