# Book Distillation Workflow — Canonical SOP

**Purpose:** The complete methodology for unpacking a large rich text (book,
academic paper collection, course transcript, internal documentation corpus)
into a structured set of production-grade Claude skills + reusable knowledge-base
references + an all-encompassing consolidated summary.

This is the SOP. Future text distillations should follow it. Deviations should
be deliberate, not accidental.

---

## When to Use This Workflow

- Distilling a technical book (300+ pages) into reusable skills
- Processing a domain-specific corpus where the same patterns repeat
- Onboarding a new domain (e.g., a new industry vertical) into the skill tree
- Migrating tribal knowledge from a body of writing into a queryable form

**Don't use this workflow for:**
- Single-chapter content (overkill — write a skill directly)
- Personal notes / blog posts (no structured frameworks to extract)
- Live-changing material (this produces a snapshot; refresh effort is meaningful)

---

## Output Artifacts (The Five Layers)

For every text processed, you produce **five layers** of artifacts. Each
serves a different purpose and lives in a specific location.

| Layer | What it is | Lives in | Reading audience |
|---|---|---|---|
| **1. Skills** | Action-focused decision rules (one per major chapter or section cluster) | `<category>/<skill-name>/SKILL.md` | Claude (auto-invoked); user when triggered |
| **2. Additional Experts** | Best practices + advice + worked examples in expert voice | `<category>/references/<book-slug>/additional-experts.md` | User browsing for deeper guidance |
| **3. Frameworks** | Catalog of every named framework with cross-references | `<category>/references/<book-slug>/frameworks.md` | User looking up specific framework names |
| **4. Consolidated Summary** | All-encompassing per-text overview tying everything together | `<category>/references/<book-slug>/complete-distillation.md` | User wanting the single-doc view of a book |
| **5. Working Artifacts** | Chunks, screens, parses, digests | `/tmp/scaledown-eval/outputs/<book-slug>/` | Process traceability; usually not opened |

**Why five layers, not one?**

- Skills are loaded into Claude's context at invocation. They must be tight and decision-focused.
- Additional Experts gives the user a "second brain" of advice they can browse.
- Frameworks is a lookup catalog (alphabetical + cross-referenced).
- Consolidated Summary is the single-document view for the user who wants "everything about this book in one place" — including redundancy with existing skills and notable items not yet captured.
- Working artifacts preserve traceability — useful for re-running passes or debugging.

---

## The Pipeline at a Glance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   STAGE 0 — PDF PREP        Convert image-based PDFs to text-extractable     │
│                              (ocrmypdf wrapper)                              │
│                                                                              │
│   STAGE 1 — RECONNAISSANCE  Detect TOC + extract chunks for each section     │
│                              (extract_chapter.py)                            │
│                                                                              │
│   STAGE 2 — SCREEN          ScaleDown /summarize + /extract on every chunk   │
│                              (scaledown_client.py screen)                    │
│                                                                              │
│   STAGE 3 — TRIAGE          Score each chunk on density / transferability /  │
│                              freshness; pick distillables                    │
│                                                                              │
│   STAGE 4 — INDEX (deep)    Full ScaleDown indexing on distillable chunks    │
│                              (scaledown_client.py index)                     │
│                                                                              │
│   STAGE 5 — PARSE           Expert categorizes content into structured JSON  │
│                              (Claude w/ persona skill loaded)                │
│                                                                              │
│   STAGE 6 — PRODUCTIZE      Expert generates skill markdown from PARSE JSON  │
│                              (Claude, same persona)                          │
│                                                                              │
│   STAGE 7 — REFERENCE FILES Pull best practices → additional-experts.md      │
│                              Pull frameworks → frameworks.md                 │
│                              (One pair per book, in shared references/)      │
│                                                                              │
│   STAGE 8 — CONSOLIDATED    Single-document summary of everything            │
│              SUMMARY        (complete-distillation.md per book)              │
│                                                                              │
│   STAGE 9 — SKILL-CREATOR   Validate + finalize skill placement              │
│              (or direct write) (anthropic-skills:skill-creator OR write directly) │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Crucially: ScaleDown is involved at Stages 2, 4, and 7 only. Stages 5, 6, 8 are pure Claude.**

---

