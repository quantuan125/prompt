# Plan: Develop New CLAUDE.md for Perpetual Trading Analysis Application

## Stakeholder Summary
We will create a modern, effective CLAUDE.md file to replace the deprecated role-based configuration. This new file will provide Claude Code with essential project context, development patterns, and architectural guidance specific to our perpetual trading analysis application. The goal is to improve AI assistance quality while preventing instruction conflicts through a streamlined, modular approach.

## Technical Overview

### Current State Analysis
- **Deprecated Configuration**: Current CLAUDE.md uses outdated role-based patterns (`context`, `review`, `profiles`) that are no longer supported
- **Settings Incompatibility**: Claude Code v1.0.51+ removed support for these configuration fields
- **Missing Project Context**: No current guidance on application architecture, development patterns, or domain-specific requirements

### Target State
- **Streamlined CLAUDE.md**: Focused file following modern Claude Code best practices
- **Modular Documentation**: References to existing project documentation rather than duplication
- **Domain Awareness**: Trading-specific context and architectural patterns
- **Development Optimization**: Clear guidance for AI-assisted development workflows

## Implementation Strategy

### Phase 1: Core Structure Development
Create focused CLAUDE.md with essential sections:

**Project Identity & Architecture**
- Streamlit-based perpetual trading analysis application
- Component-based architecture with standardized patterns (ui_, fb_, dp_, svc_ prefixes)
- File-based JSON storage with sophisticated backup/migration system
- Multi-page application structure (Open Positions, Closed Positions, Analytics, Pine Script)

**Development Commands & Workflows**
- Application startup: `streamlit run app.py`
- Documentation maintenance: `python documentation/scripts/update_doc.py`
- Testing patterns (based on existing pytest structure)
- Migration execution procedures

**Architectural Constraints**
- Required patterns: Component isolation, Facade, Builder, Service, Controller
- Prohibited patterns: Direct database access, monolithic components
- File organization requirements: Feature-based components with standardized sub-structure
- Data handling: JSON-based storage with backup before modifications

**Code Quality Standards**
- Import patterns: Relative imports within components
- Error handling: Comprehensive validation at multiple layers
- Naming conventions: Descriptive prefixes indicating component type
- Documentation requirements: Updates required for component changes

### Phase 2: Modular Documentation Integration
Implement references to existing documentation:

**Architecture References**
- `@documentation/general.md` - Overall system architecture
- `@documentation/closing_position/architecture.md` - Component patterns
- `@documentation/tv_ingest/architecture.md` - External integration patterns

**Development Guidelines**
- `@documentation/main/template_guideline.md` - Coding standards and quality metrics
- `@documentation/main/process_guideline.md` - Versioning and documentation processes

**Feature-Specific Context**
- `@documentation/analytics/` - Analytics component guidance
- `@documentation/open_positions/` - Position management patterns
- `@documentation/grid/` - UI grid component standards

### Phase 3: Domain-Specific Optimization
Add trading application specific guidance:

**Position Management Context**
- Position lifecycle understanding (open -> active -> closed)
- Required validation for position data integrity
- Session management and position organization patterns
- Risk/reward calculation requirements

**Analytics Development Patterns**
- Chart builder architecture (category, timeline, hourly, strategy)
- Data processor implementation standards
- Service layer patterns for complex analytics
- Visualization component organization

**TradingView Integration Guidelines**
- Webhook handling patterns
- Pine Script data processing requirements
- Real-time data ingestion protocols
- External API integration best practices

### Phase 4: AI Assistance Optimization
Configure optimal development assistance patterns:

**Tool Usage Guidelines**
- Preferred tools for different tasks (Read vs Task vs Grep)
- When to use TodoWrite for complex multi-step operations
- File modification patterns (Edit vs MultiEdit preferences)
- Search strategies for large codebase navigation

**Quality Gates**
- Always check existing patterns before implementing new features
- Mandatory backup before structural changes
- Required documentation updates for component changes
- Test validation requirements

**Adherence Verification**
- Confirmation mechanisms to verify rule following
- Response patterns that indicate architectural compliance
- Clear indicators for domain understanding

## Risk Assessment

### High Priority Risks
- **Instruction Conflicts**: Too much content could create contradictions
  - *Mitigation*: Start minimal, add complexity gradually, test adherence
- **Pattern Deviation**: AI might not follow established architectural patterns
  - *Mitigation*: Clear prohibitions, reference existing examples, verification mechanisms

### Medium Priority Risks
- **Context Overload**: Large CLAUDE.md could reduce effectiveness
  - *Mitigation*: Modular approach with external references, progressive enhancement
- **Domain Misunderstanding**: Trading concepts might be misinterpreted
  - *Mitigation*: Explicit definitions, reference to existing position structures

### Low Priority Risks
- **Documentation Drift**: References might become outdated
  - *Mitigation*: Regular review cycle, automated documentation updates

## Success Criteria

### Technical Metrics
- **Architectural Compliance**: Claude consistently follows component patterns
- **Code Quality**: Generated code matches existing project standards
- **Development Velocity**: Faster feature implementation with proper patterns
- **Domain Accuracy**: Correct handling of trading concepts and data structures

### Qualitative Indicators
- **Reduced Corrections**: Fewer manual fixes needed for AI-generated code
- **Pattern Consistency**: New components follow established architecture
- **Documentation Coherence**: Automatic reference to relevant project docs
- **Context Retention**: Better understanding maintained across sessions

## Implementation Timeline

### Immediate (Phase 1)
- Create core CLAUDE.md structure
- Implement essential commands and constraints
- Add basic architectural guidance

### Short-term (Phase 2-3)
- Add modular documentation references
- Implement domain-specific context
- Test adherence mechanisms

### Medium-term (Phase 4)
- Optimize AI assistance patterns
- Refine based on usage feedback
- Document lessons learned

## Rollback Strategy

### Immediate Rollback
- Restore current CLAUDE.md from git history
- Revert to manual instruction approach if needed

### Gradual Rollback
- Remove problematic sections while keeping working parts
- Fall back to external documentation references
- Use hooks for critical constraints if CLAUDE.md fails

## Documentation & Testing Deliverables

### Primary Deliverable
- **New CLAUDE.md**: Located at project root, following modern Claude Code patterns

### Supporting Documentation
- **Plan Document**: `prompt/planner/planner_notes/prompt/claude/plan_claude.md`
- **Implementation Guide**: Instructions for testing and refining the new configuration
- **Adherence Testing**: Mechanisms to verify Claude is following the guidance

### Validation Requirements
- **Functionality Test**: Verify Claude understands project architecture
- **Pattern Test**: Confirm adherence to component organization
- **Domain Test**: Validate trading concept understanding
- **Integration Test**: Ensure compatibility with existing documentation system

This plan transforms the deprecated CLAUDE.md into a modern, effective project memory system specifically tailored for the perpetual trading analysis application's architecture and development needs.

---

**Plan Version**: v1.0.0  
**Created**: 2025-07-12  
**Target**: CLAUDE.md modernization  
**Status**: Implementation Ready