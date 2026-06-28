# Formal Analysis and Supply Chain Security for Agentic AI Skills

**Source:** https://arxiv.org/html/2603.00195v1
**Date:** February 27, 2026
**Key Focus:** Introducing **SkillFortify**, the first formal analysis framework for securing the agentic AI skill supply chain against malicious tools and privilege escalation.

---

## 1. Executive Summary
The rapid growth of agentic AI ecosystems (e.g., OpenClaw, Anthropic Agent Skills) has introduced a massive supply chain attack surface. In early 2026, the *ClawHavoc* campaign successfully infiltrated over 1,200 malicious skills into marketplaces. Existing security tools rely on heuristics that cannot guarantee safety.

**SkillFortify** addresses this gap by providing:
- **Formal Guarantees:** Sound static analysis and capability confinement.
- **High Performance:** 96.95% F1 score with 100% precision (0% false positives).
- **Scalability:** Resolves 1,000-node dependency graphs in <100ms.

---

## 2. The Threat Landscape (2026)
- **CVE-2026-25253:** The first CVE for an agentic AI system—a remote code execution (RCE) vulnerability in the OpenClaw runtime.
- **ClawHavoc Campaign:** Infiltrated 1,200+ malicious skills using the AMOS credential stealer.
- **MalTool Benchmark:** Cataloged 6,487 malicious tools; found that VirusTotal fails to detect the majority of agent-targeted malware.
- **Vulnerability Rate:** 26.1% of 42,447 analyzed agent skills exhibit at least one security vulnerability.

---

## 3. SkillFortify: Core Contributions

### A. DY-Skill Attacker Model
An adaptation of the Dolev-Yao model to the five-phase skill lifecycle: **Install -> Load -> Configure -> Execute -> Persist.**
> **Theorem 3.6 (DY-Skill Maximality):** Any symbolic attacker on the supply chain can be simulated by a DY-Skill trace.

### B. Static Analysis via Abstract Interpretation
SkillFortify uses a four-element capability lattice to prove a skill cannot exceed its declared permissions:
`{NONE <= READ <= WRITE <= ADMIN}`

- **Soundness Guarantee:** If the analysis reports a skill as safe, its concrete execution *cannot* access resources beyond declared capabilities.

### C. SAT-Based Dependency Resolution
Modern agents compose dozens of skills. SkillFortify models this as an **Agent Dependency Graph (ADG)** and uses a SAT solver (Glucose3) to ensure:
1. Version constraints are met.
2. No conflicting skills are co-installed.
3. **Security Bounds:** No skill in the chain exceeds the allowed capability set.

### D. Trust Score Algebra
A multi-signal system (Provenance, Behavioral, Community, Historical) that propagates trust through dependencies.
- **Monotonicity:** Positive evidence never reduces a trust score.
- **Exponential Decay:** Trust erodes for unmaintained skills (half-life of ~139 days).

---

## 4. Implementation & Performance

### Supported Formats
- **Claude Code Skills:** Markdown with YAML frontmatter.
- **Model Context Protocol (MCP):** JSON-RPC server configurations.
- **OpenClaw Skills:** YAML manifests.

### Key Metrics (SkillFortifyBench - 540 Skills)
| Metric | Result |
|:---|:---|
| **Precision** | 100% (Zero False Positives) |
| **Recall** | 94.07% |
| **F1 Score** | 96.95% |
| **Scan Speed** | 2.55ms per skill |
| **1k Node Resolution** | 92.4ms |

---

## 5. Actionable Artifacts

### The `skill-lock.json`
SkillFortify generates a deterministic lockfile to ensure reproducibility and integrity.
```json
{
  "skills": {
    "api-client": {
      "version": "3.0.1",
      "hash": "sha256:c5d6e7f8a9b0c1d2e3f4...",
      "capabilities": ["read_env", "net_access"],
      "trust_score": 0.68,
      "analysis": { "status": "clean", "max_severity": "NONE" }
    }
  },
  "integrity": "sha256:e7f8a9b0c1d2e3f4..."
}
```

### Agent Skill Bill of Materials (ASBOM)
Generates CycloneDX 1.6-compatible ASBOMs, allowing enterprises to integrate AI skill security into existing vulnerability management pipelines (e.g., Dependency-Track).

---

## 6. Limitations & Future Work
- **Relational Attacks:** Typosquatting and dependency confusion require external registry data for 100% detection.
- **Dynamic Behavior:** Static analysis cannot catch skills that fetch malicious payloads from remote servers *after* passing inspection.
- **Future Integration:** Plans for a **Skill Registry Verification Protocol** (cryptographic signing) and real-time IDE integration (VS Code/Cursor).

---

## 7. Conclusion
SkillFortify shifts the agent security paradigm from **heuristic scanning** ("we didn't find anything bad") to **formal verification** ("this skill is mathematically confined to these permissions"). It provides the necessary rigor for moving agentic AI from experimentation to enterprise production.

**Tool Availability:** [github.com/varun369/skillfortify](https://github.com/varun369/skillfortify)
