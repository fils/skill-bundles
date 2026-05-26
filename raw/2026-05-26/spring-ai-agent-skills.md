# Spring AI Agentic Patterns — Agent Skills

**Source:** https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills
**Fetched:** 2026-05-26
**Dependency:** Spring AI 2.0.0-M2+, spring-ai-agent-utils v0.4.2

## Overview
Modular framework for extending AI agent capabilities in Spring AI ecosystem. Part of `spring-ai-agent-utils` toolkit. LLM-agnostic (OpenAI, Anthropic, Google Gemini, etc.).

## Structure
Standard SKILL.md directory (compatible with Claude Code Skills):
```
my-skill/
├── SKILL.md          # YAML frontmatter + instructions
├── scripts/          # Python, Node, etc.
├── references/       # Documentation
└── assets/           # Templates, resources
```

## Three Core Tools
1. **SkillsTool (Required)** — discovery + loading of SKILL.md
2. **FileSystemTools (Optional)** — LLM reads reference files
3. **ShellTools (Optional)** — LLM executes helper scripts (via Bash)

## Example Configuration (Java)
```java
ChatClient chatClient = chatClientBuilder
    .defaultToolCallbacks(SkillsTool.builder()
        .addSkillsDirectory(".claude/skills")
        .build())
    .defaultTools(FileSystemTools.builder().build())
    .defaultTools(ShellTools.builder().build())
    .build();
```

## Progressive Disclosure Workflow
1. Discovery — agent loads name + description at startup
2. Activation — full SKILL.md on match
3. Execution — follow instructions, execute scripts, read refs

## Key Benefits
- LLM Agnostic — define once, use across providers
- Context Efficiency — lean context window
- Portability — version-controlled, cross-project sharing
- Integration — Dynamic Tool Discovery + Tool Argument Augmentation

## Critical Considerations
- **Security:** Scripts execute on host without sandboxing — use containers
- **Human-in-the-Loop:** no built-in approval — implement custom ToolCallback wrappers
- **Anthropic Native vs Generic:** Native runs in Anthropic cloud sandbox; Generic runs in your environment, model-agnostic

## Series Roadmap
- Part 2: AskUserQuestionTool
- Part 3: TodoWriteTool
- Part 4: Subagent Orchestration
- Part 5: A2A Integration
