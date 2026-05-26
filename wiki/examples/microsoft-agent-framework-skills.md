# Microsoft Agent Framework — Enterprise Agent Skills Implementation

**Source:** https://learn.microsoft.com/en-us/agent-framework/agents/skills
**Date Added:** 2026-05-26 (Iteration 11)
**License:** Microsoft Docs (public)
**Bundle Type:** Enterprise Platform · .NET/C# Implementation · Python Implementation
**Confidence:** 9/10

## Name & Origin

Microsoft's implementation of the Agent Skills open specification within the **Microsoft Agent Framework**, a comprehensive enterprise agent platform. Provides three implementation types (file-based, code-defined, class-based) with deep .NET and Python ecosystem integration.

## Skills Included

- Standard SKILL.md-based skill creation and discovery
- Progressive disclosure (4-stage: Advertise → Load → Read Resources → Run Scripts)
- Script execution with optional human approval gating
- Multi-source composition (aggregate, filter, deduplicate skills)

## Context Elements

- **SKILL.md Specification (Microsoft variant):** YAML frontmatter with `name`, `description`, `license`, `compatibility`, `metadata.author`, `metadata.version` — extended from the base spec with first-class versioning and compatibility fields
- **Progressive Disclosure API:** `load_skill` (load SKILL.md), `read_skill_resource` (supplementary files), `run_skill_script` (execute code) — four-stage protocol with explicit token budgets (100t → 5kt → on-demand → on-demand)
- **Implementation Types:**
  - *File-Based:* `AgentSkillsProvider` (C#) / `SkillsProvider.from_paths()` (Python) — standard filesystem discovery
  - *Code-Defined (Inline):* `@skill.resource` / `@skill.script` decorators — dynamic content, local state closure
  - *Class-Based:* `AgentClassSkill<T>` (C#) / `ClassSkill` (Python) — distributable via NuGet/PyPI
- **Script Approval:** `ScriptApproval = true` / `require_script_approval=True` gates execution behind human intervention
- **Dependency Injection:** C# skills resolve services via `IServiceProvider` parameter; Python receives runtime kwargs
- **Skills vs Workflows Decision Guide:** AI-decided path (skills) vs explicit path (workflows)

## How Context Elements Support Skills

Microsoft's implementation is notable for its **enterprise-grade integration**:

1. **DI and Runtime Context:** Skills can receive authenticated user context, database connections, and configuration — making them first-class enterprise components
2. **Script Approval:** The human-in-the-loop gating mechanism addresses [[owasp-agentic-skills-top-10]]'s AST06 (Weak Isolation) concern
3. **Multi-Source Composition:** Aggregating, filtering, and deduplicating skills from files, code, and packages mirrors [[graph-of-skills-dependency-retrieval]]'s composition patterns
4. **Versioning:** The `metadata.version` field in SKILL.md frontmatter supports the version pinning recommended by [[nvidia-verified-agent-skills]]

## Composition Notes

This is the **most complete enterprise platform implementation** documented so far:

| Feature | Microsoft Agent Framework | [[spring-ai-agent-skills]] | [[agent-skills-spec]] |
|---------|--------------------------|---------------------------|----------------------|
| Languages | C#, Python | Java | N/A (spec) |
| Script Approval | Yes (built-in) | No (custom wrapper) | N/A |
| DI Support | Yes (IServiceProvider) | No | N/A |
| Multi-Source | Yes (aggregate/filter/dedup) | Single directory | N/A |
| Package Distribution | NuGet, PyPI | Maven/Gradle | N/A |
| Progressive Disclosure | 4-stage API | 3-stage (discovery→activation→execution) | 3-level spec |

The **Skills vs Workflows** decision guide is particularly valuable — it formalizes when to use skill bundles vs deterministic workflows, a distinction missing from most other implementations.

## Reproducibility

High — full documentation on Microsoft Learn with C# and Python code examples. Requires Microsoft Agent Framework SDK (production-ready).

## Bundle Links
- [[spring-ai-agent-skills]] — Java ecosystem counterpart
- [[agent-skills-spec]] — The open standard Microsoft implements
- [[nvidia-verified-agent-skills]] — Enterprise governance benchmark
- [[graph-of-skills-dependency-retrieval]] — Related composition pattern
