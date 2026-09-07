param([string]$ReportPath = "C:\WPAI\hiding-inappropriate-inventory.md")
$ErrorActionPreference = "Stop"
if (-not (Test-Path $ReportPath)) { throw "Missing report: $ReportPath" }
$c = Get-Content $ReportPath -Raw
foreach ($s in @(
  "## Methodology","## Findings","## Zero-hit","E:\special",
  "Videos\xxx","Memories\Private","Charlene","VeraCrypt","Tinder",
  "E:\special.zip","E:\Users\bu1k1\special.7z",
  "C:\Users\Bulkl\Desktop","searched-but-unavailable","OneDrive\Desktop"
)) {
  if ($c -notlike "*$s*") { throw "Report missing required content: $s" }
}
if ($c -notmatch 'exclud') { throw "Report methodology must document E:\special exclusion" }
if ($c -match 'E:\\special\\[^\s`\]]+\.(mp4|jpg|jpeg|png|mpeg)') { throw "Report must not inventory E:\special media files" }
foreach ($p in @(
  "C:\Users\Bulkl\Videos\xxx",
  "E:\Users\bu1k1\Desktop\Memories\Private",
  "E:\special.zip",
  "E:\Users\bu1k1\special.7z"
)) {
  if (-not (Test-Path $p)) { throw "Reported path missing on disk: $p" }
}
if (Test-Path "C:\Users\Bulkl\Desktop") { throw "Desktop unexpectedly present; methodology said unavailable" }
foreach ($p in @("C:\Program Files\VeraCrypt","C:\Program Files\Tinder")) {
  if (Test-Path $p) { throw "Report claims absence but exists: $p" }
}
# Size sanity for archives
$zip = Get-Item "E:\special.zip"
$sz = Get-Item "E:\Users\bu1k1\special.7z"
if ($zip.Length -lt 1GB) { throw "E:\special.zip unexpectedly small: $($zip.Length)" }
if ($sz.Length -lt 1GB) { throw "E:\Users\bu1k1\special.7z unexpectedly small: $($sz.Length)" }
Write-Output "PASS: $ReportPath structural + exclusion + skeptic-gap paths OK"
Write-Output "special.zip_bytes=$($zip.Length)"
Write-Output "bu1k1_special.7z_bytes=$($sz.Length)"
Write-Output "desktop_exists=$(Test-Path 'C:\Users\Bulkl\Desktop')"
Write-Output "onedrive_desktop_exists=$(Test-Path 'C:\Users\Bulkl\OneDrive\Desktop')"
