/**
 * Shared utilities for inbox-lifecycle-manager scripts.
 *
 * READ-ONLY helpers. Nothing in this file writes to Smartlead.
 */

export const API_BASE = "https://server.smartlead.ai/api/v1";
export const API_KEY = process.env.SMARTLEAD_API_KEY;

if (!API_KEY) {
  console.error("Missing env var: SMARTLEAD_API_KEY");
  process.exit(1);
}

// Smartlead 403s some default HTTP clients. A browser UA is the reliable path.
export const UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36";

export function parseFlag(args: string[], flag: string, def?: string): string | undefined {
  const arg = args.find((a) => a.startsWith(`${flag}=`));
  return arg ? arg.split("=").slice(1).join("=") : def;
}

export function hasFlag(args: string[], flag: string): boolean {
  return args.includes(flag);
}

export async function fetchJson(url: string, options: RequestInit = {}): Promise<any> {
  const opts: RequestInit = {
    ...options,
    headers: { "User-Agent": UA, ...(options.headers ?? {}) },
  };
  for (let attempt = 0; attempt < 5; attempt++) {
    const resp = await fetch(url, opts);
    if (resp.status === 429 || resp.status >= 500) {
      const retryAfter = Number(resp.headers.get("retry-after")) || 0;
      const wait = retryAfter * 1000 || 1000 * 2 ** attempt;
      console.error(`  [${resp.status}] retry ${attempt + 1}/5 in ${wait}ms`);
      await new Promise((r) => setTimeout(r, wait));
      continue;
    }
    if (!resp.ok) {
      const body = await resp.text().catch(() => "");
      throw new Error(`HTTP ${resp.status}: ${body.slice(0, 300)}`);
    }
    return resp.json();
  }
  throw new Error(`Exhausted retries: ${url.replace(API_KEY!, "***")}`);
}

export interface InboxAccount {
  id: number;
  from_email?: string;
  from_name?: string;
  created_at?: string;
  message_per_day?: number;
  type?: string;
  tags?: { id: number; name: string }[];
  warmup_details?: {
    status?: string;
    warmup_reputation?: string;
    is_warmup_blocked?: boolean;
  };
  is_smtp_success?: boolean;
  is_imap_success?: boolean;
  [key: string]: any;
}

/** Page every inbox on the account. NEVER stop early on a short page mid-run. */
export async function listAllInboxes(): Promise<InboxAccount[]> {
  const all: InboxAccount[] = [];
  const limit = 100; // hard cap: limit>100 silently returns 0 rows on this endpoint
  let offset = 0;
  for (;;) {
    const url = `${API_BASE}/email-accounts?api_key=${API_KEY}&offset=${offset}&limit=${limit}`;
    const batch: InboxAccount[] = await fetchJson(url);
    if (!Array.isArray(batch) || batch.length === 0) break;
    all.push(...batch);
    if (batch.length < limit) break;
    offset += limit;
  }
  return all;
}

export interface DomainMetric {
  domain: string;
  sent: number;
  replied: number;
  positive_replied: number;
  bounced: number;
}

/**
 * Live per-domain sent / replied / bounced for a date window.
 * This endpoint accepts a larger page size than the /email-accounts cap.
 */
export async function domainMetrics(
  startDate: string,
  endDate: string,
  clientIds?: string
): Promise<Map<string, DomainMetric>> {
  const out = new Map<string, DomainMetric>();
  const pageSize = 1000;
  let offset = 0;
  for (;;) {
    const params = new URLSearchParams({
      api_key: API_KEY!,
      start_date: startDate,
      end_date: endDate,
      full_data: "true",
      limit: String(pageSize),
      offset: String(offset),
    });
    if (clientIds) params.set("client_ids", clientIds);
    const json = await fetchJson(
      `${API_BASE}/analytics/mailbox/domain-wise-health-metrics?${params}`
    );
    const rows: any[] = json?.data?.domain_health_metrics ?? [];
    if (rows.length === 0) break;
    for (const r of rows) {
      const domain = String(r.domain || "").toLowerCase();
      if (!domain) continue;
      const prev = out.get(domain);
      const m: DomainMetric = {
        domain,
        sent: Number(r.sent || 0) + (prev?.sent ?? 0),
        replied: Number(r.replied || 0) + (prev?.replied ?? 0),
        positive_replied: Number(r.positive_replied || 0) + (prev?.positive_replied ?? 0),
        bounced: Number(r.bounced || 0) + (prev?.bounced ?? 0),
      };
      out.set(domain, m);
    }
    if (rows.length < pageSize) break;
    offset += pageSize;
  }
  return out;
}

export function domainOf(inbox: InboxAccount): string {
  const email = String(inbox.from_email || inbox.email || "");
  return email.includes("@") ? email.split("@").pop()!.toLowerCase() : "";
}

export function daysAgo(n: number): string {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().slice(0, 10);
}

export function today(): string {
  return new Date().toISOString().slice(0, 10);
}

export function writeCsv(path: string, rows: Record<string, any>[]): void {
  const { writeFileSync, mkdirSync } = require("fs");
  const { dirname } = require("path");
  mkdirSync(dirname(path), { recursive: true });
  if (rows.length === 0) {
    writeFileSync(path, "");
    return;
  }
  const headers = Object.keys(rows[0]);
  const esc = (v: any) => {
    const s = v === null || v === undefined ? "" : String(v);
    return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
  };
  const lines = [headers.join(",")];
  for (const r of rows) lines.push(headers.map((h) => esc(r[h])).join(","));
  writeFileSync(path, lines.join("\n") + "\n");
}

export function readCsv(path: string): Record<string, string>[] {
  const { readFileSync } = require("fs");
  const text = readFileSync(path, "utf8").trim();
  if (!text) return [];
  const lines = text.split("\n");
  const headers = splitCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const cells = splitCsvLine(line);
    const row: Record<string, string> = {};
    headers.forEach((h, i) => (row[h] = cells[i] ?? ""));
    return row;
  });
}

function splitCsvLine(line: string): string[] {
  const out: string[] = [];
  let cur = "";
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (inQuotes) {
      if (c === '"' && line[i + 1] === '"') { cur += '"'; i++; }
      else if (c === '"') inQuotes = false;
      else cur += c;
    } else if (c === '"') inQuotes = true;
    else if (c === ",") { out.push(cur); cur = ""; }
    else cur += c;
  }
  out.push(cur);
  return out;
}
