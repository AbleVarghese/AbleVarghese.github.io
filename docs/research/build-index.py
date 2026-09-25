#!/usr/bin/env python3
"""Generate a stable, bounded Markdown index for a research directory."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path


def summary(path: Path) -> str:
    try:
        text = path.read_bytes()[:65536].decode("utf-8", "replace")
    except OSError:
        return "unreadable"
    lines = text.splitlines()
    headings = [line.lstrip("#").strip() for line in lines if line.startswith("#")]
    first = headings or [line.strip() for line in lines if line.strip()]
    return "; ".join(first[:3]).replace("|", "\\|")[:180] or "binary or empty"


def build_index(root: Path, output: Path) -> int:
    output = output.resolve()
    rows: list[str] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.resolve() == output:
            continue
        relative = path.relative_to(root).as_posix()
        if "__pycache__" in relative.split("/"):
            continue
        rows.append(f"| [`{relative}`]({relative}) | {path.stat().st_size:,} | {summary(path)} |")
    content = "\n".join(
        [
            "# Research index",
            "",
            "> Generated mechanically from `docs/research/`. Run `python3 docs/research/build-index.py`; this is the overlap-check surface.",
            "",
            "| File | Bytes | Headings / first semantic line |",
            "|---|---:|---|",
            *rows,
            "",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=output.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    os.replace(temporary, output)
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root / "INDEX.md").resolve()
    print(f"indexed {build_index(root, output)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
