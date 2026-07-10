# Agent Skills: A Data-Driven Analysis of Claude Skills (arXiv:2602.08004)

**Source:** https://arxiv.org/abs/2602.08004  
**PDF:** https://arxiv.org/pdf/2602.08004  
**Authors:** George Ling, Shanshan Zhong, Richard Huang  
**Submitted:** 8 Feb 2026  
**Subjects:** cs.SE; cs.SI  
**Signal rating:** 9/10 (largest empirical marketplace analysis found this run)

## Abstract summary

Large-scale analysis of **40,285 publicly listed skills** from a major marketplace. Skills framed as reusable, program-like modules with triggering conditions, procedural logic, and tool interactions.

## Key findings

1. **Burst publication** — skill publication occurs in short bursts tracking community attention shifts
2. **Content concentration** — software engineering workflows dominate skill content; information retrieval + content creation drive substantial *adoption*
3. **Supply–demand imbalance** across categories
4. **Length distribution** heavy-tailed, but most skills remain within typical prompt budgets
5. **Ecosystem homogeneity** — widespread intent-level redundancy
6. **Safety risks** — non-trivial skills enable state-changing or system-level actions

## Implications for skill bundles

- Bundle design should fight homogeneity (unique composition + formal constraints)
- Marketplace scale (~40k) >> curated catalogs; need validation/governance layers
- Intent-level redundancy suggests need for mapping/taxonomies (SSSOM-like) across skill catalogs
- Safety finding aligns with workshop 37% flaw rate and prior OWASP AST10 / PurpleBox / Mondoo work in this wiki

## Composition notes

- Empirical infrastructure-layer framing matches catalog thesis: skills as emerging infrastructure requiring formal context artifacts
- Complements SkillsBench (+16.2pp curated) and security audits with marketplace-level statistics
