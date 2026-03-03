---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC004'
version: '1.8.0'
date: '2026-03-03'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: Program Governance (PROGRAM) — Phase 0 / Stream ST001 / Activity P-PH000-ST001-AC004: Author P-STD-004 (File Naming & Directory Convention)

## I. EXECUTIVE SUMMARY

**Purpose**: Author `P-STD-004` (File Naming & Directory Convention) as a program-level combined standard-specification file. Uses Seed-First methodology: rapid structural promotion of proposal v3.4.0 (24 approved DRs) into normative CLAUSE format as `draft`, followed by post-seeding gap/risk/issues analysis, CLAUSE amendments, and cross-initiative validation before `accepted` status.

**Non-goals**:
- This activity does not amend the proposal (v3.4.0 is the final input; all changes go directly into P-STD-004 CLAUSEs).
- This activity does not execute directory migrations (T104-PH001-ST007 scope).
- This activity does not author new conventions beyond those approved in the proposal; it formalizes existing conventions as normative CLAUSEs.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC004`
**Objective**: Produce P-STD-004 as a P-STD-001-conformant combined standard-specification file, validated against multiple initiative directory structures, with a formal post-seeding analysis.
**Execution Mode**: `GATED`
**Depends On**: `—`

**Context**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (v3.4.0 — primary input)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` (governing authoring standard)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` (reference semantics + CLAUSE-011 timeline file naming)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` (authoring guideline)
- `prompt/templates/consultant/standards/template_standard_specs.md` (combined file template)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (gate verification rules)
- `prompt/templates/consultant/workspace/template_workspace_verification.md` (verification template)
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (downstream update target)
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (downstream update target)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/plan_P-PH000-ST001-AC004.md` (this plan)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES002.md` (SES002 decisions: Seed-First + analysis/proposal stream-level enforcement)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES003.md` (SES003 decisions: placement policy, archive model, reference semantics)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/analysis/analysis_P-PH000-ST001-AC004-GATE-002_external-review-disposition.md` (external review analysis supporting GATE-002 package)

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `P-PH000-ST001-AC004-TK001` | Rapid Seed: Structural Promotion of Proposal v3.4.0 to P-STD-004 (draft) | `completed` | LLM_Developer | — | `standard_P-STD-004_...md` | Proposal v3.4.0, P-STD-001, P-STD-005, `guideline_standard_specs.md` | Seeded `P-STD-004` draft created at `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`. |
| TK001.1 | `P-PH000-ST001-AC004-TK001.1` | Produce Verification Evidence (GATE-001 readiness) | `completed` | LLM_Reviewer | TK001 | `verification_P-PH000-ST001-AC004_gate-001.md` | `guideline_workspace_verification.md`, `template_workspace_verification.md` | Verification evidence produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-001.md` (GDR recorded). |
| GATE-001 | `P-PH000-ST001-AC004-GATE-001` | Client Review of Seeded P-STD-004 (draft) | `completed` | Client | TK001.1 | Pass/fail | — | Client Decision recorded in the GDR of `verification_P-PH000-ST001-AC004_gate-001.md`: APPROVE (2026-02-27). |
| TK002 | `P-PH000-ST001-AC004-TK002` | Post-Seeding Gap/Risk/Issues Analysis | `completed` | LLM_Consultant | GATE-001 | `analysis_P-PH000-ST001-AC004_...md` | P-STD-004 (draft), P-STD-001, P-STD-005 | Analysis produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC004_p-std-004-proposal-seeding-assessment.md`. |
| TK002.1 | `P-PH000-ST001-AC004-TK002.1` | Produce Verification Evidence (GATE-002 readiness) | `completed` | LLM_Reviewer | TK002 | `verification_P-PH000-ST001-AC004_gate-002.md` | `guideline_workspace_verification.md`, `template_workspace_verification.md` | Verification evidence produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-002.md` (GDR recorded: APPROVE, 2026-03-01). |
| TK002.2 | `P-PH000-ST001-AC004-TK002.2` | GIR Disposition Proposal (GATE-002 decision package) | `completed` | LLM_Consultant | TK002.1 | `proposal_P-PH000-ST001-AC004-TK002.2_...md` | TK002 analysis + TK002.1 verification | Proposal produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md` (Client dispositions recorded 2026-03-01). |
| TK002.3 | `P-PH000-ST001-AC004-TK002.3` | External Review Analysis (GATE-002 package) | `completed` | LLM_Consultant | TK002.2 | `analysis_P-PH000-ST001-AC004-GATE-002_external-review-disposition.md` | `analysis_type: external_review` exemplar + GATE-002 package | External review analysis produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/analysis/analysis_P-PH000-ST001-AC004-GATE-002_external-review-disposition.md`. |
| GATE-002 | `P-PH000-ST001-AC004-GATE-002` | Client Review of Analysis Findings | `completed` | Client | TK002.2 | Pass/fail | — | Client Decision recorded in the GDR of `verification_P-PH000-ST001-AC004_gate-002.md`: APPROVE (2026-03-01). Decision Reference: `proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md`. |
| TK003 | `P-PH000-ST001-AC004-TK003` | Apply Analysis-Driven CLAUSE Amendments | `completed` | LLM_Developer | GATE-002 | `standard_P-STD-004_...md` | GATE-002 approved findings | GATE-002-approved GIR remediations applied to `standard_P-STD-004_file-naming-and-directory-convention.md` (including archive model, `<scope-UID>`, and reference resilience). |
| TK003.1 | `P-PH000-ST001-AC004-TK003.1` | Clarify Formal Reference vs Subclause Reference (P-STD-005) | `completed` | LLM_Developer | GATE-002 | `standard_P-STD-005_...md` | GIR-010 disposition (GATE-002) | P-STD-005 amended: `P-STD-005-CLAUSE-004E` clarifies full formal reference vs subclause pointer usage. |
| TK003.2 | `P-PH000-ST001-AC004-TK003.2` | (Superseded) Work Package: GIR-006 Stream-Only `analysis/` + `proposal/` Migration & Enforcement | `cancelled` | LLM_Consultant | GATE-002 | — | — | Superseded by GATE-002 (2026-03-01): `analysis/` + `proposal/` MAY be activity-level when placement matches `<scope-UID>`; stream-only migration/enforcement no longer applies. |
| TK003.3 | `P-PH000-ST001-AC004-TK003.3` | Work Package: GIR-011 `_gate-###` Verification Filename Normalization & Enforcement | `completed` | LLM_Consultant | GATE-002 | `T104-PH001-ST007` | GIR-011 (approved option b) + repo inventory | Work package recorded under TK003.3 (authoritative rename inventory + deterministic rename targets + enforcement requirements). |
| TK003.4 | `P-PH000-ST001-AC004-TK003.4` | Amend P-STD-004: Activity-Level `analysis/` + `proposal/` Allowed with `<scope-UID>` Match | `completed` | LLM_Developer | GATE-002 | `standard_P-STD-004_...md` | GATE-002 placement policy decision (2026-03-01) | P-STD-004 amended: activity-level `analysis/` and `proposal/` allowed with `<scope-UID>` placement alignment rule. |
| TK004 | `P-PH000-ST001-AC004-TK004` | Downstream Updates (SPS, workspace_documentation_rules.md, Binding Rule) | `completed` | LLM_Consultant | TK003 | `sps_P-PROGRAM.md`, `workspace_documentation_rules.md`, P-STD-004 | — | Downstream updates applied: SPS `P-STD-004` row updated with Canonical Path; `workspace_documentation_rules.md` §7 retargeted to `P-STD-004`; binding-by-reference rule added to `P-STD-004-CLAUSE-002E`. |
| TK004.2 | `P-PH000-ST001-AC004-TK004.2` | Disposition Proposal (GATE-003 greenlight package for TK005) | `completed` | LLM_Consultant | TK004, `T104-PH001-ST007-AC004.1` | `proposal_P-PH000-ST001-AC004-TK004.2_tk005-greenlight-disposition-package.md` | `guideline_workspace_plan.md`, `guideline_workspace_verification.md` | Disposition proposal produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/proposal/proposal_P-PH000-ST001-AC004-TK004.2_tk005-greenlight-disposition-package.md` (canonical GDR embedded with `Client Decision: pending`). |
| TK004.1 | `P-PH000-ST001-AC004-TK004.1` | Evidence-First Package Audit (GATE-003 readiness) | `completed` | LLM_Consultant | TK004.2 | `verification_P-PH000-ST001-AC004_gate-003-package-audit.md` | `guideline_workspace_verification.md`, TK004.2 proposal + evidence set | Evidence-first audit produced: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-003-package-audit.md` (verdict: PASS; no blocking findings). |
| GATE-003 | `P-PH000-ST001-AC004-GATE-003` | Pre-TK005 Greenlight: Review + Remediation Dispositions | `planned` | Client | TK004.1 | Pass/fail | — | Client decision recorded in the GDR section of the TK004.2 proposal (canonical decision record). |
| TK005 | `P-PH000-ST001-AC004-TK005` | Incorporate P Migration Findings | `planned` | LLM_Consultant | GATE-003 | `standard_P-STD-004_...md` | P migration evidence (post-AC004.1 delta migration) | — |
| TK006 | `P-PH000-ST001-AC004-TK006` | Incorporate T102 Migration Findings | `planned` | LLM_Consultant | TK004, `T104-PH001-ST007-AC005` | `standard_P-STD-004_...md` | T102 migration evidence | — |
| TK007 | `P-PH000-ST001-AC004-TK007` | Produce Verification Evidence (GATE-004 acceptance readiness) | `planned` | LLM_Reviewer | TK004 | `verification_P-PH000-ST001-AC004_gate-004.md` | `guideline_workspace_verification.md`, `template_workspace_verification.md` | — |
| GATE-004 | `P-PH000-ST001-AC004-GATE-004` | Cross-Initiative Validation: P-STD-004 draft → accepted | `planned` | Client | TK007 | Pass/fail | P-RISK-002 | — |

