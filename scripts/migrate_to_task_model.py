#!/usr/bin/env python3
"""
Migration Script: Component-Centric to Task-Centric Workflow State

Migrates from component-centric to task-centric workflow state.
This migration preserves all existing workflow data while restructuring
it to support concurrent tasks on the same component.

Usage:
    python migrate_to_task_model.py [--dry-run] [--backup-dir DIR]
"""

import json
import shutil
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WorkflowStateMigrator:
    """Migrates workflow state from component-centric to task-centric structure."""
    
    def __init__(self, state_file: str = None, backup_dir: str = None):
        if state_file is None:
            # Use robust path resolution
            script_dir = Path(__file__).parent
            project_root = script_dir.parent
            state_file = project_root / "config" / "workflow_state.json"
            
        self.state_file = Path(state_file)
        self.backup_dir = Path(backup_dir) if backup_dir else self.state_file.parent / "backups"
        
    def create_backup(self) -> Path:
        """Create a backup of the current state file."""
        if not self.state_file.exists():
            logger.warning(f"State file does not exist: {self.state_file}")
            return None
            
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"workflow_state_backup_{timestamp}.json"
        backup_path = self.backup_dir / backup_name
        
        shutil.copy2(self.state_file, backup_path)
        logger.info(f"Created backup: {backup_path}")
        
        return backup_path
    
    def load_current_state(self) -> Dict[str, Any]:
        """Load the current workflow state."""
        if not self.state_file.exists():
            logger.warning(f"State file does not exist: {self.state_file}")
            return {}
            
        with open(self.state_file, 'r') as f:
            return json.load(f)
    
    def migrate_to_task_centric(self, old_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert component-centric workflow state to task-centric structure.
        
        Old structure:
        {
          "active_workflows": {
            "component_name": {
              "current_phase": "development",
              "current_version": "2.5.1",
              "history": { ... }
            }
          }
        }
        
        New structure:
        {
          "active_tasks": {
            "task-001": {
              "task_type": "component_feature",
              "target_name": "component_name", 
              "status": "in_progress",
              "active_phase": "development",
              "created": "2025-07-13T...",
              "history": { ... }
            }
          }
        }
        """
        logger.info("Starting migration to task-centric structure")
        
        # Initialize new structure
        new_state = {
            "_description": "Tracks the current state of all active development workflows",
            "_instructions": "This file is automatically updated by the state manager",
            "system_info": {
                "version": "2.0.0",
                "mode": "task-centric", 
                "last_updated": datetime.now().isoformat(),
                "migration_date": datetime.now().isoformat(),
                "migrated_from": old_state.get("system_info", {}).get("version", "1.0.0")
            },
            "active_tasks": {},
            "completed_tasks": {},
            "task_counter": 1
        }
        
        # Migrate active workflows to active tasks
        active_workflows = old_state.get("active_workflows", {})
        task_counter = 1
        
        for component, workflow_data in active_workflows.items():
            task_id = f"migrated-task-{task_counter:03d}"
            
            # Determine task type based on workflow data
            task_type = "component_feature"  # Default assumption
            if "documentation" in component.lower():
                task_type = "documentation_update"
            elif "test" in component.lower():
                task_type = "test_update"
                
            # Create task from workflow
            task = {
                "task_type": task_type,
                "target_name": component,
                "status": "in_progress",
                "human_brief": f"Migrated from component workflow {component}",
                "active_phase": workflow_data.get("current_phase", "unknown"),
                "created": datetime.now().isoformat(),
                "migrated_from": "component_workflow",
                "history": {}
            }
            
            # Convert workflow history to task history
            workflow_history = workflow_data.get("history", {})
            for phase, phase_data in workflow_history.items():
                task["history"][phase] = {
                    "status": phase_data.get("status", "completed"),
                    "started": phase_data.get("started", "unknown"),
                    "completed": phase_data.get("completed"),
                    "artifact_path": phase_data.get("file", ""),
                    "author": phase_data.get("author", "unknown"),
                    "version": phase_data.get("version", "unknown")
                }
                
            new_state["active_tasks"][task_id] = task
            task_counter += 1
            
            logger.info(f"Migrated component '{component}' to task '{task_id}'")
        
        # Migrate completed workflows to completed tasks
        completed_workflows = old_state.get("completed_workflows", {})
        
        for component, workflow_data in completed_workflows.items():
            task_id = f"migrated-completed-{task_counter:03d}"
            
            task = {
                "task_type": "component_feature",
                "target_name": component,
                "status": "completed",
                "human_brief": f"Migrated completed workflow {component}",
                "active_phase": "completed",
                "created": workflow_data.get("completed", datetime.now().isoformat()),
                "completed": workflow_data.get("completed", datetime.now().isoformat()),
                "migrated_from": "component_workflow",
                "verdict": workflow_data.get("verdict", "unknown"),
                "last_version": workflow_data.get("last_version", "unknown"),
                "phases_completed": workflow_data.get("phases_completed", [])
            }
            
            new_state["completed_tasks"][task_id] = task
            task_counter += 1
            
            logger.info(f"Migrated completed component '{component}' to task '{task_id}'")
        
        # Update task counter
        new_state["task_counter"] = task_counter
        
        # Preserve version registry if it exists
        if "version_registry" in old_state:
            new_state["component_versions"] = old_state["version_registry"]
            
        logger.info(f"Migration complete. Created {len(new_state['active_tasks'])} active tasks and {len(new_state['completed_tasks'])} completed tasks")
        
        return new_state
    
    def save_migrated_state(self, new_state: Dict[str, Any], dry_run: bool = False) -> bool:
        """Save the migrated state to file."""
        if dry_run:
            logger.info("DRY RUN: Would save migrated state to file")
            return True
            
        try:
            with open(self.state_file, 'w') as f:
                json.dump(new_state, f, indent=2)
                
            logger.info(f"Saved migrated state to: {self.state_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save migrated state: {e}")
            return False
    
    def validate_migration(self, old_state: Dict[str, Any], new_state: Dict[str, Any]) -> bool:
        """Validate that the migration preserved all important data."""
        logger.info("Validating migration...")
        
        # Count components/tasks
        old_active_count = len(old_state.get("active_workflows", {}))
        old_completed_count = len(old_state.get("completed_workflows", {}))
        new_active_count = len(new_state.get("active_tasks", {}))
        new_completed_count = len(new_state.get("completed_tasks", {}))
        
        logger.info(f"Active workflows: {old_active_count} -> {new_active_count} tasks")
        logger.info(f"Completed workflows: {old_completed_count} -> {new_completed_count} tasks")
        
        # Basic validation
        if new_active_count != old_active_count:
            logger.warning(f"Active count mismatch: {old_active_count} vs {new_active_count}")
            
        if new_completed_count != old_completed_count:
            logger.warning(f"Completed count mismatch: {old_completed_count} vs {new_completed_count}")
        
        # Check that system info was updated
        if new_state.get("system_info", {}).get("mode") != "task-centric":
            logger.error("System mode was not updated to task-centric")
            return False
            
        if new_state.get("system_info", {}).get("version") != "2.0.0":
            logger.error("System version was not updated to 2.0.0")
            return False
        
        logger.info("Migration validation passed")
        return True
    
    def migrate(self, dry_run: bool = False, force: bool = False) -> bool:
        """
        Perform the complete migration process.
        
        Args:
            dry_run: If True, don't actually save changes
            force: If True, proceed even if state is already migrated
            
        Returns:
            True if migration succeeded, False otherwise
        """
        logger.info(f"Starting workflow state migration (dry_run={dry_run})")
        
        # Load current state
        old_state = self.load_current_state()
        if not old_state:
            logger.error("Could not load current state")
            return False
        
        # Check if already migrated
        current_mode = old_state.get("system_info", {}).get("mode", "")
        if current_mode == "task-centric" and not force:
            logger.info("State is already task-centric. Use --force to re-migrate.")
            return True
        
        # Create backup
        if not dry_run:
            backup_path = self.create_backup()
            if backup_path is None:
                logger.error("Could not create backup")
                return False
        
        # Perform migration
        try:
            new_state = self.migrate_to_task_centric(old_state)
            
            # Validate migration
            if not self.validate_migration(old_state, new_state):
                logger.error("Migration validation failed")
                return False
            
            # Save new state
            if not self.save_migrated_state(new_state, dry_run):
                logger.error("Failed to save migrated state")
                return False
                
            logger.info("Migration completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Migration failed: {e}")
            return False


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Migrate workflow state from component-centric to task-centric structure",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be migrated without making changes')
    parser.add_argument('--force', action='store_true',
                       help='Force migration even if already task-centric')
    parser.add_argument('--state-file', 
                       help='Path to workflow state file (default: prompt/config/workflow_state.json)')
    parser.add_argument('--backup-dir',
                       help='Directory for backups (default: same as state file)')
    
    args = parser.parse_args()
    
    # Initialize migrator
    migrator = WorkflowStateMigrator(args.state_file, args.backup_dir)
    
    # Run migration
    success = migrator.migrate(dry_run=args.dry_run, force=args.force)
    
    if success:
        if args.dry_run:
            print("✅ Migration validation passed (dry run)")
        else:
            print("✅ Migration completed successfully")
        return 0
    else:
        print("❌ Migration failed")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())