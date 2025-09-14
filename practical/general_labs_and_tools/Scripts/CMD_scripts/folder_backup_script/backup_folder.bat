@echo off
REM ===================================================
REM Folder Backup Script
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-09-14
REM ===================================================

echo ==========================================
echo Welcome to Folder Backup Script!
echo ==========================================

REM Prompt user for source folder
set /p source=Enter the full path of the folder to backup: 

REM Check if source exists
if not exist "%source%" (
    echo Source folder does not exist!
    pause
    exit /b
)

REM Prompt user for destination folder
set /p destination=Enter the backup destination path: 

REM Create destination folder if it doesn't exist
if not exist "%destination%" (
    mkdir "%destination%"
)

REM Backup folder using xcopy
xcopy "%source%" "%destination%\%~nxs" /E /I /Y
echo ==========================================
echo Backup completed successfully!
echo Source: %source%
echo Destination: %destination%\%~nxs
echo ==========================================
pause
