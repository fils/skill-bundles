# agentskills.io Specification (2026-07-09)

**Source:** https://agentskills.io/specification

**Key Ideas:**
- Updated SKILL.md frontmatter: name, description, license, compatibility, metadata, allowed-tools.
- Progressive disclosure: metadata (100 tokens) → full instructions → references/assets on demand.
- Validation via skills-ref library.
- Directory: SKILL.md + scripts/ + references/ + assets/.

**Context Elements:**
- Formal YAML frontmatter + naming rules.
- Optional allowed-tools and compatibility constraints.

**Composition Notes:**
- Core example of skill bundle spec that enables SHACL/SSSOM-style validation layers in future.

**Signal:** 10/10 — canonical reference.