---
name: api-gateway-and-service-mesh
description: >
  Pick and operate API Gateway (north-south traffic) vs Service Mesh
  (east-west traffic) — Control Plane / Data Plane architecture, sidecar
  proxy vs sidecar-less (eBPF) vs proxyless gRPC libraries, Zero Trust
  architecture, full-proxy model. Use when designing the edge of a system,
  choosing between Kong/Apigee/Tyk and Istio/Linkerd/Consul, deciding sidecar
  vs eBPF, or implementing zero trust between services. Triggers: "API
  Gateway vs Service Mesh", "north-south vs east-west", "Istio vs Linkerd",
  "sidecar vs eBPF", "control plane data plane", "Zero Trust", "API gateway
  selection". Produces a chosen edge + mesh architecture with rationale.
---

# API Gateway and Service Mesh

You apply Bernardez & Olejár's clear separation: **API Gateway handles
north-south traffic** (external → system) and **Service Mesh handles
east-west traffic** (service → service inside the system). Each has a
control plane / data plane architecture; choosing the right tools depends
on team capability and traffic profile.

---

## When to Use This Skill

- Designing the system's edge (the API gateway tier)
- Picking among API gateway products (Kong, Apigee, AWS API Gateway, Tyk, etc.)
- Deciding whether to adopt a service mesh (Istio, Linkerd, Consul, Cilium)
- Selecting sidecar vs sidecar-less (eBPF) implementation
- Implementing Zero Trust between internal services
- Capacity / latency planning for edge + mesh

---

## North-South vs East-West

```
                        ┌──── External clients ────┐
                        │  (browsers, mobile,       │
                        │   third-party APIs)       │
                        ▼
              ┌──────────────────────────┐
              │     API Gateway          │     ← North-South
              │   (north-south edge)     │       (ingress)
              └────────────┬─────────────┘
                           │
                           ▼
              ┌─────────────────────────────────┐
              │                                  │
              │   ┌────────┐    ┌────────┐      │
              │   │ Svc A  │◄──►│ Svc B  │      │  ← East-West
              │   │ (mesh) │    │ (mesh) │      │   (service-to-service)
              │   └────┬───┘    └────┬───┘      │
              │        │             │           │
              │        ▼             ▼           │
              │   ┌────────┐    ┌────────┐      │
              │   │ Svc C  │    │ Svc D  │      │
              │   │ (mesh) │    │ (mesh) │      │
              │   └────────┘    └────────┘      │
              │                                  │
              │   Service Mesh (east-west)       │
              └──────────────────────────────────┘
```

**API Gateway:** Single point of entry. Authenticates clients. Rate-limits. Translates protocols. Routes to backends.

**Service Mesh:** Manages internal service-to-service communication. Mutual TLS. Traffic policies. Observability for the internal mesh.

---

## Control Plane / Data Plane

```
[OPERATOR / DEVELOPER]
        │
        ▼
[CONTROL PLANE]  ◄── Where you configure routes, policies, certificates.
        │           Examples: Istiod (Istio), Linkerd control plane, Kong's Admin API
        │
        ▼
[DATA PLANE]    ◄── Where requests actually flow. Proxies/sidecars/handlers.
                    Examples: Envoy proxies, Linkerd2-proxy, Cilium eBPF
        │
        ▼
[ROUTED REQUEST → BACKEND SERVICE]
```

Both API gateways and service meshes follow this split. The control plane is the brain; the data plane is the muscle.

---

## API Gateway Responsibilities

| Concern | What it handles |
|---|---|
| **Authentication** | Validate API keys, JWTs, OAuth tokens |
| **Authorization** | Apply policies before backend hit |
| **Rate Limiting / Load Shedding** | Protect backends from overuse |
| **TLS Termination** | Decrypt at edge; backends use mTLS or plain HTTP internal |
| **Routing** | Path / header / version / weight-based |
| **Protocol Translation** | gRPC ↔ REST, SOAP ↔ REST, WebSocket bridging |
| **Aggregation** | Single response from multiple backends (composite/BFF style) |
| **Observability** | Top-line metrics, traces, logs at the edge |
| **Caching** | Response caching for cacheable endpoints |
| **Threat Detection** | WAF integration, IP allow/deny |

