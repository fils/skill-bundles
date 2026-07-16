#!/usr/bin/env python3
"""Insert 2026-07-16 run notes into wiki/metrics.md if missing."""
from pathlib import Path

p = Path("wiki/metrics.md")
text = p.read_text()
if "2026-07-16 Run Notes" in text:
    print("already present")
    raise SystemExit(0)

marker = "| Cognitive Artifacts Framework | New (Externalization four-form taxonomy) |"
idx = text.find(marker)
if idx < 0:
    print("marker not found")
    raise SystemExit(1)

# find end of that line
line_end = text.find("\n", idx)
after = text[line_end + 1 :]
# expect blank line then ## 2026-07-15
insert_block = """
| Native Multi-Harness Evaluation Protocol | New (WildClawBench OpenClaw/Claude Code/Codex/Hermes) |
| Skill Internalization Dynamic Curriculum | New (SKILL0 on-policy helpfulness annealing) |
| Collective Skill Tree Search + Transfer Scoring | New (CSTS CSN-Gen/CSN-Assess) |
| Skill Compatibility / Reject-as-Resource | New (R3-Skill Set-Compat routing) |
| ASSC SkillBOM Multi-Channel Deps | New (skill/package/service graphs + lockfiles) |
| One-Time Copy Reuse Model | New (Registry→Repository maintenance science) |
| SE Activity→Skill Lifecycle Mapping | New (Inside the Skill Market) |

## 2026-07-16 Run Notes (Iteration 41)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-16/` (created today). Last commit 2026-07-15 (0b9b792). Digests current through 2026-07-15. No leftover uncommitted raw.
- Anti-stagnation: Followed 2026-07-15 priority list (WildClawBench first hit) + diversified into Jul-2026 arXiv (ASSCs, Registry→Repository, SE market) + SKILL0 internalization + CSTS + R3-Skill. All 7 sources novel (none in prior week digests). Theme: evaluation + internalization + supply-chain inventory + maintenance science.
- Phase 1: **7 sources** — WildClawBench, SKILL0, OpenClaw-Skill CSTS, R3-Skill, ASSCs, Registry→Repository, Inside Skill Market. All novel.
- Phase 2: 7 new example articles + daily digest.
- Phase 3: index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A + lint pass.
- Phase 5: Unconditional git commit + push.
- Daily sources: 7 | New examples: 7 | Papers: 0 | Updated: 0 | New patterns: 6 | New context elements: 7
"""
# Keep one blank line before next section
new_text = text[: line_end + 1] + insert_block + after
# avoid double blank if after already starts with \n
while "\n\n\n\n" in new_text:
    new_text = new_text.replace("\n\n\n\n", "\n\n\n")
p.write_text(new_text)
print("metrics updated")
print("has 07-16", "2026-07-16 Run Notes" in new_text)
print("has 07-15", "2026-07-15 Run Notes" in new_text)
