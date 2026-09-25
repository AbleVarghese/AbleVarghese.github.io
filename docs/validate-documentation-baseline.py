from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARKER = re.compile(r"^<!-- baseline-required: ([^\s]+) -->$", re.MULTILINE)
LINK = re.compile(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)")
TRACEABILITY_PATH = "docs/requirements/STAGE-0-TRACEABILITY-MATRIX-2026-09.md"
TRACEABILITY_IDS = ("BR-01", "PR-01", "SR-01", "VT-01")


def validate(root: Path) -> list[str]:
    baseline = root / "docs" / "DOCUMENTATION-BASELINE-2026-09.md"
    if not baseline.is_file():
        return [f"missing baseline: {baseline}"]

    required = MARKER.findall(baseline.read_text(encoding="utf-8"))
    if not required:
        return [f"no baseline-required markers: {baseline}"]

    errors: list[str] = []
    for relative in required:
        artifact = root / relative
        if not artifact.is_file():
            errors.append(f"missing required artifact: {relative}")
            continue
        content = artifact.read_text(encoding="utf-8")
        if not content.strip():
            errors.append(f"empty required artifact: {relative}")
            continue
        for target in LINK.findall(content):
            if "://" in target or target.startswith(("mailto:", "tel:")):
                continue
            destination = artifact.parent / target
            if not destination.is_file():
                errors.append(
                    f"broken local link: {relative} -> {destination.relative_to(root)}"
                )
        if relative == TRACEABILITY_PATH:
            for identifier in TRACEABILITY_IDS:
                if identifier not in content:
                    errors.append(f"missing traceability ID: {identifier}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the documentation-baseline artifact contract.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print("documentation baseline: FAIL", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("documentation baseline: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
