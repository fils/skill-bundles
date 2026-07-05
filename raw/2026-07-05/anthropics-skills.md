# anthropics/skills

**Source:** https://github.com/anthropics/skills (public repo for Agent Skills, updated recently 2026-07-05)
**Type:** Official Anthropic demonstration of Agent Skills

## Key Points
- Demonstrates what's possible with Claude's skills system.
- Range from creative (art, music, design) to technical applications.
- Contains spec/ and template/ directories.
- Skills are folders with instructions, scripts, resources that Claude loads dynamically.

## Context Elements
- Uses the Agent Skills format (SKILL.md + supporting files).
- References the open specification at agentskills.io.
- No explicit SHACL or SSSOM mentioned, but serves as reference implementation for how skills bundle resources.

## Composition Notes
- Shows creative + technical skill variety.
- Emphasizes dynamic loading for specialized tasks.

**Relevance to Skill Bundles:** Foundational reference implementation. Many downstream bundles (NVIDIA, addyosmani, community) build on this pattern.