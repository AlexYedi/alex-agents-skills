#!/usr/bin/env tsx
// Pings every configured API. Prints ✅/⚠️/❌ status table.
// Run: npx tsx scripts/verify-credentials.ts

import { env, printTable } from "./_lib.ts";

interface Check {
  service: string;
  status: "✅" | "⚠️" | "❌";
  notes: string;
}

async function checkDynadot(): Promise<Check> {
  if (!env.DYNADOT_API_KEY) return { service: "Dynadot", status: "❌", notes: "DYNADOT_API_KEY not set" };
  try {
    const r = await fetch(`https://api.dynadot.com/api3.json?key=${env.DYNADOT_API_KEY}&command=account_info`);
    const j: any = await r.json();
    if (j.Response?.ResponseCode === 0 || j.AccountInfoResponse) {
      const balance = j.AccountInfoResponse?.AccountInfo?.AccountBalance || "unknown";
      return { service: "Dynadot", status: "✅", notes: `Wallet: ${balance}` };
    }
    return { service: "Dynadot", status: "❌", notes: `API error: ${j.Error || JSON.stringify(j).slice(0, 80)}` };
  } catch (e: any) {
    return { service: "Dynadot", status: "❌", notes: `Network error: ${e.message}` };
  }
}

async function checkZapmail(): Promise<Check> {
  if (!env.ZAPMAIL_API_KEY) return { service: "Zapmail", status: "❌", notes: "ZAPMAIL_API_KEY not set" };
  try {
    const r = await fetch("https://api.zapmail.ai/api/v2/domains/assignable?limit=5&page=1", {
      headers: { "x-auth-zapmail": env.ZAPMAIL_API_KEY },
    });
    if (r.status === 200) {
      const j: any = await r.json();
      const count = j?.data?.length ?? 0;
      return { service: "Zapmail", status: "✅", notes: `${count} assignable domains visible` };
    }
    return { service: "Zapmail", status: "❌", notes: `HTTP ${r.status}` };
  } catch (e: any) {
    return { service: "Zapmail", status: "❌", notes: `Network error: ${e.message}` };
  }
}

async function checkProspeo(): Promise<Check> {
  if (!env.PROSPEO_API_KEY) return { service: "Prospeo", status: "❌", notes: "PROSPEO_API_KEY not set" };
  try {
    // Tiny request to test auth — 1 result, no credit charge
    const r = await fetch("https://api.prospeo.io/search-person", {
      method: "POST",
      headers: { "X-KEY": env.PROSPEO_API_KEY, "Content-Type": "application/json" },
      body: JSON.stringify({ page: 1, filters: { person_location_search: { include: ["California, United States #US"] } } }),
    });
    if (r.status === 200) {
      return { service: "Prospeo", status: "✅", notes: "Auth OK" };
    }
    if (r.status === 401) return { service: "Prospeo", status: "❌", notes: "Invalid API key" };
    return { service: "Prospeo", status: "❌", notes: `HTTP ${r.status}` };
  } catch (e: any) {
    return { service: "Prospeo", status: "❌", notes: `Network error: ${e.message}` };
  }
}

async function checkSmartlead(): Promise<Check> {
  if (!env.SMARTLEAD_API_KEY) return { service: "Smartlead", status: "⚠️", notes: "Not configured (optional if using Instantly)" };
  try {
    const r = await fetch(`https://server.smartlead.ai/api/v1/campaigns?api_key=${env.SMARTLEAD_API_KEY}`);
    if (r.status === 200) {
      const j: any = await r.json();
      const count = Array.isArray(j) ? j.length : 0;
      return { service: "Smartlead", status: "✅", notes: `${count} campaigns` };
    }
    return { service: "Smartlead", status: "❌", notes: `HTTP ${r.status}` };
  } catch (e: any) {
    return { service: "Smartlead", status: "❌", notes: `Network error: ${e.message}` };
  }
}

async function checkInstantly(): Promise<Check> {
  if (!env.INSTANTLY_API_KEY) return { service: "Instantly", status: "⚠️", notes: "Not configured (optional if using Smartlead)" };
  try {
    const r = await fetch("https://api.instantly.ai/api/v2/workspace", {
      headers: { "Authorization": `Bearer ${env.INSTANTLY_API_KEY}` },
    });
    if (r.status === 200) {
      const j: any = await r.json();
      return { service: "Instantly", status: "✅", notes: `Workspace: ${j?.name || "OK"}` };
    }
    if (r.status === 401) return { service: "Instantly", status: "❌", notes: "Bearer token invalid" };
    return { service: "Instantly", status: "❌", notes: `HTTP ${r.status}` };
  } catch (e: any) {
    return { service: "Instantly", status: "❌", notes: `Network error: ${e.message}` };
  }
}

async function main() {
  console.log("Checking credentials...\n");
  const checks = await Promise.all([
    checkDynadot(), checkZapmail(), checkProspeo(), checkSmartlead(), checkInstantly(),
  ]);
  printTable(checks as any);
  console.log();

  const hasSendingPlatform = checks.some(c => (c.service === "Smartlead" || c.service === "Instantly") && c.status === "✅");
  const failed = checks.filter(c => c.status === "❌");

  if (failed.length > 0) {
    console.log(`❌ ${failed.length} service(s) failing. Fix before continuing.`);
    process.exit(1);
  }
  if (!hasSendingPlatform) {
    console.log("❌ You need at least one of Smartlead or Instantly configured.");
    process.exit(1);
  }
  console.log("✅ All required services OK. Ready to launch.");
}

main().catch(e => { console.error(e); process.exit(1); });
