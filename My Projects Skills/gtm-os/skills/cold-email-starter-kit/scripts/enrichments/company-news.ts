#!/usr/bin/env tsx
// Enrich leads with recent company news via OpenWebNinja (RapidAPI).
// Adds columns: recent_news_title, recent_news_url, recent_news_date, recent_news_snippet
// Run: npx tsx scripts/enrichments/company-news.ts --input leads.csv --output leads-news.csv --days 90

import { env, required, parseArgs, readCsv, writeCsv, createQueue, retry } from "../_lib.ts";

const BLOCKLIST_KEYWORDS = ["obituary", "wikipedia", "jobs.", "careers.", "lawsuit", "indictment"];

function isBlocked(item: any): boolean {
  const text = `${item?.title || ""} ${item?.snippet || ""} ${item?.url || ""}`.toLowerCase();
  return BLOCKLIST_KEYWORDS.some(k => text.includes(k));
}

async function main() {
  const { flags } = parseArgs();
  const input = (flags.input as string) || "leads.csv";
  const output = (flags.output as string) || "leads-news.csv";
  const days = parseInt((flags.days as string) || "90");

  const key = required("RAPIDAPI_KEY");

  const leads = readCsv(input);
  console.log(`Enriching ${leads.length} leads with recent news (last ${days} days)...`);

  const queue = createQueue(5);
  const errors: any[] = [];
  let enriched = 0;

  // Dedupe by company_name to avoid redundant API calls
  const byCompany = new Map<string, { title: string; url: string; date: string; snippet: string } | null>();

  const enriched_rows = await Promise.all(leads.map(lead => queue.add(async () => {
    if (!lead.company_name) return { ...lead };

    if (byCompany.has(lead.company_name)) {
      const cached = byCompany.get(lead.company_name);
      if (cached) {
        return { ...lead, recent_news_title: cached.title, recent_news_url: cached.url, recent_news_date: cached.date, recent_news_snippet: cached.snippet };
      }
      return { ...lead };
    }

    try {
      const url = new URL("https://openweb-ninja.p.rapidapi.com/google-search");
      url.searchParams.set("query", `"${lead.company_name}" news OR blog OR announcement`);
      url.searchParams.set("num_results", "5");
      url.searchParams.set("date_range", `${days}d`);

      const res = await retry(() => fetch(url.toString(), {
        headers: { "X-RapidAPI-Key": key, "X-RapidAPI-Host": "openweb-ninja.p.rapidapi.com" },
      }));
      if (!res.ok) {
        errors.push({ company: lead.company_name, error: `HTTP ${res.status}` });
        byCompany.set(lead.company_name, null);
        return { ...lead };
      }
      const j: any = await res.json();
      const results = (j?.results || []).filter((r: any) => !isBlocked(r)).slice(0, 1);
      if (results.length === 0) {
        byCompany.set(lead.company_name, null);
        return { ...lead };
      }
      const top = results[0];
      const record = { title: top.title || "", url: top.url || "", date: top.date || "", snippet: top.snippet || "" };
      byCompany.set(lead.company_name, record);
      enriched++;
      return { ...lead, recent_news_title: record.title, recent_news_url: record.url, recent_news_date: record.date, recent_news_snippet: record.snippet };
    } catch (e: any) {
      errors.push({ company: lead.company_name, error: e.message });
      byCompany.set(lead.company_name, null);
      return { ...lead };
    }
  })));

  writeCsv(output, enriched_rows);
  if (errors.length > 0) writeCsv("company-news-errors.csv", errors);

  console.log(`\n✅ Enriched ${enriched}/${leads.length} with news (${errors.length} errors)`);
  console.log(`Saved to ${output}`);
}

main().catch(e => { console.error(e); process.exit(1); });
