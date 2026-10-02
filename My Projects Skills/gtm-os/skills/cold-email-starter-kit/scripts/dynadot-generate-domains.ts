#!/usr/bin/env tsx
// Generate candidate domain names and check Dynadot availability.
// Run: npx tsx scripts/dynadot-generate-domains.ts --brand acme --count 20 --tld info
//
// Outputs: generated-domains.csv in the skill root with columns: domain, available, price

import { env, required, parseArgs, writeCsv, sleep, retry } from "./_lib.ts";

const PREFIXES = [
  "go", "get", "try", "my", "the", "hey", "use", "run", "hello",
  "meet", "find", "join", "with", "one", "via", "top",
];
const SUFFIXES = [
  "hq", "hub", "app", "pro", "lab", "co", "now", "go", "io",
  "team", "desk", "lab", "base", "core", "edge", "flow", "point",
];

interface DomainCandidate {
  domain: string;
  available: string;
  price: string;
}

async function checkBatch(domains: string[], apiKey: string): Promise<DomainCandidate[]> {
  const url = new URL("https://api.dynadot.com/api3.json");
  url.searchParams.set("key", apiKey);
  url.searchParams.set("command", "search");
  url.searchParams.set("show_price", "1");
  url.searchParams.set("currency", "USD");
  domains.forEach((d, i) => url.searchParams.set(`domain${i}`, d));

  const res = await retry(() => fetch(url.toString()).then(r => r.json() as Promise<any>));
  const results = res?.SearchResponse?.SearchResults || [];
  return results.map((r: any): DomainCandidate => ({
    domain: r.DomainName,
    available: r.Available || "no",
    price: r.Price || "",
  }));
}

async function main() {
  const { flags } = parseArgs();
  const brand = (flags.brand as string) || "";
  const count = parseInt((flags.count as string) || "20");
  const tld = (flags.tld as string) || "info";
  const checkOnly = !!flags["check-only"];
  const maxPrice = parseFloat((flags["max-price"] as string) || "3.5");

  if (!brand) {
    console.error("Usage: --brand <keyword> [--count 20] [--tld info] [--max-price 3.5] [--check-only]");
    process.exit(1);
  }

  const apiKey = required("DYNADOT_API_KEY");

  // Build candidate list
  const candidates = new Set<string>();
  for (const p of PREFIXES) candidates.add(`${p}${brand}.${tld}`);
  for (const s of SUFFIXES) candidates.add(`${brand}${s}.${tld}`);
  const brandSuffix = Array.from(candidates).filter(d => d.length <= 30);

  console.log(`Generated ${brandSuffix.length} candidate domains for brand "${brand}".`);
  console.log(`Checking availability on Dynadot (batches of 100)...\n`);

  const allResults: DomainCandidate[] = [];
  for (let i = 0; i < brandSuffix.length; i += 100) {
    const batch = brandSuffix.slice(i, i + 100);
    try {
      const results = await checkBatch(batch, apiKey);
      allResults.push(...results);
      process.stdout.write(`Checked ${Math.min(i + 100, brandSuffix.length)}/${brandSuffix.length}\r`);
    } catch (e: any) {
      console.error(`\nBatch failed: ${e.message}`);
    }
    await sleep(1000);
  }
  console.log();

  // Filter available + in price range
  const available = allResults
    .filter(r => r.available === "yes" && parseFloat(r.price) <= maxPrice)
    .sort((a, b) => a.domain.length - b.domain.length) // shorter first
    .slice(0, count);

  if (available.length === 0) {
    console.log(`No available domains found under $${maxPrice} for .${tld}.`);
    console.log("Try a different brand keyword or increase --max-price.");
    process.exit(1);
  }

  console.log(`Found ${available.length} available domains under $${maxPrice}:`);
  console.log();
  available.forEach(r => console.log(`  ${r.domain.padEnd(30)} $${r.price}`));
  console.log();

  const totalCost = available.reduce((sum, r) => sum + parseFloat(r.price), 0);
  console.log(`Total cost if all purchased: $${totalCost.toFixed(2)}`);

  const outPath = "generated-domains.csv";
  writeCsv(outPath, available);
  console.log(`\nSaved to ${outPath}`);

  if (checkOnly) {
    console.log("(--check-only mode, no purchase)");
    return;
  }

  console.log("\nNext step: review the list, then run:");
  console.log("  npx tsx scripts/dynadot-bulk-purchase.ts --list generated-domains.csv");
}

main().catch(e => { console.error(e); process.exit(1); });
