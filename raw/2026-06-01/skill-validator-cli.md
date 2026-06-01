# agent-ecosystem/skill-validator — CLI Validator + LLM-as-Judge

**Extracted:** 2026-06-01
**Source:** https://github.com/agent-ecosystem/skill-validator
**License:** MIT | **Language:** Go 100% | **Stars:** 151 | **Forks:** 25
**Latest Release:** v1.5.6 (Apr 28, 2026)

## What It Is

A **CLI tool that validates and scores Agent Skill packages** (per the agentskills.io SKILL.md spec) — going well beyond spec compliance to check link rot, token cost, content quality, cross-language contamination, and LLM-as-judge quality scoring.

> "Spec compliance is table stakes. `skill-validator` goes further: it checks that links actually resolve, flags files that shouldn't be in a skill directory, reports token counts so you can see how much of an agent's context window your skill will consume, analyzes content quality metrics, detects cross-language contamination, and offers LLM-as-judge scoring to evaluate skill quality across dimensions like clarity, actionability, and novelty. A spec-compliant skill that has broken links or a 60k-token reference file will technically pass the spec but perform poorly in practice."

## Installation

- **Homebrew:** `brew install agent-ecosystem/tap/skill-validator`
- **Go:** `go install github.com/agent-ecosystem/skill-validator/cmd/skill-validator@latest`
- **Pre-commit hook:** Available for **13 platforms** (claude, codex, copilot, cursor, gemini-cli, kiro, mistral-vibe, roo-code, trae, windsurf, amp, cline, goose)
- **Library:** Go import as `github.com/agent-ecosystem/skill-validator/{orchestrate,judge,evaluate}`

## Command Surface (Lifecycle-Mapped)

| Stage | Command | What It Answers |
|---|---|---|
| Scaffolding | `validate structure` | Does it conform to the spec and can agents use it? |
| Writing content | `analyze content` | Is the instruction quality good? |
| Adding examples | `analyze contamination` | Am I introducing cross-language contamination? |
| Review | `validate links` | Do external links still resolve? |
| Quality scoring | `score evaluate` | How does an LLM judge rate this skill? |
| Comparing models | `score report` | How do scores compare across different LLM providers? |
| Pre-publish | `check` | Run everything (except LLM scoring) |

## Context Elements (This Is a Tool, but It's Also a Bundle)

- **Validation rules:** Spec-compliance + custom allow/deny rules (`--allow-extra-frontmatter`, `--allow-flat-layouts`, `--allow-dirs=evals,testing`)
- **Content quality metrics:** word count, code block count/ratio, code languages, sentence count, imperative count/ratio, strong/weak language markers, information density, instruction specificity, section count, list item count
- **Contamination detection:** Multi-interface tools (0.3 weight), application language mismatch (0.4 weight), scope breadth (0.3 weight) → produces a Levenshtein-style contamination level
- **LLM-as-judge:** Pluggable `LLMClient` interface — `judge.NewClient(judge.ClientOptions{...})` works with OpenAI, Azure, custom endpoints. Scores on **clarity, actionability, novelty** (plus likely more — full dimension list in source)
- **Reference checking:** Validates external (HTTP/HTTPS) links in SKILL.md separately from internal (relative) links checked by `validate structure`
- **Exit codes:** 0=clean, 1=errors, 2=warnings, 3=CLI usage error. `--strict` treats warnings as errors.
- **Pre-commit hooks for 13 platforms:** Treats the skill itself as a unit that can be guarded across all major coding agents.

## Why It Matters for the Catalog

This is **validation tooling for skill bundles** — analogous to SHACL for RDF data, lint for code, or a CI pipeline for typed contracts. The fact that it's shipped as a single Go binary with **pre-commit hooks for 13 different agents** is itself a composition pattern: one validator, many targets.

**Cross-reference:** Pairs with the **OWASP Agentic Skills Top 10** and **Agentic Trust Framework** in the wiki — both define what bad skills look like; skill-validator provides automated detection of the *quality* dimension (not yet security scoring — that's the gap filled by `agentskill-sh/ags`).

**Cross-reference:** The `validate structure` command's strict mode + per-platform hooks pattern resembles **GraphGuard OS** (in the catalog) — both apply policy-as-code to multi-platform agent surfaces.
