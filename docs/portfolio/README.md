# WPAI Portfolio Finishing Program

This directory is the source-linked operating record for turning WPAI projects
into finished products. It complements the company registry; it does not replace
project-local specifications, tests, release records, or the canonical
[WPAI Constitution](https://github.com/MrWizard94-Compile/Agents-Constitution).
Use `wpai-constitution` through the root entry; this directory is not law.

## Start here

1. Read [`../../AGENTS.md`](../../AGENTS.md),
   [`../../WPAI-CONTEXT.md`](../../WPAI-CONTEXT.md), and
   [`../../WPAI-ROADMAP.md`](../../WPAI-ROADMAP.md).
2. Read [`SOFTWARE-FINISHING-LEDGER.md`](SOFTWARE-FINISHING-LEDGER.md) for the
   director-selected software-first order and the two-part quality bar.
3. Use [`inventory-2026-09-08.json`](inventory-2026-09-08.json) for current
   bounded census evidence. Regenerate it with:

   ```powershell
   python -X utf8 .\docs\portfolio\collect_inventory.py `
     --root C:\WPAI `
     --output C:\WPAI\docs\portfolio\inventory-2026-09-08.json
   ```

4. Enter one project at a time through its local `AGENTS.md`, README, product
   specification, architecture, and current Git state. A census record never
   certifies build health or product readiness.

## Evidence rules

- **Verified** means a dated current-state command, inspected artifact, or live
  workflow proves the claim at the same scope.
- **Declared** means a project source states the claim but it has not been
  independently revalidated in the current finishing pass.
- **Blocked** identifies an exact missing decision, dependency, ownership
  boundary, or external action.
- **Unknown** stays unknown. Absence of a failure is not evidence of readiness.

The raw inventory records paths, source fingerprints, declared check commands,
and independent Git metadata. It deliberately excludes source contents,
credentials, runtime data, dependency trees, archives, and build execution.

