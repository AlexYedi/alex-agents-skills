---
name: distributed-caching-patterns
description: >
  Apply distributed caching correctly - the four caching patterns
  (cache-aside, read-through, write-through, write-behind), TTL and
  staleness, key design, hash partitioning across cache nodes (Redis /
  memcached), and the HTTP / web caching layer (CDN, ETag, Cache-Control,
  Expires, browser/proxy/edge tiers). Use when introducing or tuning a cache,
  diagnosing stale-read or low-hit-rate issues, designing an HTTP caching
  policy, or choosing between application caching and web caching. Triggers -
  "cache-aside vs read-through", "write-through vs write-behind", "Redis vs
  memcached", "CDN", "ETag / Cache-Control", "cache invalidation",
  "cache hit rate", "stale reads from cache", "DAX". Produces a caching
  design with explicit pattern, key design, and invalidation policy.
---

# Distributed Caching Patterns

You design and tune the caching layer that protects services and databases
from heavy reads. Done right, caching is the single most cost-effective
scaling lever — Twitter spends ~3% of its infrastructure on caches at their
scale, and aims for ≥80% hit rates that meaningfully unburden the database.
Done wrong, caches produce stale reads, broken invalidations, and outages.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 6): the
two flavors of caching (application-level and web/HTTP), the four classic
patterns, and the operational realities of running a distributed cache.

---

## When to Use This Skill

- Adding a cache to relieve database load
- Diagnosing low cache hit rate or stale reads
- Choosing between cache-aside / read-through / write-through / write-behind
- Designing TTL and invalidation policy
- Configuring HTTP caching headers (ETag, Cache-Control, Expires)
- Choosing between Redis, memcached, and managed alternatives (DAX, ElastiCache)

---

## The Two Flavors of Caching

| | Application Cache | Web / HTTP Cache |
|---|---|---|
| Where | Server-side, between app and DB | Anywhere on the request path: browser, proxy, CDN, reverse proxy |
| Access | Explicit code reads/writes | Built into the HTTP protocol |
| Examples | Redis, memcached, ElastiCache, DAX | Browser cache, ISP proxy, CloudFront, Akamai, Fastly |
| Granularity | Anything keyed (DB row, computed result) | URLs (HTTP responses) |
| Control | Application defines all logic | HTTP headers govern behavior |

**They compose.** A high-traffic public API typically has both: CDN/edge cache
on the front, Redis behind the application servers.

---

## Application Cache: The Four Patterns

```
Cache-aside              Read-through              Write-through            Write-behind
─────────────            ────────────              ─────────────             ────────────
App → Cache?             App → Cache               App → Cache → DB         App → Cache
miss?                       (Cache fetches            (sync write)             (async write
App → DB                     from DB on miss)        ↓                          to DB later)
App writes Cache            App writes Cache → DB    response                  response
                                                                                ↓
                                                                                DB
```

### Cache-Aside (Most Common, Most Resilient)

```
                 ┌────────────┐
                 │    App     │
                 └─┬───────┬──┘
              miss │       │ hit
                   ▼       │
              ┌───────┐    │
              │ Cache │ ◄──┘
              └───┬───┘
                  │ miss
                  ▼
              ┌───────┐
              │  DB   │
              └───────┘
                  │
                  ▼
          (App writes value
           back to cache)
```

**Flow:**
1. App checks cache.
2. **Hit:** return cached value.
3. **Miss:** app queries DB, populates cache, returns value.

**Properties:**
- App owns all the logic.
- **Resilient to cache failure** — degraded performance, not failure. If cache
  is down, app falls through to DB.
- Easy to scale Redis/memcached because they have no application semantics.

**Default choice in massively scalable systems.**

### Read-Through

Cache fetches from DB transparently on miss via a provider hook.

```
App → Cache → (on miss, cache calls provider → DB) → return
```

- Cleaner app code; cache library handles miss path.
- **Hard dependency on cache** — if cache is down, app can't reach data.
- Examples: NCache, Hazelcast with cache loaders.

### Write-Through

Application writes to cache, which writes synchronously to DB.

- Cache and DB stay consistent.
- **Slow** — every write pays both caches' and DB's write cost.
- Useful when reads must always see latest writes (consistency over latency).

### Write-Behind / Write-Back

Application writes to cache; cache asynchronously writes to DB later.

