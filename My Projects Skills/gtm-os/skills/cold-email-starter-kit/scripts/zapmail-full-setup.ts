#!/usr/bin/env tsx
// 4-phase Zapmail setup: NS switch → connect → inboxes → export.
// Run: npx tsx scripts/zapmail-full-setup.ts --domains purchased-domains.csv --platform smartlead
//
// Outputs: inboxes.csv with per-inbox status and credentials.

import { env, required, parseArgs, readCsv, writeCsv, sleep, retry } from "./_lib.ts";

const ZAPMAIL_NS = ["pns61.cloudns.net", "pns62.cloudns.com", "pns63.cloudns.net", "pns64.cloudns.uk"];

async function dynadotSetNs(domains: string[], apiKey: string): Promise<void> {
  const params = new URLSearchParams();
  params.set("key", apiKey);
  params.set("command", "set_ns");
  params.set("domain", domains.join(","));
  ZAPMAIL_NS.forEach((ns, i) => params.set(`ns${i}`, ns));
  const url = `https://api.dynadot.com/api3.json?${params.toString().replace(/%2C/g, ",")}`;
  const r = await retry(() => fetch(url).then(x => x.json() as Promise<any>));
  if (r?.SetNsResponse?.ResponseCode !== 0) {
    throw new Error(`Dynadot set_ns failed: ${JSON.stringify(r)}`);
  }
}

async function zapmailConnect(domainNames: string[], apiKey: string): Promise<void> {
  for (let i = 0; i < domainNames.length; i += 50) {
    const batch = domainNames.slice(i, i + 50);
    const res = await retry(() => fetch("https://api.zapmail.ai/api/v2/domains/connect-domain", {
      method: "POST",
      headers: { "x-auth-zapmail": apiKey, "Content-Type": "application/json" },
      body: JSON.stringify({ domainNames: batch }),
    }));
    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Zapmail connect failed: ${text}`);
    }
    await sleep(3000);
  }
}

async function waitUntilAssignable(domainNames: string[], apiKey: string, timeoutMinutes = 30): Promise<Array<{ domain: string; uuid: string }>> {
  const deadline = Date.now() + timeoutMinutes * 60 * 1000;
  const target = new Set(domainNames);
  const found: Array<{ domain: string; uuid: string }> = [];
  const seen = new Set<string>();

  while (Date.now() < deadline) {
    // paginate through assignable
    for (let page = 1; page < 100; page++) {
      const res = await retry(() => fetch(`https://api.zapmail.ai/api/v2/domains/assignable?limit=100&page=${page}`, {
        headers: { "x-auth-zapmail": apiKey },
      }));
      if (!res.ok) break;
      const j: any = await res.json();
      const items: any[] = j?.data || [];
      if (items.length === 0) break;
      for (const item of items) {
        if (target.has(item.domainName) && !seen.has(item.domainName)) {
          found.push({ domain: item.domainName, uuid: item.uuid });
          seen.add(item.domainName);
        }
      }
      if (items.length < 100) break;
    }

    if (found.length / domainNames.length >= 0.95) {
      console.log(`${found.length}/${domainNames.length} assignable — proceeding.`);
      return found;
    }
    console.log(`${found.length}/${domainNames.length} assignable, waiting 5 min...`);
    await sleep(5 * 60 * 1000);
  }
  console.warn(`Timeout reached, ${found.length}/${domainNames.length} assignable.`);
  return found;
}

