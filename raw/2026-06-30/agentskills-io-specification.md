# Agent Skills Specification (agentskills.io)

**Source:** https://agentskills.io/specification (accessed 2026-06-30)
**Standard:** Open specification (originally Anthropic, now cross-platform).

## Key Ideas
- Skill = directory with at minimum `SKILL.md` (YAML frontmatter + Markdown instructions).
- Optional: scripts/, references/, assets/.
- Frontmatter: name (lowercase-hyphen, 1-64 chars), description (1-1024 chars, must describe what + when), license, compatibility, metadata, allowed-tools (experimental).
- Progressive disclosure: metadata first, full instructions on activation, resources on demand.
- Validation via skills-ref library.
- Works across Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, VS Code, etc.

## Composition Notes (Bundle Pattern)
The spec itself defines the **minimal viable skill bundle format**. Real bundles (e.g. addyosmani, anthropics) extend it with personas, references/checklists (vocabularies/taxonomies), scripts, and platform adapters. SKILL.md is the core; context elements live in references/ and scripts/.

## Quotes
> "A skill is a directory containing, at minimum, a `SKILL.md` file."
> "Progressive disclosure... Keep main `SKILL.md` under 500 lines."

**Reproducibility:** High — open spec, reference implementation, validation tools.
**Relevance to Skill Bundles:** Foundational standard that all bundles must follow; many bundles add SHACL/SSSOM/rules on top.