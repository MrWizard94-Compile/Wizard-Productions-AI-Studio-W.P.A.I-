param([string]$ReportPath = "C:\WPAI\leftover-residue-inventory.md")
$ErrorActionPreference = "Stop"
if (-not (Test-Path $ReportPath)) { throw "Missing $ReportPath" }
$c = Get-Content $ReportPath -Raw
foreach ($s in @("leftover","DuckDuckGo","RunningInstances","Infrastructure","E:\special","Methodology","Unreachable","Prefetch","Access denied","ACCESS_DENIED")) {
  if ($c -notlike "*$s*") { throw "Missing: $s" }
}
# Must NOT claim Prefetch None as a zero-hit without successful listing
if ($c -match '(?i)Prefetch[^\n]*\|\s*\*\*None\*\*') { throw "Report still claims Prefetch None in zero-hit table" }
$tlog = "C:\Users\Bulkl\AppData\Local\Temp\grok-goal-5fd7ca38293c\implementer\search-temp-prefetch.log"
if (-not (Test-Path $tlog)) { throw "Missing temp-prefetch log" }
$t = Get-Content $tlog -Raw
if ($t -notmatch 'PREFETCH_LIST_STATUS\|ACCESS_DENIED') { throw "Prefetch log missing ACCESS_DENIED status" }
if (-not (Test-Path "C:\Users\Bulkl\Downloads\DuckDuckGo.Installer.exe")) { throw "DDG installer missing" }
if (-not (Test-Path "C:\Users\Bulkl\AppData\Local\Temp\DuckDuckGo\RunningInstances")) { throw "DDG RunningInstances missing" }
Write-Output "PASS: leftover report + Prefetch unreachable honesty OK"
