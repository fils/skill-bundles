# Flash Brew Digital "Validate Skill" — GitHub Action for SKILL.md Spec Compliance

**Extracted:** 2026-06-01
**Source:** https://github.com/marketplace/actions/validate-skill
**Source repo:** https://github.com/Flash-Brew-Digital/validate-skill
**Publisher:** Flash Brew Digital | **Author:** Ben Sabic
**License:** MIT | **Version:** v1.0.0
**Tags:** `code-quality` · `ai-assisted` | **Not certified by GitHub** (third-party action)

## What It Is

A **GitHub Action that validates SKILL.md files against the Agent Skills specification** (https://agentskills.io/specification). It is the CI/CD complement to the `agent-ecosystem/skill-validator` CLI — where the Go CLI runs locally with pre-commit hooks, this Action runs in PR pipelines.

## Why Use It

- **Cross-agent compatibility** — Ensure skill works across all coding agents that support the Agent Skills spec
- **CLI compatibility** — Valid skills install correctly with tools like the Vercel Skills CLI
- **Catch errors early** — Validate skills in CI before they reach production
- **Spec compliance** — Ensure SKILL.md follows the official specification
- **Configurable** — Ignore rules, enforce directory structures, strict mode
- **Reference checking** — Verify that file references in skill actually exist
- **CI-friendly outputs** — JSON arrays for errors and warnings for programmatic use

## Inputs

| Input | Default | Description |
|---|---|---|
| `path` | `.` | Path to skill directory containing SKILL.md |
| `fail-on-warning` | `false` | Treat warnings as errors |
| `ignore-rules` | `""` | Comma-separated rule IDs to ignore (e.g., `name-match-directory`) |
| `enforce-directories` | `""` | Comma-separated dirs the skill must include (e.g., `scripts`) |
| `validate-references` | `false` | Check that file references in SKILL.md exist |

## Outputs

| Output | Description |
|---|---|
| `valid` | Whether SKILL.md is valid (true/false) |
| `errors` | JSON array of validation errors |
| `warnings` | JSON array of validation warnings |

## Validation Rules

### Required
- **`name`:** 1–64 chars, lowercase alphanumeric with hyphens, no leading/trailing/consecutive hyphens, **must match directory name**
- **`description`:** 1–1024 chars, non-empty

### Optional (with constraints)
- **`license`:** Must be string
- **`compatibility`:** 1–500 chars
- **`metadata`:** Key-value mapping with string values
- **`allowed-tools`:** Space-delimited string

### Structure
- YAML frontmatter must be present between `---` markers
- Frontmatter must be valid YAML

### Warnings
- Very short descriptions (< 50 chars)
- Empty body content
- Body exceeding 500 lines
- Unknown frontmatter fields

## Why It Matters for the Catalog

`validate-skill` is the **lightest-weight** validator in the catalog — pure CI/CD integration, no LLM dependency, fast YAML structural checks. It is what you put in a `.github/workflows/` to guard a skill repo's PR quality.

**Cross-reference:**
- `agent-ecosystem/skill-validator` (Go CLI) — local dev + pre-commit; this action is the CI gate
- `agentskill-sh/ags` (CLI + marketplace) — registry-level security scoring; this action is per-skill structural validation
- `owasp-agentic-skills-top-10` (catalog) — defines *what* a vulnerable skill is; this action catches *structural* problems only

## Bundle Density

Lower than the CLI/marketplace options, but more accessible:
- Single GitHub Action (1 YAML + Action code)
- Inputs/outputs: 5/3
- Validation rules: 4 required-field + 4 structural + 4 warnings
- Distribution: GitHub Marketplace
- Companion CLI: Vercel Skills CLI (`skills.sh`) — valid skills install correctly

## Reproducibility Assessment

**High.** Open source, GitHub Marketplace listing, documented inputs/outputs, example workflows in repo (simple + advanced).
