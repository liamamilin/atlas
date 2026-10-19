"""V1 shared evidence and fixed batch API; no direct state override endpoints."""
from __future__ import annotations

import json
import re
from urllib.parse import parse_qs

from .cases import CaseLibrary
from .store import FactoryError
from .v1_batches import BatchService, select_case_basis


def dispatch_v1(method, route, query, body, store):
    from .worker import ensure_worker
    library = CaseLibrary(store)
    params = parse_qs(query)
    if method == "GET" and route == "applications":
        return library.list_apps(), 200
    if method == "GET" and route == "cases":
        return library.list_cases(app_id=params.get("app_id", [None])[0], scenario_id=params.get("scenario_id", [None])[0]), 200
    match = re.fullmatch(r"cases/([A-Za-z0-9:_-]+)/revisions/([1-9][0-9]*)", route)
    if method == "GET" and match:
        case = library.get_case(match[1], int(match[2]))
        templates = [a for a in store.artifacts() if any(r["case_id"] == case["case_id"] and r["revision"] == case["revision"] for r in a.get("provenance", {}).get("case_basis", {}).get("case_refs", []))]
        return {**case, "fixed_reference": library.case_ref(case["case_id"], case["revision"]), "templates": templates}, 200
    if method == "GET" and route == "case-reference":
        return library.resolve_case_ref(params.get("ref", [""])[0], params.get("digest", [None])[0]), 200
    match = re.fullmatch(r"scenarios/(scn_[a-f0-9]{32})/basis", route)
    if method == "GET" and match:
        scene = store.scenario(match[1])
        cases = library.list_cases(scenario_id=scene["id"])
        basis, blockers = select_case_basis(store, scene["id"], scene["revision"])
        if not basis:
            blockers.append({"code": "case_research_required", "reason": "No reviewed fixed-source case for this scenario revision."})
        artifacts = [a for a in store.artifacts() if a.get("scenario_id") == scene["id"] and a.get("scenario_revision") == scene["revision"]]
        stage = "published" if any(a["state"] == "published" for a in artifacts) else "template_review" if artifacts else "template_input_ready" if basis and not blockers else "case_research"
        return {"scenario_id": scene["id"], "revision": scene["revision"], "cases": cases, "case_basis": basis, "blockers": blockers, "stage": stage, "artifacts": artifacts}, 200
    service = BatchService(store)
    if method == "POST" and route == "plans/preview":
        return service.preview(body), 201
    match = re.fullmatch(r"plans/(plan_[a-f0-9]{32})(?:/(run|report|pause|resume|cancel))?", route)
    if match:
        pid, action = match[1], match[2]
        if method == "GET" and not action:
            return service.plan(pid), 200
        if method == "GET" and action == "report":
            result = service.report(pid)
            if result["batch"] and result["batch"]["state"] in {"running", "paused"}:
                if result["batch"]["state"] == "running":
                    ensure_worker(store)
            return result, 200
        if method == "POST" and action == "run":
            result = service.run(pid, body)
            ensure_worker(store)
            return result, 202
        if method == "POST" and action in {"pause", "resume", "cancel"}:
            result = service.action(pid, action)
            if action == "resume":
                ensure_worker(store)
            return result, 200
    if method == "GET" and route == "gates":
        with store.connect() as con:
            campaign_id = params.get("campaign_id", [None])[0]
            rows = con.execute("SELECT body FROM v1_campaign_gate WHERE campaign_id=?", (campaign_id,)) if campaign_id else con.execute("SELECT body FROM v1_campaign_gate ORDER BY created_at DESC")
            return [json.loads(r[0]) for r in rows], 200
    raise FactoryError("V1 route not found", "not_found", 404)
