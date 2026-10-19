"""Reproducible local export check. No provider calls or application execution."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))

HERE = Path(__file__).resolve().parent
ORIGINAL = (
    ROOT
    / "docs/template-factory/cognition-pilots/bookmark-2026-10-17/tpl_3f303c2a69ea49b7aa1e5d01eba340f5.zip"
)
EXPECTED = "22a2b1e426c6eee0778459540aaf2d7dd34e390140a55e1ccda2bbb51e5b6a4b"


def main():
    from template_factory.artifacts import archive_tree, tree_manifest
    from template_factory.blueprints import (
        export_development,
        freeze_blueprint,
        unpack_archive,
    )

    data = ORIGINAL.read_bytes()
    assert hashlib.sha256(data).hexdigest() == EXPECTED
    result = {
        "scope": "local phase-handoff export only; no LLM, application or bundled acceptance execution",
        "original_zip_sha256": EXPECTED,
        "original_version": "0.1.12",
        "exports": [],
    }
    with tempfile.TemporaryDirectory() as temporary:
        work = Path(temporary)
        source = work / "source"
        source.mkdir()
        unpack_archive(data, source)
        before = tree_manifest(source)
        spec = json.loads((source / "template.json").read_text())
        assert spec["version"] == result["original_version"]
        frozen = freeze_blueprint(
            source, work / "frozen", {"origin": "local-handoff-export-verification"}
        )
        for phase in ("P0", "P2"):
            out = work / phase
            export_development(
                work / "frozen", frozen["digest"], out, "bookmark-trial", phase
            )
            assert tree_manifest(out / "blueprint") == before
            packet = json.loads((out / "CURRENT_PHASE.json").read_text())
            through = {
                p["id"]
                for p in spec["phases"][
                    : next(i for i, p in enumerate(spec["phases"]) if p["id"] == phase)
                    + 1
                ]
            }
            assert packet["acceptance"] == [
                a for a in spec["acceptance"] if a["phase"] in through
            ]
            assert packet["decisions"] == spec["decisions"]
            assert packet["scenario"] == spec["scenario"]
            assert packet["evidence_status"] == "not_run_by_export"
            archive = HERE / f"bookmark-v0.1.12-{phase.lower()}-handoff.zip"
            generated = archive_tree(out, work / f"{phase}.zip").read_bytes()
            if archive.exists():
                assert archive.read_bytes() == generated, (
                    "Existing pilot differs; preserve it and use a new pilot directory"
                )
            else:
                archive.write_bytes(generated)
            result["exports"].append(
                {
                    "phase": phase,
                    "prerequisite_phases": packet["prerequisite_phases"],
                    "feature_count": len(packet["features"]),
                    "case_count": len(packet["acceptance"]),
                    "negative_case_count": sum(
                        a["type"] == "negative" for a in packet["acceptance"]
                    ),
                    "decision_count": len(packet["decisions"]),
                    "blueprint_bytes": sum(
                        (out / "blueprint" / rel).stat().st_size for rel in before
                    ),
                    "entry_files_bytes": sum(
                        (out / f).stat().st_size
                        for f in (
                            "AGENT.md",
                            "HANDOFF.md",
                            "CURRENT_PHASE.json",
                            "PROJECT_DECISIONS.json",
                        )
                    ),
                    "byte_scope": "UTF-8 file sizes, not measured context usage, tokens, cost or speed",
                    "source_files_byte_identical": True,
                    "archive": archive.name,
                    "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                    "phase_scope_warning": "Original P0 excludes category management and search; export does not rephase it."
                    if phase == "P0"
                    else "Includes P0/P1 prerequisites and optional legacy features; not a newly redesigned core P0.",
                }
            )
        assert tree_manifest(source) == before
    assert hashlib.sha256(ORIGINAL.read_bytes()).hexdigest() == EXPECTED
    (HERE / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
