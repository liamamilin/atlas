"""Run pinned blueprint acceptance programs against an isolated application."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import time
import uuid

from atlas_runtime import atomic_json
from privacy import redact_text
from .artifacts import copy_tree, relative, tree_manifest
from .blueprints import read_json
from .runtime import DockerVerifier, IMAGES
from .store import FactoryError

RUNNER_SCHEMA = "atlas.acceptance-runner.v1"
RESULT_SCHEMA = "atlas.acceptance-result.v1"
PLACEHOLDERS = {"base_url", "app_root", "data_dir", "case_id"}
MAX_CASES = 500


def _invalid(message, code="acceptance_adapter_invalid"):
    raise FactoryError(message, code, 409)


def validate_runner_manifest(source, spec, phase=None):
    """Validate runner.json against the normative acceptance rows in ``spec``."""
    path = Path(source) / "acceptance/runner.json"
    if not path.is_file() or path.is_symlink():
        _invalid("blueprint acceptance runner binding is missing", "acceptance_adapter_missing")
    try:
        value = read_json(path)
    except FactoryError as error:
        raise FactoryError("invalid acceptance runner manifest JSON", "acceptance_adapter_invalid", 409) from error
    if (not isinstance(value, dict) or set(value) != {"schema", "result_schema", "cases"}
            or value.get("schema") != RUNNER_SCHEMA
            or value.get("result_schema") != RESULT_SCHEMA):
        _invalid("invalid acceptance runner manifest")
    rows = spec.get("acceptance") if isinstance(spec, dict) else None
    if not isinstance(rows, list) or not rows or len(rows) > MAX_CASES:
        _invalid("normative blueprint acceptance cases are invalid")
    normative = {}
    for row in rows:
        if (not isinstance(row, dict) or not isinstance(row.get("id"), str)
                or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,199}", row["id"])):
            _invalid("normative blueprint acceptance case is invalid")
        if row["id"] in normative:
            _invalid("duplicate normative acceptance case id")
        implementation = row.get("implementation")
        try:
            implementation = relative(implementation)
        except FactoryError as error:
            raise FactoryError("normative acceptance implementation path is invalid", "acceptance_adapter_invalid", 409) from error
        suffix = Path(implementation).suffix
        if suffix not in {".py", ".js", ".mjs", ".cjs"}:
            _invalid("unsupported acceptance implementation", "acceptance_adapter_missing")
        impl = Path(source) / implementation
        if impl.is_symlink() or not impl.is_file():
            _invalid("normative acceptance implementation is missing", "acceptance_adapter_missing")
        normative[row["id"]] = {"implementation": implementation, "language": "python" if suffix == ".py" else "node", "phase": row.get("phase")}
    bindings = value.get("cases")
    if not isinstance(bindings, dict) or set(bindings) != set(normative):
        _invalid("runner bindings must exactly match normative acceptance case ids")
    checked = {}
    for case_id in normative:
        binding = bindings[case_id]
        if not isinstance(binding, dict) or set(binding) != {"args"}:
            _invalid("each runner binding must contain only args")
        args = binding["args"]
        if not isinstance(args, list) or len(args) > 100:
            _invalid("acceptance runner args must be a bounded list")
        rendered = []
        for arg in args:
            if isinstance(arg, str):
                if len(arg) > 4000 or any(c in arg for c in ("\x00", "\n", "\r")):
                    _invalid("invalid acceptance runner argument")
                if arg.startswith("{") or arg.endswith("}") or "{" in arg or "}" in arg:
                    token = arg[1:-1] if arg.startswith("{") and arg.endswith("}") else None
                    if token not in PLACEHOLDERS:
                        _invalid("runner placeholder must be a supported standalone token")
                    rendered.append({"placeholder": token})
                else:
                    rendered.append({"literal": arg})
            else:
                _invalid("runner args must be strings")
        checked[case_id] = {**normative[case_id], "args": rendered}
    phase_rows = spec.get("phases", [])
    if phase is None:
        selected = set(normative)
        selected_phases = [r.get("id") for r in phase_rows if isinstance(r, dict)]
    else:
        phase_id = phase.get("id") if isinstance(phase, dict) else phase
        if not isinstance(phase_id, str):
            _invalid("invalid requested blueprint phase")
        ids = [r.get("id") for r in phase_rows if isinstance(r, dict)]
        if phase_id not in ids:
            _invalid("requested blueprint phase does not exist")
        selected_phases = ids[:ids.index(phase_id) + 1]
        selected = {cid for cid, item in normative.items() if item["phase"] in selected_phases}
    if not selected:
        _invalid("requested phase has no pinned acceptance cases", "acceptance_adapter_missing")
    return {"schema": RUNNER_SCHEMA, "result_schema": RESULT_SCHEMA,
            "cases": {key: checked[key] for key in normative},
            "selected_case_ids": [key for key in normative if key in selected],
            "selected_phases": selected_phases}


def phase_required_evidence(spec, phase):
    """Return immutable host evidence requirements for a phase.

    Absence preserves the legacy contract. Declared external items are not
    satisfied by application uploads or by acceptance suite output.
    """
    phase_id = phase.get("id") if isinstance(phase, dict) else phase
    mapping = spec.get("phase_required_evidence")
    if mapping is None:
        return []
    if not isinstance(mapping, dict):
        raise FactoryError("phase_required_evidence must be a phase map")
    phase_rows = [row.get("id") for row in spec.get("phases", []) if isinstance(row, dict)]
    phases = set(phase_rows)
    if not set(mapping) <= phases:
        raise FactoryError("phase evidence references an undeclared phase")
    if phase_id is not None and phase_id not in phases:
        raise FactoryError("phase evidence requested for an undeclared phase")
    selected_through = phase_rows if phase_id is None else phase_rows[:phase_rows.index(phase_id) + 1]
    result, seen = [], set()
    for selected in phase_rows:
        items = mapping.get(selected, [])
        if not isinstance(items, list) or len(items) > 30:
            raise FactoryError("phase evidence must contain at most 30 items per phase")
        for item in items:
            if not isinstance(item, dict):
                raise FactoryError("phase evidence item must be an object")
            identifier, description, executor = item.get("id"), item.get("description"), item.get("executor")
            if (item.get("kind") != "external"
                    or not isinstance(identifier, str) or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", identifier)
                    or identifier in seen or not isinstance(description, str) or not description.strip()
                    or len(description) > 2000 or not isinstance(executor, str)
                    or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", executor)):
                raise FactoryError("invalid or duplicate phase evidence requirement")
            seen.add(identifier)
            if selected in selected_through:
                result.append({"id": identifier, "kind": "external", "description": description.strip(), "executor": executor})
    return result


def _strict_result(text, case_id):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("duplicate key")
            out[key] = value
        return out
    def constant(_):
        raise ValueError("non-finite number")
    try:
        # Each invocation emits one protocol JSON object; ignore no surrounding text.
        value = json.loads(text, object_pairs_hook=pairs, parse_constant=constant)
    except (ValueError, TypeError, RecursionError):
        return None
    if (not isinstance(value, dict) or set(value) != {"schema", "case_id", "status", "assertions"}
            or value.get("schema") != RESULT_SCHEMA
            or value.get("case_id") != case_id or value.get("status") not in {"passed", "failed", "unverified"}
            or not isinstance(value.get("assertions"), list) or not value["assertions"]):
        return None
    seen = set()
    for assertion in value["assertions"]:
        if (not isinstance(assertion, dict) or set(assertion) != {"id", "passed", "detail"}
                or not isinstance(assertion.get("id"), str) or not assertion["id"]
                or assertion["id"] in seen or type(assertion.get("passed")) is not bool
                or not isinstance(assertion.get("detail"), str)):
            return None
        seen.add(assertion["id"])
    return value


class BlueprintRuntimeVerifier(DockerVerifier):
    """Execute frozen, authored acceptance programs in restricted Docker containers."""

    def _budget_call(self, argv, cancelled, deadline, timeout=None):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise FactoryError("blueprint verification timed out", "verification_timeout", 409)
        return self._call(argv, cancelled, min(timeout, remaining) if timeout is not None else remaining)

    def _startup_capture(self, name, deadline, report):
        diagnostic_deadline = deadline
        if diagnostic_deadline <= time.monotonic():
            diagnostic_deadline = time.monotonic() + 5
        captured = {}
        for label, path in (("stdout", "/state/startup.stdout"), ("stderr", "/state/startup.stderr")):
            try:
                result = self._budget_call(["exec", name, "cat", path], lambda: False, diagnostic_deadline, 5)
                captured[label] = redact_text(result["output"])[-16000:]
            except Exception as error:
                captured[label] = ""
                report.setdefault("startup_capture_errors", []).append(redact_text(str(error))[:500])
        if report.get("startup"):
            report["startup"]["captured_output"] = captured

    def verify(self, app, source, spec, phase, evidence, runtime, cancelled=lambda: False, progress=lambda _: None):
        deadline = time.monotonic() + self.timeout
        source_path, app_path = Path(source), Path(app)
        if source_path.is_symlink() or app_path.is_symlink():
            raise FactoryError("blueprint and application roots cannot be symlinks", "runtime_unavailable", 409)
        source, app, evidence = source_path.resolve(), app_path.resolve(), Path(evidence)
        manifest = validate_runner_manifest(source, spec, phase)
        required_evidence = phase_required_evidence(spec, phase)
        if not isinstance(runtime, dict) or runtime.get("profile") not in {"python-web", "node-web", "static-web", "cli"}:
            raise FactoryError("unsupported application runtime", "runtime_unavailable", 409)
        if not app.is_dir() or app.is_symlink():
            raise FactoryError("application source directory is unavailable", "runtime_unavailable", 409)
        if not self.executable:
            raise FactoryError("Docker is not installed", "runtime_unavailable", 503)
        evidence.mkdir(parents=True, exist_ok=True)
        app_hash_before = tree_manifest(app)
        app_digest_before = hashlib.sha256(json.dumps(app_hash_before, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        suite_inventory = tree_manifest(source)
        suite_digest = hashlib.sha256(json.dumps(suite_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        work_root = Path(tempfile.mkdtemp(prefix="atlas-blueprint-runtime-"))
        app_copy, suite_copy = work_root / "application", work_root / "suite"
        try:
            copy_tree(app, app_copy)
            copy_tree(source, suite_copy)
        except Exception:
            shutil.rmtree(work_root, ignore_errors=True)
            raise
        prefix = "atlas-blueprint-" + uuid.uuid4().hex[:20]
        app_name, test_name = prefix + "-app", prefix + "-test"
        app_profile = runtime["profile"]
        lang = manifest["cases"][manifest["selected_case_ids"][0]]["language"] if manifest["selected_case_ids"] else "python"
        # Runtime choice is determined per implementation; mixing languages uses a tester per case.
        report = {"passed": False, "outcome": "unavailable", "case_results": [],
                  "binding": {"source": str(source), "phase": phase.get("id") if isinstance(phase, dict) else phase,
                              "runtime": app_profile, "suite_digest": suite_digest,
                              "suite_inventory": suite_inventory},
                  "suite_status": "pending", "phase_status": "unverified" if required_evidence else "pending",
                  "required_evidence": required_evidence,
                  "external_evidence": [{"id": item["id"], "status": "missing"} for item in required_evidence],
                  "environment": {"engine": "docker", "containers": [], "network": "none"},
                  "app_source_sha256_before": app_digest_before,
                  "app_source_inventory_before": app_hash_before,
                  "cleanup": {"containers_removed": [], "workspace_removed": False}}
        names, primary = [app_name], None
        test_images = {IMAGES["python-web"] if manifest["cases"][cid]["language"] == "python" else IMAGES["node-web"] for cid in manifest["selected_case_ids"]}
        images_to_prepare = {IMAGES[app_profile], *test_images}
        image_ids = {}
        try:
            docker_info = self._budget_call(["info", "--format", "{{.ServerVersion}}"], cancelled, deadline, 10)
            if not docker_info["passed"]:
                raise FactoryError("Docker did not respond; start Docker Desktop", "runtime_unavailable", 503)
            for image in images_to_prepare:
                inspected = self._budget_call(["image", "inspect", image], cancelled, deadline, 15)
                if not inspected["passed"]:
                    progress("Preparing pinned verifier image " + image)
                    pulled = self._budget_call(["pull", image], cancelled, deadline, 600)
                    if not pulled["passed"]:
                        raise FactoryError("could not prepare verifier image", "runtime_unavailable", 503)
                resolved = self._budget_call(["image", "inspect", "--format", "{{.Id}}", image], cancelled, deadline, 15)
                image_id = resolved["output"].strip()
                if not resolved["passed"] or not re.fullmatch(r"sha256:[0-9a-f]{64}", image_id):
                    raise FactoryError("Docker image did not resolve to an immutable id", "runtime_unavailable", 503)
                image_ids[image] = image_id
            report["environment"]["images"] = {name: {"reference": key, "id": name} for key, name in image_ids.items()}
            app_keepalive = ["node", "-e", "setInterval(()=>{},10000)"] if app_profile == "node-web" else ["python3", "-c", "import time; time.sleep(86400)"]
            def base_args(name, image, source_dir, destination):
                args = ["run", "-d", "--name", name, "--label", "atlas.factory=" + self.owner,
                        "--network", "none", "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
                        "--pids-limit=256", "--memory=1g", "--cpus=2", "--user", f"{os.getuid()}:{os.getgid()}",
                        "--tmpfs", "/tmp:rw,nosuid,size=512m,mode=1777", "--env", "HOME=/tmp",
                        "--env", "PYTHONDONTWRITEBYTECODE=1", "--mount", f"type=bind,src={source_dir},dst={destination}" ]
                if destination == "/workspace":
                    args += ["--workdir", destination]
                    args += ["--tmpfs", "/state:rw,nosuid,size=128m,mode=1777"]
                args += [image, *(app_keepalive if name == app_name else (["node", "-e", "setInterval(()=>{},10000)"] if image == IMAGES["node-web"] else ["python3", "-c", "import time; time.sleep(86400)"]))]
                return args
            created = self._budget_call(base_args(app_name, image_ids[IMAGES[app_profile]], app_copy, "/workspace"), cancelled, deadline, 30)
            if not created["passed"]:
                raise FactoryError("could not create restricted application container", "runtime_unavailable", 503)
            report["environment"]["containers"].append(app_name)
            for phase_name in ("install", "build"):
                for argv in runtime.get(phase_name, []):
                    result = self._budget_call(["exec", app_name, *argv], cancelled, deadline)
                    report.setdefault("setup", []).append({"phase": phase_name, **result})
                    if not result["passed"]:
                        report.update(outcome="unavailable" if phase_name == "install" else "blocked",
                                      failure="offline application dependency setup failed" if phase_name == "install" else "application build failed")
                        return report
            testers = {}
            if app_profile == "cli":
                result = self._budget_call(["exec", app_name, *runtime["smoke"]], cancelled, deadline)
                report["startup"] = {"kind": "cli-smoke", **result}
                report["startup"]["status"] = "passed" if result["passed"] else "blocked"
                if not result["passed"]:
                    report.update(outcome="blocked", failure="CLI smoke command failed")
                    return report
                base_url = ""
            else:
                port = runtime["port"]
                if app_profile == "node-web":
                    launcher = ["node", "-e", "const fs=require('fs'),cp=require('child_process');const out=fs.openSync('/state/startup.stdout','a'),err=fs.openSync('/state/startup.stderr','a');const p=cp.spawn(process.argv[1],process.argv.slice(2),{detached:true,stdio:['ignore',out,err]});p.unref();", *runtime["start"]]
                else:
                    launcher = ["python3", "-c", "import subprocess,sys; out=open('/state/startup.stdout','ab',buffering=0); err=open('/state/startup.stderr','ab',buffering=0); p=subprocess.Popen(sys.argv[1:],stdin=subprocess.DEVNULL,stdout=out,stderr=err,start_new_session=True); print(p.pid)", *runtime["start"]]
                start = self._budget_call(["exec", "-d", app_name, *launcher], cancelled, deadline, 15)
                report["startup"] = {"kind": "web-start", **start}
                report["startup"]["status"] = "pending" if start["passed"] else "blocked"
                if not start["passed"]:
                    self._startup_capture(app_name, deadline, report)
                    report.update(outcome="blocked", failure="application start command failed")
                    return report
                # A tester container shares only the app's network namespace. Its image is fixed and code is mounted RO.
                tester_image = IMAGES["python-web"] if lang == "python" else IMAGES["node-web"]
                test_args = ["run", "-d", "--name", test_name, "--label", "atlas.factory=" + self.owner,
                             "--network", "container:" + app_name, "--read-only", "--cap-drop=ALL",
                             "--security-opt=no-new-privileges", "--pids-limit=128", "--memory=512m", "--cpus=1",
                             "--user", f"{os.getuid()}:{os.getgid()}", "--tmpfs", "/tmp:rw,nosuid,size=128m,mode=1777",
                             "--tmpfs", "/state:rw,nosuid,size=128m,mode=1777", "--env", "HOME=/tmp",
                             "--mount", f"type=bind,src={suite_copy},dst=/suite,readonly",
                             "--mount", f"type=bind,src={app_copy},dst=/application,readonly",
                             image_ids[tester_image], *( ["node", "-e", "setInterval(()=>{},10000)"] if tester_image == IMAGES["node-web"] else ["python3", "-c", "import time; time.sleep(86400)"]) ]
                names.append(test_name)
                ready = self._budget_call(test_args, cancelled, deadline, 30)
                if not ready["passed"]:
                    report["startup"]["status"] = "unavailable"
                    raise FactoryError("could not create acceptance runner container", "runtime_unavailable", 503)
                testers[tester_image] = test_name
                report["environment"]["containers"].append(test_name)
                base_url = f"http://127.0.0.1:{port}"
                ready_cmd = (["python3", "-c", "import sys,time,urllib.request; u=sys.argv[1]; end=time.time()+30\nwhile time.time()<end:\n try: urllib.request.urlopen(u,timeout=1).read(1); sys.exit(0)\n except Exception: time.sleep(.2)\nsys.exit(1)", base_url + runtime.get("readiness_path", "/")] if lang == "python" else ["node", "-e", "const u=process.argv[1],end=Date.now()+30000; (async()=>{while(Date.now()<end){try{const r=await fetch(u);if(r.ok)process.exit(0)}catch{} await new Promise(r=>setTimeout(r,200))}process.exit(1)})()", base_url + runtime.get("readiness_path", "/")])
                ready_result = self._budget_call(["exec", test_name, *ready_cmd], cancelled, deadline, 35)
                report["startup"]["readiness"] = ready_result
                report["startup"]["status"] = "passed" if ready_result["passed"] else "blocked"
                if not ready_result["passed"]:
                    self._startup_capture(app_name, deadline, report)
                    report.update(outcome="blocked", failure="web application did not pass HTTP readiness")
                    return report
                self._startup_capture(app_name, deadline, report)
            for case_id in manifest["selected_case_ids"]:
                binding = manifest["cases"][case_id]
                tester_image = IMAGES["python-web"] if binding["language"] == "python" else IMAGES["node-web"]
                if tester_image not in testers:
                    tname = prefix + "-test-" + binding["language"]
                    names.append(tname)
                    network = "none" if app_profile == "cli" else "container:" + app_name
                    keepalive = (["node", "-e", "setInterval(()=>{},10000)"] if binding["language"] == "node" else ["python3", "-c", "import time; time.sleep(86400)"])
                    test_args = ["run", "-d", "--name", tname, "--label", "atlas.factory=" + self.owner,
                                 "--network", network, "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
                                 "--pids-limit=128", "--memory=512m", "--cpus=1", "--user", f"{os.getuid()}:{os.getgid()}",
                                 "--tmpfs", "/tmp:rw,nosuid,size=128m,mode=1777", "--tmpfs", "/state:rw,nosuid,size=128m,mode=1777",
                                 "--env", "HOME=/tmp", "--mount", f"type=bind,src={suite_copy},dst=/suite,readonly",
                                 "--mount", f"type=bind,src={app_copy},dst=/application,readonly",
                                 image_ids[tester_image], *keepalive]
                    cr = self._budget_call(test_args, cancelled, deadline, 30)
                    if not cr["passed"]:
                        raise FactoryError("could not create acceptance runner container", "runtime_unavailable", 503)
                    testers[tester_image] = tname
                    report["environment"]["containers"].append(tname)
                test_name = testers[tester_image]
                argv = (["python3", "/suite/" + binding["implementation"]] if binding["language"] == "python" else ["node", "/suite/" + binding["implementation"]])
                for item in binding["args"]:
                    argv.append(item["literal"] if "literal" in item else {"base_url": base_url, "app_root": "/application", "data_dir": "/state", "case_id": case_id}[item["placeholder"]])
                progress("Acceptance: " + case_id)
                result = self._budget_call(["exec", test_name, *argv], cancelled, deadline)
                stdout = result.get("stdout", result["output"])
                stdout_truncated = bool(result.get("stdout_truncated", False))
                parsed = None if stdout_truncated else _strict_result(stdout, case_id)
                status = "unverified" if parsed is None else parsed["status"]
                assertions_passed = bool(parsed and all(x["passed"] for x in parsed["assertions"]))
                passed = bool(parsed and result["exit_code"] == 0 and status == "passed" and assertions_passed)
                if parsed and (status == "failed" or not assertions_passed):
                    visible_status = "failed"
                    reason = "one or more authored acceptance assertions failed"
                elif parsed and status == "passed" and result["exit_code"] != 0:
                    visible_status = "unverified"
                    reason = "runner exited nonzero despite reporting a pass"
                elif parsed is None:
                    visible_status = "unverified"
                    reason = ("acceptance stdout was truncated by the verifier transport" if stdout_truncated
                              else "runner output was missing or did not match the acceptance result protocol")
                elif status == "unverified":
                    visible_status = "unverified"
                    reason = "authored runner could not verify this case"
                else:
                    visible_status, reason = "passed", None
                report["case_results"].append({"id": case_id, "case_id": case_id, "status": visible_status,
                                         "passed": passed, "command": result["argv"], "exit_code": result["exit_code"],
                                         "output": redact_text(result["output"])[-16000:], "assertions": parsed["assertions"] if parsed else None,
                                         "stderr": redact_text(result.get("stderr", ""))[-8000:],
                                         "reason": reason})
                if not passed:
                    report.update(outcome="blocked" if visible_status == "failed" else "unavailable",
                                  failure=reason, error=reason)
                    return report
            report["suite_status"] = "passed"
            if required_evidence:
                report.update(passed=False, outcome="unverified", phase_status="unverified",
                              code="phase_evidence_missing",
                              error="required independent phase evidence has not been registered")
            else:
                report.update(passed=True, outcome="passed", phase_status="passed")
            return report
        except FactoryError as error:
            primary = error
            if report.get("startup", {}).get("status") == "pending":
                report["startup"]["status"] = "unavailable"
            if report.get("startup", {}).get("kind") == "web-start" and "captured_output" not in report["startup"]:
                self._startup_capture(app_name, deadline, report)
            report.update(outcome="unavailable" if error.code in {"runtime_unavailable", "verification_timeout", "cancelled"} else "blocked",
                          failure=redact_text(str(error)), error_code=error.code)
            raise
        finally:
            try:
                app_hash_after = tree_manifest(app) if app.exists() else None
            except Exception as hash_error:
                app_hash_after = None
                report["cleanup"].setdefault("errors", []).append("could not recheck source inventory: " + redact_text(str(hash_error))[:500])
            report["app_source_inventory_after"] = app_hash_after
            report["app_source_sha256_after"] = hashlib.sha256(json.dumps(app_hash_after, sort_keys=True, separators=(",", ":")).encode()).hexdigest() if app_hash_after is not None else None
            report["app_source_unchanged"] = report["app_source_sha256_after"] == app_digest_before
            if not report["app_source_unchanged"]:
                report.update(passed=False, outcome="blocked", failure="submitted application source changed during verification")
            report["container_logs"] = {}
            for name in reversed(names):
                if self.executable:
                    try:
                        logs = self._call(["logs", "--tail", "100", name], lambda: False, 10)
                        report["container_logs"][name] = redact_text(logs["output"])[-16000:]
                    except Exception as log_error:
                        report["cleanup"].setdefault("errors", []).append("logs " + name + ": " + redact_text(str(log_error))[:500])
                    try:
                        removed = self._call(["rm", "-f", name], lambda: False, 20)
                        if removed["passed"]:
                            report["cleanup"]["containers_removed"].append(name)
                        else:
                            output = removed.get("output", "").lower()
                            if "no such container" in output or "no such object" in output:
                                report["cleanup"].setdefault("containers_absent", []).append(name)
                            else:
                                inspected = self._call(["inspect", name], lambda: False, 10)
                                if inspected["passed"]:
                                    report["cleanup"].setdefault("errors", []).append("container remains after removal attempt: " + name)
                                elif "no such container" in inspected.get("output", "").lower() or "no such object" in inspected.get("output", "").lower():
                                    report["cleanup"].setdefault("containers_absent", []).append(name)
                                else:
                                    report["cleanup"].setdefault("errors", []).append("could not verify container removal: " + name)
                    except Exception as cleanup_error:
                        report["cleanup"].setdefault("errors", []).append(redact_text(str(cleanup_error))[:500])
            shutil.rmtree(work_root, ignore_errors=True)
            report["cleanup"]["workspace_removed"] = not work_root.exists()
            report["cleanup"]["success"] = (len(report["cleanup"]["containers_removed"]) + len(report["cleanup"].get("containers_absent", [])) == len(names)
                                                     and report["cleanup"]["workspace_removed"]
                                                     and not report["cleanup"].get("errors"))
            report["cleanup"]["status"] = "passed" if report["cleanup"]["success"] else "failed"
            if not report["cleanup"]["success"]:
                report.update(passed=False, outcome="unavailable", failure=report.get("failure", "verification cleanup did not complete"))
                report["phase_status"] = "unverified"
            if report.get("suite_status") == "pending":
                if report.get("outcome") == "blocked":
                    report["suite_status"] = "blocked"
                    report["phase_status"] = "blocked"
                else:
                    report["suite_status"] = "unverified"
                    report["phase_status"] = "unverified"
            try:
                atomic_json(evidence / "report.json", report)
            except Exception:
                if primary is None:
                    raise
