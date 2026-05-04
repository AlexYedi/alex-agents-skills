---
name: data-mesh-domain-topologies
description: >
  Pick and operate the right Data Mesh domain topology — Fully Federated,
  Governed, Partially Federated, Hub-and-Spoke, Centralized, Source-Aligned,
  Consumer-Aligned, Coarse-Grained, or Value Chain-Aligned — and apply
  domain-driven data product principles (Golden Source, Common Driveway,
  data ownership rules). Use when scoping Data Mesh adoption, choosing a
  domain topology that fits the org, designing landing zones, defining what
  a "data product" means at the company, or reconciling Mesh principles
  with existing centralized infrastructure. Triggers: "Data Mesh adoption",
  "domain topology", "data product definition", "fully federated vs
  governed mesh", "hub-and-spoke for data", "domain landing zones", "data
  ownership at scale". Produces a chosen topology with rationale and a
  data product blueprint.
---

# Data Mesh and Domain Topologies (At Scale)

You apply Piethein Strengholt's *Data Management at Scale* taxonomy: Data Mesh
isn't a single architecture — it's a **family of domain topologies** with
different decentralization tradeoffs. You pick the topology that fits the
organization's current capability, not the textbook ideal.

---

## When to Use This Skill

- Scoping Data Mesh adoption at a large enterprise
- Choosing a domain topology that fits actual capability (not aspiration)
- Designing landing zones for data ingestion and consumption
- Defining what counts as a "data product" at this company
- Resolving disputes about data ownership across domains
- Migrating from a centralized data warehouse / lake toward Mesh

---

## The Core Concept: Data as a Product, Owned by a Domain

A **data product** is the smallest independently deployable unit. It bundles:
- The **data** itself (raw, curated, or aggregated)
- **Metadata** (schema, semantics, lineage, owner, SLAs, classifications)
- **Infrastructure** (storage, compute, governance hooks)
- **Code** (transformations, validators, serving APIs)

The domain owns it end-to-end. Other domains *consume* it via standardized interfaces.

**Three foundational rules:**

1. **Capture and modify only at the Golden Source.** The authoritative dataset for any concept lives in exactly one domain. Modifications happen there with the owner's approval. No exceptions.

2. **New data means new ownership.** A domain that derives new facts from another's data owns those new facts — not the original source.

3. **Don't distribute data you don't own.** If a downstream consumer wants data from a third domain, route them to the originating domain. Don't proxy.

---

## The Topology Spectrum

```
DECENTRALIZED                                                CENTRALIZED
─────────────                                                ───────────

Fully       Value-Chain    Partially    Source/     Hub-and-   Centralized
Federated   Aligned        Federated    Consumer-   Spoke      Domain
                                        Aligned                Topology
   ▲                                                              ▲
   │                                                              │
"True Mesh"                                                "Mesh in name only"
```

### 1. Fully Federated

```
Domain A ←──────→ Domain B
     ↑                ↑
     ↓                ↓
Domain C ←──────→ Domain D
```

**Mechanics:** No central orchestrator. Direct lines between domains. Each domain is autonomous end-to-end.

**When:** Mature platform engineering. Domain teams have data engineering capability. Clear, stable domain boundaries.

**Failure mode:** "Decentralized chaos." Without strong governance + self-serve platform, this becomes N point-to-point integrations with inconsistent semantics.

### 2. Governed Domain

```
Domain A ──┐                  ┌── Domain D
           ├──► Distribution ◄┤
Domain B ──┤      Layer       ├── Domain E
           │  (centrally       │
Domain C ──┘    managed)       └── Domain F
```

**Mechanics:** Domains own their products, but the **distribution layer is centrally managed**. Cross-domain access flows through the central layer with consistent contracts.

**When:** Hybrid approach. Domain ownership exists but enterprise governance is non-negotiable (compliance, security, audit).

**Why it's common:** Most large organizations land here, even when they say "Data Mesh."

### 3. Partially Federated

```
Domain A ──► Central Engineering Team ──► Domain B
              (owns data plumbing for
               domains lacking skill)
```

**Mechanics:** Some domains own their data; others hand it to a central team that operates the pipelines.

**When:** Organizations transitioning toward Mesh. Mature domains operate autonomously; less mature ones are supported by central.

**Tension:** Central team can become bottleneck for the "not yet ready" domains. Plan transitions to autonomy.

