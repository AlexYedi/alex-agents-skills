---
name: api-security-and-lifecycle
description: >
  Apply API security and lifecycle: STRIDE + DREAD threat modeling, OAuth2
  grants (Authorization Code, PKCE, Client Credentials, Device, deprecated
  Resource Owner Password), JWT/JWS/JWE, OpenID Connect, the API lifecycle
  (Planned → Beta → Live → Deprecated → Retired), versioning, observability
  (RED metrics, three pillars), feature toggles, dark launches. Use when
  designing API security, picking the right OAuth2 grant, threat-modeling
  an API, planning API versioning, defining deprecation policy, or setting
  up observability. Triggers: "OAuth2 flow selection", "PKCE", "JWT vs
  opaque token", "STRIDE threat model", "API deprecation policy",
  "RED metrics", "feature toggles", "dark launch". Produces a chosen
  security model + lifecycle policy.
---

# API Security and Lifecycle

You apply the security and lifecycle discipline from *Mastering API
Architecture*: threat model with STRIDE/DREAD, pick the right OAuth2 grant,
manage API evolution through a five-stage lifecycle, and observe with the
three pillars + RED metrics.

---

## When to Use This Skill

- Designing authentication / authorization for an API
- Picking the right OAuth2 grant for a specific client type
- Threat-modeling a new or existing API
- Planning API versioning + deprecation
- Setting up observability (metrics, logs, traces)
- Implementing feature toggles + dark launches for risk-managed releases

---

## Threat Modeling

### STRIDE

A categorization of threats — six categories. Walk each for every API surface:

| Category | Threat | Example |
|---|---|---|
| **S**poofing | Identity falsified | Attacker presents stolen JWT |
| **T**ampering | Data altered in transit / at rest | Modified request body bypasses validation |
| **R**epudiation | Action denied; no proof | User claims "I didn't do that"; no audit log |
| **I**nformation disclosure | Data leaked | Verbose errors expose internals; unindexed endpoint |
| **D**enial of service | Availability impaired | Floods, expensive queries |
| **E**levation of privilege | Gain unauthorized access | Auth bypass; SQL injection to admin |

For each API, list potential STRIDE threats and the mitigation.

### DREAD

Once threats are listed, prioritize via DREAD scoring (1-10 each):

- **D**amage potential
- **R**eproducibility (is the exploit reliable?)
- **E**xploitability (skill required?)
- **A**ffected users
- **D**iscoverability (how easy to find?)

Sum or average → priority. Address high-DREAD threats first.

**Caveat:** Both STRIDE and DREAD are heuristics, not guarantees. Use them as structured checklists, not theology.

---

## OAuth 2.0 Grants — Picking the Right One

```
   PUBLIC                          CONFIDENTIAL
   CLIENTS                         CLIENTS
   (no secret)                     (server-side, can keep secret)
   
   ▲                                    ▲
   │                                    │
   │ - SPAs                              │ - Server-rendered websites
   │ - Mobile apps                       │ - Backend services
   │ - IoT devices                       │
   │                                    │
   ▼                                    ▼
```

### Authorization Code Grant (Confidential clients)

```
[User] ──► [Client] ──► [Auth Server] ──► [User authenticates]
                                  │
                                  ▼
                            [Auth code returned to Client]
                                  │
                          [Client exchanges code +
                           client_secret for token]
                                  │
                                  ▼
                            [Access token + Refresh token]
```

**When:** Server-side web apps that can keep `client_secret` confidential.

### Authorization Code Grant + PKCE (Public clients)

PKCE = Proof Key for Code Exchange. Replaces the `client_secret` with a cryptographic challenge.

**When:** SPAs, mobile apps. **The default for public clients in modern OAuth.**

**Why PKCE:** Without PKCE, public clients are vulnerable to authorization-code interception attacks.

### Client Credentials Grant

```
[Service A] ──client_id + client_secret──► [Auth Server]
                                                  │
                                                  ▼
                                        [Access token]
```

**When:** Machine-to-machine. No user involved. Internal services authenticating to each other.

### Device Authorization Grant

```
[Device] ──► [Auth Server] ──► [User code displayed on device]

[User on phone] ──► [Auth Server] ──► [Enters code, authorizes]

[Device] ──polls──► [Auth Server] ──► [Token granted]
```

**When:** IoT, smart TVs, CLI tools without browser input.

### Resource Owner Password Credentials Grant (DEPRECATED)

