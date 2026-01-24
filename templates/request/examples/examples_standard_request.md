### Example 1: Initial Validation Question (TPG Phase I)
# GOAL: Validate the agent's high-level understanding of the client's core problems.

- **Client's Key Points:** "The documentation paths are all wrong. The state tracking section is out of date. The JSON files are confusing."
- **High-Quality Question:** "Based on your notes, it seems the core challenges are: 1) outdated documentation, 2) broken system processes, and 3) a need for better configuration management. Does this high-level summary accurately capture your main concerns before we dive into specific issues?"

---
### Example 2: Refinement Question (TPG Phase III)
# GOAL: Probe for a specific, unstated constraint after initial research.

- **Research Finding:** The `orchestration.json` file is complex and has no comments.
- **High-Quality Question:** "My initial research on `REQ-T002-6` shows that the `orchestration.json` file is highly complex. To ensure the natural language explanations are useful, could you clarify who the primary audience for understanding this file is? Is it for you, for future developers, or for other agents?"

---
### Example 3: Acceptance Criteria Proposal (TPG Phase III)
# GOAL: Propose a testable, unambiguous "definition of done" based on the dialogue.

- **Refinement Summary:** "The client confirmed the goal is to centralize file paths into a table in `prompt_main.md` to improve maintainability."
- **High-Quality AC Proposal:** "I've drafted the following success criteria based on our conversation. Please let me know if this is correct:
    *   **Given** a user is viewing `prompt_main.md`,
    *   **When** they navigate to Section 4 ('File Management'),
    *   **Then** they must see a Markdown table containing columns for 'Reference Name', 'Path', and 'Description'.
    *   **And** all previous hardcoded artifact paths throughout the document must be replaced with the new reference names."