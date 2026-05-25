# Awesome OpenClaw Skills — CLI Utilities Catalog

**Source:** https://github.com/VoltAgent/awesome-openclaw-skills/blob/main/categories/cli-utilities.md
**Date:** 2026-05-25
**Signal:** 8/10

## Overview
Catalog of 179 CLI-based skills for the OpenClaw ecosystem. Wide coverage across system management, developer tools, security, AI lifecycle, finance, and social media.

## Notable Security & Guardrail Skills
- agent-hardening: Input sanitization against injection attacks
- messageguard: Filters outgoing text to prevent secret leaks
- error-guard: Prevents agent deadlocks, system safety
- totp: TOTP verification for sensitive operations
- audit-code: Security-focused review for hardcoded secrets

## Memory & Context Management Skills
- arc-memory-pruner: Prunes/compacts agent memory files
- context-compactor: Token-based compaction for local models
- session-state-tracker: Persistent state across restarts via lifecycle hooks

## Development Skills
- clean-pytest: Maintainable testing patterns
- dependency-audit: Security risks, outdated packages
- agents-skill-tdd-helper: Enforces TDD-style loops
- sql-query-generator: Secure SQL with validation

## Connection to Skill Bundles
This catalog demonstrates the **ecosystem-scale taxonomy pattern** — 179 skills organized by domain, showing how skills cluster around use cases. The security skills (agent-hardening, messageguard, error-guard) represent a **security bundle** within the larger ecosystem, similar to [[claude-skills-ecosystem-1116]]'s 754 cybersecurity skills mapped to MITRE/NIST.
