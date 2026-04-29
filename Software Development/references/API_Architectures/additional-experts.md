# Mastering API Architecture — Additional Expert Notes

> Best practices from *Mastering API Architecture* (Bernardez, Olejár, et al., O'Reilly).

## About the Authors

A team from Container Solutions / Black Pepper. Voice: practitioner-grounded; comfortable with both architectural diagrams and Kubernetes YAML. Concrete examples; explicit ADR culture.

## Foundational Mindset Shifts

1. **API-First, not implementation-first.** Design APIs as durable contracts before any code.
2. **Architecture is a journey.** Evolutionary architecture + fitness functions; no fixed destination.
3. **North-south at gateway; east-west at mesh.** Don't conflate.
4. **Zero Trust internally.** Perimeter security is not enough.
5. **Deploy ≠ release.** Feature toggles + dark launches uncouple them.
6. **Threats evolve with architecture.** Re-threat-model at major changes.
7. **One Live API version at a time.** New Live → predecessor Deprecated.

## Best Practices by Topic

### API design
- API-First with OpenAPI / AsyncAPI spec
- Mock server before implementation
- Consumer interviews before design
- Generate stub code; consumers integrate against mocks
- Consumer-Driven Contracts (Pact) in CI

### Architecture documentation
- C4 Container + Component diagrams
- ADRs for every meaningful decision
- ADR template: Context, Decision, Consequences, Status
- Status hygiene: Proposed → Accepted → Deprecated → Superseded (link forward)

### Migration
- Strangler Fig with API gateway as the routing layer
- Facade for hiding migration from consumers
- Adapter for modernizing legacy protocols
- Cloud migration: pick strategy per workload (6+ R's)

### Edge architecture
- API Gateway for north-south: auth, rate limit, TLS termination, aggregation
- Service Mesh for east-west: mTLS, retries, traffic policies, observability
- Both have control plane / data plane split
- Sidecar for polyglot; eBPF for performance; proxyless gRPC for gRPC-only

### Security
- STRIDE threat modeling at design time
- DREAD prioritization
- Auth Code + PKCE for public clients (default)
- Auth Code Grant for confidential clients
- Client Credentials for service-to-service
- Device Grant for IoT / CLI
- OIDC for human identity
- Short-lived JWT (15 min) + refresh tokens
- Sanitized errors externally; verbose internally

### Lifecycle
- 5 stages: Planned → Beta → Live → Deprecated → Retired
- One Live at a time
- 6-month minimum deprecation notice
- Sunset header + email + portal communication
- URL-based versioning (/v1/, /v2/)

### Observability
- RED metrics on every endpoint
- Three pillars: metrics, logs, traces
- Correlation IDs injected at gateway, propagated everywhere
- OpenTelemetry as the wire format

### Release management
- Feature toggles separate deploy from release
- Dark launches validate new paths in shadow
- Canary releases via mesh weight-based routing
- Toggle lifecycle: Created → Released → Removed (90-day cleanup)

## Specific Advice with Rationale

### "API-First"
**Why:** APIs are public; implementations are private. Designing API last produces APIs that mirror DB schemas.
**Apply:** OpenAPI spec → mock → consumer feedback → implement.

### "Information hiding"
**Why:** Consumers depend on the contract. The implementation should be free to change.
**Apply:** API mirrors business semantics, not DB structure. Fields are domain concepts, not column names.

### "Fitness functions in CI"
**Why:** Architecture quality drifts without enforcement.
**Apply:** 3-5 to start (latency, coverage, dependency depth). CI fails if violated.

### "Consumer-Driven Contracts"
**Why:** Producer can't predict every consumer use. CDC tests catch it before deploy.
**Apply:** Pact contracts from each consumer. Producer CI runs them all.

### "Zero Trust internally"
**Why:** Internal compromise gives attackers free run if perimeter alone is the defense.
**Apply:** mTLS via mesh. Identity-based authz. Least privilege per service.

### "Auth Code + PKCE for public clients"
**Why:** Public clients can't keep secrets; PKCE replaces secret with cryptographic challenge.
**Apply:** Mobile apps, SPAs, CLI tools — Auth Code + PKCE. Implicit flow is dead.

### "Short-lived JWTs"
**Why:** JWT possession = access; revocation is hard. Short expiry limits exposure.
**Apply:** 15-minute access tokens; refresh tokens for renewal.

### "OIDC over pure OAuth2"
**Why:** OAuth2 grants access; OIDC tells you who. Most use cases need both.
**Apply:** Use OIDC-compliant providers (Auth0, Okta, Azure AD).

### "Strangler Fig for migrations"
**Why:** Big-bang migrations concentrate risk. Strangler enables incremental verification.
**Apply:** API gateway as routing layer; migrate piece by piece; shrink legacy.

## Worked Examples

### Migrating monolith to API-first microservices
See `api-design-and-evolution` skill.

### Adopting service mesh incrementally
See `api-gateway-and-service-mesh` skill.

### Securing a public B2B SaaS API
See `api-security-and-lifecycle` skill.

## Anti-Patterns Deeper Than Skill Files

- **Implementation-first APIs** — design mirrors DB schema; consumers struggle
- **ADRs as documentation theater** — written at design time; never updated
- **Layered APIs across network boundaries** — N hops per request; latency multiplied
- **Service mesh as first move** — Istio for 3 services; massive ops burden
- **Gateway as application server** — business logic in Lua plugins
- **Sidecar on stateful services** — DB connection pool wars
- **Trusting "inside the network"** — Zero Trust violation
- **JWT with no revocation strategy** — long-lived tokens; can't logout effectively
- **Resource Owner Password Grant** in 2026 — defeats OAuth's purpose
- **"We'll version when needed"** — surprise breaking changes in production
- **Toggle sprawl** — 200 flags; nobody knows which are live
- **Deprecating without sunset date** — APIs live forever
- **Verbose external errors** — information disclosure
- **STRIDE walkthrough as one-off** — threats evolve; the doc doesn't
- **Logs without correlation IDs** — distributed debugging is archaeology

## Process Wisdom

- ADR per decision; status hygiene; PR-reviewed
- Quarterly threat model review
- Weekly toggle cleanup pass (or 90-day automatic removal)
- Per-API: STRIDE table + RED dashboard + ADR list + OpenAPI spec — a "one-pager" surface
- Consumer comms before deprecation: email, portal banner, headers, slack channel
- Migration runbooks for retired APIs preserved for years (compliance)

## Career / Context Wisdom

- API architect role is rising at large enterprises
- Edge engineering (API gateway + mesh) is its own subspecialty
- Security at the API layer is a growing concern post-major-breaches
- Evolutionary architecture mindset is the durable contribution; specific tools change

Source: *Mastering API Architecture* (Bernardez, Olejár, et al., O'Reilly).
