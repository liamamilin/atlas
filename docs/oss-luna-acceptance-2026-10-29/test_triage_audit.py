import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import triage_audit as triage


class EvidenceBoundaries(unittest.TestCase):
    def test_quotes_relax_whitespace_only(self):
        text="Heading\nUse [a+b]  in\nproduction."
        q="Use [a+b] in production."
        value=triage.locate(text,q)
        self.assertEqual(value['state'],'whitespace_equivalent')
        self.assertEqual(value['line'],2)
        self.assertEqual(triage.locate(text,"use [a+b] in production.")['state'],'not_found')
        self.assertEqual(triage.locate(text,"Use [a+b] in production!")['state'],'not_found')

    def test_omission_marker_is_never_evidence(self):
        self.assertEqual(triage.locate('[ARCHIVE TEXT OMITTED]','[ARCHIVE TEXT OMITTED]')['state'],'non_source_marker')
        self.assertEqual(triage.locate('abc','')['state'],'no_quote')

    def record(self):
        return {'model_disposition':'confirmed','source_check':None,'integrity_gaps':[],
                'signals':[],'evidence':[{'original':{'state':'literal'}}],'kind':'unsupported_claim'}

    def test_existing_conditions_route_without_dismissing(self):
        r=self.record();r['signals']=['scenario_already_conditional','scenario_has_explicit_conditions']
        self.assertEqual(triage.group_for(r),'existing_qualifications')
        self.assertEqual(r['model_disposition'],'confirmed')

    def test_exact_source_decision_never_overrides_integrity_gap(self):
        r=self.record();r['source_check']={'disposition':'corroborated'};r['integrity_gaps']=['missing source']
        self.assertEqual(triage.group_for(r),'integrity_gap')

    def test_quote_match_is_not_semantic_approval(self):
        self.assertEqual(triage.group_for(self.record()),'claim_alignment')
        r=self.record();r['model_disposition']='dismissed'
        self.assertEqual(triage.group_for(r),'model_dismissed_reference')

    def test_missing_quote_and_missing_review_stay_open(self):
        r=self.record();r['evidence']=[{'original':{'state':'not_found'}}]
        self.assertEqual(triage.group_for(r),'citation_gap')
        r['model_disposition']='missing_secondary_result'
        self.assertEqual(triage.group_for(r),'review_failure')

    def test_scenario_identity_and_actual_conditions(self):
        payload={'card':{},'coverage':{'files_included':1},'scenario_matches':[{'scenario_id':'real','applicability':'conditional','conditions':['requires host'],'reason':'部分功能，需核实'}]}
        finding={'field':'scenario_match','scenario_id':'wrong'}
        values=triage.target_values(payload,finding)
        self.assertEqual(values,[])
        self.assertIn('scenario_id_not_in_frozen_project',triage.signals(payload,finding,values))
        r=self.record();r['signals']=triage.signals(payload,finding,values)
        self.assertEqual(triage.group_for(r),'invalid_target_reference')
        finding['scenario_id']='real';values=triage.target_values(payload,finding)
        flags=triage.signals(payload,finding,values)
        self.assertIn('scenario_already_conditional',flags)
        self.assertIn('scenario_has_explicit_conditions',flags)

    def test_feature_paraphrase_is_not_an_exact_patch_target(self):
        payload={'card':{'features':[{'text':'Supports A'},{'text':'Supports B'}]}}
        v=triage.target_values(payload,{'field':'features','claim':'Supports C'})
        self.assertEqual(len(v),2)
        self.assertFalse(any(x['claim_exact_match'] for x in v))

    def test_license_proposal_preserves_authorization_labels(self):
        before={'status':'open_source','spdx':'MIT','note':'Verified text'}
        payload={'card':{'license':copy.deepcopy(before)}}
        record={'repository_id':127054182,'id':'127054182:issue-0','repository':'owner/repo','source_check':{'reason':'third-party scope'},'evidence':[],
                'input_path':'input.json','input_sha256':'p','repository_data_sha256':'r'}
        p=triage.proposal(record,payload)
        self.assertEqual(payload['card']['license'],before)
        self.assertEqual(p['changes'][0]['path'],'/card/license/note')
        self.assertFalse(p['approved']);self.assertFalse(p['auto_apply'])
        self.assertEqual(p['patch_on_frozen_packet'][0]['op'],'test')
        self.assertTrue(p['blockers'])

    def test_archive_tamper_stops_instead_of_becoming_a_rule_result(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);file=root/'source.json';file.write_text('{"readme":null}')
            checker=triage.Evidence(None)
            with patch.object(triage.audit.core,'ARCHIVE',root):
                with self.assertRaises(AssertionError):checker.archive('source.json','incorrect')


if __name__=='__main__':unittest.main()
