"""Scoped full-leaf authorization and durable operator state, never a G1 grant."""

import hashlib
import json
import time

from .store import FactoryError, digest

MODEL = "opencode-go/minimax-m3.1-flash-free"
REVISED_MODEL = "open-design/deepseek-v4.1-flash"
MODEL_SWITCH_AUTHORIZATION = "docs/template-factory/open-design-switch-2026-10-22/authorization/USER_MODEL_SWITCH.txt"
ROUND_AUTHORIZATION = "docs/template-factory/workflow-rounds-2026-10-22/authorization/USER_REQUEST.txt"


def ensure_schema(con):
    con.execute(
        "CREATE TABLE IF NOT EXISTS auxiliary_full_plan (id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,phase TEXT NOT NULL UNIQUE,request_json TEXT NOT NULL,request_digest TEXT NOT NULL,baseline INTEGER NOT NULL,max_calls INTEGER NOT NULL,window_seconds INTEGER NOT NULL,model TEXT NOT NULL,status TEXT NOT NULL,created REAL NOT NULL,started REAL,deadline REAL,reason TEXT)"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS auxiliary_full_leaf (plan_id TEXT NOT NULL,slug TEXT NOT NULL,ordinal INTEGER NOT NULL,state TEXT NOT NULL,body TEXT NOT NULL,updated REAL NOT NULL,PRIMARY KEY(plan_id,slug))"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS auxiliary_full_event (id INTEGER PRIMARY KEY,plan_id TEXT NOT NULL,slug TEXT,kind TEXT NOT NULL,body TEXT NOT NULL,created REAL NOT NULL)"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS auxiliary_workflow_gate(plan_id TEXT PRIMARY KEY,body TEXT NOT NULL,updated REAL NOT NULL)"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS auxiliary_reference_pilot(id TEXT PRIMARY KEY,plan_id TEXT NOT NULL,campaign_id TEXT NOT NULL,phase TEXT NOT NULL UNIQUE,request_json TEXT NOT NULL,request_digest TEXT NOT NULL,max_calls INTEGER NOT NULL,status TEXT NOT NULL,created REAL NOT NULL,updated REAL NOT NULL,pause_anchor INTEGER NOT NULL DEFAULT 0)"
    )
    pilot_columns = {row[1] for row in con.execute("PRAGMA table_info(auxiliary_reference_pilot)")}
    if "pause_anchor" not in pilot_columns:
        con.execute("ALTER TABLE auxiliary_reference_pilot ADD COLUMN pause_anchor INTEGER NOT NULL DEFAULT 0")
    con.execute(
        "CREATE TABLE IF NOT EXISTS auxiliary_reference_pilot_event(id INTEGER PRIMARY KEY,pilot_id TEXT NOT NULL,kind TEXT NOT NULL,body TEXT NOT NULL,created REAL NOT NULL)"
    )


