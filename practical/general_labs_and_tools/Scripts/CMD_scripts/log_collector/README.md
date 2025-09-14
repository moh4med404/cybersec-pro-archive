# Log Collector 

Collect Windows Event Logs (Application, System, Security) into a timestamped folder for analysis or forensic review.

**File:** `log_collector.bat`  
**Author:** Moh4med404  
**Date:** 2025-09-14

## What it does

- Creates a timestamped folder named `EventLogs_<COMPUTERNAME>_<YYYY-MM-DD_HH-MM-SS>`.
- Exports:
  - `Application` log → `Application_<COMPUTERNAME>_<timestamp>.evtx`
  - `System` log → `System_<COMPUTERNAME>_<timestamp>.evtx`
  - `Security` log → `Security_<COMPUTERNAME>_<timestamp>.evtx` (requires Administrator)
- Prints exported file list.

## Requirements

- Windows (tested on Windows 10/11 / Windows Server)
- `wevtutil` (built into modern Windows)
- PowerShell (built into modern Windows)
- To collect the **Security** event log you **must** run the script as Administrator.

## How to Use

1. Place `log_collector.bat` on the target system (or a removable drive).
2. Right-click the file and choose **Run as administrator** (recommended to collect Security log).
   - If you can't run as admin, you will still get Application and System logs if permitted.
3. Follow the console prompts (there are none — it auto-creates the folder and exports).
4. Find the exported `.evtx` files in the created folder `EventLogs_<COMPUTERNAME>_<timestamp>`.

## How to Test (safe test)

1. On your test machine, create a few test events:
   - To create an application event:
     ```powershell
     Write-EventLog -LogName Application -Source "Application" -EntryType Information -EventId 1001 -Message "Test Application Event"
     ```
     (If `Write-EventLog` source not available, use an existing source or `New-EventLog` to create one.)
   - To create a system-like event, use a simple local script or wait for system events — for testing Application/System export the test event above is enough.
2. Run `log_collector.bat` as Administrator.
3. Verify the `.evtx` files exist in the folder.
4. Open the `.evtx` files on a Windows machine:
   - Double-clicking `.evtx` opens Event Viewer, or from Event Viewer use **Open Saved Log...** to inspect.
5. Confirm the test event(s) appear inside `Application_*.evtx` (or other logs as relevant).

## Notes & Best Practices

- Running as Administrator is recommended for completeness.
- Copy the exported `.evtx` files off the host to a secure analyst workstation for analysis (do not analyze on the original host unless necessary).
- For automated collection across many hosts, consider running this via scheduled task or remote command (PSRemoting / management system) and centralizing outputs.
- For long-term logging/collection use SIEM/forwarding instead of only ad-hoc .evtx exports.


