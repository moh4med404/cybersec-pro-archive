# User Account Audit 

Collects local user and group information and attempts to extract last logon times for each user.

**File:** `user_account_audit.bat`  
**Author:** Moh4med404  
**Date:** 2025-08-25

## What it does

- Creates a timestamped folder `UserAudit_<COMPUTERNAME>_<YYYY-MM-DD_HH-MM-SS>`.
- Produces:
  - `users.txt` — one username per line (best-effort using PowerShell `Get-LocalUser` or `net user` fallback).
  - `users_details.csv` — CSV with `Username,AccountActive,Comment,LastLogon`.
  - `groups.txt` — local group names.
  - `group_membership.txt` — human-readable listing of group members via `net localgroup`.
- Attempts to extract `Last logon` info from `net user <username>` output. This works for local accounts and many Windows versions; domain accounts and some OS configurations may not show last logon here.

## Requirements

- Windows (tested on Win10/Win11/Windows Server).
- `net` (built-in) and, preferably, PowerShell for more reliable username enumeration.
- Running as Administrator is recommended but not strictly required for many read-only queries.

## How to Use

1. Place `user_account_audit.bat` on the target host.
2. Right-click → **Run as administrator** (recommended).
3. The script runs without further prompts and creates the output folder.
4. Copy output files to a secure analyst machine for review.

## How to Test (safe test)

1. Create a local test user:
   ```powershell
   net user TestUser P@ssw0rd! /add
