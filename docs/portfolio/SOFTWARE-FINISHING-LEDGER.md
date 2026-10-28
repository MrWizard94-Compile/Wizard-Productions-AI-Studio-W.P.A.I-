# WPAI Software Finishing Ledger

**Observed:** 2026-09-08  
**Director priority:** Software products first  
**Authority:** [`../../AGENTS.md`](../../AGENTS.md) and the accepted canonical [WPAI Constitution](https://github.com/MrWizard94-Compile/Agents-Constitution), loaded through `wpai-constitution`  
**Census:** [`inventory-2026-09-08.json`](inventory-2026-09-08.json)

## What WPAI is

Wizard Productions AI Studio is a human-directed creative-media studio. Its
near-term products and music are intended to fund internal tooling and
long-horizon research. AI collaborators own detailed investigation,
implementation, verification, and review packaging; the human director owns
vision, architectural veto, and consequential external actions. The company
voice is transparent about AI assistance and insists that every shipped work
shows deliberate human direction and finishing.

The portfolio is a set of independently owned projects under one studio, not a
single source monorepo. Each product keeps its own Git history, instructions,
runtime boundary, and release evidence.

## The two-part completion bar

A project is only finished when both columns pass with current evidence.

| Production grade | Studio grade |
| --- | --- |
| Intended scope is implemented without stubs or broken integrations. | The primary user journey feels complete from first launch through saved or exported result. |
| Clean build, lint, type/static analysis, dependency audit, and meaningful tests cover normal, negative, and failure paths. | Visual language, copy, naming, credits, and AI disclosure consistently express WPAI. |
| Inputs and trust boundaries are validated; secrets, path traversal, injection, unsafe deserialization, and excess privilege are addressed. | Interaction design is coherent, accessible, responsive, and free of debug surfaces, placeholders, and dead controls. |
| Installation, configuration, upgrade, rollback or recovery, and failure diagnostics are documented and verified. | Defaults, onboarding, examples, and help reduce operator effort and ambiguity. |
| Runtime behavior is exercised through the real client or transport on intended hardware; resource and performance limits are measured where material. | Content and assets receive a human-quality pass, including audio, images, typography, metadata, and provenance where applicable. |
| Release artifacts are reproducible, version-aligned, integrity-checked, licensed, and built from the reviewed source. | A real-device acceptance pass proves the product delivers the intended experience, not merely that it starts. |
| Project Git state, manifest, documentation, and delivery report match the exact release candidate. | Store/listing copy, screenshots, support path, and distribution package accurately describe the delivered product. |

Passing a README claim, a startup check, or a narrow test suite is insufficient.
Public deployment, store upload, spending, credentials, and external messages
remain separate director-controlled actions.

## Census result

The bounded census found **76** current or registry-declared roots: **72 present**,
**4 missing at their registered paths**, **57 registry-listed**, **19 present but
not registered**, and **60 with an independently observed Git root**. It found
**28 software records**. These numbers describe inventory coverage, not product
completion. Twenty-eight independent repositories had working-tree changes at
the observation time; changes may belong to the director or other active work
and must be preserved.

## Software completion order

| Order | Project | Evidence state | Completion handling |
| ---: | --- | --- | --- |
| 1 | RepoForge | **Verification in progress.** Source declares 1.1.0 while the customer ZIP and README were 1.0.0. The existing source tree was otherwise clean when entered. | Finish safe rerun behavior, deterministic 1.1.0 packaging, full gates, and a locally upload-ready artifact. |
| 2 | Mixin Field Manual | **Declared live product; current release not certified.** Clean independent Git root and local build/check scripts exist. | Rebuild from source, run content/link/package checks, compare the sold archive, and synchronize listing/version evidence. |
| 3 | PyMason | **Strong candidate.** Version 1.5.0, clean independent Git root, manifest, tests, smoke check, and desktop build command are declared. | Run source and packaged desktop gates, then exercise the real visual authoring, execution, persistence, import/export, accessibility, and onboarding flows. |
| 4 | DigiChar | **Strong candidate.** Version 3.0.0, clean independent Git root, local-first Tauri architecture, lockfile, manifest, and combined check command are declared. | Verify finance correctness and persistence, Docker Ollama behavior on the recorded hardware, privacy boundaries, recovery, desktop packaging, and end-user flows. |
| 5 | GrokForge | **Mature source, ownership gap.** Version 1.5.0 and lint/test/smoke commands are declared, but it has no independent Git root and is excluded by the root registry. | Establish project ownership and history without absorbing it into the root registry, then perform CLI-host, session, diff/review, hook, packaging, and Windows runtime gates. |
| 6 | NYS Homeschool Document Studio | **Mature source, ownership gap.** Product README and manifest exist, but no independent Git root was observed. | Establish ownership, build the WPF app, and verify recovery, editing, printing, export/import fidelity, accessibility, packaging, and real Windows use. |
| 7 | GrokVerse / Pinkhold | **Declared 1.0.0, ownership gap.** Check and test commands exist; no independent Git root was observed. | Establish ownership, then verify the complete game loop, content controls, offline launch, performance, asset provenance, and Windows package. |
| 8 | obsidian-mcp-server | **Operational candidate, ownership gap.** Version 1.2.1 and build/test evidence exist, but the project has no independent Git root. | Preserve its local-only trust boundary, re-run the real stdio transport and negative scope cases, then establish repository ownership and package it. |
| 9 | RickPrime | **Audit blocked at Git boundary.** Version 1.0.0 and extensive checks are declared; Git rejected the current account because the repository is owned by another Windows identity. | Resolve repository ownership deliberately, then verify integrations, local Ollama, data boundaries, packaging, and complete workstation journeys. |
| 10 | HellForge | **Active development.** Version 0.1.0 on `improve/wpai-operator-v2` with existing untracked work. | Preserve current work, reconcile the branch, then exercise real PTYs, process lifecycle, agent launches, splits, recovery, accessibility, and packaging. |
| 11 | StudioOps | **Active control-plane development.** `improve/control-plane-v2` has extensive existing changes and runtime-generated experiment records. | Separate source from generated experiments, reconcile ownership, verify control-plane invariants and real HITL actions, then audit and package the site and operator tools. |
| 12 | XLang / Aether | **Advanced active development.** Current `codex/xlang-local-first-studio` work is not a final release gate. | Complete the approved language/product scope, full self-host and compatibility gates, native matrix, docs, and clean release evidence. |
| 13 | QuillForge | **Foundation in active development.** Rust source and lockfile exist with a materially dirty tree. | Reconcile the current document-kernel work, then complete the Word-class user surface, durability, export, accessibility, performance, and installer gates. |
| 14 | TwoTell | **Private alpha in active development.** Version 0.1.0, broad verification commands, and substantial uncommitted source exist. | Preserve and reconcile the alpha, then finish consent/privacy/security, mobile/API integration, migrations, recovery, abuse cases, accessibility, and device acceptance. |
| 15 | PsyForge | **Phase-bounded research product.** P0–P6 are declared; current source has substantial changes. P7 expansion requires a director decision. | Stabilize and certify the authorized P0–P6 slice. Do not expand corpus, models, agents, or recommendation authority beyond the approved boundary. |
| 16 | TrackForge | **Verified foundation, incomplete product.** Clean native C++/JUCE root; its README explicitly says it is not a completed studio DAW. | Implement and verify the product plan in complete audio-safe slices, including transport, recording/editing, mixing, persistence, plugins, export, accessibility, and real audio-device use. |
| 17 | WPAI Explorer | **Active development.** Version 1.0.0 with extensive existing changes and a local Ollama/Docker design. | Reconcile current work, validate data provenance and scope, then verify models, search, desktop packaging, recovery, performance, and end-user knowledge workflows. |
| 18 | XTechBot | **Early product.** Version 0.1.0, one tracked change, build/lint commands, and no declared test command. | Add intended-behavior tests and verify OAuth secret handling, rate limits, draft/approval guarantees, live-mode separation, local Ollama, observability, and packaging. |
| 19 | Random Story Generator | **Legacy candidate.** Clean Git root and requirements file; no root-level declared quality commands were discovered. | Establish current product intent, then audit local Ollama behavior, generation controls, persistence/export, model failure handling, UI quality, tests, and packaging. |
| 20 | GitHub Code Crawler | **Utility candidate.** Clean Git root with README and requirements; no root-level declared quality commands were discovered. | Verify API contracts, token and rate-limit handling, license/provenance capture, pagination, retries, output integrity, tests, and distribution. |
| 21 | AtoZ Grabber | **Uncertified automation with existing change.** | Review authorization and account risk, then test timing, session expiry, selection correctness, safe failure, notifications, recovery, and installer behavior before any live use. |
| 22 | Workstation | **Unfinished imported app.** Version 0.0.0 and generic AI Studio documentation remain. | Decide its distinct product role, replace imported scaffolding and cloud assumptions, then build the complete local WPAI product or archive it cleanly. |
| 23 | Bundle.Social | **Insufficient product evidence.** The registered root is present and clean but has no discovered entry document or manifest. | Recover authoritative scope and source if they exist; otherwise archive the empty shell cleanly. |
| 24 | APODE | **Declared not started and revenue-gated** in its implementation plan. | Keep gated until the studio activates it; then implement from the approved plan as a complete product. |
| 25 | FUSE | **Parked in the revenue plan.** Version 1.0.0 exposes start/build scripts but no declared test or lint command. | Do not advance until reactivated; then perform a full Electron product audit rather than treating the version as completion evidence. |
| 26 | YumNom | **Parked by director decision.** | Do not advance until explicitly reactivated. Preserve its current changes. |
| 27 | BitBurner Scripts | **Registered path missing.** | Locate the intended replacement or record a clean archive/removal decision in the registry. |
| 28 | HidoutHunter | **Registered path missing.** | Locate the intended replacement or record a clean archive/removal decision in the registry. |

This order favors existing revenue products, then clean and mature product
candidates, then active foundations and phase-gated work. It will be updated
only from stronger current evidence or a new director decision.

## Current execution

RepoForge 1.1.0 is the active completion target. Its entry audit found a stale
1.0.0 customer package and unsafe rerun staging. Completion requires a
source-matched deterministic ZIP, regression coverage proving unrelated Git
changes stay untouched, synchronized customer copy, a mechanical Constitution
gate, and a documented local release receipt. Store upload remains a separate
external action.

