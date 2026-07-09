# NVIDIA/skills (2026-07-09)

**Source:** https://github.com/nvidia/skills (2.4k stars, 403 commits, active Jul 8 2026)

**Key Ideas:**
- Official NVIDIA-verified AI agent skills for CUDA-X, AI Blueprints, cuOpt, NeMoClaw, Dynamo, Physical AI, Omniverse.
- Bundled as .agents/plugins + .claude-plugin with skills.sh.json and metadata.json.
- Recent: chore(metadata) regenerate + broaden nvidia-skills plugin from cuOpt-only to full ecosystem.

**Context Elements:**
- SHACL validation implied in plugin manifests.
- Structured skill bundles with progressive disclosure.

**Composition Notes:**
- Skills + plugin manifests + validation metadata = production-grade NVIDIA skill bundle.
- High reproducibility via npx skills add.

**Signal:** 9/10 — direct high-signal example of vendor-curated skill bundle with formal context.