"""Durable, single-coordinator full-leaf auxiliary production. No application runs."""

import argparse
import concurrent.futures
import fcntl
import hashlib
import io
import json
import os
import plistlib
from pathlib import Path
import shutil
import signal
import sqlite3
import subprocess
import threading
import time
import urllib.request
import urllib.error
import zipfile

from produce_batch import ROOT, produce
from produce_with_opencode import (
    CAMPAIGN,
    CLI,
    checkpoint,
    fixed_json,
    manifest_files,
    pin_sources,
    readable_candidate,
    register_catalog,
    safe_file,
    validate_read_coverage,
    validate_review,
)
from template_factory.store import FactoryStore, FactoryError, digest
from template_factory.full_auxiliary import FullAuxiliaryService, MODEL
from template_factory.auxiliary_workflow import WorkflowService, STEPS
from template_factory.cases import CaseLibrary
from template_factory.sources import github_repo, request_bytes
from atlas_runtime import atomic_json
import full_leaf_profiles as profiles

DEFAULT_ROOT = ROOT / "docs/template-factory/full-leaf-auxiliary-2026-10-21"
PLAN_ID = "full-leaf-auxiliary-2026-10-21"
PUBLISH = threading.Lock()
GLOBAL_CODES = {
    "full_plan_integrity",
    "full_plan_binding",
    "budget_deadline",
    "budget_round_boundary",
    "budget_exhausted",
    "budget_paused",
    "full_plan_paused",
    "full_uncertain",
    "full_provider_unavailable",
    "workflow_integrity",
    "workflow_host_error",
}
TECH_CODES = {
    "cli_protocol",
    "cli_timeout",
    "cli_failed",
    "cli_no_result",
    "cli_output_truncated",
}
LOCAL_CODES = {
    "auxiliary_content",
    "source_unavailable",
    "source_selection_invalid",
    "leaf_delivery_error",
    *TECH_CODES,
    "budget_retry_limit",
    "budget_leaf_exhausted",
    "budget_first_pass_reserve",
}


def leaf_failure_code(error, stage):
    # Unknown exceptions are host failures.  A leaf may continue only when a
    # known, explicitly classified content or per-item delivery failure occurs.
    code = getattr(error, "code", None)
    if isinstance(error, sqlite3.DatabaseError):
        return "workflow_host_error"
    if isinstance(error, OSError) and error.errno == __import__("errno").ENOSPC:
        return "workflow_host_error"
    if code in GLOBAL_CODES:
        return code
    if code in LOCAL_CODES:
        return code
    if isinstance(error, urllib.error.HTTPError) and error.code in {403, 429, 500, 502, 503, 504}:
        code = "full_provider_unavailable"
    elif (
        isinstance(error, FactoryError)
        and code == "source_download_failed"
        and isinstance(error.__cause__, urllib.error.HTTPError)
        and error.__cause__.code in {404, 410}
    ):
        code = "source_unavailable"
    elif (
        isinstance(error, FactoryError)
        and code == "source_download_failed"
        and isinstance(error.__cause__, urllib.error.URLError)
    ):
        code = "full_provider_unavailable"
    elif stage == "source_pin" and isinstance(error, urllib.error.HTTPError) and error.code in {404, 410}:
        code = "source_unavailable"
    elif (
        stage == "freeze_import_export"
        and isinstance(error, urllib.error.HTTPError)
        and error.code == 422
    ) or (
        stage == "verify_download"
        and isinstance(error, urllib.error.HTTPError)
        and error.code in {404, 410, 422}
    ):
        code = "leaf_delivery_error"
    elif isinstance(error, urllib.error.URLError):
        code = "full_provider_unavailable"
    return code if code in GLOBAL_CODES or code in LOCAL_CODES else "workflow_host_error"


def load(path):
    return json.loads(Path(path).read_text())


def canonical_github_repo(value):
    """Validate a GitHub repository URL before case-insensitive identity matching."""
    try:
        return github_repo(value).casefold()
    except (FactoryError, ValueError) as error:
        raise FactoryError(
            "selected source is not a valid GitHub repository URL",
            "source_selection_invalid",
            409,
        ) from error


def validate_research_source_selection(research):
    """Reject malformed model source choices as local selection failures."""
    canonical_github_repo(research.get("repository"))
    files = research.get("files")
    try:
        if not isinstance(files, list) or not 2 <= len(files) <= 8:
            raise ValueError("select 2–8 distinct small source files")
        normalized = [safe_file(name) for name in files]
        if normalized != files or len(set(normalized)) != len(normalized):
            raise ValueError("source selection contains duplicate or non-canonical paths")
        if not any(
            Path(name).name.lower().startswith(("license", "copying", "notice"))
            for name in normalized
        ):
            raise ValueError("license text must be among pinned files")
    except ValueError as error:
        raise FactoryError(str(error), "source_selection_invalid", 409) from error


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def materialize_case_snapshot(snapshot, folder, store, *, namespace):
    """Recreate bytes for a canonical CaseLibrary pin without resolving HEAD.

    CaseLibrary snapshots intentionally contain provenance and hashes, not a
    machine-specific local_root. Reuse its exact commit and manifest to fill
    the normal source cache; never replace a mismatching cached file.
    """
    repository = snapshot.get("repository")
    commit = snapshot.get("commit_sha")
    files = snapshot.get("files")
    if (
        not isinstance(files, dict)
        or not files
        or not isinstance(commit, str)
        or len(commit) != 40
        or any(ch not in "0123456789abcdef" for ch in commit)
    ):
        raise ValueError("reused case snapshot lacks a fixed commit/file manifest")
    license_info = snapshot.get("license") or {}
    license_spdx = license_info.get("spdx_id")
    license_files = snapshot.get("license_files")
    if (
        not isinstance(license_spdx, str)
        or not license_spdx.strip()
        or license_spdx.upper() in {"NOASSERTION", "NONE"}
        or not isinstance(license_files, list)
        or not license_files
        or any(name not in files for name in license_files)
    ):
        raise FactoryError("source license unclear; stop before generation", "source_unavailable", 409)
    try:
        repo = github_repo(repository)
    except (FactoryError, ValueError, TypeError) as error:
        raise FactoryError(
            "trusted case snapshot has an invalid repository identity",
            "workflow_integrity",
            409,
        ) from error
    source_root = Path(store.root) / "sources" / namespace
    local = source_root / folder.parent.name / folder.name
    local.mkdir(parents=True, exist_ok=True)
    local = local.resolve(strict=True)
    for name, expected in files.items():
        relative = Path(name)
        if (not name or relative.is_absolute() or "\\" in name
                or any(part in {"", ".", ".."} for part in name.split("/"))):
            raise ValueError("reused source manifest contains an unsafe path")
        if (
            not isinstance(expected, str)
            or len(expected) != 64
            or any(ch not in "0123456789abcdef" for ch in expected)
        ):
            raise ValueError("reused source manifest contains an invalid SHA-256")
        target = local / relative
        current = local
        for part in relative.parts[:-1]:
            current = current / part
            if current.is_symlink():
                raise ValueError("reused source path contains a symlink")
            current.mkdir(exist_ok=True)
        if target.is_symlink():
            raise ValueError("reused source path contains a symlink")
        try:
            target.resolve(strict=False).relative_to(local)
        except ValueError as error:
            raise ValueError("reused source path escapes its snapshot root") from error
        if target.exists():
            if target.is_symlink() or not target.is_file() or sha(target) != expected:
                raise FactoryError(
                    "cached reused source bytes differ from fixed case digest",
                    "workflow_integrity",
                    409,
                )
            continue
        data = request_bytes(
            f"https://raw.githubusercontent.com/{repo}/{commit}/{name}", 180_000
        )
        data.decode("utf-8")
        if hashlib.sha256(data).hexdigest() != expected:
            raise FactoryError(
                "downloaded fixed-commit bytes differ from case digest",
                "workflow_integrity",
                409,
            )
        target.write_bytes(data)
    if manifest_files(local) != files:
        raise FactoryError(
            "materialized reused source inventory differs",
            "workflow_integrity",
            409,
        )
    result = {
        key: value
        for key, value in snapshot.items()
        if key not in {"snapshot_id", "file_manifest_digest", "local_root", "_validated_root"}
    }
    result["local_root"] = str(local.resolve())
    pin = {
        "repository": repository,
        "commit_sha": commit,
        "paths": list(files),
        "collected_at": snapshot.get("collected_at"),
        "repository_id": snapshot.get("repo_id"),
        "license_spdx": license_spdx,
    }
    fixed_json(folder / "SOURCE_PIN.json", pin)
    fixed_json(folder / "source-snapshot.json", result)
    return result


def shared_provider_fault(error):
    # A completed HTTP response with malformed/incomplete model output is a
    # per-leaf protocol failure, not evidence of shared auth/network failure.
    # Keep the original charged receipt and apply the same one-recovery limit.
    if "provider.invalid-output" in str(error).lower():
        return False
    return getattr(error, "code", None) == "cli_unavailable" or (
        getattr(error, "code", None) == "cli_failed"
        and any(
            word in str(error).lower()
            for word in (
                "unauthorized",
                "insufficient",
                "balance",
                "credit",
                "api key",
                "rate limit",
                "429",
                "connection",
                "network",
                "quota",
                "limit exceeded",
                "usage limit",
                "too many requests",
                "authentication",
                "401",
                "402",
                "403",
                "502",
                "503",
                "504",
                "service unavailable",
                "overloaded",
            )
        )
    )


def compact_completed_work(work):
    """Keep authoritative calls/frozen ZIPs; compress only duplicate audit copies."""
    audit = work / "audit"
    if audit.exists():
        archive = work / "audit-evidence.zip"
        expected = {
            p.relative_to(audit).as_posix(): sha(p)
            for p in audit.rglob("*")
            if p.is_file()
        }
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
            for name in sorted(expected):
                z.write(audit / name, name)
        with zipfile.ZipFile(archive) as z:
            if {
                n: hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist()
            } != expected:
                raise ValueError("audit compression changed evidence")
        atomic_json(
            work / "AUDIT_ARCHIVE.json",
            {"sha256": sha(archive), "files": expected, "raw_calls_retained": True},
        )
        shutil.rmtree(audit)
    # These are exact materialization copies of calls/*/source and frozen ZIPs.
    for name in (
        "materials",
        "review-materials",
        "packages/candidate",
        "packages/template-snapshot",
        "packages/development-package",
    ):
        path = work / name
        if path.is_dir():
            shutil.rmtree(path)


