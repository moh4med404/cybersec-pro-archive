@echo off
REM ===================================================
REM System Info Reporter
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-09-14
REM ===================================================

echo ==========================================
echo Welcome to System Info Reporter!
echo This will generate a report of your system.
echo ==========================================

REM Set output file
set report=SystemReport.txt

REM Write header
echo SYSTEM INFORMATION REPORT > %report%
echo Generated on %date% at %time% >> %report%
echo ------------------------------------------ >> %report%

REM Get system information
systeminfo >> %report%

echo ==========================================
echo Report generated successfully: %report%
echo You can open it to view system information.
echo ==========================================
pause
