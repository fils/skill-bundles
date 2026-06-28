# The Agent Skills Ecosystem in 2026: Who's Building, What's Working, and What's Next

**Source:** https://agentman.ai/blog/agent-skills-ecosystem-report-2026
**Date:** June 2026

---

## 1. Executive Summary
In less than nine months, **Agent Skills** transitioned from a proprietary Anthropic feature to a cross-vendor open standard. While the ecosystem boasts millions of skills and support from ~40 major platforms, the market is currently defined by a sharp divide between **high-volume, low-quality public catalogs** and **high-value, curated enterprise libraries**.

---

## 2. Key Facts & Figures (June 2026)
- **Standardization:** Anthropic launched Agent Skills in Oct 2025; published as an open standard at `agentskills.io` on Dec 18, 2025.
- **Adoption:** ~40 compatible products including OpenAI Codex, GitHub Copilot, Cursor, Gemini CLI, and VS Code.
- **Scale:** SkillsMP indexes **1.9 million** public skills scraped from GitHub.
- **Quality Gap:** SkillsBench found the average quality score of public skills is **6.2/12**.
- **Performance Impact:** Curated skills increase agent pass rates by **16.2 percentage points** (up to 51.9 points in healthcare).
- **Security Risk:** 36% of skills tested by Snyk contained **prompt injections**; an audit of 22k skills found ~141k total issues.

---

## 3. Technical Architecture: The SKILL.md Standard
The ecosystem is built on **SKILL.md** packages—folders containing instructions, scripts, and resources.

> "MCP gave agents hands. Skills give them judgment. The reason this ecosystem exploded in nine months isn't the format — it's that a skill written once now runs in Claude, Codex, Cursor, and a dozen other tools without a rewrite." — Prasad Thammineni, CEO, Agentman

### Progressive Disclosure
To minimize context costs, agents use a "progressive disclosure" model:
1. **Pre-load:** Agent only loads the skill's **name** and **description**.
2. **Execution:** Full instructions are loaded only when a task matches the description.

---

## 4. The Directory Landscape
| Directory | Catalog Size | Curation / Security |
|:---|:---|:---|
| **Anthropic Official** | Small | Manually curated & verified |
| **Skills.sh** | 100,000s | Open, npm-style CLI install |
| **SkillsMP** | ~1.9 Million | Scraped; no security review |
| **Agensi** | Small | 8-point security scan |
| **Agentman** | 90 Skills | Practitioner-authored; production-ready |

---

## 5. Growth by Category
While engineering dominates by volume, business and regulated domains show the highest value-add.

- **Development & Engineering:** 288,811 skills
- **Product Management:** 86,948 skills
- **Marketing:** 74,510 skills
- **Healthcare & Life Sciences:** 6,354 skills (Highest performance gains)

---

## 6. Critical Challenges: Quality & Security
The "catch" to the rapid growth of the ecosystem is the lack of vetting.
- **Bloat vs. Focus:** 2–3 targeted skills improved performance by **18.6 points**, whereas monolithic "all-in-one" skills actually **reduced performance by 2.9 points**.
- **Security:** Skills execute bundled scripts. An unaudited skill is an unaudited dependency with code-execution rights.
- **Rule of Thumb:** Treat community skills like open-source packages; review source code before installation.

---

## 7. Future Outlook (H2 2026)
1. **Trust Infrastructure:** Security scanning will become mandatory for enterprise adoption.
2. **Governance Scrutiny:** Neutral stewardship of the `agentskills.io` standard will be a priority for the Agentic AI Foundation.
3. **Vertical Depth:** Value is shifting from generic horizontal skills to deep, domain-specific procedures (Legal, Finance, Healthcare).
4. **Management Tools:** Enterprise focus on version control, audit trails, and centralized provisioning.

---

## 8. About Agentman
Agentman focuses on the **top-quartile** of skill quality.
- **Library:** 90 production-ready skills with named inputs, typed outputs, and full revision history.
- **Agent Builder:** A no-code platform to assemble skills into working agents.
- **Medman:** A real-world application for medical practices.
  - *Example:* Eligibility verification agent runs at **$0.50/check** vs. the **$6.72** industry benchmark.
