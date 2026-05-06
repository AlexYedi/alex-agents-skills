---
description: Walk the greenfield data platform architecture chain — lifecycle, frameworks, mesh vs centralized, integration, dataops, governance, then handoff to schema design.
---

You are guiding a greenfield data platform architecture exercise using the chain documented at `Data Engineering/playbooks/01-greenfield-platform.md`.

Walk these steps in order, applying the named skill at each step:

1. **Frame** — `Data Engineering/architecture/lifecycle-and-principles` — establish lifecycle stages, undercurrents, and the 9 architecture principles for the user's context.
2. **Framework** — `Data Engineering/architecture/architecture-frameworks` — pick TOGAF, DAMA, AWS Well-Architected, Lambda vs Kappa, MDS vs Live Stack with rationale.
3. **Branch on org structure:**
   - Federated / domain-oriented org → `Data Engineering/architecture/data-mesh-topologies` (pick a topology, define data product principles)
   - Centralized → `Data Engineering/architecture/storage-and-modeling-patterns` (warehouse vs lake vs lakehouse, pick model)
4. **Integration** — `Data Engineering/architecture/integration-patterns` — cross-domain flow: APIs vs events vs CDC, sync vs async, choreography vs orchestration.
5. **Operating model** — `Data Engineering/architecture/dataops-and-platforms` — SLOs, semantic layer, FinOps, dbt-style analytics-as-code.
6. **Governance** — `Data Engineering/governance-and-quality/mdm-and-federated-governance` — MDM style, data contracts, ABAC, catalog architecture.
7. **Handoff** — when implementation begins, transition to `Data Engineering/databases/database-designer` (the playbook ends here; schema work follows playbook 02).

For each step:
- State the decision being made
- Cite the trade-offs the named skill enumerates
- Capture the user's chosen direction before moving to the next step

If the user signals a deviation ("skip step N", "I already chose X", "just use [specific skill]"), honor it and adjust the chain — playbooks are defaults to deviate from, not workflows to march through.

Reference the full playbook for decision-point details:
**`Data Engineering/playbooks/01-greenfield-platform.md`**
