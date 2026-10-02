"""Decide what an Audiences write may contain, and which writer has to carry it.

The failure this module exists to prevent is the quiet one. A value the field's declared type
cannot parse is **accepted**: the write returns success, the value is counted as updated, and
it reads back verbatim on the record — and it matches no filter, ever. Three of the four
places you would look agree the value is there. Only a filter disagrees, and by then the
audience has been built on it.

So every value is checked against its field's declared type BEFORE the write, and anything
that fails is dropped with a named reason rather than sent and hoped for.
"""

import re

# ------------------------------------------------------------------ the field plan

# Adopted by DISPLAY NAME, never created blindly: creating a field whose name is already in
# use silently appends a suffix, so an unconditional create makes a second column every run
# and splits the data across both.
#
# Types are chosen for what has to be FILTERABLE afterwards, which is why `score` is the only
# number here and why nothing is a boolean: a boolean cannot be coverage-checked — `= false`
# also returns every record the field was never set on, so no query separates "explicitly
# false" from "never touched".

PEOPLE_FIELDS = [
    ("Conference", "text", "conference_name"),
    ("Conference start", "date", "conference_start"),
    ("Conference location", "text", "conference_location"),
    ("Conference campaign id", "text", "campaign_id"),
    ("Attendee record id", "text", "lanyard_contact_id"),
    ("Attendee tier", "text", "tier"),
    ("Attendee score", "number", "score"),
    ("Attendee rank", "number", "rank"),
    ("Attendance confidence", "text", "attendance_confidence"),
    ("Attendance evidence", "text", "attendance_evidence"),
    ("Attendance source", "text", "attendance_source"),
    # Which edition the evidence is about. Load-bearing once a list can be seeded: seeding
    # LAST year's attendee list is legitimate evidence that somebody may come again, and is
    # not evidence that they are coming. This column is where that difference lives, so a
    # segment can require this year rather than assuming it.
    ("Attendance year", "text", "attendance_year"),
    ("Dossier state", "text", "dossier_state"),
    ("Dossier headline", "text", "headline"),
    ("Dossier summary", "text", "dossier_summary"),
    ("Their company", "text", "company_summary"),
    ("Why they score", "text", "score_rationale"),
    ("Buying signals", "text", "buying_signals"),
    ("Conversation openers", "text", "openers"),
    ("Value prop", "text", "value_prop"),
    ("Dossier written at", "date", "written_at"),
]

# TIER COMES FROM THE OTHER RESPONSE FORMAT, not from the dossier. Measured: no contact in
# the rich format carries a tier under any key, so a client reading only that format writes a
# permanently empty tier column. The flat projection has it for every contact, and a second
# read costs nothing — neither this API nor Audiences moved a credit meter — so both are read
# and merged on identity. Tier is worth the round trip: "who are the S-tiers" is the first
# question anybody asks of a conference list.

COMPANY_FIELDS = [
    ("Conference", "text", "conference_name"),
    ("Conference campaign id", "text", "campaign_id"),
    ("Attending this conference", "text", "attending_flag"),
    ("Dossier written at", "date", "written_at"),
]

# Built-in fields written alongside the adopted ones. These already exist on every workspace.
PEOPLE_BUILTINS = ["name", "first_name", "last_name", "title", "email", "linkedin_url", "phone"]
COMPANY_BUILTINS = ["org_name", "domain"]

# Upsert match keys are fixed by the platform and cannot be extended — a custom field is
# never a match key. Each selected lookup field is REQUIRED and rejects an empty string, so
# a writer exists per key rather than one writer choosing at run time. The key a given
# attendee is matched on comes from `route_match_key` below; the company is always matched
# on its domain, because a company with neither a domain nor a LinkedIn URL cannot be
# upserted at all and its people are written unlinked instead.
ACCOUNT_MATCH_KEY = "domain"


# --------------------------------------------------------------------- validation

_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}([T ].*)?$")
_NUMERIC = re.compile(r"^-?\d+(\.\d+)?$")


