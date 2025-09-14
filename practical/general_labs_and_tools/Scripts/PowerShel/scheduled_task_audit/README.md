# Scheduled Task Audit 

Audits scheduled tasks on Windows hosts and highlights tasks running with administrative privileges.

**File:** `scheduled_task_audit.ps1`  
**Author:** Moh4med404  
**Date:** 2025-08-22

## Features

- Lists all scheduled tasks.
- Identifies tasks running with elevated privileges (`RunLevel = Admin`).
- Captures:
  - TaskName
  - TaskPath
  - RunLevel
  - UserId
  - Enabled status
  - Current state
- Outputs results to CSV.

## Requirements

- Windows 10/11/Server
- PowerShell 5.1+
- Administrative privileges recommended for full visibility

## How to Use

1. Open PowerShell (as Administrator for best results).
2. Navigate to the script folder.
3. Run:
```powershell
.\scheduled_task_audit.ps1
``` 