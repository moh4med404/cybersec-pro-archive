#!/bin/bash
# ===================================================
# System Resource Monitor
# Author: Moh4med404
# Date: 2025-09-14
# Purpose: Log CPU, memory, and disk usage
# ===================================================

echo "Starting System Resource Monitor..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="SystemResourceAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/system_resources_$TIMESTAMP.csv"
echo "Timestamp,CPU_Usage,Memory_Usage,Disk_Usage" > "$CSV_FILE"

# Collect system resource usage
timestamp=$(date +"%Y-%m-%d %H:%M:%S")
cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')  # user + system CPU
mem=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')
disk=$(df -h / | awk 'NR==2 {print $5}')

echo "$timestamp,$cpu,$mem,$disk" >> "$CSV_FILE"

echo "System resource audit completed."
echo "CSV report generated: $CSV_FILE"
