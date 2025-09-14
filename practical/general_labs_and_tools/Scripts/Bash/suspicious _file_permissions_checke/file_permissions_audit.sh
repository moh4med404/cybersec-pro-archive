#!/bin/bash
# ===================================================
# Suspicious File Permissions Checker
# Author: Moh4med404
# Date: 2025-09-09
# Purpose: Scan for world-writable files in critical directories
# ===================================================

echo "Starting Suspicious File Permissions Audit..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="FilePermAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/world_writable_files_$TIMESTAMP.csv"
echo "Path,Permissions,Owner,Group" > "$CSV_FILE"

# Directories to scan
DIRS=("/etc" "/var" "/usr" "/home")

for dir in "${DIRS[@]}"; do
    find "$dir" -type f -perm -0002 2>/dev/null | while read -r file; do
        perms=$(stat -c %A "$file")
        owner=$(stat -c %U "$file")
        group=$(stat -c %G "$file")
        echo "$file,$perms,$owner,$group" >> "$CSV_FILE"
    done
done

echo "File permissions audit completed."
echo "CSV report generated: $CSV_FILE"
