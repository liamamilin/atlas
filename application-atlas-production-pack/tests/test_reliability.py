import concurrent.futures
from contextlib import closing, redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

CODE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE))
import atlas_runtime as rt
import classify as classifier
import draft_new
import gate_check
import promote_draft as promote
from review_store import fingerprint, corpus_revision, update_review, load_review


class RetrievalTests(unittest.TestCase):
    def test_scores_follow_slug_and_neighbors_are_unique(self):
        slugs = tuple(f"s{i:02}" for i in range(20))
        values = np.linspace(.1, .99, 20)
        state = classifier.Snapshot(slugs, np.column_stack((values, np.zeros(20))), {}, {},
            {s: set(slugs[:10]) for s in slugs[10:]}, {})
        with patch.object(classifier, '_embed', return_value=[np.array([1., 0.])]):
            pool, scores = classifier.candidates('query', state=state)
        self.assertEqual(pool[0], 's19')
        self.assertAlmostEqual(scores['s19'], .99)
        self.assertEqual(len(pool), 16)
        self.assertEqual(len(set(pool)), 16)
        with patch.object(classifier, 'candidates', return_value=(pool, scores)):
            hits = draft_new.collision('query')
        self.assertEqual(hits[0][0], 's19')
        self.assertAlmostEqual(hits[0][1], .99)

    def test_cache_reloads_after_atomic_database_replacement(self):
        def make(path, names):
            with closing(sqlite3.connect(path)) as con:
                con.executescript('''CREATE TABLE leaf(slug,name_zh,l0_zh,overview,section_id);
                    CREATE TABLE embedding(slug,vec);
                    CREATE TABLE relation(from_slug,to_slug,to_name,distinction);''')
                for name in names:
                    con.execute('INSERT INTO leaf VALUES (?,?,?,?,?)', (name,name,'core','overview','01.01'))
                    con.execute('INSERT INTO embedding VALUES (?,?)', (name,np.array([1.,0.],dtype=np.float32).tobytes()))
                con.commit()
        with tempfile.TemporaryDirectory() as temp:
            db, new = Path(temp)/'atlas.sqlite', Path(temp)/'new.sqlite'
            make(db, ['first'])
            with patch.object(classifier, 'DB', str(db)), patch.object(classifier, '_snapshot', None), patch.object(classifier, '_signature', None):
                old = classifier.snapshot()
                make(new, ['first','second'])
                os.replace(new, db)
                with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                    snapshots = list(pool.map(lambda _: classifier.snapshot(), range(8)))
                self.assertEqual(old.slugs, ('first',))
                self.assertTrue(all(s.slugs == ('first','second') for s in snapshots))


class GateTests(unittest.TestCase):
    def test_accepted_labels_are_explicit_and_partial_results_fail(self):
        items = [{'name':'钉钉','expect':'team-messaging-application'}]
        rows, summary = gate_check.score_rows([{'name':'钉钉','got':'team-workspace-platform'}], items)
        self.assertTrue(summary['passed'])
        self.assertEqual(summary['raw_accuracy'], 0)
        with self.assertRaises(ValueError):
            gate_check.score_rows([], items)

    def test_request_failure_is_recorded_and_cannot_pass(self):
        items = [{'name':'sample','desc':'test','expect':'first'}]
        with redirect_stdout(io.StringIO()):
            rows = gate_check.run_items(items, lambda _: (_ for _ in ()).throw(OSError('offline')), sleep=lambda _:None)
        _, summary = gate_check.score_rows(rows,items)
        self.assertFalse(summary['passed'])
        self.assertEqual(summary['errors'],1)
        self.assertFalse(rows[0]['ret1'])


