---
date: 2026-07-10
sources:
  - raw/2026-07-10/openmontage-agentic-video.md
  - https://github.com/calesthio/OpenMontage
skills_included: 500+
context_elements:
  - pipeline-manifests
  - human-approval-gates
  - checkpoint-audit-trail
  - tool-registry
  - multi-platform-packaging
composition_notes: Domain production system with hard human gates and provenance checkpoints.
reproducibility: Medium-High — AGPL-3.0, active monorepo; full media pipeline deps are heavy
---

# OpenMontage Video Production Skills

**Origin:** [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) (~36.3k stars)

## Skills included

500+ agent skills across 12 video production pipelines and 52 tools. Layer-3 provider skills (e.g. Gemini Omni Flash conversational video edit). Multi-platform packaging for Claude, Codex, Cursor, Copilot, `.agents/skills`.

## Context elements

- **Pipeline manifests** — stage ordering and gate defaults
- **Human approval gates** — completed gated stages require `human_approved=True` (GATE VIOLATION otherwise)
- **Checkpoint / audit trail** — stage versioning, history archive, `events.jsonl` (cost, scene_id, start/finish/error)
- **Provider capability map** — quality_score + fallback lists as soft model ontology
- **Tools registry** — 52 tools instrumented via BaseTool

## How context supports skills

Gates and checkpoints are **hard constraints** on skill execution (authorization + provenance), not soft guidance. Analogous to promotion gates in [[agentic-trust-framework-csa]] and Iron Laws in engineering discipline bundles.

## Composition notes / reusability

- Infrastructure-as-skills for **media production** (extends conference-infra pattern from [[agents-at-conferences-infrastructure]])
- Strong human-in-the-loop formalization rarely this explicit in software-only skill repos

## Reproducibility assessment

**Medium-High.** Open source and documented protocols; full reproduction needs multi-provider API keys and media toolchain.

## Related

- [[agentic-trust-framework-csa]]
- [[constraint-rules-as-context]]
- [[skill-bundle-patterns]]

[[backlinks]]