### 4. Hub-and-Spoke

```
                    [Hub]
                   ╱  │  ╲
                  ╱   │   ╲
            Domain A  │   Domain C
                      │
                  Domain B
```

**Mechanics:** Central hub mediates all data movement. Domains don't talk to each other directly.

**When:** Strict governance / audit requirements. Visibility over every data movement is non-negotiable. Banking, healthcare, government.

**Tradeoff:** Hub becomes a chokepoint. Operational excellence of the hub determines org velocity.

### 5. Source-Aligned

```
Source-side                           Consumer-side
(centralized)                          (federated)

[Source A] ─►                                 ┌── Consumer Domain X
[Source B] ─► Central Source-Aligned Layer ──┼── Consumer Domain Y
[Source C] ─►                                 └── Consumer Domain Z
```

**Mechanics:** Centralization on the source side; federation on the consumer side. Consumers freely build on top of normalized source data.

**When:** Sources are heterogeneous (legacy systems, vendor SaaS) but consumers can self-serve.

### 6. Consumer-Aligned

```
Source-side                           Consumer-side
(federated)                           (centralized)

Domain A ─►                                  ┌── Consumer A
Domain B ─► Central Consumer-Aligned Layer ──┼── Consumer B
Domain C ─►                                  └── Consumer C
```

**Mechanics:** Reverse of source-aligned. Sources are autonomous; central layer harmonizes for consumers.

**When:** Many consumers asking "give me the joined-up view." A central serving layer reduces consumer-side complexity.

### 7. Centralized Domain Topology

```
                    [Single Domain-Oriented
                     Data Platform]
                            ↑
              ┌─────────────┼─────────────┐
              │             │             │
          Domain A      Domain B      Domain C
        (uses central) (uses central) (uses central)
```

**Mechanics:** One platform, multiple teams operating their slice. Domain-oriented in *organization*, centralized in *infrastructure*.

**When:** Smaller orgs that want Mesh-like ownership without infrastructure complexity. Cost optimization through shared compute. MDM is easier centralized.

### 8. Coarse-Grained Domain Topology

```
[Big Domain "Sales & Marketing"]
   ├── Sub-team X
   ├── Sub-team Y
   └── Sub-team Z

[Big Domain "Finance & Operations"]
   ├── Sub-team P
   ├── Sub-team Q
```

**Mechanics:** Domains aligned to large business units (Sales, Finance, Ops) instead of fine-grained.

**When:** Org has large teams that share data heavily; pure fine-grained would create endless boundary disputes.

**Tradeoff:** Looser ownership. Sub-teams within a coarse domain may duplicate effort.

### 9. Value Chain-Aligned

```
Source ──► Operational ──► Analytical ──► Operational ──► Source
            Domain         Domain          Domain
              ↑              ↑               ↑
              └──────────────┴───────────────┘
              Stream-aligned: same team owns the
              entire end-to-end value chain slice
```

**Mechanics:** Domains span the full lifecycle of a value chain — operational and analytical concerns owned together.

**When:** "Stream-aligned teams" in Team Topologies sense. End-to-end ownership outweighs technology specialization.

---

## Landing Zone Patterns

A landing zone is the **infrastructure boundary** for data — the physical or logical container in which a domain's data products live.

### Single Data Landing Zone

One management zone, one data zone. Maximum control, minimum complexity.
**When:** Small to mid-size orgs. Single regulatory regime.

### Source- and Consumer-Aligned Landing Zones

Two zones, segregated by purpose:
- **Source zone:** complex onboarding (CDC connectors, schema management)
- **Consumer zone:** optimized for consumption (ML, analytics)

**When:** Heterogeneous sources need different handling than consumption workloads.

### Multiple Data Landing Zones

Separate zones by geography, risk profile, trust level, or cost. Linked via a central management zone.

**When:** Large enterprises with regulatory boundaries (EU vs US data); separate trust domains; cost segregation.

### Multiple Data Management Landing Zones

Multiple management zones — for organizations with conflicting data management policies (regulated subsidiary + non-regulated parent, for example).

---

## The "Common Driveway" Pattern

Standardize the **endpoints** for inter-domain data sharing without forcing a single integration style.

