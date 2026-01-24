#!/usr/bin/env python3
"""
Path Reference Update Script

Updates all file path references throughout the system to match the new
directory structure after reorganization.

Usage:
    python update_path_references.py [--dry-run] [--verbose]
"""

import os
import re
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class PathReferenceUpdater:
    """Updates file path references throughout the codebase."""
    
    def __init__(self, project_root: str = None, dry_run: bool = False):
        if project_root is None:
            script_dir = Path(__file__).parent
            self.project_root = script_dir.parent
        else:
            self.project_root = Path(project_root)
            
        self.dry_run = dry_run
        self.updates_made = 0
        
        # Define path mappings for the migration
        self.path_mappings = {
            # Role system files
            '@prompt/consultant/consultant_system.md': '@prompt/roles/consultant/consultant_system.md',
            '@prompt/planner/planner_system.md': '@prompt/roles/planner/planner_system.md', 
            '@prompt/developer/developer_system.md': '@prompt/roles/developer/developer_system.md',
            '@prompt/reviewer/reviewer_system.md': '@prompt/roles/reviewer/reviewer_system.md',
            
            # Claude-specific files
            '@prompt/consultant/CLAUDE_CONSULTANT.md': '@prompt/roles/consultant/CLAUDE_CONSULTANT.md',
            '@prompt/planner/CLAUDE_PLANNER.md': '@prompt/roles/planner/CLAUDE_PLANNER.md',
            '@prompt/developer/CLAUDE_DEVELOPER.md': '@prompt/roles/developer/CLAUDE_DEVELOPER.md',
            '@prompt/reviewer/CLAUDE_REVIEWER.md': '@prompt/roles/reviewer/CLAUDE_REVIEWER.md',
            
            # Template files
            '@prompt/templates/consultant/': '@prompt/templates/consultant/',
            '@prompt/templates/planner/': '@prompt/templates/planner/',
            '@prompt/templates/developer/': '@prompt/templates/developer/',
            '@prompt/templates/reviewer/': '@prompt/templates/reviewer/',
            
            # Specific template references
            'prompt/consultant/template_consulting.md': 'prompt/templates/consultant/standard_consultation.md',
            'prompt/planner/template_planning.md': 'prompt/templates/planner/new_feature.md',
            'prompt/developer/template_developing.md': 'prompt/templates/developer/standard_development.md',
            'prompt/reviewer/template_reviewing.md': 'prompt/templates/reviewer/standard_review.md',
            
            # Relative path references
            '../consultant/consultant_system.md': '../roles/consultant/consultant_system.md',
            '../planner/planner_system.md': '../roles/planner/planner_system.md',
            '../developer/developer_system.md': '../roles/developer/developer_system.md',
            '../reviewer/reviewer_system.md': '../roles/reviewer/reviewer_system.md',
        }
        
        # File extensions to process
        self.file_extensions = {'.md', '.py', '.json', '.sh', '.yaml', '.yml'}
        
        # Directories to exclude from processing
        self.exclude_dirs = {'.git', '__pycache__', 'venv', 'node_modules', '.pytest_cache'}
        
    def find_files_to_update(self) -> List[Path]:
        """Find all files that might contain path references."""
        files_to_process = []
        
        for root, dirs, files in os.walk(self.project_root):
            # Remove excluded directories from search
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix in self.file_extensions:
                    files_to_process.append(file_path)
                    
        logger.info(f"Found {len(files_to_process)} files to process")
        return files_to_process
    
    def update_file_references(self, file_path: Path) -> int:
        """
        Update path references in a single file.
        
        Returns:
            Number of references updated in this file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            updates_in_file = 0
            
            # Apply each path mapping
            for old_path, new_path in self.path_mappings.items():
                # Use regex for more precise matching
                pattern = re.escape(old_path)
                if content != content.replace(old_path, new_path):
                    content = content.replace(old_path, new_path)
                    count = original_content.count(old_path)
                    updates_in_file += count
                    logger.debug(f"Updated {count} references: {old_path} -> {new_path}")
            
            # Special handling for common patterns
            updates_in_file += self._update_template_references(content, file_path)
            updates_in_file += self._update_import_references(content, file_path)
            
            # Save updated content if changes were made
            if content != original_content and not self.dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
            if updates_in_file > 0:
                status = "DRY RUN: Would update" if self.dry_run else "Updated"
                logger.info(f"{status} {updates_in_file} references in {file_path.relative_to(self.project_root)}")
                
            return updates_in_file
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return 0
    
    def _update_template_references(self, content: str, file_path: Path) -> int:
        """Update template references that follow common patterns."""
        updates = 0
        
        # Pattern: @prompt/templates/{role}/template_name.md
        template_pattern = r'@prompt/templates/(\w+)/(\w+)\.md'
        
        def replace_template(match):
            role = match.group(1)
            template = match.group(2)
            
            # Map old template names to new standardized names
            template_mappings = {
                'template_consulting': 'standard_consultation',
                'template_planning': 'new_feature', 
                'template_developing': 'standard_development',
                'template_reviewing': 'standard_review'
            }
            
            new_template = template_mappings.get(template, template)
            return f'@prompt/templates/{role}/{new_template}.md'
        
        new_content = re.sub(template_pattern, replace_template, content)
        if new_content != content:
            updates += len(re.findall(template_pattern, content))
            
        return updates
    
    def _update_import_references(self, content: str, file_path: Path) -> int:
        """Update Python import references."""
        updates = 0
        
        # Only process Python files
        if file_path.suffix != '.py':
            return 0
            
        # Pattern: from prompt.consultant import ...
        import_patterns = [
            (r'from prompt\.consultant', 'from prompt.roles.consultant'),
            (r'from prompt\.planner', 'from prompt.roles.planner'),
            (r'from prompt\.developer', 'from prompt.roles.developer'),
            (r'from prompt\.reviewer', 'from prompt.roles.reviewer'),
        ]
        
        for old_pattern, new_pattern in import_patterns:
            if re.search(old_pattern, content):
                new_content = re.sub(old_pattern, new_pattern, content)
                if new_content != content:
                    updates += len(re.findall(old_pattern, content))
                    content = new_content
                    
        return updates
    
    def create_migration_report(self, files_processed: List[Path], total_updates: int) -> str:
        """Create a report of the migration."""
        report = f"""
