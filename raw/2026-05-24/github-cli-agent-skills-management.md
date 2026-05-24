# GitHub CLI Agent Skills Management (`gh skill`)

**Source:** https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/
**Date Accessed:** 2026-05-24
**Author:** GitHub Blog

---

## Key Ideas
- GitHub introduced `gh skill` command (v2.90.0+) for discovering, installing, managing, and publishing agent skills
- Skills follow the open Agent Skills specification (agentskills.io)
- Compatible with: GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI
- Supply chain integrity features: immutable releases, content-addressed detection via git tree SHA, portable provenance tracking in SKILL.md frontmatter
- Version pinning: lock skills to specific tags or SHAs

## Bundle Context Elements
- **YAML Configuration:** SKILL.md frontmatter for metadata, provenance, version tracking
- **Supply Chain Security:** Content-addressed detection, version pinning, immutability
- **Cross-Platform:** Works across all major AI coding agents

## Quotes
> "Skills are not verified by GitHub and may contain prompt injections or malicious scripts. Use `gh skill preview` to inspect content before installation."

## Reproducibility
- High: Official GitHub CLI commands, well-documented
- Commands: `gh skill install`, `gh skill update`, `gh skill publish`

## Confidence: 9/10
