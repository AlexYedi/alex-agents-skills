# Additional Experts and Surrounding Literature

Companion-author and adjacent-source map for *Foundations of Scalable Systems*.

---

## The Author

**Ian Gorton** is a Director and Professor of Computer Science at Northeastern
University's Khoury College of Computer Sciences (Seattle campus). He created
and teaches CS6650, *Building Scalable Distributed Systems*, the graduate
course that the book's content was developed for and field-tested through.

Gorton's career arc: senior researcher at the Pacific Northwest National
Laboratory (chief architect on multi-petabyte scientific data systems), Chief
Technology Officer at MedeAnalytics, and academic positions before NEU. His
distinctive contribution is the engineering-school perspective: every concept
is grounded in code examples, real production case studies, and the day-to-day
trade-offs an engineer actually has to navigate.

The book's voice — concrete, pragmatic, slightly skeptical of vendor marketing,
quick to cite specific failure modes — comes from this teaching-and-consulting
mix.

---

## Reviewers and Contributors (per Acknowledgments)

These names are useful as additional voices in the same space:

- **Mark Richards** — Software architect; founder of DeveloperToArchitect.com;
  co-author of *Fundamentals of Software Architecture* and *Software Architecture:
  The Hard Parts*. Wrote the foreword-style endorsement for the book.
- **Matt Stine** — Engineer at Pivotal/VMware on cloud-native and reactive
  systems; author of *Migrating to Cloud-Native Application Architectures*.
- **Jess Males** — Engineer at Capital One.
- **Adnan Rashid** — Engineer at Microsoft.
- **Eoin Woods** — CTO at Endava; co-author of *Software Systems Architecture*.
- **Anna Liu** — Senior Manager at Amazon Web Services.
- **John Klein** — Carnegie Mellon SEI; software architecture researcher.
- **Len Bass** — Carnegie Mellon SEI emeritus; co-author of *Software Architecture
  in Practice* (the foundational architecture textbook).

---

## Surrounding Literature

A reading map of books that pair well with *Foundations of Scalable Systems*:

### Architectural Foundations

