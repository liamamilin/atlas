"""Scoped full-leaf authorization and durable operator state, never a G1 grant."""

import hashlib
import json
import time

from .store import FactoryError, digest

MODEL = "opencode-go/minimax-m3.1-flash-free"


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
            grant = json.loads(plan["request_json"])
            root = (self.store.pack.parent / grant["scope"]["path"]).parent.resolve()
            expected = root / "items" / leaf / work_name / "calls"
            if path.parent != expected or not (path / "LAUNCH_INTENT.json").exists():
                raise FactoryError("recovery path differs", "full_plan_binding", 409)
            row = json.loads(member["body"])
            binding = json.loads((path / "BINDING.json").read_text())
            if (
                binding["model"] != plan["model"]
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
                "directory": str(path.relative_to(self.store.pack.parent)),
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
                "requested_model": plan["model"],
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
                    not name.startswith(
                        (
                            "application-atlas-production-pack/template_factory/",
                            "examples/assisted-trials/",
                        )
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


def full_reservation_locked(
    con, campaign, identity, phase, plan_id, model, stage, now, kind="production"
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
    if (
        plan_id != row["id"]
        or model != row["model"]
        or not identity.startswith(plan_id + ":")
    ):
        raise FactoryError(
            "full plan call identity/model differs", "full_plan_binding", 409
        )
    if kind not in {"research", "production", "review"}:
        raise FactoryError(
            "full plan cannot fund application/runtime calls", "full_plan_binding", 409
        )
    slug = identity[len(plan_id) + 1 :]
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
