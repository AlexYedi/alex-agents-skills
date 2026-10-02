#!/usr/bin/env tsx
// Full paginated Prospeo search → CSV.
// Run: npx tsx scripts/prospeo-full-export.ts --title "VP Sales" --location "United States" --headcount-min 50 --headcount-max 200 --limit 2000
//
// Handles state-by-state splitting when total > 25K results.
// Output: leads.csv

import { env, required, parseArgs, writeCsv, sleep, retry, multiFlag, confirm } from "./_lib.ts";

const US_STATES = [
  "California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania",
  "Ohio", "Georgia", "North Carolina", "Michigan", "New Jersey", "Virginia",
  "Washington", "Arizona", "Massachusetts", "Tennessee", "Indiana", "Missouri",
  "Maryland", "Wisconsin", "Colorado", "Minnesota", "South Carolina", "Alabama",
  "Louisiana", "Kentucky", "Oregon", "Oklahoma", "Connecticut", "Utah",
];

async function searchPage(filters: any, page: number, apiKey: string): Promise<any> {
  const res = await retry(() => fetch("https://api.prospeo.io/search-person", {
    method: "POST",
    headers: { "X-KEY": apiKey, "Content-Type": "application/json" },
    body: JSON.stringify({ page, filters }),
  }));
  if (!res.ok) throw new Error(`Prospeo ${res.status}: ${await res.text()}`);
  return await res.json();
}

function mapResult(r: any): Record<string, string> {
  const p = r.person || {};
  const c = r.company || {};
  const loc = p.location || {};
  return {
    email: p.email || "",
    first_name: p.first_name || "",
    last_name: p.last_name || "",
    full_name: p.full_name || "",
    role_title: p.current_job_title || "",
    linkedin_url: p.linkedin_url || "",
    city: loc.city || "",
    state: loc.state || "",
    country: loc.country || "",
    company_name: c.name || "",
    company_domain: c.domain || "",
    company_industry: c.industry || "",
    company_headcount: (c.headcount || "").toString(),
    company_linkedin: c.linkedin_url || "",
  };
}

async function main() {
  const { flags } = parseArgs();
  const titles = multiFlag(flags, "title");
  const location = (flags.location as string) || "United States";
  const headcountMin = flags["headcount-min"] ? parseInt(flags["headcount-min"] as string) : undefined;
  const headcountMax = flags["headcount-max"] ? parseInt(flags["headcount-max"] as string) : undefined;
  const industries = multiFlag(flags, "industry");
  const techs = multiFlag(flags, "tech");
  const limit = parseInt((flags.limit as string) || "2000");
  const output = (flags.output as string) || "leads.csv";
  const verifiedOnly = flags["verified-only"] !== "false";

  if (titles.length === 0) {
    console.error("Usage: --title 'VP Sales' --title 'Head of Sales' [--location 'United States'] [--headcount-min 50] [--headcount-max 200] [--industry 'Software Development'] [--limit 2000] [--output leads.csv]");
    process.exit(1);
  }

  const apiKey = required("PROSPEO_API_KEY");

  const baseFilters: any = {
    person_location_search: { include: [location === "United States" ? "United States #US" : location] },
    person_job_title: { include: titles, match_only_exact_job_titles: false },
  };
  if (headcountMin !== undefined || headcountMax !== undefined) {
    baseFilters.company_headcount_custom = {};
    if (headcountMin !== undefined) baseFilters.company_headcount_custom.min = headcountMin;
    if (headcountMax !== undefined) baseFilters.company_headcount_custom.max = headcountMax;
  }
  if (industries.length > 0) baseFilters.company_industry = { include: industries };
  if (techs.length > 0) baseFilters.company_technology = { include: techs };
  if (verifiedOnly) baseFilters.person_contact_details = { email: ["VERIFIED"] };

  // First page to get total count
  console.log("Checking total result count...");
  const first = await searchPage(baseFilters, 1, apiKey);
  const totalCount = first?.pagination?.total_count || 0;
  const totalPages = first?.pagination?.total_page || 0;

  if (totalCount === 0) {
    console.error("Prospeo returned 0 results. Try removing filters.");
    process.exit(1);
  }

  const willFetch = Math.min(limit, totalCount);
  const estCredits = willFetch; // 1 credit per result

  console.log(`Found ${totalCount} total matches.`);
  console.log(`Will fetch up to ${willFetch} results (~${estCredits} credits).`);
  const ok = await confirm(`Confirm? (y/N)`);
  if (!ok) { console.log("Cancelled."); process.exit(0); }

  const all: any[] = [];

  if (totalCount >= 25000 && location === "United States") {
    // State-by-state fallback
    console.log(`Total > 25K, splitting by US state...`);
    for (const state of US_STATES) {
      if (all.length >= limit) break;
      const stateFilters = JSON.parse(JSON.stringify(baseFilters));
      stateFilters.person_location_search.include = [`${state}, United States #US`];
      const sFirst = await searchPage(stateFilters, 1, apiKey);
      const sTotal = sFirst?.pagination?.total_count || 0;
      const sPages = Math.min(sFirst?.pagination?.total_page || 0, Math.ceil((limit - all.length) / 25));
      for (let p = 1; p <= sPages; p++) {
        if (all.length >= limit) break;
        const data = p === 1 ? sFirst : await searchPage(stateFilters, p, apiKey);
        (data?.results || []).forEach((r: any) => all.push(mapResult(r)));
        await sleep(500);
      }
      console.log(`  ${state}: ${sTotal} available, collected ${all.length} total so far`);
    }
  } else {
    // Simple pagination
    for (let p = 1; p <= totalPages; p++) {
      if (all.length >= limit) break;
      const data = p === 1 ? first : await searchPage(baseFilters, p, apiKey);
      (data?.results || []).forEach((r: any) => all.push(mapResult(r)));
      process.stdout.write(`Page ${p}/${totalPages}, collected ${all.length}...\r`);
      await sleep(500);
    }
    console.log();
  }

  const trimmed = all.slice(0, limit);

  // Dedupe by email
  const seen = new Set<string>();
  const deduped = trimmed.filter(r => {
    if (!r.email || seen.has(r.email)) return false;
    seen.add(r.email);
    return true;
  });

  writeCsv(output, deduped);
  console.log(`\n✅ Saved ${deduped.length} leads to ${output}`);
}

main().catch(e => { console.error(e); process.exit(1); });
