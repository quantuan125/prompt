---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
version: '1.0.0'
date: '2025-11-22'
status: 'draft'
author: 'LLM_Consultant (Sub-Consultant)'
decision_owner_role: 'Client'
source_epic: 'T810A-SYSTEM'
target_request: 'request_T810A1-PROMPT.md'
source_handoff: 'handoff_brief_T810A1-PROMPT_epic-changes.md'
---

# CONSULTANCY PLAN: T810A1 Epic Changes Integration

## I. EXECUTIVE SUMMARY

This plan defines how to integrate Epic T810A Phase 2/3/4 changes into the T810A1 Request (`request_T810A1-PROMPT.md`) in a way that is fully compliant with `T102-STD-004 (Decision Records Index)` and `T102-STD-005 (ID Specification & Rules)`. It translates the epic-level handoff brief into concrete editing steps and design proposals that an LLM_Developer can follow without re-running the full analysis.

The plan focuses on four main outcomes:
- Clean separation between **inherited Epic governance** (27 E‑RIDs + Epic GDRs/RES/ADRs) and **feature-specific deltas** (T810A1 F‑RIDs and F‑GDRs).
- Restructured Sections III.E–III.N in the Request to reflect promotion/demotion decisions and the new Inherited Considerations model.
- Explicit, T102-compliant treatment of T810A1-specific requirements and decisions (retained F‑RIDs and demoted F‑GDRs).
- A manual, traceable mapping between old and new IDs and references, suitable for future automation.

---

## II. PHASE OVERVIEW

| Phase | Objective | Key Deliverables | Duration Estimate |
|:------|:----------|:----------------|:------------------|
| **Phase 0** | Standards & Baseline Review | T102-STD-004/005 checklist; confirmed Epic vs Feature authority set | 0.5–1.0 h |
| **Phase 1** | Section Restructuring & Inheritance Table | New Sections III.E/III.F; 8-row Inherited Considerations table | 1.5–2.0 h |
| **Phase 2** | F‑RID Cleanup & Renumbering | Updated ASSUM/DEP/NFR/CON sections; manual old→new mapping | 2.0–3.0 h |
| **Phase 3** | Governance Integration (F‑GDRs + Story References) | New Feature Governance Decisions section; updated S05/S06/S07/S08 refs | 2.0–3.0 h |
| **Phase 4** | Issues & Risks Alignment | Confirmed III.N Open Issues & Risks content/format post-renumber | 0.5–1.0 h |
| **Phase 5** | ID & Reference Validation + Handoff | Full-document ID/reference audit; implementation checklist for LLM_Developer | 1.0–1.5 h |

**Total Estimated Duration** (analysis + update): 7.5–11.5 hours.

---

## III. PHASE 0 — STANDARDS & BASELINE REVIEW

**Objective:** Ensure all later edits obey `T102-STD-004` and `T102-STD-005` and that the T810A1 team has a shared understanding of which rules live at Epic vs Feature scope.

### A. T102-STD-004 (Decision Records Index) — Implementation Rules

**Scope in this plan**
- Applies to:  
  - Epic GDRs already in `sps_T810-GASTRO.md`.  
  - New Feature Governance Decisions section in T810A1 with `T810A1-GDR-001` and `T810A1-GDR-002`.

**Key rules to enforce**
1. **Index schema** (FR‑001)  
   - Use a table with columns: `GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor`.  
   - IDs: `T810A1-GDR-001`, `T810A1-GDR-002`.  
   - Title: short, Title Case, 2–8 words.  
   - Status: use `{Proposed, Accepted, Deprecated}`; for demoted GDRs, treat as `Accepted` unless Client directs otherwise.  
   - Owner: `Client`.  
   - Effective: ISO date `YYYY-MM-DD` matching handoff (e.g., `2025-10-27`).  
   - Supersedes: `—` for now.  
   - Anchor: lower‑kebab, e.g. `#t810a1-gdr-001-tracking-first-clinical-protocol`.

