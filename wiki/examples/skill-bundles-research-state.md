# Current State of Skill Bundles Research (May 2026)

**Date:** 2026-05-23  
**Iteration:** 5

## Summary After 5 Iterations

After running five daily research cycles, the following picture has emerged:

### Strongest Areas
- **Ontology + Skills**: Clear examples exist (Ontologizer, OpenClaw PKB)
- **Rules & Governance**: Good signals from Veto and Tool-Use Firewall
- **Declarative Context**: Most mature bundles pair skills with markdown plans and configuration files

### Weakest Areas
- **SHACL Validation**: Only one partial example (Schimatos). No clear "skill + SHACL" bundles found.
- **SSSOM Mapping**: Zero relevant examples discovered.
- **Formal Rules + Skills**: Still mostly middleware rather than integrated bundles.

## Key Insight

Current agent skill ecosystems appear to be adopting **governance and ontology layers** faster than formal semantic validation (SHACL) or mapping standards (SSSOM). This may be because rules and ontologies are easier to integrate into existing agent runtimes (Claude Code, OpenClaw, etc.) than full semantic web technologies.

## Recommended Next Research Directions
- Focus on academic papers about "verified tool use" or "safe agent architectures"
- Investigate whether any major agent frameworks have internal validation layers that could be exposed as skills
- Explore the intersection of skill bundles and Model Context Protocol (MCP) governance tools

This document serves as a living snapshot of the research state.