## Where ScaleDown Fits (Specific Nodes)

ScaleDown's role: **mechanical pre-processing**. Build a structured map of
each chunk before Claude touches it. ScaleDown is never a substitute for
Claude — it's an input-shaping layer.

### Node 1: Stage 2 — Screening

- **Endpoint:** `/summarization/abstractive` + `/extract`
- **Purpose:** Cheap triage of every chunk — should this be deeply distilled?
- **Why ScaleDown:** Reading 30+ chunks via Claude would take all night. ScaleDown processes them in parallel in minutes.
- **Outputs:** `screen_digest.md` + `screen_entities.json` per chunk

### Node 2: Stage 4 — Deep Indexing

- **Endpoint:** Same as above, with longer max_tokens for digest
- **Purpose:** Build a structured map of the chunk that Claude will use as a navigation aid in PARSE
- **Why ScaleDown:** Claude can read source faster when it has an entity index pointing at the structural elements
- **Outputs:** `digest.md` + `entities.json` per distillable chunk

### Node 3: Stage 7 — (Optional) Cross-chapter synthesis input

- **Endpoint:** `/summarization/abstractive` on a per-chunk digest if needed
- **Purpose:** Compress chunk content for cross-chapter pattern analysis
- **Why ScaleDown:** Cross-chapter synthesis at the chunk level requires too many tokens; ScaleDown digests make it feasible

### Where ScaleDown DOES NOT fit

- **PARSE (Stage 5):** Expert categorization is nuanced. Claude reads the source.
- **PRODUCTIZE (Stage 6):** Skill markdown generation requires synthesis judgment.
- **References (Stage 7 outputs):** Best practices and framework writeups need expert voice. Claude does this.
- **Consolidated Summary (Stage 8):** Cross-cutting integration is a Claude job.

### ScaleDown failure modes encountered

- **`/extract` returning HTTP 200 with body "Internal Server Error"** on certain chunks. Workaround: fall back to `/summarize` only. The digest is rich enough for triage and PARSE navigation.
- **JSON decode errors** in the Python client when ScaleDown returns malformed responses. Defensive code: `except json.JSONDecodeError: log and continue with summarize-only data`.
- **Empty entity arrays** when the chunk has no identifiable named patterns. Acceptable — proceed with empty `entities.json`.

---

## Stage-by-Stage Detail

### Stage 0: PDF Preparation

**Purpose:** Get text-extractable input for the rest of the pipeline.

**Decision tree:**

```
Is the source already plain text or markdown?
├── Yes → skip to Stage 1
└── No → it's a PDF
    │
    Run pypdf extract on a sample page. Does it return text?
    ├── Yes → text-based PDF. Skip OCR. Stage 1.
    └── No / empty → image-based PDF. Run OCR.
```

**OCR command:**
```bash
ocrmypdf --output-type pdf --skip-text --jobs 4 \
  "/path/to/source.pdf" \
  "/tmp/scaledown-eval/books/<slug>_ocr.pdf"
```

**Time expectation:** 5-30 minutes per book depending on size. Run multiple OCRs sequentially (each saturates CPU).

**Verification:** After OCR completes, run pypdf on the OCR'd PDF and confirm text appears.

**Output:** `/tmp/scaledown-eval/books/<slug>_ocr.pdf`

---

### Stage 1: Reconnaissance

**Purpose:** Identify chapter/section boundaries and extract chunks for each.

**Two paths:**

#### Path A — TOC Detection (preferred when reliable)

```bash
python3 scripts/extract_chapter.py /tmp/scaledown-eval/books/<slug>_ocr.pdf --toc
```

This uses regex patterns to detect chapter headings. Inspect the output. If
chapter starts are monotonically increasing and titles look reasonable, use
this path.

#### Path B — Even Page-Range Chunking (fallback)