2. **GDR body structure** (FR‑002)  
   - Immediately under the table, create a list item per GDR:  
     `* **T810A1-GDR-001 (Tracking-First Clinical Protocol)** {#t810a1-gdr-001-tracking-first-clinical-protocol}`  
   - Shared subheadings (bold labels with trailing periods):  
     - **Context:** first sentence may cite Epic GDR/ADR authority if relevant.  
     - **Decision:** clear, imperative policy; if it adopts an ADR, say `Adopt <ADR-ID> ...` per FR‑005.  
     - **Consequences:** (+)/(±)/(-) bullets.  
     - **References:** canonical IDs to SPS/Concept/Request items.  
   - Do **not** add ADR-only fields (Specification, Alternatives, Provenance) here; T810A1 GDRs stay at GDR level.

3. **Placement & cross-artifact linking** (FR‑003/FR‑005)  
   - Place Feature GDRs in a dedicated section `Feature Governance Decisions` within the Request; do not scatter them into stories.  
   - Use ID-only references in stories (e.g., `` `T810A1-GDR-001` ``) and let readers navigate to the GDR body.

### B. T102-STD-005 (ID Specification & Rules) — Implementation Rules

**Scope in this plan**
- Governs all IDs in the updated Request: E‑RIDs, F‑RIDs, F‑GDRs, Issues, Risks, Stories, etc.

**Key rules to enforce**
1. **Scope vs Rule IDs (FR‑001/FR‑002)**  
   - Scope IDs (I/E/F/S): keep existing `T810`, `T810A`, `T810A1`, `T810A1-Sxx`.  
   - Rule IDs (RIDs): maintain category tokens (`ASSUM`, `DEP`, `CON`, `QG`, `NFR`, `IF`, `INT`, `ISSUE`, `RISK`, `GDR`).  
   - Decision IDs: `T810A1-GDR-###`; no ADRs within the Request.

2. **Precedence & directionality (FR‑003)**  
   - Epic RIDs and GDRs **govern** Feature IDs; T810A1 must not redefine Epic rules.  
   - T810A1 RIDs may implement or refine Epic rules but must not contradict them; variances would require ADRs in Concept (out of scope for this plan).

3. **ID categories and renumbering (FR‑004)**  
   - Within each Feature category (ASSUM, DEP, NFR, CON, IF, INT, ISSUE, RISK), IDs must be contiguous starting from `001` after cleanup.  
   - When promoting/deleting F‑RIDs, do not leave gaps; renumber retained items and update all references.

4. **Reference syntax & inheritance contract** (FR‑006 and Concept guidance)  
   - Use backticks for ID references in prose and tables: `` `T810A-QG-001` ``, `` `T810A1-NFR-003` ``.  
   - Use the **Inherited Considerations table** as the contract for Epic inheritance:  
     - Table row per category, listing all Epic IDs rather than copying their text.  
     - Downstream sections reference these Epic IDs instead of inlining Epic content.

**Deliverable for Phase 0**
- A short, internal checklist summarizing the items above, attached as comments at the top of this plan or as a local note for the implementing LLM_Developer.

---

## IV. PHASE 1 — SECTION RESTRUCTURING & INHERITANCE TABLE

**Objective:** Restructure Section III of the Request so that Epic‑level rules are inherited via a single, well-formed table (III.E), while feature-specific assumptions and dependencies are cleanly isolated (III.F).

### A. Section Splits & Renumbering

1. **Split current Section III.E**  
   - Replace the existing `### E. Inheritences, Assumptions & Dependencies` block with two sections:  
     - `### E. Inherited Considerations` — table only.  
     - `### F. Assumptions & Dependencies` — feature-specific items only.

