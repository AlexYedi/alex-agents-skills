# Chapter 2 — Framework Lenses

Chapter 1 stratified the AI stack into eighteen layers. This chapter applies five analytical lenses to that same stack. None of the lenses is right on its own. OCQ classifies but does not position. Wardley positions but does not filter for durability. Helmer's 7 Powers filter for durability but ignore unmet need. Ecosystem JTBD surfaces unmet need but is silent on competitive structure. Talent and capital flow are pure empirical signal — useful only after the other four have given you somewhere to look.

The reason to apply all five to the same field is convergence. Any single framework can be miscalibrated, fashion-driven, or biased toward the author's own discipline. When five independent frames point at the same opportunity, the same constraint, or the same crux, that is the signal that survives doubt. When they diverge, the divergence itself is informative — it names the open question honestly rather than papering over it.

This chapter answers what each lens reveals about the stack as it stands in mid-2026. It does not yet answer what to do about it. Bets, risks, cruxes, and the action map live in Chapter 3, drawing on the patterns surfaced here. The Talent & Capital Flow section (§2.5) covers methodology only — the actual tables live in Chapter 4. The full per-stratum scores below feed Plate 2 (OCQ Heatmap), Plate 3 (Wardley Map), and Plate 4 (Powers × Layer Grid).

## §2.1 OCQ × Layer Matrix

### Lens definitions

**OPPORTUNITY.** Where value is being created faster than the field's prevailing narrative reflects. Specifically: structural inefficiency, underserved jobs-to-be-done, mispriced talent, mispositioned distribution. Not "things that are good." Scored 1–5 on three dimensions:

- **Confidence** — how sure we are
- **Time-to-Monetize** — 5 = soon
- **Claimability for Alex** — can someone with enterprise B2B GTM plus AI-builder fluency act on it

Total: /15.

**CHALLENGE.** The binding constraint or latent feedback loop that, if it tightens or fires, materially reprices everything above it. Not "things that are hard"; things that bind. Scored:

- **Severity** — how much it reprices
- **Probability** — likelihood it bites
- **Alex Exposure** — how much it affects his bets specifically

Total: /15.

**OPEN QUESTION.** A crux the field is betting on without admitting it; an answer would change other answers. Phrased as actual questions. Scored:

- **Decidability Horizon** — 5 = decidable soon
- **Answer-Asymmetry** — how much bets diverge based on the answer
- **Bet-Size Implication** — how much the playbook would shift

Total: /15.

Resist 15/15 grade inflation. The lens definitions exist to produce a distribution, not validation.

### How to use this matrix

Read across to compare strata: where does opportunity intensity cluster, where do challenges concentrate, which open questions are decidable in the next four quarters versus in 2027 and beyond. Read down within a single stratum to balance the three lenses — a 15/15 opportunity with a 14/15 binding challenge in the same layer is not the same picture as a 15/15 opportunity with a 7/15 constraint. The lens is a filter, not a validation device: if every cell is scoring 13+, the scoring is broken, not the field. Use the matrix to surface where conviction is warranted, where it isn't, and where the next moves should be staged. Cross-reference with Plate 2 (OCQ Heatmap) for the visual read.

### Per-stratum scoring

#### Stratum I — Power

- **Top Opportunity.** Behind-the-meter gas-plus-storage GTM into hyperscaler site-selection teams while interconnect queues sit on 4–7 year backlogs. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** Transformer and HVDC lead times of 130+ weeks across Hitachi, Siemens, GE Vernova — every announced gigawatt assumes supply that does not exist. (13/15 — S:5 / P:5 / E:3)
- **Top Open Question.** Will FERC and PJM force hyperscalers to pay full cost-of-service for transmission upgrades, or will the co-located-load loophole hold? (12/15 — D:4 / A:5 / B:3)

#### Stratum II — Facility

- **Top Opportunity.** Direct-to-chip liquid-cooling retrofit services for the 2021–2023 air-cooled fleet; Blackwell racks at 120–140 kW exceed air-cooling thresholds and CoreWeave, Lambda, Cologix, Stack, Aligned all need the work. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Water-rights and zoning approvals are the new binding constraint in Phoenix, Northern Virginia, and Dublin; WUE specs are now contractual. (11/15 — S:4 / P:5 / E:2)
- **Top Open Question.** Does single-phase or two-phase immersion cooling become standard by 2027, or does cold-plate direct-to-chip win the decade? (11/15 — D:4 / A:4 / B:3)

#### Stratum III — Compute

- **Top Opportunity.** Enterprise GTM for inference-optimized silicon alternatives (Groq, Cerebras, SambaNova, Tenstorrent) targeting cost-conscious latency-sensitive workloads; inference TCO is now a CFO conversation. (13/15 — C:4 / T:4 / Cl:5)
- **Top Challenge.** HBM3e/HBM4 supply is the actual bottleneck — SK Hynix sold out through 2026, every GPU forecast downstream of three Korean fab decisions. (14/15 — S:5 / P:5 / E:4)
- **Top Open Question.** Does inference compute demand actually 10× from 2025–2027 as agentic and reasoning workloads suggest, or do algorithmic efficiency gains flatten the curve? (14/15 — D:4 / A:5 / B:5)

#### Stratum IV — Fabric

- **Top Opportunity.** Enterprise sales for Ethernet-AI (Spectrum-X, Tomahawk 6, Cisco Silicon One P200) into buyers refusing InfiniBand lock-in; UEC 1.0 ratified mid-2025, Meta/Oracle/xAI all on Ethernet at 100k+ GPU scale. (13/15 — C:4 / T:4 / Cl:5)
- **Top Challenge.** NVLink 5/6 plus NVSwitch is a stickier moat than CUDA at rack-scale; UALink silicon is 18–24 months from competing — locks NVIDIA pricing on training clusters through 2027. (12/15 — S:5 / P:4 / E:3)
- **Top Open Question.** Does the scale-up NVLink-style coherent-memory domain keep expanding to 576+ GPUs and crowd out scale-out, or do UEC/SHARPv4 improvements commoditize fabric? (12/15 — D:3 / A:5 / B:4)