def host():
    pack = ROOT / "application-atlas-production-pack"
    store = FactoryStore(pack / "atlas/template-factory", pack)
    return store, FullAuxiliaryService(store)


def get_bytes(api, route):
    with urllib.request.urlopen(api.rstrip("/") + route, timeout=90) as response:
        return response.read()


def verify_plan(root):
    request = load(root / "AUTHORIZATION_REQUEST.json")
    for name in ("scope", "authorization"):
        if sha(ROOT / request[name]["path"]) != request[name]["sha256"]:
            raise FactoryError(
                "frozen plan authorization/scope changed", "full_plan_integrity", 409
            )
    scope = load(root / "FROZEN_SCOPE.json")
    if (
        scope["prompt_digest"] != profiles.PROMPT_DIGEST
        or scope["profile"] != profiles.VERSION
    ):
        raise FactoryError(
            "producer prompt version changed", "full_plan_integrity", 409
        )
    expected_hosts = scope.get("host_source_sha256", {})
    _, service = host()
    revision = service.host_revision(PLAN_ID)
    if revision:
        if revision["scope_sha256"] != request["scope"]["sha256"]:
            raise FactoryError(
                "host revision scope differs", "full_plan_integrity", 409
            )
        expected_hosts = revision["new_host_sha256"]
    for name, expected in expected_hosts.items():
        if sha(ROOT / name) != expected:
            raise FactoryError(
                "production host source changed: " + name, "full_plan_integrity", 409
            )
    return request, scope


def selected_scenario(work):
    """SCENARIO.json aliases scenario.json on macOS. Preserve the old bytes."""
    target = work / "SELECTED_SCENARIO.json"
    legacy = work / "SCENARIO.json"
    if not target.exists() and legacy.exists():
        original = legacy.read_bytes()
        value = json.loads(original)
        if "id" not in value:
            if value != load(work / "RESEARCH.json")["scenario"]:
                raise ValueError("legacy research scenario differs")
            preserved = work / "LEGACY_RESEARCH_SCENARIO.json"
            if preserved.exists() and preserved.read_bytes() != original:
                raise ValueError("legacy scenario preservation differs")
            legacy.rename(preserved)
            target.write_bytes(original)
            fixed_json(
                work / "SCENARIO_CHECKPOINT_MIGRATION.json",
                {
                    "original_name": "SCENARIO.json",
                    "preserved_name": preserved.name,
                    "sha256": sha(preserved),
                    "new_name": target.name,
                    "content_changed": False,
                },
            )
    return target


def freeze(root, api):
    if (root / "FROZEN_SCOPE.json").exists():
        return verify_plan(root)[1]
    store, service = host()
    baseline = service.ledger.snapshot()
    if baseline["active"]:
        raise ValueError("cannot freeze while historical calls are active")
    from export_atlas import parse_directory, slugify

    tree, leaves, duplicates = parse_directory()
    assert not duplicates
    attachment = root / "authorization/atlas-all-leaves-handoff-2026-10-21"
    draft = load(attachment / "atlas-all-leaves-inventory.json")
    catalog = json.loads(get_bytes(api, "/api/factory/assisted-templates"))
    atomic_json(root / "CATALOG_BEFORE.json", catalog)
    covered, rejected = {}, []
    for row in catalog["items"]:
        entry = row["files"]["development"]
        if not entry.get("available"):
            rejected.append(
                {
                    "artifact_id": row["artifact_id"],
                    "reason": "development package unavailable/withdrawn",
                }
            )
            continue
        data = get_bytes(api, entry["url"])
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError("existing usable download digest differs")
        import io

        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for name in (
                "HANDOFF.md",
                "KNOWLEDGE.md",
                "CURRENT_PHASE.json",
                "ACCEPTANCE_CONTRACT.json",
            ):
                assert name in z.namelist(), name
            assert (
                json.loads(z.read(".atlas-blueprint.json"))["template_digest"]
                == row["digest"]
            )
            for case in row["cases"]:
                actual = CaseLibrary(store).get_case(case["case_id"], case["revision"])
                assert actual["digest"] == case["digest"]
        covered.setdefault(row["leaf"], []).append(
            {
                "artifact_id": row["artifact_id"],
                "digest": row["digest"],
                "development_sha256": entry["sha256"],
                "cases": row["cases"],
                "runtime": row["runtime"],
            }
        )
    source_order = [slugify(x["name"]) for x in leaves]
    assert len(source_order) == len(set(source_order))
    with sqlite3.connect(store.pack / "atlas/atlas.sqlite") as con:
        indexed = {x[0] for x in con.execute("SELECT slug FROM leaf")}
    items, exclusions = [], []
    byname = {slugify(x["name"]): x for x in leaves}
    tree_by_id = {x["id"]: x for x in tree}
    for slug in ["expense-tracking-application", "calendar-application"] + [
        x
        for x in source_order
        if x not in {"expense-tracking-application", "calendar-application"}
    ]:
        raw = store.pack / "applications" / (slug + ".md")
        if slug not in indexed or not raw.is_file():
            exclusions.append(
                {
                    "leaf": slug,
                    "reason": "missing formal leaf index or applications document",
                }
            )
            continue
        store.leaf(slug)
        ancestry = []
        section = tree_by_id.get(byname[slug]["section_id"])
        while section:
            ancestry.insert(0, {"id": section["id"], "name": section["name"]})
            section = tree_by_id.get(section["parent"])
        item = {
            "leaf": slug,
            "key": slug,
            "leaf_sha256": sha(raw),
            "classification_path": ancestry,
            "directory_section": byname[slug]["section_id"],
            "display_name": byname[slug]["name"],
            "covered": covered.get(slug, []),
        }
        if slug in {"expense-tracking-application", "calendar-application"}:
            oldkey = (
                "daily-expenses" if slug.startswith("expense") else "personal-calendar"
            )
            old = ROOT / "docs/template-factory/go-minimax-batch-2026-10-21" / oldkey
            item.update(
                fixed_scenario=load(old / "REQUEST.json")["scenario"],
                prior_failure={
                    "path": str((old / "FAILURE.json").relative_to(ROOT)),
                    "sha256": sha(old / "FAILURE.json"),
                },
            )
            if slug.startswith("expense"):
                item["reuse_source"] = {
                    "path": str(old.relative_to(ROOT)),
                    "snapshot_sha256": sha(old / "source-snapshot.json"),
                    "proposal_sha256": sha(old / "audit/discovery/RESULT.json"),
                }
        items.append(item)
    protected = {}
    for path in list((ROOT / "docs/template-factory").rglob("*.zip")) + list(
        (ROOT / "examples").glob("*-trial/data/*.sqlite3")
    ):
        if root not in path.parents:
            protected[str(path.relative_to(ROOT))] = sha(path)
    atomic_json(root / "PRESERVATION_BEFORE.json", protected)
    atomic_json(root / "BUDGET_BEFORE.json", baseline)
    atomic_json(root / "CASES_BEFORE.json", CaseLibrary(store).list_cases())
    backup = store.root / "operator-evidence" / PLAN_ID
    backup.mkdir(parents=True, exist_ok=True)
    with (
        store.connect() as source,
        sqlite3.connect(backup / "factory-before.sqlite") as target,
    ):
        source.backup(target)
    authorization = attachment / "CODEX_INSTRUCTION.txt"
    scope = {
        "schema": "atlas.full-leaf-auxiliary-scope.v1",
        "full_plan_id": PLAN_ID,
        "source_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "directory_sha256": sha(store.pack / "DIRECTORY.md"),
        "attachment_sha256": sha(
            root / "authorization/Atlas-all-leaves-Codex-handoff-2026-10-21.zip"
        ),
        "authorization_sha256": sha(authorization),
        "profile": profiles.VERSION,
        "prompt_digest": profiles.PROMPT_DIGEST,
        "review_format": 2,
        "raw_directory_leaves": len(source_order),
        "attachment_directory_agrees": set(source_order)
        == {x["slug"] for x in draft["leaves"]},
        "formal_scope": len(items),
        "exclusions": exclusions,
        "rejected_coverage": rejected,
        "covered_distinct_leaves": sum(bool(x["covered"]) for x in items),
        "pending": sum(not x["covered"] for x in items),
        "indexed_outside_directory": sorted(indexed - set(source_order)),
        "host_source_sha256": {
            str(p.relative_to(ROOT)): sha(p)
            for p in [
                Path(__file__).resolve(),
                Path(profiles.__file__).resolve(),
                ROOT
                / "application-atlas-production-pack/template_factory/full_auxiliary.py",
                ROOT / "application-atlas-production-pack/template_factory/budget.py",
                ROOT / "examples/assisted-trials/produce_batch.py",
                ROOT / "examples/assisted-trials/produce_with_opencode.py",
                ROOT / "examples/assisted-trials/export_trial.py",
            ]
        },
        "items": items,
    }
    atomic_json(root / "FROZEN_SCOPE.json", scope)
    request = {
        "schema": "atlas.full-leaf-auxiliary-authorization.v1",
        "full_plan_id": PLAN_ID,
        "campaign_id": CAMPAIGN,
        "phase": "auxiliary-full-" + PLAN_ID,
        "baseline": baseline["cli_sessions_used"],
        "max_new_calls": 7200,
        "per_leaf_calls": 6,
        "concurrency": 2,
        "batch_size": 20,
        "window_seconds": 2592000,
        "model": MODEL,
        "scope": {
            "path": str((root / "FROZEN_SCOPE.json").relative_to(ROOT)),
            "sha256": sha(root / "FROZEN_SCOPE.json"),
        },
        "authorization": {
            "path": str(authorization.relative_to(ROOT)),
            "sha256": sha(authorization),
        },
    }
    atomic_json(root / "AUTHORIZATION_REQUEST.json", request)
    return scope


