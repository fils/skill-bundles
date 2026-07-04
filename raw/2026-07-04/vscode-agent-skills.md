# Use Agent Skills in VS Code (GitHub Copilot)

**Source:** https://code.visualstudio.com/docs/agent-customization/agent-skills
**Date ingested:** 2026-07-04
**Type:** Official documentation / integration guide

**Key content:**
- Agent Skills are portable across VS Code, Copilot CLI, Copilot cloud agent.
- Stored in .github/skills/, .claude/skills/, .agents/skills/ (project) or user profile.
- SKILL.md with YAML frontmatter (name, description) + instructions.
- Can include scripts, examples, resources.
- Progressive disclosure and on-demand loading.
- Compared to custom instructions: skills are more structured, portable, and include resources.

**Context elements present:**
- Directory conventions and discovery rules
- SKILL.md schema
- Resource linking syntax
- Multi-agent host compatibility matrix

**Relevance to skill bundles:** Shows how the open standard is implemented in a major IDE/agent host, with explicit support for bundling instructions + scripts + resources.