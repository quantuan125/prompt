# File: prompt/scripts/migrate_to_enhanced_versioning.py
#!/usr/bin/env python3
"""
Migration script for enhanced Task ID + Version + Iteration Counter system.
Converts existing artifacts to new naming convention and folder structure.
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

class ArtifactMigrator:
    """Handles migration of existing artifacts to new structure."""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.backup_path = self.base_path / "migration_backup"
        
    def migrate_all_artifacts(self) -> bool:
        """Migrate all existing artifacts to new structure."""
        try:
            # Create backup
            self._create_backup()
            
            # Migrate by category
            self._migrate_consultations()
            self._migrate_plans()
            self._migrate_developments()
            self._migrate_reviews()
            
            # Update state file
            self._update_state_file()
            
            logger.info("Migration completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Migration failed: {e}")
            self._rollback_changes()
            return False
    
    def _migrate_consultations(self):
        """Migrate consultation artifacts."""
        consultation_path = self.base_path / "artifacts" / "consultations"
        for file_path in consultation_path.rglob("consultation_*.md"):
            self._migrate_single_file(file_path, "consultation")
    
    def _migrate_single_file(self, file_path: Path, artifact_type: str):
        """Migrate a single artifact file to new structure."""
        # Parse existing filename to extract component and version
        filename = file_path.name
        if "_v" in filename:
            base_name, version_part = filename.rsplit("_v", 1)
            version = version_part.replace(".md", "")
            component = base_name.replace(f"{artifact_type}_", "")
        else:
            # Handle legacy naming
            component = "unknown"
            version = "1.0.0"
        
        # Generate new structure
        task_id = self._generate_task_id(component, artifact_type)
        new_folder = self.base_path / "artifacts" / f"{artifact_type}s" / component / task_id
        new_filename = f"{artifact_type}_{component}_{task_id}_v{version}_i1.md"
        new_path = new_folder / new_filename
        
        # Create folder and move file
        new_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, new_path)
        
        # Update file content with new header
        self._update_file_header(new_path, task_id, artifact_type, component, version)
