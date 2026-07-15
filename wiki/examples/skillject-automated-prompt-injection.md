---
title: "SkillJect: Automated Skill-Based Prompt Injection for Coding Agents"
date: 2026-07-15
sources: ["arXiv:2602.14211", "https://github.com/jiaxiaojunQAQ/SkillJect"]
skills_included: ["Poisoned skill generation (artifact + instruction channels)", "Front-loaded inducement strategy", "Closed-loop multi-agent refinement", "Helper script payload embedding"]
context_elements: ["Two-channel attack model (artifact + instruction)", "SKILL.md rewriting with front-loaded inducement", "Closed-loop multi-agent process (Attack→Victim→Evaluate)", "Trace-driven refinement", "Cross-platform support (Claude Code, OpenClaw)"]
composition: "Attack framework: Attack Agent generates poisoned skill (payload in helper script + front-loaded inducement in SKILL.md) → Victim Agent executes task with poisoned skill → Evaluate Agent inspects traces → feedback to Attack Agent for iterative refinement. Payload stays fixed; SKILL.md is rewritten."
reproducibility: "Open-sourced on GitHub (jiaxiaojunQAQ/SkillJect). Supports Claude Code, OpenClaw. Methods: direct_execution, skillject, template_injection, baseline."
rating: 9
---

# SkillJect: Automated Skill-Based Prompt Injection for Coding Agents

**Origin:** arXiv:2602.14211, Feb 2026 (v3: Jun 2026)
**Citations:** 7
**GitHub:** https://github.com/jiaxiaojunQAQ/SkillJect
**Authors:** Xiaojun Jia, Jie Liao, Simeng Qin, Jindong Gu, Wenqi Ren, Xiaochun Cao, Yang Liu, Philip Torr

## Overview

SkillJect is the first **automated** framework for generating poisoned skills against skill-enabled agent systems. Unlike manual skill-injection attacks that are brittle and easily detected, SkillJect uses a closed-loop multi-agent process to iteratively generate and refine poisoned skills that are both effective and stealthy.

## Two-Channel Attack

1. **Artifact channel** — Hides the malicious payload inside an auxiliary helper script (e.g., `scripts/setup.py`, `lib/utils.js`). The payload is not in the SKILL.md itself, making it harder to detect by instruction-level scanning.

2. **Instruction channel** — Rewrites SKILL.md with a **front-loaded inducement strategy**:
   - Places injected content at the **beginning** of SKILL.md (exploiting LLM's tendency to weight early instructions more heavily)
   - Frames the helper script as a **mandatory prerequisite** or initialization step
   - Provides an **executable example command** referencing the helper-script path
   - Makes the malicious helper appear to be a legitimate setup step

## Closed-Loop Multi-Agent Process

```
Attack Agent → generates poisoned skill
    ↓
Victim Agent → executes downstream task with poisoned skill
    ↓
Evaluate Agent → inspects execution traces for payload execution
    ↓
Feedback → Attack Agent diagnoses failure, rewrites SKILL.md (payload fixed)
    ↓ (loop)
```

The **payload stays fixed** while the SKILL.md inducement strategy is iteratively refined based on trace feedback.

## Supported Platforms

- **Agents:** Claude Code, OpenClaw
- **Methods:** direct_execution, skillject, template_injection, baseline
- **Attack categories:** Multiple (experiments across platforms, LLMs, and categories)

## Context Elements

- **Two-channel attack model** — Artifact (helper script) + instruction (SKILL.md) separation
- **SKILL.md rewriting** — Manipulation of the skill definition file (cf. [[agent-skills-spec]])
- **Front-loaded inducement** — Exploiting positional bias in LLM instruction following
- **Closed-loop multi-agent** — Attack→Victim→Evaluate feedback cycle
- **Trace-driven refinement** — Execution trace analysis for iterative improvement

## Relation to Skill Bundle Patterns

SkillJect demonstrates that the SKILL.md specification itself is an attack surface. The skill bundle structure (instructions + scripts + resources) can be weaponized.

- Attack vector distinct from [[badskill-backdoor-model-in-skill]] (prompt injection vs. model poisoning)
- Related to [[maltool-malicious-tool-attacks]] (code-level attacks — SkillJect targets the skill definition layer)
- Defense counterpart: [[skillspector-nvidia-security-scanner]] (must scan helper scripts, not just SKILL.md)
- Related to [[skillguard-permission-framework]] (must govern auxiliary scripts, not just main skill)
- Exploits the [[agent-skills-spec]] SKILL.md format

## Key Insight

Poisoned skills are a persistent (not one-shot) threat: they are loaded repeatedly as trusted guidance. The two-channel attack (payload in helper script + inducement in SKILL.md) and closed-loop multi-agent refinement make automated generation of stealthy, effective poisoned skills feasible. This elevates skill-based prompt injection from manual, brittle attacks to automated, adaptive threats.

[[backlinks]]
