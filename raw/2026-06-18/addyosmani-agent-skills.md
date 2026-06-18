# addyosmani/agent-skills — Production-Grade Engineering Skills Bundle

**Source:** https://github.com/addyosmani/agent-skills (extracted 2026-06-18)
**Date ingested:** 2026-06-18
**Signal:** Very High — 24 structured skills + lifecycle + personas + verification gates (closest to formal context elements)

## Key Ideas
- 24 production-grade skills for AI coding agents covering full engineering lifecycle: DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP.
- Includes 4 agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor).
- Every skill has consistent anatomy: Frontmatter, Overview, When to Use, Process (step-by-step), Rationalizations, Red Flags, Verification.
- Strong emphasis on verification, quality gates, anti-rationalization tables.
- Slash commands and hooks for integration.

## Context Elements Present
- **Verification/Validation:** Explicit "Verification (evidence requirements)" section in every skill; personas for security, performance, testing.
- **Rules & Best Practices:** Embedded as "Key Principle", "Red Flags", checklists in references/.
- **Taxonomy/Ontology:** Lifecycle stages + persona roles provide a taxonomy of engineering workflows.
- No SHACL or SSSOM found, but the structured SKILL.md + references/ act as a lightweight ontology + rule set.

## Relevance to Skill Bundles
This is a prime example of a **skill bundle** with rich context: 24 skills + personas + references/checklists + lifecycle ontology. The verification sections and personas provide guardrails similar to SHACL shapes or rule sets. High reproducibility via consistent frontmatter and process steps.

## Composition Patterns
- Meta-skill (`using-agent-skills`) maps work to correct workflow.
- Sub-agents/personas invoked for specialized review.
- Progressive disclosure + progressive verification.

**License:** MIT
**Stars:** ~62.6k (as of extraction)