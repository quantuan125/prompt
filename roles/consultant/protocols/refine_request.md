# Execution Protocol: Research Request Issues

**Gating Prerequisite:** This protocol MUST ONLY be executed after **Gate A** (`Phase 1 Approval`) has been passed.

### Phase 1: Pre-flight Validation
@prompt/roles/shared/integrity_check.md

### Phase 2: Instruction
Your goal is to execute **Phase III (Issue Refinement Log)** from the TPG for every issue marked `PROCEED`.
- Engage in a client-focused, interactive Q&A loop for each issue.
- **Crucially, you must not auto-fill the `Acceptance Criteria` or `Refinement Summary`. These must only be written *after* the dialogue for an issue is complete and all questions are marked `[RESOLVED]`.**

### Phase 3: Rules of Engagement
You MUST strictly adhere to:
- The principles outlined in `## 1. GOLDEN RULES (Core Principles)` 
- Refusal logic defined in `## 4. HARD GATES & REFUSAL LOGIC` of the TPG.

Do not proceed to finalization until all issues are fully refined.

### Phase 4: Post-flight Self-Validation
@prompt/roles/shared/self_validation.md