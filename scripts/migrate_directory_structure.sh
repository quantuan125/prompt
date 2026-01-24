#!/bin/bash
# File: prompt/scripts/migrate_directory_structure.sh
#
# Directory Structure Migration Script
# Migrates from mixed role-centric and function-centric organization
# to pure function-centric layout with prompt/roles/, prompt/templates/
#
# Usage: ./migrate_directory_structure.sh [--dry-run] [--backup-dir DIR]

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BACKUP_DIR="$PROJECT_ROOT/migration_backup_$(date +%Y%m%d_%H%M%S)"
DRY_RUN=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --backup-dir)
            BACKUP_DIR="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [--dry-run] [--backup-dir DIR]"
            echo "  --dry-run      Show what would be moved without making changes"
            echo "  --backup-dir   Directory for backup (default: migration_backup_TIMESTAMP)"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Create backup function
create_backup() {
    if [[ "$DRY_RUN" == "true" ]]; then
        log "DRY RUN: Would create backup at $BACKUP_DIR"
        return
    fi
    
    log "Creating backup at $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
    
    # Backup existing directories that will be modified
    for dir in consultant planner developer reviewer templates; do
        if [[ -d "$PROJECT_ROOT/$dir" ]]; then
            cp -r "$PROJECT_ROOT/$dir" "$BACKUP_DIR/"
            log "Backed up $dir"
        fi
    done
    
    log "Backup completed"
}

# Execute or simulate command
execute_cmd() {
    if [[ "$DRY_RUN" == "true" ]]; then
        log "DRY RUN: $1"
    else
        log "Executing: $1"
        eval "$1"
    fi
}

# Create new directory structure
create_new_structure() {
    log "Creating new directory structure..."
    
    # Create new standard directories
    execute_cmd "mkdir -p $PROJECT_ROOT/roles/{consultant,planner,developer,reviewer}"
    execute_cmd "mkdir -p $PROJECT_ROOT/templates/{consultant,planner,developer,reviewer}"
    execute_cmd "mkdir -p $PROJECT_ROOT/archive/{artifacts,config,roles,templates}"
    
    log "New directory structure created"
}