If TOC detection misfires (e.g., chapter 3 starts on page 15 but chapter 2 starts on page 26 — that's wrong), fall back to even page-range chunks:

```bash
# Example for a 376-page book — 8 sections of ~45 pages each
for range in "10-50" "50-90" "90-130" "130-170" "170-210" "210-250" "250-290" "290-340"; do
  out_name=$(echo $range | tr '-' '_')
  python3 scripts/extract_chapter.py /tmp/scaledown-eval/books/<slug>_ocr.pdf \
    --pages $range \
    --out /tmp/scaledown-eval/outputs/<slug>/sec_${out_name}_chunk.txt
done
```

**Page-range guidance:**
- 30-50 pages per chunk is the sweet spot
- Less than 30 → too many chunks to screen
- More than 50 → ScaleDown more likely to fail or produce diluted output

**Output:** `/tmp/scaledown-eval/outputs/<slug>/sec_<range>_chunk.txt` files

---

### Stage 2: Screen

**Purpose:** Run cheap ScaleDown calls on every chunk for triage.

```bash
source /tmp/scaledown_key.env
python3 scripts/scaledown_client.py screen \
  /tmp/scaledown-eval/outputs/<slug>/sec_<range>_chunk.txt \
  /tmp/scaledown-eval/outputs/<slug>/sec_<range>_screen
```

This produces `screen_digest.md` + `screen_entities.json` per chunk.

**Run all chunks in parallel** via separate Bash calls. ScaleDown handles concurrent requests fine.

**Time expectation:** 5-15 seconds per chunk. With 8 chunks running in parallel, ~30 seconds total wall time.

**Output:** Per-chunk screen directory with digest + entities

---

### Stage 3: Triage

**Purpose:** Score each chunk; decide which to fully distill.

Read the `screen_digest.md` for each chunk. For each, score on three axes (1-5):

| Axis | Question |
|---|---|
| **Density** | How many named frameworks, principles, anti-patterns? |
| **Transferability** | Will these ideas apply across multiple future projects? |
| **Freshness** | Is the content current and durable, or dated? |

**Total score = average. Recommendation:**
- **≥ 4.0** → distill (full pipeline)
- **2.5-3.9** → skim (keep digest only, no skill)
- **< 2.5** → skip

**Important calibration:**
- A 7-section book typically has 3-5 worth distilling. Don't over-produce skills.
- **Distinctiveness check:** If the section overlaps heavily with skills already in the repo (or with sections you've already distilled in this book), defer. Quality over quantity.
- Domain-specific judgement applies. A "career advice" chapter might score high on density but low on transferability.

**Output:** Manifest update with chapter scores + recommendations.

---

### Stage 4: Index (Deep)

**Purpose:** Build a comprehensive entity index for chunks selected for distillation.

```bash
python3 scripts/scaledown_client.py index \
  /tmp/scaledown-eval/outputs/<slug>/sec_<range>_chunk.txt \
  /tmp/scaledown-eval/outputs/<slug>/sec_<range>_index
```

This is similar to Stage 2 but with longer summary max_tokens and higher confidence
threshold. The output (`digest.md` + `entities.json`) becomes the navigation aid
for the expert in Stage 5.

**Output:** Per-chunk index directory.

---

### Stage 5: PARSE (Expert Pass 1)

**Purpose:** Categorize the chunk through a domain expert's lens.

**Inputs:**
- The source chunk (full text)
- The Stage 4 entity index
- The Stage 4 digest
- The PARSE prompt (`references/pass1-parse-prompt.md`)
- A persona skill loaded via Skill tool (cto-architect, ai-product-strategy, etc.)

**Output JSON structure** (top-level keys):
- `main_ideas`
- `frameworks`
- `principles`
- `anti_patterns`
- `decision_rules`
- `mental_models`
- `worked_examples`
- `gotchas`
- `citations`
- `definitions`

Each is an array of structured objects. See `references/pass1-parse-prompt.md`
for the full schema.

**Quality bar:** Don't infer categories. Only include items named or explicit
in the chunk. Empty arrays are fine.

**Output:** `<chapter>_parse.json`

---

### Stage 6: PRODUCTIZE (Expert Pass 2)

**Purpose:** Turn the categorization into a production-ready skill.

**Inputs:**
- The Stage 5 PARSE JSON ONLY (do NOT re-include the source chunk)
- The PRODUCTIZE prompt (`references/pass2-productize-prompt.md`)
- Same persona skill as Stage 5

**Output:** Skill markdown with proper YAML frontmatter, ready for skill-creator OR direct placement.

**Artifact selection rules:**
- Skill: always (mandatory)
- Template / Checklist / Script / Reference doc: conditional, only if warranted by content
- Don't over-produce. A typical chapter yields 1-2 artifacts.

**Output:** `<category>/<skill-name>/SKILL.md` (placed directly OR via skill-creator)

---

### Stage 7: References (One Pair Per Book)

**Purpose:** Build the shared knowledge base for this text.

After all skills for a book are produced, write **two reference files**:

#### `additional-experts.md`

**Voice:** Expert speaking. Best practices + advice + worked examples.

**Sections (canonical structure):**
1. About the Expert(s) — bio, credentials, voice characteristics
2. Foundational mindset shifts the book teaches
3. Best practices organized by topic
4. Specific advice with rationale
5. Worked examples (anchored to source where possible)
6. Anti-patterns deeper than what's in the action-focused skill files
7. Process wisdom (how the expert recommends running things)
8. Career / context wisdom if applicable
9. When to apply these practices (cross-refs to skill files)

**Length:** 400-700 lines typical.

#### `frameworks.md`

**Voice:** Catalog. Definitions and cross-references.

**Sections (canonical structure):**
1. Framework Index (alphabetical table)
2. Framework Catalog (detailed entries)
3. Cross-Reference Map (visual ASCII showing which frameworks combine)
4. How to use this catalog

**Each framework entry:**
- Name + originator
- Structure
- When to apply
- Cross-references to other frameworks
- Caveats

**Length:** 400-700 lines typical.

**Location:** `<category>/references/<book-slug>/`

---

### Stage 8: Consolidated Summary

**Purpose:** The all-encompassing single-document view of this text.

This is the file a user opens when they want **"everything about this book in
one place."** It must be additive over the skill + additional-experts +
frameworks files — not just a regurgitation.

**Sections (canonical structure):**

1. **Source identification** — book, author, edition, when distilled
2. **Executive summary** (1-2 paragraphs) — what this book is and why it matters
3. **The big takeaways** (5-10 high-level insights at the executive level)
4. **Skills derived from this book** — list with cross-refs to skill files + one-line description of when to use each
5. **Frameworks index** — list with cross-ref to `frameworks.md` for detail
6. **Best practices index** — list with cross-ref to `additional-experts.md`
7. **Decision rules consolidated** — every named "if X, do Y" rule across all skills
8. **Anti-patterns consolidated** — every named anti-pattern across all skills
9. **Worked examples consolidated** — pointer to each one
10. **Notable content NOT in skill files** — deeper insights, edge cases, side topics from chapters that scored "skim" or "skip"
11. **Redundant content with existing repo** — mapped: "this book covers X, but `Product/measuring-product-market-fit/` already covers it well — defer to existing skill"
12. **Recommended reading order** for this book's distilled content
13. **When to invoke which skill** — a routing guide

**Length:** 600-900 lines typical.

**Location:** `<category>/references/<book-slug>/complete-distillation.md`

**Why this layer matters:**
- Single-file overview eliminates navigation across 6+ files
- Cross-linking between skills surfaces relationships that aren't obvious from individual skill files
- Identification of redundancy with existing repo helps avoid duplication
- Capture of NOT-yet-captured content prevents knowledge loss
- Reading order / navigation guide makes the book actually usable as a reference

---

### Stage 9: Skill-Creator Integration

**Purpose:** Validate + finalize skill placement.

Two paths:

#### Path A — Use skill-creator (recommended for new contributors)

```
Skill tool → invoke `anthropic-skills:skill-creator` with the draft skill
```

skill-creator validates structure, adds proper YAML frontmatter, places file
in the correct location.

#### Path B — Direct write (when you know the conventions cold)

Use Write tool directly. Verify against an existing skill in the same category
to confirm convention.

**Quality gates either way:**
- YAML frontmatter has `name` and `description`
- Description includes 3-5 example trigger phrases
- Description ends with what the skill produces
- Skill body is in the established structure (When to Use → Frameworks → Principles → Anti-Patterns → Decision Rules → Worked Example → Gotchas → Further Reading)
- File is in the right category folder (Product, Software Development, GTM, etc.)

---

## File Outputs and Routing Table

For a single text, the full output set:

```
PERMANENT (in alex-agents-skills/):
─────────────────────────────────

<category>/<skill-1>/SKILL.md           # New skill from this book
<category>/<skill-2>/SKILL.md           # New skill from this book
<category>/<skill-N>/SKILL.md           # ... typically 2-4 per book

<category>/references/<book-slug>/
├── additional-experts.md               # Best practices + advice
├── frameworks.md                       # Catalog of frameworks
└── complete-distillation.md            # All-encompassing summary

WORKING (in /tmp/scaledown-eval/, ephemeral):
──────────────────────────────────

books/<slug>_ocr.pdf                    # OCR'd PDF (large)

outputs/<slug>/
├── sec_<range>_chunk.txt               # Extracted text per chunk
├── sec_<range>_screen/                 # Screen output per chunk
│   ├── screen_digest.md
│   └── screen_entities.json
├── sec_<range>_index/                  # Deep index per distillable chunk
│   ├── digest.md
│   └── entities.json
├── <chapter>_parse.json                # PARSE output
└── <chapter>_skill_draft.md            # PRODUCTIZE output (before final placement)

manifest.json                           # Master execution log
```

---

## Quality Checkpoints (Human Review Points)

The pipeline is designed to be runnable autonomously, but quality elevates
when human review happens at three points:

### Checkpoint 1: After Triage (Stage 3)

**What to review:** The list of chunks tagged `distill` vs `skim` vs `skip`.

**Why:** Triage scoring is rubric-based but judgement-laden. A human can
override "this scored 4.2 but I know we already have a skill for it" or
"this scored 3.8 but the framework is unique and worth distilling."

### Checkpoint 2: After PARSE (Stage 5)

**What to review:** The structured categorization JSON.

**Why:** This is where false positives and missed items show up. If a framework
got tagged as a principle, fix it before PRODUCTIZE amplifies the error.

### Checkpoint 3: After Final Skill Placement (Stage 9)

**What to review:** The skill in its final location.

**Why:** Skill discovery depends on the YAML description. If the trigger
phrasing isn't right, the skill won't fire when it should. Also: spot-check
that the skill stands alone (doesn't reference "the book" or "chapter X" — it
must be useful even to a Claude instance that hasn't read the source).

### Skipping checkpoints (autonomous mode)

When running autonomously (overnight, batch processing), all three checkpoints
can be skipped. Quality is somewhat reduced. Plan a review pass the next day.

---

## Cost & Time Expectations

### Per-text cost (per book of ~300 pages):

- **OCR (one-time):** Free; CPU time only. 10-30 minutes wall time.
- **ScaleDown screening (Stage 2):** ~8 calls × ~5K chars input each → minor cost.
- **ScaleDown indexing (Stage 4):** ~3-4 calls per distillable chunk → minor cost.
- **Claude PARSE (Stage 5):** ~25K tokens input + ~3K tokens output × ~3-4 chunks = ~100K tokens total.
- **Claude PRODUCTIZE (Stage 6):** ~3K tokens input + ~3K tokens output × ~3-4 chunks = ~25K tokens total.
- **Claude references (Stage 7):** ~3K tokens × 2 files = ~6K tokens (mostly output).
- **Claude consolidated summary (Stage 8):** ~5K tokens output.

**Total per book:** ~150K Claude tokens, modest ScaleDown cost.

### Per-text time:

- **Active human time:** 1-2 hours including reviews.
- **Wall-clock time:** 4-8 hours including OCR (which can run unattended).
- **Autonomous mode:** 1-2 hours wall time, no human attention required.

### Batch processing:

For a stack of N books, total cost scales linearly. The reusable artifacts
(scripts, prompts, schemas) make N=2nd book ~30% faster than N=1st.

---

## How to Add a New Book (Procedure)

1. **Place the source PDF** somewhere accessible (e.g., `~/Desktop/full texts/`).

2. **Decide book metadata:**
   - Title and slug (kebab-case, e.g., `building-ai-powered-products`)
   - Domain (AI product? Software architecture? GTM? etc.)
   - Primary expert skill to use as PARSE/PRODUCTIZE persona
   - Target category folder in alex-agents-skills (`Product/`, `Software Development/`, etc.)

3. **Add to manifest:** Either invoke `book-distiller` skill OR add a new entry to `/tmp/scaledown-eval/manifest.json` manually.

4. **Run Stages 0-3 (PDF prep + screen + triage):**
   - OCR if needed
   - TOC detect (Path A) or page-range chunk (Path B)
   - Screen all chunks
   - Score and pick distillables

5. **Run Stages 4-6 per distillable chunk:**
   - Index (deep)
   - PARSE (with appropriate persona)
   - PRODUCTIZE (with same persona)

6. **Run Stage 7 once for the book:**
   - Write `additional-experts.md`
   - Write `frameworks.md`

7. **Run Stage 8 once for the book:**
   - Write `complete-distillation.md` consolidating everything

8. **Run Stage 9 to finalize:**
   - skill-creator OR direct placement
   - Verify each skill in its final location

9. **Update the manifest** with all artifacts produced.

10. **(Optional) Update STACK_README.md** if any new tools or patterns were added that should be discoverable.

---

## Elevations and Improvements (How to Make This Better)

### Elevation 1: Multi-evaluator panel for high-stakes books

For especially valuable books, run PARSE through 2-3 different persona experts in parallel and merge their categorizations. Disagreements surface places where the book has interpretive ambiguity worth flagging.

### Elevation 2: Cross-book synthesis

After 5+ books are distilled, run a meta-pass: which frameworks recur? Which contradict each other? This is a separate workflow but built on the same artifacts.

### Elevation 3: Continuous re-distillation

Books age. The frameworks they describe become standards or get superseded. Plan annual review of distilled skills. Mark stale or update.

### Elevation 4: Linked reading order

Some books reference each other (the same field, citing each other). Build cross-book reference maps so a user querying about one framework finds related coverage in another book.

### Elevation 5: Skill-eval harness

Run each new skill through the skill-creator's eval harness (if available) to measure trigger discovery rate and quality. Iterate the description until the skill fires reliably for relevant prompts.

### Elevation 6: Domain-tuning the entity schema

The current entity schema is generic (`framework`, `principle`, `anti_pattern`, etc.). For specialized domains (legal, medical, finance) consider domain-specific entity types ("regulation", "case_law", "compliance_requirement"). Override the schema in `references/entity-schema.json` per book if needed.

### Elevation 7: Source-anchored citations

For each distilled skill, optionally anchor major claims back to specific page numbers in the source. Costly to maintain but valuable for legal/compliance contexts.

---

## Failure Modes & Recovery

| Failure | Cause | Recovery |
|---|---|---|
| OCR fails / produces garbage | PDF is corrupted or has weird encoding | Try a different OCR engine (macOS Vision API, cloud OCR) |
| TOC detection misfires | Book uses unusual chapter heading format | Fall back to even page-range chunking |
| ScaleDown `/extract` returns "Internal Server Error" | Server-side bug on certain chunks | Use `/summarize` only; entity index may be empty |
| ScaleDown 429 rate limit | Too many parallel calls | Backoff 60s and retry |
| pypdf returns empty text | PDF needs OCR | Run Stage 0 OCR step |
| Persona skill not found | Wrong skill name in metadata | Check available skills via `/skills` or skill list |
| skill-creator rejects draft | Missing or malformed frontmatter | Re-run PRODUCTIZE with explicit frontmatter requirements |
| Parse JSON malformed | Persona prompt drift | Re-invoke with explicit JSON contract reminder |

---

## Notes on Tooling

The pipeline is bootstrapped by:

- `scripts/ocr_pdf.py` — wrapper for `ocrmypdf`
- `scripts/extract_chapter.py` — TOC detect + page-range chunking via `pypdf`
- `scripts/scaledown_client.py` — HTTP client for ScaleDown endpoints

These live in `book-distiller/scripts/` and are reusable across all texts.

The persona skills (cto-architect, ai-product-strategy, etc.) are pre-existing
skills in alex-agents-skills/. Don't write new persona skills for distillation work — use what's there.

---

## Bottom Line

This workflow is the canonical path. It produces:
- Action-focused skills that fire when relevant
- Browsable expert-voice references
- Catalog-style framework lookup files
- All-encompassing per-book consolidated summaries
- Traceability via working artifacts

Follow it for any new text distillation. Deviations should be deliberate and
documented.
