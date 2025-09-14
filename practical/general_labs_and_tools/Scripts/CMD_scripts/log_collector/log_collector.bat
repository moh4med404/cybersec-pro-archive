@echo off
REM ===================================================
REM Log Collector Script
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-09-09
REM Purpose: Export Windows Event Logs for forensic/analysis
REM ===================================================

echo ==========================================
echo Windows Event Log Collector
echo ==========================================
echo NOTE: Exporting the Security log requires Administrator privileges.
echo If not running as admin, Security export will fail.
echo ==========================================

REM Get timestamp in safe filename format via PowerShell
for /f "usebackq delims=" %%T in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'"`) do set ts=%%T

REM Prepare output folder
set outdir=EventLogs_%COMPUTERNAME%_%ts%
if not exist "%outdir%" mkdir "%outdir%"

REM Export Application log
echo Exporting Application log...
wevtutil epl Application "%outdir%\Application_%COMPUTERNAME%_%ts%.evtx"
if %errorlevel% equ 0 (
  echo Application exported to %outdir%\Application_%COMPUTERNAME%_%ts%.evtx
) else (
  echo Warning: Failed to export Application log (error %errorlevel%).
)

REM Export System log
echo Exporting System log...
wevtutil epl System "%outdir%\System_%COMPUTERNAME%_%ts%.evtx"
if %errorlevel% equ 0 (
  echo System exported to %outdir%\System_%COMPUTERNAME%_%ts%.evtx
) else (
  echo Warning: Failed to export System log (error %errorlevel%).
)

REM Export Security log (requires Admin)
echo Exporting Security log (requires admin)...
wevtutil epl Security "%outdir%\Security_%COMPUTERNAME%_%ts%.evtx"
if %errorlevel% equ 0 (
  echo Security exported to %outdir%\Security_%COMPUTERNAME%_%ts%.evtx
) else (
  echo Warning: Failed to export Security log (likely requires Administrator privileges).
)

REM Optional: list exported files
echo ------------------------------------------
echo Exported files in %outdir%:
dir /b "%outdir%"
echo ------------------------------------------

echo Done. Collected logs are in: %outdir%
pause
