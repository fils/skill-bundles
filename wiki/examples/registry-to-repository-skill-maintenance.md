---
type: Skill Bundle Example
title: 'From Registry to Repository: Skill Authorship, Reuse & Maintenance'
description: First empirical study treating AI agent skills as **engineered software artefacts** — authored, reused, customized, and maintained — rather than only as agent capabilities.
resource: https://arxiv.org/abs/2607.00911
timestamp: '2026-07-16T00:00:00Z'
date: 2026-07-16
sources:
- arXiv:2607.00911
skills_included:
- Registry skills (skills.sh)
- Personal-use GitHub skills
- Reuse-link adaptation
context_elements:
- SWEBOK KA classification of skills
- Six-theme SKILL.md content taxonomy
- Six-theme maintenance taxonomy
- One-time copy reuse model
- Registry vs repository dual channel
composition: 'Empirical study: 18,463 registry + 23,199 personal skills, 3,709 reuse links; content + maintenance taxonomies for skill-as-artefact engineering.'
reproducibility: arXiv:2607.00911 Jul 2026; large mined corpus + qualitative coding of 180 skills / 444 modifications.
rating: 9
---

# From Registry to Repository: Skill Authorship, Reuse & Maintenance

**Origin:** Gao, Lulla, Lin, Baltes, Treude, Zahedi, arXiv:2607.00911, Jul 1 2026

## Overview

First empirical study treating AI agent skills as **engineered software artefacts** — authored, reused, customized, and maintained — rather than only as agent capabilities. Spans the **registry channel** (skills.sh) and the **personal-use repository channel** (GitHub).

## Corpus

| Channel | Count |
|---------|-------|
| skills.sh registry | 18,463 |
| Personal-use (5,876 repos) | 23,199 |
| Reuse links recovered | 3,709 |
| SE skills (SWEBOK-classified) | 29,450 |

## Content Taxonomy (6 themes)

1. Scoping and orchestrating
2. Running the execution lifecycle
3. Ensuring output quality
4. Governing agent conduct
5. Grounding domain knowledge
6. User/agent coordination

Software Construction dominates SWEBOK KAs with a long specialized tail.

## Maintenance Findings

- Reuse is largely a **one-time copy** (near-verbatim); **53% never modified** after adoption
- Subsequent local maintenance is overwhelmingly **additive**
- Primary change targets: reworking operational specifications; adapting knowledge/resources
- **Behavioral contracts** (how skill interacts with users, monitors state, recovers from failure) remain almost untouched
- Registry updates rarely flow back into forks (copy-fork drift)

## Edit Taxonomy (6)

metadata · operational specs · behavioral constraints · knowledge/resources · compatibility · polishing

## Context Elements

- **Dual-channel lifecycle** — publish vs local infrastructure skills
- **Copy-fork reuse model** — not package-manager-style updates
- **Stable behavioral contract** — soft interface that resists churn
- **Additive evolution** — accretes domain knowledge rather than refactoring structure

## Relation to Skill Bundle Patterns

- Maintenance science for [agent skills spec](agent-skills-spec.md) and marketplace catalogs
- Explains versioning immaturity seen in [inside skill market se activities](inside-skill-market-se-activities.md) (companion 2026-07-16)
- Motivates lockfiles/manifests from [assc skill supply chains skillbom](assc-skill-supply-chains-skillbom.md)
- Complements [skillopt trainable skill parameters](skillopt-trainable-skill-parameters.md) (systematic skill improvement vs ad-hoc edits)
- Complements [skillreducer token efficiency](skillreducer-token-efficiency.md) (many skills bloated/non-actionable)

## Key Insight

Skill bundles behave like **editable documentation dependencies**, not immutable packages: copy once, rarely pull updates, add local knowledge, leave behavioral contracts alone. Registries and tools should optimize for consolidating re-authored domain knowledge and project-specific bindings — not assume npm-style update streams.

