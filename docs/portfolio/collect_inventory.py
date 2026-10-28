"""Collect bounded, local portfolio evidence without executing project code.

Only named project containers and registry paths are traversed. Reparse points
are recorded without following them. Git facts require an independent Git root;
an ignored project inside the company registry cannot inherit its clean status.
This census records evidence availability, never product readiness.
"""

import argparse
import hashlib
import json
import re
import stat
import subprocess
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


CONTAINERS = (
    "Software", "AI-Research", "Gaming/Games", "Gaming/Minecraft/Mods-1.20.1-Forge",
    "Gaming/Minecraft/Mods-1.21.1-NeoForge", "Gaming/Minecraft/Modpacks",
    "Gaming/Minecraft/Mods-1.20.1-Forge/SteampunkFactory",
)
FIXED = (
    "Gaming/TerraBlock", "Gaming/Minecraft/ATM_Fix", "Gaming/Minecraft/mod-test-suite",
    "Gaming/Minecraft/Omni_Framework", "Music", "Brand", "Graphics", "Quantum", "Spark",
)
CONTAINER_ONLY = {"Gaming/Minecraft/Mods-1.20.1-Forge/SteampunkFactory"}
DOCUMENT_NAMES = {
    "agents.md", "claude.md", "readme.md", "readme.txt", "design.md", "spec.md",
    "architecture.md", "status.md", "roadmap.md", "plan.md", "product-direction.md",
    "delivery-report.md", "manifest.md", "outline.md", "listing.md", "spark.md",
}
MANIFEST_NAMES = {
    "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "cargo.toml",
    "cargo.lock", "pyproject.toml", "requirements.txt", "uv.lock", "poetry.lock",
    "cmakelists.txt", "build.gradle", "build.gradle.kts", "gradle.properties",
    "pom.xml", "global.json", "directory.build.props",
}


def safe_path(root, relative):
    """Require a clean root-relative path and reject all reparse ancestors."""
    parts = PurePosixPath(relative).parts
    if (not parts or "\\" in relative or ":" in relative
            or PurePosixPath(relative).is_absolute()
            or any(p in (".", "..") for p in relative.split("/"))
            or any(not p for p in relative.split("/"))):
        raise ValueError("Path must be clean and relative")
    current = root
    for part in parts:
        current = current / part
        try:
            info = current.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 1024:
            raise ValueError("Reparse boundary")
    return current


def registry_paths(text):
    """Read only the first path column of project registry table rows."""
    return set(re.findall(r"^\| `((?:Software|AI-Research|Games|Gaming)/[^`]+)` \|", text, re.M))


def git_facts(path):
    """Read an owned repository, with bounded commands and no persistent config."""
    if not (path / ".git").exists():
        return {"state": "no-independent-git-root"}

    def run(*args):
        return subprocess.run(
            ["git", "--no-optional-locks", "-C", str(path), *args],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20,
        )

    try:
        top = run("rev-parse", "--show-toplevel")
        if top.returncode:
            reason = "ownership-check-rejected" if "dubious ownership" in top.stderr else "git-query-failed"
            return {"state": reason}
        if Path(top.stdout.strip()).resolve() != path.resolve():
            return {"state": "inherited-git-root"}
        head = run("rev-parse", "--verify", "HEAD")
        branch = run("branch", "--show-current")
        status = run("status", "--porcelain=v1", "--untracked-files=all")
        worktrees = run("worktree", "list", "--porcelain")
        if any(r.returncode for r in (branch, status, worktrees)):
            return {"state": "git-query-failed"}
        changes = status.stdout.splitlines()
        return {
            "state": "observed", "head": head.stdout.strip() if head.returncode == 0 else None,
            "branch": branch.stdout.strip() or "detached",
            "changed_entries": len(changes),
            "untracked_entries": sum(s.startswith("??") for s in changes),
            "worktree_count": sum(s.startswith("worktree ") for s in worktrees.stdout.splitlines()),
        }
    except (OSError, subprocess.TimeoutExpired):
        return {"state": "git-query-unavailable"}


def source_fact(root, path):
    """Fingerprint a bounded source file; never capture its contents."""
    rel = path.relative_to(root).as_posix()
    safe_path(root, rel)
    size = path.stat().st_size
    fact = {"path": rel, "bytes": size}
    if size <= 2_000_000:
        fact["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    else:
        fact["hash_state"] = "above-two-megabyte-read-limit"
    return fact


def inspect_project(root, relative, registered):
    record = {"path": relative, "registered": registered, "readiness": "not-certified"}
    try:
        path = safe_path(root, relative)
        if not path.is_dir():
            return dict(record, state="missing")
        files = sorted((p for p in path.iterdir() if p.is_file()), key=lambda p: p.name.lower())
        sources = [p for p in files if p.name.lower() in DOCUMENT_NAMES | MANIFEST_NAMES
                   or p.suffix.lower() in (".sln", ".slnx", ".csproj")]
        record.update(
            state="present", git=git_facts(path),
            root_file_count=len(files),
            sources=[source_fact(root, p) for p in sources],
            test_entry_paths=[(path / name).relative_to(root).as_posix()
                              for name in ("tests", "test", "Tests", "scripts", "cli/tests")
                              if (path / name).is_dir()],
        )
        package = path / "package.json"
        if package.is_file() and package.stat().st_size <= 2_000_000:
            safe_path(root, package.relative_to(root).as_posix())
            try:
                data = json.loads(package.read_text(encoding="utf-8-sig"))
                record["package_version"] = data.get("version")
                record["declared_checks"] = sorted(data.get("scripts", {}).keys())
            except (ValueError, AttributeError, TypeError):
                record["manifest_state"] = "invalid-json-object"
    except ValueError:
        record["state"] = "reparse-or-invalid-path"
    except OSError:
        record["state"] = "filesystem-query-failed"
    return record


def collect(root):
    """Return all registered roots plus direct roots in the named containers."""
    root = root.resolve(strict=True)
    registry = root / "PROJECT-REGISTRY.md"
    registered = registry_paths(registry.read_text(encoding="utf-8-sig"))
    candidates = set(registered) | set(FIXED)
    errors = []
    excluded = []
    for relative in CONTAINERS:
        try:
            container = safe_path(root, relative)
            if not container.is_dir():
                errors.append({"path": relative, "reason": "container-missing"})
                continue
            for child in sorted(container.iterdir(), key=lambda p: p.name.lower()):
                if not child.is_dir():
                    continue
                rel = child.relative_to(root).as_posix()
                if child.name.startswith(".") or rel in CONTAINER_ONLY:
                    excluded.append({"path": rel, "reason": "agent-state-or-container"})
                else:
                    candidates.add(rel)
        except (ValueError, OSError):
            errors.append({"path": relative, "reason": "container-unreadable-or-reparse"})
    records = [inspect_project(root, p, p in registered) for p in sorted(candidates, key=str.lower)]
    return {
        "schema_version": 1, "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root), "priority": "Software products first (director, 2026-09-08)",
        "method": "Registry union named direct project containers; source fingerprints and owned Git metadata only",
        "limits": ["No project build, runtime, deployment, commercial status, or artistic quality is certified",
                   "No recursive vendor, reference, archive, credential, model, or runtime-content scan",
                   "Nested components belong to their listed project; unnamed folders remain candidates"],
        "registry_source": source_fact(root, registry),
        "containers": list(CONTAINERS), "excluded": excluded, "errors": errors,
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = collect(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"records": len(result["records"]), "errors": result["errors"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