#### Stratum V — Parallelism

- **Top Opportunity.** Inference-platform enterprise GTM (Modal, Baseten, Replicate, Fireworks, Together) — inference is becoming a procurement category separate from training; enterprise AE roles at $300–500K OTE are open. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** The vertically integrated NVIDIA stack (CUDA + cuDNN + NCCL + Megatron-Core + TensorRT-LLM) punishes parallelism-layer-only optimizers; most independent startups become NVIDIA features within 24 months. (11/15 — S:4 / P:4 / E:3)
- **Top Open Question.** Do agent runtimes (LangGraph, OpenAI Agents SDK, Claude Agent SDK, Mastra) consolidate on a winner by 2027, or collapse into model providers as a feature? (14/15 — D:4 / A:5 / B:5)

#### Stratum VI — Data

- **Top Opportunity.** Enterprise data-licensing brokerage — the buyer set is roughly 15 frontier labs, the seller set is every enterprise on a proprietary corpus; Reddit-Google $60M, Reddit-OpenAI $70M, HarperCollins/Wiley/Taylor & Francis prove publishers can negotiate eight-figure ARR. Single most claimable opportunity in the stack for enterprise-GTM-plus-contract fluency. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Data supply is collapsing into a two-tier market — frontier labs with paid corpora versus everyone else with degrading open data; Common Crawl quality is falling as scrapers get blocked. (10/15 — S:4 / P:4 / E:2)
- **Top Open Question.** Will EU AI Act Article 53's "sufficiently detailed summary" requirement be enforced as a teeth-bearing audit regime, or watered down to a checkbox? (13/15 — D:4 / A:5 / B:4)

#### Stratum VII — Pretraining

- **Top Opportunity.** Apache-2.0 frontier-class open weights (Qwen 3.5, Mistral Large 3, Llama 4 Scout) eliminate the licensing tax for enterprise deployments — value shifts to fine-tuning, hosting, and integration, all GTM-shaped. (12/15 — C:4 / T:5 / Cl:3)
- **Top Challenge.** Pretraining capex (~$500M–$1B+ per frontier run by 2026) creates an oligopoly of ~6 labs capturing 80% of the value above the model layer; Llama 4 Behemoth rumored at $3B+. (12/15 — S:5 / P:5 / E:2)
- **Top Open Question.** Does diffusion-based language modeling (Mercury at 1,109 tok/s) displace autoregressive transformers for latency-sensitive enterprise workloads by 2027? (11/15 — D:3 / A:4 / B:4)

#### Stratum VIII — Post-training

- **Top Opportunity.** Eval-as-a-product / eval-as-a-service for enterprise procurement — public benchmarks (SWE-bench Verified, ARC-AGI-2, FrontierMath) do not match enterprise-specific needs; custom eval harnesses are sellable advisory work at high margin. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** Benchmarks reset annually; SWE-bench Verified jumped from ~50% to 94% in 18 months, so enterprise buyers are procuring capability that is obsolete in 6 months at one-tenth the cost. (12/15 — S:3 / P:5 / E:4)
- **Top Open Question.** Is pure-RL emergence (DeepSeek-R1-Zero — reasoning without SFT) the dominant post-training paradigm by 2027, or a one-off? Answer reprices the entire human-preference labeling industry. (13/15 — D:3 / A:5 / B:5)

#### Stratum IX — Model Providers

- **Top Opportunity.** Multi-model procurement consultancy for the Fortune 1000 — no CIO wants single-vendor lock-in; aggregators went zero-markup May 2025; enterprises lack the playbook to negotiate Anthropic EAs against Azure OpenAI commitments against Bedrock inference pricing. $300–500K ACV with no incumbent. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Frontier-lab direct sales motion is consolidating downstream — Anthropic and OpenAI both built named-account coverage of the Global 2000 through 2025–26. The window for an independent implementation partner is narrowing. (13/15 — S:4 / P:5 / E:4)
- **Top Open Question.** Does Anthropic's reported $30B ARR survive contact with audited 2026 revenue? OpenAI CRO disputed the figure as ~$8B overstated. Decidable Q2–Q3 2026. (14/15 — D:4 / A:5 / B:5)

#### Stratum X — Inference Engines

- **Top Opportunity.** Inference-cost-optimization-as-a-service ("FinOps for tokens"). vLLM, SGLang RadixAttention prefix-cache, Dynamo disaggregated prefill/decode, EAGLE-3 speculative decoding, FP4 quantization, and routing combined can deliver 3–10× cost reduction; the median enterprise is running un-tuned vLLM on over-provisioned H100s. CFOs sign these. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Hyperscaler bundling absorbs the optimization layer — when Bedrock rolls out automatic FP8 + speculative decoding + cache routing as a setting, third-party shops compress. (11/15 — S:4 / P:4 / E:3)
- **Top Open Question.** Will enterprises tolerate open-weight quantized models in production, or insist on frontier-API quality? Bifurcates by vertical and determines whether the opportunity is "tune your Llama deployment" or "negotiate better EA terms." (13/15 — D:3 / A:5 / B:5)

#### Stratum XI — Retrieval and Memory

