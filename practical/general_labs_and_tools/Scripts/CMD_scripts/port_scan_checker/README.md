# Port Scan Checker

Checks if specified TCP ports are open on the local system and logs results.

**File:** `port_scan_checker.bat`  
**Author:** Moh4med404  
**Date:** 2025-09-14

## What it does

- Creates a timestamped folder `PortScan_<COMPUTERNAME>_<timestamp>`.
- Produces:
  - `port_scan_<timestamp>.csv` — CSV with `Port,Status` (Open/Closed).
  - `port_scan_<timestamp>.log` — human-readable log with scan results.
- Default ports scanned (if user presses Enter): `21,22,23,25,53,80,443,3389,445,135`.
- Can accept custom comma-separated list of ports.

## Requirements

- Windows (10/11/Server)
- PowerShell recommended for TCP checks (`Test-NetConnection` cmdlet)

## How to Use

1. Download `port_scan_checker.bat`.
2. Open Command Prompt and navigate to the folder.
3. Run:
   ```cmd
   port_scan_checker.bat
   ```