class CoordinatedCLI(CLI):
    def __init__(self, root, service):
        super().__init__()
        self.root, self.service = root, service

    def run(self, directory, prompt, model, timeout, cancelled, progress, **kwargs):
        while True:
            verify_plan(self.root)
            try:
                return super().run(
                    directory,
                    prompt,
                    model,
                    timeout,
                    lambda: self.service.control_state(PLAN_ID) == "stopped",
                    progress,
                    **kwargs,
                )
            except FactoryError as error:
                if error.code != "budget_concurrency":
                    raise
                with (directory / "SLOT_WAITS.jsonl").open("a") as out:
                    out.write(
                        json.dumps(
                            {
                                "at": time.time(),
                                "code": error.code,
                                "no_model_started": True,
                            }
                        )
                        + "\n"
                    )
                if self.service.control_state(PLAN_ID) != "running":
                    raise FactoryError(
                        "plan paused waiting for model slot", "full_plan_paused", 409
                    )
                time.sleep(5)


def _verify_call(path, leaf_sha, model):
    binding, result, receipt, summary = (
        load(path / name)
        for name in (
            "BINDING.json",
            "RESULT.json",
            "DELIVERED.json",
            "cli-summary.json",
        )
    )
    if receipt != {"binding_digest": digest(binding), "result_digest": digest(result)}:
        raise ValueError("full-stage receipt differs")
    if (
        binding["model"] != model
        or summary["requested_model"] != model
        or summary["delivery_status"] != "delivered"
    ):
        raise ValueError("full-stage model/delivery differs")
    if binding["leaf_sha256"] != leaf_sha or sha(path / "leaf.md") != leaf_sha:
        raise ValueError("full-stage leaf differs")
    if binding["input_digest"] != digest(load(path / "input.json")) or binding[
        "source"
    ] != manifest_files(path / "source"):
        raise ValueError("full-stage input/source changed")
    if sha(path / "original-response.json") != summary["original_response_sha256"]:
        raise ValueError("full-stage raw response changed")
    return summary


