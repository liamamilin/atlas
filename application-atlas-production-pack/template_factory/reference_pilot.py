"""Durable, two-leaf product-reference verification inside a paused full plan."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys

from .full_auxiliary import ensure_schema
from .store import FactoryError, digest

PROFILE_VERSION = "product-reference-v1"
PROFILE_SOURCE = "examples/assisted-trials/product_reference_profile.py"
SCHEMA = "atlas.reference-pilot.v1"


class ReferencePilotService:
    """Register and control a tiny first-pass pilot without a new budget grant."""

    def __init__(self, store, campaign_id="atlas-v1-first-production-2026-10-19", clock=None):
        import time
        self.store, self.campaign_id = store, campaign_id
        self.clock = clock or time.time
        with store.connect(True) as con:
            ensure_schema(con)

    def register(self, request):
        self._validate_shape(request)
        with self.store.connect(True) as con:
            plan = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (request["plan_id"], self.campaign_id),
            ).fetchone()
            if not plan:
                raise FactoryError("original full plan is not registered", "full_plan_binding", 409)
            if digest(json.loads(plan["request_json"])) != plan["request_digest"]:
                raise FactoryError("original full authorization changed", "full_plan_integrity", 409)
            if plan["status"] != "paused" or plan["model"] != "open-design/deepseek-v4.1-flash":
                raise FactoryError("pilot requires the paused Open Design full plan", "full_plan_paused", 409)
            if plan["deadline"] != 1795181744.123177 or plan["max_calls"] != 7200:
                raise FactoryError("original full-plan window or allowance changed", "full_plan_integrity", 409)
            active = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                (self.campaign_id, plan["phase"]),
            ).fetchone()[0]
            if active:
                raise FactoryError("drain original phase reservations before pilot registration", "full_plan_paused", 409)
            existing = con.execute(
                "SELECT * FROM auxiliary_reference_pilot WHERE id=? OR plan_id=?",
                (request["pilot_id"], request["plan_id"]),
            ).fetchone()
            if existing:
                if existing["request_digest"] != digest(request):
                    raise FactoryError("pilot ID/idempotency key already bound", "reference_pilot_binding", 409)
                return self._receipt(existing)
            original = json.loads(plan["request_json"])
            scope_path = (self.store.pack.parent / original["scope"]["path"]).resolve()
            if (not scope_path.is_relative_to(self.store.pack.parent.resolve())
                    or hashlib.sha256(scope_path.read_bytes()).hexdigest() != original["scope"]["sha256"]):
                raise FactoryError("original full scope integrity differs", "full_plan_integrity", 409)
            scope = json.loads(scope_path.read_text())
            scope_items = {x["leaf"]: x for x in scope["items"]}
            for item in request["leaves"]:
                leaf = item["leaf"]
                frozen = con.execute(
                    "SELECT state,body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                    (plan["id"], leaf),
                ).fetchone()
                if not frozen or frozen["state"] != "reused" or leaf not in scope_items:
                    raise FactoryError("pilot leaves must be frozen reused leaves", "reference_pilot_scope", 409)
                body = json.loads(frozen["body"])
                frozen_sha = body.get("leaf_sha256")
                if item["frozen_leaf_sha256"] != frozen_sha or scope_items[leaf].get("leaf_sha256") != frozen_sha:
                    raise FactoryError("pilot frozen leaf hash differs", "reference_pilot_scope", 409)
                self._verify_leaf_input(item, leaf, con=con)
                used = con.execute(
                    "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity=? AND status!='not_started'",
                    (self.campaign_id, plan["phase"], plan["id"] + ":" + leaf),
                ).fetchone()[0]
                if used:
                    raise FactoryError("pilot leaf already has charged calls", "reference_pilot_scope", 409)
            self._verify_source_ci(con, plan, request)
            self._verify_user_request(request)
            phase = plan["phase"]
            now = self.clock()
            pause_anchor = con.execute(
                "SELECT COALESCE(MAX(id),0) FROM auxiliary_full_event WHERE plan_id=?",
                (plan["id"],),
            ).fetchone()[0]
            con.execute(
                "INSERT INTO auxiliary_reference_pilot(id,plan_id,campaign_id,phase,request_json,request_digest,max_calls,status,created,updated,pause_anchor) VALUES(?,?,?,?,?,?,6,'active',?,?,?)",
                (request["pilot_id"], plan["id"], self.campaign_id, phase,
                 json.dumps(request, ensure_ascii=False, sort_keys=True), digest(request), now, now, pause_anchor),
            )
            con.execute(
                "INSERT INTO auxiliary_reference_pilot_event(pilot_id,kind,body,created) VALUES(?,'registered',?,?)",
                (request["pilot_id"], json.dumps({"request": request, "request_digest": digest(request)}, ensure_ascii=False), now),
            )
            row = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=?", (request["pilot_id"],)).fetchone()
            return self._receipt(row)

    def get(self, pilot_id):
        with self.store.connect() as con:
            row = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=? AND campaign_id=?",
                              (pilot_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("reference pilot not found", "not_found", 404)
            calls = [dict(x) for x in con.execute(
                "SELECT identity,stage,status,job_id,created,started,finished FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity LIKE ? ORDER BY created",
                (self.campaign_id, row["phase"], row["plan_id"] + ":%"),
            ) if any(x["identity"] == row["plan_id"] + ":" + leaf["leaf"] for leaf in json.loads(row["request_json"])["leaves"])]
            return {**self._receipt(row), "calls": calls,
                    "remaining_calls": row["max_calls"] - sum(c["status"] != "not_started" for c in calls)}

    def action(self, pilot_id, action, reason="operator"):
        if action not in {"pause", "complete"}:
            raise FactoryError("unknown pilot action", "reference_pilot_binding", 409)
        status = {"pause": "paused", "complete": "completed"}[action]
        with self.store.connect(True) as con:
            row = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=? AND campaign_id=?",
                              (pilot_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("reference pilot not found", "not_found", 404)
            if row["status"] == "active":
                con.execute("UPDATE auxiliary_reference_pilot SET status=?,updated=? WHERE id=?",
                            (status, self.clock(), pilot_id))
                con.execute("INSERT INTO auxiliary_reference_pilot_event(pilot_id,kind,body,created) VALUES(?,?,?,?)",
                            (pilot_id, action, json.dumps({"reason": reason}), self.clock()))
        return self.get(pilot_id)

    @staticmethod
    def _receipt(row):
        req = json.loads(row["request_json"])
        return {"pilot_id": row["id"], "plan_id": row["plan_id"], "phase": row["phase"],
                "status": row["status"], "request_digest": row["request_digest"],
                "leaves": [x["leaf"] for x in req["leaves"]], "max_calls": row["max_calls"],
                "created": row["created"]}

    def _validate_shape(self, r):
        if not isinstance(r, dict) or r.get("schema") != SCHEMA or r.get("campaign_id") != self.campaign_id:
            raise FactoryError("invalid reference pilot schema/campaign", "reference_pilot_binding", 409)
        if r.get("profile_version") != PROFILE_VERSION or not re.fullmatch(r"[0-9a-f]{64}", str(r.get("prompt_digest", ""))):
            raise FactoryError("reference profile identity differs", "reference_pilot_binding", 409)
        profile_path = self.store.pack.parent / PROFILE_SOURCE
        spec = importlib.util.spec_from_file_location("_atlas_reference_profile", profile_path)
        module = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(profile_path.parent))
        try:
            spec.loader.exec_module(module)
        finally:
            sys.path.pop(0)
        if r["profile_version"] != module.VERSION or r["prompt_digest"] != module.PROMPT_DIGEST:
            raise FactoryError("pilot profile/prompt digest differs from current source", "reference_pilot_binding", 409)
        if (not r.get("plan_id") or not r.get("pilot_id") or not r.get("idempotency_key")
                or not re.fullmatch(r"[0-9a-f]{64}", str(r.get("production_source_sha256", "")))):
            raise FactoryError("pilot plan/id/source binding required", "reference_pilot_binding", 409)
        leaves = r.get("leaves")
        if not isinstance(leaves, list) or not 1 <= len(leaves) <= 2 or len({x.get("leaf") for x in leaves if isinstance(x, dict)}) != len(leaves):
            raise FactoryError("pilot must bind exactly one or two unique leaves", "reference_pilot_scope", 409)
        for x in leaves:
            if (not isinstance(x, dict) or not x.get("leaf")
                    or not re.fullmatch(r"[0-9a-f]{64}", str(x.get("frozen_leaf_sha256", "")))
                    or not re.fullmatch(r"[0-9a-f]{64}", str(x.get("input_sha256", "")))
                    or not re.fullmatch(r"[0-9a-f]{64}", str(x.get("snapshot_sha256", "")))
                    or not x.get("input_path") or not x.get("snapshot_path")):
                raise FactoryError("invalid leaf input digest", "reference_pilot_scope", 409)

    def _verify_leaf_input(self, item, leaf, con=None):
        root = self.store.pack.parent.resolve()
        paths = []
        for key in ("input_path", "snapshot_path"):
            raw = root / item[key]
            path = raw.resolve()
            if raw.is_symlink() or not path.is_relative_to(root) or not path.is_file():
                raise FactoryError("product-reference input path is unsafe or missing", "reference_pilot_integrity", 409)
            paths.append(path)
        input_path, snapshot_path = paths
        if hashlib.sha256(input_path.read_bytes()).hexdigest() != item["input_sha256"]:
            raise FactoryError("product-reference input bytes differ", "reference_pilot_integrity", 409)
        if hashlib.sha256(snapshot_path.read_bytes()).hexdigest() != item["snapshot_sha256"]:
            raise FactoryError("product-reference snapshot bytes differ", "reference_pilot_integrity", 409)
        try:
            inputs, snapshot = json.loads(input_path.read_text()), json.loads(snapshot_path.read_text())
            from examples.assisted_trials import product_reference_profile as profile
        except (ValueError, ImportError):
            # The production tree uses a hyphenated directory; import from the bound source file.
            spec = importlib.util.spec_from_file_location("_atlas_reference_profile", root / PROFILE_SOURCE)
            profile = importlib.util.module_from_spec(spec)
            sys.path.insert(0, str((root / PROFILE_SOURCE).parent))
            try:
                spec.loader.exec_module(profile)
            finally:
                sys.path.pop(0)
            inputs, snapshot = json.loads(input_path.read_text()), json.loads(snapshot_path.read_text())
        input_leaf = inputs.get("leaf")
        input_leaf_id = input_leaf if isinstance(input_leaf, str) else (
            input_leaf.get("id") or input_leaf.get("type_id") if isinstance(input_leaf, dict) else None
        )
        if input_leaf_id != leaf or inputs.get("profile_version") != PROFILE_VERSION:
            raise FactoryError("product-reference inputs bind another leaf/profile", "reference_pilot_scope", 409)
        try:
            profile._validate_inputs(inputs, snapshot)
        except (ValueError, KeyError, TypeError) as error:
            raise FactoryError("product-reference inputs/snapshot are invalid", "reference_pilot_integrity", 409) from error
        if con is not None:
            for ref in inputs["case_refs"]:
                case = con.execute(
                    "SELECT digest FROM case_revision WHERE case_id=? AND revision=?",
                    (ref["case_id"], ref["revision"]),
                ).fetchone()
                if not case or case["digest"] != ref["digest"]:
                    raise FactoryError("product-reference case reference differs from the current case library", "reference_pilot_integrity", 409)

    def verify_call(self, con, pilot, request, plan):
        """Revalidate all request, source, and frozen-scope bindings at each reservation."""
        if digest(request) != pilot["request_digest"]:
            raise FactoryError("stored reference pilot changed", "full_plan_integrity", 409)
        self._validate_shape(request)
        root = self.store.pack.parent.resolve()
        original = json.loads(plan["request_json"])
        for key in ("authorization", "scope"):
            ref = original[key]
            path = (root / ref["path"]).resolve()
            if (not path.is_relative_to(root) or not path.is_file()
                    or hashlib.sha256(path.read_bytes()).hexdigest() != ref["sha256"]):
                raise FactoryError("original full-plan source bytes changed", "full_plan_integrity", 409)
        scope = json.loads((root / original["scope"]["path"]).read_text())
        if scope.get("full_plan_id") != plan["id"]:
            raise FactoryError("original full scope identity changed", "full_plan_integrity", 409)
        scope_items = {row["leaf"]: row for row in scope["items"]}
        for item in request["leaves"]:
            frozen = con.execute(
                "SELECT state,body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                (plan["id"], item["leaf"]),
            ).fetchone()
            body = json.loads(frozen["body"]) if frozen else {}
            leaf_sha = body.get("leaf_sha256")
            if (not frozen or frozen["state"] != "reused"
                    or leaf_sha != item["frozen_leaf_sha256"]
                    or scope_items.get(item["leaf"], {}).get("leaf_sha256") != leaf_sha):
                raise FactoryError("frozen reused leaf changed after pilot registration", "reference_pilot_scope", 409)
            self._verify_leaf_input(item, item["leaf"], con=con)
        self._verify_source_ci(con, plan, request)
        self._verify_user_request(request)

    def _verify_source_ci(self, con, plan, request):
        proof = request.get("source_ci", {})
        event = con.execute("SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id DESC LIMIT 1", (plan["id"],)).fetchone()
        if not event or not isinstance(proof, dict):
            raise FactoryError("matching registered host CI evidence required", "reference_pilot_ci", 409)
        value = json.loads(event[0])
        host = value["request"]
        if digest(host) != value.get("request_digest"):
            raise FactoryError("registered host revision record changed", "full_plan_integrity", 409)
        expected = request["production_source_sha256"]
        profile_path = self.store.pack.parent / PROFILE_SOURCE
        if not profile_path.is_file() or hashlib.sha256(profile_path.read_bytes()).hexdigest() != expected:
            raise FactoryError("product-reference source bytes differ", "reference_pilot_integrity", 409)
        ci_ref = host.get("ci_proof", {})
        root = self.store.pack.parent.resolve()
        ci_path = (root / ci_ref.get("path", "")).resolve()
        if (not ci_path.is_relative_to(root) or not ci_path.is_file()
                or ci_path.is_symlink()):
            raise FactoryError("registered host CI proof is unavailable", "reference_pilot_ci", 409)
        ci = json.loads(ci_path.read_text())
        source_hashes = host.get("new_host_sha256", {})
        for rel, sha in source_hashes.items():
            source_path = (root / rel).resolve()
            if (not source_path.is_relative_to(root) or not source_path.is_file()
                    or hashlib.sha256(source_path.read_bytes()).hexdigest() != sha):
                raise FactoryError("registered host source bytes changed", "reference_pilot_integrity", 409)
        if (digest(host) != proof.get("host_revision_digest") or host.get("code_sha") != proof.get("code_sha")
                or host.get("new_host_sha256", {}).get(PROFILE_SOURCE) != expected
                or hashlib.sha256(ci_path.read_bytes()).hexdigest() != ci_ref.get("sha256")
                or ci.get("sha") != host.get("code_sha") or ci.get("status") != "completed"
                or ci.get("conclusion") != "success"):
            raise FactoryError("host revision does not bind product-reference source", "reference_pilot_ci", 409)

    def _verify_user_request(self, request):
        ref = request.get("user_request", {})
        root = self.store.pack.parent.resolve()
        raw_path = root / ref.get("path", "")
        path = raw_path.resolve()
        if (raw_path.is_symlink() or not path.is_relative_to(root) or not path.is_file()
                or hashlib.sha256(path.read_bytes()).hexdigest() != ref.get("sha256")):
            raise FactoryError("saved user request evidence differs", "reference_pilot_integrity", 409)