2. **Cascade renumbering**  
   - After introducing the new III.F, renumber subsequent sections:  
     - Old III.F → new III.G,  
     - Old III.G → new III.H,  
     - Old III.H → new III.I,  
     - Old III.I → new III.J,  
     - Old III.J → new III.K,  
     - Old III.K → new III.L,  
     - Old III.L → new III.N,  
     - Old III.M → new III.O.  
   - Update any internal references that mention section letters (e.g., “Section III.L”).

### B. Inherited Considerations Table (III.E)

**Table format**  
- Use exactly the following columns: `Source Artifact | Source ID | Category | Inherited Rule IDs`.  
- Use 8 rows to group 35 inherited items:
  - Assumptions (4 E‑RIDs).  
  - Dependencies (5 E‑RIDs).  
  - Constraints (4 E‑RIDs).  
  - Quality Goals (8 E‑RIDs).  
  - Implementation Guidance (6 E‑RIDs).  
  - Governance (4 E‑GDRs, per SPS; see QA below).  
  - Research (2 E‑RES).  
  - Architecture (3 E‑ADRs).

**Authority set and QA resolution**
- Use `sps_T810-GASTRO.md` as the authoritative source for Epic governance:  
  - Governance row: `T810A-GDR-001…004` from SPS, not the earlier handoff typo (`T810A-GDR-005`).  
  - Research row: `T810A-RES-001`, `T810A-RES-002`.  
  - Architecture row: `T810A-ADR-001`, `T810A-ADR-003`, `T810A-ADR-004`.
- For each row, list IDs and titles as concise inline items, e.g.:  
  - `T810A-QG-001 (Clinical Protocol Reliability)`, `T810A-QG-002 (Persona & Tone)`, …  
  - Do not copy full GDR/ADR bodies into the Request.

### C. Feature-Specific Assumptions & Dependencies (III.F)

**Scope:** Only items that remain feature-specific after promotion.

1. **Assumptions**  
   - Remove `T810A1-ASSUM-001/002/003` entirely; these are now Epic assumptions (`T810A-ASSUM-001…003`).  
   - Retain and renumber `T810A1-ASSUM-004` as `T810A1-ASSUM-001`.  
   - **Proposal (content-preserving refinement):**  
     - Title: change to `Session-Scoped Memory Model`.  
     - First sentence: explicitly state that it **implements** `T810A-ASSUM-004 (Platform Memory Uncertainty)` for this Feature, e.g.:  
       - “This Feature implements Epic assumption `T810A-ASSUM-004` by treating ChatGPT’s cross-session memory as non-authoritative, relying on session-scoped state plus Stable JSON profile as the canonical source.”

2. **Dependencies**  
   - Remove `T810A1-DEP-001…005` entirely; these are now Epic dependencies (`T810A-DEP-001…005`).  
   - Retain and renumber `T810A1-DEP-008` as `T810A1-DEP-001`.  
   - **Proposal (content-preserving refinement):**  
     - Emphasise its nature as a **research dependency**, not platform or schema dependency.  
     - Add an explicit reference to Epic `T810A-IG-001 (Protocol Triggering Guidance)` to show that this dependency supports the implementation of that Epic guidance in S05.

---

## V. PHASE 2 — F‑RID CLEANUP & RENUMBERING

**Objective:** Remove all promoted F‑RIDs from the Request, renumber the retained ones for each category, and update references everywhere they are used (especially in Stories S01–S10).

### A. Non-Functional Requirements (NFRs)

**Current retained NFRs**
- `T810A1-NFR-001` (Protocol Reliability) — hybrid with `T810A-QG-001`.  
+- `T810A1-NFR-002` (Persona & Tone) — hybrid with `T810A-QG-002`.  
+- `T810A1-NFR-005` (Maintainability) — hybrid with `T810A-QG-005`.  
+- `T810A1-NFR-008` (Protocol Triggering Intelligence)` — feature-specific.  
+- `T810A1-NFR-009` (Probe Phase Enforcement)` — feature-specific.

