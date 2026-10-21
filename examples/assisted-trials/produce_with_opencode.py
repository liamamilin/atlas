"""Small resumable Go-backed auxiliary producer; never resumes strict G1 jobs.

Models propose research/content. The host pins source bytes, validates references,
accounts every CLI launch, gates import on a separate-session review, and reuses
the existing auxiliary exporter and CaseLibrary. No upstream/generated code runs.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import textwrap

from produce_batch import ROOT, produce, save, request
from template_factory.budget import BudgetLedger
from template_factory.cli import CLI
from template_factory.sources import github_repo, request_bytes, resolve_commit
from template_factory.store import FactoryStore, digest
from atlas_runtime import atomic_json

MODEL = "opencode-go/deepseek-v4.1-flash"
CAMPAIGN = "atlas-v1-first-production-2026-10-19"
CHECKS = ("leaf_scope", "source_fidelity", "design_distinction", "core_journey",
          "architecture", "acceptance", "limits_and_safety")


def fixed_json(path, value):
    if path.exists():
        if json.loads(path.read_text()) != value:
            raise ValueError(f"fixed input changed: {path}; use a new output/version")
    else:
        atomic_json(path, value)


def safe_file(name):
    if (not isinstance(name, str) or not name or "\\" in name
            or name.startswith("/") or any(p in {"", ".", ".."} for p in name.split("/"))):
        raise ValueError("unsafe source/output path")
    return PurePosixPath(name).as_posix()


def manifest_files(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}


def snapshot_audit(directory):
    """OpenCode may init a private .git; retain ordinary evidence, not gitlinks."""
    target = directory.parent.parent / "audit" / directory.name
    target.mkdir(parents=True, exist_ok=True)
    names = ("BINDING.json", "DELIVERED.json", "RESULT.json", "LAUNCH_INTENT.json", "input.json", "leaf.md",
             "cli-summary.json", "events.jsonl", "stdout.log", "stderr.log", "original-response.json",
             "framing-recovery.json", "opencode.json", "process.json")
    for name in names:
        path = directory / name
        if path.is_symlink():
            raise ValueError("audit input must not be a symlink")
        if path.is_file():
            shutil.copyfile(path, target / name)
    atomic_json(target / "FILES.json", {name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
                                       for name in names if (directory / name).is_file()})


def checkpoint(directory, payload, prompt, cli, budget, source=None, leaf=None):
    """No duplicate call after delivery; an uncertain/failed launch needs inspection.

    Bind the instruction as well as all read bytes. A crashed delivered call can
    recover its existing parsed result without another model session.
    """
    directory.mkdir(parents=True, exist_ok=True)
    if source is not None:
        target = directory / "source"
        expected = manifest_files(source)
        if not target.exists():
            shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__"))
        if manifest_files(target) != expected:
            raise ValueError("checkpoint read-source changed")
    if leaf is not None:
        target = directory / "leaf.md"
        if target.exists() and target.read_bytes() != leaf:
            raise ValueError("checkpoint leaf changed")
        target.write_bytes(leaf)
    fixed_json(directory / "input.json", payload)
    binding = {"model": MODEL, "input_digest": digest(payload), "prompt": prompt,
               "source": manifest_files(directory / "source"),
               "leaf_sha256": hashlib.sha256(leaf).hexdigest() if leaf else None}
    fixed_json(directory / "BINDING.json", binding)
    result_path = directory / "RESULT.json"
    done = directory / "DELIVERED.json"
    if done.exists():
        receipt = json.loads(done.read_text())
        result = json.loads(result_path.read_text())
        if receipt != {"binding_digest": digest(binding), "result_digest": digest(result)}:
            raise ValueError("checkpoint result differs from delivered binding")
        snapshot_audit(directory)
        return result
    started = directory / "LAUNCH_INTENT.json"
    if started.exists():
        summary_path = directory / "cli-summary.json"
        summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
        # CLI persists its raw response before reporting successful delivery.
        if summary.get("delivery_status") != "delivered" or not summary.get("session_id"):
            raise ValueError("prior CLI attempt failed/uncertain; do not launch a duplicate")
        from template_factory.cli import parse_result
        result = parse_result(json.loads((directory / "original-response.json").read_text())["text"])
        if result_path.exists() and json.loads(result_path.read_text()) != result:
            raise ValueError("recovered raw result differs")
    else:
        fixed_json(started, {"binding_digest": digest(binding)})
        try:
            result = cli.run(directory, prompt, MODEL, 1800, lambda: False,
                             lambda message: print(directory.name + ": " + message, flush=True),
                             budget=budget, budget_required=True)
        finally:
            snapshot_audit(directory)
    atomic_json(result_path, result)
    atomic_json(done, {"binding_digest": digest(binding), "result_digest": digest(result)})
    snapshot_audit(directory)
    return result


def pin_sources(proposal, folder, store):
    """Resolve once before download; never let the model assign commit/digests."""
    repository = proposal["repository"]
    repo = github_repo(repository)
    paths = [safe_file(p) for p in proposal["files"]]
    if not 2 <= len(paths) <= 8 or len(paths) != len(set(paths)):
        raise ValueError("select 2–8 distinct small source files")
    pin_path = folder / "SOURCE_PIN.json"
    if pin_path.exists():
        pin = json.loads(pin_path.read_text())
        if pin["repository"] != repository or pin["paths"] != paths:
            raise ValueError("source selection changed")
    else:
        metadata = json.loads(request_bytes("https://api.github.com/repos/" + repo))
        spdx = (metadata.get("license") or {}).get("spdx_id")
        if not spdx or spdx in {"NOASSERTION", "NONE"}:
            raise ValueError("source license unclear; stop before generation")
        commit = resolve_commit(repository)
        pin = {"repository": repository, "commit_sha": commit, "paths": paths,
               "license_spdx": spdx, "repository_id": metadata["id"],
               "collected_at": datetime.now(timezone.utc).isoformat()}
        fixed_json(pin_path, pin)
    local = store.root / "sources" / folder.parent.name / folder.name
    local.mkdir(parents=True, exist_ok=True)
    for name in paths:
        target = local / name
        if not target.exists():
            data = request_bytes(f"https://raw.githubusercontent.com/{repo}/{pin['commit_sha']}/{name}", 180_000)
            data.decode("utf-8")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    files = manifest_files(local)
    if set(files) != set(paths):
        raise ValueError("source inventory differs")
    licenses = [p for p in paths if Path(p).name.lower().startswith(("license", "copying", "notice"))]
    if not licenses:
        raise ValueError("license text must be among pinned files")
    snapshot = {"repository": repository, "commit_sha": pin["commit_sha"],
                "strategy_version": "go-auxiliary-selected-files-v1", "collected_at": pin["collected_at"],
                "local_root": str(local.resolve()), "files": files, "license_files": licenses,
                "license": {"status": "located", "spdx_id": pin["license_spdx"],
                            "notice_hashes": {p: files[p] for p in licenses}},
                "license_uncertainties": ["Design reference only; no source code copied; file-level exceptions not exhaustively audited."],
                "excluded_paths": ["Unselected files; upstream not installed or run"]}
    fixed_json(folder / "source-snapshot.json", snapshot)
    return snapshot


def validate_generation(value, snapshot):
    authored, files = value["authored"], value["acceptance_files"]
    for key in ("name", "audience", "objective", "inference", "arch"):
        if not isinstance(authored.get(key), str) or not authored[key].strip():
            raise ValueError("missing authored " + key)
    for key in ("workflow", "acceptance", "features", "goals", "gaps"):
        if not isinstance(authored.get(key), list) or not authored[key] or not all(isinstance(x, str) and x.strip() for x in authored[key]):
            raise ValueError("invalid authored " + key)
    if not 3 <= len(authored["features"]) == len(authored["goals"]) <= 5:
        raise ValueError("require 3–5 features, each with an acceptance goal")
    if not isinstance(files, dict) or "probe.py" not in files or len(files) > 5:
        raise ValueError("require acceptance/probe.py and at most five files")
    for name, content in files.items():
        safe_file(name)
        if not name.endswith((".py", ".md", ".json")) or not isinstance(content, str) or len(content) > 80_000:
            raise ValueError("invalid acceptance delivery")
        if name.endswith(".py"):
            ast.parse(content)  # Parse only; never execute model code on the host.
    observations = authored.get("observations", [])
    if len(observations) < 2 or not any(o[0] == "code_observation" for o in observations):
        raise ValueError("require documentation/code observations")
    for kind, path, start, end, statement in observations:
        if kind not in {"documentation", "code_observation"} or path not in snapshot["files"] or not statement:
            raise ValueError("observation not bound to pinned source")
        lines = (Path(snapshot["local_root"]) / path).read_text().splitlines()
        if type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(lines):
            raise ValueError("observation lines outside source")
    # These identities come from host metadata, not model assertions.
    authored["repo_name"] = snapshot["repository"].removeprefix("https://github.com/")
    authored["license"] = snapshot["license"]["spdx_id"]
    authored["license_path"] = snapshot["license_files"][0]
    return authored, files


def validate_review(review, expected_digest, author_session, review_session, observations):
    if not author_session or not review_session or author_session == review_session:
        raise ValueError("independent reviewer requires a distinct actual session")
    if review.get("input_digest") != expected_digest:
        raise ValueError("review input digest differs")
    if review.get("verdict") != "pass" or review.get("issues") != []:
        raise ValueError("independent review did not pass; retain candidate and findings")
    checks = review.get("checks", {})
    if set(checks) != set(CHECKS) or any(checks[k] is not True for k in CHECKS):
        raise ValueError("independent review incomplete")
    items = review.get("observations", [])
    if (len(items) != observations or {o.get("index") for o in items} != set(range(observations))
            or any(o.get("verdict") != "accepted" or not o.get("reason") for o in items)):
        raise ValueError("every source observation must be explicitly reviewed")


def readable_candidate(directory, authored):
    """Lossless views of long JSON strings; the JSON stays authoritative.

    Files are materialized before the next review binding, never inserted into
    an ongoing session's read set. No product text, source fact or code changes.
    """
    strings = {key: value for key, value in authored.items() if isinstance(value, str)}
    manifest = {}
    for key, value in strings.items():
        name = "VIEW_" + key.upper() + ".md"
        safe_file(name)
        path = directory / name
        if path.exists() and path.read_text() != value:
            raise ValueError("derived view changed")
        path.write_text(value)
        manifest[name] = {"json_pointer": "/" + key, "sha256": hashlib.sha256(value.encode()).hexdigest()}
    scope = {key: value for key, value in authored.items() if key not in strings}
    # Arrays retain exact values in the original JSON; this summary offers
    # readable line wrapping for humans/agents without claiming byte equality.
    lines = []
    for key, values in scope.items():
        lines += ["## " + key, ""]
        for index, value in enumerate(values):
            lines += [f"### {index}", textwrap.fill(json.dumps(value, ensure_ascii=False), width=100), ""]
    (directory / "REVIEW_SCOPE.md").write_text("\n".join(lines))
    fixed_json(directory / "READ_VIEWS.json", manifest)
    (directory / "READING_GUIDE.md").write_text(
        "Read AUTHOR_INPUT.json for original fields. Its arch JSON string exceeds the read tool's "
        "per-line limit. Read VIEW_ARCH.md in pages until EOF; it is the EXACT decoded arch string, "
        "not a rewrite. READ_VIEWS.json binds each view to a JSON pointer and SHA-256. "
        "REVIEW_SCOPE.md wraps arrays for readability; AUTHOR_INPUT.json retains authoritative values. "
        "Read acceptance/probe.py and acceptance/README.md, and all source/upstream paths supplied "
        "in input.inventory. Do not guess other filenames.\n")
    return manifest


def validate_read_coverage(directory, authored):
    """Require actual tool output to contain every line of the long-field view."""
    required = {"VIEW_" + key.upper() + ".md": value for key, value in authored.items()
                if isinstance(value, str) and len(value) > 1600}
    events = [json.loads(line) for line in (directory / "events.jsonl").read_text().splitlines()]
    for name, value in required.items():
        path = directory / "source/candidate" / name
        if path.read_text() != value or any(len(line) > 1900 for line in value.splitlines()):
            raise ValueError("long-field view is not fully readable/exact")
        seen = set()
        for event in events:
            part = event.get("part", {})
            state = part.get("state", {})
            supplied = state.get("input", {}).get("path", "")
            if part.get("tool") == "read" and state.get("status") == "completed" and Path(supplied).resolve() == path.resolve():
                seen.update(int(n) for n in re.findall(r"^\s*(\d+):", state.get("output", ""), re.M))
        if not set(range(1, len(value.splitlines()) + 1)) <= seen:
            raise ValueError("independent reviewer did not read the full long-field view")


def has_long_line_truncation(directory):
    return "line truncated to 2000 chars" in (directory / "events.jsonl").read_text()


def verify_production(folder, production, authored, snapshot, *, allow_incomplete_review=False):
    """Recheck real receipts before any case/scene/import write, including reruns."""
    calls = folder / "calls"
    if not allow_incomplete_review and (folder / "SUPPLEMENTAL_FAILURE.json").exists():
        raise ValueError("latest complete-material review failed; do not register/re-export as usable")
    leaf_digest = json.loads((folder / "REQUEST.json").read_text())["leaf_sha256"]
    generation = calls / "blueprint-generate-aux"
    review = calls / "blueprint-spec-review-aux"
    raw = json.loads((generation / "RESULT.json").read_text())
    expected_author, expected_files = validate_generation(raw, snapshot)
    actual_files = {p.relative_to(folder / "acceptance").as_posix(): p.read_text()
                    for p in (folder / "acceptance").rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    if expected_author != authored or expected_files != actual_files:
        raise ValueError("reviewed candidate changed before registration")
    source_input = json.loads((generation / "input.json").read_text())
    expected_digest = digest({"authored": authored, "acceptance_files": actual_files, "source": source_input})
    if (production["review_input_digest"] != expected_digest
            or production["source_snapshot_digest"] != digest(snapshot)):
        raise ValueError("production provenance binding differs")
    sessions = {}
    for stage in ("discovery", "blueprint-generate-aux", "blueprint-spec-review-aux"):
        d = calls / stage
        result = json.loads((d / "RESULT.json").read_text())
        binding = json.loads((d / "BINDING.json").read_text())
        if json.loads((d / "DELIVERED.json").read_text()) != {"binding_digest": digest(binding), "result_digest": digest(result)}:
            raise ValueError("production stage checkpoint differs")
        summary = json.loads((d / "cli-summary.json").read_text())
        if summary["delivery_status"] != "delivered" or summary["requested_model"] != MODEL:
            raise ValueError("production CLI evidence missing")
        raw_path = d / "original-response.json"
        if summary.get("original_response_sha256") != hashlib.sha256(raw_path.read_bytes()).hexdigest():
            raise ValueError("raw model response changed")
        if binding["input_digest"] != digest(json.loads((d / "input.json").read_text())) or binding["source"] != manifest_files(d / "source"):
            raise ValueError("review/read input bytes changed")
        if binding["leaf_sha256"] != leaf_digest or hashlib.sha256((d / "leaf.md").read_bytes()).hexdigest() != leaf_digest:
            raise ValueError("review leaf bytes changed")
        sessions[stage] = summary["session_id"]
    if sessions != production["sessions"]:
        raise ValueError("production session identities differ")
    result = json.loads((review / "RESULT.json").read_text())
    if production["review_result_digest"] != digest(result):
        raise ValueError("review result differs")
    validate_review(result, expected_digest, sessions["blueprint-generate-aux"],
                    sessions["blueprint-spec-review-aux"], len(authored["observations"]))
    if not allow_incomplete_review:
        if "read_views" in json.loads((review / "input.json").read_text()):
            validate_read_coverage(review, authored)
        elif has_long_line_truncation(review):
            receipt_path = folder / "SUPPLEMENTAL_REVIEW.json"
            if not receipt_path.exists() or json.loads(receipt_path.read_text()).get("review_input_digest") != expected_digest:
                raise ValueError("complete-readable review required before registration")


def register_catalog(item, folder):
    receipt = json.loads((folder / "IMPORT_RECEIPT.json").read_text())
    package = folder / "atlas-development-package.zip"
    row = {"key": item["key"], "artifact_id": receipt["artifact_id"], "artifact_digest": receipt["digest"],
           "runtime": {"status": "not_run", "scope": "OpenCode Go 研究与生成、独立会话静态审阅；应用尚未开发或运行。",
                       "kind": "辅助模型生产，非严格工厂验收", "online_status": "not_checked", "strict_acceptance": False},
           "files": {"development": {"path": package.relative_to(ROOT).as_posix(),
                                       "sha256": hashlib.sha256(package.read_bytes()).hexdigest()}}}
    path = ROOT / "examples/assisted-trials/CATALOG.json"
    # Do not silently lose another producer's catalog addition.
    with path.with_suffix(".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        catalog = json.loads(path.read_text())
        existing = next((r for r in catalog["items"] if r["artifact_id"] == row["artifact_id"]), None)
        if existing and {k: v for k, v in existing.items() if k != "production_review"} != row:
            raise ValueError("catalog binding already differs")
        if not existing:
            catalog["items"].append(row)
            atomic_json(path, catalog)


DISCOVERY = """Use websearch/webfetch to find a real public permissively/open-source licensed
GitHub application relevant to input.scenario. A named lead is only a clue, verify it.
Read leaf.md fully; preserve the defining home/recurring-plan/history core. Return one
JSON object {repository:'https://github.com/owner/repo', files:[2–8 exact existing UTF-8
paths including license, README and relevant implementation], rationale, alternatives,
search_notes}. Do not invent commit or licensing. Host resolves and pins later.
Prefer a small selected source surface, each file under 180KB; no branch URLs as identity."""

AUTHOR = """Research the COMPLETE pinned source inventory under source/upstream/ and leaf.md.
Return one JSON {authored:{name,audience,objective,workflow:[steps],acceptance:[criteria],
observations:[[kind,path,line_start,line_end,statement],...],inference,features:[3–5 names],
goals:[one precise acceptance goal per feature],arch:markdown,gaps:[limitations]},
acceptance_files:{'probe.py':'full Python stdlib HTTP probe source','README.md':'how to run'}}.
Observation kind is documentation or code_observation; path is relative to the pinned
upstream root (not source/upstream prefix), and 1-based lines must exist. Distinguish
code observations, document claims, target design inference and not_run upstream status.
Do not attribute the target home anchor to an upstream generic chores feature unless
actually observed. No invented runtime verification or certification. Never copy upstream
implementation into target code. This is a cognition template, NOT an application.
Use a small localhost single-user Python stdlib HTTP/SQLite target; no dependencies.
Architecture must give exact data fields, API methods/paths/request/response shapes,
validation bounds/error codes, date recurrence rules and atomic failure semantics,
basic accessible UI, data-dir/start instructions. Cover the full confirmed scenario,
including explicit home/equipment anchoring, due tasks, completion history and next date.
Probe accepts --base-url and --case A01..A0N (N equals feature count) and verifies the
exact documented API with real assertions, including negative zero-write cases and date
edges. Use only disposable test records, no real-user deletes. A restart case may describe
operator stop/restart in README; never claim it was run. List runtime verification as
not_run. No whole-platform authentication, notifications, payment or SaaS expansion.
Make sensible unambiguous defaults and highlight user decision points in arch/gaps.
Return valid JSON only. Read input.json for the fixed scenario and source metadata."""

REVIEW = """You are a NEW independent reviewer, not the author. Read leaf.md, all supplied
source/upstream files and source/candidate files. Do not use an author transcript or
assume its claims true. Input binds the COMPLETE author result digest; echo it exactly
as input_digest. Check code/doc line citations against the actual fixed source, target
inferences separate, home+recurring care+history leaf scope, end-to-end scenario,
explicit architecture/API/error/date rules, probe correctness and meaningful negative
assertions, no upstream execution/certification claims, and clear limits.
Return JSON {input_digest,verdict:'pass'|'needs_changes',checks:{leaf_scope:boolean,
source_fidelity:boolean,design_distinction:boolean,core_journey:boolean,
architecture:boolean,acceptance:boolean,limits_and_safety:boolean},
observations:[{index:0-based author observation index,verdict:'accepted'|'rejected'|'uncertain',
reason:'specific cited explanation'}],issues:[blocking concrete findings],summary}.
Passing requires all checks true, every observation accepted, no issues. Do NOT waive
real mismatches to get pass. No search needed; source bytes are authoritative. Read only."""

READABLE_REVIEW = REVIEW + """\nFIRST read source/candidate/READING_GUIDE.md and READ_VIEWS.json.
Read source/candidate/VIEW_ARCH.md from line 1 through EOF (paginate when necessary).
It is the exact decoded original arch string; never rely on the truncated JSON line.
Other long string views are listed in READ_VIEWS.json. Read each completely. The host
checks line coverage of actual tool outputs, not just your declaration. Use the supplied
inventory, not guessed filenames. Original JSON, acceptance code and source bytes have
NOT changed. The prior review verdict/transcript is not provided; form your own findings.
"""


def complete_readable_review(manifest_path, api="http://127.0.0.1:5199/api/factory/"):
    """One explicitly authorized additional read-only session; no regeneration.

    This is a local auxiliary operation using the same budget phase/identity,
    not a strict G1 grant or recovery framework. It never replaces old receipts.
    """
    manifest = json.loads(manifest_path.read_text())
    item = manifest["items"][0]
    p = manifest_path.parent / item["key"]
    production = json.loads((p / "MODEL_PRODUCTION.json").read_text())
    imported = json.loads((p / "IMPORT_RECEIPT.json").read_text())
    authored = json.loads((p / "AUTHOR_INPUT.json").read_text())
    snapshot = json.loads((p / "source-snapshot.json").read_text())
    verify_production(p, production, authored, snapshot, allow_incomplete_review=True)
    prior = json.loads((p / "calls/blueprint-spec-review-aux/RESULT.json").read_text())
    authorization = json.loads((p / "READABLE_REVIEW_AUTHORIZATION.json").read_text())
    expected = {"model": MODEL, "campaign_id": CAMPAIGN, "phase": manifest["batch_id"],
                "artifact_id": imported["artifact_id"], "artifact_digest": imported["digest"],
                "review_input_digest": production["review_input_digest"], "prior_review_digest": digest(prior),
                "max_additional_cli_sessions": 1}
    if any(authorization.get(k) != v for k, v in expected.items()) or authorization.get("reply") != "允许":
        raise ValueError("supplemental authorization binding differs")
    materials = p / "review-readable-materials"
    if not materials.exists():
        shutil.copytree(p / "review-materials", materials)
    views = readable_candidate(materials / "candidate", authored)
    store = FactoryStore(ROOT / "application-atlas-production-pack/atlas/template-factory",
                         ROOT / "application-atlas-production-pack")
    ledger = BudgetLedger(store, campaign_id=CAMPAIGN)
    payload = json.loads((p / "calls/blueprint-spec-review-aux/input.json").read_text())
    payload["read_views"] = views
    stage = p / "calls/blueprint-spec-review-aux-readable"
    leaf = (p / "calls/blueprint-spec-review-aux/leaf.md").read_bytes()
    try:
        reviewed = checkpoint(stage, payload, READABLE_REVIEW, CLI(),
                              {"ledger": ledger, "identity": manifest["batch_id"] + ":" + item["key"],
                               "phase": manifest["batch_id"], "kind": "review", "stage": stage.name}, materials, leaf)
        summary = json.loads((stage / "cli-summary.json").read_text())
        if summary["session_id"] == production["sessions"]["blueprint-spec-review-aux"]:
            raise ValueError("supplemental review reused the old session")
        validate_read_coverage(stage, authored)
        validate_review(reviewed, production["review_input_digest"], production["sessions"]["blueprint-generate-aux"],
                        summary["session_id"], len(authored["observations"]))
        receipt = {"schema": "atlas.auxiliary-readable-review.v1", **expected,
                   "status": "passed", "session_id": summary["session_id"],
                   "result_digest": digest(reviewed), "view_hashes": views,
                   "author_input_sha256": hashlib.sha256((p / "AUTHOR_INPUT.json").read_bytes()).hexdigest(),
                   "note": "Original three calls, frozen bytes and initial review retained. No author or application execution."}
        fixed_json(p / "SUPPLEMENTAL_REVIEW.json", receipt)
        catalog_path = ROOT / "examples/assisted-trials/CATALOG.json"
        with catalog_path.with_suffix(".lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            catalog = json.loads(catalog_path.read_text())
            row = next(r for r in catalog["items"] if r["artifact_id"] == imported["artifact_id"])
            row["production_review"] = {"status": "passed", "file": {
                "path": (p / "SUPPLEMENTAL_REVIEW.json").relative_to(ROOT).as_posix(),
                "sha256": hashlib.sha256((p / "SUPPLEMENTAL_REVIEW.json").read_bytes()).hexdigest()}}
            atomic_json(catalog_path, catalog)
        return receipt
    except Exception as error:
        result_path = stage / "RESULT.json"
        result = json.loads(result_path.read_text()) if result_path.exists() else {}
        failure = {"schema": "atlas.auxiliary-readable-review-failure.v1", **expected,
                   "status": "needs_changes" if result.get("verdict") == "needs_changes" else "incomplete_materials",
                   "error": str(error), "issues": result.get("issues", []),
                   "result_digest": digest(result), "frozen_content_unchanged": True}
        fixed_json(p / "SUPPLEMENTAL_FAILURE.json", failure)
        item.update(state="blocked_review", error=str(error))
        save(manifest_path, manifest)
        catalog_path = ROOT / "examples/assisted-trials/CATALOG.json"
        with catalog_path.with_suffix(".lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            catalog = json.loads(catalog_path.read_text())
            row = next(r for r in catalog["items"] if r["artifact_id"] == imported["artifact_id"])
            row["production_review"] = {"status": failure["status"], "file": {
                "path": (p / "SUPPLEMENTAL_FAILURE.json").relative_to(ROOT).as_posix(),
                "sha256": hashlib.sha256((p / "SUPPLEMENTAL_FAILURE.json").read_bytes()).hexdigest()}}
            atomic_json(catalog_path, catalog)
        # Only this new auxiliary candidate is withdrawn. Original source and
        # case research survive and can be reused. No strict job/grant changes.
        artifact = next(a for a in store.artifacts() if a["id"] == imported["artifact_id"])
        if artifact["state"] != "withdrawn":
            response = request(api, f"artifacts/{artifact['id']}/review", {
                "action": "withdraw", "expected_digest": artifact["digest"],
                "review": "Auxiliary pilot stopped: complete-material independent review needs changes. See SUPPLEMENTAL_FAILURE.json; original freeze and case evidence retained. Not G1/T08."})
            save(p / "WITHDRAW_RECEIPT.json", response)
        raise
    finally:
        save(manifest_path.parent / "BUDGET_AFTER.json", ledger.snapshot())


def run(manifest_path, api, cli=None):
    manifest = json.loads(manifest_path.read_text())
    if (manifest["model"] != MODEL or manifest["campaign_id"] != CAMPAIGN
            or len(manifest["items"]) != 1 or manifest.get("max_cli_calls") != 3):
        raise ValueError("pilot requires one item and the fixed Go model/original campaign")
    folder = manifest_path.parent
    item = manifest["items"][0]
    safe_file(item["key"])
    if "/" in item["key"]:
        raise ValueError("item key must be one directory")
    p = folder / item["key"]
    p.mkdir(exist_ok=True)
    if (p / "SUPPLEMENTAL_FAILURE.json").exists():
        raise ValueError("latest complete-material review failed; retain original draft and create a reviewed revision before import")
    store = FactoryStore(ROOT / "application-atlas-production-pack/atlas/template-factory",
                         ROOT / "application-atlas-production-pack")
    ledger = BudgetLedger(store, campaign_id=CAMPAIGN)
    cli = cli or CLI()
    # A stable auxiliary segment shares the original 500-call counter, but does
    # not extend/restart/resume any historical G1 or T08 window, grant or job.
    phase = manifest["batch_id"]
    budget = {"ledger": ledger, "identity": phase + ":" + item["key"], "phase": phase}
    baseline = ledger.snapshot()
    if not (folder / "BUDGET_BEFORE.json").exists():
        save(folder / "BUDGET_BEFORE.json", baseline)
    leaf = (store.pack / "applications" / (item["leaf"] + ".md")).read_bytes()
    store.leaf(item["leaf"])
    fixed_json(p / "REQUEST.json", {"leaf": item["leaf"], "scenario": item["scenario"],
                                   "lead": item.get("case_lead"), "model": MODEL,
                                   "leaf_sha256": hashlib.sha256(leaf).hexdigest()})
    calls = p / "calls"
    def call(stage, payload, prompt, kind, source=None):
        # Three paid sessions max. Reentry never resets this bound or starts
        # another call for a failed/uncertain stage. Revisions need new inputs.
        if stage not in {"discovery", "blueprint-generate-aux", "blueprint-spec-review-aux"}:
            raise ValueError("unknown pilot stage")
        return checkpoint(calls / stage, payload, prompt, cli,
                          {**budget, "stage": stage, "kind": kind}, source, leaf)
    try:
        proposal = call("discovery", json.loads((p / "REQUEST.json").read_text()), DISCOVERY, "research")
        snapshot = pin_sources(proposal, p, store)
        materials = p / "materials"
        upstream = materials / "upstream"
        if not upstream.exists():
            shutil.copytree(snapshot["local_root"], upstream)
        if manifest_files(upstream) != snapshot["files"]:
            raise ValueError("generation source differs from host-pinned files")
        source_input = {"scenario": item["scenario"], "source": {k: v for k, v in snapshot.items() if k != "local_root"},
                        "inventory": [{"path": name, "lines": len((upstream / name).read_text().splitlines())}
                                      for name in snapshot["files"]]}
        generated = call("blueprint-generate-aux", source_input, AUTHOR, "production", materials)
        authored, files = validate_generation(generated, snapshot)
        review_materials = p / "review-materials"
        if not (review_materials / "upstream").exists():
            shutil.copytree(upstream, review_materials / "upstream")
        if manifest_files(review_materials / "upstream") != snapshot["files"]:
            raise ValueError("review source differs")
        candidate = review_materials / "candidate"
        candidate.mkdir(exist_ok=True)
        fixed_json(candidate / "AUTHOR_INPUT.json", authored)
        for name, content in files.items():
            target = candidate / "acceptance" / safe_file(name)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_text() != content:
                raise ValueError("candidate file changed")
            target.write_text(content)
        review_digest = digest({"authored": authored, "acceptance_files": files, "source": source_input})
        review_payload = {**source_input, "input_digest": review_digest, "checks": list(CHECKS)}
        prompt = REVIEW
        format_path = p / "REVIEW_FORMAT.json"
        if format_path.exists():
            review_format = json.loads(format_path.read_text())["version"]
        else:
            prior_input = calls / "blueprint-spec-review-aux/input.json"
            review_format = manifest.get("review_format", (2 if "read_views" in json.loads(prior_input.read_text()) else 1) if prior_input.exists() else 2)
            fixed_json(format_path, {"version": review_format})
        if review_format == 2:
            review_payload["read_views"] = readable_candidate(candidate, authored)
            prompt = READABLE_REVIEW
        reviewed = call("blueprint-spec-review-aux", review_payload, prompt, "review", review_materials)
        if review_format == 2:
            validate_read_coverage(calls / "blueprint-spec-review-aux", authored)
        elif has_long_line_truncation(calls / "blueprint-spec-review-aux"):
            supplement = p / "SUPPLEMENTAL_REVIEW.json"
            if not supplement.exists() or json.loads(supplement.read_text()).get("review_input_digest") != review_digest:
                raise ValueError("long JSON line truncated during review; full-material review required before registration")
        summaries = {stage: json.loads((calls / stage / "cli-summary.json").read_text()) for stage in
                     ("discovery", "blueprint-generate-aux", "blueprint-spec-review-aux")}
        validate_review(reviewed, review_digest, summaries["blueprint-generate-aux"]["session_id"],
                        summaries["blueprint-spec-review-aux"]["session_id"], len(authored["observations"]))
        fixed_json(p / "AUTHOR_INPUT.json", authored)
        for name, content in files.items():
            target = p / "acceptance" / safe_file(name)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_text() != content:
                raise ValueError("fixed acceptance changed")
            target.write_text(content)
        production = {"schema": "atlas.auxiliary-model-production.v1", "mode": "opencode-cli-go",
                      "model": MODEL, "campaign_id": CAMPAIGN, "phase": phase,
                      "review_status": "passed", "review_input_digest": review_digest,
                      "review_result_digest": digest(reviewed),
                      "source_snapshot_digest": digest(snapshot),
                      "controlled_opencode_calls_added": 3,
                      "sessions": {stage: summary["session_id"] for stage, summary in summaries.items()},
                      "upstream_runtime": "not_run", "application_runtime": "not_run",
                      "strict_acceptance": False}
        fixed_json(p / "MODEL_PRODUCTION.json", production)
        item["production_mode"] = "opencode-cli-go"
        item.update(produce(folder, item, store, api, manifest["batch_id"]))
        register_catalog(item, p)
        item["state"] = "registered_template_only"
        item.pop("error", None)
        save(manifest_path, manifest)
        save(folder / "BUDGET_AFTER.json", ledger.snapshot())
        return item
    except Exception as error:
        # Preserve all initial evidence; do not create a new identity/retry to
        # bypass an invalid/unfinished review or provider failure.
        item.update(state="blocked", error=str(error))
        save(manifest_path, manifest)
        failure = {"error": str(error), "code": getattr(error, "code", "pilot_failed"),
                   "recorded_at": datetime.now(timezone.utc).isoformat()}
        if not (p / "FAILURE.json").exists():
            save(p / "FAILURE.json", failure)
        save(folder / "BUDGET_AFTER.json", ledger.snapshot())
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--api", default="http://127.0.0.1:5199/api/factory/")
    parser.add_argument("--complete-readable-review", action="store_true",
                        help="Consume the one explicitly bound auxiliary supplemental review; never regenerate")
    args = parser.parse_args()
    manifest = args.manifest.resolve()
    with (manifest.parent / ".producer.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = complete_readable_review(manifest, args.api) if args.complete_readable_review else run(manifest, args.api)
        print(json.dumps(result, ensure_ascii=False, indent=2))
