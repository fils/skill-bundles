# Skill OS: Skills are the New Apps — Now It's Time for Skill OS

**Source:** AgenticOS 2026 Workshop Paper (os-for-agent.github.io/papers/AgenticOS_2026_paper_13.pdf)
**Authors:** Anonymous (under review)
**Signal Rating:** 9/10

## Abstract

Skills have taken the agent ecosystem by storm: major LLM agent platforms (Cursor, Claude Code, Antigravity, Coze) support skills natively, and skill counts are growing at breakneck pace. This paper surveys nearly 100,000 skills from public repositories and analyzes skill characteristics along structure, execution patterns, and system requirements. It argues skills have become a new form of application and impose new demands on the underlying system; these demands will give rise to a new system abstraction, **Skill OS**, that treats skills as first-class execution artifacts.

## Three Fundamental Properties of Skills (vs. Prompts)

1. **Locality:** The very presence of a skill implies repeated reuse
2. **Determinism:** Skills encode concrete scenarios, yielding stronger determinism and verifiability than generic prompts
3. **Environment requirements:** Skills exhibit common requirements on the runtime environment, enabling systems to serve skills more effectively

## Six Key Properties from 100K Skill Analysis

1. **Phased procedures:** Most skills explicitly specify multiple steps with natural step boundaries
2. **Semi-deterministic blocks:** Many contain blocks suitable for caching
3. **Semantic equivalence:** LLM-generated procedures are semantically equivalent despite surface-level differences (defeating exact matching)
4. **Safety requirements without enforcement:** Skills impose parallel-safety, idempotency requirements without enforcement mechanisms
5. **External dependency fragility:** Skills depend on external tools (shell, OS, databases, MCP) with high failure rates and token waste
6. **Cross-session sharing without global visibility:** Skills shared across sessions without global optimization/management

## Four Problems with Prompt-Centric Approach

1. **Semantic equivalence prevents caching:** LLMs produce semantically equivalent but differently-surfaced plans, preventing reuse of validated traces
2. **Token waste in prompt-specialized blocks:** Skills contain code/scripts/templates that must be specialized to current prompt/environment; regenerating wastes tokens
3. **Fragility from external dependencies:** When dependencies fail, executions degrade into repeated token-expensive trial-and-error
4. **Missing parallel safety:** Skills increasingly run in parallel branches; prompt-level instructions ("avoid interdependent procedures") are inadequate

## Skill OS Demands

The Skill OS abstraction must address:
1. **Locality-aware caching:** Cache skill execution results across invocations
2. **Dynamically constructed environments:** Build execution environments on demand
3. **Global skill management:** Cross-session visibility for optimization
4. **Structured failure handling:** Deterministic error handling, not trial-and-error
5. **Runtime security and auditing:** Enforce safety requirements (parallel-safety, idempotency)

## Context Elements

- **Empirical 100K skill analysis:** Largest skill corpus analysis to date
- **Six property taxonomy:** Structure, execution, system requirements
- **Skill OS abstraction:** OS-level system for skill management
- **Caching, environment construction, security enforcement:** System-level demands
- **Progressive unfolding:** Metadata at startup, full instructions on selection, resources on reference

## Key Insights

- Skills are a new form of application (like apps, not prompts)
- OS-level abstractions needed: processes → skills, virtual memory → skill caching, file permissions → skill security
- Current prompt-centric systems miss optimization opportunities (caching, parallelism, failure handling)
- Analogy to traditional OS: deterministic abstractions on complex, timing-dependent hardware
