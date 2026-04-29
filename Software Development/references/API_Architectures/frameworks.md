# Mastering API Architecture — Frameworks Catalog

## Index

| Name | Domain |
|---|---|
| ADR (Architecture Decision Record) | Documentation |
| API-First | Design |
| API Gateway | Edge |
| API Lifecycle (5 stages) | Lifecycle |
| Authorization Code Grant | OAuth |
| Authorization Code + PKCE | OAuth |
| C4 Model Diagrams | Documentation |
| Canary Release | Release |
| Client Credentials Grant | OAuth |
| Consumer-Driven Contracts (CDC) | Testing |
| Control Plane / Data Plane | Edge |
| Dark Launch | Release |
| Device Authorization Grant | OAuth |
| DREAD | Security |
| eBPF (Sidecar-less mesh) | Mesh |
| Evolutionary Architecture | Architecture |
| Facade Pattern | Migration |
| Adapter Pattern | Migration |
| Feature Toggles | Release |
| Fitness Functions | Architecture |
| Full Proxy Model | Mesh |
| JWT / JWS / JWE | Auth |
| Layered APIs (anti-pattern) | Design |
| Modules | Design |
| North-South / East-West | Edge |
| OAuth 2.0 | Auth |
| OpenID Connect (OIDC) | Auth |
| PKCE (Proof Key for Code Exchange) | Auth |
| Proxyless gRPC | Mesh |
| RED Metrics (Rate, Errors, Duration) | Observability |
| Refactor / Re-architect | Migration |
| Replatform | Migration |
| Resource Owner Password Grant (deprecated) | Auth |
| Resource-Oriented Architecture (ROA) | Design |
| REST | Design |
| Retain / Revisit | Migration |
| Seams | Design |
| Service Mesh | Edge |
| Sidecar Proxy | Mesh |
| STRIDE | Security |
| Strangler Fig | Migration |
| Test Pyramid | Testing |
| Test Quadrant | Testing |
| Three Pillars (Metrics/Logs/Traces) | Observability |
| Zero Trust | Security |

## Detailed Catalog

### API-First
**Origin:** API design discipline; popularized by Bernardez & Olejár.
**Structure:** Design API as durable contract before implementation. OpenAPI/AsyncAPI spec → mock server → consumer feedback → implement.
**When:** Always for new APIs.

### C4 Model
**Origin:** Simon Brown.
**Structure:** Context → Container → Component → Code. Top-down zoom levels.
**When:** Architecture documentation; new-team onboarding.

### ADR (Architecture Decision Record)
**Origin:** Michael Nygard, 2011.
**Structure:** Markdown doc with Status, Context, Decision, Consequences.
**When:** Every architecturally significant decision.

### Consumer-Driven Contracts
**Origin:** Pact / Ian Robinson, 2010s.
**Structure:** Consumer specifies expected interactions; producer's CI verifies it satisfies them.
**When:** Multiple consumers, evolving API.

### Test Pyramid
**Origin:** Mike Cohn / Martin Fowler.
**Structure:** Base = many unit tests; middle = service tests; top = few E2E.
**When:** Always; balances cost and coverage.

### Test Quadrant
**Origin:** Brian Marick.
**Structure:** Business/Technology × Supporting/Critique grid.
**When:** Ensuring test portfolio covers all dimensions.

### Evolutionary Architecture
**Origin:** Ford, Parsons, Kua (*Building Evolutionary Architectures*).
**Structure:** Architecture continuously refactored toward fitness functions.
**When:** Long-lived systems.

### Fitness Functions
**Structure:** Quantifiable architectural quality metrics in CI.
**Examples:** Latency, dependency depth, code coverage, security scan.
**When:** Evolutionary architecture; preventing rot.

### Modules / Seams
**Structure:** Module = boundary hiding implementation. Seam = substitution point (DI, repository).
**When:** Designing testable, refactorable systems.

### Strangler Fig
**Origin:** Martin Fowler, 2004.
**Structure:** Wrap legacy; route new traffic to new components; shrink legacy.
**When:** Any nontrivial migration.

### Facade Pattern
**Structure:** Hide whether request is served by legacy or new.
**When:** Migration with consumer transparency.

### Adapter Pattern
**Structure:** Convert between modern (REST/JSON) and legacy (SOAP/XML).
**When:** Modernizing legacy backends incrementally.

### Cloud Migration Strategies (6+ R's)
**Strategies:** Rehost / Replatform / Refactor / Repurchase / Retire / Retain.
**When:** Cloud migration; pick per-workload.

### API Gateway
**Structure:** Single entry point; auth, rate limit, TLS, routing, aggregation, observability.
**When:** External-facing APIs; system edge.

### Service Mesh
**Structure:** Manages east-west traffic; mTLS, traffic policies, observability transparently.
**When:** 10+ services; cross-service complexity.

