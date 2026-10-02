# Clay workflow build: Warm Intros

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification, and the weakest-evidenced build in the library.** Sources probed, **no
line graded.** Your first run is the verdict.

Build **member 2 (current-customer alumni)** and nothing else until it works.

## Graph

```
[1 trigger: source companies + client domain]
   -> [2 code: CONFIG CHECK -- refuse if the client is in the source set]
   -> [3 tool: people search, past-company filter]
   -> [4 code: alumni filter + exclusions]
   -> [5 code: build the line + contract]
```

**No agent node.** The line is short and its risk is entirely in *what gets named*, so a formula is
both cheaper and safer than a model here. That is unusual for this library and it is deliberate.

## Node 2 — refuse a bad source set

```python
def run(source_domains, client_domain):
    srcs = {d.lower() for d in (source_domains or [])}
    if not srcs:
        raise ValueError("no source companies; this playbook has nothing to match on")
    # If the CLIENT's own domain is in the source set, the list is wrong. Filtering
    # around it hides a configuration error that will produce a list of the client's
    # own employees.
    if (client_domain or "").lower() in srcs:
        raise ValueError("client domain is in the source set; fix the source list")
    return {"source_domains": sorted(srcs)}
```

## Node 3 — the people search

A people search with a **past-company filter** set to the client's customer or case-study companies,
with past experiences included.

What the probe confirmed on 20 rows: a **dated** matched past experience, a profile URL, a city, and
**15 of 20 had moved on.**

⚠️ **Widen the definition, or the list is unusable.** Defining a warm intro as "overlapped in time
with someone on the client's team" produces a list too small to campaign on — it never once got run.
"Ever worked there, and has since moved on" produces a real segment from the same query.

## Node 4 — alumni filter and exclusions

```python
def run(people, source_domains, client_domain):
    srcs = {d.lower() for d in (source_domains or [])}
    kept, still_there = [], 0

    for p in (people or []):
        cur  = (p.get("current_employer_domain") or "").lower()
        mail = (p.get("email") or "").split("@")[-1].lower()

        # Someone STILL at the client's customer is not a warm intro -- they ARE
        # the customer. The probe found ~1 in 4 in this state.
        if cur in srcs or mail in srcs:
            still_there += 1
            continue

        # Find the matched past experience and keep it as evidence.
        match = next((e for e in (p.get("past_experiences") or [])
                      if (e.get("company_domain") or "").lower() in srcs), None)
        if not match:
            continue

        kept.append({
            "name":            p.get("full_name", ""),
            "linkedin_url":    p.get("linkedin_url", ""),
            "current_company": p.get("current_employer", ""),
            "current_domain":  cur,
            "past_company":    match.get("company", ""),
            "past_title":      match.get("title", ""),
            # Dates are kept for QA ONLY. They never reach copy: profile ranges are
            # imprecise, and "in 2018 you were at X" is both creepy and often wrong.
            "past_dates":      match.get("dates", ""),
        })

    return {"people": kept, "still_at_source": still_there, "member": "current_customer_alumni"}
```

## Node 5 — the line and the contract

```python
def run(person, member, allow_naming=False):
    emp = (person or {}).get("past_company", "").strip()
    if not emp:
        return {"warm_intro_line": "", "warm_intro_member": member, "warm_intro_evidence": ""}

    # DEFAULT: the UNNAMED form. It says the relationship without disclosing which
    # of the client's customers this is. Naming a client's customer in cold email
    # is the CLIENT's decision, not ours, and getting it wrong turns a clever
    # campaign into an awkward phone call.
    line = "you came up through %s, who we work with now" % emp
    if allow_naming:
        line = "you came up through %s, one of our customers" % emp

    return {
        "warm_intro_line":     line,
        # Seven members share one copy shape. Without the member name you cannot
        # tell which angle produced replies, which is the only way this family
        # gets narrowed to the two or three members worth keeping.
        "warm_intro_member":   member,
        # QA only. Contains employment dates. NEVER pushed to a sequencer.
        "warm_intro_evidence": "%s, %s, %s" % (emp, person.get("past_title", ""),
                                               person.get("past_dates", "")),
    }
```

⚠️ **`allow_naming` defaults to False and should be set per client, recorded, never global.**

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: warm intros (customer alumni)" | jq -r '.id')
# create the 5 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "warm-intro-alumni" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{
  "source_domains": ["customer-one.com","customer-two.com"],
  "client_domain": "our-client.com"
}]}'
```

## After the run, before anything ships

**Push the source companies onto the client's do-not-contact list.** Node 4's exclusions fix **this
run**; the block list is what stops the same people arriving through another lane next quarter.

Then **read 10 rendered lines out loud.** This playbook has no graded verdict — your first run is the
verdict, and the file owes a real fill rate and a graded sample afterwards.

## Smoke test

| What you see | What it means |
|---|---|
| Node 2 raises | the client's domain is in the source set. **Fix the source list, do not filter around it** |
| `still_at_source` is 0 | the search returned current employees only, or the past-experience flag is off |
| Almost everyone is still at the source | you searched current company, not past |
| The list is tiny | you defined the member as a time overlap. Widen it |
| Lines name a customer | `allow_naming` is on without approval |
| Lines contain dates | dates leaked from evidence into the line |
| Replies cannot be attributed | the member field is missing |
