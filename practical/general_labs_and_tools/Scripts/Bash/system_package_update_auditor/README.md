# System Package Update Auditor 

Generates a report of installed or updated packages for auditing and security tracking.

**File:** `package_update_audit.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-07

## Features

- Detects package manager: `dpkg` (Debian/Ubuntu) or `rpm` (RHEL/CentOS/Fedora).
- Outputs CSV with:
  - `Package`
  - `Version`
  - `InstallDate`
- Stores results in timestamped folder: `PackageAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash
- Root privileges recommended for full package info

## How to Use

1. Make the script executable:
```bash
chmod +x package_update_audit.sh
