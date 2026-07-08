# Agent Skills Specification (agentskills.io/specification)

**Source:** https://agentskills.io/specification
**Date ingested:** 2026-07-08
**Key ideas:** Defines the open standard for Agent Skills: directory with SKILL.md (YAML frontmatter + Markdown instructions), optional scripts/, references/, assets/. Progressive disclosure for efficient loading. Validation via skills-ref. Supports cross-agent portability (Claude, Codex, Copilot, etc.).

**Frontmatter fields:** name (required, lowercase-hyphen), description (required), license, compatibility, metadata, allowed-tools.

**Quotes:**
- "A skill is a directory containing, at minimum, a `SKILL.md` file"
- "Agents load skills through **progressive disclosure**"
- "The Agent Skills format was originally developed by Anthropic, released as an open standard"

**Relevance to skill bundles:** Core spec for packaging skills with context; many bundles will include SKILL.md + SHACL/SSSOM for validation/mapping.
