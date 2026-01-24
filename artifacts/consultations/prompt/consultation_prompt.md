# Development Proposal v2.1.0: Enhanced Versioning and Standards

**Version:** 1.0
**Author:** Senior Software Architecture Consultant
**Date:** 2025-07-13
**Status:** Proposal


## 1. Executive Summary

This document outlines the necessary architectural improvements for the v2.1.0 release of the LLM Agent System. Our recent deep-dive analysis has revealed two critical, interconnected issues that must be addressed to ensure system scalability, predictability, and maintainability:

1.  **Versioning Ambiguity:** The current system conflates the version of internal documents (like plans) with the version of the final software product, creating confusion and preventing proper iteration.
2.  **Emergent Standards Gap:** We have identified superior documentation standards during our review (e.g., linking artifacts to tasks), but these new standards have not been formally codified into the system's governance documents.

This proposal provides a set of clear, actionable tasks to resolve these issues by establishing a robust, decoupled versioning system and formally integrating these new, more advanced standards into our core documentation.

## 2. Summary of Identified Issues

### Issue 1: Ambiguous Versioning Scheme
- **The Conflict:** There is no formal distinction between the version of a software component (e.g., `tv_ingest v2.0.0`) and the version of the artifacts created to produce it (e.g., `plan_v2.0.1.md`).
- **The Impact:** This makes it impossible to iterate on a plan or consultation without creating a confusing mismatch with the final product version. It breaks the logic of Semantic Versioning for the component itself.

### Issue 2: Undocumented and Unenforced Standards
- **The Conflict:** New, more effective standards have been developed organically (e.g., the "Task Context Block" header, structured file manifests), but they do not exist in any official capacity within `general.md` or `prompt_main.md`.
- **The Impact:** There is no mechanism to enforce these best practices. This leads to inconsistent artifact quality, poor traceability between a task and its outputs, and a system that is harder to automate and debug.

## 3. Actionable Implementation Plan for v2.1.0

To resolve these issues, the following tasks must be integrated into the development plan for the v2.1.0 release.

### Action Item 1: Implement Decoupled Versioning System

*   **Goal:** Formally separate the concept of a "Product Version" from an "Artifact Version".
*   **Tasks:**
    1.  **Update `general.md`:** Add a "Project Versioning Standards" section that defines "Product/Component Versioning" (SemVer) and "Artifact Versioning" (internal revisions) as two distinct concepts.
    2.  **Update `prompt_main.md`:** Amend the "Task-Centric Workflow" section to explain that each task in `workflow_state.json` will have a `target_version` for the final product, while the `history` object tracks independently versioned artifacts.
    3.  **Update `state_manager.py`:** Augment the `start_task` CLI command to accept a `--target-version` parameter, making the intended product version an explicit part of every task's metadata.

### Action Item 2: Codify and Globalize New Artifact Standards

*   **Goal:** Ensure all workflow artifacts are traceable and consistently structured.
*   **Tasks:**
    1.  **Update `prompt_main.md`:** Add a "Standard Artifact Header" section to the "Template Design Guidelines". This header (including `Task ID`, `Task Type`, `Target`, `Artifact Type`, etc.) is mandatory for all *workflow artifacts* (plans, consultations, reviews) but not for *foundational documents*.
    2.  **Update All Templates:** Modify every template file in `prompt/templates/` to include the new mandatory header block.

### Action Item 3: Formalize Enhanced Planning Standards

*   **Goal:** Improve the quality, consistency, and efficiency of planning artifacts.
*   **Tasks:**
    1.  **Update `prompt_main.md`:** Add a "Plan Granularity and Profiles" section defining `Full` and `Lite` profiles for development plans.
    2.  **Update `prompt_main.md`:** Add a "Standardized File Manifest" section requiring the new structured table format for file changes in all plans.
    3.  **Update Planning Templates:** Modify the templates in `prompt/templates/planner/` to incorporate the structure for these new standards.
