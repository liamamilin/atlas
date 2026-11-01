from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import semantic_followup as s


class CompletionGuard(unittest.TestCase):
    def test_incomplete_scope_cannot_be_finalized(self):
        with patch.object(s,'summarize',return_value={'remaining':1,'reviewed':7122}):
            with self.assertRaisesRegex(AssertionError,'not_complete'):s.finalize()

    def test_readless_decision_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'READ_LOG.jsonl').write_text('')
            path=root/'commit.json';s.t.audit.core.atomic_json(path,[{'id':'1:issue-0','view_sha256':'not-read'}])
            with patch.object(s,'ROOT',root),patch.object(s,'scope',return_value=({'finding_ids':['1:issue-0']},[])),patch.object(s,'records',return_value={'1:issue-0':{}}):
                with self.assertRaises(AssertionError):s.commit(path)

    def test_out_of_scope_decision_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);path=root/'commit.json';s.t.audit.core.atomic_json(path,[{'id':'2:issue-0'}])
            with patch.object(s,'ROOT',root),patch.object(s,'scope',return_value=({'finding_ids':['1:issue-0']},[])):
                with self.assertRaises(AssertionError):s.commit(path)

    def test_same_finding_cannot_be_counted_twice(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);path=root/'commit.json';s.t.audit.core.atomic_json(path,[{'id':'1:issue-0'}])
            (root/'DECISIONS.jsonl').write_text('{"id":"1:issue-0"}\n')
            with patch.object(s,'ROOT',root),patch.object(s,'scope',return_value=({'finding_ids':['1:issue-0']},[])):
                with self.assertRaises(AssertionError):s.commit(path)


if __name__=='__main__':unittest.main()