---

## III. TASKS (DETAILED)

### Task TK001: Rapid Seed — Structural Promotion of Proposal v3.4.0 to P-STD-004 (draft)

**Task ID**: `P-PH000-ST001-AC004-TK001`

**Purpose**: Perform a one-time structural promotion of proposal v3.4.0 approved conventions into P-STD-004 normative CLAUSE format. The substance stays the same; the format changes from descriptive conventions to enforceable MUST/SHALL/SHOULD/MAY CLAUSEs per P-STD-001.

**Deliverable**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (status: `draft`)

**Scope**:
- In scope:
  - CLAUSE mapping: Map proposal v3.4.0 Conventions 1–9 + Archive Rules to P-STD-004 CLAUSEs
  - Substandard architecture decision (if CLAUSE count ≥10, warranted per P-STD-001-CLAUSE-003)
  - P-STD-004-ADR-001: Author decision record (adoption of proposal v3.4.0 as seed, forward-only posture, T102 permanent-grandfathering, standards placement variance)
  - Normative/informative boundary: Proposal Sections I (Purpose), II (Analysis), VII (Risks), VIII (Scaffolding) are informative — excluded from CLAUSEs
  - Analysis/proposal placement policy: seeded as stream-level-only per SES002 and then superseded by Client GATE-002 decision (2026-03-01) and implemented via TK003.4 as a scope-aligned placement rule (see `P-STD-004-CLAUSE-003F`)
  - Specification Index per P-STD-001-CLAUSE-002 (expected >5 CLAUSEs)
  - Cross-scope references per P-STD-005-CLAUSE-004 (External Reference lines)
