---
name: consulting-tacit-work-elicitation
description: >
  Critical Incident Technique (Flanagan, "The Critical Incident Technique",
  Psychological Bulletin, 51(4), 1954) combined with Contextual Inquiry
  (Beyer & Holtzblatt, *Contextual Design*, Morgan Kaufmann, 1998). Mines
  high-signal edge cases and expert judgment calls through structured
  incident interviews, then observes the everyday tacit flow of the work
  in situ using the master-apprentice model.
  Triggers - "what does the SOP not capture", "critical incident technique",
  "contextual inquiry", "shadow the expert", "what do experts actually do",
  "capture tacit knowledge", "what breaks and how do they fix it",
  "undocumented workarounds", "go watch someone do the work", "master-apprentice
  interview", "what judgment calls are people making", "the process map
  doesn't show the real work", "interview edge cases", "field observation of
  work". Produces a critical-incident log, a contextual-inquiry session guide,
  and a short list of tacit rules and workarounds discovered.
---

# Tacit Work Elicitation (Critical Incident Technique, Flanagan, 1954 + Contextual Inquiry, Beyer & Holtzblatt, 1998)

Critical Incident Technique, from John Flanagan's "The Critical Incident
Technique" (*Psychological Bulletin*, 51(4), 1954), is a set of procedures for
collecting direct observations of human behavior of critical significance to
a defined aim — the moments where expert judgment made the difference between
success and failure. Contextual Inquiry, from Hugh Beyer and Karen Holtzblatt's
*Contextual Design: Defining Customer-Centered Systems* (Morgan Kaufmann,
1998), is a field interview conducted in the person's actual workplace while
they do real work, using a master-apprentice model in which the worker
narrates and you watch and probe.

Neither a SIPOC/VSM nor an event log records what an expert does when the
happy path breaks, or the small workaround nobody wrote down because it
"just makes sense." This skill runs both methods together: CIT mines the
high-signal incidents — what breaks, what an expert does that isn't
documented anywhere — and Contextual Inquiry captures the everyday tacit flow
in situ. Together they surface the invisible work that scoping and process
mining cannot see.

---

## Where this sits in the engagement

This is Step 4 of 14, closing Phase A (Discovery) of the AI/automation
transformation engagement. It takes the bounded process from
`consulting-boundary-setting` (Step 1) — sharpened by the as-is reality from
`consulting-process-recovery` (Step 2) and priced by `consulting-cost-time-baseline`
(Step 3) — and captures the undocumented, tacit, expert work that none of
those three methods can see. It hands the enriched picture of real work
forward to `consulting-task-decomposition` (Step 5), which cannot decompose
work it doesn't know exists.

---

## When to use this skill

- The SIPOC, VSM, and process-mined flow all describe the "happy path," but frontline staff keep saying "well, it depends."
- An expert performer consistently outperforms peers and nobody can say precisely why.
- You suspect a step hides silent workarounds — manual patches around a broken system or policy.
- Event logs (Step 2) show unexplained variance in a step's duration or outcome that timestamps alone can't explain.
- You need raw material — real judgment calls, real exceptions — before decomposing the process into discrete tasks in Step 5.
- Stakeholders describe the process only in the abstract ("the analyst reviews the file") and no one has watched the actual work happen.

---

## The method

### 1. Critical Incident Technique — five steps (Flanagan, 1954)

An **incident** is any observable human activity complete enough to permit
inferences about the person performing it. It is **critical** when it made a
significant positive or negative contribution to the aim of the activity.

1. **Determine the general aim of the activity.** State, in one sentence,
   what the activity is trying to accomplish — the standard against which an
   incident's effectiveness will be judged.
2. **Set plans and specifications.** Decide who will be observed/interviewed
   (which informants), and under what situations incidents will be collected
   (which recurring or exception scenarios qualify).
3. **Collect the incidents.** For each one, capture:
   - what led up to it (the situation),
   - what the person actually did (the observable behavior),
   - the outcome, and
   - why it was effective or ineffective against the stated aim.
4. **Analyze.** Sort the collected incidents into a category framework —
   group by root cause, by step, or by type of judgment call, so patterns
   emerge across informants.
5. **Interpret and report.** Turn the categorized incidents into stated
   tacit rules, judgment heuristics, and recommendations.

CIT is deliberately biased toward the edges — near-misses, exceptions, expert
saves — because those are exactly what a standard operating procedure never
records.

### 2. Contextual Inquiry — the four principles (Beyer & Holtzblatt, 1998)

Contextual Inquiry is a field interview conducted **while the person does
real work**, not a conference-room recall session. It runs on the
**master-apprentice model**: the worker is the master, performing and
narrating their own work; you are the apprentice, watching and asking
questions to understand, not to test.

| Principle | What it means |
|---|---|
| **Context** | Be where the work happens. Watch concrete, ongoing work — not an abstract summary of it given afterward. |
| **Partnership** | Collaborate with the worker; alternate between watching in silence and probing with questions. Neither pure observation nor pure interview. |
| **Interpretation** | Share your interpretation of what you're seeing out loud, in the moment, and let the worker correct it. Facts alone are not enough — you need their meaning. |
| **Focus** | Steer the session with a clear project focus so you don't drown in detail, while staying open enough to notice surprises that break your assumptions. |

