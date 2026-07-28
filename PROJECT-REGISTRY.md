# WPAI Project Registry

**Scope:** private repository links established 2026-07-28. Each listed project has a local Git root and an `origin` under `MrWizard94-Compile`.

The WPAI root stays a lightweight registry instead of a Git submodule superproject. That preserves project ownership and prevents a root commit from referencing unpublished heads in active worktrees. Project content is not staged, committed, or pushed by the linking pass.

## Software

| Local project path | Private repository |
| --- | --- |
| `Software/APODE` | `APODE` |
| `Software/AtoZ-Grabber` | `AtoZ-Grabber` |
| `Software/BitBurner Scripts` | `BitBurner-Scripts` |
| `Software/Bundle.Social` | `Bundle-Social` |
| `Software/DigiChar` | `DigiChar` |
| `Software/FUSE` | `FUSE` |
| `Software/GitHubCodeCrawler` | `GitHubCodeCrawler` |
| `Software/HellForge` | `hellforge` |
| `Software/HidoutHunter` | `HidoutHunter` |
| `Software/MixinFieldManual` | `MixinFieldManual` |
| `Software/PyMason` | `PyMason` |
| `Software/QuillForge` | `QuillForge` |
| `Software/Random Story Generator` | `Random-Story-Generator` |
| `Software/RepoForge` | `repoforge` |
| `Software/RickPrime` | `RickPrime` |
| `Software/StudioOps` | `StudioOps` |
| `Software/Workstation` | `Workstation` |
| `Software/wpai-explorer` | `WPAI-Explorer` |
| `Software/XLang` | `XLang` |
| `Software/XTechBot` | `XTechBot` |
| `Software/YumNom` | `YumNom` |

## AI Research

| Local project path | Private repository |
| --- | --- |
| `AI-Research/AssetConverter` | `AssetConverter` |
| `AI-Research/AutomationLab` | `AutomationLab` |
| `AI-Research/Claude_Playground` | `Claude-Playground` |
| `AI-Research/deep_research_engine` | `Deep-Research-Engine` |
| `AI-Research/Grok_Playground` | `Grok-Playground` |
| `AI-Research/Janus` | `JanusPrime` |
| `AI-Research/Operation-Pinky and the Brain` | `Operation-Pinky-and-the-Brain` |
| `AI-Research/Recurrsive` | `Research` |
| `AI-Research/REL_Codex_Variant` | `REL` |
| `AI-Research/research_crawler` | `Research-Crawler` |
| `AI-Research/Smart Library` | `Smart-Library` |
| `AI-Research/Topological Hydro-Computational Engine` | `Topological-Hydro-Computational-Engine` |
| `AI-Research/TSAM` | `TSAM` |
| `AI-Research/VeriForge` | `VeriForge` |

## Gaming and games

| Local project path | Private repository |
| --- | --- |
| `Games/Cinderforge` | `Cinderforge` |
| `Games/cinderforge-(4.3)` | `Cinderforge-4-3` |
| `Gaming/TerraBlock` | `TerraBlock` |
| `Gaming/Minecraft/Omni_Framework` | `Omni-Framework` |
| `Gaming/Minecraft/mod-test-suite` | `Minecraft-Mod-Test-Suite` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/OmniFix` | `OmniFix` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/SteampunkFactory/steampunk_factory_mod` | `Steampunk-Factory-Mod` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/SteampunkFactory/steampunk_factory_rp` | `Steampunk-Factory-Resource-Pack` |
| `Gaming/Minecraft/Mods-1.21.1-NeoForge/Adaptive Attacks` | `Adaptive-Attacks` |
| `Gaming/Minecraft/Mods-1.21.1-NeoForge/Adaptive Bosses` | `Adaptive-Bosses` |
| `Gaming/Minecraft/Mods-1.21.1-NeoForge/Living_Villages` | `Living-Villages` |
| `Gaming/Minecraft/Modpacks/Aethelgard-Grand-Synthesis` | `Aethelgard-Grand-Synthesis` |
| `Gaming/Minecraft/Modpacks/Aetheria-Nexus-of-Epochs` | `Aetheria-Nexus-of-Epochs` |
| `Gaming/Minecraft/Modpacks/Aetherial-Convergence` | `Aetherial-Convergence` |
| `Gaming/Minecraft/Modpacks/Chronicles-Shattered-Cosmos` | `Chronicles-Shattered-Cosmos` |
| `Gaming/Minecraft/Modpacks/Omni32-Modpack` | `Omni32-Modpack` |
| `Gaming/Minecraft/Modpacks/Omniverse-Odyssey` | `Omniverse-Odyssey` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/Astral_Sorcery_Port` | `Astral-Sorcery-1.20.1-Port` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/Big Little Fixes` | `Big-Little-Fixes` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/Node Core` | `NodeCore` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/Valkyrien Portals` | `Valkyrien-Portals` |
| `Gaming/Minecraft/Mods-1.20.1-Forge/VS2 Ship Systems` | `VS2-Ship-Systems` |

## Baseline publication snapshot — 2026-07-28

The following project roots received an audited, private source baseline during the registry rollout. Each `main` branch was published to its listed private repository unless a pre-existing, unrelated remote history required a non-destructive baseline branch.

- **Software:** `APODE`, `AtoZ-Grabber`, `BitBurner-Scripts`, `Bundle-Social`, `FUSE`, `GitHubCodeCrawler`, `HidoutHunter`, `MixinFieldManual`, `PyMason`, `Random-Story-Generator`, `RickPrime`, `Workstation`.
- **Software with preserved unrelated remote `main`:** `repoforge` and `WPAI-Explorer` publish the local source baseline on `baseline/local-source-20260728`; their existing remote `main` histories were not overwritten.
- **AI research:** `AutomationLab`, `Claude-Playground`, `Deep-Research-Engine`, `Operation-Pinky-and-the-Brain`, `Research-Crawler`, `Topological-Hydro-Computational-Engine`, `VeriForge`.
- **Games and Minecraft:** `Cinderforge`, `Cinderforge-4-3`, `TerraBlock`, `Minecraft-Mod-Test-Suite`, `OmniFix`, `Steampunk-Factory-Mod`, `Steampunk-Factory-Resource-Pack`, `Adaptive-Attacks`, `Adaptive-Bosses`, `Living-Villages`.

All remaining catalogued project roots are linked to their private remotes. Existing projects with active worktrees were intentionally not auto-committed, rebased, merged, or reset during this rollout.

## Deliberate exclusions

- `Archives/`, `Tools/`, `Workspace/`, project backups, generated dependencies, build output, local model files, and runtime state are not standalone product repositories.
- Music, Brand, Graphics, Quantum, and `llm` remain company-division records under the private root registry rather than being split into artificial repositories.
- Third-party/reference source trees, including `Reference/`, `_reference/`, and the bundled `ModernFix` tree, are not WPAI projects and were not re-homed.
- `Gaming/Minecraft/Mods-1.21.1-NeoForge/New folder` is unnamed and therefore intentionally has no repository until the director supplies a product name.
