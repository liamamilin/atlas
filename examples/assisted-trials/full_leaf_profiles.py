"""Versioned full-leaf prompts; historical three-item prompts stay untouched."""

import json

from produce_with_opencode import READABLE_REVIEW, CHECKS, validate_generation
from template_factory.store import digest

VERSION = "full-leaf-v1"
DISCOVERY = """Read input.json and ALL of leaf.md. Select ONE small concrete scenario
that preserves this leaf's defining core, not a generic CRUD substitute. Respect a
fixed_scenario when supplied. Choose a sensible delivery profile (web, desktop,
cli, library, service, or other); do not force Python/HTTP/SQLite onto every type.
First inspect compatible_shared_cases; reuse a suitable fixed case when applicable.
Otherwise use websearch/webfetch to find a real licensed GitHub open-source project.
Verify exact paths, license text and at least one relevant implementation file.
Limit exploration to at most 6 web searches and 16 web fetches. Prefer a small
source surface, 2-8 UTF-8 files each <180KB including LICENSE and README.
Return ONLY a compact VALID JSON object in this exact shape (example, not facts):
{"repository":"https://github.com/owner/repo","files":["LICENSE","README.md","src/core.py"],"rationale":"short reason","reuse_case_id":null,"delivery_profile":"cli","scenario":{"name":"A specific workflow","audience":"one user role","objective":"one concrete core journey","workflow":["input","operate","inspect result"],"acceptance":["observable core result"]}}
Use actual verified values, no invented commit/license/runtime claims. Host pins
the version. Each prose field <700 characters, no pasted code or long narratives.
Escape ALL quotes/newlines/backslashes using JSON rules; no markdown fences or
additional text. Never repair protocol by discarding fields. Raw output is saved.
"""

AUTHOR = """Read input.json, ALL leaf.md and source/upstream/ fixed files. Produce
a cognition TEMPLATE, not an application. Preserve the fixed concrete scenario.
Choose target technology appropriate to input.delivery_profile; no blanket HTTP,
SQLite, browser or Python-target requirement. A small complete core journey is
enough, not a mature SaaS platform. 1-5 meaningful capabilities with matching goals.
SOURCE PARTITIONS ARE MANDATORY:
  requirements: ONLY the Atlas and scenario source IDs in input.source_ids;
  case_files: ONLY upstream IDs in input.source_ids;
  design_inferences: explicit target proposals, depending on known IDs.
observations contains ONLY tuples [documentation|code_observation, upstream path,
1-based start,end, statement]; NEVER leaf.md or an Atlas source path. Statements
describe actual upstream facts, not target requirements. Repository, commit and
file hashes are host-owned; don't invent source identities or runtime evidence.
Return valid JSON ONLY:
{"authored":{"name":"...","audience":"...","objective":"...","workflow":["..."],"acceptance":["..."],"observations":[["code_observation","actual/path",1,2,"observed fact"]],"inference":"explicit target inference","features":["..."],"goals":["precise corresponding acceptance"],"arch":"full architecture markdown","gaps":["known limitation"],"delivery_profile":"same as input","execution_default":"appropriate runtime and data boundary","source_refs":{"requirements":["actual Atlas ID","actual scenario ID"],"case_files":["actual upstream ID"],"design_inferences":[{"text":"target choice","depends_on":["actual ID"]}]}},"acceptance_files":{"probe.py":"full stdlib acceptance orchestrator","README.md":"how to run core verification"}}
Provide at least 2 genuine observations including code. Keep 1-5 acceptance cases
A01..A0N, exactly matching capabilities. probe.py is a portable verifier, NOT a
requirement to implement the target in Python; it may verify a CLI, library,
desktop integration, service or Web app. Document appropriate adapter/target and
operator steps when a UI is needed. It must assert observable core results and
meaningful negative cases, not just lint/count files or declare success. Do not
install/run code here. For mutable data, use isolated disposable records/directories;
never delete user records. Define precise data/contracts/edge cases appropriate
to THIS leaf, transaction/lifecycle semantics where relevant, operating commands,
human decisions/defaults and honest not_run limits. No unused platform expansion.
All source IDs must exist in input. Keep source/code/view lines <1800 characters.
Escape every JSON string properly; keep prose focused. No invented pass/certification.
"""