User gives their password directly to the client. Client passes it to auth server.

**When:** Legacy migrations only. **Do not use for new development.** Direct password handling defeats most of OAuth's value.

### Implicit Grant (DEPRECATED)

Token returned directly in URL fragment. Was used for SPAs before PKCE.

**When:** Never, in 2026. Use Authorization Code + PKCE.

---

## JWT / JWS / JWE

```
JWT (JSON Web Token) = the format
   ├── JWS (JSON Web Signature) = signed but not encrypted (most common)
   └── JWE (JSON Web Encryption) = encrypted (rarer; required when payload is sensitive)
```

### Structure (JWS)

```
xxxxx.yyyyy.zzzzz
  │     │     │
  │     │     └── Signature
  │     └── Payload (claims, base64-encoded JSON)
  └── Header (alg, type, kid)
```

**Common claims:**
- `iss` — issuer
- `sub` — subject (user ID)
- `aud` — audience (which API is this for)
- `exp` — expiration
- `iat` — issued at
- `scope` — granted scopes (custom but de-facto standard)

### JWT vs Opaque Token

| Aspect | JWT | Opaque |
|---|---|---|
| Validation | Verify signature locally | Call auth server `/introspect` |
| Revocation | Hard (need a blocklist) | Easy (auth server forgets) |
| Latency | Low (local validation) | Higher (call to auth server) |
| Size | Larger (full payload) | Tiny (random string) |
| When | High-volume reads where latency matters | Lower volume; revocation important |

**Hybrid:** Many systems use opaque tokens externally, JWTs internally (issued by gateway after introspection).

---

## OpenID Connect (OIDC)

OAuth2 = authorization (delegating access).
OIDC = OAuth2 + identity layer. Adds:
- **ID Token** (JWT) — proves who the user is
- **UserInfo endpoint** — returns user profile
- **Standard claims** (`name`, `email`, `picture`, etc.)

**Use OIDC when:** You need to know *who the user is*, not just that they granted access.

**Most modern auth providers** (Auth0, Okta, Azure AD, Google) implement OIDC. Use it instead of pure OAuth2 for any human-identity use case.

---

## API Lifecycle (Five Stages)

```
PLANNED ──► BETA ──► LIVE ──► DEPRECATED ──► RETIRED
   │          │        │           │             │
"Design     "Public,   "Stable    "Still         "Removed
 visible,    breaking   contract;  available;     from
 gathering   changes    no         use migration  production"
 feedback"   allowed"   breaking   guide"
                        changes;
                        only one
                        Live at
                        a time"
```

### Stage details

| Stage | Allowed changes | Audience | Duration |
|---|---|---|---|
| Planned | Anything; design exercise | Internal stakeholders, prospective consumers | Days to weeks |
| Beta | Breaking changes allowed; producer reserves right | Early adopters; opt-in | Weeks to a few months |
| Live | Backward-compatible only | Production consumers | Months to years |
| Deprecated | No new development; migration guide published | Existing consumers (with notice) | Min 6 months recommended |
| Retired | Removed; 410 Gone or similar | None | Permanent |

**Key rule:** Only one Live version at a time. New Live versions move predecessors to Deprecated.

### Versioning

Two common approaches:

**URL-based:** `/v1/users`, `/v2/users` — simple, widely understood.
**Header-based:** `Accept: application/vnd.example.v2+json` — cleaner URLs, harder for tooling.

**Practical guidance:** URL-based. Discoverability and ease of debugging > URL aesthetics.

### Deprecation Policy

- **Notice:** 6 months minimum before retirement
- **Communication:** Email all known consumers; banner in API docs; `Deprecation:` and `Sunset:` HTTP headers
- **Migration guide:** Published; details every change
- **Telemetry:** Track usage of deprecated version; chase down stragglers
- **Hard cutoff:** Retire on the announced date; don't keep extending

---

## Separating Deployment from Release

```
DEPLOY: code reaches production
RELEASE: feature reaches users
```

The two should be independent. Deploy frequently; release strategically.

### Feature Toggles

```
if (featureFlag("new-checkout-flow", user)) {
  // new code path
} else {
  // existing code path
}
```

**Types:**
- **Release toggles** — short-lived; remove after rollout
- **Experiment toggles** — A/B testing
- **Ops toggles** — kill switches, circuit breakers
- **Permission toggles** — premium features

**Tools:** LaunchDarkly, Unleash, Split, GrowthBook, AWS AppConfig.

