# The decision ladder in full

One verdict per domain, per window. First gate that matches wins. Nothing falls through.

```
START: one sending domain, one window (7d; fall back to 14d if 7d is under the 200-send floor)

G0. Any inbox on this domain in Warmup?
      YES -> EXCLUDED. Untouchable for its full warmup period. Stop.
      NO  -> G1

      AGGREGATING A MIXED DOMAIN: a domain can hold inboxes in several statuses at once.
      Aggregate by RESTRICTIVENESS -- Warmup > Cancel > Insurance > Active -- and carry the
      full distinct set alongside it. NEVER use min(): "Active" sorts first alphabetically,
      so min() returns the LEAST restrictive status and lets a mostly-warming domain be judged.

G1. Domain age < 30 days, OR age cannot be resolved?
      YES -> TOO_YOUNG. Never a cancel candidate, at any reply rate. Stop.
             FAIL CLOSED: unknown age lands here. Do not cancel what you cannot date.
      NO  -> G2

      AGE = the earliest creation date across the domain's inboxes. If your tool does not
      expose one, keep your own provisioning log. A missing date is "young", not "old".

G2. sent < 200 in the window?
      YES -> INSUFFICIENT_DATA. Reply rate is not evaluable. Re-check next week. Stop.
      NO  -> B0

B0. Blocklist share > 20% of classified bounces, with >= 30 classified bounces for THIS domain?
      (SMTP codes 5.7.606-5.7.614, or DSN text naming a blocklist / Spamhaus)
      YES -> BURNED. Cancel candidate. Deliberately RATE-INDEPENDENT: it sits above the
             bounce-rate gate so a domain that is majority-blocklisted at a 2.5% bounce rate
             is still caught. Do not reorder this below G3.
      NO  -> G3

G3. sent >= 50 AND bounce_rate > 3%?
      YES -> BOUNCE FORK (B1)
      bounce_rate 1-3% -> note as yellow, continue to R1
      NO  -> R1

--- B: bounce fork -----------------------------------------------------------------

B1. >= 30 bounces classified and attributed to THIS domain?
      NO  -> INSUFFICIENT_BOUNCE_SAMPLE. Stop. Never fall through to "list problem":
             an unsampled domain has a 0% sender share by construction, which is
             indistinguishable from a genuinely recipient-side bounce profile.
      YES -> B2

B2. Share of bounces attributed to our sending side ("sender share"):
      < 25%    -> LIST_PROBLEM. Revalidate the list, keep verified-valid only. Not the domain.
      25-50%   -> MIXED. Both diseases. Fix DNS auth first, then revalidate. Re-check in 7 days.
      > 50%    -> B3

B3. SPF present and not "+all", DKIM present at ANY known selector, DMARC present?
      NO  -> SENDER_AUTH. Fixable. Fix the record, re-diagnose in 7 days. DO NOT CANCEL.
      YES -> BURNED. Configuration is clean and we are still refused. Cancel candidate.

      DKIM HAS NO SINGLE SELECTOR. It is present if ANY of these resolves:
        dig TXT   google._domainkey.<d>    +short   # Google / Gmail-backed providers
        dig CNAME selector1._domainkey.<d> +short   # Microsoft 365 (a CNAME, TXT returns nothing)
        dig CNAME selector2._domainkey.<d> +short   # Microsoft 365, second key
        dig TXT   default._domainkey.<d>   +short   # generic fallback, often empty
      Checking `default` alone marks an entire healthy fleet "missing DKIM", routes every
      burned domain to SENDER_AUTH, and buys a week of republishing DKIM that already exists.

--- R: reply fork ------------------------------------------------------------------

R1. reply_rate >= 1.0%?
      YES -> HEALTHY. Keep Active. Stop.
      NO  -> R2

R2. Placement test run on this domain in the last 14 days?
      NO  -> NEEDS_PLACEMENT_TEST. Run one before condemning. Domain stays open.
      YES -> R3

R3. Inbox placement > 90%?
      YES -> NOT_DELIVERABILITY. Bounces clean, placement good, replies still low.
             This is targeting, offer, or copy. Do not cancel the domain.
      NO  -> R4

R4. Isolation: send the same copy from a known-good control fleet.
      control ~100%, ours < 100%   -> BURNED (domain-side placement failure). Cancel candidate.
      both < 100%                   -> COPY_PROBLEM. Fix the copy, not the fleet.
      control untestable            -> COPY_PROBLEM. Assume copy: cheaper to fix and reversible.

--- Final gate on every BURNED verdict ----------------------------------------------

C1. Is there an Insurance domain to swap in, or are we deliberately shrinking?
      YES -> CANCEL.
      NO  -> KEEP_BELOW_THRESHOLD. Flag it, buy replacements, cancel next week.
             Cancelling into a shortfall trades a bad reply rate for no sends at all.
```

## Verdict table

| Verdict | One sentence | Hand off to | Do NOT |
|---|---|---|---|
| `EXCLUDED` | In warmup, not judged | nothing | touch it |
| `TOO_YOUNG` | Under 30 days, or undateable | re-check when it is 30 days old | cancel it, at any reply rate |
| `INSUFFICIENT_DATA` | Under the 200-send floor | re-run next window | cancel it |
| `INSUFFICIENT_BOUNCE_SAMPLE` | Bounce elevated, under 30 classified bounces | sample more bounces, re-run | call it a list problem |
| `HEALTHY` | Reply ≥1%, bounce clean | nothing | over-optimize |
| `LIST_PROBLEM` | Recipients do not exist | list revalidation, then fix sourcing | blame the domain |
| `MIXED` | Sender share 25-50%, both diseases | fix auth first, then revalidate | pick only one half |
| `SENDER_AUTH` | SPF/DKIM/DMARC incomplete | DNS fix, re-diagnose in 7 days | cancel it, it is fixable |
| `BURNED` | Auth clean and still refused, or blocklisted | this skill's cancel path | fix DNS, it will not help |
| `COPY_PROBLEM` | Placement bad on ours AND on a control | copy rewrite, spam-word check, re-test | replace domains |
| `NOT_DELIVERABILITY` | Infrastructure fine, offer/targeting is not | campaign strategy, list quality | run more spam tests |
| `NEEDS_PLACEMENT_TEST` | Cannot decide without placement data | run the test | guess |
| `KEEP_BELOW_THRESHOLD` | Burned but nothing to replace it with | buy first, cancel next week | cancel into a shortfall |

## Promote / demote / buy

Applied after every domain has a verdict.

```
active_capacity    = sum over Active domains of (30/day x inbox count)     # 15/day for SMTP
insurance_capacity = same, over Insurance domains
goal               = daily send target
insurance_target   = 0.5 x goal

PROMOTE  while active_capacity < goal:
           take the OLDEST eligible Insurance domain (age is trust)
           eligible = not Warmup, age >= 30d OR warmed >= 14d, reputation >= 98%,
                      warmup not off, SMTP healthy
           if none eligible -> report the shortfall, do not relax the gates

DEMOTE   while active_capacity >= 1.25 x goal:
           take the WORST-performing Active domain above the keep line
           -> Insurance (warmup back on)

BUY      capacity_short = (goal + insurance_target) - (active + insurance capacity)
         if capacity_short > 0:
           inboxes = ceil(capacity_short / 30)
           domains = ceil(inboxes / inboxes_per_domain)
         report the ask in EMAILS/DAY, with the domain count as a footnote
```

New capacity is not usable for ~14 days of warmup, and not *judgeable* for 30. Buy a month ahead.
