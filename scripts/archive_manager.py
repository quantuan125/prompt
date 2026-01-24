#!/usr/bin/env python3
"""
Archive Manager for LLM Agent System

Implements the authoritative archive strategy defined in general.md.
Uses version-based archiving (archive/doc_vX.Y.Z.md) instead of 
timestamp-based approach to maintain consistency.

This addresses the conflicting archive strategies identified by the consultant
between path_utilities.py and general.md standards.
"""

import os
import shutil
import json
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict
import re

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ArchiveManager:
    """
    Implements the authoritative archive strategy defined in general.md.
    
    Uses version-based archiving (archive/doc_vX.Y.Z.md) instead of 
    timestamp-based approach to maintain consistency with project standards.
    """
    
    def __init__(self, project_root: str = None):
        if project_root is None:
            # Use robust path resolution
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.project_root = Path(os.path.dirname(script_dir))
        else:
            self.project_root = Path(project_root)
            
    def archive_document(self, doc_path: str, version: str, reason: str = None) -> Path:
        """
        Archive a document following general.md standards.
        
        Args:
            doc_path: Path to the document to archive
            version: Version string (e.g., "2.0.0")
            reason: Optional reason for archiving
            
        Returns:
            Path to the archived document
        """
        doc_path = Path(doc_path)
        
        if not doc_path.exists():
            raise FileNotFoundError(f"Document not found: {doc_path}")
            
        # Determine archive location based on document type
        if "prompt/" in str(doc_path):
            archive_dir = self.project_root / "prompt" / "archive"
            
            # Further categorize prompt archives
            if "consultant/" in str(doc_path):
                archive_dir = archive_dir / "roles" / "consultant"
            elif "planner/" in str(doc_path):
                archive_dir = archive_dir / "roles" / "planner"
            elif "developer/" in str(doc_path):
                archive_dir = archive_dir / "roles" / "developer"
            elif "reviewer/" in str(doc_path):
                archive_dir = archive_dir / "roles" / "reviewer"
            elif "config/" in str(doc_path):
                archive_dir = archive_dir / "config"
            elif "templates/" in str(doc_path):
                archive_dir = archive_dir / "templates"
            else:
                archive_dir = archive_dir / "artifacts"
                
        elif "documentation/" in str(doc_path):
            archive_dir = doc_path.parent / "archive"
        else:
            # Default archive location
            archive_dir = doc_path.parent / "archive"
            
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        # Create version-based archive name following general.md standards
        archive_name = f"{doc_path.stem}_v{version}{doc_path.suffix}"
        archive_path = archive_dir / archive_name
        
        # Copy to archive with metadata
        shutil.copy2(doc_path, archive_path)
        
        # Create archive metadata
        metadata = {
            "original_path": str(doc_path),
            "archive_path": str(archive_path),
            "version": version,
            "archived_date": datetime.now().isoformat(),
            "reason": reason or "Automated archiving",
            "file_size": doc_path.stat().st_size,
            "original_modified": datetime.fromtimestamp(doc_path.stat().st_mtime).isoformat()
        }
        
        # Save metadata
        metadata_path = archive_path.with_suffix('.metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        logger.info(f"Archived {doc_path} to {archive_path} (v{version})")
        return archive_path
        
    def clean_old_archives(self, doc_path: str, keep_versions: int = 3) -> List[Path]:
        """
        Clean old archive versions, keeping only the most recent.
        
        Args:
            doc_path: Path to the original document
            keep_versions: Number of versions to keep (default: 3)
            
        Returns:
            List of paths that were removed
        """
        doc_path = Path(doc_path)
        
        # Find archive directory
        if "prompt/" in str(doc_path):
            archive_dir = self.project_root / "prompt" / "archive"
        elif "documentation/" in str(doc_path):
            archive_dir = doc_path.parent / "archive"
        else:
            archive_dir = doc_path.parent / "archive"
            
        if not archive_dir.exists():
            return []
            
        # Find all archived versions of this document
        base_name = doc_path.stem
        pattern = re.compile(f"^{re.escape(base_name)}_v(\\d+\\.\\d+\\.\\d+)\\{doc_path.suffix}$")
        
        archived_versions = []
        for file_path in archive_dir.rglob(f"{base_name}_v*{doc_path.suffix}"):
            match = pattern.match(file_path.name)
            if match:
                version = match.group(1)
                archived_versions.append((version, file_path))
                
        if len(archived_versions) <= keep_versions:
            return []
            
        # Sort by semantic version and remove oldest
        archived_versions.sort(key=lambda x: tuple(map(int, x[0].split('.'))))
        to_remove = archived_versions[:-keep_versions]
        
        removed_paths = []
        for version, file_path in to_remove:
            try:
                # Remove archive file
                file_path.unlink()
                removed_paths.append(file_path)
                
                # Remove metadata if it exists
                metadata_path = file_path.with_suffix('.metadata.json')
                if metadata_path.exists():
                    metadata_path.unlink()
                    
                logger.info(f"Removed old archive: {file_path}")
            except Exception as e:
                logger.error(f"Failed to remove {file_path}: {e}")
                
        return removed_paths
        
    def list_archives(self, doc_path: str = None) -> List[Dict]:
        """
        List all archives, optionally filtered by document path.
        
        Args:
            doc_path: Optional path to filter archives
            
        Returns:
            List of archive information dictionaries
        """
        archives = []
        
        # Search common archive locations
        search_dirs = [
            self.project_root / "prompt" / "archive",
            self.project_root / "documentation" / "archive"
        ]
        
        for search_dir in search_dirs:
            if not search_dir.exists():
                continue
                
            for metadata_file in search_dir.rglob("*.metadata.json"):
                try:
                    with open(metadata_file, 'r') as f:
                        metadata = json.load(f)
                        
                    # Filter by document path if specified
                    if doc_path and doc_path not in metadata.get('original_path', ''):
                        continue
                        
                    archives.append(metadata)
                except Exception as e:
                    logger.error(f"Failed to read metadata {metadata_file}: {e}")
                    
        # Sort by archived date (newest first)
        archives.sort(key=lambda x: x.get('archived_date', ''), reverse=True)
        return archives
        
    def restore_archive(self, archive_path: str, target_path: str = None) -> Path:
        """
        Restore an archived document to its original location or specified path.
        
        Args:
            archive_path: Path to the archived document
            target_path: Optional target path (defaults to original location)
            
        Returns:
            Path where the document was restored
        """
        archive_path = Path(archive_path)
        
        if not archive_path.exists():
            raise FileNotFoundError(f"Archive not found: {archive_path}")
            
        # Load metadata to get original path
        metadata_path = archive_path.with_suffix('.metadata.json')
        if metadata_path.exists():
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            original_path = Path(metadata['original_path'])
        else:
            # Fallback: try to derive original path from archive name
            # This is a best-effort approach
            logger.warning(f"No metadata found for {archive_path}, using fallback restoration")
            original_path = archive_path.parent.parent / archive_path.name
            
        restore_path = Path(target_path) if target_path else original_path
        
        # Ensure parent directory exists
        restore_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy from archive
        shutil.copy2(archive_path, restore_path)
        
        logger.info(f"Restored {archive_path} to {restore_path}")
        return restore_path
        
    def get_next_version(self, doc_path: str, change_type: str = "minor") -> str:
        """
        Get the next version number for a document based on existing archives.
        
        Args:
            doc_path: Path to the document
            change_type: Type of change ("major", "minor", "patch")
            
        Returns:
            Next version string
        """
        doc_path = Path(doc_path)
        archives = self.list_archives(str(doc_path))
        
        if not archives:
            return "1.0.0"
            
        # Find the highest version
        versions = []
        for archive in archives:
            version_str = archive.get('version', '0.0.0')
            try:
                version_parts = tuple(map(int, version_str.split('.')))
                versions.append(version_parts)
            except ValueError:
                continue
                
        if not versions:
            return "1.0.0"
            
        highest = max(versions)
        major, minor, patch = highest
        
        if change_type == "major":
            return f"{major + 1}.0.0"
        elif change_type == "minor":
            return f"{major}.{minor + 1}.0"
        else:  # patch
            return f"{major}.{minor}.{patch + 1}"


def create_cli_parser():
    """Create the command-line interface parser."""
    parser = argparse.ArgumentParser(
        description="LLM Agent System Archive Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Archive a document
  python archive_manager.py archive --path "prompt/documentation/prompt_main.md" --version "2.0.0" --reason "Major update"
  
  # List archives
  python archive_manager.py list --path "prompt/documentation/"
  
  # Clean old archives
  python archive_manager.py clean --path "prompt/documentation/prompt_main.md" --keep 3
  
  # Restore an archive
  python archive_manager.py restore --archive "prompt/archive/prompt_main_v1.0.0.md"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Archive command
    archive_parser = subparsers.add_parser('archive', help='Archive a document')
    archive_parser.add_argument('--path', required=True, help='Path to document to archive')
    archive_parser.add_argument('--version', required=True, help='Version string (e.g., "2.0.0")')
    archive_parser.add_argument('--reason', help='Reason for archiving')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List archives')
    list_parser.add_argument('--path', help='Filter by document path')
    
    # Clean command
    clean_parser = subparsers.add_parser('clean', help='Clean old archives')
    clean_parser.add_argument('--path', required=True, help='Path to document')
    clean_parser.add_argument('--keep', type=int, default=3, help='Number of versions to keep')
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore an archive')
    restore_parser.add_argument('--archive', required=True, help='Path to archived document')
    restore_parser.add_argument('--target', help='Target path for restoration')
    
    # Next version command
    version_parser = subparsers.add_parser('next-version', help='Get next version number')
    version_parser.add_argument('--path', required=True, help='Path to document')
    version_parser.add_argument('--type', choices=['major', 'minor', 'patch'], default='minor', help='Type of change')
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_cli_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Initialize archive manager
    archive_manager = ArchiveManager()
    
    try:
        if args.command == 'archive':
            archive_path = archive_manager.archive_document(args.path, args.version, args.reason)
            print(f"✅ Document archived to: {archive_path}")
            return 0
            
        elif args.command == 'list':
            archives = archive_manager.list_archives(args.path)
            if archives:
                print(f"Found {len(archives)} archive(s):")
                for archive in archives:
                    print(f"  {archive['original_path']} v{archive['version']} ({archive['archived_date']})")
            else:
                print("No archives found")
            return 0
            
        elif args.command == 'clean':
            removed = archive_manager.clean_old_archives(args.path, args.keep)
            print(f"✅ Removed {len(removed)} old archive(s)")
            for path in removed:
                print(f"  Removed: {path}")
            return 0
            
        elif args.command == 'restore':
            restore_path = archive_manager.restore_archive(args.archive, args.target)
            print(f"✅ Archive restored to: {restore_path}")
            return 0
            
        elif args.command == 'next-version':
            next_version = archive_manager.get_next_version(args.path, args.type)
            print(next_version)
            return 0
            
    except Exception as e:
        logger.error(f"Command failed: {e}")
        print(f"❌ Command failed: {e}")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())