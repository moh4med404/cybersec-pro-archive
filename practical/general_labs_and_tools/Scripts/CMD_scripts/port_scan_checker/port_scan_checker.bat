@echo off
REM ===================================================
REM Port Scan Checker Script
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-09-12
REM Purpose: Check local open ports and TCP connectivity
REM ===================================================

setlocal enabledelayedexpansion

echo ==========================================
echo Port Scan Checker
echo Checks if specified ports are open on local system
echo ==========================================

REM Timestamp for folder/file names via PowerShell
for /f "usebackq delims=" %%T in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'"`) do set ts=%%T

set outdir=PortScan_%COMPUTERNAME%_%ts%
mkdir "%outdir%" >nul 2>&1

set logfile=%outdir%\port_scan_%ts%.log
set csvfile=%outdir%\port_scan_%ts%.csv

echo Port,Status > "%csvfile%"
echo Port Scan started on %date% %time% > "%logfile%"
echo Output folder: %outdir% >> "%logfile%"
echo ---------------------------------------- >> "%logfile%"

REM Default ports
set defaultPorts=21,22,23,25,53,80,443,3389,445,135

echo Default ports: %defaultPorts%
set /p portInput=Enter comma-separated ports to scan (or press Enter for defaults): 

if "%portInput%"=="" (
  set portList=%defaultPorts%
) else (
  set portList=%portInput%
)

echo Scanning ports: %portList%
echo.

REM Loop through ports
for %%P in (%portList:,= %) do (
  REM Check using PowerShell Test-NetConnection if available
  powershell -NoProfile -Command ^
    "$port=%%P; $result=Test-NetConnection -ComputerName localhost -Port $port -WarningAction SilentlyContinue; " ^
    "if($result.TcpTestSucceeded){exit 0}else{exit 1}" >nul 2>&1

  if !errorlevel! equ 0 (
    echo %%P,Open >> "%csvfile%"
    echo Port %%P is OPEN >> "%logfile%"
  ) else (
    echo %%P,Closed >> "%csvfile%"
    echo Port %%P is CLOSED >> "%logfile%"
  )
)

echo ---------------------------------------- >> "%logfile%"
echo Port scan complete. CSV: %csvfile% >> "%logfile%"
echo Done. Outputs in: %outdir%
echo ==========================================
pause
endlocal
