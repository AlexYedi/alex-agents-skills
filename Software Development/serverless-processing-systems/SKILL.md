---
name: serverless-processing-systems
description: >
  Apply serverless / FaaS correctly - AWS Lambda and Google App Engine
  (Standard) lifecycle, cold-start dynamics, memory-as-CPU tuning, region
  burst limits and reserved concurrency, parameter studies for cost /
  performance optimization, and the trade-offs vs IaaS (vendor lock-in,
  observability, debugging). Use when designing for spiky / unpredictable
  load, deciding between Lambda / GAE / IaaS, sizing Lambda memory, or
  tuning GAE scheduler parameters. Triggers - "Lambda or EC2", "cold
  start", "Lambda memory tuning", "burst limit / reserved concurrency",
  "GAE scheduler parameters", "serverless vendor lock-in", "FaaS",
  "function-as-a-service", "parameter study". Produces a serverless
  workload design with explicit memory / concurrency / scheduling settings.
---

# Serverless Processing Systems

You design and tune serverless workloads. The pitch is compelling — pay per
request, auto-scale to zero, no servers to manage — and for genuinely bursty
or unpredictable load, the economics are unmatched. The catches are real:
cold starts, region-wide burst limits, vendor lock-in, and a parameter space
that's surprising to tune.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 8): the
GAE Standard scheduler model, the Lambda function lifecycle and memory
tuning, parameter studies for cost / performance optimization, and when
serverless is and isn't the right answer.

---

## When to Use This Skill

- Choosing between Lambda / GAE / Cloud Functions / Azure Functions / IaaS
- Sizing Lambda memory and reserved concurrency
- Tuning GAE Standard scheduler parameters
- Diagnosing serverless cost overruns or performance problems
- Designing for bursty workloads (event-driven, batch fan-out)
- Deciding when *not* to go serverless

---

## The Serverless Pitch (and What It Actually Costs)

```
   IaaS (EC2 / VM)                    Serverless (Lambda / GAE)
   ─────────────────                  ──────────────────────────
   ┌──────────────┐                   ┌──────────────────────┐
   │   Pay for    │                   │  Pay per invocation  │
   │  provisioned │                   │   + duration         │
   │  capacity    │                   │   + memory           │
   │  24/7        │                   │                      │
   ├──────────────┤                   ├──────────────────────┤
   │ Min cost = $ │                   │  Min cost = $0       │
   │ regardless   │                   │  (auto-scales to     │
   │ of usage     │                   │   zero)              │
   └──────────────┘                   └──────────────────────┘

   Best when:                          Best when:
   - Steady traffic                    - Bursty / unpredictable
   - Long-running processes            - 99% of time idle, 1% peak
   - Custom networking / drivers       - Event-driven (S3, SQS,
   - Need OS / kernel control            CloudWatch)
                                       - Workload fits FaaS model
```

**Costs serverless charges that IaaS doesn't:**
- Cold starts → P99 latency hit
- Vendor lock-in → cross-cloud portability lost
- Burst limits → throttling under spikes
- Observability complexity → distributed traces are essential
- Per-invocation overhead at high steady traffic → can be more expensive than EC2

---

## AWS Lambda

### The Function Lifecycle

```
┌────────────────────────────────────────────────────────────────────┐
│                       Function Lifecycle                            │
│                                                                     │
│  Cold start                                                         │
│  (no warm instance)                                                 │
│  ─────────────────                                                  │
│  1. Allocate µVM       ← Firecracker microVM                        │
│  2. Initialize runtime ← language runtime + libs                    │
│  3. Init function code ← top-of-file code; module imports;          │
│                          DB pool creation                           │
│  4. Invoke handler                                                  │
│                                                                     │
│  Warm invocation (instance frozen, then thawed)                     │
│  ──────────────                                                     │
│  1. Thaw frozen environment   ← ~ms                                 │
│  2. Invoke handler             ← straight to work                   │
│                                                                     │
│  Idle → Frozen                                                      │
│  ─────────────                                                      │
│  Lambda freezes idle environments to free resources.                │
│  Frozen environments can be thawed without re-initialization.       │
│                                                                     │
│  Eventually:                                                        │
│  Frozen → Reaped (instance discarded)                               │
└────────────────────────────────────────────────────────────────────┘
```

**Cold start latency by language (rough):**

| Runtime | Cold start |
|---|---|
| Node.js / Python | ~100–300 ms |
| Go / Rust | ~50–150 ms |
| Java | ~500 ms – 2 s (worst) |
| Container image | varies, often 500 ms – several s |

