/**
 * AI AGENTS — A DECISIONS PLAYBOOK (VOLUME III ADDENDUM)
 * Framework analyses + agent-layer synthesis layered on the Foundation Reference.
 * Generates AI_AGENTS_ADDENDUM.docx via docx-js.
 */
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Header, Footer, AlignmentType,
  LevelFormat, HeadingLevel, BorderStyle, PageNumber,
} = require('docx');

// ---------------- Aesthetic ----------------

const FONT = 'Calibri';
const FONT_DISP = 'Georgia';
const FONT_MONO = 'Consolas';
const COLOR_INK = '1A1410';
const COLOR_ACCENT = 'A6371F';
const COLOR_VERDIGRIS = '456C5C';
const COLOR_OCHRE = 'A37425';
const COLOR_GRAY = '6E6356';

// ---------------- Helpers ----------------

function p(text, opts = {}) {
  return new Paragraph({
    children: [new TextRun({
      text, font: opts.font || FONT, size: opts.size || 22,
      bold: opts.bold, italics: opts.italics, color: opts.color || COLOR_INK,
    })],
    spacing: { before: opts.before ?? 80, after: opts.after ?? 100, line: 300 },
    alignment: opts.align || AlignmentType.JUSTIFIED,
    indent: opts.indent,
  });
}

function h1(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT_DISP, size: 40, bold: true, color: COLOR_INK })],
    spacing: { before: 480, after: 240, line: 320 },
    pageBreakBefore: true,
    heading: HeadingLevel.HEADING_1,
  });
}

function h2(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT_DISP, size: 30, bold: true, color: COLOR_INK })],
    spacing: { before: 320, after: 160, line: 320 },
    heading: HeadingLevel.HEADING_2,
  });
}

function h3(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT_DISP, size: 24, bold: true, color: COLOR_ACCENT })],
    spacing: { before: 240, after: 100, line: 300 },
    heading: HeadingLevel.HEADING_3,
  });
}

function eyebrow(text) {
  return new Paragraph({
    children: [new TextRun({
      text: text.toUpperCase(), font: FONT_MONO, size: 16, color: COLOR_ACCENT,
      characterSpacing: 60,
    })],
    spacing: { before: 200, after: 60 },
  });
}

function bullet(text, bold = false) {
  return new Paragraph({
    numbering: { reference: 'bullets', level: 0 },
    children: [new TextRun({ text, font: FONT, size: 22, bold, color: COLOR_INK })],
    spacing: { before: 40, after: 40, line: 280 },
  });
}

function bulletRich(parts) {
  return new Paragraph({
    numbering: { reference: 'bullets', level: 0 },
    children: parts.map(part => new TextRun({
      text: part.text, font: FONT, size: 22, bold: part.bold,
      italics: part.italics, color: part.color || COLOR_INK,
    })),
    spacing: { before: 40, after: 40, line: 280 },
  });
}

function rule() {
  return new Paragraph({
    children: [new TextRun({ text: '' })],
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_ACCENT, space: 1 } },
    spacing: { before: 120, after: 240 },
  });
}

function spacer(n = 120) {
  return new Paragraph({ children: [new TextRun('')], spacing: { before: n, after: n } });
}

// ---------------- Content ----------------

const docChildren = [];

// COVER

docChildren.push(
  spacer(2400),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({
      text: 'THE AGENT LAYER',
      font: FONT_DISP, size: 88, bold: true, color: COLOR_INK,
      characterSpacing: 80,
    })],
    spacing: { before: 0, after: 120 },
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({
      text: 'A DECISIONS PLAYBOOK',
      font: FONT_MONO, size: 22, color: COLOR_ACCENT,
      characterSpacing: 240,
    })],
    spacing: { before: 0, after: 480 },
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({
      text: 'ADDENDUM TO THE FOUNDATION REFERENCE · VOLUME III',
      font: FONT_DISP, size: 24, italics: true, color: COLOR_INK,
    })],
    spacing: { before: 0, after: 120 },
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({
      text: 'Five frameworks · ten sub-strata · four meta · 2025–2026',
      font: FONT_DISP, size: 20, italics: true, color: COLOR_GRAY,
    })],
    spacing: { before: 0, after: 1200 },
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({
      text: 'Compiled for A. Yedi · Five plates accompany this volume',
      font: FONT_DISP, size: 18, italics: true, color: COLOR_GRAY,
    })],
    spacing: { before: 0, after: 0 },
  }),
);

// PREAMBLE

docChildren.push(
  h1('Preamble'),
  rule(),
  p('This document is the decisions companion to the Volume III foundation report. Where the report descriptively unfolds the agent layer into ten sub-strata plus four wrapping meta-strata, this addendum layers five framework analyses on top — the OCQ Matrix, Wardley Mapping, Helmer’s 7 Powers, Ecosystem Jobs-to-be-Done, and the empirical Talent and Capital Flow tracker — and resolves them into a single playbook: seven refreshed Bets, five Structural Risks, five Cruxes, a 6/12/18-month Action Map, and an Agent-Specific Procurement Rubric that becomes the bridge to Volume II’s Bet #1 (Enterprise AI Procurement Operating Standard).'),
  p('The principle of composition is to refresh the prior seven Bets at agent-layer resolution rather than to add new ones for the sake of count. Where this volume’s analysis materially changes conviction, sequencing, or falsifiability of a Bet, the change is named explicitly with a delta annotation. Where it confirms the prior conclusion, conviction is updated but the Bet is left intact. The aim is a working surface a sharp operator can act on inside eighteen months without re-reading the whole atlas.'),
  p('Volume III’s strongest synthetic finding — the single observation that emerges from the five frameworks but did not from the prior single-band treatment of agents — is that the highest-conviction near-term opportunity for a senior enterprise GTM operator in New York is Bet #1, not Bet #2 as the prior addendum implied by ranking order. The 7 Powers screen names procurement Process Power at Meta-B as the only durable position Alex can claim rather than rent; the Wardley map places agent-procurement controls at Genesis as the unclaimed flag; the Ecosystem JTBD shows Job 6 (passing the agent-specific procurement gauntlet) as the most-underserved enterprise job; and the OCQ Matrix surfaces multiple high-claimability opportunities (signed reproducible eval reports, Article 14 oversight, trajectory cost audits, form-factor procurement diagnostics) that all compound into Bet #1 rather than into separate productized bets. The implication is a sequencing change: Bet #1 first to claim a durable position; Bet #2 second to collect equity at a power-holder; Bet #3 third as advisory practice compounding from both. The rest of this volume defends this sequencing layer by layer.'),
);

// CONTENTS

docChildren.push(
  h1('Contents'),
  rule(),
  p('Part VI — Methodology', { indent: { left: 360 } }),
  p('Part VII — The OCQ × Agent Sub-Stratum Matrix', { indent: { left: 360 } }),
  p('Part VIII — Wardley Mapping the Agent Stack', { indent: { left: 360 } }),
  p('Part IX — Helmer’s 7 Powers and Agent-Layer Durability', { indent: { left: 360 } }),
  p('Part X — Ecosystem-Level Jobs to be Done', { indent: { left: 360 } }),
  p('Part XI — Synthesis · Seven Bets Refreshed, Five Risks, Five Cruxes', { indent: { left: 360 } }),
  p('Part XII — 6 / 12 / 18-Month Action Map for Alex', { indent: { left: 360 } }),
  p('Part XIII — The Agent-Specific Procurement Rubric (Appendix to Bet #1)', { indent: { left: 360 } }),
);

// ===========================================================
// PART VI — METHODOLOGY
// ===========================================================

docChildren.push(
  h1('Part VI · Methodology'),
  rule(),
  p('Five frameworks were applied to the agent layer as defined in the foundation report — ten sub-strata (foundation models with agentic capability; agent runtimes; tool-use protocol; memory and state; planning and reasoning; action surfaces; evaluation and observability; runtime safety and guardrails; vertical agent products; end-user surfaces) plus four meta-strata (capability-level safety regimes; regulation; economics; geopolitics). The lens definitions inherit from Volume II’s Part VI Methodology and are tightened here to agent-specific application.'),

  h2('The lenses, precisely'),
  p('OPPORTUNITY (agent layer): where in the agent stack is value being created faster than the field’s prevailing narrative reflects, AND where can someone with Alex’s profile (twelve years enterprise B2B GTM, growing AI-builder fluency, NYC base) claim it inside a 12–18 month window before the layer commoditizes or consolidates? Score on three dimensions, 1–5: Confidence (how robust the evidence), Time-to-Monetize (5 = inside six months, 1 = beyond twenty-four), Claimability (5 = uncommon-leverage fit, 1 = wrong profile).'),
  p('CHALLENGE (agent layer): what is the binding constraint or latent feedback loop that, if it tightens or fires, materially reprices the layer above? Score on three dimensions, 1–5: Severity (5 = total reprice, 1 = nuisance), Probability (5 = near-certain inside eighteen months, 1 = unlikely), Alex’s exposure (5 = directly hits bets he is positioned for, 1 = orthogonal).'),
  p('OPEN QUESTION (agent layer): what is the agent-specific crux the field is betting on without admitting? Score on three dimensions, 1–5: Decidability (5 = answer-event likely inside six months, 1 = open for years), Asymmetry (5 = answer reprices more than two Bets, 1 = marginal), Bet-size (5 = greater than one-billion-dollar category outcome, 1 = niche).'),
  p('Discipline applied: if more than two of any group’s twelve opportunity scores hit 15/15, the lens has stopped working and is re-tightened. The OCQ outputs in Part VII were vetted against this rule.'),

  h2('Inheritance and delta'),
  p('Where Volume II covered a layer at the full-stack level — model providers, retrieval, regulation broadly, hyperscaler economics, geopolitics broadly — that work is referenced by name and not redone. The agent-specific Part VII matrix is additive at higher resolution. The seven Bets, five Risks, and five Cruxes from Volume II Part X are inherited as the baseline and explicitly delta’d in Part XI. The Talent and Capital Flow tracker (`OCQ_TRACKER.md`) is refreshed for agent-specific signal and feeds Part XI and Part XII; the agent-specific subset will be maintained as `AI_AGENTS_TRACKER.md` going forward.'),
);

// ===========================================================
// PART VII — OCQ × LAYER MATRIX
// ===========================================================

