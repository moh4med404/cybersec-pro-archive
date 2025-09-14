@echo off
REM ===================================================
REM Service Monitor Script
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-08-10
REM Purpose: Check critical Windows services and log their status
REM ===================================================

setlocal enabledelayedexpansion

echo ==========================================
echo Service Monitor
echo Checks status and start mode of selected services
echo ==========================================

REM Timestamp for folder/file names via PowerShell
for /f "usebackq delims=" %%T in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'"`) do set ts=%%T

set outdir=ServiceMonitor_%COMPUTERNAME%_%ts%
mkdir "%outdir%" >nul 2>&1

set csvfile=%outdir%\service_status_%ts%.csv
set logfile=%outdir%\service_status_%ts%.log

echo "Name","DisplayName","Status","StartType","ServiceType" > "%csvfile%"
echo Service Monitor started on %date% %time% > "%logfile%"
echo Output folder: %outdir% >> "%logfile%"
echo ---------------------------------------- >> "%logfile%"

REM Default critical services (can be overridden)
set defaultServices=WinDefend,wuauserv,EventLog,MpsSvc,Spooler,SamSS,TrustedInstaller

echo Default services: %defaultServices%
echo.
set /p svcinput=Enter comma-separated services to check (or press Enter to use defaults): 

if "%svcinput%"=="" (
  set svclist=%defaultServices%
) else (
  set svclist=%svcinput%
)

REM Use PowerShell to get detailed service info (preferred)
powershell -NoProfile -Command ^
  "$svcs='%svclist%'.Split(','); " ^
  " $out=@(); " ^
  " foreach($s in $svcs){ $svc=Get-Service -Name $s -ErrorAction SilentlyContinue; if($svc){ $props=[PSCustomObject]@{Name=$svc.Name; DisplayName=$svc.DisplayName; Status=$svc.Status; StartType=(Get-WmiObject -Class Win32_Service -Filter \"Name='$($svc.Name)'\").StartMode; ServiceType=(Get-WmiObject -Class Win32_Service -Filter \"Name='$($svc.Name)'\").ServiceType } else { $props=[PSCustomObject]@{Name=$s; DisplayName='(not found)'; Status='NotFound'; StartType='N/A'; ServiceType='N/A'} } $out += $props } " ^
  " $out | ConvertTo-Csv -NoTypeInformation -Force" > "%outdir%\ps_output.csv" 2> "%outdir%\ps_errors.txt"

if %errorlevel% equ 0 (
  REM Read CSV produced by PowerShell and append to final CSV/log
  for /f "usebackq skip=1 delims=" %%L in ("%outdir%\ps_output.csv") do (
    >> "%csvfile%" echo %%~L
    >> "%logfile%" echo %%~L
  )
  echo PowerShell method used. >> "%logfile%"
) else (
  REM PowerShell may be unavailable or failed — fallback to sc
  echo PowerShell failed or returned an error (see %outdir%\ps_errors.txt). Using sc fallback. >> "%logfile%"
  for %%S in (%svclist:,= %) do (
    REM Query service via sc
    for /f "tokens=2 delims=:" %%A in ('sc qc "%%S" 2^>nul ^| findstr /C:"START_TYPE" /C:"SERVICE_NAME"') do set "tmp=%%A"
    for /f "tokens=2 delims=:" %%B in ('sc query "%%S" 2^>nul ^| findstr /C:"STATE"') do set "state=%%B"
    REM cleanup variables
    set "state=!state:~1!"
    set "tmp=!tmp:~1!"
    if "!tmp!"=="" set "tmp=%%S"
    if "!state!"=="" set "state=Unknown"
    echo "!tmp!","!tmp!","!state!","Unknown","Unknown" >> "%csvfile%"
    echo Service: !tmp! Status: !state! >> "%logfile%"
  )
)

echo ---------------------------------------- >> "%logfile%"
echo Summary (CSV): %csvfile% >> "%logfile%"
echo Done. Outputs in: %outdir% >> "%logfile%"

echo ==========================================
echo Service check complete.
echo Outputs:
echo  - CSV: %csvfile%
echo  - Log: %logfile%
echo ==========================================
pause
endlocal
