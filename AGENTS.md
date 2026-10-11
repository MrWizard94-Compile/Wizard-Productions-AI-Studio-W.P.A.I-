# AGENTS — Project Entry Point (WPAI-root)

**Status:** Level 4 pointer  
**Canonical source:** https://github.com/MrWizard94-Compile/Agents-Constitution  
**Repository:** `MrWizard94-Compile/Agents-Constitution` (`main`)  
**Skill:** `wpai-constitution`

This file does **not** duplicate the constitution. Binding law lives in the GitHub
repository. Generated skill mirrors and other local copies are distributions only.

---

## Binding source (Level 1–3)

| Role | Location |
|------|----------|
| **Canonical repository** | https://github.com/MrWizard94-Compile/Agents-Constitution |
| **Skill (loader / enforcer)** | [SKILL.md](https://github.com/MrWizard94-Compile/Agents-Constitution/blob/main/SKILL.md) |
| **Source identity** | [SOURCE.json](https://github.com/MrWizard94-Compile/Agents-Constitution/blob/main/SOURCE.json) |
| **Version** | [VERSION](https://github.com/MrWizard94-Compile/Agents-Constitution/blob/main/VERSION) |
| **Always-load pointer** | [references/always-load.md](https://github.com/MrWizard94-Compile/Agents-Constitution/blob/main/references/always-load.md) |
| **Architecture** | [docs/ARCHITECTURE.md](https://github.com/MrWizard94-Compile/Agents-Constitution/blob/main/docs/ARCHITECTURE.md) |
| **Integrity** | [tools/validate-source.py](https://github.com/MrWizard94-Compile/Agents-Constitution/blob/main/tools/validate-source.py) |

Load from GitHub (`github__get_file_contents`, raw URLs, or a generated mirror of
that repository). Freeze one commit SHA of `main` for the invocation. Do not treat
a workspace folder as canonical source.

### Always load

1. This file (WPAI Level 4 entry)
2. Canonical `SKILL.md` from the repository above
3. The always-load set named in that skill and `references/always-load.md`
4. Additional modules per the applicability matrix in the canonical source

### Verify canonical source

GitHub Actions `Validate WPAI Constitution Source` on `main` must be green.

From a clone of the repository:

```powershell
python tools/validate-source.py
```

Must exit 0.

Refresh generated skill mirrors (Grok and Codex defaults):

```powershell
python distribution/sync.py
```

---

## Project-local law (Level 4)

Add project-specific mission, stack pins, and commands below as needed.
Product docs stay in this repository (README, docs/). Do not weaken canonical CONST-*
rules without a documented override.
