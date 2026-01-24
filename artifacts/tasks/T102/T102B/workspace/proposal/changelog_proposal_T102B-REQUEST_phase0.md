# CHANGELOG

## Change History Overview

| Version | Date | Type | Summary |
|:--------|:-----|:-----|:--------|
| v1.4.0 | 2026-01-19 | Major | T102-ADR-005 Compliance Update |
| v1.3.0 | 2026-01-18 | Major | Activity 2.3 IF+IG: Confirmed 3 IF + 6 IG |
| v1.2.0 | 2026-01-18 | Major | Activity 2.3 QG+ASSUM: Confirmed 3 QG + 3 ASSUM |
| v1.1.0 | 2026-01-18 | Major | Activity 2.3 DEP+CON: Confirmed 5 DEP + 4 CON |
| v1.0.0 | 2026-01-17 | Major | Initial proposal skeleton |

- **v1.5.0** (2026-01-21): Activity 2.3.7 E-NFR: Added 3 E-NFR candidates via ISO 25010
  - Added 3 E-NFR candidates via ISO 25010 scaffold dialogue — NFR-001 (Template Maintainability), NFR-002 (Authoring Friction Threshold), NFR-003 (Validation Reliability)
  - Updated inventory summary: 56 total candidates, 34 high priority
  - Research confirmed QG/NFR overlap per ISO 25010 + BABOK; kept separate with scope distinction (QG=inherited targets, NFR=epic-specific testable metrics)
  - Research confirmed E-FR deferral aligned with IEEE 830/SAFe (FR at Feature/Story, not Epic)
  - Author: LLM_Consultant

- **v1.4.0** (2026-01-19): T102-ADR-005 Compliance Update
  - Fixed CON-004 source attribution to `T102-GDR-001` + `T102B-DEP-004`
  - Renamed IF-003 to "Request Output Contract" — corrected "Concept handoff" to "Design/Plan" per `T102-GDR-001`
  - Removed internal `T102B-` references from Reference lines per `T102-ADR-005-RULE-004`
  - Added NOTE-008 (IF Schema Convention) as local standardization proposal for T102
  - Moved IG section to III.C (E-IID category) pending non-normative rewrite in Activity 2.5
  - Author: LLM_Consultant

- **v1.3.0** (2026-01-18): Activity 2.3 IF+IG: Confirmed 3 IF + 6 IG
  - Confirmed 3 IF + 6 IG
  - Populated Section III.E (IF bodies with schema tables per Option C) + Section III.F (IG bodies with high-level guidance per Option C)
  - Added NOTE-007 (Planner Handoff Deferral) per Gap IF-A
  - Updated QG-001 to reference CON-003 (removed 200-line duplication)
  - Author: LLM_Consultant

- **v1.2.0** (2026-01-18): Activity 2.3 QG+ASSUM: Confirmed 3 QG + 3 ASSUM
  - Confirmed 3 QG + 3 ASSUM
  - Removed 3 duplicates (QG-001, QG-002 per inheritance; ASSUM-003 per DEP-001 redundancy)
  - Added QG-003 (Artifact Completeness), ASSUM-003 (Author Self-Assessment) as gap remediation
  - Populated Section III.A + III.C bodies
  - Added ASSUM Validation Lifecycle Summary per T801A exemplar
  - Author: LLM_Consultant

- **v1.1.0** (2026-01-18): Activity 2.3 DEP+CON: Confirmed 5 DEP + 4 CON
  - Confirmed 5 DEP + 4 CON
  - Removed 3 duplicates (DEP-003, QG-003, QG-004)
  - Populated Section III.B + III.D bodies per T102-ADR-005
  - Author: LLM_Consultant

- **v1.0.0** (2026-01-17): Initial proposal skeleton
  - Initial proposal skeleton; Section II seeded with 55 E-ID candidates from analysis
  - Author: LLM_Consultant