A Contextual Inquiry session produces **work models** — flow (who
communicates with whom), sequence (steps and triggers), artifact (documents
and tools used), cultural (values and pressures), and physical (the
workspace layout) — that externalize tacit knowledge and workarounds the
worker may not think to mention unprompted.

### 3. How they combine

Run them in parallel on the same bounded process:

- **Contextual Inquiry** gives you the everyday tacit flow — the constant
  small adjustments, workarounds, and judgment calls a worker makes without
  noticing, surfaced by watching real work and probing in the moment.
- **CIT** gives you the high-signal extremes — the specific moments,
  recalled or observed, where something broke or an expert save made all
  the difference, structured into situation → action → outcome → why.

Neither alone is sufficient: Contextual Inquiry alone can miss rare but
consequential incidents that didn't happen to occur during the observed
session; CIT alone, working from recalled incidents, can miss the ambient
tacit flow the worker no longer notices enough to mention. Together they
produce the raw material — the real, invisible work — that Step 5 needs
before it can decompose the process into tasks.

---

## Workflow (what you do when invoked)

1. **State the activity's aim and pick expert informants.** Write the aim in
   one sentence (per CIT step 1). Identify 3–6 informants who span the
   performance range — including at least one recognized expert and one
   average performer, since the contrast is where tacit rules surface.
2. **Set the contextual-inquiry focus.** Define what you're trying to learn
   in this process (per the Focus principle) and schedule sessions in the
   real workplace, not a meeting room.
3. **Run the contextual-inquiry sessions.** Use the master-apprentice model:
   watch the worker do real work, narrate your interpretation aloud, let
   them correct you, and probe at natural pauses. Capture flow, sequence,
   artifact, cultural, and physical work-model notes as you go.
4. **In parallel, collect critical incidents.** During or immediately after
   each session, ask for specific effective and ineffective incidents:
   "tell me about a time this went really well" and "tell me about a time
   this went wrong." Log situation, lead-up, action, outcome, and
   effectiveness for each.
5. **Categorize the incidents and finalize the work models.** Sort incidents
   into a category framework (by step, by root cause, by judgment type) and
   consolidate the contextual-inquiry work models across informants.
6. **Extract the tacit rules, judgment calls, and workarounds.** For each
   category and each work-model gap, state the underlying rule or heuristic
   explicitly — the thing an expert "just knows."
7. **Hand off the enriched picture of real work.** Package the incident log,
   the session guide, and the tacit-rules list as input to
   `consulting-task-decomposition` (Step 5).

---

## Deliverable & templates

**Critical-incident log**

| Situation | Lead-up | What they did | Outcome | Effective? | Inferred rule |
|---|---|---|---|---|---|
| | | | | Y/N | |
| | | | | Y/N | |
| | | | | Y/N | |

**Contextual-inquiry session guide**

| Field | Content |
|---|---|
| Focus for this session | |
| Informant / role | |
| What to watch for | |
| Probe prompts | "Walk me through what you just did." / "What made you do it that way?" / "What would happen if you skipped that step?" / "Has this ever gone differently — how?" |
| Work models to capture | Flow / Sequence / Artifact / Cultural / Physical |

**Tacit rules and workarounds discovered**

- [Rule/workaround] — [where it applies] — [why it exists / what it compensates for]
- [Rule/workaround] — [where it applies] — [why it exists / what it compensates for]

---

## Pitfalls

- **Interviewing in a conference room instead of at the workspace.** A
  recalled summary of the work is not the work; Contextual Inquiry's first
  principle — Context — is non-negotiable.
- **Only asking about failures.** CIT explicitly wants both effective and
  ineffective incidents; expert saves are as informative as breakdowns.
- **Testing the worker instead of partnering with them.** The Partnership
  principle means alternating watching and probing as a collaborator, not
  quizzing the worker to check their competence.
- **Silently noting disagreements instead of voicing them.** The
  Interpretation principle requires you to say your reading of the situation
  out loud and let the worker correct it — a private inference you never
  check can be wrong and go uncorrected.
- **Collecting incidents without categorizing them.** Step 4 of CIT (analyze)
  is where isolated anecdotes become a pattern; skipping it leaves you with
  a pile of stories instead of a set of tacit rules.
- **Interviewing only top performers.** Contrasting expert and average
  informants is what makes the gap — and therefore the tacit rule — visible;
  a sample of only experts hides what's actually different about their work.

---

## Related

- **In-suite** — `consulting-boundary-setting` (Step 1): supplies the bounded
  process and its steps that this skill investigates for tacit content.
  `consulting-process-recovery` (Step 2) and `consulting-cost-time-baseline`
  (Step 3): their variance and cost/time data often point to exactly which
  steps need incident collection and field observation.
  `consulting-task-decomposition` (Step 5): consumes the incident log, work
  models, and tacit-rules list to decompose the enriched picture of real work
  into routine/non-routine, manual/cognitive tasks.
- **Elsewhere in the library** — `conducting-user-interviews`,
  `jtbd-fundamentals-and-interviewing`, `voice-of-customer`.
- **References** — Flanagan, "The Critical Incident Technique,"
  *Psychological Bulletin*, 51(4), 1954. Beyer & Holtzblatt, *Contextual
  Design: Defining Customer-Centered Systems* (Morgan Kaufmann, 1998).