def verify_full_production(folder, production, authored, snapshot):
    request = load(folder / "REQUEST.json")
    lineage = load(folder / "LINEAGE.json")
    if (
        production["full_plan_id"] != request["full_plan_id"]
        or request["full_plan_id"] != lineage["full_plan_id"]
        or lineage["leaf_sha256"] != request["leaf_sha256"]
    ):
        raise ValueError("full production lineage differs")
    paths = load(folder / "STAGE_PATHS.json")
    summaries = {}
    stage_models = {}
    _, model_service = host()
    allowed_models = set(model_service.allowed_models(PLAN_ID))
    for stage, path in paths.items():
        binding = load(folder / path / "BINDING.json")
        actual_model = binding.get("model")
        if actual_model not in allowed_models:
            raise ValueError("full-stage model is not authorized for this plan")
        summaries[stage] = _verify_call(folder / path, request["leaf_sha256"], actual_model)
        stage_models[stage] = actual_model
    author = folder / paths["blueprint-generate-aux"]
    reviewer = folder / paths["blueprint-spec-review-aux"]
    inputs = load(author / "input.json")
    if inputs["source"] != {
        k: v for k, v in snapshot.items() if k != "local_root"
    } or inputs["scenario"] != load(
        folder
        / (
            "SELECTED_SCENARIO.json"
            if (folder / "SELECTED_SCENARIO.json").exists()
            else "SCENARIO.json"
        )
    ):
        raise ValueError("full source/scenario differs from author inputs")
    actual, files = profiles.validate_author(
        load(author / "RESULT.json"), snapshot, inputs
    )
    expected_files = {
        p.relative_to(folder / "acceptance").as_posix(): p.read_text()
        for p in (folder / "acceptance").rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    if actual != authored or files != expected_files:
        raise ValueError("full production changed after review")
    identity = digest(
        {"authored": authored, "acceptance_files": files, "source": inputs}
    )
    review = load(reviewer / "RESULT.json")
    if (
        production["review_input_digest"] != identity
        or production["review_result_digest"] != digest(review)
        or production["source_snapshot_digest"] != digest(snapshot)
    ):
        raise ValueError("full review/source digest differs")
    if production["sessions"] != {k: v["session_id"] for k, v in summaries.items()}:
        raise ValueError("full stage sessions differ")
    recorded_models = production.get("stage_models")
    if recorded_models is not None and recorded_models != stage_models:
        raise ValueError("full stage models differ")
    if production.get("model") != summaries["blueprint-generate-aux"]["requested_model"]:
        raise ValueError("production author model differs")
    validate_read_coverage(reviewer, authored)
    validate_review(
        review,
        identity,
        summaries["blueprint-generate-aux"]["session_id"],
        summaries["blueprint-spec-review-aux"]["session_id"],
        len(authored["observations"]),
    )
    if (
        production["profile"] != profiles.VERSION
        or production["prompt_digest"] != profiles.PROMPT_DIGEST
    ):
        raise ValueError("full profile differs")


def stage_call(
    root,
    service,
    item,
    work,
    stage,
    payload,
    prompt,
    kind,
    source=None,
    lane="first",
    validator=None,
):
    pathsfile = work / "STAGE_PATHS.json"
    paths = load(pathsfile) if pathsfile.exists() else {}
    relative = paths.setdefault(stage, "calls/" + stage)
    atomic_json(pathsfile, paths)
    store = service.store
    leaf = (store.pack / "applications" / (item["leaf"] + ".md")).read_bytes()
    if hashlib.sha256(leaf).hexdigest() != item["leaf_sha256"]:
        raise ValueError("frozen leaf changed; do not swap input")
    budget = {
        "ledger": service.ledger,
        "identity": PLAN_ID + ":" + item["leaf"],
        "phase": "auxiliary-full-" + PLAN_ID,
        "plan_id": PLAN_ID,
        "job_id": PLAN_ID + ":" + item["leaf"] + ":" + work.name,
        "stage": lane + "/" + stage + "/" + work.name,
        "kind": kind,
    }
    path = work / relative
    if (
        (path / "LAUNCH_INTENT.json").exists()
        and not (path / "DELIVERED.json").exists()
        and not (path / "cli-summary.json").exists()
    ):
        proof_stage = (
            ("protocol" if "-protocol-1" in relative else lane)
            + "/"
            + stage
            + "/"
            + work.name
        )
        service.prove_unlaunched(PLAN_ID, item["leaf"], work.name, proof_stage, path)
    if (
        (path / "LAUNCH_INTENT.json").exists()
        and not (path / "DELIVERED.json").exists()
        and (path / "cli-summary.json").exists()
    ):
        old_summary = load(path / "cli-summary.json")
        if (
            old_summary.get("cli_status") == "not_started"
            and old_summary.get("output_observed") is False
        ):
            suffix = 1
            while (work / (relative + "-not-started-" + str(suffix))).exists():
                suffix += 1
            next_path = relative + "-not-started-" + str(suffix)
            fixed_json(
                work / (next_path + ".json"),
                {
                    "proven_not_started_parent": relative,
                    "summary_sha256": sha(path / "cli-summary.json"),
                    "charge_released": True,
                },
            )
            paths[stage] = next_path
            atomic_json(pathsfile, paths)
            relative = next_path
            path = work / relative
    if "-protocol-1" in relative:
        budget["stage"] = "protocol/" + stage + "/" + work.name

    effective_model = service.effective_model(PLAN_ID)
    # Existing reservations/checkpoints remain bound to the model that actually
    # owned that attempt. A protocol successor gets the current authorized model.
    if (path / "BINDING.json").exists():
        call_model = load(path / "BINDING.json")["model"]
        if call_model not in service.allowed_models(PLAN_ID):
            raise FactoryError(
                "checkpoint model is not authorized for this plan",
                "full_plan_integrity",
                409,
            )
    else:
        call_model = effective_model

    def deliver(target, selected_budget):
        try:
            try:
                result = checkpoint(
                    target,
                    payload,
                    prompt,
                    CoordinatedCLI(root, service),
                    selected_budget,
                    source,
                    leaf,
                    model=call_model,
                )
            except ValueError as error:
                if str(error) in {
                    "checkpoint read-source changed",
                    "checkpoint leaf changed",
                    "fixed input changed: input.json; use a new output/version",
                    "fixed input changed: BINDING.json; use a new output/version",
                    "checkpoint result differs from delivered binding",
                    "recovered raw result differs",
                }:
                    raise FactoryError(str(error), "workflow_integrity", 409) from error
                raise
        except FactoryError as error:
            if shared_provider_fault(error):
                fixed_json(
                    target / "SHARED_PROVIDER_FAILURE.json",
                    {"error": str(error), "code": error.code},
                )
                raise FactoryError(
                    "shared provider unavailable: " + str(error),
                    "full_provider_unavailable",
                    503,
                ) from error
            raise
        if stage == "discovery":
            try:
                profiles.validate_research(result)
            except (ValueError, TypeError, KeyError) as error:
                fixed_json(
                    target / "SCHEMA_FAILURE.json",
                    {"raw_result_digest": digest(result), "error": str(error)},
                )
                raise FactoryError(
                    "research JSON schema: " + str(error), "cli_protocol", 409
                ) from error
        if validator is not None:
            try:
                validator(result, target)
            except (ValueError, TypeError, KeyError) as error:
                fixed_json(
                    target / "SCHEMA_FAILURE.json",
                    {"raw_result_digest": digest(result), "error": str(error)},
                )
                raise FactoryError(
                    "complete-review protocol: " + str(error), "cli_protocol", 409
                ) from error
        return result

    try:
        return deliver(path, budget)
    except Exception as error:
        summary = (
            load(path / "cli-summary.json")
            if (path / "cli-summary.json").exists()
            else {}
        )
        if getattr(error, "code", None) in GLOBAL_CODES:
            raise
        if (
            (path / "SHARED_PROVIDER_FAILURE.json").exists()
            and shared_provider_fault(
                FactoryError(
                    load(path / "SHARED_PROVIDER_FAILURE.json")["error"],
                    "cli_failed",
                    503,
                )
            )
            and (
                "-protocol-1" in relative or (work / "PROTOCOL_SUCCESSOR.json").exists()
            )
        ):
            raise FactoryError(
                "shared provider unavailable: "
                + load(path / "SHARED_PROVIDER_FAILURE.json")["error"],
                "full_provider_unavailable",
                503,
            ) from error
        if shared_provider_fault(error):
            raise FactoryError(
                "shared provider unavailable: " + str(error),
                "full_provider_unavailable",
                503,
            ) from error
        if (path / "LAUNCH_INTENT.json").exists() and not summary:
            raise FactoryError(
                "launched call has no final summary; reconcile before resuming",
                "full_uncertain",
                409,
            ) from error
        technical = (
            summary.get("failure_code") in TECH_CODES
            or (path / "SCHEMA_FAILURE.json").exists()
        )
        if (path / "original-response.json").exists() and not (
            path / "PROTOCOL_DIAGNOSTIC.json"
        ).exists():
            try:
                json.loads(load(path / "original-response.json").get("text", ""))
            except json.JSONDecodeError as diagnostic:
                atomic_json(
                    path / "PROTOCOL_DIAGNOSTIC.json",
                    {
                        "error": str(diagnostic),
                        "line": diagnostic.lineno,
                        "column": diagnostic.colno,
                        "position": diagnostic.pos,
                        "original_sha256": sha(path / "original-response.json"),
                    },
                )
        if technical and "-protocol-1" not in relative:
            if (work / "PROTOCOL_SUCCESSOR.json").exists():
                raise FactoryError(
                    "one protocol recovery already used; original failed output retained",
                    "budget_retry_limit",
                    409,
                ) from error
            # One new, explicitly charged successor across all stages of a leaf.
            successor = "calls/" + stage + "-protocol-1"
            fixed_json(
                work / "PROTOCOL_SUCCESSOR.json",
                {
                    "parent_path": relative,
                    "parent_summary_sha256": sha(path / "cli-summary.json"),
                    "reason": summary.get("failure_code") or "research_schema",
                    "input_digest": digest(payload),
                    "profile": profiles.VERSION,
                },
            )
            paths[stage] = successor
            atomic_json(pathsfile, paths)
            budget["stage"] = "protocol/" + stage + "/" + work.name
            call_model = effective_model
            return deliver(work / successor, budget)
        raise


def save_accepted_research(
    service,
    item,
    work,
    authored,
    snapshot,
    review,
    identity,
    author_session,
    review_session,
):
    """A rejected template must not hide separately accepted source research."""
    if review.get("input_digest") != identity or author_session == review_session:
        return
    observations = review.get("observations", [])
    if (
        review.get("checks", {}).get("source_fidelity") is not True
        or len(observations) != len(authored["observations"])
        or {x.get("index") for x in observations} != set(range(len(observations)))
        or any(
            x.get("verdict") != "accepted" or not x.get("reason") for x in observations
        )
    ):
        return
    with PUBLISH:
        library = CaseLibrary(service.store)
        case_id = (
            "case:repo:"
            + hashlib.sha256(snapshot["repository"].encode()).hexdigest()[:24]
            + ":"
            + snapshot["commit_sha"]
        )
        for case in library.list_cases():
            if any(
                s["repository"] == snapshot["repository"]
                and s["commit_sha"] == snapshot["commit_sha"]
                and s["files"] == snapshot["files"]
                for s in case["source_snapshots"]
            ):
                case_id = case["case_id"]
                break
        scene_input = {
            k: authored[k]
            for k in ("name", "audience", "objective", "workflow", "acceptance")
        }
        scene_input.update(leaf=item["leaf"], status="draft")
        existing = [
            s
            for s in service.store.scenarios(item["leaf"])
            if all(s.get(k) == v for k, v in scene_input.items())
        ]
        scene = existing[0] if existing else service.store.save_scenario(scene_input)
        evidence = []
        for n, (kind, path, start, end, statement) in enumerate(
            authored["observations"]
        ):
            evidence.append(
                {
                    "evidence_id": "ev_full_" + str(n),
                    "kind": kind,
                    "statement": statement,
                    "location": (
                        {
                            "commit_sha": snapshot["commit_sha"],
                            "path": path,
                            "file_digest": snapshot["files"][path],
                            "line_start": start,
                            "line_end": end,
                        }
                        if kind == "code_observation"
                        else {
                            "url": snapshot["repository"]
                            + "/blob/"
                            + snapshot["commit_sha"]
                            + "/"
                            + path,
                            "material_version": snapshot["commit_sha"],
                            "content_digest": snapshot["files"][path],
                        }
                    ),
                }
            )
        payload = {
            "case_id": case_id,
            "app_name": authored["repo_name"],
            "source_snapshots": [snapshot],
            "research": {
                "summary": "Independently accepted fixed source observations; template status is separate.",
                "scope": authored["objective"],
                "unknowns": [
                    "Upstream not run; target not run; template may still require revision."
                ],
                "input_digest": identity,
                "task_id": PLAN_ID + ":" + item["leaf"] + ":" + work.name,
            },
            "observations": evidence,
            "scenario_links": [
                {
                    "scenario_id": scene["id"],
                    "scenario_revision": scene["revision"],
                    "reason": "Fixed source observations for this scenario; not a template acceptance.",
                    "evidence_ids": [x["evidence_id"] for x in evidence],
                    "adopted_scope": ["static source reference"],
                    "exclusions": ["upstream and target execution not run"],
                }
            ],
        }
        committed = library.commit_research(
            payload, PLAN_ID + ":" + item["leaf"] + ":" + work.name + ":source-review"
        )
        for obs in committed["case"]["observations"]:
            library.record_evidence_review(
                case_id,
                committed["case"]["revision"],
                obs["evidence_id"],
                "accepted",
                review_session,
                "independent_agent",
            )
        case = library.get_case(case_id, committed["case"]["revision"])
        receipt = {
            "case_id": case_id,
            "revision": case["revision"],
            "digest": case["digest"],
            "review_input_digest": identity,
            "review_session": review_session,
            "template_passed": False,
            "replayed": committed["replayed"],
        }
        original = work / "ACCEPTED_RESEARCH_RECEIPT.json"
        if original.exists():
            previous = load(original)
            if {k: v for k, v in previous.items() if k != "replayed"} != {
                k: v for k, v in receipt.items() if k != "replayed"
            }:
                raise FactoryError(
                    "accepted research binding changed", "workflow_integrity", 409
                )
            fixed_json(work / "ACCEPTED_RESEARCH_REPLAY_RECEIPT.json", receipt)
        else:
            fixed_json(original, receipt)


def workflow_outputs(*paths, url=None):
    return [
        {
            "path": str(Path(p).relative_to(ROOT)),
            "sha256": sha(p),
            **({"url": url} if url else {}),
        }
        for p in paths
    ]


def latest_failure(work):
    return work / (
        "LATEST_FAILURE.json"
        if (work / "LATEST_FAILURE.json").exists()
        else "FAILURE.json"
    )


def verify_download(work, api):
    """Real HTTP download, exact manifest/case binding; never runs target code."""
    receipt = load(work / "IMPORT_RECEIPT.json")
    data = get_bytes(api, receipt["export"]["download_url"])
    if hashlib.sha256(data).hexdigest() != receipt["exported_zip_sha256"]:
        raise FactoryError("download bytes differ", "workflow_integrity", 409)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        manifest = json.loads(z.read("HANDOFF_MANIFEST.json"))
        if manifest["template_digest"] != receipt["digest"]:
            raise FactoryError("handoff template differs", "workflow_integrity", 409)
        for name, expected in manifest["entry_sha256"].items():
            if hashlib.sha256(z.read(name)).hexdigest() != expected:
                raise FactoryError("handoff file differs", "workflow_integrity", 409)
        actual = {
            n.removeprefix("blueprint/"): hashlib.sha256(z.read(n)).hexdigest()
            for n in z.namelist()
            if n.startswith("blueprint/") and not n.endswith("/")
        }
        if actual != manifest["blueprint_sha256"]:
            raise FactoryError("blueprint files differ", "workflow_integrity", 409)
        case = json.loads(z.read("blueprint/inputs/shared-case-record.json"))
        if {k: case[k] for k in ("case_id", "revision", "digest")} != receipt[
            "case_ref"
        ]:
            raise FactoryError("download case differs", "workflow_integrity", 409)
    proof = {
        "artifact_id": receipt["artifact_id"],
        "sha256": hashlib.sha256(data).hexdigest(),
        "template_digest": receipt["digest"],
        "case_ref": receipt["case_ref"],
        "entries": manifest["entry_sha256"],
        "blueprint_files": len(actual),
        "application_runtime": "not_run",
    }
    fixed_json(work / "DOWNLOAD_VERIFIED.json", proof)
    return proof


def get_workflow_gate(service):
    gate = WorkflowService(service.store, service.campaign_id).gate(PLAN_ID)
    if gate is None:
        raise FactoryError(
            "workflow validation gate not registered", "workflow_gate", 409
        )
    return gate


def selected_first_pass_complete(items, selected_leaves):
    selected = [item for item in items if item["leaf"] in set(selected_leaves)]
    return bool(selected) and not any(
        not item.get("first_pass_done")
        and item["state"] not in {"ready_not_run", "reused"}
        for item in selected
    )


def effective_dispatch_selection(requested_leaves, persisted_leaves, known_leaves):
    requested = set(requested_leaves or [])
    persisted = set(persisted_leaves or [])
    known = set(known_leaves)
    if not requested <= known:
        raise ValueError("selected leaf is outside the frozen plan scope")
    if persisted:
        if requested and requested != persisted:
            raise ValueError("CLI selected leaves differ from the active durable dispatch")
        return persisted
    if requested:
        raise ValueError("selected run must be activated through selected start")
    return set()


def replay_completed_workflow(root, service, item, api):
    """Adopt only fully verified historical delivery; no model invocation."""
    work = ROOT / item["workdir"]
    wf = WorkflowService(service.store, service.campaign_id)
    production = load(work / "MODEL_PRODUCTION.json")
    verify_full_production(
        work,
        production,
        load(work / "AUTHOR_INPUT.json"),
        load(work / "source-snapshot.json"),
    )
    verify_download(work, api)
    output = {
        "existing_template": work / "REQUEST.json",
        "scenario": selected_scenario(work),
        "case_research": work / "source-snapshot.json",
        "generation": work / "AUTHOR_INPUT.json",
        "deterministic_check": work / "SOURCE_INPUT.json",
        "independent_review": work
        / load(work / "STAGE_PATHS.json")["blueprint-spec-review-aux"]
        / "RESULT.json",
        "freeze_import": work / "IMPORT_RECEIPT.json",
        "download": work / "DOWNLOAD_VERIFIED.json",
    }
    existing = next(
        (
            x
            for x in wf.detail(PLAN_ID, q=item["leaf"], limit=100)["items"]
            if x["leaf"] == item["leaf"]
        ),
        None,
    )
    recorded = existing["steps"] if existing else []
    if recorded and all(x["state"] in {"completed", "reused"} for x in recorded):
        for row in recorded:
            wf.begin(
                PLAN_ID, item["leaf"], row["attempt"], row["step"], row["input_digest"]
            )
        return {
            "leaf": item["leaf"],
            "artifact_id": item["artifact_id"],
            "model_calls_added": 0,
            "historical_adoption": False,
        }
    for name in STEPS:
        wf.begin(
            PLAN_ID,
            item["leaf"],
            work.name,
            name,
            digest({"verified_historical_production": production, "step": name}),
        )
        wf.complete(
            PLAN_ID,
            item["leaf"],
            work.name,
            name,
            workflow_outputs(output[name]),
            reused=True,
        )
    return {
        "leaf": item["leaf"],
        "artifact_id": item["artifact_id"],
        "model_calls_added": 0,
        "historical_adoption": True,
    }


def execute_leaf(root, service, item, api, repair=False):
    leafroot = root / "items" / item["leaf"]
    leafroot.mkdir(parents=True, exist_ok=True)
    with (leafroot / ".worker.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        work = leafroot / ("attempt-2" if repair else "attempt-1")
        work.mkdir(exist_ok=True)
        lineage = {
            "full_plan_id": PLAN_ID,
            "leaf": item["leaf"],
            "leaf_sha256": item["leaf_sha256"],
            "profile": profiles.VERSION,
            "prompt_digest": profiles.PROMPT_DIGEST,
            "parent_failure": item.get("prior_failure"),
            "content_revision": repair,
        }
        previous = leafroot / "attempt-1"
        if repair:
            lineage["parent_failure"] = {
                "path": str(latest_failure(previous).relative_to(ROOT)),
                "sha256": sha(latest_failure(previous)),
            }
        fixed_json(work / "LINEAGE.json", lineage)
        service.update_leaf(
            PLAN_ID,
            item["leaf"],
            "running",
            {
                "current_attempt": work.name,
                "first_pass_done": repair,
                "workdir": str(work.relative_to(ROOT)),
                "error": None,
                "failure_stage": None,
                "failure_code": None,
            },
        )
        wf = WorkflowService(service.store, service.campaign_id)
        step = "existing_template"
        stage = "existing_template"
        try:
            verify_plan(root)
            selected_scenario(work)
            request_path = work / "REQUEST.json"
            if not request_path.exists():
                fixed_json(
                    request_path,
                    {
                        "leaf": item["leaf"],
                        "leaf_sha256": item["leaf_sha256"],
                        "full_plan_id": PLAN_ID,
                        "profile": profiles.VERSION,
                        "model": service.effective_model(PLAN_ID),
                    },
                )
            else:
                saved_request = load(request_path)
                if (
                    saved_request.get("leaf") != item["leaf"]
                    or saved_request.get("leaf_sha256") != item["leaf_sha256"]
                    or saved_request.get("full_plan_id") != PLAN_ID
                    or saved_request.get("profile") != profiles.VERSION
                    or saved_request.get("model") not in service.allowed_models(PLAN_ID)
                ):
                    raise FactoryError(
                        "existing REQUEST.json binding is invalid",
                        "full_plan_integrity",
                        409,
                    )
            if wf.begin(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                digest(load(work / "REQUEST.json")),
            ):
                prior_catalog = json.loads(
                    get_bytes(
                        api, "/api/factory/assisted-templates?leaf=" + item["leaf"]
                    )
                )
                existing = next(
                    (
                        x
                        for x in prior_catalog["items"]
                        if x["files"].get("development", {}).get("available")
                        and (
                            not x.get("production")
                            or x["production"]["review_status"] == "passed"
                        )
                    ),
                    None,
                )
                if existing:
                    fixed_json(work / "EXISTING_TEMPLATE.json", existing)
                    # The actual download guard remains authoritative, not a cached status.
                    existing_data = get_bytes(
                        api,
                        "/api/factory/assisted-templates/"
                        + existing["artifact_id"]
                        + "/files/development",
                    )
                    if (
                        hashlib.sha256(existing_data).hexdigest()
                        != existing["files"]["development"]["sha256"]
                    ):
                        raise FactoryError(
                            "existing template download differs",
                            "workflow_integrity",
                            409,
                        )
                    wf.complete(
                        PLAN_ID,
                        item["leaf"],
                        work.name,
                        step,
                        workflow_outputs(work / "EXISTING_TEMPLATE.json"),
                        reused=True,
                    )
                    service.update_leaf(
                        PLAN_ID,
                        item["leaf"],
                        "reused",
                        {
                            "artifact_id": existing["artifact_id"],
                            "first_pass_done": True,
                            "repair_pending": False,
                        },
                    )
                    return {"leaf": item["leaf"], "state": "reused"}
                wf.complete(
                    PLAN_ID,
                    item["leaf"],
                    work.name,
                    step,
                    workflow_outputs(work / "REQUEST.json"),
                )
            if (work / "EXISTING_TEMPLATE.json").exists():
                row = next(
                    x
                    for x in wf.detail(PLAN_ID, q=item["leaf"], limit=100)["items"]
                    if x["leaf"] == item["leaf"]
                )
                if row["steps"][0]["state"] == "reused":
                    existing = load(work / "EXISTING_TEMPLATE.json")
                    data = get_bytes(
                        api,
                        "/api/factory/assisted-templates/"
                        + existing["artifact_id"]
                        + "/files/development",
                    )
                    if (
                        hashlib.sha256(data).hexdigest()
                        != existing["files"]["development"]["sha256"]
                    ):
                        raise FactoryError(
                            "existing download differs on recovery",
                            "workflow_integrity",
                            409,
                        )
                    service.update_leaf(
                        PLAN_ID,
                        item["leaf"],
                        "reused",
                        {
                            "artifact_id": existing["artifact_id"],
                            "first_pass_done": True,
                            "repair_pending": False,
                        },
                    )
                    return {"leaf": item["leaf"], "state": "reused"}
            step = "scenario"
            stage = "research"
            wf.begin(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                digest(load(work / "REQUEST.json")),
            )
            known = CaseLibrary(service.store).list_cases()
            compatible = [
                c
                for c in known
                if any(
                    s.get("leaf") == item["leaf"] for s in c.get("scenario_links", [])
                )
            ]
            if not compatible:
                compatible = [
                    c
                    for c in known
                    if any(
                        word in str(c["research"]).lower()
                        for word in item["display_name"].lower().split()
                        if len(word) > 5
                    )
                ][:8]
            research_input = {
                "leaf": item["leaf"],
                "fixed_scenario": item.get("fixed_scenario"),
                "compatible_shared_cases": [
                    {
                        "case_id": c["case_id"],
                        "revision": c["revision"],
                        "digest": c["digest"],
                        "summary": c["research"]["summary"],
                        "sources": [
                            {
                                "repository": s["repository"],
                                "commit_sha": s["commit_sha"],
                                "files": list(s["files"]),
                            }
                            for s in c["source_snapshots"]
                        ],
                    }
                    for c in compatible[:8]
                ],
            }
            if repair:
                selected_scenario(previous)
                for name in (
                    "SOURCE_PIN.json",
                    "source-snapshot.json",
                    "RESEARCH.json",
                    "SELECTED_SCENARIO.json",
                    "RESEARCH_REUSE.json",
                ):
                    if (previous / name).exists() and not (work / name).exists():
                        shutil.copyfile(previous / name, work / name)
                if not (work / "RESEARCH.json").exists():
                    raise ValueError("no fixed research for content revision")
                fixed_json(
                    work / "RESEARCH_LINEAGE.json",
                    {
                        "parent": str(previous.relative_to(ROOT)),
                        "research_sha256": sha(previous / "RESEARCH.json"),
                        "source_snapshot_sha256": sha(
                            previous / "source-snapshot.json"
                        ),
                    },
                )
            elif item.get("reuse_source") and not (work / "RESEARCH.json").exists():
                ref = item["reuse_source"]
                old = ROOT / ref["path"]
                if (
                    sha(old / "source-snapshot.json") != ref["snapshot_sha256"]
                    or sha(old / "audit/discovery/RESULT.json")
                    != ref["proposal_sha256"]
                ):
                    raise FactoryError(
                        "prior fixed source changed", "full_plan_integrity", 409
                    )
                snapshot = load(old / "source-snapshot.json")
                for path, value in snapshot["files"].items():
                    if sha(Path(snapshot["local_root"]) / path) != value:
                        raise FactoryError(
                            "prior source bytes changed", "workflow_integrity", 409
                        )
                fixed_json(work / "source-snapshot.json", snapshot)
                fixed_json(work / "RESEARCH_REUSE.json", ref)
                # Scenario is supplied, not model-authored here; author must preserve it.
                fixed_json(
                    work / "RESEARCH.json",
                    {
                        "repository": snapshot["repository"],
                        "files": list(snapshot["files"]),
                        "rationale": "Reuse the legal prior pinned research; new partitioned successor.",
                        "reuse_case_id": None,
                        "delivery_profile": "web",
                        "scenario": {
                            "name": "日常支出记录与月度分类汇总",
                            "audience": "记录个人人民币支出的本机用户",
                            "objective": item["fixed_scenario"],
                            "workflow": [
                                "管理支出分类",
                                "记录及编辑支出",
                                "按月查看金额与分类汇总",
                                "重新打开保留记录",
                            ],
                            "acceptance": [
                                "完整执行固定日常支出场景及金额重算、月份隔离、持久化"
                            ],
                        },
                    },
                )
            if not (work / "RESEARCH.json").exists():
                result = stage_call(
                    root,
                    service,
                    item,
                    work,
                    "discovery",
                    research_input,
                    profiles.DISCOVERY,
                    "research",
                )
                profiles.validate_research(result)
                fixed_json(work / "RESEARCH.json", result)
            research = load(work / "RESEARCH.json")
            profiles.validate_research(research)
            validate_research_source_selection(research)
            fixed_json(selected_scenario(work), research["scenario"])
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(selected_scenario(work), work / "RESEARCH.json"),
            )
            step = "case_research"
            wf.begin(PLAN_ID, item["leaf"], work.name, step, digest(research))
            stage = "source_pin"
            if not (work / "source-snapshot.json").exists():
                reuse_case_id = research.get("reuse_case_id")
                reused = None
                snap = None
                if reuse_case_id is not None:
                    reused = next(
                        (c for c in compatible if c["case_id"] == reuse_case_id),
                        None,
                    )
                    if reused is None:
                        raise FactoryError(
                            "selected reuse case is outside the supplied compatible cases",
                            "source_selection_invalid",
                            409,
                        )
                    selected_repo = canonical_github_repo(research["repository"])
                    snap = None
                    for candidate in reused["source_snapshots"]:
                        try:
                            candidate_repo = github_repo(candidate.get("repository"))
                        except (FactoryError, ValueError, TypeError) as error:
                            raise FactoryError(
                                "trusted case snapshot has an invalid repository identity",
                                "workflow_integrity",
                                409,
                            ) from error
                        if (candidate_repo.casefold() == selected_repo
                                and set(candidate.get("files", {})) == set(research["files"])):
                            snap = candidate
                            break
                    if snap is None:
                        raise FactoryError(
                            "selected reuse case does not contain the exact repository and files",
                            "source_selection_invalid",
                            409,
                        )
                if reused and snap:
                    materialize_case_snapshot(snap, work, service.store, namespace=PLAN_ID)
                    fixed_json(
                        work / "RESEARCH_REUSE.json",
                        {
                            "case_id": reused["case_id"],
                            "revision": reused["revision"],
                            "digest": reused["digest"],
                        },
                    )
                else:
                    try:
                        pin_sources(research, work, service.store, namespace=PLAN_ID)
                    except FactoryError as error:
                        if str(error) == "source response exceeds download limit":
                            raise FactoryError(str(error), "source_selection_invalid", 409) from error
                        if str(error) == "source license unclear; stop before generation":
                            raise FactoryError(str(error), "source_unavailable", 409) from error
                        raise
                    except ValueError as error:
                        if str(error) in {
                            "source license unclear; stop before generation",
                            "source response exceeds download limit",
                        }:
                            code = "source_unavailable" if "license" in str(error) else "source_selection_invalid"
                            raise FactoryError(str(error), code, 409) from error
                        if isinstance(error, UnicodeDecodeError):
                            raise FactoryError(str(error), "source_selection_invalid", 409) from error
                        raise
            snapshot = load(work / "source-snapshot.json")
            for name, expected in snapshot["files"].items():
                if sha(Path(snapshot["local_root"]) / name) != expected:
                    raise FactoryError("source bytes differ", "workflow_integrity", 409)
            if not (work / "upstream-evidence.zip").exists():
                with zipfile.ZipFile(
                    work / "upstream-evidence.zip", "w", zipfile.ZIP_DEFLATED
                ) as z:
                    for name in sorted(snapshot["files"]):
                        z.write(Path(snapshot["local_root"]) / name, name)
                    z.write(work / "source-snapshot.json", "source-snapshot.json")
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(
                    work / "source-snapshot.json", work / "upstream-evidence.zip"
                ),
            )
            scene = research["scenario"]
            fixed_json(selected_scenario(work), scene)
            inputs = {
                "scenario": scene,
                "fixed_scope": item.get("fixed_scenario"),
                "delivery_profile": research["delivery_profile"],
                "source": {k: v for k, v in snapshot.items() if k != "local_root"},
                "source_ids": profiles.source_ids(item["leaf_sha256"], scene, snapshot),
                "inventory": [
                    {
                        "path": n,
                        "lines": len(
                            (Path(snapshot["local_root"]) / n).read_text().splitlines()
                        ),
                    }
                    for n in snapshot["files"]
                ],
            }
            materials = work / "materials"
            materials.mkdir(exist_ok=True)
            if not (materials / "upstream").exists():
                shutil.copytree(snapshot["local_root"], materials / "upstream")
            if manifest_files(materials / "upstream") != snapshot["files"]:
                raise FactoryError("source inventory differs", "workflow_integrity", 409)
            prompt = profiles.AUTHOR
            if repair:
                feedback = load(latest_failure(previous))
                reviewfile = (
                    previous
                    / load(previous / "STAGE_PATHS.json").get(
                        "blueprint-spec-review-aux", "missing"
                    )
                    / "RESULT.json"
                )
                if reviewfile.exists():
                    feedback["review"] = load(reviewfile)
                parent_author = (
                    previous
                    / load(previous / "STAGE_PATHS.json").get(
                        "blueprint-generate-aux", "missing"
                    )
                    / "RESULT.json"
                )
                if parent_author.exists():
                    shutil.copyfile(parent_author, materials / "PARENT_CANDIDATE.json")
                inputs["revision"] = {
                    "parent_failure_sha256": sha(latest_failure(previous)),
                    "feedback": feedback,
                    "scope": "Fix existing core violations only; preserve fixed scenario, sources and delivery profile.",
                }
                prompt += "\nThis is ONE content revision. Read source/PARENT_CANDIDATE.json when supplied. Fix all concrete feedback together; do not expand scope. Return the complete revised template JSON."
            step = "generation"
            stage = "generation"
            if wf.begin(PLAN_ID, item["leaf"], work.name, step, digest(inputs)):
                generated = stage_call(
                    root,
                    service,
                    item,
                    work,
                    "blueprint-generate-aux",
                    inputs,
                    prompt,
                    "production",
                    materials,
                    lane="repair" if repair else "first",
                )
            else:
                generated = load(
                    work
                    / load(work / "STAGE_PATHS.json")["blueprint-generate-aux"]
                    / "RESULT.json"
                )
            paths = load(work / "STAGE_PATHS.json")
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(
                    work / paths["blueprint-generate-aux"] / "RESULT.json"
                ),
            )
            step = "deterministic_check"
            wf.begin(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                digest({"generated": generated, "source": inputs}),
            )
            try:
                authored, files = profiles.validate_author(generated, snapshot, inputs)
            except (ValueError, KeyError, TypeError, SyntaxError) as invalid:
                raise FactoryError(str(invalid), "auxiliary_content", 409) from invalid
            fixed_json(work / "SOURCE_INPUT.json", inputs)
            fixed_json(work / "AUTHOR_INPUT.json", authored)
            for name, content in files.items():
                p = work / "acceptance" / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content)
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(
                    work / "SOURCE_INPUT.json",
                    work / "AUTHOR_INPUT.json",
                    *[work / "acceptance" / name for name in files],
                ),
            )
            step = "independent_review"
            stage = "independent_review"
            rm = work / "review-materials"
            candidate = rm / "candidate"
            candidate.mkdir(parents=True, exist_ok=True)
            if not (rm / "upstream").exists():
                shutil.copytree(snapshot["local_root"], rm / "upstream")
            fixed_json(candidate / "AUTHOR_INPUT.json", authored)
            for name, content in files.items():
                p = candidate / "acceptance" / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content)
            identity = digest(
                {"authored": authored, "acceptance_files": files, "source": inputs}
            )
            review_input = {
                **{k: v for k, v in inputs.items() if k != "revision"},
                "input_digest": identity,
                "checks": list(profiles.CHECK_NAMES),
                "read_views": readable_candidate(candidate, authored),
            }
            if wf.begin(PLAN_ID, item["leaf"], work.name, step, identity):
                review = stage_call(
                    root,
                    service,
                    item,
                    work,
                    "blueprint-spec-review-aux",
                    review_input,
                    profiles.REVIEW,
                    "review",
                    rm,
                    lane="repair" if repair else "first",
                    validator=lambda value, target: (
                        profiles.validate_review_envelope(value, identity),
                        validate_read_coverage(target, authored),
                    ),
                )
            else:
                review = load(
                    work
                    / load(work / "STAGE_PATHS.json")["blueprint-spec-review-aux"]
                    / "RESULT.json"
                )
            paths = load(work / "STAGE_PATHS.json")
            rd = work / paths["blueprint-spec-review-aux"]
            validate_read_coverage(rd, authored)
            author_summary = load(
                work / paths["blueprint-generate-aux"] / "cli-summary.json"
            )
            review_summary = load(rd / "cli-summary.json")
            save_accepted_research(
                service,
                item,
                work,
                authored,
                snapshot,
                review,
                identity,
                author_summary["session_id"],
                review_summary["session_id"],
            )
            try:
                validate_review(
                    review,
                    identity,
                    author_summary["session_id"],
                    review_summary["session_id"],
                    len(authored["observations"]),
                )
            except ValueError as invalid:
                if review.get("verdict") == "needs_changes":
                    raise FactoryError(
                        str(invalid), "auxiliary_content", 409
                    ) from invalid
                raise
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(
                    rd / "RESULT.json", work / "ACCEPTED_RESEARCH_RECEIPT.json"
                ),
            )
            fixed_json(work / "AUTHOR_INPUT.json", authored)
            for name, content in files.items():
                p = work / "acceptance" / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content)
            summaries = {
                k: load(work / v / "cli-summary.json") for k, v in paths.items()
            }
            production = {
                "schema": "atlas.auxiliary-model-production.v1",
                "mode": "opencode-cli-go",
                "model": summaries["blueprint-generate-aux"]["requested_model"],
                "stage_models": {
                    k: load(work / v / "BINDING.json")["model"]
                    for k, v in paths.items()
                },
                "campaign_id": CAMPAIGN,
                "phase": "auxiliary-full-" + PLAN_ID,
                "full_plan_id": PLAN_ID,
                "profile": profiles.VERSION,
                "prompt_digest": profiles.PROMPT_DIGEST,
                "review_status": "passed",
                "review_input_digest": identity,
                "review_result_digest": digest(review),
                "source_snapshot_digest": digest(snapshot),
                "sessions": {k: v["session_id"] for k, v in summaries.items()},
                "research_reuse": load(work / "RESEARCH_REUSE.json")
                if (work / "RESEARCH_REUSE.json").exists()
                else None,
                "upstream_runtime": "not_run",
                "application_runtime": "not_run",
                "strict_acceptance": False,
            }
            fixed_json(work / "MODEL_PRODUCTION.json", production)
            step = "freeze_import"
            stage = "freeze_import_export"
            wf.begin(PLAN_ID, item["leaf"], work.name, step, digest(production))
            output_item = {
                "key": work.name,
                "leaf": item["leaf"],
                "production_mode": "opencode-cli-go",
            }
            with PUBLISH:
                for known_case in CaseLibrary(service.store).list_cases():
                    if any(
                        s["repository"] == snapshot["repository"]
                        and s["commit_sha"] == snapshot["commit_sha"]
                        and s["files"] == snapshot["files"]
                        for s in known_case["source_snapshots"]
                    ):
                        output_item["shared_case_id"] = known_case["case_id"]
                        break
                # Unique stable case/idempotency keys across leaves, not attempt-1 alone.
                batch_id = PLAN_ID + "-" + item["leaf"]
                result = produce(
                    work.parent,
                    output_item,
                    service.store,
                    api.rstrip("/") + "/api/factory/",
                    batch_id,
                )
                register_catalog(
                    {**output_item, "key": item["leaf"] + "-" + work.name}, work
                )
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(
                    work / "IMPORT_RECEIPT.json",
                    work / "packages/template-snapshot.zip",
                    work / "atlas-development-package.zip",
                    url=result.get("url"),
                ),
            )
            step = "download"
            stage = "verify_download"
            wf.begin(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                digest(load(work / "IMPORT_RECEIPT.json")),
            )
            verify_download(work, api)
            wf.complete(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                workflow_outputs(
                    work / "DOWNLOAD_VERIFIED.json",
                    url="/api/factory/assisted-templates/"
                    + result["artifact_id"]
                    + "/files/development",
                ),
            )
            service.update_leaf(
                PLAN_ID,
                item["leaf"],
                "ready_not_run",
                {
                    "artifact_id": result["artifact_id"],
                    "case_id": result["case_id"],
                    "case_revision": result["case_revision"],
                    "workdir": str(work.relative_to(ROOT)),
                    "first_pass_done": True,
                    "repair_pending": False,
                    "application_runtime": "not_run",
                },
            )
            try:
                compact_completed_work(work)
            except OSError as maintenance:
                atomic_json(
                    work / "MAINTENANCE_WARNING.json",
                    {"error": str(maintenance), "usable_template_unchanged": True},
                )
            return {"leaf": item["leaf"], "state": "ready_not_run"}
        except Exception as error:
            code = leaf_failure_code(error, stage)
            failure = {
                "leaf": item["leaf"],
                "stage": stage,
                "code": code,
                "error": str(error),
                "at": time.time(),
                "attempt": work.name,
                "stage_summaries": {
                    str(p.relative_to(work)): sha(p)
                    for p in work.glob("calls/*/cli-summary.json")
                },
                "raw_outputs": {
                    str(p.relative_to(work)): sha(p)
                    for p in work.glob("calls/*/original-response.json")
                },
            }
            if not (work / "FAILURE.json").exists():
                atomic_json(work / "FAILURE.json", failure)
            atomic_json(work / "LATEST_FAILURE.json", failure)
            atomic_json(work / "failures" / (str(time.time_ns()) + ".json"), failure)
            wf.fail(
                PLAN_ID,
                item["leaf"],
                work.name,
                step,
                code,
                str(error),
                paused=code in GLOBAL_CODES,
            )
            if code in GLOBAL_CODES:
                service.update_leaf(
                    PLAN_ID,
                    item["leaf"],
                    "paused",
                    {
                        "failure_stage": stage,
                        "failure_code": code,
                        "error": str(error),
                        "workdir": str(work.relative_to(ROOT)),
                    },
                )
                service.pause_if_running(PLAN_ID, code + ": " + str(error))
                return {"leaf": item["leaf"], "state": "paused", "code": code}
            content = code == "auxiliary_content"
            reserve_deferred = code == "budget_first_pass_reserve"
            if reserve_deferred:
                state = "needs_revision" if repair else "paused"
            elif content:
                state = "needs_revision"
            else:
                state = "source_unavailable" if code == "source_unavailable" else "failed"
            service.update_leaf(
                PLAN_ID,
                item["leaf"],
                state,
                {
                    "failure_stage": stage,
                    "failure_code": code,
                    "error": str(error),
                    "first_pass_done": True,
                    "repair_pending": content and not repair,
                    **(
                        {"deferred_reason": "preserve pending first-pass allowance"}
                        if reserve_deferred
                        else {}
                    ),
                    "workdir": str(work.relative_to(ROOT)),
                },
            )
            try:
                compact_completed_work(work)
            except (OSError, ValueError) as maintenance:
                atomic_json(
                    work / "MAINTENANCE_WARNING.json",
                    {"error": str(maintenance), "original_evidence_retained": True},
                )
            return {"leaf": item["leaf"], "state": state, "code": code}


