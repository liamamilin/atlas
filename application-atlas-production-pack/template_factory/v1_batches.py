"""Versioned batch plans over the existing durable factory queue.

Plans are data, never a promise of quality. All mutations use the same SQLite
transaction/fencing rules as the existing scheduler. No model is called here.
"""
from __future__ import annotations

import json
import hashlib
import re
import time
from pathlib import Path
from zipfile import ZipFile, BadZipFile

from .store import FactoryError, canonical, digest, integer, now, text, uid

POLICY = "atlas.factory-v1.1"
DEFAULT_CAMPAIGN_ID = "atlas-v1-first-production-2026-10-19"
G1_MANIFEST_SCHEMA = "atlas.g1-verification-manifest.v1"
G1_REQUIRED_CHECKS = {
    "python_audit": {"argv": ("pip-audit", "-r", "requirements.txt"), "cwd": ".", "tests": False},
    "ruff": {"argv": ("ruff", "check", "application-atlas-production-pack/privacy.py", "application-atlas-production-pack/drafts_api.py", "application-atlas-production-pack/drafts_engines/__init__.py", "application-atlas-production-pack/mcp_atlas.py", "application-atlas-production-pack/execution_service.py", "application-atlas-production-pack/execution_state.py", "application-atlas-production-pack/execution_workspace.py", "application-atlas-production-pack/opencode_client.py", "application-atlas-production-pack/opencode_cli_adapter.py", "application-atlas-production-pack/opencode_permissions.py", "application-atlas-production-pack/opencode_runtime.py", "application-atlas-production-pack/project_export.py", "application-atlas-production-pack/project_generation.py", "application-atlas-production-pack/project_store.py", "application-atlas-production-pack/project_backup.py", "application-atlas-production-pack/runtime_recovery.py", "application-atlas-production-pack/template_factory", "atlas-web/scripts/gen-data.py", "atlas-web/scripts/verify-web-data.py"), "cwd": ".", "tests": False},
    "backend_tests": {"argv": ("python", "-m", "unittest", "discover", "-s", "application-atlas-production-pack/tests", "-v"), "cwd": ".", "tests": True, "allowed_skips": 8},
    "atlas_export": {"argv": ("python", "application-atlas-production-pack/export_atlas.py"), "cwd": ".", "tests": False},
    "web_gen": {"argv": ("npm", "run", "gen"), "cwd": "atlas-web", "tests": False},
    "web_verify_data": {"argv": ("npm", "run", "verify-data"), "cwd": "atlas-web", "tests": False},
    "npm_audit": {"argv": ("npm", "audit", "--registry=https://registry.npmjs.org", "--audit-level=high"), "cwd": "atlas-web", "tests": False},
    "web_typecheck": {"argv": ("npm", "run", "typecheck"), "cwd": "atlas-web", "tests": False},
    "web_unit": {"argv": ("npm", "test"), "cwd": "atlas-web", "tests": True},
    "web_build": {"argv": ("npm", "run", "build"), "cwd": "atlas-web", "tests": False},
    "default_e2e": {"argv": ("npm", "run", "test:e2e"), "cwd": "atlas-web", "tests": True},
    "factory_e2e": {"argv": ("npm", "run", "test:e2e:factory", "--", "--reporter=line"), "cwd": "atlas-web", "tests": True},
    "docker_integration": {"argv": ("python", "application-atlas-production-pack/tests/run_required_docker_integration.py"), "cwd": ".", "tests": True, "env": {"ATLAS_RUN_DOCKER_INTEGRATION": "1"}},
}
SUPPORT = {"profiles": ["python-web"], "network": "none", "runtime_concurrency": 1,
           "production_concurrency": 2}
VERIFICATION = {"harness-review", "runtime-verification", "scenario-review", "cognitive-review", "blueprint-runtime"}


def select_case_basis(store, scenario_id, scenario_revision):
    """Latest logical-case versions only; failed history never poisons a new revision."""
    from .cases import CaseLibrary
    library = CaseLibrary(store, initialize=False)
    cases = library.list_cases(scenario_id=scenario_id)
    current = {}
    for case in cases:
        if not any(link["scenario_revision"] == scenario_revision for link in case["scenario_links"]):
            continue
        if case["case_id"] not in current or case["revision"] > current[case["case_id"]]["revision"]:
            current[case["case_id"]] = case
    refs, excluded = [], []
    for case in current.values():
        ref = {"case_id": case["case_id"], "revision": case["revision"]}
        try:
            library.require_admissible(library.evidence_basis([ref], scenario_id, scenario_revision))
            refs.append(ref)
        except FactoryError as error:
            excluded.append({**ref, "code": error.code, "reason": str(error)})
    return (library.evidence_basis(refs, scenario_id, scenario_revision) if refs else None), excluded


def migrate(store):
    with store.connect() as con:
        if con.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name IN ('v1_plan','v1_execution','v1_outbox','v1_gate','v1_campaign_gate','v1_campaign_product')").fetchone()[0] == 6:
            return
    statements = [
        "CREATE TABLE IF NOT EXISTS v1_plan(id TEXT PRIMARY KEY,digest TEXT NOT NULL,body TEXT NOT NULL,created_at TEXT NOT NULL)",
        "CREATE TABLE IF NOT EXISTS v1_execution(plan_id TEXT PRIMARY KEY,plan_digest TEXT NOT NULL,idempotency_key TEXT UNIQUE NOT NULL,batch_id TEXT UNIQUE NOT NULL,created_at TEXT NOT NULL)",
        "CREATE TABLE IF NOT EXISTS v1_outbox(id TEXT PRIMARY KEY,parent_job TEXT NOT NULL UNIQUE,artifact_id TEXT NOT NULL,body TEXT NOT NULL,state TEXT NOT NULL)",
        "CREATE TABLE IF NOT EXISTS v1_gate(name TEXT PRIMARY KEY,body TEXT NOT NULL,created_at TEXT NOT NULL)",
        "CREATE TABLE IF NOT EXISTS v1_campaign_gate(campaign_id TEXT NOT NULL,name TEXT NOT NULL,body TEXT NOT NULL,created_at TEXT NOT NULL,PRIMARY KEY(campaign_id,name))",
        "CREATE TABLE IF NOT EXISTS v1_campaign_product(campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,scenario_id TEXT NOT NULL,PRIMARY KEY(campaign_id,product_id))",
    ]
    with store.connect(True) as con:
        for sql in statements:
            con.execute(sql)


