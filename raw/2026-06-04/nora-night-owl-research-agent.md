# GRIND-Lab-Core/night_owl_research_agent (NORA)

**Source**: https://github.com/GRIND-Lab-Core/night_owl_research_agent
**arXiv**: https://arxiv.org/abs/2605.02092
**Date ingested**: 2026-06-04

## Description
Fully automatic, domain-aware AI research agent for Geoscientists, Remote Sensing researchers, and GIScientists — powered entirely by Claude Code skills. Skills-first system where all research logic lives in Markdown skill files.

## Architecture
Skills-first design with harness engineering (PreToolUse/PostToolUse/Stop/Notification hooks), MCP servers (geo_mcp, arxiv_mcp, etc.), memory & token optimization (three-layer memory), journal profiles (YAML-driven LaTeX).

## Skills (23 Workflow + Domain Knowledge)
Workflow: full-pipeline, lit-review, idea-discovery-pipeline, generate-idea, novelty-check, deploy-experiment, spatial-analysis, auto-review-loop, generate-report, paper-writing-pipeline, etc.
Domain Knowledge: spatial-methods.md, geoai-domain.md, academic-writing.md, apa-citations.md, etc.

## Context Elements
- Control Flags in CLAUDE.md: AUTO_PROCEED, HUMAN_CHECKPOINT, COMPACT_MODE, EXTERNAL_REVIEW, REVIEWER_DIFFICULTY
- Autoresearch Scoring Loop with 5 dimensions (Novelty 30%, Rigor 25%, etc.) with hard floors and weighted avg.
- Output files: NARRATIVE_REPORT.md, PAPER_PLAN.md, manuscript/, AUTO_REVIEW_REPORT.md, REVIEW_STATE.json, TELEMETRY, PROJ_NOTES.md, MEMORY.md, handoff.json
- Design principles in design_principle.md and design_principle_agents.md (9 sub-agents)

## Composition Notes
Full end-to-end pipeline chaining skills. Domain-specific (GIScience) with formal scoring, human checkpoints, harness for reliability. Strong example of skill bundle + validation (scoring loop) + rules (flags) + vocab (domain knowledge).

## Reproducibility
MIT, detailed install, launcher, templates for 7+ journals. arXiv paper provides academic backing.

---

*High signal: complete research agent as skill bundle with extensive context artifacts (scoring, harness, MCP, memory).*