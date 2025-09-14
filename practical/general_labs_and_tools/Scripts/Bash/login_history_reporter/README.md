# Login History Reporter (Blue Team)

Generates a report of all user logins in the last 7 days for auditing purposes.

**File:** `login_history_report.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-11

## Features

- Uses `last` command to extract login history.
- Outputs CSV with:
  - `Username`
  - `TTY`
  - `IP`
  - `LoginDate`
  - `LoginTime`
  - `LogoutTime`
  - `Duration`
- Stores CSV in a timestamped folder: `LoginHistoryAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash

## How to Use

1. Make the script executable:
```bash
chmod +x login_history_report.sh
```