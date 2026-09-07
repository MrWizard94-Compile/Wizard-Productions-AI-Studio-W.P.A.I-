# Private Browser / VPN Inventory

**Machine:** local Windows PC (user `Bulkl`)  
**Generated:** 2026-08-24  
**Scope:** Fixed drives `C:\`, `D:\`, `E:\`; user profile; Program Files; ProgramData; `C:\WPAI`; Docker Desktop (live + offline paths); WSL `docker-desktop`.

## Summary

No installed private/anonymity browsers (Tor Browser, Mullvad Browser, LibreWolf, Brave, etc.), no commercial or FOSS VPN clients (WireGuard, OpenVPN, NordVPN, ExpressVPN, Proton VPN, Surfshark, Tailscale, ZeroTier, Windscribe, Outline, etc.), no `.ovpn` / WireGuard config hits in the searched roots, and no Windows VPN connection profiles were found.

Docker Desktop **is** installed and, after the engine was restarted, was inventoried live. Present images and containers are AI/dev related (Ollama, Janus, WPAI Explorer, polyglot research). **None** are Tor, VPN, proxy, or private-browser stacks.

No local source trees, Dockerfiles, or notes under `C:\WPAI\Software`, `C:\WPAI\Tools`, catalogs, or `E:\MyLab\Program Dev` indicate a project to **build** a private browser or VPN.

---

## Findings (relevant hits)

Each item below includes exact path, what it is, and how it relates to this search.

| Path | Description | Use / relevance |
|------|-------------|-----------------|
| `C:\Program Files\Docker\` | Docker Desktop / CLI install root (cli-plugins + Docker app) | Container runtime install. **Not** a VPN or private browser; included because Docker was in scope and holds the only container platform on this PC. |
| `C:\Users\Bulkl\.docker\` | Docker client config home (`config.json`, `daemon.json`, buildx, contexts, mcp, models, etc.) | Offline Docker client state. No VPN/Tor project configs observed in inventory of this tree. |
| `C:\ProgramData\DockerDesktop\` | Docker Desktop machine-wide install metadata (`install-log-admin.txt`, `install-settings.json`) | Installer/admin logs for Docker Desktop. |
| `C:\Users\Bulkl\AppData\Local\Docker\` | Docker Desktop local runtime data (logs, WSL integration, locks) | Local Desktop state; WSL backend data lives under here when present. |
| `C:\Users\Bulkl\AppData\Roaming\Docker\` | Docker Desktop roaming settings (`settings-store.json`, extensions, login metadata) | User Desktop settings. Secrets/tokens not dumped. |
| `C:\Users\Bulkl\AppData\Roaming\Docker Desktop\` | Electron app cache/state for Docker Desktop UI | UI persistence only. |
| `C:\Program Files\Google\Chrome\` | Google Chrome browser install | Mainstream browser. **Not** a dedicated private/anonymity browser. Listed for coverage honesty. |
| `C:\Users\Bulkl\AppData\Local\Google\Chrome\` | Chrome user data / profile root | Profile, extensions, cache. No VPN-branded extensions identified by name (keyword-only false positives filtered). |
| `C:\Program Files (x86)\Microsoft\Edge\` | Microsoft Edge browser install | Mainstream browser. **Not** a dedicated private browser. |
| `C:\Users\Bulkl\AppData\Local\Microsoft\Edge\` | Edge user data / profile root | Same class as Chrome above. |

### Docker live inventory (daemon reachable)

| Resource | Exact identity | Description / use |
|----------|----------------|-------------------|
| Image `hello-world:latest` | ID `96498ffd522e` | Docker smoke-test image. Unrelated to VPN/browser. |
| Image `janus-cognition:latest` | ID `5306497c67e9` | Local AI/cognition image (~9 GB). Unrelated. |
| Image `janus-memory:latest` | ID `375513dda444` | Local AI memory image (~9 GB). Unrelated. |
| Image `node:20-alpine` | ID `fb4cd12c85ee` | Node.js base image. Unrelated. |
| Image `ollama/ollama:latest` | ID `6345fbc18bd7` | Ollama LLM runtime. Unrelated. |
| Image `polyglot-research-env:latest` | ID `0827f608406d` | Local research/env image. Unrelated. |
| Image `python:3.11-alpine` | ID `25976e9d34a0` | Python base image. Unrelated. |
| Image `wpai-explorer-app:latest` | ID `dff1d007f453` | WPAI Explorer app image. Unrelated. |
| Container `ollama` | ID `29f247228ac2` (Exited) | Ollama serve. Unrelated. |
| Container `janusprime-memory` | ID `0510dd72c037` (Exited) | Janus memory service. Unrelated. |
| Container `ollama-engine` | ID `ca73e67b0a59` (Exited) | Older Ollama engine container. Unrelated. |
| Volume `hfs-npm-cache` | local | npm cache volume. Unrelated. |
| Volume `janus_ollama_data` | local | Janus/Ollama data. Unrelated. |
| Volume `ollama` | local | Ollama data. Unrelated. |
| Volume `wpai-explorer_node_modules` | local | Explorer node_modules. Unrelated. |
| Volume `wpai-explorer_ollama-data` / `wpai-explorer_ollama_data` | local | Explorer Ollama data variants. Unrelated. |
| WSL distro `docker-desktop` | Running, WSL2 | Docker Desktop Linux engine backend. |

**Filtered Docker name search** (images/containers/volumes matching Tor, Mullvad, WireGuard, OpenVPN, VPN, Tailscale, shadowsocks, v2ray, xray, privoxy, i2p, Nord, Proton, Surfshark, LibreWolf, Brave): **zero hits**.

---

## Zero-hit areas (auditable)

These locations / queries were searched and produced **no** private-browser or VPN product hits:

### Known install / config paths (all missing)

- `C:\Program Files\Tor Browser`
- `C:\Program Files (x86)\Tor Browser`
- `C:\Users\Bulkl\Desktop\Tor Browser`
- `C:\Users\Bulkl\AppData\Local\Tor Browser`
- `C:\Users\Bulkl\AppData\Local\Programs\Tor Browser`
- `C:\Program Files\Mullvad VPN`
- `C:\Program Files\Mullvad Browser`
- `C:\Users\Bulkl\AppData\Local\Mullvad VPN`
- `C:\Users\Bulkl\AppData\Roaming\Mullvad VPN`
- `C:\Program Files\WireGuard`
- `C:\Users\Bulkl\AppData\Local\WireGuard`
- `C:\Users\Bulkl\AppData\Roaming\WireGuard`
- `C:\ProgramData\WireGuard`
- `C:\Program Files\OpenVPN`
- `C:\Program Files\OpenVPN Connect`
- `C:\Users\Bulkl\AppData\Local\OpenVPN Connect`
- `C:\Users\Bulkl\AppData\Roaming\OpenVPN`
- `C:\Program Files\Tailscale` / `C:\Program Files (x86)\Tailscale` / `C:\Users\Bulkl\AppData\Local\Tailscale`
- `C:\Program Files\NordVPN` (+ Local/Roaming NordVPN)
- `C:\Program Files\ExpressVPN` (+ Local ExpressVPN)
- `C:\Program Files\Proton\VPN` / `C:\Program Files\Proton Technologies` / Local+Roaming ProtonVPN
- `C:\Program Files\Surfshark`
- `C:\Program Files\BraveSoftware` / Local+Roaming BraveSoftware
- `C:\Program Files\LibreWolf`
- `C:\Program Files\ZeroTier` / `(x86)`
- `C:\Program Files\Windscribe`
- `C:\Program Files\Outline`

### `where.exe` binaries (all not found)

`tor`, `TorBrowser`, `mullvad`, `mullvad-vpn`, `wireguard`, `openvpn`, `tailscale`, `nordvpn`, `expressvpn`, `protonvpn`, `brave`, `librewolf`, `windscribe`, `zerotier-one`, `outline`

### Windows VPN / tunnel surfaces

- `Get-VpnConnection` / `-AllUserConnection`: **0** profiles
- `rasphone.pbk` under AppData and ProgramData: **missing**
- WinHTTP proxy: **direct access** (no proxy)
- VPN-like adapters (WireGuard / Wintun / TAP / NordLynx / Tailscale / ZeroTier / OpenVPN / Mullvad): **none**
- Matching driver files under `C:\Windows\System32\drivers` for wintun/wireguard/ovpn/nord/tailscale/zerotier/mullvad/windscribe: **none** (substring false positives like `atapi.sys` excluded)

### Config files

- `*.ovpn` under Documents, Downloads, `C:\WPAI\Software|Tools|docs|Workspace`, `E:\MyLab`, `E:\special`, `E:\WasOnDesktop`: **none**

### Package managers

- Chocolatey: not installed
- Scoop apps dir: not present
- `winget list` filtered for VPN/private-browser product names: **no real product matches** (only unrelated substring false positives such as “Store”, “Hotspot”/Hotpatch, “MCreator”)

### Project / docs / build evidence

- Content grep of `C:\WPAI` `*.md|txt|yml|yaml|json|ps1|…` for private browser / Tor Browser / Mullvad / WireGuard / OpenVPN / NordVPN / Tailscale / LibreWolf / build-VPN phrasing: **no matches**
- `C:\WPAI\PROJECT-REGISTRY.md` and `C:\WPAI\WPAI-CATALOG.md`: **no matches**
- `C:\Users\Bulkl\Documents` same content patterns: **no matches**
- `C:\WPAI\Software\*` project dirs (APODE, DigiChar, FUSE, HellForge, QuillForge, psyforge, PyMason, Workstation, XLang, etc.): **no VPN/private-browser product**
- `C:\WPAI\Tools\`: Godot + JDK only
- `E:\MyLab\Program Dev\`: `ai-hub-desktop` (+ zip) and `My_AI_Team.md` only — **not** VPN/browser
- Recursive `*tor*` filename sweeps under large trees (e.g. `C:\WPAI\AI-Research`) produced only **false positives** (Minecraft assets like `bioreactor_*`, Rust crates like `ctor`, “generator”, “validator”); aborted as noise — documented here so zero-claim is not silent

### Other drives

- `D:\` (label `SYSTEM`): empty root listing; no user VPN/browser content
- `E:\Program Files`: only `ModifiableWindowsApps`
- `E:\` archive names at root: no vpn/tor/mullvad/wireguard/openvpn/browser archives
- `cmd dir /s /b /ad` for Tor Browser / Mullvad / WireGuard / OpenVPN / NordVPN / Tailscale / Brave / LibreWolf on `E:\`: interrupted after partial walk; depth-2 name filters on MyLab/special/WasOnDesktop/Jarvis_WebUI/stufffromoldm2 showed **no real VPN/browser product dirs** (only MCreator/modding false positives under `E:\Users\bu1k1`)

### Browsers present but out of “private browser” class

Firefox / Waterfox / Floorp / Opera / Vivaldi / LibreWolf / Brave: **not installed**.

---

## Methodology

### Roots searched

| Root | How searched |
|------|----------------|
| `C:\Users\Bulkl` | Known-path existence checks; `where.exe`; shallow precise name pass; Downloads/Documents filename filters; AppData VPN/browser package paths; Chrome/Edge extension manifest keyword scan |
| `C:\Program Files` / `C:\Program Files (x86)` | Top-level directory listing; known VPN/browser folder existence; uninstall registry (`HKLM`/`HKCU` Uninstall keys) |
| `C:\ProgramData` | DockerDesktop path; WireGuard/OpenVPN/rasphone known paths; Start Menu shortcuts filter |
| `C:\WPAI` | Catalog/registry grep; Software/Tools/docs/Workspace listings; `*.ovpn` dir; content grep for VPN/private-browser terms |
| `D:\` | Root `dir` |
| `E:\` | Top-level listing; depth-2 on Program Files, Users, MyLab, special, WasOnDesktop, stufffromoldm2, Jarvis_WebUI; Program Dev listing; `*.ovpn` on MyLab/special/WasOnDesktop |
| Docker | First attempt while daemon down → failure captured; second attempt after user reported Docker up → live `images` / `ps -a` / `volume ls` / `network` / `compose ls` / `wsl -l -v`; offline paths under `.docker`, Program Files\Docker, ProgramData\DockerDesktop, AppData Local/Roaming Docker |

### Queries / patterns covered

Name/path/content patterns included (non-exclusive): Tor / Tor Browser, Mullvad, LibreWolf, Brave, WireGuard, OpenVPN, NordVPN, ExpressVPN, ProtonVPN, Surfshark, Tailscale, ZeroTier, Windscribe, CyberGhost, Hotspot Shield, Outline, Psiphon, shadowsocks, v2ray/xray, sing-box, softether, pritunl, i2p, Whonix, Orbot, “private browser”, `*.ovpn`, Windows VPN APIs, TAP/Wintun NICs.

### Docker daemon timeline

1. **Initial attempt:** Docker CLI present (client 29.5.3) but API pipe `dockerDesktopLinuxEngine` missing; WSL `docker-desktop` **Stopped**. Failure written to search logs / `docker-unavailable.log`. Offline Docker paths still enumerated.
2. **Re-attempt after user notice “Docker is up again”:** Daemon reachable; WSL `docker-desktop` **Running**; full image/container/volume inventory captured (see Findings).

### Limits / skipped noise

- Full recursive content scan of all of `C:\` (including huge `AI-Research` asset trees, `node_modules`, cargo registries) was **not** done line-by-line; mitigated with broad name/path sweeps, known-path checks, registry/services/adapters, and deeper greps on user/code/Docker roots.
- Broad `*Tor*` directory filters match unrelated strings (`ctor`, `monitor`, `generator`, `Store`, `Doctor`); those false positives are **not** listed as findings.
- Remote cloud accounts, phones, and other PCs were out of scope.
- Credentials/tokens in Docker login files were not copied into this report.

---

## Related but not matching intent

These exist on the machine but are **not** private browsers, VPN clients, or builds thereof:

- Google Chrome and Microsoft Edge (general web browsers)
- Docker Desktop and the AI/dev images listed above
- `E:\MyLab\Program Dev\ai-hub-desktop` (AI hub desktop project, not VPN/browser)
- Assorted WPAI Software projects (QuillForge, DigiChar, HellForge, etc.)

---

## Evidence locations (implementer scratch)

Search transcripts used to produce this report (session scratch; may be deleted when the goal ends):

- `search-filesystem.log` (+ filtered extract)
- `search-fast.log`
- `search-precise.log`
- `search-docker.log`
- `docker-unavailable.log` (first daemon-down capture)
- `docker-images-full.txt` / `docker-ps-full.txt` / `docker-volumes-full.txt`
- `search-windows-vpn.log`
- `search-e-drive-deep.log`
- `search-mylab-programdev.log`
- `search-other-drives.log`
