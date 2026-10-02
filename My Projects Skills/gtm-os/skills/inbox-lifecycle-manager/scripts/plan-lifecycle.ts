/**
 * plan-lifecycle.ts — READ-ONLY weekly keep/cancel/promote/demote/buy planner.
 *
 * Writes nothing to Smartlead. Emits plan.csv, actions.csv, and (with --snapshot)
 * snapshot.csv — the pre-state you need for a clean rollback.
 *
 *   npx tsx plan-lifecycle.ts --goal=2000 --out=./lifecycle-2026-09-29 [--snapshot]
 *     --goal=N              daily send goal, emails/day (required)
 *     --out=DIR             output directory (default ./lifecycle-<today>)
 *     --client-ids=1,2      scope to sub-clients (default: whole account)
 *     --inboxes-per-domain=3    for the buy math (default 3)
 *     --snapshot            also write snapshot.csv of current per-domain state
 *
 * Status is read from inbox tags: warmup | insurance | active | cancel.
 * Untagged inboxes that are attached and sending read as active.
 */
import {
  listAllInboxes, domainMetrics, domainOf, daysAgo, today,
  writeCsv, parseFlag, hasFlag, InboxAccount,
} from "./_lib";

// ---- thresholds (see SKILL.md "The numbers, and where they come from") -------
const REPLY_CANCEL_LINE = 1.0;   // % — below this, over the send floor, a domain is burned
const REPLY_GOOD_LINE = 1.5;     // % — comfortably healthy
const ZERO_REPLY_FLOOR = 150;    // sends — 0 replies at/above this is decisive
const MIN_SENDS_REPLY = 200;     // sends — floor before a reply rate means anything
const MIN_SENDS_BOUNCE = 50;     // sends — floor before a bounce rate means anything
const BOUNCE_FORK = 3.0;         // % — fork entry, red band, and autopause threshold
const MIN_AGE_DAYS = 30;         // days — never cancel younger, at any reply rate
const MIN_REPUTATION = 98;       // % warmup reputation to be promotable
const DEMOTE_RATIO = 1.25;       // demote when active capacity >= this x goal
const INSURANCE_RATIO = 0.5;     // hold this fraction of goal warm in reserve
const CAP_PER_INBOX: Record<string, number> = { GMAIL: 30, OUTLOOK: 30, SMTP: 15 };

const STATUS_RANK = ["active", "insurance", "cancel", "warmup"]; // ascending restrictiveness

interface DomainRow {
  domain: string;
  status: string;
  all_statuses: string;
  inbox_count: number;
  capacity_per_day: number;
  age_days: number | "";
  sent_7d: number; replied_7d: number; bounced_7d: number;
  sent_14d: number; replied_14d: number; bounced_14d: number;
  window: string;
  sent: number; reply_pct: string; bounce_pct: string;
  reputation_pct: number | "";
  warmup_off: boolean; smtp_ok: boolean;
  verdict: string;
  reason: string;
}

function statusOf(inboxes: InboxAccount[]): { status: string; all: string[] } {
  const seen = new Set<string>();
  for (const ib of inboxes) {
    const tags = (ib.tags ?? []).map((t) => String(t.name || "").toLowerCase());
    const hit = STATUS_RANK.find((s) => tags.includes(s));
    // Untagged inbox: treat warmup-on as insurance, warmup-off as active.
    const warmupOn = String(ib.warmup_details?.status || "").toUpperCase() === "ACTIVE";
    seen.add(hit ?? (warmupOn ? "insurance" : "active"));
  }
  // Aggregate by RESTRICTIVENESS, never alphabetical min().
  const status = STATUS_RANK.slice().reverse().find((s) => seen.has(s)) ?? "active";
  return { status, all: [...seen] };
}

function reputationOf(inboxes: InboxAccount[]): number | "" {
  const vals = inboxes
    .map((ib) => parseFloat(String(ib.warmup_details?.warmup_reputation ?? "").replace("%", "")))
    .filter((n) => Number.isFinite(n));
  if (vals.length === 0) return "";
  return Math.round(vals.reduce((a, b) => a + b, 0) / vals.length);
}

