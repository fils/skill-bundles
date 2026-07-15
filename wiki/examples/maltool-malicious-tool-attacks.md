---
title: "MalTool: Malicious Tool Attacks on LLM Agents"
date: 2026-07-15
sources: ["arXiv:2602.12194", "https://rdi.berkeley.edu/blog/maltool/"]
skills_included: ["Malicious tool synthesis (standalone + embedded)", "CIA triad taxonomy for agent tools", "Automated verifier (functional + diversity)", "Coding-LLM-based tool generation"]
context_elements: ["CIA triad taxonomy (confidentiality, integrity, availability)", "Automated malicious tool verifier", "Dataset of 7,027 malicious tools (1,300 standalone + 5,727 embedded)", "Structural diversity enforcement"]
composition: "Attack framework: coding LLM generates malicious tools → automated verifier validates malicious behavior + structural diversity → iterative refinement → two datasets (standalone + embedded). Evaluated against existing detection methods."
reproducibility: "arXiv:2602.12194. Authors: UC Berkeley (Dawn Song) + Duke (Neil Gong). Datasets: 1,300 standalone + 5,727 embedded malicious tools."
rating: 9
---

# MalTool: Malicious Tool Attacks on LLM Agents

**Origin:** UC Berkeley + Duke University (arXiv:2602.12194, Feb 2026)
**Citations:** 10
**Authors:** Yuepeng Hu, Yuqi Jia, Mengyuan Li, Dawn Song, Neil Gong

## Overview

MalTool is the first systematic study of **malicious tool code implementations** for LLM agents. While prior work focused on manipulating tool metadata (names, descriptions) to increase installation/selection rates, MalTool demonstrates that the real threat lies in the tool's code implementation — embedding malicious behaviors that execute when the LLM agent selects and invokes the tool.

## Attack Framework

1. **CIA triad taxonomy** — Classifies malicious tool behaviors:
   - **Confidentiality** — Data exfiltration (stealing user data, credentials, environment variables)
   - **Integrity** — Unauthorized modifications (altering files, corrupting data, injecting dependencies)
   - **Availability** — Resource exhaustion (infinite loops, memory bombs, disk filling)

2. **MalTool synthesizer** — Coding-LLM-based framework that generates tools with specified malicious behaviors:
   - **Standalone mode** — Fully malicious tool (1,300 instances)
   - **Embedded mode** — Malicious behavior hidden within otherwise benign tool (5,727 instances)

3. **Automated verifier** — Validates that generated tools:
   - Exhibit intended malicious behaviors (functional correctness)
   - Differ sufficiently from previously generated instances (structural diversity)
   - Iteratively refines until both conditions are met

## Key Findings

- **Safety-aligned LLMs still generate malicious tools** — Even with safety training, coding LLMs can be prompted to synthesize malicious tools
- **Embedded attacks are harder to detect** — Malicious behavior hidden in benign implementations evades most detection methods
- **Existing defenses insufficient** — Both conventional malware detection and LLM-agent-specific methods show limited effectiveness
- **7,027 malicious tools generated** — Largest dataset of its kind for defense evaluation

## Context Elements

- **CIA triad taxonomy** — Formal classification framework for malicious tool behaviors
- **Automated verifier** — Validation + diversity checking (functional correctness + structural uniqueness)
- **Dataset of 7,027 malicious tools** — Benchmark for defense evaluation (1,300 standalone + 5,727 embedded)

## Relation to Skill Bundle Patterns

MalTool provides the attack taxonomy and dataset that defense frameworks must address. It defines the threat model for the skill supply chain.

- Attack counterpart to [[skillspector-nvidia-security-scanner]] (defense scanning)
- Related to [[clawhavoc-marketplace-attack]] (1,184 malicious skills on ClawHub)
- Related to [[skillsieve-malicious-skill-detection]] (three-layer detection — MalTool tests its limits)
- Related to [[skillfortify-formal-verification-supply-chain]] (formal verification — 6,487 malicious tools catalogued, MalTool provides the generation methodology)
- Complements [[badskill-backdoor-model-in-skill]] (model-level vs. code-level attacks)

## Key Insight

The skill/tool supply chain threat is not just about metadata manipulation — it's fundamentally about code-level malicious behavior. Even safety-aligned LLMs can generate structurally diverse malicious tools that evade existing detection. The CIA triad provides a formal taxonomy, but new defenses are urgently needed.

[[backlinks]]
