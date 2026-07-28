# WPAI Company Context

**Purpose:** Living, source-linked orientation for Wizard Productions AI Studio (WPAI). Read this before beginning work anywhere in `C:\WPAI`, then open the relevant project-local guidance and source records.

**Status:** Root intake completed 2026-07-17; Git portfolio registry initialized 2026-07-28. This is an orientation record, not a substitute for the authoritative documents it links to.

## 1. Company Identity

WPAI is Wizard Productions AI Studio: an umbrella creative-media company organized into connected divisions. Its operating model is sequential: near-term creative and product revenue funds internal tooling and longer-horizon research.

The human director sets vision and priorities. AI collaborators own detailed investigation and implementation within the director's scope, while preserving human approval for consequential external actions.

**Authoritative sources:**

- `AGENTS Constitution` — company-wide operating constitution.
- `WPAI-ROADMAP.md` — division sequence, activation gates, and 90-day company plan.
- `REVENUE-PLAN.md` — commercial priorities and distribution-first policy.

## 2. Working Rules

- Treat `AGENTS Constitution` as the top-level operating standard: complete, documented, tested, maintainable work; protect Git history and documentation as cognitive infrastructure.
- Before entering a project, read its `AGENTS.md`, `CLAUDE.md`, README, specification, and design documents when present. Known project-local instruction files exist in AI Research projects and PyMason.
- Keep context source-linked. Label a statement as **verified**, **director decision**, or **needs verification** rather than guessing.
- Do not open, copy, log, or place credentials in this record. Use placeholders and project-local secret-handling procedures only.
- Do not automate publishing, spending, distribution, or other external commitments without explicit human approval. StudioOps documents this as a hard HITL boundary.
- The private root Git repository is a lightweight company registry, not a source-code monorepo. Each owned project has its own local Git root and private `origin`; see `PROJECT-REGISTRY.md`. Do not create root submodule pointers until the referenced project commits are safely published.

## 3. Portfolio Model

| Area                  | Role and current phase                                                                                                                   | Primary source                                                       |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `Music/`              | Active launch division and intended funding engine. Tracks, artwork, releases, distribution, marketing, and stem-pack records live here. | `Music/README.md`, `Music/CATALOG.md`, `Music/DISTRIBUTION-PLAN.md`  |
| `Graphics/`           | Dormant as a standalone division; actively supports music and brand work.                                                                | `Graphics/README.md`                                                 |
| `Gaming/`             | Active Minecraft/mod work under the Mrwizard94/WPAI umbrella; public Astral Sorcery-port release is the stated milestone.                | `Gaming/README.md`                                                   |
| `Software/`           | Active internal tooling and external-product portfolio. The StudioOps control plane is live.                                             | `Software/README.md`                                                 |
| `AI-Research/`        | Long-horizon research and invention portfolio; pre-work at division level, with many individual prototypes and research projects.        | `AI-Research/README.md`, `AI-Research/AUTONOMOUS-AI-ARCHITECTURE.md` |
| `Quantum/`            | Deliberately deferred; depends on stable AI Research and spare capacity.                                                                 | `Quantum/README.md`                                                  |
| `Brand/`              | Company visual identity and voice assets.                                                                                                | `Brand/BRAND-VOICE.md`                                               |
| `Games/`              | Separate game-concept area, currently including Cinderforge planning and project folders.                                                | `Games/GAME-CONCEPT-BRIEF.md`                                        |
| `llm/`                | Local-model/runtime and benchmark workspace.                                                                                             | `llm/bench-results-20260713-043704.txt`                              |
| `Workspace/`          | Runtime state for WPAI/HellForge tooling; inspect only when an operational task requires it.                                             | `Workspace/.wpai/`, `Workspace/.hellforge/`                          |
| `Archives/`, `Tools/` | Storage and supporting third-party/tooling areas; not default implementation targets.                                                    | Directory inventory                                                  |

## 4. Current Operating Picture

### Commercial focus

The revenue plan records a distribution-first rule: do not create additional products while finished offerings remain unlisted. It records RepoForge and Mixin Field Manual as live as of 2026-07-09, with music release, stem packs, and audience-building as the next revenue work. Treat storefront state as **needs external verification** before making any public claim or decision.

Music is the stated launch division. The roadmap records that commercial rights were cleared, the release package for **Weaponized Mind** was frozen, and a distributor/account plus release execution remained a director-controlled action.

### Music and brand intake — verified records

- The company voice is transparent about AI assistance, human-directed, and non-defensive: **“AI is in the name; the wizard is in the work.”** See `Brand/BRAND-VOICE.md`.
- `Music/CATALOG.md` records **Weaponized Mind** as the launch single, with a frozen package in `Music/Releases/Weaponized Mind/` containing the release master, video, stems, cover, lyrics, and metadata.
- `Music/EP-PLAN.md` defines **BreakThrough** as a five-track, concept-driven EP assembled after the single sequence. It is still in packaging/metadata/artwork completion, not release-ready as a full EP.
- `Music/STEM-LICENSE.md` supplies a non-exclusive, royalty-free license template, and `Music/STEM-PACKS.md` defines a $15 per-track / $39 vault packaging plan. Product publication and storefront status require external verification before action.
- The Music distribution and marketing records state legal/platform policies as research snapshots dated 2026-07-07/08. Re-verify all distributor, platform, licensing, and pricing rules before release or public use.

