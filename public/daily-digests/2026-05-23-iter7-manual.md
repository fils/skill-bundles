---
type: Daily Digest
title: 'Daily Digest — 2026-05-23 (Manual Seed: SSSOM/Mapping)'
description: '- **URL:** https://arxiv.org/html/2605.09184v1 - **Author:** Fabio Rovai (The Tesseract Academy, London) - **Type:** Peer-reviewed preprint with empirical benchmarks'
resource: https://arxiv.org/html/2605.09184v1
timestamp: '2026-05-23T00:00:00Z'
date: '2026-05-23'
---

# Daily Digest — 2026-05-23 (Manual Seed: SSSOM/Mapping)

## Sources Added

### 1. Open Ontologies Paper — Stable Matching Alignment
- **URL:** https://arxiv.org/html/2605.09184v1
- **Author:** Fabio Rovai (The Tesseract Academy, London)
- **Type:** Peer-reviewed preprint with empirical benchmarks

### 2. Open Ontologies GitHub Repository
- **URL:** https://github.com/fabio-rovai/open-ontologies
- **Type:** Production Rust MCP server (17,400 LOC, MIT license)

## Key Findings

### SSSOM/Mapping Gap — ADDRESSED

**Open Ontologies** provides the first strong example in this catalog that combines agent skills with formal mapping/alignment. Key contributions:

1. **Six-Signal Similarity Scoring:** Labels, properties, parents, instances, restrictions, neighborhood — closely mirrors SSSOM's approach to documenting mappings with provenance and confidence scores.

2. **Stable Matching Breakthrough:** 1-to-1 assignment constraint is dominant — "signal weights are irrelevant when stable matching is applied (F1 varies by <0.004), while removing stable matching drops F1 to 0.728." This is a fundamental insight for any skill bundle requiring cross-ontology mappings.

3. **Tool-Access Advantage:** LLM + MCP Tools yields F1 = 0.717 (+264% vs paper best), while raw file access (Turtle syntax) degrades performance to F1 = 0.323 (-25% vs no file). This proves that mapping quality depends on access modality, not just signal weights.

4. **Production Mapping Engine:** The `onto_align` tool implements the stable matching algorithm with LLM adjudication for ambiguous cases. This is a ready-made component that could be integrated into any agent skill bundle requiring SSSOM-style cross-ontology mapping.

### Context Element Coverage Update

| Context Element | Before | After |
|----------------|--------|-------|
| SSSOM Mapping | 0 | **1** (Open Ontologies) |
| Alignment Algorithms | 0 | **1** (Stable matching) |
| Cross-Ontology Mapping | 0 | **1** (32 standard ontologies + clinical crosswalks) |

### Benchmarks

- **OAEI Anatomy Track:** P=0.963, R=0.733, F1=0.832 (highest precision of any reported system)
- **Reasoning Speed:** 15ms vs 24,490ms (HermiT) for 50,000 axioms — 1,633x speedup
- **OntoAxiom:** MCP Extraction F1 = 0.717, +264% vs paper best

## Next Steps for Tomorrow's Run

1. Search for additional SSSOM/mapping examples beyond Open Ontologies
2. Investigate the formal SSSOM spec (https://mapping-commons.github.io/sssom/) for comparison
3. Look for other ontology alignment tools (AML, LogMap, POMAP++) as supplementary mapping examples
4. Explore whether Open Ontologies' `onto_align` could be used as a mapping skill in other bundles

## Linked Examples

- [Agent Skills Specification](../examples/agent-skills-spec.md)
- [Agentic Engineering Workflow Skills](../examples/agentic-engineering-workflow-skills.md)
- [DSPy Agent Skills Bundle: Production-Grade DSPy Optimization](../examples/dspy-agent-skills-bundle.md)
- [NORA — Night Owl Research Agent](../examples/nora-gis-research-agent.md)
- [NVIDIA Skills Repository — Multi-Product Catalog](../examples/nvidia-skills-repo.md)
- [NVIDIA Verified Agent Skills — Governance & Verification](../examples/nvidia-verified-agent-skills.md)
- [Ontologizer — OpenClaw Ontology Skill](../examples/ontologizer-openclaw-ontology-skill.md)
- [Open Ontologies — GitHub Repository (Rust MCP Server)](../examples/open-ontologies-github.md)
- [Open Ontologies — Stable Matching Alignment Paper](../examples/open-ontologies-paper.md)
- [OpenAI Codex Agent Skills — Structured Skill System](../examples/openai-codex-skills.md)
- [OpenClaw PKB Skill](../examples/openclaw-pkb-skill.md)
- [RDF Ontologies Skill — SHACL + SPARQL Integration](../examples/rdf-ontologies-skill.md)
- [Schimatos — SHACL-based Knowledge Graph Editor](../examples/schimatos-shacl-knowledge-graph.md)
- [Current State of Skill Bundles Research (May 2026)](../examples/skill-bundles-research-state.md)
- [Tool-Use Firewall](../examples/tool-use-firewall.md)
- [Veto — Authorization Kernel for AI Agents](../examples/veto-agent-authorization.md)
- [VS Code Copilot Agent Skills — Cross-Platform Standard](../examples/vscode-copilot-skills.md)