- **Fast writes** — app sees only cache latency.
- **Risk:** crash before async flush loses data.
- Useful for write-heavy workloads where eventual durability is acceptable
  (counters, telemetry).

### Choice Matrix

| Workload | Pattern |
|---|---|
| Read-heavy, app code can handle misses, cache failures shouldn't fail requests | **Cache-aside** (default) |
| Read-heavy, want simpler app code, accept hard dependency | Read-through |
| Read-heavy with strict freshness, accept latency cost | Write-through |
| Write-heavy, can tolerate brief data loss on crash | Write-behind |

---

## TTL and Staleness

**TTL (time-to-live)** evicts cached entries after a fixed duration. The
question is always: "How stale can this data be without harming the user?"

| Data type | Typical TTL | Why |
|---|---|---|
| User profile | 5–60 min | Rarely changes; brief staleness fine |
| Product catalog | 15 min – hours | Inventory updates can lag |
| Pricing | 1–5 min | Closer to source of truth |
| Auth tokens | Until expiry | Short-lived by design |
| Real-time inventory | No cache, or sub-second | Requires accurate count |

**Stale data risk:** Cached value diverges from source of truth. A user
update doesn't appear until the TTL expires, or worse — a cached stock count
shows "in stock" when it's not.

**Mitigation strategies:**

| Strategy | When |
|---|---|
| **Short TTL** | Rarely-read data, where staleness window is acceptable |
| **Explicit invalidation on write** | App-controlled writes can purge or update cache atomically |
| **Versioned cache key** | Append a version (`user:42:v17`); update bumps version, old entries age out |
| **Cache-aside with no auto-population** | Caller decides when to cache |

**Cache invalidation is famously hard.** "There are only two hard things in
Computer Science: cache invalidation and naming things." — Phil Karlton.

---

## Hash Partitioning Across Cache Nodes

Redis Cluster and memcached distribute keys across N nodes via hashing.

```
key = "user:42:profile"
hash = hash_function(key)
node = hash mod N      ← which cache node holds this key
```

**Redis Cluster:** 16,384 hash slots; each node owns a range. Adding a node
redistributes a fraction of slots. Client uses `MOVED` redirects to follow
the data.

**Hash tags (Redis):** force keys into the same slot for cross-key operations.
`user:{42}:profile` and `user:{42}:orders` share a slot via the `{42}` tag —
both live on the same node, allowing multi-key operations.

