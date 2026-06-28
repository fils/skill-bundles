# Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis

**Source:** https://arxiv.org/html/2604.02837v1
**Date:** April 2026

---

## 1. Executive Summary
This paper presents the first comprehensive security analysis of **Agent Skills**, a modular, filesystem-based packaging format for LLM-based agents (introduced by Anthropic in 2025). While Skills offer flexibility by allowing natural-language instructions and local code execution, they introduce structural vulnerabilities that differ from prior mechanisms like ChatGPT Plugins or the Model Context Protocol (MCP). The analysis identifies a massive attack surface across the Skill lifecycle, validated by real-world incidents involving ransomware and large-scale credential theft.

---

## 2. Architectural Overview & Comparison
Agent Skills represent a shift toward "natural language authorship," lowering the barrier to entry but increasing security risks.

### Key Architectural Components
- **Package Structure:** A directory containing a required `SKILL.md` (YAML frontmatter + Markdown instructions), optional executable scripts (Python, Bash, JS), and reference assets.
- **Progressive Disclosure Model:**
  - **Level 1:** Metadata (name/description) loaded into the system prompt.
  - **Level 2:** Full `SKILL.md` instructions loaded if the agent deems them relevant.
  - **Level 3:** Supplementary files or script outputs loaded on demand.
- **Trust Model:** Grants **operator-level authority** upon a single installation. This creates a "consent gap" where persistent, undifferentiated permissions are granted without per-action confirmation.

### Comparison Table (Excerpts)
| Dimension | ChatGPT Plugins | MCP | Agent Skills |
|:---|:---|:---|:---|
| **Data/Instruction Boundary** | Mitigated (Typed) | Partially Exposed | **Critically Exposed** |
| **Execution Locus** | Remote Server | Local/Remote | **Local (User Privileges)** |
| **Marketplace Review** | Mandatory | None | **None** |
| **Authorship Complexity** | High | Medium | **Low (Natural Language)** |

---

## 3. The Agent Skill Lifecycle & Attack Surface
The paper decomposes the Skill lifecycle into four phases, each introducing specific risks:
1. **Creation:** Malicious authors can hide adversarial directives in natural language that static analysis cannot detect.
2. **Distribution:** Open marketplaces without vetting allow for typosquatting and ranking manipulation.
3. **Deployment:** The "Consent Gap"—users approve a Skill based on a benign description, but grant persistent, irrevocable authority.
4. **Execution:** The agent interprets instructions at the operator level; bundled scripts execute outside the context window, making their actions invisible to the LLM.

---

## 4. Threat Taxonomy
The authors identify **7 categories** and **17 scenarios** across three attack layers.

### Layer 1: Delivery and Trust Establishment
- **T1: Supply Chain Compromise:** Typosquatting, ranking manipulation, and "Hallucinated Packages" (claiming non-existent packages referenced by AI-generated code).
- **T2: Consent Abuse:** Exploiting the persistent trust model and modifying Skill content *after* installation to inherit original approvals.

### Layer 2: Runtime Attacks
- **T3: Prompt Injection:**
  - *Direct:* Malicious instructions in `SKILL.md`.
  - *Indirect:* Skill fetches external content (e.g., a web page) containing adversarial instructions.
- **T4: Code Execution:**
  - *Malicious Scripts:* Bundled scripts running ransomware.
  - *Deferred Dependency:* Using unpinned dependencies (e.g., via Python PEP 723) to inject payloads later.
- **T5: Data Exfiltration:** Harvesting credentials, environment variables, or entire codebases silently.

### Layer 3: Persistent and Lateral Impact
- **T6: Persistence:** Poisoning agent memory files (`MEMORY.md`, `SOUL.md`) or configuration files (`settings.json`) to create backdoors.
- **T7: Multi-Agent Propagation:** "Prompt Infection" where a compromised agent replicates adversarial instructions to downstream agents.

---

## 5. Real-World Incident Analysis
The taxonomy is validated by five major security events:

| Incident | Threat Mapping | Impact |
|:---|:---|:---|
| **MedusaLocker** | T4.1, T2.1 | A "GIF converter" Skill executed ransomware via a bundled script. |
| **ClawHavoc Campaign** | T5.1, T1.1, T1.2 | 1,184 malicious Skills used typosquatting to steal API keys and crypto wallets. |
| **CVE-2025-59536** | T5.1, T6.2 | RCE and API key theft via malicious `.claude/settings.json` hooks. |
| **SafeDep PEP 723** | T4.2 | Demonstrated how unpinned dependencies allow runtime payload injection. |
| **Mitiga Silent Egress** | T5.3, T1.2 | A Skill exfiltrated a full codebase in 4 steps while leaving audit logs empty. |

> **Key Quote:** *"The ransomware was delivered and executed entirely outside the agent's reasoning process... the agent had no visibility into what the script was doing before acting on its output."*

---

## 6. Defense Directions & Research Agenda
The paper outlines a multi-layered defense strategy:

1. **Static Analysis & Sandboxing:** Isolate skill execution in containers or VMs; use static analysis to detect malicious patterns.
2. **Runtime Monitoring:** Implement real-time monitoring of skill behavior, including network calls and file system access.
3. **Supply Chain Security:** Adopt cryptographic signing (e.g., SLSA provenance), pin dependencies, and implement reputation systems.
4. **Consent Reform:** Move from persistent, blanket permissions to granular, per-action consent with user-friendly permission prompts.
5. **Memory Sanitization:** Treat agent memory files (`MEMORY.md`, `SOUL.md`) as untrusted inputs; sanitize and validate before use.

---

## 7. Implications for Skill Bundle Research
This paper is directly relevant to the skill bundles research agenda because:
- **Security as a Context Element:** The 7-category threat taxonomy is itself a formal context artifact that should be bundled with skill collections.
- **Validation Layer Parallels:** The paper's defense directions (static analysis, runtime monitoring, supply chain security) map directly to the SHACL validation / SSSOM mapping patterns documented in this wiki.
- **Lifecycle Alignment:** The four-phase lifecycle (Creation, Distribution, Deployment, Execution) aligns with the PLAN.md's emphasis on tracking the full lifecycle of skill bundles.
