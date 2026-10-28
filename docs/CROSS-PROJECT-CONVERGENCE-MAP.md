# Cross-Project Convergence Map

**Generated:** 2026-08-10  
**Scope:** Historical constitutional framework (AC), XLang/Aether, PsyForge, Recurrsive, Omni stack, and major adjacent WPAI projects  
**Method:** Extract *actual* primitives from design docs, types, architecture specs, and runnable surfaces — not marketing names  
**Stance:** Convergence means the *same abstraction* appears independently (or near-independently) in more than one product lineage. Shared constitution law is noted as *inherited*, not convergent invention.

**Governance routing correction — 2026-10-18:** This remains the August 10
research snapshot, not a fresh product, runtime or invention audit. Its AC
primitives describe the historical framework. Current law comes only from the
accepted [WPAI Constitution](https://github.com/MrWizard94-Compile/Agents-Constitution)
using `wpai-constitution` and one verified frozen source revision; this research
map does not authorize loading or distributing the retired local pack.
The recovery anchor preserves the retained local variant; it does not establish
a byte-exact reconstruction of the August 10 research input.

---

## 1. How to read this map

| Term | Meaning |
|------|---------|
| **Primitive** | A named concept that is *load-bearing* in design or code (types, kernels, gates, stores, effects) — not a UI label |
| **Independent appearance** | Same idea, different product lineage, not merely copied from a shared lib |
| **Inherited** | Shared constitutional lineage or a shared control-plane document; historical inheritance is not current source authority |
| **Projected** | Same SoT reflected in another system (e.g. Janus tasks → BLACKBOARD status) |

**Evidence grades**

| Grade | Meaning |
|-------|---------|
| **Code** | Typed/runtime artifact exists |
| **Spec** | Binding architecture/design doc |
| **Corpus** | Large written corpus with schemas (may outrun implementation) |
| **Sim** | Simulation/measurement campaign |

---

## 2. Project primitive inventories

### 2.1 Historical constitutional framework (AC)

| Primitive | Role | Evidence |
|-----------|------|----------|
| **Rule ID** (`CONST-*`, `ENG-*`, …) | Stable law atom; one home | Spec + `RULE-REGISTRY.md` |
| **Module** (`MOD-*`) | Scoped law unit + applicability matrix | Spec |
| **Authority levels 1–4** | Constitution → SOP → modules → project law | Spec |
| **Section 0 gate (15 points)** | Pre-delivery stop-ship checklist | Spec + skill/tools |
| **Definition of Done** | Machine-checkable completeness | Spec |
| **One-home (`CONST-ONEHOME-001`)** | No duplicate binding law | Spec |
| **Portable pack** | Movable identity via `PACK`/`ADOPT`/`LOCK` | Spec + tools |
| **SOP phases 1–10** | Research → design → engineer → audit → deliver | Spec |
| **Self-audit / verify-pack** | Integrity tooling for the law itself | Code (`tools/*.ps1`) |
| **Templates** (MANIFEST, ADR, OVERRIDE) | Delivery and amendment shapes | Spec |

**Domain:** quality/process *law*, not product runtime.

---

### 2.2 XLang / Aether

| Primitive | Role | Evidence |
|-----------|------|----------|
| **`weave`** | Named function / computation unit | Code + language surface |
| **`world`** | Source-file compilation unit | Code |
| **`Whole` / `Truth` / `Text` / `Bytes`** | Core value types | Code |
| **Record / shape / table** | Immutable data + dual layout (rows/columns) | Code (M6) |
| **Arena / Buffer / loan / release** | Bounded resources, no ambient allocator | Code (M2/M19a) |
| **`Error[Whole]` effect** | Abortive typed error, handle/forward | Code (M4) |
| **Comptime (`COMPTIME_WHOLE`)** | Fixed-budget pure Whole eval | Code (M5/M15/M23) |
| **Nursery (`together` / `spawn`)** | Structured cooperative concurrency | Code (M7) |
| **Task frame + `checkpoint`** | Deterministic cancel of parked frames | Code (M19e / AETH v12) |
| **Host / foreign weave + grants** | Capability-mediated external authority | Code (M8/M14/M21) |
| **AETH artifact + verifier** | Verify-before-run / forge-write | Code |
| **Seed compiler + dual-compare oracle** | Self-host product path; bootstrap as recovery | Code (BARP) |
| **`aether.ast` / `aether.edit` / diagnostic v8** | Structural authoring contract | Code |
| **Project / workspace / lock** | Offline integrity graphs | Code (M9–M18, PKG-001) |
| **Claim register** (`CLM-*`) | Proven / direction / hypothesis / prohibited | Spec |

**Domain:** deterministic local language + AI-primary structural toolchain.

---

### 2.3 PsyForge

| Primitive | Role | Evidence |
|-----------|------|----------|
| **PsychologyConcept** | Mechanism + game apps + ethical rating | Code (`src/types`) |
| **PlayerModel + trait vector** | Explorer/collector/social/… multi-axis | Code |
| **GraphNode / GraphEdge** | Concept ↔ Emotion ↔ Outcome | Code |
| **DesignAgent** | Specialized evaluator (psych/economy/ethics/designer) | Code |
| **Simulation state** | Idle/running/complete forecast loop | Code hooks |
| **REQ-\<DOMAIN\>-NNN** | Requirements with lifecycle | Corpus (Volumes I–V) |
| **Conformance (MUST/SHOULD/MAY)** | Spec language | Corpus |
| **Traceability chain** | Vision → req → arch → impl → test → compliance | Corpus |

**Domain:** behavioral intelligence for games (dashboard implemented; full backend corpus-heavy).

---

### 2.4 Recurrsive (von Neumann bypass campaign)

| Primitive | Role | Evidence |
|-----------|------|----------|
| **Iteration artifact** | Complete sim/script + results JSON + plots | Code/Sim |
| **Pinned-host weight store** | Weights live in host RAM, not full VRAM | Sim |
| **Double-buffered stream** | Transfer *i+1* while compute *i* | Sim |
| **Working-set VRAM bound** | 2–3 layer/expert buffers | Sim |
| **PCIe floor model** | Throughput bound = max(transfer, compute) | Sim |
| **MoE expert streaming** | Stream only active experts | Sim |
| **Quantized transfer + dequant** | INT8/INT4 row-block packing | Sim |
| **Prefetch predictor economics** | Miss curve vs oracle | Sim |
| **Hybrid SSM:attention ratio** | Fixed-state vs KV growth trade | Sim/MQAR |
| **Energy/memory model** | Bytes×pJ + MAC energy | Sim |
| **Retraction / evidence grade** | Explicit invalidation of bad claims | Spec (Iter 16) |

**Domain:** measured systems research on local frontier inference energy/memory.

---

### 2.5 Omni stack

Treat as three related products, not one blob.

#### Omni_Framework (launcher + loader + meta + intelligence)

| Primitive | Role | Evidence |
|-----------|------|----------|
| **Vivisection dossier** | Provenance-bound analysis of prior systems | Spec + intel DB |
| **Canonical mod model** (`omni.mod.json`) | All ecosystems import *into* one model | Spec/Code |
| **Compat-layer SPI** (7 contracts) | Claim/import/rules/transform/API/shim/lifecycle | Spec |
| **Transform cache key** | SHA-256 of jar+mappings+pipeline versions | Spec |
| **Audit store** | Per-class transform history | Spec |
| **Backtracking resolver** | Dependency solution or typed unsat | Spec |
| **Partitioned transforming classloader** | Ecosystem-tagged partitions | Spec |
| **Typed `OmniIssue`** | Failure tree with remedies | Spec |
| **Instance / component stack** | Launcher truth in SQLite | Spec |
| **Job runner** | Resumable install/repair with `resume_json` | Spec |
| **Importer trait** | Detect/enumerate/import foreign instance formats | Spec |
| **Meta service artifacts** | Versioned mappings/runtime index | Code (OmniMeta) |

#### Omni32 / AssetConverter

| Primitive | Role | Evidence |
|-----------|------|----------|
| **Mod registry** | Sources, branches, jar fallbacks | Code |
| **Queue priority** | Autonomous next-mod selection | Code |
| **Upscale policy** | Size-aware xBRZ/etc. | Code |
| **Namespace merge → pack** | Multi-mod resource pack product | Code |
| **Deploy flag (off by default)** | Explicit production side-effect | Code |

#### OmniFix

| Primitive | Role | Evidence |
|-----------|------|----------|
| **Cross-mod Mixin compat patterns** | Field/method conflict surgery | Code + MixinFieldManual corpus |

**Domain:** Minecraft ecosystem unification + asset production.

---

### 2.6 Adjacent projects (high signal)

| Project | Load-bearing primitives | Domain |
|---------|-------------------------|--------|
| **JanusPrime** | Task tree, `.aether/tasks.json` SoT, worktrees, patch proposal, **validation kernel** (LSP·AST·Rules·Build), SHA receipts, workload registry, capped briefs, doctrine seed, repair loop | Mutation engine |
| **HellForge** | PTY forge, Council bus, roles (Director/Orchestrator/Executor), journals, pressure gauge, command deck | HITL control plane |
| **QuillForge** | Command → Operations → Journal → Kernel → Derived State; `.qfdoc`; document AST; unknown-content preservation; priority stack | Document OS |
| **DigiChar** | Named Tauri commands; desktopApi boundary; shunting-yard engine; localStorage persistence; Ollama loopback-only | Desktop finance tool |
| **PyMason** | Blockly block → Python generator; workspace slots; Pyodide worker execution | Visual code builder |
| **RickPrime** | Fixed registries (Atlas/Fleet/Nexus); named IPC; Sentinel metadata scan; Knowledge Forge provenance bundles; activation gates | Workstation atlas |
| **Smart-Library** | Embeddings query; Docker heal sandbox; doctrine store | Semantic memory |
| **REL** | Session state, neural concept web, MCP/REST tool surface | Cognition layer |
| **TSAM** | ModuleGraph, ActiveWindow, energy tuple (H,S,C,Q), rewrite engine | Search/optimize research |
| **AutomationLab** | Orchestrator, Work Order, Verification Ladder, Coverage Ledger, Convergence Controller, Flag, Escalation | Janus concept wiki |
| **APODE** | Research→design→list→fulfill pipeline; hard human checkpoints | POD enterprise (pre-code) |
| **StudioOps** | Protocol bus CLI, site kit, hf-bus surface | Control-plane tooling |
| **Deep Research** | Strategy genome, immutable orchestrator, canary fitness | Self-improving research |

---

## 3. Convergence clusters

Each cluster is an abstraction that **reappears** across lineages.  
**Independence** is scored as: **High** (different problem domain, different invention path), **Medium** (same studio mind, but separate products), **Low** (explicitly shared control-plane design).

### C1 — Gate before mutation

> Nothing that matters becomes canonical without a gate.

| Project | Local name | What is gated |
|---------|------------|---------------|
| AC | Section 0 / `CONST-GATE-001` | Delivery to human |
| Janus | Validation kernel + receipt | Patch apply / accept |
| Aether | Bytecode verifier | Run / forge write |
| QuillForge | Kernel + journal path only | Document state mutation |
| OmniLoader | Resolver + transform ensure | Classpath/boot |
| Recurrsive | Evidence retraction bar | Published performance claims |
| RickPrime | Activation gates | Research node “live” posture |
| Autonomous arch | Budget / division preflight | Overnight loops / spend |
| PsyForge | Ethical rating + ethics agent | Design recommendations |
| APODE | Human checkpoints | IP, ads, logistics exceptions |

**Independence:** High between Aether/QuillForge/Omni/Recurrsive; Medium–Low for Janus↔HellForge↔AutomationLab (same control-plane thesis).

---

### C2 — Capability surface (deny-by-default authority)

> Authority is named, granted, and narrow — never ambient.

| Project | Local name |
|---------|------------|
| Aether | Host/foreign grants; empty grant = pure |
| DigiChar | Tauri capabilities + named commands |
| RickPrime | Named IPC only; no generic invoke |
| HellForge | API keys confined to Electron main |
| Janus | `files_in_scope` + no ungated FS mutation |
| OmniLauncher | OS vault tokens; capability-scoped shell |
| Smart-Library / Deep Research | Docker sandbox for code execution |

**Independence:** High (desktop IPC, language host ABI, mutation engine, game launcher).

---

### C3 — Single source of truth + derived projections

> One canonical store; everything else is a view.

| Project | SoT | Projection / derived |
|---------|-----|----------------------|
| QuillForge | Journaled kernel state | Layout, render, search, UI caches |
| OmniLauncher | SQLite instances/jobs | Vue UI (holds no truth) |
| Janus | `.aether/tasks.json` | BLACKBOARD, bus status, brief views |
| AC | One-home modules + Rule Registry | Project pointers, skill loaders |
| Aether | Verified AETH + locked project/workspace | AST/edit docs, LSP diagnostics |
| HellForge | `bus.jsonl` + journals | Council UI |
| RickPrime | Fixed registries | Atlas/Fleet/Nexus UI, Knowledge Forge |
| Autonomous arch | Explicit “no second task store” | Studio status surfaces |

**Independence:** High for product kernels; Low for Janus/HellForge BLACKBOARD wiring (deliberate).

---

### C4 — Registry as first-class structure

> Identity of work units lives in a registry, not scattered folders.

| Project | Registry of |
|---------|-------------|
| AC | Rules, modules |
| Janus | Workloads + validation profiles |
| Aether | Offline package registry cache (F-REGISTRY) |
| Omni | Mods (canonical model), census, meta artifacts |
| AssetConverter | Mod sources / queue |
| RickPrime | Company / Software / AI Research roots |
| Empire root | `PROJECT-REGISTRY.md`, `WPAI-CATALOG.md` |
| PsyForge | Domain codes + REQ IDs |

**Independence:** Medium (studio pattern) with High domain variety.

---

### C5 — Content-addressed integrity / receipts

> Prove what ran or what changed with digests, not vibes.

| Project | Mechanism |
|---------|-----------|
| Janus | SHA-256 validation receipts |
| Aether | Artifact verify; workspace/project locks (SHA) |
| OmniLoader | Transform cache key + audit.json |
| OmniLauncher | Content-addressed download cache (hashes) |
| AC | `CHECKSUMS.sha256`, verify-pack |
| AssetConverter | Pipeline outputs under deterministic policy |
| Recurrsive | Results JSON + hardware signature files |

**Independence:** High.

---

### C6 — Structural authoring (edit meaning, not only text)

> Prefer typed structure over freeform string surgery.

| Project | Mechanism |
|---------|-----------|
| Aether | `aether.edit/v8` AST ops; seed-before-write |
| PyMason | Blockly graph → Python generators |
| QuillForge | Document AST + command bus ops |
| DigiChar | Shunting-yard token AST for expressions |
| Janus | Scoped full-file patch proposals (structured JSON) |
| Omni | Canonical model import from guest manifests |

**Independence:** High (language vs visual code vs documents vs patches).

---

### C7 — Bounded working set / explicit resource plan

> Never pretend the world is infinite memory or infinite context.

| Project | Bound |
|---------|-------|
| Aether | Arena capacity, buffer owners, comptime fuel 1024, task frame capacity |
| Recurrsive | VRAM working set; PCIe as hard floor |
| TSAM | ActiveWindow W_t |
| Janus | Brief/memory/context char caps |
| QuillForge | CI performance budgets |
| Smart-Library | Token-sliced retrieval |
| OmniLoader | Transform cache GC (LRU + version sweep) |

**Independence:** High — same pressure (finite machines/context) solved per domain.

---

### C8 — Structured concurrency / hierarchical work

> Work is nested, cancellable, and owns its lifetime.

| Project | Mechanism |
|---------|-----------|
| Aether | Nurseries + task frames + checkpoints |
| Janus | Parent/child tasks + repair rounds + max loops |
| HellForge / StudioOps | Director → Orchestrator → Executor roles |
| AutomationLab | Work Order, Escalation, Convergence Controller |
| OmniLauncher | Resumable jobs with interrupt prefixes |
| APODE | Multi-team pipeline with hard stops |
| PsyForge | Multi-agent design council |

**Independence:** Medium (multi-agent studio culture) with High for Aether’s language-level form.

---

### C9 — Knowledge graph / semantic memory

> Concepts are nodes; retrieval is first-class.

| Project | Graph / memory shape |
|---------|----------------------|
| PsyForge | Concept–Emotion–Outcome + relationship edges |
| Smart-Library | Embedding index + doctrine docs |
| REL | Neural concept web + session state |
| RickPrime Knowledge Forge | Provenance + declared lineage edges |
| Omni intelligence | Launcher/loader feature matrix + dossiers |
| AutomationLab | Concept nodes mapped 1:1 to Janus components |
| TSAM | Constraint/module graphs |

**Independence:** Medium–High.

---

### C10 — Simulate / measure before promote claim

> Forecast or measure offline; do not claim production truth early.

| Project | Form |
|---------|------|
| PsyForge | Engagement/churn/revenue simulation |
| Recurrsive | Energy/throughput sims + hardware proofs |
| TSAM | Annealing search over program/module state |
| Topological Hydro | Lattice/GPE physical analogs |
| Deep Research | Canary fitness on strategy genomes |
| Aether | Dual-compare seed≡bootstrap before product claim |
| AutomationLab | Verification Ladder before integration |

**Independence:** High.

---

### C11 — Bootstrap vs product authority reduction

> Ship a self-sufficient product path; keep bootstrap as oracle/recovery only.

| Project | Pattern |
|---------|---------|
| Aether | BARP: seed product path; Rust bootstrap recovery/oracle |
| AC | Portable pack + project pointer (not monorepo law dump) |
| Janus | Doctrine seed once; executors never own full doctrine dump |
| OmniMeta | Generated meta index from measured ecosystem |
| Autonomous arch | Compose existing systems; do not invent third orchestrator |

**Independence:** Medium (conscious studio design principle).

---

### C12 — Multi-layer precedence / claim discipline

> Not every statement is equal; ranks and claim grades prevent self-deception.

| Project | Mechanism |
|---------|-----------|
| AC | Safety → human → constitution → SOP → modules → project → plan |
| QuillForge | 10-point absolute priority stack (integrity first) |
| Aether | CORE_CLAIMS: Proven / Direction / Hypothesis / Prohibited |
| Recurrsive | Retraction notices; corrected baselines |
| PsyForge | MUST/SHOULD/MAY + REQ lifecycle |
| RickPrime | Evidence labels on Research Nexus nodes |
| Janus EXECUTOR | Mutation gate doctrine |

**Independence:** High as product-local law; Medium as shared WPAI epistemology.

---

### C13 — Offline / local-first product boundary

> Default trust boundary is the machine, not the cloud.

Appears in: Aether, QuillForge, DigiChar, PyMason, HellForge, Omni, RickPrime, REL/Smart-Library Docker stack, Recurrsive hardware-local measurement, Random Story Generator, XTechBot sandbox mode.

**Independence:** Low–Medium as studio policy; still reimplemented per stack (not one shared runtime).

---

### C14 — Import / canonicalize foreign ecosystems

> Ingest alien formats into an owned model; never treat foreign state as core SoT.

| Project | Foreign → owned |
|---------|-----------------|
| OmniLoader | Fabric/NeoForge manifests → `omni.mod.json` model |
| OmniLauncher | CF/Prism/Modrinth/Official → instance SQLite |
| QuillForge | docx/md/html/… ↔ `.qfdoc` |
| AssetConverter | Mod jars/sources → Omni32 pack namespaces |
| AC ADOPT | Existing repos → pack pointer |
| GitHubCodeCrawler | GitHub API → license-filtered JSONL store |

**Independence:** High.

---

### C15 — Agent/role specialization instead of monolith mind

> Multiple specialists with fixed focus beat one omniscient agent.

| Project | Roles |
|---------|-------|
| HellForge Council | Director / Orchestrator / Executor / Local |
| PsyForge | Psychology, Economy, Ethics, Designer agents |
| Janus | Orchestrator (Claude) vs Executor (Grok/Qwen) |
| APODE | 11 teams (architecture) |
| AutomationLab | Orchestrator / Executor / Escalation nodes |
| Adaptive Bosses/Attacks | Specialized combat adaptation (game domain) |

**Independence:** Medium.

---

## 4. Convergence matrix (compact)

Rows = abstractions. Columns = major projects.  
`●` = strong primitive present · `○` = partial / adjacent · blank = absent or N/A

| Abstraction | AC | Aether | PsyForge | Recurrsive | Omni | Janus | QuillForge | HellForge | RickPrime |
|-------------|:--:|:------:|:--------:|:----------:|:----:|:-----:|:----------:|:---------:|:---------:|
| Pre-mutation gate | ● | ● | ○ | ● | ● | ● | ● | ○ | ● |
| Capability grants | ○ | ● | | | ● | ● | ○ | ● | ● |
| SoT + projections | ● | ● | ○ | | ● | ● | ● | ● | ● |
| Registry of units | ● | ● | ● | | ● | ● | ○ | ○ | ● |
| Digest / receipts | ● | ● | | ● | ● | ● | ○ | ○ | ○ |
| Structural edit | ○ | ● | | | ● | ● | ● | | ○ |
| Bounded resources | ○ | ● | | ● | ● | ● | ● | | |
| Hierarchical work | ○ | ● | ● | ○ | ● | ● | ○ | ● | ○ |
| Knowledge graph | ○ | | ● | | ● | ● | | | ● |
| Sim-before-claim | ○ | ● | ● | ● | ○ | ○ | | | ○ |
| Bootstrap reduction | ● | ● | | | ● | ● | | | ○ |
| Claim/precedence law | ● | ● | ● | ● | ● | ● | ● | ○ | ● |
| Local-first | ● | ● | ○ | ● | ● | ● | ● | ● | ● |
| Foreign canonicalize | ● | ○ | | | ● | ○ | ● | | ○ |
| Multi-agent roles | ● | | ● | | | ● | | ● | ○ |

---

## 5. Deep convergences worth productizing later

These are the strongest *studio-wide* abstractions that currently re-solve the same problem under different names. Candidates for a shared vocabulary (not necessarily a shared library — Rule of Three still applies).

### 5.1 The Gate Monad

**Pattern:** `propose → validate → receipt → commit | reject → (optional) learn`

| Lineage | Instance |
|---------|----------|
| Law | Section 0 |
| Code mutation | Janus validation kernel |
| Language runtime | Aether verifier |
| Documents | QuillForge journal apply |
| Loader | Omni transform+resolve |
| Research | Recurrsive evidence bar |

**Insight:** WPAI’s real unit of progress is not “a file changed” but “a gated transition.”

### 5.2 The Capability Envelope

**Pattern:** default zero authority; expand only via named grants with typed effects.

Aether grants, Tauri/Electron IPC allow-lists, Janus scope lists, and Omni vault refs are the same security geometry on different substrates.

### 5.3 The Canonical Kernel

**Pattern:** one mutable core; all UX/search/telemetry are pure functions of that core plus caches.

QuillForge states it most clearly; OmniLauncher and Janus enforce it operationally; AC enforces it for *law text*.

### 5.4 The Bounded Window

**Pattern:** compute only inside an explicit working set; spill or stream the rest.

Aether arenas, Recurrsive host-streaming, TSAM ActiveWindow, Janus brief caps — four domains, one finitude law.

### 5.5 The Structural Surface for AI

**Pattern:** expose a versioned structural API so agents edit meaning under a verifier, not raw text under hope.

Aether authoring protocol is the purest form; PyMason and QuillForge are domain siblings; Janus patch JSON is the industrial form.

### 5.6 The Honest Claim Lattice

**Pattern:** statements carry grade (proven / direction / hypothesis / retracted) and never float.

Aether CORE_CLAIMS, Recurrsive retractions, RickPrime evidence labels, PsyForge MUST/SHOULD/MAY, AC Rule IDs — same epistemology.

---

## 6. What is *not* convergent (important negatives)

| Tempting collapse | Why it is wrong |
|-------------------|-----------------|
| Aether `weave` ≡ Janus task | Weave is language function+ownership; task is multi-agent work unit with validation profile |
| PsyForge graph ≡ Smart-Library | One is domain ontology for behavior; the other is code-memory retrieval |
| Omni32 ≡ OmniLoader | Asset pipeline product vs runtime mod loader |
| AC Section 0 ≡ Aether verifier | Process gate for human delivery vs machine gate for bytecode safety |
| HellForge Council ≡ PsyForge Design Agents | Operator multi-agent bus vs product-domain evaluation personas |
| Recurrsive streaming ≡ Aether arenas | Hardware memory movement vs language ownership regions |
| RickPrime registries ≡ Janus workload registry | Read-only atlas/discovery vs mutation-allowed workload identity |

False merges would erase the boundaries that keep the empire operable.

---

## 7. Independence map (who invented what)

```
                    ┌─────────────────────────┐
                    │   Shared epistemology   │
                    │  (gates, claims, SoT)   │
                    │  AC + studio practice   │
                    └───────────┬─────────────┘
                                │ inherited by many
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
 ┌──────────────┐      ┌──────────────┐        ┌──────────────┐
 │ Language OS  │      │ Mutation OS  │        │ Document OS  │
 │ Aether       │      │ Janus+REL    │        │ QuillForge   │
 │ verifier,    │      │ validation   │        │ journal,     │
 │ weaves,      │      │ kernel,tasks │        │ kernel       │
 │ grants       │      └──────┬───────┘        └──────────────┘
 └──────────────┘             │
        │                     │ control plane
        │                     ▼
        │              ┌──────────────┐
        │              │ HITL shell   │
        │              │ HellForge    │
        │              │ + StudioOps  │
        │              └──────────────┘
        │
        ▼
 ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
 │ Game ecosys  │   │ Behavioral   │   │ Energy/mem   │
 │ Omni*        │   │ PsyForge     │   │ Recurrsive   │
 │ canonicalize │   │ traits+graph │   │ stream+MoE   │
 └──────────────┘   └──────────────┘   └──────────────┘
```

**Independent invention cores**

1. **Aether language semantics** (resources/effects/seed) — unique  
2. **Recurrsive measurement stack** — unique research lineage  
3. **Omni vivisection→canonical loader** — unique product lineage  
4. **QuillForge document kernel constitution** — unique product lineage  
5. **PsyForge behavioral ontology** — unique product lineage  
6. **Janus validation-gated mutation** — unique *as implementation* (concept shared with AutomationLab wiki)

**Shared cultural law** (not independent): completeness, zero warnings, human sovereignty, local-first, no second task store.

---

## 8. Primitive dictionary (crosswalk)

Use this when talking across projects without false synonymy.

| Studio concept | AC | Aether | Janus | QuillForge | Omni | PsyForge | Recurrsive |
|----------------|----|--------|-------|------------|------|----------|------------|
| Atomic unit of work | Rule / module | Weave | Task | Command | Job / resolve set | DesignAgent query | Iteration |
| Canonical state | Pack modules | Verified AETH | tasks.json + workload git | Kernel journal | SQLite + mod model | Graph + models | Results JSON + model weights layout |
| Gate | Section 0 | Verifier | Validation kernel | Kernel apply rules | Resolver/transform | Ethics/rating | Measurement validity |
| Memory bound | Constrained-hardware module | Arena/frame capacity | Brief caps | Perf budgets | Transform cache | (implicit UI) | VRAM working set |
| Authority | Level 1–4 + grants of override | Host grants | files_in_scope | Priority stack | Vault + capabilities | REQ lifecycle | Hardware truth over narrative |
| Learning store | Institutional memory module | Dual-compare corpus | Smart-Library seeds | (plugins/search later) | Intelligence DB | Psychology corpus | Plots + retracted logs |
| Failure type | Gate FAIL | Diagnostic codes | Typed validation errors | Recovery paths | OmniIssue | Ethical High risk | Retraction |

---

## 9. Highest-leverage next steps (if unifying)

Not a mandate — options ranked by “reduce re-solving without collapsing domains.”

1. **Shared Gate vocabulary** — document the Gate Monad as a studio pattern (propose/validate/receipt/commit) citing AC, Janus, Aether, QuillForge, Omni. No shared code required.  
2. **Shared Claim grades** — align RickPrime evidence labels with Aether CLM statuses and Recurrsive retraction language.  
3. **Registry schema family** — document common fields (`id`, `path`, `status`, `gate`, `evidence`) across PROJECT-REGISTRY, Janus workloads, RickPrime nexus.  
4. **Do not unify runtimes** — Aether VM, Omni classloader, QuillForge kernel, and Janus loop should remain separate engines with a common *philosophy*, not a common binary.  
5. **Rule of Three enforcement** — extract a shared library only when a third concrete implementation demands it (CONST culture already says this).

---

## 10. Source anchors

| Project | Primary anchors read |
|---------|----------------------|
| AC | Historical root and SOP in the preserved source revision below; current law uses the canonical source, not these research anchors |
| Aether | `Software/XLang/README.md`, `docs/ARCHITECTURE.md`, `docs/CORE_CLAIMS.md` |
| PsyForge | `Software/psyforge/DESIGN.md`, `src/types/index.ts`, master TOC |
| Recurrsive | `CURRENT_ARCHITECTURE.md`, `RECURSIVE_STATE.md` |
| Omni | `Omni_Framework/README.md`, `OmniLoader/ARCHITECTURE.md`, `OmniLauncher/ARCHITECTURE.md` |
| Janus | `JanusPrime-Overview.md`, `AUTONOMOUS-AI-ARCHITECTURE.md` |
| QuillForge | `README.md` (command/journal/kernel law) |
| HellForge | `README.md` |
| RickPrime | `ARCHITECTURE.md` |
| DigiChar | `docs/ARCHITECTURE.md` |
| PyMason | `PYMASON_VISION.md` |
| Catalog | `WPAI-CATALOG.md`, `PROJECT-REGISTRY.md` |

Historical recovery (not active law): `git show 3b0eacf8f3cbefbcad4c8395d324824db1919ba3:AGENTS Constitution/AGENTS.md`

---

## 11. One-sentence thesis

**WPAI’s projects independently rediscover the same six geometric laws — gate before commit, capability envelopes, single truth with projections, registries of units, bounded working sets, and graded claims — then specialize them into a language OS (Aether), a mutation OS (Janus), a document OS (QuillForge), an ecosystem unifier (Omni), a behavioral mind (PsyForge), and an energy-truth campaign (Recurrsive), all under a portable quality constitution (AC).**
