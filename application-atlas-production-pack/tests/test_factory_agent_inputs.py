"""Byte-faithful input construction, using the archived real frozen review."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.agent_inputs import build_agent_input
from template_factory.cognition import frozen_review_payload
from template_factory.store import digest

REPO = Path(__file__).resolve().parents[2]
ARCHIVE = REPO / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/actual-frozen-review/job_b01427592b164863aab5bedf7b3863bb"
BASELINE = REPO / "docs/template-factory/g1-frozen-review-recovery-2026-10-20/BASELINE.json"

class AgentInputTests(unittest.TestCase):
    def test_original_roundtrip_and_snapshot_reconstruction(self):
        original = (ARCHIVE / "input.json").read_bytes()
        parsed = json.loads(original)
        effective, raw, companion = build_agent_input(parsed)
        self.assertEqual(raw, original)
        self.assertEqual(companion, (ARCHIVE / "leaf.md").read_bytes())
        self.assertEqual(hashlib.sha256(raw).hexdigest(), "394209fae774d75bcf1fa06c4eb091f26c727438836476cb86471c3adbc1d242")
        snapshot = json.loads(BASELINE.read_text())["job"]["snapshot"]
        rebuilt, _, _ = build_agent_input(frozen_review_payload(snapshot, ARCHIVE / "source"))
        self.assertEqual(rebuilt, effective)
        self.assertEqual(digest(effective), "b4061425b435f346cd6b5e19745185ad99bebee3b5a3b983759e28e56ff6b0fa")

    def test_leaf_companion_is_idempotent_and_language_is_distinct(self):
        payload = {"leaf": {"content": "完整\n正文\n"}, "language": "zh"}
        first, raw, companion = build_agent_input(payload)
        self.assertEqual(build_agent_input(first), (first, raw, companion))
        changed, changed_raw, _ = build_agent_input({**first, "language": "en"})
        self.assertNotEqual(raw, changed_raw)
        self.assertNotEqual(digest(first), digest(changed))
        self.assertEqual(digest({k:v for k,v in first.items() if k != "language"}),
                         digest({k:v for k,v in changed.items() if k != "language"}))
        self.assertNotIn("content_file", payload["leaf"])

class LatestRecoveredAcceptanceTests(unittest.TestCase):
    def test_same_job_new_attempt_never_falls_back_to_old_pass(self):
        import sqlite3
        from template_factory.v1_catalog import review_status
        con = sqlite3.connect(':memory:')
        con.row_factory = sqlite3.Row
        con.executescript('''CREATE TABLE job(id TEXT,state TEXT,attempt INTEGER,kind TEXT,snapshot TEXT,created_at TEXT);
                            CREATE TABLE acceptance(job_id TEXT,digest TEXT,body TEXT,created_at TEXT);''')
        con.execute('INSERT INTO job VALUES(?,?,?,?,?,?)',
                    ('job_test','completed',2,'cognitive-review',json.dumps({'artifact_id':'tpl_test','artifact_digest':'digest'}),'2026-10-20'))
        con.execute('INSERT INTO acceptance VALUES(?,?,?,?)',
                    ('job_test','digest',json.dumps({'outcome':'passed','job_attempt':1}),'2026-10-20T01'))
        self.assertEqual(review_status(con,'tpl_test','digest'),'unavailable')
        con.execute('INSERT INTO acceptance VALUES(?,?,?,?)',
                    ('job_test','digest',json.dumps({'outcome':'passed','job_attempt':2}),'2026-10-20T02'))
        self.assertEqual(review_status(con,'tpl_test','digest'),'passed')
        for state in ('queued','running','failed','paused_budget'):
            con.execute('UPDATE job SET state=?',(state,))
            self.assertEqual(review_status(con,'tpl_test','digest'),'unavailable')
        con.close()

class DerivedReadAuthorizationTests(unittest.TestCase):
    def test_unregistered_manifest_cannot_enable_derived_read_permissions(self):
        import tempfile
        from unittest.mock import patch
        from template_factory.cli import CLI
        from template_factory.store import FactoryError
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / 'cognitive-review'
            (directory / 'review-materials').mkdir(parents=True)
            (directory / 'review-materials/manifest.json').write_text('{}')
            with patch('template_factory.cli.initialize_project'), patch('template_factory.cli._detect_major', return_value=2), patch('template_factory.cli.subprocess.Popen') as spawn:
                with self.assertRaises(FactoryError) as error:
                    CLI(executable='fixture-only')._run(directory,'fixture','provider/model',600,lambda:False,lambda _:None)
                self.assertEqual(error.exception.code,'evidence_grant_binding')
                spawn.assert_not_called()
