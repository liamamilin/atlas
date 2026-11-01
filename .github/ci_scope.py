"""Select a conservative CI scope; never start providers, browsers or containers."""

import argparse
import json
from pathlib import Path
import re
import subprocess


REFERENCE_FILES = {
    "application-atlas-production-pack/template_factory/product_reference.py",
    "application-atlas-production-pack/template_factory/reference_preview.py",
    "application-atlas-production-pack/template_factory/reference_pilot.py",
    "application-atlas-production-pack/tests/test_product_reference.py",
    "application-atlas-production-pack/tests/test_reference_preview.py",
    "application-atlas-production-pack/tests/test_reference_pilot.py",
    "examples/assisted-trials/product_reference_profile.py",
    "examples/assisted-trials/produce_reference_pilot.py",
    "examples/assisted-trials/tests/test_product_reference_profile.py",
    "examples/assisted-trials/tests/test_reference_pilot_runner.py",
}
REFERENCE_DOCS = (
    "docs/template-factory/product-reference-generator-2026-10-22/",
    "docs/template-factory/product-reference-pilot-2026-10-22/",
    "atlas-reference-examples-2026-10-22/",
)
DOC_SUFFIXES = {".md", ".txt", ".json", ".log", ".png", ".sha256"}


def classify(paths):
    """Unknown/mixed/shared changes always retain the existing full gate."""
    paths = list(paths)
    if not paths:
        return "full"
    for path in paths:
        if path in REFERENCE_FILES:
            continue
        if path.startswith(REFERENCE_DOCS) and Path(path).suffix.lower() in DOC_SUFFIXES:
            continue
        return "full"
    # Even docs-only reference commits exercise the reference contract tests.
    return "reference"


def changed_paths(base, head):
    if not all(re.fullmatch(r"[0-9a-f]{40}", value or "") and value != "0" * 40 for value in (base, head)):
        return []
    try:
        output = subprocess.run(
            ["git", "diff", "--no-renames", "--name-only", "-z", base, head],
            capture_output=True, check=True, timeout=30,
        ).stdout
        return [p.decode("utf-8", errors="strict") for p in output.split(b"\0") if p]
    except (OSError, subprocess.SubprocessError, UnicodeError):
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="")
    parser.add_argument("--head", default="")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    paths = changed_paths(args.base, args.head)
    mode = classify(paths)
    print(json.dumps({"mode": mode, "files": paths}, ensure_ascii=False))
    if args.output:
        with args.output.open("a", encoding="utf-8") as stream:
            stream.write("mode=" + mode + "\n")
