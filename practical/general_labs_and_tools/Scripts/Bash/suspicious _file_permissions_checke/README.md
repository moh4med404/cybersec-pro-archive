# Suspicious File Permissions Checker 

Scans critical directories for world-writable files that may indicate misconfigurations or security risks.

**File:** `file_permissions_audit.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-09

## Features

- Scans `/etc`, `/var`, `/usr`, `/home` for world-writable files.
- Outputs CSV with:
  - `Path`
  - `Permissions`
  - `Owner`
  - `Group`
- Stores results in folder: `FilePermAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash
- Root privileges recommended for full scan

## How to Use

1. Make script executable:
```bash
chmod +x file_permissions_audit.sh
```