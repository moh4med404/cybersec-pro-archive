# Event Log Exporter 

Exports Windows Event Logs (Application, System, Security) into a timestamped folder for analysis.

**File:** `event_log_exporter.ps1`  
**Author:** Moh4med404  
**Date:** 2025-08-20

## Features

- Exports `Application`, `System`, and `Security` logs.
- Saves logs in a folder named `EventLogs_<COMPUTERNAME>_<timestamp>`.
- Supports automated collection for audits or forensic purposes.

## Requirements

- Windows (tested on 10/11/Server)
- PowerShell
- Administrative privileges required to export Security log.

## How to Use

1. Open PowerShell as Administrator (recommended for Security log).
2. Navigate to the script folder.
3. Run the script:
```powershell
.\event_log_exporter.ps1
```