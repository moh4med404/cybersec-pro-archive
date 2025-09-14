# Failed Login Attempt Reporter (Blue Team)

Parses Linux authentication logs to report failed login attempts, including user and IP.

**File:** `failed_login_report.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-06

## Features

- Extracts all failed SSH/password login attempts.
- Saves output to CSV:
  - `Date`
  - `Time`
  - `User`
  - `IP`
- Stores results in a timestamped folder: `FailedLoginAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Access to `/var/log/auth.log` or `/var/log/secure`
- Bash

## How to Use

1. Make script executable:
```bash
chmod +x failed_login_report.sh
```
