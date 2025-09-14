#!/bin/bash
# ===================================================
# Sudo Command History Auditor
# Author: Moh4med404
# Date: 2025-09-05
# Purpose: Collect sudo command history for auditing
# ===================================================

echo "Starting Sudo Command History Audit..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="SudoAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

# CSV output file
CSV_FILE="$OUTDIR/sudo_history_$TIMESTAMP.csv"
echo "Username,Command,Date" > "$CSV_FILE"

# Loop through all user sudo logs
for user_dir in /home/*; do
    user=$(basename "$user_dir")
    sudo_log="/var/log/sudo-logs/$user" # optional log location; fallback to /var/log/auth.log
    if [[ -f "/var/log/auth.log" ]]; then
        grep "sudo:" /var/log/auth.log | grep "$user" | while read -r line; do
            # Extract command and date
            date_str=$(echo "$line" | awk '{print $1,$2,$3}')
            cmd=$(echo "$line" | awk -F"COMMAND=" '{print $2}')
            echo "$user,\"$cmd\",\"$date_str\"" >> "$CSV_FILE"
        done
    fi
done

echo "Sudo command audit completed."
echo "CSV report generated: $CSV_FILE"
