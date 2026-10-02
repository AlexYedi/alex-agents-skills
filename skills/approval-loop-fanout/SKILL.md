---
name: approval-loop-fanout
description: Reusable pattern for generating per-item output across a large batch using parallel Claude Code Task sub-agents, with a human approval loop that tunes the prompt before full fan-out. Show 1 sample, collect edits, run 10, approve, run 10 more — stop when 2 consecutive rounds need zero edits, then scale to the whole list. Always uses the Task tool, never an external API key. Use when a task needs per-row, per-lead, per-file, or per-record generation at a scale where getting the prompt wrong is expensive. Worked example is cold-email personalization; the pattern applies to any batch generation. For what to write in a personalized email, see `personalization-engine` or `cold-email-personalization`.
---

# Approval-Loop Fan-Out

Generating output for hundreds of items has one dominant failure mode: you run the whole batch, then discover the prompt was subtly wrong. This skill is the antidote — a tuning loop that converges the prompt on small samples with human review, and only then fans out.

Two separable pieces:

1. **The approval loop** — how to converge a prompt on samples before spending the full batch.
2. **The fan-out** — how to parallelize with Claude Code Task sub-agents once the prompt is settled.

The worked example throughout is cold-email personalization (per-lead situation lines, value lines, CTAs), because that's where the pattern was built. It transfers directly to any per-item generation: classifying records, summarizing files, drafting replies, labeling a dataset, generating per-tenant config.

## Always Task tool — never an API key

This skill runs entirely inside Claude Code via the Task tool. No Anthropic SDK calls, no OpenAI calls. This is intentional:

- **No extra API spend.** Uses your Claude Code plan.
- **No key management.** Works out of the box.
- **Parallel by design.** Claude Code spawns multiple Task sub-agents in one message, letting 100 leads finish in the time it takes to personalize 10.

At very large scale (1,000+ leads), the tuned prompt can optionally be shipped to the Anthropic API for throughput. But TUNING and normal campaign runs (under 500 leads) always go through the Task tool.

## The approval loop (before full fan-out)

Don't personalize 500 leads and then discover the prompt is wrong. Loop first, then scale.

### Round 0 — Sample on 1 lead

1. Pick one lead from the batch with a rich `company_description`.
2. Show the user: "Here's the company description I'm working with. Based on this, what would you say to personalize?"
3. Display what YOU (Claude) would generate for `situation_line`, `value_line`, `cta_soft`.
4. Ask: "Does this feel right? Edit it, and I'll re-tune."

### Round 1-N — Batch of 10 with approval

1. Spawn one Task sub-agent with the current prompt + 10 leads.
2. Display all 10 results in a table:
   ```
   Lead                  | situation_line                          | value_line                    | cta_soft
   jane@acme.com         | You're building the only APM for Ruby.  | Our Ruby customers find ...   | Worth 10 min?
   john@otherco.com      | ...                                     | ...                           | ...
   ```
3. Ask: "Any edits? Point at the row number and say what's wrong."
4. If the user has edits, update the prompt (or add rules like "never use the word X") and re-run a new batch.
5. If the user has **zero edits for 2 consecutive rounds**, the prompt is locked. Scale to the full list.

### Scale — Full fan-out

Once locked:
- Split remaining leads into batches of 10-20.
- Launch 3-10 parallel Task sub-agents (one per variant × batch).
- Merge results by `lead_id`.

## When to use

- Any batch where per-item generated values are needed (beyond simple token substitution)
- When you have 50+ items and want generated output without writing each one by hand
- When an orchestration skill or command needs parallel per-item generation as a sub-step

## Don't use this for

- Small batches (<20 items) — just generate inline in the main conversation
- Static output (the same text for every item) — fan-out wastes tokens

## The pattern

### 1. Prepare the lead batch

Before fanning out, your lead batch should be a JSON array where each lead has:

```json
{
  "lead_id": "<stable identifier>",
  "first_name": "<str>",
  "last_name": "<str>",
  "email": "<str>",
  "company_name": "<str>",
  "company_domain": "<str>",
  "company_description": "<1-3 sentences about what the company does>",
  "title": "<str>",
  "linkedin_url": "<optional>",
  "enrichment_data": { ... any extra signals ... }
}
```

The richer the `company_description`, the better the personalization. If you only have company names, the output will be generic.

### 2. Define the output schema

Decide up front what fields each sub-agent must return. Example:

```json
{
  "lead_id": "<same id>",
  "situation_line": "<1 sentence — what you noticed about their company>",
  "value_line": "<1 sentence — connecting their situation to your offer>",
  "cta_soft": "<1 sentence — soft ask, e.g. 'worth a 15 min chat?'>"
}
```

Fewer fields = less that can go wrong. Default to 3 fields maximum per variant.

### 3. Split into variants (A/B/C)

If testing 3 copy variants, run 3 parallel sub-agents per company (or per batch). Each gets a different *angle* prompt:

- **Variant A**: Lead with a pain observation. "Noticed X on your site..."
- **Variant B**: Lead with a compliment + transition. "Your approach to Y is unique..."
- **Variant C**: Lead with a question. "How are you thinking about Z?"

This gives you 3x the data from one list — you can A/B/C test which angle resonates.

### 4. Batch size

- **Small batches are the right default: 10-20 leads per sub-agent.**
- Bigger batches = fewer agents = cheaper but worse quality (agent loses context)
- Smaller batches = more agents = higher quality but more context usage in parent

