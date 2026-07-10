---
date: 2026-07-10
sources:
  - raw/2026-07-10/vercel-labs-agent-skills.md
  - https://github.com/vercel-labs/agent-skills
skills_included: 5+
context_elements:
  - constraint-rules
  - progressive-disclosure
  - remote-handbook-fetch
  - platform-vendor-implementation
  - skills-sh-distribution
composition_notes: Vendor constraint-rule bundles encoding engineering handbooks as portable skills.
reproducibility: High — public MIT monorepo, agentskills.io format, skills.sh listing
---

# Vercel Labs Agent Skills

**Origin:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (~28.9k stars)

## Skills included

- `vercel-optimize` — cost/performance/reliability audit of Vercel projects
- `react-best-practices` — 40+ rules, 8 impact-ranked categories
- `web-design-guidelines` — 100+ UI/a11y/UX rules
- `writing-guidelines` — 80+ writing handbook rules (remote-fetch source repo)
- `react-native-guidelines`

## Context elements

- **Constraint rules as skill body** — large rule catalogs (see [[constraint-rules-as-context]])
- **Progressive disclosure** — thin SKILL.md + on-demand references / remote handbook
- **Vendor platform implementation** — official Vercel skills
- **Distribution** — skills.sh registry badge; `AGENTS.md` + CLAUDE.md symlink for universal agents

## How context supports skills

Rules are the primary context artifact: skills activate dense, versioned engineering policy rather than free-form advice. Remote-fetch handbooks keep constraints current without bloating skill install size.

## Composition notes / reusability

- Pattern peers: [[addyosmani-engineering-skills]], [[superpowers-engineering-discipline-skills]]
- Official vendor pattern peers: [[anthropic-official-skills]], [[nvidia-verified-skills]] / NVIDIA skills repo

## Reproducibility assessment

**High.** MIT, agentskills.io structure, public monorepo.

## Related

- [[constraint-rules-as-context]]
- [[addyosmani-engineering-skills]]
- [[vscode-copilot-skills]]

[[backlinks]]
