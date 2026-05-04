# Data Management at Scale — Additional Expert Notes

> Best practices from Piethein Strengholt's *Data Management at Scale* (O'Reilly, 2nd ed.).

## About the Author

**Piethein Strengholt** — Microsoft Data Architect, ex-ABN AMRO. Operates at the intersection of enterprise data architecture and modern Mesh / Fabric thinking. Voice: pragmatic, regulatory-aware, distrustful of pure ideology (criticizes both "Mesh-or-bust" and "MDM-everything").

## Foundational Mindset Shifts

1. **Decentralization is a spectrum, not a binary.** "Are we doing Data Mesh?" is the wrong question. "Which topology fits our current capability?" is the right one.
2. **Platform investment is the lever for Mesh success.** Without self-serve infrastructure, decentralization is chaos.
3. **Domain ownership requires DDD discipline.** Bounded contexts, ubiquitous language. Without these, "domain" boundaries are arbitrary.
4. **Data contracts are API contracts.** Treat them with the same versioning rigor.
5. **Federated governance via automation, not committees.** Manual approval at scale fails; declarative policy enforcement scales.
6. **MDM is narrow by design.** 5-10 entities. Don't try to unify everything.
7. **Distinguish data products from domain data stores (DDS).** Products are stable, contract-bound. DDS is consumer-side, transient.

## Best Practices by Topic

### Topology selection
- Start at Centralized or Governed for orgs < 100 engineers
- Plan toward Fully Federated only if platform engineering is strong
- Hub-and-Spoke for strict audit / regulatory contexts
- Coarse-Grained when business units share data heavily and fine-grained boundaries cause political fights
- Value Chain-Aligned for stream-aligned teams (Team Topologies sense)

### Data product design
- Logical entity in metamodel; physical implementation can vary
- Schema + SLA + ownership + classification is non-optional metadata
- Self-discoverable via catalog
- Versioned contracts; deprecation cycle for breaking changes

### MDM scoping
- 5-10 stable, broadly-shared, critical entities (Customer, Product, Account, Site, Employee — typical)
- Reject transactional data from MDM scope
- Master IDs assigned centrally; mapped to source-system local IDs
- Start with Registry style; mature toward Consolidation / Coexistence as appropriate

### Catalog operations
- Owner per entry; quarterly review
- Stale entries archived
- Glossary co-authored with business
- Search-first UX

### Governance automation
- Policies as code (OPA + Rego)
- ABAC for fine-grained access (PEP at data plane)
- Data contracts in Git; CI enforces schema compatibility
- Auto-grant for compliant requests; human review for exceptions

### Integration pattern selection
- Async by default; sync when truly required
- Strongly consistent reads only when use case demands
- Standard endpoints (Common Driveway) over standard implementations
- Choreography for autonomy; orchestration for sagas

## Specific Advice with Rationale

### "Capture and modify only at the Golden Source"
**Why:** Multiple update points = multiple sources of truth = no source of truth.
**Apply:** Read-only access cross-domain. Modifications routed back to source domain owner.

### "New facts → new ownership"
**Why:** Derived data has its own lifecycle and quality concerns.
**Apply:** Domain B that creates a customer health score from Domain A's customer data owns the score, not the underlying customer.

### "Don't distribute data you don't own"
**Why:** Proxies and republishing erase ownership trails.
**Apply:** Route consumers to source domains, not through your domain.

### "Bake data quality at the producer"
**Why:** Pushing quality downstream multiplies effort across N consumers.
**Apply:** Validate at ingest. Reject or flag bad records. Don't let them propagate.

### "Federated governance via automation"
**Why:** Committee-based governance scales to dozens of products, not hundreds. Automation scales.
**Apply:** OPA + Rego. Domain teams self-publish products complying with declarative policies.

### "Logical data products"
**Why:** Physical tech changes (Snowflake → Databricks → ?). Logical contracts don't.
**Apply:** Metamodel describes products as logical entities. Implementations are detail.

### "Common Driveway over single integration tech"
**Why:** Forcing all domains to use one tech is brittle and political.
**Apply:** Standardize the catalog registration format. Domains expose products via REST, events, or batch — registered uniformly.

## Worked Examples

### Adopting Governed Mesh at a 200-engineer fintech
See `data-mesh-domain-topologies` skill.

### Cross-domain customer profile (per-consumer pattern selection)
See `enterprise-data-integration-and-distribution` skill.

### Federated governance for a pharma's Data Mesh
See `mdm-and-federated-data-governance` skill.

## Anti-Patterns Deeper Than Skill Files

- **Mesh as marketing** — central DW renamed "platform"; existing teams renamed "domains"
- **Premature Full Federation** without platform readiness
- **Domain boundaries from org chart**, not DDD bounded contexts
- **Distribution layer as de facto centralized DW** — modeling re-centralized
- **Cross-domain modifications** — Golden Source rule violated
- **Federated governance with manual approval workflows** — defeats the speed
- **Async / event-driven cult** — adopting events where REST sync would be simpler
- **Composite service god classes** — composite services accumulate logic
- **CQRS + Event Sourcing as default** — adopted before need; doubles complexity
- **MDM big bang** — 18-month projects that get canceled
- **Catalog as graveyard** — entries without owners
- **RBAC where ABAC is needed** — coarse roles can't express compliance constraints
- **Knowledge graph before catalog** — heavy stack with no foundational catalog
- **Treating DDS as a data product** — consumer-side stores misused as cross-domain contracts

## Process Wisdom

- **DDD workshops before topology decisions.** Bounded contexts inform domain boundaries.
- **Self-serve platform is a year-long investment.** Plan accordingly.
- **Data contracts in Git, like API specs.** Version, deprecate, communicate.
- **Quarterly catalog reviews.** Stale metadata is misleading metadata.
- **Compliance partnership early.** Auditors care about lineage + access logs + classifications. Engineer that in.
- **Migrate via Strangler Fig.** Mesh adoption is incremental.
- **First domains for Mesh:** highest-consumption + clearest ownership. Customer + Payments are common starting points.

## Career / Context Wisdom

- **Data Mesh consultant arms race is over.** "Adopt Data Mesh" is no longer a differentiator. The hard work is the migration.
- **Platform engineering is the rising data role.** Building self-serve infrastructure is where leverage lives.
- **Data contract specialists** are emerging as a distinct role at large orgs.
- **Strengholt's pragmatism is its own brand.** Comfortable saying "Mesh isn't right for you" — rare among consultants.
- **The book is Microsoft-leaning** in tooling examples. Architectural points are vendor-agnostic; concrete tools chapter shows Microsoft bias.

Source: *Data Management at Scale* (Strengholt, O'Reilly, 2nd edition).
