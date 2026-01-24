# Development Plan: Decoupled Versioning System for Documentation

**Version:** 2.1.0  
**Component:** prompt  
**Author:** LLM_Planner  
**Date:** 2025-07-15  
**Reason for Update:** Implementing Consultant Feedback - Resolving Versioning Ambiguity Issue  
**Estimated Effort:** Medium (~6 hours)

## Stakeholder Summary

### What We're Doing
Implementing a clear separation between software product versions and development artifact versions to eliminate confusion and enable proper iteration on planning documents without creating version conflicts.

### Why It Matters
The current system conflates artifact versions (like `plan_v2.0.1.md`) with product versions (like `tv_ingest v2.0.0`), making it impossible to iterate on plans without creating confusing version mismatches. This resolves the core versioning ambiguity identified in the consultation.

### Key Points
- **Timeline/Effort:** 6 dev hrs (~2 calendar days)
- **Risk Level:** Low - Documentation-only changes with clear rollback path
- **User Impact:** None - Internal process improvement only
- **Dependencies:** None - Self-contained documentation updates

---

## Technical Planning Document

### Executive Summary

This plan addresses the critical versioning ambiguity identified in consultation_prompt.md by implementing a decoupled versioning system that separates product/component versions from artifact versions. The solution introduces explicit target_version tracking for final products while allowing artifact iteration through a new naming convention and metadata structure.

The implementation focuses exclusively on documentation updates to establish clear standards, update templates with mandatory headers, and provide guidance for the new versioning approach without touching any programming files.

### Key Metrics
- **Files Modified:** 6 files across documentation and templates
- **New Components:** 0 new files/classes
- **Breaking Changes:** No - backward compatible documentation updates
- **Performance Impact:** None - documentation-only changes

## Pre-Planning Validation

### 1. Consultation Analysis ✓
- **Solutions Identified:** 
  - Decoupled versioning system separating product and artifact versions
  - Mandatory artifact headers with task context
  - Enhanced planning standards with structured file manifests
- **Conflicts Resolved:** None - all recommendations aligned with current architecture
- **Assumptions Verified:** Focus on documentation-only changes confirmed

### 2. Codebase Verification ✓
- **Components Affected:**
  - Primary: `prompt/documentation/prompt_main.md`
  - Secondary: `documentation/general.md`
  - Templates: All files in `prompt/templates/`
- **Pattern Compatibility:** Confirmed alignment with existing documentation patterns
- **Naming Standards:** Verified convention compliance with current structure

### 3. Feasibility Assessment ✓
- **Technical Feasibility:** Confirmed - straightforward documentation updates
- **Performance Analysis:** 
  - Current: No performance metrics applicable
  - Target: No performance impact expected
- **Breaking Changes:** None - maintains backward compatibility

### 4. Risk Analysis ✓
**Primary Risks:**
1. **Documentation Inconsistency:** Different interpretation of new standards → **Mitigation:** Provide clear examples and decision trees
2. **User Confusion:** Complex versioning rules → **Mitigation:** Start with simple examples and clear guidelines

## Compatibility Analysis

### Recommendation Mapping

**Consultant Recommendation 1:** Implement Decoupled Versioning System
- **Current State:** `prompt/documentation/prompt_main.md` lines 159-171 define current versioning rules
- **Proposed Change:** Add "Project Versioning Standards" section with clear separation
- **Pattern Match:** Similar to existing versioning documentation in `general.md`
- **Integration:** Connects via cross-references to existing workflow sections

**Consultant Recommendation 2:** Codify New Artifact Standards
- **Current State:** Templates in `prompt/templates/` use basic metadata blocks
- **Proposed Change:** Add mandatory artifact headers with task context
- **Pattern Match:** Consistent with existing template structure patterns
- **Integration:** Integrates with current template design guidelines

**Consultant Recommendation 3:** Formalize Enhanced Planning Standards
- **Current State:** Basic planning template exists at `prompt/templates/planner/standard_planning.md`
- **Proposed Change:** Add plan granularity profiles and structured file manifests
- **Pattern Match:** Extends current planning methodology
- **Integration:** Builds upon existing planning workflow

