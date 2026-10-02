#!/usr/bin/env tsx
// End-to-end Smartlead campaign creation: create → save sequence → attach inboxes → add leads.
// Run: npx tsx scripts/smartlead-create-campaign.ts --name "My First" --sequence sequence.json --leads leads.csv

import { env, required, parseArgs, readCsv, retry } from "./_lib.ts";
import fs from "node:fs";

const API = "https://server.smartlead.ai/api/v1";

async function smartleadPost(path: string, body: any, key: string): Promise<any> {
  const res = await retry(() => fetch(`${API}${path}?api_key=${key}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  }));
  if (!res.ok) throw new Error(`Smartlead ${path} → ${res.status}: ${await res.text()}`);
  return await res.json();
}

async function smartleadGet(path: string, key: string): Promise<any> {
  const res = await retry(() => fetch(`${API}${path}${path.includes("?") ? "&" : "?"}api_key=${key}`));
  if (!res.ok) throw new Error(`Smartlead ${path} → ${res.status}`);
  return await res.json();
}

async function main() {
  const { flags } = parseArgs();
  const name = (flags.name as string) || `Campaign ${new Date().toISOString().slice(0, 10)}`;
  const sequenceFile = (flags.sequence as string) || "sequence.json";
  const leadsFile = (flags.leads as string) || "leads.csv";

  const key = required("SMARTLEAD_API_KEY");

  // 1. Create campaign
  console.log(`Creating campaign "${name}"...`);
  const created = await smartleadPost("/campaigns/create", { name }, key);
  const campaignId = created?.id || created?.campaign_id;
  if (!campaignId) throw new Error(`Campaign create failed: ${JSON.stringify(created)}`);
  console.log(`✅ Campaign created: ${campaignId}`);

  // 2. Save sequence
  if (fs.existsSync(sequenceFile)) {
    console.log(`Saving sequence from ${sequenceFile}...`);
    const sequences = JSON.parse(fs.readFileSync(sequenceFile, "utf8"));
    await smartleadPost(`/campaigns/${campaignId}/sequences`, { sequences }, key);
    console.log(`✅ Sequence saved (${Array.isArray(sequences) ? sequences.length : 0} steps)`);
  } else {
    console.warn(`⚠️  No sequence file at ${sequenceFile}, skipping sequence upload.`);
  }

  // 3. Attach all warmed email accounts
  console.log("Fetching email accounts...");
  const accounts = await smartleadGet("/email-accounts?limit=200", key);
  const list = Array.isArray(accounts) ? accounts : (accounts?.data || []);
  const ids = list.map((a: any) => a.id).filter(Boolean);
  if (ids.length > 0) {
    console.log(`Attaching ${ids.length} email accounts...`);
    await smartleadPost(`/campaigns/${campaignId}/email-accounts`, { email_account_ids: ids }, key);
    console.log(`✅ Accounts attached.`);
  } else {
    console.warn("⚠️  No email accounts found — campaign cannot send until accounts are attached.");
  }

  // 4. Add leads in batches of 100
  if (fs.existsSync(leadsFile)) {
    const leads = readCsv(leadsFile);
    console.log(`Adding ${leads.length} leads in batches of 100...`);
    let added = 0;
    for (let i = 0; i < leads.length; i += 100) {
      const batch = leads.slice(i, i + 100).map(l => ({
        email: l.email,
        first_name: l.first_name,
        last_name: l.last_name,
        company_name: l.company_name,
        custom_fields: {
          company_domain: l.company_domain,
          role_title: l.role_title,
          ai_customer_type: l.ai_customer_type,
          ai_company_mission: l.ai_company_mission,
          recent_news_title: l.recent_news_title,
          company_phone: l.company_phone,
        },
      }));
      try {
        await smartleadPost(`/campaigns/${campaignId}/leads`, { lead_list: batch }, key);
        added += batch.length;
        process.stdout.write(`  ${added}/${leads.length}\r`);
      } catch (e: any) {
        console.warn(`\n  batch ${i}-${i + 100} failed: ${e.message}`);
      }
    }
    console.log(`\n✅ Added ${added} leads.`);
  }

  // 5. Set default schedule (M-F 9-5, 30 emails/day/inbox)
  console.log("Setting default schedule...");
  try {
    await smartleadPost(`/campaigns/${campaignId}/schedule`, {
      timezone: "America/New_York",
      days_of_the_week: [1, 2, 3, 4, 5],
      start_hour: "09:00",
      end_hour: "17:00",
      min_time_btw_emails: 10,
      max_new_leads_per_day: 30,
    }, key);
    console.log("✅ Schedule set.");
  } catch (e: any) {
    console.warn(`⚠️  Schedule failed: ${e.message}`);
  }

  console.log();
  console.log("✅ Campaign ready in DRAFT status.");
  console.log(`   https://app.smartlead.ai/app/email-campaign/${campaignId}`);
  console.log();
  console.log("Next:");
  console.log(`  1. Visit the URL above, review the sequence + leads`);
  console.log(`  2. Run the launch checklist from references/12-launch-checklist.md`);
  console.log(`  3. Hit Start in the Smartlead UI`);
}

main().catch(e => { console.error(e); process.exit(1); });
