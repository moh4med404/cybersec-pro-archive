@echo off
REM ===================================================
REM User Account Audit Script
REM ===================================================
REM Author: Moh4med404
REM Date: 2025-08-29
REM Purpose: Gather local user, group and last logon info
REM ===================================================

echo ==========================================
echo User Account Audit
echo Collects users, groups and last logon times
echo ==========================================

REM Get safe timestamp using PowerShell
for /f "usebackq delims=" %%T in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'"`) do set ts=%%T

set outdir=UserAudit_%COMPUTERNAME%_%ts%
mkdir "%outdir%" >nul 2>&1

echo Gathering list of local users...
net user > "%outdir%\users_list_raw.txt"
REM Save a cleaner list of usernames (net user output splits into columns)
for /f "skip=4 tokens=*" %%L in ('type "%outdir%\users_list_raw.txt" ^| findstr /R /C:".*"') do (
  echo %%L>> "%outdir%\users_lines.tmp"
)
REM Remove header/footer lines by trimming first and last lines
REM Simpler approach: use PowerShell to get usernames (fallback for robust parsing)
powershell -NoProfile -Command "Get-LocalUser | Select-Object -ExpandProperty Name" > "%outdir%\users.txt" 2>nul
if %errorlevel% neq 0 (
  REM If Get-LocalUser not available, fall back to parsing net user output
  for /f "skip=6 tokens=*" %%u in ('net user') do (
    if "%%u"=="" goto :afterNetUserParse
    for %%a in (%%u) do echo %%a>> "%outdir%\users.txt"
  )
)
:afterNetUserParse

echo Gathering detailed user info (net user)...
echo Username,AccountActive,Comment,LastLogon > "%outdir%\users_details.csv"
for /f "usebackq delims=" %%U in ("%outdir%\users.txt") do (
  set "uname=%%U"
  call :get_user_info "%%U"
)

echo Gathering local groups...
net localgroup > "%outdir%\groups_list_raw.txt"
powershell -NoProfile -Command "Get-LocalGroup | Select-Object -ExpandProperty Name" > "%outdir%\groups.txt" 2>nul
if %errorlevel% neq 0 (
  REM fallback parse
  for /f "skip=4 tokens=*" %%G in ('type "%outdir%\groups_list_raw.txt" ^| findstr /R /C:".*"') do (
    for %%g in (%%G) do echo %%g>> "%outdir%\groups.txt"
  )
)

echo Gathering group membership (net localgroup "GroupName")...
> "%outdir%\group_membership.txt" (
  for /f "usebackq delims=" %%G in ("%outdir%\groups.txt") do (
    echo ----------------------------------------
    echo Group: %%G
    echo ----------------------------------------
    net localgroup "%%G"
    echo.
  )
)

echo Cleanup temp files...
if exist "%outdir%\users_lines.tmp" del "%outdir%\users_lines.tmp" >nul 2>&1
if exist "%outdir%\users_list_raw.txt" del "%outdir%\users_list_raw.txt" >nul 2>&1
if exist "%outdir%\groups_list_raw.txt" del "%outdir%\groups_list_raw.txt" >nul 2>&1

echo ==========================================
echo Audit complete. Outputs in folder: %outdir%
dir /b "%outdir%"
echo ==========================================
pause
exit /b

:get_user_info
REM %1 = username
setlocal
set "u=%~1"
REM Query net user for details
for /f "delims=" %%X in ('net user "%u%" ^| findstr /C:"Account active" /C:"Comment" /C:"Last logon"') do (
  echo %%X>> "%outdir%\tmp_user_info_%u%.txt"
)
REM Prepare CSV line: Username,AccountActive,Comment,LastLogon
set "acctActive="
set "comment="
set "lastLogon="
for /f "usebackq tokens=1,* delims=:" %%A in ("%outdir%\tmp_user_info_%u%.txt") do (
  set "fld=%%A"
  set "val=%%B"
  call :trim "%%A" fld
  call :trim "%%B" val
  if /I "%%A"=="Account active" set "acctActive=%%B"
  if /I "%%A"=="Comment" set "comment=%%B"
  if /I "%%A"=="Last logon" set "lastLogon=%%B"
)
if defined acctActive (
  echo %u%,%acctActive%,%comment%,%lastLogon%>> "%outdir%\users_details.csv"
) else (
  REM If no net user info, write username only
  echo %u%,N/A,N/A,N/A>> "%outdir%\users_details.csv"
)
if exist "%outdir%\tmp_user_info_%u%.txt" del "%outdir%\tmp_user_info_%u%.txt" >nul 2>&1
endlocal
exit /b

:trim
REM trim helper: %1 text, returns in variable name given by %2
setlocal enabledelayedexpansion
set "s=%~1"
if defined s (
  for /f "tokens=* delims= " %%T in ("!s!") do set "s=%%T"
  :loopTrim
  if not "!s:~-1!"==" " goto :doneTrim
  set "s=!s:~0,-1!"
  goto loopTrim
)
:doneTrim
endlocal & set "%2=%s%"
exit /b