docChildren.push(
  h1('Part VII · The OCQ × Agent Sub-Stratum Matrix'),
  rule(),
  p('Each of the ten sub-strata and four meta-strata is treated below with a compressed framing paragraph, the top three Opportunities (the field-narrative-lag thesis), the top two Challenges (the binding constraint), and the top two Open Questions (the agent-specific crux). Every entry ties to a 2025–2026 datapoint and carries a falsifiability mark for opportunities, a watch-signal for challenges, and an answer-event for open questions. Scoring follows the lens definitions in Part VI.'),

  // STRATUM I
  h2('Stratum I · Foundation models with agentic capability'),
  p('The agent-relevant frontier is four numbers — TAU-bench, SWE-Bench Verified, OSWorld, GAIA/BrowseComp — and one ceiling: error compounding under context degradation past 32K tokens of tool traces. Capability advances continue but the bottleneck has shifted to per-step reliability for unattended use. The Anthropic sub-agents pattern is ahead by approximately six months and will be table-stakes by Q4 2026. Test-time compute economics bifurcate the market into interactive (Sonnet / Flash / 4o class) and autonomous back-office (Opus / GPT-5 thinking / Deep Think). Reasoning regression past 32K is a real, under-discussed limit.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Skills-catalog authorship for the Claude Agent SDK ', bold: true }, { text: '— the SDK\'s skills primitive (Sep 2025) is ahead-of-peers by approximately six months and is publicly authorable. A 12-month window exists to publish a small, sharp set of enterprise-GTM skills that get cited in field accounts. Score 4/4/5 (Conf/TTM/Claim). Falsifiability: if OpenAI Agents SDK and Google ADK ship handoff/team primitives at functional parity within 6 months and Anthropic does not extend the catalog model, the authorship window closes.' }]),
  bulletRich([{ text: 'Thinking-budget cost-arbitrage advisory ', bold: true }, { text: '— OpenAI\'s `reasoning_effort` knob exposed Feb–Apr 2026 and Anthropic\'s extended-thinking budgets make per-task economics buyer-controllable. Most enterprise deployments default to high; the typical task does not earn it. Audit-and-route advisory stacks onto Bet #4. Score 4/5/4. Falsifiability: if hyperscaler auto-routing ships by Q4 2026 with default-on behavior, this collapses into platform-bundled feature.' }]),
  bulletRich([{ text: 'Computer-use procurement audit ', bold: true }, { text: '— the gap between OSWorld 50–55% and the human 72% / per-step ~99% required for unattended autonomous use will not close in 2026. Buyer-side audit framework for "what computer-use tasks pass our reliability bar" is sellable today to F500 risk officers exploring AI BPO. Score 4/4/5. Falsifiability: a frontier model crossing OSWorld 65% by Q3 2026 collapses the watch-only / supervised distinction.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Foundation labs walking up-stack into vertical applications ', bold: true }, { text: '— ChatGPT Business connectors, Claude for Work, Gemini Workspace agents directly compress the value of vertical-agent companies (Sierra, Glean, Harvey targets). Severity 5 / Probability 4 / Alex exposure 5 (hits Bet #2 directly). Watch signal: connector marketplace launches and named-customer deflection from vertical incumbents.' }]),
  bulletRich([{ text: 'Reasoning regression past 32K context ', bold: true }, { text: '— acknowledged by Anthropic Sept 2025 SDK release notes and OpenAI Aug 2025 GPT-5 system card. Until sub-agent or long-context architectures fully solve this, every long-horizon agent is bottlenecked at trajectory length. Severity 4 / Probability 4 / Alex exposure 3. Watch: Claude 5 / GPT-6 / Gemini 3 long-context benchmarks at trajectory level.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'OSWorld 65% by Q3 2026 — yes or no ', bold: true }, { text: '— the threshold that moves computer use from supervised to deployable for narrow back-office. Decidability 4 / Asymmetry 5 / Bet-size 5. Answer event: a frontier-system score on the public scoreboard.' }]),
  bulletRich([{ text: 'When does ASL-4 capability emerge ', bold: true }, { text: '— Anthropic\'s capability tier triggers deployment freezes; if 2026 vs. 2027 differs by twelve months, capability-tier-based competitor advantage windows shift. Decidability 3 / Asymmetry 4 / Bet-size 4. Answer: Anthropic capability disclosure or evaluation publication.' }]),

  // STRATUM II
  h2('Stratum II · Agent runtimes and harnesses'),
  p('The runtime layer is the thinnest by gross margin in the agent stack and is splitting along the model spine rather than consolidating. Four serious enterprise contenders (Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph 1.0) plus a credible OSS / TS-native middle (Mastra, Pydantic AI, CrewAI, Smolagents, AutoGen / AG2). The "neutral runtime" promise is real but losing ground in greenfield 2026 builds because vendor SDKs ship faster than neutral wrappers. Value accrues to the model below and the application above.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Migration audit between LangChain 2024 and a vendor SDK ', bold: true }, { text: '— several F500 shops standardized on LangChain in 2024 and now face a stay-or-rip decision. Sellable advisory, six-month window before LangGraph 1.0 stabilizes the migration tooling. Score 4/4/4.' }]),
  bulletRich([{ text: 'Runtime selection rubric for AI procurement ', bold: true }, { text: '— folds into the Bet #1 Playbook as the "which SDK does your vendor ship on" check; the SDK choice gates capability surface, observability hooks, and lock-in. Score 4/4/5.' }]),
  bulletRich([{ text: 'Sub-agents pattern training ', bold: true }, { text: '— Anthropic\'s sub-agents primitive is the cleanest expression of the privilege-separation pattern (web-reading sub-agent without write tokens). Six-month window to be the canonical voice on enterprise application. Score 3/4/5.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Runtime commoditization ', bold: true }, { text: '— LangGraph 1.0 GA Oct 2025 made the field competitive; LangSmith carries the margin. Pure runtime opportunities collapse to twelve months. Severity 4 / Probability 5 / Exposure 3.' }]),
  bulletRich([{ text: 'Vendor-SDK lock-in within the model-shop ', bold: true }, { text: '— Anthropic shops increasingly cannot run on OpenAI; F500 multi-model strategy gets harder. Severity 3 / Probability 4 / Exposure 3.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does LangChain Inc. sustain $40–60M+ LangSmith ARR ', bold: true }, { text: '— Harrison Chase\'s "LangSmith is the margin layer" public posture (Sep 2025+) is an honest concession against interest; the question is whether observability sustains where the runtime did not. Decidability 4 / Asymmetry 3 / Bet-size 3. Answer: 2026 ARR disclosure or leak.' }]),
  bulletRich([{ text: 'Does Google A2A win cross-vendor commitment ', bold: true }, { text: '— without major non-Google adoption it dies or stays Genesis. Decidability 3 / Asymmetry 3 / Bet-size 2.' }]),

  // STRATUM III
  h2('Stratum III · Tool-use protocol (MCP)'),
  p('The MCP spec is held; the experience is fragmenting silently. Eleven thousand four hundred registered servers as of April 2026 with bimodal quality; four hyperscalers committed; Linux Foundation governance (December 2025) removed the Anthropic kill-switch objection. Fork vectors are real: OpenAI Responses-API proprietary tool calls bypass MCP for latency; A2A overlaps MCP for agent-to-agent; Anthropic `tool_use` blocks remain proprietary native; long-tail server quality is bimodal. The durable MCP power locates not in the protocol itself but in the gateway control plane (Cloudflare Workers AI MCP, Kong MCP Gateway GA July 2025, Pomerium identity-aware proxy).'),
  h3('Opportunities'),
  bulletRich([{ text: 'MCP-gateway buyer advisory ', bold: true }, { text: '— the gateway category is the durable middleware position. Pair-with-Cloudflare/Kong/Pomerium as the AI-procurement specialist on gateway deployment, auth flows, audit, server quality grading. Stacks onto Bet #3 with the reframe that the gateway sub-category is the punctuation, not the spec. Score 4/4/5.' }]),
  bulletRich([{ text: 'Private-registry curation for F500 ', bold: true }, { text: '— enterprises will de facto fork by maintaining private MCP registries (first-party tier from Stripe, Linear, GitHub, Cloudflare, Notion, Atlassian, Datadog, Snowflake, Databricks, ServiceNow plus internal). Curation rubric is sellable. Score 4/4/4.' }]),
  bulletRich([{ text: 'MCP server constellations for enterprise GTM SaaS ', bold: true }, { text: '— Salesforce, Outreach, Gong, Highspot, Zoominfo, Linear — many incumbent SaaS systems ship zero or one MCP server. Window for productization is Q2–Q4 2026; defensibility is in matching server design to the Job 4 / Job 1 underserved-outcome list. Score 3/3/4.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Silent MCP fork via Responses-API proprietary path ', bold: true }, { text: '— production OpenAI agents bypass MCP for latency; "MCP-compatible but not MCP-native" is the growing pattern. If this becomes dominant by 2027, Bet #3 thesis weakens materially. Severity 4 / Probability 4 / Exposure 4.' }]),
  bulletRich([{ text: 'SaaS incumbents shipping first-party MCP servers ', bold: true }, { text: '— Snowflake, Databricks, ServiceNow first-party shipping (Q1–Q2 2026) commoditizes the productized-server thesis the moment it lands. Severity 4 / Probability 5 / Exposure 3. Reframe Bet #3 to advisory.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'MCP commons or fork by EOY 2026 ', bold: true }, { text: '— inherited Crux #3. The protocol is held; the experience is the open question. Decidability 4 / Asymmetry 5 / Bet-size 5. Answer: major-vendor proprietary tool-use schema announcements; Linux Foundation governance stability.' }]),
  bulletRich([{ text: 'Does the MCP gateway category cross ten F500 logos by Q3 2026 ', bold: true }, { text: '— if Cloudflare + Kong + Pomerium cumulatively cross ten named F500, the durable middleware thesis is confirmed. Decidability 4 / Asymmetry 4 / Bet-size 4.' }]),

  // STRATUM IV
  h2('Stratum IV · Memory and state'),
  p('Memory is RAG-with-writes, not a distinct primitive. Approximately seven of ten vendor pitches collapse to "we summarize and write to a vector database." The standalone category ceiling is $200–400 million ARR split across two or three vendors. Lab-native memory (ChatGPT, Claude Projects April 2026, Gemini personalization March 2026) absorbs the consumer and prosumer tier; Zep retains a defensible compliance-sensitive enterprise niche; Mem0 and Letta straddle. Knowledge-graph hybrids (Microsoft GraphRAG, LightRAG) hold partial production traction; HippoRAG, PathRAG, OG-RAG remain research-only.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Memory architecture as a service line inside Bet #5 ', bold: true }, { text: '— fold memory selection (lab-native vs. Mem0 vs. Letta vs. Zep vs. pgvector-and-summarize) into the Enterprise RAG Architecture Practice rather than as a separate Bet. Score 4/4/5.' }]),
  bulletRich([{ text: 'Procurement memory checklist (Article 17, Schrems-II, contextual integrity) ', bold: true }, { text: '— no vendor ships a contextual-integrity primitive. Buyer-side audit checklist is sellable as a Bet #1 module. Score 4/4/5.' }]),
  bulletRich([{ text: 'Healthcare and finance memory deployment with Zep ', bold: true }, { text: '— Zep is the only credible HIPAA-ready story; vertical advisory pairs cleanly with healthcare-agent vendor selection. Score 3/3/4.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Lab-native memory absorbs consumer and prosumer ', bold: true }, { text: '— Claude Projects memory GA April 2026, ChatGPT 800M MAU, Gemini personalization GA March 2026. Standalone category compresses to compliance-niche by 2027. Severity 4 / Probability 5 / Exposure 2.' }]),
  bulletRich([{ text: 'Lock-in risk per vendor ', bold: true }, { text: '— Claude memory cannot be queried by a GPT agent. Multi-model enterprise stacks need portable memory; nobody ships one cleanly. Severity 3 / Probability 4 / Exposure 2.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Standalone memory absorbed by 2027 ', bold: true }, { text: '— inherited Crux #5. Directional answer from this volume: absorbed for consumer/prosumer, standalone-niche for compliance enterprise. Decidability 4 / Asymmetry 3 / Bet-size 3. Answer: Mem0 or Letta acquisition vs. independent Series B at materially higher valuation.' }]),
  bulletRich([{ text: 'Does contextual integrity become a procurement standard ', bold: true }, { text: '— if Helen Nissenbaum\'s "memory written in B2B sales must not surface in HR" frame enters EU AI Act enforcement guidance, a new category opens. Decidability 2 / Asymmetry 5 / Bet-size 4.' }]),

  // STRATUM V
  h2('Stratum V · Planning, reasoning, test-time compute'),
  p('Most production agents in May 2026 are three-to-seven-step ReAct loops with a reasoning model, a verifier, and a planner-executor split routing seventy-to-eighty-five percent of tokens through cheap executors. Tree-of-Thoughts and meta-planning are lab curiosities. The reasoning-model tier (o1/o3/Claude extended thinking/Gemini Deep Think/DeepSeek R1/Qwen QwQ/Kimi K1.5) collapsed two distinctions: the model now does internal multi-step search before emitting; tool use during reasoning collapses the outer ReAct loop. Test-time compute beyond approximately eight thousand reasoning tokens has unattractive economics for most enterprise classes.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Trajectory cost-and-latency audit (FinOps for Trajectories) ', bold: true }, { text: '— the named highest-score opportunity in B2: planner-executor-verifier routing as a sellable F500 audit. 12-month window before Bedrock auto-routing defaults on. Stacks onto Bet #4 with explicit decay. Score 5/5/5.' }]),
  bulletRich([{ text: 'Reasoning-budget procurement rubric ', bold: true }, { text: '— buyer-side "should this task be on `reasoning_effort=high` or medium" decision tree. Bet #1 module. Score 4/4/5.' }]),
  bulletRich([{ text: 'Open-weight reasoning deployment advisory (DeepSeek / Qwen / Kimi) ', bold: true }, { text: '— for F500 with political risk acceptance, twenty-to-forty-percent of US frontier inference cost makes on-premises reasoning realistic. Advisory window is 12 months. Score 3/3/3.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Hyperscaler auto-routing of planner-executor ', bold: true }, { text: '— Vercel AI Gateway, AWS Bedrock, Martian, OpenRouter all expose tier-routing as config; default-on auto-routing plausible by H2 2027. Severity 4 / Probability 4 / Exposure 5 (hits Bet #4 window directly).' }]),
  bulletRich([{ text: 'Reasoning-model opacity to enterprise buyers ', bold: true }, { text: '— buyers cannot reason about internal CoT faithfulness or RLVR-pipeline generalization. Treat reasoning marketing as opaque. Severity 3 / Probability 5 / Exposure 2.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does test-time compute hit diminishing returns at thirty-two thousand reasoning tokens ', bold: true }, { text: '— inherited Crux. Anthropic Feb 2026 and OpenAI `reasoning_effort=high` documentation already warn about "overthinking." Decidability 4 / Asymmetry 4 / Bet-size 4.' }]),
  bulletRich([{ text: 'Does open-weight reasoning narrow the gap to single digits by H2 2026 ', bold: true }, { text: '— DeepSeek R2 leak suggestion. If real, on-prem reasoning advisory inflates. Decidability 3 / Asymmetry 3 / Bet-size 3.' }]),

  // STRATUM VI
  h2('Stratum VI · Action surfaces'),
  p('Sandboxes are production-ready and commoditizing on a twenty-four-month timer. Browser automation is production-ready in narrow lanes; the boring baseline (Playwright plus a good model) still wins for sites with stable DOM and no aggressive anti-bot. Full computer use is still demo-grade in May 2026 — OSWorld 50–55%, WebArena 70%, AndroidWorld 50%, with error compounding making unattended autonomous use a 2027 question. Voice agents are production-ready for short scripted calls and collapse on the long tail. The moat is operational tooling around the surface (recording, replay, evaluation, compliance) not the surface itself.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Sandboxing as a procurement control ', bold: true }, { text: '— SOC 2 / ISO 27001 control like "AI-001: AI-generated code MUST execute in isolated tenancy with default-deny egress." Vanta-shaped mapping plus buyer audit. Bet #1 module. Score 4/4/5.' }]),
  bulletRich([{ text: 'Vertical voice agent packaging (debt collection, intake, dental, field-service) ', bold: true }, { text: '— substrate is commoditizing (LiveKit + Cartesia + Realtime API); vertical packaging plus compliance plus integrations is the moat. Advisory to vendors or as deployment partner. Score 3/3/3.' }]),
  bulletRich([{ text: 'Computer-use reliability rubric for buyers ', bold: true }, { text: '— "what tasks meet our internal reliability threshold given OSWorld 50–55%" is a structured-rubric advisory. Bet #1 module. Score 4/4/5.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Surface commoditization on twenty-four-month timer ', bold: true }, { text: '— Browserbase $50M ARR is real but the underlying Chromium is open. Margin moves to the operational layer. Severity 4 / Probability 5 / Exposure 3.' }]),
  bulletRich([{ text: 'Voice regulatory enforcement (TCPA, GDPR, state consent) ', bold: true }, { text: '— Q1 2026 enforcement uptick already forced Vapi / Retell / Bland to ship consent capture. Cost-of-compliance is rising; small voice-agent vendors squeeze. Severity 3 / Probability 5 / Exposure 2.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'OSWorld 65% on a frontier system by Q3 2026 ', bold: true }, { text: '— shared with Stratum I; the binding metric for computer-use deployability. Decidability 4 / Asymmetry 5 / Bet-size 5.' }]),
  bulletRich([{ text: 'Voice-to-voice floor crosses three-hundred-millisecond turn-taking ', bold: true }, { text: '— the natural-cadence line. Current floor approximately 500–800 ms. If sub-300 by H2 2026, voice consolidates faster. Decidability 4 / Asymmetry 3 / Bet-size 3.' }]),

  // STRATUM VII
  h2('Stratum VII · Evaluation and observability'),
  p('Agents broke LLM evaluation on four axes: trajectories not turns, replay as debug primitive, online evaluation not just offline, cost and latency as first-class signals. Tier-1 vendors with enterprise traction are LangSmith, Braintrust, Langfuse, Arize, Galileo. OpenTelemetry GenAI semantic conventions stabilized in January 2026; trace ingest is no longer a lock-in vector. Lock-in is in evaluation logic and judge models (regression sets as Braintrust YAML or Galileo metric definitions take a quarter to port). Partial consolidation by 2027 with two-to-three pure-plays acquired by hyperscalers or runtime vendors by end of 2026.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Signed reproducible eval reports — the load-bearing Bet #1 wedge ', bold: true }, { text: '— no vendor ships turnkey signed reports tied to model pin, dataset hash, harness version that survive a regulator subpoena. Inspect AI closest but not turnkey. The procurement-readiness gap. Score 5/4/5.' }]),
  bulletRich([{ text: 'Internal-eval-set curation as a service ', bold: true }, { text: '— every serious enterprise builds 200–1,000-trajectory regression sets from production traffic. Curation methodology as advisory plus tooling pair with Braintrust / Langfuse. Score 4/3/4.' }]),
  bulletRich([{ text: 'Multi-party agent audit (vendor + customer + auditor on one trace with redaction) ', bold: true }, { text: '— Genesis stage; no vendor ships. Long-cycle build; advisory-first beachhead. Score 3/2/4.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Native model-provider eval eats the bottom ', bold: true }, { text: '— Anthropic Claude Agent SDK eval templates (March 2026), OpenAI Traces, Anthropic eval dashboards. Pure-play eval pressed from above and below. Severity 3 / Probability 5 / Exposure 2.' }]),
  bulletRich([{ text: 'Hyperscaler bundling of observability ', bold: true }, { text: '— AWS Bedrock, Azure, GCP guardrails ship "good enough" at zero procurement friction. Severity 4 / Probability 5 / Exposure 3.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does Braintrust win as eval consolidator by EOY 2026 ', bold: true }, { text: '— rumored Series B $60M Q1 2026 leak. If real, M&A path consolidates the middle. Decidability 4 / Asymmetry 3 / Bet-size 3.' }]),
  bulletRich([{ text: 'Does Inspect AI become the EU AI Act conformity standard ', bold: true }, { text: '— cited in February 2026 conformity drafts. If formally adopted, audit-grade vendors pivot to Inspect-compatible. Decidability 4 / Asymmetry 4 / Bet-size 4.' }]),

  // STRATUM VIII
  h2('Stratum VIII · Runtime safety and guardrails'),
  p('Indirect prompt injection via tool returns remains unsolved. Vendors quoting 99.X% detection report against known-pattern corpora; adaptive-adversary numbers fall to 60–80%. Defense-in-depth is the only honest answer: untrusted tool returns, action confirmation, output validation, sub-agent privilege separation, continuous red-team. Protect AI to Palo Alto for $700M in Q3 2025 was the bell. Standalone runtime safety mostly absorbed into hyperscaler bundles by 2027 except a Lakera-shaped cross-cloud, model-neutral, audit-grade niche.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Adaptive-adversary red-team audit as Bet #1 module ', bold: true }, { text: '— buyer-side framework for testing agent vendors against attacker-aware injection. Promptfoo, Garak, Lakera Red as substrate; advisory wraps. Score 4/3/4.' }]),
  bulletRich([{ text: 'Tool-boundary policy template ', bold: true }, { text: '— "which tools the agent can invoke unsupervised, which require approval, which are blocked when context is tainted." No vendor ships a turnkey template. Bet #1 module. Score 4/3/5.' }]),
  bulletRich([{ text: 'OSS guardrail orchestration consulting ', bold: true }, { text: '— NeMo Guardrails 1.0 GA April 2026 plus Llama Guard 3 plus Prompt Guard 2. Open-source floor risen; F500 deployment advisory. Score 3/3/3.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Hyperscaler bundles absorb the middle ', bold: true }, { text: '— AWS Bedrock Guardrails, Purview AI Hub, Vertex Model Armor cover 80% at zero friction. Pure-plays roll up. Severity 4 / Probability 5 / Exposure 2.' }]),
  bulletRich([{ text: 'Indirect prompt injection cannot be solved by any vendor today ', bold: true }, { text: '— the EchoLeak / AgentSmith class will recur. Defensive stack always layered, never complete. Severity 4 / Probability 5 / Exposure 4 (hits any production-touching-money deployment).' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does Lakera survive as last independent at scale ', bold: true }, { text: '— or get acquired (Cisco, Palo Alto, hyperscaler) by EOY 2026. Decidability 4 / Asymmetry 2 / Bet-size 2.' }]),
  bulletRich([{ text: 'Does adaptive-adversary red-team enter EU AI Act conformity assessment ', bold: true }, { text: '— if so, the procurement-readiness gap is closed by regulation, not the market. Decidability 3 / Asymmetry 4 / Bet-size 4.' }]),

  // STRATUM IX
  h2('Stratum IX · Vertical agent products'),
  p('Nine domains. Multiple-winner at Coding, CX, Healthcare, Creative, Finance. Winner-take-most at Knowledge (Glean), Legal AmLaw100 (Harvey), RevOps (Clay only). The Bret Taylor outcome-pricing thesis is segment-specific (CX confirmed; healthcare partial; failed elsewhere). Foundation-lab encroachment ranking is Knowledge > Coding > RevOps > Creative > CX > Healthcare > Legal > Finance. The NYC Bet #2 target list refreshes to ten companies: Sierra, Decagon, Glean, Hippocratic, Hebbia, Harvey, Rogo, Clay, Ramp AI org, Runway — plus Mistral Le Chat Enterprise for the EU sovereign play.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Sierra Field-CTO / Head-of-Enterprise-East seat ', bold: true }, { text: '— NYC dual-HQ, $175M+ ARR at 4× YoY, Bret Taylor monthly NYC cadence, Stripe/Ramp/Salesforce alumni pipeline at peak migration. Highest-aligned Bet #2 target. Score 5/5/5.' }]),
  bulletRich([{ text: 'Hebbia or Rogo NYC-native vertical-agent role ', bold: true }, { text: '— under-funded relative to ARR velocity (both overdue for next round); NYC HQ; financial-services-adjacent; consulting alumni pipeline less competed than Stripe/Ramp. Hebbia\'s VP Revenue NYC hire March 2026 is the signal. Score 4/4/5.' }]),
  bulletRich([{ text: 'Pricing-model advisory for vertical agent vendors ', bold: true }, { text: '— per-seat vs. per-resolution vs. per-encounter is segment-specific. Two-year operational scar tissue compresses to a usable advisory framework. Score 3/3/4.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Foundation-lab encroachment, Knowledge segment first ', bold: true }, { text: '— ChatGPT Business connectors hit Glean directly; Knowledge is highest-encroachment. Severity 4 / Probability 4 / Exposure 4.' }]),
  bulletRich([{ text: 'Synthetic SDR quality ceiling (11x cautionary tale) ', bold: true }, { text: '— RevOps over-funded and under-performing; only Clay survives. Severity 3 / Probability 5 / Exposure 2.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Anthropic ARR — $24B or $30B ', bold: true }, { text: '— inherited Crux #1. Single load-bearing variable for Bet #2 valuation and timing. Decidability 5 (Q3 2026 disclosure or leak) / Asymmetry 5 / Bet-size 5.' }]),
  bulletRich([{ text: 'Does outcome pricing extend beyond CX into knowledge or finance ', bold: true }, { text: '— Bret Taylor thesis is segment-specific so far. Decidability 3 / Asymmetry 4 / Bet-size 3.' }]),

  // STRATUM X
  h2('Stratum X · End-user surfaces and form factor'),
  p('Form factor is the binding constraint on enterprise agentic adoption in May 2026, not capability. Twelve form factors: chat web, chat mobile, CLI, IDE inline, agentic triggers, browser sidebar, embedded SaaS, remote messaging, voice inbound, wearable/AR, computer-use UX, API. Microsoft 365 Copilot ($5B+ ARR, ~30M paid seats) is the largest single agentic-revenue position in 2026. WhatsApp Business API opening to agentic vendors in January 2026 means the global majority\'s first AI surface is a WhatsApp agent. The US-coastal sequence "chat web → IDE inline → computer use" is a US-coastal narrative.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Form-factor procurement audit ', bold: true }, { text: '— buyer-side framework for "which form factor passes our CISO" (Slack inherits DLP; extensions block by default; computer use no-go in regulated). Single highest-scoring opportunity in B4. Score 5/4/5.' }]),
  bulletRich([{ text: 'Agentic-trigger compliance advisory under Article 14 ', bold: true }, { text: '— EU AI Act Article 14 enforcement guidance draft April 2026 directly implicates cron/webhook unattended agents in regulated sectors. Bet #1 module with named regulatory anchor. Score 5/4/4.' }]),
  bulletRich([{ text: 'WhatsApp-native enterprise agent advisory ', bold: true }, { text: '— US F500 with India/LatAm/Africa operations need consent-compliant, audit-capable WhatsApp deployment. Yellow.ai / Haptik / Gupshup ecosystem advisory. Score 3/3/3.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Microsoft Copilot 365 distribution moat ', bold: true }, { text: '— $5B+ ARR, existing-seat renewal; pure-plays trail by an order of magnitude. Severity 4 / Probability 5 / Exposure 2.' }]),
  bulletRich([{ text: 'Anthropic first-party surface deficit ', bold: true }, { text: '— no Apple Intelligence slot, no native voice product, Claude mobile feature-thin, no top-10 enterprise SaaS embedding. Structural shape, not temporary. Severity 3 / Probability 5 / Exposure 3 (if Alex bets Bet #2 inside Anthropic-channel verticals).' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does Apple Intelligence ship Claude integration by EOY 2026 ', bold: true }, { text: '— Bloomberg April 2026 confirmed talks; no ship. Decidability 4 / Asymmetry 4 / Bet-size 4.' }]),
  bulletRich([{ text: 'Does unattended-agent reliability cross 99% per step by H2 2027 ', bold: true }, { text: '— if so, form factor stops being binding and capability returns as the constraint. Decidability 2 / Asymmetry 5 / Bet-size 5.' }]),

  // META A
  h2('Meta-A · Capability-level safety regimes'),
  p('Anthropic ASL framework (ASL-3 invoked for Claude Opus 4 May 2025), OpenAI Preparedness Framework with adjustment clause, Google Frontier Safety Framework, UK AISI Inspect framework, US AISI restructured 2026, METR time-horizon doubling. The ASL framework is Anthropic\'s most defensible single-vendor brand position but is not baked into EU AI Code of Practice, NIST AI RMF GenAI Profile, or ISO 42001. UK AISI Inspect cited explicitly in EU AI Act conformity-assessment drafts February 2026 — the quiet vendor-neutral standard.'),
  h3('Opportunities'),
  bulletRich([{ text: 'Capability-safety translation for enterprise procurement ', bold: true }, { text: '— "what does ASL-3 mean for our deployment review" / "what triggers an OpenAI Preparedness adjustment clause" translated for F500 risk officers. Bet #1 module. Score 4/3/4.' }]),
  bulletRich([{ text: 'Inspect AI deployment advisory ', bold: true }, { text: '— UK AISI framework as the vendor-neutral choice cited in EU conformity drafts. Position pre-formal-adoption. Score 3/3/3.' }]),
  bulletRich([{ text: 'METR time-horizon framework for capability briefing ', bold: true }, { text: '— most-cited single chart in the field. Bet #6 newsletter target as a translation lever. Score 3/3/3.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'OpenAI Preparedness adjustment-clause activation ', bold: true }, { text: '— inherited Risk #3 from Volume II. If invoked, voluntary safety regimes destabilize. Severity 4 / Probability 3 / Exposure 3.' }]),
  bulletRich([{ text: 'Lab-internal safety as competitive disadvantage ', bold: true }, { text: '— Anthropic\'s deployment discipline could lose share to less-restrictive competitors. Severity 3 / Probability 3 / Exposure 3.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'When does ASL-4 capability emerge ', bold: true }, { text: '— 2026 vs 2027 differs by twelve months of competitor window. Decidability 3 / Asymmetry 4 / Bet-size 4.' }]),
  bulletRich([{ text: 'Does any major lab invoke the Preparedness adjustment clause publicly ', bold: true }, { text: '— if yes, the voluntary regime story changes. Decidability 3 / Asymmetry 4 / Bet-size 4.' }]),

  // META B
  h2('Meta-B · Regulation'),
  p('EU AI Act Article 55 GPAI obligations enforceable August 2025; conformity-assessment guidance drafts February 2026; Article 14 human-oversight enforcement guidance draft April 2026. CA SB 53 effective January 2026. Federal preemption volatility from the Trump December 2025 executive order resolves through 2026–2027. Sectoral overlays bite hardest at FINRA / broker-dealer (finance), HIPAA / FDA SaMD (healthcare), TCPA / state consent (voice). Bartz v. Anthropic settlement at $1.5 billion and NYT v. OpenAI dynamic re-price vendor terms.'),
  h3('Opportunities'),
  bulletRich([{ text: 'EU AI Act Article 14 human-oversight playbook ', bold: true }, { text: '— April 2026 draft directly implicates agentic-trigger form factor. Buyer-side playbook the highest-actionability regulatory lever in the volume. Score 5/4/4.' }]),
  bulletRich([{ text: 'Sectoral overlay advisory (finance, health, voice) ', bold: true }, { text: '— FINRA, HIPAA, TCPA agent-specific applications. Pairs with vertical agent vendor selection. Score 4/4/4.' }]),
  bulletRich([{ text: 'Bet #1 expansion into regulated geography ', bold: true }, { text: '— EU residency wedge for F500 EU-subsidiaries; Mistral-equivalent pairing. Score 4/4/4.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'EU AI Act paper-tiger outcome ', bold: true }, { text: '— inherited Crux #4. If first enforcement late 2026 stays small and procedural, Bet #1 TAM stays niche. Severity 4 / Probability 3 / Exposure 5.' }]),
  bulletRich([{ text: 'US federal preemption volatility ', bold: true }, { text: '— Trump EO court fights resolve through 2026–2027; CA SB 53 lawsuits active. Severity 3 / Probability 4 / Exposure 4.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does EU place autonomous agents in Annex III high-risk ', bold: true }, { text: '— named highest-asymmetry open question in B3. If yes, Bet #1 TAM 3×. Decidability 3 / Asymmetry 5 / Bet-size 5.' }]),
  bulletRich([{ text: 'When does first GPAI fine land ', bold: true }, { text: '— Crux #4 answer event. Decidability 4 / Asymmetry 5 / Bet-size 5.' }]),

  // META C
  h2('Meta-C · Economics'),
  p('Per-token pricing fell roughly four-to-ten times for frontier APIs from Q1 2024 to Q1 2026; per-task agent economics did not fall the same way because trajectory length grew. CX trajectory four-to-twenty-five-thousand tokens at a few cents; coding agent thirty-to-two-hundred-fifty-thousand at twenty cents to three dollars; deep research half-a-million to five million at one to twenty dollars. Planner-executor split is the durable architectural idea; per-resolution pricing dominates CX; per-encounter dominates healthcare; per-seat survives where outcomes resist attribution.'),
  h3('Opportunities'),
  bulletRich([{ text: 'FinOps for Trajectories — distinct from FinOps for Tokens ', bold: true }, { text: '— per-task planner-executor routing audit. 12-month window before hyperscaler auto-routing defaults. Score 5/5/5 (named max in B2 and B4).' }]),
  bulletRich([{ text: 'Outcome-pricing rubric for vertical-agent buyers ', bold: true }, { text: '— per-resolution validation, per-encounter rate-setting, per-FTE-equivalent benchmarking. Bet #1 module. Score 4/4/4.' }]),
  bulletRich([{ text: 'Cross-cloud trajectory cost transparency ', bold: true }, { text: '— Vercel AI Gateway, AWS Bedrock, OpenRouter trajectory-level cost reporting. Procurement input. Score 3/3/3.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'Token-price decline outpaces optimization ', bold: true }, { text: '— named max in B4 challenges. If frontier inference compresses another four-to-ten times in 2026, the "optimization" thesis goes below the line of caring for many enterprise workloads. Severity 4 / Probability 4 / Exposure 5.' }]),
  bulletRich([{ text: 'Hyperscaler bundling of routing ', bold: true }, { text: '— Bedrock auto-optim, Vertex routing, Azure routing default-on plausible H2 2027. Severity 4 / Probability 4 / Exposure 5.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Inference compute — 10x growth or flat ', bold: true }, { text: '— inherited Crux #2. Determines whether Bet #4 / Meta-C window stays open or closes faster. Decidability 4 (Q4 2026 hyperscaler earnings) / Asymmetry 5 / Bet-size 5.' }]),
  bulletRich([{ text: 'Does outcome-based pricing become procurement standard outside CX ', bold: true }, { text: '— Bret Taylor thesis. If yes, vertical-agent ACVs reshape. Decidability 3 / Asymmetry 4 / Bet-size 4.' }]),

  // META D
  h2('Meta-D · Geopolitics'),
  p('Sovereign agents are the new operational form. Mistral Le Chat Enterprise (€600M Series C at €11B March 2026) is the only credible non-US enterprise-agent platform. UAE G42 plus Humain (KSA) extend a sovereign AI thesis into the agent layer with Falcon-derived deployments. India Sarvam and Krutrim politically funded sub-scale. China Manus (Butterfly Effect, $500M rumored valuation Q1 2026) and Coze (ByteDance) non-investable from US-LP perspective but real. US Commerce November 2025 advanced-chip-export authorizations to G42 and Humain set precedent; agent-capability export restrictions are a 2026–2027 regulatory front.'),
  h3('Opportunities'),
  bulletRich([{ text: 'EU residency wedge for F500 EU-subsidiaries ', bold: true }, { text: '— Mistral-equivalent partner play for US F500 with German, French, Nordic operations on AI Act-aligned posture. Bet #1 expansion. Score 4/3/4.' }]),
  bulletRich([{ text: 'Sovereign-agent procurement framework ', bold: true }, { text: '— "where does the trajectory run, where does the memory persist, where do action logs accrue" as the new procurement axis comparable to data residency for SaaS. Score 4/3/4.' }]),
  bulletRich([{ text: 'Non-US capability-safety translation ', bold: true }, { text: '— UK AISI Inspect, Singapore AISI, EU AI Office as the non-US capability-safety counterparts. Bet #1 international module. Score 3/3/3.' }]),
  h3('Challenges'),
  bulletRich([{ text: 'US-LP non-investability of Chinese verticals ', bold: true }, { text: '— Manus, Coze, WeChat agent platforms are real and growing but cannot enter Alex\'s capital path. Severity 2 / Probability 5 / Exposure 1.' }]),
  bulletRich([{ text: 'Export-control regime expansion to agent capability ', bold: true }, { text: '— full computer use, autonomous decision-making could enter export controls 2026–2027. Severity 3 / Probability 3 / Exposure 2.' }]),
  h3('Open questions'),
  bulletRich([{ text: 'Does Mistral cross $500M ARR by Q3 2027 ', bold: true }, { text: '— validates the sovereign enterprise-agent thesis. Decidability 4 / Asymmetry 3 / Bet-size 3.' }]),
  bulletRich([{ text: 'Does any major non-US sovereign cap-safety institute become a F500 procurement reference ', bold: true }, { text: '— if UK AISI Inspect is adopted by F500 procurement, the international reference architecture shifts. Decidability 3 / Asymmetry 4 / Bet-size 4.' }]),
);

// ===========================================================
// PART VIII — WARDLEY
// ===========================================================

docChildren.push(
  h1('Part VIII · Wardley Mapping the Agent Stack'),
  rule(),
  p('A Wardley map plots components by user-visibility (vertical axis) and evolution stage (horizontal axis: Genesis → Custom-built → Product/Rental → Commodity/Utility). The discipline of the lens is to read the slope, not the snapshot: where each component is going next, not just where it sits. The Volume II Wardley analysis covered the full AI stack; this part refreshes placement at agent-stratum resolution and identifies the 2026–2027 punctuated equilibria specific to the agent layer.'),

  h2('What Wardley says about agents now'),
  p('Most of the agent stack is not where its press releases place it. The narrative reads "MCP won, computer use is here, agents are deploying." The map shows MCP is a stable spec with a fragmenting experience, computer use is Genesis-bordering-Custom for unattended autonomous work, and most "production agents" are three-to-seven-step ReAct loops with a verifier. Evolution is bifurcated: infrastructure beneath the runtime (sandboxes, browsers, gateways, TTS, telephony) is on a twenty-four-month commodity trajectory; the operational layer above (evaluation, observability, guardrails, procurement controls, vertical workflow integration) is Custom-to-early-Product and is where durable margin lives. The field is not consolidating; it is stratifying. Surfaces below the runtime commoditize fast; vertical and compliance layers harden into moats. That is the strategic terrain.'),

  h2('Anchored user needs (top of map)'),
  p('Four user-need anchors define the dependency chains for the agent map. The first is completing a multi-step research-and-reporting task autonomously — the GAIA / BrowseComp / Deep Research use case (Anthropic Research, OpenAI Deep Research, Gemini Deep Research, Manus, Genspark). The second is operating a browser or computer to complete a back-office workflow — claims processing, expense, vendor onboarding; the CFO-credible "AI BPO" pitch. The third is handling a customer query end-to-end with voice, tools, and escalation — the Sierra / Decagon / Hippocratic / Vapi pattern and the only domain where outcome pricing has landed. The fourth is writing, testing, and merging a production code change — Claude Code / Cursor / Codex / Devin / Augment; the only category where AI labor is priced like FTE displacement at scale.'),

  h2('Layer-by-layer placement'),
  p('At the end-user surface layer (Stratum X), chat web and desktop sit at Product racing toward Commodity for casual use and back toward Custom for high-stakes; chat mobile is Product trending Commodity-bundled-with-OS; CLI surfaces are Product with slow commoditization; IDE inline is Product stratifying with Cursor and Copilot most durable; browser sidebar is Custom-to-Product for consumer but stalled at Custom for regulated; embedded SaaS surfaces sit at Product trending Commodity-bundled; computer-use UX is Genesis-to-Custom and will not cross to Product without OSWorld at sixty-five percent; voice inbound is Custom-to-Product crossing the natural-cadence line for short calls; wearable and AR is Genesis with smart glasses progressing and pendants dead; API / SDK is Product trending Commodity.'),
  p('At the vertical-product layer (Stratum IX), customer experience products sit at Custom-to-Product with a confirmed two-winner shape (Sierra, Decagon); knowledge search-agents are Custom-to-Product trending Product with ChatGPT Business encroachment; legal stays Custom-to-Product with the lowest encroachment risk; healthcare sits at Custom with HIPAA / FDA SaMD fencing; RevOps is Custom-struggling with only Clay durable; coding is Product multi-winner at prosumer and winner-take-most at enterprise; finance is Custom with NYC-anchored players (Rogo, Hebbia, Ramp AI) holding; creative is Product (ElevenLabs, Runway, Suno with RIAA risk); sovereign vertical products (Mistral, Sarvam, Manus) sit at Custom with EU AI Act enforcement as the catalyst that could move Mistral-equivalents to Product inside Europe.'),
  p('At the action-surface layer (Stratum VI), sandboxes are Product converging to Commodity within twenty-four months (Firecracker plus Linux plus Python); browser automation is Product with the operational layer on top retaining durability (Browserbase plus Stagehand plus session-recording); voice substrate is Product trending Commodity (LiveKit + Cartesia + Realtime API + Twilio/Telnyx); voice orchestration is Custom-to-Product consolidating to one or two winners with compliance as moat. At the runtime layer (Stratum II), Claude Agent SDK and OpenAI Agents SDK sit at Custom-to-Product racing to Product; Google ADK is Custom and thin outside GCP; LangGraph 1.0 is Product with margin moving to LangSmith; Mastra, Pydantic AI, CrewAI are Custom-niche-Product. At the protocol layer (Stratum III), the MCP spec is Product (held); MCP gateways are Custom-to-Product crossing in H2 2026; first-party MCP servers are Product with the long tail abandonware; A2A is Genesis.'),
  p('At the memory layer (Stratum IV), lab-native memory is Custom-to-Product with Claude Projects April 2026 GA, absorbing consumer and prosumer; standalone memory (Mem0, Letta, Zep) is Genesis-to-Custom with the compliance wedge as the only path forward; GraphRAG and LightRAG sit at Custom with selective production traction. At the planning layer (Stratum V), reasoning models are Product with `reasoning_effort` as buyer-controllable; planner-executor split is Product (gateway config flag); RLVR / GRPO trajectory fine-tunes are Genesis-to-Custom open to vertical-agent vendors who own their verifier data. At the eval/obs/safety layer (Strata VII–VIII), OpenTelemetry GenAI is Product (commodity ingest); eval platforms (Braintrust, LangSmith, Galileo) are Custom-to-Product with eval logic as lock-in and partial consolidation by 2027; Inspect AI is Custom and audit-grade; runtime guardrails (Lakera, NeMo) are Custom-to-Product mostly absorbed by 2027. At the procurement-grade controls "layer" — signed eval reports, multi-party audit, EU Act tie-out — components sit at Genesis. No vendor ships turnkey. This is the unclaimed flag.'),

  h2('The five-to-seven punctuated equilibria for 2026–2027'),
  h3('1. MCP gateways — Custom to Product, H2 2026'),
  p('Kong GA July 2025; Cloudflare expansion; Pomerium identity-aware proxy. The enterprise control plane (authentication, audit, rate-limiting, secret-injection) hardens. Reprices custom MCP builds; opens adjacent-possible for MCP-native iPaaS, policy-firewall products, F500-private registries. This sharpens Bet #3: the gateway sub-category, not the spec itself, is the punctuation.'),
  h3('2. Computer use — Genesis to Custom, mid-to-late 2026'),
  p('OSWorld 50–55% crosses approximately sixty-five percent on a frontier system; end-to-end reliability sits at roughly thirty percent at fifty steps. The stage jump is real but it is piloted-in-narrow-lanes, not deployable for unattended back-office. Reprices RPA incumbents (UiPath, Automation Anywhere); opens adjacent-possible for AI-augmented BPO at a fifth the cost for reversible, auditable click sequences. Unattended autonomous computer use stays a 2027–2028 question.'),
  h3('3. Voice telephony substrate — Product to Commodity, mid-to-late 2026'),
  p('LiveKit + Cartesia + OpenAI Realtime + Twilio/Telnyx is a stack default with sub-six-hundred-millisecond voice-to-voice for short calls. Substrate commoditizes; voice orchestration (Vapi, Retell, Bland) consolidates to one or two winners with compliance as moat. Reprices Genesys, NICE, Five9 incumbents; opens vertical voice (healthcare intake, debt collection, dental, field service).'),
  h3('4. Standalone memory — forced binary, resolves H2 2026'),
  p('Either Mem0, Letta, and Zep harden the compliance wedge — Zep most likely, approximately $50 million ARR by 2027 — or absorbed: lab-native at the consumer end, runtime primitives at the developer end. The directional answer for this volume: absorbed for consumer and prosumer, niche-standalone for compliance enterprise. Memory\'s access pattern is RAG-with-writes, not a distinct primitive. Refreshes Crux #5; rolls memory architecture into Bet #5 as a service line.'),
  h3('5. Procurement-grade agent controls — Genesis to Custom, Q4 2026'),
  p('No vendor today ships signed eval reports plus multi-party audit plus EU AI Act conformity plus action-rollback plus adaptive-adversary red-team as a turnkey bundle. EU AI Act GPAI enforcement starts August 2026; the first conformity-assessment draft (February 2026) names Inspect AI explicitly. First Custom solutions emerge from Big-4 consulting plus a Lakera-shaped partner. This is the unclaimed flag for Bet #1. The Wardley-defensible position is not "Drata for AI" (Settle-quadrant SaaS, harder cold-start) but the buyer-side Playbook that names the gap between what vendors ship and what regulators will require. Plant the flag with the open Playbook; SaaS is a downstream option, not the first move.'),
  h3('6. Eval / observability consolidation — Product, Q4 2026 to H1 2027'),
  p('OpenTelemetry stabilization killed ingest lock-in; eval logic remains. The category ceiling is approximately $300 million ARR. LangSmith stays because LangGraph stays; Braintrust is the most likely consolidator; Langfuse wins EU and self-host; two-to-three of {Galileo, Patronus, HumanLoop, Comet, Helicone, AgentOps} are acquired by hyperscalers or runtime vendors by end of 2026. The pure-play eval thesis reprices from defensible to acquisition-target.'),
  h3('7. Foundation labs walking up-stack — continuous 2026'),
  p('ChatGPT Business connectors, Claude for Work, Gemini Enterprise reprice Glean, Notion AI, and Copilot 365\'s monopoly continuously. Vertical-agent companies with deep workflow integration, outcome SLAs, and custom guardrails (Sierra, Decagon, Harvey, Hippocratic) are the least vulnerable — the moat is integration plus change-management, not the model. This confirms Bet #2 and sharpens the target list around vertical workflow integration depth.'),

  h2('Strategic quadrants'),
  h3('Pioneer (Genesis — build / explore, expect failures)'),
  p('Procurement-grade signed eval bundles (no vendor turnkey; Inspect AI closest). Computer use for unattended back-office (still thirty percent at fifty steps). Multi-party agent audit (vendor + customer + auditor on one trace with redaction). Contextual-integrity primitives for memory (no vendor ships "written in B2B sales, refuse to surface in HR"). Sovereign agent stacks for EU AI Act–exposed F500 EU-subsidiaries (Mistral-equivalent partner play). MCP-native iPaaS replacing Zapier (technically possible; no winner).'),
  h3('Settle (Custom to Product — productize what works)'),
  p('MCP server constellations for enterprise GTM SaaS (Salesforce, Outreach, Gong, Highspot, Zoominfo, Linear) — Bet #3\'s buildable target. Vertical voice agents (debt collection, healthcare intake, NPS-detractor recovery) — substrate is commodity, vertical packaging plus compliance is the moat. Vertical AI workers with deep workflow integration — the Sierra / Decagon / Harvey / Hippocratic pattern; Bet #2 = take a GTM role inside one rather than build one. Enterprise-acceptance evaluation and observability (SOC 2, model-risk, signed reports, red-team artifacts) — "Drata for AI agents." AI procurement / deal-desk SaaS — Bet #1\'s downstream product. Memory architecture as a service line (folded into Bet #5).'),
  h3('Consume (Product to Commodity — rent, do not build)'),
  p('Foundation models via API or AI Gateway. Sandboxes (E2B, Modal, Vercel Sandbox). Headless browsers (Browserbase plus Playwright). Voice substrate (LiveKit, Cartesia, Deepgram, Twilio / Telnyx). Agent runtimes — use the SDK of your dominant model provider. MCP transport plus first-party servers. AI gateways (Vercel, Cloudflare, OpenRouter). Vector databases, embeddings, rerankers (pgvector or Turbopuffer plus Voyage or Cohere). OpenTelemetry GenAI tracing.'),
  h3('Utility / Build-around (ubiquitous)'),
  p('Linux, Postgres, Chromium, WebRTC, Firecracker, Python and TypeScript, PyTorch, the public internet, Kubernetes, OpenTelemetry, Markdown, JSON-RPC.'),

  h2('Implications for Alex'),
  p('Alex\'s compounding advantage is enterprise GTM judgment — twelve years of F1000-buyer-side procurement scar tissue — plus AI-builder fluency. That fits Settle, with a Pioneer flag on procurement-grade controls and a disciplined Consume stance on everything below the runtime. The agent-layer map sharpens the prior bet stack in three specific ways. First, the unclaimed Pioneer flag is procurement-grade agent controls sold first as a buyer-side audit framework, not a vendor product. This is Bet #1\'s Wardley-defensible position. Second, Settle holds the highest-conviction zone with Bet #2 (vertical agent GTM role) and Bet #3 (MCP-native enterprise integration practice) intact but timing-sharpened around the gateway sub-category. Third, Consume names the silent leverage: anything below the agent runtime is a rent decision, with the twenty-four-month commoditization timer favorable to buyers and the build-cost unfavorable to builders.'),
  p('Where the map disagrees with the field, two corrections matter. "MCP won" is half-true — the spec is held and the experience is fragmenting. Bet #3 plans for "MCP-compatible baseline," not "MCP-native interop guarantee." "Computer use is here" is wrong for unattended autonomous work through 2026. Error compounding (ninety-five percent per step across twenty steps is thirty-six percent end-to-end) is the hard ceiling. Bet on watched and narrow products; do not bet on autonomous back-office agents to clear F500 procurement before mid-2027.'),
);

// ===========================================================
// PART IX — 7 POWERS
// ===========================================================

docChildren.push(
  h1('Part IX · Helmer’s 7 Powers and Agent-Layer Durability'),
  rule(),
  p('Helmer\'s 7 Powers — Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power — require both benefit and barrier. Mindshare is not a power. Hype is not a power. Applied strictly to the agent layer, the screen is brutal: capability gaps close in months; the runtime is the thinnest gross-margin layer; MCP is by design a non-moat. The real power positions are narrow.'),

  h2('Per-stratum power assessment'),
  p('At the foundation-model layer (Stratum I), the moat that endures is Process Power on the RL-from-trajectory-data pipeline (RLVR plus GRPO plus PRMs plus verifier harness) — not the architecture. The capability lead is rentable; DeepSeek R2 and Qwen3 close the gap at four-to-six times lower cost. Trajectory-data Process Power strengthens as labs accumulate proprietary RL data from their own products (Claude Code, ChatGPT Agent). The Cornered Resource is the approximately two-hundred senior researchers who have shipped large-parameter frontier models with reasoning loops. Branding is narrow: Anthropic owns "safety plus coding"; OpenAI owns "consumer." At the runtime layer (Stratum II), almost no powers exist. Switching costs are shallow (LangGraph-to-Claude-SDK migration is a quarter). LangChain Brand is eroding to fatigue. Vendor SDKs derive their pull from the model, not the runtime. Do not build a company here.'),
  p('At the MCP / tool-use protocol layer (Stratum III), Network Economies are forming at the registry level (eleven thousand four hundred servers in April 2026; first-party Stripe / Linear / GitHub / Snowflake servers compounding). But open protocols are by design non-moats. The durable power at this layer locates at the MCP gateway control plane (Cloudflare, Kong, Pomerium) — Switching Costs through authentication, audit, and secret-injection enterprise plumbing. Anthropic\'s Counter-Positioning win is permanent and underweighted: shipping MCP first, getting it adopted, then donating to the Linux Foundation in December 2025 — locking the standard while disclaiming control. No US lab can now re-claim spec authority. At the memory layer (Stratum IV), powers are thin. Zep has nascent Switching Costs in compliance-sensitive accounts. Lab absorption is the dominant force; only Zep holds a durable niche on compliance Process Power.'),
  p('At the planning and reasoning layer (Stratum V), powers exist inside frontier labs only (Process Power via PRM, RLVR, GRPO pipelines that buyers cannot inspect). External to labs, there is none — planner-executor-verifier is a config flag in gateway products. At the action-surface layer (Stratum VI), powers are mixed. Browserbase has emerging Switching Costs through session recording, replay, and the Stagehand DX layer — but Chromium is not proprietary. LiveKit at the WebRTC infrastructure layer is the closest thing to a Cornered Resource — the only credible AI-native real-time substrate. The Anthropic / OpenAI / Google computer-use products are demoware-grade and will not generate power until OSWorld crosses approximately seventy percent.'),
  p('At the eval and observability layer (Stratum VII), Switching Costs are real in evaluation logic (regression sets as Braintrust YAML or Galileo metric definitions take a quarter to port). OpenTelemetry GenAI conventions stabilized in January 2026 killed lock-in on trace ingest. LangSmith has tight LangGraph Switching Costs; Braintrust has eval-as-CI workflow stickiness. The durable niche is signed and auditable evaluation reports tied to EU AI Act and NIST AI RMF — and nobody ships this turnkey today. That is Bet #1\'s opening. At the runtime-safety layer (Stratum VIII), powers are thin. Lakera Brand plus early Switching Costs in regulated accounts; no prompt-injection moat. Mostly absorbed into hyperscaler bundles within eighteen months.'),
  p('At the vertical-product layer (Stratum IX) — the upper-stack power concentration — Process Power plus Switching Costs are real at Sierra (customer-experience outcome-pricing operational scar tissue plus per-resolution SLA enforcement infrastructure that took two years to build), Harvey (BigLaw RLHF on contract data plus privilege and bar liability fence), Abridge (Epic embedding depth plus clinician workflow integration), Hippocratic (per-call labor-substitute pricing plus state licensing buy-in plus Cerner and Epic integrations), Glean (organization-wide data graph that compounds with usage — the closest thing to Network Economies in the vertical layer). Cornered Resource is rare here; Harvey\'s Cravath and A&O Shearman design-partner relationships are the closest. F1000 buying is RFP-driven, not brand-driven; Branding matters less than usually claimed. Vertical-specific Process Power strengthens for the two-to-three winners per vertical and erodes for the long tail.'),
  p('At the end-user-surface layer (Stratum X), surface-by-surface differentiation. Microsoft Copilot 365 has Switching Costs (enterprise seat lock-in, M365 graph integration) plus Scale Economies (existing channel); it is the largest agentic-revenue position of 2026 with $5 billion ARR and approximately thirty million paid seats. Apple Intelligence has Cornered Resource (Neural Engine plus iOS distribution) plus Switching Costs. WhatsApp (Meta) has Cornered Resource — the dominant AI surface for the global majority once the agentic API opened in January 2026. Anthropic has Branding plus Process Power on the model but a first-party-surface deficit (no Apple Intelligence slot; Claude mobile feature-thin; no native voice product; Claude for Chrome paying-tier only). Anthropic\'s enterprise power is real but routes through API, IDE, and CLI surfaces, not consumer surfaces — a structural shape, not a temporary gap.'),

  h2('Meta-strata'),
  p('At Meta-A (capability safety), Anthropic holds Branding (uniquely owns "safety" in enterprise mind) plus Process Power (Constitutional AI, interpretability program) plus Cornered Resource (alignment researchers, approximately two hundred globally; Anthropic retained Jan Leike). Strengthening with EU AI Act conformity-assessment drafts (February 2026) citing Inspect AI explicitly. The most defensible single-vendor position in the entire stack. At Meta-B (regulation), Counter-Positioning for Mistral and EU-resident challengers under EU AI Act enforcement (late 2026): a US frontier lab cannot match "data never leaves the EU" without re-architecting its training pipeline. Palantir holds Process Power (accreditation craft) plus Cornered Resource (cleared personnel plus government relationships) at the FedRAMP / IL5-IL6 / HIPAA frontier — decades-deep. Strengthening with EU AI Act enforcement and US federal preemption volatility. This is where Bet #1 sits.'),
  p('At Meta-C (economics), powers are eroding. Token prices compress four-to-ten times per cycle; OpenRouter and Bedrock commoditize switching. Hyperscalers retain Scale Economies on inference infrastructure but pure-play inference (Groq, Together, Fireworks) has Process Power on kernels without durable Switching Costs. Anthropic\'s valuation depends on capability-lead-pricing surviving the next two cycles; it might not. At Meta-D (geopolitics), Counter-Positioning for Mistral (EU sovereignty), Sarvam (India), Manus (China-language-data Cornered Resource — Mandarin trajectory data US labs cannot legally train on). Manus\'s Cornered Resource on Chinese-language agent-trajectory data is real and US-discourse-underweighted.'),

  h2('The five most durable agent-layer power positions, May 2026'),
  p('NVIDIA at the substrate layer — Cornered Resource (CoWoS, HBM allocation) plus Process Power (CUDA) plus Scale Economies — three powers stacked, agent-stack-relevant via inference economics, durable through 2030 on training and eroding faster at inference. Anthropic\'s alignment plus trajectory-data Process Power — Constitutional AI plus Claude Code RL-from-production-trajectories plus the approximately two-hundred-person alignment talent pool. The capability lead is rentable; the Process Power on internal RL pipelines compounds with own-product usage. Endures past 2027 because the data flywheel is self-reinforcing.'),
  p('Sierra in CX — vertical Process Power plus Switching Costs. Outcome-pricing operational scar tissue, per-resolution SLA infrastructure, two-year head start on the operational moat. Helmer-strict: this is Process Power, not Brand. Endures because the operational practices took two years to build, are not codifiable in a runbook, and Decagon (the closest competitor) is one cycle behind on the same curve. Glean\'s organizational data graph — Network Economies, vertical-bounded. Value increases with users inside the same enterprise; cross-system graph is hard to replicate; ChatGPT Business connectors attack the wedge but cannot replicate the org-graph density. Endures eighteen-to-twenty-four months past 2027 if Microsoft does not ship a credible cross-tenant equivalent.'),
  p('MCP gateway control plane (Cloudflare, Kong, Pomerium) — Switching Costs via auth, audit, rate-limit, and secret-injection enterprise plumbing. Once an F500 has thirty-plus MCP servers wired through Kong\'s gateway with SSO and audit, ripping it out is a year of work. Strengthens as the registry grows. This is the durable MCP power — not "build at the MCP layer" but "own the enterprise control plane around it." Honorable mentions: Harvey at AmLaw 100 (Process Power plus privilege and bar fence; smaller TAM); Microsoft Copilot (Scale plus Switching, inherits OpenAI dependency); Palantir at the federal frontier; Browserbase\'s operational layer.'),

  h2('The five most over-rated power positions'),
  p('Cursor at $9.9 billion valuation as a durable position. Real ARR (more than $500 million run-rate), but the moat is mindshare plus developer experience, not power. Anthropic owns the model underneath (Claude Code is the encroacher); IDE inline is the form factor most exposed to foundation-lab walk-up. Switching Costs are low — engineers move IDEs in a week. Branding is not a moat. LangChain / LangGraph as the "neutral runtime moat." API churn fatigue is real; vendor SDKs ship faster; the field narrative is ahead of evidence. The durable LangChain bet is LangSmith observability, not the runtime. Memory companies (Mem0, Letta) as standalone categories. "Pinecone for memory" is the wrong analogy. Lab absorption plus RAG-with-writes economics plus opaque enterprise compliance story. Letta\'s pivot to "stateful agent runtime" is the implicit concession.'),
  p('11x and the "synthetic SDR" category. $20 million flat ARR, churn spike, Hayden Sukkar publicly conceding the quality ceiling. RevOps buyers reject vendor outcome attribution. No power. Clay survives by owning data, not by being an agent. Standalone runtime-safety vendors (excluding Lakera\'s red-team niche). Indirect prompt injection is unsolved; hyperscaler bundles cover eighty percent at zero procurement friction; Protect AI to Palo Alto was the consolidation bell. Apex, Calypso, Cranium most likely roll up. Pure-play guardrails are not a durable power.'),

  h2('Implications for Alex — career-bet calibration'),
  p('The 7 Powers screen produces a sequencing insight no other framework does. Bet #1 (Procurement Operating Standard) is the highest-power-density career bet in the portfolio — Counter-Positioning on EU AI Act enforcement plus signed-eval-report gap plus tool-boundary policy gap plus action-rollback procurement frame. This is Process Power that compounds with each F500 engagement and that no incumbent (Vanta, Drata, Secureframe) currently fills. Bet #2 (vertical agent GTM seat) is the highest-equity bet but it rents power from Anthropic, Sierra, Harvey, Glean. Bet #3 (MCP-native enterprise integration practice) is advisory power, not platform power — operational Process Power flavor from doing it ten-plus times, not software moat. The sequence the screen produces: Bet #1 first to claim the durable position, Bet #2 second to collect equity at a power-holder while the procurement scar tissue compounds, Bet #3 third as advisory practice that draws from both.'),
  p('The 7 Powers target list for Bet #2 sharpens. The most durable upper-stack positions are Sierra (Process Power on outcome-pricing operations plus emerging vertical Switching Costs), Harvey (lowest-encroachment-risk vertical due to privilege and bar liability fence), Glean (vertical-bounded Network Economies), Abridge (Epic embedding depth), Hippocratic (state licensing buy-in plus per-call labor-substitute pricing), Hebbia (NYC-native financial-services-adjacent), Rogo (banking workflow Process Power developing). The over-rated list eliminates 11x, Cresta, Lavender, and any RevOps target other than Clay from serious consideration — they do not pass the power screen even where ARR is real.'),
);

// ===========================================================
// PART X — ECOSYSTEM JTBD
// ===========================================================

docChildren.push(
  h1('Part X · Ecosystem-Level Jobs to be Done'),
  rule(),
  p('Christensen, Ulwick, and Moesta framed Jobs-to-be-Done as the top-down lens for what users hire a system for. Applied to the agent layer specifically, seven ecosystem-level jobs emerge. Each is mapped through Ulwick\'s eight-phase Job Map (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude) with the most-overlooked outcome at each phase named and the top three underserved desired outcomes flagged with importance-satisfaction gaps.'),

  h2('Job 1 · Complete a discrete back-office task without babysitting'),
  p('An operations or finance leader has a multi-step rules-governed workflow — invoice triage, payroll exception, contract abstraction, refund, KYC — and wants the agent to take it inbox-to-archive over hours-to-days, fail safely, and report. Buyer is the VP of Operations, Controller, or Shared Services lead. Willingness to pay is $25,000–$150,000 per workflow per year mid-market and $500,000–$2 million F500, often priced per-resolution, per-document, or per-FTE-replaced.'),
  p('The phase map surfaces the gaps. Define: time to translate an SOP into an agent specification — n8n and Zapier serve partially; no "SOP-to-agent" owner exists. Locate: percentage of source data reachable — Glean and Hebbia for search; ETL bespoke. Prepare: confidence tools have correct write-scope and rollback — sandboxes for code; no SaaS-write equivalent. Confirm: pre-run probability the run will not stall at step twelve — PRMs are internal at labs and not exposed to buyers. Execute: trajectories that succeed-as-judged but write wrong — the silent-failure problem, unserved. Monitor: time to detect a looping run before token blow-out. Modify: mid-flight intervention by a non-engineer — replay UIs are engineer-only. Conclude: audit-grade run summary a controller will sign — universally unserved. The three highest-importance underserved outcomes: minimize time to diagnose why a partial-failure run stopped (importance 9 / satisfaction 3); increase percentage of unattended runs producing tamper-evident, signed evidence packs (8/2); minimize trajectories that complete-as-judged but write the wrong value to a system of record (10/4 — the silent-failure problem).'),

  h2('Job 2 · Run a customer-facing conversation to resolution'),
  p('A CX or growth leader needs every contact — chat, voice, WhatsApp, SMS, email — to either resolve to a stated outcome or hand off warm with full context. Buyer is the VP of CX (incumbent) or CRO when retention-coupled. Willingness to pay anchors at $1–$4 per resolved ticket (Sierra, Decagon), $9 per hour "RN equivalent" (Hippocratic), $0.05–$0.15 per minute outbound voice (Vapi, Retell).'),
  p('The phase map: Define — time to agree what "resolved" means with the business (Sierra Outcomes leads); Locate — percentage of identity and history found across CRM/billing/help-desk; Prepare — channel compliance (TCPA, GDPR, state consent, HIPAA) pre-call, unserved; Confirm — cold-start hallucination on policies told but not tested; Execute — first-contact resolution without misrepresenting policy; Monitor — time to detect a class of failure; Modify — non-engineer CX lead ships a fix same-day, universally unserved; Conclude — handoff with no re-asking, ticket linked, full context (Sierra leads, the rest lose CSAT). The three highest-importance underserved outcomes: minimize percentage of escalations where the human re-asks something the agent already asked (10/3); increase confidence a WhatsApp or SMS agent is consent-compliant across jurisdictions pre-launch (9/2 — WhatsApp Business API opened January 2026 with almost no compliance tooling); minimize time for a non-engineer CX lead to ship a policy correction (9/3). The non-US note matters: WhatsApp-native (Yellow.ai, Haptik, Gupshup, Meta first-party) is the dominant global shape with the same phase map and a materially worse threat model — no end-to-end encryption guarantees, no audit-log inheritance.'),

  h2('Job 3 · Execute a multi-step coding change including PR review and merge'),
  p('An engineering lead has a specified change and wants the agent to branch, code, test, open the PR, satisfy CI, respond to review, and merge — without senior babysitting. Buyer is the Engineering Director, VP of Engineering, or CTO. Willingness to pay is $200–$500 per seat per month enterprise (Cursor Teams, Copilot Enterprise, Claude Code); success-priced is not stable.'),
  p('The phase map: Define — time from ticket to fully-scoped agent task (spec quality is the bottleneck); Locate — percentage of repo, doc, PR, and test context surfaced; Prepare — secrets and keys exposed during execution; Confirm — pre-PR confidence the change will not break unknown downstream; Execute — trajectories that pass tests but regress in production (SWE-Bench Verified is gameable); Monitor — wall-clock to know if CI failure is flaky vs. real; Modify — reviewer redirects mid-PR without restart; Conclude — residue (dead branches, abandoned WIPs post-merge), unserved. The three highest-importance underserved outcomes: minimize percentage of agent PRs that pass review and CI but need senior rewrite within thirty days (9/4); reduce time to disambiguate flaky CI vs. agent regression vs. environment (8/3); increase percentage of code-agent runs producing audit-grade authorship and provenance metadata (model pin, prompt, dataset hash) for compliance and IP defense (7/2 — becomes 10 in regulated industries post-Bartz and NYT v. OpenAI). The over-served caution: "make any code change from a prompt" is over-served (fourteen-plus funded players). The gaps live at the end of the job map.'),

  h2('Job 4 · Operate a SaaS application on the user’s behalf'),
  p('A line-of-business user knows the tool (Salesforce, Workday, SAP, NetSuite, ServiceNow, Notion, Linear) but does not want to drive it. Buyer is the line manager who owns the workflow — RevOps Director, FP&A lead, Service Desk lead — not IT. IT is compliance veto. Willingness to pay anchors as embedded in seat (Agentforce $30–$125, Copilot $30) or standalone $50–$200 per seat for cross-tool orchestrators (Glean, Hebbia).'),
  p('The phase map: Define — natural-language intent to executable plan (embedded copilots lead); Locate — percentage of user\'s actual app state correctly perceived (computer-use fails in production; embedded cheats via API); Prepare — OAuth blast radius for a transient task, universally unserved; Confirm — user trust the agent will not touch out-of-scope; Execute — first-try success on multi-screen workflows (Mariner approximately thirty-five-to-forty percent on OSWorld); Monitor — cognitive load of watching a SaaS-UI agent in real time (the form-factor problem); Modify — pause, edit goal, resume mid-task (ChatGPT Agent leads); Conclude — unambiguous record of what changed (embedded ships change-logs; cross-tool does not). The three highest-importance underserved outcomes: reduce OAuth blast radius — increase percentage of tasks running with least-privilege, time-boxed, scope-bounded credentials (9/2 — MCP 0.3 auth closes this eventually; today unserved; the Bet #3 wedge); increase percentage of cross-tool tasks (Salesforce → Outreach → Gong → Slack) that complete without a human reconnecting the chain (8/3); minimize calendar time a non-IT line manager waits to deploy a new agent into a sanctioned tool (8/3 — procurement gauntlet hits hardest here because the buyer is not the seat owner). Persona honesty: vendor marketing targets the CIO; the true buyer is the line manager. IT is procurement, not customer. Vendors who pitch the line manager and bring IT along sell faster (Glean\'s Slack-first wedge).'),

  h2('Job 5 · Stay current on a domain and act on what changes'),
  p('An operator (PM, AE, RevOps, compliance, architect, investor) needs a fast-moving domain monitored, summarized, prioritized, and surfaced only for decisions they would make. Buyer is the operator ($20–$200 per month) or the employer for team tier ($500–$5,000 per seat per year — AlphaSense, Hebbia, Perplexity Enterprise, Glean). The job inherits and narrows from Volume II\'s Job 3: same shape, any domain.'),
  p('The three highest-importance underserved outcomes: minimize time from event to operator-deciding (not just notified) (9/2 — Bet #6\'s target); increase confidence the filter is not silently dropping contrarian sources (8/3); minimize duplicate processing across email, Slack, RSS, podcast, newsletter, and X for the same event (7/3).'),

  h2('Job 6 · Pass agent-specific enterprise procurement and risk review'),
  p('An AI-agent vendor enters an F1000 cycle and must satisfy InfoSec, Legal, Privacy, AI Governance, Procurement, and the business sponsor on agent-specific risks — autonomy scope, tool-boundary policy, indirect prompt injection, action rollback, sub-agent privilege, Article 14 oversight, eval reproducibility — to close within the buyer\'s planning cycle. The job inherits and narrows from Volume II\'s Job 4. Buyer is the AI vendor\'s sales leader; the real customer is the F1000 committee. Willingness to pay anchors at $50,000–$250,000 per year for a tool that closes the gap (Vanta-shape).'),
  p('The phase map is the Playbook\'s table of contents. Define — map the buyer\'s six counterparty checklists to vendor evidence (Vanta and Drata for SOC 2; nothing AI-specific). Locate — artifacts (model cards, evaluations, DPAs, AI policy) in one place (TrustCenter partial). Prepare — agent-trajectory eval evidence the buyer accepts (no turnkey signed report). Confirm — pre-call confidence AI Governance will sign, unserved. Execute — time in queue at each of six counterparties (Vanta-style workflow needed). Monitor — visibility into which counterparty is blocking, unserved. Modify — counterparty-specific evidence packs on demand. Conclude — evidence freshness through annual review. The three highest-importance underserved outcomes: minimize calendar time from security questionnaire to signed AI Governance sign-off (10/2 — Bet #1\'s target); increase percentage of agent-specific risk questions (indirect injection, tool-boundary, action rollback, sub-agent privilege) the vendor answers in standardized form (9/2); reduce bespoke effort for an EU AI Act / NIST AI RMF / ISO 42001 conformity tie-out (8/2 — rising fast). The honest demand check: buyer-side demand is real and growing (Volume III A6 lists the five questions). Vendor-side demand is partly marketing-induced. Buyer-pull is sufficient — the falsifiability test (500 downloads / 50 inbound conversations in 60 days) is the measurement.'),

  h2('Job 7 · Onboard or ramp a new role using an agent-augmented training stack'),
  p('A manager hires into an AI-native role (AE, FDE, Applied AI engineer, CS, ops analyst) and wants the hire to reach productive output in weeks rather than quarters by pairing them with an agent that scaffolds workflow, coaches tool-by-tool, and produces an observable trace for ramp assessment. Buyer is the hiring manager (primary), L&D / People Ops (channel). Willingness to pay anchors at the L&D budget of $1,200 per employee per year (ATD 2024); compressing a six-month ramp to three is worth $20,000–$80,000 per hire. Most "AI for onboarding" is repackaged LMS — this job is different. An agent that does the work alongside the new hire and tapers as the hire ramps. Nobody ships it cleanly in May 2026.'),

  h2('Cross-job synthesis'),
  p('Three patterns underserve universally. First, Conclude. Across all seven jobs, the Conclude phase — signed evidence pack (Job 1), warm handoff (Job 2), provenance metadata (Job 3), change-log (Job 4), decision routing (Job 5), counterparty evidence (Job 6), agent taper (Job 7) — is the worst-served phase. Vendors compete on Execute. Buyers feel pain at Conclude. Single highest-leverage pattern in the volume. Second, Modify by a non-engineer. Replay UIs exist for engineers (LangSmith, Braintrust); cockpit UIs for the line manager, the CX lead, the FP&A director do not. Every job map shows a Modify gap of seven or higher. This is the operator-translation gap inside the runtime — adjacent to Bet #6, productizable. Third, Confirm (pre-flight). Process-reward models exist inside frontier labs but are not exposed to buyers. Pre-flight checks are technically feasible and commercially absent. Closing this turns Job 1 from "agent attempts, sometimes succeeds" into "agent commits, reliably succeeds" — the difference between $25,000 and $250,000 ACV.'),
  p('Three patterns over-serve. Execute on coding tasks: Cursor, Claude Code, Codex, Augment, Cognition, Lovable, Replit, Bolt, v0, Magic, Reflection, Factory, Plandex, Aider, Cline, Continue — fourteen-plus funded players, marginal demand at Execute exhausted. Locate / enterprise search-agents: Glean has the moat; Hebbia is the NYC specialist; Notion AI, Copilot, ChatGPT Business connectors, Slack AI, Box AI all attack — twelve vendors for a Locate problem consolidating to two-to-three winners. Execute on inbound chat: web and mobile chat-as-form-factor is over-served; the next hundred chat UIs will not move enterprise demand. The win is Conclude (escalation handoff) and Confirm (pre-deployment trust), not more chat.'),
  p('Recommendations tied to Bets. Bet #1 (Procurement Playbook) maps precisely to Job 6. The Job 6 phase map is the Playbook\'s table of contents. The five risk-officer questions from Volume III A6 (signed reproducible eval reports; adversarial-test suite; tool-boundary policy; action-rollback story; EU AI Act / NIST AI RMF / ISO 42001 conformity tie-out) are the five chapter prompts. The Opportunity-10 on "calendar-time to AI Governance sign-off" is the falsifiable hypothesis. Position eventual SaaS as "Vanta for the agent-specific gauntlet" with the Conclude-phase evidence pack as the demo. Bet #2 (vertical agent GTM seat) maps to Jobs 2, 4, and 7. Sierra and Decagon win Job 2; Glean and Hebbia win Job 4 in knowledge; Hippocratic wins Job 2 plus Job 7 in clinical; Harvey wins Job 4 in legal; Rogo and Ramp AI win Job 4 in finance. The Field-CTO or Director-of-GTM role is paid to close the Confirm + Modify + Conclude gaps for one job in one vertical. Frame interviews around "your sales team is selling Execute; the buyer is signing on Confirm and Conclude — here is how I close that." Sierra (NYC dual-HQ) is the cleanest fit; Hebbia and Rogo are NYC-native sleepers worth equal weight. Bet #3 (MCP-native integration) maps to Job 4\'s OAuth blast radius and Job 1\'s missing write-action sandbox. Job 4\'s "least-privilege, time-boxed credentials" is what MCP 0.3 auth enables but no incumbent SaaS has shipped. Filter the Bet #3 audit by which Job 4 / Job 1 outcomes each unlocks. Do not ship for completeness; ship for the Confirm / Conclude gap. The cross-Bet through-line: Conclude is the connective tissue. Bet #1 sells the Conclude gap; Bet #2 closes it inside a vertical; Bet #3 ships the substrate; Bet #6 is the distribution layer that makes the rest reach.'),
);

// ===========================================================
// PART XI — SYNTHESIS: 7 BETS, 5 RISKS, 5 CRUXES (refreshed)
// ===========================================================

docChildren.push(
  h1('Part XI · Synthesis — Seven Bets Refreshed, Five Risks, Five Cruxes'),
  rule(),
  p('Five frameworks were applied at agent-layer resolution. Where they converged, conviction strengthens. Where they diverged, the open questions are honest. The seven Bets from Volume II carry over rather than multiply; each is refreshed with the agent-specific delta. Five Structural Risks and five Cruxes update accordingly.'),

  h2('How the agent-layer frameworks converged'),
  p('The single observation all five agent-layer frameworks produced is that the highest-power-density, highest-claimability, highest-asymmetry near-term opportunity for Alex sits in agent-specific procurement (Bet #1), not the vertical-agent GTM role (Bet #2). The OCQ Matrix surfaces multiple high-claimability opportunities — signed reproducible eval reports, EU AI Act Article 14 human-oversight playbook, tool-boundary policy template, agent-trajectory cost audit, form-factor procurement audit, sandboxing-as-control mapping, sectoral overlay advisory — that all compound into Bet #1 as modules rather than into separate productized bets. The Wardley map places procurement-grade agent controls at Genesis stage — the only unclaimed flag at Pioneer. The 7 Powers screen names procurement Process Power at Meta-B as the only durable position Alex can claim rather than rent. The Ecosystem JTBD analysis maps Job 6 phase-by-phase to the Playbook\'s table of contents. The Talent and Capital Flow tracker confirms NYC peak hiring window for Bet #2 but also confirms that the Stripe / Ramp / Datadog / Snowflake migration is creating its own marketplace at the procurement-readiness layer where the buyers are. The sequencing implication is unambiguous: Bet #1 first, Bet #2 second, Bet #3 third.'),

  h2('The seven Bets — refreshed'),

  h3('Bet 1 · The Enterprise AI Procurement Operating Standard (agent-specific)'),
  p('Hypothesis (refreshed). Every F1000 stood up an AI council in 2024–2025 and is procuring AI agents specifically — not just LLMs — with six non-overlapping approvers (InfoSec, Legal, Privacy, AI Governance, Procurement, business sponsor) plus an agent-specific overlay that no incumbent owns: tool-boundary policy, indirect prompt-injection adaptive red-team, action-rollback documentation, sub-agent privilege separation, signed reproducible eval reports, EU AI Act Article 14 human-oversight tie-out, sectoral overlay (FINRA, HIPAA, TCPA). A commercial operator with twelve years of buyer-side procurement scar tissue plus AI-builder fluency can plant the canonical flag in 90 days by publishing the open Playbook that names these gaps. Falsifiability. If the open Playbook gets fewer than 500 downloads or fewer than 50 inbound conversations in 60 days, or if Vanta, Drata, or Secureframe ship a credible AI-specific agent-procurement product in that window, the productized SaaS thesis is dead. Conviction. Five stars — refreshed up from the prior addendum on the strength of five-framework convergence. Delta from Volume II. Adds the seven agent-specific overlays (tool-boundary, action-rollback, etc.); adds the EU AI Act Article 14 anchor as the most actionable near-term regulatory lever; reframes from "publish, then advise, then productize" to "publish, observe, advise on procurement audits, decide on productization at month nine." Next action. Outline the Playbook in Week 1 using the Job 6 phase map and the A6 five-questions structure. Thirty expert interviews in Weeks 2–6. Publish in Week 12 with the open downloadable Procurement Rubric attached.'),

  h3('Bet 2 · Vertical Agent GTM Leadership Role'),
  p('Hypothesis. Sierra ($175M+ ARR at $10B rumored March 2026), Decagon ($80M+ at $4.5B), Glean ($300M+ at $7.2B), Harvey ($100M+ at $5B), Hippocratic ($50M+ at $2B), Hebbia (NYC HQ, $50M+, raise overdue), Rogo (NYC HQ, $30M+ at $400M), Clay (NYC HQ, $80M+ at $1.5B), Ramp AI org (NYC HQ, $20B+ raise rumored Q2 2026), Runway (NYC Chelsea HQ, $100M+) plus Augment ($40M at $977M) and Decagon are hiring exactly Alex\'s profile at $300–$400K base plus 0.05–0.40% equity. NYC vertical-agent hiring is at historic peak Q2 2026. Falsifiability. If 6 months of focused NYC search yields no offers in this band, the bet on Alex\'s profile is wrong or the market is more SF-anchored than the talent flow suggests. Conviction. Five stars — held. Delta from Volume II. Expanded NYC target list adds Hebbia, Rogo, Clay, Runway, Ramp AI org alongside the existing Sierra / Decagon / Glean / Harvey / Hippocratic / Augment / Decagon set. The 7 Powers screen sharpens the highest-power targets (Sierra, Harvey, Glean) and eliminates the over-rated (Cresta, Lavender, any RevOps target other than Clay). The Anthropic ARR Crux (Q3 2026 disclosure or leak) becomes the single load-bearing valuation variable. Next action. Time the offer before the up-round at Hebbia, Rogo, or Augment. Open consulting-alumni pipeline (BCG / McKinsey / Bain AI practice partners) as a less-competed feed-stock into Sierra / Hebbia / Harvey. Sign before Anthropic ARR resolution Q3 2026 if conviction is high; after if wobbly.'),

  h3('Bet 3 · MCP-Native Enterprise Integration Practice (reframed)'),
  p('Hypothesis (refreshed). MCP crossed Genesis-to-late-Custom in December 2025 (Linux Foundation governance); the spec is held and the experience is fragmenting silently along four fork vectors. The durable power is at the gateway control plane (Cloudflare, Kong, Pomerium) — Switching Costs via auth / audit / rate-limit / secret-injection — and at first-party MCP servers from SaaS incumbents (Stripe, Linear, GitHub, Snowflake, Databricks, ServiceNow). Productized servers commoditize the moment Salesforce or HubSpot ships first-party. Alex\'s claimable position is advisory / practice, not platform — Process Power flavor (operational scar tissue from doing it ten-plus times) plus Branding flavor (canonical voice via the Playbook). Falsifiability. If MCP forks (Anthropic-vs-OpenAI proprietary tool-use schemas diverge materially, or A2A wins agent-to-agent without MCP), the entire MCP-layer thesis weakens. Watch for any major vendor unilaterally extending MCP without spec coordination. Conviction. Four stars — held with the reframe. Delta from Volume II. Reframed from "build MCP servers for enterprise GTM SaaS" to "advisory and practice layer around MCP gateway deployment plus private-registry curation plus first-party server quality grading." Productize at month twelve or eighteen if scar tissue justifies. Next action. Q2 2026 audit of the ten SaaS systems most lacking MCP servers in enterprise GTM, filtered by Job 4 / Job 1 outcome unlock. Pair-with-Cloudflare / Kong / Pomerium as the AI-procurement specialist on gateway deployment.'),

  h3('Bet 4 · Inference Cost Optimization / FinOps for Trajectories'),
  p('Hypothesis (refreshed). The median enterprise runs un-tuned vLLM on over-provisioned H100s. EAGLE-3 at three-to-six-point-five times, FP4 quantization, prompt caching, and aggregator routing can deliver three-to-ten times cost reduction at the token level. At the trajectory level, the planner-executor-verifier split — route seventy-to-eighty-five percent of tokens through cheap executors — is the durable architectural idea and the FinOps-for-Trajectories advisory layer. The procurement-side audit is sellable today; the technical work is straightforward for a two-person services team. Falsifiability. AWS Bedrock auto-optimization features ship in 2026, slamming the twelve-month window. Or token prices fall fast enough that "optimization" is below the line of caring for many enterprise workloads. Conviction. Four stars. Delta from Volume II. Splits into two layers: per-token FinOps (the Volume II framing) and per-trajectory FinOps (the agent-specific reframing). The latter has a sharper twelve-month window because hyperscaler auto-routing of planner-executor is plausible by H2 2027. Next action. Free first audit for five mid-market AI-spending companies; build case studies; decide by Q3 2026 whether to scale or fold into Bet #1 as a module.'),

  h3('Bet 5 · Enterprise RAG plus Memory Architecture Practice'),
  p('Hypothesis (refreshed). F500 enterprises are paralyzed by eight-plus vector DB options, five embedding choices, three reranker options, four retrieval paradigms, plus the memory-architecture question (lab-native vs. Mem0 vs. Letta vs. Zep vs. summarize-and-pgvector). The decision is $50,000–$500,000 per workload and they have no vendor-neutral guidance. Pure architecture sale; commercial fluency is the asset. Falsifiability. Long-context (Gemini 2M tokens, Claude prompt caching) eats RAG at the low end faster than enterprise-scale grows at the high end. Or vector DB consolidation makes the choice trivial. Conviction. Four stars. Delta from Volume II. Folds memory architecture into the service line per the Crux #5 directional answer (consumer/prosumer absorbed; compliance-enterprise niche-standalone). Next action. Bundle as "Enterprise AI Architecture Audit" alongside Bet #1\'s Playbook and Bet #4\'s FinOps. Three-product practice, one buyer.'),

  h3('Bet 6 · Operator’s Translation Newsletter / Public Voice'),
  p('Hypothesis. Weekly "operator\'s translation" newsletter — translate frontier capabilities into specific operator implications (enterprise AE, RevOps lead, GTM head). Compounds positioning for everything else. JTBD Job 5 distribution layer; the "what changed → I should change Y" gap. Falsifiability. If subscriber growth is below 2,000 in 6 months and no inbound role or advisory comes from it, kill at month 6 or commit harder. Conviction. Three stars. Delta from Volume II. Confirmed as the distribution layer for the rest of the bets; the JTBD analysis sharpens the angle around Conclude-phase translation ("what should you do next?") rather than executive-brief summarization. Next action. Kit v1 published Week 2. Decide on cadence by Week 4.'),

  h3('Bet 7 · VC Operating Partner / Platform Path'),
  p('Hypothesis. VC platform teams need someone who can read technical updates and translate them to portfolio-company GTM teams. NYC funds (Lerer Hippeau AI-platform rumored Q1 2026, FirstMark MAD AI specialist, Insight NYC AI-advisory, Lux sci-tech / AI) are visibly hiring for this profile. Falsifiability. If Bets 1, 2, 3 land, this is downstream and lower priority. If none land by month 12, this becomes the primary path. Conviction. Three stars; four if it becomes primary. Delta from Volume II. The VC-principal-to-operator pattern (Carey Lai Insight → Sierra April 2026 and similar) confirms platform and operator paths converging at the senior level. Next action. Build relationships at three NYC funds via RAAIS, Betaworks, and FirstMark MAD events. No active applications until Q4 2026 unless Bets 1–3 stall.'),

  h2('The five Structural Risks — agent-layer refreshed'),
  h3('Risk 1 · Foundation labs walking up-stack into vertical applications'),
  p('Threatens Bet #2 most directly. ChatGPT Business connectors, Claude for Work, Gemini Workspace agents continuously compress vertical-agent vendor moats. Watch the Connectors / Skills / Apps store on each platform. Mitigate by targeting verticals with regulatory or workflow moats (legal, healthcare, financial services) where horizontal foundations cannot easily land. The 7 Powers screen confirms the mitigation: Harvey, Abridge, Hippocratic, Rogo have the deepest vertical Process Power.'),
  h3('Risk 2 · MCP silent fork via Responses-API proprietary path'),
  p('Threatens Bet #3 thesis materially if "MCP-compatible but not MCP-native" becomes dominant by 2027. Watch for OpenAI Responses-API extensions outpacing MCP-spec evolution; watch A2A adoption outside Google; watch quality split between first-party MCP servers and the long tail. Mitigate by reframing Bet #3 to advisory plus gateway-adjacent rather than productized servers; this is now done.'),
  h3('Risk 3 · Anthropic ARR resolution (single load-bearing variable for Bet #2 timing)'),
  p('Anthropic ARR ($24B vs. $30B disputed) resolves Q3 2026. Lower bound: vertical-agent valuations compress twenty-to-thirty percent (Sierra $10B to $6–$8B); equity bands tighten; timing slows. Upper bound: equity strengthens; timing accelerates. Both ends are defensible in May 2026. Mitigate by signing Bet #2 before resolution if conviction is high, after if wobbly.'),
  h3('Risk 4 · Hyperscaler bundling of runtime safety, eval, sandbox, and routing'),
  p('Threatens Bet #4\'s per-token / per-trajectory window and the standalone eval / observability category. AWS Bedrock auto-optim, Vertex routing, Azure routing default-on plausible H2 2027. Pure-play eval-and-observability pure-plays roll up. Mitigate by folding FinOps into Bet #1 modules and treating eval as a Bet #1 procurement-rubric input rather than a standalone build.'),
  h3('Risk 5 · EU AI Act paper-tiger outcome'),
  p('Threatens Bet #1 advisory TAM. If first enforcement late 2026 stays small and procedural, Bet #1 stays niche but defensible. Sell EU compliance (stable) plus contractual compliance (always required) rather than CA-specific or US-state-specific programs. The Wardley placement of procurement-grade controls at Genesis holds regardless; the productized SaaS path is the part that gates on EU teeth.'),

  h2('The five Cruxes — agent-layer refreshed'),
  h3('Crux 1 · Anthropic ARR — $24B or $30B'),
  p('Decidability Q2–Q3 2026 (audited reports or leaks). Lower bound = vertical-agent valuations compress twenty-to-thirty percent. Upper bound = Bet #2 timing accelerates. Watch The Information (Stephanie Palazzolo), Anthropic disclosure cadence, Stripe data leaks.'),
  h3('Crux 2 · MCP — commons or silent fork by EOY 2026'),
  p('Decidability H2 2026. Fork = Bet #3 dies in productized-server form; commons = advisory practice accelerates. The reframe to gateway-adjacent advisory means Bet #3 is defensible either way; the productization decision gates on this Crux. Watch major-vendor proprietary tool-use schema announcements; watch A2A adoption.'),
  h3('Crux 3 · OSWorld 65% on a frontier system by Q3 2026'),
  p('Decidability Q3 2026 (public scoreboard event). The threshold that moves computer use from supervised to deployable for narrow back-office. If crossed, the unattended-agent reliability binding constraint relaxes a quarter earlier than this volume assumes; Bet #3 should add an MCP-servers-for-the-systems-back-office-computer-use-agents-need sub-line. Watch the OSWorld leaderboard.'),
  h3('Crux 4 · EU AI Act Article 14 enforcement teeth (late 2026)'),
  p('Decidability late 2026 (first enforcement actions). Determines whether Bet #1 advisory becomes a $10-billion-plus category or stays niche. Watch Commission guidance and first GPAI fines. The April 2026 Article 14 oversight draft is the most actionable near-term lever.'),
  h3('Crux 5 · Long-term memory — standalone or absorbed'),
  p('Decidability 12–18 months. Directional answer from this volume: absorbed for consumer / prosumer; standalone-niche for compliance enterprise. Bet #5 folds memory architecture as a service line. Watch Anthropic, OpenAI, Google native memory feature launches; watch Mem0 and Letta funding events.'),
);

// ===========================================================
// PART XII — 6/12/18-MONTH ACTION MAP
// ===========================================================

docChildren.push(
  h1('Part XII · 6 / 12 / 18-Month Action Map for Alex'),
  rule(),
  p('The seven Bets translate into a sequenced playbook. The sequence is the synthesis of all five framework analyses applied at agent-layer resolution: Bet #1 first to claim a durable position, Bet #2 second to collect equity at a power-holder, Bet #3 third as advisory practice compounding from both. Bets #4 and #5 fold into Bet #1 as modules; Bet #6 is the distribution layer that makes the rest reach; Bet #7 is the long-arc fallback.'),

  h2('Months 0–6 · Plant the procurement flag and run the vertical-agent role search in parallel'),
  bullet('Bet #1 — outline the Procurement Playbook in Week 1 using the Job 6 phase map and the A6 five-questions structure as the table of contents and chapter prompts. Thirty expert interviews in Weeks 2–6 with F1000 InfoSec, Legal, Privacy, AI Governance, Procurement, and business-sponsor counterparties to validate the gaps. Publish in Week 12 with the open downloadable Procurement Rubric attached. Measure the 500-downloads / 50-inbound test at day 60.'),
  bullet('Bet #2 — open the NYC search in parallel from Week 1 with a target list of ten: Sierra (Field-CTO / Head-of-Enterprise-East seat, highest-aligned), Decagon, Glean, Harvey, Hippocratic, Hebbia, Rogo, Clay, Ramp AI org, Runway. Time the offer before the up-round at Hebbia, Rogo, or Augment (the under-funded relative to ARR velocity targets). Open the consulting-alumni pipeline (BCG / McKinsey / Bain AI practice partners in NYC) as a less-competed feed-stock into Sierra / Hebbia / Harvey.'),
  bullet('Bet #6 — publish the operator-translation newsletter Kit v1 by Week 4. Cadence decision by Week 8 (weekly vs. biweekly). Cross-pollinate Bet #1 Playbook downloads with newsletter subscribers; correlation is the right-audience proof.'),
  bullet('Bet #4 — pilot one trajectory cost-and-latency audit as the Bet #1 module test case. Free first audit for one mid-market AI-spending company; case study at month 6.'),
  bullet('Track Crux #1 (Anthropic ARR Q3 2026 resolution) as the single load-bearing Bet #2 timing variable. Sign before resolution if conviction is high; after if wobbly.'),

  h2('Months 6–12 · Commit to whichever survived'),
  bullet('If Bet #1 Playbook clears the falsifiability test (500 downloads / 50 inbound), commit to the advisory phase: 3–5 paid engagements at $25–100K each, with at least two Procurement Audit reports and one Article 14 oversight playbook in deliverables. Decision on SaaS productization at month nine.'),
  bullet('If Bet #2 offer has not landed by month 6 in the target band, expand to the second tier (Decagon NYC, Regal, smaller bands). If no offer by month 9, the bet on Alex\'s profile is wrong OR the market is more SF-anchored than the data suggests. Reassess.'),
  bullet('If Bet #6 has crossed 5,000 subscribers and 3+ inbound advisory or role conversations, commit harder (weekly cadence, paid tier). If not, kill at month 6 per falsifiability.'),
  bullet('Bet #3 audit of the ten SaaS systems most lacking MCP servers in enterprise GTM (Q3 2026). Pair-with-Cloudflare / Kong / Pomerium as the AI-procurement specialist on gateway deployment. Decide on productization vs. advisory-only at month twelve.'),
  bullet('Track Crux #2 (MCP commons or fork by EOY 2026), Crux #3 (OSWorld 65%), Crux #4 (EU AI Act teeth). Each answer-event reprices one or more bets.'),

  h2('Months 12–18 · Compound around the survivors'),
  bullet('Bet #1 — if SaaS productization decision is GO, capitalize. If NO, sustain the advisory practice at $250–500K annual revenue with three-product bundling (Playbook + Architecture Audit + FinOps for Trajectories).'),
  bullet('Bet #2 — if a vertical-agent role landed, the first twelve months are about delivering on the Confirm + Modify + Conclude gaps for that vertical\'s primary job. The advisory practice continues at a controlled cadence.'),
  bullet('Bet #3 — productize at month twelve or eighteen if scar tissue justifies; otherwise sustain as advisory.'),
  bullet('Bet #7 — if Bets 1, 2, 3 stall, this becomes the primary path. Build relationships at three NYC funds via RAAIS, Betaworks, FirstMark MAD; active applications Q4 2026.'),
  bullet('Track all five Cruxes monthly. The one that resolves first reprices the next 12 months\' sequencing.'),

  h2('Per-quarter check-in template'),
  p('Status against each Bet: hypothesis still holding? Leading indicators moving the right way? Conviction up, down, or flat? Cruxes resolved in the quarter — which bets re-rank? Risks materialized — which bets need defensive moves? Talent and Capital Flow refresh — what is the NYC hiring market doing? Each quarter should produce a one-page tracker update plus a single-decision focus for the next twelve weeks.'),
);

// ===========================================================
// PART XIII — AGENT-SPECIFIC PROCUREMENT RUBRIC
// ===========================================================

docChildren.push(
  h1('Part XIII · The Agent-Specific Procurement Rubric (Appendix to Bet #1)'),
  rule(),
  p('This appendix is the agent-specific section of the future Enterprise AI Procurement Operating Standard. Per the Volume III mandate, it must drop into the Playbook as Part XIII or as a standalone rubric document. The structure follows the Job 6 phase map (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude) and the five risk-officer questions from the Volume III A6 brief. Each section names what the buyer should ask, what good vendor answers look like, what vapor sounds like, and where to verify.'),

  h2('1. Define — Map the agent\'s autonomy scope'),
  p('Ask the vendor: What does this agent do unattended? What requires a human approval gate? What requires sub-agent privilege separation? Where does the agent\'s decision authority stop? Good answer: a written autonomy scope document with a tool-by-tool authority list ("agent can read invoices, can route to approver, cannot post journal entries without controller sign-off"), with action-confirmation gates documented, sub-agent privilege separated. Vapor: "the agent uses your existing approval flows" without a written map. Verify: ask for the system prompt, the tool schema, and a trajectory replay of a representative task.'),

  h2('2. Locate — Inventory the data and tool reach'),
  p('Ask: What systems does the agent read? What does it write? What is the OAuth blast radius for a typical task? Where does memory live physically? Who can subpoena it? Good answer: a data-flow diagram with named systems, scopes per tool call, MCP server inventory, memory residency commitment (US, EU, both), Schrems-II posture, GDPR Article 17 forget API with auditable deletion confirmation, HIPAA BAA available if applicable. Vapor: "we follow industry best practices." Verify: ask for a DPA, a memory residency commitment in writing, and a sample deletion-confirmation log.'),

  h2('3. Prepare — Tool-boundary policy and runtime safety stack'),
  p('Ask: Show me your tool-boundary policy. Which tools can the agent invoke unsupervised? Which require approval? Which are blocked when context is tainted by external content? What is your defense stack for indirect prompt injection via tool returns? Show me your adaptive-adversary test results (not public-corpus). Good answer: a five-layer defense stack — treat tool returns as untrusted (tag bytes, degrade high-privilege when planning context is tainted); action-confirmation gates for write/pay/send/escalate or run in reversible sandbox; output validation and schema enforcement; sub-agent privilege separation; continuous red-team (Promptfoo, Garak, Lakera Red, or equivalent). Adaptive-adversary numbers between 60–80%, honestly disclosed. Vapor: 99% PI detection without adaptive-adversary qualification. Verify: ask for the most recent red-team report and the adaptive-adversary methodology.'),

  h2('4. Confirm — Pre-flight evaluation evidence'),
  p('Ask: Show me a signed reproducible eval report for this agent against my use case, with model pin, dataset hash, harness version. Show me your trajectory regression set. How big is it? How was it curated? How often is it refreshed? Good answer: a written signed report tied to a specific model pin (e.g., claude-opus-4-5-20251101), dataset hash, harness version, and a regression set of 200–1,000 trajectories curated from production traffic with monthly refresh cadence. Inspect AI compatibility is a plus; OpenTelemetry GenAI conventions for trace ingest are table stakes. Vapor: "our internal benchmark." Verify: ask to reproduce one score on the buyer-side; treat unreproducible scores as untrusted.'),

  h2('5. Execute — Action-rollback story'),
  p('Ask: Show me the action-rollback story for every write tool. If the agent writes the wrong value into our system of record, what is the recovery path? Good answer: write tools wrapped in a reversible-action layer (database row versioning, idempotency keys, dead-letter queues for irreversible side effects with human approval before execution), audit log accessible to the buyer in real time, alerting on anomalous write rates. Vapor: "we have logging." Verify: ask for a sample audit log and the recovery procedure for a synthetic incident.'),

  h2('6. Monitor — Trajectory observability and silent-failure detection'),
  p('Ask: How do I detect a trajectory that completes-as-judged but writes the wrong value to a system of record? What is your silent-failure rate? How do I instrument my own observability against your agent? Good answer: trajectory observability exposed to the buyer via OpenTelemetry GenAI conventions, sample-based human review of agent decisions, written silent-failure rate from production with the methodology, and integration hooks for the buyer\'s SIEM. Vapor: "you can use our dashboard." Verify: ask for an exported sample trace and confirm it parses in the buyer\'s observability stack.'),

  h2('7. Modify — Non-engineer intervention capability'),
  p('Ask: Can a non-engineer line manager redirect the agent mid-task or correct a policy without an engineering ticket? How long does it take to ship a policy correction? Good answer: a cockpit UI built for the line manager (CX lead, FP&A director) with policy editing, prompt editing, and approval-flow editing without code; ship-time measured in hours not days. Vapor: "you can file a support ticket." Verify: ask for a live demo from a non-engineer.'),

  h2('8. Conclude — Counterparty evidence and audit pack'),
  p('Ask: Show me the EU AI Act / NIST AI RMF GenAI Profile / ISO 42001 conformity-assessment tie-out. Show me how this evidence stays fresh through annual review. Good answer: a written tie-out document mapping the vendor\'s controls to each named framework with named control IDs and reproducible evidence per control. Counterparty-specific evidence packs available for each of the buyer\'s six approval lanes (InfoSec, Legal, Privacy, AI Governance, Procurement, business sponsor). Annual refresh process documented. Vapor: "we have SOC 2." Verify: ask for the tie-out and walk it line-by-line.'),

  h2('Scoring guidance'),
  p('Rate each of the eight sections on a five-point scale (5 = excellent / verified / signed evidence; 1 = vapor / unverifiable / unwilling to disclose). A vendor scoring below 3 average should not pass an F1000 AI Governance review on agent-specific procurement as of May 2026. The buyer should expect that approximately twenty percent of agent vendors today clear an average of 3.5 or higher on this rubric; the remaining eighty percent need either a roadmap commitment in writing or a contractual SLA backed by exit terms. The Procurement Playbook will maintain a vendor-readiness leaderboard updated quarterly as part of the public artifact.'),

  h2('Closing note'),
  p('This rubric is the buyer-side complement to the vendor-side eval and observability roadmap (Stratum VII). The procurement-readiness gap in the agent layer is not that buyers do not know what to ask; it is that no canonical source compiles the questions in agent-specific form and validates the answers. The Volume III observation is that the canonical source is what Bet #1 ships. The rubric above is the demo. The Playbook is the full document. The SaaS productization is the option, not the first move.'),
);

// ---------------- DOCUMENT ASSEMBLY ----------------

const doc = new Document({
  creator: 'A. Yedi',
  title: 'The Agent Layer — A Decisions Playbook (Volume III Addendum)',
  description: 'Five framework analyses applied at agent-layer resolution; seven refreshed Bets, five Risks, five Cruxes.',
  styles: {
    default: {
      document: { run: { font: FONT, size: 22, color: COLOR_INK } },
    },
  },
  numbering: {
    config: [{
      reference: 'bullets',
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: '•',
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 240 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 },
        size: { width: 12240, height: 15840 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({
            text: 'SUBSTRATE · VOLUME III · DECISIONS PLAYBOOK',
            font: FONT_MONO, size: 14, color: COLOR_GRAY,
            characterSpacing: 80,
          })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({
            children: ['Page ', PageNumber.CURRENT, ' of ', PageNumber.TOTAL_PAGES],
            font: FONT_MONO, size: 14, color: COLOR_GRAY,
          })],
        })],
      }),
    },
    children: docChildren,
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(__dirname + '/AI_AGENTS_ADDENDUM.docx', buf);
  console.log('Wrote AI_AGENTS_ADDENDUM.docx ·', (buf.length / 1024).toFixed(1), 'KB');
});
