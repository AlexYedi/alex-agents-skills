# Recommended Resources for Enriching the CTO-Architect Skill

These resources can be added as reference material over time to improve the quality
and consistency of architecture guidance. Organized by category, prioritized by
relevance to Alex's stack.

---

## Architecture Patterns & System Design

| Resource | Why It's Valuable |
|----------|-------------------|
| [System Design Primer](https://github.com/donnemartin/system-design-primer) (109k+ stars) | Comprehensive reference for scalability patterns, caching, load balancing, and distributed system fundamentals — good baseline for any architecture discussion |
| [System Design 101 by ByteByteGo](https://github.com/ByteByteGoHq/system-design-101) | Visual explanations of complex systems using diagrams — aligns with the skill's emphasis on Mermaid visualization |
| [Awesome Design Patterns](https://github.com/DovAmir/awesome-design-patterns) | Curated list of architecture and design patterns across languages and paradigms |
| **Distilled** — *Foundations of Scalable Systems* (Gorton, O'Reilly 2022) | Already distilled in `Software Development/references/foundations-of-scalable-systems/`. Comprehensive textbook on scalable distributed systems — load balancing, caching, messaging, microservices resilience, sharding, eventual vs strong consistency, Kafka, Flink. Use the derived skills (`scalability-foundations`, `distributed-systems-essentials`, etc.) for implementation-depth questions. |
| **Distilled** — *Fundamentals of Software Architecture* (Richards/Ford, O'Reilly 2020) | Already distilled in `Software Development/references/fundamentals-of-software-architecture/`. Higher-level architectural style choice; complements Gorton (style) + Gorton (implementation). |

**How to use**: Extract the patterns most relevant to Supabase + Vercel + Next.js
architectures and add condensed versions to a `references/architecture-patterns.md`
file over time. For scalability-specific questions, the Gorton-derived skills
already cover the canonical content — invoke them directly rather than
reinventing the patterns here.

---

## ADR (Architecture Decision Record) Templates

| Resource | Why It's Valuable |
|----------|-------------------|
| [Joel Parker Henderson's ADR repo](https://github.com/joelparkerhenderson/architecture-decision-record) | The most comprehensive ADR collection — multiple templates, real examples, lifecycle guidance |
| [MADR (Markdown ADRs)](https://github.com/adr/madr) | Lightweight markdown-first templates in full, minimal, and bare variants — ideal for solo builders who want structure without overhead |
| [Michael Nygard's original ADR format](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md) | The original: Title, Status, Context, Decision, Consequences. Simple enough to actually use consistently |

**How to use**: Bundle a preferred ADR template in `references/adr-template.md` so
the skill can produce consistent decision records. The Nygard format is recommended
as the default — it's the simplest that works.

---

## AI/LLM Application Architecture

| Resource | Why It's Valuable |
|----------|-------------------|
| [LangChain RAG documentation](https://python.langchain.com/docs/tutorials/rag/) | Canonical patterns for RAG pipelines with modular retriever/generator/orchestration separation |
| [RAGFlow's "From RAG to Context" review](https://ragflow.io/blog/rag-review-2025-from-rag-to-context) | 2025 year-end review covering the shift from basic RAG to Context Engineering — directly relevant to building with pgvector + Supabase |
| [Advanced RAG Techniques (Neo4j)](https://neo4j.com/blog/genai/advanced-rag-techniques/) | Deep dive on GraphRAG, CRAG (Corrective RAG), and hybrid retrieval patterns |
| [RAGOps paper](https://arxiv.org/html/2506.03401v1) | Framework for operating and managing RAG pipelines in production — monitoring, evaluation, and maintenance patterns |

**How to use**: When Alex builds RAG features, the skill should reference these
patterns to recommend the right chunking strategy, retrieval approach, and evaluation
framework. Consider adding a condensed `references/rag-patterns.md` once the
pgvector embedding pipeline is built.

---

## Supabase-Specific Patterns

| Resource | Why It's Valuable |
|----------|-------------------|
| [Supabase RLS Best Practices](https://supabase.com/docs/guides/troubleshooting/rls-performance-and-best-practices-Z5Jjwv) | Official performance guidance — indexing columns used in policies, caching function results per-statement |
| [Production RLS Patterns (MakerKit)](https://makerkit.dev/blog/tutorials/supabase-rls-best-practices) | Multi-tenant RLS patterns with account membership tables and role-based access |
| [2025 Supabase Security Guide](https://github.com/orgs/supabase/discussions/38690) | Pentest-based findings — common RLS missteps, permissive policies, missing WITH CHECK clauses |
| [Edge Functions docs + examples](https://supabase.com/docs/guides/functions) | Official patterns for auth, Kysely type-safe queries, and database interaction from edge functions |
| [Securing Edge Functions](https://supabase.com/docs/guides/functions/auth) | Auth patterns inside functions — req.headers.authorization, service role vs anon key usage |

**How to use**: These should be the first reference when the skill recommends data
model changes or RLS policies. Consider bundling the key security findings into the
stack-context reference.

---

## Next.js + Vercel Architecture

| Resource | Why It's Valuable |
|----------|-------------------|
| [Next.js App Router docs](https://nextjs.org/docs/app) | Canonical reference for server components, route handlers, middleware, caching |
| [Vercel Architecture documentation](https://vercel.com/docs/architecture) | How Vercel's infrastructure works — edge network, serverless functions, ISR, and deployment model |
| [Next.js SaaS Starter (Vercel)](https://github.com/vercel/nextjs-subscription-payments) | Production-ready SaaS template with Supabase auth + Stripe — directly relevant to Alex's stack |

**How to use**: Reference when designing new Next.js applications or evaluating
server component vs. client component boundaries.

---

## n8n Workflow Patterns

| Resource | Why It's Valuable |
|----------|-------------------|
| [n8n workflow templates](https://n8n.io/workflows/) | Community library of automation patterns — good source for common integration patterns |
| [n8n documentation](https://docs.n8n.io/) | Official docs for webhook triggers, error handling, sub-workflows |

**How to use**: When the skill designs automation that belongs in n8n, reference
community patterns to avoid reinventing common integrations.

---

## Security Checklists

| Resource | Why It's Valuable |
|----------|-------------------|
| [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist) | Concise, actionable checklist for API design — auth, input, output, CI/CD security |
| [OWASP Top 10](https://owasp.org/www-project-top-ten/) | Industry standard vulnerability categories — good for framing security reviews |

**How to use**: Bundle a condensed security checklist in `references/security-checklist.md`
that the skill references during architecture reviews. Focus on the items most relevant
to a solo builder's stack: auth, API keys, RLS, env var hygiene, and CORS.

---

## Recommended Addition Sequence

Don't add everything at once. Prioritize based on what Alex is actively building:

1. **Now**: ADR template (`references/adr-template.md`) — immediately useful for
   every architecture session
2. **When building RAG**: `references/rag-patterns.md` condensed from LangChain +
   RAGFlow resources
3. **When scaling**: `references/security-checklist.md` condensed from API Security
   Checklist + Supabase security guide
4. **Over time**: `references/architecture-patterns.md` with patterns extracted from
   System Design Primer, filtered for relevance to Alex's scale