# Move role system prompts to centralized location
migrate_role_files() {
    log "Migrating role system files..."
    
    # Migrate consultant files
    if [[ -f "$PROJECT_ROOT/consultant/consultant_system.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/consultant/consultant_system.md' '$PROJECT_ROOT/roles/consultant/'"
    fi
    
    if [[ -f "$PROJECT_ROOT/consultant/CLAUDE_CONSULTANT.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/consultant/CLAUDE_CONSULTANT.md' '$PROJECT_ROOT/roles/consultant/'"
    fi
    
    # Migrate planner files  
    if [[ -f "$PROJECT_ROOT/planner/planner_system.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/planner/planner_system.md' '$PROJECT_ROOT/roles/planner/'"
    fi
    
    if [[ -f "$PROJECT_ROOT/planner/CLAUDE_PLANNER.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/planner/CLAUDE_PLANNER.md' '$PROJECT_ROOT/roles/planner/'"
    fi
    
    # Migrate developer files
    if [[ -f "$PROJECT_ROOT/developer/developer_system.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/developer/developer_system.md' '$PROJECT_ROOT/roles/developer/'"
    fi
    
    if [[ -f "$PROJECT_ROOT/developer/CLAUDE_DEVELOPER.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/developer/CLAUDE_DEVELOPER.md' '$PROJECT_ROOT/roles/developer/'"
    fi
    
    # Migrate reviewer files
    if [[ -f "$PROJECT_ROOT/reviewer/reviewer_system.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/reviewer/reviewer_system.md' '$PROJECT_ROOT/roles/reviewer/'"
    fi
    
    if [[ -f "$PROJECT_ROOT/reviewer/CLAUDE_REVIEWER.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/reviewer/CLAUDE_REVIEWER.md' '$PROJECT_ROOT/roles/reviewer/'"
    fi
    
    log "Role files migrated"
}

# Move template files to centralized templates
migrate_template_files() {
    log "Migrating template files..."
    
    # Migrate consultant templates
    if [[ -f "$PROJECT_ROOT/consultant/template_consulting.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/consultant/template_consulting.md' '$PROJECT_ROOT/templates/consultant/standard_consultation.md'"
    fi
    
    # Migrate planner templates
    if [[ -f "$PROJECT_ROOT/planner/template_planning.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/planner/template_planning.md' '$PROJECT_ROOT/templates/planner/new_feature.md'"
    fi
    
    # Migrate developer templates
    if [[ -f "$PROJECT_ROOT/developer/template_developing.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/developer/template_developing.md' '$PROJECT_ROOT/templates/developer/standard_development.md'"
    fi
    
    # Migrate reviewer templates
    if [[ -f "$PROJECT_ROOT/reviewer/template_reviewing.md" ]]; then
        execute_cmd "mv '$PROJECT_ROOT/reviewer/template_reviewing.md' '$PROJECT_ROOT/templates/reviewer/standard_review.md'"
    fi
    
    log "Template files migrated"
}

# Archive old directories
archive_old_directories() {
    log "Archiving old directory structure..."
    
    # Move remaining files to archive
    for role in consultant planner developer reviewer; do
        if [[ -d "$PROJECT_ROOT/$role" ]]; then
            # Check if directory has remaining files
            if [[ $(find "$PROJECT_ROOT/$role" -type f | wc -l) -gt 0 ]]; then
                execute_cmd "mv '$PROJECT_ROOT/$role' '$PROJECT_ROOT/archive/roles/${role}_old'"
                log "Archived remaining $role files"
            else
                execute_cmd "rmdir '$PROJECT_ROOT/$role'"
                log "Removed empty $role directory"
            fi
        fi
    done
    
    log "Old directories archived"
}

# Update symlinks for backward compatibility
create_compatibility_links() {
    log "Creating compatibility symlinks..."
    
    # Create symlinks for critical files that external scripts might reference
    execute_cmd "ln -sf 'roles/consultant/consultant_system.md' '$PROJECT_ROOT/consultant_system.md'"
    execute_cmd "ln -sf 'roles/planner/planner_system.md' '$PROJECT_ROOT/planner_system.md'"
    execute_cmd "ln -sf 'roles/developer/developer_system.md' '$PROJECT_ROOT/developer_system.md'"
    execute_cmd "ln -sf 'roles/reviewer/reviewer_system.md' '$PROJECT_ROOT/reviewer_system.md'"
    
    log "Compatibility symlinks created"
}

# Validate migration
validate_migration() {
    log "Validating migration..."
    
    # Check that key files exist in new locations
    local validation_failed=false
    
    # Check role files
    for role in consultant planner developer reviewer; do
        if [[ ! -f "$PROJECT_ROOT/roles/$role/${role}_system.md" ]]; then
            log "WARNING: Missing $PROJECT_ROOT/roles/$role/${role}_system.md"
            validation_failed=true
        fi
    done
    
    # Check template directories exist
    for role in consultant planner developer reviewer; do
        if [[ ! -d "$PROJECT_ROOT/templates/$role" ]]; then
            log "WARNING: Missing template directory for $role"
            validation_failed=true
        fi
    done
    
    if [[ "$validation_failed" == "true" ]]; then
        log "VALIDATION FAILED: Some issues detected"
        return 1
    else
        log "Validation passed"
        return 0
    fi
}

# Main migration function
main() {
    log "Starting directory structure migration..."
    log "Project root: $PROJECT_ROOT"
    log "Dry run: $DRY_RUN"
    
    # Verify we're in the right place
    if [[ ! -f "$PROJECT_ROOT/config/workflow_state.json" ]]; then
        log "ERROR: Not in correct project directory (missing workflow_state.json)"
        exit 1
    fi
    
    # Create backup
    create_backup
    
    # Perform migration steps
    create_new_structure
    migrate_role_files
    migrate_template_files
    archive_old_directories
    create_compatibility_links
    
    # Validate migration
    if validate_migration; then
        log "✅ Directory migration completed successfully"
        if [[ "$DRY_RUN" == "false" ]]; then
            log "Backup created at: $BACKUP_DIR"
        fi
        return 0
    else
        log "❌ Directory migration completed with warnings"
        return 1
    fi
}

# Run main function
main "$@"