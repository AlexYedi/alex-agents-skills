/**
 * apply-lifecycle.ts — apply the TAG changes from actions.csv. DRY RUN unless --apply.
 *
 *   npx tsx apply-lifecycle.ts --actions=./lifecycle-2026-09-29/actions.csv          # dry run
 *   npx tsx apply-lifecycle.ts --actions=./lifecycle-2026-09-29/actions.csv --apply
 *
 * This script changes TAGS ONLY. It never cancels a provider subscription — that is a
 * separate, explicitly approved, manually batched step. See references/cancellation-safety.md.
 *
 * It reads every mutated domain back afterwards and reports confirmed vs unverified.
 * An unverified domain means the run is NOT done.
 */
import {
  API_BASE, API_KEY, fetchJson, listAllInboxes, domainOf,
  parseFlag, hasFlag, readCsv, InboxAccount,
} from "./_lib";

const MANAGED = ["active", "insurance", "warmup", "cancel"];
const BATCH = 10; // small batches, verified one at a time — see cancellation-safety.md

async function setTag(inbox: InboxAccount, to: string): Promise<void> {
  // Same endpoint and payload shape as smartlead-inbox-manager/scripts/tag-inboxes.ts.
  // Smartlead has no tag-delete on every version: replace the whole list, omitting the
  // managed tags we are superseding and keeping everything else the user put there.
  const keep = (inbox.tags ?? [])
    .filter((t: any) => !MANAGED.includes(String(t.name).toLowerCase()))
    .map((t: any) => ({ id: t.id, name: t.name, color: t.color }));
  const tags = [...keep, { name: to }];
  await fetchJson(`${API_BASE}/email-accounts/tag?api_key=${API_KEY}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email_account_ids: [inbox.id], tags }),
  });
}

async function main() {
  const args = process.argv.slice(2);
  const actionsPath = parseFlag(args, "--actions");
  if (!actionsPath) { console.error("Required: --actions=path/to/actions.csv"); process.exit(1); }
  const live = hasFlag(args, "--apply");

  const actions = readCsv(actionsPath).filter((a) => a.domain && a.to);
  if (actions.length === 0) { console.log("No actions in file. Nothing to do."); return; }

  const inboxes = await listAllInboxes();
  const byDomain = new Map<string, InboxAccount[]>();
  for (const ib of inboxes) {
    const d = domainOf(ib);
    if (!d) continue;
    if (!byDomain.has(d)) byDomain.set(d, []);
    byDomain.get(d)!.push(ib);
  }

  console.log(`${live ? "APPLYING" : "DRY RUN"} — ${actions.length} domain actions\n`);
  for (const a of actions) {
    const ibs = byDomain.get(a.domain.toLowerCase()) ?? [];
    console.log(`  ${a.action.padEnd(8)} ${a.domain.padEnd(32)} ${a.from} -> ${a.to}  (${ibs.length} inboxes)  ${a.reason ?? ""}`);
    if (ibs.length === 0) console.log(`           !! no inboxes found for this domain — skipped`);
  }

  if (!live) {
    console.log(`\nDRY RUN. Nothing changed. Re-run with --apply after an explicit yes.`);
    return;
  }

  const confirmed: string[] = [];
  const unverified: string[] = [];

  for (let i = 0; i < actions.length; i += BATCH) {
    const batch = actions.slice(i, i + BATCH);
    for (const a of batch) {
      const ibs = byDomain.get(a.domain.toLowerCase()) ?? [];
      // Whole domain or nothing: every inbox on the domain moves together.
      for (const ib of ibs) {
        try { await setTag(ib, a.to.toLowerCase()); }
        catch (e) { console.error(`  write failed ${ib.from_email}: ${e}`); }
      }
    }
    // Read back this batch before touching the next one. A 200 is not proof.
    const fresh = await listAllInboxes();
    const freshByDomain = new Map<string, InboxAccount[]>();
    for (const ib of fresh) {
      const d = domainOf(ib);
      if (!d) continue;
      if (!freshByDomain.has(d)) freshByDomain.set(d, []);
      freshByDomain.get(d)!.push(ib);
    }
    for (const a of batch) {
      const ibs = freshByDomain.get(a.domain.toLowerCase()) ?? [];
      const ok = ibs.length > 0 && ibs.every((ib) =>
        (ib.tags ?? []).some((t) => String(t.name).toLowerCase() === a.to.toLowerCase()));
      (ok ? confirmed : unverified).push(a.domain);
    }
    console.log(`  batch ${Math.floor(i / BATCH) + 1}: ${confirmed.length} confirmed, ${unverified.length} unverified so far`);
  }

  console.log(`
=== Readback ===
confirmed:  ${confirmed.length}
unverified: ${unverified.length}${unverified.length ? "  <- THE RUN IS NOT DONE. These stay on the open list." : ""}
${unverified.length ? unverified.join("\n") : ""}

Tags only. No provider subscription was cancelled. Do that separately, in small
verified batches, after a second explicit approval — references/cancellation-safety.md.
`);
}

main().catch((e) => { console.error(e); process.exit(1); });
