---
type: Skill Bundle Example
title: agent-ecosystem/skill-validator — CLI Validator + LLM-as-Judge
description: A **CLI tool that validates and scores Agent Skill packages** (per the agentskills.io SKILL.md spec) — going well beyond spec compliance to check link rot, token cost, content quality, cross-language contamination, an...
resource: https://github.com/agent-ecosystem/skill-validator
timestamp: '2026-06-01T00:00:00Z'
date: '2026-06-01'
---

# agent-ecosystem/skill-validator — CLI Validator + LLM-as-Judge

**Source:** https://github.com/agent-ecosystem/skill-validator
**Date Added:** 2026-06-01 (Iteration 13)
**License:** MIT | **Language:** Go 100% | **Stars:** 151 | **Forks:** 25
**Latest Release:** v1.5.6 (Apr 28, 2026)
**Bundle Type:** Validation Tooling · LLM-as-Judge · Multi-Platform Pre-commit
**Confidence:** 10/10

## Name & Origin

A **CLI tool that validates and scores Agent Skill packages** (per the agentskills.io SKILL.md spec) — going well beyond spec compliance to check link rot, token cost, content quality, cross-language contamination, and LLM-as-judge quality scoring.

> "Spec compliance is table stakes. `skill-validator` goes further: it checks that links actually resolve, flags files that shouldn't be in a skill directory, reports token counts so you can see how much of an agent's context window your skill will consume, analyzes content quality metrics, detects cross-language contamination, and offers LLM-as-judge scoring to evaluate skill quality across dimensions like clarity, actionability, and novelty. A spec-compliant skill that has broken links or a 60k-token reference file will technically pass the spec but perform poorly in practice."

## Skills Included (1 tool, 7 commands)

| Stage | Command | What It Answers |
|---|---|---|
| Scaffolding | `validate structure` | Does it conform to the spec and can agents use it? |
| Writing content | `analyze content` | Is the instruction quality good? |
| Adding examples | `analyze contamination` | Am I introducing cross-language contamination? |
| Review | `validate links` | Do external links still resolve? |
| Quality scoring | `score evaluate` | How does an LLM judge rate this skill? |
| Comparing models | `score report` | How do scores compare across different LLM providers? |
| Pre-publish | `check` | Run everything (except LLM scoring) |

## Context Elements

- **Validation rules:** Spec-compliance + custom allow/deny rules (`--allow-extra-frontmatter`, `--allow-flat-layouts`, `--allow-dirs=evals,testing`)
- **Content quality metrics:** word count, code block count/ratio, code languages, sentence count, imperative count/ratio, strong/weak language markers, information density, instruction specificity, section count, list item count
- **Contamination detection:** Multi-interface tools (0.3 weight), application language mismatch (0.4 weight), scope breadth (0.3 weight) → produces a contamination level
- **LLM-as-judge:** Pluggable `LLMClient` interface — `judge.NewClient(judge.ClientOptions{...})` works with OpenAI, Azure, custom endpoints. Scores on **clarity, actionability, novelty** (and likely more)
- **Reference checking:** Validates external (HTTP/HTTPS) links in SKILL.md separately from internal (relative) links
- **Exit codes:** 0=clean, 1=errors, 2=warnings, 3=CLI usage error. `--strict` treats warnings as errors.

## Distribution

- **Homebrew:** `brew install agent-ecosystem/tap/skill-validator`
- **Go:** `go install github.com/agent-ecosystem/skill-validator/cmd/skill-validator@latest`
- **Pre-commit hooks:** 13 platforms — `claude`, `codex`, `copilot`, `cursor`, `gemini-cli`, `kiro`, `mistral-vibe`, `roo-code`, `trae`, `windsurf`, `amp`, `cline`, `goose`
- **Library:** Go imports for `orchestrate`, `judge`, `evaluate` packages

## How Context Elements Support Skills

This is **validation tooling for skill bundles** — analogous to SHACL for RDF data, lint for code, or a CI pipeline for typed contracts. The fact that it's shipped as a single Go binary with **pre-commit hooks for 13 different agents** is itself a composition pattern: one validator, many targets.

The 3-axis content quality scoring (imperative count/ratio, strong/weak language markers, information density) and contamination detection implement a lightweight **shape grammar** for SKILL.md content.

## Composition Notes

The `validate structure` command's strict mode + per-platform hooks pattern resembles [graphguard os guardrails](graphguard-os-guardrails.md) — both apply policy-as-code to multi-platform agent surfaces.

`skill-validator` is the **local / pre-commit** layer. The CI/CD layer is filled by [validate skill github action](validate-skill-github-action.md). The **registry / marketplace** layer is filled by [agentskill sh ags security scoring](agentskill-sh-ags-security-scoring.md). Together they form a three-layer validation stack:

1. **Pre-commit** (this tool, local Go binary)
2. **CI/CD** (Validate Skill GitHub Action, structural checks)
3. **Registry** (ags security scanner, 12-threat-category scoring)

## Reproducibility

**Very High.** Open-source, MIT-licensed, semver releases, full Go API, 13 platform hooks, homebrew + go install + pre-commit + library use paths all supported. Latest release v1.5.6 from Apr 2026 — actively maintained.

## Bundle Links
- [graphguard os guardrails](graphguard-os-guardrails.md) — Policy-as-code for multi-platform agent surfaces
- [owasp agentic skills top 10](owasp-agentic-skills-top-10.md) — Defines *what* a vulnerable skill is
- [agentic trust framework csa](agentic-trust-framework-csa.md) — Defines *maturity levels* for trust
- [validate skill github action](validate-skill-github-action.md) — CI/CD complement
- [agentskill sh ags security scoring](agentskill-sh-ags-security-scoring.md) — Registry-level security scanner
- [dspy agent skills bundle](dspy-agent-skills-bundle.md) — LLM-as-judge pattern precedent
