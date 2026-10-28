"""Boundary and evidence semantics for the portfolio census."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import collect_inventory as census


class CensusTests(unittest.TestCase):
    def test_registry_reads_only_project_path_column(self):
        text = "| `Software/Alpha` | `Remote` |\n| `Gaming/Games/Beta` | `Other` |\n| `Archives/Old` | `Software/False` |"
        self.assertEqual(census.registry_paths(text), {"Software/Alpha", "Gaming/Games/Beta"})

    def test_traversal_and_absolute_paths_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for value in ("../other", "/absolute", "C:/other", "Software//A", "Software/./A", "Software\\A", ""):
                with self.subTest(value=value), self.assertRaises(ValueError):
                    census.safe_path(root, value)

    def test_parent_repository_cannot_certify_ignored_child(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(census.subprocess, "run") as run:
                self.assertEqual(census.git_facts(Path(directory)), {"state": "no-independent-git-root"})
                run.assert_not_called()

    def test_missing_registered_project_is_retained(self):
        with tempfile.TemporaryDirectory() as directory:
            result = census.inspect_project(Path(directory), "Software/Absent", True)
            self.assertEqual(result["state"], "missing")
            self.assertTrue(result["registered"])
            self.assertEqual(result["readiness"], "not-certified")

    def test_only_allowed_sources_are_read_and_no_content_is_copied(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "Software" / "Alpha"
            project.mkdir(parents=True)
            (project / "README.md").write_text("Documentation", encoding="utf-8")
            (project / ".env").write_text("private fixture", encoding="utf-8")
            (project / "package.json").write_text('{"version":"1.0","scripts":{"test":"example"}}', encoding="utf-8")
            result = census.inspect_project(root, "Software/Alpha", False)
            self.assertEqual({s["path"] for s in result["sources"]}, {"Software/Alpha/README.md", "Software/Alpha/package.json"})
            self.assertEqual(result["declared_checks"], ["test"])
            self.assertNotIn("private fixture", str(result))
            self.assertEqual(result["readiness"], "not-certified")

    def test_census_discovers_new_project_and_retains_old_location(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Software" / "New").mkdir(parents=True)
            (root / "Software" / ".agent").mkdir()
            (root / "PROJECT-REGISTRY.md").write_text("| `Games/Old` | `Old` |", encoding="utf-8")
            with patch.object(census, "CONTAINERS", ("Software",)), patch.object(census, "FIXED", ()):
                result = census.collect(root)
            self.assertEqual([p["path"] for p in result["records"]], ["Games/Old", "Software/New"])
            self.assertEqual(result["errors"], [])
            self.assertEqual(len(result["excluded"]), 1)

    def test_invalid_manifest_is_evidence_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "Software" / "Alpha"
            project.mkdir(parents=True)
            (project / "package.json").write_text("[]", encoding="utf-8")
            result = census.inspect_project(root, "Software/Alpha", False)
            self.assertEqual(result["manifest_state"], "invalid-json-object")


if __name__ == "__main__":
    unittest.main()
