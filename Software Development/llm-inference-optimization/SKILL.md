---
name: llm-inference-optimization
description: >
  Optimize LLM inference for production: latency, throughput, cost. Covers
  quantization, batching, KV cache optimization, speculative decoding, prompt
  caching, model parallelism, and decoupled prefill/decode. Use when latency is
  too high, when GPU costs are unsustainable, when scaling LLM workloads, or
  when deciding between hosted APIs and self-hosting. Triggers: "reduce LLM
  latency", "lower inference cost", "scale our LLM serving", "quantize the
  model", "speed up generation", "self-host vs API", "prompt caching for our
  app". Produces structured optimization plan covering applicable techniques
  and expected gains.
---

# LLM Inference Optimization

You optimize production LLM inference. Inference is where AI economics break or
hold — model size and serving strategy determine whether unit economics work.

This skill operationalizes Chip Huyen's inference optimization framework into
concrete decisions.

---

## When to Use This Skill

- Latency is too high (users abandon at p99 > 3s)
- GPU costs are unsustainable at current scale
- Throughput is the bottleneck preventing scaling
- Deciding between hosted APIs (OpenAI/Anthropic) and self-hosting
- Production deployment requires hitting specific latency/cost targets
- Multi-tenant serving needs to maximize GPU utilization

---

## The Two Inference Phases

LLM inference has two phases with different optimization profiles. Understanding
this is foundational.

| Phase | What happens | Bottleneck | Optimization target |
|---|---|---|---|
| **Prefill** | Process all input tokens in parallel | Compute-bound | Throughput |
| **Decode** | Generate output tokens one at a time | Memory-bandwidth-bound | Latency |

**Why this matters:** Prefill and decode have *different* optimal hardware and
strategies. Optimizing them together is suboptimal.

---

## Optimization Techniques

### Quantization (model size + memory)

| Method | When to use | Tradeoff |
|---|---|---|
| **PTQ** (Post-Training Quantization) | Already-trained model; want to reduce inference cost | Some quality loss; cheap to apply |
| **QAT** (Quantization-Aware Training) | New model; want minimal quality loss | Slower training; better quality preservation |
| **Quantization levels** | INT8 for most cases; INT4 for memory-constrained, with care | Lower precision = more quality loss |

**Default:** INT8 PTQ. Validate quality on your eval set; revert if degradation > acceptable threshold.

### Batching (throughput)

| Strategy | How it works | Best for |
|---|---|---|
| **Static batching** | Fixed batch size; wait until full | Predictable workloads, training |
| **Dynamic batching** | Process when window expires or threshold met | Mixed workload with bounded latency |
| **Continuous batching** | Returns completed requests immediately, fills slots with new ones | Production serving with mixed sequence lengths — best general-purpose choice |

**Default for production:** Continuous batching. Major frameworks (vLLM, TGI) implement it.

### KV Cache Optimization

The KV cache stores computed attention values for previously-generated tokens
to avoid recomputation. It's the main memory consumer during decode.

- **PagedAttention** (vLLM): Manages KV cache like virtual memory, reduces fragmentation
- **Flash Attention**: Reduces memory bandwidth via tile-based attention
- **KV cache compression**: Quantize the cache itself to INT8

### Prompt Caching

If multiple requests share a prefix (e.g., system prompt), cache it.

| Cache scope | Use when |
|---|---|
| **Per-session** | User conversation has stable system prompt |
| **Cross-session** | Many users share the same system prompt (your typical app) |
| **Anthropic prompt caching API** | Hosted; 5-min TTL; 90% discount on cached input |

**Default:** Cache the system prompt + persona/skill prompt. Cache reads cost ~10% of normal input.

### Speculative Decoding

Use a small "draft" model to propose tokens; verify with target model in parallel.

- **Best for:** When draft model can produce reasonable text most of the time (e.g., next token is often the obvious one)
- **Speedup:** Often 2-3x for general text; less for highly novel content
- **Setup cost:** Need both draft and target models loaded

### Inference with Reference

When output significantly overlaps with input (e.g., editing tasks, summaries),
copy spans from input rather than regenerating.

**Best for:** Code refactoring, summarization with citations, structured edits.

### Parallel Decoding

Generate multiple future tokens simultaneously. Methods: Lookahead, Medusa.

**Tradeoff:** More compute per step, fewer steps. Net throughput gain when verification is cheap.

### Decoupling Prefill and Decode

Run prefill on compute-optimized hardware, decode on memory-bandwidth-optimized hardware.

**Best for:** Large-scale production where you can dedicate hardware classes.

### Model Parallelism

Split a single model across multiple GPUs.

| Type | What it splits | Best for |
|---|---|---|
| **Tensor parallelism** | Splits weight matrices across GPUs | Large models that don't fit on one GPU |
| **Pipeline parallelism** | Splits layers across GPUs | Very large models; can interleave with batching |
| **Expert parallelism** (MoE) | Distributes experts across GPUs | Mixture-of-experts models |

---

## Optimization Decision Tree

