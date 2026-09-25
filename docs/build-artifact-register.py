#!/usr/bin/env python3
"""Generate a stable register for documentation and source artifacts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import tempfile
from pathlib import Path

VERSION = re.compile(r"20\d{2}-\d{2}")
REQUIRED_SOURCE_COLUMNS = {
    "id",
    "lifecycle",
    "classification",
    "canonical_path",
    "sha256",
    "version",
}


def sha256_prefix(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def lifecycle(path: Path) -> str:
    if "_archive" in path.parts or ".pre-" in path.name or ".attempt" in path.name:
        return "archive"
    if path.name == "INDEX.md":
        return "generated"
    return "active"


def version(path: Path) -> str:
    match = VERSION.search(path.as_posix())
    return match.group(0) if match else "n/a"


def document_rows(docs_root: Path, output: Path) -> list[str]:
    rows: list[str] = []
    for path in sorted(item for item in docs_root.rglob("*") if item.is_file()):
        if path.resolve() == output.resolve():
            continue
        relative = path.relative_to(docs_root).as_posix()
        if "__pycache__" in relative.split("/"):
            continue
        artifact_class = relative.split("/", 1)[0] if "/" in relative else "docs"
        rows.append(
            f"| {artifact_class} | {lifecycle(path.relative_to(docs_root))} | {version(path.relative_to(docs_root))} "
            f"| [`{relative}`]({relative}) | {path.stat().st_size:,} | `{sha256_prefix(path)}` |"
        )
    return rows


def source_records(manifest: Path) -> list[dict[str, str]]:
    with manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None or not REQUIRED_SOURCE_COLUMNS.issubset(reader.fieldnames):
            raise ValueError(f"{manifest} lacks required source-manifest columns")
        return sorted(reader, key=lambda row: row["id"])


def validate_source_records(records: list[dict[str, str]], repository_root: Path) -> None:
    for row in records:
        path = repository_root / row["canonical_path"]
        if not path.exists():
            if row["lifecycle"] == "local-private":
                continue
            raise ValueError(f"source integrity: missing {row['id']} at {path}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != row["sha256"]:
            raise ValueError(f"source integrity: SHA-256 mismatch for {row['id']}")


def source_rows(records: list[dict[str, str]]) -> list[str]:
    rows: list[str] = []
    for row in records:
        path = row["canonical_path"].replace("|", "\\|")
        rows.append(
            f"| {row['id']} | {row['lifecycle']} | {row['classification']} | `{path}` "
            f"| `{row['sha256'][:16]}` | {row['version']} |"
        )
    return rows


def source_manifest_reference(docs_root: Path, sources_manifest: Path) -> tuple[str, str]:
    try:
        display = sources_manifest.relative_to(docs_root.parent).as_posix()
        return display, f"../{display}"
    except ValueError:
        return sources_manifest.as_posix(), sources_manifest.as_uri()


def build_register(docs_root: Path, sources_manifest: Path, output: Path) -> tuple[int, int]:
    documents = document_rows(docs_root, output)
    records = source_records(sources_manifest)
    validate_source_records(records, docs_root.parent)
    sources = source_rows(records)
    manifest_display, manifest_link = source_manifest_reference(docs_root, sources_manifest)
    content = "\n".join(
        [
            "# Artifact register",
            "",
            "> Generated mechanically. It inventories every documentation artifact and every row in the source manifest; it does not replace the detailed research index.",
            "",
            "## Documentation artifacts",
            "",
            "| Class | Lifecycle | Version | Path | Bytes | SHA-256 prefix |",
            "|---|---|---|---|---:|---|",
            *documents,
            "",
            "## Source artifacts",
            "",
            f"> Source-manifest authority: [`{manifest_display}`]({manifest_link}).",
            "",
            "| Source ID | Lifecycle | Classification | Canonical path | SHA-256 prefix | Version |",
            "|---|---|---|---|---|---|",
            *sources,
            "",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=output.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    os.replace(temporary, output)
    return len(documents), len(sources)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs-root", type=Path, default=Path(__file__).parent)
    parser.add_argument("--sources-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    docs_root = args.docs_root.resolve()
    sources_manifest = args.sources_manifest.resolve()
    output = (args.output or docs_root / "ARTIFACT-REGISTER.md").resolve()
    documents, sources = build_register(docs_root, sources_manifest, output)
    print(f"registered {documents} documentation artifacts and {sources} source artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