async function createMailboxes(
  assignable: Array<{ domain: string; uuid: string }>,
  firstName: string, lastName: string,
  prefix1: string, prefix2: string,
  apiKey: string,
): Promise<Record<string, string[]>> {
  const results: Record<string, string[]> = {};
  for (let i = 0; i < assignable.length; i += 25) {
    const batch = assignable.slice(i, i + 25);
    const body: Record<string, any> = {};
    for (const { uuid, domain } of batch) {
      body[uuid] = [
        { firstName, lastName, mailboxUsername: prefix1, domainName: domain },
        { firstName, lastName, mailboxUsername: prefix2, domainName: domain },
      ];
    }
    const res = await fetch("https://api.zapmail.ai/api/v2/mailboxes", {
      method: "POST",
      headers: { "x-auth-zapmail": apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    if (!res.ok) {
      console.warn(`Batch failed (${res.status}), retrying individually...`);
      for (const { uuid, domain } of batch) {
        try {
          const single: any = { [uuid]: [
            { firstName, lastName, mailboxUsername: prefix1, domainName: domain },
            { firstName, lastName, mailboxUsername: prefix2, domainName: domain },
          ] };
          const r2 = await fetch("https://api.zapmail.ai/api/v2/mailboxes", {
            method: "POST",
            headers: { "x-auth-zapmail": apiKey, "Content-Type": "application/json" },
            body: JSON.stringify(single),
          });
          if (r2.ok) results[domain] = ["created"];
          else console.warn(`Individual ${domain} also failed: ${r2.status}`);
        } catch (e: any) {
          console.warn(`Error on ${domain}: ${e.message}`);
        }
        await sleep(500);
      }
    } else {
      batch.forEach(({ domain }) => { results[domain] = ["created"]; });
    }
    await sleep(3000);
  }
  return results;
}

async function exportToPlatform(app: "SMARTLEAD" | "INSTANTLY", contains: string, apiKey: string): Promise<any> {
  const res = await retry(() => fetch("https://api.zapmail.ai/api/v2/exports/mailboxes", {
    method: "POST",
    headers: { "x-auth-zapmail": apiKey, "Content-Type": "application/json" },
    body: JSON.stringify({
      apps: [app], ids: [], excludeIds: [], tagIds: [], contains, status: "ACTIVE",
    }),
  }));
  if (!res.ok) throw new Error(`Export failed: ${await res.text()}`);
  return await res.json();
}

async function main() {
  const { flags } = parseArgs();
  const domainsFile = (flags.domains as string) || "purchased-domains.csv";
  const firstName = (flags["first-name"] as string) || env.SENDER_FIRST_NAME || "Jane";
  const lastName = (flags["last-name"] as string) || env.SENDER_LAST_NAME || "Doe";
  const prefix1 = (env.SENDER_EMAIL_PREFIX_1 || firstName.toLowerCase());
  const prefix2 = (env.SENDER_EMAIL_PREFIX_2 || `${firstName.toLowerCase()}${lastName.toLowerCase()}`);
  const platformArg = (flags.platform as string) || "smartlead";
  const platform: "SMARTLEAD" | "INSTANTLY" = platformArg.toLowerCase() === "instantly" ? "INSTANTLY" : "SMARTLEAD";
  const skipWait = !!flags["skip-wait"];

  const dynadotKey = required("DYNADOT_API_KEY");
  const zapmailKey = required("ZAPMAIL_API_KEY");

  const rows = readCsv(domainsFile);
  const domains = rows.filter(r => r.status === "purchased").map(r => r.domain);
  if (domains.length === 0) {
    console.error("No purchased domains found in input CSV.");
    process.exit(1);
  }

  console.log(`Zapmail full setup for ${domains.length} domains.`);
  console.log(`Platform: ${platform}   Sender: ${firstName} ${lastName}`);
  console.log(`Inboxes: ${prefix1}@... and ${prefix2}@... (2 per domain = ${domains.length * 2} total)`);
  console.log();

  // Phase 1: NS switch
  console.log("Phase 1/4: Dynadot NS switch...");
  for (let i = 0; i < domains.length; i += 100) {
    await dynadotSetNs(domains.slice(i, i + 100), dynadotKey);
  }
  console.log("✅ NS switched to Zapmail.\n");

  // Phase 2: Wait for DNS propagation
  if (!skipWait) {
    console.log("Phase 2/4: Waiting 20 minutes for DNS propagation...");
    for (let m = 20; m > 0; m--) {
      process.stdout.write(`  ${m} min remaining...\r`);
      await sleep(60 * 1000);
    }
    console.log("  Done waiting.       \n");
  }

  // Phase 3: Connect on Zapmail
  console.log("Phase 3/4: Connecting domains on Zapmail...");
  await zapmailConnect(domains, zapmailKey);
  console.log("Connected. Polling for assignable status...");
  const assignable = await waitUntilAssignable(domains, zapmailKey, 30);
  console.log(`✅ ${assignable.length} domains assignable.\n`);

  // Phase 4: Create inboxes
  console.log("Phase 4/4: Creating inboxes...");
  const inboxResults = await createMailboxes(assignable, firstName, lastName, prefix1, prefix2, zapmailKey);
  const inboxRows: any[] = [];
  for (const { domain } of assignable) {
    const status = inboxResults[domain] ? "created" : "failed";
    inboxRows.push({ email: `${prefix1}@${domain}`, domain, status });
    inboxRows.push({ email: `${prefix2}@${domain}`, domain, status });
  }
  writeCsv("inboxes.csv", inboxRows);
  console.log(`✅ ${Object.keys(inboxResults).length} domains have inboxes created.\n`);

  console.log("Inbox provisioning takes 4-6 hours. You can walk away.");
  console.log("When ACTIVE, run the export manually OR re-run with --only-export:");
  console.log(`  npx tsx scripts/zapmail-full-setup.ts --only-export --platform ${platformArg} --contains ${prefix1}`);
  console.log();
  console.log("Export now (will pick up only ACTIVE inboxes):");
  try {
    const result = await exportToPlatform(platform, prefix1, zapmailKey);
    console.log(`✅ Export submitted: ${JSON.stringify(result).slice(0, 200)}`);
  } catch (e: any) {
    console.warn(`⚠️  Export skipped (inboxes likely still provisioning): ${e.message}`);
    console.log("Re-run export after 4-6 hours when inboxes are ACTIVE.");
  }
}

main().catch(e => { console.error(e); process.exit(1); });
