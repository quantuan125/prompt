# Bug Analysis: {{target_name}}

## Metadata Block
- **Version:** {{version}}
- **Author:** Consultant
- **Date:** {{date}}
- **Status:** {{status}}
- **Task ID:** {{task_id}}
- **Bug Severity:** {{severity}}

## Executive Summary

[Provide a 2-3 sentence summary of the bug impact and recommended fix approach for stakeholders]

## Bug Description

### Symptoms Observed
[Describe the observable behavior that indicates the bug]

### Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. **Expected Result:** [What should happen]
5. **Actual Result:** [What actually happens]

### Environment Details
- **Component Version:** {{component_version}}
- **Environment:** {{environment}}
- **Dependencies:** {{dependencies}}

## Root Cause Analysis

### Investigation Findings
[Detailed analysis of the underlying cause]

### Code Analysis
[Specific code sections or logic that are problematic]

### Data Flow Analysis
[How data moves through the system and where it breaks]

## Impact Assessment

### User Impact
- **Severity:** {{user_severity}}
- **Affected Users:** {{affected_users}}
- **Business Impact:** {{business_impact}}

### System Impact
- **Performance:** {{performance_impact}}
- **Data Integrity:** {{data_integrity_impact}}
- **Security:** {{security_impact}}

## Proposed Solutions

### Option 1: {{fix_option_1}} (Recommended)

**Approach:** [Direct fix to root cause]

**Implementation:**
```python
# Example fix code
{{example_fix_code}}
```

**Risk Level:** {{risk_level_1}}
**Effort:** {{effort_1}}

**Advantages:**
- [Benefit 1]
- [Benefit 2]

**Disadvantages:**
- [Risk 1]
- [Risk 2]

### Option 2: {{fix_option_2}} (Alternative)

**Approach:** [Alternative approach]

**Implementation:**
[Alternative implementation approach]

**Risk Level:** {{risk_level_2}}
**Effort:** {{effort_2}}

### Option 3: {{fix_option_3}} (Workaround)

**Approach:** [Temporary workaround]

**Implementation:**
[Workaround implementation]

**Risk Level:** {{risk_level_3}}
**Effort:** {{effort_3}}

## Testing Strategy

### Unit Tests Required
- [Test case 1]
- [Test case 2]
- [Test case 3]

### Integration Tests Required
- [Integration test 1]
- [Integration test 2]

### Regression Tests
- [Areas to verify haven't broken]

## Prevention Measures

### Code Review Focus Areas
[What to look for in future reviews to prevent similar bugs]

### Additional Monitoring
[Metrics or alerts that could have caught this earlier]

### Process Improvements
[Development process changes to prevent recurrence]

## Next Steps

1. **For Planner:** [Specific guidance for fix planning]
2. **Urgency Level:** {{urgency}}
3. **Dependencies:** [Any prerequisites for the fix]

## Integration with Other Roles

This bug analysis will be consumed by the Planner role to create a detailed fix plan. Key handoff points:
- Root cause identification with code locations
- Fix recommendation with implementation guidance
- Testing requirements for validation