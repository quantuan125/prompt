# Communication Brief: T810A RID Renumbering Task

**To**: LLM_Developer
**From**: LLM_Consultant
**Date**: 2025-10-23
**Subject**: Final RID Numbering for Epic T810A Migration Plan
**Priority**: High (Blocks Phase 3 GDR Alignment)

---

## Context

We've completed comprehensive F-RID → E-RID migration consultations for Epic T810A (Gastroenterologist Agent System) across all requirement categories:

- ✅ Assumptions (4 Epic + 1 Feature)
- ✅ Dependencies (5 Epic + 1 Feature)
- ✅ Constraints (4 Epic + 3 Feature + 1 reclassified to QG)
- ✅ Quality Goals (8 Epic + 5 Feature)
- ✅ Implementation Guidance (6 Epic NEW)

During this process, we used **placeholder IDs** (QG-XXX, NFR-XXX) for two requirements created via hybrid splits and reclassifications. These need final sequential numbering before proceeding to Phase 3 (Epic GDR Alignment).

---

## Problem Statement

**Placeholder IDs requiring final numbering**:

1. **`T810A-QG-XXX` (Clarification Over Guessing)**
   - **Origin**: Created from CON-004 (No-Guessing Principle) reclassification — hybrid split Epic QG + Feature NFR
   - **Status**: Epic-level Quality Goal principle (clarification mechanisms over guessing when data insufficient)
   - **Current references**: IG-002, GDR-001, T810A1-NFR-XXX
   - **Proposed final ID**: `T810A-QG-008` (sequential after QG-007 Confidence Communication)

2. **`T810A1-NFR-XXX` (Probe-Before-Answer Enforcement)**
   - **Origin**: Created from CON-004 hybrid split — Feature-level implementation of QG-XXX
   - **Status**: T810A1-specific NFR (≥2 questions minimum before guidance)
   - **Current references**: IG-002, T810A1-NFR-001
   - **Proposed final ID**: `T810A1-NFR-009` (sequential; original NFR-009 was superseded by this new one)

---

## Task Requirements

**File to Update**:
```
prompt/artifacts/tasks/T810/consultant/workspace/plan/T810A/epic_T810A_population_plan.md
```

**Specific Actions**:

### 1. **Global Search & Replace**
Replace ALL occurrences of placeholder IDs throughout the plan file:
- `T810A-QG-XXX` → `T810A-QG-008`
- `T810A1-NFR-XXX` → `T810A1-NFR-009`

Ensure replacements occur in:
- Section 2.3 (Constraints) — CON-004 hybrid analysis
- Section 2.4 (Quality Goals) — QG summary tables
- Section 2.5 (Implementation Guidance) — IG-002 references
- Any cross-reference notes throughout document

### 2. **Update Section "## 2. Promotion Candidates (Feature → Epic)"**

Locate and update the promotion summary table to reflect final IDs:

**Before** (current state with placeholders):
```markdown
## 2. Promotion Candidates (Feature → Epic)
...
- QG-XXX (Clarification Over Guessing) — created from CON-004 reclassification
- T810A1-NFR-XXX (Probe-Before-Answer Enforcement) — created from CON-004 hybrid
```

**After** (with final IDs):
```markdown
## 2. Promotion Candidates (Feature → Epic)
...
- QG-008 (Clarification Over Guessing) — created from CON-004 reclassification
- T810A1-NFR-009 (Probe-Before-Answer Enforcement) — created from CON-004 hybrid
```

### 3. **Verification Checklist**

After updates, verify:
- [ ] No instances of "XXX" placeholder remain in plan file
- [ ] All cross-references to QG-008 and NFR-009 are consistent
- [ ] Section 2 promotion summary table uses final IDs
- [ ] Section 2.3 (Constraints) CON-004 hybrid section uses final IDs
- [ ] Section 2.4 (Quality Goals) summary uses final IDs
- [ ] Section 2.5 (Implementation Guidance) IG-002 content uses final IDs

---

## Deliverable

**Updated file**: `epic_T810A_population_plan.md` with:
1. All placeholder IDs replaced with final sequential numbers
2. Section 2 (Promotion Candidates) updated with final ID references
3. Consistent cross-referencing throughout document

**Expected completion**: Before LLM_Consultant proceeds to Phase 3 (Epic GDR Alignment) consultation.

---

## Additional Notes

**Why Sequential Numbering**:
- Per T102-STD-005 governance standards, RIDs use sequential numbering within categories
- QG-008 follows QG-007 (Confidence Communication) naturally
- NFR-009 is logical as it superseded the original T810A1-NFR-009 (Probe Phase Enforcement) which was replaced by this hybrid split

**No Content Changes Required**:
- This is purely an ID renumbering task
- Content of QG-008 and NFR-009 remains as drafted
- Only ID strings and references need updating

---

## Questions or Blockers

If any ambiguities arise during renumbering, escalate to LLM_Consultant before proceeding.

**Contact**: This consultation session (T810A Epic Migration)

---

**End of Brief**