### Dark Launches

Deploy new code paths but don't expose them to users. Run in shadow mode (new + old in parallel; compare outputs). Validates the new path before customer impact.

### Canary Releases

Roll out to small % of users; monitor; ramp up if healthy. Service mesh weight-based routing makes this easy.

---

## Observability — Three Pillars + RED

### Three Pillars

| Pillar | What it captures | Granularity |
|---|---|---|
| **Metrics** | Aggregate counts, gauges, histograms | Per service, per minute |
| **Logs** | Discrete events with context | Per request |
| **Traces** | Request flow across services | Per request |

### RED (Rate, Errors, Duration)

For every API endpoint, measure:
- **R**ate — requests per second
- **E**rrors — error rate
- **D**uration — latency distribution (p50, p95, p99)

These three answer "is the API healthy?" most of the time.

### Correlation IDs

Inject a request ID at the gateway. Propagate through every internal call. Logs include it. Traces include it. Now you can trace a single user's request across the entire system.

```
Client request →  Gateway adds X-Request-ID: abc123
                  ↓
                  Service A logs include "request_id=abc123"
                  ↓
                  Service A calls Service B with X-Request-ID: abc123
                  ↓
                  Service B logs include "request_id=abc123"
                  ...
```

---

## Principles

- **Threat model every public API** with STRIDE + DREAD. Rinse and repeat.
- **Auth Code + PKCE for public clients; Auth Code for confidential.** Resource Owner Password is dead.
- **OIDC over OAuth2** for human-identity use cases.
- **JWT for low-latency local validation; opaque for revocability.** Or hybrid.
- **One Live version at a time.** New Live → predecessor goes Deprecated.
- **6-month minimum deprecation notice.**
- **Feature toggles separate deploy from release.**
- **RED metrics on every endpoint** are the bar for observability.
- **Correlation IDs propagated everywhere.** Without them, distributed debugging is archaeology.
- **TLS termination at gateway**; mTLS internally.

---

## Anti-Patterns

### Resource Owner Password Grant in 2026

**Looks like:** "Our mobile app passes user password to our API."

**Why it fails:** Defeats OAuth's purpose; password handled by client; high attack surface.

**The fix:** Authorization Code Grant + PKCE.

### JWT With No Revocation Strategy

**Looks like:** Long-lived JWTs (24h+). User logs out — token still valid. Stolen token is good for a day.

**Why it fails:** JWTs are bearer tokens; possession = access. Logout doesn't help.

**The fix:** Short-lived access tokens (15 min); refresh tokens (revocable). Or hybrid (opaque externally, JWT internally).

### "We'll Version When We Need To"

**Looks like:** Breaking change ships in production. Consumers break. Hotfix attempt makes it worse.

**Why it fails:** Versioning policy must be defined *before* needed.

**The fix:** From day 1, define versioning scheme + deprecation timeline. Even if you only have one version.

### Toggle Sprawl

**Looks like:** 200 feature flags. Some 2 years old. Nobody knows which are still relevant.

**Why it fails:** Code complexity proliferates. Each flag is a branch + risk.

**The fix:** Owner per flag. Lifecycle: Created → Released → Removed. Quarterly cleanup.

### Logs Without Correlation IDs

**Looks like:** "An error happened in service B at 14:32." No way to find related logs in service A or C.

**Why it fails:** Distributed debugging requires correlation.

**The fix:** Inject X-Request-ID at gateway; propagate everywhere; log structurally with the field.

### "Verbose Errors for Debugging"

**Looks like:** Production errors include stack traces, SQL details, internal endpoints.

**Why it fails:** Information disclosure (STRIDE I). Helps attackers map your system.

**The fix:** Log verbose internally; return sanitized errors externally. Map internal codes to external categories.

### Deprecating Without Sunset

**Looks like:** "v1 is deprecated" — no removal date. Five years later, half of consumers still on v1.

**Why it fails:** Without a deadline, consumers don't migrate.

**The fix:** Deprecation includes Sunset date (6+ months out). Communicate. Stick to it.

### Threat Modeling as One-Off

**Looks like:** STRIDE walkthrough at design time. Never revisited. Architecture changes invalidate it.

**Why it fails:** Threats evolve as the system does.

**The fix:** Revisit threat model at major releases or annually. Keep STRIDE table in repo as living doc.

---

## Decision Rules

