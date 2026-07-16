---
type: Skill Bundle Example
title: VS Code Copilot Agent Skills — Cross-Platform Standard
description: VS Code Copilot Agent Skills — Microsoft's implementation of the agentskills.io open standard for GitHub Copilot in VS Code, Copilot CLI, and Copilot cloud agent.
resource: https://code.visualstudio.com/docs/copilot/customization/agent-skills
timestamp: '2026-05-23T00:00:00Z'
date: '2026-05-23'
---

# VS Code Copilot Agent Skills — Cross-Platform Standard

**Date:** 2026-05-23
**Source:** https://code.visualstudio.com/docs/copilot/customization/agent-skills
**Confidence:** 5/5 (Official Microsoft documentation)

## Name & Origin
VS Code Copilot Agent Skills — Microsoft's implementation of the agentskills.io open standard for GitHub Copilot in VS Code, Copilot CLI, and Copilot cloud agent.

## Skills Included
Agent Skills implemented as portable folders with:
- Mandatory SKILL.md with YAML frontmatter
- Optional scripts, resources, and linked files
- Extension contribution via package.json
- Forked context mode for subagent execution

## Context Elements
- **YAML frontmatter schema**: Strict field types including name (must match directory), description (max 1024 chars), argument-hint, user-invocable, disable-model-invocation, and context mode
- **Multi-storage locations**: Project-level (.github/skills/, .claude/skills/, .agents/skills/) and user-level (~/.copilot/skills/, ~/.claude/skills/, ~/.agents/skills/) with scope resolution
- **Progressive loading**: Three-tier disclosure (Discovery → Instructions → Resource Access)
- **Extension contribution**: Declarative skill bundling via VS Code extension package.json
- **Linked file resolution**: Markdown relative paths control which files the agent can see

## How Context Elements Support Skills
The frontmatter schema provides declarative control over skill behavior (invocation policy, context isolation). The progressive loading pattern manages context budgets. Extension contribution enables skill distribution as part of VS Code extensions.

## Composition Notes
This demonstrates skill portability across agents (Claude Code, Codex, Cursor) through the open standard. The forked context mode represents an emerging pattern for resource isolation within skill bundles.

## Reproducibility
High — official VS Code documentation with clear creation methods (manual, AI-generated, conversation extraction).
