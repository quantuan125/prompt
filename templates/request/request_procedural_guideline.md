## 1. CORE PRINCIPLES

1. **Single Source of Truth:** The Issue Table in Section II is primary. Section V is derivative. Do not edit separately.
2. **Ask → Log → Resolve:** Every question follows `[PENDING]` → Answer → Summary → `[RESOLVED]` state machine.
3. **Gate Compliance:** HALT at gates if conditions unmet. Use exact wording from "Gates & Refusal Logic."
4. **Analysis, Not Solutioning:** Tier 1 Research (Section II) validates problems, not solutions.
5. **Tokenized Placeholders:** Artifact uses `*[TOKEN_NAME]*`. See "Field Reference" for fill instructions.

---

## 2. CORE CONTENT WORKFLOW 
<!-- BEGIN SCOPE: create_request
   knowledge: 
     - "prompt/templates/request/request_structural_template.md"
   prereq:
      - "The task is new and no request artifact for this task_id exists."
   success:
      - "A new request artifact exists."
      - "Section A1-A3 are populated (P1 met)."
      - "After P1 met, A4 is synthesized."
      - "Gate A is present and ready for client approval"
-->

### A. Problem Framing & Validation
1.  Archive the raw request; populate `*[ARCHIVE_LINK]*` and `*[KEY_POINTS_SUMMARY]*`.
2.  Synthesize the initial `*[PROBLEM_STATEMENT]*`.
3.  Ask 1-2 `*[VALIDATION_QUESTION]*`s to clarify the problem statement.
4.  Execute the `General Clarification Dialogue` loop until **P1** is met (all questions are `[RESOLVED]`).
5.  **AFTER P1 is met,** synthesize the final `*[VALIDATED_MANDATE]*` from the completed dialogue.
**--> GATE A: Await Mandate Approval.**
<!-- END SCOPE: create_request -->

<!-- BEGIN SCOPE: research_request
   knowledge:
      - "The current request artifact."
   prereq:
      - "Gate A is passed."
   success:
      - "The `Issue Index Table` is populated."
      - "An Issue Card with a final `PROCEED` or `SKIP` assessment exists for each issue."
      - "For every `PROCEED` issue:"
        - "A new `Refinement Log` block has been scaffolded in Section C."
        - "An initial `*[REFINEMENT_QUESTION]*` is populated for each new Refinement Log, ready for the next phase."
      - "Gate B is present and ready for client approval."
-->
### B. Problem Analysis & Research
1. Create Issue Index Table with columns: `Req. ID | Title | Status`
2. Decompose validated problem into discrete issues
3. For each issue, create and fully populate a corresponding `Issue Card`, including Analysis, Research, and a final `Assessment`.
4. **AFTER all issues in Section B are assessed,** scaffold the `Refinement Log` in Section C by creating a block for each `PROCEED` issue and populating it with initial, high-level `*[REFINEMENT_QUESTION]*`
**--> GATE B: Await Analysis & Research Approval.**
<!-- END SCOPE: research_request -->

<!-- BEGIN SCOPE: refine_request
   knowledge:
      - "The current request artifact."
   prereq:
      - "Gate B is passed"
   success:
      - "For every `PROCEED` issue:
        -  "All questions are `[RESOLVED]` in the `Refinement Dialogue` (P2 met)"
        - "After P2 met, `Acceptance Criteria` are defined and `Refinement Summary` is written."
      - "Gate C is present and ready for client approval."
-->
### C. Issue Refinement Log
1.  For each `PROCEED` issue, execute the `Refinement Dialogue` Q&A loop until **P2** is met following:
   - Ask `*[REFINEMENT_QUESTION]*` (mark `[PENDING]`)
   - Capture `*[CLIENT_ANSWER]*` and `*[ANSWER_SUMMARY]*`
   - Add optional `*[CONSULTANT_FINDING]*`
   - Mark question `[RESOLVED]`
2.  **AFTER P2 is met for an issue,** initiate a new, collaborative dialogue with the client to define and populate the `Acceptance Criteria` for that issue.
3.  Once ACs are defined, write the final `*[REFINEMENT_SUMMARY]*` for that issue.
4.  Repeat for all `PROCEED` issues.

**--> GATE C: Await Refinement Approval.**
<!-- END SCOPE: refine_request -->

