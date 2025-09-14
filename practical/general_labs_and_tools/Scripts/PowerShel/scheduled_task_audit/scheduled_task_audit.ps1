# ===================================================
# Scheduled Task Audit
# Author: Moh4med404
# Date: 2025-08-22
# Purpose: Audit scheduled tasks, highlighting tasks running as Admin
# ===================================================

Write-Host "Scheduled Task Audit"

# Timestamp for output
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$outDir = "TaskAudit_$env:COMPUTERNAME`_$timestamp"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$csvFile = Join-Path $outDir "ScheduledTaskReport_$timestamp.csv"

# Get all scheduled tasks
$tasks = Get-ScheduledTask | ForEach-Object {
    $taskName = $_.TaskName
    $taskPath = $_.TaskPath
    $principal = $_.Principal
    $runLevel = if ($principal.RunLevel -eq "Highest") { "Admin" } else { "Standard" }
    [PSCustomObject]@{
        TaskName = $taskName
        TaskPath = $taskPath
        RunLevel = $runLevel
        UserId = $principal.UserId
        Enabled = $_.Enabled
        State = (Get-ScheduledTaskInfo -TaskName $taskName -TaskPath $taskPath).State
    }
}

# Export CSV
$tasks | Export-Csv -Path $csvFile -NoTypeInformation
Write-Host "Scheduled task audit report generated: $csvFile"
