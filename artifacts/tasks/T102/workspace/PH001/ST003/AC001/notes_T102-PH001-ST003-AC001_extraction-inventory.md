---
artifact_type: 'NOTES'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream: 'ST003'
activity_id: 'T102-PH001-ST003-AC001'
version: '1.0.0'
date: '2026-02-08'
status: 'completed'
author: 'LLM_Developer'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST003/plan_T102-PH001-ST003.md'
---

# AC001 Final Extraction Inventory (ADR -> STD)

| Scope | Old ADR ID | New STD ID | Canonical Path | Migration Mode | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Initiative | `T102-ADR-001` | `T102-STD-001` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md` | Extract + create | Completed |
| Initiative | `T102-ADR-002` | `T102-STD-002` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-002_canonical-yaml-header.md` | Extract + create | Completed |
| Initiative | `T102-ADR-003` | `T102-STD-003` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md` | Extract + create | Completed |
| Initiative | `T102-ADR-005` | `T102-STD-005` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` | Script migrate + normalize | Completed |
| Initiative | `T102-ADR-006` | `T102-STD-006` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` | Extract + create | Completed |
| Initiative | `T102-ADR-007` | `T102-STD-007` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` | Extract + create | Completed |
| Initiative | `T102-ADR-008` | `T102-STD-008` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-008_organisation-baseline-index.md` | Extract + create | Completed |
| Initiative | `T102-ADR-009` | `T102-STD-009` | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-009_governance-standards-specification.md` | Script migrate + normalize | Completed |
| Epic | `T102A-ADR-001` | `T102A-STD-001` | `prompt/artifacts/tasks/T102/consultant/standards/T102A-STD-001_governance-roadmap-snapshot.md` | Extract + create | Completed |
| Epic | `T102A-ADR-002` | `T102A-STD-002` | `prompt/artifacts/tasks/T102/consultant/standards/T102A-STD-002_feature-register-index.md` | Extract + create | Completed |
| Epic | `T102B-ADR-001` | `T102B-STD-001` | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-001_request-architecture-standard.md` | Script migrate + normalize | Completed |
| Epic | `T102B-ADR-002` | `T102B-STD-002` | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-002_section-classification-standard.md` | Script migrate + normalize | Completed |
| Epic | `T102B-ADR-003` | `T102B-STD-003` | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-003_story-fr-deferral-standard.md` | Script migrate + normalize | Completed |
| Epic | `T102B-ADR-004` | `T102B-STD-004` | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-004_request-lite-specification.md` | Script migrate + normalize | Completed |
| Epic | `T102C-ADR-001` | `T102C-STD-001` | `prompt/artifacts/tasks/T102/T102C/standard/standard_T102C-STD-001_concept-architectural-framework.md` | Extract + create | Completed |
| Feature | `T102A-SPSST-ADR-0001` | `T102A-SPSST-STD-0001` | `prompt/artifacts/tasks/T102/consultant/standards/T102A-SPSST-STD-0001_approvals-in-body.md` | Legacy source extraction + create | Completed |

## Notes

- T102B canonical location decision applied: files remain in `prompt/artifacts/tasks/T102/T102B/standards/`.
- Stage 2 global reference propagation executed over `prompt/` with governance exclusions for output/raw artifacts.
