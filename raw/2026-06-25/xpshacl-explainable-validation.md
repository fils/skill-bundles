# xpSHACL: Explainable SHACL Validation using Retrieval-Augmented Generation and LLMs

**Source:** https://arxiv.org/html/2507.08432v1 (arXiv)  
**Ingested:** 2026-06-25

## Key Ideas
- xpSHACL combines rule-based justification trees with RAG + LLMs (OpenAI, Gemini, Claude, Ollama) to produce human-readable explanations for SHACL constraint violations.
- Supports multiple LLM backends; tested on LOV ontologies.
- Python implementation using pyshacl, openai, etc.
- Provides actionable correction suggestions tailored to violation type.

## Relevance to Skill Bundles
Strong example of SHACL validation skill bundled with LLM/RAG explanation skills. Shows how SHACL shapes + LLM explanation forms a reusable bundle for explainable validation in agent workflows. Open source code available.