def progress(root, service):
    state = service.status(PLAN_ID)
    mode = getattr(service, "dispatch_mode", lambda _: "legacy")(PLAN_ID)
    state["dispatch_mode"] = mode
    atomic_json(
        root / "PROGRESS.json",
        {k: v for k, v in state.items() if k not in {"items", "calls"}},
    )
    atomic_json(root / "RESULTS.json", {"items": state["items"]})
    atomic_json(
        root / "CALL_LEDGER.json",
        {
            "calls": state["calls"],
            "historical_baseline": state["baseline"],
            "new_calls": state["new_calls"],
            "effective_max_cumulative": state["baseline"] + state["max_calls"],
        },
    )
    return state


def dispatch_lanes(selected_leaves, mode):
    if mode == "full_first_round":
        return (False,)
    if mode == "pilot_complete":
        return (False, True)
    return (False,) if selected_leaves else (False, True)


def write_round_report(root, state):
    """A failure is a result, never an implied pass or a request to restart."""
    report = {
        "schema": "atlas.auxiliary-round-report.v1",
        "full_plan_id": PLAN_ID,
        "mode": state.get("dispatch_mode", "legacy"),
        "observed_at": time.time(),
        "status": state["status"],
        "reason": state.get("reason"),
        "counts": state.get("counts", {}),
        "new_calls": state["new_calls"],
        "historical_baseline": state["baseline"],
        "active_calls": state.get("active_calls"),
        "items": [
            {key: item.get(key) for key in (
                "leaf", "state", "current_attempt", "failure_stage", "failure_code",
                "error", "workdir", "artifact_id", "case_id", "case_revision", "repair_pending",
            )}
            for item in state["items"]
        ],
        "application_runtime": "not_run",
    }
    atomic_json(root / "ROUND_REPORT.json", report)
    if state["status"] != "running":
        path = root / "round-reports" / (str(time.time_ns()) + ".json")
        atomic_json(path, report)
    return report


