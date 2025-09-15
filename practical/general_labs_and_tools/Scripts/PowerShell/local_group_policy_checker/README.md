# Local Group Policy Checker 

Audits key local security policies on Windows hosts.

**File:** `local_gpo_checker.ps1`  
**Author:** Moh4med404  
**Date:** 2025-08-21

## Features

- Checks:
  - Minimum password length
  - Password complexity
  - Account lockout threshold and duration
  - Audit logon events
- Outputs results to CSV for review.

## Requirements

- Windows (10/11/Server)
- PowerShell
- Administrative privileges recommended

## How to Use

1. Open PowerShell (preferably as Administrator).
2. Navigate to the script folder.
3. Run:
```powershell
.\local_gpo_checker.ps1
```