**Mitigation:**
- **Provisioned concurrency** — Lambda keeps N instances warm. Pay extra; cold
  starts disappear for those N.
- **Smaller deployment package** — fewer modules to load.
- **Lazy-load heavy libraries** — defer until first use, sometimes a wash.
- **Use a faster runtime** — switching Java to Go can drop P99 by 1+ second.

### Memory Allocation = CPU Allocation

The most important Lambda tuning knob.

```
Memory             vCPU              Cost / 100 ms
───────────        ───────────       ─────────────
128 MB             tiny share        cheapest
512 MB             small share
1024 MB            larger share
1769 MB            ≈ 1 vCPU          ← critical inflection
3008 MB            > 1 vCPU
10240 MB           ~6 vCPU           most expensive
```

**The non-obvious truth:** higher memory often *reduces* total cost. CPU-bound
function at 512 MB taking 4 seconds = 4 × cost-per-100ms-at-512MB. Same function
at 1769 MB might take 1 second = 1 × cost-per-100ms-at-1769MB. Compare per-
invocation totals, not per-millisecond rates.

**Rule:** measure across memory settings. AWS Lambda Power Tuning (open-source
tool) automates this.

### Burst Limits and Reserved Concurrency

Each AWS region has a **per-account burst limit** — the number of concurrent
Lambda executions allowed before throttling kicks in.

| Region | Initial burst | Sustained |
|---|---|---|
| us-east-1 | 3,000 | +500/min beyond burst |
| us-west-2, eu-west-1 | 3,000 | +500/min |
| eu-central-1, ap-northeast-1 | 1,000 | +500/min |
| smaller regions | 500 | +500/min |

**The trap:** one Lambda in your account can consume the entire burst limit
during a spike, starving every other Lambda.

