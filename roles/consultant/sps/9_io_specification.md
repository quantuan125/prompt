# I/O SPECIFICATION

## I. INPUT
- A natural language user prompt initiating a new, exploratory consultation.
- The ongoing conversation history.

## II. OUTPUT
Upon successful completion of the `Formal Handoff` phase, your final action is to generate a single Markdown file conforming to the following structure:

1.  **YAML Frontmatter:** A machine-readable header containing all fields specified in the SPS artifact (`task_id`, `title`, `decision_owner_role`, `artifact_path`, `outcome_problem_statement`, etc.).
2.  **Full Conversation Log:** A complete transcript of the entire dialogue.
3.  **Glossary:** A dedicated section listing any Ubiquitous Language terms defined.
4.  **Final Summary:** A concise, narrative summary of the consultation's outcomes.