- **Mark Richards & Neal Ford — *Fundamentals of Software Architecture***
  (O'Reilly, 2020). Covers higher-level architectural styles, characteristics
  ("ilities"), connascence, and the architect's discipline. Gorton fills in
  the scalable-systems implementation depth that Richards/Ford intentionally
  abstract away.

- **Mark Richards & Neal Ford — *Software Architecture: The Hard Parts***
  (O'Reilly, 2021). Distributed-architecture trade-offs at the
  monolith-to-microservices decision boundary.

- **Len Bass, Paul Clements, Rick Kazman — *Software Architecture in
  Practice*** (Addison-Wesley, 4th ed.). The CMU/SEI canonical textbook on
  quality attributes and architecture analysis.

### Distributed Systems Depth

- **Martin Kleppmann — *Designing Data-Intensive Applications*** (O'Reilly,
  2017). The deepest mainstream treatment of replication, partitioning,
  consistency, and consensus. Gorton is faster to action; Kleppmann goes
  deeper into the algorithms.

- **Alex Petrov — *Database Internals*** (O'Reilly, 2019). Storage engines
  (B-trees, LSM-trees), distributed coordination, replication. One level
  below Gorton.

- **Brendan Burns — *Designing Distributed Systems*** (O'Reilly, 2018).
  Pattern catalog for container-orchestrator-era distributed systems.

### Microservices

- **Sam Newman — *Building Microservices*** (O'Reilly, 2nd ed., 2021). The
  reference. Newman's principles are quoted directly in Gorton's Ch 9.

- **Sam Newman — *Monolith to Microservices*** (O'Reilly, 2019). The pragmatic
  decomposition guide.

- **Adrian Cockcroft, ed. — *Beyond Microservices*** and **Daniel Bryant — many
  conference talks** are good supplements to Newman.

### Eventual Consistency, Consensus, and Distributed Algorithms

- **Werner Vogels et al. — *Dynamo: Amazon's Highly Available Key-value Store***
  (SOSP 2007 paper). The Dynamo paper that birthed Riak/Cassandra/Voldemort
  and the sloppy-quorum + version-vector pattern Gorton describes in Ch 11.

- **Diego Ongaro & John Ousterhout — *In Search of an Understandable Consensus
  Algorithm (Raft)*** (USENIX ATC 2014). The original Raft paper; readable in
  a single sitting.

- **James Corbett et al. — *Spanner: Google's Globally-Distributed Database***
  (OSDI 2012). The Spanner / TrueTime / commit-wait paper Ch 12 references.

- **Kyle Kingsbury — *Jepsen reports*** at jepsen.io. Empirical consistency
  testing of every database Gorton mentions and many more. Cited explicitly
  in Ch 12.

- **Marc Brooker — *AWS architecture talks and blog posts*** (re:Invent talks
  on DynamoDB, Lambda). Insider perspective on the AWS systems Gorton uses
  as case studies.

### Messaging and Event-Driven

- **Gregor Hohpe & Bobby Woolf — *Enterprise Integration Patterns*** (Addison-
  Wesley, 2003). The pattern catalog for messaging and routing — Gorton's Ch 7
  patterns trace back here.

- **Ben Stopford — *Designing Event-Driven Systems*** (O'Reilly, 2018, free
  ebook from Confluent). Kafka-centric event-driven architecture. Direct
  complement to Ch 14.

- **Gunnar Morling — *Change Data Capture* essays at debezium.io**.

### Stream Processing

- **Tyler Akidau, Slava Chernyak, Reuven Lax — *Streaming Systems*** (O'Reilly,
  2018). Definitive treatment of streaming theory — windows, watermarks,
  triggers, accumulation. Direct complement to Ch 15. Akidau's 2015 essay
  *The world beyond batch: Streaming 101/102* is the warm-up.

- **Fabian Hueske & Vasiliki Kalavri — *Stream Processing with Apache Flink***
  (O'Reilly, 2019). Deep on the Flink runtime and APIs.

- **Adam Bellemare — *Building Event-Driven Microservices*** (O'Reilly, 2020).
  Event-streaming for microservices.

### Production Operations

- **Mike Roberts — *Programming AWS Lambda*** (O'Reilly, 2020). Companion to
  Ch 8.

- **Yan Cui — *Production-Ready Serverless* (Manning, 2018) and his blog at
  theburningmonk.com**.

- **Brendan Gregg — *Systems Performance* (Addison-Wesley, 2nd ed., 2020)**
  for the OS/network/disk layer Gorton's app-tier chapters sit on top of.

### Concurrent Programming (Ch 4 supplement)

- **Brian Goetz et al. — *Java Concurrency in Practice*** (Addison-Wesley,
  2006). The canonical reference for the Java APIs Ch 4 surveys.

- **Maurice Herlihy & Nir Shavit — *The Art of Multiprocessor Programming***
  (Morgan Kaufmann, 2nd ed., 2020). Theory-leaning concurrency depth.

---

## How to Use This Map

| If your goal is… | Read after Gorton |
|---|---|
| To understand consistency and replication algorithms deeply | Kleppmann (DDIA), then the Raft and Dynamo papers |
| To design real microservices well | Newman (Building Microservices) and Stopford |
| To go deeper on one specific platform (Kafka, Flink, Lambda) | The dedicated O'Reilly title for that platform |
| To verify production claims of a database | Jepsen reports |
| To teach this material | Bass/Clements/Kazman + Richards/Ford for the architectural framing layer above Gorton |
| To audit performance issues in a Java service | Goetz (Java Concurrency in Practice) for the per-node concurrency layer below Gorton's Ch 4 |

---

## Source

*Foundations of Scalable Systems* by Ian Gorton (O'Reilly, 2022) and the
acknowledgments / further-reading sections referenced throughout the book.
