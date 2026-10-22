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
ALIGNMENT_SCHEMA = "atlas.reference-pilot-host-alignment.v1"
KIND_ALIASES = {"readme": "documentation", "doc": "documentation", "license": "documentation", "source": "code_observation"}
OBSERVATION_PREFIX = "source/upstream/"


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
            alignment = self._latest_alignment(con, row)
            return {**self._receipt(row), "calls": calls,
                    "remaining_calls": row["max_calls"] - sum(c["status"] != "not_started" for c in calls),
                    "host_alignment_digest": alignment.get("alignment_digest") if alignment else None,
                    "effective_profile_source_sha256": alignment.get("new_profile_source_sha256") if alignment else json.loads(row["request_json"]).get("production_source_sha256")}

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

    def align_host(self, pilot_id, body):
        """Append one tested host-output normalization; retain the original request and calls."""
        if (not isinstance(body, dict) or body.get("schema") != ALIGNMENT_SCHEMA
                or body.get("pilot_id") != pilot_id or not body.get("idempotency_key")):
            raise FactoryError("invalid reference pilot alignment request", "reference_pilot_binding", 409)
        with self.store.connect(True) as con:
            pilot = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=? AND campaign_id=?",
                                (pilot_id, self.campaign_id)).fetchone()
            if not pilot:
                raise FactoryError("reference pilot not found", "not_found", 404)
            prior = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='host_alignment' ORDER BY id",
                                (pilot_id,)).fetchall()
            for event in prior:
                saved = json.loads(event[0])
                alignment = saved["alignment"]
                if alignment.get("idempotency_key") == body["idempotency_key"]:
                    if digest(alignment) != saved.get("alignment_digest") or alignment != body:
                        raise FactoryError("alignment idempotency key conflicts", "reference_pilot_binding", 409)
                    return self._alignment_receipt(alignment, saved["alignment_digest"])
            if prior:
                raise FactoryError("one host alignment is allowed for this pilot", "reference_pilot_binding", 409)
            request = json.loads(pilot["request_json"])
            plan = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                               (pilot["plan_id"], self.campaign_id)).fetchone()
            if not plan or plan["status"] != "paused" or pilot["status"] not in {"active", "paused", "completed"}:
                raise FactoryError("alignment requires the same paused full plan", "full_plan_paused", 409)
            if digest(json.loads(plan["request_json"])) != plan["request_digest"]:
                raise FactoryError("original full authorization changed", "full_plan_integrity", 409)
            if (body.get("prior_request_digest") != pilot["request_digest"]
                    or body.get("profile_version") != request["profile_version"]
                    or body.get("prompt_digest") != request["prompt_digest"]
                    or body.get("previous_profile_source_sha256") != request["production_source_sha256"]
                    or body.get("inputs_digest") != self._inputs_digest(request)):
                raise FactoryError("alignment changed pilot identity, inputs, or prompts", "reference_pilot_binding", 409)
            if (plan["model"] != "open-design/deepseek-v4.1-flash"
                    or plan["deadline"] != 1795181744.123177 or plan["max_calls"] != 7200):
                raise FactoryError("alignment changed the original full-plan window or model", "full_plan_integrity", 409)
            controls = con.execute("SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='control' AND id>?",
                                   (plan["id"], pilot["pause_anchor"])).fetchall()
            if any(json.loads(x[0]).get("action") == "pause" for x in controls):
                raise FactoryError("later full-plan pause revoked pilot alignment", "full_plan_paused", 409)
            calls = [dict(x) for x in con.execute(
                "SELECT identity,stage,status,kind FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started' AND stage LIKE ?",
                (self.campaign_id, pilot["phase"], "%/" + pilot_id),
            )]
            selected = {pilot["plan_id"] + ":" + x["leaf"] for x in request["leaves"]}
            calls = [x for x in calls if x["identity"] in selected]
            if (not calls or any(x["stage"] != "reference/research/" + pilot_id or x["status"] != "completed"
                                 or x["kind"] != "research" for x in calls)):
                raise FactoryError("alignment requires terminal research-only pilot calls", "reference_pilot_paused", 409)
            self._verify_original_host_receipt(con, plan, request)
            outcomes = self._validate_alignment_evidence(con, request, body, calls, verify_calls=True)
            host = self._verify_alignment_host(con, plan, body)
            now = self.clock()
            alignment = dict(body)
            envelope = {"alignment": alignment, "alignment_digest": digest(alignment),
                        "prior_request_digest": pilot["request_digest"],
                        "old_profile_source_sha256": request["production_source_sha256"],
                        "new_profile_source_sha256": body["new_profile_source_sha256"],
                        "code_sha": host["code_sha"], "outcomes": outcomes,
                        "kind_aliases": KIND_ALIASES, "path_prefix": OBSERVATION_PREFIX}
            con.execute("INSERT INTO auxiliary_reference_pilot_event(pilot_id,kind,body,created) VALUES(?,'host_alignment',?,?)",
                        (pilot_id, json.dumps(envelope, ensure_ascii=False, sort_keys=True), now))
            con.execute("UPDATE auxiliary_reference_pilot SET status='active',updated=? WHERE id=?",
                        (now, pilot_id))
            con.execute("INSERT INTO auxiliary_reference_pilot_event(pilot_id,kind,body,created) VALUES(?,'alignment_resume',?,?)",
                        (pilot_id, json.dumps({"reason": "tested host protocol alignment", "calls_reused": True}), now))
            return self._alignment_receipt(alignment, envelope["alignment_digest"])

    @staticmethod
    def _alignment_receipt(alignment, alignment_digest):
        return {"pilot_id": alignment["pilot_id"], "alignment_digest": alignment_digest,
                "status": "active", "code_sha": alignment["code_sha"],
                "new_profile_source_sha256": alignment["new_profile_source_sha256"]}

    @staticmethod
    def _inputs_digest(request):
        return digest([{"leaf": item["leaf"], "input_sha256": item["input_sha256"],
                        "snapshot_sha256": item["snapshot_sha256"]} for item in request["leaves"]])

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
        self._verify_user_request(request)
        alignment = self._latest_alignment(con, {"id": request["pilot_id"], "plan_id": plan["id"]}, plan=plan)
        if alignment:
            self._verify_alignment_record(con, request, plan, alignment)
        else:
            self._verify_source_ci(con, plan, request)

    def _latest_alignment(self, con, pilot, plan=None):
        events = con.execute(
            "SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='host_alignment' ORDER BY id",
            (pilot["id"],),
        ).fetchall()
        if not events:
            return None
        if len(events) != 1:
            raise FactoryError("reference pilot has an invalid alignment chain", "full_plan_integrity", 409)
        envelope = json.loads(events[0][0])
        alignment = envelope.get("alignment", {})
        if digest(alignment) != envelope.get("alignment_digest"):
            raise FactoryError("reference pilot alignment record changed", "full_plan_integrity", 409)
        if plan is None:
            plan = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=?", (pilot["plan_id"],)).fetchone()
        host = self._verify_alignment_host(con, plan, alignment)
        if (envelope.get("new_profile_source_sha256") != alignment.get("new_profile_source_sha256")
                or envelope.get("code_sha") != host["code_sha"]
                or envelope.get("prior_request_digest") != alignment.get("prior_request_digest")):
            raise FactoryError("reference pilot alignment receipt changed", "full_plan_integrity", 409)
        registration = con.execute("SELECT request_json FROM auxiliary_reference_pilot WHERE id=?", (pilot["id"],)).fetchone()
        self._verify_alignment_record(con, json.loads(registration["request_json"]), plan,
                                      {**envelope, "alignment": alignment})
        return {**envelope, "alignment": alignment}

    def _verify_alignment_record(self, con, request, plan, envelope):
        alignment = envelope["alignment"]
        if (alignment.get("prior_request_digest") != digest(request)
                or alignment.get("profile_version") != request["profile_version"]
                or alignment.get("prompt_digest") != request["prompt_digest"]
                or alignment.get("previous_profile_source_sha256") != request["production_source_sha256"]
                or alignment.get("inputs_digest") != self._inputs_digest(request)):
            raise FactoryError("reference pilot alignment lineage differs", "full_plan_integrity", 409)
        self._validate_alignment_evidence(con, request, alignment, None, verify_calls=False)

    def _verify_alignment_host(self, con, plan, alignment):
        events = con.execute(
            "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id",
            (plan["id"],),
        ).fetchall()
        matched = None
        for event in events:
            value = json.loads(event[0])
            host = value.get("request", {})
            if digest(host) == alignment.get("host_revision_digest"):
                if value.get("request_digest") != digest(host):
                    raise FactoryError("alignment host revision record changed", "full_plan_integrity", 409)
                matched = host
        if not events or digest(json.loads(events[-1][0])["request"]) != alignment.get("host_revision_digest"):
            raise FactoryError("alignment does not bind the latest host revision", "reference_pilot_ci", 409)
        if not matched or matched.get("code_sha") != alignment.get("code_sha"):
            raise FactoryError("alignment host revision identity differs", "reference_pilot_ci", 409)
        self._verify_host_bytes(matched, alignment.get("new_profile_source_sha256"))
        return matched

    def _verify_original_host_receipt(self, con, plan, request):
        """Keep the initial source/CI receipt verifiable after a newer host revision is registered."""
        proof = request.get("source_ci", {})
        rows = con.execute(
            "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id",
            (plan["id"],),
        ).fetchall()
        for row in rows:
            event = json.loads(row[0])
            host = event.get("request", {})
            if (digest(host) == proof.get("host_revision_digest")
                    and event.get("request_digest") == digest(host)
                    and host.get("code_sha") == proof.get("code_sha")
                    and host.get("new_host_sha256", {}).get(PROFILE_SOURCE) == request.get("production_source_sha256")):
                ci_ref = host.get("ci_proof", {})
                ci_path = self._evidence_path(ci_ref, "original CI proof")
                ci = json.loads(ci_path.read_text())
                if ci.get("sha") == host.get("code_sha") and ci.get("status") == "completed" and ci.get("conclusion") == "success":
                    return
        raise FactoryError("original registered host/CI receipt is unavailable", "reference_pilot_ci", 409)

    def _verify_host_bytes(self, host, expected_profile_sha):
        root = self.store.pack.parent.resolve()
        profile_path = root / PROFILE_SOURCE
        if (host.get("new_host_sha256", {}).get(PROFILE_SOURCE) != expected_profile_sha
                or not profile_path.is_file()
                or hashlib.sha256(profile_path.read_bytes()).hexdigest() != expected_profile_sha):
            raise FactoryError("aligned profile source bytes differ", "reference_pilot_integrity", 409)
        for rel, sha in host.get("new_host_sha256", {}).items():
            source_path = (root / rel).resolve()
            if (not source_path.is_relative_to(root) or not source_path.is_file()
                    or hashlib.sha256(source_path.read_bytes()).hexdigest() != sha):
                raise FactoryError("registered host source bytes changed", "reference_pilot_integrity", 409)
        ci_ref = host.get("ci_proof", {})
        ci_path = (root / ci_ref.get("path", "")).resolve()
        if not ci_path.is_relative_to(root) or not ci_path.is_file():
            raise FactoryError("registered host CI proof is unavailable", "reference_pilot_ci", 409)
        ci = json.loads(ci_path.read_text())
        if (hashlib.sha256(ci_path.read_bytes()).hexdigest() != ci_ref.get("sha256")
                or ci.get("sha") != host.get("code_sha") or ci.get("status") != "completed"
                or ci.get("conclusion") != "success"):
            raise FactoryError("exact successful host CI proof missing", "reference_pilot_ci", 409)

    def _validate_alignment_evidence(self, con, request, alignment, calls=None, verify_calls=True):
        if verify_calls:
            pilot_id = request["pilot_id"]
            pilot = con.execute("SELECT phase FROM auxiliary_reference_pilot WHERE id=?", (pilot_id,)).fetchone()
            if not pilot:
                raise FactoryError("reference pilot disappeared", "full_plan_integrity", 409)
            selected = {request["plan_id"] + ":" + x["leaf"] for x in request["leaves"]}
            calls = [dict(x) for x in con.execute(
                "SELECT identity,stage,status,kind FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started' AND stage LIKE ?",
                (self.campaign_id, pilot["phase"], "%/" + pilot_id),
            ) if x["identity"] in selected]
            if (not calls or any(x["stage"] != "reference/research/" + pilot_id
                                 or x["status"] != "completed" or x["kind"] != "research" for x in calls)):
                raise FactoryError("alignment requires terminal research-only pilot calls", "reference_pilot_paused", 409)
        adaptation_ref = alignment.get("adaptation", {})
        adaptation_path = self._evidence_path(adaptation_ref, "adaptation")
        adaptation = json.loads(adaptation_path.read_text())
        if (adaptation.get("schema") != "atlas.reference-pilot-research-adaptation.v1"
                or adaptation.get("pilot_id") != request["pilot_id"]
                or adaptation.get("kind_aliases") != KIND_ALIASES
                or adaptation.get("path_prefix") != OBSERVATION_PREFIX):
            raise FactoryError("research adaptation does not match the fixed normalization", "reference_pilot_integrity", 409)
        raw_rows, raw_outcomes = adaptation.get("leaves", []), alignment.get("outcomes", [])
        if not isinstance(raw_rows, list) or not isinstance(raw_outcomes, list):
            raise FactoryError("alignment evidence lists are malformed", "reference_pilot_integrity", 409)
        rows = {x.get("leaf"): x for x in raw_rows if isinstance(x, dict)}
        outcomes = {x.get("leaf"): x for x in raw_outcomes if isinstance(x, dict)}
        if len(rows) != len(raw_rows) or len(outcomes) != len(raw_outcomes):
            raise FactoryError("alignment evidence contains duplicate or malformed leaves", "reference_pilot_integrity", 409)
        if verify_calls:
            called_leaves = {x["identity"].split(":", 1)[1] for x in (calls or [])}
        else:
            called_leaves = {x["leaf"] for x in request["leaves"]}
        if set(rows) != called_leaves or set(outcomes) != called_leaves:
            raise FactoryError("alignment evidence does not exactly cover completed research calls", "reference_pilot_integrity", 409)
        registered = {x["leaf"]: x for x in request["leaves"]}
        for leaf in called_leaves:
            row, outcome = rows[leaf], outcomes[leaf]
            if not isinstance(row.get("canonical_observations"), list):
                raise FactoryError("canonical observation list missing", "reference_pilot_integrity", 409)
            raw_path = self._evidence_path({"path": row.get("raw_result_path"),
                                            "sha256": row.get("raw_result_sha256")}, "raw result")
            raw = json.loads(raw_path.read_text())
            raw_observations = raw.get("observed_upstream")
            canonical = row["canonical_observations"]
            if not isinstance(raw_observations, list) or len(raw_observations) != len(canonical):
                raise FactoryError("raw and canonical observations differ in length", "reference_pilot_integrity", 409)
            expected = []
            for source, normalized in zip(raw_observations, canonical):
                if (not isinstance(source, list) or len(source) != 5
                        or not isinstance(normalized, list) or len(normalized) != 5):
                    raise FactoryError("research observation tuple malformed", "reference_pilot_integrity", 409)
                kind, path, start, end, text = source
                canonical_kind = KIND_ALIASES.get(kind.lower(), kind.lower()) if isinstance(kind, str) else None
                canonical_path = path[len(OBSERVATION_PREFIX):] if isinstance(path, str) and path.startswith(OBSERVATION_PREFIX) else path
                allowed_kinds = set(KIND_ALIASES.values())
                if (not isinstance(kind, str) or canonical_kind not in allowed_kinds
                        or not isinstance(path, str) or not isinstance(canonical_path, str)
                        or not canonical_path or ".." in canonical_path.split("/")
                        or normalized != [canonical_kind, canonical_path, start, end, text]):
                    raise FactoryError("host adaptation changed observation data beyond the fixed aliases/prefix", "reference_pilot_integrity", 409)
                expected.append(normalized)
            if digest({**raw, "observed_upstream": expected}) != row.get("canonical_result_digest"):
                raise FactoryError("canonical research result digest differs", "reference_pilot_integrity", 409)
            leaf_request = registered[leaf]
            inputs = json.loads(self._bound_file(leaf_request["input_path"], leaf_request["input_sha256"]).read_text())
            snapshot = json.loads(self._bound_file(leaf_request["snapshot_path"], leaf_request["snapshot_sha256"]).read_text())
            profile = self._profile_module()
            try:
                profile._observations(expected, snapshot, inputs["trusted_source_ids"])
            except (ValueError, KeyError, TypeError) as error:
                raise FactoryError("canonical observations do not match pinned source ranges", "reference_pilot_integrity", 409) from error
            outcome_path = self._evidence_path(outcome, "initial outcome")
            if outcome_path.name != "OUTCOME.initial-protocol.json":
                raise FactoryError("initial protocol outcome must remain separately preserved", "reference_pilot_integrity", 409)
            result = json.loads(outcome_path.read_text())
            if (result.get("leaf") != leaf or result.get("status") != "failed"
                    or result.get("completed_stages") != ["research"]
                    or result.get("error_type") != "ValueError"
                    or result.get("reason") != "observation is not bound to a trusted upstream source"
                    or result.get("publication_status") != "not_published"
                    or result.get("application_runtime_status") != "not_run"):
                raise FactoryError("initial research outcome is not the known host protocol failure", "reference_pilot_integrity", 409)
        return [{"leaf": leaf, "path": outcomes[leaf]["path"], "sha256": outcomes[leaf]["sha256"]}
                for leaf in sorted(called_leaves)]

    def _bound_file(self, relative, sha256):
        ref = {"path": relative, "sha256": sha256}
        path = self._evidence_path(ref, "bound file")
        if hashlib.sha256(path.read_bytes()).hexdigest() != sha256:
            raise FactoryError("bound evidence bytes changed", "reference_pilot_integrity", 409)
        return path

    def _evidence_path(self, ref, name):
        if (not isinstance(ref, dict) or not isinstance(ref.get("path"), str)
                or not re.fullmatch(r"[0-9a-f]{64}", str(ref.get("sha256", "")))):
            raise FactoryError(f"{name} path/digest binding is required", "reference_pilot_integrity", 409)
        root = self.store.pack.parent.resolve()
        raw = root / ref["path"]
        path = raw.resolve()
        if raw.is_symlink() or not path.is_relative_to(root) or not path.is_file():
            raise FactoryError(f"{name} path is unsafe or missing", "reference_pilot_integrity", 409)
        if hashlib.sha256(path.read_bytes()).hexdigest() != ref["sha256"]:
            raise FactoryError(f"{name} bytes differ", "reference_pilot_integrity", 409)
        return path

    def _profile_module(self):
        profile_path = self.store.pack.parent / PROFILE_SOURCE
        spec = importlib.util.spec_from_file_location("_atlas_reference_profile", profile_path)
        module = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(profile_path.parent))
        try:
            spec.loader.exec_module(module)
        finally:
            sys.path.pop(0)
        return module

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

