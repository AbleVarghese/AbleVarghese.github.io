from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR = Path(__file__).parents[1] / "validate-documentation-baseline.py"
spec = importlib.util.spec_from_file_location("documentation_baseline_validator", VALIDATOR)
assert spec and spec.loader
validator_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator_module)
validate = validator_module.validate


class DocumentationBaselineValidatorTest(unittest.TestCase):
    def test_validator_exists(self) -> None:
        validator = Path(__file__).parents[1] / "validate-documentation-baseline.py"
        self.assertTrue(validator.is_file(), "documentation-baseline validator must exist")

    def test_current_baseline_is_complete(self) -> None:
        root = Path(__file__).parents[2]
        validator = Path(__file__).parents[1] / "validate-documentation-baseline.py"
        result = subprocess.run(
            [sys.executable, str(validator), "--root", str(root)],
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_required_artifact_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "DOCUMENTATION-BASELINE-2026-09.md").write_text(
                "<!-- baseline-required: docs/example.md -->\n", encoding="utf-8"
            )
            (docs / "example.md").write_text(" \n", encoding="utf-8")
            self.assertIn("empty required artifact: docs/example.md", validate(root))

    def test_incomplete_traceability_chain_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            requirements = docs / "requirements"
            requirements.mkdir(parents=True)
            (docs / "DOCUMENTATION-BASELINE-2026-09.md").write_text(
                "<!-- baseline-required: docs/requirements/STAGE-0-TRACEABILITY-MATRIX-2026-09.md -->\n",
                encoding="utf-8",
            )
            (requirements / "STAGE-0-TRACEABILITY-MATRIX-2026-09.md").write_text(
                "| BR-01 | PR-01 | |\n", encoding="utf-8"
            )
            self.assertIn(
                "missing traceability ID: SR-01",
                validate(root),
            )

    def test_broken_local_link_in_required_artifact_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "DOCUMENTATION-BASELINE-2026-09.md").write_text(
                "<!-- baseline-required: docs/example.md -->\n", encoding="utf-8"
            )
            (docs / "example.md").write_text("See [missing](missing.md).\n", encoding="utf-8")
            self.assertIn(
                "broken local link: docs/example.md -> docs/missing.md",
                validate(root),
            )


if __name__ == "__main__":
    unittest.main()
