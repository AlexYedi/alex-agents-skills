# Chapter 6 — Appendix

This chapter is the support layer for the other six. The glossary defines the acronyms and methodology terms the body chapters use without breaking flow to gloss them. The sources give every cited number a place to chase. The methodology notes lock the analytical choices the body chapters implicitly relied on — why XI–XII are combined, why the OCQ lens scores /15 in three sub-dimensions, why conviction stars map to specific evidence levels. The update protocol and change log keep the artifact maintainable twelve months from now, when memory of why a choice was made has faded and the temptation to "tidy" is highest. Reference, not narrative.

## §6.1 Glossary

Alphabetized. Extends the canonical list in spec §3.8 with the terms actually used in Ch 1–5.

| Term | Definition |
|---|---|
| 7 Powers | Hamilton Helmer's framework for durable strategic power. The seven: Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power. Ch 2 §2.3. |
| Action-confirmation gate | Operating discipline at the end of each ritual — explicitly name "what you do not do" so the cadence does not bloat. Ch 5 §5.1. |
| ARR | Annual Recurring Revenue. |
| ASIC | Application-Specific Integrated Circuit — custom silicon (TPU, Trainium, Maia, MTIA, Sohu). |
| ASL | AI Safety Level — Anthropic's RSP capability tier (ASL-2 deployed, ASL-3 active, ASL-4 thresholds partially specified). |
| BBU | Battery Backup Unit — rack-level battery for OCP Open Rack v3. |
| Bet | A named opportunity Alex is choosing to pursue or hold. Seven listed in Ch 3 §3.1. |
| Binding constraint | What actually limits scaling at a stratum (e.g. transformers and interconnect at Stratum I, HBM and CoWoS-L at Stratum III). Ch 1, per-stratum block. |
| BM25 | Probabilistic sparse retrieval algorithm; baseline for keyword search in hybrid RAG. |
| C2PA | Coalition for Content Provenance and Authenticity — image/audio watermarking standard. |
| CBRN | Chemical, Biological, Radiological, Nuclear — frontier safety threat category. |
| ColBERT | Late-interaction neural retrieval (token-level scoring). |
| Commodity / Utility | Wardley evolution stage 4. Rentable, undifferentiated, price-competitive. |
| CoWoS | Chip-on-Wafer-on-Substrate — TSMC's advanced 2.5D packaging; CoWoS-L is the variant binding HBM-rich GPU supply. |
| CPO | Co-Packaged Optics — optical interconnect integrated into the switch ASIC package. |
| Crux | An unresolved question whose answer re-ranks every bet. Five listed in Ch 3 §3.3. |
| Custom-Built | Wardley evolution stage 2. Bespoke per-customer engineering; not yet a standard product. |
| DC | Data Center, or Direct Current depending on context. |
| DP | Data Parallelism — replicate model, split data across replicas. |
| DPU | Data Processing Unit — programmable NIC handling offloaded network/storage/security work (BlueField, Pensando, Nitro). |
| EP | Expert Parallelism — split experts of an MoE model across GPUs. |
| FCF | Free Cash Flow. |
| FERC | Federal Energy Regulatory Commission — US grid regulator; rejected the Talen-Amazon behind-the-meter ISA. |
| FSDP | Fully Sharded Data Parallel — PyTorch sharding strategy (FSDP2 = DTensor-based). |
| Genesis | Wardley evolution stage 1. Novel, untested, exploratory. |
| GPAI | General-Purpose AI — EU AI Act term for foundation models. |
| GraphRAG | Knowledge-graph-augmented retrieval; Microsoft GraphRAG uses Leiden clustering + community summaries. |
| GRPO | Group Relative Policy Optimization — DeepSeek's PPO variant; drops value network, computes advantages relative to a group mean. |
| HBM | High-Bandwidth Memory; HBM3e current, HBM4 ramping. SK Hynix ~62% share. |
| IPU | Intelligence Processing Unit — Graphcore's accelerator class; broader: Intel IPU E2100 (DPU equivalent). |
| JTBD | Jobs-to-Be-Done — framework lineage Christensen → Ulwick → Bettencourt. Six ecosystem jobs in Ch 2 §2.4. |
| LPO | Linear Pluggable Optics — lower-power non-DSP optics; 30–50% module power cut vs. retimed. |
| M&A | Mergers and Acquisitions. |
| MCP | Model Context Protocol — Anthropic-originated tool-use standard, donated to Linux Foundation Dec 2025. |
| MCP fork | The risk that a major vendor unilaterally extends MCP with proprietary schemas, fragmenting the commons. Crux 3, Ch 3 §3.3. |
| MEP | Mechanical, Electrical, Plumbing — 50–60% of data-center capex. |
| Meta-stratum | Horizontal layer that wraps every primary stratum (Safety, Regulation, Economics, Geopolitics). Ch 1 Part V. |
| MFU | Model FLOPs Utilization — fraction of theoretical FLOPs achieved during a training run. |
| MoE | Mixture of Experts — sparse activation; only a subset of expert sub-networks fires per token. |
| MTEB | Massive Text Embedding Benchmark — Hugging Face leaderboard. |
| NCCL | NVIDIA Collective Communications Library — GPU collectives. RCCL is AMD's; OneCCL is Intel's. |
| NVL | NVIDIA NVLink rack form-factor (NVL72, NVL144, NVL576). |
| OCQ | Opportunity / Challenge / Open Question — the matrix lens. Ch 2 §2.1. |
| Operator translation | Translating frontier capability announcements into specific operator implications for a named persona; the JTBD Job 3 gap-7 outcome and the Bet #6 thesis. |
| PFAS | Per- and polyfluoroalkyl substances — "forever chemicals"; regulatory pressure has retreated two-phase immersion cooling. |
| PPA | Power Purchase Agreement — long-term electricity contract; hyperscaler PPAs anchor Stratum I. |
| Procurement playbook | Bet #1's deliverable — operator-voice canonical guide for how F1000 buys AI vendors. Ch 3 §3.1. |
| Product | Wardley evolution stage 3. Rentable as a standard product; multiple vendors. |
| Punctuated equilibrium | Wardley term — a sharp transition from one evolution stage to the next that reprices everything depending on the component. Five expected 2026–2027. Ch 2 §2.2. |
| PP | Pipeline Parallelism — split layers across GPUs sequentially. |
| PUE | Power Usage Effectiveness — total facility power / IT power. 1.0 is the floor; hyperscale best ~1.10. |
| RAG | Retrieval-Augmented Generation. |
| RCCL | ROCm Communications Collective Library — AMD's NCCL equivalent. |
| RLVR | Reinforcement Learning from Verifiable Rewards — reward signal is a unit test or symbolic verifier. |
| RSP | Responsible Scaling Policy — Anthropic's frontier-safety framework; v3.1 effective Apr 2, 2026. |
| Settle quadrant | Wardley strategic choice — productize what is currently bespoke. Where Alex's bets concentrate. |
| SMR | Small Modular Reactor — sub-300 MWe nuclear (NuScale, X-energy, Kairos, TerraPower). |
| SPLADE | Sparse lexical neural retrieval; learned sparse alternative to BM25. |
| Stratum / strata | A horizontal layer in the AI stack; numbered I–XIV plus Meta A–D. |
| TP | Tensor Parallelism — split single-layer matmuls across GPUs. |
| WUE | Water Usage Effectiveness — liters per kWh; sub-0.20 is the modern target. |