**Renumbering plan**
- Delete `T810A1-NFR-003`, `NFR-004`, `NFR-006`, `NFR-007` entirely (now Epic QGs).  
- Keep the following IDs post-renumber:  
  - `T810A1-NFR-001` — unchanged.  
  - `T810A1-NFR-002` — unchanged.  
  - `T810A1-NFR-005` → `T810A1-NFR-003`.  
  - `T810A1-NFR-008` → `T810A1-NFR-004`.  
  - `T810A1-NFR-009` → `T810A1-NFR-005`.

**Content-preserving refinement proposals**
1. **NFR-001 (Protocol Reliability)**  
   - Add an opening sentence: “This Feature implements Epic quality goal `T810A-QG-001 (Clinical Protocol Reliability)` by specifying a 5-phase execution pattern for LLM_Gastro.”  
   - Keep the detailed loop description unchanged.

2. **NFR-002 (Persona & Tone)**  
   - Add a reference line tying back to `T810A-QG-002 (Persona & Tone)`.  
   - Clarify that this NFR defines **phase-specific tone mapping** for this Feature (e.g., Tracking vs Probe vs Coach), not the global persona definition.

3. **NFR-003 (renamed from NFR-005, Maintainability)**  
   - Reframe as: “Implementation of `T810A-QG-005 (Architecture Maintainability)` via a 9-block prompt structure.”  
   - Preserve the assurance that all future changes should be made via block-level edits rather than ad-hoc rewriting.

4. **NFR-004 (renamed from NFR-008, Protocol Triggering Intelligence)**  
   - Explicitly reference `T810A-IG-001 (Protocol Triggering Guidance)` and position this NFR as the Feature’s concrete 3‑way classification scheme (Tracking-only / Full Protocol / Simple Q&A).  
   - Keep the detailed triggers unchanged.

5. **NFR-005 (renamed from NFR-009, Probe Phase Enforcement)**  
   - Explicitly reference `T810A-QG-008 (Clarification Over Guessing)` and `T810A-IG-002 (Probe Phase Enforcement)`.  
   - Emphasise that this NFR encodes the **minimum 2-loop** pattern and Anti-Patterns for T810A1.

**Cross-reference updates**
- Update all references in Stories, Interfaces, and Integration Notes to use the new NFR IDs.  
- Example: where S05 currently cites `T810A1-NFR-008` for triggering logic, update to `T810A1-NFR-004`; where S06 references `NFR-009`, update to `NFR-005`.

### B. Constraints (CONs)

**Current retained constraints**
- `T810A1-CON-002` (Risk Acceptance).  
+- `T810A1-CON-003` (Open Knowledge Base).  
+- `T810A1-CON-005` (Tooling Deferral).

**Renumbering plan**
- Delete `T810A1-CON-001`, `CON-004`, `CON-006`, `CON-007`, `CON-008` (now Epic CONs/QGs).  
- Renumber retained constraints:  
  - `T810A1-CON-002` → `T810A1-CON-001`.  
  - `T810A1-CON-003` → `T810A1-CON-002`.  
  - `T810A1-CON-005` → `T810A1-CON-003`.

**Content-preserving refinement proposals**
1. **CON-001 (Risk Acceptance)**  
   - Clarify this is a **user-level acceptance** constraint specific to T810A1’s use of ChatGPT, not an Epic-wide risk policy.  
   - Add a reference to `T810A-CON-003 (Clinical Compliance Deferral)` in the description to show alignment.

2. **CON-002 (Open Knowledge Base)**  
   - Clarify that general training + search tools are allowed **within ChatGPT’s governance bounds** per `T810A-CON-002 (Platform Compatibility)`.  
   - Make explicit that this constraint does not override Epic-level restrictions on knowledge sources.

