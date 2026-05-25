# Constraint Rules as Skill Context

## Overview

Some skill bundles encode **prohibitions and constraint rules** directly into their SKILL.md files, going beyond procedural instructions to enforce behavioral boundaries. This pattern treats skills not just as "how to do X" but as "what you must never do when doing X."

## Examples

### Superpowers "Iron Laws"
The [[superpowers-engineering-discipline-skills]] framework embeds non-negotiable constraints:
- TDD: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"
- Verification: "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"
- Debugging: "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"

These are **declarative prohibitions** — the agent reads the constraint and is forbidden from violating it.

### Red Flags (Negative Constraints)
Superpowers also documents **rationalization patterns** (Red Flags) that agents commonly use to skip discipline:
- "Tests passing on first run."
- "Keeping deleted code as reference."
- Using words like "should", "probably", or "seems to"

This is a **second-order constraint**: the agent is taught to recognize its own rationalizations.

### Security Constraints
[[nvidia-verified-agent-skills]] uses cryptographic signing (OpenSSF) as a constraint — unsigned skills cannot be installed. [[veto-agent-authorization]] implements a veto kernel where authorization decisions constrain what skills can execute.

### SHACL Validation as Constraint
[[graphguard-os-guardrails]] uses SHACL shapes + Cypher rules as deterministic guardrails — constraints that LLMs cannot bypass through prompt engineering. [[xpshacl-explainable-shacl]] adds explainability: when validation fails, the agent receives the reason.

## Pattern Classification

| Type | Mechanism | Examples |
|------|-----------|----------|
| Declarative Prohibition | Text constraint in SKILL.md | Superpowers Iron Laws |
| Negative Constraint | Anti-pattern documentation | Superpowers Red Flags |
| Cryptographic | Signature verification | NVIDIA OpenSSF |
| Schema Validation | SHACL shape checking | GraphGuard OS, xpSHACL |
| Authorization Kernel | Runtime veto decisions | Veto |

## Relationship to Other Concepts

- [[skill-bundle-patterns]]: Constraint rules are the most restrictive form of context element
- [[validator-explanation-pattern]]: Constraints need explanation when violated (xpSHACL pattern)
- Dependency constraints (Graph of Skills): Skills that require prerequisites can be viewed as constraints

## Status
Strong pattern — 5+ documented examples with distinct mechanisms.