<!-- BEGIN SCOPE: finalize_request
   knowledge:
      - "The current request artifact."
   prereq:
      - "Gate C is passed."
   success:
      - "Section D is generated. (P3 met)"
      - "After P3 met, Section E is is fully and collaboratively populated."
      - "Gate D is present and ready for client approval."
      - "The Core Content of the artifact is complete."
-->

### D. Validated Problem Summary
1. Clone Issue Index Table from Section II
2. Add Priority column based on business impact
3. Add `*[PROBLEM_SUMMARY]*` descriptions for each issue

### E. Global Solution Constraints
1. **AFTER P3 is met** (the summary table is complete), initiate a new, collaborative dialogue with the client to define and populate all NFRs and `*[SCOPE_BOUNDARIES]*` in Section E.
**--> GATE D: Await Global Constraints Approval.**
<!-- END SCOPE: finalize_request -->

---

## 3. FIELD REFERENCE (Token Mapping)

### **Table 1: Tokens Within "IV. CORE CONTENT"**

| Token | Subsection | Instruction |
|-------|------------|-------------|
| `*[ARCHIVE_LINK]*` | IV-A | Direct markdown link to saved `raw_request.md` file |
| `*[KEY_POINTS_SUMMARY]*` | IV-A | Extract 3-5 critical bullet points from raw request |
| `*[PROBLEM_STATEMENT]*` | IV-A | Synthesize 2-3 point summary of core challenges |
| `*[VALIDATION_QUESTION]*` | IV-A | High-level validation question about problem statement |
| `*[RESOLVED_QUESTION]*` | IV-A, IV-C | Previously answered clarification questions |
| `*[CLIENT_ANSWER]*` | IV-A, IV-C | The client's full raw answer to dialogue questions |
| `*[ANSWER_SUMMARY]*` | IV-A, IV-C | Concise interpretation of client's response |
| `*[VALIDATED_MANDATE]*` | IV-A | Final client-approved problem paragraph after dialogue |
| `*[ISSUE_TITLE]*` | IV-B | Clear, specific title based on client's actual words |
| `*[BUSINESS_RATIONALE]*` | IV-B | One sentence on business value |
| `*[DEPENDENCIES]*` | IV-B | Prerequisites or related components for the issue |
| `*[ANALYSIS]*` | IV-B | Detailed analysis content for issue understanding |
| `*[ASSUMPTION]*` | IV-B | Working assumptions about the issue or system |
| `*[CONSTRAINT]*` | IV-B | Known limitations or constraints affecting the issue |
| `*[TECH_CONTEXT]*` | IV-B | Primary code files/components related to issue |
| `*[SYSTEM_DESCRIPTION]*` | IV-B | Technical description of relevant system components |
| `*[KEY_FINDINGS]*` | IV-B | Most important research discoveries |
| `*[TECHNICAL_DEBT]*` | IV-B | Identified technical debt related to the issue |
| `*[TECH_LIMITATIONS]*` | IV-B | Technical limitations that may impact solutions |
| `*[ISSUE_DEPENDENCIES]*` | IV-B | Dependencies specific to this issue |
| `*[ASSESSMENT_REASONING]*` | IV-B | Clear reasoning for PROCEED/SKIP decision |
| `*[REFINEMENT_TITLE]*` | IV-C | Title for the refinement section (mirrors issue title) |
| `*[ISSUE_DESCRIPTION]*` | IV-C | Detailed description of the issue being refined |
| `*[REFINEMENT_QUESTION]*` | IV-C | Specific question to clarify issue requirements |
| `*[CONSULTANT_FINDING]*` | IV-C | Optional additional insights from the consultant |
| `*[GIVEN_CONTEXT]*` | IV-C | Context clause for Given/When/Then acceptance criteria |
| `*[WHEN_ACTION]*` | IV-C | Action clause for Given/When/Then acceptance criteria |
| `*[THEN_OUTCOME]*` | IV-C | Expected outcome for Given/When/Then acceptance criteria |
| `*[AND_OUTCOME]*` | IV-C | Additional outcomes for acceptance criteria |
| `*[REFINEMENT_SUMMARY]*` | IV-C | 1-2 sentence agreed problem definition |
| `*[PROBLEM_SUMMARY]*` | IV-D | Concise one-sentence finalized problem description |
| `*[PERFORMANCE_REQ]*` | IV-E | Specific performance requirements and metrics |
| `*[SECURITY_REQ]*` | IV-E | Security and authentication requirements |
| `*[COMPLIANCE_REQ]*` | IV-E | Regulatory or compliance requirements |
| `*[USABILITY_REQ]*` | IV-E | User experience and usability requirements |
| `*[MAINTAINABILITY_REQ]*` | IV-E | Code maintainability and documentation requirements |
| `*[SCOPE_BOUNDARIES]*` | IV-E | Items explicitly out of scope |