3. **CON-003 (Tooling Deferral)**  
   - Reframe as a feature-level constraint tied to `T810A-DEP-003 (Toolbox Interface)` and `T810A-CON-001 (System Prompt Scope)`.  
   - Suggest a short note in the description, e.g., “This constraint operationalises the Epic decision to defer custom tool integrations to Feature `T810A4`.”

### C. Interfaces & Integration Notes (for completeness)

**Interfaces (IFs)**
- Retain `T810A1-IF-001…006`; no renumbering.  
- Update descriptions to add Epic IG references per handoff:  
  - `IF-003` → reference `T810A-IG-003 (Explicit Classification)` and `T810A-QG-007`.  
  - `IF-004` → reference `T810A-IG-001 (Protocol Triggering Guidance)`.  
  - `IF-005` → reference `T810A-IG-006 (Session Context Injection & Handoff)`.  
  - `IF-006` → reference `T810A-IG-004 (Dynamic JSON Single-Entry Pattern)`.

**Integration Notes (INTs)**
- Retain `T810A1-INT-001…005`; no renumbering.  
- Update descriptions with Epic references:  
  - `INT-002` → `T810A-IG-006`.  
  - `INT-004` → `T810A-DEP-004` and `T810A-IG-004`.  
  - `INT-005` → `T810A-IG-005`.

### D. Manual Old→New ID Mapping

**Deliverable**
- Create a small table (in this plan or as an appendix in the Request) mapping **old F‑RID IDs to new IDs** for all retained items, e.g.:  
  - `T810A1-ASSUM-004` → `T810A1-ASSUM-001`.  
  - `T810A1-DEP-008` → `T810A1-DEP-001`.  
  - `T810A1-NFR-005` → `T810A1-NFR-003`.  
  - `T810A1-NFR-008` → `T810A1-NFR-004`.  
  - `T810A1-NFR-009` → `T810A1-NFR-005`.  
  - `T810A1-CON-002` → `T810A1-CON-001`, etc.
- This mapping is **manual by design** (per QA) and will support future automated linting without introducing tooling now.

---

## VI. PHASE 3 — GOVERNANCE INTEGRATION (F‑GDRs + STORY REFERENCES)

**Objective:** Integrate demoted GDRs as Feature-level governance decisions (T810A1-GDR-001/002) and realign story-level references (especially S05/S06/S07/S08) with the new inheritance structure.

### A. Feature Governance Decisions Section

**Placement**
- Insert a new section `Feature Governance Decisions` after Feature Integration Notes and before Stories & Specification.  
- After Phase 1 renumbering, this section is targeted to be **Section III.K**, but final letter should be validated once all headings are in place.

