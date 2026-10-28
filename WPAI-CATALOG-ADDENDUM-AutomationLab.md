# WPAI Catalog — AutomationLab Addendum
**Generated:** 2026-07-30  
**Merge into:** `WPAI-CATALOG.md` under Division 5 — AI Research  
**Status:** Previously uncataloged — missed in original pass.

---

## AutomationLab
**Path:** `C:\WPAI\AI-Research\AutomationLab\`  
**Governance routing corrected 2026-10-18:** Use AutomationLab's project entry and the canonical [WPAI Constitution](https://github.com/MrWizard94-Compile/Agents-Constitution) through `wpai-constitution`. The former local-pack binding is historical, not current authority. Other catalog observations remain dated evidence.  
**Discovered via:** Obsidian vault stats — held the most cross-linked notes in the empire (9 inlinks each on Orchestrator and EXECUTOR.md).

AutomationLab is the **conceptual origin and living specification** for the JanusPrime execution architecture, scoped specifically to the Astral Sorcery port project. It contains two sub-projects with distinct purposes.

---

### Sub-project 1 — Automation Architecture
**Path:** `AutomationLab/Automation Architecture/`  
**Type:** Obsidian knowledge wiki (has its own `.obsidian/` vault config)  
**Purpose:** Canonical component-level specification of the autonomous mod-porting system, documented as a set of tightly interlinked concept nodes. Every node is a single responsibility — no prose, no ambiguity.

**Relationship to JanusPrime:** This IS the JanusPrime spec as applied to the Astral Sorcery port. The architectural vocabulary here (Orchestrator, Executor, Work Order, etc.) maps 1:1 onto the Janus implementation:

| AutomationLab Concept | JanusPrime Reality |
|-----------------------|--------------------|
| Orchestrator | Claude (via `janus.config.json` doctrine injection) |
| Executor | Grok Build (`grok-build`, headless, `bypassPermissions`) |
| MCP | HellForge bus + `Project-Janus/packages/mcp-server/` |
| Work Order | `.aether/tasks.json` task entries |
| Smart Library | `AI-Research/Janus/Smart-Library/` (ChromaDB + Ollama) |
| REL | `AI-Research/REL_Codex_Variant/` (FastAPI + ChromaDB) |
| Reference Source | Frozen 1.16.5 Astral Sorcery clone at `.claude/reference/` |
| Asset Converter | `AI-Research/AssetConverter/` (Omni32 pipeline) |
| Verification Ladder | Real Gradle gate sequence (compile → Checkstyle → SpotBugs → datagen → unit → GameTest → client-boot → build) |
| Coverage Ledger | 100% Port Manifest accounting — no silent drops |
| Convergence Controller | Max-attempt circuit breaker in orchestrator logic |
| Escalation | HITL handoff to Director (Rob) via HellForge bus |

**Architecture nodes** (each a single `.md` file, all wiki-linked):

| Node | One-line responsibility |
|------|------------------------|
| `Orchestrator.md` | Follows CLAUDE doctrine; builds Port Manifest; decomposes into Work Orders via MCP; reconciles Coverage Ledger; integrates through Integration Gate; routes Escalation to User |
| `Executor.md` | Transforms source per Work Order using Smart Library transforms against Reference Source oracle; sends output to AST_LSP; memory of prior Flags prevents re-shipping rejected fixes |
| `Work Order.md` | Unit contract: scope, phase, dependencies, acceptance gates, Smart Library references, DoD, bounded attempts; executed by Executor, verified by AST_LSP; attempt count feeds Convergence Controller |
| `AST_LSP.md` | QA gate: runs Verification Ladder **fail-closed**; emits structured Flags to Executor; passes only all-green output to Orchestrator |
| `MCP.md` | Transport/dispatch bus — not a decision node; carries Work Orders down and Flags/output up; exposes AST_LSP gate tooling as callable MCP/CLI tools |
| `Port Manifest.md` | Complete inventory of Reference Source — every registry object, class, asset, data file with dependency graph; basis for Work Order decomposition; every artifact appears exactly once |
| `Flag.md` | Structured rejection from AST_LSP: which gate, file, symbol, raw diagnostic, category, suggested Smart Library transform; drives Executor revision; feeds Convergence Controller |
| `Escalation.md` | Precise actionable handoff to User/Director when Convergence Controller cannot converge or dependency wall hit; carries failing Flags; logged to REL |
| `Convergence Controller.md` | Bounds Executor↔AST_LSP loop with max attempts and global circuit breaker; routes Escalation on exhaustion; fail-safe by construction |
| `Coverage Ledger.md` | Reconciles 100% of Port Manifest entries at delivery: each is `passed` or `deferred` with justification and Escalation record; enforces no silent drops; delivery refused while any entry is `pending` or `in_progress` |
| `Verification Ladder.md` | Ordered fail-closed gate sequence: compile → Checkstyle → SpotBugs → datagen-validate → unit → GameTest → client-boot → Integration Gate; each rung is real tooling, not opinion; first failure emits Flag and stops |
| `Integration Gate.md` | Whole-assembly verification (full `build`, all GameTests) after per-unit Work Orders pass; clears integrated output for Orchestrator delivery |
| `Smart Library.md` | Cognition for Orchestrator: evidence-backed catalog of 1.16.5→1.20.1 transforms plus Reference Source oracle; each entry carries gate proof; refined on write-back from accepted Work Orders |
| `REL.md` | Durable memory: decisions, outcomes, escalations, Transform Record provenance; write-back on every acceptance; persists under port repo `.claude/` |
| `Reference Source.md` | Frozen 1.16.5 source tree (`.claude/reference/AstralSorcery-1.16`) — behavioral/parity oracle; consulted by Smart Library and Executor; scanned to build Port Manifest |
| `Asset Converter.md` | Tool for Executor: migrates non-code artifacts (models, blockstates, recipes/loot→datagen JSON, lang, sounds, textures); output gated by datagen `--validate` rung of Verification Ladder |
| `Transform Record.md` | Per-artifact provenance on acceptance: Work Order, source→target, Smart Library transforms applied, passing gate run, content hash; reproducible audit, stored in REL |
| `User.md` | Director: sends Prompt to Orchestrator; final approval authority; endpoint for Escalation; accepted gate-verified output and unresolved Flags surface here — closes the loop back to human |

**References directory** (`references/`) — cognition seed for the Smart Library node. Verified knowledge base for the 1.16.5 → 1.20.1 Astral Sorcery port:

| File | Contents |
|------|---------|
| `README.md` | How to use the references: conceptual map only — exact signatures always resolved against live MDK and AST_LSP compile gate, never hand-copied from memory |
| `forge-1.16.5-to-1.20.1-deltas.md` | Master rename/registration/data table: type renames (CompoundNBT→CompoundTag, World→Level, etc.), registration backbone changes (DeferredRegister), Block/Item traps (Material removed in 1.20), Capabilities (stays Forge-style), Networking (SimpleChannel stays — not CustomPacketPayload), Tags, Lifecycle/Mixins/AT, Java 8→17 |
| `rendering-and-gui.md` | PoseStack, GuiGraphics, BlockEntityRenderer, shader-based draws — highest visual-parity risk |
| `worldgen-1.16-to-1.20.md` | Configured/placed features + BiomeModifiers — largest single delta |
| `optional-integrations.md` | JEI, Curios, ObserverLib, Patchouli, Botania, CraftTweaker, Tombstone |
| `toolchain-and-gates.md` | Exact Gradle tasks the Verification Ladder (AST_LSP) invokes |

**Toolchain (from `toolchain-and-gates.md`):**  
ForgeGradle `[6.0,6.2)` · Java 17 · official/Mojmap mappings · MC 1.20.1 · Forge 47.3.0 · Mixin 0.8.5

**Verification Ladder gate sequence:**

| # | Gate | Gradle task | Policy |
|---|------|-------------|--------|
| 1 | Compile | `compileJava` | `-Xlint:unchecked` + `-Xlint:rawtypes` · any error fails |
| 2 | Checkstyle | `checkstyleMain` | v10.17.0 · `ignoreFailures=false` |
| 3 | SpotBugs | `spotbugsMain` | v4.8.6 · `ignoreFailures=false` |
| 4 | Asset/schema | `runData` | `--all --validate --existing` |
| 5 | Unit | `test` | JUnit 5 |
| 6 | GameTest | `runGameTestServer` | `forge.enabledGameTestNamespaces=astralsorcery` |
| 7 | Client-boot | `runClient` | Needs auto-quit/timeout harness |
| 8 | Integration | `build` | Full assembly: gates 1–3 + test |

**Critical "over-porting" warning documented in references/README.md:**  
This port targets **1.20.1, NOT 1.20.5+/NeoForge**. Therefore: NBT stays (`CompoundTag` alive), Forge capabilities stay (`LazyOptional` + `ICapabilityProvider`), `SimpleChannel` networking stays. DataComponents, attachment system, and `StreamCodec` are 1.20.5+/NeoForge — explicitly forbidden. Over-porting these is the classic way to wreck a 1.20.1 codebase.

---

### Sub-project 2 — Agent Smith
**Path:** `AutomationLab/Agent Smith/`  
**Type:** Obsidian vault (has its own `.obsidian/` vault config)  
**File:** `Agent_Smith.md` — a single long document  
**Purpose:** Conceptual design conversation capturing the original creative session that produced the "Agent Smith Project" vision — a far more ambitious AI-driven universal mod porting architecture.

**What it is:** A transcript of a design conversation (with Grok or similar AI, likely pre-JanusPrime) where Rob designed a novel **3D Hexagonal Cyclone Neural Network** architecture for autonomously porting 50% of the 1.12–1.16 Minecraft modding ecosystem to 1.21 NeoForge. The conversation covers:

- 16×16 → 256×256 → 4× 64×64 grid architecture evolution
- 3D Hexagonal Close-Packed (HCP) lattice as the computational substrate
- Cyclone/vortex data routing (centripetal noise filtering, angular propagation)
- Four specialized sub-models: Logic Engine (Java 8→21), Registry Core (NBT→DataComponents), Asset Whisperer (JSON/textures), Data Synthesizer (worldgen/datapacks)
- Why 4× 64×64 beats one 256×256 (GPU symmetry, cross-mod latent vector alignment, automatic conflict resolution)
- Pre-harmonized CurseForge releases under the "Agent Smith Project" banner with full original author credits
- The philosophy: quality over speed, open-source craftsmanship, free mods always
- 2026 AI landscape assessment — how Claude Opus 4 + Grok Build + native multi-agent orchestration makes this executable now

**Status:** Conceptual / research artifact. Not yet implemented. JanusPrime (current system) is the practical realization of a subset of these ideas — it handles the Astral Sorcery port specifically with the same Orchestrator/Executor/Verification pattern, but not the universal mass-porting vision. Agent Smith remains the longer-horizon goal.

**Key design insight captured:** The 4× 64×64 symmetry means all mods are processed through the same geometric coordinate system → their internal vector spaces become standardized → they natively resolve registry conflicts without compatibility patches → compatibility patches become structurally impossible, not just avoidable.

**The "magnum opus" framing:** Port 50%+ of the 1.12–1.16 modding ecosystem to 1.21 NeoForge, release each as standalone pre-harmonized open-source mods on CurseForge with full original author credits. Start with Essential Utility & QoL mods (small code footprint, fast iteration, immediately embeds into every player's game).

---

## Updated Summary Statistics (post-AutomationLab)

| Metric | Previous | Updated |
|--------|---------|---------|
| AI Research projects (distinct) | 11 | **12** |
| Obsidian vaults nested within WPAI | 0 documented | **2** (AutomationLab/Automation Architecture, AutomationLab/Agent Smith) |
| Janus spec documented | Partial | **Complete** — Automation Architecture is the canonical spec |

---

## Cross-Reference Notes

- `AI-Research/Janus/EXECUTOR.md` (9 inlinks in vault graph) — referenced by this spec as the Grok Build doctrine document
- AutomationLab is the **design-time documentation** layer for JanusPrime, which is the **runtime implementation** layer
- The Agent Smith vision extends JanusPrime's scope from "port Astral Sorcery" to "port 50% of the 1.12–1.16 ecosystem universally"
- The `references/` knowledge base feeds the actual Smart Library at `AI-Research/Janus/Smart-Library/`
