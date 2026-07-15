# SkillJect: Automating Stealthy Skill-Based Prompt Injection for Coding Agents

**Source:** arXiv:2602.14211 (cs.CR, cs.AI)
**Authors:** Xiaojun Jia, Jie Liao, Simeng Qin, Jindong Gu, Wenqi Ren, Xiaochun Cao, Yang Liu, Philip Torr
**Submitted:** Feb 15, 2026 (v1); revised Jun 16, 2026 (v3)
**Citations:** 7
**GitHub:** https://github.com/jiaxiaojunQAQ/SkillJect
**Signal Rating:** 9/10

## Abstract

Agent skills extend LLM agents with task-specific instructions, executable scripts, and auxiliary resources, improving reusability but creating a new supply-chain attack surface. A malicious or compromised skill can be repeatedly loaded as trusted guidance and steer downstream tool use. Existing skill-based prompt-injection attacks are often manual and brittle.

**SkillJect** is the first automated framework for generating poisoned skills against skill-enabled agent systems. Uses two coordinated channels:

1. **Artifact channel** — Hides the payload inside an auxiliary helper script.
2. **Instruction channel** — Rewrites SKILL.md with a front-loaded inducement strategy: places injected content at the beginning and frames the helper script as a mandatory prerequisite or initialization step. The rewritten instruction explicitly references the helper-script path and provides an executable example command, making the helper appear legitimate.

## Closed-Loop Multi-Agent Process

- **Attack Agent** — Generates poisoned skills
- **Victim Agent** — Executes downstream tasks with the poisoned skill
- **Evaluate Agent** — Inspects execution traces to determine whether the hidden payload was executed
- **Feedback loop** — Attack Agent uses evaluation feedback to diagnose failure causes and rewrite SKILL.md, keeping the payload fixed

## Supported Platforms & Methods

- **Agents:** Claude Code, OpenClaw
- **Methods:** direct_execution, skillject, template_injection, baseline
- **Attack categories:** Multiple (experiments across skill-enabled platforms, backend LLMs, and attack categories)

## Key Ideas

1. **Two-channel attack** — Separating payload (artifact/helper script) from inducement (instruction/SKILL.md) makes detection harder.
2. **Front-loaded inducement** — Placing injected content at the beginning of SKILL.md exploits the LLM's tendency to weight early instructions more heavily.
3. **Closed-loop refinement** — Multi-agent feedback loop iteratively improves attack effectiveness by learning from failed attempts.
4. **Mandatory prerequisite framing** — Framing the malicious helper script as a "mandatory initialization step" with an executable example command makes it appear legitimate.
5. **Persistent threat** — Poisoned skills are loaded repeatedly as trusted guidance, making them a persistent (not one-shot) attack vector.

## Context Elements

- **SKILL.md rewriting** — Instruction channel manipulates the skill definition file
- **Helper script injection** — Artifact channel embeds payload in auxiliary scripts
- **Trace-driven closed-loop refinement** — Multi-agent feedback for iterative improvement
- **Cross-platform attack** — Supports Claude Code and OpenClaw ecosystems

## Relation to Existing Wiki

- Attack vector distinct from [[badskill-backdoor-model-in-skill]] (model poisoning vs. prompt injection)
- Related to [[maltool-malicious-tool-attacks]] (code-level malicious tools)
- Defense counterpart: [[skillspector-nvidia-security-scanner]] (scanning for malicious patterns)
- Related to [[skillguard-permission-framework]] (runtime governance)
- Exploits the SKILL.md specification from [[agent-skills-spec]]
