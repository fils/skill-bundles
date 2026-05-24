# GitHub CLI Agent Skills Management (`gh skill`)

**Source:** https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/  
**Date Added:** 2026-05-24 (Iteration 8)  
**Author:** GitHub Blog  
**Bundle Type:** Supply Chain Security + Cross-Platform Skill Distribution  
**Confidence:** 9/10

## Name & Origin

GitHub introduced the `gh skill` command (CLI v2.90.0+) for discovering, installing, managing, and publishing agent skills across the entire agent ecosystem. Skills follow the open Agent Skills specification (agentskills.io).

## Skills Included

- Skill discovery and search (`gh skill search`)
- Skill installation from GitHub repos (`gh skill install`)
- Skill updates with content-addressed detection (`gh skill update`)
- Skill publishing with spec validation (`gh skill publish`)
- Version pinning for reproducibility (`--pin sha`)
- Agent-specific targeting (`--agent claude-code`, `--agent codex`, etc.)

## Context Elements

- **YAML Configuration:** SKILL.md frontmatter carries provenance metadata (repo, ref, tree SHA)
- **Supply Chain Security:** Immutable releases, content-addressed detection via git tree SHA, version pinning
- **Cross-Platform Compatibility:** Works with GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI, Antigravity
- **Portable Provenance:** Tracking metadata written into SKILL.md frontmatter so "source of truth" stays with the file

## How Context Elements Support Skills

The supply chain integrity features represent a novel context element: **provenance tracking**. By recording the git tree SHA and enabling version pinning, `gh skill` ensures that skills are reproducible and tamper-evident. The content-addressed detection means `gh skill update` checks actual content changes, not just version numbers.

The cross-platform compatibility is significant: the same skill can be installed on any major agent host with the `--agent` flag, demonstrating that the agentskills.io standard enables true portability.

## Composition Notes

`gh skill` is a distribution and governance bundle, not a skill bundle itself. However, it provides the **infrastructure** for skill bundle distribution:
1. Discovery (`gh skill search`)
2. Installation (`gh skill install`)
3. Supply chain integrity (immutability, pinning)
4. Publishing (`gh skill publish --fix` for auto-spec validation)

The security warning is notable: *"Skills are not verified by GitHub and may contain prompt injections or malicious scripts."* This creates a gap — the distribution system exists, but there is no automated verification layer for skill safety.

## Reproducibility

High — official GitHub CLI commands, well-documented, available for all major platforms.

## Key Insight

The `gh skill` ecosystem represents the **maturity phase** of agent skills: when skills become a distribution target with package-manager semantics (install, update, pin, publish), the ecosystem moves from ad-hoc to production-ready.
