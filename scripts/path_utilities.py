#!/usr/bin/env python3
"""
Path utilities for the LLM Agent System.
Provides standard methods for artifact and configuration management.
"""

import os
import yaml
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ArtifactManager:
    """Manage artifacts following the standard directory structure"""
    
    def __init__(self, prompt_root: str = "prompt"):
        self.prompt_root = Path(prompt_root)
        self.artifacts_root = self.prompt_root / "artifacts"
        
    def get_artifact_path(self, component: str, artifact_type: str, version: str) -> Path:
        """
        Build standard artifact path.
        
        Args:
            component: Component name (e.g., "tv_ingest")
            artifact_type: Type singular (e.g., "plan", "review")
            version: Semantic version (e.g., "2.5.1")
            
        Returns:
            Path to artifact file
        """
        type_plural = f"{artifact_type}s"
        if artifact_type == "devnotes":
            type_plural = "implementations"
        elif artifact_type == "test_report":
            type_plural = "tests"
            
        return self.artifacts_root / type_plural / component / f"{artifact_type}_v{version}.md"
        
    def find_latest_artifact(self, component: str, artifact_type: str) -> Optional[Tuple[str, Path]]:
        """
        DEPRECATED: Use state_manager.py instead.
        
        This function is deprecated in favor of the centralized state manager.
        It will be removed in the next major version.
        
        Returns:
            Tuple of (version, path) or None if not found
        """
        import warnings
        import subprocess
        
        warnings.warn(
            "find_latest_artifact is deprecated. Use state_manager.py CLI instead.",
            DeprecationWarning,
            stacklevel=2
        )
        
        # CRITICAL FIX: Use robust path resolution instead of relative paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        state_manager_path = os.path.join(current_dir, 'state_manager.py')
        
        try:
            result = subprocess.run([
                "python", state_manager_path, 
                "get-latest-artifact", 
                "--component", component, 
                "--type", artifact_type
            ], capture_output=True, text=True, cwd=current_dir)
            
            if result.returncode == 0:
                # Parse state manager output
                path_str = result.stdout.strip()
                if path_str:
                    path = Path(path_str)
                    version = self._extract_version_from_path(path)
                    return (version, path)
        except Exception as e:
            logger.error(f"State manager call failed: {e}")
            
        # Fallback to legacy filesystem discovery (temporary backward compatibility)
        return self._legacy_find_latest_artifact(component, artifact_type)
    
    def _extract_version_from_path(self, path: Path) -> str:
        """Extract version from artifact path."""
        pattern = re.compile(r"_v(\d+\.\d+\.\d+)\.md$")
        match = pattern.search(path.name)
        return match.group(1) if match else "unknown"
    
    def _legacy_find_latest_artifact(self, component: str, artifact_type: str) -> Optional[Tuple[str, Path]]:
        """
        Legacy filesystem discovery (temporary backward compatibility).
        This will be removed when all components migrate to state manager.
        """
        type_plural = f"{artifact_type}s"
        if artifact_type == "devnotes":
            type_plural = "implementations"
        elif artifact_type == "test_report":
            type_plural = "tests"
            
        component_dir = self.artifacts_root / type_plural / component
        
        if not component_dir.exists():
            return None
            
        # Find all versions
        versions = []
        pattern = re.compile(f"^{artifact_type}_v(\\d+\\.\\d+\\.\\d+)\\.md$")
        
        for file_path in component_dir.glob(f"{artifact_type}_v*.md"):
            match = pattern.match(file_path.name)
            if match:
                version = match.group(1)
                versions.append((version, file_path))
                
        if not versions:
            return None
            
        # Sort by semantic version
        versions.sort(key=lambda x: tuple(map(int, x[0].split('.'))))
        return versions[-1]  # Return latest
        
    def create_artifact(self, component: str, artifact_type: str, version: str, content: str) -> Path:
        """Create a new artifact with the given content"""
        artifact_path = self.get_artifact_path(component, artifact_type, version)
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(artifact_path, 'w') as f:
            f.write(content)
            
        logger.info(f"Created artifact: {artifact_path}")
        return artifact_path
        
    # NOTE: archive_artifact method removed - replaced by archive_manager.py
    # which implements the authoritative archive strategy defined in general.md