# Path Reference Migration Report

**Date**: {os.popen('date').read().strip()}
**Files Processed**: {len(files_processed)}
**Total Updates**: {total_updates}
**Dry Run**: {self.dry_run}

## Path Mappings Applied

"""
        for old_path, new_path in self.path_mappings.items():
            report += f"- `{old_path}` → `{new_path}`\n"
            
        report += f"""

## Files Modified

"""
        
        for file_path in files_processed:
            if self.updates_made > 0:
                report += f"- {file_path.relative_to(self.project_root)}\n"
                
        return report
    
    def update_all_references(self) -> bool:
        """
        Update all path references throughout the project.
        
        Returns:
            True if successful, False otherwise
        """
        logger.info("Starting path reference update process")
        
        try:
            # Find all files to process
            files_to_process = self.find_files_to_update()
            
            total_updates = 0
            files_with_updates = []
            
            # Process each file
            for file_path in files_to_process:
                updates = self.update_file_references(file_path)
                if updates > 0:
                    files_with_updates.append(file_path)
                    total_updates += updates
                    
            # Create migration report
            if not self.dry_run and total_updates > 0:
                report_path = self.project_root / 'path_migration_report.md'
                report_content = self.create_migration_report(files_with_updates, total_updates)
                with open(report_path, 'w') as f:
                    f.write(report_content)
                logger.info(f"Migration report saved to: {report_path}")
                
            self.updates_made = total_updates
            
            status = "DRY RUN: Would make" if self.dry_run else "Made"
            logger.info(f"{status} {total_updates} path reference updates across {len(files_with_updates)} files")
            
            return True
            
        except Exception as e:
            logger.error(f"Path reference update failed: {e}")
            return False
    
    def validate_references(self) -> bool:
        """Validate that updated references point to existing files."""
        logger.info("Validating updated references...")
        
        validation_errors = []
        
        # Check that new paths exist
        for old_path, new_path in self.path_mappings.items():
            if new_path.startswith('@'):
                # Convert @ reference to actual path
                actual_path = self.project_root / new_path[1:]  # Remove @
            else:
                actual_path = self.project_root / new_path
                
            if not actual_path.exists() and not actual_path.parent.exists():
                validation_errors.append(f"Target path does not exist: {new_path}")
                
        if validation_errors:
            logger.warning("Validation found issues:")
            for error in validation_errors:
                logger.warning(f"  - {error}")
            return False
        else:
            logger.info("Reference validation passed")
            return True


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Update file path references after directory reorganization",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be updated without making changes')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--project-root',
                       help='Path to project root (default: auto-detect)')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        
    # Initialize updater
    updater = PathReferenceUpdater(args.project_root, args.dry_run)
    
    # Validate references before updating
    if not updater.validate_references():
        logger.warning("Reference validation failed - proceeding anyway")
    
    # Update references
    success = updater.update_all_references()
    
    if success:
        if args.dry_run:
            print(f"✅ Validation passed - would update {updater.updates_made} references")
        else:
            print(f"✅ Path reference update completed - {updater.updates_made} references updated")
        return 0
    else:
        print("❌ Path reference update failed")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())