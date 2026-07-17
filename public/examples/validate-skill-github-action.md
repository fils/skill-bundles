---
type: Skill Bundle Example
title: Flash Brew Digital "Validate Skill" — GitHub Action for SKILL.md Spec Compliance
description: A **GitHub Action that validates SKILL.md files against the Agent Skills specification** (https://agentskills.io/specification).
resource: https://github.com/marketplace/actions/validate-skill
timestamp: '2026-06-01T00:00:00Z'
date: '2026-06-01'
---

# Flash Brew Digital "Validate Skill" — GitHub Action for SKILL.md Spec Compliance

**Source:** https://github.com/marketplace/actions/validate-skill
**Source repo:** https://github.com/Flash-Brew-Digital/validate-skill
**Date Added:** 2026-06-01 (Iteration 13)
**Publisher:** Flash Brew Digital | **Author:** Ben Sabic
**License:** MIT | **Version:** v1.0.0
**Tags:** `code-quality` · `ai-assisted` | **Not certified by GitHub** (third-party action)
**Bundle Type:** CI/CD Validation · Spec Compliance · Lightweight Linter
**Confidence:** 9/10

## Name & Origin

A **GitHub Action that validates SKILL.md files against the Agent Skills specification** (https://agentskills.io/specification). It is the **CI/CD complement** to the [skill validator cli](skill-validator-cli.md) CLI — where the Go CLI runs locally with pre-commit hooks, this Action runs in PR pipelines.

## Skills Included (1 Action)

- **`validate-skill`** — Validates `SKILL.md` against the Agent Skills spec. Cross-agent compatible, CLI-compatible (Vercel Skills CLI), CI-friendly JSON outputs.

## Context Elements (Validation Rules)

### Required Fields
- **`name`:** 1–64 chars, lowercase alphanumeric with hyphens, no leading/trailing/consecutive hyphens, **must match directory name**
- **`description`:** 1–1024 chars, non-empty

### Optional Fields (with constraints)
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

## How Context Elements Support Skills

`validate-skill` is the **lightest-weight** validator in the catalog — pure CI/CD integration, no LLM dependency, fast YAML structural checks. It is what you put in `.github/workflows/` to guard a skill repo's PR quality.

The action's design is a **minimal viable validator** — it implements *just* the structural and frontmatter rules from the Agent Skills spec. Heavier checks (content quality, contamination, LLM-as-judge, link rot) live in [skill validator cli](skill-validator-cli.md). Security threat scanning lives in [agentskill sh ags security scoring](agentskill-sh-ags-security-scoring.md). This is a clean **separation of concerns** across the validation stack.

## Composition Notes

### Inputs

| Input | Default | Description |
|---|---|---|
| `path` | `.` | Path to skill directory containing SKILL.md |
| `fail-on-warning` | `false` | Treat warnings as errors |
| `ignore-rules` | `""` | Comma-separated rule IDs to ignore (e.g., `name-match-directory`) |
| `enforce-directories` | `""` | Comma-separated dirs the skill must include (e.g., `scripts`) |
| `validate-references` | `false` | Check that file references in SKILL.md exist |

### Outputs (CI-friendly JSON)

| Output | Description |
|---|---|
| `valid` | Whether SKILL.md is valid (true/false) |
| `errors` | JSON array of validation errors |
| `warnings` | JSON array of validation warnings |

### Example Workflow (Advanced)
```yaml
- name: Validate SKILL.md
  uses: Flash-Brew-Digital/validate-skill@v1
  with:
    path: ./my-skill
    fail-on-warning: "true"
    validate-references: "true"
```

## Reproducibility

**High.** Open source, GitHub Marketplace listing, documented inputs/outputs, example workflows in repo (simple + advanced).

## Bundle Links
- [skill validator cli](skill-validator-cli.md) — Local/pre-commit complement (heavier checks)
- [agentskill sh ags security scoring](agentskill-sh-ags-security-scoring.md) — Registry-level security scanner
- [agent skills spec](agent-skills-spec.md) — The specification being enforced
- [graphguard os guardrails](graphguard-os-guardrails.md) — Policy-as-code precedent
- [owasp agentic skills top 10](owasp-agentic-skills-top-10.md) — Security specification that complements structural validation
