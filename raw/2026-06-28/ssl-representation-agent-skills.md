# From Skill Text to Skill Structure: The Scheduling-Structural-Logical (SSL) Representation

**Source:** https://arxiv.org/html/2604.24026v1
**Date:** April 2026
**Authors:** Qiliang Liang, Hansi Wang, Zhong Liang, Yang Liu (Peking University)

---

## 1. Executive Summary
Current Large Language Model (LLM) agent systems represent "skills" (bundles of instructions, tools, and control flows) as text-heavy artifacts (e.g., `SKILL.md`). This creates a bottleneck for machine reasoning, as invocation interfaces, execution structures, and side effects are entangled in unstructured text.

This paper introduces the **Scheduling-Structural-Logical (SSL)** representation—the first structured representation for agent skills. SSL disentangles skill artifacts into a three-layer JSON graph, significantly improving performance in **Skill Discovery** (retrieval) and **Risk Assessment** (security).

---

## 2. The SSL Representation Framework
SSL draws on classical linguistic knowledge representation (Schank & Abelson) to map unstructured documents into a typed three-layer graph.

### The Three Layers
1. **Scheduling Layer (Skill-Level Interface):** Focuses on *when* to invoke. Captures goals, intent signatures, and coarse control-flow features.
2. **Structural Layer (Scene-Level Execution):** Focuses on *how* work is organized. Groups operations into "scenes" (e.g., Prepare, Acquire, Act, Verify).
3. **Logical Layer (Atomic Actions):** Focuses on *what* resources are used. Decomposes scenes into primitive actions (e.g., READ, CALL_TOOL) with explicit resource scopes (e.g., CREDENTIALS, NETWORK).

### Key Design Principles
- **Compact:** Preserves only evidence needed for management/use.
- **Typed:** Uses restricted vocabularies (enums) for comparability.
- **Grounded:** Summarizes only what is explicitly in the source; no hallucinated behavior.

---

## 3. Technical Implementation: The Normalizer
The authors developed an LLM-based normalizer to convert `SKILL.md` files into SSL schema via a four-pass pipeline:
1. **Skill Record Extraction:** Captures metadata and top-level patterns.
2. **Scene Decomposition:** Breaks the document into 2-5 macro-level scenes.
3. **Logic-Step Expansion:** Identifies atomic operations and resource boundaries.
4. **Verification:** Enforces structural well-formedness and identifier consistency.

### Restricted Vocabularies (Excerpts)
| Category | Allowed Values |
|:---|:---|
| **Scene Types** | PREPARE, ACQUIRE, REASON, ACT, VERIFY, RECOVER, FINALIZE |
| **Logical Primitives** | READ, SELECT, COMPARE, VALIDATE, INFER, WRITE, CALL_TOOL, REQUEST, etc. |
| **Resource Scopes** | MEMORY, LOCAL_FS, CODEBASE, PROCESS, USER_DATA, CREDENTIALS, NETWORK |

---

## 4. Evaluation & Results

### Evaluation I: Skill Discovery (Retrieval)
**Task:** Match 403 user queries to the correct skill in a registry of 6,184 candidates.
- **Baseline (Description only):** 0.573 MRR
- **SSL-Rich (Description + SSL):** **0.707 MRR**
- **Insight:** Concise structured summaries are more effective retrieval interfaces than raw, long-form documentation.

### Evaluation II: Risk Assessment (Security)
**Task:** Identify risks (data exfiltration, privilege escalation, etc.) in 500 skills.
- **Baseline (Full SKILL.md):** 0.744 Macro F1
- **Full SKILL.md + SSL:** **0.787 Macro F1**
- **Insight:** SSL makes operational risks (like credential access) salient, but works best *alongside* the original `SKILL.md` to provide context for severity.

---

## 5. Key Excerpts & Code Snippets

### SSL Schema Formulation
> "SSL maps an unstructured skill document into a typed representation: G_d = (r_sch, G_str, G_log, R_cont, R_entry)"

### Example SSL Logic Step (JSON)
```json
{
  "logic_step_id": "L_READ_GUIDE",
  "act_type": "READ",
  "input_args": ["$guide_file_path"],
  "output_binding": "$loaded_guidelines",
  "actor": "skill",
  "object": "style_guide_file",
  "instrument": "filesystem.read",
  "resource_scope": "LOCAL_FS",
  "resource_target": "$guide_file_path",
  "next_step_rules": [
    {"condition": "success", "target": "YIELD_SUCCESS"},
    {"condition": "default", "target": "YIELD_FAIL"}
  ]
}
```

---

## 6. Actionable Insights for Developers
- **Don't Replace, Augment:** SSL is an "evidence interface." Use it to index and flag skills, but keep the original `SKILL.md` for nuanced human/agent interpretation.
- **Standardize Resource Scopes:** By tagging skills with specific scopes (e.g., `NETWORK`, `CREDENTIALS`), systems can implement automated policy checks before an agent executes a skill.
- **Improve Discovery:** Adding `intent_signature` and `scene_goal` fields to skill metadata significantly boosts the accuracy of skill routing in large-scale agentic systems.

---

## 7. Limitations
- **Static Analysis:** SSL cannot capture dynamic behaviors (e.g., payloads downloaded at runtime).
- **Generated Code:** SSL may understate risks if the skill *generates* malicious code rather than *performs* a malicious action directly.
