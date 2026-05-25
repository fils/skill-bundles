# Anthropic Official Skills Repository

## Overview

The official [anthropics/skills](https://github.com/anthropics/skills) repository (~140k stars) is the **canonical reference implementation** for agent skills. It contains the full spec, minimal templates, working example skills, and the **source-available code** for Claude's native document generation capabilities (PDF, DOCX, PPTX, XLSX). This repository is the **primary skill bundle** — it packages the entire skill mechanism as a distributable set of skills, templates, and specifications.

**Context Elements:** Agent Skills specification (`/spec`) · Minimal skill template (`/template`) · Apache 2.0 licensing (most skills) · Source-available document skills · Beta API integration documentation

## Repository Structure

### `/spec`
The **Agent Skills specification** — defines the SKILL.md format, YAML frontmatter schema, directory layout, and progressive disclosure semantics. Published as an open standard at [agentskills.io](https://agentskills.io).

### `/template`
A minimal starting point for new skill creation — demonstrates the required structure (SKILL.md with frontmatter + optional supporting files).

### `/skills`
Example and production skills organized by domain:
- **Creative/Design:** Art, music, and design applications
- **Technical:** Web app testing, MCP server generation
- **Enterprise:** Communications, branding, workflow automation
- **Document Capabilities:** `docx`, `pdf`, `pptx`, `xlsx` (source-available) — these power Claude's native document features

### Claude API Integration
- Beta headers: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`
- Container parameter with up to 8 skills per request
- Custom skills: SKILL.md at top level, max 30MB total
- Environment constraints: no network, no runtime installs, isolated per request
- Mid-session tool/server updates without version bumps

### Plugin Marketplace
```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## Context Elements

**Type: Specification (Open Standard)** — The `/spec` directory defines the formal schema for SKILL.md (name: 64 chars, description: 1024 chars, YAML frontmatter requirements).

**Type: Template** — The `/template` directory provides a reference implementation that demonstrates correct structure.

**Type: Licensing Taxonomy** — Apache 2.0 for most skills, source-available for document capabilities. This dual licensing is a context element that affects distribution and modification rights.

**Type: API Integration Spec** — Beta headers, container parameter schema, and versioning strategy constitute the formal integration contract between skills and the Claude API.

## Composition Notes
This repository is the **meta-bundle of the entire ecosystem** — it contains the spec, examples, templates, and working production skills. The document skills (`pdf`, `docx`, `pptx`, `xlsx`) demonstrate how to combine:
- SKILL.md instructions
- Bundled scripts with validation logic
- File system operations within isolated containers
- File ID generation and retrieval via Files API

## Confidence
10/10 — Official Anthropic repository, primary source.

## Sources
- https://github.com/anthropics/skills
- https://platform.claude.com/docs/en/build-with-claude/skills-guide