class ConfigManager:
    """Manage configuration files"""
    
    def __init__(self, prompt_root: str = "prompt"):
        self.prompt_root = Path(prompt_root)
        self.config_root = self.prompt_root / "_config"
        
    def load_shared_definitions(self) -> Dict:
        """Load shared definitions"""
        config_path = self.config_root / "shared_definitions.yaml"
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
            
    def load_project_context(self) -> Dict:
        """Load project context"""
        config_path = self.config_root / "project_context.yaml"
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
            
    def load_workflow_state(self) -> Dict:
        """Load current workflow state"""
        config_path = self.config_root / "workflow_state.yaml"
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
            
    def update_workflow_state(self, component: str, updates: Dict) -> None:
        """Update workflow state for a component"""
        state = self.load_workflow_state()
        
        if component not in state["active_components"]:
            state["active_components"][component] = {}
            
        state["active_components"][component].update(updates)
        state["active_components"][component]["last_updated"] = datetime.now().isoformat()
        state["last_updated"] = datetime.now().isoformat()
        
        config_path = self.config_root / "workflow_state.yaml"
        with open(config_path, 'w') as f:
            yaml.dump(state, f, default_flow_style=False)
            
        logger.info(f"Updated workflow state for {component}")


class RoleManager:
    """Manage role definitions and prompts"""
    
    def __init__(self, prompt_root: str = "prompt"):
        self.prompt_root = Path(prompt_root)
        self.roles_root = self.prompt_root / "roles"
        
    def load_role_prompt(self, role: str, claude_specific: bool = False) -> str:
        """Load system prompt for a role"""
        role_dir = self.roles_root / role
        
        if claude_specific:
            prompt_file = role_dir / f"CLAUDE_{role.upper()}.md"
            if not prompt_file.exists():
                logger.warning(f"Claude-specific prompt not found for {role}, using generic")
                prompt_file = role_dir / "system.md"
        else:
            prompt_file = role_dir / "system.md"
            
        with open(prompt_file, 'r') as f:
            return f.read()
            
    def load_conversation_template(self, role: str) -> Optional[str]:
        """Load conversation template for a role"""
        template_path = self.roles_root / role / "conversation.md"
        
        if not template_path.exists():
            return None
            
        with open(template_path, 'r') as f:
            return f.read()
            
    def build_full_prompt(self, role: str, task_context: Dict, claude_specific: bool = False) -> str:
        """Build complete prompt with context injection"""
        # Load base prompt
        base_prompt = self.load_role_prompt(role, claude_specific)
        
        # Load shared context
        config_mgr = ConfigManager(self.prompt_root)
        shared_defs = config_mgr.load_shared_definitions()
        project_ctx = config_mgr.load_project_context()
        
        # Build context section
        context_section = "\n## Current Context\n\n"
        context_section += f"**Component:** {task_context.get('component', 'Unknown')}\n"
        context_section += f"**Version:** {task_context.get('version', 'Unknown')}\n"
        context_section += f"**Phase:** {task_context.get('phase', 'Unknown')}\n\n"
        
        # Add project standards
        context_section += "### Project Standards\n"
        for key, value in project_ctx.get('naming_conventions', {}).items():
            context_section += f"- **{key}:** `{value}`\n"
            
        # Combine prompt sections
        full_prompt = base_prompt + "\n\n" + context_section
        
        return full_prompt


