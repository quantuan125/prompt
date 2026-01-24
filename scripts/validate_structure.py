#!/usr/bin/env python3
"""
Validation script to ensure directory structure follows standards.
Run from project root: python prompt/scripts/validate_structure.py
"""

import os
import yaml
import re
from pathlib import Path
from typing import List, Tuple, Dict
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StructureValidator:
    def __init__(self, prompt_root="prompt"):
        self.prompt_root = Path(prompt_root)
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_all(self) -> bool:
        """Run all validation checks"""
        logger.info("Starting structure validation")
        
        checks = [
            self.validate_root_structure,
            self.validate_config_files,
            self.validate_templates,
            self.validate_roles,
            self.validate_artifacts,
            self.validate_components,
            self.validate_naming_conventions,
            self.validate_no_mixed_content,
            self.validate_version_consistency
        ]
        
        for check in checks:
            check()
            
        self.print_report()
        return len(self.errors) == 0
        
    def validate_root_structure(self):
        """Validate root directory structure exists"""
        logger.info("Validating root structure")
        
        required_dirs = [
            "_config",
            "_templates",
            "_archive",
            "roles",
            "artifacts", 
            "components",
            "scripts"
        ]
        
        for dir_name in required_dirs:
            dir_path = self.prompt_root / dir_name
            if not dir_path.exists():
                self.errors.append(f"Missing required directory: {dir_name}")
            elif not dir_path.is_dir():
                self.errors.append(f"{dir_name} exists but is not a directory")
                
    def validate_config_files(self):
        """Validate configuration files exist and are valid"""
        logger.info("Validating configuration files")
        
        config_files = {
            "shared_definitions.yaml": ["statuses", "artifact_types", "roles"],
            "project_context.yaml": ["architecture", "naming_conventions"],
            "workflow_state.yaml": ["active_components"]
        }
        
        config_dir = self.prompt_root / "_config"
        
        for file_name, required_keys in config_files.items():
            file_path = config_dir / file_name
            
            if not file_path.exists():
                self.errors.append(f"Missing config file: {file_name}")
                continue
                
            try:
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    
                if not data:
                    self.errors.append(f"Config file {file_name} is empty")
                    continue
                    
                for key in required_keys:
                    if key not in data:
                        self.errors.append(f"Config file {file_name} missing required key: {key}")
                        
            except yaml.YAMLError as e:
                self.errors.append(f"Invalid YAML in {file_name}: {e}")
                
    def validate_templates(self):
        """Validate template files"""
        logger.info("Validating templates")
        
        template_dir = self.prompt_root / "_templates"
        expected_templates = [
            "consultation.md",
            "planning.md",
            "development.md",
            "review.md"
        ]
        
        found_templates = list(template_dir.glob("*.md"))
        found_names = [t.name for t in found_templates]
        
        for template in expected_templates:
            if template not in found_names:
                self.warnings.append(f"Missing expected template: {template}")
                
        # Check template structure
        for template_path in found_templates:
            self._validate_template_structure(template_path)
            
    def _validate_template_structure(self, template_path: Path):
        """Validate individual template structure"""
        with open(template_path, 'r') as f:
            content = f.read()
            
        # Check for required sections
        required_sections = ["## Metadata", "## Executive Summary", "## Next Steps"]
        
        for section in required_sections:
            if section not in content:
                self.warnings.append(f"Template {template_path.name} missing section: {section}")
                
    def validate_roles(self):
        """Validate role directories and files"""
        logger.info("Validating roles")
        
        roles_dir = self.prompt_root / "roles"
        
        # Load expected roles from config
        config_path = self.prompt_root / "_config" / "shared_definitions.yaml"
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                expected_roles = config.get("roles", [])
        else:
            expected_roles = ["consultant", "planner", "developer", "reviewer"]
            
        for role in expected_roles:
            role_dir = roles_dir / role
            
            if not role_dir.exists():
                self.errors.append(f"Missing role directory: {role}")
                continue
                
            # Check for required files
            required_files = ["system.md"]
            optional_files = [f"CLAUDE_{role.upper()}.md", "conversation.md"]
            
            for file_name in required_files:
                if not (role_dir / file_name).exists():
                    self.errors.append(f"Role {role} missing required file: {file_name}")
                    
            for file_name in optional_files:
                if not (role_dir / file_name).exists():
                    self.info.append(f"Role {role} missing optional file: {file_name}")
                    
    def validate_artifacts(self):
        """Validate artifact directory structure"""
        logger.info("Validating artifacts")
        
        artifacts_dir = self.prompt_root / "artifacts"
        expected_types = ["consultations", "plans", "implementations", "reviews", "tests"]
        
        for artifact_type in expected_types:
            type_dir = artifacts_dir / artifact_type
            
            if not type_dir.exists():
                self.warnings.append(f"Missing artifact type directory: {artifact_type}")
                continue
                
            # Check artifacts follow naming convention
            for component_dir in type_dir.iterdir():
                if component_dir.is_dir():
                    self._validate_artifact_files(component_dir, artifact_type)
                    
    def _validate_artifact_files(self, component_dir: Path, artifact_type: str):
        """Validate artifact files in a component directory"""
        # Determine expected prefix
        prefix_map = {
            "consultations": "consultation",
            "plans": "plan",
            "implementations": "devnotes",
            "reviews": "review",
            "tests": "test_report"
        }
        
        expected_prefix = prefix_map.get(artifact_type, artifact_type.rstrip('s'))
        pattern = re.compile(f"^{expected_prefix}_v\\d+\\.\\d+\\.\\d+\\.md$")
        
        for file_path in component_dir.glob("*.md"):
            if not pattern.match(file_path.name):
                self.errors.append(
                    f"Artifact {file_path.relative_to(self.prompt_root)} "
                    f"doesn't follow naming convention: {expected_prefix}_vX.Y.Z.md"
                )
                
    def validate_components(self):
        """Validate component metadata"""
        logger.info("Validating components")
        
        components_dir = self.prompt_root / "components"
        
        # Find all components with artifacts
        artifact_components = set()
        artifacts_dir = self.prompt_root / "artifacts"
        
        for type_dir in artifacts_dir.iterdir():
            if type_dir.is_dir():
                for component_dir in type_dir.iterdir():
                    if component_dir.is_dir():
                        artifact_components.add(component_dir.name)
                        
        # Check each component has metadata
        for component in artifact_components:
            component_dir = components_dir / component
            
            if not component_dir.exists():
                self.warnings.append(f"Component {component} has artifacts but no metadata directory")
                continue
                
            context_file = component_dir / "context.yaml"
            if not context_file.exists():
                self.warnings.append(f"Component {component} missing context.yaml")
                
    def validate_naming_conventions(self):
        """Validate all files follow naming conventions"""
        logger.info("Validating naming conventions")
        
        # Check for spaces in filenames
        for file_path in self.prompt_root.rglob("*"):
            if " " in file_path.name:
                self.errors.append(f"File contains spaces: {file_path.relative_to(self.prompt_root)}")
                
            # Check for uppercase in paths (except CLAUDE_ prefix)
            if file_path.is_file() and not file_path.name.startswith("CLAUDE_"):
                if any(c.isupper() for c in file_path.stem):
                    self.warnings.append(
                        f"File uses uppercase (should be lowercase): "
                        f"{file_path.relative_to(self.prompt_root)}"
                    )
                    
    def validate_no_mixed_content(self):
        """Ensure artifacts aren't mixed with system files"""
        logger.info("Validating content separation")
        
        # Check role directories don't contain artifacts
        roles_dir = self.prompt_root / "roles"
        artifact_pattern = re.compile(r".*_v\d+\.\d+\.\d+\.md$")
        
        for role_dir in roles_dir.iterdir():
            if role_dir.is_dir():
                for file_path in role_dir.rglob("*.md"):
                    if artifact_pattern.match(file_path.name):
                        self.errors.append(
                            f"Artifact found in role directory: "
                            f"{file_path.relative_to(self.prompt_root)}"
                        )
                        
    def validate_version_consistency(self):
        """Validate version numbers are consistent"""
        logger.info("Validating version consistency")
        
        # Check workflow state versions match artifact versions
        workflow_state_path = self.prompt_root / "_config" / "workflow_state.yaml"
        
        if workflow_state_path.exists():
            with open(workflow_state_path, 'r') as f:
                workflow_state = yaml.safe_load(f)
                
            active_components = workflow_state.get("active_components", {})
            
            for component, state in active_components.items():
                current_version = state.get("current_version")
                if current_version:
                    # Find latest artifact versions
                    self._check_version_consistency(component, current_version)
                    
    def _check_version_consistency(self, component: str, expected_version: str):
        """Check if component artifacts match expected version"""
        artifacts_dir = self.prompt_root / "artifacts"
        
        for type_dir in artifacts_dir.iterdir():
            if type_dir.is_dir():
                component_dir = type_dir / component
                if component_dir.exists():
                    # Find latest version
                    versions = []
                    for file_path in component_dir.glob("*_v*.md"):
                        match = re.search(r"_v(\d+\.\d+\.\d+)\.md$", file_path.name)
                        if match:
                            versions.append(match.group(1))
                            
                    if versions and expected_version not in versions:
                        self.warnings.append(
                            f"Component {component} workflow state shows v{expected_version} "
                            f"but found versions: {', '.join(sorted(versions))}"
                        )
                        
    def print_report(self):
        """Print validation report"""
        print("\n" + "="*60)
        print("STRUCTURE VALIDATION REPORT")
        print("="*60)
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)})")
            print("-" * 40)
            for error in self.errors:
                print(f"  • {error}")
                
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)})")
            print("-" * 40)
            for warning in self.warnings:
                print(f"  • {warning}")
                
        if self.info:
            print(f"\nℹ️  INFO ({len(self.info)})")
            print("-" * 40)
            for info in self.info:
                print(f"  • {info}")
                
        print("\n" + "="*60)
        
        if not self.errors:
            print("✅ Structure validation PASSED")
        else:
            print("❌ Structure validation FAILED")
            
        print(f"\nSummary: {len(self.errors)} errors, {len(self.warnings)} warnings, {len(self.info)} info")
        print("="*60 + "\n")
        
    def generate_structure_tree(self):
        """Generate a visual tree of the current structure"""
        logger.info("Generating structure tree")
        
        def print_tree(directory: Path, prefix: str = "", is_last: bool = True):
            """Recursively print directory tree"""
            connector = "└── " if is_last else "├── "
            print(prefix + connector + directory.name)
            
            if directory.is_dir():
                extension = "    " if is_last else "│   "
                items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name))
                
                for i, item in enumerate(items):
                    is_last_item = i == len(items) - 1
                    if item.name not in ['.DS_Store', '__pycache__', '.git']:
                        print_tree(item, prefix + extension, is_last_item)
                        
        print("\nCurrent Directory Structure:")
        print("prompt/")
        
        items = sorted(self.prompt_root.iterdir(), key=lambda x: (x.is_file(), x.name))
        for i, item in enumerate(items):
            if item.name not in ['.DS_Store', '__pycache__', '.git']:
                print_tree(item, "", i == len(items) - 1)


if __name__ == "__main__":
    validator = StructureValidator()
    
    # Run validation
    is_valid = validator.validate_all()
    
    # Generate structure tree
    response = input("\nGenerate directory tree? (y/N): ")
    if response.lower() == 'y':
        validator.generate_structure_tree()
        
    # Exit with appropriate code
    exit(0 if is_valid else 1)