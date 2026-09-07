---
name: agents-constitution
description: >
  Load and enforce the AGENTS Constitution portable pack: quality law (AGENTS.md),
  process law (SOP.md), Section 0 pre-delivery gate, Definition of Done, module
  applicability matrix, and pack tools (verify-pack / self-audit / full self-run).
  Use when the user runs /agents-constitution, asks to apply the constitution,
  run Section 0 / pre-delivery gate, package a production delivery under WPAI law,
  adopt the pack into a project, or run the pack against itself (self-audit,
  verify-pack, full constitution self-run). Also use for WPAI empire delivery work
  that must satisfy CONST-GATE-001 and CONST-DONE-001.
metadata:
  short-description: "Enforce AGENTS Constitution pack"
  pack-version-pin: "5.0.1"
---

# AGENTS Constitution

This skill is the **loader and enforcer**. Binding rules live only in the pack
(`CONST-ONEHOME-001`). Do **not** restate full modules here. Read pack files;
cite Rule IDs.

## Modes

Infer mode from the user message / slash args. First match wins.

| Mode | Triggers | Goal |
|------|----------|------|
| `self-run` | "against itself", self-audit, verify pack, full self-run, `self-run` | Run pack tools on the pack root |
| `gate` | Section 0, pre-delivery gate, gate check, `gate` | Score current work against the 15-point gate |
| `adopt` | adopt, point project, install pack, `adopt` | Attach a project to the pack per ADOPT.md |
| `enforce` | default; delivery, implement, ship, package | Load law and bind the entire task |

## Step 0 — Resolve pack root

Discovery order (stop at first **valid** pack):

1. Env vars `AGENTS_CONSTITUTION_ROOT` or `WPAI_CONSTITUTION` (if set)
2. Optional local pin: read `references/pack-root.local` next to this SKILL.md (one absolute path, one line; may be absent)
3. Walk **up** from the workspace path and from the current working directory
4. Check siblings of those walk stops for folders named `AGENTS Constitution` or `AGENTS-Constitution`
5. Run `scripts/resolve-pack.ps1` (same discovery; use its stdout path)

A path is **valid** only if all exist relative to it:

- `VERSION`
- `AGENTS.md` (must mention `CONST-GATE-001`)
- `SOP.md`
- `tools/verify-pack.ps1`

Store as `PACK_ROOT`. If none resolve: **stop and ask the human** for the pack path. Do not invent law.

Prefer pack-relative paths in any pack edits (`GOV-PORT-001`). Absolute paths are fine only in local pin files and diagnostics under `reports/`.

## Step 1 — Always-load set

Read these files from `PACK_ROOT` (and project Level-4 pointer if present) before substantive work:

1. Project-root `AGENTS.md` **if** it is a Level-4 pointer into this pack (see `templates/PROJECT-POINTER.template.md`)
2. `AGENTS.md` (SOUL — Section 0 gate lives here)
3. `SOP.md`
4. `constitution/03-DEFINITION-OF-DONE.md`
5. `standards/ENGINEERING.md`
6. `standards/TESTING.md`
7. `standards/DOCUMENTATION.md`

Then load additional modules from the **applicability matrix** in pack `AGENTS.md` for the task type. When unsure, load the candidate module.

Quick load shortcuts (signals → module under `PACK_ROOT`):

| Signal | Module |
|--------|--------|
| Untrusted input, auth, secrets | `standards/SECURITY.md` |
| Delivery / handoff | `operations/DELIVERY.md`, `collaboration/REVIEW-PACKAGING.md` |
| Release / ship | `operations/RELEASES.md` |
| Multi-agent | `collaboration/MULTI-AGENT.md` |
| Refactor | `operations/REFACTORING.md` |
| Novel R&D / invention | `specialist/NOVEL-RND.md`, `specialist/IP-AND-INVENTION.md` |

Catalog: `RULE-REGISTRY.md`, `MODULE-INDEX.md`.

## Step 2 — Mode procedures

### Mode: `enforce` (default)