def run(root, api, selected_leaves=None):
    root.mkdir(parents=True, exist_ok=True)
    with (root / ".coordinator.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        request, scope = verify_plan(root)
        store, service = host()
        selected_leaves = effective_dispatch_selection(
            selected_leaves,
            service.selected_leaves(PLAN_ID),
            {item["leaf"] for item in scope["items"]},
        )
        state = service.status(PLAN_ID)
        if state["status"] not in {"running", "registered"}:
            return progress(root, service)
        if state["status"] == "registered":
            service.control(PLAN_ID, "resume", "coordinator active")
        atomic_json(
            root / "PROCESS.json",
            {
                "pid": os.getpid(),
                "started": time.time(),
                "cwd": str(ROOT),
                "plan_id": PLAN_ID,
                "source_commit": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
            },
        )
        signal.signal(
            signal.SIGTERM,
            lambda *_: service.control(
                PLAN_ID, "pause", "coordinator received SIGTERM; no new dispatch"
            ),
        )
        try:
            mode = getattr(service, "dispatch_mode", lambda _: "legacy")(PLAN_ID)
            for repair in dispatch_lanes(selected_leaves, mode):
                while service.status(PLAN_ID)["status"] == "running":
                    verify_plan(root)
                    if shutil.disk_usage(root).free < 5 * 1024**3:
                        service.control(PLAN_ID, "pause", "disk_free_below_5_GiB")
                        break
                    state = progress(root, service)
                    pending = [
                        x
                        for x in state["items"]
                        if (x.get("repair_pending") and repair)
                        or (
                            not repair
                            and x["state"] in {"pending", "running", "paused"}
                            and not x.get("first_pass_done")
                        )
                    ]
                    if selected_leaves:
                        pending = [x for x in pending if x["leaf"] in selected_leaves]
                    if not pending:
                        break
                    gate = get_workflow_gate(service)
                    if gate and gate["mode"] == "validation":
                        pending = [x for x in pending if x["leaf"] in gate["leaves"]]
                        if not pending:
                            break
                    batch = pending[:20]
                    atomic_json(
                        root / "CURRENT_BATCH.json",
                        {
                            "started": time.time(),
                            "lane": "repair" if repair else "first",
                            "leaves": [x["leaf"] for x in batch],
                        },
                    )
                    with concurrent.futures.ThreadPoolExecutor(
                        max_workers=2
                    ) as executor:
                        futures = set()
                        queue = iter(batch)
                        for _ in range(2):
                            item = next(queue, None)
                            if item:
                                futures.add(
                                    executor.submit(
                                        execute_leaf, root, service, item, api, repair
                                    )
                                )
                        while futures:
                            done, futures = concurrent.futures.wait(
                                futures,
                                timeout=30,
                                return_when=concurrent.futures.FIRST_COMPLETED,
                            )
                            for future in done:
                                result = future.result()
                                print(json.dumps(result), flush=True)
                                if service.status(PLAN_ID)["status"] == "running":
                                    item = next(queue, None)
                                    if item:
                                        futures.add(
                                            executor.submit(
                                                execute_leaf,
                                                root,
                                                service,
                                                item,
                                                api,
                                                repair,
                                            )
                                        )
                            progress(root, service)
                    progress(root, service)
            state = progress(root, service)
            if selected_leaves and state["status"] == "running":
                if selected_first_pass_complete(state["items"], selected_leaves):
                    service.control(PLAN_ID, "pause", "selected leaf run complete")
                    state = progress(root, service)
            if mode == "full_first_round" and state["status"] == "running":
                service.control(PLAN_ID, "pause", "round one complete; review recorded failures before round two")
                state = progress(root, service)
            gate = get_workflow_gate(service)
            if state["status"] == "running" and gate and gate["mode"] == "validation":
                service.control(
                    PLAN_ID,
                    "pause",
                    "workflow_validation_complete: evaluate actual results before opening full dispatch",
                )
                state = progress(root, service)
            if not selected_leaves and state["status"] == "running" and not any(
                x["state"] in {"pending", "running", "paused"}
                or x.get("repair_pending")
                for x in state["items"]
            ):
                service.control(
                    PLAN_ID,
                    "complete",
                    "completed_with_failures"
                    if any(
                        x["state"] not in {"ready_not_run", "reused"}
                        for x in state["items"]
                    )
                    else "all covered",
                )
        except BaseException as error:
            service.pause_if_running(
                PLAN_ID,
                getattr(error, "code", "coordinator_error") + ": " + str(error),
            )
            raise
        finally:
            write_round_report(root, progress(root, service))


def start_daemon(root, api, selected_leaves=None):
    """launchd owns the coordinator after the chat/terminal exits; no cron loop."""
    _, service = host()
    plan_state = service.status(PLAN_ID)
    resuming_selected = plan_state["status"] == "paused"
    if resuming_selected and not selected_leaves:
        raise ValueError("a paused plan can start only with selected leaves")
    if plan_state["status"] not in {"registered", "running", "paused"}:
        raise ValueError("plan is not startable")
    verify_plan(root)
    selected_leaves = list(selected_leaves or [])
    if selected_leaves and (
        len(selected_leaves) > 3
        or len(set(selected_leaves)) != len(selected_leaves)
        or any(not isinstance(leaf, str) or not leaf for leaf in selected_leaves)
    ):
        raise ValueError("selected dispatch requires one to three unique leaf names")
    scope = load(root / "FROZEN_SCOPE.json")
    known = {item["leaf"] for item in scope["items"]}
    if selected_leaves:
        if not set(selected_leaves) <= known:
            raise ValueError("selected leaf is outside the frozen plan scope")
        if not resuming_selected:
            active_selection = set(service.selected_leaves(PLAN_ID))
            if not active_selection:
                raise ValueError("selected leaves must be durably activated while the plan is paused")
            if set(selected_leaves) != active_selection:
                raise ValueError("selected leaves must exactly match the active durable dispatch")
    if resuming_selected and plan_state.get("active_calls", 0) != 0:
        raise ValueError("cannot resume selected dispatch while model calls are active")
    label = "com.atlas.full-leaf-auxiliary-20261021"
    target = "gui/" + str(os.getuid()) + "/" + label
    plist = root / "coordinator.plist"
    import sys

    config = {
        "Label": label,
        "ProgramArguments": [
            sys.executable,
            str(Path(__file__).resolve()),
            "run",
            "--root",
            str(root),
            "--api",
            api,
        ],
        "WorkingDirectory": str(ROOT),
        "RunAtLoad": True,
        "KeepAlive": {"SuccessfulExit": False},
        "ThrottleInterval": 30,
        "StandardOutPath": str(root / "runner.log"),
        "StandardErrorPath": str(root / "runner.stderr.log"),
        "EnvironmentVariables": {
            "PATH": str(Path.home() / ".opencode/bin")
            + ":/usr/local/bin:/usr/bin:/bin",
            "PYTHONUNBUFFERED": "1",
        },
    }
    for leaf in selected_leaves or []:
        config["ProgramArguments"].extend(["--leaf", leaf])
    encoded = plistlib.dumps(config)
    old_bytes = plist.read_bytes() if plist.exists() else None
    found = subprocess.run(
        ["launchctl", "print", target], capture_output=True, text=True
    )
    booted_out = False
    live = bool(found.returncode == 0 and __import__("re").search(r"(?m)^\s*pid = [1-9]\d*\s*$", found.stdout))
    if resuming_selected and live:
        raise ValueError("cannot resume selected dispatch while coordinator is live")
    if resuming_selected and found.returncode == 0 and old_bytes is None:
        raise ValueError("loaded supervisor has no local plist to verify")
    if old_bytes is not None and old_bytes != encoded:
        old_config = plistlib.loads(old_bytes)
        new_config = plistlib.loads(encoded)
        old_args = old_config.get("ProgramArguments", [])
        new_args = new_config.get("ProgramArguments", [])
        old_leaf_args = daemon_leaf_args(old_args)
        if (
            old_config.get("Label") != label
            or {k: v for k, v in old_config.items() if k != "ProgramArguments"}
            != {k: v for k, v in new_config.items() if k != "ProgramArguments"}
            or strip_leaf_args(old_args) != strip_leaf_args(new_args)
        ):
            raise ValueError("supervisor definition changed beyond selected leaf arguments")
        if not set(old_leaf_args) <= known:
            raise ValueError("existing supervisor selects a leaf outside the frozen plan scope")
        state = service.status(PLAN_ID)
        if live or state.get("active_calls", 0) != 0:
            raise ValueError("cannot change selected leaves while coordinator/model calls are active")
        archived_hash = hashlib.sha256(old_bytes).hexdigest()
        archive = root / ("coordinator.previous-" + archived_hash + ".plist")
        if archive.exists() and archive.read_bytes() != old_bytes:
            raise ValueError("existing archived supervisor bytes differ")
        if not archive.exists():
            archive.write_bytes(old_bytes)
        atomic_json(
            root / ("coordinator.previous-" + archived_hash + ".json"),
            {"path": archive.name, "sha256": archived_hash, "label": label},
        )
        if found.returncode == 0:
            subprocess.run(["launchctl", "bootout", target], check=True)
            booted_out = True
        plist.write_bytes(encoded)
    elif old_bytes is None:
        plist.write_bytes(encoded)
    if resuming_selected and found.returncode == 0 and not booted_out:
        subprocess.run(["launchctl", "bootout", target], check=True)
        booted_out = True
    if resuming_selected:
        service.resume_selected(PLAN_ID, selected_leaves)
    try:
        if found.returncode or booted_out:
            subprocess.run(
                ["launchctl", "bootstrap", "gui/" + str(os.getuid()), str(plist)],
                check=True,
            )
        elif "pid = " not in found.stdout:
            subprocess.run(["launchctl", "kickstart", target], check=True)
        actual = subprocess.run(
            ["launchctl", "print", target], check=True, capture_output=True, text=True
        )
    except BaseException:
        if resuming_selected and service.control_state(PLAN_ID) == "running":
            service.control(PLAN_ID, "pause", "selected supervisor activation failed")
        raise
    receipt = {
        "supervisor": "launchd",
        "label": label,
        "target": target,
        "plist_sha256": sha(plist),
        "observed_at": time.time(),
        "actual": actual.stdout,
        "note": "Launchd survives this chat and terminal. Machine sleep/offline stops progress; reboot/login may require start again. Checkpoints and original 30-day clock persist.",
    }
    atomic_json(root / "START_RECEIPT.json", receipt)
    return receipt


def strip_leaf_args(arguments):
    """Normalize only trailing repeatable leaf selectors; every other arg stays bound."""
    return arguments[: len(arguments) - len(daemon_leaf_args(arguments) * 2)]


def daemon_leaf_args(arguments):
    try:
        index = arguments.index("--leaf")
    except ValueError:
        return []
    suffix = arguments[index:]
    if len(suffix) % 2 or any(suffix[n] != "--leaf" for n in range(0, len(suffix), 2)):
        raise ValueError("selected leaf arguments must be trailing --leaf/value pairs")
    return suffix[1::2]


def supervised_run(root, api, selected_leaves=None):
    while True:
        run(root, api, selected_leaves)
        _, service = host()
        state = service.status(PLAN_ID)
        if (
            state["status"] != "paused"
            or not str(state["reason"]).startswith("full_provider_unavailable:")
            or state["active_calls"]
        ):
            return
        retry = service.schedule_provider_recovery(PLAN_ID)
        if retry is None:
            return
        atomic_json(
            root / ("PROVIDER_BACKOFF_" + str(retry["number"]) + ".json"), retry
        )
        while time.time() < retry["resume_after"]:
            current = service.status(PLAN_ID)
            if current["status"] != "paused" or current["reason"] != state["reason"]:
                return
            progress(root, service)
            time.sleep(min(10, retry["resume_after"] - time.time()))
        service.control(
            PLAN_ID,
            "resume",
            "bounded shared-provider recovery, normal reservations remain charged",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=[
            "freeze",
            "register",
            "start",
            "run",
            "status",
            "pause",
            "resume",
            "stop",
            "workflow-validation",
            "workflow-replay",
            "workflow-open-full",
            "workflow-round",
        ],
    )
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--api", default="http://127.0.0.1:5199")
    parser.add_argument("--leaf", action="append", default=[])
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "freeze":
        state = freeze(root, args.api)
        print(
            json.dumps(
                {k: v for k, v in state.items() if k != "items"},
                ensure_ascii=False,
                indent=2,
            )
        )
        return
    store, service = host()
    if args.command == "register":
        request, _ = verify_plan(root)
        result = service.register(request)
        atomic_json(root / "REGISTRATION.json", result)
    elif args.command == "workflow-validation":
        verify_plan(root)
        result = WorkflowService(store).set_validation(PLAN_ID, args.leaf)
        atomic_json(root / "WORKFLOW_VALIDATION_GATE.json", result)
    elif args.command == "workflow-replay":
        verify_plan(root)
        selected = [
            x for x in service.status(PLAN_ID)["items"] if x["leaf"] in args.leaf
        ]
        if len(selected) != len(args.leaf) or any(
            x["state"] != "ready_not_run" for x in selected
        ):
            raise ValueError("replay requires exact already completed plan leaves")
        before = service.status(PLAN_ID)["new_calls"]
        result = {
            "results": [
                replay_completed_workflow(root, service, x, args.api) for x in selected
            ]
        }
        result["new_calls"] = service.status(PLAN_ID)["new_calls"] - before
        atomic_json(root / "WORKFLOW_REPLAY_RECEIPT.json", result)
    elif args.command == "workflow-open-full":
        verify_plan(root)
        if not args.evidence:
            raise ValueError("actual workflow validation evidence required")
        workflow = WorkflowService(store)
        workflow.set_gate_passed(PLAN_ID, load(args.evidence))
        result = workflow.open_full(PLAN_ID)
        atomic_json(root / "WORKFLOW_FULL_GATE_RECEIPT.json", result)
    elif args.command == "workflow-round":
        verify_plan(root)
        if not args.evidence:
            raise ValueError("persisted round request with authorization required")
        result = service.resume_round(load(args.evidence))
        atomic_json(root / "ROUND_ACTIVATION_RECEIPT.json", result)
    elif args.command == "run":
        return supervised_run(root, args.api, args.leaf)
    elif args.command == "start":
        result = start_daemon(root, args.api, args.leaf)
    elif args.command in {"pause", "resume", "stop"}:
        result = service.control(PLAN_ID, args.command)
    else:
        result = service.status(PLAN_ID)
    print(
        json.dumps(
            {k: v for k, v in result.items() if k not in {"items", "calls"}},
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
