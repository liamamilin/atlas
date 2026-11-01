import copy
import json
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import full_audit as audit
from audit_ledger import Ledger, CAP, MICRO, charges, reservation


class AuditSafeguards(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.stack = ExitStack()
        self.stack.enter_context(patch.object(audit, "STATE_DB", self.root / "audit.sqlite"))
        self.stack.enter_context(patch.object(audit, "DATA", self.root / "data"))
        self.stack.enter_context(patch.object(audit, "DOC", self.root / "docs"))
        audit.DATA.mkdir()
        audit.DOC.mkdir()
        self.ledger = Ledger(audit.STATE_DB)
        self.payload = {"card": {"repository_id": 1}, "sources": [{"id": "s0", "kind": "readme", "text": "Planned feature. Existing README capability."}], "scenario_matches": [], "coverage": {"files_included": 1}}
        self.review = {"repository_id": 1, "verdict": "pass", "summary": "Source-based check complete", "checks": {k:"supported" for k in ("facts","project_type","license_label","scenario_matches")}, "issues": [], "limitations": []}
        self.add_projects(range(1, 101))

    def tearDown(self):
        self.stack.close()
        self.tmp.cleanup()

    def add_projects(self, ids):
        with self.ledger.connect() as con:
            con.executemany("INSERT OR IGNORE INTO projects(rid,full_name,data_sha,domain) VALUES(?,?,?,?)", [(i, "public/project"+str(i), "sha", "domain") for i in ids])

    def runner(self):
        return audit.Runner({"limits": []})

    def test_concurrent_reservations_never_exceed_cap(self):
        with ThreadPoolExecutor(max_workers=12) as pool:
            keys=list(pool.map(lambda rid: self.ledger.reserve(rid,"primary","openai","gpt-6-luna",MICRO,"now","payload","prompt"), range(1,101)))
        self.assertEqual(sum(k is not None for k in keys),50)
        with self.ledger.connect() as con:
            balance=self.ledger.balance(con)
        self.assertEqual(balance["reserved_micro"],CAP)
        self.assertEqual(balance["available_micro"],0)

    def test_unknown_billing_survives_crash_and_duplicate_claim_is_denied(self):
        key=self.ledger.reserve(1,"primary","openai","gpt-6-luna",10000,"now","p","q")
        self.assertIsNone(self.ledger.reserve(1,"primary","openai","gpt-6-luna",10000,"now","p","q"))
        self.ledger.recover_inflight()
        with self.ledger.connect() as con:
            self.assertEqual(self.ledger.balance(con)["reserved_micro"],10000)
            self.assertEqual(con.execute("SELECT state FROM requests WHERE id=?",(key,)).fetchone()[0],"uncertain")
            self.assertEqual(con.execute("SELECT primary_status FROM projects WHERE rid=1").fetchone()[0],"pending")
        self.ledger.recover_inflight()
        with self.ledger.connect() as con:
            self.assertEqual(self.ledger.balance(con)["reserved_micro"],10000)

    def test_historical_receipt_cannot_be_charged_twice(self):
        receipt={"usage":{"prompt_tokens":4000,"completion_tokens":400}}
        for _ in range(2):
            self.ledger.import_receipt(1,"primary","openai","gpt-6-luna",self.root/"old.json",receipt,"then")
        with self.ledger.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM requests").fetchone()[0],1)
            self.assertEqual(self.ledger.balance(con)["charged_upper_micro"],700)

    def test_cost_reserves_peak_and_accounts_for_provider_bill(self):
        usage={"prompt_tokens":4000,"prompt_cache_hit_tokens":1000,"completion_tokens":400,"cost":0.002}
        estimate,upper=charges(usage,"opencode-go",False)
        self.assertEqual(estimate,2000)
        self.assertEqual(upper,2000)
        estimate,upper=charges({k:v for k,v in usage.items() if k!="cost"},"opencode-go",False)
        self.assertGreater(upper,estimate)
        body={"messages":[{"content":"长文字"*1000}]}
        self.assertGreater(reservation(body,"opencode-go"),upper)
        self.assertIsNone(charges({},"openai"))

    def test_confirmed_without_official_evidence_stays_unresolved(self):
        payload={**self.payload,"primary_findings":[{"finding_id":"issue-0"}]}
        review={"repository_id":1,"adjudications":[{"finding_id":"issue-0","disposition":"confirmed","source_id":"s0","quote":"invented proof"}]}
        result=audit.secondary_validation(review,payload)
        self.assertEqual(result["adjudications"][0]["disposition"],"unresolved")
        result["adjudications"][0].update(disposition="confirmed",quote="Planned feature.")
        self.assertEqual(audit.secondary_validation(result,payload)["adjudications"][0]["disposition"],"confirmed")
        with self.assertRaises(ValueError):
            audit.secondary_validation({"repository_id":1,"adjudications":[]},payload)

    def test_balance_receipt_releases_only_measured_peak_allowance(self):
        usage={"prompt_tokens":4000,"completion_tokens":400,"cost":0.0007201,
               "opencode":{"billing_source":"balance","list_cost":0.0007201}}
        self.assertEqual(charges(usage,"opencode-go",True),(721,721))
        usage["cost"]=usage["opencode"]["list_cost"]=0
        self.assertEqual(charges(usage,"opencode-go"),(0,0))
        usage["opencode"]["billing_source"]="subscription"
        self.assertEqual(charges(usage,"opencode-go")[1],1680)
        usage["opencode"]={"billing_source":"balance","list_cost":1}
        self.assertEqual(charges(usage,"opencode-go")[1],1680)
        usage["cost"]=float("nan")
        self.assertEqual(charges(usage,"opencode-go")[1],1680)
        usage.update(cost=0,opencode=["malformed"])
        self.assertEqual(charges(usage,"opencode-go")[1],1680)

    def test_cache_write_pricing_replaces_input_and_respects_long_context(self):
        usage={"prompt_tokens":12000,"completion_tokens":400,
               "prompt_tokens_details":{"cached_tokens":4000,"cache_write_tokens":7000}}
        self.assertEqual(charges(usage,"openai"),(1215,1700))
        usage={"prompt_tokens":300000,"completion_tokens":400,
               "prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":300000}}
        self.assertEqual(charges(usage,"openai"),(75300,75300))
        usage["prompt_tokens_details"]["cache_write_tokens"]=300001
        self.assertIsNone(charges(usage,"openai"))
        usage["prompt_tokens_details"]["cache_write_tokens"]=True
        self.assertIsNone(charges(usage,"openai"))

    def test_measured_settlement_keeps_other_unknown_reservations(self):
        unknown=self.ledger.reserve(1,"primary","openai","gpt-6-luna",10000,"now","p","q")
        self.ledger.settle(unknown,{"error_code":"timeout"},None,"now")
        key=self.ledger.reserve(2,"secondary","opencode-go","deepseek-v4.1-flash",10000,"now","p","q")
        # Secondary defaults to none, so make the test project eligible first.
        self.assertIsNone(key)
        with self.ledger.connect() as con:
            con.execute("UPDATE projects SET secondary_status='pending' WHERE rid=2")
        key=self.ledger.reserve(2,"secondary","opencode-go","deepseek-v4.1-flash",10000,"now","p","q")
        usage={"prompt_tokens":4000,"completion_tokens":400,"cost":0.00072,
               "opencode":{"billing_source":"balance","list_cost":0.00072}}
        self.ledger.settle(key,{"usage":usage},charges(usage,"opencode-go"),"now")
        with self.ledger.connect() as con:
            balance=self.ledger.balance(con)
            self.assertEqual(balance["reserved_micro"],10000)
            self.assertEqual(balance["charged_upper_micro"],720)
            self.assertEqual(con.execute("SELECT state FROM requests WHERE id=?",(unknown,)).fetchone()[0],"uncertain")

    def test_labeled_missing_sources_are_limits_not_model_failure(self):
        runner=self.runner()
        with self.ledger.connect() as con:
            con.execute("UPDATE projects SET coverage=? WHERE rid=1",(json.dumps({"files_included":0}),))
        runner.save_review(1,"primary",self.review)
        with self.ledger.connect() as con:
            row=con.execute("SELECT outcome,secondary_status FROM projects WHERE rid=1").fetchone()
        self.assertEqual(tuple(row),("pass_with_limits","none"))

    def test_paid_receipt_is_recovered_without_another_request(self):
        payload_sha=audit.core.digest(audit.core.canonical(self.payload))
        prompt_sha=audit.core.digest(audit.PRIMARY_PROMPT)
        key=self.ledger.reserve(1,"primary","openai","gpt-6-luna",10000,"now",payload_sha,prompt_sha)
        receipt={"text":json.dumps(self.review),"finish_reason":"stop"}
        self.ledger.settle(key,receipt,(700,700),"now")
        self.ledger.recover_inflight()
        with patch.object(audit,"build_payload",return_value=(self.payload,"file-sha")), patch.object(audit.core.atlas_model,"resolve",side_effect=AssertionError("no credentials or network needed")):
            runner=self.runner()
            self.assertEqual(runner.execute(1,"primary"),"recovered_receipt")
        with self.ledger.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM requests").fetchone()[0],1)
            self.assertEqual(con.execute("SELECT primary_status FROM projects WHERE rid=1").fetchone()[0],"done")

    def test_paid_response_and_focused_review_use_same_four_slot_dispatcher(self):
        runner=self.runner()
        with self.ledger.connect() as con:
            con.execute("DELETE FROM projects WHERE rid>4")
        def payload(rid,stage):
            value=copy.deepcopy(self.payload)
            value["card"]["repository_id"]=rid
            return value
        def send(body,provider,model):
            value=json.loads(body["messages"][1]["content"])
            review={**self.review,"repository_id":value["card"]["repository_id"]}
            return {"model":model,"usage":{"prompt_tokens":4000,"completion_tokens":400},"choices":[{"finish_reason":"stop","message":{"content":json.dumps(review)}}]}
        with patch.object(runner,"payload",side_effect=payload),patch.object(runner,"send",side_effect=send),patch.object(audit.core.atlas_model,"resolve",return_value={"base_url":"https://api.openai.com/v1"}):
            with self.ledger.connect() as con:
                con.execute("UPDATE projects SET coverage=?",(json.dumps({"files_included":1}),))
            runner.run(max_primary=4,max_secondary=0)
        self.assertEqual(runner.status,"checkpoint_test_complete")
        with self.ledger.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM projects WHERE primary_status='done'").fetchone()[0],4)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM requests WHERE state='settled'").fetchone()[0],4)
            self.assertGreater(self.ledger.balance(con)["available_micro"],0)


if __name__=="__main__":
    unittest.main()