### API Gateway Selection

| Tool | Strengths | When |
|---|---|---|
| **Kong** | OSS + enterprise; plugin ecosystem; PostgreSQL/Cassandra-backed | OSS-leaning; Linux-native |
| **AWS API Gateway** | Native AWS integration; serverless | AWS-committed; small to mid scale |
| **Apigee** | Mature; enterprise-grade analytics; Google-owned | Enterprise; willing to pay |
| **Tyk** | OSS; Go-based; lightweight | Performance-sensitive; OSS-required |
| **Cloudflare Workers / Vercel** | Edge-deployed; serverless | Global edge; static + dynamic mixed |
| **Envoy + custom config** | Maximum flexibility | Mature SRE team; willing to build |

**Practical heuristic:** Prefer managed (AWS API Gateway, Apigee, Cloudflare) for small/mid teams. Self-hosted (Kong, Envoy) when control matters more than ops burden.

---

## Service Mesh Responsibilities

| Concern | What it handles |
|---|---|
| **mTLS between services** | Automatic, certificate-managed |
| **Traffic policies** | Retry, timeout, circuit breaker, load balancing |
| **Canary / Blue-green** | Weight-based routing for safe deploys |
| **Observability** | Per-call metrics, distributed traces, dependency graph |
| **Identity-based authorization** | "Service A may call Service B's read endpoints only" |
| **Failure injection** | Chaos testing in production |

### Service Mesh Selection

| Tool | Strengths | When |
|---|---|---|
| **Istio** | Most features; large community; complex | Mature platform team; need every feature |
| **Linkerd** | Simpler; Rust proxy; lower resource use | Want a service mesh; don't want Istio's complexity |
| **Consul** | Service discovery + mesh; HashiCorp ecosystem | Already using HashiCorp tooling |
| **Cilium** | eBPF-based (sidecar-less); Layer 3/4 + 7 | Want kernel-level performance; modern Linux |
| **AWS App Mesh** | Managed Envoy on AWS | AWS-committed; small teams |

**Practical heuristic:** Linkerd unless you specifically need Istio's features. eBPF (Cilium) for performance-sensitive deployments on modern Kubernetes.

---

## Implementation Patterns

### Sidecar Proxy (the original)

```
┌─── Pod ───┐              ┌─── Pod ───┐
│           │              │           │
│  App      │   ──TCP──►   │  App      │
│  ▲        │              │  ▲        │
│  │        │              │  │        │
│  ▼        │              │  ▼        │
│  Envoy    │              │  Envoy    │
│  (sidecar)│              │  (sidecar)│
└─────┬─────┘              └─────┬─────┘
      │                            │
      └────────► Mesh ◄─────────────┘
              network
              (mTLS)
```

**Pros:** Polyglot (works for any language). Battle-tested. Granular policies.
**Cons:** Latency (extra hop). Resource overhead (CPU/memory per pod). Complexity.

### Sidecar-Less (eBPF)

```
┌─── Pod ───┐              ┌─── Pod ───┐
│           │              │           │
│  App      │   ──────►    │  App      │
│           │              │           │
└───────────┘              └───────────┘
       ▲                          ▲
       │                          │
   ────┴────                  ────┴────
   eBPF in       Mesh policy    eBPF in
   kernel       enforcement      kernel
```

**Pros:** Kernel-level performance. No sidecar overhead.
**Cons:** Modern Linux only. eBPF tooling maturity. L7 capabilities still developing.

**Tools:** Cilium (mature). Recent Istio Ambient Mode (sidecar-less option).

### Proxyless gRPC

```
[App with gRPC library that includes mesh logic]
                ▲
                │ (control plane updates library config)
                │
         [Control Plane]
         (e.g., Google Traffic Director)
```