- **Top Opportunity.** Enterprise RAG architecture practice — vector-DB market is fragmented (Pinecone / Qdrant / Weaviate / Chroma / Milvus / LanceDB / pgvector / Turbopuffer); reranker selection, hybrid retrieval, Matryoshka migration. Pure architecture-and-procurement sale; Alex's structural wheelhouse. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Long-context models are partially eating RAG — Gemini 2.5 Pro at 1–2M tokens, Claude prompt caching, GPT-5 router compress the low-end TAM. (11/15 — S:3 / P:4 / E:4)
- **Top Open Question.** Is long-term memory a permanent product category (Mem0, Letta, Zep, Cognee) or a feature absorbed by frontier labs in 2026? Decidable in 12–18 months. (15/15 — D:5 / A:5 / B:5)

#### Stratum XII — Orchestration

- **Top Opportunity.** MCP server productization for vertical SaaS incumbents — 97M monthly SDK downloads, 10,000+ active servers, Linux Foundation donation Dec 2025; most mid-market vertical SaaS still ships zero or one MCP server. The land-grab window is roughly Q2–Q4 2026. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Framework half-life is ~12 months — LangChain 1.0, then LangGraph as center of gravity, then OpenAI Agents SDK, then Claude Agent SDK. Any deep practice on a single framework is one release from a rewrite. Mitigation: build at the MCP / protocol layer. (12/15 — S:4 / P:5 / E:3)
- **Top Open Question.** Will MCP remain a protocol commons or fork into proprietary tool-use schemas? Linux Foundation governance is a strong commons signal but every successful protocol has had a fork moment. (14/15 — D:4 / A:5 / B:5)

#### Stratum XIII — Application Layer

- **Top Opportunity.** Vertical agent GTM lead role at a Series B/C agent company — Sierra ($10B / $100M+ ARR), Decagon ($4.5B), Glean ($7.2B), Harvey ($5B), Hippocratic, Augment all hiring for Alex's exact profile. The market is in scarcity for enterprise-AE-with-AI-fluency at NYC. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Foundation model providers walking up-stack into vertical apps — ChatGPT Connectors/Agents/Apps, Claude for Work plus skills plus computer-use; every vertical agent now competes with "ChatGPT can already do 70% of that, natively, for $30/seat." (11/15 — S:4 / P:5 / E:2)
- **Top Open Question.** Will the agent-application layer concentrate to 1–3 winners per vertical, or fragment into a long tail of 50 specialists? Sierra/Decagon/Harvey/Glean look winner-take-most but sub-verticals may fragment. (13/15 — D:3 / A:5 / B:5)

#### Stratum XIV — The User

- **Top Opportunity.** Apple-Gemini Siri partnership (Jan 2026) creates a discrete distribution event — hundreds of millions get a competent agent on their phone by default. Apps that ship proper App Intents in the next 6–9 months capture distribution before the surface crowds. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** Default-distribution risk to every standalone consumer AI app — Siri (Gemini-powered), Gemini on Pixel/Samsung, Copilot on Windows weaken the case for installing standalone apps for the marginal user. (10/15 — S:4 / P:4 / E:2)
- **Top Open Question.** Where does inference settle — cloud-frontier, edge-PCC, or on-device — and in what mix per workload class? Apple's PCC bet is "you do not have to choose, we will route." (13/15 — D:3 / A:5 / B:5)

#### Meta-A — Safety and Alignment

- **Top Opportunity.** Enterprise AI governance / AI-risk-officer tooling — RSPs and Preparedness Framework are de facto procurement reference docs F500 risk committees are mapping their controls onto; EU AI Act August 2026 is the forcing function. (12/15 — C:4 / T:4 / Cl:4)
- **Top Challenge.** OpenAI Preparedness Framework v2's adjustment clause signals voluntary RSPs are unstable under competitive pressure — reprices any business built on assumed self-restraint. (11/15 — S:4 / P:4 / E:3)
- **Top Open Question.** Will interpretability advances (concept injection, circuit tracing) make models verifiably honest about their reasoning by 2027, or reveal alignment is shallower than claimed? Verified-honest unlocks 10× regulated TAM; verified-deceptive triggers a deployment freeze. (13/15 — D:3 / A:5 / B:5)

#### Meta-B — Regulation

- **Top Opportunity.** EU AI Act compliance practice for US enterprises with EU footprint — GPAI obligations live Aug 2025, transparency Aug 2026, legacy compliance Aug 2027. Boutique sitting between counsel and engineering = $250K–$1M ACV with multi-year tail. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Federal preemption volatility — the December 2025 Trump preemption EO is being litigated; courts will sort it through 2026–2027. Mitigate by selling EU compliance plus contractual compliance. (12/15 — S:4 / P:4 / E:4)
- **Top Open Question.** Does EU AI Act's 2026 transparency obligation create real compliance work, or get watered down via implementing acts? Decidable by mid-2026. (15/15 — D:5 / A:5 / B:5)

#### Meta-C — Economics

- **Top Opportunity.** Hyperscaler-procurement advisory for F500 buyers facing 2026 commit cycles — $660–770B aggregate hyperscaler capex, ~75% AI; most buyers negotiate without benchmarks. Structured commit-negotiation, model-portfolio design, exit-clause language at $100–500K per engagement. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Hyperscaler FCF stress plus AI revenue pull-forward equals 2027 capex air-pocket risk — Amazon FCF projected -$17B 2026; Anthropic at $30B and OpenAI at ~$24B are impressive but small versus capex. (10/15 — S:4 / P:3 / E:3)
- **Top Open Question.** What is the real run-rate ROI on $660–770B of 2026 hyperscaler AI capex, and when does the market force a measurement? Any 2-quarter window with decelerating enterprise AI ARR and a hyperscaler write-down reprices the entire stack simultaneously. (14/15 — D:4 / A:5 / B:5)

#### Meta-D — Geopolitics

