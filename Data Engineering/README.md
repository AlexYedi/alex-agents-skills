# Data Engineering

Skills, agent bundles, and references covering the full data engineering lifecycle — architecture, governance, hands-on schema design, production pipelines, and retrieval (RAG / KG / text-to-SQL).

## How to Use This Folder

Five subdirectories, organized by **when you'd invoke them**. Pick the subdirectory that matches your trigger; each skill inside is scoped to a specific decision or task.

| You're doing... | Go to | Top-level skills |
|---|---|---|
| Scoping or designing a data platform | [`architecture/`](architecture/) | lifecycle-and-principles, architecture-frameworks, storage-and-modeling-patterns, data-mesh-topologies, integration-patterns, dataops-and-platforms |
| Setting up MDM, contracts, audit, access control | [`governance-and-quality/`](governance-and-quality/) | mdm-and-federated-governance, data-quality-auditor |
| Hands-on schema, index, or migration work | [`databases/`](databases/) | database-designer (POWERFUL tier — includes scripts) |
| Building / running production pipelines | [`pipelines/`](pipelines/) | analytics-pipeline-orchestration, enrichment-pipeline |
| RAG, knowledge graphs, embeddings, text-to-SQL | [`retrieval/`](retrieval/) | rag-architect, knowledge-graph-modeling/applications/platform-integration, text-to-sql; tutorials/ for learning material |
| Background reading | [`references/`](references/) | Data_Engineering_Basics, Data_Management_At_Scale, Knowledge_Graph book distillations + structured-vs-unstructured-retrieval decision aid |

## Decision Tree by Trigger

**"I'm starting a new data platform"** → `architecture/lifecycle-and-principles` → `architecture/architecture-frameworks` → `architecture/storage-and-modeling-patterns` (designs flow into the storage layer)

**"I need to design a database schema / migration"** → `databases/database-designer` (its references include normalization, index strategy, full schema example). Pair with `architecture/storage-and-modeling-patterns` for the conceptual frame (Kimball/Inmon/SCD/lakehouse).

**"My data quality is bad"** → `governance-and-quality/data-quality-auditor` for audit/profile work. For the surrounding contracts and policy frame, use `governance-and-quality/mdm-and-federated-governance`.

**"I need to enrich GTM data / build a waterfall"** → `pipelines/enrichment-pipeline` (full bundle with agents, commands, skills, providers.yaml). For the surrounding integration architecture (events vs APIs vs batch), see `architecture/integration-patterns`.

**"I need to ship analytics / dashboards / instrumentation"** → `pipelines/analytics-pipeline-orchestration`. For the operating model, see `architecture/dataops-and-platforms`.

**"I need to build retrieval over my data"** → start at `references/structured-vs-unstructured-retrieval.md` to choose KG vs RAG, then go to `retrieval/rag-architect` (RAG path) or `retrieval/knowledge-graph-modeling` (KG path). For SQL-over-natural-language, see `retrieval/text-to-sql`.

## What Lives Where

```
Data Engineering/
├── README.md                                      ← you are here
├── architecture/                                  ← theory, frameworks, scoping
│   ├── lifecycle-and-principles/                  Reis & Housley lifecycle + 9 architecture principles
│   ├── architecture-frameworks/                   TOGAF, DAMA, AWS WA, Lambda/Kappa, MDS vs Live
│   ├── storage-and-modeling-patterns/             Cache, lakehouse, Kimball/Inmon, SCD, joins
│   ├── data-mesh-topologies/                      Mesh domain topologies + data product principles
│   ├── integration-patterns/                      APIs, events, CQRS, choreography vs orchestration
│   └── dataops-and-platforms/                     DataOps, MDS/Live Stack, semantic layer, FinOps
├── governance-and-quality/                        ← MDM, contracts, audit, access
│   ├── mdm-and-federated-governance/              MDM styles, data contracts, ABAC, catalogs
│   └── data-quality-auditor/                      Profile + anomaly detection (SKILL + scripts)
├── databases/                                     ← hands-on schema work
│   └── database-designer/                         Schema, index, migration (SKILL + .py scripts)
├── pipelines/                                     ← production pipelines
│   ├── analytics-pipeline-orchestration/          Events, models, dashboards (agent bundle)
│   └── enrichment-pipeline/                       150+ providers, waterfalls, identity res. (full bundle)
├── retrieval/                                     ← RAG, KG, embeddings, text-to-SQL
│   ├── rag-architect/                             RAG pipeline design (SKILL + .py scripts)
│   ├── knowledge-graph-modeling/                  Property graph vs RDF, ontology vs taxonomy
│   ├── knowledge-graph-applications/              Identity resolution, fraud, dependency analysis
│   ├── knowledge-graph-platform-integration/      ETL, Spark, Kafka Connect, GDS
│   ├── text-to-sql/                               NL → SQL with prompting + RAG
│   └── tutorials/                                 ← learning notebooks (not invokable skills)
│       ├── retrieval_augmented_generation/
│       └── contextual-embeddings/
└── references/                                    ← background reading shared across skills
    ├── Data_Engineering_Basics/                   Book distillation
    ├── Data_Management_At_Scale/                  Book distillation
    ├── Knowledge_Graph/                           Book distillation
    └── structured-vs-unstructured-retrieval.md    KG vs RAG decision aid
```

## Tier and Type Conventions

- **POWERFUL tier** — invoked for substantial design or implementation work; usually has supporting `.py` scripts (e.g., `database-designer`, `rag-architect`, `data-quality-auditor`).
- **Standard SKILL.md** — focused conceptual or design playbook; no scripts (e.g., the `architecture/` skills).
- **Bundle** — a folder with `agents/` + `commands/` + `skills/` (e.g., `enrichment-pipeline`, `analytics-pipeline-orchestration`). Invoke the bundle's lead agent or a specific command/skill.
- **Tutorial** — `.ipynb` learning material under `retrieval/tutorials/`. Not invoked as a skill; read it to learn a technique.

## Cross-References at a Glance

Skills inside this folder cross-reference each other in their respective SKILL.md files. The pairings:

- **storage-and-modeling-patterns** ↔ **database-designer** (theory ↔ practice)
- **dataops-and-platforms** ↔ **analytics-pipeline-orchestration** (theory ↔ ops)
- **integration-patterns** ↔ **enrichment-pipeline** (patterns ↔ implementation)
- **mdm-and-federated-governance** ↔ **data-quality-auditor** (policy ↔ audit)
- **knowledge-graph-modeling/applications/platform-integration** ↔ **rag-architect** (structured ↔ unstructured retrieval, both bridge through `references/structured-vs-unstructured-retrieval.md`)

## Future Work (v2)

Cross-skill *chaining* — programmatic invocation between skills (one skill consumes another's output) — is deferred. Today, cross-skill composition is documented prose in SKILL.md cross-references and the `enrichment-expert` lead agent's delegation flow. Formalizing chained invocation contracts is the next iteration.