## Implementation Plan

### Phase 1: Core Documentation Updates [~3 hours]

#### Task 1.1: Update prompt_main.md with Project Versioning Standards

We begin by adding a comprehensive "Project Versioning Standards" section to `prompt/documentation/prompt_main.md` after the existing versioning rules section. This new section will establish the fundamental distinction between product and artifact versioning.

The implementation starts with creating the new section structure:

```markdown
### 4.2 Project Versioning Standards

The system maintains two distinct versioning concepts that must never be conflated:

#### Product/Component Versioning
- **Purpose**: Tracks the actual software component version (e.g., `tv_ingest v2.0.0`)
- **Format**: Semantic versioning (Major.Minor.Patch)
- **Scope**: Applied to the final deliverable software component
- **Stability**: Only changes when the component functionality changes

#### Artifact Versioning  
- **Purpose**: Tracks development artifact iterations (e.g., `plan_target_v2.0.0_iter_1.md`)
- **Format**: `[artifact_type]_target_v[PRODUCT_VERSION]_iter_[ITERATION].md`
- **Scope**: Applied to planning documents, consultations, reviews
- **Flexibility**: Can iterate multiple times for the same target product version
```

This section will include practical examples showing how a plan targeting `tv_ingest v2.0.0` might go through iterations `iter_1`, `iter_2`, etc., without affecting the target product version.

#### Task 1.2: Update Task-Centric Workflow Section

We modify the existing "Task-Centric Workflow" section in `prompt_main.md` to explain how the `workflow_state.json` will track both `target_version` and `iteration` as separate fields. This ensures the state management system properly supports the new versioning approach.

#### Task 1.3: Update general.md with Artifact Iteration Guidance

We add a new subsection to `documentation/general.md` that provides specific guidance on when to use product versus artifact versioning, including decision trees and examples for common scenarios.

### Phase 2: Template and Process Updates [~2 hours]

#### Task 2.1: Update All Templates with Mandatory Headers

We systematically update each template in `prompt/templates/` to include the new mandatory artifact header block:

```markdown
## Task Context Block
- **Task ID:** [Unique identifier linking to workflow_state.json]
- **Task Type:** [consultation/planning/development/review]
- **Target Component:** [Component name]
- **Target Version:** [Final product version this artifact supports]
- **Artifact Type:** [Type of artifact being created]
- **Iteration:** [Iteration number for this artifact]
```

This header ensures every workflow artifact is properly contextualized and traceable back to its originating task and target product version.

#### Task 2.2: Add Enhanced Planning Standards

We extend the planning template to include:
- **Plan Granularity Profiles**: Define "Full" and "Lite" planning profiles for different complexity levels
- **Standardized File Manifest**: Require structured tables showing all file changes
- **Iteration Tracking**: Clear documentation of which iteration this plan represents

### Phase 3: Documentation Consistency [~1 hour]

#### Task 3.1: Update Template Design Guidelines

We ensure all template guidelines in `prompt_main.md` section 7 reflect the new versioning approach and mandatory header requirements, maintaining consistency across all documentation.

#### Task 3.2: Add Cross-Reference Links

We add appropriate cross-references between the updated sections to ensure users can easily navigate between related versioning concepts and find relevant guidance.

---

## Documentation & Testing Deliverables

### 1. Documentation Updates
- **`prompt/documentation/prompt_main.md`:** Add Project Versioning Standards section and update Task-Centric Workflow section
- **`documentation/general.md`:** Include new versioning rules and artifact iteration guidance
- **All templates in `prompt/templates/`:** Add mandatory Task Context Block headers
- **Change history entries:** Document versioning system improvements in respective change_history.md files

### 2. Validation Requirements
- All existing documentation links remain functional after updates
- New versioning standards are consistently applied across all templates
- Clear examples provided for both product and artifact versioning scenarios
- Cross-references between related sections are accurate and helpful

---

## Dependencies & Blockers

### Internal Dependencies
None - All changes are self-contained within documentation files

### External Dependencies
None - No external systems or services affected