## §6.2 Sources & further reading

Organized by category, not by chapter. Every entry is a thing to actually read on a recurring cadence; if it never gets opened, drop it from the rotation.

### Primary data sources (keep these fresh)

- **IEA Electricity 2026** — annual report on global electricity demand, with the data-center sub-section. Read at release; re-read Stratum I after.
- **EPRI 2026 grid update** — US-specific data-center load projections; primary citation for "9–17% of US generation by 2030."
- **PJM auction reports** — quarterly capacity auction clears; primary citation for Dominion zone $444.26/MW-day and the 833% YoY data-center attribution.
- **NVIDIA quarterly earnings + GTC keynotes (Mar)** — capex commentary, capacity guidance, rack-scale reference designs (Rubin Ultra Kyber 600 kW landed at GTC 2026).
- **Anthropic, OpenAI, Google financial disclosures** — what gets published vs. leaked; the gap is signal. Crux 1 lives in this gap.
- **The Information (subscription)** — Stephanie Palazzolo on AI funding, M&A, talent; canonical secondary source for ARR leaks.
- **Pallet newsletters** — talent-flow aggregator; primary signal for the Stripe/Ramp/Datadog/Snowflake → Sierra/Decagon migration.
- **Air Street Capital "State of AI Report"** — annual, Nathan Benaich + Othmane Sebbouh; the year-in-review of record.
- **Artificial Analysis** — independent model benchmarks; latency/cost tradeoffs.
- **MTEB leaderboard** — embedding model rankings (Hugging Face).
- **Hugging Face Agents leaderboard** — agent reliability across tasks.
- **OSWorld / WebArena benchmarks** — computer-use agent reliability. Watch for the 70%+ threshold (Crux-adjacent for Bet #3).
- **Stanford Digital Economy Lab "Canaries in the Coal Mine"** — labor-displacement evidence; cited at Meta-D for entry-level hiring impact.
- **SemiAnalysis (Dylan Patel)** — capacity tracking for CoWoS-L, HBM, neocloud deploy ratios; canonical for Risk 1 watch.

### Framework lineage (the books)

- **Hamilton Helmer — *7 Powers*** — durable strategic power; Ch 2 §2.3 lens.
- **Simon Wardley — *Wardley Maps* (online book)** — evolution × value chain; Ch 2 §2.2 lens.
- **Anthony Ulwick — *Jobs to Be Done* / *What Customers Want*** — Outcome-Driven Innovation; outcome statement structure.
- **Lance Bettencourt + Anthony Ulwick — "The Customer-Centered Innovation Map" (HBR)** — the 8-phase Job Map (Define → Locate → Prepare → Confirm → Execute → Monitor → Modify → Conclude).
- **Clayton Christensen — *Competing Against Luck*** — JTBD as causal theory; foundational.

### Operator newsletters / blogs to skim weekly

- **Latent Space** (swyx) — developer-leaning AI synthesis.
- **Stratechery** (Ben Thompson) — strategy-leaning; hyperscaler economics.
- **Air Street Press** (Nathan Benaich) — investment perspective.
- **Sam Bhagwat (Mastra)** — agent ecosystem, TypeScript-side.
- **One Useful Thing** (Ethan Mollick) — capability change for non-technical readers.
- **Pallet's role aggregations** — recurring; the talent-flow primary surface.

### Regulatory primary sources

- **EU AI Act text + Commission guidance** — GPAI obligations live Aug 2, 2025; transparency Aug 2, 2026; legacy compliance Aug 2, 2027. Read the implementing acts when they land — Crux 4.
- **California SB 53 (Transparency in Frontier AI Act)** — signed Sep 29, 2025; effective Jan 1, 2026. Captures developers training >10^26 FLOPs at companies >$500M revenue.
- **Trump December 2025 Executive Order on "Eliminating State Law Obstruction of National AI Policy"** — federal preemption; Risk 4 trigger; watch court rulings 2026–2027.
- **FERC orders on behind-the-meter siting** — Talen-Amazon ISA rejection (Nov 2024, Apr 2025); re-filed as front-of-meter PPA.

### Texas / Colorado AI laws (sourcing TODO)

Ch 1 Meta-B references "Texas and Colorado have parallel regimes" without statute numbers.

- **Colorado** — SB 24-205 ("Consumer Protections for Interactions with Artificial Intelligence Systems"), signed 2024-05-17, effective 2026-02-01. Confirm citation before next major refresh.
- **Texas** — TODO. Identify the operative Texas AI consumer-protection bill (HB / SB number, signing date, effective date). Resolve before the next twice-yearly refresh (§6.4).

### Companies named that warrant their own watchlist URL

Single watch-source per row. Add to your reader rotation.

- **Anthropic** — anthropic.com/news; Dario / Jack Clark on X.
- **OpenAI** — openai.com/blog; The Information for the unleaked.
- **Google DeepMind** — deepmind.google/discover; I/O keynote (May).
- **Meta Superintelligence Labs (MSL)** — Zuckerberg posts; Pallet for cluster-hire signal.
- **NVIDIA** — investor.nvidia.com; GTC March; Computex June.
- **AMD** — ir.amd.com; Lisa Su keynotes.
- **TSMC** — pr.tsmc.com; quarterly capex commentary.
- **SK Hynix / Micron** — quarterly HBM ramp telemetry.
- **Sierra** — sierra.ai blog + Bret Taylor on X.
- **Decagon** — The Information + LinkedIn for hiring posture.
- **Glean** — glean.com/blog; enterprise search-agent reference deploys.
- **Harvey** — harvey.ai/news; legal vertical proof points.
- **Hippocratic AI** — hippocratic.ai; Munjal Shah interviews.
- **Cursor** — cursor.com/blog; Aman Sanger on X.
- **Augment Code** — augmentcode.com.
- **Lovable** — lovable.dev; Anton Osika on X.
- **Mastra** — mastra.ai blog; Sam Bhagwat on X.
- **Vercel (AI SDK + AI Gateway)** — vercel.com/blog/ai.
- **CoreWeave** — coreweave.com/blog; quarterly disclosures.
- **Crusoe** — crusoe.ai; Stargate deploy disclosures.
- **Stargate** — coverage in The Information + Bloomberg; no first-party site.
- **MongoDB (Voyage)** — mongodb.com/blog; embedding/rerank releases.
- **Pinecone, Qdrant, Weaviate, Chroma, Turbopuffer** — each blog; M&A watch (Crux 5 adjacent).
- **Mem0, Letta, Zep, Cognee** — memory category; funding rounds are Crux 5 signal.
- **Apollo Research, METR, Pattern Labs** — third-party eval; report releases.
- **Frontier Model Forum** — frontiermodelforum.org; joint publications.
- **Linux Foundation Agentic AI Foundation** — MCP governance; Crux 3 watch.

## §6.3 Methodology notes

### §6.3.1 Why 14 strata + 4 meta-strata (not 18 flat)

The meta-strata wrap rather than stack. Safety, Regulation, Economics, and Geopolitics each apply across every primary stratum — a power constraint at Stratum I is also a regulation question (siting, FERC) and a geopolitics question (Stargate UAE, sovereign capital), without being subordinate to either. Flattening to 18 would force a single ordinal position where the actual relationship is orthogonal. The spec preserves this framing (spec §3.1); chapters should not "fix" it by renumbering.

### §6.3.2 Why Strata XI–XII are combined

The original report treats Retrieval, Memory, and Orchestration as one band because in production they share the same buyer, the same procurement gauntlet (Job 4), and the same Wardley evolution-stage cluster (Custom-Built crossing into Product). A vector database does not get bought separately from the orchestration framework that calls it; a memory layer is selected against the same enterprise architecture review as the retrieval layer below it. The spec preserves the combined framing (spec §3.1, note on XI–XII). Documenting it here so future-Alex does not "tidy" XI–XII apart and break the Ch 3 bet cross-references that depend on the joint treatment (Bets #3 and #5 both cite Strata XI–XII).

### §6.3.3 Lens scoring discipline (the /15 distribution)

OCQ scores three sub-dimensions 1–5, totaling /15. Definitions (spec §3.3):

- **Opportunity** = Confidence + Time-to-Monetize + Claimability-for-Alex.
- **Challenge** = Severity + Probability + Alex-Exposure.
- **Open Question** = Decidability-Horizon + Answer-Asymmetry + Bet-Size-Implication.

The score-discipline note from the spec is binding: resist 15/15 grade inflation. The lens exists to produce a distribution, not a validation. Ch 2 §2.1's "Pattern read" subsection explicitly names the six 15/15 Opportunity scores in the matrix as a calibration signal — the Claimability-for-Alex sub-dimension is doing most of the work, and that is the correct read of the field for one specific operator, not a bug. The quarterly deep review (Ch 5 §5.3) includes a grade-inflation audit on exactly this point.

### §6.3.4 Conviction stars (★) calibration

Used in Ch 3 §3.1 and Ch 4 §4.2. The mapping is evidence-anchored, not affect-anchored:

- **★★★★★** — framework convergence across 5/5 lenses + named bet target in active pursuit (Bets #1 and #2 meet this bar).
- **★★★★** — framework convergence across 4/5 + clear next action with a falsifiable trigger (Bets #3, #4, #5).
- **★★★** — framework convergence across 3/5 + real but not primary; contingent on what other bets do not land (Bets #6 and #7).
- **★★** — real but not actionable; watch only.
- **★** — noted but inactive; effectively killed.

Re-rate monthly with explicit reasoning (Ch 5 §5.2 step 1). Conviction is the live signal; the underlying bet narrative is stable.

### §6.3.5 Falsifiability requirement

Every bet in Ch 3 carries an explicit falsifiability statement. The methodological commitment is that a bet which cannot be killed by a future datapoint is not a bet — it is a belief. The monthly conviction ritual (Ch 5 §5.2 step 2) checks each bet's leading indicators against observed movement; the quarterly review (Ch 5 §5.3 step 1) checks whether the falsifiability conditions themselves still apply. If a bet has been carried for three months without any leading indicator moving, the indicator list is stale — fix the list before re-rating the bet.

### §6.3.6 Time discipline on numbers

Every number in the body chapters carries a date (spec §7). The reason is operational: twelve months from now, the reader needs to know whether "Sierra $100M ARR Oct 2025 at 400% YoY" is fresh enough to anchor a current bet or has been overtaken by audited 2026 disclosures. Numbers without dates rot silently. Numbers with dates can be re-evaluated against the current state of the field. The same discipline applies to disputed figures (Anthropic ARR $24B vs. $30B, Apr 2026) — log the range, the source, and the date; do not pick a midpoint.

## §6.4 Update protocol

Reproduces spec §10 with the chapter-bound ritual added (canonical reference).

| Cadence | What updates | Where | Owner | Ritual |
|---|---|---|---|---|
| Weekly | Noticing prompts (no tracker writes) | Notes system | Alex | Ch 5 §5.1 |
| Bi-weekly | Talent moves, capital events | Ch 4 §4.3, §4.4 | Alex | Ch 5 §5.1.5 |
| Monthly | Bet conviction, leading indicators, cruxes status | Ch 3, Ch 4 §4.2, §4.8 | Alex | Ch 5 §5.2 |
| Trigger-based | Crux resolved, risk fired | Ch 4 §4.8, §4.9 | Alex | (immediate) |
| Quarterly | Framework re-read, risk re-check, drill rotation, score-discipline audit | Ch 2, Ch 3, Ch 5 | Alex | Ch 5 §5.3 |
| Twice-yearly | Source re-extract, plate regen, spec version bump, EPUB rebuild | All | Alex | Ch 5 §5.4 |

### How to bump the version

Minor (1.1, 1.2, ...) — content additions, citation refreshes, table updates, new sub-section inside an existing chapter, single bet re-rating logged. Lands as a row in §6.5 below. Monthly cadence at most.

Major (2.0, 3.0, ...) — taxonomy change (renumbering strata, retiring a framework, adding a new chapter), structural shift to the bets/cruxes/risks set, change to the OCQ lens definitions or conviction-star calibration. Lands as a paragraph-length entry in §6.5 with explicit "what changed and why." Twice-yearly cadence at most; usually aligned with the §5.4 refresh.

Tie-break rule: if you are not sure whether a change is minor or major, treat it as major and write the paragraph. The cost of over-documenting is small; the cost of a silent taxonomy shift discovered six months later is high (cross-references in Ch 3 and Ch 4 break, plates render against a stale spec).

## §6.5 Change log

| Date | Version | Change | Driver |
|---|---|---|---|
| 2026-05-20 | 1.0 | Initial consolidation: merged `AI_STACK_REPORT.docx` + `AI_STACK_ADDENDUM.docx` + `OCQ_TRACKER.md` + `HANDOVER_*.md` into a single 7-chapter workbook with 5 plates and an EPUB build. Archived original visual philosophy and HANDOVER drafts to `_archive/`. | Reduce friction; make the substrate actionable rather than referential. |
| _next_ | _next_ | _Bi-weekly tracker syncs do not log here; only monthly conviction changes and above land in this table._ | — |

Major version bumps land here with a paragraph-length "what changed and why" explanation. Minor bumps land as table rows. When a Crux resolves (Ch 4 §4.8) and the resolution re-ranks two or more bets, that combination is itself a minor-version-worthy event and should be logged.

## Apply

Open §6.2 and skim the source list. Pick one source you do not currently follow — add it to your reading rotation this week. The job is not to know every source; it is to keep the rotation fresh enough that no single source becomes a single point of failure for what you know about this field. If you currently rely on three sources, you are one outage away from a blind spot; if you rely on twelve, the rotation will collapse under its own weight. The right number is six to eight, with two new ones every twice-yearly refresh and two retired in the same session.
