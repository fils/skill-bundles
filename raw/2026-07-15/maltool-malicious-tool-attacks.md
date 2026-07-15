# MalTool: Malicious Tool Attacks on LLM Agents

**Source:** arXiv:2602.12194 (cs.CR)
**Authors:** Yuepeng Hu, Yuqi Jia, Mengyuan Li, Dawn Song, Neil Gong
**Submitted:** Feb 12, 2026 (v1); revised May 9, 2026 (v3)
**Citations:** 10
**Affiliation:** UC Berkeley (Dawn Song) + Duke University (Neil Gong)
**Blog:** https://rdi.berkeley.edu/blog/maltool/
**Signal Rating:** 9/10

## Abstract

In a malicious tool attack, an attacker uploads a malicious tool to a distribution platform; once a user inadvertently installs the tool and the LLM agent selects it during task execution, the tool can compromise the user's security and privacy. Prior work focuses on manipulating tool names and descriptions to increase the likelihood of installation by users and selection by LLM agents. However, a successful attack also requires embedding malicious behaviors in the tool's code implementation, which remains largely unexplored.

**MalTool** is the first systematic study of malicious tool code implementations. Key contributions:

1. **Taxonomy of malicious tool behaviors** based on the confidentiality-integrity-availability (CIA) triad, tailored to LLM-agent settings.
2. **MalTool framework** — A coding-LLM-based framework that synthesizes tools exhibiting specified malicious behaviors, either as standalone tools or embedded within otherwise benign implementations.
3. **Automated verifier** — Validates whether generated tools exhibit intended malicious behaviors and differ sufficiently from previously generated instances, iteratively refining until success.
4. **Datasets** — 1,300 standalone malicious tools + 5,727 real-world tools with embedded malicious behaviors.
5. **Detection gap** — Existing detection methods (conventional malware detection + LLM-agent-specific methods) show limited effectiveness, highlighting urgent need for new defenses.

## Key Ideas

- **Code-level attacks matter** — Prior work focused on metadata manipulation (names, descriptions); MalTool shows code-level malicious behavior is the real threat.
- **Safety-aligned LLMs still generate malicious tools** — Even safety-aligned coding LLMs can be prompted to synthesize malicious tools.
- **CIA triad for agent tools** — Confidentiality (data exfiltration), Integrity (unauthorized modifications), Availability (resource exhaustion).
- **Standalone vs. embedded** — Two attack modes: fully malicious standalone tools vs. malicious behavior embedded within otherwise benign implementations.
- **Structural diversity** — Automated verifier ensures malicious tools are structurally diverse (not just copies), evading pattern-based detection.

## Context Elements

- **CIA triad taxonomy** — Classification framework for malicious tool behaviors
- **Automated verifier** — Validation + diversity checking (functional correctness + structural uniqueness)
- **Dataset of 7,027 malicious tools** — 1,300 standalone + 5,727 embedded; benchmark for defense evaluation

## Relation to Existing Wiki

- Attack counterpart to [[skillspector-nvidia-security-scanner]] (defense)
- Related to [[clawhavoc-marketplace-attack]] (1,184 malicious skills)
- Related to [[skillsieve-malicious-skill-detection]] (detection framework)
- Related to [[skillfortify-formal-verification-supply-chain]] (6,487 malicious tools catalogued)
- Provides the attack taxonomy that defense frameworks (SkillSpector, SkillFortify, SkillSieve) must address
