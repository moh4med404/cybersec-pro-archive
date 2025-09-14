# Active SSH Session Auditor 

Audits all active SSH sessions on a Linux system, capturing user, IP, login time, and TTY.

**File:** `ssh_session_audit.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-08

## Features

- Lists active SSH sessions (`who | grep pts/`).
- Outputs CSV with:
  - `Username`
  - `IP`
  - `LoginTime`
  - `TTY`
- Stores CSV in a timestamped folder: `SSHSessionAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash

## How to Use

1. Make the script executable:
```bash
chmod +x ssh_session_audit.sh
```