**Index table**
- Add a table following T102-STD-004 FR‑001:

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T810A1-GDR-001` | Tracking-First Clinical Protocol | Accepted | Client | 2025-10-27 | — | #t810a1-gdr-001-tracking-first-clinical-protocol |
| `T810A1-GDR-002` | Session Workflow Architecture | Accepted | Client | 2025-10-27 | — | #t810a1-gdr-002-session-workflow |

**Bodies**
- Under the table, insert full GDR bodies from the handoff brief (Phase 3 Demoted GDR content), normalised as follows:
  - Ensure each uses the list-item + bold heading + anchor pattern.  
  - Add explicit **Context** link back to the Epic GDRs where relevant, e.g.:  
    - “Per `T810A-GDR-001` and `T810A-QG-001`, this Feature specifies a concrete 5-phase tracking-first protocol with a minimum 2-loop pattern.”  
  - In **Decision**, keep the feature-specific mechanics (5-phase protocol, 2-loop minimum, first-session vs daily-session flows).  
  - In **Consequences**, highlight the impact on S05, S07, and the Execution Protocol’s strictness (prevention over recovery).  
  - In **References**, include both Epic IDs (QGs/IGs/ADRs) and key Feature IDs (relevant NFRs and INTs).

### B. Proposals for Retained F‑GDRs (Content-Preserving)

1. **T810A1-GDR-001 (Tracking-First Clinical Protocol)**  
   - **Scope:** Governs S05 Execution Protocol and NFR-001/NFR-005.  
   - **Context (proposal):**  
     - Start with “Per `T810A-QG-001` and `T810A-IG-002`, a consistent tracking-first conversational pattern is required to ensure clinical reliability and sufficient probing before coaching.”  
   - **Decision (proposal):**  
     - Codify: 5-phase protocol; minimum 2-loop pattern; Probe-before-Coach gating; no numeric confidence in user-facing text (but allow internal JSON numeric confidence per `T810A-ADR-001`).  
   - **Consequences (proposal highlights):**  
     - (+) Reduces risk of premature coaching (aligns with S06 anti-patterns).  
     - (±) May require patient education and longer initial sessions.  
     - (-) Increases implementation complexity in S05.  
   - **References:**  
     - Epic: `T810A-QG-001`, `T810A-QG-008`, `T810A-IG-001`, `T810A-IG-002`, `T810A-ADR-001`.  
     - Feature: `T810A1-NFR-001`, `T810A1-NFR-005`, `T810A1-S05-*`, `T810A1-IF-006`.

2. **T810A1-GDR-002 (Session Workflow Architecture)**  
   - **Scope:** Governs session lifecycle: Step 0 Memory Review, Stable/Dynamic JSON loading, first-session vs daily-session flows.  
   - **Context (proposal):**  
     - Start with “Per `T810A-GDR-002`, `T810A-IG-004`, `T810A-IG-005`, and `T810A-IG-006`, features must define a consistent session workflow architecture matching Stable/Dynamic JSON split and session context injection patterns.”  
   - **Decision (proposal):**  
     - Codify:  
       - First session hybrid onboarding (profile creation, expectation setting).  
       - Daily session pattern (Memory review → load Stable JSON → load previous report → run protocol).  
       - Dual-output report (`INT-002`) as the default handoff artifact.  
   - **Consequences (proposal highlights):**  
     - (+) Enables cross-session continuity and manual JSON persistence.  
     - (±) Introduces a strong dependency on T810A2 schemas for Stable/Dynamic JSON.  
     - (-) Adds complexity to S05 and S09 story specifications.  
   - **References:**  
     - Epic: `T810A-GDR-002`, `T810A-GDR-003`, `T810A-IG-004`, `T810A-IG-005`, `T810A-IG-006`.  
     - Feature: `T810A1-INT-002`, `T810A1-INT-004`, `T810A1-INT-005`, `T810A1-S05-*`, `T810A1-S09-*`.

### C. Updating S05/S06/S07/S08 References

**Execution Protocol (S05)**  
- Replace vague “per GDR-001/002/003” language with explicit ID references:  
  - Use `T810A-IG-002` for Probe enforcement rules.  
  - Use `T810A-IG-004` for Dynamic JSON single-entry pattern.  
  - Use `T810A-ADR-001` and `T810A-QG-007` for confidence communication constraints.  
  - Use `T810A1-GDR-001` and `T810A1-GDR-002` for feature-specific execution choices (loop count, Step 0, step ordering).

**Behavioral Guardrails (S06)**  
- Ensure all no-guessing and anti-pattern examples reference Epic `T810A-QG-008` but tie enforcement back to `T810A1-NFR-005` and `T810A1-GDR-001`.

**Quality Criteria (S07)**  
- Update NFR references to use new IDs (NFR-001…005).  
- When citing general quality goals, point to `T810A-QG-*` instead of the deleted NFR-003/004/006/007.

**Exemplars (S08)**  
- Ensure exemplars:  
  - Demonstrate ≥2 Probe questions before coaching.  
  - Demonstrate qualitative confidence language, no numeric percentages.  
  - Include at least one first-session and one daily-session example that align with `T810A1-GDR-002`.

---

## VII. PHASE 4 — ISSUES & RISKS ALIGNMENT

**Objective:** Confirm that the Open Issues & Risks section in T810A1 matches the demoted content from the Epic and remains structurally correct after section renumbering.

### A. Content Verification

1. **Issues**  
   - Verify `T810A1-ISSUE-001…004` in the Request match wording, Owner, Status, Priority, and dates from the handoff’s Phase 4 demoted Issues.  
   - Confirm the table format aligns with T102 template (Issues header, 8 columns).

2. **Risks**  
   - Verify `T810A1-RISK-001…005` match the demoted risks definitions from the handoff.  
   - Confirm Status and Priority values are unchanged.

### B. Section Renumbering & References

- Ensure section heading changes from `### L. Open Issues & Risks` to `### N. Open Issues & Risks` (post earlier insertions).  
- Update any cross-references (if present) that point to “Section III.L” to instead point to “Section III.N”.