```
Domain A's choice           Common Driveway          Domain B's choice
of integration                 (standard               of integration
style:                          endpoints)              style:

  REST API ──────────────►                ◄────────── Event Stream
  Event Stream ──────────►                ◄────────── REST API
  CSV dump ──────────────►                ◄────────── SQL view
                              All exposed
                              via the same
                              metadata catalog
```

The "driveway" is the **catalog + standardized contract format**. Domains implement the underlying integration however they like, as long as they expose it through the standard registration.

---

## Principles

- **Avoid data silos AND avoid integration hubs.** Both produce tight coupling and inconsistent transformations. The Mesh's goal is *neither*.
- **Capture once, modify only at the Golden Source.** No exceptions for "convenience."
- **New facts → new ownership.** Derived data has its own owner; not the source's.
- **Self-serve platform is the lever.** Without a real platform, decentralization is chaos. Most Mesh failures are platform underinvestment.
- **Federated governance > centralized governance.** Automated policy enforcement at the data product level beats committee approvals.
- **Domain teams must want this.** Imposed Mesh fails. The transition requires buy-in from domain leaders.
- **Ubiquitous language per domain.** Each domain speaks its own DDD bounded context. Translation happens at boundaries.
- **Topologies evolve.** Most orgs start centralized, grow toward governed, and only some reach fully federated. That's healthy.

---

## Anti-Patterns

### Mesh Without Platform

**Looks like:** Renaming the central data team "Platform team", calling existing teams "domains", declaring victory.

**Why it fails:** No new self-serve infrastructure. Domains end up rebuilding the same plumbing. Worse than centralized.

**The fix:** Real platform engineering investment. Self-serve catalog, infrastructure templates, automated governance. Mesh starts at the platform.

### Premature Full Federation

**Looks like:** Org adopts "Fully Federated Mesh" because it's the canonical version. Domains aren't ready. Chaos.

**Why it fails:** Skipping the maturity ladder. Few domains have the data engineering capability for full autonomy.

**The fix:** Start at Governed or Partially Federated. Migrate domains to autonomy as they mature.

### Domain Boundaries Drawn by Org Chart

**Looks like:** Each VP gets a "domain." Boundaries follow politics, not data semantics.

**Why it fails:** Domain models don't match business reality. Cross-domain joins become endless reconciliation.

**The fix:** Domain Driven Design (DDD) workshops to map bounded contexts. Boundaries follow ubiquitous language, not org chart.

### Distribution Layer as De Facto Centralized DW

**Looks like:** "Governed Mesh" with a central distribution layer — but the layer becomes where all data ends up modeled. Domains only "produce" raw data.

**Why it fails:** It's just a centralized DW with extra steps. No domain ownership in practice.

**The fix:** Distribution layer enforces contracts only. Modeling stays in domains.

### Allowing Cross-Domain Modifications

**Looks like:** "Domain B can update Domain A's customer record because we needed to fix a typo."

**Why it fails:** Golden Source rule violated. Inconsistency cascades. Trust collapses.

**The fix:** Read-only access cross-domain. Modifications require routing back to the source domain.

### Hiding Data Products Behind Bureaucracy

**Looks like:** Strict governance committee gates every new data product. Approvals take months.

**Why it fails:** Defeats the speed advantage of Mesh.

**The fix:** Federated governance via automated policy enforcement. Domain teams can self-publish products that comply with declarative policies.

### Coarse-Grained as Compromise

**Looks like:** "We can't agree on fine-grained domains, so we'll go coarse-grained."

**Why it fails:** Coarse-grained is its own architectural choice with tradeoffs. Using it as a compromise produces all the problems of both fine and coarse.

**The fix:** Make coarse-grained a deliberate choice driven by team structure (Team Topologies), not by inability to agree.

---

## Decision Rules

