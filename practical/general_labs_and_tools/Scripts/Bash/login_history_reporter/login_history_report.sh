#!/bin/bash
# ===================================================
# Login History Reporter
# Author: Moh4med404
# Date: 2025-09-11
# Purpose: Report all user logins in the last 7 days
# ===================================================

echo "Starting Login History Report..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="LoginHistoryAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/login_history_$TIMESTAMP.csv"
echo "Username,TTY,IP,LoginDate,LoginTime,LogoutTime,Duration" > "$CSV_FILE"

# Extract login history for last 7 days
last -F | grep "$(date --date='7 days ago' '+%b %e')" -A 1000 | while read -r line; do
    # Skip empty lines and headers
    [[ -z "$line" || "$line" =~ "wtmp" ]] && continue
    username=$(echo "$line" | awk '{print $1}')
    tty=$(echo "$line" | awk '{print $2}')
    ip=$(echo "$line" | awk '{print $3}')
    login_date=$(echo "$line" | awk '{print $4}')
    login_time=$(echo "$line" | awk '{print $5}')
    logout_time=$(echo "$line" | awk '{print $6}')
    duration=$(echo "$line" | awk '{print $7}')
    echo "$username,$tty,$ip,$login_date,$login_time,$logout_time,$duration" >> "$CSV_FILE"
done

echo "Login history audit completed."
echo "CSV report generated: $CSV_FILE"
