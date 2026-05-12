# Additional Experts & Further Reading — Software Architecture: The Hard Parts

Where to go after this book. Other thinkers in the trade-off-analysis tradition, complementary texts, and related distillations in this repo.

---

## The Four Authors — Background and Adjacent Work

### Mark Richards

30+ years independent consulting; founder of DeveloperToArchitect.com (free training video catalog widely used for architect onboarding). Distinct voice: practitioner-confident, war-story-grounded, allergic to silver bullets.

**Other work you should know:**
- *Fundamentals of Software Architecture* (with Neal Ford, O'Reilly 2020) — **already distilled in this repo at** `references/fundamentals-of-software-architecture/`. Required prequel to *The Hard Parts*. If you haven't read it, do that first.
- *Software Architecture Patterns* (O'Reilly 2015) — short, free, the 5-style catalog (Layered, Event-Driven, Microkernel, Microservices, Space-Based) that *Fundamentals* later expands.

### Neal Ford

Director and Software Architect at Thoughtworks. Brings the **evolutionary architecture** and **fitness function** vocabulary into this book.

**Other work you should know:**
- *Building Evolutionary Architectures* (with Rebecca Parsons & Patrick Kua, O'Reilly 2017; 2nd ed 2023) — companion to *The Hard Parts* on the governance side. Fitness functions are barely a paragraph here; that book is 200 pages on the topic. Read it after *Hard Parts* if you'll be writing architecture governance for an enterprise.
- *Functional Thinking* (O'Reilly 2014) — orthogonal but useful for the FP-as-design-tool angle.

### Pramod Sadalage

Thoughtworks; the database thinker in the author group. Sadalage owns Ch 6, Ch 9, Ch 10 in *Hard Parts*.

**Other work you should know:**
- *NoSQL Distilled* (with Martin Fowler, Addison-Wesley 2012) — the canonical short text on the four NoSQL data models (Key-Value, Document, Column Family, Graph). Pairs with the `scalable-database-design-and-sharding` skill in this repo.
- *Refactoring Databases* (with Scott Ambler, Addison-Wesley 2006) — the schema-evolution playbook. Still the reference text on this topic.

### Zhamak Dehghani

Originator of **Data Mesh**. Owns Ch 14 in *Hard Parts*.

**Other work you should know:**
- *Data Mesh: Delivering Data-Driven Value at Scale* (O'Reilly 2022) — the full treatment of Ch 14's primer. If your work touches analytics, data products, or federated data governance, the *Hard Parts* chapter is appetizer; this book is the meal.
- Her original 2019 ThoughtWorks blog post — "How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh" — is the canonical short-form introduction.

---

## Adjacent Thinkers (not in the author group)

### Sam Newman — *Building Microservices* (O'Reilly, 2nd ed 2021)

The other essential microservices text. Newman's voice is operational where Richards's voice is architectural. *Building Microservices* spends more time on:
- Deployment topologies and platforms
- Observability and operational concerns
- Migration strategies (Strangler Fig in detail)
- Security at the service boundary

*The Hard Parts* spends more time on:
- Trade-off method
- Data ownership and decomposition
- Saga taxonomy
- Contract coupling

The two books are complementary, not redundant. If you only read one, read this one. If you can read two, add Newman.

### Eric Evans — *Domain-Driven Design* (Addison-Wesley 2003)

Bounded contexts, ubiquitous language, aggregates. *The Hard Parts* assumes DDD vocabulary throughout (especially Ch 5–7). If "bounded context" is unfamiliar, read Evans first or — for a shorter on-ramp — Vaughn Vernon's *Implementing Domain-Driven Design* (2013) or *Domain-Driven Design Distilled* (2016).

### Chris Richardson — *Microservices Patterns* (Manning 2018)

The other saga book. Richardson's saga treatment is more code-detailed (he ships sample implementations in Java) where *Hard Parts* is more taxonomy-detailed. If you're implementing a saga and want code-level guidance, Richardson is the reference. If you're deciding *which* saga, *Hard Parts* is the reference.

### Vlad Khononov — *Learning Domain-Driven Design* (O'Reilly 2021)

Newer, shorter, more accessible than Evans. Pairs well with *Hard Parts* if you need DDD background. Also covers the same architectural-decomposition territory but lighter on the trade-off analysis side.

### Susanne Kaiser — *Adaptive Systems with Domain-Driven Design* (Addison-Wesley 2024)

The Wardley-Maps-meets-DDD-meets-team-topologies synthesis. Useful if you're trying to extend the trade-off method to include team/organizational coupling, which *The Hard Parts* deliberately leaves out of scope.

### Manuel Pais & Matthew Skelton — *Team Topologies* (IT Revolution 2019)

The organizational coupling text. *Hard Parts* mentions team structure rarely; Team Topologies is the canonical text on how Conway's Law shapes service boundaries. Read this if you suspect your services map to teams in a way that's working against you.

---

## Related Distillations in This Repo

| Reference folder | When to use alongside Hard Parts |
|---|---|
| `references/fundamentals-of-software-architecture/` | Read this *first*. Hard Parts assumes it as background. |
| `references/foundations-of-scalable-systems/` | Gorton's text on scale. Use for storage-layer scaling vocabulary not covered in Hard Parts. |
| `references/API_Architectures/` | Bernardez & Olejár on API design. Use for the contract specifics that Hard Parts Ch 13 treats at architectural level. |
| `references/modern-software-engineering/` | Dave Farley. Use for the continuous-delivery + fitness-function discipline that Hard Parts assumes but doesn't teach. |
| `references/progit/` | Git mechanics. Useful when implementing the Component-Based Decomposition Ch 5 patterns at the repo level. |

---

## Articles & Talks (Free)

### From the authors

- **DeveloperToArchitect.com** (Richards) — free video catalog. Especially: the "Software Architecture Monday" series. Many videos directly cover *Hard Parts* topics in shorter form than the book.
- **Neal Ford on InfoQ** — multiple talks on architectural fitness functions and evolutionary architecture.
- **Dehghani's Data Mesh ThoughtWorks blog post** (2019) — the canonical short-form Data Mesh intro.
- **Richards & Ford on architectural quanta** — multiple conference talks under the title *"The Architectural Quantum"*. Find on YouTube; ~45 min.

### Trade-off / decision discipline

- Michael Nygard's **"Documenting Architecture Decisions"** (2011 blog post) — the foundational ADR post. Hard Parts uses the same ADR shape.
- Spotify's engineering blog on ADRs — pragmatic implementation.
- Pat Helland's **"Life Beyond Distributed Transactions"** (2007 ACM Queue article) — the foundational essay on giving up distributed transactions. Hard Parts' saga chapters stand on this.

### Sagas

- Chris Richardson's **microservices.io** site — saga implementation patterns with code.
- Hector Garcia-Molina & Kenneth Salem's **"Sagas"** (1987 SIGMOD paper) — the original saga paper. Worth reading if you want to know where the term came from. Surprisingly readable.

---

## When to NOT Reach For This Book

This is the **don't-load-this-folder** counterpart in `INDEX.md`, but expanded:

- **Greenfield architecture from a clean slate** — *Fundamentals* is a better starting point. *Hard Parts* is about messy in-flight decomposition.
- **Frontend architecture** — the book is server-side. Frontend coupling has different shapes.
- **Code-level design patterns** — the book operates above the class level. Use GoF or *Refactoring* (Fowler).
- **Database design at the table level** — the book is above the table level. Use Sadalage's *NoSQL Distilled* or *Refactoring Databases*.
- **Operational SRE / observability** — out of scope. Use Beyer et al.'s *Site Reliability Engineering* or *Observability Engineering* (Majors, Fong-Jones, Miranda).
- **Specific cloud platform patterns** — out of scope. Use the platform's well-architected docs (AWS / GCP / Azure).

---

## How to Get Maximum Value from the Hard Parts Method

After reading the book and skills derived from it, the long-term practice is:

1. **Write ADRs for every non-trivial decision.** Don't skip ones you're confident about; future engineers can't tell intentional from incidental without an ADR.
2. **Use the trade-off table format consistently.** A team that uses the same table format for every decision builds a corpus that compounds in value — future-team can compare new decisions against old ones.
3. **Run fitness functions in CI.** The book mentions these briefly; *Building Evolutionary Architectures* is the deep dive.
4. **Bring stakeholders into the trade-off analysis early.** Sysops Squad Ch 6 (Dana the DBA) and Ch 7 (Sam the security lead) are warnings, not features — both characters were brought in late, both pushed back, both improved the outcome. Invite them earlier next time.
5. **Read other people's ADRs.** The skill of writing good ADRs is largely the skill of having read many ADRs. Public ADR repos (Spotify, Arc42 examples, the ADR organization on GitHub) are useful sources.

---

## Citation

When citing this book in ADRs or design docs:

> Ford, N., Richards, M., Sadalage, P., & Dehghani, Z. (2021). *Software Architecture: The Hard Parts — Modern Trade-Off Analyses for Distributed Architectures*. O'Reilly Media.

For specific frameworks, cite the chapter:

> The 8 transactional saga patterns (Ford et al. 2021, Ch 12).
> Trade-off analysis 3-step method (Ford et al. 2021, Ch 2 and Ch 15).