function ageOf(inboxes: InboxAccount[]): number | "" {
  const dates = inboxes
    .map((ib) => ib.created_at)
    .filter(Boolean)
    .map((d) => new Date(String(d)).getTime())
    .filter((t) => Number.isFinite(t));
  if (dates.length === 0) return ""; // unresolvable -> treated as TOO_YOUNG downstream
  return Math.floor((Date.now() - Math.min(...dates)) / 86400000);
}

function capacityOf(inboxes: InboxAccount[]): number {
  return inboxes.reduce((sum, ib) => {
    const type = String(ib.type || "GMAIL").toUpperCase();
    const perDay = ib.message_per_day && ib.message_per_day > 0
      ? ib.message_per_day
      : (CAP_PER_INBOX[type] ?? 30);
    return sum + perDay;
  }, 0);
}

function judge(r: DomainRow): { verdict: string; reason: string } {
  if (r.status === "warmup" || r.all_statuses.includes("warmup"))
    return { verdict: "EXCLUDED", reason: "in warmup; untouchable" };
  if (r.age_days === "" )
    return { verdict: "TOO_YOUNG", reason: "age unresolvable; fail closed, never cancel" };
  if ((r.age_days as number) < MIN_AGE_DAYS)
    return { verdict: "TOO_YOUNG", reason: `${r.age_days}d old, floor is ${MIN_AGE_DAYS}d` };
  if (r.warmup_off && !r.smtp_ok)
    return { verdict: "ALREADY_DEAD", reason: "warmup off AND SMTP failing; not sending at all" };
  if (r.warmup_off && r.status !== "active")
    return { verdict: "HELD", reason: "warmup off; reputation unreadable, hold from promotion" };
  if (r.sent < MIN_SENDS_REPLY)
    return { verdict: "INSUFFICIENT_DATA", reason: `${r.sent} sends, floor is ${MIN_SENDS_REPLY}` };

  const bouncePct = parseFloat(r.bounce_pct);
  if (r.sent >= MIN_SENDS_BOUNCE && bouncePct > BOUNCE_FORK)
    return {
      verdict: "BOUNCE_FORK",
      reason: `bounce ${r.bounce_pct}% > ${BOUNCE_FORK}% — classify the bounce codes before cancelling`,
    };

  const replyPct = parseFloat(r.reply_pct);
  if (replyPct >= REPLY_GOOD_LINE)
    return { verdict: "HEALTHY", reason: `reply ${r.reply_pct}% — keep` };
  if (replyPct >= REPLY_CANCEL_LINE)
    return { verdict: "HEALTHY", reason: `reply ${r.reply_pct}% — at or above the ${REPLY_CANCEL_LINE}% line` };
  if (r.replied_7d + r.replied_14d === 0 && r.sent >= ZERO_REPLY_FLOOR)
    return { verdict: "BURNED", reason: `0 replies on ${r.sent} sends` };
  return { verdict: "BURNED", reason: `reply ${r.reply_pct}% < ${REPLY_CANCEL_LINE}% on ${r.sent} sends` };
}

