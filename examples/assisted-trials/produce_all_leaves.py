"""Durable, single-coordinator full-leaf auxiliary production. No application runs."""

import argparse
import concurrent.futures
import fcntl
import hashlib
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
    validate_read_coverage,
    validate_review,
)
from template_factory.store import FactoryStore, FactoryError, digest
from template_factory.full_auxiliary import FullAuxiliaryService, MODEL
from template_factory.cases import CaseLibrary
from atlas_runtime import atomic_json
import full_leaf_profiles as profiles

DEFAULT_ROOT = ROOT / "docs/template-factory/full-leaf-auxiliary-2026-10-21"
PLAN_ID = "full-leaf-auxiliary-2026-10-21"
PUBLISH = threading.Lock()
GLOBAL_CODES = {
    "full_plan_integrity",
    "full_plan_binding",
    "budget_deadline",
    "budget_exhausted",
    "budget_paused",
    "full_plan_paused",
    "full_uncertain",
    "full_provider_unavailable",
}
TECH_CODES = {
    "cli_protocol",
    "cli_timeout",
    "cli_failed",
    "cli_no_result",
    "cli_output_truncated",
}


def load(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


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
    for stage, path in paths.items():
        summaries[stage] = _verify_call(folder / path, request["leaf_sha256"], MODEL)
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

    def deliver(target, selected_budget):
        try:
            result = checkpoint(
                target,
                payload,
                prompt,
                CoordinatedCLI(root, service),
                selected_budget,
                source,
                leaf,
                model=MODEL,
            )
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
        if (path / "SHARED_PROVIDER_FAILURE.json").exists() and shared_provider_fault(
            FactoryError(load(path / "SHARED_PROVIDER_FAILURE.json")["error"], "cli_failed", 503)
        ) and (
            "-protocol-1" in relative or (work / "PROTOCOL_SUCCESSOR.json").exists()
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
        atomic_json(
            work / "ACCEPTED_RESEARCH_RECEIPT.json",
            {
                "case_id": case_id,
                "revision": case["revision"],
                "digest": case["digest"],
                "review_input_digest": identity,
                "review_session": review_session,
                "template_passed": False,
                "replayed": committed["replayed"],
            },
        )


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
                "path": str((previous / "FAILURE.json").relative_to(ROOT)),
                "sha256": sha(previous / "FAILURE.json"),
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
            },
        )
        stage = "research"
        try:
            verify_plan(root)
            selected_scenario(work)
            fixed_json(
                work / "REQUEST.json",
                {
                    "leaf": item["leaf"],
                    "leaf_sha256": item["leaf_sha256"],
                    "full_plan_id": PLAN_ID,
                    "profile": profiles.VERSION,
                    "model": MODEL,
                },
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
                        raise ValueError("prior source bytes changed")
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
            stage = "source_pin"
            if not (work / "source-snapshot.json").exists():
                reused = next(
                    (
                        c
                        for c in compatible
                        if c["case_id"] == research.get("reuse_case_id")
                    ),
                    None,
                )
                snap = (
                    next(
                        (
                            s
                            for s in reused["source_snapshots"]
                            if s["repository"] == research["repository"]
                            and set(s["files"]) == set(research["files"])
                        ),
                        None,
                    )
                    if reused
                    else None
                )
                if snap and Path(snap["local_root"]).is_dir():
                    fixed_json(
                        work / "source-snapshot.json",
                        {
                            k: v
                            for k, v in snap.items()
                            if k not in {"snapshot_id", "file_manifest_digest"}
                        },
                    )
                    fixed_json(
                        work / "RESEARCH_REUSE.json",
                        {
                            "case_id": reused["case_id"],
                            "revision": reused["revision"],
                            "digest": reused["digest"],
                        },
                    )
                else:
                    pin_sources(research, work, service.store, namespace=PLAN_ID)
            snapshot = load(work / "source-snapshot.json")
            for name, expected in snapshot["files"].items():
                if sha(Path(snapshot["local_root"]) / name) != expected:
                    raise ValueError("source bytes differ")
            if not (work / "upstream-evidence.zip").exists():
                with zipfile.ZipFile(
                    work / "upstream-evidence.zip", "w", zipfile.ZIP_DEFLATED
                ) as z:
                    for name in sorted(snapshot["files"]):
                        z.write(Path(snapshot["local_root"]) / name, name)
                    z.write(work / "source-snapshot.json", "source-snapshot.json")
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
                raise ValueError("source inventory differs")
            prompt = profiles.AUTHOR
            if repair:
                feedback = load(previous / "FAILURE.json")
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
                    "parent_failure_sha256": sha(previous / "FAILURE.json"),
                    "feedback": feedback,
                    "scope": "Fix existing core violations only; preserve fixed scenario, sources and delivery profile.",
                }
                prompt += "\nThis is ONE content revision. Read source/PARENT_CANDIDATE.json when supplied. Fix all concrete feedback together; do not expand scope. Return the complete revised template JSON."
            stage = "generation"
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
            authored, files = profiles.validate_author(generated, snapshot, inputs)
            fixed_json(work / "SOURCE_INPUT.json", inputs)
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
            validate_review(
                review,
                identity,
                author_summary["session_id"],
                review_summary["session_id"],
                len(authored["observations"]),
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
                "model": MODEL,
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
            stage = "freeze_import_export"
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
            code = getattr(error, "code", "content_or_host_validation")
            if isinstance(error, urllib.error.URLError) and (
                not isinstance(error, urllib.error.HTTPError)
                or error.code in {403, 429, 500, 502, 503, 504}
            ):
                code = "full_provider_unavailable"
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
                if service.control_state(PLAN_ID) != "stopped":
                    service.control(PLAN_ID, "pause", code + ": " + str(error))
                return {"leaf": item["leaf"], "state": "paused", "code": code}
            content = (
                stage == "generation" and code == "content_or_host_validation"
            ) or (
                stage == "independent_review"
                and code == "content_or_host_validation"
                and "review" in locals()
                and review.get("verdict") == "needs_changes"
            )
            state = (
                "needs_revision"
                if content
                else ("source_unavailable" if stage == "source_pin" else "failed")
            )
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


def run(root, api):
    root.mkdir(parents=True, exist_ok=True)
    with (root / ".coordinator.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        request, scope = verify_plan(root)
        store, service = host()
        if service.status(PLAN_ID)["status"] not in {"running", "registered"}:
            return progress(root, service)
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
            for repair in (False, True):
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
            if state["status"] == "running" and not any(
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
            if service.control_state(PLAN_ID) != "stopped":
                service.control(
                    PLAN_ID,
                    "pause",
                    getattr(error, "code", "coordinator_error") + ": " + str(error),
                )
            raise
        finally:
            progress(root, service)


def start_daemon(root, api):
    """launchd owns the coordinator after the chat/terminal exits; no cron loop."""
    _, service = host()
    if service.control_state(PLAN_ID) not in {"registered", "running"}:
        raise ValueError("resume the formally paused plan before starting")
    verify_plan(root)
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
    encoded = plistlib.dumps(config)
    if plist.exists() and plist.read_bytes() != encoded:
        raise ValueError(
            "supervisor definition changed; inspect existing launchd service"
        )
    plist.write_bytes(encoded)
    found = subprocess.run(
        ["launchctl", "print", target], capture_output=True, text=True
    )
    if found.returncode:
        subprocess.run(
            ["launchctl", "bootstrap", "gui/" + str(os.getuid()), str(plist)],
            check=True,
        )
    elif "pid = " not in found.stdout:
        subprocess.run(["launchctl", "kickstart", target], check=True)
    actual = subprocess.run(
        ["launchctl", "print", target], check=True, capture_output=True, text=True
    )
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


def supervised_run(root, api):
    while True:
        run(root, api)
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
        ],
    )
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--api", default="http://127.0.0.1:5199")
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
    elif args.command == "run":
        return supervised_run(root, args.api)
    elif args.command == "start":
        result = start_daemon(root, args.api)
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
