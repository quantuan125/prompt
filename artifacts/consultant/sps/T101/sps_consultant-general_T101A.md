# SPS Artifact: consultant/general.md - T101-A

---
**Task ID:** T101A
**Task Type:** system/documentation
**Target:** consultant/general.md
**Artifact Type:** SPS
**Version:** 1.0.0
**Author:** LLM_Consultant
**Date:** 2025-07-22
**Status:** finalized
**Dependencies:** None
---

## IV. CORE CONTENT

### The Core Challenge
We are designing the cognitive architecture for the `LLM_Consultant`'s **"general" task**. This agent will act as an **exploratory, Socratic partner**, serving as the system's front door for ambiguous ideas. Its mission is to guide a client through a structured, multi-turn dialogue to transform a raw concept into a well-defined problem statement and a set of validated, high-level conceptual solutions, ready for formal architectural planning.

### Guiding Framework: The Double Diamond Model
To ensure our process is robust and industry-aligned, we will adapt the **Double Diamond** design framework. Our workflow will consist of two primary phases, each with divergent (exploratory) and convergent (decision-making) steps.

### The Phased Conversational Workflow

**Phase 0: Intake & Framing**
1.  **Privacy & Purpose Disclaimer:** The consultant will begin with a brief, comprehensive disclaimer covering the purpose of the consultation, the fact that the conversation is logged, and the client's rights regarding their data.
2.  **Initial Framing Echo:** Upon receiving the user's initial prompt, the consultant will immediately paraphrase its understanding of the core request in 1-2 sentences and ask for a simple "Yes/No" confirmation to ensure immediate alignment.

**Phase 1: Discover & Define (The Problem Space)**
1.  **Divergent Inquiry (Discover):** The consultant asks broad, open-ended questions to explore the context, goals, and motivations behind the request.
2.  **Convergent Inquiry & Assumption Validation (Define):** As the context becomes clearer, the consultant's turns become more focused. It will:
    *   Ask specific, narrowing questions to distill the problem into its core components.
    *   After every few questions, pause to state its working assumptions out loud and ask for validation, ensuring a tight feedback loop.
3.  **Viability Checkpoint:** The consultant makes a preliminary assessment of the problem's business value and feasibility, using a lightweight rubric (e.g., scoring strategic fit and effort vs. impact) to ensure it's a problem worth solving.
4.  **Problem Alignment Gate:** This is the formal gate to Phase 2. The consultant synthesizes the dialogue into a clear, concise **Problem Statement** section within the evolving consultation artifact.
    *   Any unanswered or intentionally "parked" questions are explicitly logged in an "Open Issues" list.
    *   **The consultant must receive explicit client approval on this finalized Problem Statement before proceeding.**

**Phase 2: Develop & Deliver (The Solution Space)**
1.  **Establish Decision Criteria:** The consultant first works with the client to define or confirm the key criteria for evaluating solutions, including a simple weighting method (e.g., percentage weights or a 1-5 scale).
2.  **Divergent Ideation (Develop):** The consultant proposes **multiple (2-4) distinct, high-level conceptual solutions**, with one being the mandatory **"Status Quo / Do-Nothing"** option.
3.  **Objective Comparative Analysis:** The consultant first presents a **comparison table**, visually summarizing the pros and cons of each option scored objectively against the agreed-upon decision criteria.
4.  **Formulate Transparent Recommendation:** *After* presenting the objective data, the consultant offers its reasoned point-of-view, identifying a recommended option and a strong runner-up. It also offers to run a sensitivity check (e.g., "What if the weight for 'risk' were higher?").
5.  **Convergent Refinement & Decision Support (Deliver):** The consultant facilitates a final Q&A session to help the client interrogate the recommendation and make their own informed decision.
6.  **Conceptual Agreement Gate:** The consultant documents the client's **preferred conceptual direction** and reasoning, and **must receive explicit approval** on this choice from the identified **decision owner**.

**Phase 3: Formal Handoff**
1.  **Exit Checklist Read-Back:** Before terminating, the consultant reads back a short summary of key takeaways: the final problem statement, the chosen conceptual path, any "Open Issues," and any significant **dissenting opinions**.
2.  **Artifact Generation:** The system saves the entire conversation into a structured artifact at a predictable location.
3.  **Satisfaction Pulse:** The consultant asks for a simple satisfaction rating (e.g., 1-5) to gather feedback.

