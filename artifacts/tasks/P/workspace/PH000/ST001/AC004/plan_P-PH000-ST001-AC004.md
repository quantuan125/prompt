---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC004'
version: '1.1.0'
date: '2026-02-26'
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

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `P-PH000-ST001-AC004-TK001` | Rapid Seed: Structural Promotion of Proposal v3.4.0 to P-STD-004 (draft) | `planned` | LLM_Developer | — | `standard_P-STD-004_...md` | Proposal v3.4.0, P-STD-001, P-STD-005, `guideline_standard_specs.md` | — |
| TK001.1 | `P-PH000-ST001-AC004-TK001.1` | Produce Verification Evidence (GATE-001 readiness) | `planned` | LLM_Reviewer | TK001 | `verification_P-PH000-ST001-AC004_gate-001.md` | `guideline_workspace_verification.md`, `template_workspace_verification.md` | — |
| GATE-001 | `P-PH000-ST001-AC004-GATE-001` | Client Review of Seeded P-STD-004 (draft) | `planned` | Client | TK001.1 | Pass/fail | — | — |
| TK002 | `P-PH000-ST001-AC004-TK002` | Post-Seeding Gap/Risk/Issues Analysis | `planned` | LLM_Consultant | GATE-001 | `analysis_P-PH000-ST001-AC004_...md` | P-STD-004 (draft), P-STD-001, P-STD-005 | — |
| TK002.1 | `P-PH000-ST001-AC004-TK002.1` | Produce Verification Evidence (GATE-002 readiness) | `planned` | LLM_Reviewer | TK002 | `verification_P-PH000-ST001-AC004_gate-002.md` | `guideline_workspace_verification.md`, `template_workspace_verification.md` | — |
| GATE-002 | `P-PH000-ST001-AC004-GATE-002` | Client Review of Analysis Findings | `planned` | Client | TK002.1 | Pass/fail | — | — |
| TK003 | `P-PH000-ST001-AC004-TK003` | Apply Analysis-Driven CLAUSE Amendments | `planned` | LLM_Developer | GATE-002 | `standard_P-STD-004_...md` | GATE-002 approved findings | — |
| TK004 | `P-PH000-ST001-AC004-TK004` | Downstream Updates (SPS, workspace_documentation_rules.md, Binding Rule) | `planned` | LLM_Consultant | TK003 | `sps_P-PROGRAM.md`, `workspace_documentation_rules.md`, P-STD-004 | — | — |
| TK005 | `P-PH000-ST001-AC004-TK005` | Incorporate P Migration Findings | `planned` | LLM_Consultant | TK004, `T104-PH001-ST007-AC004` | `standard_P-STD-004_...md` | P migration evidence | — |
| TK006 | `P-PH000-ST001-AC004-TK006` | Incorporate T102 Migration Findings | `planned` | LLM_Consultant | TK004, `T104-PH001-ST007-AC005` | `standard_P-STD-004_...md` | T102 migration evidence | — |
| TK007 | `P-PH000-ST001-AC004-TK007` | Produce Verification Evidence (GATE-003 acceptance readiness) | `planned` | LLM_Reviewer | TK004 | `verification_P-PH000-ST001-AC004_gate-003.md` | `guideline_workspace_verification.md`, `template_workspace_verification.md` | — |
| GATE-003 | `P-PH000-ST001-AC004-GATE-003` | Cross-Initiative Validation: P-STD-004 draft → accepted | `planned` | Client | TK007 | Pass/fail | P-RISK-002 | — |

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
  - Analysis/proposal stream-level restriction: Encode as normative CLAUSE — `analysis/` and `proposal/` are stream-level ONLY (client decision from SES002)
  - Specification Index per P-STD-001-CLAUSE-002 (expected >5 CLAUSEs)
  - Cross-scope references per P-STD-005-CLAUSE-004 (External Reference lines)
- Out of scope:
  - Proposal amendment (v3.4.0 is final input)
  - Normative content beyond what is in the proposal
  - Cross-initiative validation (GATE-003)

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
   - Convention 4 (Timeline Hierarchy) → CLAUSE(s) for workspace timeline structure + type subdirectory rules. **MUST explicitly state**: `analysis/` and `proposal/` are stream-level ONLY; activity-level type subdirectories are restricted to `snotes/`, `raw/`, `verification/`, `dev-report/`. (Client decision SES002)
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
- [ ] Analysis/proposal stream-level restriction encoded as normative CLAUSE
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

### GATE-002: Client Review of Analysis Findings

**Task ID**: `P-PH000-ST001-AC004-GATE-002`

**Entry Criteria**:
- TK002.1 complete (verification evidence produced)
- Analysis artifact fully authored

**Reviewer**: Client

**Exit Criteria**:
- Client approves GIR dispositions (resolve/accept/defer per item)
- Client approves file naming normalization recommendations
- No blocking findings remain unaddressed
- Client decision recorded in the GDR section of `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-002.md`

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

### Task TK005: Incorporate P Migration Findings

**Task ID**: `P-PH000-ST001-AC004-TK005`

**Purpose**: Incorporate convention findings from the P directory migration (`T104-PH001-ST007-AC004`) into P-STD-004 as CLAUSE amendments or GIR register entries.

**Deliverable**:
- Updated P-STD-004 (if amendments needed)
- GIR register addendum (if new gaps/risks identified)

**Depends On**: TK004, `T104-PH001-ST007-AC004` (Script Enhancement + P Directory Migration)

**Inputs Required**:
- `T104-PH001-ST007-AC004` migration evidence (dev-report, validation report)
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

### Task TK007: Produce Verification Evidence (GATE-003 Acceptance Readiness)

**Task ID**: `P-PH000-ST001-AC004-TK007`

**Purpose**: Produce independent gate verification evidence that P-STD-004 is ready for acceptance review at GATE-003, including: cross-initiative validation evidence status, remaining GIR items, and explicit deferrals (if any).

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-003.md`

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

### GATE-003: Cross-Initiative Validation — P-STD-004 draft → accepted

**Task ID**: `P-PH000-ST001-AC004-GATE-003`

**Entry Criteria**:
- TK007 complete (verification evidence produced)
- P-STD-004 candidate for acceptance is post-TK004
- Cross-initiative validation evidence is available OR explicitly deferred (see Timebox rule below)

**Reviewer**: Client

**Exit Criteria**:
- P-RISK-002 mitigation confirmed (minimum 2 additional initiatives beyond T104 validated)
- No blocking GIR items remain
- Client approves P-STD-004 status change from `draft` to `accepted`
- Client decision recorded in the GDR section of `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-003.md`

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
| Downstream | workspace_documentation_rules.md | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Cross-stream | T104-PH001-ST007 (migration stream) | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| Deliverable | P-STD-004 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| Deliverable | Post-seeding Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC004_p-std-004-proposal-seeding-assessment.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-26 | Initial | Activity plan created. Seed-First methodology (IEEE PAR + W3C Living CR pattern): rapid seed → post-seeding analysis → amendments → cross-initiative validation. 6 tasks + 3 gates. Evidence: AC004-SES002 consultation (2026-02-26). |
| v1.1.0 | 2026-02-26 | Amendment | Added TK-before-gate verification tasks (TK001.1, TK002.1, TK007) per verification guideline; updated gate dependencies and exit criteria to require GDR recording; added GATE-003 timebox rule (7 days) for migration evidence deferrals; added SES002 notes + verification guideline/template to context and links. |
