# ===================================================
# Local Group Policy Checker
# Author: Moh4med404
# Date: 2025-08-21
# Purpose: Audit key local security policies
# ===================================================

Write-Host "Local Group Policy Checker"

# Timestamp for output
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$outDir = "GPOAudit_$env:COMPUTERNAME`_$timestamp"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

# Output CSV file
$csvFile = Join-Path $outDir "GPOReport_$timestamp.csv"

# Policies to check
$policies = @(
    @{Name="MinimumPasswordLength"; Cmd="secedit /export /cfg $env:TEMP\secpol.cfg; Select-String 'MinimumPasswordLength' $env:TEMP\secpol.cfg"},
    @{Name="PasswordComplexity"; Cmd="secedit /export /cfg $env:TEMP\secpol.cfg; Select-String 'PasswordComplexity' $env:TEMP\secpol.cfg"},
    @{Name="LockoutThreshold"; Cmd="secedit /export /cfg $env:TEMP\secpol.cfg; Select-String 'LockoutBadCount' $env:TEMP\secpol.cfg"},
    @{Name="LockoutDuration"; Cmd="secedit /export /cfg $env:TEMP\secpol.cfg; Select-String 'LockoutDuration' $env:TEMP\secpol.cfg"},
    @{Name="AuditLogonEvents"; Cmd="auditpol /get /category:* | Select-String 'Logon/Logoff'"}
)

# Collect policies
$results = @()
foreach ($policy in $policies) {
    try {
        $value = Invoke-Expression $policy.Cmd | ForEach-Object { $_.ToString().Trim() }
        $results += [PSCustomObject]@{Policy=$policy.Name; Value=$value}
    } catch {
        $results += [PSCustomObject]@{Policy=$policy.Name; Value="Error retrieving"}
    }
}

# Export CSV
$results | Export-Csv -Path $csvFile -NoTypeInformation
Write-Host "Local GPO report generated: $csvFile"