def validate_value(value, data_type):
    """Return (ok, coerced, reason). `reason` is set only when ok is False.

    A False here means the value is dropped from the write, not that the write fails: a
    contact with an unparseable score is still worth having, minus the score.
    """
    if value is None or value == "":
        return False, None, "empty"

    if data_type in ("text", "string"):
        return True, str(value), None

    if data_type == "number":
        if isinstance(value, bool):
            return False, None, "boolean_into_number"
        if isinstance(value, (int, float)):
            return True, value, None
        cleaned = str(value).strip().replace(",", "")
        cleaned = cleaned.lstrip("$£€")
        if _NUMERIC.match(cleaned):
            return True, float(cleaned) if "." in cleaned else int(cleaned), None
        # This is the exact shape that gets silently accepted and then filters as empty.
        return False, None, "not_a_number"

    if data_type == "date":
        v = str(value).strip()
        if _ISO_DATE.match(v):
            return True, v, None
        return False, None, "not_an_iso_date"

    if data_type == "email":
        v = str(value).strip().lower()
        if v.count("@") == 1 and "." in v.split("@")[1] and " " not in v:
            return True, v, None
        return False, None, "not_an_email"

    if data_type == "url":
        v = str(value).strip()
        if "://" in v and " " not in v and "." in v:
            return True, v, None
        if "." in v and " " not in v and v:
            return True, "https://" + v.lstrip("/"), None
        return False, None, "not_a_url"

    if data_type == "boolean":
        # Deliberately unreachable from the field plan. Kept so an added boolean field fails
        # loudly here instead of producing a column nobody can measure coverage on.
        return False, None, "boolean_fields_cannot_be_coverage_checked"

    return True, str(value), None


# ------------------------------------------------------------------------ routing

# A blank association writes NO RECORD AT ALL — not an unlinked one — so "has a company" and
# "has no company" are different writers rather than one writer with an optional field.
# Combined with one writer per match key, that is four contact lanes, and they are decided
# here rather than in the graph.

ROUTE_LINKED_EMAIL = "linked_email"
ROUTE_LINKED_LINKEDIN = "linked_linkedin"
ROUTE_UNLINKED_EMAIL = "unlinked_email"
ROUTE_UNLINKED_LINKEDIN = "unlinked_linkedin"
ROUTE_UNWRITABLE = "unwritable"


def route_for(shaped, link_company=True):
    """Pick the writer lane for one contact. Returns (route, reason).

    LinkedIn is preferred over email as the match key: for a conference attendee it is the
    more stable identity, and two people at one company can share an inbox alias while never
    sharing a profile.
    """
    has_linkedin = bool(shaped.get("linkedin_url"))
    has_email = bool(shaped.get("email"))
    linked = bool(link_company and shaped.get("company_domain"))

    if not has_linkedin and not has_email:
        return ROUTE_UNWRITABLE, "no valid match key: neither a LinkedIn URL nor an email"

    if has_linkedin:
        return (ROUTE_LINKED_LINKEDIN if linked else ROUTE_UNLINKED_LINKEDIN), "matched on LinkedIn URL"
    return (ROUTE_LINKED_EMAIL if linked else ROUTE_UNLINKED_EMAIL), "matched on email"


def route_is_linked(route):
    return route in (ROUTE_LINKED_EMAIL, ROUTE_LINKED_LINKEDIN)


def route_match_key(route):
    return "email" if route in (ROUTE_LINKED_EMAIL, ROUTE_UNLINKED_EMAIL) else "linkedin_url"


def plan_writes(shaped_contacts, link_company=True):
    """Group a run's contacts by lane, and separate out the ones nothing can write.

    Returns (by_route, unwritable) so the plan shown before any write states both.
    """
    by_route, unwritable = {}, []
    for s in shaped_contacts:
        route, reason = route_for(s, link_company=link_company)
        if route == ROUTE_UNWRITABLE:
            unwritable.append((s, reason))
        else:
            by_route.setdefault(route, []).append(s)
    return by_route, unwritable
