"""Authorized read-only design probe of v0.1.5; no programs generated/executed."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import textwrap

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from atlas_runtime import atomic_json  # noqa: E402
from template_factory.blueprints import verify_frozen  # noqa: E402
from template_factory.cli import CLI  # noqa: E402
from template_factory.cognition import (  # noqa: E402
    DESIGN_DIMENSIONS,
    DESIGN_REVIEW_PROMPT,
    research_context,
    validate_review,
)
from template_factory.store import FactoryStore, digest  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
store = FactoryStore(pilot, pack)
artifact = next(
    a for a in store.artifacts() if a["id"] == "tpl_231994f1a0a841d6b040d66de3287a6a"
)
bundle = pilot / artifact["bundle_path"]
spec = verify_frozen(bundle, artifact["digest"])
probe = pilot / "jobs/design-probe/attempt-1/blueprint-spec-review-probe"
if probe.exists():
    raise SystemExit(
        "Probe already exists; inspect its evidence instead of duplicating calls."
    )
source = probe / "source"
source.mkdir(parents=True)
subprocess.run(["git", "init", "--quiet", str(probe)], check=True)
fields = (
    "title",
    "roles",
    "features",
    "decisions",
    "phases",
    "acceptance",
    "architecture_markdown",
    "limits",
)
plan = {
    "spec": {key: spec[key] for key in fields},
    "file_plan": [
        {
            "path": path.relative_to(bundle / "source").as_posix(),
            "purpose": "Pinned acceptance program; this probe reviews its specification only.",
        }
        for path in sorted((bundle / "source/acceptance").iterdir())
        if path.name != "plan.json"
    ],
}
atomic_json(source / "SPECIFICATION.json", plan)
(source / "ARCHITECTURE.md").write_text(spec["architecture_markdown"])
(source / "RESEARCH.md").write_text(research_context(spec["research"]))
draft = [
    "# Confirmed scenario\n"
    + json.dumps(spec["scenario"], ensure_ascii=False, indent=2)
]
draft.extend(
    "# " + key + "\n" + json.dumps(plan["spec"][key], ensure_ascii=False, indent=2)
    for key in fields
    if key != "architecture_markdown"
)
draft.append(
    "# file_plan\n" + json.dumps(plan["file_plan"], ensure_ascii=False, indent=2)
)
(source / "DRAFT.md").write_text(
    "\n\n".join(
        "\n".join(textwrap.fill(line, width=120) for line in part.splitlines())
        for part in draft
    )
)
atomic_json(
    probe / "input.json",
    {
        "language": "zh",
        "proposal_digest": digest(plan),
        "artifact_digest": artifact["digest"],
        "source_inventory": sorted(path.name for path in source.iterdir()),
    },
)
active = probe.parent / "active"
active.write_text("Authorized design-only probe; no production or runtime execution.")
implementation_at_start = hashlib.sha256(
    (pack / "template_factory/cognition.py").read_bytes()
).hexdigest()
prompt_at_start = hashlib.sha256(DESIGN_REVIEW_PROMPT.encode()).hexdigest()
print(
    json.dumps({"event": "design_probe_started", "artifact": artifact["id"]}),
    flush=True,
)
try:
    raw = CLI().run(
        probe,
        DESIGN_REVIEW_PROMPT,
        "open-design/deepseek-v4.1-flash",
        1200,
        lambda: False,
        lambda _: None,
    )
    report = validate_review(raw, source, DESIGN_DIMENSIONS)
    report["scope"] = (
        "Independent specification design probe only; no program generation, execution, publication or source refresh."
    )
    report["artifact_digest"] = artifact["digest"]
    report["proposal_digest"] = digest(plan)
    report["implementation_at_start_sha256"] = implementation_at_start
    report["prompt_at_start_sha256"] = prompt_at_start
    atomic_json(probe / "report.json", report)
    atomic_json(Path(__file__).parent / "design-preflight-probe.json", report)
    print(
        json.dumps(
            {
                "event": "design_probe_finished",
                "outcome": report["outcome"],
                "checks": [
                    (row["dimension"], row["outcome"]) for row in report["checks"]
                ],
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
finally:
    active.unlink(missing_ok=True)