For 100 leads:
- 10 sub-agents × 10 leads = good quality
- 5 sub-agents × 20 leads = faster
- 2 sub-agents × 50 leads = quality drops

For 1000 leads:
- Consider running in rounds of 100 (to avoid hitting context limits in parent)
- Each round launches 10 sub-agents of 10 leads each

### 5. The sub-agent prompt template

Every personalization sub-agent gets a prompt of this shape:

```
You are personalizing cold email fields for N leads.

CONTEXT:
- We sell: <one sentence from client-profile.yaml>
- Our ICP: <one sentence>
- Our offer: <the CTA we're asking them to respond to>
- Tone: <casual | formal | peer-to-peer>

FIELDS TO GENERATE (per lead):
- situation_line: <definition + 1 good example + 1 bad example>
- value_line: <definition + 1 good example + 1 bad example>
- cta_soft: <definition + 1 good example + 1 bad example>

RULES:
1. Never fabricate facts. If the company description is thin, say something generic but not false.
2. Never use em dashes (—). Use periods or commas.
3. Never use the word "leverage", "synergy", "ecosystem".
4. Maximum length: <N words per field>.
5. If a lead is missing company_description, return "<fields cannot be generated — skip>"

LEADS:
<JSON array>

RETURN:
A JSON array with the same lead_ids and the personalization fields. Save to /tmp/personalization-<batch-id>.json and print "DONE" when complete.
```

### 6. Fan-out code pattern

Pseudocode for the orchestrator (runs in the main Claude Code conversation):

```
leads = load leads from JSON
batches = chunk leads into groups of 10-20

for each batch:
  for each variant in [A, B, C]:
    Task(
      description: "Personalize batch <i> variant <v>",
      subagent_type: "general-purpose",
      prompt: <template above with variant-specific angle>
    )

# All tasks run in parallel (multiple tool calls in one message)

Wait for all tasks to finish, then read /tmp/personalization-*.json and merge.
```

Or, launching all in a single message with multiple Task calls:

```
# Launch 3 parallel sub-agents for one batch (variants A, B, C)
Task(description: "batch-1-variant-A", ...)
Task(description: "batch-1-variant-B", ...)
Task(description: "batch-1-variant-C", ...)
```

### 7. Error handling

Sub-agents can:
- Return malformed JSON
- Skip leads (if data is too thin)
- Refuse to generate (if content feels risky)

The orchestrator should:
1. Validate every returned JSON matches the output schema
2. For missing lead_ids: retry once with a "strict mode" prompt that emphasizes no-skip
3. For leads that genuinely can't be personalized (missing description): mark as `personalization_status: "skipped"` and use static copy instead

Never ship personalization fields that contain the string "cannot be generated" or similar — filter these out before upload.

### 8. Merge and upload

After all sub-agents complete:

1. Read `/tmp/personalization-*.json` files
2. Merge by `lead_id`
3. Each lead now has:
   ```json
   {
     ...original lead fields,
     "variant_a": { "situation_line": "...", "value_line": "...", "cta_soft": "..." },
     "variant_b": { ... },
     "variant_c": { ... }
   }
   ```
4. When uploading to Smartlead/Instantly, map each field to a custom variable. Convention:
   - Smartlead: use `{{situation_line_a}}`, `{{value_line_a}}`, etc.
   - If running 3 A/B/C campaigns, upload variant_a fields to campaign A, variant_b to B, etc.

## Approval loop stop rule

The loop exits automatically when:
- The user gives **zero corrections for 2 consecutive rounds** of 10 leads, OR
- The user explicitly says "lock it, scale up"

On stop:
1. Save the final tuned prompt to `~/cold-email-ai-skills/profiles/<business-slug>/personalization-prompt.txt`
2. Save a `client-profile.yaml` metadata entry:
   ```yaml
   personalization_prompt:
     path: profiles/<slug>/personalization-prompt.txt
     variant_count: 3
     tuned_at: YYYY-MM-DD
     rounds_to_convergence: 3
   ```
3. Launch the parallel fan-out on the remaining leads.

If the user gives edits on round N+1 after 2 approved rounds, that's fine — the counter resets, and the loop continues.

## Quality checks

Before uploading, manually spot-check 5 random leads per variant. Common issues:
- **Repetition across leads** (sub-agent wrote the same line 10 times) → retry that batch with diversity instruction
- **Factually wrong claims** (company does X when they actually do Y) → strengthen "never fabricate" rule in prompt
- **Unnatural phrasing** (AI-speak like "I was intrigued by..." every time) → add forbidden-phrases list
- **Hedging / vagueness** ("Your company might be doing X...") → add rule "assert, don't hedge"

## References

- `references/prompt-template.md` — copy-pasteable prompt template for the sub-agent

## Related skills

- `experiment-design-kit` / `single-variable-experiments` — if you're tuning the prompt as a measured experiment rather than by eye
- `personalization-engine`, `cold-email-personalization` — what to write per item, once this pattern decides how to generate it at scale
- `karpathy-coder` — general discipline for keeping generated output reviewable

## Note on provenance

This pattern was built for cold-email personalization in a GTM pipeline, which is why the worked examples use leads and email variables. The loop-then-fan-out structure is the transferable part; swap in your own item type and output fields.
