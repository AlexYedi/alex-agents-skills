# Chapter 1 — The Substrate

The AI stack is one connected system from the electrical grid to the end user. Stratifying it into discrete layers is an analytical move, not a description of nature. The purpose is to make scaling constraints, pricing logic, and competitive position legible — to ask, at each layer, what binds, who owns the choke point, and how the layer below reprices the layer above when it moves.

This chapter cuts the stack into fourteen primary strata plus four meta-strata that wrap the whole column. The numbering and naming match the original report so cross-references in the tracker remain valid. Strata I–V cover the physical substrate (power, facility, compute, fabric, parallelism). Strata VI–VIII cover the data and training pipeline. Strata IX–XIV cover inference, middleware, application, and the user. Meta-A through Meta-D — safety, regulation, economics, geopolitics — apply across every layer rather than at any single one.

Each stratum entry follows the same four-part structure: **Position** (what it is, what it depends on, what depends on it); **What lives there** (named players, binding metrics, 2026 datapoints); **Binding constraints** (what limits scaling now); **Evolution stage** (Wardley: Genesis, Custom-Built, Product, or Commodity/Utility); **What changed in the last 12 months** (two to three dated datapoints). Read top to bottom for a full pass, or jump to a stratum to refresh one node. Plate 1 (Substrate Column) is the visual key.

![Plate 1 — Substrate Column](plates/01_substrate_column.svg)

## Part I — Power and Facility

### Stratum I — Power

**Position.** The base layer. Every layer above runs on electrons that have to be generated, transmitted, and delivered to a transformer pad at a data-center site. Power gates every other constraint — chips, racks, models — because compute without firm dispatchable power is a press release. Power depends on generation, transmission, transformer manufacturing, and regulatory siting; everything above depends on it.

**What lives there.**
- Global data-center electricity demand reached ~485 TWh in 2025; projected 950–1,100 TWh by 2030, roughly 3% of global electricity (IEA, 2026-01).
- US data centers projected at 9–17% of US generation by 2030 vs. 4% in 2023 (EPRI, 2026).
- Hyperscaler PPAs: Microsoft 835 MW Three Mile Island restart (Crane Clean Energy Center, online 2027); Amazon 1,920 MW Susquehanna + 5 GW X-energy SMR by 2039; Google 500 MW Kairos SMR (2030–2035); Meta >7 GW Entergy gas for Hyperion (Louisiana); xAI ~35 Solar SMT-130 turbines onsite at Memphis Colossus.
- PJM 2025/26 base residual auction cleared $269.92/MW-day system-wide, $444.26/MW-day in Dominion zone — an 833% YoY increase, ~63% attributed to data-center load (PJM, 2025-12).
- SMR vendors: NuScale (NRC-approved, 77 MWe), X-energy Xe-100 (80 MWe HTGR), Kairos KP-FHR, TerraPower Natrium.

**Binding constraints.** Power transformer lead times ~120 weeks with a 30% supply deficit through 2025 (Wood Mackenzie, 2025); interconnection queue ~1,400 GW of generation plus 890 GW of storage; transmission permitting horizons ~10 years. Generation is not the bottleneck — transformers and interconnect are.

**Evolution stage.** Commodity/Utility for incumbent grid; Genesis for SMR-powered AI campuses. SMRs will not deliver commercial MWh before 2028–2030.

**What changed in the last 12 months.**
- FERC rejected the behind-the-meter Talen-Amazon ISA twice (Nov 2024, Apr 2025); restructured to front-of-meter PPA, no FERC approval required.
- Stargate Abilene flagship went live on Oracle Cloud Infrastructure (Sep 2025).
- Meta announced >7 GW Entergy gas for Hyperion Louisiana over a 15-year horizon (Mar 2026).

### Stratum II — Facility

**Position.** The mechanical and electrical envelope around the compute. Sized first for power, then for fiber. Depends on Stratum I (electrons), and on transformer and switchgear delivery; gates Strata III–V (no rack lands without cooling and busbar). The Blackwell-era rack — 132 kW liquid-cooled — broke the assumptions of every air-cooled data center built before 2023.

**What lives there.**
- Critical-IT-load capex: $10–12M per MW fully built (Cushman & Wakefield, 2025); MEP 50–60%; greenfield delivery 18–36 months.
- Rack power trajectory: H100 HGX 10–15 kW → GB200 NVL72 132 kW → Rubin Ultra Kyber ~600 kW (2027).
- Cooling: direct-to-chip liquid is production default for GB200; rear-door HX retrofits up to ~80 kW; single-phase immersion at hyperscale; two-phase retreated under PFAS pressure.
- PUE: industry average 1.55–1.60; hyperscale best-in-class 1.10–1.20; Google fleet TTM 1.09.
- Open Compute Project Open Rack v3: 48 V DC, vertical busbars to 1,000 A, blind-mate connections, rack-level BBUs.
- Operators: Equinix, Digital Realty, QTS (Blackstone), CyrusOne (KKR), STACK (IPI), Aligned (Macquarie); neoclouds CoreWeave (850 MW operational, ~600,000 GPUs, $66.8B contracted backlog), Lambda, Crusoe, Nebius, Together, Voltage Park, Applied Digital.
- Flagship 2025 builds: Stargate Abilene; Meta Hyperion (>7 GW, Louisiana); Meta Prometheus (~1 GW, Ohio); xAI Colossus 1 and 2 (Memphis); Microsoft Mt Pleasant (>5 GW, Wisconsin); Stargate UAE 1 GW (authorized Nov 2025).

**Binding constraints.** Transformer and switchgear lead times; liquid-cooling manifold and CDU supply; water permitting in arid regions (WUE below 0.20 L/kWh is the target). The retrofit base of air-cooled colos is mostly stranded above 80 kW per rack.

**Evolution stage.** Product for hyperscale facility design; Custom-Built for AI-factory-scale campuses (Stargate-class is bespoke); Genesis for Kyber-class 600 kW racks.

