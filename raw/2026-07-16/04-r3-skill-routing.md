# R3-Skill: Query-Conditional Skill Routing & Compatibility

**Source:** https://arxiv.org/abs/2606.03565 | https://github.com/Tencent/R3-Skill
**Models:** https://huggingface.co/tencent/R3-embedding-0.6b , R3-rerank-0.6b
**Date:** Jun–Jul 2026 (v4) | Tencent IMA / Youtu Lab
**Signal rating:** 9/10

## Key ideas
- Skill retrieval ≠ document retrieval: top-K success depends on **skill compatibility under a query**, not independent relevance.
- **Reject-as-Resource (R3):** use LLM rejection decisions (which skills should *not* co-retrieve) as compatibility supervision — normally discarded.
- Benchmark R3-Skill: 10,246 skills, 8 super-domains, 41,592 accepted queries, 32,828 rejected annotations, 8-class rejection taxonomy; bilingual CN/EN; expert-verified test set.
- Two-stage retriever: R3-Embedding + R3-Reranker; Hit@1=0.7521, NDCG@10=0.8173, Set-Compat=0.3188.
- Motivation: full library ≈21.2M tokens; body (not description) carries routing signal; sandbox cold-start requires K-skill install only.

## Why skill-bundles
First formal treatment of **composition-aware skill retrieval** as a context element — bridges SkillCraft/GoS dependency retrieval and SkillsBench negative-delta findings.
