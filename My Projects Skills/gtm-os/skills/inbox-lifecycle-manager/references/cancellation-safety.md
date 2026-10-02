# Cancellation safety

Cancelling inboxes is the only step in a cold email program that is both expensive to get wrong
and impossible to fully undo. This file is the procedure.

## The two-approval rule

Tag changes and provider cancellations are **different decisions with different blast radii** and
they get **separate approvals**.

| | Tag change (Active → Cancel) | Provider cancellation |
|---|---|---|
| Effect | stops the domain being attached to campaigns | ends the subscription, eventually deletes the mailbox |
| Reversible | instantly, from the snapshot | only while still *scheduled*; not after the period lapses |
| Billing | none | stops the charge |
| Default | this is what you do first | only after an explicit second yes |

Standing default: **tags only**, unless the human explicitly approves provider cancellation on
this run's plan. Ask the question in those words: *"Tags only, or also cancel at the provider?"*

Let the tag change sit for a few days first. A domain that is tagged `Cancel` is already costing
you nothing but the subscription, and the delay buys you a free window to notice a mistake.

## Before you fire a single cancel

1. **Snapshot.** Dump the current status of every domain in the batch to a dated file. Confirm the
   file is non-empty before proceeding — a zero-row snapshot means a broken query, not an empty
   fleet, and it is the difference between a five-minute rollback and a permanent loss.
2. **Enumerate.** Build an explicit list of domain IDs (or subscription IDs). Read it. Count it.
   Confirm the count matches the plan.
3. **Confirm ownership.** Verify each domain is actually yours to cancel, at the provider, in the
   account you think you are in.
4. **Check the revert path exists** — the specific endpoint, dashboard button, or support process
   that un-cancels. Find it *before* you cancel, not while you are panicking.

## The procedure

```
for each batch of ~10 domains:
    cancel the batch, one explicit ID at a time
    READ BACK the subscription state for every ID in the batch
    report: confirmed / unverified / needs-manual-check
    any "unverified" -> the batch is NOT done; it stays on the open list for a human
    only then proceed to the next batch
```

**Never report a cancel run as successful off the cancel responses alone.** A 200 means the
request was accepted, not that the subscription is gone. The readback is the evidence.

## The five ways this goes wrong

1. **Partial / pattern matching.** A cancel call that accepts a name fragment, prefix, or "cancel
   all matching" mode will match more than you meant. A real run intended 190 domains and
   scheduled full-subscription cancellation on 1,289 collateral ones. Pass explicit IDs, always.
2. **Blind retry.** An ambiguous or timed-out response is not a failure. Retrying it has cancelled
   *neighbouring* subscriptions on real provider APIs. Read state back, then decide.
3. **Counting "already cancelled" as an error.** A retry loop that treats an idempotent no-op as a
   failure will keep escalating and eventually do something destructive.
4. **Stale input file.** A cancel script that defaults its input CSV to some path from months ago
   will happily cancel a months-old list. Pass the input path explicitly, every run.
5. **Parallelism above the rate limit.** Firing ten cancels at once into a limit of twenty per
   minute produces 429s that look like failures, which triggers (2). Serialize cancels. They are
   not the slow part of your week.

If a provider's cancel API has ever over-cancelled on you, **stop using it**. Export a dated list
and cancel through the dashboard, or send it to the provider. A spreadsheet and ten minutes is
cheaper than a fleet.

## Rollback

| What | Window | How |
|---|---|---|
| Tag / status change | unlimited | restore from the snapshot |
| Scheduled provider removal | until the billing period lapses | the provider's revert endpoint or support; verify the state after |
| Lapsed subscription | gone | the mailbox and its warmed reputation are unrecoverable; the domain registration may still be yours |

Decide fast. The whole reversibility window is the days between "scheduled" and "lapsed".

## What never gets cancelled

- Any domain under 30 days old, at any reply rate
- Any domain under the 200-send floor for the window
- Any domain in warmup
- Any domain whose only problem is a fixable DNS/auth gap (`SENDER_AUTH`)
- Any domain whose bounces are majority recipient-side (that is a list problem)
- Half a domain — cancellation is whole-domain or not at all
- A healthy domain, to hit a spend target. Cut the goal instead, deliberately.