- Out of scope:
  - Proposal amendment (v3.4.0 is final input)
  - Normative content beyond what is in the proposal
  - Cross-initiative validation (GATE-004)

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (v3.4.0) — primary content source
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` — governing authoring standard
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` — reference semantics + CLAUSE-011 (Timeline File Naming)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` — authoring guideline
- `prompt/templates/consultant/standards/template_standard_specs.md` — combined file template
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES001.md` — prior session decisions (DEC001–DEC007)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES002.md` — commissioning decisions (Seed-First + analysis/proposal stream-level enforcement)

**Steps**:
1. Read proposal v3.4.0 fully (all 9 Conventions + 24 DRs + Archive Rules).
2. Read P-STD-001 (governing standard for combined file authoring).
3. Read P-STD-005 (reference semantics + CLAUSE-011 timeline file naming — ensure no normative duplication between P-STD-004 and P-STD-005-CLAUSE-011).
4. Read `guideline_standard_specs.md` and `template_standard_specs.md`.
5. Determine substandard architecture. Recommended grouping if CLAUSE count warrants:
   - `P-STD-004A` — Directory Structure (Conventions 1, 3, 4, 5, 6, 7)
   - `P-STD-004B` — File Naming & Stems (Convention 2 + archive naming from Convention 8)
   - Alternative: flat CLAUSEs if total count stays under 10
6. Map each proposal Convention to CLAUSEs:
   - Convention 1 (Initiative Root) → CLAUSE(s) for root directory structure
   - Convention 2 (File Naming Stems) → CLAUSE(s) for prefix patterns and stem registry table
   - Convention 3 (Combined STD Placement) → CLAUSE or absorbed into root structure
   - Convention 4 (Timeline Hierarchy) → CLAUSE(s) for workspace timeline structure + type subdirectory rules. (Note: initial SES002 stream-only posture was superseded by TK003.4; current normative rule is scope-aligned placement per `P-STD-004-CLAUSE-003F`.)
   - Convention 5 (Stream 0) → CLAUSE or subclause for ST000 naming/ID scoping
   - Convention 6 (SSOT Scope) → CLAUSE for SSOT organization rules
   - Convention 7 (Epic/Feature Self-Similarity) → CLAUSE for self-similar structure
   - Convention 8 (Archive Strategy) → CLAUSE(s) for two-tier archive model (versioned `_v#.#.#` vs deprecated no-suffix, per DR-24)
   - Convention 9 (Research Organization) → CLAUSE for RES-ID paired structure
7. Convert descriptive language to normative (MUST/SHALL/SHOULD/MAY) per P-STD-001-CLAUSE-008.
8. Author P-STD-004-ADR-001 per P-STD-001-CLAUSE-025 template (Context, Decision, Alternatives, Consequences, Traceability).
9. Author Specification Index per P-STD-001-CLAUSE-002.
10. Add cross-scope references with `External Reference:` lines per P-STD-005-CLAUSE-004.
11. Author `## References` and `## Provenance` per P-STD-001-CLAUSE-028.
12. Set frontmatter status to `draft` per P-STD-001-CLAUSE-004A.

**Success Criteria**:
- [ ] P-STD-004 combined file exists at `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` with `draft` status
- [ ] Canonical structure follows P-STD-001-CLAUSE-001A (5 required sections in order)
- [ ] All 9 proposal Conventions mapped to normative CLAUSEs
- [ ] Analysis/proposal placement policy encoded as a normative CLAUSE (current: scope-aligned placement per `P-STD-004-CLAUSE-003F`)
- [ ] P-STD-004-ADR-001 exists with required subheadings (Context, Decision, Alternatives, Consequences, Traceability)
- [ ] Specification Index present per P-STD-001-CLAUSE-002
- [ ] Cross-scope references follow P-STD-005-CLAUSE-004
- [ ] No proposal content changes — structure/format promotion only

---

### Task TK001.1: Produce Verification Evidence (GATE-001 Readiness)

**Task ID**: `P-PH000-ST001-AC004-TK001.1`

**Purpose**: Produce independent gate verification evidence that the seeded P-STD-004 exists, is structurally conformant to P-STD-001, and is ready for Client review at GATE-001. This task follows the TK-before-gate pattern and MUST be completed before the Client decision gate proceeds.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-001.md`

**Inputs Required**:
- Seeded P-STD-004 (TK001 output)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- `prompt/templates/consultant/workspace/template_workspace_verification.md`
- Proposal v3.4.0 (baseline)
- P-STD-001 + P-STD-005 (compliance + reference semantics)

**Steps**:
1. Read the seeded P-STD-004 fully and confirm the `draft` status is present in frontmatter.
2. Verify P-STD-004 combined-file structure and required sections per P-STD-001.
3. Verify traceability: confirm each proposal Convention (1–9) is represented by one or more normative CLAUSEs (no unmapped conventions).
4. Verify the Convention 4 rule is encoded: `analysis/` and `proposal/` are stream-level ONLY; activity-level type subdirectories are restricted to `snotes/`, `raw/`, `verification/`, `dev-report/` (SES002 decision).
5. Author the verification artifact using the verification template:
   - Evidence Set (all artifacts reviewed)
   - Per-criterion checks (expected vs observed evidence)
   - Gate Recommendation (verdict)
   - Gate Decision Record (GDR) with `Client Decision: pending`

**Success Criteria**:
- [ ] Verification artifact exists at the deliverable path
- [ ] Evidence Set lists all reviewed artifacts (P-STD-004, proposal, P-STD-001, P-STD-005, this plan)
- [ ] Verdict issued per `guideline_workspace_verification.md` §VIII
- [ ] GDR section present with `Client Decision: pending`

---

### GATE-001: Client Review of Seeded P-STD-004 (draft)

**Task ID**: `P-PH000-ST001-AC004-GATE-001`

**Entry Criteria**:
- TK001.1 complete (verification evidence produced)
- P-STD-004 file exists with `draft` status
- CLAUSE mapping is traceable to proposal Conventions

**Reviewer**: Client

**Exit Criteria**:
- Client confirms CLAUSE mapping is correct and complete
- Client confirms substandard architecture (if used) is appropriate
- No blocking structural issues
- P-STD-004 `draft` approved as the normative reference surface for downstream activities (`T104-PH001-ST007-AC004`, `T104-PH001-ST007-AC005`)
- Client decision recorded in the GDR section of `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-001.md`

---

### Task TK002: Post-Seeding Gap/Risk/Issues Analysis

**Task ID**: `P-PH000-ST001-AC004-TK002`

**Purpose**: Perform a comprehensive CLAUSE-level gap/risk/issues assessment of P-STD-004 (draft). Targets: CLAUSE completeness, normative language accuracy, file naming convention normalization per P-STD-005, analysis/proposal placement enforcement, cross-reference compliance, and comparison with T104 migration evidence.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC004_p-std-004-proposal-seeding-assessment.md` (stream-level placement)

