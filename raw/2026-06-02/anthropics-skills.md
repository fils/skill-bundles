# anthropics/skills: Public repository for Agent Skills

Source: https://github.com/anthropics/skills
Date ingested: 2026-06-02

Repository: anthropics/skills
Stars: 145k | Forks: 17.1k

This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see agentskills.io.

Core Definition: "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."

## Repository Structure

- skills/ : Skill examples (Creative, Technical, Enterprise, Document)
- .claude-plugin/
- spec/
- template/

Includes production document skills (docx, pdf, pptx, xlsx).

## How to Use

/plugin marketplace add anthropics/skills

Then install document-skills etc.

## Creating a Basic Skill

Requires folder with SKILL.md containing YAML frontmatter + instructions.

Template provided with name, description, instructions, examples, guidelines.

## Document Skills (Production Reference)

skills/docx, skills/pdf, skills/pptx, skills/xlsx — source-available reference implementations.

This is a canonical, high-volume example of skill bundles from the originators (Anthropic). Strong on practical, production document skills. No formal SHACL/SSSOM context elements visible in summary, but the structure itself is a model for bundling.

Note: High signal, ingested for daily digest.