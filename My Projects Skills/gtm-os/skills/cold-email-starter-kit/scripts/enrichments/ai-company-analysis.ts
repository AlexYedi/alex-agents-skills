#!/usr/bin/env tsx
// Enrich leads with AI-generated company analysis (GPT-4o-mini via OpenRouter).
// Adds columns: ai_company_summary, ai_industry_category, ai_customer_type, ai_company_mission
// Run: npx tsx scripts/enrichments/ai-company-analysis.ts --input leads.csv --output leads-ai.csv

import { env, required, parseArgs, readCsv, writeCsv, createQueue, retry } from "../_lib.ts";

async function callLLM(prompt: string, model: string, key: string): Promise<any> {
  const res = await retry(() => fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: { "Authorization": `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      model,
      messages: [{ role: "user", content: prompt }],
      response_format: { type: "json_object" },
      max_tokens: 500,
    }),
  }));
  if (!res.ok) throw new Error(`OpenRouter ${res.status}: ${await res.text()}`);
  const j: any = await res.json();
  const content = j?.choices?.[0]?.message?.content;
  return content ? JSON.parse(content) : null;
}

async function main() {
  const { flags } = parseArgs();
  const input = (flags.input as string) || "leads.csv";
  const output = (flags.output as string) || "leads-ai.csv";
  const model = (flags.model as string) || "openai/gpt-4o-mini";

  const key = required("OPENROUTER_API_KEY");

  const leads = readCsv(input);
  console.log(`Enriching ${leads.length} leads with AI analysis (${model})...`);

  const queue = createQueue(20);
  const errors: any[] = [];
  let enriched = 0;

  const enriched_rows = await Promise.all(leads.map(lead => queue.add(async () => {
    if (!lead.company_name) return { ...lead };
    const prompt = `Given this company:
Name: ${lead.company_name}
Domain: ${lead.company_domain || "unknown"}
Industry: ${lead.company_industry || "unknown"}
Headcount: ${lead.company_headcount || "unknown"}

Provide:
1. company_summary: one-sentence what they do (max 15 words)
2. industry_category: specific vertical (e.g. "HR tech", "defense contracting")
3. customer_type: who they sell to (max 10 words)
4. company_mission: what they exist to help customers achieve (max 15 words)

Respond as JSON with exactly these keys: {"company_summary", "industry_category", "customer_type", "company_mission"}`;

    try {
      const result = await callLLM(prompt, model, key);
      if (result && result.company_summary) {
        enriched++;
        return {
          ...lead,
          ai_company_summary: result.company_summary || "",
          ai_industry_category: result.industry_category || "",
          ai_customer_type: result.customer_type || "",
          ai_company_mission: result.company_mission || "",
        };
      }
      return { ...lead };
    } catch (e: any) {
      errors.push({ email: lead.email, company: lead.company_name, error: e.message });
      return { ...lead };
    }
  })));

  writeCsv(output, enriched_rows);
  if (errors.length > 0) writeCsv("ai-company-analysis-errors.csv", errors);

  console.log(`\n✅ Enriched ${enriched}/${leads.length} with AI analysis (${errors.length} errors)`);
  console.log(`Saved to ${output}`);
}

main().catch(e => { console.error(e); process.exit(1); });