**Scope**:
- In scope:
  - P-STD-001 compliance audit of P-STD-004 (draft) — same checklist pattern as AC007-TK001
  - P-STD-005 reference compliance check
  - **File naming convention normalization**: Assess whether file naming conventions across ALL artifact types (`plan_`, `notes_`, `snotes_`, `analysis_`, `proposal_`, `verification_`, `dev-report_`, `standard_`, `roadmap_`, `comm_`, `raw_`) follow a consistent, navigable pattern aligned with P-STD-005 ID standards. Identify inconsistencies and recommend normalization
  - Analysis/proposal stream-level enforcement: verify CLAUSE correctly restricts to stream-level; document migration items for T104-PH001-ST007
  - Normative/informative boundary verification
  - Convention 4 type subdirectory conflict resolution verification (UID-scope trigger vs stream-level restriction)
  - GIR register with severity classification
- Out of scope:
  - Standard amendment (TK003)
  - Migration script changes (T104-PH001-ST007 scope)

**Inputs Required**:
- `standard_P-STD-004_...md` (draft, post-GATE-001) — target of analysis
- `standard_P-STD-001_...md` — compliance reference
- `standard_P-STD-005_...md` — reference semantics + CLAUSE-011
- `proposal_T104-PH001-ST002-AC000_...md` (v3.4.0) — verify completeness of CLAUSE mapping
- `workspace_documentation_rules.md` — downstream impact assessment
- T104-PH001-ST007-AC004 readiness analysis (if available) — migration evidence input

**Steps**:
1. Read P-STD-004 (draft) fully.
2. Read P-STD-001 fully. Perform structural compliance audit (same checklist pattern as AC007-TK001 — P-STD-001A through P-STD-001D).
3. Read P-STD-005. Verify all cross-scope references follow P-STD-005-CLAUSE-004.
4. **File naming normalization analysis**: Review all artifact type prefixes in P-STD-004 Convention 2 CLAUSEs. Assess whether their naming pattern (stem + UID + topic) is consistent, navigable, and aligned with P-STD-005-CLAUSE-011 (Timeline File Naming). Cross-check to avoid normative duplication between P-STD-004 and P-STD-005-CLAUSE-011. Identify inconsistencies that should be resolved as CLAUSE amendments.
5. **Analysis/proposal placement enforcement**: Verify the seeded CLAUSE correctly restricts `analysis/` and `proposal/` to stream-level only. Document specific migration items for T104-PH001-ST007 (list existing AC-level files that need correction).
6. **Normative language audit**: Verify MUST/SHALL/SHOULD/MAY usage is consistent with P-STD-001-CLAUSE-008. Flag any descriptive language that should be normative or vice versa.
7. **Convention completeness check**: Cross-reference every proposal Convention and sub-rule against P-STD-004 CLAUSEs. Identify gaps (proposal content not captured in CLAUSEs).
8. **Produce GIR register**: Type (`Gap`, `Issue`, `Risk`), Severity (`Critical`, `Major`, `Minor`), Status (`open`, `resolved`, `accepted`).
9. **Produce implementation readiness assessment**: Can P-STD-004 serve as normative authority for downstream activities? What conditions remain?

**Success Criteria**:
- [ ] P-STD-001 compliance audit completed
- [ ] P-STD-005 reference compliance verified
- [ ] File naming normalization assessment completed
- [ ] Analysis/proposal stream-level restriction verified + migration items documented
- [ ] Convention completeness check: zero unmapped proposal content
- [ ] GIR register produced with all items categorized
- [ ] Implementation readiness assessment produced

---

### Task TK002.1: Produce Verification Evidence (GATE-002 Readiness)

**Task ID**: `P-PH000-ST001-AC004-TK002.1`

**Purpose**: Produce independent gate verification evidence that the post-seeding analysis artifact is complete, internally consistent, and ready for Client disposition at GATE-002.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-002.md`

**Inputs Required**:
- TK002 analysis deliverable
- P-STD-004 (draft)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- `prompt/templates/consultant/workspace/template_workspace_verification.md`

**Steps**:
1. Read the analysis artifact fully and confirm all declared sections/checklists are present.
2. Verify that the GIR register exists and each item is categorized (Gap/Issue/Risk) with Severity and Status.
3. Verify that file naming normalization recommendations are explicit and testable (not vague).
4. Author the verification artifact using the verification template, including a Gate Recommendation and a GDR with `Client Decision: pending`.

**Success Criteria**:
- [ ] Verification artifact exists at the deliverable path
- [ ] Evidence Set lists analysis artifact + P-STD-004 + this plan
- [ ] Verdict issued per `guideline_workspace_verification.md` §VIII
- [ ] GDR section present with `Client Decision: pending`

---

### Task TK002.2: GIR Disposition Proposal (GATE-002 Decision Package)

**Task ID**: `P-PH000-ST001-AC004-TK002.2`

**Purpose**: Convert TK002’s GIR register into a decision-ready disposition package for the Client at GATE-002. This proposal enumerates every GIR item with options, a consultant recommendation, and a Client decision checkbox. The completed proposal serves as the authoritative per-GIR disposition record; the GATE-002 GDR references this proposal as its decision package.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md`

**Inputs Required**:
- TK002 analysis deliverable
- TK002.1 verification evidence
- P-STD-004 (draft)

**Steps**:
1. Read the TK002 analysis GIR register (GIR-001…GIR-011) and remediation text.
2. For each GIR item, author a disposition entry with: options (resolve/accept/defer), recommendation, rationale, and explicit execution target (TK003 / TK003.1 / T104-PH001-ST007).
3. Include a Client checkbox decision line per GIR item plus a final Client confirmation block.

**Success Criteria**:
- [ ] Proposal artifact exists at the deliverable path
- [ ] Every GIR item (GIR-001…GIR-011) has an explicit recommended resolution with rationale
- [ ] Each GIR item includes a Client decision checkbox block
- [ ] Downstream execution mapping is explicit (TK003 vs TK003.1 vs T104-PH001-ST007)

---

### GATE-002: Client Review of Analysis Findings

**Task ID**: `P-PH000-ST001-AC004-GATE-002`

**Entry Criteria**:
- TK002.1 complete (verification evidence produced)
- TK002.2 complete (GIR disposition proposal authored)
- TK002.3 complete (external review analysis package produced)
- Analysis artifact fully authored

