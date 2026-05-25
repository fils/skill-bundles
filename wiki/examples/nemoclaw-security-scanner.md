# NemoClaw: NVIDIA Agent Skills Security Scanner

## Overview

NemoClaw is NVIDIA's **agent skill security scanning** system referenced by [[nvidia-verified-agent-skills]] and the [[mondoo-agent-skills-security]] analysis. It provides LLM-assisted security review of skill definitions, scripts, and bundled resources to detect vulnerabilities, prompt injections, and malicious patterns that traditional static analysis misses.

**Context Elements:** LLM-assisted reasoning for security review · Vulnerability detection patterns · SKILL.md analysis · Script scanning · Prompt injection detection

## Capabilities

Based on NVIDIA's verified agent skills ecosystem:
- Detects hidden instructions (HTML comments, Unicode invisible text)
- Identifies credential harvesting patterns in bundled scripts
- Flags suspicious network calls in `scripts/` directories
- Validates that allowed-tools constraints are appropriate for the skill's stated purpose
- Analyzes SKILL.md instructions for manipulation patterns

## Relationship to Other Context Elements

NemoClaw scanning represents the **LLM-assisted validation** pattern complementing the cryptographic signing in [[nvidia-verified-agent-skills]]:
- **OpenSSF signing** verifies authenticity (who published this skill)
- **NemoClaw scanning** verifies intent (what does this skill actually do)
- Together they form the two pillars of [[verified-skill-governance]]

## Confidence
7/10 — Referenced in both NVIDIA verified agents docs and Mondoo security analysis as an active tool.

## Sources
- Referenced in https://mondoo.com/blog/agent-skills-real-power-real-risk
- Referenced in NVIDIA verified agent skills ecosystem documentation
