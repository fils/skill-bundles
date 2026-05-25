# Claude API Agent Skills: Official Integration Guide

## Overview

This entry covers the **official Claude API integration mechanism** for Agent Skills via the `container` parameter. Unlike SDK-level skills, these are skills loaded at request time into an isolated code execution environment — representing a distinct deployment pattern for skill bundles.

**Context Elements:** Beta header schema · Container parameter specification · File ID lifecycle · Version pinning via epoch timestamps · 30MB bundle size limit · 8-skill-per-request constraint

## API Integration Model

### Required Beta Headers
| Header | Purpose |
|--------|---------|
| `code-execution-2025-08-25` | Enables code execution environment |
| `skills-2025-10-02` | Enables the Skills API |
| `files-api-2025-04-14` | Required for file upload/download |

### Container Parameter
```python
container={
    "skills": [
        {"type": "anthropic", "skill_id": "pptx", "version": "20251013"},
        {"type": "custom", "skill_id": "skill_xAbCd...", "version": "latest"}
    ]
}
```

### Lifecycle
1. Claude receives skill metadata in system prompt
2. Copies files to `/skills/{directory}/` in sandboxed container
3. Loads full SKILL.md only when task triggers the skill (progressive disclosure)
4. Container is fresh per request unless `container.id` reused

### Constraints
- Up to 8 skills per request
- Custom skills: SKILL.md at top level, max 30MB total
- No network access within container
- No runtime installs (only pre-installed packages)
- Version pinning: epoch timestamps for production, "latest" for development
- Prompt caching: changing skill list breaks cache

## Context Elements

**Type: API Contract Schema** — The combination of beta headers, container parameter format, and version strings constitutes a formal integration contract.

**Type: Version Pinning Scheme** — Custom skills use epoch timestamps, pre-built skills use date-based versions (`20251013`). Pinning prevents breaking changes.

**Type: Bundle Size Constraint** — 30MB limit enforces lean skill packages with progressive disclosure.

**Type: File ID Lifecycle** — Skills that generate artifacts (documents, images) return `file_id` references that must be downloaded via the Files API — a formal artifact tracking pattern.

## Mid-Session Updates
The API supports **mid-session tool/server updates** without version bumps, enabling dynamic skill loading during long-running operations. Long-running skills may return `pause_turn` stop reason, requiring the client to echo back the response to continue execution.

## Confidence
10/10 — Official Anthropic API documentation, primary source.

## Sources
- https://platform.claude.com/docs/en/build-with-claude/skills-guide
