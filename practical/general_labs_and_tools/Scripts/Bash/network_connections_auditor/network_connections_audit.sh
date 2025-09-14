#!/bin/bash
# ===================================================
# Network Connections Auditor
# Author: Moh4med404
# Date: 2025-09-13
# Purpose: List active network connections and highlight unusual ports
# ===================================================

echo "Starting Network Connections Audit..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="NetworkAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/network_connections_$TIMESTAMP.csv"
echo "Protocol,LocalAddress,LocalPort,RemoteAddress,RemotePort,State,PID/Program" > "$CSV_FILE"

# List active TCP/UDP connections
ss -tunap | tail -n +2 | while read -r line; do
    proto=$(echo "$line" | awk '{print $1}')
    local_addr=$(echo "$line" | awk '{print $5}' | awk -F: '{print $1}')
    local_port=$(echo "$line" | awk '{print $5}' | awk -F: '{print $2}')
    remote_addr=$(echo "$line" | awk '{print $6}' | awk -F: '{print $1}')
    remote_port=$(echo "$line" | awk '{print $6}' | awk -F: '{print $2}')
    state=$(echo "$line" | awk '{print $2}')
    pid_prog=$(echo "$line" | awk '{print $7}')
    echo "$proto,$local_addr,$local_port,$remote_addr,$remote_port,$state,$pid_prog" >> "$CSV_FILE"
done

echo "Network connections audit completed."
echo "CSV report generated: $CSV_FILE"
