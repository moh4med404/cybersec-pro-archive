# Sudo Command History Auditor 

Collects all `sudo` commands executed by users for auditing purposes.

**File:** `sudo_history_audit.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-05

## Features

- Extracts all `sudo` commands from `/var/log/auth.log`.
- Saves the output in a CSV file with:
  - `Username`
  - `Command`
  - `Date`
- Stores results in a timestamped folder: `SudoAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Access to `/var/log/auth.log` (requires root privileges)
- Bash

## How to Use

1. Make the script executable:
```bash
chmod +x sudo_history_audit.sh
``` 