REVIEW = (
    READABLE_REVIEW.replace(
        "home+recurring care+history leaf scope",
        "the supplied leaf's defining core and concrete scenario",
    )
    + """
This is an auxiliary core-usable template, not mature SaaS certification. Review
ALL current contracts and verifier code; block real core contradictions, false
sources, wrong arithmetic/state transitions, missing meaningful acceptance and
unread content. Do not require new non-core features or aesthetic refinements.
Check requirement/upstream/design source partition and appropriate delivery form.
Python probe.py is a verification orchestrator, not a mandatory Python HTTP app.
Known limitations and unrun states must be explicit. Return the complete exact
review JSON (all seven checks, every observation index, concrete blocking issues).
Never ignore a core defect to pass. New independent session, no author transcript.
"""
)


def source_ids(leaf_sha, scenario, snapshot):
    return {
        "requirements": {
            "atlas:" + leaf_sha: "leaf.md",
            "scenario:" + digest(scenario): "fixed scenario",
        },
        "upstream": {
            "upstream:" + digest({"path": path, "sha256": value}): {
                "path": path,
                "repository": snapshot["repository"],
                "commit_sha": snapshot["commit_sha"],
            }
            for path, value in snapshot["files"].items()
        },
    }


def validate_research(result):
    if not isinstance(result, dict) or set(result) != {
        "repository",
        "files",
        "rationale",
        "reuse_case_id",
        "delivery_profile",
        "scenario",
    }:
        raise ValueError("research schema keys differ")
    if result["delivery_profile"] not in {
        "web",
        "desktop",
        "cli",
        "library",
        "service",
        "other",
    }:
        raise ValueError("invalid delivery profile")
    if (
        not isinstance(result["rationale"], str)
        or not 1 <= len(result["rationale"]) <= 700
    ):
        raise ValueError("research rationale must be compact")
    scene = result["scenario"]
    if set(scene) != {"name", "audience", "objective", "workflow", "acceptance"}:
        raise ValueError("scenario schema keys differ")
    for key in ("name", "audience", "objective"):
        if not isinstance(scene[key], str) or not 1 <= len(scene[key]) <= 700:
            raise ValueError("invalid compact scenario field")
    for key in ("workflow", "acceptance"):
        if (
            not isinstance(scene[key], list)
            or not 1 <= len(scene[key]) <= 10
            or any(not isinstance(x, str) or not 1 <= len(x) <= 700 for x in scene[key])
        ):
            raise ValueError("invalid scenario list")
    if not isinstance(result["files"], list) or not 2 <= len(result["files"]) <= 8:
        raise ValueError("research source selection size")
    return result


def validate_author(value, snapshot, inputs):
    authored, files = validate_generation(value, snapshot, full=True)
    if authored.get("delivery_profile") != inputs[
        "delivery_profile"
    ] or not authored.get("execution_default"):
        raise ValueError("delivery profile/default missing or changed")
    refs = authored.get("source_refs", {})
    if set(refs) != {"requirements", "case_files", "design_inferences"}:
        raise ValueError("source partitions required")
    ids = inputs["source_ids"]
    if (
        set(refs["requirements"]) != set(ids["requirements"])
        or not refs["case_files"]
        or not set(refs["case_files"]) <= set(ids["upstream"])
    ):
        raise ValueError("source partition uses unknown or wrong-role IDs")
    observed_ids = {
        "upstream:" + digest({"path": o[1], "sha256": snapshot["files"][o[1]]})
        for o in authored["observations"]
    }
    if not observed_ids <= set(refs["case_files"]):
        raise ValueError("observations absent from case source IDs")
    known = set(ids["requirements"]) | set(ids["upstream"])
    if not refs["design_inferences"] or any(
        not x.get("text")
        or not x.get("depends_on")
        or not set(x["depends_on"]) <= known
        for x in refs["design_inferences"]
    ):
        raise ValueError("target inferences require known source IDs")
    json.dumps(value)  # Validation only; never repair malformed raw output.
    return authored, files


PROMPT_DIGEST = digest(
    {"version": VERSION, "discovery": DISCOVERY, "author": AUTHOR, "review": REVIEW}
)
CHECK_NAMES = CHECKS


def validate_review_envelope(value, identity):
    if (
        not isinstance(value, dict)
        or value.get("input_digest") != identity
        or value.get("verdict") not in {"pass", "needs_changes"}
        or set(value.get("checks", {})) != set(CHECKS)
        or any(type(x) is not bool for x in value["checks"].values())
        or not isinstance(value.get("issues"), list)
        or not isinstance(value.get("observations"), list)
    ):
        raise ValueError("independent review protocol/envelope differs")
    if value["verdict"] == "needs_changes" and not value["issues"]:
        raise ValueError("needs_changes requires concrete blocking findings")
    if value["verdict"] == "pass" and (
        value["issues"] or not all(value["checks"].values())
    ):
        raise ValueError("review pass contradicts checks/issues")
