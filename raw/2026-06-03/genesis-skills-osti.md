# Genesis Skills Repository (OSTI)

**Source**: https://gitlab.osti.gov/genesis/genesis-skills
**Type**: Curated Agent Skills bundle repository
**License**: Apache 2.0 (root), mixed third-party
**Last Updated**: ~1 week ago (commit c790b43a)
**Skill Count**: 74 skills

## Description

A curated collection of 74 Claude Code skills (following the Agent Skills open standard) that extend Claude with domain expertise for science, engineering, HPC, and AI workflows. Part of the Genesis Mission at OSTI.

Skills are distributed as markdown files (`SKILL.md`) with YAML frontmatter. Includes an `unpack.sh` installer and `skill-search` discovery skill.

## Key Features

- **Installation**: `./unpack.sh` (symlinks or copy mode, supports domains)
- **Discovery**: `skill-search` skill for catalog exploration
- **Invocation**: `/skill-name` or context-activated
- **Harness support**: Also populates `.agents/skills/` for Codex/Gemini

## Bundled Skill Categories

**Genesis Core** (3)
- literature-search
- academy (distributed scientific computing)
- skill-search

**Anthropic Skills** (16)
**OpenAI Skills** (22)
**Superpowers** (8) — re-packaged
**LangChain Skills** (8)
**HuggingFace Skills** (8)
**HPC Skills** (5) — Slurm, PBS, Frontier, Perlmutter, Aurora
**Plasma Simulation** (2) — GS2, Gkeyll
**ModCon BASE Data Skills** (3) — Croissant, HDMF, datacards

## Repository Structure

```
genesis-skills/
├── unpack.sh
├── skill-search/
├── skills/
│   ├── academy/
│   ├── literature-search/
│   ├── anthropic-skills/
│   ├── openai-skills/
│   ├── superpowers-skills/
│   ├── langchain-skills/
│   ├── huggingface-skills/
│   ├── hpc-skills/
│   ├── plasma-sim-skills/
│   └── modcon-skills/
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE
└── README.md
```

## Relevance to Skill Bundles Research

- Large-scale real-world example of skill packaging and distribution
- Follows the exact Agent Skills / SKILL.md specification
- Demonstrates domain-specific bundling (HPC, plasma, scientific computing)
- Includes re-packaging of existing bundles (Superpowers)
- Government lab provenance with clear governance (CONTRIBUTING.md, review process)
- Strong emphasis on discoverability and installation tooling

## Links

- Repo: https://gitlab.osti.gov/genesis/genesis-skills
- Issues: https://gitlab.osti.gov/genesis/genesis-skills/-/issues
- Contact: genesis@osti.gov

---

**Ingestion note**: Extracted 2026-06-03 via web tools. High-signal example for validation, distribution, and domain taxonomy patterns.