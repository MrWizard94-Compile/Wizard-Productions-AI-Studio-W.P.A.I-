# Constrained Hardware and Cost

```
Document: Constrained Hardware and Cost
Module ID: MOD-SPC-HW-001
Version: 1.2.0
Status: Binding
Authority: AGENTS.md
Applies When: Limited RAM/CPU/GPU, cognitive-load packaging, high compute/token cost, repeated agent context
Dependencies:
  - AGENTS.md
  - standards/PERFORMANCE.md
  - standards/SECURITY.md
  - collaboration/REVIEW-PACKAGING.md
Overrides: None
```

---

## HW-RESPECT-001 — Real Constraints

Design with real constraints:

* Hardware (GPU VRAM, RAM, CPU, storage)  
* Economic (prefer free/open/offline tools)  
* Cognitive (ADHD/ODD/AuDHD, hyperfocus windows, context switching)  
* Time and energy  

## HW-MEM-001 — Allocation Discipline

* Minimize allocations in hot paths.
* Prefer object reuse, primitive arrays, and stack patterns where safe and clear.
* Document expected peak memory for new subsystems.
* Avoid large temporary collections that cause GC or memory pressure.
* Prefer streaming / incremental algorithms over “load everything” for large datasets.
* Profile under realistic constrained conditions when introducing heavy systems.

## HW-ALT-001 — Lighter Alternatives

* When a solution has high resource cost, document the cost and provide a lighter alternative if feasible.
* Prefer algorithms that degrade gracefully under constrained hardware.
* Never assume high-end workstations or unlimited cognitive bandwidth.

## COST-TOKEN-001 — Token and Compute Economics

* Be conscious of AI tokens, GPU compute, storage, and human review time.
* Prefer solutions that minimize future token burn (docs, self-contained deliveries, selective module loading).
* For repeated stable context, use the bounded agent working cache required by `COST-CACHE-001`; do not repeatedly reload the same verified facts without a freshness reason.
* High compute tasks: document expected cost; seek confirmation if large.
* Optimize for long-term empire economics, not only the current conversation.

## COST-CACHE-001 — Bounded Agent Working Cache

* When a task repeatedly consults stable, non-sensitive context, the AI must save the minimum sufficient verified working set in its available task-local cache and actively reuse that cache for repeated decisions.
* Cache only compact facts that are safe and useful to reuse: selected source paths, version/identity values, declared invariants, bounded limits, completed command evidence, and the current validation plan. The canonical file, command output, remote state, or human instruction remains the source of truth.
* Revalidate or invalidate cached facts after a relevant file mutation, VCS/network state change, new human direction, workspace switch, cache mismatch, or before an irreversible action, publication, or completion claim. A cache hit is never evidence that mutable external state is still current.
* Keep caches task-scoped and bounded. Do not cache secrets, credentials, tokens, raw sensitive user data, or unrelated repository contents. Do not turn an agent working cache into product persistence, a hidden build input, or an ambient authority channel (`SEC-SECRET-001`, `SEC-INPUT-001`).
* Record cache use only when it materially affects the delivery or an audit. The rule exists to reduce repeated token/compute use without weakening research, verification, reproducibility, or human oversight.

---

*Canonical home for hardware, cognitive, and cost constraints.*
