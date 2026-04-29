# Mastering API Architecture — Complete Distillation

## 1. Source Identification
- **Title:** Mastering API Architecture: Design, Operate, and Evolve API-Based Systems
- **Authors:** James Gough, Daniel Bryant, Matthew Auburn (per O'Reilly publication)
- **Publisher:** O'Reilly Media
- **Pages:** ~229 OCR'd
- **Distilled in this repo:** 2026-04-29
- **Skills produced:** 3

## 2. Executive Summary

The book treats APIs as **first-class architectural artifacts** and provides a complete operational toolkit: design (API-First, ADRs, C4), evolution (fitness functions, Strangler Fig), edge (Gateway + Mesh with control/data plane), security (STRIDE, OAuth2 grants, Zero Trust), lifecycle (5 stages, deprecation), and observability (RED metrics, three pillars, correlation IDs). The book's value is the integrated discipline — most teams have 60% of these patterns; the rest is where outages live.

## 3. The Big Takeaways

1. **API-First.** Design the API as a contract before implementing.
2. **ADRs for every meaningful decision.** Status hygiene matters.
3. **Strangler Fig + Facade** is the canonical migration pattern.
4. **North-South at gateway; East-West at mesh.** Don't conflate.
5. **Control plane / data plane** for both gateway and mesh.
6. **Zero Trust internally.** mTLS + identity-based authz.
7. **STRIDE + DREAD** for threat modeling.
8. **Auth Code + PKCE for public clients; Auth Code for confidential.** Resource Owner Password is dead.
9. **OIDC over pure OAuth2** for human identity.
10. **JWT for local validation; opaque for revocability; hybrid possible.**
11. **One Live API version at a time.** 6-month minimum deprecation.
12. **Feature toggles separate deploy from release.**
13. **RED metrics + three pillars + correlation IDs** as observability baseline.
14. **Fitness functions in CI** prevent architectural rot.
15. **Sidecar / eBPF / proxyless** are three valid mesh implementations; pick by team capability.

## 4. Skills Derived

| Skill | When |
|---|---|
| [`api-design-and-evolution`](../../api-design-and-evolution/SKILL.md) | API-First design, ADRs, contracts, fitness functions, Strangler Fig, Facade/Adapter |
| [`api-gateway-and-service-mesh`](../../api-gateway-and-service-mesh/SKILL.md) | Edge architecture; gateway vs mesh; sidecar vs eBPF; Zero Trust |
| [`api-security-and-lifecycle`](../../api-security-and-lifecycle/SKILL.md) | STRIDE, OAuth2 grants, JWT, OIDC, lifecycle, observability |

## 5. Frameworks Index
See `frameworks.md`. 40+ frameworks covering: API-First, ADR, C4, CDC, Test Pyramid/Quadrant, Evolutionary Architecture, Fitness Functions, Strangler/Facade/Adapter, 6+ R's, API Gateway, Service Mesh, Control/Data Plane, Sidecar/eBPF/Proxyless, Zero Trust, STRIDE/DREAD, OAuth2 grants, PKCE, OIDC, JWT/JWS/JWE, API Lifecycle, Deprecation, Feature Toggles, Dark Launch, Canary, Three Pillars, RED, Correlation IDs.

## 6. Best Practices Index
See `additional-experts.md`. Topics: API design (API-First, OpenAPI, mocks, CDC), architecture documentation (C4, ADRs), migration (Strangler Fig + 6+ R's), edge architecture (gateway + mesh), security (STRIDE/DREAD/OAuth/JWT), lifecycle (5 stages, versioning, deprecation), observability (RED + three pillars), release management (toggles, dark launch, canary).

## 7. Decision Rules Consolidated

| Condition | Action |
|---|---|
| New API | API-First; OpenAPI spec; mock server; consumer interviews |
| Need to communicate architecture | C4 Container + Component diagrams |
| Architecturally significant decision | Write an ADR |
| Multiple consumers, evolving API | Consumer-Driven Contracts in CI |
| Test suite slow/flaky | Audit pyramid shape |
| Architecture rotting | Fitness functions in CI |
| Migrating legacy | Strangler Fig + Facade |
| Modernizing legacy backend | Adapter pattern |
| Cloud migration | 6+ R's per workload |
| External-facing APIs | API Gateway |
| 10+ services | Consider service mesh (Linkerd default) |
| Performance-sensitive mesh | eBPF (Cilium) |
| Polyglot services | Sidecar mesh |
| gRPC-only | Proxyless gRPC |
| New API security | STRIDE walkthrough at design |
| Public clients (SPA, mobile) | Auth Code + PKCE |
| Confidential clients (server) | Auth Code Grant |
| Service-to-service | Client Credentials |
| IoT / CLI | Device Authorization Grant |
| Need user identity | OIDC |
| Need local token validation | JWT (15-min expiry + refresh tokens) |
| Need revocation | Opaque tokens (or hybrid) |
| New API version | Beta → Live; predecessor goes Deprecated |
| Deprecating | 6+ months notice; Sunset header; migration guide |
| Risky change | Feature toggle + canary |
| New endpoint | Dark launch shadow before user access |
| Setting up observability | RED + three pillars + correlation IDs |
| Production error | Sanitized externally; verbose internally |

## 8. Anti-Patterns Consolidated

- API designed by implementers without consumer input
- "We'll document decisions later" (no ADRs)
- No CDC; producer hopes consumers don't break
- Inverted test pyramid (mostly E2E)
- Layered APIs across network boundaries
- Strangler without routing investment
- Big-bang cloud migration
- Fitness functions as one-off documents
- ADRs without status hygiene
- Service mesh as first move (premature)
- API gateway as application server (logic in plugins)
- Mesh on stateful services (DB connection pools)
- Trusting "inside" the network (Zero Trust violated)
- Sidecar without resource tuning (OOMs)
- Gateway without HA
- Resource Owner Password Grant in 2026
- JWT with no revocation strategy
- "We'll version when we need to"
- Toggle sprawl
- Logs without correlation IDs
- Verbose external errors
- Deprecating without sunset date
- Threat modeling as one-off

## 9. Worked Examples Pointer

| Example | Skill |
|---|---|
| Migrating monolith to API-First microservices | `api-design-and-evolution` |
| Adopting service mesh incrementally | `api-gateway-and-service-mesh` |
| Securing public B2B SaaS API | `api-security-and-lifecycle` |

## 10. Notable Content NOT in Skill Files

- **Specific gateway product comparisons** — vendor matrix; ages fast.
- **Detailed Istio configuration** — covered briefly; Istio docs are canonical.
- **Async API patterns** (AsyncAPI spec, event-driven APIs) — touched on; deeper coverage in event-driven specific resources.
- **Cloud-specific implementations** — examples in book; not skill-worthy.
- **GraphQL specifics** — REST/HTTP focus; GraphQL is mentioned but not central.

## 11. Redundancy with Existing Repo Coverage

| Topic | Existing | Relationship |
|---|---|---|
| Distributed system patterns | `distributed-system-patterns` | **Adjacent.** That skill is general; this is API-specific. |
| Architecture characteristics | `architecture-characteristics-and-tradeoffs` | **Adjacent.** Architecture-level; API skills go a layer down. |
| Modular software | `software-modularity-principles` | **Adjacent.** Modules + seams concepts shared. |
| Iterative engineering | `iterative-engineering-practices` | **Adjacent.** Feature toggles + dark launch overlap. |
| API gateway / mesh in DMS | `enterprise-data-integration-and-distribution` | **Different scope.** DMS focuses on data integration; this on API operations. |

**Net assessment:** No direct overlap. API skills add operational depth on top of architectural principles.

## 12. Recommended Reading Order

For a developer designing a new API:
1. `api-design-and-evolution` — API-First, ADRs, fitness functions
2. `additional-experts.md` mindset shifts + design best practices
3. `api-security-and-lifecycle` — STRIDE, OAuth, lifecycle
4. `api-gateway-and-service-mesh` — when system grows beyond a single service

For an architect designing a system's edge:
1. `api-gateway-and-service-mesh` first
2. `api-security-and-lifecycle` for security at edge
3. `api-design-and-evolution` for migration patterns

For a team adopting evolutionary architecture:
1. `api-design-and-evolution` (fitness functions, modules, seams)
2. `api-security-and-lifecycle` (toggles, dark launch, canary)
3. `additional-experts.md` for fitness function examples

## 13. When to Invoke Which Skill

| User intent | Skill |
|---|---|
| "Design an API" / "API-First" | `api-design-and-evolution` |
| "Strangler Fig migration" | `api-design-and-evolution` |
| "Fitness function" / "ADR template" | `api-design-and-evolution` |
| "API Gateway vs Service Mesh" | `api-gateway-and-service-mesh` |
| "Istio vs Linkerd" | `api-gateway-and-service-mesh` |
| "Sidecar vs eBPF" | `api-gateway-and-service-mesh` |
| "Zero Trust" | `api-gateway-and-service-mesh` |
| "OAuth flow selection" | `api-security-and-lifecycle` |
| "JWT vs opaque tokens" | `api-security-and-lifecycle` |
| "API deprecation policy" | `api-security-and-lifecycle` |
| "STRIDE threat model" | `api-security-and-lifecycle` |
| "Feature toggles" / "dark launch" | `api-security-and-lifecycle` |
| "RED metrics" / "observability" | `api-security-and-lifecycle` |

Source: *Mastering API Architecture* (O'Reilly), distilled 2026-04-29.
