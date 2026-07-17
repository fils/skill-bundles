---
type: Skill Bundle Example
title: Awesome OpenClaw Skills — 179 CLI Utilities Catalog
description: A curated catalog of 179 CLI-based skills for the OpenClaw ecosystem, organized by domain category.
resource: https://github.com/VoltAgent/awesome-openclaw-skills
timestamp: '2026-05-25T00:00:00Z'
date: 2026-05-25
sources:
- https://github.com/VoltAgent/awesome-openclaw-skills
skills_included:
- 179 CLI skills across 6+ categories
context_elements:
- Category taxonomy (system, dev, security, AI lifecycle, finance, social)
- clawskills.sh marketplace integration
- Security bundle subset (agent-hardening, messageguard, error-guard, totp)
- Memory management pattern (pruning, compaction, state tracking)
composition_notes: 'Large ecosystem catalog demonstrating taxonomy-based organization at 179 skills.

  Contains an implicit security bundle (4+ guardrail skills) and memory management bundle.

  Similar to [claude skills ecosystem 1116](claude-skills-ecosystem-1116.md) but focused on CLI utilities rather than general skills.

  '
reproducibility: High — curated markdown catalog
confidence: 8/10
---

# Awesome OpenClaw Skills: 179 CLI Utilities

## Overview

A curated catalog of 179 CLI-based skills for the OpenClaw ecosystem, organized by domain category. Available at clawskills.sh for discovery and installation.

## Category Breakdown

### System Management & Automation
- iyeque-local-system-info (CPU, RAM, disk via psutil)
- restic-home-backup (encrypted backups with systemd)
- wol-sleep-pc (Wake-on-LAN/Sleep-on-LAN)

### Development & Code Quality
- audit-code (security review for hardcoded secrets)
- clean-pytest (Fake-based testing patterns)
- dependency-audit (security risks, outdated packages)
- agents-skill-tdd-helper (TDD enforcement for agents)
- sql-query-generator (secure SQL with validation)

### Security & Guardrails
- agent-hardening (input sanitization)
- messageguard (outgoing text filtering)
- error-guard (deadlock prevention)
- totp (TOTP verification for sensitive operations)

### Memory & Context Management
- arc-memory-pruner (memory compaction)
- context-compactor (token-based for local models)
- session-state-tracker (persistent state via hooks)

### Finance & Business
- Trading skills (A-share, HK, US markets)
- Freelance management (client tracking, invoice chasing)
- Strategy frameworks (MBB methodologies)

## Bundle Patterns Identified

### Security Bundle (4+ skills)
agent-hardening + messageguard + error-guard + totp = **defensive skill bundle**. This is analogous to [graphguard os guardrails](graphguard-os-guardrails.md) (SHACL + Cypher + Shadow) but at the CLI utility level.

### Memory Bundle (3 skills)
arc-memory-pruner + context-compactor + session-state-tracker = **context lifecycle management**. This represents a bundle for managing the agent's internal state.

### Development Bundle (5+ skills)
audit-code + clean-pytest + dependency-audit + tdd-helper + sql-query-generator = **development workflow bundle**, similar to the patterns in [agentic engineering workflow skills](agentic-engineering-workflow-skills.md).

## Source Attribution
Raw source: [awesome openclaw skills cli](../../raw/2026-05-25/awesome-openclaw-skills-cli.md)