**What changed in the last 12 months.**
- GB200 NVL72 shipped at scale; 132 kW liquid-cooled racks are now the default unit.
- Stargate UAE 1 GW authorized by US Commerce Department (Nov 2025).
- NVIDIA published Kyber 600 kW rack reference for Rubin Ultra (Mar 2026, GTC).

## Part II — Compute and Networking

### Stratum III — Compute

**Position.** The silicon that runs training and inference. Depends on facility (power, cooling, rack), HBM and CoWoS-L packaging (Stratum III sub-supply), and TSMC leading-edge logic. Gates Stratum VII (pretraining) and Stratum X (inference economics).

**What lives there.**
- NVIDIA holds ~80% frontier accelerator share at >75% gross margins. Lineage: Hopper (H100, H200) → Blackwell (B100, B200, GB200, GB200 NVL72: 36 Grace + 72 Blackwell, 132 kW, 13.5 TB HBM3e) → Blackwell Ultra (B300, 288 GB HBM3e, 1,400 W, H2 2025) → Rubin NVL144 (H2 2026, HBM4 at 13 TB/s per GPU) → Rubin Ultra NVL576 "Kyber" (H2 2027, ~600 kW, 365 TB HBM4e, 4.6 PB/s) → Feynman (2028, co-packaged optics standard).
- AMD: MI300X / MI325X / MI355X (CDNA 4, 288 GB HBM3e, ~20 PFLOPS FP4); ROCm 7 closed the kernel-parity gap; MI400 "Helios" rack-scale in 2026. Intel cancelled Falcon Shores Jan 2025; Jaguar Shores repositioned as rack-scale.
- Hyperscaler ASICs: Google TPU v7 Ironwood (192 GB HBM3e per chip, 9,216-chip pods, 42.5 FP8 ExaFLOPS per pod) anchors Anthropic and Apple; AWS Trainium 3 (Dec 2025, 3 nm, 144 GB HBM3e, 2.52 PFLOPS FP8) underpins Anthropic Project Rainier (~400,000 chips); Microsoft Maia 200 (TSMC 3 nm, 216 GB HBM3e); Meta MTIA on v300/400/450/500 cadence; Apple M5 (Oct 2025, ~4× M4 GPU compute).
- Inference startups: Cerebras WSE-3 (4T transistors, >1,000 tok/s on Llama 3.1-405B); Groq LPU (~750 tok/s on Llama 3.1-8B); SambaNova RDU SN40L; Tenstorrent (Wormhole, Blackhole, RISC-V); Etched Sohu (transformer-only ASIC).

**Binding constraints.** HBM (SK Hynix ~62% share, Micron 21%, Samsung 17%; 2026 capacity pre-booked by NVIDIA and OpenAI before year began) and TSMC CoWoS-L (75–80 KWPM end-2025, targeting 120–130 KWPM end-2026). Without CoWoS-L allocation, leading-edge dies are stranded inventory.

**Evolution stage.** Product for Hopper and Blackwell; Custom-Built for Rubin Ultra rack-scale systems; Genesis for transformer-only ASICs and wafer-scale.

**What changed in the last 12 months.**
- NVIDIA acquired Run:ai (FTC review closed Jan 2025), open-sourced KAI scheduler, acquired SchedMD/Slurm (Dec 2025).
- H20 export halt (Apr 2025) then reversal (Jul 2025); NVIDIA China share fell from ~95% to ~55% as Huawei Ascend 910C/920 absorbed the gap.
- TSMC announced an additional $100B US investment in Mar 2025 (total commitment $165B).

### Stratum IV — Fabric

**Position.** The interconnect that turns thousands of GPUs into one training run or one inference cluster. Three sub-layers: scale-up (inside an NVLink domain), scale-out (across racks and pods), and the optical layer increasingly binding them. Depends on switching ASICs and optics; gates parallelism (Stratum V) and effective MFU.

**What lives there.**
- Scale-up: NVLink 4 (900 GB/s, Hopper) → NVLink 5 (1.8 TB/s, Blackwell) → NVLink 6 (~3.6 TB/s, Rubin) → NVLink 7 (1.5 PB/s aggregate, Rubin Ultra). GB200 NVL72 uses ~5,000 NVLink copper cables — no optics inside the rack. UALink 1.0 (Apr 2025, 200 Gbps/lane, up to 1,024 accelerators; AMD/Intel/Apple/Alibaba/AWS/Cisco/Google/HPE/Meta/Microsoft promoters); first silicon late 2026 / early 2027.
- Scale-out: NVIDIA Quantum-X800 InfiniBand (XDR, 800 Gb/s, sub-100 ns latency); Spectrum-X Ethernet (51.2 Tb/s, RoCE-optimized; xAI Colossus reportedly hit 95% throughput vs. ~60% on commodity Ethernet); Broadcom Tomahawk 6 "Davisson" (102.4 Tb/s, Jun 2025); Cisco Silicon One P200 (51.2 Tb/s, 1,000 km coherent); Ultra Ethernet Consortium 1.0 (Jun 2025).
- DPUs/SmartNICs: NVIDIA BlueField-3 (400 Gb/s) and BlueField-4 (Oct 2025, 800 Gb/s with Grace + ConnectX-9); AMD Pensando Pollara 400 (UEC-aligned); AWS Nitro v5; Intel IPU E2100.
- Optics: 800 G default for AI builds; 1.6 T in 2026; LPO cuts module power 30–50%; CPO shipping in Quantum-X Photonics (H2 2025) and Spectrum-X Photonics (2026). Lightmatter (Passage M1000, ~$4.4B valuation), Ayar Labs (TeraPHY chiplet).
- Storage fabric: GPUDirect Storage 40+ GB/s per host; WekaIO, VAST Data, DDN EXAScaler (4 TB/s to NVIDIA Eos), IBM Storage Scale, Pure FlashBlade.

**Binding constraints.** Optics availability and CPO serviceability; switching-ASIC supply; protocol fragmentation between InfiniBand, Ethernet (UEC), and UALink. Vendor lock at the scale-up layer is structural: there is no open NVLink today.

**Evolution stage.** Product for InfiniBand and 800 G Ethernet; Custom-Built for rack-scale NVLink and CPO; Genesis for UALink silicon.

