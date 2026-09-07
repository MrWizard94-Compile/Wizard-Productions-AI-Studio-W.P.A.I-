# Validates private-browser-vpn-inventory.md structure (research deliverable gate)
param([string]$ReportPath = "C:\WPAI\private-browser-vpn-inventory.md")
$ErrorActionPreference = "Stop"
if (-not (Test-Path $ReportPath)) { throw "Missing report: $ReportPath" }
$c = Get-Content $ReportPath -Raw
foreach ($s in @("## Methodology","## Findings","## Zero-hit","C:\Program Files\Docker","WireGuard","Tor Browser","OpenVPN","Mullvad","Get-VpnConnection")) {
  if ($c -notlike "*$s*") { throw "Report missing required content: $s" }
}
# Spot-check claimed absences
foreach ($p in @("C:\Program Files\Tor Browser","C:\Program Files\WireGuard","C:\Program Files\Mullvad VPN")) {
  if (Test-Path $p) { throw "Report claims absence but path exists: $p" }
}
# Spot-check claimed presence
foreach ($p in @("C:\Program Files\Docker","C:\Users\Bulkl\.docker")) {
  if (-not (Test-Path $p)) { throw "Report lists path but missing on disk: $p" }
}
Write-Output "PASS: $ReportPath structural + spot-check OK"
