"""Three fixed leaf/scenario items, existing Go producer, shared durable budget.

No applications, automatic content repair or strict campaign resumption. Each
failed item retains its checkpoint; other items continue. A rerun cannot relaunch
an uncertain/failed paid operation or change the model/inputs of a checkpoint.
"""
import argparse
import fcntl
import hashlib
import json
from pathlib import Path

from produce_batch import ROOT
from produce_with_opencode import CAMPAIGN, fixed_json, run, safe_file
from template_factory.budget import BudgetLedger
from template_factory.store import FactoryStore
from atlas_runtime import atomic_json


def execute(path, api, only=None):
    request = json.loads(path.read_text())
    root = path.parent
    if only and only not in {item["key"] for item in request["items"]}:
        raise ValueError("unknown fixed batch item")
    source = ROOT / request["authorization_ref"]
    if hashlib.sha256(source.read_bytes()).hexdigest() != request["authorization_sha256"]:
        raise ValueError("batch authorization source changed")
    store = FactoryStore(ROOT / "application-atlas-production-pack/atlas/template-factory", ROOT / "application-atlas-production-pack")
    ledger = BudgetLedger(store, campaign_id=CAMPAIGN)
    for item in request["items"]:
        if "/" in safe_file(item["key"]):
            raise ValueError("batch item key must be a single directory")
        store.leaf(item["leaf"])
        raw = (store.pack / "applications" / (item["leaf"] + ".md")).read_bytes()
        if hashlib.sha256(raw).hexdigest() != item["leaf_sha256"]:
            raise ValueError("fixed batch leaf changed")
    registration = ledger.register_auxiliary_batch(request["phase"], request["identity"], request)
    fixed_json(root / "REGISTRATION.json", registration)
    if not (root / "BUDGET_BEFORE.json").exists():
        atomic_json(root / "BUDGET_BEFORE.json", ledger.snapshot())
    outcomes = []
    for item in request["items"]:
        manifest_path = root / (item["key"] + ".manifest.json")
        expected = {"schema": "atlas.auxiliary-go-item.v1", "batch_id": request["phase"], "campaign_id": CAMPAIGN,
                    "model": request["model"], "max_cli_calls": 3, "budget_identity": request["identity"],
                    "prompt_profile": "leaf-scenario-v1", "review_format": 2}
        if manifest_path.exists():
            previous = json.loads(manifest_path.read_text())
            if any(previous.get(k) != v for k, v in expected.items()) or any(previous["items"][0].get(k) != v for k, v in item.items()):
                raise ValueError("batch item manifest binding changed")
        else:
            atomic_json(manifest_path, {**expected, "items": [{**item, "develop_representative": False}]})
        if only and item["key"] != only:
            continue
        try:
            print("START " + item["key"], flush=True)
            result = run(manifest_path, api)
            outcomes.append(result)
        except Exception as error:
            outcomes.append({"key": item["key"], "state": "blocked", "error": str(error)})
            print("BLOCKED " + item["key"] + ": " + str(error), flush=True)
        finally:
            atomic_json(root / "BUDGET_AFTER.json", ledger.snapshot())
            # A focused replay must not erase other items' completed/failed states.
            all_items = []
            for fixed in request["items"]:
                saved = root / (fixed["key"] + ".manifest.json")
                value = json.loads(saved.read_text())["items"][0] if saved.exists() else dict(fixed)
                value.setdefault("state", "pending_or_running")
                all_items.append(value)
            atomic_json(root / "RESULTS.json", {"items": all_items, "model": request["model"], "application_runtime": "not_run"})
    return outcomes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--item")
    parser.add_argument("--api", default="http://127.0.0.1:5199/api/factory/")
    args = parser.parse_args()
    with args.request.parent.joinpath(".producer.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        print(json.dumps(execute(args.request.resolve(), args.api, args.item), ensure_ascii=False, indent=2))