class PublicationTests(unittest.TestCase):
    def test_failure_rolls_back_all_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root/'atlas').mkdir()
            old = root/'old'; new = root/'new'; absent=root/'absent'
            old.write_text('before');new.write_text('after')
            real = rt.atomic_copy
            def fail_once(source,target):
                if Path(target)==absent.resolve():
                    raise OSError('disk error')
                return real(source,target)
            with patch.object(rt,'atomic_copy',side_effect=fail_once):
                with self.assertRaises(OSError):rt.publish_files([(new,old),(new,absent)],root)
            self.assertEqual(old.read_text(),'before')
            self.assertFalse(absent.exists())
            self.assertFalse((root/'atlas/.publish').exists())

    def test_recover_interrupted_cutover(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);journal=root/'atlas/.publish';journal.mkdir(parents=True)
            target=root/'live';target.write_text('partial');(journal/'0').write_text('original')
            rt.atomic_json(journal/'journal.json',{'committed':False,'files':[{'target':str(target),'backup':'0'}]})
            rt.recover_publication(root)
            self.assertEqual(target.read_text(),'original')

    def test_corpus_lock_prevents_concurrent_updates(self):
        with tempfile.TemporaryDirectory() as temp:
            with rt.corpus_lock(temp):
                with self.assertRaises(RuntimeError):
                    with rt.corpus_lock(temp):pass

    def test_review_updates_do_not_clobber_other_drafts(self):
        with tempfile.TemporaryDirectory() as temp:
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
                list(pool.map(lambda n:update_review(f'draft-{n}',{'verdict':'new'},temp),range(30)))
            self.assertEqual(len(load_review(temp)),30)


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.pack=Path(self.temp.name)/'pack';self.pack.mkdir()
        for name in ['applications','research','atlas','logs','drafts']:(self.pack/name).mkdir()
        self.body=(CODE/'applications/cli-accounting-tool.md').read_text()
        for slug,title in [('existing-tool','Existing Tool')]:
            (self.pack/'applications'/f'{slug}.md').write_text(self.body.replace('# CLI Accounting Tool',f'# {title}',1))
            (self.pack/'research'/f'{slug}.md').write_text('## Boundary Findings\nTests\n## Uncertainties\nNone')
        (self.pack/'DIRECTORY.md').write_text('# Test\n## 01 Tools\n### 01.01 Tools\n- Existing Tool\n')
        (self.pack/'STATUS.md').write_text('# Status\n')
        for name in ['mvp_apps.json','mvp_apps_classified.json','pilot_synthetic.json']:(self.pack/name).write_text('[]')
        (self.pack/'pilot_clean.json').write_text(json.dumps([{'name':'sample','desc':'tool','expect':'existing-tool'}]))
        (self.pack/'atlas/section-zh.json').write_text('[{"id":"01.01","name_zh":"工具"}]')
        (self.pack/'atlas/translations.jsonl').write_text(json.dumps({'slug':'existing-tool','name_zh':'工具','aliases_zh':[],'l0_zh':'definition'})+'\n')
        self.run_script(self.pack,'export_atlas.py')
        self.fill_aux(self.pack)
        self.web=Path(self.temp.name)/'web';self.web.mkdir();(self.web/'meta.json').write_text('{"old":true}')
        self.draft=self.pack/'drafts/wip-new.md'
        self.draft.write_text('---\nslug: wip-new\nname: New Tool\nname_zh: 新工具\ndesc: new idea\nsource: human\nstatus: draft\ncreated: 2026-09-13\nengine: test\n---\n'+self.body.replace('# CLI Accounting Tool','# New Tool',1))
        (self.pack/'drafts/wip-new.research.md').write_text('## Boundary Findings\nTests\n## Uncertainties\nNone')
        self.review()

    def run_script(self,pack,name):
        result=subprocess.run([sys.executable,str(CODE/name)],env={**os.environ,'ATLAS_PACK':str(pack),'ATLAS_WEB_OUT':str(pack/'web-data')},capture_output=True,text=True)
        if result.returncode:raise AssertionError(result.stdout+'\n'+result.stderr)

    def fill_aux(self,pack):
        with closing(sqlite3.connect(pack/'atlas/atlas.sqlite')) as con:
            con.execute('CREATE TABLE IF NOT EXISTS embedding(slug TEXT PRIMARY KEY,model,dim,vec)')
            for (slug,) in con.execute('SELECT slug FROM leaf').fetchall():
                con.execute('INSERT OR REPLACE INTO embedding VALUES (?,?,?,?)',(slug,'bge-m3',2,np.array([1.,0.],dtype=np.float32).tobytes()))
                con.execute('INSERT OR REPLACE INTO leaf_zh_body VALUES (?,?,?,?,?,?,?)',(slug,'overview','how','rules','variants','products','test'))
                con.execute('UPDATE leaf SET name_zh=?,l0_zh=? WHERE slug=?',('名称','definition',slug))
            con.commit()

    def review(self,verdict='new',best=None):
        update_review('wip-new',{'verdict':verdict,'best':best,'draft_fingerprint':fingerprint('wip-new',self.pack),'corpus_revision':corpus_revision(self.pack)},self.pack)

    def runner(self,stage,command):
        name=Path(command[1]).name
        if name=='export_atlas.py':self.run_script(stage,name)
        elif name=='translate_zh.py':
            with closing(sqlite3.connect(stage/'atlas/atlas.sqlite')) as con:
                rows=con.execute('SELECT slug FROM leaf').fetchall()
            with (stage/'atlas/translations.jsonl').open('w') as f:
                for (slug,) in rows:f.write(json.dumps({'slug':slug,'name_zh':'名称','l0_zh':'definition','aliases_zh':[]})+'\n')
        elif name=='embed_leaves.py':self.fill_aux(stage)
        elif name=='gen-data.py':self.run_script(stage,'../atlas-web/scripts/gen-data.py')
        elif name=='gate_check.py':
            rt.atomic_json(stage/'atlas/gate_regression.json',[{'name':'sample','got':'existing-tool'}])
            rt.atomic_json(stage/'atlas/gate_summary.json',{'accuracy':1.,'passed':True})

    def test_export_failure_leaves_database_intact(self):
        before=(self.pack/'atlas/atlas.sqlite').read_bytes()
        with (self.pack/'DIRECTORY.md').open('a') as f:f.write('- Missing Tool\n')
        with self.assertRaises(AssertionError):self.run_script(self.pack,'export_atlas.py')
        self.assertEqual((self.pack/'atlas/atlas.sqlite').read_bytes(),before)

    def test_export_preserves_unchanged_embeddings_and_accepts_aliases(self):
        # Keep translation fields identical to the source record.
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:
            con.execute("UPDATE leaf SET name_zh='工具'");con.commit()
        self.run_script(self.pack,'export_atlas.py')
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:self.assertEqual(con.execute('SELECT count(*) FROM embedding').fetchone()[0],1)
        p=self.pack/'DIRECTORY.md';p.write_text(p.read_text().replace('- Existing Tool','- Existing Tool / Alternate Tool'))
        self.run_script(self.pack,'export_atlas.py')
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:
            self.assertEqual(con.execute('SELECT slug FROM leaf').fetchone()[0],'existing-tool')
            self.assertEqual(con.execute('SELECT count(*) FROM embedding').fetchone()[0],0)

    def test_alias_of_an_existing_acronym_name_keeps_canonical_slug(self):
        (self.pack/'applications/existing-tool.md').rename(self.pack/'applications/existing-tool-et.md')
        (self.pack/'research/existing-tool.md').rename(self.pack/'research/existing-tool-et.md')
        path=self.pack/'DIRECTORY.md'
        path.write_text(path.read_text().replace('- Existing Tool','- Existing Tool / ET / New Alias'))
        self.run_script(self.pack,'export_atlas.py')
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:
            self.assertEqual(con.execute('SELECT slug FROM leaf').fetchone()[0],'existing-tool-et')


    def test_missing_stale_or_variant_review_cannot_create_leaf(self):
        (self.pack/'drafts/review.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'查重'):promote.validate_promotion('wip-new','new','01.01',self.pack)
        self.review('variant','existing-tool')
        with self.assertRaisesRegex(ValueError,'新类型'):promote.validate_promotion('wip-new','new','01.01',self.pack)
        self.review();self.draft.write_text(self.draft.read_text()+'\nEdit')
        with self.assertRaisesRegex(ValueError,'查重'):promote.validate_promotion('wip-new','new','01.01',self.pack)

    def test_low_gate_does_not_modify_live_corpus(self):
        before=(self.pack/'atlas/atlas.sqlite').read_bytes();directory=(self.pack/'DIRECTORY.md').read_text()
        def fail_gate(stage,command):
            self.runner(stage,command)
            if Path(command[1]).name=='gate_check.py':
                rt.atomic_json(stage/'atlas/gate_regression.json',[{'name':'sample','got':'none'}])
        with redirect_stdout(io.StringIO()),self.assertRaisesRegex(RuntimeError,'回归未达标'):
            promote.promote('wip-new','new','01.01',self.pack,self.web,fail_gate)
        self.assertEqual((self.pack/'atlas/atlas.sqlite').read_bytes(),before)
        self.assertEqual((self.pack/'DIRECTORY.md').read_text(),directory)
        self.assertFalse((self.pack/'applications/new-tool.md').exists())
        self.assertTrue((self.pack/'drafts/wip-new.research.md').exists())
        self.assertFalse(load_review(self.pack)['wip-new']['promoted'])
        self.assertFalse(load_review(self.pack)['wip-new']['gate_ok'])
        self.assertEqual(json.loads((self.web/'meta.json').read_text()),{'old':True})

    def test_api_rejects_stale_review_before_starting_background_work(self):
        import drafts_api
        self.draft.write_text(self.draft.read_text()+'\nChanged')
        handler=object.__new__(drafts_api.Handler)
        handler.path='/api/promote'
        handler._body=lambda:{'slug':'wip-new','action':'new','section':'01.01'}
        responses=[]
        handler._json=lambda body,code=200:responses.append((body,code))
        validate=promote.validate_promotion
        with patch.object(promote,'validate_promotion',side_effect=lambda slug,action,target:validate(slug,action,target,self.pack)), patch.object(drafts_api.threading,'Thread') as thread:
            handler.do_POST()
        self.assertEqual(responses[0][1],409)
        thread.assert_not_called()

    def test_api_does_not_enqueue_a_draft_already_promoting_in_another_process(self):
        import drafts_api
        self.draft.write_text(self.draft.read_text().replace('status: draft','status: promoting'))
        handler=object.__new__(drafts_api.Handler)
        handler.path='/api/promote'
        handler._body=lambda:{'slug':'wip-new','action':'new','section':'01.01'}
        responses=[]
        handler._json=lambda body,code=200:responses.append((body,code))
        validate=promote.validate_promotion
        with patch.object(promote,'validate_promotion',side_effect=lambda slug,action,target:validate(slug,action,target,self.pack)), patch.object(drafts_api.threading,'Thread') as thread:
            handler.do_POST()
        self.assertEqual(responses[0][1],409)
        thread.assert_not_called()
        self.assertIn('status: promoting',self.draft.read_text())


    def test_pipeline_exception_preserves_draft_research_and_database(self):
        before=(self.pack/'atlas/atlas.sqlite').read_bytes()
        def unavailable(stage,command):raise OSError('provider unavailable')
        with self.assertRaisesRegex(OSError,'provider unavailable'):
            promote.promote('wip-new','new','01.01',self.pack,self.web,unavailable)
        self.assertEqual((self.pack/'atlas/atlas.sqlite').read_bytes(),before)
        self.assertTrue((self.pack/'drafts/wip-new.research.md').exists())
        self.assertIn('status: draft',self.draft.read_text())


    def test_success_publishes_and_keeps_draft_id(self):
        with redirect_stdout(io.StringIO()):result=promote.promote('wip-new','new','01.01',self.pack,self.web,self.runner)
        self.assertTrue(result['promoted']);self.assertEqual(result['final_slug'],'new-tool')
        self.assertTrue(self.draft.exists());self.assertIn('status: promoted',self.draft.read_text())
        self.assertEqual(json.loads((self.web/'meta.json').read_text())['leafCount'],2)
        self.assertTrue((self.pack/'applications/new-tool.md').exists())
        with self.assertRaisesRegex(ValueError,'状态'):promote.validate_promotion('wip-new','new','01.01',self.pack)

    def test_merge_rebuilds_data_without_adding_a_leaf(self):
        self.review('variant','existing-tool')
        with redirect_stdout(io.StringIO()):result=promote.promote('wip-new','merge','existing-tool',self.pack,self.web,self.runner)
        self.assertTrue(result['promoted'])
        self.assertIn('Existing Tool / New Tool',(self.pack/'DIRECTORY.md').read_text())
        self.assertEqual(json.loads((self.web/'meta.json').read_text())['leafCount'],1)


if __name__=='__main__':unittest.main()