**Reviewer**: Client

**Exit Criteria**:
- Client approves GIR dispositions (resolve/accept/defer per item)
- Client approves file naming normalization recommendations
- No blocking findings remain unaddressed
- Client dispositions recorded in `proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md`
- Client decision recorded in the GDR section of `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-002.md` with `Decision Reference` pointing to TK002.2

---

### Task TK003: Apply Analysis-Driven CLAUSE Amendments

**Task ID**: `P-PH000-ST001-AC004-TK003`

**Purpose**: Apply GATE-002-approved amendments to P-STD-004 (draft). Includes: GIR remediations, file naming normalization fixes, normative language corrections, and any structural changes.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

**Inputs Required**:
- GATE-002 approved analysis findings and GIR dispositions
- P-STD-004 (draft, post-GATE-001)

**Steps**:
1. Read GATE-002 verification artifact for approved dispositions.
2. Apply each approved GIR remediation to P-STD-004.
3. Apply file naming normalization amendments.
4. Apply normative language corrections.
5. Verify Specification Index is accurate after amendments.
6. Verify cross-scope references still conform to P-STD-005-CLAUSE-004.
7. Bump P-STD-004 version in frontmatter/Provenance.

**Success Criteria**:
- [ ] All GATE-002-approved GIR remediations applied
- [ ] File naming normalization amendments applied
- [ ] Specification Index accurate post-amendment
- [ ] Cross-scope references verified
- [ ] No normative semantic drift from proposal v3.4.0 intent

---

### Task TK003.1: Clarify Formal Reference vs Subclause Reference (P-STD-005)

**Task ID**: `P-PH000-ST001-AC004-TK003.1`

**Purpose**: Implement the GATE-002 disposition for GIR-010 by clarifying P-STD-005 reference semantics. Specifically: clarify that the full formal reference format applies to main CLAUSE IDs (and standard tokens) only, while subclause IDs may appear only as inline short-hand pointers.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

**Depends On**: GATE-002

**Inputs Required**:
- GATE-002-approved GIR-010 disposition (recorded in TK002.2 proposal)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

**Steps**:
1. Read the GIR-010 disposition as recorded in the TK002.2 proposal file.
2. Amend `P-STD-005-CLAUSE-004` to explicitly distinguish:
   - Full formal references (main CLAUSE IDs and standard tokens)
   - Subclause IDs as inline pointers only (not full-formal references)
3. Verify that the amended language does not introduce contradictions with existing cross-scope reference examples.
4. Bump P-STD-005 version in frontmatter/Provenance per P-STD-001 lifecycle rules.

**Success Criteria**:
- [ ] `P-STD-005-CLAUSE-004` explicitly constrains full formal references to main CLAUSE IDs and standard tokens
- [ ] Subclause pointer usage is clarified as inline short-hand only
- [ ] No contradictory examples remain in P-STD-005 References section

---

### Task TK003.2: (Superseded) Work Package — GIR-006 Stream-Only `analysis/` + `proposal/` Migration & Enforcement

**Task ID**: `P-PH000-ST001-AC004-TK003.2`

**Purpose**: **Cancelled (superseded)**. This task previously tracked migration/enforcement work to keep `analysis/` and `proposal/` stream-level only. It is superseded by the GATE-002 Client decision (2026-03-01) allowing activity-level `analysis/` and `proposal/` when placement matches `<scope-UID>` (implemented via TK003.4).

**Depends On**: GATE-002

**Deliverable**: — (cancelled)

**Inputs Required**: —

**Steps**: —

**Success Criteria**:
- [ ] Task is explicitly cancelled with supersession rationale recorded (Task Register Action + this task section).

---

### Task TK003.3: Work Package — GIR-011 `_gate-###` Verification Filename Normalization & Enforcement

**Task ID**: `P-PH000-ST001-AC004-TK003.3`

**Purpose**: Implement the approved GATE-002 disposition for GIR-011 by making the rename/enforcement work explicit and trackable within this activity plan while keeping execution in `T104-PH001-ST007`. This task produces a deterministic work package: (a) rename inventory/mapping for existing `-GATE-###` verification files, and (b) enforcement requirements to ensure T102’s first migration iteration conforms from the start.

**Depends On**: GATE-002

**Deliverable**:
- Work package content recorded under this task section and referenced from the GIR-011 disposition in `proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md`

**Inputs Required**:
- Repository scan inventory of non-conformant verification filenames (pattern: `verification_*-GATE-###*.md`)
- GATE-002 GIR-011 disposition (recorded in TK002.2 proposal)

**Work package (authoritative inventory + deterministic mapping)**:

**Rename rule**:
- Replace `-GATE-###` with `_gate-###` in verification filenames (underscore + lowercase qualifier).

**Authoritative inventory (repo scan)**:
The following files are the complete set of known `verification_*-GATE-###*.md` non-conformant instances (scan pattern `verification_*GATE-*.md` under `prompt/artifacts/tasks/`):

| Current path (non-conformant) | Rename target (conformant) |
|:--|:--|
| `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/verification/verification_P-PH000-ST001-AC002-GATE-002_tk005-supplement.md` | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/verification/verification_P-PH000-ST001-AC002_gate-002_tk005-supplement.md` |
| `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC001/verification/verification_P-PH000-ST004-AC001-GATE-002_report-acceptance_P-RES-001.md` | `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC001/verification/verification_P-PH000-ST004-AC001_gate-002_report-acceptance_P-RES-001.md` |
| `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC002/verification/verification_P-PH000-ST004-AC002-GATE-002_report-acceptance.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC002/verification/verification_P-PH000-ST004-AC002_gate-002_report-acceptance.md` |
| `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC002/verification/verification_P-PH000-ST004-AC002-GATE-002_report-acceptance_iteration-2.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC002/verification/verification_P-PH000-ST004-AC002_gate-002_report-acceptance_iteration-2.md` |
| `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004-GATE-001_commissioning-readiness.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-001_commissioning-readiness.md` |
| `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004-GATE-001_convention-compliance.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-001_convention-compliance.md` |
| `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004-GATE-001_p-migration-readiness.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-001_p-migration-readiness.md` |
| `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004-GATE-002_post-migration-quality.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-002_post-migration-quality.md` |

**Reference-update requirements**:
- For each renamed file, update any in-repo references that cite the old path/name, including (non-exhaustive): stream/activity plans, verification “Decision Reference” fields, notes registers, session notes, and any scripts that contain hard-coded paths.
- Minimum mechanical check: search for `-GATE-00` and update references to the new `_gate-00` paths.

**Enforcement requirements (T104-PH001-ST007 scope)**:
- Validators and migration/scaffolding tools MUST reject new verification artifacts using `-GATE-###` and MUST enforce `_gate-###`.
- T102 first-migration iteration MUST use `_gate-###` from the start (no `-GATE-###` legacy tolerance).

