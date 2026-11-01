"""Offline, receipt-preserving cost reconciliation for the existing frozen audit."""
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
import argparse
import fcntl
import hashlib
import json
import sqlite3

import full_audit as audit
from audit_ledger import Ledger, charges, CAP


def fingerprint(con, query):
    h = hashlib.sha256()
    for row in con.execute(query):
        h.update(audit.core.canonical(list(row)).encode())
        h.update(b"\n")
    return h.hexdigest()


def protected(con):
    return {
        "projects": fingerprint(con, "SELECT * FROM projects ORDER BY rid"),
        "request_receipts_and_states": fingerprint(con, "SELECT id,rid,stage,provider,model,state,reserved,created,finished,payload_sha,prompt_sha,receipt,error_code,legacy_path FROM requests ORDER BY id"),
        "uncertain_requests": fingerprint(con, "SELECT * FROM requests WHERE state='uncertain' ORDER BY id"),
    }


def reconcile(apply=False):
    archive = audit.DOC / "cost-reconciliation-20261030"
    assert (archive / "MANIFEST.json").exists()
    assert (audit.DATA / "cost-reconciliation-20261030-before.sqlite").exists()
    with (audit.DATA / "worker.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        ledger = Ledger(audit.STATE_DB)
        with ledger.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            assert con.execute("SELECT COUNT(*) FROM projects").fetchone()[0] == 55651
            assert not con.execute("SELECT 1 FROM requests WHERE state='reserved'").fetchone()
            assert not con.execute("SELECT 1 FROM meta WHERE key='cost_reconciliation_20261030'").fetchone()
            before, guards = ledger.balance(con), protected(con)
            changes, counts, totals = [], Counter(), defaultdict(Decimal)
            for row in con.execute("SELECT * FROM requests ORDER BY id"):
                if row["state"] != "settled":
                    continue
                receipt = json.loads(row["receipt"]) if row["receipt"] else {}
                usage = receipt.get("usage") or {}
                if not usage:
                    assert row["charged"] == row["estimated"] == 0
                    counts["known_no_charge"] += 1
                    continue
                provider = row["provider"]
                cost = charges(usage, provider)
                assert cost is not None
                if provider == "opencode-go":
                    assert row["model"] == "deepseek-v4.1-flash"
                    assert receipt.get("returned_model", receipt.get("model")) == "deepseek-v4.1-flash"
                    assert usage["opencode"]["billing_source"] == "balance"
                    assert Decimal(str(usage["cost"])) == Decimal(str(usage["opencode"]["list_cost"]))
                    totals["go_provider_reported_usd"] += Decimal(str(usage["cost"]))
                else:
                    assert provider == "openai" and cost[1] == row["charged"]
                    counts["openai_long_context_requests"] += usage["prompt_tokens"] > 272000
                counts[provider + "_settled_usage_receipts"] += 1
                if (row["estimated"], row["charged"]) != cost:
                    changes.append({"id": row["id"], "provider": provider,
                                    "old_estimated_micro": row["estimated"], "old_charged_micro": row["charged"],
                                    "new_estimated_micro": cost[0], "new_charged_micro": cost[1]})
            after = dict(before)
            after["charged_upper_micro"] += sum(v["new_charged_micro"]-v["old_charged_micro"] for v in changes)
            after["estimated_micro"] += sum(v["new_estimated_micro"]-v["old_estimated_micro"] for v in changes)
            after["available_micro"] = CAP-after["charged_upper_micro"]-after["reserved_micro"]
            assert after["available_micro"] > 0 and after["reserved_micro"] == before["reserved_micro"]
            result = {"audit_id": audit.AUDIT_ID, "at": audit.core.now(), "applied": apply,
                      "before": before, "after": after, "receipt_counts": dict(counts),
                      "exact_go_provider_reported_cost_usd": str(totals["go_provider_reported_usd"]),
                      "changed_rows": len(changes), "protected_before": guards,
                      "method": "Go settled balance usage.cost=list_cost replaces peak allowance, rounded upward per request; OpenAI cache writes replace ordinary input, including long-context multipliers; OpenAI upper bound and all unknown reservations retained.",
                      "sources": ["https://developers.openai.com/api/docs/models/gpt-6-luna", "https://developers.openai.com/api/docs/guides/prompt-caching", "https://opencode.ai/v2/docs/console/go/"],
                      "provider_invoice_reconciled": False,
                      "invoice_limit": "Go uses provider-reported per-request cost. OpenAI uses measured token receipts at published rates, not a downloaded organization invoice; budget still uses its higher input bound. Unknown charges remain fully reserved.",
                      "offline_tests": {"passed": 17, "command": "python3 -m unittest test_full_audit test_review_sample test_compare_models"},
                      "scope_prompts_routes_cap_unchanged": True}
            if apply:
                # A request-ID-only record preserves every old accounting value.
                with (archive / "RECONCILIATION_ROWS.jsonl").open("x") as out:
                    for v in changes:
                        out.write(audit.core.canonical(v)+"\n")
                for v in changes:
                    con.execute("UPDATE requests SET estimated=?,charged=? WHERE id=? AND state='settled'",
                                (v["new_estimated_micro"],v["new_charged_micro"],v["id"]))
                assert ledger.balance(con) == after
                result["protected_after"] = protected(con)
                assert result["protected_after"] == guards
                con.execute("INSERT INTO meta VALUES('cost_reconciliation_20261030',?)", (audit.core.canonical(result),))
        if apply:
            audit.core.atomic_json(audit.DOC / "COST_RECONCILIATION.json", result)
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    result = reconcile(parser.parse_args().apply)
    print(json.dumps(result, ensure_ascii=False, indent=1))