class FullAuxiliaryService:
    def __init__(
        self, store, campaign_id="atlas-v1-first-production-2026-10-19", clock=time.time
    ):
        self.store, self.campaign_id, self.clock = store, campaign_id, clock
        from .budget import BudgetLedger

        self.ledger = BudgetLedger(store, campaign_id=campaign_id, clock=clock)

    def register(self, request):
        if (
            request.get("schema") != "atlas.full-leaf-auxiliary-authorization.v1"
            or request.get("campaign_id") != self.campaign_id
            or request.get("model") != MODEL
            or request.get("max_new_calls") != 7200
            or request.get("per_leaf_calls") != 6
            or request.get("concurrency") != 2
            or request.get("batch_size") != 20
            or request.get("window_seconds") != 2592000
            or not request.get("full_plan_id")
            or request.get("phase") != "auxiliary-full-" + request["full_plan_id"]
        ):
            raise FactoryError(
                "invalid fixed full-plan authorization", "full_plan_binding", 409
            )
        root = self.store.pack.parent
        for key in ("authorization", "scope"):
            ref = request[key]
            path = (root / ref["path"]).resolve()
            if (
                not path.is_relative_to(root.resolve())
                or hashlib.sha256(path.read_bytes()).hexdigest() != ref["sha256"]
            ):
                raise FactoryError(
                    "authorization/scope bytes differ", "full_plan_integrity", 409
                )
        scope = json.loads((root / request["scope"]["path"]).read_text())
        if scope["full_plan_id"] != request["full_plan_id"] or len(
            {x["leaf"] for x in scope["items"]}
        ) != len(scope["items"]):
            raise FactoryError("scope identity differs", "full_plan_integrity", 409)
        baseline = self.ledger.snapshot()
        with self.store.connect(True) as con:
            prior = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=?",
                (request["full_plan_id"],),
            ).fetchone()
            if prior:
                if prior["request_digest"] != digest(request):
                    raise FactoryError(
                        "full plan already bound", "full_plan_binding", 409
                    )
                return self._receipt(prior)
            if (
                baseline["active"]
                or request["baseline"] != baseline["cli_sessions_used"]
            ):
                raise FactoryError(
                    "full-plan baseline changed/active", "full_plan_baseline", 409
                )
            charged = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                (self.campaign_id,),
            ).fetchone()[0]
            active = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                (self.campaign_id,),
            ).fetchone()[0]
            if (
                active
                or charged + baseline["external_cli_sessions_used"]
                != request["baseline"]
            ):
                raise FactoryError(
                    "baseline changed under registration lock",
                    "full_plan_baseline",
                    409,
                )
            con.execute(
                "INSERT INTO auxiliary_full_plan VALUES(?,?,?,?,?,?,?,?,?,'registered',?,NULL,NULL,NULL)",
                (
                    request["full_plan_id"],
                    self.campaign_id,
                    request["phase"],
                    json.dumps(request, sort_keys=True),
                    digest(request),
                    request["baseline"],
                    7200,
                    2592000,
                    MODEL,
                    self.clock(),
                ),
            )
            for n, item in enumerate(scope["items"]):
                state = "reused" if item.get("covered") else "pending"
                con.execute(
                    "INSERT INTO auxiliary_full_leaf VALUES(?,?,?,?,?,?)",
                    (
                        request["full_plan_id"],
                        item["leaf"],
                        n,
                        state,
                        json.dumps(item, ensure_ascii=False),
                        self.clock(),
                    ),
                )
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'registered',?,?)",
                (request["full_plan_id"], json.dumps(request), self.clock()),
            )
            return self._receipt(
                con.execute(
                    "SELECT * FROM auxiliary_full_plan WHERE id=?",
                    (request["full_plan_id"],),
                ).fetchone()
            )

    @staticmethod
    def _receipt(row):
        return {
            k: row[k]
            for k in (
                "id",
                "campaign_id",
                "phase",
                "request_digest",
                "baseline",
                "max_calls",
                "window_seconds",
                "model",
                "created",
            )
        }

    def status(self, plan_id):
        with self.store.connect() as con:
            row = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (plan_id, self.campaign_id),
            ).fetchone()
            if not row:
                raise FactoryError("full plan not registered", "not_found", 404)
            items = [
                {**json.loads(x["body"]), "state": x["state"]}
                for x in con.execute(
                    "SELECT * FROM auxiliary_full_leaf WHERE plan_id=? ORDER BY ordinal",
                    (plan_id,),
                )
            ]
            calls = [
                dict(x)
                for x in con.execute(
                    "SELECT id,identity,stage,status,job_id,requested_model,outcome,created,started,finished FROM tf_budget_reservation WHERE campaign_id=? AND phase=? ORDER BY created",
                    (self.campaign_id, row["phase"]),
                )
            ]
        from collections import Counter

        counts = dict(Counter(x["state"] for x in items))
        charged = [c for c in calls if c["status"] != "not_started"]
        terminal = {
            "reused",
            "ready_not_run",
            "failed",
            "needs_revision",
            "source_unavailable",
            "unsupported",
        }
        return {
            **self._receipt(row),
            "status": row["status"],
            "reason": row["reason"],
            "started": row["started"],
            "deadline": row["deadline"],
            "counts": counts,
            "total": len(items),
            "handled": sum(x["state"] in terminal for x in items),
            "attempted": len({c["identity"] for c in charged}),
            "new_calls": len(charged),
            "remaining_calls": row["max_calls"] - len(charged),
            "active_calls": sum(
                c["status"] in {"reserved", "spawn_intent", "started", "uncertain"}
                for c in calls
            ),
            "items": items,
            "calls": calls,
            "provider_requests": None,
            "observed_model": None,
            "cost": None,
        }

    def control_state(self, plan_id):
        with self.store.connect() as con:
            row = con.execute(
                "SELECT status FROM auxiliary_full_plan WHERE id=?", (plan_id,)
            ).fetchone()
            return row[0] if row else "unregistered"

    def host_revision(self, plan_id):
        with self.store.connect() as con:
            row = con.execute(
                "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id DESC LIMIT 1",
                (plan_id,),
            ).fetchone()
        if not row:
            return None
        value = json.loads(row[0])
        if digest(value["request"]) != value["request_digest"]:
            raise FactoryError(
                "host revision record changed", "full_plan_integrity", 409
            )
        return value["request"]

    @staticmethod
    def _model_revisions(con, plan_id, row, root=None):
        """Read and verify the append-only model amendment chain."""
        events = con.execute(
            "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='model_revision' ORDER BY id",
            (plan_id,),
        ).fetchall()
        model = MODEL
        revisions = []
        original = json.loads(row["request_json"])
        if digest(original) != row["request_digest"]:
            raise FactoryError("stored full authorization changed", "full_plan_integrity", 409)
        if original.get("model") != MODEL:
            raise FactoryError("initial model binding changed", "full_plan_integrity", 409)
        for event in events:
            value = json.loads(event[0])
            request = value.get("request", {})
            if digest(request) != value.get("request_digest"):
                raise FactoryError("model revision record changed", "full_plan_integrity", 409)
            if revisions or request.get("previous_model") != model or request.get("new_model") != REVISED_MODEL:
                raise FactoryError("model revision lineage changed", "full_plan_integrity", 409)
            authorization = request.get("authorization", {})
            if (authorization.get("path") != MODEL_SWITCH_AUTHORIZATION
                or not authorization.get("sha256")):
                raise FactoryError("model revision authorization missing", "full_plan_integrity", 409)
            if root is not None:
                auth_path = (root / authorization["path"]).resolve()
                if (not auth_path.is_relative_to(root.resolve()) or not auth_path.is_file()
                    or hashlib.sha256(auth_path.read_bytes()).hexdigest() != authorization["sha256"]):
                    raise FactoryError("model revision authorization changed", "full_plan_integrity", 409)
            model = request["new_model"]
            revisions.append(request)
        if row["model"] != model:
            raise FactoryError("effective model binding changed", "full_plan_integrity", 409)
        return model, revisions

    def effective_model(self, plan_id):
        with self.store.connect() as con:
            row = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?", (plan_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("full plan not registered", "not_found", 404)
            return self._model_revisions(con, plan_id, row, self.store.pack.parent)[0]

    def allowed_models(self, plan_id):
        with self.store.connect() as con:
            row = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?", (plan_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("full plan not registered", "not_found", 404)
            _, revisions = self._model_revisions(con, plan_id, row, self.store.pack.parent)
            return [MODEL] + [x["new_model"] for x in revisions]

    def register_model_revision(self, request):
        if request.get("schema") != "atlas.full-leaf-model-revision.v1" or not request.get("reason"):
            raise FactoryError("invalid model revision", "full_plan_binding", 409)
        plan_id = request.get("full_plan_id")
        with self.store.connect(True) as con:
            row = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?", (plan_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("unknown plan", "not_found", 404)
            root = self.store.pack.parent.resolve()
            model, revisions = self._model_revisions(con, plan_id, row, root)
            for value in revisions:
                if value == request:
                    receipt = con.execute("SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='model_revision' ORDER BY id", (plan_id,)).fetchall()[revisions.index(value)]
                    return json.loads(receipt[0])["receipt"]
            if model != MODEL or request.get("previous_model") != model or request.get("new_model") != REVISED_MODEL:
                raise FactoryError("model revision lineage differs", "full_plan_binding", 409)
            grant = json.loads(row["request_json"])
            auth = grant["authorization"]
            auth_path = (root / auth["path"]).resolve()
            if (not auth_path.is_relative_to(root) or hashlib.sha256(auth_path.read_bytes()).hexdigest() != auth["sha256"]
                or request.get("authorization_sha256") != auth["sha256"]):
                raise FactoryError("original authorization changed", "full_plan_integrity", 409)
            user_auth = request.get("authorization", {})
            if user_auth.get("path") != MODEL_SWITCH_AUTHORIZATION:
                raise FactoryError("model revision authorization path differs", "full_plan_binding", 409)
            user_auth_path = (root / user_auth.get("path", "")).resolve()
            if (not user_auth.get("sha256") or not user_auth_path.is_relative_to(root)
                or not user_auth_path.is_file()
                or hashlib.sha256(user_auth_path.read_bytes()).hexdigest() != user_auth["sha256"]):
                raise FactoryError("model revision authorization changed", "full_plan_integrity", 409)
            scope = grant["scope"]
            scope_path = (root / scope["path"]).resolve()
            if (not scope_path.is_relative_to(root) or hashlib.sha256(scope_path.read_bytes()).hexdigest() != scope["sha256"]):
                raise FactoryError("original scope changed", "full_plan_integrity", 409)
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status IN ('reserved','spawn_intent','started','uncertain')", (self.campaign_id, row["phase"])).fetchone()[0]
            if row["status"] != "paused" or active:
                raise FactoryError("drain and pause before model activation", "full_plan_paused", 409)
            receipt = {"full_plan_id": plan_id, "request_digest": digest(request), "previous_model": model,
                       "new_model": REVISED_MODEL, "authorization_sha256": auth["sha256"],
                       "user_authorization_sha256": user_auth["sha256"],
                       "baseline": row["baseline"], "max_calls": row["max_calls"],
                       "started": row["started"], "deadline": row["deadline"], "registered_at": self.clock()}
            con.execute("INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'model_revision',?,?)",
                        (plan_id, json.dumps({"request": request, "request_digest": digest(request), "receipt": receipt}), self.clock()))
            con.execute("UPDATE auxiliary_full_plan SET model=? WHERE id=?", (REVISED_MODEL, plan_id))
            return receipt

    def prove_unlaunched(self, plan_id, leaf, work_name, stage, directory):
        """A required reservation never existed; retain intent and record host proof."""
        from atlas_runtime import atomic_json
        from pathlib import Path

        path = Path(directory).resolve()
        with self.store.connect(True) as con:
            plan = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (plan_id, self.campaign_id),
            ).fetchone()
            member = con.execute(
                "SELECT body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                (plan_id, leaf),
            ).fetchone()
            if not plan or not member:
                raise FactoryError("unknown recovery scope", "full_plan_binding", 409)
            repo_root = self.store.pack.parent.resolve()
            _, revisions = self._model_revisions(con, plan_id, plan, repo_root)
            allowed_models = [MODEL] + [x["new_model"] for x in revisions]
            plan_root = (repo_root / json.loads(plan["request_json"])["scope"]["path"]).parent.resolve()
            if not plan_root.is_relative_to(repo_root):
                raise FactoryError("recovery scope path differs", "full_plan_binding", 409)
            expected = plan_root / "items" / leaf / work_name / "calls"
            if path.parent != expected or not (path / "LAUNCH_INTENT.json").exists():
                raise FactoryError("recovery path differs", "full_plan_binding", 409)
            row = json.loads(member["body"])
            binding = json.loads((path / "BINDING.json").read_text())
            if (
                binding.get("model") not in allowed_models
                or binding["leaf_sha256"] != row["leaf_sha256"]
                or json.loads((path / "LAUNCH_INTENT.json").read_text())[
                    "binding_digest"
                ]
                != digest(binding)
            ):
                raise FactoryError(
                    "recovery binding differs", "full_plan_integrity", 409
                )
            jobs = con.execute(
                "SELECT status FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity=? AND job_id=? AND stage=?",
                (
                    self.campaign_id,
                    plan["phase"],
                    plan_id + ":" + leaf,
                    plan_id + ":" + leaf + ":" + work_name,
                    stage,
                ),
            ).fetchall()
            if any(x[0] != "not_started" for x in jobs) or any(
                (path / n).exists()
                for n in [
                    "process.json",
                    "events.jsonl",
                    "stdout.log",
                    "original-response.json",
                    "DELIVERED.json",
                ]
            ):
                raise FactoryError(
                    "call may have started; cannot prove free recovery",
                    "full_uncertain",
                    409,
                )
            proof = {
                "plan_id": plan_id,
                "leaf": leaf,
                "stage": stage,
                "directory": str(path.relative_to(repo_root)),
                "intent_sha256": hashlib.sha256(
                    (path / "LAUNCH_INTENT.json").read_bytes()
                ).hexdigest(),
                "charged_reservations": 0,
                "process_or_output_artifacts": False,
                "kind": "host_proven_not_started",
                "observed_at": self.clock(),
            }
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,slug,kind,body,created) VALUES(?,?,'proved_not_started',?,?)",
                (plan_id, leaf, json.dumps(proof), self.clock()),
            )
        atomic_json(path / "NOT_STARTED_PROOF.json", proof)
        atomic_json(
            path / "cli-summary.json",
            {
                "requested_model": binding["model"],
                "session_id": None,
                "cli_status": "not_started",
                "delivery_status": "failed",
                "output_observed": False,
                "failure_code": "host_proven_not_started",
                "reservation_id": None,
                "host_proof_digest": digest(proof),
            },
        )
        return proof

    def register_host_revision(self, request):
        """Append tested host-code correction; never rewrite scope, quota or clock."""
        if request.get(
            "schema"
        ) != "atlas.full-leaf-host-revision.v1" or not request.get("reason"):
            raise FactoryError("invalid host revision", "full_plan_binding", 409)
        plan_id = request["full_plan_id"]
        with self.store.connect(True) as con:
            row = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (plan_id, self.campaign_id),
            ).fetchone()
            if not row:
                raise FactoryError("unknown plan", "not_found", 404)
            prior = con.execute(
                "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id DESC LIMIT 1",
                (plan_id,),
            ).fetchone()
            if prior and json.loads(prior[0])["request_digest"] == digest(request):
                return json.loads(prior[0])["receipt"]
            grant = json.loads(row["request_json"])
            root = self.store.pack.parent
            if (
                hashlib.sha256(
                    (root / grant["authorization"]["path"]).read_bytes()
                ).hexdigest()
                != grant["authorization"]["sha256"]
            ):
                raise FactoryError(
                    "original authorization changed", "full_plan_integrity", 409
                )
            scope = json.loads((root / grant["scope"]["path"]).read_text())
            if (
                hashlib.sha256((root / grant["scope"]["path"]).read_bytes()).hexdigest()
                != grant["scope"]["sha256"]
                or request["scope_sha256"] != grant["scope"]["sha256"]
                or request["authorization_sha256"] != grant["authorization"]["sha256"]
            ):
                raise FactoryError(
                    "host correction cannot change frozen authorization/scope",
                    "full_plan_integrity",
                    409,
                )
            previous = (
                json.loads(prior[0])["request"]["new_host_sha256"]
                if prior
                else scope["host_source_sha256"]
            )
            added = set(request["new_host_sha256"]) - set(previous)
            workflow_module = "application-atlas-production-pack/template_factory/auxiliary_workflow.py"
            if (
                workflow_module in request["new_host_sha256"]
                and request.get("workflow_gate_required") is not True
            ):
                raise FactoryError(
                    "workflow host activation requires validation gate",
                    "workflow_gate",
                    409,
                )
            if (
                request["previous_host_sha256"] != previous
                or not set(previous) <= set(request["new_host_sha256"])
                or any(
                    not (
                        name.startswith(
                            (
                                "application-atlas-production-pack/template_factory/",
                                "examples/assisted-trials/",
                            )
                        )
                        or name in {
                            "application-atlas-production-pack/drafts_api.py",
                            "application-atlas-production-pack/tests/test_reference_pilot.py",
                        }
                    )
                    for name in added
                )
            ):
                raise FactoryError(
                    "host correction lineage differs", "full_plan_binding", 409
                )
            for name, value in request["new_host_sha256"].items():
                path = (root / name).resolve()
                if (
                    not path.is_relative_to(root.resolve())
                    or hashlib.sha256(path.read_bytes()).hexdigest() != value
                ):
                    raise FactoryError(
                        "tested host bytes differ", "full_plan_integrity", 409
                    )
            ci_path = (root / request["ci_proof"]["path"]).resolve()
            if not ci_path.is_relative_to(root.resolve()):
                raise FactoryError(
                    "CI proof outside repository", "full_plan_binding", 409
                )
            ci = json.loads(ci_path.read_text())
            if (
                hashlib.sha256(
                    (root / request["ci_proof"]["path"]).read_bytes()
                ).hexdigest()
                != request["ci_proof"]["sha256"]
                or ci.get("sha") != request["code_sha"]
                or ci.get("status") != "completed"
                or ci.get("conclusion") != "success"
            ):
                raise FactoryError(
                    "exact host CI proof missing", "full_plan_binding", 409
                )
            active = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                (self.campaign_id, row["phase"]),
            ).fetchone()[0]
            if row["status"] != "paused" or active:
                raise FactoryError(
                    "drain and pause before host activation", "full_plan_paused", 409
                )
            receipt = {
                "full_plan_id": plan_id,
                "request_digest": digest(request),
                "code_sha": request["code_sha"],
                "previous_host_sha256": previous,
                "new_host_sha256": request["new_host_sha256"],
                "baseline": row["baseline"],
                "max_calls": row["max_calls"],
                "started": row["started"],
                "deadline": row["deadline"],
                "registered_at": self.clock(),
            }
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'host_revision',?,?)",
                (
                    plan_id,
                    json.dumps(
                        {
                            "request": request,
                            "request_digest": digest(request),
                            "receipt": receipt,
                        }
                    ),
                    self.clock(),
                ),
            )
            return receipt

    def schedule_provider_recovery(self, plan_id):
        """At most two shared-service backoffs, not free provider probes."""
        with self.store.connect(True) as con:
            count = con.execute(
                "SELECT COUNT(*) FROM auxiliary_full_event WHERE plan_id=? AND kind='provider_backoff'",
                (plan_id,),
            ).fetchone()[0]
            if count >= 2:
                return None
            body = {
                "number": count + 1,
                "resume_after": self.clock() + (60 if count == 0 else 300),
                "new_probe_call": False,
            }
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'provider_backoff',?,?)",
                (plan_id, json.dumps(body), self.clock()),
            )
            return body

    def update_leaf(self, plan_id, slug, state, details):
        allowed = {
            "reused",
            "ready_not_run",
            "pending",
            "running",
            "paused",
            "needs_revision",
            "failed",
            "source_unavailable",
            "unsupported",
        }
        if state not in allowed:
            raise ValueError("invalid leaf state")
        with self.store.connect(True) as con:
            old = con.execute(
                "SELECT body,state FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                (plan_id, slug),
            ).fetchone()
            if not old:
                raise FactoryError(
                    "leaf outside frozen scope", "full_plan_binding", 409
                )
            body = json.loads(old["body"])
            if old["state"] in {"reused", "ready_not_run"} and (
                old["state"] != state
                or any(body.get(k) != v for k, v in details.items())
            ):
                raise FactoryError(
                    "cannot rewrite completed leaf", "full_plan_binding", 409
                )
            body.update(details)
            con.execute(
                "UPDATE auxiliary_full_leaf SET state=?,body=?,updated=? WHERE plan_id=? AND slug=?",
                (
                    state,
                    json.dumps(body, ensure_ascii=False),
                    self.clock(),
                    plan_id,
                    slug,
                ),
            )
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,slug,kind,body,created) VALUES(?,?,?,?,?)",
                (plan_id, slug, state, json.dumps(details), self.clock()),
            )

    def control(self, plan_id, action, reason="operator"):
        if action not in {"resume", "pause", "stop", "complete"}:
            raise ValueError("unknown action")
        state = {
            "resume": "running",
            "pause": "paused",
            "stop": "stopped",
            "complete": "completed",
        }[action]
        with self.store.connect(True) as con:
            row = con.execute(
                "SELECT status FROM auxiliary_full_plan WHERE id=?", (plan_id,)
            ).fetchone()
            if not row:
                raise FactoryError("unknown full plan", "not_found", 404)
            if row[0] == "stopped" and action != "stop":
                raise FactoryError(
                    "stopped plan cannot dispatch", "full_plan_stopped", 409
                )
            con.execute(
                "UPDATE auxiliary_full_plan SET status=?,reason=? WHERE id=?",
                (state, reason, plan_id),
            )
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'control',?,?)",
                (
                    plan_id,
                    json.dumps({"action": action, "reason": reason}),
                    self.clock(),
                ),
            )
        return self.status(plan_id)

    def pause_if_running(self, plan_id, reason):
        """Pause once without letting concurrent callers overwrite the first reason."""
        with self.store.connect(True) as con:
            row = con.execute(
                "SELECT status FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (plan_id, self.campaign_id),
            ).fetchone()
            if not row:
                raise FactoryError("unknown full plan", "not_found", 404)
            if row["status"] not in {"running", "registered"}:
                return False
            con.execute(
                "UPDATE auxiliary_full_plan SET status='paused',reason=? WHERE id=? AND campaign_id=?",
                (reason, plan_id, self.campaign_id),
            )
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'control',?,?)",
                (plan_id, json.dumps({"action": "pause", "reason": reason}), self.clock()),
            )
            return True

    def record_source_outcome(self, plan_id, leaf, event_key, outcome, detail=None):
        """Persist real source-network outcomes and pause after three distinct leaf failures.

        Callers must report ``success`` only after a real network GET succeeds and
        ``exhausted`` only after that leaf's bounded HTTP retry policy is spent.
        """
        if (not isinstance(leaf, str) or not leaf or not isinstance(event_key, str)
            or not event_key.strip() or not isinstance(outcome, str)
            or outcome not in {"success", "exhausted"}):
            raise FactoryError("invalid source outcome", "full_plan_binding", 409)
        if detail is None:
            detail = {}
        if not isinstance(detail, dict):
            raise FactoryError("source outcome detail must be an object", "full_plan_binding", 409)
        host = detail.get("host", "public-source")
        if host not in {"public-source", "api.github.com", "raw.githubusercontent.com"}:
            raise FactoryError("unsupported source host", "full_plan_binding", 409)
        payload = {"plan_id": plan_id, "leaf": leaf, "event_key": event_key,
                   "outcome": outcome, "host": host, "detail": detail}
        payload_digest = digest(payload)
        with self.store.connect(True) as con:
            plan = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (plan_id, self.campaign_id),
            ).fetchone()
            if not plan:
                raise FactoryError("unknown full plan", "not_found", 404)
            member = con.execute(
                "SELECT 1 FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                (plan_id, leaf),
            ).fetchone()
            if not member:
                raise FactoryError("leaf outside frozen scope", "full_plan_binding", 409)
            events = con.execute(
                "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='source_health' ORDER BY id",
                (plan_id,),
            ).fetchall()
            failures = set()
            for event in events:
                saved = json.loads(event[0])
                prior = saved.get("request", {})
                prior_digest = saved.get("request_digest")
                if digest(prior) != prior_digest:
                    raise FactoryError("source outcome record changed", "full_plan_integrity", 409)
                if prior.get("outcome") not in {"success", "exhausted"}:
                    raise FactoryError("source outcome record has invalid outcome", "full_plan_integrity", 409)
                if prior.get("event_key") == event_key:
                    if prior_digest != payload_digest:
                        raise FactoryError("source event key reused with different payload", "full_plan_binding", 409)
                    return saved["result"]
                if prior.get("host", "public-source") == host:
                    if prior.get("outcome") == "success":
                        failures.clear()
                    elif prior.get("outcome") == "exhausted":
                        failures.add(prior["leaf"])
                else:
                    continue
            if outcome == "success":
                failures.clear()
            else:
                failures.add(leaf)
            distinct = sorted(failures)
            should_pause = len(distinct) >= 3 and plan["status"] in {"running", "registered"}
            result = {"plan_id": plan_id, "event_key": event_key, "outcome": outcome, "host": host,
                      "paused": bool(should_pause), "distinct_failures": distinct,
                      "threshold": 3}
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,slug,kind,body,created) VALUES(?,?,'source_health',?,?)",
                (plan_id, leaf, json.dumps({"request": payload, "request_digest": payload_digest,
                                            "result": result}), self.clock()),
            )
            if should_pause:
                reason = "full_source_unavailable: three distinct leaves exhausted source retries"
                con.execute(
                    "UPDATE auxiliary_full_plan SET status='paused',reason=? WHERE id=? AND campaign_id=? AND status IN ('running','registered')",
                    (reason, plan_id, self.campaign_id),
                )
                con.execute(
                    "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'control',?,?)",
                    (plan_id, json.dumps({"action": "pause", "reason": reason}), self.clock()),
                )
            return result

    def selected_leaves(self, plan_id):
        with self.store.connect() as con:
            row = con.execute(
                "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='selected_dispatch' ORDER BY id DESC LIMIT 1",
                (plan_id,),
            ).fetchone()
        if not row:
            return []
        event = json.loads(row[0])
        receipt = event.get("receipt", {})
        if (digest(event["leaves"]) != event.get("selection_digest")
            or receipt.get("leaves") != event["leaves"]
            or receipt.get("selection_digest") != event["selection_digest"]):
            raise FactoryError("selected dispatch record changed", "full_plan_integrity", 409)
        if event.get("mode") == "full_first_round":
            return []
        return event["leaves"]

    def dispatch_mode(self, plan_id):
        with self.store.connect() as con:
            row = con.execute(
                "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='selected_dispatch' ORDER BY id DESC LIMIT 1",
                (plan_id,),
            ).fetchone()
        if not row:
            return "legacy"
        event = json.loads(row[0])
        self.selected_leaves(plan_id)  # Verify the same durable selection binding.
        mode = event.get("mode", "selected_first_pass")
        if mode not in {"selected_first_pass", "pilot_complete", "full_first_round"}:
            raise FactoryError("unknown dispatch mode", "full_plan_integrity", 409)
        return mode

    def resume_round(self, request):
        """Append a bounded round under the original scope, budget and deadline.

        pilot_complete closes the existing three-leaf revision loop. Full round
        one attempts each remaining leaf once, then pauses for a human review;
        it never silently enters content repair or resets previous failures.
        """
        mode = request.get("mode")
        if (request.get("schema") != "atlas.auxiliary-round.v1"
            or mode not in {"pilot_complete", "full_first_round"}
            or not request.get("reason")):
            raise FactoryError("invalid round request", "full_plan_binding", 409)
        plan_id = request.get("full_plan_id")
        with self.store.connect(True) as con:
            row = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                              (plan_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("unknown plan", "not_found", 404)
            prior = con.execute("SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='selected_dispatch' ORDER BY id DESC LIMIT 1",
                                (plan_id,)).fetchone()
            root = self.store.pack.parent.resolve()
            grant = json.loads(row["request_json"])
            round_auth = request.get("authorization", {})
            if round_auth.get("path") != ROUND_AUTHORIZATION:
                raise FactoryError("round authorization path differs", "full_plan_binding", 409)
            for binding in (grant["authorization"], grant["scope"], round_auth):
                path = (root / binding.get("path", "")).resolve()
                if (not path.is_relative_to(root) or not path.is_file()
                    or hashlib.sha256(path.read_bytes()).hexdigest() != binding.get("sha256")):
                    raise FactoryError("round authorization/scope changed", "full_plan_integrity", 409)
            if prior:
                saved = json.loads(prior[0])
                if saved.get("round_request_digest") == digest(request):
                    return saved["receipt"]
            if row["status"] != "paused":
                raise FactoryError("round activation requires paused plan", "full_plan_paused", 409)
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                                 (self.campaign_id, row["phase"])).fetchone()[0]
            if active:
                raise FactoryError("drain calls before round activation", "full_plan_paused", 409)
            if request.get("original_request_digest") != row["request_digest"]:
                raise FactoryError("round changes original plan", "full_plan_binding", 409)
            if self.clock() >= (row["deadline"] or float("inf")):
                raise FactoryError("original deadline exhausted", "budget_deadline", 409)
            model, _ = self._model_revisions(con, plan_id, row, root)
            if request.get("model") != model:
                raise FactoryError("round model differs", "full_plan_binding", 409)
            members = {x[0] for x in con.execute("SELECT slug FROM auxiliary_full_leaf WHERE plan_id=?", (plan_id,))}
            leaves = request.get("leaves")
            if (not isinstance(leaves, list) or not leaves or any(not isinstance(x, str) for x in leaves)
                or len(leaves) != len(set(leaves)) or not set(leaves) <= members
                or (mode == "pilot_complete" and len(leaves) > 3)
                or (mode == "full_first_round" and set(leaves) != members)):
                raise FactoryError("round leaf scope differs", "full_plan_binding", 409)
            gate = con.execute("SELECT body FROM auxiliary_workflow_gate WHERE plan_id=?", (plan_id,)).fetchone()
            if not gate or json.loads(gate[0]).get("status") != "passed" or json.loads(gate[0]).get("mode") != "full":
                raise FactoryError("actual workflow gate required", "full_plan_paused", 409)
            selection = sorted(leaves)
            receipt = {"full_plan_id": plan_id, "mode": mode, "leaves": selection,
                       "selection_digest": digest(selection), "round_request_digest": digest(request),
                       "baseline": row["baseline"], "max_calls": row["max_calls"],
                       "started": row["started"], "deadline": row["deadline"], "resumed_at": self.clock()}
            event = {"mode": mode, "leaves": selection, "selection_digest": digest(selection),
                     "round_request": request, "round_request_digest": digest(request), "receipt": receipt}
            con.execute("INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'selected_dispatch',?,?)",
                        (plan_id, json.dumps(event), self.clock()))
            con.execute("UPDATE auxiliary_full_plan SET status='running',reason=? WHERE id=?",
                        ("round dispatch: " + mode, plan_id))
            return receipt

    def resume_selected(self, plan_id, leaves):
        """Resume a drained plan with a durable dispatch boundary of at most three leaves."""
        if (not isinstance(leaves, list) or not 1 <= len(leaves) <= 3
            or any(not isinstance(x, str) or not x for x in leaves)
            or len(set(leaves)) != len(leaves)):
            raise FactoryError("selected dispatch requires one to three unique leaves", "full_plan_binding", 409)
        selection = sorted(leaves)
        selection_digest = digest(selection)
        with self.store.connect(True) as con:
            row = con.execute(
                "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
                (plan_id, self.campaign_id),
            ).fetchone()
            if not row:
                raise FactoryError("unknown plan", "not_found", 404)
            latest = con.execute(
                "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='selected_dispatch' ORDER BY id DESC LIMIT 1",
                (plan_id,),
            ).fetchone()
            if row["status"] == "running":
                if latest:
                    prior = json.loads(latest[0])
                    if prior.get("selection_digest") == selection_digest and prior.get("leaves") == selection:
                        return prior["receipt"]
                raise FactoryError("running plan has a different selected dispatch", "full_plan_paused", 409)
            if row["status"] != "paused":
                raise FactoryError("selected dispatch requires a paused plan", "full_plan_paused", 409)
            active = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                (self.campaign_id, row["phase"]),
            ).fetchone()[0]
            if active:
                raise FactoryError("drain active reservations before selected dispatch", "full_plan_paused", 409)
            members = {
                x["slug"]: x["state"]
                for x in con.execute(
                    "SELECT slug,state FROM auxiliary_full_leaf WHERE plan_id=?", (plan_id,)
                )
            }
            if any(x not in members or members[x] not in {"pending", "running", "paused", "needs_revision"} for x in selection):
                raise FactoryError("selected leaf outside dispatchable frozen scope", "full_plan_binding", 409)
            receipt = {
                "full_plan_id": plan_id,
                "leaves": selection,
                "selection_digest": selection_digest,
                "baseline": row["baseline"],
                "max_calls": row["max_calls"],
                "started": row["started"],
                "deadline": row["deadline"],
                "resumed_at": self.clock(),
            }
            con.execute(
                "INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'selected_dispatch',?,?)",
                (plan_id, json.dumps({"leaves": selection, "selection_digest": selection_digest, "receipt": receipt}), self.clock()),
            )
            con.execute(
                "UPDATE auxiliary_full_plan SET status='running',reason='selected dispatch' WHERE id=?",
                (plan_id,),
            )
            return receipt


