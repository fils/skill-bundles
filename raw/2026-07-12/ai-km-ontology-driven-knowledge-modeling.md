# AI-KM: Agent Skills and Ontology-Driven Knowledge Modeling

**Source:** https://www.sciencedirect.com/science/article/pii/S235271102600347X
**Date:** 2026-07-12
**Journal:** SoftwareX, Volume 35, September 2026, 102855
**Authors:** Haolin Wen, Songyi Wang, Bingjie Li, Junfen Xiong, Tong Chen, Xin Liang
**DOI:** https://doi.org/10.1016/j.softx.2026.102855
**Signal:** 8/10
**License:** Open Access

## Abstract (v6.6.1 Software Update)

This update introduces two significant capabilities:

### 1. Agentic Skill Framework
- Encapsulates complex AI behaviors as **reusable, conversation-invokable skills**
- Supports both:
  - **Predefined expert skills** — manually authored skill definitions
  - **Autonomous planning mode** — for novel tasks where no predefined skill exists
- Skills are invoked through conversation, making them accessible to domain experts

### 2. Ontology-Driven Knowledge Modeling
- Elevates knowledge representation from simple slice structures to **formal, machine-interpretable ontologies**
- Built through **natural language entity extraction**
- Domain experts encode expertise as both:
  - **Executable skills** (dynamic process)
  - **Structured knowledge** (formal ontology)

### Closed Loop Design
Knowledge is represented as formal structure and applied as dynamic process, creating a **closed loop**:
1. Knowledge → Ontology (formal representation)
2. Ontology → Skills (executable behavior)
3. Skills → Knowledge (feedback from execution)

## Relevance to Skill Bundles

AI-KM is a rare example of **skills + ontologies** in a single integrated system:
1. **Skills + ontology integration** — directly addresses the skill bundle thesis (skills bundled with formal context artifacts)
2. **Conversation-invokable skills** — skills as conversational primitives, not just CLI/file-based
3. **Autonomous planning mode** — system generates skills for novel tasks where no predefined skill exists
4. **Natural language → ontology** — entity extraction builds the ontology from NL input, lowering the barrier to formal knowledge modeling
5. **Closed-loop design** — knowledge → skills → knowledge feedback cycle

This is a concrete implementation of the "skills bundled with ontologies" pattern from the skill bundle taxonomy.

## Key Quotes

> "Encapsulates complex AI behaviors as reusable, conversation-invokable skills, supporting both predefined expert skills and an autonomous planning mode for novel tasks"

> "Elevates knowledge representation from simple slice structures to formal, machine-interpretable ontologies built through natural language entity extraction"

> "Creating a closed loop where knowledge is represented as formal structure and applied as dynamic process"

## Links
- Article: https://www.sciencedirect.com/science/article/pii/S235271102600347X
- DOI: https://doi.org/10.1016/j.softx.2026.102855
- Previous version: https://doi.org/10.1016/j.softx.2024.101840