class ComponentManager:
    """Manage component metadata"""
    
    def __init__(self, prompt_root: str = "prompt"):
        self.prompt_root = Path(prompt_root)
        self.components_root = self.prompt_root / "components"
        
    def load_component_context(self, component: str) -> Optional[Dict]:
        """Load context for a component"""
        context_path = self.components_root / component / "context.yaml"
        
        if not context_path.exists():
            return None
            
        with open(context_path, 'r') as f:
            return yaml.safe_load(f)
            
    def create_component(self, component: str, description: str, owner: str) -> None:
        """Create a new component with metadata"""
        component_dir = self.components_root / component
        component_dir.mkdir(parents=True, exist_ok=True)
        
        context = {
            "component": {
                "name": component,
                "description": description,
                "owner": owner,
                "created": datetime.now().isoformat(),
                "architecture": {
                    "pattern": "service-facade",
                    "language": "python"
                }
            }
        }
        
        with open(component_dir / "context.yaml", 'w') as f:
            yaml.dump(context, f, default_flow_style=False)
            
        logger.info(f"Created component: {component}")
        
    def get_component_history(self, component: str) -> List[Dict]:
        """Get version history for a component"""
        artifact_mgr = ArtifactManager(self.prompt_root)
        history = []
        
        # Check all artifact types
        artifact_types = ["consultation", "plan", "devnotes", "review", "test_report"]
        
        for artifact_type in artifact_types:
            latest = artifact_mgr.find_latest_artifact(component, artifact_type)
            if latest:
                version, path = latest
                history.append({
                    "type": artifact_type,
                    "version": version,
                    "path": str(path.relative_to(self.prompt_root)),
                    "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
                })
                
        return sorted(history, key=lambda x: x["modified"], reverse=True)


# Example usage functions
def example_create_plan():
    """Example: Create a new plan artifact"""
    artifact_mgr = ArtifactManager()
    config_mgr = ConfigManager()
    
    # Create a plan
    component = "tv_ingest"
    version = "2.5.2"
    
    content = """# Development Plan: TV Ingest Enhancement

## Metadata Block
- **Version:** 2.5.2
- **Author:** Planner Alpha
- **Date:** 2024-01-07
- **Status:** ready_for_review

## Executive Summary
This plan outlines the implementation of enhanced caching...
"""
    
    # Create the artifact
    artifact_path = artifact_mgr.create_artifact(component, "plan", version, content)
    
    # Update workflow state
    config_mgr.update_workflow_state(component, {
        "current_phase": "planning",
        "current_version": version,
        "status": "ready_for_review"
    })
    
    print(f"Created plan at: {artifact_path}")
    

def example_find_artifacts():
    """Example: Find latest artifacts for a component"""
    artifact_mgr = ArtifactManager()
    component_mgr = ComponentManager()
    
    component = "tv_ingest"
    
    # Get component context
    context = component_mgr.load_component_context(component)
    if context:
        print(f"Component: {context['component']['name']}")
        print(f"Description: {context['component']['description']}")
        
    # Get component history
    history = component_mgr.get_component_history(component)
    print(f"\nComponent History:")
    for item in history:
        print(f"  - {item['type']} v{item['version']} ({item['modified']})")
        

def example_build_prompt():
    """Example: Build a complete prompt for a role"""
    role_mgr = RoleManager()
    
    # Build prompt for developer role
    prompt = role_mgr.build_full_prompt("developer", {
        "component": "tv_ingest",
        "version": "2.5.2", 
        "phase": "implementation"
    }, claude_specific=True)
    
    print("Generated Developer Prompt:")
    print("-" * 40)
    print(prompt[:500] + "...")  # Print first 500 chars


if __name__ == "__main__":
    print("LLM Agent System Path Utilities\n")
    
    examples = {
        "1": ("Create a plan artifact", example_create_plan),
        "2": ("Find component artifacts", example_find_artifacts),
        "3": ("Build role prompt", example_build_prompt)
    }
    
    print("Available examples:")
    for key, (desc, _) in examples.items():
        print(f"  {key}. {desc}")
        
    choice = input("\nSelect example (1-3): ")
    
    if choice in examples:
        print(f"\nRunning: {examples[choice][0]}\n")
        examples[choice][1]()
    else:
        print("Invalid choice")