**What changed in the last 12 months.**
- Ultra Ethernet Consortium published 1.0 spec (Jun 2025).
- Broadcom Tomahawk 6 launched as first single-die 100+ Tb/s switch (Jun 2025).
- NVIDIA BlueField-4 at 800 Gb/s with integrated Grace (Oct 2025).

### Stratum V — Parallelism

**Position.** The software discipline that lets a training run span tens of thousands of GPUs without falling off a cliff in effective utilization. Depends on fabric bandwidth and on collective-communication libraries; gates pretraining cost and feasibility (Stratum VII).

**What lives there.**
- "4D parallelism" — Data, Tensor, Pipeline, Expert — is the frontier default. Typical recipe: TP=8 inside NVLink domain, PP=8 across nodes, DP across pods, EP for MoE layers.
- Frameworks: PyTorch FSDP2 (DTensor-based) and Megatron-LM / Megatron-Core dominate NVIDIA; DeepSpeed retains substantial install base; JAX with `jit` and `shard_map` dominates TPU.
- Kernel layer: FlashAttention 2/3 (FA3: 75% MFU on H100, 1.2 PFLOPs/s FP8); OpenAI Triton; ThunderKittens.
- Collectives: NCCL on NVIDIA; RCCL (AMD); OneCCL (Intel); SHARP v4 runs collectives inside the InfiniBand switch fabric.
- MFU: 50–70% on best-in-class frontier runs.
- Failure rates at scale: Meta Llama 3.1 405B training run experienced 419 interruptions in 54 days, roughly one every three hours.

**Binding constraints.** Sub-second restart from in-memory checkpoints is the next bar; current checkpoint recovery still dominates wall-clock loss. Software-engineer talent for systems-level training infra is thin and expensive. Failure-mode complexity scales super-linearly with cluster size.

**Evolution stage.** Product for FSDP/Megatron/JAX recipes at known scales; Custom-Built for >100k-GPU runs; the recipe knowledge itself is a Cornered Resource at a handful of frontier labs.

**What changed in the last 12 months.**
- FlashAttention-3 published, reaching 75% MFU on H100 (Jul 2024 paper, mainstream adoption through 2025).
- NVIDIA acquired SchedMD (Slurm) Dec 2025, completing scheduler consolidation that started with Run:ai.
- Slurm now runs inside Kubernetes via Slinky CRDs.

## Part III — Data, Pretraining, Post-training

### Stratum VI — Data

**Position.** The training corpus — pre-training mix, post-training labels, evaluation sets. Depends on web crawling, licensing deals, synthetic generation, and copyright law. Gates the legal defensibility and the capability ceiling of every model above it.

**What lives there.**
- Substrate: Common Crawl. Derived: RefinedWeb, RedPajama-Data v2 (30T tokens, 84 CC dumps), FineWeb (15T tokens, 96 snapshots), FineWeb-Edu (1.3T tokens, Llama-3-70B classifier), Dolma (AI2, 3T fully documented), Nemotron-CC v2 (NVIDIA, 6.3T including 1.9T synthetic).
- Code: BigCode The Stack v2 (67.5 TB raw, ~900B training tokens, SWHID-traceable, opt-out, PII-scrubbed).
- Multilingual: CulturaX (167 languages), mC4, ROOTS, OSCAR, FineWeb-2 (1,000+ languages).
- Multimodal: Re-LAION-5B, DataComp/CommonPool (12.8B image-text pairs), COYO, DOCCI.
- Synthetic share: Nemotron-CC's 1.9T synthetic tokens; Microsoft Phi family entirely synthetic; teacher distillation universal (Llama 4 Behemoth → Maverick/Scout, Gemini Ultra → Flash, R1 → R1-Distill). Pretraining mix is now 20–50% model-generated at most labs.
- Tokenizers: tiktoken (BPE, 200k vocab on GPT-4o); SentencePiece (Gemini, Gemma, T5); Hugging Face tokenizers.

**Binding constraints.** Three layers: (1) copyright — Bartz v. Anthropic settled Aug 2025 for $1.5B across ~500,000 books at ~$3,000 each, the largest copyright recovery in US history; lawful corpora = fair use, pirated = infringement; (2) crawl access — Cloudflare default-blocked AI crawlers across new domains Jul 2025 with managed robots.txt and a Pay-Per-Crawl HTTP 402 system, citing OpenAI's 1,700:1 crawl-to-referral ratio and Anthropic's 73,000:1; (3) provenance — EU AI Act August 2026 transparency provisions will entrench C2PA-class watermarking as compliance baseline in Europe.

**Evolution stage.** Product for licensed and synthetic pipelines; Custom-Built for frontier-lab data engineering; Commodity for Common Crawl raw substrate.

**What changed in the last 12 months.**
- Bartz v. Anthropic settled Aug 2025 — first priced copyright training liability.
- Cloudflare default-block live Jul 2025; OpenAI / Anthropic crawler asymmetry now industry-known.
- Nemotron-CC v2 released Q1 2025; beat DCLM and FineWeb-Edu via classifier ensembling.

### Stratum VII — Pretraining

**Position.** The training run that produces a base model. Depends on data (Stratum VI), parallelism (V), fabric (IV), compute (III). What lives above: post-training (VIII) and everything downstream.

**What lives there.**
- Architecture: decoder-only Transformer remains the trunk. Attention evolved MHA → MQA → GQA → MLA (DeepSeek Multi-head Latent Attention: 32× KV cache compression, ~20× speedup).
- Mixture-of-Experts dominates above ~70B: Mixtral 8×7B/8×22B; DeepSeek V2 (236B / 21B active), V3 (671B / 37B active, claimed $5.6M compute on 2,048 H800s); Llama 4 Scout (109B / 17B, 16 experts), Maverick (400B / 17B, 128 experts + 1 shared), Behemoth (~2T / 288B); Qwen 3/3.5 (Apache 2.0, toggleable thinking); Mistral Large 3 (~675B / 41B, Apache 2.0).
- Non-Transformer: Mamba/Mamba-2 SSMs; hybrid Jamba; Inception Labs Mercury diffusion LM (1,109 tok/s on H100, ~10× autoregressive).
- Multimodal: SigLIP 2 vision encoders feeding Gemma; Chameleon and Show-o VQ-VAE image tokenization; Janus/Janus-Pro decoupled encoding paths.
- Position encoding: RoPE universal; YaRN dominant for context extension.
- Compute costs: GPT-4 ~$78–100M compute, ~$200M+ all-in; Llama 3.1 405B ~$170M compute on >$500M program; frontier next-gen runs in the $1B+ range. Hardware 47–67% of total cost; R&D personnel 29–49%.
- Scaling: Chinchilla recommends ~20 tokens per parameter for compute-optimal; inference economics push the opposite way (Llama 3 8B trained on 15T tokens, ~1,875 tokens per parameter — suboptimal for training but optimal for inference lifetime).