### **Table 2: Tokens Outside "IV. CORE CONTENT"**

| Token | Section | Instruction |
|-------|---------|-------------|
| `[Target]` | Header | Target component or system name |
| `[Task ID]` | Header | Unique task identifier |
| `[TASK_ID]` | I-Metadata | Task identifier for requirement IDs |
| `[system/component/documentation/testing]` | I-Metadata | Category of task type |
| `[component_name/document_name]` | I-Metadata | Specific target name |
| `[X.Y.Z]` | I-Metadata, X-Changelog | Version number |
| `[LLM Role]` | I-Metadata | Author role (Consultant, Analyst, etc.) |
| `[YYYY-MM-DD]` | I-Metadata, VI-Appendix | Date in ISO format |
| `[in_progress/ready_for_review/approved]` | I-Metadata | Current status of the request |
| `[List of prerequisite tasks or components]` | I-Metadata | Dependencies for this request |
| `*[EXECUTIVE_SUMMARY]*` | II | High-level overview of the entire request artifact |
| `*[Client Name]*` | VI-Appendix | Client name for amendment log |
| `*[AMENDMENT_SUMMARY]*` | VI-Appendix | Summary of changes made in amendments |
| `*[CHANGE_SUMMARY]*` | X-Changelog | Brief description of changes for change history entries |

---

## 4. GATE LOGIC & REFUSAL MESSAGES
*   **Procedural Gates (P-Gates)** are internal workflow markers, implemented as HTML comments. They guide the agent's next action without halting.
*   **Hard Gates (H-Gates)** are major phase checkpoints, implemented as visible checkboxes. They require explicit human approval and will cause the agent to HALT if their conditions are not met.

| Gate ID | Gate Type | Condition / Trigger | Agent Action / Refusal Message |
|:---|:---|:---|:---|
| **P1** | Procedural | All questions in `General Clarification Dialogue` are `[RESOLVED]`. | **Proceed:** Synthesize the `Validated Problem Mandate`. |
| **P2** | Procedural | All questions in an issue's `Refinement Dialogue` are `[RESOLVED]`. | **Proceed:** Engage the client to collaboratively define `Acceptance Criteria` for that specific issue. |
| **P3** | Procedural | The `Validated Problem Summary` (Section D) has been generated. | **Proceed:** Engage the client to collaboratively define `Global Solution Constraints` (Section E). |
| **A** | Hard | **`Gate A: Mandate Approval` checkbox is unchecked.** | **HALT & REFUSE:** "I cannot proceed to detailed analysis until the `Validated Problem Mandate` is approved. Please review and check the box in Section A.4." |
| **B** | Hard | **`Gate B: Analysis & Research Approval` checkbox is unchecked.** | **HALT & REFUSE:** "I must have approval for the completed analysis and initial questions before we can begin the deep refinement. Please review Section B and check the box." |
| **C** | Hard | **`Gate C: Refinement Approval` checkbox is unchecked.** | **HALT & REFUSE:** "I must have approval for all refined issues before we can define global constraints. Please review the completed refinements in Section C and check the box." |
| **D** | Hard | **`Gate D: Global Constraints Approval` checkbox is unchecked.** | **HALT & REFUSE:** "Before the Core Content is considered complete, we must have approval on the final NFRs and Scope. Please review Section E and check the box." |

---


## 5. UPDATE & CHANGE-HISTORY RULES

<!-- BEGIN SCOPE: update_request
   knowledge:
      - "The current request artifact."
   prereq:
      - "The request artifact already exists."
      - "A specific change request has been provided."
   success:
      - "The requested change is applied to the artifact."
      - "A new entry is added to the Amendment Log (if applicable)."
      - "A new, correctly formatted line is appended to the Changelog."
-->
- Any modification to a signed-off artifact requires a new entry in the `Amendment Log`.
- ALL modifications (initial creation and subsequent updates) require a new, timestamped entry in the `Changelog`.
- **Changelog Format:** `**vX.Y.Z_iN:** <YYYY-MM-DD> – <Concise 5-7 word summary of the change>`
<!-- END SCOPE: update_request -->