def _sha256_file(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def _npm_audit_report_passes(log):
    """Accept only a complete npm text summary meeting the fixed high threshold."""
    lines = str(log).splitlines()
    if not any(line.strip() for line in lines):
        return False
    if any(re.match(r"^\s*(?:npm\s+ERR!|error\b)", line, re.IGNORECASE) for line in lines):
        return False
    known = {"info", "low", "moderate", "high", "critical"}
    severities = re.findall(r"^\s*Severity:\s*(\S+)\s*$", str(log), re.IGNORECASE | re.MULTILINE)
    normalized = [value.lower() for value in severities]
    if any(value not in known or value in {"high", "critical"} for value in normalized):
        return False

    summaries = []
    zero = re.compile(r"^\s*found\s+0\s+vulnerabilities\s*$", re.IGNORECASE)
    counts = re.compile(
        r"^\s*(?:found\s+)?(?P<items>\d+\s+(?:info|low|moderate|high|critical)"
        r"(?:\s*,\s*\d+\s+(?:info|low|moderate|high|critical))*)"
        r"\s+severity\s+vulnerabilit(?:y|ies)\s*$",
        re.IGNORECASE,
    )
    for line in lines:
        if zero.fullmatch(line):
            summaries.append([])
            continue
        match = counts.fullmatch(line)
        if match:
            summaries.append([
                (int(amount), severity.lower())
                for amount, severity in re.findall(
                    r"(\d+)\s+(info|low|moderate|high|critical)",
                    match.group("items"), re.IGNORECASE,
                )
            ])
    if len(summaries) != 1:
        return False
    return all(severity not in {"high", "critical"} for _, severity in summaries[0])


def _g1_source_digest(root):
    """Bind the G1 checks to the current factory, tests, web source and CI files."""
    root = Path(root).resolve()
    files = []
    pack = root / "application-atlas-production-pack"
    candidates = (
        pack / "template_factory",
        pack / "tests",
        root / "atlas-web" / "src",
        root / "atlas-web" / "e2e",
        root / "atlas-web" / "tests",
        root / "atlas-web" / "scripts",
    )
    for directory in candidates:
        if not directory.is_dir():
            continue
        paths = directory.rglob("*")
        for path in paths:
            if not path.is_file() or "__pycache__" in path.parts or path.is_symlink():
                continue
            if directory.name in {"template_factory", "tests"} and "application-atlas-production-pack" in directory.parts:
                if path.suffix not in {".py", ".json", ".txt", ".toml", ".yml", ".yaml"}:
                    continue
            elif path.suffix not in {".ts", ".tsx", ".js", ".mjs", ".cjs", ".py", ".json", ".html", ".css"}:
                continue
            files.append(path)
    files.extend(path for path in (
        pack / "drafts_api.py",
        pack / "atlas_runtime.py",
        pack / "drafts_engines" / "__init__.py",
        pack / "export_atlas.py",
        pack / "privacy.py",
        pack / "mcp_atlas.py",
        pack / "execution_service.py",
        pack / "execution_state.py",
        pack / "execution_workspace.py",
        pack / "opencode_client.py",
        pack / "opencode_cli_adapter.py",
        pack / "opencode_permissions.py",
        pack / "opencode_runtime.py",
        pack / "project_export.py",
        pack / "project_generation.py",
        pack / "project_store.py",
        pack / "project_backup.py",
        pack / "runtime_recovery.py",
        pack / "mvp_apps.json",
        root / "atlas-web" / "package.json",
        root / "atlas-web" / "package-lock.json",
        root / "atlas-web" / "playwright.factory.config.ts",
        root / "atlas-web" / "vite.config.ts",
        root / "atlas-web" / "tsconfig.json",
        root / "atlas-web" / "playwright.config.ts",
        root / ".github" / "workflows" / "checks.yml",
        root / "requirements.txt",
        root / "pyproject.toml",
    ) if path.is_file() and not path.is_symlink())
    entries = []
    for path in sorted(set(files)):
        entries.append({"path": path.relative_to(root).as_posix(), "sha256": _sha256_file(path)})
    return hashlib.sha256(json.dumps(entries, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _manifest_check_failures(path, plan, sample_scenario_id):
    """Validate host-written evidence; a submitted `passed` boolean is never enough."""
    failures = []
    workspace = Path(plan["_workspace_root"]).resolve()
    manifest_path = Path(path).expanduser()
    if not manifest_path.is_absolute():
        manifest_path = workspace / manifest_path
    try:
        manifest_path = manifest_path.resolve(strict=True)
        manifest_path.relative_to(workspace)
    except (OSError, ValueError):
        return ["manifest_missing_or_outside_workspace"]
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return ["manifest_invalid_json"]
    if not isinstance(manifest, dict) or manifest.get("schema") != G1_MANIFEST_SCHEMA:
        failures.append("manifest_schema_invalid")
        return failures
    expected = {"campaign_id": plan["campaign_id"], "plan_id": plan["id"],
                "plan_digest": plan["digest"], "sample_scenario_id": sample_scenario_id}
    for key, value in expected.items():
        if manifest.get(key) != value:
            failures.append("manifest_" + key + "_mismatch")
    current_source_digest = _g1_source_digest(workspace)
    if manifest.get("source_tree_sha256") != current_source_digest:
        failures.append("source_or_test_tree_changed")
    checks = manifest.get("checks")
    if not isinstance(checks, dict):
        failures.append("required_check_records_missing")
        return failures
    for name, requirement in G1_REQUIRED_CHECKS.items():
        record = checks.get(name)
        if not isinstance(record, dict):
            failures.append("check_missing:" + name)
            continue
        if record.get("status") != "passed" or record.get("exit_code") != 0:
            failures.append("check_not_passed:" + name)
        expected_skips = requirement.get("allowed_skips", 0)
        if record.get("skipped") != expected_skips:
            failures.append("check_skipped:" + name)
        if requirement["tests"] and (isinstance(record.get("tests_run"), bool) or not isinstance(record.get("tests_run"), int) or record["tests_run"] <= 0):
            failures.append("check_no_tests:" + name)
        argv = record.get("argv")
        if not isinstance(argv, list) or tuple(argv) != requirement["argv"]:
            failures.append("check_command_mismatch:" + name)
        if record.get("cwd") != requirement["cwd"]:
            failures.append("check_cwd_mismatch:" + name)
        if requirement.get("env") and record.get("env") != requirement["env"]:
            failures.append("check_environment_mismatch:" + name)
        raw_log_path = record.get("log_path")
        if not isinstance(raw_log_path, str) or not raw_log_path:
            failures.append("check_log_missing:" + name)
            continue
        log_path = Path(raw_log_path)
        if not log_path.is_absolute():
            log_path = workspace / log_path
        try:
            log_path = log_path.resolve(strict=True)
            log_path.relative_to(workspace)
            raw = log_path.read_bytes()
            log = raw.decode("utf-8", errors="replace")
        except (OSError, ValueError):
            failures.append("check_log_missing_or_outside_workspace:" + name)
            continue
        if record.get("log_sha256") != hashlib.sha256(raw).hexdigest():
            failures.append("check_log_digest_mismatch:" + name)
        if not log.strip():
            failures.append("check_log_empty:" + name)
        if name == "backend_tests":
            count = re.search(r"Ran (\d+) tests? in [\d.]+s", log)
            skip_count = re.search(r"\(skipped=(\d+)\)", log)
            skip_lines = re.findall(r"^(\w+) \([^\n]+\) \.\.\. skipped '([^']+)'$", log, re.MULTILINE)
            known_skip_reasons = {"set ATLAS_RUN_DOCKER_INTEGRATION=1 to run isolated local Docker tests", "opt-in synthetic Docker queue integration"}
            known_skip_tests = {
                "test_cli_smoke_and_mixed_python_node_acceptance",
                "test_mixed_python_node_cases_pass_against_stdlib_web_app_and_preserve_source",
                "test_negative_acceptance_valid_failed_json_and_nonzero_exit_is_blocked",
                "test_node_web_launcher_serves_real_request_to_python_tester",
                "test_startup_exception_exit_is_blocked_and_traceback_is_preserved",
                "test_startup_exception_traceback_is_captured_from_stderr",
                "test_total_timeout_removes_every_owned_container",
                "test_real_docker_through_api_queue_and_pinned_frozen_source",
            }
            actual_skipped = int(skip_count.group(1)) if skip_count else 0
            if (not count or "OK" not in log or int(count.group(1)) != record.get("tests_run")
                    or actual_skipped != record.get("skipped")
                    or len(skip_lines) != record.get("skipped")
                    or {name for name, _ in skip_lines} != known_skip_tests
                    or any(reason not in known_skip_reasons for _, reason in skip_lines)):
                failures.append("check_execution_not_proven:" + name)
        elif name == "python_audit" and "No known vulnerabilities found" not in log:
            failures.append("check_execution_not_proven:" + name)
        elif name == "ruff" and ("All checks passed" not in log):
            failures.append("check_execution_not_proven:" + name)
        elif name in {"web_unit", "default_e2e", "factory_e2e"}:
            passed = (re.search(r"\b(\d+) passed\b", log)
                      if name != "web_unit" else
                      re.search(r"^# pass (\d+)$", log, re.MULTILINE) or re.search(r"\b(\d+) passed\b", log))
            if not passed or int(passed.group(1)) != record.get("tests_run"):
                failures.append("check_execution_not_proven:" + name)
        elif name == "web_gen" and "gen" not in log.lower():
            failures.append("check_execution_not_proven:" + name)
        elif name == "web_verify_data" and "verify-data" not in log.lower():
            failures.append("check_execution_not_proven:" + name)
        elif name == "atlas_export" and ("sqlite ->" not in log.lower() or "json   ->" not in log.lower()):
            failures.append("check_execution_not_proven:" + name)
        elif name == "npm_audit" and not _npm_audit_report_passes(log):
            failures.append("check_execution_not_proven:" + name)
        elif name == "web_typecheck" and ("tsc --noEmit" not in log or re.search(r"error TS\d+", log)):
            failures.append("check_execution_not_proven:" + name)
        elif name == "web_build" and ("vite build" not in log or "built in" not in log):
            failures.append("check_execution_not_proven:" + name)
        elif name == "docker_integration":
            summaries = re.findall(r"\{[^\n]*\"status\"[^\n]*\}", log)
            if not summaries or any('"status": "blocked_external"' in row or '"status":"blocked_external"' in row for row in summaries):
                failures.append("check_blocked_or_unproven:docker_integration")
            else:
                try:
                    summary = json.loads(summaries[-1])
                    if summary.get("status") != "passed" or summary.get("tests_run", 0) <= 0 or summary.get("skipped") != 0:
                        failures.append("check_blocked_or_unproven:docker_integration")
                except (ValueError, TypeError):
                    failures.append("check_execution_not_proven:docker_integration")
    return failures


class BatchService:
    def __init__(self, store):
        self.store = store
        migrate(store)

    def _admit(self, scenario_id, policy):
        scenario = self.store.scenario(scenario_id)
        if scenario["status"] == "ready":
            return scenario, {"kind": "human_confirmed", "revision": scenario["revision"]}
        if scenario["status"] == "draft" and policy == "reviewed-draft-v1":
            # This is explicit batch-policy admission, NEVER a fake user confirmation.
            visible = next(s for s in self.store.scenarios() if s["id"] == scenario_id)
            current = next((r for r in visible.get("reviews", []) if r.get("current")), None)
            if current and current["outcome"] == "passed":
                return scenario, {"kind": "batch_policy", "policy": policy,
                                  "review_id": current["id"], "revision": scenario["revision"],
                                  "note": "Independent current review admitted by policy; human status remains draft."}
        raise FactoryError("scenario lacks current admission; confirm or review it", "scenario_not_ready", 409)

    def _default_campaign(self):
        """Continue the campaign from the first persisted execution, else use the V1 seed name."""
        with self.store.connect() as con:
            row = con.execute(
                "SELECT p.body FROM v1_execution e JOIN v1_plan p ON p.id=e.plan_id "
                "ORDER BY e.created_at,e.rowid LIMIT 1"
            ).fetchone()
        if row:
            try:
                campaign = json.loads(row[0]).get("campaign_id")
                if isinstance(campaign, str) and campaign:
                    return campaign
            except (TypeError, ValueError):
                pass
        return DEFAULT_CAMPAIGN_ID

    def preview(self, value):
        from .cases import CaseLibrary
        ids = value.get("scenario_ids")
        if not isinstance(ids, list) or not ids or len(ids) > 10 or len(set(ids)) != len(ids):
            raise FactoryError("select 1–10 distinct scenarios")
        segment = value.get("segment", "G1")
        if segment not in {"G1", "T08"}:
            raise FactoryError("segment must be G1 or T08")
        model = text(value.get("model", "opencode-go/deepseek-v4.1-flash"), "provider/model", 200)
        if not re.fullmatch(r"[a-zA-Z0-9._:/#-]+", model) or "/" not in model or model.startswith("-"):
            raise FactoryError("model must use provider/model format")
        policy = value.get("admission_policy", "ready-only-v1")
        if policy not in {"ready-only-v1", "reviewed-draft-v1"}:
            raise FactoryError("unsupported admission policy")
        samples = value.get("runtime_sample_ids", [])
        if not isinstance(samples, list) or len(set(samples)) != len(samples) or not set(samples) <= set(ids):
            raise FactoryError("runtime samples must be distinct selected scenarios")
        if segment == "T08" and len(samples) < 3:
            raise FactoryError("T08 requires at least 3 prespecified runtime sample scenarios", "sample_scope_insufficient", 409)
        config = {"name": text(value.get("name", "Atlas V1 " + segment), "name", 160),
                  "kind": "v1-production", "model": model, "language": value.get("language", "zh"),
                  "concurrency": integer(value.get("concurrency", 2), "concurrency", 1, 2),
                  "timeout": integer(value.get("timeout", 900), "timeout", 30, 7200),
                  "repair_attempts": integer(value.get("repair_attempts", 1), "repair_attempts", 0, 2),
                  "acceptance_protocol": "atlas.acceptance-runner.v1",
                  "cognition_guidance": value.get("cognition_guidance", "")}
        if config["language"] not in {"zh", "en"}:
            raise FactoryError("language must be zh or en")
        if not isinstance(config["cognition_guidance"], str) or len(config["cognition_guidance"]) > 12000:
            raise FactoryError("invalid guidance")
        campaign_id = text(value.get("campaign_id", self._default_campaign()), "campaign_id", 200)
        seeds, excluded = [], []
        library = CaseLibrary(self.store)
        artifacts = self.store.artifacts()
        for sid in ids:
            try:
                scene, admission = self._admit(sid, policy)
                leaf = self.store.leaf(scene["leaf"])
                cases = library.list_cases(scenario_id=sid)
                basis, case_exclusions = select_case_basis(self.store, sid, scene["revision"])
                product_id = "product-" + digest({"scenario_id": sid})[:24]
                campaign = campaign_id
                reusable = next((a for a in artifacts if a.get("provenance", {}).get("v1", {}).get("campaign_id") == campaign
                                 and a.get("provenance", {}).get("v1", {}).get("product_id") == product_id
                                 and a["state"] == "published" and a.get("catalog_eligible") and a.get("review_status") == "passed"
                                 and a.get("provenance", {}).get("case_basis") == basis
                                 and a.get("scenario_revision") == scene["revision"]), None) if basis else None
                with self.store.connect() as con:
                    previous = con.execute("SELECT id,state FROM job WHERE kind='case-research' AND json_extract(snapshot,'$.v1.campaign_id')=? AND json_extract(snapshot,'$.v1.product_id')=? ORDER BY created_at DESC,rowid DESC LIMIT 1", (campaign, product_id)).fetchone()
                if not basis and previous and value.get("research_action") != "new_revision":
                    excluded.append({"scenario_id": sid, "code": "research_resume_required", "job_id": previous["id"],
                                     "reason": "Existing research must be resumed from its checkpoint; explicitly request new_revision for a genuinely new study."})
                    continue
                seeds.append({"product_id": "product-" + digest({"scenario_id": sid})[:24],
                              "leaf": leaf, "scenario": scene, "scenario_digest": digest(scene),
                              "admission": admission, "case_basis": basis,
                              "case_exclusions": case_exclusions,
                              "case_catalog_digest": digest([(c["case_id"], c["revision"], c["digest"]) for c in cases]),
                              "repository_hints": value.get("repository_hints", {}).get(sid, []),
                              "reuse_artifact": {"id": reusable["id"], "digest": reusable["digest"]} if reusable else None,
                              "next_stage": "reuse-published" if reusable else "template" if basis else "case-research",
                              "template_input_ready": bool(basis), "runtime_sample": sid in samples})
            except FactoryError as error:
                excluded.append({"scenario_id": sid, "code": error.code, "reason": str(error)})
        plan = {"schema": "atlas.batch-plan.v1", "id": uid("plan"), "created_at": now(),
                "policy_version": POLICY, "evidence_policy": "fixed-reviewed-code-v1",
                "admission_policy": policy, "support": SUPPORT, "segment": segment,
                "campaign_id": campaign_id,
                "config": config, "seeds": seeds, "excluded": excluded,
                "limits": {"max_products": 10, "cli_sessions": 500, "segment_seconds": 28800,
                           "production": config["concurrency"], "runtime": 1,
                           "business_repairs": 2, "transient_retries": 2}}
        plan["digest"] = digest(plan)
        with self.store.connect(True) as con:
            con.execute("INSERT INTO v1_plan VALUES(?,?,?,?)", (plan["id"], plan["digest"], canonical(plan), plan["created_at"]))
        return plan

    def plan(self, plan_id):
        with self.store.connect() as con:
            row = con.execute("SELECT body FROM v1_plan WHERE id=?", (plan_id,)).fetchone()
        if not row:
            raise FactoryError("batch plan not found", "not_found", 404)
        plan = json.loads(row[0])
        if digest({k: v for k, v in plan.items() if k != "digest"}) != plan["digest"]:
            raise FactoryError("plan digest mismatch", "integrity", 409)
        return plan

    def run(self, plan_id, value):
        plan = self.plan(plan_id)
        key = text(value.get("idempotency_key"), "idempotency_key", 200)
        if value.get("expected_plan_digest") != plan["digest"]:
            raise FactoryError("plan changed", "revision_conflict", 409)
        from .budget import BudgetLedger
        # Persistence must exist before a job can ever start its first model.
        ledger = BudgetLedger(self.store, campaign_id=plan["campaign_id"])
        batch_id = uid("bat")
        with self.store.connect(True) as con:
            prior = con.execute("SELECT * FROM v1_execution WHERE plan_id=? OR idempotency_key=?", (plan_id, key)).fetchone()
            if prior:
                if prior["plan_id"] != plan_id or prior["idempotency_key"] != key:
                    raise FactoryError("idempotency key belongs to a different execution", "conflict", 409)
                batch_id = prior["batch_id"]
            else:
                if not plan["seeds"]:
                    raise FactoryError("no admitted seed", "no_admitted_seed", 409)
                if plan["segment"] == "T08":
                    gate = con.execute("SELECT body FROM v1_campaign_gate WHERE campaign_id=? AND name='G1'", (plan["campaign_id"],)).fetchone()
                    gate_body = json.loads(gate[0]) if gate else {}
                    if (not gate_body.get("passed")
                            or gate_body.get("campaign_id") != plan["campaign_id"]
                            or gate_body.get("source_tree_sha256") != _g1_source_digest(self.store.pack.parent)):
                        raise FactoryError("G1 has not passed for this campaign; T08 is not allowed", "g1_required", 409)
                # Recheck inside queue write transaction. No half batch or model call on conflict.
                for seed in plan["seeds"]:
                    current = con.execute("SELECT body FROM scenario WHERE id=?", (seed["scenario"]["id"],)).fetchone()
                    if not current or digest(json.loads(current[0])) != seed["scenario_digest"] or self.store.leaf(seed["leaf"]["slug"])["fingerprint"] != seed["leaf"]["fingerprint"]:
                        raise FactoryError("scenario/leaf changed since preview", "stale_plan", 409)
                    if seed["admission"]["kind"] == "batch_policy":
                        _, current_admission = self._admit(seed["scenario"]["id"], plan["admission_policy"])
                        if current_admission != seed["admission"]:
                            raise FactoryError("admission review changed since preview", "stale_plan", 409)
                    if seed["case_basis"]:
                        from .cases import CaseLibrary
                        CaseLibrary(self.store, initialize=False).require_admissible(seed["case_basis"])
                    if seed.get("reuse_artifact"):
                        reused = con.execute("SELECT digest,state FROM artifact WHERE id=?", (seed["reuse_artifact"]["id"],)).fetchone()
                        from .v1_catalog import review_status
                        if not reused or reused["digest"] != seed["reuse_artifact"]["digest"] or reused["state"] != "published" or review_status(con, seed["reuse_artifact"]["id"], reused["digest"]) != "passed":
                            raise FactoryError("selected reusable template changed since preview", "stale_plan", 409)
                    from .cases import CaseLibrary
                    current_cases = CaseLibrary(self.store, initialize=False).list_cases(scenario_id=seed["scenario"]["id"])
                    if digest([(c["case_id"], c["revision"], c["digest"]) for c in current_cases]) != seed["case_catalog_digest"]:
                        raise FactoryError("case catalog changed since preview", "stale_plan", 409)
                at = now()
                ledger.begin_segment(plan["segment"], con=con)
                known = {r[0] for r in con.execute("SELECT product_id FROM v1_campaign_product WHERE campaign_id=?", (plan["campaign_id"],))}
                planned = {seed["product_id"] for seed in plan["seeds"]}
                if len(known | planned) > 10:
                    raise FactoryError("campaign product cap includes G1 and previous plans", "product_limit", 409)
                for seed in plan["seeds"]:
                    con.execute("INSERT OR IGNORE INTO v1_campaign_product VALUES(?,?,?)", (plan["campaign_id"], seed["product_id"], seed["scenario"]["id"]))
                con.execute("INSERT INTO batch VALUES(?,?,?,?)", (batch_id, "running", canonical(plan["config"]), at))
                con.execute("INSERT INTO v1_execution VALUES(?,?,?,?,?)", (plan_id, plan["digest"], key, batch_id, at))
                for seed in plan["seeds"]:
                    if seed.get("reuse_artifact"):
                        continue
                    v1 = {"campaign_id": plan["campaign_id"], "plan_id": plan_id, "plan_digest": plan["digest"],
                          "product_id": seed["product_id"], "segment": plan["segment"], "policy_version": POLICY}
                    snap = {**seed, "v1": v1, "config": plan["config"], "source_url": ""}
                    kind = "blueprint-production" if seed["case_basis"] else "case-research"
                    con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (uid("job"), batch_id, kind, "queued", kind, 1, None, None, canonical(snap), None, at, at))
        return {"plan_id": plan_id, "plan_digest": plan["digest"], "batch": self.store.batch(batch_id)}

    def execution(self, plan_id):
        with self.store.connect() as con:
            row = con.execute("SELECT batch_id FROM v1_execution WHERE plan_id=?", (plan_id,)).fetchone()
        return self.store.batch(row[0]) if row else None

    def gate(self, campaign_id, name="G1"):
        """Read a host-assessed campaign gate; never mutates or grants it."""
        with self.store.connect() as con:
            row = con.execute("SELECT body FROM v1_campaign_gate WHERE campaign_id=? AND name=?",
                              (str(campaign_id), str(name))).fetchone()
        return json.loads(row[0]) if row else None

    def action(self, plan_id, action):
        if action not in {"pause", "resume", "cancel"}:
            raise FactoryError("invalid batch action")
        plan = self.plan(plan_id)
        with self.store.connect(True) as con:
            execution = con.execute("SELECT batch_id FROM v1_execution WHERE plan_id=?", (plan_id,)).fetchone()
            if not execution:
                raise FactoryError("plan not started", "not_started", 409)
            # One BEGIN IMMEDIATE covers parent and every currently queued
            # successor/runtime batch. Queue writers cannot slip between child
            # discovery and the state update; claim also fences descendants by
            # their authoritative parent plan state.
            batch_ids = {execution["batch_id"]}
            batch_ids.update(row[0] for row in con.execute(
                "SELECT DISTINCT batch_id FROM job WHERE json_extract(snapshot,'$.v1.plan_id')=?",
                (plan_id,),
            ))
            rows = {row["id"]: row for row in con.execute(
                "SELECT id,state FROM batch WHERE id IN (%s)" % ",".join("?" for _ in batch_ids),
                tuple(sorted(batch_ids)),
            )}
            if len(rows) != len(batch_ids):
                raise FactoryError("plan batch is unavailable", "not_found", 404)
            if action != "cancel" and any(row["state"] == "cancelled" for row in rows.values()):
                raise FactoryError("cancelled batch cannot resume", "conflict", 409)
            state = {"pause": "paused", "resume": "running", "cancel": "cancelled"}[action]
            at = now()
            con.executemany("UPDATE batch SET state=? WHERE id=?", [(state, batch_id) for batch_id in sorted(batch_ids)])
            if action == "cancel":
                placeholders = ",".join("?" for _ in batch_ids)
                con.execute(
                    f"UPDATE job SET state='cancelled',token=NULL,lease=NULL,updated_at=? WHERE batch_id IN ({placeholders}) AND state IN ('queued','running')",
                    (at, *sorted(batch_ids)),
                )
        return {"plan_id": plan_id, "plan_digest": plan["digest"], "batch": self.store.batch(execution["batch_id"])}

    def assess_g1(self, plan_id, verification_manifest_path):
        """Assess and persist G1 from host evidence; this is deliberately not an API action.

        The method does not run commands or call a provider. It verifies a completed
        plan, current case/template/runtime records, local external-evidence files,
        and host test logs bound to the current source/test tree.
        """
        from .api import controlled_path
        from .blueprints import verify_frozen
        from .cases import CaseLibrary
        from .runtime_jobs import tree_manifest
        from .v1_catalog import catalog_eligibility, review_status

        plan = self.plan(plan_id)
        workspace = self.store.pack.parent.resolve()
        reasons = []
        if plan.get("segment") != "G1":
            reasons.append("plan_is_not_G1")
        if not plan.get("seeds"):
            reasons.append("plan_has_no_admitted_products")
        sample = next((seed for seed in plan.get("seeds", []) if seed.get("runtime_sample")), None)
        if sample is None:
            reasons.append("G1_runtime_sample_not_prespecified")
        if sample is None:
            sample_scenario_id = None
        else:
            sample_scenario_id = sample.get("scenario", {}).get("id")
        resolved_basis = sample.get("case_basis") if sample else None
        if sample and not resolved_basis:
            # Research is a separate checkpointed stage. The immutable preview
            # stays basis-null; its successor production job pins the research
            # result and is the authoritative fixed snapshot for G1.
            with self.store.connect() as con:
                rows = list(con.execute(
                    "SELECT snapshot,state,created_at,rowid FROM job "
                    "WHERE json_extract(snapshot,'$.v1.plan_id')=? "
                    "AND json_extract(snapshot,'$.v1.product_id')=? "
                    "ORDER BY created_at DESC,rowid DESC",
                    (plan_id, sample.get("product_id")),
                ))
            for row in rows:
                try:
                    snapshot = json.loads(row["snapshot"])
                except (TypeError, ValueError):
                    continue
                candidate_basis = snapshot.get("case_basis")
                candidate_scene = snapshot.get("scenario", {})
                if (row["state"] in {"queued", "running", "completed"}
                        and candidate_basis
                        and candidate_scene.get("id") == sample.get("scenario", {}).get("id")
                        and candidate_scene.get("revision") == sample.get("scenario", {}).get("revision")):
                    resolved_basis = candidate_basis
                    break
        if sample is None or not resolved_basis:
            reasons.append("sample_has_no_fixed_case_basis")

        # A host assessment checks the persisted queue instead of trusting a
        # client-supplied report or gate value.
        batch_report = self.report(plan_id)
        if (not batch_report.get("batch") or batch_report["batch"].get("state") in {"paused", "cancelled"}
                or any(job["state"] in {"queued", "running", "paused_budget"} for job in (batch_report.get("batch") or {}).get("jobs", []))):
            reasons.append("G1_queue_not_quiescent")

        artifact = None
        if sample:
            matching_artifacts = [item for item in batch_report.get("artifacts", [])
                                  if item.get("artifact_type") == "product-blueprint"
                                  and item.get("provenance", {}).get("v1", {}).get("campaign_id") == plan["campaign_id"]
                                  and item.get("provenance", {}).get("v1", {}).get("plan_id") == plan_id
                                  and item.get("provenance", {}).get("v1", {}).get("product_id") == sample.get("product_id")
                                  and item.get("provenance", {}).get("case_basis") == resolved_basis]
            artifact = max(matching_artifacts, key=lambda item: (item.get("created_at", ""), item.get("revision", 0), item.get("id", "")), default=None)
        target_binding = None
        target_binding_digest = None
        runtime_run_id = None
        delivery_checkpoint = None
        delivery_job_snapshot = None
        if artifact is None:
            reasons.append("sample_template_missing")
        else:
            basis = artifact.get("provenance", {}).get("case_basis")
            if basis != resolved_basis:
                reasons.append("template_case_basis_mismatch")
            if not basis:
                reasons.append("template_case_basis_missing")
            else:
                try:
                    CaseLibrary(self.store, initialize=False).require_admissible(basis)
                except FactoryError as error:
                    reasons.append("template_case_basis_not_admissible:" + error.code)
            try:
                with self.store.connect() as con:
                    current_review = review_status(con, artifact["id"], artifact["digest"])
                eligibility = catalog_eligibility(self.store, artifact)
                if artifact.get("state") != "published" or not artifact.get("catalog_eligible") or not eligibility.get("catalog_eligible"):
                    reasons.append("sample_template_not_currently_catalog_eligible")
                if current_review != "passed":
                    reasons.append("sample_template_review_not_passed")
                bundle = controlled_path(self.store, artifact["bundle_path"])
                frozen = verify_frozen(bundle, artifact["digest"])
                if frozen.get("case_basis") != basis:
                    reasons.append("frozen_template_case_basis_mismatch")
            except (FactoryError, OSError, ValueError, KeyError) as error:
                reasons.append("sample_template_integrity_failed:" + getattr(error, "code", type(error).__name__))

            # Latest target run wins. An older pass cannot conceal a later
            # unavailable, stale or different-phase run.
            with self.store.connect() as con:
                runtime_jobs = list(con.execute(
                    "SELECT id,state,snapshot,attempt FROM job WHERE kind='blueprint-runtime' "
                    "AND json_extract(snapshot,'$.artifact_id')=? ORDER BY created_at DESC,rowid DESC",
                    (artifact["id"],),
                ))
                latest = runtime_jobs[0] if runtime_jobs else None
                run_row = con.execute(
                    "SELECT body FROM acceptance WHERE artifact_id=? AND job_id=? ORDER BY created_at DESC,rowid DESC LIMIT 1",
                    (artifact["id"], latest["id"] if latest else ""),
                ).fetchone() if latest else None
                development_rows = list(con.execute(
                    "SELECT id,state,snapshot FROM job WHERE kind='application-development' "
                    "AND json_extract(snapshot,'$.artifact_id')=? "
                    "ORDER BY created_at DESC,rowid DESC",
                    (artifact["id"],),
                ))
                for development_row in development_rows:
                    if development_row["state"] != "completed":
                        continue
                    try:
                        development_snapshot = json.loads(development_row["snapshot"])
                    except (TypeError, ValueError):
                        continue
                    cp = con.execute(
                        "SELECT body FROM checkpoint WHERE job_id=? AND name='application-delivery'",
                        (development_row["id"],),
                    ).fetchone()
                    if cp:
                        try:
                            checkpoint_record = json.loads(cp["body"])
                            checkpoint_body = checkpoint_record.get("result") if isinstance(checkpoint_record, dict) else None
                        except (TypeError, ValueError):
                            continue
                        if (isinstance(checkpoint_body, dict)
                                and development_snapshot.get("artifact_digest") == artifact.get("digest")
                                and development_snapshot.get("phase") == "P0"
                                and development_snapshot.get("case_basis") == resolved_basis
                                and checkpoint_body.get("case_basis_digest") == (resolved_basis or {}).get("basis_digest")):
                            delivery_checkpoint = checkpoint_body
                            delivery_job_snapshot = development_snapshot
                            break
            if delivery_checkpoint is None:
                reasons.append("P0_development_delivery_checkpoint_missing")
            if not latest or not run_row:
                reasons.append("P0_runtime_run_missing")
            else:
                runtime_run_id = json.loads(run_row[0]).get("id")
                runtime_snapshot = json.loads(latest["snapshot"])
                runtime = json.loads(run_row[0])
                target_binding = runtime.get("target_binding")
                if latest["state"] != "completed":
                    reasons.append("P0_runtime_job_not_completed")
                if runtime_snapshot.get("selected_phase") != "P0" or runtime.get("selected_phase") != "P0":
                    reasons.append("P0_runtime_phase_mismatch")
                if runtime.get("method") != "blueprint-runtime" or runtime.get("digest") != artifact["digest"]:
                    reasons.append("P0_runtime_artifact_binding_mismatch")
                if (runtime.get("outcome") != "passed" or runtime.get("suite_status") != "passed"
                        or runtime.get("phase_status") != "passed" or runtime.get("startup", {}).get("status") != "passed"
                        or runtime.get("cleanup", {}).get("success") is not True):
                    reasons.append("P0_runtime_suite_or_cleanup_not_passed")
                if not isinstance(target_binding, dict) or target_binding != runtime_snapshot.get("target_binding"):
                    reasons.append("P0_runtime_target_binding_mismatch")
                else:
                    target_binding_digest = digest(target_binding)
                    if (target_binding.get("artifact_id") != artifact["id"]
                            or target_binding.get("artifact_digest") != artifact["digest"]
                            or target_binding.get("scenario_id") != sample_scenario_id
                            or target_binding.get("scenario_revision") != sample.get("scenario", {}).get("revision")
                            or target_binding.get("case_basis_digest") != (resolved_basis or {}).get("basis_digest")
                            or target_binding.get("selected_phase") != "P0"
                            or not target_binding.get("application_digest") or not target_binding.get("suite_digest")):
                        reasons.append("P0_runtime_binding_does_not_match_fixed_sample")
                selected_cases = target_binding.get("selected_case_ids", []) if isinstance(target_binding, dict) else []
                results = runtime.get("case_results", [])
                passed_cases = {item.get("id") for item in results if item.get("status") == "passed"}
                if not selected_cases or not set(selected_cases) <= passed_cases:
                    reasons.append("P0_required_cases_not_all_passed")
                required = runtime.get("required_evidence", [])
                registered = runtime.get("registered_phase_evidence", {})
                if not required or not isinstance(registered, dict) or any(item.get("id") not in registered for item in required):
                    reasons.append("P0_independent_external_evidence_missing")
                else:
                    # Re-open each registered proof below the host-controlled
                    # runtime evidence directory and verify bytes and binding.
                    for requirement in required:
                        record = registered[requirement["id"]]
                        evidence_path = record.get("evidence_path", "")
                        prefix = f"jobs/{latest['id']}/attempt-{latest['attempt']}/runtime-evidence/external/"
                        if not isinstance(evidence_path, str) or not evidence_path.startswith(prefix):
                            reasons.append("P0_external_evidence_path_invalid:" + str(requirement.get("id")))
                            continue
                        try:
                            proof_path = controlled_path(self.store, evidence_path)
                            raw = proof_path.read_bytes()
                            proof = json.loads(raw)
                            if hashlib.sha256(raw).hexdigest() != record.get("sha256"):
                                reasons.append("P0_external_evidence_digest_mismatch:" + str(requirement.get("id")))
                            if (proof.get("schema") != "atlas.phase-evidence.v1"
                                    or proof.get("requirement_id") != requirement.get("id")
                                    or proof.get("target_digest") != target_binding_digest
                                    or proof.get("outcome") != "passed"
                                    or proof.get("executor") != record.get("executor")):
                                reasons.append("P0_external_evidence_binding_invalid:" + str(requirement.get("id")))
                        except (FactoryError, OSError, ValueError, TypeError) as error:
                            reasons.append("P0_external_evidence_unreadable:" + str(requirement.get("id")) + ":" + getattr(error, "code", type(error).__name__))

                # Prove the tested target is still the exact saved delivery,
                # not merely an uploaded project name or runtime flag.
                try:
                    submission = controlled_path(self.store, runtime_snapshot["submission_path"])
                    receipt_path = submission.parent / "delivery-receipt.json"
                    archive_path = submission.parent / "application.zip"
                    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
                    app_root = receipt["app_root"]
                    app_path = controlled_path(self.store, str((submission / app_root).relative_to(self.store.root)))
                    inventory = tree_manifest(app_path)
                    app_digest = hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
                    archive_digest = _sha256_file(archive_path)
                    if (not isinstance(target_binding, dict)
                            or receipt != runtime_snapshot.get("delivery")
                            or archive_digest != runtime_snapshot.get("archive_sha256")
                            or app_digest != target_binding.get("application_digest")):
                        reasons.append("P0_application_delivery_binding_invalid")
                    if (delivery_checkpoint is not None
                            and (delivery_checkpoint.get("archive_sha256") != archive_digest
                                 or delivery_checkpoint.get("application_digest") != app_digest
                                 or delivery_checkpoint.get("delivery_receipt") != receipt
                                 or delivery_job_snapshot.get("handoff_sha256") != delivery_checkpoint.get("handoff_sha256"))):
                        reasons.append("P0_development_delivery_does_not_match_runtime")
                    if delivery_checkpoint is not None:
                        try:
                            original_delivery = controlled_path(self.store, delivery_checkpoint.get("archive_path", ""))
                            if _sha256_file(original_delivery) != archive_digest:
                                reasons.append("P0_development_delivery_archive_hash_mismatch")
                        except (FactoryError, OSError, TypeError) as error:
                            reasons.append("P0_development_delivery_archive_unreadable:" + getattr(error, "code", type(error).__name__))
                except (FactoryError, OSError, ValueError, TypeError, KeyError) as error:
                    reasons.append("P0_application_delivery_unreadable:" + getattr(error, "code", type(error).__name__))

        # Use a local path and fresh logs with cryptographic hashes. The
        # manifest cannot grant a pass by setting a boolean: each required
        # command, exit, skip count, log and source-tree binding is inspected.
        check_plan = {**plan, "_workspace_root": str(workspace)}
        try:
            manifest_path = Path(verification_manifest_path).expanduser()
            if not manifest_path.is_absolute():
                manifest_path = workspace / manifest_path
            manifest_path = manifest_path.resolve(strict=True)
            manifest_digest = _sha256_file(manifest_path)
            reasons.extend(_manifest_check_failures(manifest_path, check_plan, sample_scenario_id))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if not isinstance(manifest, dict):
                manifest = {}
            if manifest.get("support_scope") != plan.get("support"):
                reasons.append("manifest_support_scope_mismatch")
            export = manifest.get("development_export") if isinstance(manifest, dict) else None
            if not isinstance(export, dict) or not artifact:
                reasons.append("standard_development_export_missing")
            else:
                if (export.get("artifact_id") != artifact.get("id")
                        or export.get("artifact_digest") != artifact.get("digest")
                        or export.get("selected_phase") != "P0"):
                    reasons.append("standard_development_export_binding_mismatch")
                try:
                    export_path = controlled_path(self.store, export.get("archive_path", ""))
                    if _sha256_file(export_path) != export.get("archive_sha256"):
                        reasons.append("standard_development_export_digest_mismatch")
                    with ZipFile(export_path) as archive:
                        members = set(archive.namelist())
                        if not {"HANDOFF.md", "CURRENT_PHASE.json", "ACCEPTANCE_CONTRACT.json"} <= members:
                            reasons.append("standard_development_export_incomplete")
                        current = json.loads(archive.read("CURRENT_PHASE.json"))
                        contract = json.loads(archive.read("ACCEPTANCE_CONTRACT.json"))
                        current_basis = current.get("case_basis") if isinstance(current.get("case_basis"), dict) else {}
                        if (current.get("template_digest") != artifact.get("digest")
                                or current.get("selected_phase") != "P0"
                                or current_basis.get("basis_digest") != (resolved_basis or {}).get("basis_digest")
                                or contract.get("template_digest") != artifact.get("digest")
                                or contract.get("selected_phase") != "P0"
                                or contract.get("case_basis_digest") != (resolved_basis or {}).get("basis_digest")):
                            reasons.append("standard_development_export_contents_mismatch")
                except (FactoryError, OSError, ValueError, KeyError, BadZipFile, TypeError) as error:
                    reasons.append("standard_development_export_unreadable:" + getattr(error, "code", type(error).__name__))
        except (OSError, TypeError, ValueError):
            manifest_digest = None
            reasons.append("manifest_missing_or_unreadable")

        # Keep deterministic reason ordering and write the campaign-scoped
        # gate atomically. No legacy/global v1_gate entry can unlock T08.
        reasons = list(dict.fromkeys(reasons))
        result = {
            "schema": "atlas.g1-assessment.v1", "campaign_id": plan["campaign_id"],
            "plan_id": plan_id, "plan_digest": plan["digest"],
            "sample_scenario_id": sample_scenario_id,
            "artifact_id": artifact.get("id") if artifact else None,
            "artifact_digest": artifact.get("digest") if artifact else None,
            "case_basis_digest": (resolved_basis or {}).get("basis_digest") if sample else None,
            "runtime_run_id": runtime_run_id, "target_binding_digest": target_binding_digest,
            "development_delivery_archive_sha256": delivery_checkpoint.get("archive_sha256") if delivery_checkpoint else None,
            "manifest_path": str(manifest_path.relative_to(workspace)) if 'manifest_path' in locals() and manifest_path.is_relative_to(workspace) else None,
            "manifest_sha256": manifest_digest,
            "source_tree_sha256": _g1_source_digest(workspace),
            "passed": not reasons, "status": "passed" if not reasons else "blocked",
            "reasons": reasons, "assessed_at": now(),
        }
        with self.store.connect(True) as con:
            con.execute(
                "INSERT INTO v1_campaign_gate(campaign_id,name,body,created_at) VALUES(?, 'G1', ?, ?) "
                "ON CONFLICT(campaign_id,name) DO UPDATE SET body=excluded.body,created_at=excluded.created_at",
                (plan["campaign_id"], canonical(result), result["assessed_at"]),
            )
        return result

    def complete_research(self, job, basis):
        """Research checkpoint remains independently reusable if later construction fails."""
        from .cases import CaseLibrary
        CaseLibrary(self.store).validate_basis(basis)
        with self.store.connect(True) as con:
            owned = con.execute("SELECT * FROM job WHERE id=? AND token=? AND state='running' AND lease>?", (job["id"], job["token"], time.time())).fetchone()
            if not owned:
                raise FactoryError("research ownership lost", "lease_lost", 409)
            snapshot = json.loads(owned["snapshot"])
            snapshot["case_basis"] = basis
            snapshot["next_stage"] = "template"
            at = now()
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (uid("job"), job["batch_id"], "blueprint-production", "queued", "blueprint-generate", 1, None, None, canonical(snapshot), None, at, at))
            con.execute("UPDATE job SET state='completed',stage='case-committed',updated_at=? WHERE id=?", (at, job["id"]))
            con.execute("INSERT OR REPLACE INTO checkpoint VALUES(?,?,?)", (job["id"], "committed-case-basis", canonical({"result": basis, "digest": digest(basis)})))

    def report(self, plan_id):
        plan, batch = self.plan(plan_id), self.execution(plan_id)
        reuse_ids = {seed["reuse_artifact"]["id"] for seed in plan["seeds"] if seed.get("reuse_artifact")}
        artifacts = [a for a in self.store.artifacts() if a.get("provenance", {}).get("v1", {}).get("plan_id") == plan_id or a["id"] in reuse_ids]
        products = {}
        for a in artifacts:
            pid = a["provenance"]["v1"]["product_id"]
            p = products.setdefault(pid, {"artifact_ids": [], "reviewed": False, "published": False, "p0_runtime": False})
            p["artifact_ids"].append(a["id"])
            p["reviewed"] |= a.get("review_status") == "passed"
            p["published"] |= a["state"] == "published" and a.get("catalog_eligible", False)
            p["p0_runtime"] |= a["state"] == "published" and a.get("catalog_eligible", False) and any(r.get("method") == "blueprint-runtime" and r.get("phase_status") == "passed" and r.get("selected_phase") == "P0" and r.get("digest") == a["digest"] for r in a["acceptances"])
        jobs = batch["jobs"] if batch else []
        if batch:
            with self.store.connect() as con:
                related = [self.store._job(r) for r in con.execute("SELECT * FROM job WHERE json_extract(snapshot,'$.v1.plan_id')=? ORDER BY created_at,rowid", (plan_id,))]
            jobs = related
            batch["jobs"] = related
            if batch["state"] not in {"paused", "cancelled"}:
                batch["state"] = "running" if any(j["state"] in {"queued", "running"} for j in related) else "completed" if all(j["state"] == "completed" for j in related) else "needs_attention"
        n = len(plan["seeds"])
        sample_ids = [s["scenario"]["id"] for s in plan["seeds"] if s["runtime_sample"]]
        sample_passed = [s["scenario"]["id"] for s in plan["seeds"] if s["runtime_sample"] and products.get(s["product_id"], {}).get("p0_runtime")]
        counts = {"products_planned": n, "candidate_products": len(products), "frozen_versions": len(artifacts),
                  "formally_published_versions": sum(a["state"] == "published" for a in artifacts),
                  "reviewed_products": sum(p["reviewed"] for p in products.values()),
                  "published_products": sum(p["published"] for p in products.values()),
                  "p0_runtime_products": sum(p["p0_runtime"] for p in products.values()),
                  "queue_completed": sum(j["state"] == "completed" for j in jobs), "queue_total": len(jobs),
                  "sample_passed": len(sample_passed), "sample_required": len(sample_ids)}
        quality = "not_run" if not batch else "in_progress"
        if batch and batch["state"] in {"completed", "needs_attention", "cancelled"}:
            quality = "passed" if n and counts["published_products"] == n and len(sample_ids) >= 3 and len(sample_passed) == len(sample_ids) else "partial"
        from .budget import BudgetLedger
        ledger = BudgetLedger(self.store, campaign_id=plan["campaign_id"])
        report = {"schema": "atlas.batch-report.v1", "plan": plan, "batch": batch, "counts": counts,
                "products": products, "artifacts": artifacts, "quality_result": quality,
                "runtime_targets": [{"artifact_id": a["id"], "artifact_digest": a["digest"], "run_id": r["id"], "phase_status": r.get("phase_status"), "target_binding": r.get("target_binding"), "environment": r.get("environment"), "report": r.get("job_id")} for a in artifacts for r in a["acceptances"] if r.get("method") == "blueprint-runtime"],
                "runtime_sampling_gate": "passed" if len(sample_ids) >= 3 and sample_ids == sample_passed else "not_passed",
                "failed_items": [{"job_id": j["id"], "stage": j["stage"], "state": j["state"], "error": j["error"],
                                  "recovery": "/api/factory/jobs/" + j["id"] + "/retry"} for j in jobs if j["state"] in {"failed", "interrupted", "needs_review", "paused_budget"}],
                "budget": ledger.status(), "provider_requests": None, "cost": None,
                "next_batch": {"automatic_expansion": False, "recommendation": "Review this fixed batch, address missing evidence, then explicitly freeze the next range."}}
        from .v1_reporting import enrich_report
        report["evidence_report"] = enrich_report(self.store, report)
        return report
