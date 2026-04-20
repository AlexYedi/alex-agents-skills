# How I work

## Roles
I operate as CTO (architecture/strategy) and IC (building).
"Build X" = write production-ready code and deploy it.
"Plan X" = help me think through architecture first.

## Communication
- Lead with the decision, then reasoning
- Flag blockers immediately, don't bury them
- Be direct. If something won't work, say so and propose the alternative
- Short responses for tactical work

## Code standards
- Never put secrets in code files — keys in .env or native UI only
- Write complete files, never partial snippets
- Validate against the actual API contract before writing requests
- Check the real schema before assuming column names

## Workflow
- Check the Linear issue before building
- Update Linear status when Done
- New n8n workflows = new files, never bolt onto existing ones

## Stack I use everywhere
n8n · Supabase · Claude API · Linear · Cursor · Gmail · Google Calendar
Full stack details always live in STACK_README.md at the repo root.
