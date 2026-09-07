param([string]$ReportPath = "C:\WPAI\wsl-docker-desktop-inventory.md")
$ErrorActionPreference = "Stop"
if (-not (Test-Path $ReportPath)) { throw "Missing $ReportPath" }
$c = Get-Content $ReportPath -Raw
foreach ($s in @(
  "\\wsl.localhost\docker-desktop","wireguard.ko","vpnkit","Infrastructure",
  "Failed to mount D:","search-wsl-theme-patterns.log","EMPTY","vpnkit-bridge","mnt\host"
)) {
  if ($c -notlike "*$s*") { throw "Missing required content: $s" }
}
$plog = Join-Path $env:LOCALAPPDATA "Temp\grok-goal-42446af232cd\implementer\search-wsl-theme-patterns.log"
# Prefer sibling scratch via report-path if needed - also accept C:\WPAI-adjacent evidence note
$scratchLog = "C:\Users\Bulkl\AppData\Local\Temp\grok-goal-42446af232cd\implementer\search-wsl-theme-patterns.log"
if (-not (Test-Path $scratchLog)) { throw "Missing per-pattern log: $scratchLog" }
$pr = Get-Content $scratchLog -Raw
foreach ($p in @("EMPTY|tinder|","EMPTY|mullvad|","EMPTY|ovpn|","COUNT|wireguard|","Failed to mount D:")) {
  if ($pr -notlike "*$p*") { throw "Pattern log missing evidence: $p" }
}
$ko = "\\wsl.localhost\docker-desktop\lib\modules\6.18.33.1-microsoft-standard-WSL2\kernel\drivers\net\wireguard\wireguard.ko"
if (-not (Test-Path $ko)) { throw "wireguard.ko missing" }
if (Test-Path "\\wsl.localhost\docker-desktop\etc\wireguard") { throw "etc/wireguard unexpectedly exists" }
Write-Output "PASS: report + per-pattern EMPTY evidence + D: mount methodology OK"
