# Large File Monitor 

Scans critical directories for files larger than a configurable size (default: 100MB) and outputs a CSV report.

**File:** `large_file_monitor.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-13

## Features

- Scans `/etc`, `/var`, `/usr`, `/home` for files larger than default 100MB.
- Outputs CSV with:
  - `Path`
  - `Size`
  - `Owner`
  - `Group`
  - `Permissions`
- Stores results in timestamped folder: `LargeFileAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash
- Root privileges recommended for full scan

## How to Use

1. Make the script executable:
```bash
chmod +x large_file_monitor.sh
``` 