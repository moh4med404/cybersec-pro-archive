#!/bin/bash
# ===================================================
# Failed Login Attempt Reporter
# Author: Moh4med404
# Date: 2025-09-06
# Purpose: Report failed login attempts for auditing
# ===================================================

echo "Starting Failed Login Attempt Report..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="FailedLoginAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

# CSV output file
CSV_FILE="$OUTDIR/failed_login_$TIMESTAMP.csv"
echo "Date,Time,User,IP" > "$CSV_FILE"

# Determine log file
if [[ -f "/var/log/auth.log" ]]; then
    LOGFILE="/var/log/auth.log"
elif [[ -f "/var/log/secure" ]]; then
    LOGFILE="/var/log/secure"
else
    echo "No suitable auth log file found!"
    exit 1
fi

# Parse failed login attempts
grep "Failed password" "$LOGFILE" | while read -r line; do
    date_str=$(echo "$line" | awk '{print $1,$2,$3}')
    user=$(echo "$line" | awk -F"user " '{print $2}' | awk '{print $1}')
    ip=$(echo "$line" | awk -F"from " '{print $2}' | awk '{print $1}')
    echo "\"$date_str\",\"$user\",\"$ip\"" >> "$CSV_FILE"
done

echo "Failed login report completed."
echo "CSV report generated: $CSV_FILE"
