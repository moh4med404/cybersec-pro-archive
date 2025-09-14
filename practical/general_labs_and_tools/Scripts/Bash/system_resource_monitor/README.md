# System Resource Monitor 

Logs CPU, memory, and disk usage for system auditing and monitoring.

**File:** `system_resource_monitor.sh`  
**Author:** Moh4med404  
**Date:** 2025-09-14

## Features

- Collects:
  - `CPU_Usage` (%)
  - `Memory_Usage` (%)
  - `Disk_Usage` (% of root `/`)
- Outputs CSV in a timestamped folder: `SystemResourceAudit_<hostname>_<timestamp>`.

## Requirements

- Linux system
- Bash
- Root privileges not required, but recommended for complete system stats

## How to Use

1. Make the script executable:
```bash
chmod +x system_resource_monitor.sh
