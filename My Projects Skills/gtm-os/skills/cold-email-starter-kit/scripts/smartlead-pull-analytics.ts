#!/usr/bin/env tsx
// Pull Smartlead analytics to CSV.
// Run: npx tsx scripts/smartlead-pull-analytics.ts --campaign-id 12345

import { env, required, parseArgs, writeCsv, retry } from "./_lib.ts";

const API = "https://server.smartlead.ai/api/v1";

async function main() {
  const { flags } = parseArgs();
  const campaignId = flags["campaign-id"] as string;
  const since = (flags.since as string) || new Date(Date.now() - 30 * 86400000).toISOString().slice(0, 10);
  const until = (flags.until as string) || new Date().toISOString().slice(0, 10);
  const output = (flags.output as string) || "analytics.csv";

  if (!campaignId) { console.error("Usage: --campaign-id <id> [--since YYYY-MM-DD] [--until YYYY-MM-DD]"); process.exit(1); }

  const key = required("SMARTLEAD_API_KEY");

  console.log(`Pulling Smartlead analytics for campaign ${campaignId}, ${since} → ${until}...`);

  // Overall stats
  const overall = await retry(() => fetch(`${API}/campaigns/${campaignId}/analytics?api_key=${key}`).then(r => r.json() as Promise<any>));

  // By-date stats
  const byDate = await retry(() => fetch(`${API}/campaigns/${campaignId}/analytics-by-date?api_key=${key}&start_date=${since}&end_date=${until}`).then(r => r.json() as Promise<any>));

  // Print summary
  console.log("\nOverall stats:");
  console.log(`  Sent:      ${overall?.sent_count || 0}`);
  console.log(`  Opened:    ${overall?.open_count || 0}`);
  console.log(`  Clicked:   ${overall?.click_count || 0}`);
  console.log(`  Replied:   ${overall?.reply_count || 0}`);
  console.log(`  Bounced:   ${overall?.bounce_count || 0}`);
  console.log(`  Unsub:     ${overall?.unsubscribed_count || 0}`);

  const sent = overall?.sent_count || 0;
  if (sent > 0) {
    const openRate = ((overall?.open_count || 0) / sent * 100).toFixed(1);
    const replyRate = ((overall?.reply_count || 0) / sent * 100).toFixed(1);
    const bounceRate = ((overall?.bounce_count || 0) / sent * 100).toFixed(1);
    console.log(`  Open rate: ${openRate}%`);
    console.log(`  Reply rate: ${replyRate}%`);
    console.log(`  Bounce rate: ${bounceRate}%`);
  }

  // Save CSV
  const rows = Array.isArray(byDate) ? byDate : (byDate?.data || []);
  if (rows.length > 0) {
    writeCsv(output, rows);
    console.log(`\nSaved daily breakdown to ${output}`);
  }
}

main().catch(e => { console.error(e); process.exit(1); });