async function main() {
  const args = process.argv.slice(2);
  const goal = Number(parseFlag(args, "--goal", "0"));
  if (!goal) { console.error("Required: --goal=<emails per day>"); process.exit(1); }
  const outDir = parseFlag(args, "--out", `./lifecycle-${today()}`)!;
  const clientIds = parseFlag(args, "--client-ids");
  const perDomain = Number(parseFlag(args, "--inboxes-per-domain", "3"));

  console.log("Pulling inbox inventory...");
  const inboxes = await listAllInboxes();
  console.log(`  ${inboxes.length} inboxes`);

  console.log("Pulling live 7d + 14d domain metrics...");
  const [m7, m14] = await Promise.all([
    domainMetrics(daysAgo(7), today(), clientIds),
    domainMetrics(daysAgo(14), today(), clientIds),
  ]);
  console.log(`  ${m7.size} domains with 7d activity, ${m14.size} with 14d`);

  const byDomain = new Map<string, InboxAccount[]>();
  for (const ib of inboxes) {
    const d = domainOf(ib);
    if (!d) continue;
    if (!byDomain.has(d)) byDomain.set(d, []);
    byDomain.get(d)!.push(ib);
  }

  const rows: DomainRow[] = [];
  for (const [domain, ibs] of byDomain) {
    const { status, all } = statusOf(ibs);
    const a = m7.get(domain) ?? { domain, sent: 0, replied: 0, positive_replied: 0, bounced: 0 };
    const b = m14.get(domain) ?? { domain, sent: 0, replied: 0, positive_replied: 0, bounced: 0 };
    // Prefer the 7d window; fall back to 14d only when 7d is under the send floor.
    const use7 = a.sent >= MIN_SENDS_REPLY;
    const w = use7 ? a : b;
    const pct = (n: number, d: number) => (d > 0 ? ((n / d) * 100).toFixed(2) : "0.00");

    const row: DomainRow = {
      domain, status, all_statuses: all.sort().join("|"),
      inbox_count: ibs.length,
      capacity_per_day: capacityOf(ibs),
      age_days: ageOf(ibs),
      sent_7d: a.sent, replied_7d: a.replied, bounced_7d: a.bounced,
      sent_14d: b.sent, replied_14d: b.replied, bounced_14d: b.bounced,
      window: use7 ? "7d" : "14d",
      sent: w.sent,
      reply_pct: pct(w.replied, w.sent),
      bounce_pct: pct(w.bounced, w.sent),
      reputation_pct: reputationOf(ibs),
      warmup_off: ibs.every((ib) => String(ib.warmup_details?.status || "").toUpperCase() !== "ACTIVE"),
      smtp_ok: ibs.some((ib) => ib.is_smtp_success !== false),
      verdict: "", reason: "",
    };
    const v = judge(row);
    row.verdict = v.verdict;
    row.reason = v.reason;
    rows.push(row);
  }

  // ---- capacity, promote, demote, buy ---------------------------------------
  const activeCap = rows.filter((r) => r.status === "active" && r.verdict !== "BURNED")
    .reduce((s, r) => s + r.capacity_per_day, 0);
  const insuranceRows = rows.filter(
    (r) => r.status === "insurance" &&
      !["EXCLUDED", "TOO_YOUNG", "ALREADY_DEAD", "HELD", "BURNED"].includes(r.verdict) &&
      (r.reputation_pct === "" || (r.reputation_pct as number) >= MIN_REPUTATION)
  ).sort((a, b) => Number(b.age_days || 0) - Number(a.age_days || 0)); // OLDEST first

  const burned = rows.filter((r) => r.verdict === "BURNED");
  const actions: Record<string, any>[] = [];

  let cap = activeCap;
  let reserve = [...insuranceRows];

  // Cancel a burned domain only if a reserve can replace its capacity.
  // activeCap above already EXCLUDES burned domains, so a cancel costs nothing more here
  // and a kept-below-threshold domain (still sending) has to be added back in.
  for (const r of burned) {
    const swap = reserve.shift();
    if (swap) {
      actions.push({ domain: r.domain, action: "CANCEL", from: r.status, to: "cancel",
        capacity_per_day: r.capacity_per_day, verdict: r.verdict, reason: r.reason });
      actions.push({ domain: swap.domain, action: "PROMOTE", from: "insurance", to: "active",
        capacity_per_day: swap.capacity_per_day, verdict: swap.verdict,
        reason: `replaces ${r.domain}; oldest eligible reserve (${swap.age_days}d)` });
      cap += swap.capacity_per_day;
    } else {
      r.verdict = "KEEP_BELOW_THRESHOLD";
      r.reason += " — no reserve to swap in; BUY FIRST, cancel next week";
      if (r.status === "active") cap += r.capacity_per_day;
    }
  }

  // Fill to goal from what's left of the reserve, oldest first.
  while (cap < goal && reserve.length) {
    const s = reserve.shift()!;
    actions.push({ domain: s.domain, action: "PROMOTE", from: "insurance", to: "active",
      capacity_per_day: s.capacity_per_day, verdict: s.verdict,
      reason: `fill to goal; oldest eligible reserve (${s.age_days}d)` });
    cap += s.capacity_per_day;
  }

  // Demote the worst healthy Active domains while well over goal.
  if (cap >= goal * DEMOTE_RATIO) {
    const demotable = rows
      .filter((r) => r.status === "active" && r.verdict === "HEALTHY")
      .sort((a, b) => parseFloat(a.reply_pct) - parseFloat(b.reply_pct));
    for (const r of demotable) {
      if (cap - r.capacity_per_day < goal) break;
      actions.push({ domain: r.domain, action: "DEMOTE", from: "active", to: "insurance",
        capacity_per_day: r.capacity_per_day, verdict: r.verdict,
        reason: `active capacity ${cap}/day >= ${DEMOTE_RATIO}x goal` });
      cap -= r.capacity_per_day;
      if (cap < goal * DEMOTE_RATIO) break;
    }
  }

  const insuranceCap = reserve.reduce((s, r) => s + r.capacity_per_day, 0);
  const shortfall = Math.max(0, goal * (1 + INSURANCE_RATIO) - (cap + insuranceCap));
  const inboxesToBuy = Math.ceil(shortfall / 30);
  const domainsToBuy = Math.ceil(inboxesToBuy / perDomain);

  writeCsv(`${outDir}/plan.csv`, rows.sort((a, b) => b.sent - a.sent) as any);
  writeCsv(`${outDir}/actions.csv`, actions);
  if (hasFlag(args, "--snapshot")) {
    writeCsv(`${outDir}/snapshot.csv`, rows.map((r) => ({
      domain: r.domain, status: r.status, all_statuses: r.all_statuses,
      inbox_count: r.inbox_count, captured_at: new Date().toISOString(),
    })));
    console.log(`\nSnapshot written. Confirm it is non-empty before any apply.`);
  }

  const count = (v: string) => rows.filter((r) => r.verdict === v).length;
  console.log(`
=== Lifecycle plan ${today()} ===
Domains:            ${rows.length}   (${inboxes.length} inboxes)
Goal:               ${goal}/day     Active capacity after plan: ${cap}/day (${Math.round(cap / goal * 100)}%)
Insurance reserve:  ${insuranceCap}/day   (target ${goal * INSURANCE_RATIO}/day)

Verdicts
  HEALTHY                    ${count("HEALTHY")}
  BURNED (cancel)            ${count("BURNED")}
  KEEP_BELOW_THRESHOLD       ${count("KEEP_BELOW_THRESHOLD")}   <- buy replacements first
  BOUNCE_FORK                ${count("BOUNCE_FORK")}   <- classify bounce codes, do not cancel yet
  INSUFFICIENT_DATA          ${count("INSUFFICIENT_DATA")}
  TOO_YOUNG                  ${count("TOO_YOUNG")}
  EXCLUDED (warmup)          ${count("EXCLUDED")}
  HELD (warmup off)          ${count("HELD")}
  ALREADY_DEAD               ${count("ALREADY_DEAD")}

Actions: ${actions.filter(a => a.action === "CANCEL").length} cancel, ${actions.filter(a => a.action === "PROMOTE").length} promote, ${actions.filter(a => a.action === "DEMOTE").length} demote
Buy:     ${shortfall > 0 ? `${shortfall}/day short -> ${inboxesToBuy} inboxes (~${domainsToBuy} domains)` : "nothing"}

Wrote ${outDir}/plan.csv and ${outDir}/actions.csv
NOTHING WAS CHANGED. Review, get an explicit yes, then run apply-lifecycle.ts.
`);
}

main().catch((e) => { console.error(e); process.exit(1); });
