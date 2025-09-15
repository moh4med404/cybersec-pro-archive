# Service Hardening Audit 

Audits critical Windows services for running status and secure startup configuration.

**File:** `service_hardening_audit.ps1`  
**Author:** Moh4med404  
**Date:** 2025-08-22

## Features

- Checks critical services:
  - Windows Defender (`WinDefend`)
  - Windows Update (`wuauserv`)
  - Event Log (`EventLog`)
  - Firewall (`MpsSvc`)
  - Print Spooler (`Spooler`)
  - Security Accounts Manager (`SamSS`)
  - TrustedInstaller (`TrustedInstaller`)
- Outputs:
  - `ServiceName`, `DisplayName`, `Status`, `StartMode`, `ServiceType`
- Generates timestamped CSV for auditing.

## Requirements

- Windows 10/11/Server
- PowerShell
- Administrative privileges recommended for full audit

## How to Use

1. Open PowerShell.
2. Run the script:
```powershell
.\service_hardening_audit.ps1
```