- **Top Opportunity.** Compliance / export-control advisory and embedded sales at NVIDIA, AMD, hyperscalers managing the H20 / B30A / sovereign-cloud labyrinth — BIS rule updates created a permanent compliance function inside every chip and cloud company. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** TSMC's 90%+ leading-edge concentration on Taiwan is a single-point-of-failure that reprices the entire stack on any Strait event; insurance markets price 5–15% over 5 years. (12/15 — S:5 / P:3 / E:4)
- **Top Open Question.** Does sovereign AI become a real procurement category (50+ countries with own stacks by 2028) or collapse back into 3–4 hyperscaler-as-vassal arrangements? The Stargate UAE / Humain KSA template is the test. (12/15 — D:3 / A:5 / B:4)

### Pattern read

Opportunity intensity clusters unmistakably in the middle and upper bands — Strata VI (Data, 15/15), IX (Model Providers, 15/15), X (Inference Engines, 15/15), XI (Retrieval, 15/15), XII (Orchestration, 15/15), XIII (Application, 15/15), plus Meta-B (Regulation) and Meta-C (Economics) at the same ceiling. The physical-substrate strata (I–IV) score 13/15 at best because they are not in Alex's claimability band, not because opportunity is absent. Six 15/15 opportunities is too many — the lens is producing distribution, but the claimability-for-Alex dimension is doing most of the work, since each of those opportunities is structurally GTM-shaped.

Challenge intensity clusters at Stratum III (HBM, 14/15) and Stratum I (transformers, 13/15) — the physical-substrate bottlenecks that reprice everything above. Then a second cluster at Strata IX–XIII (direct-lab sales consolidation, framework half-life, foundation-lab walk-up-stack risk) — challenges in the same strata where the opportunity scores highest, which is correctly informative rather than contradictory: this is the field of play, not a quiet pasture.

Open Questions decidable soonest cluster around H2 2026: Anthropic ARR (Stratum IX, 14/15, Decidability 4), EU AI Act enforcement (Meta-B, 15/15, Decidability 5), and long-term memory absorption (Stratum XI, 15/15, Decidability 5). Three high-asymmetry cruxes resolve in the same 6-month window. That window is the planning anchor for the bets in Chapter 3. See Plate 2 for the visual heatmap.

![Plate 2 — OCQ Heatmap](plates/02_ocq_heatmap.svg)

## §2.2 Wardley Mapping the Stack

### Anchor needs

Four user needs anchor the top of the map. Everything below cascades as dependency to satisfy these.

- **Reliable AI assistance for enterprise knowledge work.** Analysts, lawyers, engineers, and ops teams need AI that reads, reasons, and produces work-product against private corporate context without hallucinating away the trust margin.
- **AI agents that operate computers and browsers on the user's behalf.** Multi-step task completion — research, fill forms, navigate SaaS apps, complete back-office work — without a human babysitting each click.
- **Conversational and voice AI for customer-facing workflows.** Autonomous support, sales qualification, scheduling, and outbound that closes loops rather than escalating.
- **Vertical AI workers in regulated and high-stakes domains.** Legal (Harvey), customer support (Decagon, Sierra), revenue ops (Clay), healthcare scribing — where domain workflow knowledge is the moat.

### Stack placement

**Stratum I — Power.** Commodity/Utility for the incumbent grid; Genesis for SMR-powered AI campuses (Kairos, X-energy, Oklo, NuScale — first commercial AI-dedicated nuclear ~2028). Direction: incumbent grid is becoming a constrained commodity as data-center load reprices regional capacity auctions; SMRs trend right but slowly.

**Stratum II — Facility.** Product for hyperscale design; Custom-Built for AI-factory-scale campuses (Stargate-class is bespoke); Genesis for 600 kW Kyber-class racks. Liquid cooling has crossed from Custom-Built into Product through 2025; immersion is still earlier.

**Stratum III — Compute.** Product for Hopper and Blackwell; Custom-Built for Rubin Ultra rack-scale; Genesis for transformer-only ASICs (Etched Sohu) and wafer-scale (Cerebras). HBM and CoWoS-L are the binding inputs, not silicon design itself.

**Stratum IV — Fabric.** Product for InfiniBand and 800 G Ethernet; Custom-Built for rack-scale NVLink and CPO; Genesis for UALink silicon. Scale-up is moving rightward only slowly because NVIDIA controls the protocol; scale-out is moving rightward faster because UEC is now ratified.

**Stratum V — Parallelism.** Product for FSDP / Megatron / JAX recipes at known scales; Custom-Built for >100k-GPU runs. The recipe knowledge itself sits in a Cornered Resource (frontier labs) and is moving rightward only through paper releases and personnel diaspora.

**Stratum VI — Data.** Product for licensed and synthetic pipelines; Custom-Built for frontier-lab data engineering; Commodity for the Common Crawl raw substrate. Licensing is moving rightward rapidly as deal precedents accumulate; provenance tooling is still Custom-Built.

**Stratum VII — Pretraining.** Product for the recipe; Custom-Built for the frontier runs themselves. Commodity is not visible — pretraining is concentrating, not commoditizing. Open-weight frontier-minus-one (Llama 4, Qwen 3.5, DeepSeek V4) is the one rightward pull.

**Stratum VIII — Post-training.** Product for SFT/DPO; Custom-Built for RLVR/GRPO at frontier scale; Genesis for chain-of-thought monitorability and process reward models. Test-time compute knobs (Claude 64k thinking, o3, Deep Think) crossed into Product through 2025.

**Stratum IX — Model Providers.** Product. Pricing is converging; differentiation has shifted to latency tier, caching mechanics, and rate-limit policy. AI gateways (Vercel, Cloudflare, OpenRouter) crossed into late-Product / Commodity through 2025–26.

