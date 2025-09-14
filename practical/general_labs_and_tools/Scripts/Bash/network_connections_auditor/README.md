# Network Connections Auditor 

Audits active network connections on the system, highlighting unusual ports for monitoring and security auditing.

**File:** `network_connections_audit.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-13

## Features

- Lists all active TCP and UDP connections.
- Captures:
  - `Protocol`
  - `LocalAddress`
  - `LocalPort`
  - `RemoteAddress`
  - `RemotePort`
  - `State`
  - `PID/Program`
- Outputs CSV in a timestamped folder: `NetworkAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash
- `ss` command available (`iproute2` package)
- Root privileges recommended for full process info

## How to Use

1. Make the script executable:
```bash
chmod +x network_connections_audit.sh
```