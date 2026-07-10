# OpenMontage — Agentic Video Production Skill System

**Source:** https://github.com/calesthio/OpenMontage  
**Stars:** ~36.3k (2026-07-10)  
**License:** AGPL-3.0  
**Claim:** World's first open-source agentic video production system  
**Signal rating:** 8/10 (domain pipeline skills + human approval gates + multi-agent platform packaging)

## Summary

Agentic video production studio: **12 pipelines, 52 tools, 500+ agent skills**. Turns AI coding assistants into a full video production system. Multi-platform packaging: `.agents/skills`, `.claude`, `.codex/prompts`, `.cursor`, Copilot command files.

## Bundle-relevant architecture

- Layered skills (Layer 3 skills e.g. `gemini-omni` for video editing loops)
- **Checkpoint protocol + human approval gates** — gated stages require `human_approved=True` or GATE VIOLATION
- Checkpoint history archive for stage versioning / gate audit trail / replay
- `events.jsonl` instrumentation (start/finish/error, scene_id, cost) for live board
- Manifest-binding gates (`human_approval_default: true` on assets stage)
- Provider fleet: Veo, Sora, Gemini Omni Flash (conversational edit without full regeneration), music, TTS, images
- Backlot live board for production status

## Context elements

| Element | Present? | Notes |
|---------|----------|-------|
| Skills (500+) | Yes | Domain video production |
| Pipelines / workflows | Yes | 12 pipelines, ordered stages |
| Constraint / gate rules | Yes | Human approval gates as hard constraints |
| Audit / provenance trail | Yes | Checkpoints + events.jsonl |
| Multi-platform distribution | Yes | Claude/Codex/Cursor/Copilot/.agents |
| Tools registry | Yes | 52 tools |

## Composition pattern

**Domain production system = skills + pipeline manifests + approval gates + audit trail**. Closest analogs in catalog: Superpowers (discipline gates), Agentic Trust Framework (promotion gates), NVIDIA verified skills (governance). Novel domain: video media production rather than software engineering.

## Composition notes

- Human-in-the-loop as first-class context element (not just post-hoc review)
- Provider quality_score + fallback lists = soft ontology of model capabilities
- Strong example of "infrastructure-as-skills" beyond conference protocols

## Follow-ups

- Deep-read AGENT_GUIDE / checkpoint-protocol for formal gate taxonomy
- Compare gate model to CSA Agentic Trust Framework maturity gates