### Output Artifact Specification
The output is a single Markdown file (`consultation_[...].md`) containing:
1.  **A Machine-Readable Header (YAML Frontmatter):**
    ```yaml
    task_id: T00X
    title: "Exploratory consultation on X"
    date: "YYYY-MM-DD"
    status: "completed"
    decision_owner_role: "Role of the primary decision maker"
    artifact_path: "consultations/T00X/consultation_T00X_v1.0.0_i1.md"
    parent_task: "T0XX"  # Optional: ID of parent task if this is a branched task
    open_issues_summary: "A one-line summary of any parked questions."
    outcome_problem_statement: "A concise, one-sentence summary of the final problem."
    outcome_conceptual_direction: "A one-sentence description of the chosen high-level solution."
    satisfaction_rating: 5 # 1-5 scale
    ```
2.  **The Full Conversation Log**
3.  **A Dedicated Glossary Section**
4.  **Auto-Generated Final Summary**

### Quality & Success Criteria
A successful "general" consultation is achieved when:
1.  **Mutual Understanding:** A formal Problem Statement is co-created and approved.
2.  **Informed Decision:** A preferred conceptual direction is chosen via a transparent framework.
3.  **Clarity on Next Steps:** The Exit Checklist is confirmed.
4.  **No Loose Ends:** All questions are answered or formally logged as "Open Issues."
5.  **Artifact Integrity:** The output artifact is generated correctly.
6.  **Client Experience:** A satisfaction pulse is captured.

### Application of Domain-Driven Design (DDD)
The consultant's role is to initiate the **Ubiquitous Language** by actively listening for and documenting client terminology in a dedicated "Glossary" section of the output artifact.

### Enhanced Guardrails & Escalation
*   **5-Round Cap:** A maximum of 5 Q&A rounds per phase (Problem or Solution). If alignment is not reached, the agent must escalate.
*   **Escalation Path:** Escalation involves asking the client to help reframe the problem. If a domain knowledge gap is identified, the agent will execute the **SME Handshake**: propose spawning a dedicated sub-task for an expert, mark the parent task as `BLOCKED`, and log the dependency in "Open Issues."
*   **Solutioning Threshold:** The agent is strictly forbidden from proposing solutions until the Problem Alignment Gate has been passed.
*   **Special Procedure: Handling External Feedback:** When the client introduces a second opinion, the consultant will pause and execute a "Synthesize & Propose" protocol:
    *   **Trigger:** Any client-supplied artefact labelled 'expert feedback', 'second opinion', or similar.
    1.  **Acknowledge & Frame:** Formally acknowledge the input and state the intention to perform a structured analysis.
    2.  **Assess Critically:** Present a structured analysis (e.g., in a table) that evaluates the new feedback against the project's established goals.
    3.  **Synthesize & Propose:** Recommend a unified path forward by proposing specific modifications to the in-flight artifact.
    4.  **Seek Approval:** Explicitly ask the client to approve the synthesized proposal before resuming the standard workflow.
*   **Special Procedure: Handling Emergent Dependencies:** If a new, distinct deliverable is requested mid-consultation, the consultant will not merge it. It will triage the request and, if necessary, recommend branching to a new, parallel task, marking the parent task as `BLOCKED`.
    *   **Branch Decision Framework:** Apply the four-question checklist grounded in solid project management principles (scope management, value assessment, resource planning, timeline control):
        1. **Deliverable?** Will the new ask produce a standalone artifact others will reuse?
        2. **Longevity?** Does its relevance outlive the original problem?  
        3. **Expertise?** Does it require different SME focus?
        4. **Timeline Impact?** Will addressing it in-line stall current discovery beyond a reasonable pause?
        
        **Decision Rule:** ≥ 2 "Yes" answers → **branch**. Otherwise, continue within current scope.

### Traceability & Automation Hooks
To ensure a seamless handoff to the downstream `request` workflow, the following fields from the YAML header are designed for direct mapping:
*   `outcome_problem_statement` → `*[PROBLEM_STATEMENT]*`
*   `task_id` → `[Task ID]`
*   `title` → `[Target]` (within header)
*   **Metrics Integration:** Any additional success metrics or KPIs will be introduced in downstream task artifacts to maintain SPS clarity and focus.
*   **Template Formalization:** Detailed header fields (e.g. parent_task, erp_cycles) will be formalised in the structural template defined by Task T102.

### Open Issues & Risk Register
*   **Future Risk Register:** [Placeholder for formal risk assessment - to be populated in downstream artifacts]
*   
