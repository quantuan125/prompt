# SPS Artifact: consultant/sps-templates - T101-B

---
**Task ID:** T101-B
**Task Type:** system/documentation
**Target:** consultant/sps-templates
**Artifact Type:** SPS
**Version:** 1.0.0
**Author:** LLM_Consultant
**Date:** 2025-07-23
**Status:** in_progress
**Dependencies:** T101-A
---

## IV. CORE CONTENT

### A. The Core Challenge
We need to design and produce the first versions (v1.0.0) of two foundational artifacts: the **SPS Structural Template (SPSST)** and the **SPS Procedural Guideline (SPSPG)**.

### B. Purpose & Goal
These artifacts will equip the `LLM_Consultant` with the standardized tools required to execute its "general" consultation task. The primary goal is to enable the consultant to produce a lean, focused, and validated **SPS (Synthesized Problem Statement) Artifact**. This SPS artifact will serve as the formal, machine-parseable input for the downstream `request` workflow, effectively replacing and standardizing the "Problem Framing & Validation" step of that process.

### C. Key Requirements & Specifications

#### 1. For the SPS Structural Template (SPSST):
- **Structural Compliance:** The overall template MUST adhere to the master structure defined in Section 7 of `prompt_main.md`.
- **Core Content Design:** The `IV. CORE CONTENT` section must be lean and specifically designed for problem framing. It will contain dedicated sections for:
    - The finalized **Problem Statement**.
    - A list of **Open Issues** (for parked questions and dependencies).
    - A **Glossary** (for the Ubiquitous Language).
    - A section for **Exploratory Notes**, where information from external feedback can be logged without altering the core problem definition.

#### 2. For the SPS Procedural Guideline (SPSPG):
- **Machine-Readable Contract:** It MUST be a machine-readable contract using `SCOPE` blocks to define the agent's executable sub-tasks.
- **Scope Naming Convention:** All `SCOPE` blocks MUST follow the `<action>_sps` naming convention (e.g., `framing_sps`, `defining_sps`).
- **Defined Procedures:** It MUST contain the explicit procedural steps for the agent to execute the **Branch Decision Framework** and the protocol for handling **external feedback**.

#### 3. Guiding Principles:
- **Lean Governance:** The artifacts will intentionally defer heavy governance tracking (e.g., detailed risk registers, decision logs) to the downstream `request` process, keeping the SPS focused on clean problem definition.
- **System Integration:** A new `sps_manifest.json` file will be created to manage the versions and dependencies of these new template artifacts, ensuring they are properly integrated into the overall system.