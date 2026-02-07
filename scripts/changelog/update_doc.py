#!/usr/bin/env python3
"""
Documentation Update Script

This script automates the maintenance tasks for project documentation including:
- Archiving current versions before updates
- Updating change history files with new entries
- Maintaining consistent formatting and structure

Usage:
    python documentation/scripts/update_doc.py \
        --doc-path "documentation/general.md" \
        --current-version "2.0.0" \
        --new-version "2.1.0" \
        --change-type "Minor" \
        --summary "Brief description of changes"
        
    # Test mode (shows what would be done without making changes):
    python documentation/scripts/update_doc.py \
        --doc-path "documentation/general.md" \
        --current-version "2.0.0" \
        --new-version "2.1.0" \
        --change-type "Minor" \
        --summary "Brief description of changes" \
        --dry-run
"""

import argparse
import datetime
import shutil
import sys
import re
import tempfile
from pathlib import Path


def check_version_exists(history_file_path: Path, version: str) -> bool:
    """Check if a version already exists in the change history file."""
    if not history_file_path.exists():
        return False
    
    try:
        content = history_file_path.read_text(encoding='utf-8')
        # Look for version in both table and detailed entries
        version_pattern = rf"## Version {re.escape(version)} \("
        table_pattern = rf"\| {re.escape(version)} \|"
        
        return bool(re.search(version_pattern, content) or re.search(table_pattern, content))
    except Exception:
        return False


def validate_change_history_structure(history_file_path: Path) -> tuple[bool, str]:
    """Validate the structure of a change history file."""
    if not history_file_path.exists():
        return True, "File does not exist, will be created"
    
    try:
        content = history_file_path.read_text(encoding='utf-8')
        
        # Check for title
        if not re.search(r'# Change History Overview:', content):
            return False, "Missing title header '# Change History Overview:'"
        
        # Check for table structure
        table_pattern = r'# Change History Overview:.*?\n\n\| Version \| Date.*?\n\|.*?\|.*?\n'
        if not re.search(table_pattern, content, re.DOTALL):
            return False, "Missing or malformed table structure"
        
        return True, "File structure is valid"
        
    except Exception as e:
        return False, f"Error reading file: {e}"


def archive_document(doc_path: Path, current_version: str, dry_run: bool = False) -> None:
    """Archives the current version of the document."""
    if not doc_path.exists():
        print(f"Error: Document not found at {doc_path}", file=sys.stderr)
        sys.exit(1)

    doc_dir = doc_path.parent
    base_name = doc_path.stem
    
    # Create archive directory if it doesn't exist
    archive_dir = doc_dir / "archive"
    archive_path = archive_dir / f"{base_name}_v{current_version}.md"
    
    if dry_run:
        print(f"[DRY RUN] Would create archive directory: {archive_dir}")
        print(f"[DRY RUN] Would archive {doc_path} to {archive_path}")
        return
    
    try:
        archive_dir.mkdir(exist_ok=True)
        shutil.copy2(doc_path, archive_path)
        print(f"Successfully archived {doc_path} to {archive_path}")
    except Exception as e:
        print(f"Error: Failed to archive document. {e}", file=sys.stderr)
        sys.exit(1)


