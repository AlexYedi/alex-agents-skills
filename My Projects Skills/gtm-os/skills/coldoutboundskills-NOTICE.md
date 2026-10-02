# Third-party skills: growthenginenowoslawski/coldoutboundskills

- **Source:** https://github.com/growthenginenowoslawski/coldoutboundskills @ `a7389091241af01316bed8d370a3ec0e6e60e696` (2026-08-18)
- **Imported:** 2026-10-01, shared at a GrowthEngineX event.
- **License:** MIT (full text below).

## How it was installed
- 46 skills via `npx skills add … -a claude-code --copy` (tracked in `skills-lock.json`).
- 3 copied by hand because their upstream frontmatter doesn't parse (not in `skills-lock.json`; `skills update` won't refresh them):
  - `clay-playbooks`: unquoted `description` containing `: `. Quoted locally. Upstream `skills/playbooks/README.md` copied in as `clay-playbooks/README.md`.
  - `playbook-google-site-search`: same issue, same fix.
  - `zapmail-domain-setup-public`: missing `name`. Added.
- Upstream nests the playbooks under `skills/playbooks/`. Claude Code only discovers skills one level deep, so they are flattened into `.claude/skills/`.

## Deliberately NOT imported
| Upstream item | Why |
|---|---|
| `competitor-engagers` | Scrapes LinkedIn post engagers via RapidAPI. Violates the locked gtm-os ethics rule (no LinkedIn/X scraping). |
| `playbooks/playbook-linkedin-engagement` | Same rule: LinkedIn engager scraping via Apify. |
| `playbooks/playbook-social-posts` | Same rule: LinkedIn post scraping via Apify. |
| `Common Outbound Lists/` (527 MB) | Data, not skills. Includes a 12M-row Google Maps scrape. Too heavy for git; fetch from upstream if ever needed. |

## Local edits (marked `[gtm-os local]` or "not installed in gtm-os")
- `cold-email-starter-kit`: deleted `scripts/enrichments/linkedin-profile.ts` (RapidAPI LinkedIn scraper) and annotated its references.
- `playbook-new-in-role`: source-chain step 3 (Apify Sales Navigator scraper) marked DO NOT USE.
- `cold-email-kickoff`, `clay-playbooks`, `playbook-warm-intros`: references to the excluded skills annotated.
- `perfect-company-list/clay-workflow.md`, `clay-playbooks/README.md`: paths fixed for the flattened layout.

## Upstream license
```
MIT License

Copyright (c) 2026 GrowthEngineX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
