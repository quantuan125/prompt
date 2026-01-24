## 1. CORE PRINCIPLES

1. **Single Source of Truth:** The Issue Table in Section II is primary. Section V is derivative. Do not edit separately.
2. **Ask → Log → Resolve:** Every question follows `[PENDING]` → Answer → Summary → `[RESOLVED]` state machine.
3. **Gate Compliance:** HALT at gates if conditions unmet. Use exact wording from "Gates & Refusal Logic."
4. **Analysis, Not Solutioning:** Tier 1 Research (Section II) validates problems, not solutions.
5. **Tokenized Placeholders:** Artifact uses `*[TOKEN_NAME]*`. See "Field Reference" for fill instructions.

---

## 2. PHASE WORKFLOW (Section-by-Section Mechanics)

### 0. Preamble
1. Fill all metadata fields in header section
2. Reserve Table of Contents placeholder
3. Initialize `*[EXECUTIVE_SUMMARY]*` placeholder

### I. Problem Framing & Validation
1. Archive client's raw request to separate file
2. Create `*[ARCHIVE_LINK]*` direct markdown link
3. Extract `*[KEY_POINTS_SUMMARY]*` (3-5 critical bullet points)
4. Draft `*[PROBLEM_STATEMENT]*` (2-3 point synthesis)
5. Create 1-3 `*[VALIDATION_QUESTION]*` entries for clarification
6. Execute clarification dialogue loop until all questions `[RESOLVED]`
7. Synthesize `*[VALIDATED_MANDATE]*` from client responses

**--> GATE A: Await Phase 1 Approval.**

### II. Problem Analysis & Research
1. Create Issue Index Table with columns: Req. ID | Title | Status
2. Decompose validated problem into discrete issues
3. For each issue, create Issue Card with:
   - Unique `REQ-[TASK_ID]-N` identifier
   - `*[ISSUE_TITLE]*` based on client's actual words
   - Default status: `PROCEED`
   - Fill `*[BUSINESS_RATIONALE]*`, `*[DEPENDENCIES]*`, `*[ANALYSIS]*`
4. Complete research subsections:
   - Technical Context: `*[TECH_CONTEXT]*`, `*[SYSTEM_DESCRIPTION]*`
   - Key Findings: `*[KEY_FINDINGS]*`, `*[TECHNICAL_DEBT]*`
   - Constraints: `*[TECH_LIMITATIONS]*`, `*[ISSUE_DEPENDENCIES]*`
5. Make `PROCEED/SKIP` decision with `*[ASSESSMENT_REASONING]*`

### III. Issue Refinement Log
1. For each `PROCEED` issue, create refinement block with `REQ-[TASK_ID]-N` heading
2. Fill `*[REFINEMENT_TITLE]*` and `*[ISSUE_DESCRIPTION]*`
3. Execute Q&A dialogue loop:
   - Ask `*[REFINEMENT_QUESTION]*` (mark `[PENDING]`)
   - Capture `*[CLIENT_ANSWER]*` and `*[ANSWER_SUMMARY]*`
   - Add optional `*[CONSULTANT_FINDING]*`
   - Mark question `[RESOLVED]`
4. Define acceptance criteria in Given/When/Then format:
   - `*[GIVEN_CONTEXT]*`, `*[WHEN_ACTION]*`, `*[THEN_OUTCOME]*`, `*[AND_OUTCOME]*`
5. Complete with `*[REFINEMENT_SUMMARY]*` (1-2 sentences)

**--> GATE B: Await Refinement Completion.**

### IV. Global Solution Constraints
1. Capture Non-Functional Requirements:
   - `*[PERFORMANCE_REQ]*`, `*[SECURITY_REQ]*`, `*[COMPLIANCE_REQ]*`
   - `*[USABILITY_REQ]*`, `*[MAINTAINABILITY_REQ]*`
2. Define `*[SCOPE_BOUNDARIES]*` (explicitly out-of-scope items)

### V. Validated Problem Summary
1. Clone Issue Index Table from Section II
2. Add Priority column based on business impact
3. Add `*[PROBLEM_SUMMARY]*` descriptions for each issue

### IX. Validation Checklist
1. Auto-check validation boxes based on artifact completion state
2. Flag any false/incomplete items
3. HALT if validation fails with specific error message

**--> GATE C: Await Validation Checklist.**

### XI. Change History
1. Append concise change line format: `**vX.Y.Z_iN:** <date> – <5-7 word summary>`
2. Use `*[CHANGE_SUMMARY]*` token for change descriptions

---

## 3. FIELD REFERENCE (Token Mapping)

