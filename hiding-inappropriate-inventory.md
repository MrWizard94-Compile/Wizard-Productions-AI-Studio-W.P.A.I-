# Concealment / Dating / Inappropriate-Activity Inventory

**Machine:** local Windows PC (user `Bulkl`)  
**Generated:** 2026-08-24  
**Wife name used as contrast cue only:** Charlene  
**Parallel to:** `C:\WPAI\private-browser-vpn-inventory.md`

## Summary

No installed dating apps (Tinder, Bumble, Hinge, Ashley Madison, Seeking, Feeld, etc.), no VeraCrypt/TrueCrypt/Cryptomator-style vault software, no desktop Replika/Character.AI/OnlyFans clients, and **no Chrome/Edge history hits** for pornhub.com, tinder.com, bumble.com, hinge.co, character.ai, or replika.com.

**Relevant hits outside the excluded `E:\special` folder** include:

1. A local adult-video folder at `C:\Users\Bulkl\Videos\xxx`
2. A large “Private” media folder at `E:\Users\bu1k1\Desktop\Memories\Private` (separate path from `E:\special`; contents overlap thematically / by filename with that excluded tree)
3. Archive `E:\special.zip` (~9.35 GB) on the `E:\` drive root — **outside** the excluded folder
4. Archive `E:\Users\bu1k1\special.7z` (~4.62 GB) at the secondary profile root — distinct from `Private\special.7z`
5. Multiple Chrome profiles (including Charlene’s) and Snapchat **web** login residue on two of those profiles
6. A weak AI-companion-adjacent signal: Google My Activity URL on Chrome Profile 1 containing query `candy.ai` (not a confirmed visit to candy.ai itself)

Deliberate gap: **`E:\special` (the folder) was not inventoried** (user exclusion). Adult media known to live there will not appear as findings below. Archives named `special` that live **outside** that folder path are listed.

This report does **not** paste explicit media, chat bodies, passwords, or session tokens — path + purpose only.

---

## Findings (relevant hits)

| Path | Description | Apparent use |
|------|-------------|--------------|
| `C:\Users\Bulkl\Videos\xxx` | Folder named `xxx` containing **7** `.mp4` files (~1.8 GB total). Filenames are adult-oriented (explicit titles present on disk; not listed here). | Local adult video library **outside** `E:\special`. |
| `E:\special.zip` | Zip archive at **`E:\` drive root** (exact size **10038090296** bytes / 10,038,090,296 ≈ **9.35 GB**; last write 2026-02-23). Path is **not** inside the excluded folder `E:\special\`. Contents not opened/extracted. | Likely compressed backup/export of the excluded “special” media set (name + size class). Listed because it sits outside the exclusion path. |
| `E:\Users\bu1k1\special.7z` | 7-Zip archive at the **`bu1k1` profile root** (exact size **4960204133** bytes / 4,960,204,133 ≈ **4.62 GB**; last write 2024-04-08). Distinct path from `E:\Users\bu1k1\Desktop\Memories\Private\special.7z` (same byte size/timestamp — probable copy). Contents not opened. | Compressed private/adult media archive stored at profile root, outside `E:\special\`. |
| `E:\Users\bu1k1\Desktop\Memories\Private` | Directory named `Private` under `Memories` on the secondary user profile desktop path. ~**170** files / ~**10 GB** (images, videos, phone `IMG_`/`VID_`/`Screenshot_` media, plus its own nested `special.7z`). | Private/adult personal media collection **outside** the excluded `E:\special` path. Overlaps by name/content class with that excluded folder; still reportable because this path was not excluded. |
| `E:\Users\bu1k1\Desktop\Memories\Private\special.7z` | Nested copy of the ~4.62 GB `special.7z` archive inside the Private folder (same size/timestamp as profile-root archive). | Archive member of the Private media collection; listed separately from `E:\Users\bu1k1\special.7z` so both exact paths are auditable. |
| `E:\Users\bu1k1\Desktop\Memories\` | Parent folder containing `Private\`, `Pictures.zip`, and one PNG asset. | Container for the Private media set above. |
| `C:\Users\Bulkl\AppData\Local\Google\Chrome\User Data\` | Chrome user-data root with **multiple profiles**: `Default`, `Profile 1`, `Profile 2`, `Profile 3` (+ System Profile). | Multi-account browser setup (see profile table). Not encrypted concealment software, but a dual/multi-identity surface. |
| `...\Chrome\User Data\Default` | Profile display name **Rob**; Google account `bulkleyrob1@gmail.com` (gaia name Rob Bulkley). | Primary Rob browsing profile. |
| `...\Chrome\User Data\Profile 1` | Profile display name **Rob**; Google account `bu1k13y@gmail.com`. | Second Rob Google account profile. History includes Snapchat web login flows and a Google My Activity URL with `q=candy.ai`. |
| `...\Chrome\User Data\Profile 2` | Profile display name **Charlene**; Google account `victoriaaphrodite1994@gmail.com` (gaia name Charlene Herrington). | Wife’s Chrome profile on this PC. History includes Snapchat web login flows. |
| `...\Chrome\User Data\Profile 3` | Profile display name **Robert**; Google account `bulkleyrobert1@gmail.com`. | Third Rob/Robert Google account profile. Adult/dating host scan: zero hits. |
| Chrome History (Profile 1 & 2) — Snapchat hosts | Visits to `snapchat.com` / `accounts.snapchat.com` (login, captcha, password, web client). No Snapchat **desktop** app install found. | Snapchat used via browser. Social/messaging residue (can be benign or dating-adjacent; presence only recorded). |
| Chrome History (Profile 1) — Google My Activity | URL on `myactivity.google.com` including query parameter `q=candy.ai`. | Indicates a My Activity search/filter for the string `candy.ai` (AI companion brand). **Not** a recorded navigation to `https://candy.ai` itself (exact-host count for candy.ai site was this query URL only). |
| `C:\Users\Bulkl\Downloads\Consolidate\` | Exported / ingested AI chat archives (`conversations-*.json`, `chat.html`, zip bundles, `ingested-ai-chats`). | Local archive of AI assistant chats (creative/work/medical/music topics observed in samples). Keyword greps produced hits inside huge JSON blobs; sampled context was **not** AI-girlfriend product chat. Listed because it is AI chat residue on disk. |
| `C:\Users\Bulkl\Downloads\secure_vault.ae` (and sibling `*.ae`) | Small text sources whose header identifies **Aether** language samples (“Aether Secure Vault: RSA-based Cryptographic Verification Engine”), plus `aether_gen.ae`, `complex_vm.ae`, etc. | Programming / language demos — **not** AxCrypt encrypted containers despite `.ae` extension and “vault” naming. |

### Chrome profile map (from `Local State`)

| Profile folder | UI name | Gaia name | Signed-in email (as stored by Chrome) |
|----------------|---------|-----------|----------------------------------------|
| Default | Rob | Rob Bulkley | bulkleyrob1@gmail.com |
| Profile 1 | Rob | Rob Bulkley | bu1k13y@gmail.com |
| Profile 2 | Charlene | Charlene Herrington | victoriaaphrodite1994@gmail.com |
| Profile 3 | Robert | Robert Bulkley | bulkleyrobert1@gmail.com |

---

## Zero-hit areas (auditable)

### Concealment / crypto vaults

- VeraCrypt / TrueCrypt / Cryptomator / Boxcryptor / AxCrypt / Folder Lock / SafeHouse: **not installed** (`where.exe`, known Program Files / AppData paths, uninstall registry, Start Menu, services)
- Container extensions scanned under Documents/Downloads/OneDrive/WPAI/MyLab/WasOnDesktop (`*.hc`, `*.tc`, `*.kdbx`, `*.vault`, …): **no real vault containers** found (Aether `.ae` sources excluded as false positives)
- No dating/secret “vault” apps in `winget list` filter
- Hidden dirs under Documents/Downloads/Videos: only normal Windows junction noise (`My Music`, etc.), plus the intentional `Videos\xxx` finding above
- BitLocker cmdlet unavailable / no extra encrypted data volume beyond normal NTFS volumes `C:` (Windows) and `E:` (Data); `D:` empty SYSTEM volume

### Dating apps / sites

- Desktop/Store installs: Tinder, Bumble, Hinge, OkCupid, Match, Grindr, POF, Ashley Madison, Seeking, Feeld — **missing**
- Exact host history (Chrome all profiles + Edge Default): `tinder.com`, `bumble.com`, `hinge.co`, `ashleymadison`, `okcupid`, `match.com` — **0**
- Bookmarks scan for dating/adult hosts: **none** on Chrome Default / Profile 1 and Edge Default

### Sexual sites / AI girlfriend products (browser)

- Exact host history: `pornhub.com`, `onlyfans.com`, `character.ai`, `replika.com`, `crushon.ai`, `janitorai`, `dreamgf` — **0** across profiles
- Desktop Replika / Character.AI / Candy.ai / Romantic AI / OnlyFans clients — **missing**
- Telegram / Signal / WhatsApp / Snapchat **desktop** / Discord **desktop** — **missing** (Discord and Snapchat appear via **web** in Chrome history only; Discord samples were gaming/mod communities)

### Project / docs

- `C:\WPAI` catalog/software text greps for AI girlfriend / dating-app build notes: **no dedicated project**
- Steam `steamapps\common` adult/waifu/hentai-named titles: **none** matched by name filter

### Excluded by request

- **`E:\special\` (folder)**: path exists; **contents not listed or described** per user instruction. Methodology records this deliberate gap. Sibling/outside archives `E:\special.zip` and `E:\Users\bu1k1\special.7z` are **not** covered by that exclusion and appear in Findings.

---

## Related / false positives (not counted as target findings)

| Item | Why filtered |
|------|----------------|
| `C:\WPAI\Software\obsidian-mcp-server\...\vault` | Code module named “vault” for Obsidian notes |
| `E:\Users\bu1k1\AppData\...\Microsoft\Vault` | Windows Credential Vault |
| Recycle Bin `bumblezone` assets | Minecraft “The Bumblezone” mod residue |
| YouTube “Family Affair” history hit | Music video title containing “affair” |
| Profile 2 history “Bumble Bee” frog/shrimp pages | Animal product pages, not Bumble the dating app |
| Mary J. Blige / other substring noise | Keyword collision only |

---

## Methodology

### Explicit exclusion

- **`E:\special\` (folder only)**: do not inventory or describe contents. Adult material there is out of scope for this report even though a thorough search would otherwise include it.
- Archives with similar names that live **outside** that folder — including `E:\special.zip` and `E:\Users\bu1k1\special.7z` — **are** in scope and listed under Findings (path + size/purpose only; contents not opened).

### Roots searched

| Root | How |
|------|-----|
| `C:\Users\Bulkl` (Documents, Downloads, Videos, AppData Local/Roaming, OneDrive) | Known-path installs; filename sweeps; hidden-dir pass; media name counts; `.ae`/vault extensions |
| `C:\Users\Bulkl\Desktop` | **Searched-but-unavailable:** `Test-Path` / `dir` return missing (no Desktop folder or junction under the profile). Not an ACL denial — path absent. |
| `C:\Users\Bulkl\OneDrive\Desktop` | Used as the redirected/replacement desktop surface; top-level listing + depth-3 name filter for dating/adult/conceal patterns (no additional dating/adult hits beyond normal work shortcuts/docs). |
| `C:\Program Files`, `C:\Program Files (x86)`, `C:\ProgramData` | Top-level listing; known dating/conceal paths; Start Menu shortcuts |
| Uninstall registry + `winget list` | Product-name filters for dating/conceal/AI companion |
| `C:\WPAI` | Software/docs/workspace listings; content greps |
| `D:\` | Empty SYSTEM volume (noted) |
| `E:\` except folder `E:\special\` | Drive-root archives (`E:\special.zip`), MyLab, WasOnDesktop, Jarvis_WebUI, `E:\Users\bu1k1` (including profile-root `special.7z` and `Desktop\Memories\Private`), Program Files |
| Chrome / Edge | Profile enumeration from `Local State`; bookmarks keyword scan; History via SQLite copy (dating/adult/AI-companion patterns + exact-host recount) |

### Searched-but-unavailable / gaps

| Path | Status |
|------|--------|
| `C:\Users\Bulkl\Desktop` | Missing on disk (`ROOT_MISS` / `Test-Path=False`). Desktop content lives under `C:\Users\Bulkl\OneDrive\Desktop` instead. |
| `E:\special\` (folder contents) | Present but **intentionally not inventoried** (user exclusion). |

### Query classes

Concealment (VeraCrypt, TrueCrypt, Cryptomator, vault/private/hidden/xxx folder names, `*.hc`/`*.tc`/`*.kdbx`), dating (Tinder, Bumble, Hinge, Ashley Madison, Seeking, Feeld, OkCupid, Match, Grindr, POF), sexual/AI companion (OnlyFans, Pornhub, Chaturbate, Fansly, Replika, Character.AI, Candy.ai, Romantic AI, NSFW chatbot hosts), messaging often used for private chat (Snapchat/Telegram/Signal/WhatsApp/Discord — install + history), multi-profile browser cues, and non-spouse intimate naming greps in personal docs (no strong non-Charlene love-letter hits in depth-3 Documents/Downloads text samples).

### Limits

- Binary media **without** suggestive names may be under-detected (no full ML image classification).
- Browser History reflects retained SQLite rows only (cleared history would not appear).
- Remote phone-only apps / cloud DMs not synced to this disk were out of scope.
- Keyword noise filtered; only curated hits listed.
- Large archives (`special.zip` / `special.7z`) were **not** extracted; purpose inferred from path, name, and size only.

### Evidence transcripts (scratch)

Session scratch (deleted when goal ends): `search-filesystem.log`, `search-apps-registry.log`, `search-browsers.log`, `search-concealment.log`, `search-content.log`, `browser-history-hits.log`, `browser-history-adult-dating.log`, `browser-hosts-exact.log`, `search-findings-detail.log`, `skeptic-gap-fix.log`.