1. Complete Step 0–1.
2. Follow `SOP.md` phases appropriate to scope (human may truncate scope; quality gates do not auto-waive).
3. Implement fully: no stubs, no TODO ship, dependency-first (`CONST-COMPLETE-001`, `CONST-DEP-001`).
4. Before presenting anything to the human, execute **Mode: `gate`** and pass all applicable items.
5. Package the handoff per `collaboration/REVIEW-PACKAGING.md` (`REV-PACK-001`).

### Mode: `gate`

1. Resolve `PACK_ROOT`; re-read Section 0 in pack `AGENTS.md` (canonical 15-point checklist).
2. For the **current deliverable** (diff, new files, or named package), score each of the 15 items: PASS / FAIL / N/A (with reason).
3. N/A is allowed only as pack hardening notes allow (e.g. IP / multi-agent when truly absent; pure internal docs for some security items). Record N/A in the self-audit log.
4. Any applicable FAIL → **stop-ship**. Remediate; do not present partial work as done.
5. Emit a short self-audit log (3–12 lines): what was verified, N/As, residual doubt.

### Mode: `self-run`

Run tools against `PACK_ROOT` (PowerShell). Prefer explicit `-PackRoot`:

```powershell
pwsh -File "$PACK_ROOT/tools/verify-pack.ps1" -PackRoot "$PACK_ROOT"
pwsh -File "$PACK_ROOT/tools/self-audit.ps1" -PackRoot "$PACK_ROOT"
pwsh -File "$PACK_ROOT/tools/run-full-constitution-self.ps1" -PackRoot "$PACK_ROOT"
```

Optional release aid:

```powershell
pwsh -File "$PACK_ROOT/tools/write-checksums.ps1" -PackRoot "$PACK_ROOT"
```

Expected: all invoked tools exit **0**. Reports land under `PACK_ROOT/reports/` (not law). Summarize PASS/FAIL with report paths. If verify-pack fails, treat as stop-ship for pack integrity (`GOV-INT-001`).

When the skill **itself** is being authored or changed: run `self-run` on the pack **and** `gate` on the skill files (dogfood).

### Mode: `adopt`

1. Read `ADOPT.md` and `templates/PROJECT-POINTER.template.md`.
2. Choose Option A/B/C per human preference (default: shared pack + project pointer).
3. Write/update project-root pointer with **relative** pack path only.
4. Run `verify-pack.ps1` on the pack (exit 0).
5. Tell agents: load project pointer → pack always-load set → matrix modules.

## Hard constraints (do not restate full text)

These cannot be silently waived by skill convenience or casual human "just ship it" without a filled project override (`templates/PROJECT-OVERRIDE.template.md`, `GOV-OVR-001`):

- `CONST-GATE-001` — Section 0 before delivery
- `CONST-COMPLETE-001` / `CONST-DEP-001` — no partial / dependency-first
- `CONST-DONE-001` — Definition of Done
- `ENG-WARN-001` — zero warnings; no silent suppressions
- `TEST-BEHAVIOR-001` — tests against intended behavior
- `SEC-INPUT-001` / `SEC-SECRET-001` — validation and secrets hygiene

Authority order: safety/legal → explicit human instruction (still cannot silent-waive the above) → pack SOUL → SOP → modules → project law → task plans. Full text: `constitution/01-AUTHORITY-AND-PRECEDENCE.md`.

Pack amendments: `LOCK.md` — complete file replacements, version bump, verify-pack green. This skill is a **non-law Grok interface**; changing skill files does not amend constitution modules unless the human also directs pack law edits.

## Delivery packaging minimum

When presenting work under this skill, include at least:

1. What / why (one sentence)
2. MANIFEST of changed paths (`templates/MANIFEST.template.md`)
3. How to verify (exact commands + expected exit)
4. Section 0 self-audit confirmation
5. Suggested commit message(s) if git applies
6. Next actions for the human

## Anti-patterns

- Copying long constitution text into SKILL.md or project docs (breaks one-home)
- Hardcoding host paths into pack binding law
- Marking gate items N/A to skip real work
- Shipping with TODOs, stubs, or "polish later"
- Editing LOCKED pack law without explicit human amendment request
