# Leftover / Orphaned Residue Inventory (Both Themes)

**Generated:** 2026-08-24  
**Focus:** leftover, separated, partial, or residual artifacts — not a full live-install catalog  
**Themes:** (a) private browser / VPN / privacy tooling (b) dating / AI companion / concealment-adjacent  
**Prior reports cited:** `private-browser-vpn-inventory.md`, `hiding-inappropriate-inventory.md`, `wsl-docker-desktop-inventory.md`  
**Exclusion:** `E:\special\` folder contents not inventoried

## Summary

Most “live install” paths for Tor, Mullvad, WireGuard (Windows app), OpenVPN, commercial VPNs, Tinder/Bumble/Replika, etc. remain **absent**. What **does** remain are **residue pieces**: DuckDuckGo installer files + Temp run evidence (browser ran recently but is not permanently installed), browser history of DuckDuckGo Browser download / `duck.ai`, Recent shortcuts to WSL `wireguard*` infrastructure paths, split adult-media archives/folders outside `E:\special\`, and multi Chrome profiles.

**Judgment call on DuckDuckGo:** Downloads + Temp `RunningInstances` prove **download + run**; missing Program Files/Appx/Start Menu prove **not currently a durable install** (uninstalled or bootstrapper-only).

**Judgment call on WireGuard under WSL:** Recent Explorer access to `wireguard.ko` / `wireguard\` / `wireguard.h` under `\\wsl.localhost\docker-desktop` is real leftover *navigation* residue, but the targets remain **Docker/WSL infrastructure**, not a user VPN client leftover (see WSL inventory).

---

## Findings (leftovers / separated pieces)

| Path | Description | Apparent use / leftover class |
|------|-------------|-------------------------------|
| `C:\Users\Bulkl\Downloads\DuckDuckGo.Installer.exe` | Signed DuckDuckGo Browser installer (~12.3 MB; LW 2026-07-21). | **Leftover installer** after privacy-browser download. |
| `C:\Users\Bulkl\Downloads\DuckDuckGo.appinstaller` | App Installer manifest for Desktop Browser 0.169.3.0 (LW 2026-08-19). | **Leftover manifest** pointing at DuckDuckGo MSIX CDN bundle. |
| `C:\Users\Bulkl\AppData\Local\Temp\DuckDuckGo\` | Temp tree created 2026-07-21 when installer/bootstrap ran. | **Run residue.** |
| `C:\Users\Bulkl\AppData\Local\Temp\DuckDuckGo\RunningInstances\*` | Instance lock/log files naming `DDG-Browser` for this user SID; RUNNING/SHUTTING_DOWN on **2026-08-19** and **2026-08-20**. | **Proof browser process ran** recently despite no durable install path. |
| `C:\Users\Bulkl\AppData\Local\Temp\DuckDuckGo.Installer\` | Installer cache/temp (created 2026-07-21; updated into Aug 2026). | **Installer leftover.** |
| Chrome History — `duckduckgo.com/windows` (Default) | Visits titled “Download the DuckDuckGo Browser for Windows”. | **Download-page residue** tied to the installer files. |
| Chrome History — `duck.ai` (Default, Profile 1, Profile 3) | DuckDuckGo private AI chat site. | **AI companion-adjacent residue** (Duck.ai product), not a dating-app install. |
| Chrome History — Google My Activity with `q=candy.ai` (Profile 1; documented in prior hiding inventory) | My Activity filter/search for `candy.ai`. | **Weak AI-companion brand residue** (query only; not a candy.ai site install). |
| `C:\Users\Bulkl\AppData\Roaming\Microsoft\Windows\Recent\wireguard.lnk` | Recent shortcut → `\\wsl.localhost\docker-desktop\lib\modules\...\drivers\net\wireguard` | **Navigation leftover** to WSL WireGuard **kernel driver dir** (infra). |
| `...\Recent\wireguard.ko.lnk` | Recent shortcut → `...\wireguard\wireguard.ko` | Same — **infra module file** opened/viewed via Explorer. |
| `...\Recent\wireguard.h.lnk` | Recent shortcut → containerd overlay snapshot path `...\usr\include\linux\wireguard.h` | **Infra header** inside Docker Desktop snapshot FS — not user VPN config. |
| `...\Recent\docker-desktop (wsl.localhost).lnk` | Recent shortcut to `\\wsl.localhost\docker-desktop` | Shows the WSL share was browsed (context for WireGuard discovery). |
| `\\wsl.localhost\docker-desktop\lib\modules\...\wireguard\wireguard.ko` | Stock WSL2 kernel module (~220 KB). | **Infrastructure** (re-verified). Not user VPN leftover. |
| `\\wsl.localhost\docker-desktop\run\host-services\vpnkit*.sock` + `usr\bin\vpnkit-bridge` | Docker Desktop vpnkit networking. | **Infrastructure** (re-verified). |
| `C:\Users\Bulkl\Videos\xxx` | Folder of 7 adult-titled MP4s (~1.8 GB). | **Separated adult media** outside `E:\special\` (cited from hiding inventory; re-verified present). |
| `E:\special.zip` | ~9.35 GB zip at `E:\` root. | **Split/outside archive** related to excluded special media set; path not inside `E:\special\`. |
| `E:\Users\bu1k1\special.7z` | ~4.62 GB 7z at profile root. | **Separated archive** (sibling/copy of Private nest). |
| `E:\Users\bu1k1\Desktop\Memories\Private\` (+ nested `special.7z`) | ~170 files / ~10 GB private media tree. | **Separated private/adult collection** outside excluded folder. |
| Chrome multi-profile map (`Local State`) | Default/Profile1 Rob accounts; Profile2 Charlene; Profile3 Robert. | **Dual/multi-account surface** (re-verified); not itself a dating app leftover. |
| `C:\Users\Bulkl\Downloads\*.ae` (`secure_vault.ae`, etc.) | Aether language sample sources. | **Not** AxCrypt vault leftovers (header-identified earlier); listed only to avoid misclassification. |

---

## Already-documented vs freshly re-verified

| Item | Status this pass |
|------|------------------|
| DuckDuckGo Downloads + Temp RunningInstances | **Re-verified present**; judgment refined (run leftover, not durable install) |
| WSL `wireguard.ko` / vpnkit | **Re-verified present**; still labeled infrastructure |
| `Videos\xxx`, `E:\special.zip`, `special.7z`, `Memories\Private` | **Re-verified present** |
| Prior inventory Markdown files under `C:\WPAI\` | Present |
| Windows WireGuard/OpenVPN/Tor/Mullvad/Tinder/etc. installs | Still **absent** (PATH False matrix) |

---

## Zero-hit residue areas

| Residue class | Result |
|---------------|--------|
| Orphaned Program Files / LocalAppData app folders for Tor, Mullvad, WireGuard, OpenVPN, Nord, Tailscale, Brave, LibreWolf, Tinder, Bumble, Hinge, Replika, VeraCrypt | **None** (durable install paths False) |
| `*.ovpn` under Downloads/Documents/OneDrive/WPAI Software|Tools / E MyLab|WasOnDesktop | **None** |
| Recycle Bin theme products | **None** (only Minecraft `bumblezone` false positives) |
| `/etc/wireguard` inside docker-desktop | **Missing** |
| Durable DuckDuckGo Appx / Program Files / Start Menu | **Missing** despite run residue |

## Unreachable / incomplete residue surfaces

| Surface | Status |
|---------|--------|
| `C:\Windows\Prefetch` | **Access denied** on enumeration (`UnauthorizedAccessException`; `Test-Path` returns True but `Get-ChildItem` cannot list). Theme Prefetch zero-hit is **not claimed**. Documented in `{SCRATCH}/search-temp-prefetch.log` as `PREFETCH_LIST_STATUS\|ACCESS_DENIED_OR_ERROR`. |

---

## False positives filtered

| Item | Why |
|------|-----|
| Recycle `bumblezone` / `bumble_*.png` | Minecraft mod assets |
| LocalAppData `History`, `IsolatedStorage`, `VirtualStore` | Substring `tor` only |
| Aether `*.ae` “secure_vault” | Programming samples, not encrypted vaults |
| Store package names containing “Store” | Unrelated to VPN |

---

## Methodology

### Residue classes searched

1. **Downloads** installers/manifests (`*.exe`, `*.appinstaller`, name patterns for both themes)  
2. **Temp** theme-named folders + children (DuckDuckGo RunningInstances)  
3. **Prefetch** — attempted; listing **Access Denied** (see Unreachable)  
4. **Recycle Bin** name filter  
5. **AppData Local/Roaming / Packages** orphan folder names  
6. **Recent** `.lnk` targets for wireguard/duck/wsl/inventory  
7. **Known-path re-verify matrix** (DuckDuckGo, Tor/Mullvad/VPN/dating, adult split paths, WSL infra)  
8. **Browser History** residue hosts (DuckDuckGo download, duck.ai, dating/VPN download pages)  
9. **Prior `C:\WPAI\*-inventory.md`** citation + existence check  

### Roots

`C:\Users\Bulkl\Downloads`, `AppData\Local\Temp`, Prefetch, Recycle, AppData Local/Roaming, Recent, Chrome/Edge History, `C:\WPAI`, selected `E:\` paths **outside** `E:\special\`, light `wsl -d docker-desktop` checks.

### Unreachable / warnings

- **`C:\Windows\Prefetch`:** path exists but listing is **Access Denied** (`System.UnauthorizedAccessException`). Prefetch is therefore under **Unreachable**, not Zero-hit — no “None” claim without a successful file count. Evidence: `{SCRATCH}/search-temp-prefetch.log` (`PREFETCH_LIST_STATUS|ACCESS_DENIED_OR_ERROR`).
- `wsl: Failed to mount D:\` on WSL invocations (empty SYSTEM volume); continued on reachable paths.  
- `E:\special\` contents excluded by policy.  
- Full Windows re-scan via `mnt\host` out of scope.

### Evidence (scratch)

- `{SCRATCH}/search-leftovers.log`  
- `{SCRATCH}/search-temp-prefetch.log`  
- `{SCRATCH}/search-appdata-orphans.log`  
- `{SCRATCH}/search-browser-residue.log` / `browser-residue-hits.log`  

---

## Bottom line

**Leftovers that matter for the two themes:**

1. **DuckDuckGo Browser** — installer files + Temp proof it **ran** (Aug 19–20) without a lasting install footprint.  
2. **WSL WireGuard/vpnkit** — still infra; Recent shortcuts show those paths were **opened in Explorer**.  
3. **Adult/private media split** outside `E:\special\` (`Videos\xxx`, `special.zip` / `special.7z`, `Memories\Private`).  
4. **duck.ai / DuckDuckGo download history** — privacy/AI-adjacent browsing residue.  
5. **No leftover dating-app installs** or `*.ovpn` / Windows WireGuard client orphans found in residue locations searched.
