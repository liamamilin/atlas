"""Durable, append-only workflow progress for an authorized full auxiliary plan."""

import hashlib
import json
import re
import time
from pathlib import Path
from urllib.parse import quote, urlparse

from .store import FactoryError, canonical

STEPS = (
    "existing_template",
    "scenario",
    "case_research",
    "generation",
    "deterministic_check",
    "independent_review",
    "freeze_import",
    "download",
)


class WorkflowService:
    def __init__(
        self, store, campaign_id="atlas-v1-first-production-2026-10-19", clock=time.time
    ):
        self.store, self.campaign_id, self.clock = store, campaign_id, clock
        with store.connect(True) as con:
            con.execute(
                "CREATE TABLE IF NOT EXISTS auxiliary_workflow_step(plan_id TEXT NOT NULL,leaf TEXT NOT NULL,attempt TEXT NOT NULL,step TEXT NOT NULL,state TEXT NOT NULL,input_digest TEXT NOT NULL,body TEXT NOT NULL,updated REAL NOT NULL,PRIMARY KEY(plan_id,leaf,attempt,step))"
            )
            con.execute(
                "CREATE TABLE IF NOT EXISTS auxiliary_workflow_event(id INTEGER PRIMARY KEY AUTOINCREMENT,plan_id TEXT NOT NULL,leaf TEXT,attempt TEXT,step TEXT,kind TEXT NOT NULL,body TEXT NOT NULL,created REAL NOT NULL)"
            )
            con.execute(
                "CREATE TABLE IF NOT EXISTS auxiliary_workflow_gate(plan_id TEXT PRIMARY KEY,body TEXT NOT NULL,updated REAL NOT NULL)"
            )

    def _plan(self, con, plan_id):
        p = con.execute(
            "SELECT * FROM auxiliary_full_plan WHERE id=? AND campaign_id=?",
            (plan_id, self.campaign_id),
        ).fetchone()
        if not p:
            raise FactoryError(
                "full plan not registered for campaign", "not_found", 404
            )
        return p

    def _member(self, con, plan_id, leaf):
        r = con.execute(
            "SELECT body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
            (plan_id, leaf),
        ).fetchone()
        if not r:
            raise FactoryError("leaf is outside frozen plan", "workflow_binding", 409)
        return json.loads(r[0])

    def _attempt(self, attempt):
        if not isinstance(attempt, str) or not re.fullmatch(
            r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}", attempt
        ):
            raise FactoryError("unsafe attempt", "workflow_binding", 409)

    def _event(self, con, plan, leaf, attempt, step, kind, body):
        con.execute(
            "INSERT INTO auxiliary_workflow_event(plan_id,leaf,attempt,step,kind,body,created) VALUES(?,?,?,?,?,?,?)",
            (plan, leaf, attempt, step, kind, canonical(body), self.clock()),
        )

    def begin(self, plan_id, leaf, attempt, step, input_digest):
        self._attempt(attempt)
        if (
            step not in STEPS
            or not isinstance(input_digest, str)
            or not re.fullmatch(r"[a-fA-F0-9]{64}", input_digest)
        ):
            raise FactoryError("invalid workflow step or input digest")
        with self.store.connect(True) as c:
            self._plan(c, plan_id)
            self._member(c, plan_id, leaf)
            row = c.execute(
                "SELECT * FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                (plan_id, leaf, attempt, step),
            ).fetchone()
            if row and row["input_digest"] and row["input_digest"] != input_digest:
                raise FactoryError(
                    "workflow input digest changed", "workflow_integrity", 409
                )
            if row and row["state"] in ("completed", "reused"):
                self._verify_outputs(json.loads(row["body"]).get("outputs", []))
                return False
            n = STEPS.index(step)
            if n and any(
                not (
                    x := c.execute(
                        "SELECT state FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                        (plan_id, leaf, attempt, prev),
                    ).fetchone()
                )
                or x[0] not in ("completed", "reused")
                for prev in STEPS[:n]
            ):
                raise FactoryError(
                    "workflow predecessor is incomplete", "workflow_order", 409
                )
            if not row:
                started = self.clock()
                c.execute(
                    "INSERT INTO auxiliary_workflow_step VALUES(?,?,?,?,?,?,?,?)",
                    (
                        plan_id,
                        leaf,
                        attempt,
                        step,
                        "running",
                        input_digest,
                        canonical({"outputs": [], "started": started}),
                        started,
                    ),
                )
                self._event(
                    c,
                    plan_id,
                    leaf,
                    attempt,
                    step,
                    "started",
                    {"input_digest": input_digest},
                )
            elif row["state"] != "running":
                body = json.loads(row["body"])
                body.setdefault("started", row["updated"])
                body.pop("code", None)
                body.pop("error", None)
                c.execute(
                    "UPDATE auxiliary_workflow_step SET state='running',input_digest=?,body=?,updated=? WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                    (
                        input_digest,
                        canonical(body),
                        self.clock(),
                        plan_id,
                        leaf,
                        attempt,
                        step,
                    ),
                )
                self._event(
                    c,
                    plan_id,
                    leaf,
                    attempt,
                    step,
                    "resumed",
                    {"input_digest": input_digest},
                )
            return True

    def _verify_outputs(self, outputs):
        root = self.store.pack.parent.resolve()
        for o in outputs:
            rel = Path(o["path"])
            if rel.is_absolute() or ".." in rel.parts:
                raise FactoryError(
                    "workflow output path must be repository-relative",
                    "workflow_integrity",
                    409,
                )
            p = (root / rel).resolve()
            if (
                not p.is_relative_to(root)
                or not p.is_file()
                or hashlib.sha256(p.read_bytes()).hexdigest() != o["sha256"]
            ):
                raise FactoryError(
                    "workflow output changed or missing", "workflow_integrity", 409
                )

    def output_file(self, plan_id, leaf, attempt, step, index):
        self._attempt(attempt)
        if (
            step not in STEPS
            or isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
        ):
            raise FactoryError("invalid workflow output index")
        with self.store.connect() as c:
            self._plan(c, plan_id)
            self._member(c, plan_id, leaf)
            row = c.execute(
                "SELECT state,body FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                (plan_id, leaf, attempt, step),
            ).fetchone()
        if not row or row["state"] not in {"completed", "reused"}:
            raise FactoryError("workflow output not found", "not_found", 404)
        outputs = json.loads(row["body"]).get("outputs", [])
        if index >= len(outputs):
            raise FactoryError("workflow output not found", "not_found", 404)
        output = outputs[index]
        self._verify_outputs([output])
        path = (self.store.pack.parent.resolve() / output["path"]).resolve()
        content_type = (
            "text/plain;charset=utf-8"
            if path.suffix.lower() in {".json", ".py", ".md", ".txt"}
            else "application/zip"
            if path.suffix.lower() == ".zip"
            else "application/octet-stream"
        )
        return path, path.name, content_type

    def complete(self, plan_id, leaf, attempt, step, outputs, reused=False):
        self._attempt(attempt)
        if step not in STEPS or not isinstance(outputs, list) or not outputs:
            raise FactoryError("completion requires output evidence")
        checked = []
        root = self.store.pack.parent.resolve()
        for item in outputs:
            if (
                not isinstance(item, dict)
                or not isinstance(item.get("path"), str)
                or not re.fullmatch(r"[a-fA-F0-9]{64}", str(item.get("sha256", "")))
            ):
                raise FactoryError("invalid workflow output")
            rel = Path(item["path"])
            if rel.is_absolute() or ".." in rel.parts:
                raise FactoryError(
                    "workflow output path must be repository-relative",
                    "workflow_integrity",
                    409,
                )
            p = (root / rel).resolve()
            if (
                not p.is_relative_to(root)
                or not p.is_file()
                or hashlib.sha256(p.read_bytes()).hexdigest() != item["sha256"]
            ):
                raise FactoryError(
                    "workflow output path/hash invalid", "workflow_integrity", 409
                )
            o = {"path": item["path"], "sha256": item["sha256"]}
            if "url" in item:
                u = item["url"]
                if not isinstance(u, str):
                    raise FactoryError("invalid output URL")
                parsed = urlparse(u)
                if u.lower().startswith("javascript:") or not (
                    u.startswith(("/api/", "/factory?", "/browse", "/types?"))
                    or (parsed.scheme == "http" and parsed.netloc == "127.0.0.1:5188")
                ):
                    raise FactoryError("invalid output URL")
                o["url"] = u
            checked.append(o)
        with self.store.connect(True) as c:
            self._plan(c, plan_id)
            self._member(c, plan_id, leaf)
            row = c.execute(
                "SELECT * FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                (plan_id, leaf, attempt, step),
            ).fetchone()
            if row and row["state"] in ("completed", "reused"):
                existing = json.loads(row["body"])
                if existing.get("outputs") != checked or existing.get("reused") != bool(
                    reused
                ):
                    raise FactoryError("completion differs", "workflow_integrity", 409)
                return existing
            if not row or row["state"] != "running":
                raise FactoryError(
                    "step must begin before completion", "workflow_order", 409
                )
            body = {
                "outputs": checked,
                "reused": bool(reused),
                "started": json.loads(row["body"]).get("started"),
                "finished": self.clock(),
            }
            state = "reused" if reused else "completed"
            c.execute(
                "UPDATE auxiliary_workflow_step SET state=?,body=?,updated=? WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                (state, canonical(body), self.clock(), plan_id, leaf, attempt, step),
            )
            self._event(c, plan_id, leaf, attempt, step, state, body)
            return body

    def fail(self, plan_id, leaf, attempt, step, code, error, paused=False):
        self._attempt(attempt)
        with self.store.connect(True) as c:
            self._plan(c, plan_id)
            self._member(c, plan_id, leaf)
            row = c.execute(
                "SELECT * FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                (plan_id, leaf, attempt, step),
            ).fetchone()
            if row and row["state"] in ("completed", "reused"):
                return
            state = "paused" if paused else "failed"
            prior = json.loads(row["body"]) if row else {}
            body = {
                **prior,
                "code": str(code),
                "error": str(error),
                "finished": self.clock(),
            }
            if row:
                body.setdefault("started", row["updated"])
            if row:
                c.execute(
                    "UPDATE auxiliary_workflow_step SET state=?,body=?,updated=? WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                    (
                        state,
                        canonical(body),
                        self.clock(),
                        plan_id,
                        leaf,
                        attempt,
                        step,
                    ),
                )
            else:
                c.execute(
                    "INSERT INTO auxiliary_workflow_step VALUES(?,?,?,?,?,?,?,?)",
                    (
                        plan_id,
                        leaf,
                        attempt,
                        step,
                        state,
                        "",
                        canonical(body),
                        self.clock(),
                    ),
                )
            self._event(c, plan_id, leaf, attempt, step, state, body)

    def gate(self, plan_id):
        with self.store.connect() as c:
            self._plan(c, plan_id)
            r = c.execute(
                "SELECT body FROM auxiliary_workflow_gate WHERE plan_id=?", (plan_id,)
            ).fetchone()
            return json.loads(r[0]) if r else None

    def _active(self, c, phase):
        return c.execute(
            "SELECT count(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status IN ('reserved','spawn_intent','started','uncertain')",
            (self.campaign_id, phase),
        ).fetchone()[0]

    def set_validation(self, plan_id, leaves):
        if (
            not isinstance(leaves, list)
            or not 1 <= len(leaves) <= 5
            or len(set(leaves)) != len(leaves)
        ):
            raise FactoryError("validation gate requires 1..5 unique leaves")
        with self.store.connect(True) as c:
            p = self._plan(c, plan_id)
            if p["status"] != "paused" or self._active(c, p["phase"]):
                raise FactoryError(
                    "validation gate requires paused plan and no active calls",
                    "workflow_gate",
                    409,
                )
            for leaf in leaves:
                self._member(c, plan_id, leaf)
            initial_states = {}
            for leaf in leaves:
                initial_states[leaf] = c.execute(
                    "SELECT state FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                    (plan_id, leaf),
                ).fetchone()[0]
            value = {
                "mode": "validation",
                "status": "ready",
                "leaves": leaves,
                "created_at": self.clock(),
                "initial_states": initial_states,
            }
            old = c.execute(
                "SELECT body FROM auxiliary_workflow_gate WHERE plan_id=?", (plan_id,)
            ).fetchone()
            if old:
                prior = json.loads(old[0])
                if prior.get("leaves") != leaves or prior.get("mode") != "validation":
                    raise FactoryError("gate leaves immutable", "workflow_gate", 409)
                return prior
            c.execute(
                "INSERT INTO auxiliary_workflow_gate VALUES(?,?,?)",
                (plan_id, canonical(value), self.clock()),
            )
            self._event(c, plan_id, None, None, None, "validation_gate_set", value)
            return value

    def set_gate_passed(self, plan_id, evidence):
        keys = {
            "kind": "atlas.auxiliary-workflow-validation.v1",
            "static_checks_passed": True,
            "replay_new_calls": 0,
            "resume_verified": True,
            "failed_leaf_isolated": True,
        }
        if (
            not isinstance(evidence, dict)
            or any(evidence.get(k) != v for k, v in keys.items())
            or not evidence.get("fresh_ready_leaves")
        ):
            raise FactoryError("validation evidence incomplete", "workflow_gate", 409)
        with self.store.connect(True) as c:
            p = self._plan(c, plan_id)
            row = c.execute(
                "SELECT body FROM auxiliary_workflow_gate WHERE plan_id=?", (plan_id,)
            ).fetchone()
            if p["status"] != "paused" or self._active(c, p["phase"]) or not row:
                raise FactoryError(
                    "paused validation gate with zero calls required",
                    "workflow_gate",
                    409,
                )
            g = json.loads(row[0])
            fresh = evidence["fresh_ready_leaves"]
            if g.get("mode") != "validation":
                raise FactoryError(
                    "validation gate mode required", "workflow_gate", 409
                )
            already_passed = g.get("status") == "passed"
            if already_passed and g.get("evidence") != evidence:
                raise FactoryError(
                    "passed gate evidence is immutable", "workflow_gate", 409
                )
            if (
                not isinstance(fresh, list)
                or not fresh
                or any(x not in g["leaves"] for x in fresh)
            ):
                raise FactoryError(
                    "fresh leaves outside validation gate", "workflow_gate", 409
                )
            for leaf in fresh:
                if g.get("initial_states", {}).get(leaf) in {"ready_not_run", "reused"}:
                    raise FactoryError(
                        "previously ready leaf cannot prove fresh validation",
                        "workflow_gate",
                        409,
                    )
                leafrow = c.execute(
                    "SELECT state FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                    (plan_id, leaf),
                ).fetchone()
                if not leafrow or leafrow[0] != "ready_not_run":
                    raise FactoryError(
                        "fresh leaf is not ready_not_run", "workflow_gate", 409
                    )
                rows = c.execute(
                    "SELECT * FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? ORDER BY updated DESC",
                    (plan_id, leaf),
                ).fetchall()
                by_step = {}
                for step_row in rows:
                    by_step.setdefault(step_row["step"], step_row)
                download = by_step.get("download")
                if not download or download["state"] != "completed":
                    raise FactoryError(
                        "fresh download must be completed in the current attempt",
                        "workflow_gate",
                        409,
                    )
                attempt = download["attempt"]
                latest_attempt = (
                    max(rows, key=lambda item: item["updated"])["attempt"]
                    if rows
                    else None
                )
                if attempt != latest_attempt:
                    raise FactoryError(
                        "download is not from current attempt", "workflow_gate", 409
                    )
                for step_name in STEPS:
                    step_row = c.execute(
                        "SELECT * FROM auxiliary_workflow_step WHERE plan_id=? AND leaf=? AND attempt=? AND step=?",
                        (plan_id, leaf, attempt, step_name),
                    ).fetchone()
                    if not step_row or step_row["state"] not in {"completed", "reused"}:
                        raise FactoryError(
                            "fresh attempt is missing a completed workflow step",
                            "workflow_gate",
                            409,
                        )
                    body = json.loads(step_row["body"])
                    if (
                        not body.get("outputs")
                        or body.get("finished") is None
                        or body["finished"] < g["created_at"]
                    ):
                        raise FactoryError(
                            "fresh workflow step lacks post-gate output evidence",
                            "workflow_gate",
                            409,
                        )
                    self._verify_outputs(body["outputs"])
            if already_passed:
                return g
            g.update(status="passed", evidence=evidence)
            c.execute(
                "UPDATE auxiliary_workflow_gate SET body=?,updated=? WHERE plan_id=?",
                (canonical(g), self.clock(), plan_id),
            )
            self._event(
                c, plan_id, None, None, None, "validation_gate_passed", evidence
            )
            return g

    def open_full(self, plan_id):
        with self.store.connect(True) as c:
            self._plan(c, plan_id)
            r = c.execute(
                "SELECT body FROM auxiliary_workflow_gate WHERE plan_id=?", (plan_id,)
            ).fetchone()
            if not r:
                raise FactoryError("gate missing", "workflow_gate", 409)
            g = json.loads(r[0])
            if g["status"] != "passed":
                raise FactoryError("gate not passed", "workflow_gate", 409)
            plan = self._plan(c, plan_id)
            if plan["status"] != "paused" or self._active(c, plan["phase"]):
                raise FactoryError(
                    "opening full mode requires paused plan and zero active calls",
                    "workflow_gate",
                    409,
                )
            if g["mode"] == "full":
                return g
            g["mode"] = "full"
            c.execute(
                "UPDATE auxiliary_workflow_gate SET body=?,updated=? WHERE plan_id=?",
                (canonical(g), self.clock(), plan_id),
            )
            self._event(c, plan_id, None, None, None, "full_mode_opened", {})
            return g

    def list_plans(self):
        from .full_auxiliary import ensure_schema

        with self.store.connect(True) as c:
            ensure_schema(c)
            ids = [
                r[0]
                for r in c.execute(
                    "SELECT id FROM auxiliary_full_plan WHERE campaign_id=? ORDER BY created DESC",
                    (self.campaign_id,),
                )
            ]
        return {"plans": [self._summary(x) for x in ids]}

    def _summary(self, plan_id):
        from .full_auxiliary import FullAuxiliaryService

        status = FullAuxiliaryService(self.store, self.campaign_id, self.clock).status(
            plan_id
        )
        return {k: v for k, v in status.items() if k not in ("items", "calls")} | {
            "gate": self.gate(plan_id)
        }

    def detail(self, plan_id, offset=0, limit=20, state="", q=""):
        if (
            isinstance(offset, bool)
            or not isinstance(offset, int)
            or offset < 0
            or isinstance(limit, bool)
            or not isinstance(limit, int)
            or not 1 <= limit <= 100
        ):
            raise FactoryError("invalid pagination")
        from .full_auxiliary import FullAuxiliaryService

        full = FullAuxiliaryService(self.store, self.campaign_id, self.clock).status(
            plan_id
        )
        summary = self._summary(plan_id)
        with self.store.connect() as c:
            rows = c.execute(
                "SELECT * FROM auxiliary_workflow_step WHERE plan_id=? ORDER BY updated",
                (plan_id,),
            ).fetchall()
        filtered = [
            x
            for x in full["items"]
            if (not state or x["state"] == state)
            and (
                not q
                or q.casefold()
                in (x["leaf"] + " " + str(x.get("display_name", ""))).casefold()
            )
        ]
        byleaf = {}
        for r in rows:
            byleaf.setdefault(r["leaf"], {}).setdefault(r["attempt"], {})[r["step"]] = {
                **json.loads(r["body"]),
                "state": r["state"],
                "input_digest": r["input_digest"],
                "updated": r["updated"],
            }
        items = []
        for x in filtered[offset : offset + limit]:
            attempts = byleaf.get(x["leaf"], {})
            latest = (
                max(
                    attempts,
                    key=lambda a: max(
                        (v.get("updated", 0) for v in attempts[a].values()), default=0
                    ),
                )
                if attempts
                else None
            )
            latest_steps = attempts[latest] if latest else {}
            step_list = []
            for name in STEPS:
                data = latest_steps.get(
                    name, {"state": "pending", "input_digest": None, "outputs": []}
                )
                rowout = {
                    "step": name,
                    "attempt": latest,
                    "state": data.get("state", "pending"),
                    "input_digest": data.get("input_digest"),
                    "outputs": data.get("outputs", []),
                }
                if rowout["state"] in {"completed", "reused"}:
                    for output_index, output in enumerate(rowout["outputs"]):
                        if not output.get("url"):
                            output["url"] = (
                                f"/api/factory/auxiliary-workflows/{quote(str(plan_id), safe='')}/leaves/{quote(str(x['leaf']), safe='')}/steps/{quote(str(latest), safe='')}/{quote(name, safe='')}/outputs/{output_index}"
                            )
                for key in ("code", "error", "started", "finished"):
                    if key in data:
                        rowout[key] = data[key]
                step_list.append(rowout)
            identity = plan_id + ":" + x["leaf"]
            calls = [call for call in full["calls"] if call["identity"] == identity]
            items.append({**x, "steps": step_list, "calls": calls})
        return {
            "plan": summary,
            "items": items,
            "pagination": {"offset": offset, "limit": limit, "total": len(filtered)},
        }
