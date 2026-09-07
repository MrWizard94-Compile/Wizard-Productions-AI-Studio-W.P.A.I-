# WSL `docker-desktop` Deep Inventory (WireGuard + Both Themes)

**Target:** `\\wsl.localhost\docker-desktop` (also `\\wsl$\docker-desktop`, `wsl -d docker-desktop`)  
**Generated:** 2026-08-24  
**Themes covered:** (a) private-browser / VPN — WireGuard first; (b) concealment / dating / sexual / AI-companion  
**Related prior reports:** `private-browser-vpn-inventory.md`, `hiding-inappropriate-inventory.md`

## Executive judgment (WireGuard)

**What your wife likely found is real — and it is infrastructure, not a user WireGuard VPN setup.**

Inside `docker-desktop` there is a stock **WSL2 Linux kernel WireGuard driver** (`wireguard.ko`) under the kernel modules tree, plus Docker Desktop **vpnkit** networking sockets/config. There is **no** `/etc/wireguard`, **no** `wg` / `wg-quick` client binaries, and **no** `wg0.conf` / user WireGuard config files in this distro.

That means: finding “WireGuard” under `\\wsl.localhost\docker-desktop` is **expected for Docker Desktop / WSL2** and is **not** the same thing as installing or configuring the WireGuard VPN app on Windows.

---

## Findings (relevant hits)

