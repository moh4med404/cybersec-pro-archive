#!/bin/bash
# ===================================================
# Hidden Files Finder
# Author: Moh4med404
# Date: 2025-09-13
# Purpose: Scan user home directories for hidden files
# ===================================================

echo "Starting Hidden Files Audit..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="HiddenFilesAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/hidden_files_$TIMESTAMP.csv"
echo "User,Path,Permissions,Owner,Group" > "$CSV_FILE"

# Scan all user home directories
for user_dir in /home/*; do
    user=$(basename "$user_dir")
    find "$user_dir" -type f -name ".*" 2>/dev/null | while read -r file; do
        perms=$(stat -c %A "$file")
        owner=$(stat -c %U "$file")
        group=$(stat -c %G "$file")
        echo "$user,$file,$perms,$owner,$group" >> "$CSV_FILE"
    done
done

echo "Hidden files audit completed."
echo "CSV report generated: $CSV_FILE"
