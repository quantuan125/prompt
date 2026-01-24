#!/usr/bin/env python3
"""
System Validation Script

Automated consistency checker for the LLM agent system.
Validates that documentation follows hierarchy rules, all required
sections are present, and no redundancy violations exist.

This prevents future documentation drift and ensures system consistency.

Usage:
    python validate_system.py [--fix] [--verbose] [--report FILE]
"""

import os
import re
import json
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class ValidationIssue:
    """Represents a validation issue found in the system."""
    level: str  # 'error', 'warning', 'info'
    category: str
    file_path: str
    line_number: Optional[int]
    message: str
    suggestion: Optional[str] = None


class SystemValidator:
    """
    Automated consistency checker for the LLM agent system.
    
    Validates that documentation follows hierarchy rules, all required
    sections are present, and no redundancy violations exist.
    """
    
    def __init__(self, project_root: str = None):
        if project_root is None:
            script_dir = Path(__file__).parent
            self.project_root = script_dir.parent
        else:
            self.project_root = Path(project_root)
            
        self.issues: List[ValidationIssue] = []
        
        # Required header fields per general.md
        self.required_header_fields = {
            'Title', 'Version', 'Purpose', 'Audience', 'Last Updated', 'Change History'
        }
        
        # Standard documentation files that must follow hierarchy
        self.hierarchy_docs = [
            'prompt/documentation/prompt_main.md',
            'documentation/general.md'
        ]
        
        # Role system files
        self.role_files = [
            'prompt/consultant/consultant_system.md',
            'prompt/planner/planner_system.md', 
            'prompt/developer/developer_system.md',
            'prompt/reviewer/reviewer_system.md'
        ]
        
    def add_issue(self, level: str, category: str, file_path: str, 
                  message: str, line_number: Optional[int] = None, 
                  suggestion: Optional[str] = None):
        """Add a validation issue."""
        self.issues.append(ValidationIssue(
            level=level,
            category=category,
            file_path=file_path,
            line_number=line_number,
            message=message,
            suggestion=suggestion
        ))
        
    def validate_file_headers(self) -> bool:
        """Validate that all documentation files have proper headers."""
        logger.info("Validating file headers...")
        
        docs_to_check = self.hierarchy_docs + self.role_files
        all_valid = True
        
        for doc_path in docs_to_check:
            full_path = self.project_root / doc_path
            if not full_path.exists():
                self.add_issue('warning', 'missing_file', doc_path, 
                             f"File does not exist: {doc_path}")
                all_valid = False
                continue
                
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Extract header fields
                found_fields = set()
                lines = content.split('\n')
                
                for i, line in enumerate(lines[:20]):  # Check first 20 lines
                    if line.startswith('**') and line.endswith('**'):
                        # Extract field name
                        match = re.match(r'\*\*([^*]+):\*\*', line)
                        if match:
                            field_name = match.group(1).strip()
                            found_fields.add(field_name)
                            
                # Check for missing required fields
                missing_fields = self.required_header_fields - found_fields
                if missing_fields:
                    self.add_issue('error', 'missing_header_fields', doc_path,
                                 f"Missing required header fields: {', '.join(missing_fields)}",
                                 suggestion="Add missing fields to document header")
                    all_valid = False
                    
                # Check for Change History field specifically
                if 'Change History' not in found_fields:
                    self.add_issue('error', 'missing_change_history', doc_path,
                                 "Missing required 'Change History' field in header",
                                 suggestion="Add **Change History:** field referencing change history file")
                    all_valid = False
                    
            except Exception as e:
                self.add_issue('error', 'file_read_error', doc_path, 
                             f"Could not read file: {e}")
                all_valid = False
                
        return all_valid
    
    def validate_hierarchy_references(self) -> bool:
        """Validate that role files reference the hierarchy properly."""
        logger.info("Validating hierarchy references...")
        
        all_valid = True
        required_reference = '@prompt/documentation/prompt_main.md'
        
        for role_file in self.role_files:
            full_path = self.project_root / role_file
            if not full_path.exists():
                continue
                
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if required_reference not in content:
                    self.add_issue('error', 'missing_hierarchy_reference', role_file,
                                 f"Missing reference to {required_reference}",
                                 suggestion="Add reference to master workflow in execution protocol")
                    all_valid = False
                    
            except Exception as e:
                self.add_issue('error', 'file_read_error', role_file,
                             f"Could not read file: {e}")
                all_valid = False
                
        return all_valid
    
    def validate_redundancy(self) -> bool:
        """Check for redundant content across documentation files."""
        logger.info("Validating against redundancy...")
        
        all_valid = True
        
        # Check for duplicated archive rules
        archive_keywords = ['archive', 'Archive Strategy', 'Archive Rules', 'Archive Structure']
        files_with_archive_content = []
        
        for doc_path in self.hierarchy_docs + self.role_files:
            full_path = self.project_root / doc_path
            if not full_path.exists():
                continue
                
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Check for substantial archive content (not just references)
                archive_sections = 0
                for keyword in archive_keywords:
                    if keyword in content:
                        # Check if it's defining rules vs referencing
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            if keyword in line and '##' in line:  # Section header
                                # Look for rule definitions in next 10 lines
                                section_content = '\n'.join(lines[i:i+10])
                                if any(word in section_content.lower() for word in 
                                      ['keep', 'versions', 'timestamp', 'naming']):
                                    archive_sections += 1
                                    break
                                    
                if archive_sections > 0:
                    files_with_archive_content.append(doc_path)
                    
            except Exception as e:
                self.add_issue('error', 'file_read_error', doc_path,
                             f"Could not read file: {e}")
                
        # If multiple files define archive rules, flag as redundancy
        if len(files_with_archive_content) > 1:
            self.add_issue('warning', 'redundant_archive_rules', 
                         ', '.join(files_with_archive_content),
                         "Multiple files define archive rules instead of referencing general.md",
                         suggestion="Remove duplicate rules and reference @documentation/general.md")
            all_valid = False
            
        return all_valid
    
    def validate_template_structure(self) -> bool:
        """Validate template directory structure and content."""
        logger.info("Validating template structure...")
        
        all_valid = True
        template_dir = self.project_root / 'prompt' / 'templates'
        
        required_roles = ['consultant', 'planner', 'developer', 'reviewer']
        
        for role in required_roles:
            role_template_dir = template_dir / role
            if not role_template_dir.exists():
                self.add_issue('error', 'missing_template_dir', str(role_template_dir),
                             f"Missing template directory for {role}",
                             suggestion=f"Create directory {role_template_dir}")
                all_valid = False
                continue
                
            # Check for at least one template file
            template_files = list(role_template_dir.glob('*.md'))
            if not template_files:
                self.add_issue('warning', 'empty_template_dir', str(role_template_dir),
                             f"Empty template directory for {role}",
                             suggestion="Add template files for this role")
                all_valid = False
                
        return all_valid
    
    def validate_state_manager_integration(self) -> bool:
        """Validate that role files properly integrate with state manager."""
        logger.info("Validating state manager integration...")
        
        all_valid = True
        state_manager_calls = [
            'python prompt/scripts/state_manager.py get-task-info',
            'python prompt/scripts/state_manager.py complete-phase'
        ]
        
        for role_file in self.role_files:
            full_path = self.project_root / role_file
            if not full_path.exists():
                continue
                
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                missing_calls = []
                for call in state_manager_calls:
                    if call not in content:
                        missing_calls.append(call)
                        
                if missing_calls:
                    self.add_issue('warning', 'incomplete_state_integration', role_file,
                                 f"Missing state manager calls: {', '.join(missing_calls)}",
                                 suggestion="Add complete state manager integration")
                    all_valid = False
                    
            except Exception as e:
                self.add_issue('error', 'file_read_error', role_file,
                             f"Could not read file: {e}")
                all_valid = False
                
        return all_valid
    
    def validate_configuration_files(self) -> bool:
        """Validate configuration files exist and are properly structured."""
        logger.info("Validating configuration files...")
        
        all_valid = True
        config_files = [
            'prompt/config/workflow_state.json',
            'prompt/config/orchestration.json',
            'prompt/config/project_context.json'
        ]
        
        for config_file in config_files:
            full_path = self.project_root / config_file
            if not full_path.exists():
                self.add_issue('error', 'missing_config_file', config_file,
                             f"Missing configuration file: {config_file}",
                             suggestion="Create the required configuration file")
                all_valid = False
                continue
                
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    json.load(f)  # Validate JSON syntax
                    
            except json.JSONDecodeError as e:
                self.add_issue('error', 'invalid_json', config_file,
                             f"Invalid JSON syntax: {e}",
                             suggestion="Fix JSON syntax errors")
                all_valid = False
            except Exception as e:
                self.add_issue('error', 'file_read_error', config_file,
                             f"Could not read file: {e}")
                all_valid = False
                
        return all_valid
    
    def validate_script_files(self) -> bool:
        """Validate that required script files exist and are executable."""
        logger.info("Validating script files...")
        
        all_valid = True
        required_scripts = [
            'prompt/scripts/state_manager.py',
            'prompt/scripts/archive_manager.py',
            'prompt/scripts/migrate_to_task_model.py',
            'prompt/scripts/update_path_references.py'
        ]
        
        for script_file in required_scripts:
            full_path = self.project_root / script_file
            if not full_path.exists():
                self.add_issue('error', 'missing_script', script_file,
                             f"Missing required script: {script_file}",
                             suggestion="Create the required script file")
                all_valid = False
                continue
                
            # Check if executable (on Unix systems)
            if hasattr(os, 'access') and not os.access(full_path, os.X_OK):
                self.add_issue('warning', 'script_not_executable', script_file,
                             f"Script is not executable: {script_file}",
                             suggestion="Make script executable with chmod +x")
                
        return all_valid
    
    def generate_report(self) -> str:
        """Generate a comprehensive validation report."""
        
        # Count issues by level
        error_count = len([i for i in self.issues if i.level == 'error'])
        warning_count = len([i for i in self.issues if i.level == 'warning'])
        info_count = len([i for i in self.issues if i.level == 'info'])
        
        report = f"""# System Validation Report

**Date:** {os.popen('date').read().strip()}
**Total Issues:** {len(self.issues)}
**Errors:** {error_count}
**Warnings:** {warning_count}
**Info:** {info_count}

## Summary

"""
        
        if len(self.issues) == 0:
            report += "✅ **All validation checks passed!** The system is consistent and properly configured.\n\n"
        else:
            report += f"❌ **{len(self.issues)} issues found** that need attention.\n\n"
            
        # Group issues by category
        issues_by_category = {}
        for issue in self.issues:
            if issue.category not in issues_by_category:
                issues_by_category[issue.category] = []
            issues_by_category[issue.category].append(issue)
            
        # Report by category
        for category, category_issues in issues_by_category.items():
            report += f"### {category.replace('_', ' ').title()}\n\n"
            
            for issue in category_issues:
                icon = "🔴" if issue.level == "error" else "⚠️" if issue.level == "warning" else "ℹ️"
                report += f"{icon} **{issue.level.upper()}**: {issue.message}\n"
                report += f"   - **File:** {issue.file_path}\n"
                if issue.line_number:
                    report += f"   - **Line:** {issue.line_number}\n"
                if issue.suggestion:
                    report += f"   - **Suggestion:** {issue.suggestion}\n"
                report += "\n"
                
        return report
    
    def validate_all(self) -> bool:
        """
        Run all validation checks.
        
        Returns:
            True if all validations pass, False otherwise
        """
        logger.info("Starting comprehensive system validation...")
        
        all_valid = True
        
        # Run all validation checks
        checks = [
            self.validate_file_headers,
            self.validate_hierarchy_references,
            self.validate_redundancy,
            self.validate_template_structure,
            self.validate_state_manager_integration,
            self.validate_configuration_files,
            self.validate_script_files
        ]
        
        for check in checks:
            try:
                if not check():
                    all_valid = False
            except Exception as e:
                logger.error(f"Validation check failed: {e}")
                self.add_issue('error', 'validation_error', 'system',
                             f"Validation check failed: {e}")
                all_valid = False
                
        # Summary
        error_count = len([i for i in self.issues if i.level == 'error'])
        warning_count = len([i for i in self.issues if i.level == 'warning'])
        
        if all_valid:
            logger.info("✅ All validation checks passed!")
        else:
            logger.warning(f"❌ Validation found {error_count} errors and {warning_count} warnings")
            
        return all_valid


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Validate LLM agent system consistency",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--report', 
                       help='Save validation report to file')
    parser.add_argument('--project-root',
                       help='Path to project root (default: auto-detect)')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        
    # Initialize validator
    validator = SystemValidator(args.project_root)
    
    # Run validation
    is_valid = validator.validate_all()
    
    # Generate report
    report = validator.generate_report()
    
    if args.report:
        with open(args.report, 'w') as f:
            f.write(report)
        print(f"📄 Validation report saved to: {args.report}")
    else:
        print(report)
    
    # Return appropriate exit code
    if is_valid:
        print("✅ System validation completed successfully")
        return 0
    else:
        print("❌ System validation found issues")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())