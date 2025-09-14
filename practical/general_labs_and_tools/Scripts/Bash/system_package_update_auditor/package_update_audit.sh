#!/bin/bash
# ===================================================
# System Package Update Auditor
# Author: Moh4med404
# Date: 2025-09-07
# Purpose: Audit recently installed/updated packages
# ===================================================

echo "Starting System Package Update Audit..."

# Create timestamped output directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTDIR="PackageAudit_$(hostname)_$TIMESTAMP"
mkdir -p "$OUTDIR"

CSV_FILE="$OUTDIR/package_updates_$TIMESTAMP.csv"
echo "Package,Version,InstallDate" > "$CSV_FILE"

# Determine package manager
if command -v dpkg >/dev/null 2>&1; then
    echo "Detected Debian/Ubuntu system..."
    dpkg-query -W -f='${Package},${Version},${Status}\n' | grep "install ok installed" >> "$CSV_FILE"
elif command -v rpm >/dev/null 2>&1; then
    echo "Detected RHEL/CentOS/Fedora system..."
    rpm -qa --qf "%{NAME},%{VERSION},%{INSTALLTIME:date}\n" >> "$CSV_FILE"
else
    echo "Unsupported package manager."
    exit 1
fi

echo "Package update audit completed."
echo "CSV report generated: $CSV_FILE"