**Binding constraints.** Cluster availability, electricity at site, HBM allocation, and training-systems talent. Beyond ~$1B per run, capex commitment to the next-gen model is a board-level decision.

**Evolution stage.** Product for the recipe; Custom-Built for the frontier runs themselves; Commodity is not in sight — pretraining is concentrating, not commoditizing.

**What changed in the last 12 months.**
- DeepSeek V3 demonstrated frontier-tier outcomes on ~60%-of-H100 silicon with strong systems engineering (Dec 2024).
- Llama 4 herd shipped natively multimodal MoE (Apr 2025).
- Mistral Large 3 went Apache 2.0 (2025) — open-weight permissive licensing converged at frontier scale.

### Stratum VIII — Post-training

**Position.** What turns a base model into a useful assistant or reasoner. Depends on the base model (VII) and on annotation, verification, and RL infrastructure. Gates capability per parameter — the single largest lever above compute since 2024.

**What lives there.**
- SFT on instructions remains the entry point; LIMA / Alpaca lesson — quality dominates quantity.
- RLHF (train reward model, PPO against it) overtaken by simpler preference methods: DPO (closed-form, no explicit reward model), IPO, KTO (single-rating), ORPO (combined SFT + preference).
- Constitutional AI / RLAIF (Anthropic): LLM critic governed by written constitution; primary preference signal for Claude 4 series.
- Reinforcement Learning from Verifiable Rewards (RLVR): reward signal is unit test or symbolic verifier — eliminates reward hacking in domains where correctness is automatically checkable.
- Group Relative Policy Optimization (GRPO, DeepSeek): PPO variant that drops the value network, computes advantages relative to mean reward of a sampled group; the practical engine of the R1 family.
- Test-time compute: o1 (Sep 2024), o3 (Dec 2024), Claude extended thinking (3.7 Sonnet then 4-series with 64k thinking budgets), Gemini 2.5 Deep Think, DeepSeek R1. Small model thinking 30 seconds beats 14× larger model answering immediately.
- Distillation (Llama 4 Behemoth → Maverick/Scout; Gemini Ultra → Flash; R1 → R1-Distill on Qwen-7B/Llama-70B) and speculative decoding (EAGLE-3 at 3.0–6.5× over autoregressive baseline) close the inference-economics loop.

**Binding constraints.** Verifier coverage — RLVR only works where correctness is automatically checkable, which constrains gains to math, code, formal proofs. Reward hacking in non-verifiable domains is unresolved. Annotation talent for domain-specific reward modeling is thin.

**Evolution stage.** Product for SFT/DPO; Custom-Built for RLVR/GRPO at frontier scale; Genesis for chain-of-thought monitorability and process reward models.

**What changed in the last 12 months.**
- DeepSeek-R1 paper (Nature, Aug 2025) demonstrated pure-RL reasoning emergence without SFT cold start.
- Claude 4-series shipped 64k extended-thinking budgets (Sonnet 4.5 Sep 2025, Opus 4.5 Nov 2025).
- Frontier Model Forum published joint paper on chain-of-thought monitorability (Jan 2026).

## Part IV — Inference, Middleware, Application

### Stratum IX — Model Providers

**Position.** The API endpoint a developer or enterprise actually calls. Depends on Strata III–VIII (the models and the runtime to serve them) and on the inference engines below (X). What lives above: every application and agent that uses an LLM.

**What lives there.**
- Anthropic: Opus 4.5 ($5/$25 per million input/output tokens), Sonnet 4.5 ($3/$15), Haiku 4.5 ($1/$5). Prompt caching: 5-minute writes at 1.25× input, 1-hour writes at 2×, reads at 0.10×. Batch API at 50% discount. Combined caching + batch yields ~95% effective discount on repeated context.
- OpenAI: GPT-5 family (released Aug 7, 2025); automatic prompt caching at ≥1024 tokens, granular at 128-token boundaries; cached reads at 0.25–0.5× input price.
- Google AI / Vertex AI: Gemini 2.5 Pro and Flash with Deep Think; implicit and explicit caching; VPC-SC and IAM at Vertex tier.
- AWS Bedrock and Azure OpenAI Service: multi-model marketplaces with provisioned throughput.
- Aggregators: OpenRouter; Vercel AI Gateway (launched May 2025 at zero markup, forced OpenRouter to drop fees on first 1M BYOK requests Oct 2025).
- Inference clouds running 200+ models on owned GPUs: Fireworks, Together AI, DeepInfra, Lepton, Modal, Baseten, Replicate, Anyscale, RunPod.
- Custom-silicon clouds: Cerebras (~3,000 tok/s on GPT-OSS-120B), Groq (~750 tok/s on Llama 3.1-8B with deterministic latency), SambaNova (~580 tok/s on Llama 3.1-70B, ~129 tok/s/user on 405B).
- Latency: MLPerf Inference 5.1 interactive scenario for 8B-class specifies TTFT ≤ 0.5s and TPOT ≤ 30ms.

**Binding constraints.** Per-token frontier pricing eroded 4–10× vs. 2024, partially offset by reasoning models consuming 100–10,000× more inference compute per query. Inference compute supply, not algorithmic ceiling, gates aggregate revenue.