---

## VIII. PHASE 5 — ID & REFERENCE VALIDATION + HANDOFF

**Objective:** Perform a full-document sanity check on IDs and references and create a concise checklist for LLM_Developer to validate after implementation.

### A. Validation Checklist (Per T102-STD-004/005)

1. **Section structure**
   - [ ] Section III.E is table-only `Inherited Considerations` with 8 rows and 35 inherited items.  
   - [ ] Section III.F contains only feature-specific ASSUM/DEP after cleanup.  
   - [ ] Section headings from III.E through III.O follow the expected cascade.

2. **F‑RID content & numbering**
   - [ ] All promoted F‑RIDs (20 items) are removed from the Request.  
   - [ ] Retained F‑RIDs are renumbered to start at 001 in each category with no gaps.  
   - [ ] All references to old IDs are updated to new IDs or Epic IDs as appropriate.

3. **Epic reference integration**
   - [ ] Interfaces and Integration Notes descriptions include required Epic IG/DEP references.  
   - [ ] Stories S05–S07 point to Epic QGs/IGs/ADRs instead of deleted NFR/CON IDs.

4. **Feature Governance Decisions**
   - [ ] New Feature Governance Decisions section exists with T102-STD-004-compliant index and bodies for `T810A1-GDR-001/002`.  
   - [ ] S05 and related stories use `T810A1-GDR-001/002` consistently when referring to Feature-level policies.

5. **Issues & Risks**
   - [ ] Open Issues & Risks section (III.N) content matches handoff text and SPS demotion decisions.  
   - [ ] Table formats match T102 Issues/Risks guidance.

6. **ID semantics**
   - [ ] All IDs follow `T102-STD-005` category tokens and patterns.  
   - [ ] All ID references in prose and tables use backticks.

### B. Handoff Notes for LLM_Developer

Provide LLM_Developer with:
- This plan file as the canonical implementation guide for T810A1 Epic changes integration.  
- The manual old→new ID mapping table.  
- A note to treat `sps_T810-GASTRO.md` as the authority when resolving discrepancies between earlier drafts and the handoff brief (e.g., GDR-005 typo).

---

## IX. OPEN QUESTIONS & DECISION POINTS

The following items require Client/Epic consultant confirmation before or during implementation:

1. **Confidence Policy Wording in S05:**  
   - Should the Execution Protocol explicitly restate the numeric confidence prohibition and internal numeric usage rules from `T810A-ADR-001`, or simply reference the ADR and rely on Epic-level wording?

2. **Placement of Old→New ID Mapping Table:**  
   - Do you prefer this mapping to live in the Request (e.g., in Appendix V) for long-term traceability, or remain only in internal workspace notes like this plan?

3. **Degree of Textual Trimming for Hybrid NFRs/CONs:**  
   - For NFR-001/002/003 and CON-001/002/003, is it acceptable to add short “implements Epic <ID>” lead-in sentences (as proposed) and otherwise keep existing text intact, or should we also compress repetitive phrasing to further reduce duplication?

