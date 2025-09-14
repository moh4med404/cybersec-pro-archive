@echo off
REM ===================================================
REM File Cleaner Script
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-09-14
REM ===================================================

echo ==========================================
echo Welcome to File Cleaner Script!
echo This will remove .tmp and .log files.
echo ==========================================

REM Ask for folder path
set /p folder=Enter the folder path to clean: 

REM Check if folder exists
if not exist "%folder%" (
    echo Folder "%folder%" does not exist!
    pause
    exit /b
)

REM Delete unwanted files
del /Q "%folder%\*.tmp"
del /Q "%folder%\*.log"

echo ==========================================
echo Cleaning completed!
echo Removed .tmp and .log files from: %folder%
echo ==========================================
pause
