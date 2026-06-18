# anthropics/skills — Official Anthropic Agent Skills Repository

**Source:** https://github.com/anthropics/skills (extracted 2026-06-18)
**Date ingested:** 2026-06-18
**Signal:** High — official reference implementation + template + document skills

## Key Ideas
- Public repo demonstrating Agent Skills for Claude (and compatible agents).
- Contains `skills/` with examples (Creative & Design, Development & Technical, Enterprise & Communication, Document Skills).
- Includes document creation/editing skills (docx, pdf, pptx, xlsx) that are source-available.
- `spec/` and `template/` for creating custom skills.
- Usage: `/plugin marketplace add anthropics/skills` then install specific skills.

## Structure
- SKILL.md files with YAML frontmatter (name, description) + instructions.
- Demonstrates bundling of instructions + resources.

## Relevance to Skill Bundles
Shows official packaging of skills with practical context (document tools). Context elements are implicit in the skill definitions rather than formal SHACL/SSSOM.

## Quotes
"Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."