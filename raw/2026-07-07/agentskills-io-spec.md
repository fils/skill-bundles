# Agent Skills Overview (agentskills.io)

**Source:** https://agentskills.io/home (2026-07-07)

**Key Ideas:**
- Lightweight open format for extending AI agent capabilities.
- Core: folder with SKILL.md (name, description, instructions) + optional scripts/, references/, assets/.
- Progressive disclosure: Discovery → Activation → Execution (minimizes context footprint).
- Supported by many clients: Claude, Codex, Cursor, VS Code, Databricks, Snowflake, etc.
- Originally from Anthropic, now open standard (GitHub: agentskills/agentskills, Discord community).

**Relevance to Skill Bundles:** Canonical definition and ecosystem. Shows how skills are packaged as portable, version-controlled folders that can include formal context (references, templates). Strong example of skill + supporting artifacts without heavy SHACL/SSSOM yet.

**Quotes:**
> "Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand."

**Composition Notes:** Skills are designed for cross-product reuse. Discovery phase allows agents to hold many skills cheaply.