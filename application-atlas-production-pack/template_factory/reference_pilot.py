"""Durable, two-leaf product-reference verification inside a paused full plan."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
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
            revisions = []
            for event in con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id", (pilot_id,)):
                envelope = json.loads(event[0])
                if digest(envelope.get("request")) != envelope.get("request_digest"):
                    raise FactoryError("reference continuation record changed", "full_plan_integrity", 409)
                revisions.append({"request": envelope["request"], "request_digest": envelope["request_digest"],
                                  "effective_max_calls": envelope["effective_max_calls"]})
            if revisions:
                alignment = self._historical_alignment(con, row)
            else:
                alignment = self._latest_alignment(con, row)
            effective_max = revisions[-1]["effective_max_calls"] if revisions else row["max_calls"]
            return {**self._receipt(row), "calls": calls, "revisions": revisions,
                    "effective_max_calls": effective_max,
                    "original_max_calls": row["max_calls"],
                    "remaining_calls": effective_max - sum(c["status"] != "not_started" for c in calls),
                    "host_alignment_digest": alignment.get("alignment_digest") if alignment else None,
                    "effective_profile_source_sha256": revisions[-1]["request"].get("production_source_sha256") if revisions else (alignment.get("new_profile_source_sha256") if alignment else json.loads(row["request_json"]).get("production_source_sha256"))}

    def get_revision(self, pilot_id, leaf, revision_id):
        """Return one immutable revision request and its durable stage reservations."""
        with self.store.connect() as con:
            pilot = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=? AND campaign_id=?",
                                (pilot_id, self.campaign_id)).fetchone()
            if not pilot:
                raise FactoryError("reference pilot not found", "not_found", 404)
            matches = []
            for event in con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id",
                                     (pilot_id,)):
                envelope = json.loads(event[0])
                request = envelope.get("request", {})
                if digest(request) != envelope.get("request_digest"):
                    raise FactoryError("reference continuation record changed", "full_plan_integrity", 409)
                if request.get("leaf") == leaf and request.get("revision_id") == revision_id:
                    matches.append(envelope)
            if len(matches) != 1:
                raise FactoryError("reference revision not found or ambiguous", "not_found", 404)
            request = matches[0]["request"]
            prior = self._prior_revision(con, pilot, leaf, revision_id)
            self._verify_revision_parents(request, leaf, con=con, pilot=pilot,
                                          original_request=json.loads(pilot["request_json"]), prior=prior)
            calls = [dict(row) for row in con.execute(
                "SELECT identity,stage,status,job_id,created,started,finished FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity=? AND stage IN (?,?) ORDER BY created",
                (self.campaign_id, pilot["phase"], pilot["plan_id"] + ":" + leaf,
                 "reference/author/" + pilot_id + "/" + revision_id,
                 "reference/review/" + pilot_id + "/" + revision_id))]
            return {"pilot_id": pilot_id, "leaf": leaf, "revision_id": revision_id,
                    "request": request, "request_digest": matches[0]["request_digest"],
                    "effective_max_calls": matches[0]["effective_max_calls"], "calls": calls}

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

    def begin_revision(self, pilot_id, body):
        """Append a bounded author/review continuation to the existing pilot."""
        if (not isinstance(body, dict) or body.get("schema") != "atlas.reference-pilot-revision.v1"
                or body.get("pilot_id") != pilot_id or not body.get("revision_id")
                or not body.get("idempotency_key")):
            raise FactoryError("invalid reference pilot revision request", "reference_pilot_binding", 409)
        with self.store.connect(True) as con:
            pilot = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=? AND campaign_id=?",
                                (pilot_id, self.campaign_id)).fetchone()
            if not pilot:
                raise FactoryError("reference pilot not found", "not_found", 404)
            prior_events = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id",
                                       (pilot_id,)).fetchall()
            for event in prior_events:
                envelope = json.loads(event[0])
                if digest(envelope.get("request")) != envelope.get("request_digest"):
                    raise FactoryError("reference continuation record changed", "full_plan_integrity", 409)
            for event in prior_events:
                saved = json.loads(event[0])
                revision = saved["request"]
                if revision.get("idempotency_key") == body["idempotency_key"]:
                    if digest(revision) != saved.get("request_digest") or revision != body:
                        raise FactoryError("revision idempotency key conflicts", "reference_pilot_binding", 409)
                    return {"pilot_id": pilot_id, "revision_id": revision["revision_id"],
                            "revision_digest": saved["request_digest"], "status": "registered",
                            "effective_max_calls": saved["effective_max_calls"],
                            "idempotent": True, "receipt_only": True}
            if pilot["status"] not in {"active", "completed"}:
                raise FactoryError("pilot is paused or terminal", "full_plan_paused", 409)
            request = json.loads(pilot["request_json"])
            plan = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                               (pilot["plan_id"], self.campaign_id)).fetchone()
            if not plan or plan["status"] != "paused":
                raise FactoryError("continuation requires the same paused full plan", "full_plan_paused", 409)
            if digest(json.loads(plan["request_json"])) != plan["request_digest"]:
                raise FactoryError("original full authorization changed", "full_plan_integrity", 409)
            leaf = body.get("leaf")
            bound_leaves = {x["leaf"] for x in request["leaves"]}
            if (body.get("original_request_digest", body.get("prior_request_digest")) != pilot["request_digest"]
                    or body.get("inputs_digest", self._inputs_digest(request)) != self._inputs_digest(request)
                    or body.get("plan_id") != pilot["plan_id"] or leaf not in bound_leaves):
                raise FactoryError("continuation changed pilot, frozen inputs, or plan", "reference_pilot_binding", 409)
            self._verify_revision_host(con, plan, body)
            self._verify_user_request({"user_request": body.get("latest_user_request", {})})
            controls = con.execute("SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='control' AND id>?",
                                   (plan["id"], pilot["pause_anchor"])).fetchall()
            if any(json.loads(control[0]).get("action") == "pause" for control in controls):
                raise FactoryError("later full-plan pause revoked continuation", "full_plan_paused", 409)
            self._verify_frozen_revision_inputs(con, plan, request)
            calls = con.execute("SELECT identity,stage,status FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started'",
                                (self.campaign_id, pilot["phase"])).fetchall()
            selected_calls = [c for c in calls if c["identity"] in {pilot["plan_id"] + ':' + x['leaf'] for x in request['leaves']}]
            if any(c["status"] in {"reserved", "spawn_intent", "started", "uncertain"} for c in selected_calls):
                raise FactoryError("active or uncertain pilot call blocks continuation", "full_uncertain", 409)
            mine = [c for c in selected_calls if c["stage"] == "reference/research/" + pilot_id]
            if not mine or len(mine) > 6 or any(c["status"] != "completed" for c in mine):
                raise FactoryError("continuation requires completed original research calls", "reference_pilot_paused", 409)
            if len(mine) != len(request["leaves"]):
                raise FactoryError("continuation requires one original research call per leaf", "reference_pilot_paused", 409)
            leaf_revisions = [json.loads(e[0])["request"] for e in prior_events if json.loads(e[0])["request"].get("leaf") == leaf]
            if any(x.get("revision_id") == body["revision_id"] for x in leaf_revisions):
                raise FactoryError("revision identity already used for this leaf", "reference_pilot_binding", 409)
            if (body.get("revision_id") != "r2" and (body.get("revision_id") != "r3" or not leaf_revisions)
                    or body.get("revision_id") == "r3" and leaf_revisions[-1].get("revision_id") != "r2"):
                raise FactoryError("revision must continue the registered r2/r3 chain", "reference_pilot_binding", 409)
            prior = leaf_revisions[-1] if leaf_revisions else None
            parent_values = self._verify_revision_parents(body, leaf, con=con, pilot=pilot,
                                                          original_request=request, prior=prior)
            if body.get("revision_id") == "r3":
                previous_id = "reference/author/" + pilot_id + "/r2"
                previous_review = "reference/review/" + pilot_id + "/r2"
                author_done = any(c["identity"] == pilot["plan_id"] + ":" + leaf and c["stage"] == previous_id and c["status"] == "completed" for c in selected_calls)
                review_rows = [c for c in selected_calls if c["identity"] == pilot["plan_id"] + ":" + leaf and c["stage"] == previous_review]
                if not author_done:
                    raise FactoryError("r3 requires a terminal r2 author", "reference_pilot_paused", 409)
                if parent_values["outcome"].get("status") == "needs_changes":
                    if not any(c["status"] == "completed" for c in review_rows):
                        raise FactoryError("needs_changes r2 requires a terminal independent review", "reference_pilot_paused", 409)
                elif review_rows:
                    raise FactoryError("failed r2 must not create an unnecessary review call", "reference_pilot_paused", 409)
            registered_calls = con.execute("SELECT identity,stage FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started'",
                                           (self.campaign_id, pilot["phase"])).fetchall()
            pilot_calls = [c for c in registered_calls if c["identity"] in {pilot["plan_id"] + ':' + x['leaf'] for x in request['leaves']}]
            own_calls = [c for c in pilot_calls if c["identity"] == pilot["plan_id"] + ":" + leaf]
            if len(pilot_calls) >= 12 or len(own_calls) >= 6:
                raise FactoryError("continuation allowance exhausted", "budget_exhausted", 409)
            event = {"request": body, "request_digest": digest(body), "effective_max_calls": 12,
                     "prior_request_digest": pilot["request_digest"],
                     "research_calls": [{"identity": c["identity"], "stage": c["stage"], "status": c["status"]} for c in mine]}
            con.execute("INSERT INTO auxiliary_reference_pilot_event(pilot_id,kind,body,created) VALUES(?,'revision',?,?)",
                        (pilot_id, json.dumps(event, ensure_ascii=False, sort_keys=True), self.clock()))
            if pilot["status"] == "completed":
                con.execute("UPDATE auxiliary_reference_pilot SET status='active',updated=? WHERE id=?",
                            (self.clock(), pilot_id))
            return {"pilot_id": pilot_id, "revision_id": body["revision_id"],
                    "revision_digest": event["request_digest"], "status": "registered", "effective_max_calls": 12,
                    "idempotent": False, "receipt_only": False}

    def _prior_revision(self, con, pilot, leaf, revision_id):
        if revision_id != "r3":
            return None
        rows = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id",
                           (pilot["id"],)).fetchall()
        found = [json.loads(row[0]).get("request", {}) for row in rows
                 if json.loads(row[0]).get("request", {}).get("leaf") == leaf
                 and json.loads(row[0]).get("request", {}).get("revision_id") == "r2"]
        if len(found) != 1:
            raise FactoryError("r3 requires one registered r2 checkpoint", "reference_pilot_integrity", 409)
        return found[0]

    def _verify_revision_parents(self, body, leaf, *, con=None, pilot=None,
                                 original_request=None, prior=None):
        parents = body.get("parents")
        required = {"research": "research/RESULT.json",
                    "research_receipt": "research/DELIVERED.json",
                    "author": "author/RESULT.json",
                    "author_receipt": "author/DELIVERED.json"}
        if body.get("revision_id") in {"r2", "r3"}:
            required["outcome"] = "OUTCOME.json"
        allowed_parent_sets = {frozenset(required)}
        if body.get("revision_id") == "r3":
            allowed_parent_sets.add(frozenset(set(required) | {"review", "review_receipt"}))
        if not isinstance(parents, dict) or frozenset(parents) not in allowed_parent_sets:
            raise FactoryError("revision parents do not match the prior generation checkpoints", "reference_pilot_integrity", 409)
        values, paths = {}, {}
        for name, suffix in required.items():
            ref = parents[name]
            path = self._evidence_path(ref, "revision parent " + name)
            if not str(ref["path"]).endswith(suffix):
                raise FactoryError("revision parent path is outside its expected prior-stage lineage", "reference_pilot_integrity", 409)
            paths[name] = Path(ref["path"])
            try:
                values[name] = json.loads(path.read_text())
            except ValueError as error:
                raise FactoryError("revision parent checkpoint is not JSON", "reference_pilot_integrity", 409) from error
        if values["outcome"].get("leaf") != leaf:
            raise FactoryError("revision outcome belongs to another leaf", "reference_pilot_integrity", 409)
        generation_root = paths["research"].parent.parent
        if (generation_root.name != "generation"
                or paths["author"].parent.parent != generation_root
                or paths["research_receipt"].parent != paths["research"].parent
                or paths["author_receipt"].parent != paths["author"].parent
                or paths["outcome"].parent != generation_root.parent
                or leaf not in paths["outcome"].parts):
            raise FactoryError("revision parents do not share the same leaf generation lineage", "reference_pilot_integrity", 409)
        if body.get("revision_id") == "r2":
            item = next((x for x in (original_request or {}).get("leaves", []) if x.get("leaf") == leaf), None)
            expected_parent = Path(item["input_path"]).parent if item else None
            if expected_parent is None or generation_root != expected_parent / "generation":
                raise FactoryError("r2 parents do not belong to the original registered sample generation", "reference_pilot_integrity", 409)
            checkpoint_root = expected_parent / "official-checkpoints"
            for stage in ("research", "author"):
                binding_path = self.store.pack.parent / generation_root / stage / "BINDING.json"
                delivered_path = self.store.pack.parent / generation_root / stage / "DELIVERED.json"
                result_path = self.store.pack.parent / generation_root / stage / "RESULT.json"
                input_path = self.store.pack.parent / generation_root / stage / "INPUT.json"
                summary_path = self.store.pack.parent / checkpoint_root / stage / "cli-summary.json"
                root = self.store.pack.parent.resolve()
                for derived in (binding_path, delivered_path, result_path, input_path, summary_path):
                    if derived.is_symlink() or not derived.resolve().is_relative_to(root) or not derived.is_file():
                        raise FactoryError("original stage checkpoint is unsafe or missing", "reference_pilot_integrity", 409)
                binding, delivered = json.loads(binding_path.read_text()), json.loads(delivered_path.read_text())
                result, stage_input, summary = json.loads(result_path.read_text()), json.loads(input_path.read_text()), json.loads(summary_path.read_text())
                session_ids = {row.get("sessionID") for row in delivered.get("read_events", []) if row.get("sessionID")}
                session = summary.get("session_id")
                reservation_stage = "reference/" + stage + "/" + pilot["id"]
                records = con.execute("SELECT id,identity,stage,status,job_id,kind FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity=? AND stage=? AND status='completed'",
                                      (self.campaign_id, pilot["phase"], pilot["plan_id"] + ":" + leaf, reservation_stage)).fetchall()
                if (binding.get("stage") != stage or binding.get("payload_digest") != digest(stage_input)
                        or delivered.get("binding_digest") != digest(binding)
                        or delivered.get("result_digest") != digest(result)
                        or not session or session_ids != {session} or summary.get("exit_code") != 0
                        or records and records[0]["kind"] != ("research" if stage == "research" else "production")
                        or summary.get("reservation_id") != (records[0]["id"] if len(records) == 1 else None)
                        or len(records) != 1 or not records[0]["job_id"]):
                    raise FactoryError("original stage binding, delivery, session, or call-ledger lineage differs", "reference_pilot_integrity", 409)
        else:
            if not prior or Path(prior.get("generation_path", "")) != generation_root:
                raise FactoryError("r3 parents do not match the registered r2 generation path", "reference_pilot_integrity", 409)
            for name, suffix in (("author", "author/RESULT.json"),
                                 ("author_receipt", "author/DELIVERED.json")):
                if paths[name] != generation_root / suffix:
                    raise FactoryError("r3 author parent is not the registered r2 author result", "reference_pilot_integrity", 409)
            if con is None or pilot is None:
                raise FactoryError("r3 ledger context is unavailable", "reference_pilot_integrity", 409)
            research_session = self._verify_revision_stage_files(generation_root, "research", leaf, pilot, con)
            self._verify_revision_stage_files(generation_root, "author", leaf, pilot, con)
            if "review" in parents:
                self._verify_revision_stage_files(generation_root, "review", leaf, pilot, con)
            prior_research = self._evidence_path(prior["parents"]["research"], "r2 research result")
            prior_receipt = self._evidence_path(prior["parents"]["research_receipt"], "r2 research delivery")
            old_result, old_receipt = json.loads(prior_research.read_text()), json.loads(prior_receipt.read_text())
            old_session_ids = {row.get("sessionID") for row in old_receipt.get("read_events", []) if row.get("sessionID")}
            if digest(old_result) != values["research_receipt"].get("result_digest") or old_session_ids != {research_session}:
                raise FactoryError("r3 research differs from the registered r2 research session/result", "reference_pilot_integrity", 409)
        expected_output = Path("docs/template-factory/product-reference-convergence-2026-10-22") / leaf / body.get("revision_id", "") / "generation"
        if Path(body.get("generation_path", "")) != expected_output:
            raise FactoryError("revision output path is outside its fixed leaf/revision generation root", "reference_pilot_integrity", 409)
        if (values["research_receipt"].get("result_digest") != digest(values["research"])
                or values["author_receipt"].get("result_digest") != digest(values["author"])):
            raise FactoryError("delivered result digest differs from its saved result", "reference_pilot_integrity", 409)
        if body.get("revision_id") == "r2":
            if (values["outcome"].get("status") != "failed"
                    or values["outcome"].get("completed_stages") != ["research", "author"]):
                raise FactoryError("r2 must preserve the original terminal author failure", "reference_pilot_integrity", 409)
        elif (values["outcome"].get("status") == "failed"
              and values["outcome"].get("completed_stages") not in (["author"], ["research", "author"])):
            raise FactoryError("failed r2 parent must terminate after its author stage", "reference_pilot_integrity", 409)
        elif (values["outcome"].get("status") == "needs_changes"
              and values["outcome"].get("completed_stages") not in (None, ["author", "review"], ["research", "author", "review"])):
            raise FactoryError("needs_changes r2 parent must include its independent review stage", "reference_pilot_integrity", 409)
        elif values["outcome"].get("status") not in {"failed", "needs_changes"}:
            raise FactoryError("r3 parent must preserve a terminal failed or needs_changes outcome", "reference_pilot_integrity", 409)
        optional = set(parents) - set(required)
        for key in optional:
            suffix = "review/RESULT.json" if key == "review" else "review/DELIVERED.json"
            ref = parents[key]
            path = self._evidence_path(ref, "revision parent " + key)
            expected_path = generation_root / suffix
            if not str(ref["path"]).endswith(suffix) or Path(ref["path"]) != expected_path:
                raise FactoryError("revision review parent path is outside its prior-stage lineage", "reference_pilot_integrity", 409)
        if body.get("revision_id") == "r3":
            has_review = "review" in parents and "review_receipt" in parents
            outcome = values["outcome"]
            if outcome.get("status") == "needs_changes" and not has_review:
                raise FactoryError("needs_changes r2 requires its independent review checkpoint", "reference_pilot_integrity", 409)
            if outcome.get("status") == "failed" and has_review:
                raise FactoryError("deterministic failed r2 does not require a review call", "reference_pilot_integrity", 409)
        return values

    def _verify_revision_stage_files(self, generation_root, stage, leaf, pilot, con):
        root = self.store.pack.parent.resolve()
        binding_path = root / generation_root / stage / "BINDING.json"
        delivered_path = root / generation_root / stage / "DELIVERED.json"
        result_path = root / generation_root / stage / "RESULT.json"
        input_path = root / generation_root / stage / "INPUT.json"
        summary_path = root / generation_root.parent / "official-checkpoints" / stage / "cli-summary.json"
        for path in (binding_path, delivered_path, result_path, input_path, summary_path):
            if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
                raise FactoryError("revision stage evidence is missing or unsafe", "reference_pilot_integrity", 409)
        binding, delivered = json.loads(binding_path.read_text()), json.loads(delivered_path.read_text())
        result, stage_input, summary = json.loads(result_path.read_text()), json.loads(input_path.read_text()), json.loads(summary_path.read_text())
        sessions = {row.get("sessionID") for row in delivered.get("read_events", []) if row.get("sessionID")}
        session = summary.get("session_id")
        revision_id = Path(generation_root).parent.name
        reservation_stage = ("reference/research/" + pilot["id"] if stage == "research"
                             else "reference/" + stage + "/" + pilot["id"] + "/" + revision_id)
        rows = con.execute("SELECT id,identity,stage,status,job_id,kind FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity=? AND stage=? AND status='completed'",
                           (self.campaign_id, pilot["phase"], pilot["plan_id"] + ":" + leaf, reservation_stage)).fetchall()
        if (binding.get("stage") != stage or binding.get("payload_digest") != digest(stage_input)
                or delivered.get("binding_digest") != digest(binding)
                or delivered.get("result_digest") != digest(result)
                or not session or sessions != {session} or summary.get("exit_code") != 0
                or rows and rows[0]["kind"] != {"research": "research", "author": "production", "review": "review"}[stage]
                or summary.get("reservation_id") != (rows[0]["id"] if len(rows) == 1 else None)
                or len(rows) != 1 or not rows[0]["job_id"]):
            raise FactoryError("r2 stage binding, delivery, session, or completed ledger lineage differs", "reference_pilot_integrity", 409)
        return session

    def _verify_revision_host(self, con, plan, body):
        host_event = con.execute("SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id DESC LIMIT 1",
                                 (plan["id"],)).fetchone()
        if not host_event:
            raise FactoryError("latest registered host CI evidence required", "reference_pilot_ci", 409)
        envelope = json.loads(host_event[0])
        host = envelope.get("request", {})
        if (digest(host) != envelope.get("request_digest") or digest(host) != body.get("source_ci", {}).get("host_revision_digest")
                or host.get("code_sha") != body.get("source_ci", {}).get("code_sha")):
            raise FactoryError("continuation does not bind latest registered host revision", "reference_pilot_ci", 409)
        self._verify_host_bytes(host, body.get("production_source_sha256"))
        module = self._profile_module()
        if body.get("profile_version") != module.VERSION or body.get("prompt_digest") != module.PROMPT_DIGEST:
            raise FactoryError("continuation prompt/profile differs from current source", "reference_pilot_binding", 409)

    def _verify_frozen_revision_inputs(self, con, plan, request):
        original = json.loads(plan["request_json"])
        root = self.store.pack.parent.resolve()
        for key in ("authorization", "scope"):
            ref = original[key]
            path = (root / ref["path"]).resolve()
            if not path.is_relative_to(root) or hashlib.sha256(path.read_bytes()).hexdigest() != ref["sha256"]:
                raise FactoryError("original full-plan frozen scope changed", "full_plan_integrity", 409)
        for item in request["leaves"]:
            frozen = con.execute("SELECT state,body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                                 (plan["id"], item["leaf"])).fetchone()
            scope = json.loads((root / original["scope"]["path"]).read_text())
            scope_item = next((x for x in scope["items"] if x["leaf"] == item["leaf"]), {})
            if (not frozen or frozen["state"] != "reused"
                    or json.loads(frozen["body"]).get("leaf_sha256") != item["frozen_leaf_sha256"]
                    or scope_item.get("leaf_sha256") != item["frozen_leaf_sha256"]):
                raise FactoryError("continuation changed frozen leaf", "reference_pilot_scope", 409)
            self._verify_leaf_input(item, item["leaf"], con=con)

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

    @staticmethod
    def _historical_alignment(con, pilot):
        rows = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='host_alignment' ORDER BY id",
                           (pilot["id"],)).fetchall()
        if len(rows) > 1:
            raise FactoryError("reference pilot has an invalid historical alignment chain", "full_plan_integrity", 409)
        if not rows:
            return None
        envelope = json.loads(rows[0][0])
        alignment = envelope.get("alignment", {})
        if (digest(alignment) != envelope.get("alignment_digest")
                or envelope.get("old_profile_source_sha256") != alignment.get("previous_profile_source_sha256")
                or envelope.get("new_profile_source_sha256") != alignment.get("new_profile_source_sha256")):
            raise FactoryError("historical alignment receipt changed", "full_plan_integrity", 409)
        return {**envelope, "alignment": alignment}

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
        revisions = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id",
                                (pilot["id"],)).fetchall()
        if not revisions:
            self._validate_shape(request)
        elif (request.get("schema") != SCHEMA or request.get("campaign_id") != self.campaign_id
              or request.get("profile_version") != PROFILE_VERSION):
            raise FactoryError("stored reference pilot identity changed", "full_plan_integrity", 409)
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
        if revisions:
            # Preserve the old alignment as a historical receipt. Validate each append-only
            # continuation against the latest profile/CI bytes without reinterpreting it
            # through today's prompt or host source.
            last = json.loads(revisions[-1][0])
            body = last.get("request", {})
            if digest(body) != last.get("request_digest"):
                raise FactoryError("reference continuation record changed", "full_plan_integrity", 409)
            self._verify_revision_host(con, plan, body)
            self._verify_user_request({"user_request": body.get("latest_user_request", {})})
            if body.get("original_request_digest", body.get("prior_request_digest")) != pilot["request_digest"]:
                raise FactoryError("continuation no longer binds original pilot", "full_plan_integrity", 409)
        else:
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