def full_reservation_locked(
    con, campaign, identity, phase, plan_id, model, stage, now, kind="production", store=None
):
    row = con.execute(
        "SELECT * FROM auxiliary_full_plan WHERE phase=? AND campaign_id=?",
        (str(phase), campaign),
    ).fetchone()
    if not row:
        bound = con.execute(
            "SELECT id FROM auxiliary_full_plan WHERE campaign_id=?", (campaign,)
        ).fetchall()
        if str(phase).startswith("auxiliary-full-") or any(
            plan_id == x[0] or identity.startswith(x[0] + ":") for x in bound
        ):
            raise FactoryError("full plan not registered", "full_plan_binding", 409)
        return None
    if digest(json.loads(row["request_json"])) != row["request_digest"]:
        raise FactoryError(
            "stored full authorization changed", "full_plan_integrity", 409
        )
    effective_model, _ = FullAuxiliaryService._model_revisions(con, plan_id, row)
    if (
        plan_id != row["id"]
        or model != effective_model
        or not identity.startswith(plan_id + ":")
    ):
        raise FactoryError(
            "full plan call identity/model differs", "full_plan_binding", 409
        )
    pilot = con.execute(
        "SELECT * FROM auxiliary_reference_pilot WHERE phase=? AND campaign_id=?",
        (str(phase), campaign),
    ).fetchone()
    if str(stage or "").startswith("reference/"):
        if not pilot:
            raise FactoryError("reference pilot not registered", "full_plan_binding", 409)
        return _reference_pilot_reservation_locked(
            con, campaign, identity, phase, plan_id, model, stage, now, kind, pilot, row, store
        )
    if kind not in {"research", "production", "review"}:
        raise FactoryError(
            "full plan cannot fund application/runtime calls", "full_plan_binding", 409
        )
    slug = identity[len(plan_id) + 1 :]
    selected = con.execute(
        "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='selected_dispatch' ORDER BY id DESC LIMIT 1",
        (plan_id,),
    ).fetchone()
    if selected:
        selection = json.loads(selected[0])
        receipt = selection.get("receipt", {})
        if (digest(selection.get("leaves")) != selection.get("selection_digest")
            or receipt.get("leaves") != selection.get("leaves")
            or receipt.get("selection_digest") != selection.get("selection_digest")):
            raise FactoryError("selected dispatch record changed", "full_plan_integrity", 409)
        if slug not in selection["leaves"]:
            raise FactoryError("leaf outside selected dispatch", "full_plan_paused", 409)
        mode = selection.get("mode", "selected_first_pass")
        if mode in {"pilot_complete", "full_first_round"}:
            req = selection.get("round_request", {})
            if (digest(req) != selection.get("round_request_digest")
                or req.get("mode") != mode or sorted(req.get("leaves", [])) != selection["leaves"]):
                raise FactoryError("round request changed", "full_plan_integrity", 409)
            if mode == "full_first_round" and str(stage).startswith("repair/"):
                raise FactoryError("content repair deferred until round analysis", "budget_round_boundary", 409)
    elif effective_model == REVISED_MODEL:
        raise FactoryError("selected dispatch required before Open Design reservations", "full_plan_paused", 409)
    gate_row = con.execute(
        "SELECT body FROM auxiliary_workflow_gate WHERE plan_id=?", (plan_id,)
    ).fetchone()
    host_revision = con.execute(
        "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='host_revision' ORDER BY id DESC LIMIT 1",
        (plan_id,),
    ).fetchone()
    if (
        host_revision
        and json.loads(host_revision[0])["request"].get("workflow_gate_required")
        and not gate_row
    ):
        raise FactoryError(
            "workflow validation gate not registered", "full_plan_paused", 409
        )
    if gate_row:
        gate = json.loads(gate_row[0])
        if gate["mode"] == "validation" and slug not in gate["leaves"]:
            raise FactoryError(
                "leaf outside fixed workflow validation gate", "full_plan_paused", 409
            )
    leaf = con.execute(
        "SELECT state FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
        (plan_id, slug),
    ).fetchone()
    if (
        not leaf
        or leaf[0] not in {"running", "needs_revision", "paused"}
        or row["status"] != "running"
    ):
        raise FactoryError("full plan/leaf cannot dispatch", "full_plan_paused", 409)
    if not stage or str(stage).split("/", 1)[0] not in {"first", "protocol", "repair"}:
        raise FactoryError("full plan stage lane required", "full_plan_binding", 409)
    parts = str(stage).split("/")
    names = {"discovery", "blueprint-generate-aux", "blueprint-spec-review-aux"}
    if (
        len(parts) != 3
        or parts[1] not in names
        or parts[2] not in {"attempt-1", "attempt-2"}
        or (
            parts[0] == "repair"
            and (parts[1] == "discovery" or parts[2] != "attempt-2")
        )
        or (parts[0] == "first" and parts[2] != "attempt-1")
    ):
        raise FactoryError(
            "full stage outside fixed attempt contract", "full_plan_binding", 409
        )
    calls = [
        dict(x)
        for x in con.execute(
            "SELECT identity,stage,status FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started'",
            (campaign, phase),
        )
    ]
    own = [c for c in calls if c["identity"] == identity]
    if str(stage).startswith("first/") and any(c["stage"] == stage for c in own):
        raise FactoryError(
            "first stage already charged; reuse its checkpoint", "full_uncertain", 409
        )
    if len(own) >= 6:
        raise FactoryError(
            "full leaf allowance exhausted", "budget_leaf_exhausted", 409
        )
    if len(calls) >= row["max_calls"]:
        raise FactoryError(
            "full plan/leaf allowance exhausted", "budget_exhausted", 409
        )
    if str(stage).startswith("protocol/") and any(
        str(c["stage"]).startswith("protocol/") for c in own
    ):
        raise FactoryError(
            "one protocol recovery already used", "budget_retry_limit", 409
        )
    if str(stage).startswith("repair/"):
        scope = str(stage).split("/", 2)[1]
        if any(str(c["stage"]).startswith("repair/" + scope + "/") for c in own):
            raise FactoryError(
                "one content revision per stage", "budget_retry_limit", 409
            )
    if not str(stage).startswith("first/"):
        remaining = 0
        for pending in con.execute(
            "SELECT slug,state FROM auxiliary_full_leaf WHERE plan_id=? AND state IN ('pending','running','paused')",
            (plan_id,),
        ):
            first = sum(
                c["identity"] == plan_id + ":" + pending[0]
                and str(c["stage"]).startswith("first/")
                for c in calls
            )
            remaining += max(0, 3 - first)
        if row["max_calls"] - len(calls) - 1 < remaining:
            raise FactoryError(
                "preserve pending first-pass allowance",
                "budget_first_pass_reserve",
                409,
            )
    if row["deadline"] is not None and now >= row["deadline"]:
        raise FactoryError("full plan deadline exhausted", "budget_deadline", 409)
    if row["started"] is None:
        con.execute(
            "UPDATE auxiliary_full_plan SET started=?,deadline=? WHERE id=?",
            (now, now + row["window_seconds"], plan_id),
        )
    return row