| Situation | Action |
|---|---|
| Designing public API | STRIDE walkthrough at design time |
| Server-side web app needing OAuth | Authorization Code Grant |
| SPA / mobile app needing OAuth | Authorization Code + PKCE |
| Service-to-service auth | Client Credentials Grant |
| IoT / CLI tool needing user auth | Device Authorization Grant |
| Need to know who the user is | OIDC (not pure OAuth2) |
| Token must be locally validated | JWT (signed) |
| Token must be revocable | Opaque (introspect at auth server) |
| Both | Hybrid — opaque external, JWT internal |
| New API version needed | Plan: Beta → Live; mark predecessor Deprecated |
| Deprecating an API | 6+ months notice; Sunset header; migration guide |
| Risky change | Feature toggle + canary release |
| Setting up observability | RED metrics + three pillars + correlation IDs |
| Production error | Sanitized response externally; verbose log internally |
| Threat model freshness | Revisit annually or at major release |

---

## Worked Example: Securing a Public API for B2B SaaS

**Context:** B2B SaaS. Public REST API. Customers' developers integrate. Need: OAuth2, rate limiting, threat detection, RED observability.

**Choices:**

| Concern | Decision |
|---|---|
| OAuth2 grant for partner backends | Client Credentials Grant (server-to-server) |
| OAuth2 grant for partner web dashboards | Authorization Code + PKCE |
| Token format | JWT, 15-minute expiry; refresh token in opaque form |
| Identity claims | OIDC (`sub`, `email`, `org_id`) |
| API gateway | Kong with OIDC plugin + rate-limit + IP-allow plugins |
| Threat model | STRIDE walkthrough at design; quarterly review |
| Versioning | URL-based (/v1/, /v2/); 6-month deprecation policy |
| Feature toggles | Unleash (OSS); flags removed within 90 days of full rollout |
| Dark launch | New endpoints shipped behind toggle; shadow-mode validate before customer access |
| Observability | RED on every endpoint; correlation ID propagated; OpenTelemetry to Datadog |
| Logs | Structured JSON; sanitized errors externally; verbose internal |
| Audit | Every authentication + sensitive action logged with user, IP, timestamp |

**STRIDE table for `/v1/customers/{id}` GET:**

| Threat | Mitigation |
|---|---|
| Spoofing | OAuth2 + JWT validation at gateway |
| Tampering | TLS in transit; idempotent reads anyway |
| Repudiation | Audit log on every read |
| Information disclosure | Authorization check (org_id matches token's org); minimal response payload |
| Denial of service | Rate limit per token; cache layer |
| Elevation of privilege | Per-endpoint scope check; least-privilege defaults |

**Result:** API hardened from day 1. Threat model is a living document.

**Lesson:** Security + lifecycle discipline at the start is far cheaper than retrofitting. The cost of post-incident retrofit dwarfs design-time investment.

---

## Gotchas

- **JWT signature verification requires the public key.** Configure `kid` (key ID) in header; gateway fetches from JWKS endpoint. Cache aggressively.
- **PKCE doesn't replace OAuth2 secret in confidential clients.** Both secrets and PKCE for max safety, but PKCE alone is sufficient for public clients.
- **Refresh tokens are bearer tokens too.** They need same protection as access tokens. Revoke aggressively on logout.
- **OAuth2 ≠ OIDC.** OAuth2 grants access; OIDC adds user identity. They compose.
- **STRIDE is not exhaustive.** It's a checklist starter. Specific threats (e.g., race conditions, business logic flaws) need their own analysis.
- **Sunset headers are advisory.** Some clients ignore them. Combine with email + portal communication.
- **Feature toggle storage matters.** Flags in DB → ad hoc; flags in dedicated tool → audit trail + UX.
- **Distributed traces have a sampling cost.** 100% sampling at high traffic is expensive. Adaptive or tail-based sampling helps.
- **Correlation IDs need entry-point injection.** Without gateway-level injection, services can't trace requests they didn't originate.

---

## Further Reading

- *Mastering API Architecture* (Bernardez & Olejár), Chapters on Security, Lifecycle, Observability
- *OAuth 2.0 in Action* by Justin Richer & Antonio Sanso (Manning)
- *Threat Modeling: Designing for Security* by Adam Shostack
- OpenID Connect specification at openid.net
- See `api-design-and-evolution` for design principles + Strangler Fig
- See `api-gateway-and-service-mesh` for where security policies are enforced

Source: *Mastering API Architecture* (Bernardez & Olejár), Chapters on Security, Lifecycle, Observability.
