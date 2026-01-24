#!/usr/bin/env python3
"""
Central State Manager for LLM Agent System

Provides safe, atomic operations for managing LLM agent workflow state
with file locking to prevent corruption from concurrent access.

This replaces the unsafe direct JSON file manipulation pattern and
establishes workflow_state.json as the authoritative source of truth.
"""

import json
import fcntl
import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime
from contextlib import contextmanager

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class StateManager:
    """
    Centralized, transactional state management for workflow_state.json.
    
    Provides safe, atomic operations for managing LLM agent workflow state
    with file locking to prevent corruption from concurrent access.
    """
    
    def __init__(self, state_file: str = None):
        if state_file is None:
            # Use robust path resolution
            script_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(script_dir)
            state_file = os.path.join(project_root, "config", "workflow_state.json")
            
        self.state_file = Path(state_file)
        self._ensure_state_file_exists()
        
    def _ensure_state_file_exists(self):
        """Ensure the state file exists with proper structure."""
        if not self.state_file.exists():
            # Create minimal valid state structure
            initial_state = {
                "_description": "Tracks the current state of all active development workflows",
                "_instructions": "This file is automatically updated by the state manager",
                "system_info": {
                    "version": "2.0.0",
                    "mode": "task-centric",
                    "last_updated": datetime.now().isoformat()
                },
                "active_tasks": {},
                "completed_tasks": {},
                "task_counter": 1
            }
            
            # Ensure parent directory exists
            self.state_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.state_file, 'w') as f:
                json.dump(initial_state, f, indent=2)
                
    def start_task(self, task_id: str, task_type: str, target_name: str, 
               target_version: str, human_brief: str, phase: str = "consultation") -> bool:
        """Start a new task with enhanced version tracking."""
        try:
            with self._locked_state_access() as state:
                if task_id in state.get("active_tasks", {}):
                    logger.error(f"Task {task_id} already exists")
                    return False
                    
                # Initialize task with enhanced schema
                state.setdefault("active_tasks", {})[task_id] = {
                    "task_type": task_type,
                    "target_name": target_name,
                    "target_version": target_version,  # New field
                    "status": "in_progress",
                    "human_brief": human_brief,
                    "active_phase": phase,
                    "created": datetime.now().isoformat(),
                    "folder_path": f"artifacts/{phase}s/{target_name}/{task_id}",  # New field
                    "history": {
                        phase: {
                            "status": "in_progress",
                            "started": datetime.now().isoformat(),
                            "iterations": {},
                            "latest_iteration": 0
                        }
                    }
                }
                
                return True
                
        except Exception as e:
            logger.error(f"Failed to start task {task_id}: {e}")
            return False
        
    def complete_phase(self, task_id: str, artifact_type: str, 
                  status: str = "ready_for_review") -> str:
        """Complete current phase and generate artifact path with iteration tracking."""
        try:
            with self._locked_state_access() as state:
                task = state.get("active_tasks", {}).get(task_id)
                if not task:
                    logger.error(f"Task {task_id} not found")
                    return None
                    
                current_phase = task["active_phase"]
                target_name = task["target_name"]
                target_version = task["target_version"]
                
                # Calculate next iteration
                phase_history = task["history"].get(current_phase, {})
                iterations = phase_history.get("iterations", {})
                next_iteration = len(iterations) + 1
                
                # Generate artifact path using new convention
                folder_path = f"artifacts/{artifact_type}s/{target_name}/{task_id}"
                artifact_name = f"{artifact_type}_{target_name}_{task_id}_v{target_version}_i{next_iteration}.md"
                artifact_path = f"{folder_path}/{artifact_name}"
                
                # Update task history with new iteration
                if "iterations" not in phase_history:
                    phase_history["iterations"] = {}
                
                phase_history["iterations"][str(next_iteration)] = {
                    "artifact_path": artifact_name,
                    "status": "active",
                    "created": datetime.now().isoformat()
                }
                phase_history["latest_iteration"] = next_iteration
                phase_history["status"] = "completed"
                
                # Ensure folder exists
                os.makedirs(folder_path, exist_ok=True)
                
                return artifact_path
                
        except Exception as e:
            logger.error(f"Failed to complete phase for task {task_id}: {e}")
            return None
    
    def get_task_info(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific task."""
        try:
            with self._locked_state_access() as state:
                return state.get("active_tasks", {}).get(task_id)
        except Exception as e:
            logger.error(f"Failed to get task info for {task_id}: {e}")
            return None
    
    def list_active_tasks(self, target_name: Optional[str] = None, 
                         task_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """List active tasks, optionally filtered by target or type."""
        try:
            with self._locked_state_access() as state:
                tasks = []
                for task_id, task_data in state.get("active_tasks", {}).items():
                    # Apply filters if specified
                    if target_name and task_data.get("target_name") != target_name:
                        continue
                    if task_type and task_data.get("task_type") != task_type:
                        continue
                        
                    task_info = task_data.copy()
                    task_info["task_id"] = task_id
                    tasks.append(task_info)
                    
                return tasks
        except Exception as e:
            logger.error(f"Failed to list active tasks: {e}")
            return []
    
    def get_latest_artifact(self, component: str, artifact_type: str) -> Optional[str]:
        """Legacy method for backward compatibility during migration."""
        # First try new structure
        # This is a simplified implementation for the sake of the example.
        # A real implementation would need to query the state for tasks related to the component.
        tasks = self.list_active_tasks(target_name=component)
        if tasks:
            # This is a simplification. A real implementation would need to find the latest iteration.
            task = tasks[-1]
            task_id = task["task_id"]
            target_version = task["target_version"]
            folder_path = f"artifacts/{artifact_type}s/{component}/{task_id}"
            # This is a simplification. A real implementation would need to find the latest iteration.
            artifact_name = f"{artifact_type}_{component}_{task_id}_v{target_version}_i1.md"
            artifact_path = f"{folder_path}/{artifact_name}"
            if os.path.exists(artifact_path):
                return artifact_path

        # Fall back to legacy structure
        legacy_patterns = [
            f"{artifact_type}_v*.md",
            f"{artifact_type}_{component}_v*.md"
        ]
        
        for pattern in legacy_patterns:
            matches = list(Path("prompt/artifacts").rglob(pattern))
            if matches:
                return str(matches[-1])  # Return most recent
        
        return None
    
    def check_task_conflicts(self, task_id: str, target_name: str) -> List[str]:
        """Check for potential conflicts with other active tasks."""
        try:
            conflicts = []
            active_tasks = self.list_active_tasks(target_name=target_name)
            
            for task in active_tasks:
                if task["task_id"] != task_id:
                    conflicts.append(f"Task {task['task_id']} also working on {target_name}")
                    
            return conflicts
            
        except Exception as e:
            logger.error(f"Failed to check task conflicts: {e}")
            return []
    
    @contextmanager
    def _locked_state_access(self):
        """Context manager for safe, locked access to state file."""
        # CRITICAL FIX: Use separate read/write operations to prevent corruption
        lock_acquired = False
        read_file = None
        
        try:
            read_file = open(self.state_file, 'r')
            fcntl.flock(read_file.fileno(), fcntl.LOCK_EX)
            lock_acquired = True
            
            state = json.load(read_file)
            yield state
            
            # Write to file safely with proper truncation
            with open(self.state_file, 'w') as write_file:
                json.dump(state, write_file, indent=2)
                write_file.flush()  # Ensure data is written to buffer
                os.fsync(write_file.fileno())  # Force OS to write to disk
                
        except json.JSONDecodeError as e:
            logger.error(f"JSON corruption detected in state file: {e}")
            raise
        except Exception as e:
            logger.error(f"State access error: {e}")
            raise
        finally:
            if lock_acquired and read_file:
                fcntl.flock(read_file.fileno(), fcntl.LOCK_UN)
            if read_file:
                read_file.close()


def create_cli_parser():
    """Create the command-line interface parser."""
    parser = argparse.ArgumentParser(
        description="LLM Agent System State Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start a new task
  python state_manager.py start-task --task-id "task-001" --type "component_feature" --target "tv_ingest" --brief "Implement enhanced caching"
  
  # Complete current phase
  python state_manager.py complete-phase --task-id "task-001" --output "path/to/artifact.md" --status "ready_for_review"
  
  # Get task information
  python state_manager.py get-task-info --task-id "task-001"
  
  # List active tasks
  python state_manager.py list-tasks --target "tv_ingest"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Start task command
    start_parser = subparsers.add_parser('start-task', help='Start a new task')
    start_parser.add_argument('--task-id', required=True, help='Unique task identifier')
    start_parser.add_argument('--type', required=True, help='Task type (e.g., component_feature)')
    start_parser.add_argument('--target', required=True, help='Target component name')
    start_parser.add_argument('--brief', required=True, help='Brief description of the task')
    start_parser.add_argument('--phase', default='consultation', help='Starting phase (default: consultation)')
    
    # Complete phase command
    complete_parser = subparsers.add_parser('complete-phase', help='Complete current phase')
    complete_parser.add_argument('--task-id', required=True, help='Task identifier')
    complete_parser.add_argument('--output', required=True, help='Path to output artifact')
    complete_parser.add_argument('--status', default='ready_for_review', help='Output status')
    
    # Get task info command
    info_parser = subparsers.add_parser('get-task-info', help='Get task information')
    info_parser.add_argument('--task-id', required=True, help='Task identifier')
    
    # List tasks command
    list_parser = subparsers.add_parser('list-tasks', help='List active tasks')
    list_parser.add_argument('--target', help='Filter by target component')
    list_parser.add_argument('--type', help='Filter by task type')
    
    # Get latest artifact command (backward compatibility)
    artifact_parser = subparsers.add_parser('get-latest-artifact', help='Get latest artifact path')
    artifact_parser.add_argument('--component', required=True, help='Component name')
    artifact_parser.add_argument('--type', required=True, help='Artifact type')
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_cli_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Initialize state manager
    state_manager = StateManager()
    
    try:
        if args.command == 'start-task':
            success = state_manager.start_task(
                args.task_id, args.type, args.target, args.brief, args.phase
            )
            if success:
                print(f"✅ Task {args.task_id} started successfully")
                return 0
            else:
                print(f"❌ Failed to start task {args.task_id}")
                return 1
                
        elif args.command == 'complete-phase':
            success = state_manager.complete_phase(args.task_id, args.output, args.status)
            if success:
                print(f"✅ Phase completed for task {args.task_id}")
                return 0
            else:
                print(f"❌ Failed to complete phase for task {args.task_id}")
                return 1
                
        elif args.command == 'get-task-info':
            task_info = state_manager.get_task_info(args.task_id)
            if task_info:
                print(json.dumps(task_info, indent=2))
                return 0
            else:
                print(f"❌ Task {args.task_id} not found")
                return 1
                
        elif args.command == 'list-tasks':
            tasks = state_manager.list_active_tasks(args.target, args.type)
            if tasks:
                print(json.dumps(tasks, indent=2))
            else:
                print("No active tasks found")
            return 0
            
        elif args.command == 'get-latest-artifact':
            artifact_path = state_manager.get_latest_artifact(args.component, args.type)
            if artifact_path:
                print(artifact_path)
                return 0
            else:
                print(f"❌ No artifact found for {args.component}")
                return 1
                
    except Exception as e:
        logger.error(f"Command failed: {e}")
        print(f"❌ Command failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())