| Path | Description | Use / classification |
|------|-------------|----------------------|
| `\\wsl.localhost\docker-desktop\lib\modules\6.18.33.1-microsoft-standard-WSL2\kernel\drivers\net\wireguard\` | Kernel driver directory for WireGuard in the Microsoft WSL2 kernel build `6.18.33.1-microsoft-standard-WSL2`. | **Infrastructure.** Ships with the WSL2 kernel used by Docker Desktop. Not a user-installed VPN client folder. |
| `\\wsl.localhost\docker-desktop\lib\modules\6.18.33.1-microsoft-standard-WSL2\kernel\drivers\net\wireguard\wireguard.ko` | Loadable kernel module file (~220,264 bytes). Confirmed via UNC and `wsl ls`. | **Infrastructure.** Kernel module binary; presence alone does not mean a VPN tunnel was configured. |
| `\\wsl.localhost\docker-desktop\run\host-services\vpnkit.sock` | Unix socket for Docker Desktop **vpnkit** host networking service. | **Infrastructure.** Docker Desktop virtual networking (name contains “vpn” but is not WireGuard user VPN). |
| `\\wsl.localhost\docker-desktop\run\host-services\vpnkit-data.sock` | Companion vpnkit data socket. | **Infrastructure.** Docker Desktop networking. |
| `\\wsl.localhost\docker-desktop\run\host-services\gvisor-ethernet-vpnkit-protocol.sock` | gVisor ethernet ↔ vpnkit protocol socket. | **Infrastructure.** Docker Desktop networking stack. |
| `\\wsl.localhost\docker-desktop\usr\bin\vpnkit-bridge` | Docker Desktop **vpnkit-bridge** binary (~13.3 MB) on the VM PATH. | **Infrastructure.** Part of Docker Desktop’s networking stack; not a user WireGuard/OpenVPN client. |
| `\\wsl.localhost\docker-desktop\tmp\docker-desktop-root\etc\kubeadm\vpnkit-controller.yaml` | Overlay copy of vpnkit controller YAML inside Docker Desktop rootfs staging. | **Infrastructure.** Desktop/LinuxKit packaging residue. |
| `\\wsl.localhost\docker-desktop\tmp\docker-desktop-root\etc\vpnkit-expose-port.json` | vpnkit port-expose config JSON in staging rootfs. | **Infrastructure.** |
| `\\wsl.localhost\docker-desktop\tmp\docker-desktop-root\run\host-services\vpnkit*.sock` (and gvisor-ethernet-vpnkit-protocol.sock) | Staging copies of the same vpnkit sockets under `tmp\docker-desktop-root`. | **Infrastructure.** |
| `\\wsl.localhost\docker-desktop\tmp\docker-desktop-root-ro\etc\kubeadm\vpnkit-controller.yaml` | Read-only overlay twin of vpnkit controller YAML. | **Infrastructure.** |
| `\\wsl.localhost\docker-desktop\tmp\docker-desktop-root-ro\etc\vpnkit-expose-port.json` | Read-only overlay twin of vpnkit port config. | **Infrastructure.** |
| `\\wsl.localhost\docker-desktop\mnt\host\` | Projection of Windows host drives into the WSL VM (`c`, `d`, `e`, plus `wsl` / `wslg`). | **Host bind mount.** Named for scope only — not treated as Linux-native content. Full Windows re-inventory via this path was **not** performed. |

### Linux-native equivalents (same hits)

| Linux path inside `docker-desktop` | Same classification |
|------------------------------------|---------------------|
| `/lib/modules/6.18.33.1-microsoft-standard-WSL2/kernel/drivers/net/wireguard/` | Kernel WireGuard driver dir |
| `/lib/modules/.../wireguard/wireguard.ko` | Kernel module |
| `/run/host-services/vpnkit.sock` (+ `vpnkit-data.sock`, `gvisor-ethernet-vpnkit-protocol.sock`) | Docker vpnkit |
| `/tmp/docker-desktop-root/.../vpnkit*` | Desktop staging copies |

---

## Explicit non-findings (user VPN / both themes)

These were checked under the **docker-desktop Linux tree** (not a full Windows re-scan) with **per-pattern raw transcripts** in `{SCRATCH}/search-wsl-theme-patterns.log` (also appended into `search-wsl-docker-desktop.log`). Each pattern was queried individually; empty patterns are logged as `EMPTY|<name>|0 hits` / `WSL_EMPTY|<name>|0 paths`.

| Pattern query | Result under non-host roots |
|---------------|-----------------------------|
| `*wireguard*` | **Hits** — kernel module dir + `wireguard.ko` only (infra) |
| `*vpnkit*` | **Hits** — host-service sockets + `usr\bin\vpnkit-bridge` (infra) |
| `*wg-quick*` | **EMPTY** (0) |
| `wg0.conf` | **EMPTY** (0) |
| `*.ovpn` | **EMPTY** (0) |
| `*openvpn*` | **EMPTY** (0) |
| `*mullvad*` | **EMPTY** (0) |
| `*tailscale*` | **EMPTY** (0) |
| `*nordvpn*` / `*protonvpn*` / `*surfshark*` | **EMPTY** (0) |
| `*librewolf*` / `*tor*browser*` | **EMPTY** (0) |
| `*tinder*` / `*bumble*` / `*hinge*` | **EMPTY** (0) |
| `*replika*` / `*onlyfans*` / `*pornhub*` | **EMPTY** (0) |
| `*veracrypt*` / `*truecrypt*` | **EMPTY** (0) |
| `\\wsl.localhost\docker-desktop\etc\wireguard` | **Missing** |
| `wg` / `wg-quick` binaries | **Missing** (`NO_WG_BIN` / `NO_WG_QUICK`) |

### False positives filtered

| Path | Why ignored |
|------|-------------|
| `...\usr\bin\factor` | Substring `tor` in “factor” — BusyBox/util binary, not Tor Browser |
| `...\usr\bin\wget` | Substring `wg` — HTTP downloader, not WireGuard |
| `...\usr\sbin\pwhistory_helper` | PAM helper; unrelated substring noise |

---

## Host-mount scoping (`mnt\host`)

| Item | Detail |
|------|--------|
| Present | `\\wsl.localhost\docker-desktop\mnt\host` with top-level `c`, `d`, `e`, `wsl`, `wslg` |
| Policy | **Not** used to redo a full `C:\` / `E:\` inventory “as Linux content” |
| Spot-check | Attempted shallow depth-2 name filter for `wireguard` / `wg-quick` / `*.ovpn`; **access denied** on recurse (documented). Top-level drive letters only confirmed. |
| Exclusion | If `E:\special` is visible through `mnt\host\e\special`, it remains **out of scope** (same exclusion as prior inventory) |

---

## Methodology

### Roots / access methods

1. UNC: `\\wsl.localhost\docker-desktop` (primary for Explorer-parity with what a person browsing that share would see)
2. UNC alt: `\\wsl$\docker-desktop` (reachable)
3. Shell: `wsl -d docker-desktop` for `ls`, `command -v wg`, `/etc/wireguard` checks, and per-pattern `find`
4. Distro state: `docker-desktop` **Running** (WSL2)

### Unreachable / warnings (continue on reachable)

- **Recurring WSL warning:** `wsl: Failed to mount D:\, see dmesg for more details.` appears on essentially every `wsl -d docker-desktop` invocation (also captured in spotcheck / wireguard logs). **D:\ is a tiny empty SYSTEM volume on the host;** WSL fails to mount it into the VM. Search **continued on all reachable roots** (`/etc`, `/lib/modules`, `/run`, `/usr`, UNC share, `mnt\host\c` / `e`, etc.). This is **not** treated as a WireGuard/theme hit — only a host-drive mount failure.
- Shallow recurse under `mnt\host` returned **Access is denied** for depth-2 listing; top-level `c`/`d`/`e`/`wsl`/`wslg` still enumerated. No full Windows re-inventory attempted through the bind mount.

### Queries

- WireGuard: `*wireguard*`, `wireguard.ko`, `/etc/wireguard`, `wg`, `wg-quick`, `wg0.conf`, modules under `/lib/modules/.../drivers/net/`
- Docker net: `*vpnkit*` (sockets + `vpnkit-bridge`)
- Theme (a) **per-pattern with EMPTY lines:** openvpn, mullvad, tailscale, nordvpn, protonvpn, surfshark, librewolf, tor-browser, `*.ovpn`, wg-quick, wg0.conf
- Theme (b) **per-pattern with EMPTY lines:** tinder, bumble, hinge, replika, onlyfans, pornhub, veracrypt, truecrypt
- Pruned from deep walks: full `mnt\host` Windows trees; intentional non-inventory of `E:\special`

### Why this answers the WireGuard concern

Explorer under `\\wsl.localhost\docker-desktop` can surface the folder name **`wireguard`** inside `lib\modules\...\drivers\net\`. That path is the **kernel driver package**, sitting next to other network drivers. Combined with **vpnkit** sockets/bridge (Docker’s own networking), the share contains multiple “vpn/wireguard”-looking names that are **normal for Docker Desktop**, not proof of a personal WireGuard VPN install.

### Evidence transcripts (scratch)

- `{SCRATCH}/search-wsl-wireguard.log`
- `{SCRATCH}/search-wsl-docker-desktop.log`
- `{SCRATCH}/search-wsl-unc-wireguard.log`
- `{SCRATCH}/search-wsl-theme-patterns.log` — **raw per-pattern HIT/EMPTY/WSL_EMPTY/WSL_WARN lines**

---

## Zero-hit summary (auditable)

Inside docker-desktop **excluding** host bind-mount Windows content:

- No user WireGuard configuration directory or client tools  
- No private anonymity browsers  
- No dating / adult / AI-girlfriend application trees  
- Only WireGuard/vpn-related names = **kernel module + Docker vpnkit infrastructure**
