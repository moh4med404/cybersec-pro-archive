# Hidden Files Finder 

Scans all user home directories for hidden files (`.*`) and outputs a report for auditing purposes.

**File:** `hidden_files_audit.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-13

## Features

- Scans `/home/*` directories for hidden files.
- Outputs CSV with:
  - `User`
  - `Path`
  - `Permissions`
  - `Owner`
  - `Group`
- Stores results in a timestamped folder: `HiddenFilesAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash
- Root privileges recommended for full scan

## How to Use

1. Make the script executable:
```bash
chmod +x hidden_files_audit.sh
```