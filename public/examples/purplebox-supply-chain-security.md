---
type: Skill Bundle Example
title: PurpleBox Security — AI Agent Skills Supply Chain Risk Analysis
description: PurpleBox Security published a comprehensive analysis of the security risks in the Agent Skills marketplace ecosystem.
resource: https://www.prplbx.com/blog/agent-skills-supply-chain
timestamp: '2026-05-25T00:00:00Z'
date: 2026-05-25
sources:
- https://www.prplbx.com/blog/agent-skills-supply-chain
skills:
- Security audit procedures for agent skills
- Attack taxonomy identification
context_elements:
- Attack taxonomy (6 vectors)
- CVE documentation (CVE-2026-25253)
- Marketplace infection rate tracking
- Security gap analysis (4 critical gaps)
- Remediation playbooks (immediate/short-term/long-term)
composition_notes: 'Negative example showing what skill bundles LACK — the security context elements that should

  be included but aren''t in the Agent Skills specification. Maps directly to the need for

  validation, signing, and authorization layers in bundles.

  '
reproducibility: High — published article with full data
confidence: 9/10
---

# PurpleBox Security: AI Agent Skills Supply Chain Risk

## Overview

PurpleBox Security published a comprehensive analysis of the security risks in the Agent Skills marketplace ecosystem. Within 7 weeks of the [agent skills spec](agent-skills-spec.md) open standard release, researchers identified a **12% infection rate** in public marketplaces — 341 malicious skills on ClawHub alone, ~900 total identified globally.

## The ClawHavoc Campaign

A coordinated attack responsible for 335/341 malicious skills:
- **Crypto Tools**: 111 malicious skills (Solana/Phantom wallet utilities)
- **YouTube/Polymarket**: 91 malicious skills (summarizers, trading bots)
- **Typosquats**: 29 near-misspellings of official CLI tools

## Attack Taxonomy (Context Element Gap Mapping)

| # | Attack Vector | What It Exploits |
|---|---|---|
| 1 | Supply Chain Poisoning | Open marketplace with no code signing |
| 2 | Prompt Injection via SKILL.md | No prompt sanitization layer |
| 3 | Unsigned Executable Code | Scripts run at agent privilege level |
| 4 | Social Engineering (ClickFix) | Users paste base64 commands |
| 5 | Discoverability Hijacking | No metadata integrity checks |
| 6 | Credential Exfiltration | Access to ~/.clawdbot/.env |

## Critical Vulnerability
CVE-2026-25253 (CVSS 8.8): 1-click RCE via query parameter `gatewayUrl` accepting WebSocket auto-connect with credentials.

## Security Gaps in the Standard
1. **No code signing** — no way to verify author or integrity
2. **No sandboxing guidance** — no execution isolation
3. **No permission models** — no enforcement layer
4. **No integrity checks** — no hash verification or path boundary enforcement

## Relation to Skill Bundle Security
This article directly maps to context elements needed in skill bundles:

| Gap | Existing Counterexample in Catalog |
|---|---|
| Code signing | [nvidia verified agent skills](nvidia-verified-agent-skills.md) (OpenSSF) |
| Sandboxing | [nemoclaw security scanner](nemoclaw-security-scanner.md) |
| Authorization | [veto agent authorization](veto-agent-authorization.md) |
| Supply chain | [github cli skill management](github-cli-skill-management.md) |
| Scanning | [mondoo agent skills security](mondoo-agent-skills-security.md) (14 attack patterns) |

## Why This Matters for Bundles
PurpleBox shows that skill bundles are an **active attack surface**. Any skill bundle design that doesn't include security as a context element (validation, signing, authorization, scanning) is vulnerable to the attack vectors documented here. This article provides the **theoretical foundation** for why bundles like [graphguard os guardrails](graphguard-os-guardrails.md), [tool use firewall](tool-use-firewall.md), and [veto agent authorization](veto-agent-authorization.md) exist — they are the defense against these attacks.

## Source Attribution
Raw source: [purplebox supply chain risk](../../raw/2026-05-25/purplebox-supply-chain-risk.md)