**Consistent hashing** (used by memcached and Redis Cluster's slot model)
minimizes redistribution on resize: adding node N+1 reshuffles only ~1/(N+1)
of keys, not all of them. Plain modulo would reshuffle ~all keys on resize.

---

## Web / HTTP Caching

The HTTP protocol bakes caching into every layer of the request path.

```
┌────────────┐    ┌──────────┐    ┌──────────┐    ┌─────────────┐    ┌────────┐
│  Browser   │ →  │ Org/ISP  │ →  │   CDN    │ →  │  Reverse    │ →  │ Origin │
│   cache    │    │  proxy   │    │   edge   │    │   proxy     │    │ server │
└────────────┘    └──────────┘    └──────────┘    └─────────────┘    └────────┘
   private          shared          shared           shared              ←── HTTP
```

Each layer respects HTTP cache headers and stores responses for reuse.

### The HTTP Cache Headers That Matter

| Header | What it does |
|---|---|
| **`Cache-Control`** | The modern primary directive. Examples: `public, max-age=300` (cacheable by anyone, 5 min) or `private, no-cache` (only browser, must revalidate). |
| **`Expires`** | Absolute expiration time. Older than `Cache-Control`; Cache-Control wins when both present. |
| **`Last-Modified`** | Timestamp the resource last changed. Used with `If-Modified-Since` for conditional GET. |
| **`ETag`** | Opaque identifier for the response content. Used with `If-None-Match` for conditional GET. Server returns 304 Not Modified if unchanged. |
| **`Vary`** | Which request headers affect the response (e.g., `Vary: Accept-Encoding`). Critical for proxies — wrong Vary causes wrong-content delivery. |

### Conditional GETs: 304 Not Modified

```
Browser                                            Origin
  │                                                  │
  ├── GET /image.png ─────────────────────────────→  │
  │ ←──────────────  200 OK  ──────────────────────  │
  │                  ETag: "abc123"                  │
  │                  Cache-Control: max-age=300      │
  │                                                  │
  │  (300 seconds pass)                              │
  │                                                  │
  ├── GET /image.png ─────────────────────────────→  │
  │      If-None-Match: "abc123"                     │
  │ ←────────  304 Not Modified  ──────────────────  │
  │     (zero-byte body)                             │
```

The browser keeps the cached body; the server confirms it's still valid.
Avoids re-transferring the bytes.

### CDN Edge Caching

CDNs (CloudFront, Akamai, Fastly) cache content at edge POPs close to users.
For static assets, this turns "transcontinental round-trip" into "30-mile
round-trip." For HTML / dynamic content, you can cache parts via edge
includes or fragments.

**Don't cache things you shouldn't.** Set `Cache-Control: private, no-cache`
on personalized / authenticated responses. A misconfigured CDN serving one
user's account page to another is the canonical horror story.

### Public vs Private Cache

| `Cache-Control` value | Cacheable by |
|---|---|
| `public` | Browser, proxy, CDN — everyone |
| `private` | Browser only |
| `no-cache` | Cacheable but must revalidate every time |
| `no-store` | Never cache (sensitive data) |

---

## Principles

- **Cache data that is read frequently and changes rarely.** Inventory
  catalogs, contact data, event metadata.
- **Aim for ≥80% hit rate.** Below this, the cache isn't earning its
  complexity. Measure it.
- **Cache-aside is the default** for application caching. Most resilient
  to cache failure; simplest model.
- **Separate cache from source of truth.** The cache is derived; the DB
  is canonical. Never use the cache as the only place data lives unless
  you've designed for it.
- **TTL is a guess about staleness tolerance.** Tune based on real
  user experience.
- **Invalidate on write where possible.** Don't rely on TTL alone for
  data the user just changed.
- **Set appropriate `Cache-Control` on every response** — including
  `private, no-cache` on personalized content.
- **Use ETags for revalidation.** They make 304 responses cheap.
- **Front static assets with a CDN.** It's the cheapest wins-vs-effort
  trade in caching.

---

## Anti-Patterns

### Cache as Source of Truth

**Looks like:** "Just keep it in Redis, the DB is too slow." Then Redis
crashes. Data gone.

**Why it fails:** Caches are derived data. They evict, restart, fail.
Without a source of truth, data is lost.

**The fix:** DB is canonical. Cache is derived. If you genuinely need an
in-memory primary store, design for AOF persistence, replication, and
recovery — and treat it as a database, not a cache.

### Long TTL on Mutable Data

**Looks like:** 24-hour TTL on user profiles. User updates profile; sees
old version for 24 hours. Files support ticket.

**Why it fails:** TTL is a fallback; for user-mutated data, invalidate on
write.

**The fix:** TTL of minutes to an hour at most. Explicit invalidation
(or update-on-write) when the user changes the data.

### Forgotten `Cache-Control` Headers

**Looks like:** API returns user-personalized data with no `Cache-Control`.
Default proxy behavior caches it. Different users see other users' data.

**Why it fails:** Without explicit headers, proxies make assumptions. Some
cache by default, some don't.

**The fix:** Every response sets `Cache-Control` explicitly. Personalized
endpoints get `private, no-cache` (or `no-store` for sensitive data).

### Cache Stampede on Miss

**Looks like:** A popular cached value expires. 1,000 requests miss
simultaneously, all hit the DB. DB falls over.

**Why it fails:** TTL expiration creates a thundering herd.

**The fix:** "Locking" patterns — first miss gets a lock, others wait or
serve stale. Or stagger TTLs (jitter ±20%). Or use the `mutex` pattern
in Redis.

### Caching Authenticated User Data Publicly

**Looks like:** `GET /me` cached on the CDN with `public, max-age=300`.
User A's profile served to User B from the edge.

**Why it fails:** Personalized endpoints must be `private`.

**The fix:** `Cache-Control: private, no-cache` on any endpoint dependent
on auth.

### Write-Behind with No Crash Recovery

**Looks like:** Telemetry counters in Redis with write-behind to Postgres.
Redis crashes. 10 minutes of counter increments lost.

**Why it fails:** Write-behind buffers writes that haven't yet been persisted.

**The fix:** AOF (append-only file) persistence on Redis. Or shorter flush
interval. Or accept the loss explicitly.

### Stale ETags After a Bug Fix

**Looks like:** Deploy a fix to a CSS file. Old browser caches still serve
old CSS because the URL didn't change.

**Why it fails:** ETag changes only when content changes; URL-based
fingerprinting changes on rebuild.

**The fix:** Hash-fingerprint static asset filenames (`app.a8f3.css`).
Long `max-age` is then safe — new versions get new URLs.

---

## Decision Rules

| Situation | Action |
|---|---|
| Read-heavy, hot keys, DB saturating | Add Redis with cache-aside |
| Need transparent miss handling | Read-through (NCache, Hazelcast) |
| Strict freshness across reads | Write-through |
| Counter / telemetry workload | Write-behind (with AOF) |
| Static assets | CDN with hashed-fingerprint URLs and long TTL |
| Authenticated API responses | `Cache-Control: private, no-cache` |
| API responses that vary by Accept-Encoding | `Vary: Accept-Encoding` |
| Multiple servers, shared cache | Distributed cache (Redis Cluster) — not per-replica memory |
| One Redis isn't enough | Cluster mode with hash slots |
| Need cross-key transactions | Hash tags to co-locate, or accept that you can't |
| DynamoDB read costs spiking | DAX (DynamoDB Accelerator) |

---

## Worked Example: Caching for a SaaS Product API

**Context:** B2B SaaS, 100K users, 50 req/s peak, Postgres backend. Most
endpoints are read-heavy. P95 DB query latency is 80 ms; we want API P95
under 100 ms.

**Caching design:**

| Endpoint | Cache pattern | Key | TTL | Invalidation |
|---|---|---|---|---|
| `GET /products` (catalog) | Cache-aside (Redis) | `products:list:v{n}` | 1 hour | On product CRUD: bump version |
| `GET /products/:id` | Cache-aside | `product:{id}:v{n}` | 1 hour | Bump version on update |
| `GET /me` (user profile) | Cache-aside | `user:{id}:profile` | 5 min | Explicit `DEL` on update |
| `GET /static/*` | CDN (CloudFront) | URL-fingerprinted | 1 year | Filename hash changes on rebuild |
| `POST /orders` | No cache | n/a | n/a | Mutating; idempotency key only |

**Cache topology:**
- Redis Cluster with 3 master + 3 replica nodes (managed: ElastiCache).
- Cache-aside throughout app code.
- Hit rate target: 85%+ on `/products`, 70%+ on `/me`.

**Result:** Steady-state DB load drops to ~20% of pre-cache. P95 API latency
drops to ~40 ms (cache hits) / ~120 ms (misses).

**Failure modes monitored:**
- Cache hit rate (alert if drops below 70%).
- Cache eviction rate (signals memory pressure).
- DB query rate (signals cache stampede or invalidation bug).

---

## Gotchas

- **Cache invalidation is hard.** Plan for it; don't rely on TTL alone.
- **Stampedes on TTL expiration** can crash a DB. Jitter TTLs ±20%.
- **Hash-tag forcing in Redis** colocates keys but defeats sharding for
  those keys. Use sparingly.
- **`Vary` headers proliferate cache entries.** `Vary: Cookie` essentially
  defeats caching.
- **CDN cache-purge has propagation delay.** Even after a "purge", edge
  POPs can serve stale content for seconds to minutes.
- **AOF fsync trade-off in Redis** — `appendfsync everysec` is the typical
  middle ground; `always` is durable but slow.
- **DynamoDB DAX is per-table.** Useful only for high-read DynamoDB
  workloads; not a general cache.
- **Memcached has simpler semantics than Redis** — pure KV, no data types.
  Redis's data types (lists, sets, sorted sets, hashes) make it more
  versatile but also more complex.
- **Browser back/forward cache (bfcache)** holds whole pages including form
  state. `no-store` prevents this — disable only when necessary.

---

## Related Skills

- `scalability-foundations` — when to add a cache at all
- `load-balancing-and-app-services` — what fronts the cache
- `scalable-database-design-and-sharding` — what's behind the cache
- `eventual-consistency-mechanics` — staleness as a consistency model
- `frontend-dev` — browser-side caching, service workers
- `api-design-and-evolution` — designing APIs to be cache-friendly

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 6.