def _reference_pilot_reservation_locked(con, campaign, identity, phase, plan_id,
                                        model, stage, now, kind, pilot, original=None, store=None):
    request = json.loads(pilot["request_json"])
    if digest(request) != pilot["request_digest"]:
        raise FactoryError("stored reference pilot changed", "full_plan_integrity", 409)
    if original is None:
        original = con.execute(
            "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
            (pilot["plan_id"], campaign),
        ).fetchone()
    if (not original or plan_id != original["id"] or model != original["model"]
            or not identity.startswith(original["id"] + ":")):
        raise FactoryError("reference pilot call binding differs", "full_plan_binding", 409)
    if store is not None:
        from .reference_pilot import ReferencePilotService
        service = object.__new__(ReferencePilotService)
        service.store, service.campaign_id = store, campaign
        service.verify_call(con, pilot, request, original)
    if original["status"] != "paused" or pilot["status"] != "active":
        raise FactoryError("reference pilot/full plan is paused", "full_plan_paused", 409)
    later_controls = con.execute(
        "SELECT body FROM auxiliary_full_event WHERE plan_id=? AND kind='control' AND id>? ORDER BY id",
        (original["id"], pilot["pause_anchor"]),
    ).fetchall()
    if any(json.loads(event[0]).get("action") == "pause" for event in later_controls):
        raise FactoryError("full-plan pause after pilot registration revoked pilot calls", "full_plan_paused", 409)
    if kind not in {"research", "production", "review"}:
        raise FactoryError("reference pilot cannot fund this call", "full_plan_binding", 409)
    slug = identity[len(original["id"]) + 1:]
    members = {x["leaf"]: x for x in request["leaves"]}
    if slug not in members:
        raise FactoryError("leaf outside registered reference pilot", "full_plan_binding", 409)
    frozen = con.execute(
        "SELECT state,body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
        (original["id"], slug),
    ).fetchone()
    if not frozen or frozen["state"] != "reused":
        raise FactoryError("reference pilot leaf is not a frozen reused leaf", "full_plan_paused", 409)
    stage_parts = str(stage or "").split("/")
    stage_to_kind = {"research": "research", "author": "production", "review": "review"}
    revision_id = None
    if len(stage_parts) == 4 and stage_parts[0] == "reference" and stage_parts[1] in {"author", "review"}:
        revision_id = stage_parts[3]
        revision = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id DESC",
                               (pilot["id"],)).fetchall()
        registered = False
        for event in revision:
            envelope = json.loads(event[0])
            body = envelope.get("request", {})
            if digest(body) != envelope.get("request_digest"):
                raise FactoryError("reference continuation record changed", "full_plan_integrity", 409)
            if body.get("revision_id") == revision_id and body.get("leaf") == slug:
                registered = True
        if not registered:
            raise FactoryError("reference continuation stage is not registered", "full_plan_binding", 409)
    if (not ((len(stage_parts) == 3 and stage_parts[0] == "reference"
              and stage_parts[1] in stage_to_kind and stage_parts[2] == pilot["id"])
             or (revision_id is not None and stage_parts[2] == pilot["id"]))
            or stage_to_kind.get(stage_parts[1]) != kind):
        raise FactoryError("reference pilot only permits its three first-pass stages", "full_plan_binding", 409)
    calls = con.execute(
        "SELECT identity,stage,status FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started'",
        (campaign, original["phase"]),
    ).fetchall()
    own = [c for c in calls if c["identity"] == identity]
    pilot_calls = [c for c in calls if c["stage"] and c["stage"].startswith("reference/")
                   and (c["stage"].endswith("/" + pilot["id"]) or ("/" + pilot["id"] + "/") in c["stage"])]
    if any(c["stage"] == stage for c in own):
        raise FactoryError("reference stage already charged; reuse checkpoint", "full_uncertain", 409)
    has_events = con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='auxiliary_reference_pilot_event'").fetchone()
    continuation = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id DESC LIMIT 1",
                               (pilot["id"],)).fetchone() if has_events else None
    effective_limit = json.loads(continuation[0]).get("effective_max_calls", pilot["max_calls"]) if continuation else pilot["max_calls"]
    if len(own) >= 6 or len(pilot_calls) >= effective_limit or len(calls) >= original["max_calls"]:
        raise FactoryError("reference pilot allowance exhausted", "budget_exhausted", 409)
    pending_remaining = 0
    for pending in con.execute(
        "SELECT slug FROM auxiliary_full_leaf WHERE plan_id=? AND state IN ('pending','running','paused')",
        (original["id"],),
    ):
        first = sum(c["identity"] == original["id"] + ":" + pending["slug"]
                    and str(c["stage"]).startswith("first/") for c in calls)
        pending_remaining += max(0, 3 - first)
    if original["max_calls"] - len(calls) - 1 < pending_remaining:
        raise FactoryError("preserve pending full-plan first-pass allowance", "budget_first_pass_reserve", 409)
    if original["deadline"] is not None and now >= original["deadline"]:
        raise FactoryError("original full-plan deadline exhausted", "budget_deadline", 409)
    return original
