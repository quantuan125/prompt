# Documentation Update Plan: {{target_name}} v{{version}}

**Version:** {{version}}  
**Component:** {{target_name}}  
**Author:** LLM_Planner  
**Date:** {{date}}  
**Reason for Update:** {{reason}}
**Estimated Effort:** {{effort_size}} (~{{hours}} hours)

## Stakeholder Summary

### What We're Doing
{{what_description}}

### Why It Matters
{{why_description}}

### Key Points
- **Timeline / Effort:** {{hours}} dev hrs (~{{calendar_days}} calendar days)
- **Risk Level:** {{risk_level}} - {{risk_explanation}}
- **User Impact:** {{user_impact}}
- **Dependencies:** {{dependencies}}

---

## Technical Planning Document

### Executive Summary

{{executive_summary}}

### Key Metrics
- **Documents Modified:** {{docs_modified}}
- **New Documentation:** {{new_docs}}
- **Archive Actions:** {{archive_actions}}
- **Standards Compliance:** {{compliance_updates}}

## Pre-Planning Validation

### 1. Documentation Analysis ✓
- **Current State:** {{current_state}}
- **Gaps Identified:** {{gaps_identified}}
- **Standards Violations:** {{standards_violations}}

### 2. Standards Verification ✓
- **General.md Compliance:** {{general_compliance}}
- **Header Standards:** {{header_standards}}
- **Version Requirements:** {{version_requirements}}

### 3. Impact Assessment ✓
- **Affected Documents:** {{affected_documents}}
- **Cross-References:** {{cross_references}}
- **Archive Requirements:** {{archive_requirements}}

## Implementation Plan

### Phase 1: Preparation [~{{phase1_hours}} hours]

#### Task 1.1: Archive Current Versions

{{archive_description}}

Using the archive manager:
```bash
python prompt/scripts/archive_manager.py archive \
    --path "{{document_path}}" \
    --version "{{current_version}}" \
    --reason "{{archive_reason}}"
```

#### Task 1.2: Validate Standards Compliance

{{validation_description}}

### Phase 2: Content Updates [~{{phase2_hours}} hours]

#### Task 2.1: Update Document Headers

{{header_update_description}}

Required header format:
```markdown
**Title:** {{document_title}}
**Version:** {{new_version}}
**Purpose:** {{document_purpose}}
**Audience:** {{target_audience}}
**Last Updated:** {{update_date}}
**Change History:** {{change_history_path}}
```

#### Task 2.2: Update Content Sections

{{content_update_description}}

#### Task 2.3: Update Cross-References

{{cross_reference_updates}}

### Phase 3: Quality Assurance [~{{phase3_hours}} hours]

#### Task 3.1: Validate Documentation Hierarchy

{{hierarchy_validation}}

#### Task 3.2: Update Change History

{{change_history_updates}}

#### Task 3.3: Final Review and Validation

{{final_validation}}

---

## Documentation & Testing Deliverables

### 1. Documentation Updates
{{documentation_deliverables}}

### 2. Validation Requirements
- **Standards Compliance:** All documents follow general.md standards
- **Cross-Reference Validation:** All internal links verified
- **Archive Completion:** Previous versions properly archived
- **Change History Updates:** All changes documented in change history files

---

## Dependencies & Blockers

### Internal Dependencies
{{internal_dependencies}}

### Standards Dependencies
{{standards_dependencies}}

### Mitigation Plan
{{mitigation_plan}}

## Risk Mitigation

### Risk Register

| Risk | Probability | Impact | Mitigation | Trigger |
|------|-------------|--------|------------|---------|
| Documentation drift | Medium | Medium | Automated validation | Standards violations found |
| Version conflicts | Low | High | Archive before changes | Multiple versions detected |
| Cross-reference breaks | Medium | Low | Validation scripts | Broken links detected |

### Rollback Procedure

**Quick Rollback (< 5 minutes):**
```bash
# Restore from archive
python prompt/scripts/archive_manager.py restore \
    --archive "{{archive_path}}" \
    --target "{{original_path}}"
```

**Full Rollback (if needed):**
{{full_rollback_steps}}

## Validation Criteria

### Documentation Quality Checks
- [ ] All headers follow standardized format
- [ ] Version numbers are consistent
- [ ] Change history is updated
- [ ] Cross-references are valid
- [ ] Archive process completed

### Standards Compliance
- [ ] General.md standards followed
- [ ] No redundant content across documents
- [ ] Proper hierarchy maintained
- [ ] Template usage documented

## Acceptance Criteria

### Documentation Requirements
{{documentation_requirements}}

### Operational Readiness
- [ ] Documentation accessible to target audience
- [ ] Archive process documented
- [ ] Update procedures established
- [ ] **All standards compliance verified**

## Deployment Plan

### Staging Review
{{staging_review_process}}

### Production Update
{{production_update_process}}

### Post-Deployment
{{post_deployment_verification}}

---

## Appendices

### A. Document Changes

```
{{document_changes_manifest}}
```

### B. Archive Actions

```
{{archive_actions_detail}}
```

### C. Standards Checklist

```
{{standards_checklist}}
```

---

## Plan Completeness Checklist
- [ ] Documentation scope clearly defined
- [ ] Archive requirements specified
- [ ] Standards compliance addressed
- [ ] Cross-reference updates planned
- [ ] Change history updates included
- [ ] Validation procedures defined
- [ ] Rollback procedures documented