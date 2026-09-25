from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class BuildIndexTest(unittest.TestCase):
    def test_generates_stable_index_and_excludes_itself(self) -> None:
        script = Path(__file__).parents[1] / "build-index.py"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "alpha.md").write_text("# Alpha\n\nUseful text.\n", encoding="utf-8")
            (root / "nested").mkdir()
            (root / "nested" / "facts.tsv").write_text("id\tvalue\n1\tone\n", encoding="utf-8")
            (root / "__pycache__").mkdir()
            (root / "__pycache__" / "generated.pyc").write_bytes(b"not research")
            output = root / "INDEX.md"

            first = subprocess.run(
                [sys.executable, str(script), "--root", str(root), "--output", str(output)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            first_bytes = output.read_bytes()
            self.assertIn(b"[`alpha.md`](alpha.md)", first_bytes)
            self.assertIn(b"[`nested/facts.tsv`](nested/facts.tsv)", first_bytes)
            self.assertNotIn(b"[`INDEX.md`](INDEX.md)", first_bytes)
            self.assertNotIn(b"__pycache__", first_bytes)

            second = subprocess.run(
                [sys.executable, str(script), "--root", str(root), "--output", str(output)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first_bytes, output.read_bytes())


if __name__ == "__main__":
    unittest.main()