**Evolution stage.** Product. Pricing is converging; the surface is differentiated by latency tier, caching mechanics, and rate-limit policy more than by raw model quality.

**What changed in the last 12 months.**
- GPT-5 launched with unified architecture and built-in router (Aug 2025).
- Claude Opus 4.5 and Sonnet 4.5 shipped (Sep–Nov 2025) with 64k thinking budgets.
- Vercel AI Gateway launched at zero markup (May 2025); OpenRouter dropped BYOK fees on first 1M requests (Oct 2025).

### Stratum X — Inference Engines

**Position.** The serving runtime that turns model weights into tokens at a target latency and cost. Depends on compute, fabric, quantization recipes, and KV-cache management; gates everything an application can afford to do.

**What lives there.**
- vLLM (now under PyTorch Foundation) is the open-source default. Primitives: PagedAttention (KV cache as virtual memory addressed via block tables), continuous batching at iteration-level scheduling, chunked prefill.
- SGLang: RadixAttention (radix tree of KV prefixes, 85–95% prefix hit rate on few-shot vs. vLLM's 15–25%); compressed FSM for constrained decoding (3× faster JSON, up to 6.4× higher throughput on agent/RAG/JSON workloads). Day-one DeepSeek V3/R1 support Jan 2025.
- NVIDIA Dynamo (GTC 2025): disaggregated prefill/decode (compute-bound and memory-bound on separate GPU pools), LLM-aware routing exploiting KV locality, KV-cache offloading HBM → DRAM → SSD, async GPU-to-GPU via NIXL.
- TensorRT-LLM: NVIDIA first-party LLM stack with FP8/FP4 quantization.
- Local/consumer: llama.cpp / GGUF underpins Ollama, LM Studio, Jan.ai. PyTorch ExecuTorch 1.0 (50 KB runtime, 12+ hardware backends) is the official on-device runtime. Apple MLX exploits unified memory zero-copy on Apple Silicon.
- Speculative decoding: EAGLE-3 (NeurIPS 2025) at 3.0–6.5× over autoregressive via training-time-testing with low/mid/high feature fusion.
- Quantization: FP8 default on Hopper/Blackwell; NVFP4/MXFP4 doubles throughput on Blackwell; AWQ beats GPTQ at 4-bit on outlier-prone activations; SmoothQuant migrates dynamic range from activations to weights for W8A8; GGUF imatrix (IQ) quants dominate consumer with Q4_K_M as typical sweet spot.

**Binding constraints.** KV-cache memory dominates context-length economics; quantization quality at FP4 still has open holes on long-context reasoning; serving heterogeneous reasoning + non-reasoning traffic on the same pool is unsolved.

**Evolution stage.** Product. vLLM/SGLang/TensorRT-LLM are mature and converging. Disaggregated prefill/decode (Dynamo) is Custom-Built crossing toward Product.

**What changed in the last 12 months.**
- NVIDIA Dynamo announced at GTC 2025 — positioned as "the inference operating system for AI factories."
- vLLM moved under PyTorch Foundation governance (2025).
- XGrammar became default constrained-decoding backend in vLLM/SGLang/TensorRT-LLM (Mar 2026, <40 µs per token).

### Strata XI–XII — Retrieval, Memory, Orchestration

**Position.** The middleware band that turns a model API into an agent doing work. Three sub-areas, treated jointly because in production they are inseparable: retrieval gets the right context in; memory persists state across turns and sessions; orchestration chains tool calls, model calls, and control flow. Depends on model providers (IX) and inference engines (X); gates the entire application layer (XIII) — without this band, an LLM is a chat box.

**What lives there.**

Retrieval. The vector-DB market has stratified by latency and operational posture. Independent benchmarks place Qdrant at the latency frontier (~2 ms p99) above FAISS, Milvus, Pinecone, and Weaviate. Selection: Pinecone for managed zero-ops; Qdrant for filtered-search latency; Weaviate for hybrid (vector + BM25) and multimodal; Chroma for dev-local; Milvus/Zilliz for billion-vector scale; LanceDB for embedded multimodal lakehouse; pgvector + pgvectorscale when Postgres already exists; Turbopuffer for object-storage-backed multi-tenant. Graph: Neo4j, Memgraph, ArangoDB, Neptune, KuzuDB, FalkorDB.

Embedding leaders: Voyage AI voyage-3-large (acquired by MongoDB; SOTA on MTEB retrieval); OpenAI text-embedding-3-large; Cohere embed v4; NVIDIA NV-Embed-v2; Nomic Embed v2; BAAI BGE-M3 (100+ languages); Jina v5; Mistral embed. Matryoshka embeddings (truncatable without quality cliff) are standard. Rerankers — the highest-ROI single addition to a RAG pipeline — include Cohere Rerank 4, Voyage Rerank 2.5, mxbai-rerank, Jina Reranker v2. Best-practice pipeline: dense + sparse (BM25 or SPLADE) + reciprocal rank fusion + cross-encoder reranker yields 15–30% better retrieval accuracy than pure vector search.

Knowledge-graph-from-text frameworks: Microsoft GraphRAG (Leiden clustering, community summaries); HippoRAG / HippoRAG2 (neurobiologically-inspired personalized PageRank); PathRAG; OG-RAG. Substantial multi-hop accuracy gains over flat vector search.

Memory. Long-term memory became a discrete sub-stratum in 2025. Mem0 offers transparent vector + graph integration. Letta (formerly MemGPT) treats memory as agent-editable state via tool calls. Zep tracks temporal knowledge graphs. Cognee provides cognitive-architecture-inspired layers. The Crux question (see Ch 3 §3.7) is whether long-term memory remains standalone or gets absorbed into model providers' native context handling.

Orchestration. Three layers. Python-first frameworks: LangChain 1.0 / LangGraph 1.0 / LangSmith (dominant; LangSmith added Insights Agent for production trace clustering and Multi-Turn Evals in 2025); LlamaIndex (RAG and document-heavy); DSPy (Stanford, with MIPROv2 prompt optimizer); TextGrad (prompts as differentiable); Haystack (deepset); Semantic Kernel converging with AutoGen into Microsoft Agent Framework. TypeScript: Vercel AI SDK is the default with `streamText`, `generateObject` (Zod-typed), tool calling, agents, MCP integration; Mastra (YC W25, $13M seed) layers memory, workflows, evals, observability on top of AI SDK; Pydantic AI is the strict-typing path.

Vendor agent SDKs converged in 2025: OpenAI Agents SDK (Mar 2025; cleanest handoff model — `transfer_to_agent_b` is a tool call carrying conversation history; strong voice integration); Google ADK (Apr 2025; hierarchical agent trees, multi-language, deep Vertex AI integration); Anthropic Claude Agent SDK (deepest MCP integration, computer-use focus). Heuristic: Claude wins reasoning quality, OpenAI wins developer experience, Google wins cost. CrewAI, AutoGen/AG2, Smolagents in the multi-agent layer. Non-developer: n8n + AI nodes, Zapier AI, Make.com.

Model Context Protocol, published by Anthropic in Nov 2024, became the integration substrate. The Nov 2025 spec release reported 97M monthly SDK downloads, 10,000+ active MCP servers in production, hundreds of MCP clients, 5,800+ connectors in the registry. OpenAI, Hugging Face, and LangChain adopted MCP across 2025. In Dec 2025 Anthropic donated MCP to the Linux Foundation's Agentic AI Foundation, co-founded with Block and OpenAI.

Computer-use agents are the largest single capability shift of 2025: Anthropic Computer Use (Oct 2024); Claude for Chrome (Aug 2025, expanded to Pro/Team/Enterprise Dec 2025); OpenAI Operator (Jan 2025, merged into ChatGPT Agent — Operator scored 87% on WebVoyager vs. Anthropic Computer Use at 56%); Google Project Mariner (I/O 2025, 10 simultaneous tasks for AI Ultra).

Adjacent: AI gateways (Vercel AI Gateway, Cloudflare AI Gateway, Portkey, Helicone, LiteLLM, Kong); observability (LangSmith, Langfuse, Arize AX/Phoenix, Datadog AI Observability); eval (Promptfoo — acquired by OpenAI 2025; Braintrust — PR-blocking at Perplexity/Airtable/Replit; Patronus, DeepEval, OpenAI Evals, Langfuse); guardrails (NVIDIA NeMo Guardrails, Guardrails AI, Lakera, Protect AI, Bedrock Guardrails, Llama Guard); constrained generation (Outlines, Instructor, XGrammar, llguidance).

**Binding constraints.** Standards fragmentation across agent SDKs; memory schemas are not interoperable; eval rigor at the application layer is uneven. MCP being a commons vs. a fork (Crux 3, see Ch 3 §3.7) is the H2 2026 question — adoption is broad but governance is new.

**Evolution stage.** Product for vector DBs, AI gateways, observability; Custom-Built for agent orchestration and memory; Genesis for computer-use agents and GraphRAG.

**What changed in the last 12 months.**
- MCP donated to Linux Foundation Agentic AI Foundation (Dec 2025).
- Voyage AI acquired by MongoDB (2025); Promptfoo acquired by OpenAI (2025).
- Mastra raised $13M seed (YC W25) — TypeScript agent stack consolidating.
- Computer-use agents crossed from demo into production at Operator/Mariner/Claude-for-Chrome scale (2025).

### Stratum XIII — Application Layer

**Position.** The product a user buys or uses. Depends on the entire stack below; what lives above is the user themselves (XIV). This is where domain workflow knowledge becomes a moat and where revenue accrues to people, not chips.

**What lives there.**
- Consumer chat: ChatGPT 64.5% share at end-2025 (down from 86.7% at start of 2025; weekly users doubled to ~900M); Google Gemini 21.5% (year's biggest gainer, ~400M MAU); Microsoft Copilot ~14%; Perplexity ~$20B valuation, 780M monthly queries; Claude.ai ~3.2% (concentrated technical/professional); Grok 2.9%.
- Coding: GitHub Copilot incumbent (multi-model since 2025); Cursor (precision tool for large codebases); Windsurf (acquired by Cognition for $250M after Google acqui-hired founders); Cline (dominant OSS Cursor alternative); Aider, Continue, Cody, Tabnine, JetBrains AI. Replit Ghostwriter/Agent grew ARR $10M → $100M in nine months.
- AI app builders: Bolt.new, v0 (Vercel), Lovable ($20M ARR in two months), StackBlitz.
- Agentic coding: Claude Code (Anthropic terminal agent, Feb 2025); OpenAI Codex CLI; Devin (Cognition, 13.9% SWE-bench Verified; Devin 2.0 added Interactive Planning); Factory; Augment Code ($252M Series B at $977M valuation); Sweep; Reflection AI; Greptile.
- Productivity: Microsoft 365 Copilot ($30/user/month); Google Workspace Gemini (bundled); Notion AI, Slack AI, Coda AI, Mem, Granola (heavily used by executives), Read AI.
- Creative: Midjourney v7, Flux 1.1 Pro, Ideogram 2.0, Imagen 4, GPT Image 2, Recraft V4, Adobe Firefly Image 3 (only major model with formal commercial indemnification); video — Sora 2, Veo 3.1, Runway Gen-4, Kling 3.0 Omni; voice — ElevenLabs, OpenAI gpt-realtime, Cartesia, Sesame, Hume; music — Suno (settled $500M with WMG Nov 2025), Udio, Stable Audio.
- Vertical / enterprise: Harvey ($5B, legal); Hippocratic AI (health); Glean ($7.2B, enterprise search); Sierra ($10B, $100M ARR Oct 2025 at 400% YoY, brand-native CX agents); Decagon ($4.5B, $35M annualized); Ema, Cresta, Forethought.

**Binding constraints.** Enterprise procurement, security, and compliance review (Job 4 in the ecosystem JTBD list, see §3.4) — the longest cycle in B2B AI sales. Distribution moats at Microsoft Copilot, Google Workspace, ChatGPT compress middle-tier app economics.

**Evolution stage.** Product for consumer chat and horizontal productivity; Custom-Built for vertical agents (Sierra, Harvey, Decagon) — workflow integration is the moat.

**What changed in the last 12 months.**
- ChatGPT share fell from 86.7% to 64.5% over 2025 as Gemini and Copilot took ground.
- Sierra reached $100M ARR at 400% YoY (Oct 2025) — vertical-agent unit economics now publicly proved.
- Windsurf acquired by Cognition for $250M after Google acqui-hired founders (2025).

### Stratum XIV — The User

**Position.** The end surface — chat, voice, IDE, browser, mobile, increasingly the operating system. Depends on every layer below; nothing depends on it (this is the top of the column). The 2025–2026 shift was on-device inference becoming useful for routine tasks, which changes where the model runs and therefore where the data goes.

**What lives there.**
- Apple Intelligence: ~3B-parameter quantized on-device model with Private Cloud Compute fallback for harder tasks; Foundation Models framework exposed to developers; Jan 2026 partnership announced to use Gemini in upcoming Siri.
- Google Gemini Nano: system-level on-device LLM via Android AICore on Pixel 8/9/10 and Samsung S24/S25.
- Microsoft / Qualcomm Copilot+ PCs: Phi-Silica running natively on Hexagon NPU; Snapdragon X2 Elite Extreme delivers 80 TOPS.
- Small language model trend (Gemma 3, Phi-4, Qwen 3 small variants, Mistral Small, Llama 3.2 1B/3B, Danube): 1B–8B parameters, INT4/FP4 quantization, <4 GB footprint, 30+ tok/s on phone NPUs.
- Surfaces: chat (ChatGPT, Claude, Gemini apps); voice (Apple Siri redesign, Alexa+, Google Assistant successor flows, Vapi/Retell/Bland in the developer tier); IDE (Cursor, Copilot, Claude Code); browser (Claude for Chrome, Operator, Mariner); mobile (Apple Intelligence, Gemini Nano).

**Binding constraints.** Battery and thermal budgets on device; consumer behavioral change ("ask the AI" vs. open the app); regulatory restrictions on minors and high-risk use cases.

**Evolution stage.** Product for chat and IDE surfaces; Custom-Built for voice and browser agents; Genesis for the hybrid on-device + cloud orchestration pattern.

**What changed in the last 12 months.**
- Apple M5 launched Oct 2025 with ~4× M4 GPU compute via per-core Neural Accelerators.
- Apple announced Gemini partnership for Siri (Jan 2026).
- Claude for Chrome expanded to Pro/Team/Enterprise tiers (Dec 2025).

## Part V — The Meta-Strata

### Meta-A — Safety and Alignment

**Position.** A horizontal layer that wraps every stratum above. Not a stack-level technology; a governance and research discipline. Depends on interpretability research, evaluation infrastructure, and frontier-lab policy commitments.

**What lives there.**
- Anthropic Responsible Scaling Policy: v3.0 effective Feb 24, 2026; v3.1 effective Apr 2, 2026. Separates unilateral mitigations from industry-conditional ones; refines ASL-3 deployment standards by access tier; ASL-4 thresholds tied to autonomous AI R&D capability remain partially specified.
- OpenAI Preparedness Framework v2 (Apr 15, 2025): collapses earlier multi-tier categories into "High" / "Critical" across long-range autonomy, sandbagging, autonomous replication and adaptation, undermining safeguards, CBRN. Controversial adjustment clause: OpenAI may revise safeguards if a rival lab ships high-risk without comparable mitigations.
- Google DeepMind Frontier Safety Framework: Critical Capability Levels for autonomy, biosecurity, cybersecurity, ML R&D; shifted from sparse autoencoders to "pragmatic interpretability."
- Mechanistic interpretability: Anthropic circuit tracing with cross-layer transcoders (Mar 2025); "Biology of a Large Language Model" study on Claude 3.5 Haiku; MIT Technology Review named the field a 2026 breakthrough.
- Third-party eval: METR (RE-Bench, capability assessments on DeepSeek-R1 / Claude 3.5 Sonnet / o1); Apollo Research (scheming detection); Pattern Labs (cyber, CBRN red teams). Dangerous-capability evals: WMDP, Cybench, persuasion suites.
- Frontier Model Forum (Anthropic, Google, Microsoft, OpenAI; Meta absent): 2026 publications on chain-of-thought monitorability and frontier nuclear security; FMF members began sharing intelligence on adversarial distillation by Chinese rivals (Apr 2026).
- Model welfare: Anthropic program under Kyle Fish (Apr 2025); Eleos AI Research external evals; Claude Opus 4.6 system card (Feb 2026) documents self-reported 15–20% consciousness probability.

**Binding constraints.** Interpretability is not yet at the bar of reliably detecting most model problems (Anthropic publicly targets 2027). The OpenAI Preparedness adjustment clause is one of the five Structural Risks (see Ch 3 §3.6).

**Evolution stage.** Custom-Built. Standards are converging but not commodified; interpretability is Genesis at the research frontier.

### Meta-B — Regulation

**Position.** Jurisdictional rules that bind every layer. Depends on legislative cycles and enforcement capacity. What it touches: data (VI), models (VII–IX), application (XIII), and the user (XIV).

**What lives there.**
- EU AI Act: GPAI obligations effective Aug 2, 2025; transparency, AI-generated-content labeling, Commission enforcement Aug 2, 2026; pre-existing GPAI models compliant by Aug 2, 2027. Every Member State must operate at least one AI Sandbox.
- US federal: Biden EO 14110 rescinded Jan 20, 2025; Trump EO 14179 ("Removing Barriers to American Leadership in AI") signed three days later. Action Plan delivered Jul 2025: data-center permitting acceleration, "non-woke" AI procurement, infrastructure expansion. Dec 2025 EO on "Eliminating State Law Obstruction of National AI Policy" signals federal preemption pressure. NIST AI Safety Institute rebranded to AI Standards and Innovation. NIST AI RMF remains de facto compliance reference.
- US state: California SB 1047 vetoed 2024; SB 53 (Transparency in Frontier AI Act) signed Sep 29, 2025, effective Jan 1, 2026. Captures frontier developers training >10^26 FLOPs at companies >$500M revenue (practically OpenAI, Anthropic, Google DeepMind, Meta, Microsoft). Requires annual frameworks, Cal OES critical-incident reporting, whistleblower protections, AG-enforced civil penalties. Texas and Colorado have parallel regimes.
- International: UK AI Safety Institute renamed AI Security Institute Feb 14, 2025 (national-security framing); AISI Frontier AI Trends Report 2025 first evidence-anchored capability progression measurement. China CAC Generative AI Service Regulations and Algorithm Filing remain operative.
- Copyright: Bartz v. Anthropic ($1.5B); NYT v. OpenAI in pretrial SDNY; Andersen v. Stability AI ongoing.
- TAKE IT DOWN Act signed May 19, 2025 — operative federal deepfake statute; 48-hour platform takedown for non-consensual intimate imagery including AI-generated forgeries.

**Binding constraints.** Federal preemption volatility (Structural Risk 4, see Ch 3 §3.6) — California SB 53 has teeth on paper, but federal preemption pressure escalated through 2026. EU AI Act enforcement capacity is the late-2026 crux (Crux 4, §3.7).

**Evolution stage.** Custom-Built. Rules are written, enforcement is not yet mature.

### Meta-C — Economics

**Position.** The capital flows and unit economics that fund every layer. Depends on capital markets, cloud P&L discipline, and per-token pricing dynamics.

**What lives there.**
- Hyperscaler capex roughly quadrupled since GPT-4. 2026 aggregate projected $660–770B: Amazon ~$200B, Alphabet $175–185B, Meta $115–135B, Microsoft $110–120B, Oracle ~$50B — roughly 75% AI-related.
- Free-cash-flow consequences: Morgan Stanley projects Amazon FCF at -$17B 2026 (BofA: -$28B); Pivotal projects Alphabet FCF crashing ~90% to ~$8B from $73B in 2025.
- Stargate: $500B over four years; OpenAI/SoftBank/Oracle/MGX principals; NVIDIA/Microsoft/Arm/Cisco technology partners. Abilene live on Oracle Cloud Infrastructure; five additional sites announced Sep 2025; ~7 GW planned capacity, >$400B three-year deployment.
- Model-lab revenue: OpenAI ARR $2B (2023) → $6B (2024) → $20B (end-2025) → ~$24B (Apr 2026). Anthropic ARR $1B (Dec 2024) → $9B (end-2025) → $14B (Feb) → $19B (Mar) → $30B (Apr 2026), ~80% enterprise, eight of Fortune 10 are Claude customers, >500 customers >$1M annually. OpenAI CRO disputed $30B figure as overstated ~$8B in internal memo — this is Crux 1 (Anthropic ARR $24B vs. $30B, Q2–Q3 2026 resolution; see Ch 3 §3.7).
- Talent: Meta Superintelligence Labs re-rated the field. Reported packages: Ruoming Pang ~$200M over multi-year; Andrew Tulloch ~$1.5B over six years. Senior frontier IC + team-lead comp credibly clears $1–10M annually at OpenAI/Anthropic/GDM. Founder labs: Safe Superintelligence (Sutskever/Gross/Levy, ~$2B at $32B); Thinking Machines (Mira Murati, ~$2B seed at $10–12B).

**Binding constraints.** Hyperscaler FCF reckoning (Structural Risk 2, §3.6); model-lab gross margin compression as per-token prices erode 4–10×; talent-cost inflation.

**Evolution stage.** Custom-Built. Capital structures (SPV financing, sovereign co-investment) are still being invented.

### Meta-D — Geopolitics

**Position.** The international layer over chips, models, and capital. Depends on export controls, sovereign capital, and Taiwan supply-chain stability.

**What lives there.**
- Chip war: H20 reversal Apr→Jul 2025; NVIDIA China share fell ~95% → ~55% as Huawei Ascend 910C/920 absorbed the gap. NVIDIA shipped >1M H20s to China by late 2024 — 5:1 lead over Ascend volume but closing. B30A (Blackwell-class) decision is the next inflection.
- Taiwan dependency: TSMC fabricates ~90% of leading-edge logic. TSMC Arizona entered 4nm volume production early 2025 (Apple, NVIDIA). Advanced packaging still routes back to Taiwan. TSMC committed an additional $100B US investment Mar 2025 (total $165B): three new fabs, two advanced packaging facilities, R&D center. Genuine supply-chain de-risking is 3–5 years out.
- Gulf as third pole: G42 (UAE, Mubadala-backed) — Stargate UAE 1 GW announced May 22, 2025 with OpenAI/Oracle/NVIDIA/SoftBank/Cisco. Humain (Saudi PIF, 2025) plans 500 MW AMD + 500 MW NVIDIA over five years; 18,000 GB300 units in 2026; ~$10B AMD commitment. US Commerce authorized advanced chip exports to G42 and Humain Nov 19, 2025.
- Sovereign models: France/Mistral (most credible EU frontier); UAE Falcon and K2; India BharatGPT and Krutrim; Singapore SEA-LION; Saudi Allam.
- Labor displacement: Stanford Digital Economy Lab "Canaries in the Coal Mine" (Aug 2025): entry-level hiring in AI-exposed jobs fell 13% since LLM proliferation; CS graduates faced 6.1% unemployment in 2025 — nearly double philosophy majors.

**Binding constraints.** Taiwan strait stability; export-control policy reversals; sovereign-AI capital terms (who owns the IP when MGX or PIF underwrites the buildout).

**Evolution stage.** Custom-Built. "Compute as foreign policy" is operationally real but the doctrine is still being written.

## Apply

Pick three strata you couldn't explain to a buyer in 60 seconds. Write a 2-sentence explanation of each — what it does, what it depends on. Then for each, write the binding constraint in one sentence using a 2026 number (e.g., "CoWoS-L capacity 75–80 KWPM end-2025"). Re-check next month: did the constraint move? If yes, which stratum above just got repriced? This drill takes ten minutes and surfaces the strata you're handwaving — usually the ones a senior buyer or interviewer will probe hardest. Rotate strata each pass so the weak spots get covered.