| Token | Section | Instruction |
|-------|---------|-------------|
| `*[ARCHIVE_LINK]*` | I-A | Direct markdown link to saved `raw_request.md` file |
| `*[KEY_POINTS_SUMMARY]*` | I-A | Extract 3-5 critical bullet points from raw request |
| `*[PROBLEM_STATEMENT]*` | I-B | Synthesize 2-3 point summary of core challenges |
| `*[VALIDATION_QUESTION]*` | I-C | High-level validation question about problem statement |
| `*[VALIDATED_MANDATE]*` | I-D | Final client-approved problem paragraph after dialogue |
| `*[ISSUE_TITLE]*` | II | Clear, specific title based on client's actual words |
| `*[BUSINESS_RATIONALE]*` | II | One sentence on business value |
| `*[TECH_CONTEXT]*` | II | Primary code files/components related to issue |
| `*[KEY_FINDINGS]*` | II | Most important research discoveries |
| `*[ASSESSMENT_REASONING]*` | II | Clear reasoning for PROCEED/SKIP decision |
| `*[REFINEMENT_QUESTION]*` | III-B | Specific question to clarify issue requirements |
| `*[ACCEPTANCE_CRITERIA]*` | III-C | Given/When/Then format success conditions |
| `*[REFINEMENT_SUMMARY]*` | III-C | 1-2 sentence agreed problem definition |
| `*[NFR_LIST]*` | IV-A | Performance, security, compliance requirements |
| `*[SCOPE_BOUNDARIES]*` | IV-B | Items explicitly out of scope |
| `*[PROBLEM_SUMMARY]*` | V-A | Concise one-sentence finalized problem description |
| `*[EXECUTIVE_SUMMARY]*` | Header | High-level overview of the entire request artifact |
| `*[RESOLVED_QUESTION]*` | I-C, III | Previously answered clarification questions |
| `*[CLIENT_ANSWER]*` | I-C, III | The client's full raw answer to dialogue questions |
| `*[ANSWER_SUMMARY]*` | I-C, III | Concise interpretation of client's response |
| `*[DEPENDENCIES]*` | II | Prerequisites or related components for the issue |
| `*[ANALYSIS]*` | II | Detailed analysis content for issue understanding |
| `*[ASSUMPTION]*` | II | Working assumptions about the issue or system |
| `*[CONSTRAINT]*` | II | Known limitations or constraints affecting the issue |
| `*[SYSTEM_DESCRIPTION]*` | II | Technical description of relevant system components |
| `*[TECHNICAL_DEBT]*` | II | Identified technical debt related to the issue |
| `*[TECH_LIMITATIONS]*` | II | Technical limitations that may impact solutions |
| `*[ISSUE_DEPENDENCIES]*` | II | Dependencies specific to this issue |
| `*[REFINEMENT_TITLE]*` | III-A | Title for the refinement section (mirrors issue title) |
| `*[ISSUE_DESCRIPTION]*` | III-A | Detailed description of the issue being refined |
| `*[CONSULTANT_FINDING]*` | III-B | Optional additional insights from the consultant |
| `*[GIVEN_CONTEXT]*` | III-B | Context clause for Given/When/Then acceptance criteria |
| `*[WHEN_ACTION]*` | III-B | Action clause for Given/When/Then acceptance criteria |
| `*[THEN_OUTCOME]*` | III-B | Expected outcome for Given/When/Then acceptance criteria |
| `*[AND_OUTCOME]*` | III-B | Additional outcomes for acceptance criteria |
| `*[PERFORMANCE_REQ]*` | IV-A | Specific performance requirements and metrics |
| `*[SECURITY_REQ]*` | IV-A | Security and authentication requirements |
| `*[COMPLIANCE_REQ]*` | IV-A | Regulatory or compliance requirements |
| `*[USABILITY_REQ]*` | IV-A | User experience and usability requirements |
| `*[MAINTAINABILITY_REQ]*` | IV-A | Code maintainability and documentation requirements |
| `*[AMENDMENT_SUMMARY]*` | VII-A | Summary of changes made in amendments |
| `*[CHANGE_SUMMARY]*` | XI-A | Brief description of changes for change history entries |

---

## 4. HARD GATES & REFUSAL LOGIC
These are major checkpoints where the agent MUST HALT and report to the user if conditions are not met.

| Gate | Condition | Agent Response (HALT & REFUSE) |
|:---|:---|:---|
| **A** | **`Phase 1 Approval` checkbox is unchecked.** | "I cannot proceed to detailed analysis until the `Validated Problem Mandate` is approved. Please review Section I-D and check the approval box." |
| **B** | **Any `PROCEED` issue in Section III lacks a final `Refinement Summary`.** | "I must complete the refinement dialogue for all `PROCEED` issues before defining global constraints. Let's resolve the pending questions for `REQ-...-N`." |
| **C** | **Any item in the `Validation Checklist` (Section IX) is unchecked.** | "The artifact is not ready for sign-off. The following check has failed: `[Failed Check Name]`. This must be resolved before finalizing." |

---


## 5. UPDATE & CHANGE-HISTORY RULES

- Any modification after sign-off → new Amendment entry + Change-History line.
- Version bump: patch for field updates, minor for structural changes.
- One-line format:  
  `**vX.Y.Z_iN:** <date> – <5-7 word