**Stratum X — Inference Engines.** Product. vLLM, SGLang, TensorRT-LLM are mature and converging. Disaggregated prefill/decode (NVIDIA Dynamo) is Custom-Built crossing toward Product. Speculative decoding (EAGLE-3) is already in Product.

**Strata XI–XII — Retrieval, Memory, Orchestration.** Product for vector DBs, AI gateways, observability; Custom-Built for agent orchestration and memory; Genesis for computer-use agents and GraphRAG. MCP is the most-watched component — late-Custom crossing into Product in H1 2026.

**Stratum XIII — Application Layer.** Product for consumer chat and horizontal productivity; Custom-Built for vertical agents (Sierra, Harvey, Decagon, Hippocratic) — workflow integration is the moat and is not commoditizing.

**Stratum XIV — The User.** Product for chat and IDE surfaces; Custom-Built for voice and browser agents; Genesis for the hybrid on-device + cloud orchestration pattern (Apple PCC, Gemini Nano routing).

**Meta-A — Safety and Alignment.** Custom-Built. Standards are converging but not commodified; interpretability is Genesis at the research frontier.

**Meta-B — Regulation.** Custom-Built. Rules are written, enforcement is not yet mature. EU AI Act August 2026 transparency is the rightward pull.

**Meta-C — Economics.** Custom-Built. Capital structures (SPV financing, sovereign co-investment, Stargate) are still being invented.

**Meta-D — Geopolitics.** Custom-Built. "Compute as foreign policy" is operationally real but the doctrine is still being written.

### Punctuated equilibria expected 2026–2027

Five specific transitions expected in the next eighteen months. Each one reprices everything that depends on it.

- **MCP: late-Custom → Product (H1 2026).** Linux Foundation governance landed Dec 2025; OpenAI/Anthropic/Google/Microsoft shipping first-class support. Reprices every bespoke "tool integration" framework — LangChain tools, custom function-calling wrappers, vendor-specific connector SDKs. Adjacent-possible: MCP server marketplace, MCP-native iPaaS, security/governance around MCP audit logs.
- **Computer-use agents: Genesis → Custom-Built (mid–late 2026).** Operator, Mariner, Claude for Chrome cross 70%+ on WebArena/OSWorld. Reprices RPA — UiPath, Automation Anywhere — and lights up agent-completed back-office workflows (claims, AP, vendor onboarding).
- **HBM4 + CoWoS-L: Custom → Product (late 2026 → 2027).** SK Hynix and Micron HBM4 ramps; TSMC CoWoS-L capacity doubles from 75–80 KWPM to 120–130 KWPM. Eases the throttle on Rubin and unlocks a second tier of frontier labs. Inference cost per token crosses below new floors that make agent loops economical that were not.
- **Voice agent reliability: Custom → Product (mid-2026).** Realtime APIs plus Cartesia/Deepgram latency improvements push voice past the uncanny threshold for 80% of customer-service calls. Reprices BPO seats and IVR vendors. Vertical voice (healthcare intake, debt collection, restaurant ordering) becomes defensible.
- **AI gateways: Product → late-Product/Commodity (through 2026).** Vercel, Cloudflare, OpenRouter race-to-bottom on routing/caching/observability. Margin moves up-stack into policy/governance (PII redaction, prompt firewall, cost ceilings).

### Strategic quadrants

For someone in Alex's exact position: **Pioneer** computer-use agents in enterprise contexts and AI-procurement governance (write, observe, do not productize yet). **Settle** on a vertical AI worker for a function Alex has sold into for 12 years — RFP/security-questionnaire automation, deal desk co-pilot, AI-native SDR tooling — or an MCP server for a system enterprise GTM lives in (Salesforce, Outreach, Gong, Highspot). **Consume** Vercel AI Gateway, Turbopuffer or pgvector + Voyage, vLLM via a serverless inference provider, headless browser, voice telephony, STT/TTS, sandboxing — all rentable for cents. **Utility** for grid, fiber, cloud primitives, PyTorch, Kubernetes, Postgres.

### Pattern read

The strongest cluster is the Custom-Built → Product zone in the middle of the stack: agent orchestration, vertical agents, MCP, computer-use, voice, enterprise governance. That zone is exactly where Alex's GTM judgment compounds — productizing what is currently bespoke. The trap is misplacing components everyone places wrong. Two specific errors recur in the field: (1) treating vector databases as a Product-tier moat when they are crossing into commoditization (pgvector + Turbopuffer + every cloud-platform vector feature killed the standalone tier); (2) treating LangChain / LlamaIndex as a durable Product when direct SDKs and MCP are eating them from below. See Plate 3 for the full map.

![Plate 3 — Wardley Map of the AI Stack](plates/03_wardley_map.svg)

## §2.3 Helmer's 7 Powers

### The 7 powers (one-line each)

- **Scale Economies.** Declining unit costs as production grows.
- **Network Economies.** Value increases with users or nodes connected.
- **Counter-Positioning.** Incumbents cannot copy without destroying their existing business.
- **Switching Costs.** High cost for the customer to leave.
- **Branding.** Durable affective association that commands a premium.
- **Cornered Resource.** Privileged access to a critical input.
- **Process Power.** Embedded organizational know-how that is hard to replicate.

### Per-stratum power inventory

**Stratum I — Power.** Cornered Resource (Constellation, Vistra, Talen — interconnect queues and nuclear-adjacent land); Scale Economies (hyperscaler 10–20 GW PPAs); Process Power (Constellation/Vistra in nuclear restart). All strengthening. Durable.

