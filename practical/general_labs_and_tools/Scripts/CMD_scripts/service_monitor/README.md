# Service Monitor

Monitors the status and start type of Windows services and writes a timestamped CSV and log.

**File:** `service_monitor.bat`  
**Author:** Moh4med404  
**Date:** 2025-09-03

## What it does

- Creates a timestamped folder `ServiceMonitor_<COMPUTERNAME>_<timestamp>`.
- Produces:
  - `service_status_<timestamp>.csv` — CSV with columns: `Name,DisplayName,Status,StartType,ServiceType`.
  - `service_status_<timestamp>.log` — human-readable log and summary.
- Uses PowerShell (preferred) to query `Get-Service` + `Win32_Service` for start type and service type.
- If PowerShell is unavailable/returns error, falls back to `sc` queries.

## Default services (used when you press Enter)
`WinDefend, wuauserv, EventLog, MpsSvc, Spooler, SamSS, TrustedInstaller`

You can override by providing a comma-separated list of service names when prompted.

## Requirements

- Windows (tested on Windows 10/11/Server)
- PowerShell recommended (modern Windows includes it)
- No admin required to query service status, but some service details may require elevated privileges.

## How to Use

1. Download `service_monitor.bat`.
2. Open Command Prompt and navigate to the script folder.
3. Run:
   ```cmd
   service_monitor.bat
   ```