### Mitigation Plan
Not applicable - no blocking dependencies identified

## Risk Mitigation

### Risk Register

| Risk | Probability | Impact | Mitigation | Trigger |
|------|-------------|--------|------------|---------|
| Documentation Inconsistency | Medium | Medium | Clear examples and decision trees | Confusion reports from users |
| User Confusion | Low | Medium | Simple examples and clear guidelines | Questions about new versioning |
| Implementation Delays | Low | Low | Straightforward documentation updates | Missing deadlines |

### Rollback Procedure

**Quick Rollback (< 5 minutes):**
```bash
# 1. Revert prompt_main.md to previous version
git checkout HEAD~1 -- prompt/documentation/prompt_main.md

# 2. Revert general.md to previous version  
git checkout HEAD~1 -- documentation/general.md

# 3. Revert all templates
git checkout HEAD~1 -- prompt/templates/
```

**Full Rollback (if needed):**
1. Restore all modified files from backup
2. Update change history to document rollback
3. Notify stakeholders of rollback completion

## Validation Criteria

### Technical Validation (For Reviewers)

**Documentation Quality:**
- All versioning examples are clear and consistent
- New standards don't conflict with existing processes
- Templates include all mandatory elements
- Cross-references are accurate and functional

**Process Validation:**
- New versioning approach supports artifact iteration
- Product versions remain stable during planning phases
- Clear escalation path for version conflicts
- Backward compatibility maintained

### Code Quality Checks
- [ ] All markdown syntax is valid
- [ ] Links and references are functional
- [ ] Examples are accurate and helpful
- [ ] No spelling or grammatical errors

## Acceptance Criteria

### Business Requirements (For PM/Client)

**Feature Delivery:**
- [ ] Clear separation between product and artifact versions documented
- [ ] All templates include mandatory task context headers
- [ ] Examples provided for common versioning scenarios
- [ ] Backward compatibility maintained with existing artifacts

**User Experience:**
- [ ] Documentation is easy to understand and navigate
- [ ] Clear decision trees for versioning choices
- [ ] Practical examples for real-world scenarios
- [ ] Consistent formatting across all updated files

### Operational Readiness
- [ ] All documentation files pass markdown validation
- [ ] Links and cross-references are functional
- [ ] Change history entries are properly formatted
- [ ] **Documentation updated & change_history entries present**

## Deployment Plan

### Staging Deployment
1. Create branch for versioning updates
2. Apply all documentation changes
3. Review for consistency and accuracy
4. Test all links and references

### Production Deployment
1. **Phase 1:** Merge documentation updates
2. **Phase 2:** Verify all links and references work
3. **Phase 3:** Notify stakeholders of new versioning standards

### Post-Deployment
- [ ] Verify all documentation is accessible
- [ ] Check that examples are clear and helpful
- [ ] Confirm cross-references work correctly
- [ ] Gather feedback on new versioning approach

---

## Appendices

### A. File Changes
```
Modified (Documentation):
- prompt/documentation/prompt_main.md
- documentation/general.md
- prompt/templates/consultant/standard_consultation.md
- prompt/templates/planner/standard_planning.md
- prompt/templates/developer/standard_development.md
- prompt/templates/reviewer/standard_review.md

Modified (Change History):
- prompt/documentation/prompt_main_change_history.md
- documentation/general_change_history.md
```

### B. New Section Structure
```markdown
# New sections being added:

## In prompt_main.md:
### 4.2 Project Versioning Standards
- Product/Component Versioning
- Artifact Versioning
- Practical Examples
- Decision Trees

## In general.md:
### 8. Artifact Iteration Guidelines
- When to iterate vs. version
- Naming conventions
- Best practices
```

---

## Plan Completeness Checklist
- [x] Stakeholder summary is clear and non-technical
- [x] Plan includes explicit documentation and test tasks
- [x] All deliverables are listed in the "Documentation & Testing Deliverables" section
- [x] File manifest in Appendix A is complete
- [x] Estimates are consistent between header, stakeholder summary, and phase breakdowns
- [x] Rollback procedure is defined
- [x] Focus maintained on documentation-only changes as requested