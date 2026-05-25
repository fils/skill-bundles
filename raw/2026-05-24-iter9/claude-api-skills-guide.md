# Claude API Agent Skills - Official Documentation
# Simon Willison: Claude Skills Analysis
# Claude API: Using Agent Skills
# Simon Willison: Skills vs MCP analysis

**URLs:** 
- https://platform.claude.com/docs/en/build-with-claude/skills-guide
- https://simonwillison.net/2025/Oct/16/claude-skills/
**Date Retrieved:** 2026-05-24

## Claude API Skills Guide
- Beta headers: code-execution-2025-08-25, skills-2025-10-02, files-api-2025-04-14
- Container parameter with up to 8 skills per request
- Custom skills: SKILL.md at top level, name (64 chars), description (1024 chars), total <30MB
- No network access, no runtime installs
- Container isolation per request unless container.id reused
- Version pinning via epoch timestamps for production

## Simon Willison Analysis
- Skills potentially bigger deal than MCP due to simplicity and token efficiency
- Skills vs MCP comparison: Low complexity, low tokens, file-based vs protocol-based
- Skills depend on filesystem + code execution environment
- Sandbox critical for safety
- Cross-model compatibility (Codex CLI, Gemini CLI can use via file reading)
- Claude Code is a "general agent" — anything achievable via CLI can be automated through skills
- Cambrian explosion predicted due to low barrier to entry
