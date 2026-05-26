# Microsoft Agent Framework — Agent Skills

**Source:** https://learn.microsoft.com/en-us/agent-framework/agents/skills
**Fetched:** 2026-05-26

## Core Structure
Standard SKILL.md directory layout (compatible with open spec):
```
expense-report/
├── SKILL.md                          # YAML frontmatter + markdown
├── scripts/validate.py               # Executable code
├── references/POLICY_FAQ.md          # Reference docs (on-demand)
└── assets/expense-report-template.md # Static resources
```

## SKILL.md Format
```yaml
---
name: expense-report
description: File and validate employee expense reports.
license: Apache-2.0
compatibility: Requires python3
metadata:
  author: contoso-finance
  version: "2.1"
---
```
Name: max 64 chars, lowercase/hyphens/numbers. Description: max 1024 chars.

## Progressive Disclosure (4 stages)
1. Advertise (~100 tokens) — name + description only
2. Load (<5000 tokens) — full SKILL.md via `load_skill`
3. Read Resources — `read_skill_resource` for supplementary files
4. Run Scripts — `run_skill_script` for bundled code

## 3 Implementation Types
### A. File-Based Skills
Discovered from filesystem. C#: `AgentSkillsProvider`. Python: `SkillsProvider.from_paths()`.

### B. Code-Defined (Inline) Skills
Dynamic content, close over local state. Decorators: `@skill.resource`, `@skill.script`.

### C. Class-Based Skills
For distribution via NuGet or PyPI. C#: subclass `AgentClassSkill<T>`. Python: subclass `ClassSkill`.

## Advanced Features
- Dependency Injection (C#) and runtime kwargs (Python)
- Script Approval gating — human-in-the-loop
- Multi-Source Composition — aggregate, filter, deduplicate

## Skills vs Workflows
| Feature | Agent Skills | Workflows |
|---------|-------------|-----------|
| Control | AI decides path (Creative) | Explicit path (Deterministic) |
| Resilience | Single turn, full retry | Checkpointing, resume |
| Side Effects | Idempotent/low-risk | Sensitive actions |
| Complexity | Single-domain | Multi-step, multi-agent |

**Rule of Thumb:** Use skill if AI figures out HOW. Use workflow to guarantee WHAT.