**Records requiring reconciliation before operational decisions:**

1. Track counts differ: `Music/README.md` and the root roadmap describe 22 tracks, while `Music/CATALOG.md` records 27 total tracks (21 WAV masters, 5 MP3-only, 1 video-only).
2. Release cadence differs: `Music/DISTRIBUTION-PLAN.md` proposes 1–2 week singles; `Music/MARKETING-PLAN.md` proposes 3–4 weeks.
3. `Music/STEM-PACKS.md` lists **Night Drive** as a 9-stem sellable set, while `Music/CATALOG.md` records only WAV + MP3 for that track. Inspect the asset folder and resolve the source record before listing it.

### Operational tooling

`Software/StudioOps/` is a Git repository containing:

- the owned static studio site for `wpaistudio.net`;
- a PowerShell council-bus CLI;
- the `wpai.ps1` control plane, including approvals, budget/kill controls, music-package validation, and overnight safeguards;
- the Improve Swarm / Hell Forge tooling for evidence-based local experimentation.

### Explicit project status

- **YumNom is parked.** This is a director decision recorded on 2026-07-17. Do not advance it unless the director explicitly reactivates it.
- PyMason has a current project directory plus dated backups. Prefer `Software/PyMason/` if it is reactivated, and read its `AGENTS.md` first.

### Git portfolio registry — director decision, 2026-07-28

- The root remote `MrWizard94-Compile/Wizard-Productions-AI-Studio-W.P.A.I-` is private and attached to `C:\WPAI` on `main`.
- Each cataloged WPAI-owned project root has a private GitHub remote and a local `origin`, documented in `PROJECT-REGISTRY.md`. Existing project histories and working changes were preserved.
- The linking pass did **not** stage, commit, or push project content. Before any project receives its first baseline push, inspect its ignore rules, secret exposure, generated output, and current working state; never publish credentials or runtime data merely because the remote is private.
- Third-party/reference trees, archive folders, runtime state, backup snapshots, and the unnamed `Gaming/Minecraft/Mods-1.21.1-NeoForge/New folder` are deliberately excluded from the project registry.

## 5. Project Intake Index

This index identifies project roots and required entry documents. It does not imply that each project has been audited at code level.

### Software

- `StudioOps/` — Git repository; start with `README.md`.
- `PyMason/` — start with `AGENTS.md` and `README.md`; dated backup folders are historical snapshots.
- `YumNom/` — Git repository; `SPEC.md`; **parked**.
- `HellForge/`, `XTechBot/` — Git repositories with README/package manifests.
- `RepoForge/`, `MixinFieldManual/`, `APODE/`, `AtoZ-Grabber/`, `GitHubCodeCrawler/`, `FUSE/`, and older utility projects — cataloged; require project-level intake before changes.

### AI Research

- `Janus/` — Git repository; read `AGENTS.md`, `CLAUDE.md`, then `README.md` before work.
- `Smart Library/` — Git repository with `AGENTS.md` and `CLAUDE.md`.
- `AssetConverter/`, `Recurrsive/`, `Grok_Playground/`, `REL_Codex_Variant/`, and `TSAM/` — Git project roots with local readme/manifest guidance where listed.
- `deep_research_engine/`, `research_crawler/`, `VeriForge/`, `Topological Hydro-Computational Engine/`, and other research folders — cataloged but not yet code-level audited.

### Gaming and game concepts

- `Gaming/Minecraft/mod-test-suite/` has a README; Minecraft mod and modpack folders need targeted intake before work.
- `Games/Cinderforge/` and `Games/cinderforge-(4.3)/` each have a README; the parent pitch and v1-plan documents provide portfolio-level context.

## 6. Intake Coverage and Update Protocol

| Scope                                                           | Coverage as of 2026-07-17      | Next handling                                                      |
| --------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------ |
| Root governance and strategy                                    | Reviewed                       | Keep this record synchronized when company-level decisions change. |
| Division charters and root inventory                            | Reviewed                       | Use the linked sources for current specifics.                      |
| Project roots, Git boundaries, and local guidance               | Cataloged                      | Read local guidance before modifying any project.                  |
| Project architecture, tests, build health, and deployment state | Not yet systematically audited | Audit on entry or through focused portfolio-intake passes.         |
| Credentials and private keys                                    | Intentionally excluded         | Never add them to this file.                                       |

When updating this record:

1. Prefer the project-local source of truth for technical details.
2. Record dated, material director decisions here when they affect multiple future tasks.
3. Remove or revise superseded claims rather than letting stale context accumulate.
4. Keep this document concise enough to make a fresh AI productive quickly.
