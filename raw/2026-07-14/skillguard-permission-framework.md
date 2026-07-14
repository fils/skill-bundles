# SkillGuard: A Permission Framework for Agent Skills

**Source:** arXiv:2606.03024 (https://arxiv.org/html/2606.03024v1)
**Date:** Submitted 02 Jun 2026
**Authors:** Shidong Pan (CSIRO), Xiaoyu Sun (ANU), Tianyi Zhang (ANU), Dianshu Liao (ANU), Meixue Si (UNSW), Zhenchang Xing (CSIRO & ANU)
**Code:** https://github.com/Dianshu-Liao/SkilLGuard
**Signal Rating:** 9/10

## Summary

SkillGuard is a skill-centric permission framework that treats skills as permission-bearing executable artifacts. It introduces a dual-plane governance model that jointly regulates context influence (what a skill injects into an agent's reasoning) and action side effects (what a skill causes the agent to do at runtime).

## Five Core Components

1. **Skill Manifest** — each skill declares its capability surface through a manifest; instantiates declared permissions into runtime policy state
2. **Runtime permission access control** — maps host-specific tool invocations to canonical capabilities, checks each action against live session policy
3. **User-mediated authorization** — users can approve once, approve for session, or deny
4. **Deny-by-default enforcement** — actions not explicitly permitted are blocked
5. **Capability inference + behavior monitoring** — infers skill capabilities and monitors runtime behavior

## Dual-Plane Governance Model

- **Context plane:** skills introduce instructions, examples, retrieved documents, memory fragments, hidden assumptions that reshape agent reasoning
- **Action plane:** skills trigger tool calls, file/secret access, code execution, network communication, delegation to other agents/skills/MCP servers

## Evaluation

- 315 real-world skills evaluated
- Permission taxonomy covers 99.76% of observed protected objects
- Automated manifest generation: 91.0% F1
- Adversarial: contextual injection attack success reduced from 32.37% → 23.02%
- Obvious injection attack success reduced from 25.56% → 16.67%
- Benign task utility maintained

## Skill Bundle Context

- Skill manifests = formal declaration of capability surface (context element)
- Runtime access control = enforcement/governance mechanism
- Dual-plane model = novel architectural pattern for skill governance
- Permission taxonomy = formal vocabulary for skill capabilities
- User-mediated authorization = human approval gate pattern
- Behavior monitoring = runtime verification element

## Related Work Cited

- Progent: programmable privilege control for LLM agents (tool-level)
- AgentBound: declarative access-control for MCP servers (sandbox-based)
- A2AS: agentic AI runtime security (context-oriented)
- Badskill: backdoor attacks on agent skills via model-in-skill poisoning
- Skillject: automating stealthy skill-based prompt injection

## Relevance to Skill Bundles

SkillGuard directly addresses the security/governance gap in skill bundles. The dual-plane governance model (context + action) is a novel architectural pattern that recognizes skills operate across two coupled planes. The skill manifest is a formal context element that declares capabilities before execution. This extends the skill bundle thesis from "skills + context artifacts" to "skills + permission governance + runtime enforcement."
