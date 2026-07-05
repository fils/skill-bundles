# Use Agent Skills in VS Code

**Source:** https://code.visualstudio.com/docs/agent-customization/agent-skills (2026-07-02)
**Type:** Microsoft documentation for Agent Skills in GitHub Copilot / VS Code

## Key Points
- Agent Skills is an open standard compatible with GitHub Copilot in VS Code, CLI, and cloud agent.
- Skills stored in .github/skills/, .claude/skills/, .agents/skills/ (project) or user profile locations.
- Skill types: Project skills (repo-specific) vs Personal skills.
- Progressive disclosure and automatic loading based on relevance.

## Context Elements
- Integrates with repo instructions (.github/copilot-instructions.md) for always-on context.
- Skills provide modular, on-demand capabilities.
- Custom Agents can orchestrate multiple skills.

## Composition Notes
- Demonstrates bundling skills with repo-wide instructions and custom agents.
- Supports composition: repo instructions + skills + custom agent persona.

**Relevance:** Shows integration layer for skill bundles in popular IDE/agent environments. Highlights how skills + instructions form larger bundles.