**Stratum II — Facility.** Cornered Resource (NoVA/Phoenix/Columbus land + water + fiber + power triads); Scale Economies (Equinix, Digital Realty, QTS); Switching Costs (carrier-hotel co-location). Colocation rents up 30–50% YoY in Tier-1. Durable.

**Stratum III — Compute.** NVIDIA holds Cornered Resource (CoWoS-L, HBM priority) + Scale Economies (75%+ gross margin amortizes more R&D than every competitor combined) + Process Power (CUDA, NVLink, Blackwell rack-scale engineering) + Switching Costs (CUDA kernels, customer PyTorch graphs) + Branding ("the AI company"). Five powers stacked. Durable for training; semi-durable for inference as AMD and custom silicon take share.

**Stratum IV — Fabric.** NVIDIA Cornered Resource + Process Power (Mellanox/InfiniBand, NVLink). Counter-Positioning forming via UEC (Broadcom, AMD, Meta, Microsoft). Fabric content per cluster is rising faster than price compression. Durable for Broadcom; semi-durable for NVIDIA networking.

**Stratum V — Parallelism.** Process Power (frontier labs' internal training stacks); Cornered Resource (researchers who have shipped >100B models — extremely thin labor pool); Network Economies (PyTorch / JAX ecosystems). Durable as a team-as-asset; not a GTM job pool.

**Stratum VI — Data.** Cornered Resource (Reddit, X, YouTube, GitHub, LinkedIn, Bloomberg, Thomson Reuters, ICE). Counter-Positioning (incumbents grandfathered; newcomers must license). Switching Costs (Scale AI / Surge annotation infrastructure). Durable for unique-corpus owners; eroding for generic web crawl.

**Stratum VII — Pretraining.** Process Power (OpenAI, Anthropic, Google DeepMind — increasingly the moat); Cornered Resource (senior researchers); Branding (OpenAI consumer, Anthropic coding/safety, Google multimodal); Scale Economies (capex amortization for top 4); Counter-Positioning forming via DeepSeek/Qwen/Llama on open weights. Semi-durable: durable as oligopoly, per-token economics keep collapsing.

**Stratum VIII — Post-training.** Process Power (Anthropic Constitutional AI / RLAIF; OpenAI RLHF productization; Scale AI alignment-as-a-service); Cornered Resource (alignment researchers — extremely thin); Switching Costs (customer fine-tuned weights inside provider walls). Durable inside top labs; semi-durable as standalone business.

**Stratum IX — Model Providers.** Branding (OpenAI, Anthropic — stable); Switching Costs (lower than buyers think — OpenRouter commoditized switching); Scale Economies (inference cost curves); Network Economies (Bedrock, Azure OpenAI as multi-model marketplaces). Compressing aggressively. Semi-durable: Bedrock/Azure inherit cloud moats; pure API plays compress.

**Stratum X — Inference Engines.** Process Power (Groq LPU + compiler; Together kernel engineering; Fireworks FireAttention); Network Economies (vLLM open-source community); Cornered Resource (Groq SRAM-based hardware approach). Cyclical for software-only; semi-durable for vertically integrated (Groq, Cerebras).

**Stratum XI — Retrieval and Memory.** Switching Costs (embedding lock-in — eroding with multi-vector and late-interaction); Branding (Pinecone, Weaviate — eroding as pgvector ate the bottom); Process Power (Turbopuffer, MongoDB Atlas Vector, Databricks vector — stable as features of larger platforms). Compressing hard. Cyclical for pure-play; durable only as features inside Snowflake/Databricks/MongoDB.

**Stratum XII — Orchestration.** Network Economies (MCP server ecosystem — strengthening rapidly); Branding (Vercel AI SDK strengthening; LangChain eroding); Switching Costs (30+ MCP servers wired in is real surface area to migrate); Counter-Positioning (MCP as open protocol). Durable for MCP-as-protocol (Anthropic capture); semi-durable for AI gateways; cyclical for orchestration frameworks.

**Stratum XIII — Application Layer.** Process Power + Switching Costs (Sierra, Decagon, Harvey, Abridge, Glean, Cursor — vertical workflow embedding); Branding (Cursor, Perplexity, ChatGPT consumer); Network Economies (Glean enterprise data graph, Notion AI). Compressing for horizontal; expanding for deeply-vertical agents.

**Stratum XIV — The User.** Cornered Resource (Apple Neural Engine + iOS distribution; Google Pixel + Gemini Nano); Switching Costs (iOS/Android lock-in extreme); Branding. Durable — duopoly entrenched.

**Meta-A — Safety/Alignment.** Branding (Anthropic — uniquely owns "safety" in enterprise mind); Process Power (interpretability team, RSP framework); Cornered Resource (senior alignment researchers — ~200 globally). Durable for Anthropic specifically.

**Meta-B — Regulation.** Cornered Resource (FedRAMP High, IL5/IL6, HIPAA attestations); Counter-Positioning (AWS GovCloud, Azure Government, Palantir); Process Power (Palantir's accreditation playbook). Expanding. Very durable.

**Meta-C — Economics.** Cornered Resource (Microsoft, Google, Amazon, Meta, NVIDIA balance sheets — only ~10 entities on Earth can fund a $50B training run); Scale Economies. Very durable.

**Meta-D — Geopolitics.** Cornered Resource (compliant supply-chain access to TSMC + ASML + NVIDIA); Counter-Positioning (Huawei Ascend, SMIC — strengthening within China). Very durable — bifurcated stack is now a 10-year reality.

### The five most durable agent/AI-stack positions

1. **NVIDIA.** Cornered Resource (CoWoS, HBM allocation) + Process Power (CUDA) + Scale Economies. Three powers stacked. Durable through 2030 at training; eroding faster at inference.
2. **TSMC + SK Hynix + ASML.** Cornered Resource at the most upstream point. Physically irreplaceable for a decade.
3. **Anthropic.** Branding (safety + coding) + Process Power (Constitutional AI, interpretability) + Cornered Resource (alignment talent). Contested by OpenAI but distinctively positioned for enterprise.
4. **Microsoft + AWS + Google (hyperscaler AI clouds).** Scale Economies + Switching Costs (existing cloud lock-in) + Capital. Bedrock / Azure AI inherit decades of enterprise procurement entrenchment.
5. **Palantir.** Process Power (accreditation craft) + Cornered Resource (cleared personnel + government relationships) + Switching Costs (Foundry data ontologies). Boring, durable, underweighted.

### The five most over-rated

1. **Cursor.** Brand is hot, switching cost is one prompt and a config file; underlying moat is Anthropic's. Margin compresses as Anthropic ships its own IDE surface (Claude Code already does).
2. **Pure-play vector DBs (Pinecone, Weaviate, Chroma).** Switching costs evaporated; pgvector + Turbopuffer + every cloud killed this layer.
3. **LangChain / LlamaIndex.** Early network effect, increasingly bypassed by direct SDKs (Anthropic, OpenAI Agents SDK, Vercel AI SDK).
4. **Tier-2 frontier labs (Mistral, Cohere, AI21).** Branded as frontier; lack capital to stay there. Counter-positioning via open weights is real but a different game.
5. **Inference-as-a-service pure plays (Together, Fireworks, Anyscale).** Engineering is real but margin-compressed commodity layer; will be acquired or marginalized by hyperscalers.

### Pattern read

Durable power concentrates at the physical bottom (Strata I–III) and the vertical top (Stratum XIII vertical agents + Meta-B regulation). The middle — generic model providers, generic inference, generic retrieval, generic orchestration frameworks — is where margin and durability both compress. The barrens are exactly where the most VC dollars went in 2024–25: pure-play vector DBs, framework-as-company, inference resellers. Alex's addressable career zone hugs the vertical-top cluster. See Plate 4 for the full powers × layer grid.

![Plate 4 — Powers × Layer Grid](plates/04_powers_layer_grid.svg)

## §2.4 Ecosystem JTBD

### Why ecosystem-level (not user-level) JTBD

Standard Outcome-Driven Innovation maps a single customer's functional job through eight phases (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude) and identifies desired outcomes per phase, scored on importance versus current satisfaction. Applied at the ecosystem level rather than per product, the unit shifts. Instead of asking what Cursor is hired to do, the question becomes what is the entire AI stack hired to do, and where does composition across strata fail. The opportunities surface in the seams between layers — exactly where someone with cross-stack pattern recognition and commercial fluency has structural advantage over technical specialists. The Bettencourt–Ulwick lineage of JTBD is the right scaffold here precisely because seam failures are not visible from inside any one product's lens.

### The 6 jobs

**Job 1 — Run a complete enterprise sales motion using AI as primary leverage.**
When a revenue leader needs to compress cost-per-meeting and shorten sales cycles in a 12-stage motion (ICP through outreach, discovery, demo, MEDDPICC, procurement, close, expansion), they want to substitute AI for the marginal SDR/AE hours on every stage that does not require relational judgment, so headcount scales sub-linearly to pipeline.

- Detecting AI-generated outreach (gap 7) — buyer fatigue tolerance dropped sharply in 2025; the field optimizes for volume, not authenticity.
- Mapping the actual buying committee (gap 7) — the field sells contact data; nobody sells the graph of who-influences-whom.
- Detecting and diagnosing a stalling deal (gap 6) — Gong/Clari surface activity, not causal diagnosis.

**Job 2 — Build, ship, instrument, and iterate an AI-native product as a small team.**
When a 1–10 person team is building an AI-native product, they want to compose models + retrieval + orchestration + UI + observability + evals into a deployable, measurable, iterable system, so velocity is bound by product judgment rather than integration overhead.

- Eval design that catches real production failures (gap 8) — eval-creation UIs exist; "what should I actually evaluate" advice does not.
- Causal attribution of bad outputs (gap 8) — was it the prompt, retrieval, tool, model, or user input? PostHog LLM observability is closest but does not do causal trace decomposition.
- Model migration without regression (gap 6) — every release creates silent regressions; no tool replays a corpus and diffs outputs structurally.

**Job 3 — Stay current on the AI ecosystem and act on it.**
When an operator, investor, or builder is allocating attention across an ecosystem releasing 50+ material news items per week, they want to filter signal from noise, contextualize new capability against their roadmap, and decide what to act on, so they neither fall behind nor chase every shiny object.

- Translating "X shipped" into "I should change Y" (gap 7) — Ben's Bites, TLDR AI, Latent Space stop at "X shipped." Nobody connects to your roadmap.
- Acting on signal versus hype (gap 6) — benchmarks lie, demos lie, founder threads lie; no operator-grade fact-checker.
- Personal taxonomy that survives evolution (gap 6) — last year's category labels (RAG, agents, CoT) are this year's wrong abstractions.

**Job 4 — Pass enterprise procurement, security, and compliance review for an AI vendor. [PRIORITY]**
When an AI-native vendor enters a Fortune 1000 procurement cycle, they want to satisfy InfoSec, Legal, Privacy, AI Governance, Procurement, and the business sponsor — six counterparties with non-overlapping demands — so the deal closes within the buyer's planning cycle rather than slipping two quarters. This is the priority job. It uniquely composes Alex's three rarest assets: enterprise procurement scar tissue, AI-builder fluency, and a current incentive to publish.

- The AI-specific contract addendum negotiation (gap 8) — every deal renegotiates training-data rights, output ownership, model-update notice, and hallucination indemnity from scratch.
- Mapping the buyer's AI governance org (gap 8) — most enterprises stood up an AI council in 2024–25; org charts have not caught up. Sellers waste 4–8 weeks finding the right approver.
- Capturing precedent across deals (gap 8) — every AE re-learns "how Walmart approves AI vendors" instead of inheriting institutional knowledge.

**Job 5 — Recruit, evaluate, and ramp talent in AI-native roles.**
When a hiring manager needs to fill an AI-native role (Forward-Deployed Engineer, AI PM, Applied AI Scientist, AI-native AE), they want to define the role, screen for capability that did not exist 24 months ago, and ramp the hire against a moving target, so the team's average AI fluency rises with each hire rather than regressing to legacy norms.

- Filtering for verifiable AI-native experience (gap 7) — LinkedIn is now 90% noise on AI titles.
- Screening builders versus prompters (gap 7) — interview loops have not caught up.
- Role re-specification cadence (gap 6) — most JDs are 12+ months stale.

**Job 6 — Govern AI usage across an enterprise.**
When a CIO / CISO / CDO is accountable to a board for what AI is used here, by whom, on what data, with what risk profile, they want a defensible, auditable, low-friction governance regime, so the enterprise neither blocks productive usage nor lands on the front page of the WSJ.

- Shadow AI discovery (gap 7) — Netskope/Zscaler/Harmonic do partial discovery; nobody covers AI features embedded in Notion, Slack, Salesforce.
- Low-friction enforcement (gap 7) — most policies are PDFs; enforcement is reactive.
- Board-ready usage reporting (gap 6) — boards now ask quarterly; CIOs scramble.

### Cross-job synthesis

Three underservice patterns repeat across all six jobs. **Causal attribution and diagnosis across multi-stratum systems** — appears in Job 1 (why is the deal stalling?), Job 2 (why is the LLM output wrong?), Job 4 (which counterparty is blocking?), and Job 6 (where is shadow AI?). The ecosystem is good at surfacing data, terrible at answering why. **Translation from capability to action** appears in Jobs 1, 3, and 5: the ecosystem rewards capability announcements; nobody owns the translation layer for a specific operator persona. **Cross-counterparty workflow orchestration in the enterprise** appears in Jobs 4 and 6: the enterprise has 6+ approvers with non-overlapping interests, and no tool models the workflow as a multi-counterparty negotiation. Job 4 dominates the priority ranking because it is the only one of the six where Alex's three rarest assets — buyer-side procurement scar tissue, AI-builder fluency, and current publishing incentive — compose into a position with almost no qualified competition. Buyer personas: Job 1 RevOps/Sales Ops; Job 2 Head of Applied AI; Job 3 VC Operating Partner; Job 4 Head of Enterprise Sales / Trust & Security GTM; Job 5 Head of Talent; Job 6 CIO/CISO. Job 4's buyer also has the largest budget and the longest cycle.

## §2.5 Talent & Capital Flow methodology

### What we track

- **Senior frontier talent moves** — director-level and above, comp packages above $500K, capability-cluster moves where two or more researchers move together or one senior IC takes their team across.
- **Capital events** — $100M+ rounds, M&A above $50M, infrastructure commitments above $1B, GPU/HBM allocation announcements.
- **ARR signals** — disputed-range tolerated and recorded (OpenAI ~$24B versus Anthropic $19B–$30B disputed); we log the range, the source, the date, and the dispute.
- **Public statements as decoded signal** — what does a frontier-lab CEO saying X in March imply for what they will ship by September; statements logged with hypothesis attached.
- **NYC-specific cuts** — vertical-agent moves into Alex's exact profile band (12+ years enterprise B2B + AI fluency + NYC) are double-weighted because they are addressable, not just informative.

### Cadence

Bi-weekly cadence for the rolling tables (talent moves, capital events). Trigger-based logging for one-off signals — a single major statement, a ship event, a court ruling. Monthly synthesis to feed bet re-rating. The full tables and the operating discipline that drives the cadence live in Ch 4 §4.3–§4.7.

### Signal versus noise rules

- Single moves are noise; capability-cluster moves (two or more senior researchers, or an entire team) are signal.
- Any individual package above $100M is signal regardless of who — it reprices the talent market mechanically.
- Any NYC vertical-agent hire matching Alex's profile band is double-weighted — addressable, not just observable.
- A capital event without an accompanying public deployment milestone is half-weighted; with a milestone, full weight.
- ARR figures from a single source are flagged; figures triangulated from three independent sources are logged as range, not point.

### Pointer

Methodology only here. Data tables live in Ch 4 §4.3 (talent), §4.4 (capital), §4.5 (ARR), §4.6 (public statements decoded), §4.7 (NYC snapshot).

## Apply

Pick one of the following. Twelve minutes, with a date stamp, so the result is rotatable next month.

- Score one new opportunity you heard about this week against the OCQ lens. What does it total /15 across the three dimensions? Where does it sit on the Wardley map — Pioneer, Settle, Consume, or Utility? If it scores above 13/15 on opportunity AND sits in Settle, it earns a Chapter 3 bet review.
- Pick one of the six JTBD jobs and write one underserved outcome you observed this week that the addendum did not capture. Phrase it as a desired outcome with a direction, unit, object, and context (Bettencourt structure). If the gap is above 6 in your own estimation, log it as a candidate Job 7 expansion.
- Identify one of Helmer's powers that is eroding in a stratum you operate in. What's the leading indicator — pricing compression, talent migration, a new entrant counter-positioning? If the indicator moved this month, the bet attached to that power needs a re-rate in Ch 3.

Log the result with date and the drill chosen. Rotate next month so all three drills get used quarterly.