**Success Criteria Checklist**:
- [ ] Work package enumerates all known `-GATE-###` verification files (by exact path)
- [ ] Each item includes a deterministic rename target using `_gate-###`
- [ ] Enforcement requirements explicitly call out T102 first-migration strictness (no `-GATE-###`)

---

### Task TK003.4: Amend P-STD-004 — Activity-Level `analysis/` + `proposal/` Allowed with `<scope-UID>` Match

**Task ID**: `P-PH000-ST001-AC004-TK003.4`

**Purpose**: Implement the GATE-002 Client decision (2026-03-01) that `analysis/` and `proposal/` artifacts MAY be stored at **activity level** (and stream level) as long as directory placement matches the `<scope-UID>` used in the filename. This supersedes the prior stream-only restriction and resolves GIR-006 as a **spec change** rather than a migration/enforcement package.

**Depends On**: GATE-002

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

**Scope**:
- In scope:
  - Amend P-STD-004 to allow `analysis/` and `proposal/` directories at activity level.
  - Add a deterministic scope-alignment rule: placement MUST match `<scope-UID>` (e.g., AC-scoped filenames belong under their matching `AC###/`).
  - Update any contradictory illustrative workspace skeletons and placement bullets.
- Out of scope:
  - Moving/renaming existing artifacts to match the new rule (explicitly deferred).

**Inputs Required**:
- GATE-002 decisions as recorded in `proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md`
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`
- `prompt/scripts/validate_initiative_structure.py` (current placement enforcement behavior)

**Steps**:
1. Identify all P-STD-004 clauses that define analysis/proposal placement and update them to permit activity-level usage.
2. Add/adjust the normative scope-alignment rule tying `<scope-UID>` to placement.
3. Update illustrative skeleton(s) and any “stream-only” wording to match the new policy.

**Success Criteria**:
- [ ] P-STD-004 no longer prohibits activity-level `analysis/`/`proposal/` placement.
- [ ] A scope-alignment rule is normative and unambiguous (placement MUST match `<scope-UID>`).
- [ ] No illustrative skeleton contradicts the amended policy.

---

### Task TK004: Downstream Updates (SPS, workspace_documentation_rules.md, Binding Rule)

**Task ID**: `P-PH000-ST001-AC004-TK004`

**Purpose**: Update downstream artifacts to reference P-STD-004 as the authority surface: (1) program SPS P-STD-004 row, (2) `workspace_documentation_rules.md` §7 reference, (3) downstream adopter binding rule as a CLAUSE in P-STD-004.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (P-STD-004 row with Canonical Path)
- Updated `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (§7 reference)
- Updated P-STD-004 (binding rule CLAUSE)

**Inputs Required**:
- P-STD-004 (post-TK003)
- `sps_P-PROGRAM.md` (current state)
- `workspace_documentation_rules.md` (current state)

