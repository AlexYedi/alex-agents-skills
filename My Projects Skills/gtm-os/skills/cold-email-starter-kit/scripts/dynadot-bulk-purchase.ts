#!/usr/bin/env tsx
// Bulk-purchase a list of domains from Dynadot.
// Run: npx tsx scripts/dynadot-bulk-purchase.ts --list generated-domains.csv
//
// Outputs: purchased-domains.csv

import { env, required, parseArgs, readCsv, writeCsv, sleep, confirm, retry } from "./_lib.ts";

async function getWalletBalance(apiKey: string): Promise<number> {
  const r = await fetch(`https://api.dynadot.com/api3.json?key=${apiKey}&command=account_info`);
  const j: any = await r.json();
  const raw = j?.AccountInfoResponse?.AccountInfo?.AccountBalance || "$0.00";
  return parseFloat(raw.replace("$", ""));
}

async function registerDomain(domain: string, apiKey: string): Promise<{ success: boolean; error?: string }> {
  try {
    const url = `https://api.dynadot.com/api3.json?key=${apiKey}&command=register&domain=${encodeURIComponent(domain)}&duration=1`;
    const r = await retry(() => fetch(url).then(x => x.json() as Promise<any>));
    const code = r?.RegisterResponse?.ResponseCode;
    if (code === 0) return { success: true };
    return { success: false, error: r?.RegisterResponse?.Error || "unknown" };
  } catch (e: any) {
    return { success: false, error: e.message };
  }
}

async function main() {
  const { flags } = parseArgs();
  const listPath = (flags.list as string) || "generated-domains.csv";
  const skipConfirm = !!flags.yes;

  const apiKey = required("DYNADOT_API_KEY");

  const rows = readCsv(listPath);
  const available = rows.filter(r => r.available === "yes");
  if (available.length === 0) {
    console.error("No available domains in input CSV.");
    process.exit(1);
  }

  const totalCost = available.reduce((sum, r) => sum + parseFloat(r.price || "0"), 0);
  const balance = await getWalletBalance(apiKey);

  console.log(`Found ${available.length} available domains, total cost $${totalCost.toFixed(2)}.`);
  console.log(`Wallet balance: $${balance.toFixed(2)}`);
  console.log();

  if (balance < totalCost) {
    console.error(`Insufficient wallet balance. Need $${totalCost.toFixed(2)}, have $${balance.toFixed(2)}.`);
    console.error(`Top up at https://www.dynadot.com/account (add at least $${(totalCost - balance).toFixed(2)}).`);
    process.exit(1);
  }

  if (!skipConfirm) {
    const ok = await confirm(`About to spend $${totalCost.toFixed(2)} on ${available.length} domains. Confirm? (y/N)`);
    if (!ok) { console.log("Cancelled."); process.exit(0); }
  }

  const results: any[] = [];
  for (let i = 0; i < available.length; i++) {
    const d = available[i];
    process.stdout.write(`[${i + 1}/${available.length}] ${d.domain} ... `);
    const result = await registerDomain(d.domain, apiKey);
    if (result.success) {
      console.log("✅");
      results.push({ domain: d.domain, status: "purchased", price: d.price });
    } else {
      console.log(`❌ ${result.error}`);
      results.push({ domain: d.domain, status: "failed", error: result.error });
    }
    await sleep(500); // 0.5s pause between registrations
  }

  writeCsv("purchased-domains.csv", results);

  const purchased = results.filter(r => r.status === "purchased");
  const failed = results.filter(r => r.status === "failed");

  console.log();
  console.log(`✅ Purchased: ${purchased.length}`);
  console.log(`❌ Failed: ${failed.length}`);
  console.log();
  console.log("Saved to purchased-domains.csv");
  console.log();
  console.log("Next step:");
  console.log("  npx tsx scripts/zapmail-full-setup.ts --domains purchased-domains.csv --platform smartlead");
}

main().catch(e => { console.error(e); process.exit(1); });
