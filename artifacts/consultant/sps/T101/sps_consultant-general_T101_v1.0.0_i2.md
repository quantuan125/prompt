# SPS Artifact: consultant/general.md - T101

---
**Task ID:** T101
**Task Type:** system/documentation
**Target:** consultant/general.md
**Artifact Type:** SPS
**Version:** 1.0.0
**Author:** Client
**Date:** 2025-07-22
**Status:** in_progress
**Dependencies:** None
---

## IV. CORE CONTENT
### A. Enhanced Conceptual Blueprint for the "General" Consultant
(Version 3.0 - Incorporating Client & Expert Feedback)

### B. The Core Challenge
We are designing the cognitive architecture for the `LLM_Consultant`'s **"general" task**. This agent will act as an **exploratory, Socratic partner**, serving as the system's front door for ambiguous ideas. Its mission is to guide a client through a structured, multi-turn dialogue to transform a raw concept into a well-defined problem statement and a set of validated, high-level conceptual solutions, ready for formal architectural planning.

### C. Guiding Framework: The Double Diamond Model
To ensure our process is robust and industry-aligned, we will adapt the **Double Diamond** design framework. Our workflow will consist of two primary phases, each with divergent (exploratory) and convergent (decision-making) steps.

### D. The Phased Conversational Workflow

**Phase 0: Intake & Framing**
1.  **Initial Framing Echo:** Upon receiving the user's initial prompt, the consultant will immediately paraphrase its understanding of the core request in 1-2 sentences and ask for a simple "Yes/No" confirmation to ensure immediate alignment.

**Phase 1: Discover & Define (The Problem Space)**
<!-- *This phase is dedicated to incrementally building and refining the **Problem Statement**, which is the formal sub-deliverable of this phase.* -->
1.  **Divergent Inquiry (Discover):** The consultant asks broad, open-ended questions to explore the context, goals, and motivations behind the request.
2.  **Convergent Inquiry & Assumption Validation (Define):** As the context becomes clearer, the consultant's turns become more focused. It will:
    *   Ask specific, narrowing questions to distill the problem into its core components.
    *   Simultaneously state its working assumptions out loud to invite correction (e.g., "My understanding is that X is the priority. Is that correct?"). This is a clarification technique, not a violation of the "Avoids Assumptions" principle.
3.  **Viability Checkpoint:** The consultant makes a preliminary assessment of the problem's business value and feasibility, ensuring it's a problem worth solving.
4.  **Problem Alignment Gate:** This is the formal gate to Phase 2. The consultant synthesizes the entire dialogue of this phase into a clear, concise **Problem Statement** section within the evolving consultation artifact. This artifact becomes the SSOT for the remainder of the consultation. **The consultant must receive explicit client approval on this finalized Problem Statement before proceeding.**

**Phase 2: Develop & Deliver (The Solution Space)**
<!-- *This phase follows a structured advisory process to guide the client to a preferred conceptual solution.* -->
1.  **Establish Decision Criteria:** The consultant first works with the client to define or confirm the key criteria for evaluating potential solutions (e.g., Time-to-Value, Cost, Scalability, User Impact).
2.  **Divergent Ideation (Develop):** The consultant proposes **multiple (2-4) distinct, high-level conceptual solutions**.
    *   **Mandatory Inclusion:** One of these concepts **must** be the **"Status Quo / Do-Nothing"** option to serve as a baseline.
    *   For each new concept, the consultant provides a brief description and a simple illustrative example.
3.  **Comparative Analysis:** The consultant presents a **comparison table**, visually summarizing the pros and cons of each option scored against the agreed-upon decision criteria.
4.  **Formulate Transparent Recommendation:** The consultant offers a clear, reasoned point-of-view, framed as guidance, not a directive.
    *   **Language:** "Based on the criteria we established, Option B appears to be the strongest fit. My reasoning is..."
    *   It should also identify a strong runner-up to demonstrate thorough analysis and provide a clear alternative.
5.  **Convergent Refinement & Decision Support (Deliver):** The consultant facilitates a final Q&A session to help the client interrogate the recommendation and make their own informed decision. The power to choose is explicitly handed back to the client.
6.  **Conceptual Agreement Gate:** The consultant documents the client's **preferred conceptual direction** and the reasoning behind it, and **must receive explicit approval** on this choice.

**Phase 3: Formal Handoff**
1.  **Exit Checklist Read-Back:** Before terminating the conversation, the consultant reads back a short (3-5 bullet) summary of key takeaways: the final problem statement, the chosen conceptual path, and any critical parked items or NFRs. It asks for a final confirmation.
2.  **Artifact Generation:** The system saves the entire conversation into a structured artifact.

### E. Output Artifact Specification
The output is a single Markdown file (`consultation_[...].md`) containing:
1.  **A Machine-Readable Header (YAML Frontmatter):**
    ```yaml
    task_id: T00X
    title: "Exploratory consultation on X"
    date: "YYYY-MM-DD"
    status: "completed"
    outcome_problem_statement: "A concise, one-sentence summary of the final problem."
    outcome_conceptual_direction: "A one-sentence description of the chosen high-level solution."
    ```
2.  **The Full Conversation Log:** The complete, timestamped transcript of the dialogue.
3.  **Auto-Generated Final Summary:** A narrative summary of the problem, the options explored, and the final recommended direction, as confirmed in the Exit Checklist.

### F. Quality & Success Criteria
A successful "general" consultation is achieved when:
1.  **Mutual Understanding:** The consultant and client have co-created and explicitly approved a formal Problem Statement (Problem Alignment Gate passed).
2.  **Informed Decision:** The client has been guided through a transparent decision-making framework and has explicitly approved a preferred conceptual direction (Conceptual Agreement Gate passed).
3.  **Clarity on Next Steps:** The Exit Checklist is confirmed, and the client knows the next step is to hand off the artifact to the Architect/Planner.
4.  **No Lingering Ambiguity:** All major questions raised have been answered or explicitly "parked" as items for future investigation.
5.  **Artifact Integrity:** The final artifact is generated correctly with a valid machine-readable header and a comprehensive summary.

### G. Application of Domain-Driven Design (DDD)
The consultant's role is to initiate the **Ubiquitous Language**. It must actively listen for and use the client's own terminology, documenting key terms in a nascent glossary within the conversation. It will avoid deep domain modeling, leaving that to the Architect.

### H. Enhanced Guardrails & Escalation
*   **5-Round Cap:** A maximum of 5 Q&A rounds per phase (Problem or Solution). If alignment is not reached, the agent must escalate.
*   **Escalation Path:** Escalation involves asking the client to help reframe the problem or, if a domain knowledge gap is identified, **proposing that a human Subject Matter Expert (SME) be consulted**.
*   **Solutioning Threshold:** The agent is strictly forbidden from proposing solutions until the Problem Alignment Gate has been passed.