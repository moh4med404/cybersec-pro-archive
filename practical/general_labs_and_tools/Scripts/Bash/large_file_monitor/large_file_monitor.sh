#!/bin/bash
# ===================================================
# Large File Monitor
# Author: Moh4med404
# Date: 2025-09-13
# Purpose: Scan critical directories for large files
# ===================================================

echo "Starting Large File Audit..."

# Configurable size (default: 100MB)
SIZE="+100M"

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="LargeFileAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/large_files_$TIMESTAMP.csv"
echo "Path,Size,Owner,Group,Permissions" > "$CSV_FILE"

# Directories to scan
DIRS=("/etc" "/var" "/usr" "/home")

for dir in "${DIRS[@]}"; do
    find "$dir" -type f -size "$SIZE" 2>/dev/null | while read -r file; do
        size=$(du -h "$file" | cut -f1)
        owner=$(stat -c %U "$file")
        group=$(stat -c %G "$file")
        perms=$(stat -c %A "$file")
        echo "$file,$size,$owner,$group,$perms" >> "$CSV_FILE"
    done
done

echo "Large file audit completed."
echo "CSV report generated: $CSV_FILE"
