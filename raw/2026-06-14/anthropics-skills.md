# anthropics/skills

**Source:** https://github.com/anthropics/skills (retrieved 2026-06-14)
**Type:** Official/public repository for Agent Skills (Anthropic reference implementation)
**Key Context Elements:** Agent Skills specification (spec/), SKILL.md template with YAML frontmatter (name, description), example skills in categories (Document Skills, etc.), plugin config

## Key Ideas
- Skills are folders of instructions, scripts, and resources that Claude loads dynamically.
- Official spec at agentskills.io referenced.
- Template requires YAML frontmatter + instructions, examples, guidelines.
- Includes document creation/editing skills (docx, pdf, pptx, xlsx) and many Apache 2.0 examples.
- Marketplace installation via /plugin marketplace add anthropics/skills

## Notable Quotes / Patterns
> "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."

**Composition Notes:** Emphasizes the open Agent Skills specification; skills often bundled with partner skills (e.g. Notion). Strong reference for the core skill packaging standard.

**Reproducibility:** High — public repo, clear template, spec link.