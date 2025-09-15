# ===================================================
# Service Hardening Audit
# Author: Moh4med404
# Date: 2025-08-22
# Purpose: Audit critical services for secure configuration
# ===================================================

Write-Host "Service Hardening Audit"

# Timestamp for output
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$outDir = "ServiceAudit_$env:COMPUTERNAME`_$timestamp"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$csvFile = Join-Path $outDir "ServiceHardeningReport_$timestamp.csv"

# List of critical services to audit
$criticalServices = @(
    "WinDefend", "wuauserv", "EventLog", "MpsSvc", "Spooler", "SamSS", "TrustedInstaller"
)

$results = @()
foreach ($svcName in $criticalServices) {
    try {
        $svc = Get-Service -Name $svcName -ErrorAction Stop
        $wmi = Get-WmiObject -Class Win32_Service -Filter "Name='$svcName'"
        $results += [PSCustomObject]@{
            ServiceName = $svc.Name
            DisplayName = $svc.DisplayName
            Status = $svc.Status
            StartMode = $wmi.StartMode
            ServiceType = $wmi.ServiceType
        }
    } catch {
        $results += [PSCustomObject]@{
            ServiceName = $svcName
            DisplayName = "(Not Found)"
            Status = "N/A"
            StartMode = "N/A"
            ServiceType = "N/A"
        }
    }
}

# Export CSV
$results | Export-Csv -Path $csvFile -NoTypeInformation
Write-Host "Service hardening report generated: $csvFile"