| Situation | Topology |
|---|---|
| Greenfield, < 50 engineers | Centralized Domain. Don't pretend Mesh. |
| 50-100 engineers, multiple business units | Governed Domain Topology. Central distribution + domain ownership. |
| 100+ engineers, strong domain boundaries, mature platform engineering | Plan toward Fully Federated. Stop at Governed if platform isn't ready. |
| Strict regulatory / audit requirement | Hub-and-Spoke. Visibility over every movement. |
| Heterogeneous legacy sources + analytical consumers | Source-Aligned (centralized source layer). |
| Many consumers asking for joined views | Consumer-Aligned (centralized consumer layer). |
| Stream-aligned teams (Team Topologies) | Value Chain-Aligned. End-to-end ownership. |
| Large business units that share data heavily | Coarse-Grained Domain Topology. |
| Single regulatory regime, single geography | Single Data Landing Zone. |
| Multiple geographies / regulatory regimes | Multiple Data Landing Zones, central management zone. |
| Adopting Mesh tomorrow | Don't. Confirm platform readiness first. |
| Mesh failing | Audit which underinvestment broke it: platform, governance automation, or domain capability. |
| Domain wants to modify another's data | Reject. Route them to the originating domain. |
| Domain produces derived data | New ownership; new data product. |
| Cross-domain integration needs | Use Common Driveway pattern; standardize endpoints, not styles. |

---

## Worked Example: Adopting Governed Mesh at a 200-Engineer Fintech

**Context:** Mid-size fintech, 200 engineers, 6 business domains (Lending, Payments, Risk, Compliance, Customer, Marketing). Centralized DW is the bottleneck. Compliance requires audit trails on every data movement.

**Topology choice:** Governed Domain Topology. Why:
- Compliance requires central visibility (rules out Fully Federated)
- Domains have engineering capability (rules out Hub-and-Spoke as too constraining)
- Distribution-layer pattern fits both ownership and governance needs

**Implementation outline:**

| Element | Choice |
|---|---|
| Distribution layer | Apache Iceberg tables with Unity Catalog or AWS Glue + LakeFormation |
| Self-serve platform | Internal Backstage portal — domains self-onboard data products |
| Catalog | DataHub (open-source) for metadata + lineage |
| Contracts | Data Contract Application (DCA) — domains register schema + SLAs |
| Governance automation | Open Policy Agent (OPA) — declarative policies enforced at distribution layer |
| Landing zones | Two — source-aligned (CDC ingestion) + consumer-aligned (Snowflake DW for analytics) |
| First domains | Payments + Customer — clearest ownership and high consumption |
| Migration | Strangler Fig — central DW shrinks as domains take over their products |

**Phasing:**
- Months 1-3: Platform investment. Backstage portal. DataHub. OPA policies.
- Months 4-6: Migrate Payments + Customer to data products on the new platform.
- Months 7-9: Migrate Lending + Risk.
- Months 10-12: Migrate Marketing + Compliance. Decommission central DW for these workflows.

**Result:** 12 months in, 6 domains own their data products. Central DW is for legacy reporting only. Audit visibility maintained via OPA + DataHub lineage.

**Lesson:** Governed Mesh is the right answer for most regulated mid-large enterprises. Don't aspire to Fully Federated unless the platform and domain capability genuinely warrant it.

---

## Gotchas

- **"Mesh" has become marketing.** Vendors selling "Data Mesh in a box" usually mean a centralized DW with new branding. Verify the actual architecture.
- **DDD workshops are essential.** Without bounded-context analysis, domain boundaries are arbitrary. Budget time for this.
- **Self-serve platform is a year-long investment.** Don't expect Mesh in 6 months without one.
- **Compliance teams don't care about Mesh.** They care about audit trails. Automated lineage + access policies are the actual deliverable.
- **Domain capability varies wildly.** Some domains can self-serve; others can't. Partial Federation is honest.
- **Data Fabric and Data Mesh are not opposites.** Fabric (intelligent metadata layer) often sits on top of Mesh (decentralized data products). They compose.
- **Cross-domain join performance can degrade** under fully federated topologies. The central distribution layer (Governed Mesh) helps here.
- **Common Driveway pattern requires real catalog discipline.** Without it, "standard endpoints" devolve into "everyone's spreadsheet."

---

## Further Reading

- *Data Management at Scale* by Piethein Strengholt (O'Reilly, 2nd ed.)
- *Data Mesh* by Zhamak Dehghani (O'Reilly, 2022) — the canonical reference
- *Team Topologies* by Skelton & Pais — for value-chain-aligned thinking
- *Domain-Driven Design* by Eric Evans — for bounded contexts
- See `enterprise-data-integration-and-distribution` for distribution patterns
- See `mdm-and-federated-data-governance` for MDM and catalog approaches
- See `data-engineering-lifecycle-and-principles` for the Reis & Housley lifecycle context

Source: *Data Management at Scale* (Strengholt), Chapters 1-3.
