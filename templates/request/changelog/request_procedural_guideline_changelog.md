# Change History Overview: Template Procedural Guideline (TPG)

| Version | Date       | Type  | Summary                                    |
|---------|------------|-------|--------------------------------------------|
| 1.1.0   | 2025-07-29 | Minor | Enhanced field reference with categorized token tables and improved workflow organization. |
| 1.0.0   | 2025-07-25 | Major | Initial release of separated procedural guideline extracted from request_structural_template.md template. |

---------

## Version 1.0.0 (2025-07-25)

### Type: Major

### Overview
Initial release of the Template Procedural Guideline (TPG) as a dedicated component extracted from the `request_structural_template.md` template. This represents a major architectural improvement through separation of concerns, moving from embedded HTML comment instructions to a standalone procedural guide. The TPG provides comprehensive step-by-step instructions for populating the standard request template.

### Added
- **Core Framework** with 5 Golden Rules for template usage principles
- **Phase Workflow System** with section-by-section mechanics for template completion
- **Comprehensive Field Reference** with 45+ token definitions and mapping instructions
- **Hard Gates & Refusal Logic** with formal checkpoint conditions and standardized responses
- **Update & Change History Rules** with versioning and amendment protocols
- **Detailed Section Instructions** covering all 11 template sections with specific guidance
- **Token Mapping Table** linking placeholders to their completion instructions
- **Gate Enforcement System** with specific halt conditions and required user responses
- **Professional Workflow Structure** for systematic template population

### Changed
- **Instruction Architecture** from embedded comments to standalone procedural document
- **Guidance Delivery** from scattered inline comments to organized workflow sections
- **Reference System** from implicit to explicit token-based field mapping
- **Quality Control** from informal to formal gate-based validation system

### Fixed
- **Instruction Accessibility** through dedicated procedural document instead of embedded comments
- **Workflow Clarity** with step-by-step section-by-section guidance
- **Consistency Enforcement** through standardized gate logic and refusal responses
- **Maintainability** through separated concerns and dedicated changelog

### Removed
- N/A (Initial release)

---

## Version 1.1.0 (2025-07-29)

### Type: Minor

### Overview
Significant structural enhancement to the Template Procedural Guideline (TPG) focusing on improved field reference organization and workflow clarity. This version introduces a categorized approach to token mapping and enhanced SCOPE-based workflow organization, making the template completion process more intuitive and systematically organized.

### Added
- **Categorized Token Tables**: Split field reference into two distinct tables for improved organization
  - Table 1: 35 tokens within "IV. CORE CONTENT" organized by subsections (IV-A through IV-E)
  - Table 2: 14 tokens outside "IV. CORE CONTENT" covering metadata, headers, and appendices
- **Enhanced SCOPE Comments**: Improved HTML comment structure with detailed knowledge, prerequisites, and success criteria for each workflow phase
- **Refined Section Structure**: Updated section titles for better clarity ("CORE PRINCIPLES" vs "GOLDEN RULES")
- **Improved Workflow Organization**: SCOPE-based workflow phases (create_request, research_request, refine_request, finalize_request)

### Changed
- **Field Reference Architecture**: Moved from single comprehensive table to categorized dual-table system
- **Token Organization**: Restructured token mapping to separate core content tokens from structural/metadata tokens
- **Workflow Presentation**: Enhanced workflow sections with HTML comment-based phase definitions
- **Section Numbering**: Updated references to match current template structure (IV-A, IV-B, IV-C, IV-D, IV-E)
- **Gate Logic Presentation**: Improved clarity in procedural vs hard gate explanations

### Fixed
- **Token Reference Accuracy**: Aligned all token mappings with current request_structural_template.md template structure  
- **Workflow Clarity**: Enhanced step-by-step guidance through improved section organization
- **Cross-Reference Consistency**: Ensured all section references match current template numbering

### Removed
- **Single Comprehensive Table**: Replaced with categorized approach for better usability
- **Outdated Section References**: Updated all references to match current template structure

---