```
What's the bottleneck?
├── Latency too high
│   ├── First token slow → optimize prefill (better hardware, larger batch)
│   ├── Per-token slow → smaller model, quantization, speculative decoding
│   └── Time to first token slow but generation fast → prompt caching
├── Throughput too low
│   ├── GPU underutilized → continuous batching
│   ├── KV cache fragmented → PagedAttention
│   └── Memory bandwidth saturated → quantization, KV cache compression
└── Cost too high
    ├── Many requests share prefix → prompt caching (huge win)
    ├── Hosted API costs > break-even → consider self-hosting
    └── Self-hosted GPU underutilized → continuous batching, multi-tenancy
```

---

## Self-Host vs API: Decision Matrix

| Factor | Favors Self-Hosting | Favors API |
|---|---|---|
| Volume | High, predictable | Low or unpredictable |
| Data privacy | Sensitive data, can't leave | Public or non-sensitive |
| Latency control | Need <100ms predictable | OK with 1-3s variability |
| Model flexibility | Need finetuning, customization | OK with what API offers |
| Operational overhead | Have ML ops capacity | Want to focus on product |
| Cost at scale | High volume, breakeven point passed | Low volume, API cheaper |

**Break-even guidance:** API costs scale linearly with usage. Self-hosting has
high fixed costs but flat marginal costs. Calculate your break-even volume
before deciding.

---

## Principles

- **Optimize the right phase.** Prefill is compute-bound; decode is memory-bandwidth-bound. Different optimizations for each.
- **Prompt caching is the highest-leverage optimization.** If many requests share a system prompt, caching gives 10x cost reduction with no quality impact.
- **Continuous batching > static batching for production.** Mixed workloads benefit dramatically.
- **Quantization is cheap; validate before relying on it.** PTQ is fast to apply but quality can degrade silently. Always re-eval after quantizing.
- **Measure first, optimize second.** Profile to find the actual bottleneck. Premature optimization wastes effort on the wrong problem.
- **Validate quality at every optimization step.** Each optimization has a quality cost. Compound costs can break the product silently.

---

## Anti-Patterns to Avoid

### Optimizing Without Profiling

**Looks like:** "We need to make it faster" → quantization → no measurable improvement.

**Why it fails:** You optimized the wrong thing. Real bottleneck might be retrieval, network, or single-thread code.

**The fix:** Profile first. Identify the actual bottleneck. Optimize that.

### Quantizing Without Re-Eval

**Looks like:** Quantize INT8 → ship → users complain about quality.

**Why it fails:** Quality degraded silently because eval wasn't re-run.

**The fix:** Every optimization step must include a re-eval gate.

### Self-Hosting Before Hitting Volume

**Looks like:** "We should self-host for control" at low volume → infra cost > API cost.

**Why it fails:** Self-hosting fixed costs (GPU rental, ML ops) only amortize at high volume.

**The fix:** Calculate break-even volume. Stay on API until you cross it.

### Skipping Prompt Caching

**Looks like:** Sending the same 5K-token system prompt with every request.

**Why it fails:** Paying full input rate for content that never changes. 10x cost vs cached.

**The fix:** Identify cacheable prefixes. Use Anthropic's prompt caching API or self-hosted equivalent.

---

## Decision Rules

| Condition | Action |
|---|---|
| Many requests share system prompt | Prompt caching (highest priority) |
| Mixed workload with bounded latency | Continuous batching |
| Memory pressure, fragmented KV cache | PagedAttention (vLLM) |
| Model doesn't fit on one GPU | Tensor parallelism |
| Output highly overlaps input | Inference with reference |
| Generation often picks obvious next token | Speculative decoding |
| Hosted API costs > break-even | Calculate self-host TCO |
| Sensitive data | Self-host, no API |

---

## Worked Example: Optimization Pass on a Customer Support Agent

**Baseline:** p99 latency 4.5s, $0.40/conversation, 50 conversations/sec capacity.

| Step | Optimization | Latency | Cost | Capacity |
|---|---|---|---|---|
| 0 | Baseline (vanilla serving, FP16) | 4.5s | $0.40 | 50/s |
| 1 | Prompt caching for system prompt | 3.2s | $0.18 | 50/s |
| 2 | Continuous batching (vLLM) | 2.5s | $0.15 | 200/s |
| 3 | INT8 quantization (validated quality) | 1.8s | $0.10 | 250/s |
| 4 | Speculative decoding with small draft model | 1.2s | $0.09 | 300/s |

**Lesson:** Each technique compounds. The biggest single wins were prompt
caching (cost) and continuous batching (capacity). Quantization is the lever
where most teams over-promise — validate quality after.

---

## Gotchas

- **Quantization quality cliff.** INT8 usually fine. INT4 sometimes catastrophic. Test before relying.
- **Continuous batching tail latency.** Good for throughput; can hurt p99 in some patterns. Profile both.
- **Prompt caching isn't free.** TTL is short (5 min for Anthropic); cache misses cost full input rate. Architect to maximize hit rate.
- **Speculative decoding reverse case.** When draft and target diverge often (creative writing), spec decoding is *slower* than vanilla.
- **Self-hosting hidden costs.** GPU rental is just one cost. Add: monitoring, ops, on-call, security, model versioning, model migration. Often 2-3x the GPU cost.

Source: *AI Engineering: Building Applications with Foundation Models* by Chip Huyen, Chapter 9 (Inference Optimization).
