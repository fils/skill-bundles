---
type: Concept
title: Constraint Rules as Skill Context
description: Some skill bundles encode **prohibitions and constraint rules** directly into their SKILL.md files, going beyond procedural instructions to enforce behavioral boundaries.
---

# Constraint Rules as Skill Context

## Overview

Some skill bundles encode **prohibitions and constraint rules** directly into their SKILL.md files, going beyond procedural instructions to enforce behavioral boundaries. This pattern treats skills not just as "how to do X" but as "what you must never do when doing X."

## Examples

### Superpowers "Iron Laws"
The [superpowers engineering discipline skills](../examples/superpowers-engineering-discipline-skills.md) framework embeds non-negotiable constraints:
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
[nvidia verified agent skills](../examples/nvidia-verified-agent-skills.md) uses cryptographic signing (OpenSSF) as a constraint — unsigned skills cannot be installed. [veto agent authorization](../examples/veto-agent-authorization.md) implements a veto kernel where authorization decisions constrain what skills can execute.

### SHACL Validation as Constraint
[graphguard os guardrails](../examples/graphguard-os-guardrails.md) uses SHACL shapes + Cypher rules as deterministic guardrails — constraints that LLMs cannot bypass through prompt engineering. [xpshacl explainable shacl](../examples/xpshacl-explainable-shacl.md) adds explainability: when validation fails, the agent receives the reason.

## Pattern Classification

| Type | Mechanism | Examples |
|------|-----------|----------|
| Declarative Prohibition | Text constraint in SKILL.md | Superpowers Iron Laws |
| Negative Constraint | Anti-pattern documentation | Superpowers Red Flags |
| Cryptographic | Signature verification | NVIDIA OpenSSF |
| Schema Validation | SHACL shape checking | GraphGuard OS, xpSHACL |
| Authorization Kernel | Runtime veto decisions | Veto |

## Relationship to Other Concepts

- [skill bundle patterns](skill-bundle-patterns.md): Constraint rules are the most restrictive form of context element
- [validator explanation pattern](validator-explanation-pattern.md): Constraints need explanation when violated (xpSHACL pattern)
- Dependency constraints (Graph of Skills): Skills that require prerequisites can be viewed as constraints

## Status
Strong pattern — 5+ documented examples with distinct mechanisms.