### Control Plane / Data Plane
**Structure:** Control = configuration brain; Data = request flow.
**When:** Both API gateways and meshes follow this split.

### North-South / East-West Traffic
**North-South:** External → system (ingress).
**East-West:** Service → service (internal).

### Sidecar Proxy
**Structure:** Companion proxy in same network namespace as app.
**When:** Polyglot environments; need consistent mesh behavior.

### eBPF / Sidecar-Less
**Structure:** Mesh logic in kernel via eBPF.
**When:** Performance-sensitive; modern Linux.

### Proxyless gRPC
**Structure:** Mesh logic in language-specific gRPC libraries.
**When:** gRPC-only environment; minimum latency.

### Zero Trust Architecture
**Structure:** "Trust no one, always verify"; mTLS + identity-based authz everywhere.
**When:** Modern security posture (default for new builds).

### STRIDE
**Origin:** Praerit Garg & Loren Kohnfelder, Microsoft.
**Categories:** Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
**When:** Threat modeling design phase.

### DREAD
**Origin:** Microsoft.
**Categories:** Damage, Reproducibility, Exploitability, Affected users, Discoverability.
**When:** Prioritizing identified threats.

### OAuth 2.0
**Origin:** RFC 6749.
**Grants:** Authorization Code, Auth Code + PKCE, Client Credentials, Device, (deprecated: Resource Owner Password, Implicit).
**When:** Delegated authorization.

### PKCE
**Origin:** RFC 7636.
**Structure:** Replaces `client_secret` with cryptographic challenge for public clients.
**When:** Default for SPAs and mobile apps with OAuth2.

### OpenID Connect (OIDC)
**Origin:** OpenID Foundation.
**Structure:** OAuth2 + identity layer; ID token (JWT), UserInfo endpoint.
**When:** Need to know who the user is, not just access grant.

### JWT / JWS / JWE
**Origin:** RFC 7519 + 7515 + 7516.
**Structure:** JWT = format; JWS = signed; JWE = encrypted.
**When:** Local validation; stateless tokens.

### API Lifecycle (5 Stages)
**Origin:** PayPal API standards adapted by Bernardez & Olejár.
**Stages:** Planned → Beta → Live → Deprecated → Retired.
**Rule:** Only one Live at a time.

### Versioning
**URL-based:** /v1/, /v2/ — preferred for discoverability.
**Header-based:** Accept: application/vnd.example.v2+json — cleaner URLs but harder tooling.

### Deprecation Policy
**Practice:** 6+ months notice; Sunset header; migration guide; usage telemetry; hard cutoff.

### Feature Toggles
**Types:** Release / Experiment / Ops / Permission.
**Tools:** LaunchDarkly, Unleash, Split, GrowthBook, AppConfig.

### Dark Launch
**Structure:** Deploy code; don't expose. Run shadow alongside old; compare.
**When:** High-risk changes; validation before user impact.

### Canary Release
**Structure:** Roll out to small % of users; ramp up.
**When:** Combined with mesh weight-based routing.

### Three Pillars (Observability)
**Metrics:** Aggregate counts (per service, per minute).
**Logs:** Discrete events with context (per request).
**Traces:** Request flow across services (per request).

### RED Metrics
**Origin:** Tom Wilkie / Weaveworks.
**Metrics:** Rate, Errors, Duration.
**When:** Per-endpoint observability baseline.

### Correlation IDs
**Practice:** Inject at gateway; propagate via headers; logs include them.

## Cross-Reference Map

```
                    API-FIRST (design philosophy)
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   DESIGN ARTIFACTS    EVOLUTION             MIGRATION
   - C4 Diagrams       - Evolutionary Arch    - Strangler Fig
   - ADRs              - Fitness Functions    - Facade
   - OpenAPI           - Modules / Seams       - Adapter
   - CDC                                      - 6+ R's

   EDGE ARCHITECTURE                         SECURITY
        │                                          │
   ┌────┴────────┐                          ┌─────┴────┐
   ▼            ▼                           ▼          ▼
   API        Service                   STRIDE        OAuth2
   Gateway     Mesh                     DREAD         + PKCE
   (north-     (east-                                  + OIDC
   south)      west)                    Zero Trust    JWT/JWE
   │           │                                         │
   │   Control / Data Plane                              │
   │   Sidecar / eBPF / Proxyless                        │
   │                                                       │
   └──────────────────────────────────────────────────────┘
                                                          │
                                                          ▼
                                                  LIFECYCLE
                                                  (5 stages)
                                                       │
                                                       ▼
                                                  RELEASE
                                                  - Feature Toggles
                                                  - Dark Launch
                                                  - Canary

                       OBSERVABILITY
                       - 3 Pillars
                       - RED Metrics
                       - Correlation IDs
```

Source: *Mastering API Architecture* (Bernardez, Olejár, et al.).
