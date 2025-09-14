#!/bin/bash
# ===================================================
# Active SSH Session Auditor
# Author: Moh4med404
# Date: 2025-09-08
# Purpose: List all active SSH sessions
# ===================================================

echo "Starting Active SSH Session Audit..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="SSHSessionAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/ssh_sessions_$TIMESTAMP.csv"
echo "Username,IP,LoginTime,TTY" > "$CSV_FILE"

# List active SSH sessions
who | grep "pts/" | while read -r line; do
    user=$(echo "$line" | awk '{print $1}')
    tty=$(echo "$line" | awk '{print $2}')
    ip=$(echo "$line" | awk '{print $5}' | tr -d '()')
    login_time=$(echo "$line" | awk '{print $3, $4}')
    echo "$user,$ip,$login_time,$tty" >> "$CSV_FILE"
done

echo "SSH session audit completed."
echo "CSV report generated: $CSV_FILE"