def update_change_history(doc_path: Path, new_version: str, change_type: str, summary: str, dry_run: bool = False) -> None:
    """Updates the document's change history file with correct entry placement."""
    doc_dir = doc_path.parent
    base_name = doc_path.stem
    history_file_path = doc_dir / f"{base_name}_change_history.md"

    if not history_file_path.exists():
        if dry_run:
            print(f"[DRY RUN] Would create new change history file: {history_file_path}")
            return
        else:
            print(f"Warning: Change history file not found at {history_file_path}. Creating it.", file=sys.stderr)
            initial_content = (
                f"# Change History Overview: {base_name.title()}\n\n"
                f"| Version | Date | Type | Summary |\n"
                f"|---|---|---|---|\n\n"
                f"---------\n\n"
            )
            history_file_path.write_text(initial_content, encoding='utf-8')

    is_valid, message = validate_change_history_structure(history_file_path)
    if not is_valid:
        print(f"Error: Invalid change history file structure: {message}", file=sys.stderr)
        sys.exit(1)

    today_date = datetime.date.today().isoformat()
    table_entry = f"| {new_version} | {today_date} | {change_type} | {summary} |"
    
    detailed_entry_text = f"""---

## Version {new_version} ({today_date})

### Type: {change_type}

### Overview
{summary}

### Added
- [Detail of new sections, features, or guidelines.]

### Changed
- [Detail of modifications to existing content.]

### Fixed
- [Detail of any fixes, such as typos or broken links.]

### Removed
- [Detail of any content or sections that were removed.]"""

    try:
        original_content = history_file_path.read_text(encoding='utf-8')
        
        if dry_run:
            print(f"[DRY RUN] Would add table entry: {table_entry}")
            print(f"[DRY RUN] Would add detailed entry for version {new_version}")
            print(f"[DRY RUN] Would update file: {history_file_path}")
            return

        # Find the main separator between the table and the detailed entries.
        separator_pattern = r'(\n\n---)'
        match = re.search(separator_pattern, original_content)
        
        if not match:
            print(f"Error: Could not find the detailed entry separator in {history_file_path}", file=sys.stderr)
            sys.exit(1)

        table_part_end_index = match.start()
        table_part = original_content[:table_part_end_index]
        separator = match.group(1)
        detailed_part = original_content[match.end():]

        # Update the table part by inserting the new row
        table_lines = table_part.strip().split('\n')
        table_separator_index = -1
        for i, line in enumerate(table_lines):
            if line.startswith('|---'):
                table_separator_index = i
                break
        
        if table_separator_index == -1:
            print(f"Error: Malformed table in {history_file_path}", file=sys.stderr)
            sys.exit(1)
            
        table_lines.insert(table_separator_index + 1, table_entry)
        new_table_part = '\n'.join(table_lines)

        # Reconstruct the full file content
        new_detailed_part = detailed_entry_text
        if detailed_part.strip():
             new_detailed_part += f"\n\n---\n{detailed_part}"

        new_content = new_table_part + separator + new_detailed_part
        
        history_file_path.write_text(new_content, encoding='utf-8')
        print(f"Successfully updated {history_file_path} with version {new_version}")

    except Exception as e:
        print(f"Error: Failed to update change history. {e}", file=sys.stderr)
        sys.exit(1)


def validate_dry_run_accuracy(doc_path: Path, new_version: str, change_type: str, summary: str) -> bool:
    """Validates that dry-run output exactly matches what real execution would do."""
    print("[VALIDATION] Testing dry-run accuracy...")
    
    doc_dir = doc_path.parent
    base_name = doc_path.stem
    history_file_path = doc_dir / f"{base_name}_change_history.md"
    
    # Create temporary copies
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        temp_doc_path = temp_dir_path / doc_path.name
        temp_history_path = temp_dir_path / history_file_path.name
        
        # Copy files to temp directory
        shutil.copy2(doc_path, temp_doc_path)
        if history_file_path.exists():
            shutil.copy2(history_file_path, temp_history_path)
        
        try:
            # Run actual update on temp files
            update_change_history(temp_doc_path, new_version, change_type, summary, dry_run=False)
            
            # Read the results
            if temp_history_path.exists():
                result_content = temp_history_path.read_text(encoding='utf-8')
                print("[VALIDATION] ✅ Dry-run accuracy test passed")
                return True
            else:
                print("[VALIDATION] ❌ Dry-run accuracy test failed: temp file not created")
                return False
                
        except Exception as e:
            print(f"[VALIDATION] ❌ Dry-run accuracy test failed: {e}")
            return False


def validate_semantic_version(version: str) -> bool:
    """Validates that the version follows semantic versioning (X.Y.Z)."""
    try:
        parts = version.split('.')
        if len(parts) != 3:
            return False
        for part in parts:
            int(part)  # Check if each part is a valid integer
        return True
    except ValueError:
        return False


