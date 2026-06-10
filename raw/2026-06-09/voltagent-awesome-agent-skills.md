# VoltAgent Awesome Agent Skills (Curated Catalog)

**Source:** https://github.com/VoltAgent/awesome-agent-skills
**Date Retrieved:** 2026-06-09
**Type:** GitHub Repository - Curated Catalog/Aggregation of 1,400+ Skills

---

## Summary

**Awesome Agent Skills** is a curated collection of **over 1,000 real-world Agent Skills** created by official engineering teams (Anthropic, Google, Microsoft, Stripe, etc.) and the community. Unlike mass AI-generated repositories, this collection focuses on hand-picked, proven skills for AI coding assistants.

This is a **catalog/registry type skill bundle** — it aggregates skills from many sources with quality standards, categorization, and cross-platform installation paths.

---

## Scale & Stats

- **24.7k+ Stars** | **2.7k+ Forks** | **1,400+ Skills**
- Focus: **Quality over Quantity** — "Please don't submit skills you created 3 hours ago"

---

## Cross-Platform Installation Paths (Standardized)

| Tool | Project Path | Global Path |
|------|--------------|-------------|
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| **Gemini CLI** | `.gemini/skills/` | `~/.gemini/skills/` |
| **Codex** | `.agents/skills/` | `~/.agents/skills/` |

This standardization is a **key context element** — a **mapping/registry** of where skills live per platform.

---

## Official Skills by Major Teams (Context Elements: Provenance + Categorization)

### Anthropic (Claude) — `officialskills.sh/anthropics`
- **Document Handling:** Skills for creating/editing `.docx`, `.pptx`, `.xlsx`, `.pdf`
- **Development:** `webapp-testing` (Playwright), `mcp-builder` (creating MCP servers), `web-artifacts-builder` (React/Tailwind)
- **Design:** `frontend-design`, `algorithmic-art` (p5.js), `theme-factory`

### Microsoft — `officialskills.sh/microsoft` (133 skills)
- **Azure Services:** AI Foundry, Cosmos DB, KeyVault, EventHub, Speech-to-Text
- **Core Patterns:** `cloud-solution-architect`, `continual-learning`

### Google (Gemini & Cloud) — `officialskills.sh/google-gemini`
- **Gemini API:** `gemini-live-api-dev` (streaming), `vertex-ai-api-dev`
- **Google Workspace:** CLI-based management for Drive, Sheets, Gmail, Calendar, Docs
- **Cloud Infrastructure:** `gke-basics`, `bigquery-basics`, `cloud-run-basics`

### NVIDIA — `github.com/NVIDIA/skills` (155 skills)
- **Frameworks:** Megatron-Core, NeMo-RL, TensorRT-LLM
- **Optimization:** `perf-memory-tuning`, `cuda-graphs`, `kernel-triton-writing`

### Sentry — `officialskills.sh/getsentry`
- **Workflow:** `sentry-fix-issues` (stack traces/breadcrumbs), `sentry-setup-ai-monitoring`
- **SDKs:** Platform-specific setup for 20+ languages/frameworks

---

## Specialized Domain Skills (Categorization Taxonomy)

### Product & Project Management
- **Dean Peters** (46 skills): `opportunity-solution-tree`, `jobs-to-be-done`, `tam-sam-som-calculator`
- **Paweł Huryn** (65 skills): Full PM lifecycle, `ab-test-analysis`, `outcome-roadmap`
- **Garry Tan (gstack)** (28 skills): Virtual engineering team simulation, `office-hours`, `plan-ceo-review`

### Marketing & SEO
- **Corey Haines:** Full SaaS marketing stack (SEO, Copywriting, Churn Prevention)
- **Addy Osmani:** Web quality audits for Performance, Accessibility, Core Web Vitals
- **Kim Barrett:** Direct-response advertising, `headline-matrix` generation

### Security & Web3
- **Trail of Bits:** `variant-analysis`, `semgrep-rule-creator`, `smart-contract-security`
- **Binance:** `crypto-market-rank`, `query-token-audit`, `spot-trading` via API
- **Coinbase:** `send-usdc`, `onchain-data-query`, `x402` payment protocols

---

## Quality Standards (Governance Artifacts)

### Skill Quality Criteria
- **Description:** Third-person, specific keywords (e.g., "PostgreSQL migration")
- **Progressive Disclosure:** Metadata < 100 tokens; body < 500 lines
- **No Absolute Paths:** Use relative paths or `$HOME`
- **Scoped Tools:** Declare explicit tool dependencies; avoid `*`

### Security Notice (Risk Artifact)
> "Skills in this list are curated, not audited... Agent skills can include prompt injections, tool poisoning, hidden malware payloads, or unsafe data handling patterns."

**Recommended Security Tools:**
- [Snyk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)

---

## Contributing Guidelines (Process Artifact)

- **Guideline:** "Please don't submit skills you created 3 hours ago."
- **Focus:** Community-adopted, proven skills published by established development teams.
- **Quality over Quantity** — explicit curation philosophy

---

## Composition Notes

This catalog demonstrates **registry/catalog patterns** for skill bundles:

1. **Provenance tracking**: Every skill attributed to author/organization
2. **Categorization taxonomy**: Domain-based organization (PM, Marketing, Security, etc.)
3. **Cross-platform path mapping**: Standard installation locations per agent runtime
4. **Quality gates**: Explicit criteria (description format, progressive disclosure, path hygiene, tool scoping)
5. **Security warnings**: Explicit risk articulation + recommended scanning tools
6. **Curation process**: Human-in-the-loop quality filter, not automated aggregation
7. **Official vs Community distinction**: Separate sections for major-team skills vs individual creators

---

## Key Quotes

> "Awesome Agent Skills is a curated collection of over 1,000 real-world Agent Skills created by official engineering teams (Anthropic, Google, Microsoft, Stripe, etc.) and the community. Unlike mass AI-generated repositories, this collection focuses on hand-picked, proven skills for AI coding assistants."

> "**Quality over Quantity.** Please don't submit skills you created 3 hours ago."

> "**Security Notice:** Skills in this list are curated, not audited... Agent skills can include prompt injections, tool poisoning, hidden malware payloads, or unsafe data handling patterns."

> "Skill Quality Criteria:
> - Description: Third-person, specific keywords
> - Progressive Disclosure: Metadata < 100 tokens; body < 500 lines
> - No Absolute Paths: Use relative paths or $HOME
> - Scoped Tools: Declare explicit tool dependencies; avoid *"

---

## Relevance to Skill Bundle Research

This catalog is a **meta-bundle** — a bundle of bundles. It provides:
- **Taxonomy** for categorizing skills by domain
- **Provenance model** for tracking skill origin
- **Quality framework** for evaluating bundle members
- **Security model** for risk assessment
- **Cross-platform mapping** for deployment
- **Curation methodology** for maintaining quality at scale