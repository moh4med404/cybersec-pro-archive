# ===================================================
# Event Log Exporter
# Author: Moh4med404
# Date: 2025-08-20
# Purpose: Export Windows Event Logs to timestamped folder
# ===================================================

Write-Host "Event Log Exporter"

# Get timestamp for folder name
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$outDir = "EventLogs_$env:COMPUTERNAME`_$timestamp"

# Create output folder
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

# Define logs to export
$logs = @("Application","System","Security")

foreach ($log in $logs) {
    try {
        $outfile = Join-Path $outDir "$log`_$env:COMPUTERNAME`_$timestamp.evtx"
        Write-Host "Exporting $log log..."
        Wevtutil epl $log $outfile
        Write-Host "$log exported to $outfile"
    } catch {
        Write-Warning "Failed to export $log: $_"
    }
}

Write-Host "All logs exported to $outDir"
