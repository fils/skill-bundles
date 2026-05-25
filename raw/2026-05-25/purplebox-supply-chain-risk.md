# PurpleBox Security — AI Agent Skills Supply Chain Risk

**Source:** https://www.prplbx.com/blog/agent-skills-supply-chain
**Date:** 2026-02-07 (extracted 2026-05-25)
**Signal:** 9/10

## Key Finding
Within 7 weeks of Agent Skills open standard release, 12% infection rate in public marketplaces. 341 malicious skills on ClawHub, ~900 total globally.

## The ClawHavoc Campaign
- Coordinated effort responsible for 335/341 malicious skills on ClawHub
- Crypto Tools: 111 skills (Solana/Phantom wallet)
- YouTube/Polymarket: 91 skills (summarizers, trading bots)
- Typosquats: 29 skills

## Attack Taxonomy
1. Supply Chain Poisoning — malicious code in open marketplaces
2. Prompt Injection via SKILL.md — adversarial instructions hijack context
3. Unsigned Executable Code — scripts run at agent privilege level
4. Social Engineering — ClickFix base64-encoded commands
5. Discoverability Hijacking — malicious metadata for skill selection
6. Credential Exfiltration — targeting ~/.clawdbot/.env

## Critical Vulnerability
CVE-2026-25253 (CVSS 8.8): 1-click RCE via query parameter gatewayUrl accepting WebSocket auto-connect with credentials.

## Security Gaps in Standard
- No code signing
- No sandboxing guidance
- No permission models/enforcement
- No integrity checks/hash verification

## Connection to Skill Bundles
This article maps the **security context element gap** in skill bundle design. It's a negative example showing why bundles MUST include validation, signing, and authorization layers.