**Reserved concurrency:** per-function cap that *also* reserves capacity from
the regional pool. Set it on functions that:
- Must always have headroom (latency-sensitive APIs)
- Should not exceed a limit (downstream DB can't take more)

**Throttling response:** HTTP 429 / `TooManyRequestsException`. Lambda's
guidance: retry with exponential backoff.

### Vendor Lock-In

Lambda code is small but tightly coupled to:
- Lambda's event source mappings (S3 events, DynamoDB streams, SQS, EventBridge)
- IAM execution roles
- AWS-specific SDKs in handlers
- `serverless.yml` / SAM / CDK deployment models

**Cross-cloud portability is largely myth.** Tools like Serverless Framework
abstract deployment, but performance / security / cold-start tuning is
platform-specific. Plan for lock-in or wrap providers behind a layer you own.

---

## Google App Engine Standard Environment

GAE Standard is more "managed app server" than "function execution." You
deploy an app, GAE provisions instances, and a scheduler routes requests.

### The Scheduler Knobs

```
┌────────────────────────────────────────────────────────────┐
│             GAE Standard Auto-Scaling Knobs                 │
│                                                              │
│  target_cpu_utilization          (range 0.5 – 0.95)         │
│      Scale up when avg CPU > this fraction                  │
│      Default 0.6                                             │
│                                                              │
│  max_concurrent_requests         (range 1 – 80)             │
│      Max requests one instance handles concurrently         │
│      Default 10                                              │
│                                                              │
│  target_throughput_utilization   (range 0.5 – 0.95)         │
│      Like CPU but for request throughput                    │
│      Default 0.6                                             │
│                                                              │
│  max-pending-latency             (e.g., 30 ms)              │
│      Max time a request waits in queue before forcing       │
│      a new instance                                          │
└────────────────────────────────────────────────────────────┘
```

### Parameter Study Methodology

Gorton's case study from the chapter:

| Config | CPU target | Max concurrent | Throughput | Cost |
|---|---|---|---|---|
| Default | 0.60 | 10 | baseline (100%) | baseline (100%) |
| `{CPU70, max35}` | 0.70 | 35 | 102% | **82%** |
| `{CPU80, max20}` | 0.80 | 20 | 98% | 89% |
| ... 12 configs total | | | | |

**The chosen config delivered 96% of default throughput at 55% of cost** by
running each instance harder before scaling, with higher concurrency per
instance.

**The methodology:**

1. **Pick parameters** — usually 2-3 of the most influential.
2. **Define ranges** — 3-4 values per parameter spanning realistic settings.
3. **Sweep configs** — load-test each combination with a representative
   workload.
4. **Measure** — throughput, P95/P99 latency, cost per million requests.
5. **Compare** — find the Pareto-optimal point for your goal (max throughput
   per $, or max throughput within latency SLA).

**This works for Lambda too** (memory × timeout × concurrency) and for
auto-scaling groups generally. It's a generic optimization technique
serverless makes especially valuable because the parameter space is small
and well-defined.

---

## When Serverless Wins (and Loses)

| Scenario | Serverless | IaaS |
|---|---|---|
| 99% idle, occasional spike | ✅ | ❌ pay 24/7 |
| Steady high traffic | ❌ per-invocation cost adds up | ✅ |
| Event-driven (S3, SQS, EventBridge) | ✅ native | ❌ build glue |
| <100 ms P99 SLA | ❌ cold starts | ✅ always-warm |
| GPU / specialized hardware | ❌ | ✅ |
| Long-running process (>15 min) | ❌ Lambda hard limit | ✅ |
| Cross-cloud portability required | ❌ | ✅ (with discipline) |
| Small team, no ops bandwidth | ✅ | ❌ |
| Data-heavy in-process state | ❌ stateless model | ✅ |
| Rapid iteration / prototyping | ✅ | ✅ both |

**Cloud bill shock is real.** Surveys cited in the book show 69% of
organizations overspend by ≥25%. One well-known case spent $500K on Azure
Functions before noticing.

---

## Principles

- **Use serverless when load is bursty and unpredictable**, especially with
  long idle periods.
- **For Lambda, tuning memory upward often reduces total cost.** Measure
  per-invocation totals, not per-ms rates.
- **Run a parameter study** before accepting defaults. Both Lambda
  (memory × timeout) and GAE (CPU target × concurrency) have non-obvious
  optima.
- **Set min instances / provisioned concurrency** for latency-sensitive
  paths. Cold starts are P99 killers.
- **Use reserved concurrency** to prevent one Lambda from starving others
  in a shared regional burst pool.
- **Plan for vendor lock-in.** Cross-cloud serverless portability is
  largely a myth; wrap provider APIs.
- **Monitor cost per invocation** like any other infrastructure metric.
  Cost overruns happen silently.
- **Keep functions small and focused.** Cold-start grows with deployment
  package size.

---

## Anti-Patterns

### Lambda for Steady High Traffic

**Looks like:** Public API at 500 req/s sustained, on Lambda.

**Why it fails:** At that volume, EC2 Auto Scaling Group is typically 30–60%
cheaper. Lambda economics shine on bursts; they're punitive on steady high
load.

**The fix:** Run a cost comparison vs ASG. Move to ASG if it's cheaper.

### Cold-Start-Sensitive Without Provisioned Concurrency

**Looks like:** P99 spikes to 2+ seconds during low-traffic periods. Customer
support tickets pile up.

**Why it fails:** Idle functions get reaped; first request after pays cold-
start cost.

**The fix:** Provisioned concurrency for the latency-sensitive functions, or
move to a runtime / language with cheaper cold starts.

### One Lambda Starving Others

**Looks like:** A new feature triggers high Lambda concurrency. Other
production Lambdas start throttling. Random 5xx errors.

**Why it fails:** All Lambdas in an account share a regional burst limit.

**The fix:** Reserved concurrency on critical Lambdas. Caps on the noisy ones.

### Default Memory Setting

**Looks like:** All Lambdas at 128 MB "to save money." CPU-bound functions
take 5× longer; total cost is higher than well-tuned 1769 MB.

**Why it fails:** Memory allocation is also CPU allocation.

**The fix:** AWS Lambda Power Tuning across each function. Pick the
cost-optimal memory.

### Default GAE Scheduler

**Looks like:** Default `{target_cpu=0.6, max_concurrent=10}`. Fleet runs at
20% utilization. Bill is 2× what it should be.

**Why it fails:** Default settings are conservative.

**The fix:** Parameter study. Higher CPU target + higher concurrency typically
saves 30-40% with minimal latency impact.

### Blind Trust in "Auto-Scale"

**Looks like:** Workload spikes 50× from norm. Lambda starts throttling.
Burst limit hit. Frontend errors.

**Why it fails:** Auto-scale ≠ unlimited. Burst limits are real.

**The fix:** Know your region's burst limit. Provisioned concurrency for
expected peaks. Backpressure / queueing for unexpected bursts.

### Cross-Cloud Without a Wrapper

**Looks like:** "We'll use Serverless Framework so we can move between AWS
and GCP." Deploy works on both. Performance and security tuning is platform-
specific. Migration is still a quarter of work.

**Why it fails:** The deployment is cross-cloud; the runtime characteristics
aren't.

**The fix:** Accept lock-in or wrap provider APIs (event sources, secrets,
storage) behind your own interface from day one.

---

## Decision Rules

| Situation | Action |
|---|---|
| Bursty event-driven workload (S3 → process → DB) | Lambda |
| Web app with 99% idle pattern | GAE Standard or Lambda + API Gateway |
| Steady high-throughput service | EC2 ASG with Auto Scaling |
| Long-running batch | EC2 / Batch (Lambda's 15-min cap) |
| GPU workload | EC2 / Sagemaker (Lambda has no GPU) |
| Need <100 ms P99 | Provisioned concurrency or move to always-on |
| Multi-tenant Lambda usage in one account | Reserved concurrency per critical function |
| Optimizing Lambda cost | AWS Lambda Power Tuning across memory settings |
| Optimizing GAE cost | Parameter study across CPU target × concurrency |
| Avoiding lock-in | Wrap provider APIs; accept lock-in is largely unavoidable for advanced tuning |

---

## Worked Example: Image Processing Pipeline on Lambda

**Context:** Users upload images to S3. We resize to 3 sizes, run a content-
moderation API, store metadata in DynamoDB. ~50K uploads/day, bursty (mornings
and evenings spike 5×).

**Design:**

| Component | Choice | Why |
|---|---|---|
| Trigger | S3 → Lambda (event source mapping) | Native, no glue |
| Function memory | 1769 MB (1 vCPU), tuned via Power Tuning | Image processing is CPU-bound; this is cost-optimal |
| Reserved concurrency | 50 | Caps DynamoDB write pressure; prevents starving other Lambdas |
| Provisioned concurrency | 5 | Enough to handle baseline without cold start |
| Timeout | 30 s | Per-image work is well under |
| DLQ | SQS DLQ for failed invocations | Manual retry / investigation |
| Observability | CloudWatch + X-Ray traces | P95 latency per stage |

**Cost / scale calculation:**

- 50K invocations/day × 1 GB-second avg ≈ 50K GB-s/day
- At ~$0.0000167/GB-s = ~$25/month for compute
- Provisioned concurrency (5 × 1.769 GB × 24h × 30d) ≈ $80/month
- Total: ~$105/month vs ~$200+/month for an EC2 m5.large ASG with similar
  burst headroom

**Failure modes monitored:**
- Throttling errors (`Throttles` metric).
- DLQ growth.
- P99 latency per Lambda (cold starts will spike this).
- DynamoDB write throttles (Lambda might over-call DDB).

---

## Gotchas

- **Lambda execution context reuse is real.** Top-of-file code runs once
  per cold start, not per invocation. Globals persist. Useful for
  connection reuse; dangerous for per-request state mistakes.
- **Connection pools in Lambda need care.** Connections may outlive your
  function execution. RDS Proxy / DynamoDB DAX recommended for high-fan-
  out databases.
- **Lambda VPC cold starts** were historically very slow; AWS fixed this
  ~2019, but it's still worth measuring.
- **Region's burst limit is shared across the account**, not just your
  team's functions. Coordinate.
- **GAE Standard runtimes are restricted** — Go, Java, Python, Node, PHP,
  .NET, Ruby. Need other languages? GAE Flexible (Docker on VM) or
  Cloud Run.
- **Cloud Run** is GCP's modern container-on-managed-instances offering;
  often a better fit than GAE Flexible.
- **Azure Functions has three hosting plans** — Consumption (most
  serverless), Premium (warmer), Dedicated (always-on). Pick deliberately.
- **Apache OpenWhisk and Serverless Framework** offer some portability
  but the gain is mostly deployment, not runtime.
- **Watch the bill.** Set per-function and per-account billing alarms.

---

## Related Skills

- `scalability-foundations` — when to scale at all
- `load-balancing-and-app-services` — alternative for steady traffic
- `asynchronous-messaging-patterns` — SQS / EventBridge as Lambda triggers
- `microservices-resilience-patterns` — patterns Lambda functions should
  apply downstream
- `evaluating-trade-offs` — Pareto-style parameter studies are the
  general technique

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 8. Yan
Cui's *Production-Ready Serverless* (Manning, 2018) and his blog at
theburningmonk.com are good companion deep-dives.