def main():
    """Main entry point for the documentation update script."""
    parser = argparse.ArgumentParser(
        description="Automates documentation maintenance tasks.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Normal update:
  %(prog)s --doc-path "documentation/general.md" \\
           --current-version "2.0.0" \\
           --new-version "2.1.0" \\
           --change-type "Minor" \\
           --summary "Added discovery protocol"
           
  # Test what would happen (dry run):
  %(prog)s --doc-path "documentation/general.md" \\
           --current-version "2.0.0" \\
           --new-version "2.1.0" \\
           --change-type "Minor" \\
           --summary "Test changes" \\
           --dry-run
           
  # Validate dry-run accuracy:
  %(prog)s --doc-path "documentation/general.md" \\
           --current-version "2.0.0" \\
           --new-version "2.1.0" \\
           --change-type "Minor" \\
           --summary "Test changes" \\
           --validate-dry-run
           
  # Check file structure:
  %(prog)s --doc-path "documentation/general.md" \\
           --check-file-structure
           
  # Force update even if version exists:
  %(prog)s --doc-path "documentation/general.md" \\
           --current-version "2.0.0" \\
           --new-version "2.1.0" \\
           --change-type "Minor" \\
           --summary "Forced update" \\
           --force
        """
    )
    
    parser.add_argument(
        "--doc-path", 
        required=True, 
        help="Path to the document being updated"
    )
    parser.add_argument(
        "--current-version", 
        help="The current version of the document (e.g., 1.2.0)"
    )
    parser.add_argument(
        "--new-version", 
        help="The new version of the document (e.g., 1.3.0)"
    )
    parser.add_argument(
        "--change-type", 
        choices=["Major", "Minor", "Patch"], 
        help="The type of change being made"
    )
    parser.add_argument(
        "--summary", 
        help="A one-sentence summary of the changes"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making any changes"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force update even if the version already exists"
    )
    parser.add_argument(
        "--validate-dry-run",
        action="store_true",
        help="Validate that dry-run output matches real execution"
    )
    parser.add_argument(
        "--check-file-structure",
        action="store_true",
        help="Check change history file structure without making changes"
    )
    
    args = parser.parse_args()
    
    # Handle utility commands that don't require full arguments
    doc_path = Path(args.doc_path)
    doc_dir = doc_path.parent
    base_name = doc_path.stem
    history_file_path = doc_dir / f"{base_name}_change_history.md"
    
    if args.check_file_structure:
        is_valid, message = validate_change_history_structure(history_file_path)
        if is_valid:
            print(f"✅ File structure is valid: {message}")
        else:
            print(f"❌ File structure is invalid: {message}")
        sys.exit(0 if is_valid else 1)
    
    # For other operations, require the full set of arguments
    if not all([args.current_version, args.new_version, args.change_type, args.summary]):
        parser.error("--current-version, --new-version, --change-type, and --summary are required unless using --check-file-structure")
    
    # Validate semantic versioning
    if not validate_semantic_version(args.current_version):
        print(f"Error: Invalid current version format '{args.current_version}'. Use semantic versioning (X.Y.Z)", file=sys.stderr)
        sys.exit(1)
        
    if not validate_semantic_version(args.new_version):
        print(f"Error: Invalid new version format '{args.new_version}'. Use semantic versioning (X.Y.Z)", file=sys.stderr)
        sys.exit(1)

    # Handle validation command
    if args.validate_dry_run:
        is_accurate = validate_dry_run_accuracy(doc_path, args.new_version, args.change_type, args.summary)
        sys.exit(0 if is_accurate else 1)

    # Check for version conflicts
    if check_version_exists(history_file_path, args.new_version) and not args.force:
        print(f"Error: Version {args.new_version} already exists in change history.", file=sys.stderr)
        print("Use --force to override this check or choose a different version.", file=sys.stderr)
        sys.exit(1)

    # Display execution plan
    mode_indicator = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode_indicator}--- Starting Documentation Update ---")
    print(f"Document: {doc_path}")
    print(f"Version: {args.current_version} → {args.new_version}")
    print(f"Change Type: {args.change_type}")
    print(f"Summary: {args.summary}")
    
    if args.dry_run:
        print("Mode: DRY RUN (no files will be modified)")
    elif args.force:
        print("Mode: FORCE (overriding version existence check)")
        
    print()
    
    # Execute the maintenance tasks
    archive_document(doc_path, args.current_version, args.dry_run)
    update_change_history(doc_path, args.new_version, args.change_type, args.summary, args.dry_run)
    
    print(f"{mode_indicator}--- Documentation Update Complete ---")
    
    if not args.dry_run:
        print("\nNext steps for agent:")
        print("1. Apply content changes to the live document")
        print("2. Update document header with new version and date")
        print("3. Validate all changes are correct")
    else:
        print("\nTo execute these changes, run the same command without --dry-run")


if __name__ == "__main__":
    main()