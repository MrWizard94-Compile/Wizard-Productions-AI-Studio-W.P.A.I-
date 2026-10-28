# MANIFEST — WPAI Portfolio Census and Finishing Ledger

**Delivery title:** WPAI software-first finishing program  
**Date:** 2026-09-08  
**Author:** Codex  
**Related Rule IDs:** CONST-GATE-001, CONST-DONE-001, REV-PACK-001

## Summary

A bounded, source-fingerprinted census and human-readable finishing ledger now
separate portfolio presence from verified production-grade and studio-grade
completion.

## Files

| Path | Purpose | New / Modified |
| --- | --- | --- |
| `docs/portfolio/README.md` | Start-here path and evidence semantics | New |
| `docs/portfolio/SOFTWARE-FINISHING-LEDGER.md` | Two-part quality bar, 28-project software order, and current execution target | New |
| `docs/portfolio/collect_inventory.py` | Bounded local census with path, reparse, Git-ownership, and source-fingerprint controls | New |
| `docs/portfolio/test_collect_inventory.py` | Negative and boundary tests for the census | New |
| `docs/portfolio/inventory-2026-09-08.json` | Generated current-state census evidence | New |
| `docs/portfolio/MANIFEST.md` | Delivery inventory | New |
| `docs/portfolio/DELIVERY-REPORT.md` | Verification and Rule ID self-audit | New |

## Verification

See `DELIVERY-REPORT.md` for exact commands and results.

## Risks / Trade-offs

- The census deliberately does not execute 76 project build and runtime gates.
- Existing working-tree changes are recorded but neither attributed nor altered.
- Missing and unregistered paths require registry reconciliation after project ownership is verified.

## Next actions for human

1. Review the software order and the two-part completion bar.
2. Review the RepoForge 1.1.0 local release receipt when its gate finishes.