**Steps**:
1. Update `sps_P-PROGRAM.md` P-STD-004 row: set Canonical Path to `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`, set status, set effective date.
2. Update `workspace_documentation_rules.md` §7: replace the proposal reference with P-STD-004 canonical path. Retain the summary but indicate P-STD-004 is now the authority surface.
3. Add downstream adopter binding rule to P-STD-004: initiatives SHALL adopt P-STD-004 by reference and avoid duplicating directory/naming rules in local plans (link-don't-duplicate per `T104-CON-001`).

**Success Criteria**:
- [ ] SPS P-STD-004 row has resolvable Canonical Path
- [ ] `workspace_documentation_rules.md` §7 references P-STD-004 (not the proposal)
- [ ] Downstream binding rule exists as a normative CLAUSE in P-STD-004

---

### Task TK004.1: Evidence-First Package Audit (GATE-003 Readiness)

**Task ID**: `P-PH000-ST001-AC004-TK004.1`

**Purpose**: Perform an evidence-first audit (verification-style methodology) to confirm that the GATE-003 disposition proposal is complete, internally consistent, and ready for Client decision, without relying on producer claims. This is a readiness assessment that supports the GATE-003 review.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-003-package-audit.md`

**Inputs Required**:
- TK004.2 disposition proposal (draft)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md` — evidence-first methodology + findings discipline
- All artifacts listed in the TK004.2 proposal Evidence Set

**Steps**:
1. Independently verify each Evidence Set item exists and is correctly referenced (paths resolve).
2. Check disposition coverage: no known remediation surfaces are missing (tooling, naming enforcement, plan authority drift, rerun scope).
3. Check cross-plan dependency consistency: `plan_P-PH000-ST001-AC004.md` GATE-003 blocks TK005; ST007 AC004.1 is the named execution target.
4. Record any blocking gaps as findings to be resolved before presenting GATE-003.

**Success Criteria**:
- [ ] Audit artifact exists at deliverable path
- [ ] Findings are explicit and actionable (blocking vs non-blocking called out)
- [ ] Audit confirms the proposal is decision-ready OR explicitly lists required fixes

---


### Task TK004.2: Disposition Proposal (GATE-003 Greenlight Package for TK005)

**Task ID**: `P-PH000-ST001-AC004-TK004.2`

**Purpose**: Produce the decision-ready disposition package for **GATE-003** (“GATE-002.1” client label) to review and accept everything completed through TK004 (and the planned delta migration execution target `T104-PH001-ST007-AC004.1`) before authorizing TK005 implementation.

This task follows the “decision disposition proposal” pattern exemplar:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC008/proposal/proposal_T104-PH001-ST005-AC008-TK001.1_gir-disposition-package.md`

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/proposal/proposal_P-PH000-ST001-AC004-TK004.2_tk005-greenlight-disposition-package.md`

**Scope**:
- In scope:
  - Evidence-index and disposition of all remediation decisions required to align downstream execution with **P-STD-004** (including `_gate-###` enforcement, placement policy implications, archive tooling alignment, and validator/migrator enforcement deltas).
  - Canonical gate decision capture: the **GDR is embedded in the proposal** (Client decision signal is recorded there).
  - Explicit execution ownership + target location mapping (primary execution target: `T104-PH001-ST007-AC004.1`).
- Out of scope:
  - Executing remediations (belongs to ST007 `AC004.1`).
  - Modifying P-STD-004 itself (belongs to TK005/TK006/TK007 as applicable).

**Inputs Required**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` — governing authority surface
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` — `verification_..._gate-###.md` naming rule (`P-STD-005-CLAUSE-011E`)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/dev-report/dev-report_P-PH000-ST001-AC004_tk003-tk004-execution_2026-03-01.md` — implementation evidence for TK003–TK004
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` — downstream migration stream authority + dependency surface
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md` — prior P migration baseline (revision 1)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.1.md` — delta migration remediation plan (revision 2; execution target)

**Steps**:
1. Assemble an Evidence Set covering: P-STD-004 (post-TK004), dev-report(s), ST007 plan(s), and any known inventory/work packages (e.g., TK003.3 `_gate-###` mapping).
2. Enumerate all required remediation decisions as DEC items with options + recommendation + Client decision control.
3. Map each approved disposition to an execution target (task/owner) in `T104-PH001-ST007-AC004.1`.
4. Embed the Gate Decision Record (GDR) section as the canonical approval surface for GATE-003.

**Success Criteria**:
- [ ] Proposal deliverable exists and is decision-ready (DEC register + pre-selected recommendations)
- [ ] Evidence Set is explicit and complete enough to audit
- [ ] Every remediation disposition has an explicit execution target (owner + plan location)
- [ ] Proposal contains a populated `## Gate Decision Record` section with `Client Decision: pending` at author time

---


### GATE-003: Pre-TK005 Greenlight: Review + Remediation Dispositions

**Task ID**: `P-PH000-ST001-AC004-GATE-003`

**Purpose**: Confirm that all work through TK004 (and the planned delta migration remediation plan `T104-PH001-ST007-AC004.1`) is reviewable and disposition-ready, then record explicit Client approval (or conditions) before TK005 begins.

**Entry Criteria**:
- TK004 complete
- TK004.2 disposition proposal produced (includes embedded GDR with `Client Decision: pending`)
- TK004.1 evidence-first audit produced (no unresolved blocking gaps)

**Reviewer**: Client (facilitated by LLM_Consultant)

**Exit Criteria**:
- Client decision recorded in the GDR section of the TK004.2 proposal:
  - `Client Decision` is `APPROVE` or `APPROVE WITH CONDITIONS`
  - `Decision Date` populated
  - Conditions (if any) are enumerated and mapped to owning execution targets

---

### Task TK005: Incorporate P Migration Findings

**Task ID**: `P-PH000-ST001-AC004-TK005`

**Purpose**: Incorporate convention findings from the **P delta migration revision** (`T104-PH001-ST007-AC004.1`) into P-STD-004 as CLAUSE amendments or GIR register entries.

**Deliverable**:
- Updated P-STD-004 (if amendments needed)
- GIR register addendum (if new gaps/risks identified)

**Depends On**: GATE-003

**Inputs Required**:
- `T104-PH001-ST007-AC004.1` migration evidence (dev-report, validation report)
- P-STD-004 (post-TK004)

**Steps**:
1. Read P migration evidence (dev-report, validation output, any findings).
2. Cross-reference migration findings against P-STD-004 CLAUSEs.
3. For each finding: determine if it requires a CLAUSE amendment, a GIR entry, or is already addressed.
4. Apply any needed amendments.

**Success Criteria**:
- [ ] All P migration findings reviewed against P-STD-004 CLAUSEs
- [ ] Amendments applied or GIR entries created for unaddressed findings

---

### Task TK006: Incorporate T102 Migration Findings

**Task ID**: `P-PH000-ST001-AC004-TK006`

**Purpose**: Incorporate convention findings from the T102 directory migration (`T104-PH001-ST007-AC005`) into P-STD-004, particularly around the `consultant/` absorption and multi-epic manifest patterns.

**Deliverable**:
- Updated P-STD-004 (if amendments needed)
- GIR register addendum (if new gaps/risks identified)

**Depends On**: TK004, `T104-PH001-ST007-AC005` (T102 Directory Migration)

**Inputs Required**:
- `T104-PH001-ST007-AC005` migration evidence
- P-STD-004 (post-TK005)

**Steps**:
1. Read T102 migration evidence.
2. Cross-reference against P-STD-004 CLAUSEs (particularly: `consultant/` absorption patterns, multi-epic structure, `standard/` grandfathering).
3. Apply any needed amendments.
4. Verify T102 permanent-grandfathering posture is correctly captured in P-STD-004-ADR-001.

**Success Criteria**:
- [ ] All T102 migration findings reviewed against P-STD-004 CLAUSEs
- [ ] T102 permanent-grandfathering posture confirmed or amended in P-STD-004-ADR-001
- [ ] P-STD-004 validated against minimum 2 additional initiatives beyond T104 (P + T102 = P-RISK-002 satisfied)

---

### Task TK007: Produce Verification Evidence (GATE-004 Acceptance Readiness)

**Task ID**: `P-PH000-ST001-AC004-TK007`

**Purpose**: Produce independent gate verification evidence that P-STD-004 is ready for acceptance review at GATE-004, including: cross-initiative validation evidence status, remaining GIR items, and explicit deferrals (if any).

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-004.md`

**Inputs Required**:
- P-STD-004 (post-TK004)
- TK005/TK006 outputs (if completed) or deferral notes (if deferred)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- `prompt/templates/consultant/workspace/template_workspace_verification.md`

**Steps**:
1. Read P-STD-004 (post-TK004) and confirm it is the intended candidate for `accepted` promotion.
2. Verify cross-initiative validation evidence status for: T104 (exemplar), P, T102.
3. Verify GIR items are at terminal status (`resolved` or `accepted`) OR are explicitly proposed as deferrals with rationale.
4. Author the verification artifact using the verification template, including a Gate Recommendation and a GDR with `Client Decision: pending`.

**Success Criteria**:
- [ ] Verification artifact exists at the deliverable path
- [ ] Evidence Set lists P-STD-004 + validation evidence inputs + this plan
- [ ] Deferrals (if any) are explicitly enumerated and traceable to missing inputs
- [ ] GDR section present with `Client Decision: pending`

---

### GATE-004: Cross-Initiative Validation — P-STD-004 draft → accepted

**Task ID**: `P-PH000-ST001-AC004-GATE-004`

**Entry Criteria**:
- TK007 complete (verification evidence produced)
- P-STD-004 candidate for acceptance is post-TK004
- Cross-initiative validation evidence is available OR explicitly deferred (see Timebox rule below)

**Reviewer**: Client

**Exit Criteria**:
- P-RISK-002 mitigation confirmed (minimum 2 additional initiatives beyond T104 validated)
- No blocking GIR items remain
- Client approves P-STD-004 status change from `draft` to `accepted`
- Client decision recorded in the GDR section of `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-004.md`

**Timebox rule (7 days)**:
- If migration evidence required for TK005 and/or TK006 is not available within **7 calendar days** after TK004 completes, the missing items MUST be treated as explicit deferrals in TK007 (verdict may be `PASS WITH DEFERRALS`), and the Client MUST decide whether to (A) defer acceptance (keep P-STD-004 as `draft`) or (B) accept residual risk as an exception (recorded in GDR).

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | AC004 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/plan_P-PH000-ST001-AC004.md` |
| Plan | P Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| SSOT | Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Reference | P-STD-001 (governing standard) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Reference | P-STD-005 (reference semantics) | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| Reference | Authoring Guideline | `prompt/templates/consultant/standards/guideline_standard_specs.md` |
| Reference | Combined File Template | `prompt/templates/consultant/standards/template_standard_specs.md` |
| Reference | Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Reference | Verification Template | `prompt/templates/consultant/workspace/template_workspace_verification.md` |
| Input | Proposal v3.4.0 (primary seed) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` |
| Input | AC004 SES001 Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES001.md` |
| Input | AC004 SES002 Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES002.md` |
| Input | AC004 SES003 Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES003.md` |
| Downstream | workspace_documentation_rules.md | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Cross-stream | T104-PH001-ST007 (migration stream) | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| Downstream | T104 ST007 AC004.1 (P delta migration revision) | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.1.md` |
| Deliverable | P-STD-004 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| Deliverable | Post-seeding Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC004_p-std-004-proposal-seeding-assessment.md` |
| Deliverable | GIR Disposition Proposal (TK002.2) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md` |
| Deliverable | Disposition Proposal (TK004.2; GATE-003 decision record) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/proposal/proposal_P-PH000-ST001-AC004-TK004.2_tk005-greenlight-disposition-package.md` |
| Deliverable | GATE-003 Package Audit (TK004.1) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-003-package-audit.md` |
| Deliverable | External Review Analysis (GATE-002 package) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/analysis/analysis_P-PH000-ST001-AC004-GATE-002_external-review-disposition.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-26 | Initial | Activity plan created. Seed-First methodology (IEEE PAR + W3C Living CR pattern): rapid seed → post-seeding analysis → amendments → cross-initiative validation. 6 tasks + 3 gates. Evidence: AC004-SES002 consultation (2026-02-26). |
| v1.1.0 | 2026-02-26 | Amendment | Added TK-before-gate verification tasks (TK001.1, TK002.1, TK007) per verification guideline; updated gate dependencies and exit criteria to require GDR recording; added GATE-003 timebox rule (7 days) for migration evidence deferrals; added SES002 notes + verification guideline/template to context and links. |
| v1.2.0 | 2026-02-27 | Rebaseline | Rebaselined register statuses to enforce gate semantics: recorded GATE-001 APPROVE in GDR; committed TK002 analysis deliverable and TK002.1 verification evidence; set GATE-002 to `in_progress` pending Client GDR update; blocked TK003/TK004 until GATE-002 decision is recorded. |
| v1.3.0 | 2026-02-28 | Amendment | Added TK002.2 GIR disposition proposal deliverable for GATE-002 decision readiness; updated GATE-002 dependencies and entry/exit criteria; added TK003.1 follow-on task for GIR-010 (P-STD-005 reference clarification). |
| v1.4.0 | 2026-02-28 | Amendment | QA updates: added TK003.2 (GIR-006 stream-only `analysis/`/`proposal/` migration + enforcement work package) and TK003.3 (GIR-011 `_gate-###` rename + enforcement work package) so option (b) deferrals are explicitly planned/tracked in AC004 while execution remains in `T104-PH001-ST007`; aligns with secondary-vision cleanup for `P/**` and `T104/**` and strict first-migration conformance for `T102/**`. |
| v1.5.0 | 2026-03-01 | Amendment | GATE-002 package updates: added TK002.3 external review analysis deliverable; cancelled (superseded) TK003.2 stream-only migration work package; added TK003.4 placement-policy amendment task; added post–GATE-003 TK008 discussion task for agreeing ST007 plan update construction. |
| v1.6.0 | 2026-03-01 | Update | Recorded GATE-002 APPROVE in the task register; marked TK003/TK003.1/TK003.3/TK003.4 and TK004 as completed; expanded TK003.3 with an authoritative `-GATE-###` rename inventory and deterministic rename targets. |
| v1.7.0 | 2026-03-02 | Amendment | Inserted pre-TK005 greenlight gate (GATE-003; client label “GATE-002.1”) with disposition proposal (canonical GDR in proposal) + evidence-first package audit; re-identified acceptance gate as GATE-004; introduced downstream execution target `T104-PH001-ST007-AC004.1`; cancelled TK008 as superseded. |
| v1.8.0 | 2026-03-03 | Update | Executed TK004.2 and TK004.1 deliverables for GATE-003 readiness: normalized proposal artifact to TK004.2, produced verification-style evidence-first package audit, and updated task register actions/targets accordingly. |