**Pros:** No proxy hop; minimal latency.
**Cons:** Language-specific (gRPC libraries only). Tighter coupling between app and mesh.

---

## Full Proxy vs Half Proxy

**Full proxy:** Two distinct network stacks (client-side + server-side). Full intercept and manipulation.

**Half proxy:** One network stack. Pass-through with limited manipulation.

**Most service meshes use full proxy.** Slower but more capable.

---

## Zero Trust Architecture

```
"Trust no one. Always verify."

Traditional perimeter:        Zero Trust:
─────────────────────         ──────────

[Untrusted internet]          [Untrusted internet]
        │                              │
   [Firewall]                          ▼
        │                     [Every service authenticates
        ▼                      every request, regardless
[Trusted internal              of source]
 network]                              │
        │                              ▼
   [Internal services           [mTLS + identity-based
   trust each other]             authorization at every hop]
```

**Implementation:**
- mTLS between all services (service mesh provides)
- Identity-based authz (service A's identity is verified, not its IP)
- Continuous validation, not "logged in once"
- Least privilege at every boundary

**Why it matters:** Traditional perimeter security assumes "inside is safe." Modern attacks compromise internal services; perimeter alone fails.

---

## Combining Gateway + Mesh

```
External  ──► API Gateway  ──►  Service Mesh  ◄──► Service Mesh
clients      (north-south)     (east-west)         (east-west)
                                    │
                                    ▼
                               [Backend services]
```

**Gateway responsibilities:** Edge auth, rate limit, TLS termination, external observability.
**Mesh responsibilities:** Internal mTLS, traffic policies, internal observability.

**Don't:** Try to make the gateway do east-west, or the mesh do north-south. They overlap but are tuned for different traffic.

---

## Principles

- **North-south at gateway; east-west at mesh.** Separate concerns.
- **Control plane / data plane split** is non-negotiable for both.
- **Aggregate at gateway; route at mesh.** Different aggregation makes sense at different tiers.
- **Zero Trust internally.** mTLS everywhere; identity-based authz.
- **Observability at both edges.** Gateway logs every external request; mesh tracks every internal call.
- **Edge logic stays minimal.** Gateway is the front door, not the application.
- **Mesh adoption is incremental.** Don't roll out org-wide on day 1.

---

## Anti-Patterns

### Service Mesh as First Move

**Looks like:** Adopting Istio before any actual east-west complexity exists. Three services. Massive operational burden.

**Why it fails:** Service meshes are operationally expensive. They earn their keep at scale.

**The fix:** Start without a mesh. Add when service count + cross-service complexity warrants (~10+ services typically).

### API Gateway as Application Server

**Looks like:** Business logic in gateway plugins. Custom Lua scripts in Kong doing complex transformations.

**Why it fails:** Gateway becomes hard to maintain. Logic far from owning service. Failures cross teams.

**The fix:** Edge logic only — auth, rate limit, basic transforms. Business logic in services.

### Mesh Everything Even Stateful Services

**Looks like:** Adding sidecar to a stateful database container. Latency spike. Connection pooling broken.

**Why it fails:** Sidecar proxy isn't designed for high-throughput DB connections. Stateful services have specific needs.

**The fix:** Mesh for stateless services; bypass for databases / caches / message brokers.

### Trusting "Inside" the Network

**Looks like:** Internal services bypass authn/authz because "they're trusted."

**Why it fails:** Internal compromise gives attacker free run.

**The fix:** Zero Trust. mTLS everywhere. Authenticate every request.

### Sidecar Without Pod-Level Resource Tuning

**Looks like:** Pods OOM-killed under load. Sidecar consuming 200MB per pod. Cluster bill triples.

**Why it fails:** Sidecars need their own CPU/memory budgets. Default sizing assumes idle.

**The fix:** Tune sidecar resource requests/limits. Profile under load. Or use sidecar-less (eBPF) if overhead is unacceptable.

### Gateway Without HA

**Looks like:** Single API gateway instance. Goes down → entire system inaccessible.

**Why it fails:** Gateway is the chokepoint. SPOF.

**The fix:** Multiple gateway instances behind a load balancer. Active-active. Health-checked.

---

## Decision Rules

| Situation | Action |
|---|---|
| New system, single edge concern | Start with API Gateway only; mesh comes later |
| 5-10 services, growing complexity | Consider service mesh (start with Linkerd) |
| 10+ services, mature platform team | Service mesh likely justified |
| Performance-critical mesh | eBPF (Cilium) over sidecar |
| Polyglot services | Sidecar (covers all languages) |
| gRPC-only environment | Consider proxyless gRPC |
| Edge auth + rate limiting | API Gateway |
| mTLS between services | Service Mesh provides automatically |
| External + internal traffic mixed | Both: gateway at edge, mesh inside |
| Stateful services | Bypass mesh (or use it minimally) |
| Picking gateway product | Managed (AWS, Apigee) for small teams; Kong/Envoy when control matters |
| Picking mesh product | Linkerd default; Istio if you need every feature; Cilium for performance |
| Edge logic creeping into gateway | Move to service; gateway stays thin |
| "We need gateway and mesh" | Probably yes if 5+ services + external clients |

---

## Worked Example: Adopting Mesh Incrementally on a Kubernetes Platform

**Context:** 25-engineer platform team. 30 services. Mixed languages (Go, Python, Node, Java). Currently no mesh. Pain: ad-hoc mTLS, inconsistent observability, hard to debug cross-service issues.

**Plan:**

| Phase | Action |
|---|---|
| Month 1 | Pilot Linkerd on 3 non-critical services. Verify resource overhead acceptable. |
| Month 2 | Roll out to 5 more services. Establish runbook for sidecar issues. |
| Month 3 | Adopt org-wide. Default new services to mesh-injected. |
| Month 4 | Migrate ad-hoc mTLS code to mesh-managed. Delete app-level cert handling. |
| Month 5 | Adopt traffic policies (retries, timeouts) for tier-1 services. |
| Month 6 | Add canary deployments via mesh weight-based routing. |

**Result:** Consistent mTLS. Distributed traces from edge → mesh → DB. Canary deploys are routine.

**Lesson:** Mesh adoption is a multi-month investment. Linkerd's simplicity made it possible without a dedicated platform team.

---

## Gotchas

- **Sidecar startup ordering:** App container can start before sidecar is ready, calling network → fail. Use `holdApplicationUntilProxyStarts` or equivalent.
- **mesh + database = trouble.** Long-lived DB connections + sidecar = connection pool fights. Annotate to bypass mesh on DB sidecars.
- **Istio CRDs proliferate.** Hundreds of YAML files for VirtualServices, DestinationRules, etc. Linkerd is much simpler.
- **eBPF requires Linux 5.x+** with specific kernel features. Verify cluster compatibility.
- **API gateway ≠ ingress controller.** Both sit at the edge but have different scopes. Some products bundle them; others don't.
- **Rate limit policies are tricky.** Per-IP, per-user, per-tenant — picking the right key is non-trivial.
- **Zero Trust without identity provider** is theatre. Mesh provides service identity; user identity needs OIDC at the edge.
- **Service mesh observability isn't free.** Per-call telemetry adds overhead. Sample at high traffic.

---

## Further Reading

- *Mastering API Architecture* by Bernardez & Olejár (O'Reilly), Chapters on Gateway and Mesh
- *Istio in Action* by Posta & Maloku — for Istio-specific deep dive
- Linkerd documentation — linkerd.io
- Cilium documentation — cilium.io for eBPF approach
- See `api-design-and-evolution` for API design principles
- See `api-security-and-lifecycle` for security at the edge

Source: *Mastering API Architecture* (Bernardez & Olejár), Chapters on Gateway and Mesh.
