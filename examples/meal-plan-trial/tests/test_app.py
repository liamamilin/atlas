"""Extra regression tests, independent of the frozen acceptance suite."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'app'))
from store import Store, date_range, quantity_minor
from serve import Handler
from web_support import Error, connect


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name)/'meal-plan.sqlite3'
        self.store = Store(self.path)

    def tearDown(self):
        self.temp.cleanup()

    def recipe(self, quantity='0.01', base=2, ingredient='盐', unit='g'):
        return self.store.recipe({'name':'测试菜谱','base_servings':base,'ingredients':[{'name':ingredient,'unit':unit,'quantity':quantity}]})

    def plan(self, recipe, day, count=1):
        return self.store.plan({'date':day,'recipe_id':recipe['id'],'servings':count})

    def state(self):
        return self.store.state('2026-11-02','2026-11-08')

    def dump(self):
        with connect(self.path) as con:
            return '\n'.join(con.iterdump())

    def test_round_each_plan_half_up_before_aggregation(self):
        r = self.recipe('0.01',2)
        self.plan(r,'2026-11-02');self.plan(r,'2026-11-03')
        # Each 0.005g contribution rounds to 0.01g, totaling 0.02g.
        self.assertEqual(self.state()['shopping']['items'][0]['quantity_minor'],2)
        r = self.recipe('0.01',3,unit='ml')
        self.plan(r,'2026-11-04')
        self.assertEqual(next(i for i in self.state()['shopping']['items'] if i['unit']=='ml')['quantity_minor'],0)

    def test_trim_casefold_grouping_and_units(self):
        a=self.recipe('1.25',1,' STRASSE ')
        b=self.recipe('2.50',1,'straße')
        c=self.recipe('3',1,'strasse',unit='ml')
        for r,day in [(a,'2026-11-02'),(b,'2026-11-03'),(c,'2026-11-04')]:self.plan(r,day)
        totals={i['unit']:i['quantity_minor'] for i in self.state()['shopping']['items']}
        self.assertEqual(totals,{'g':375,'ml':300})

    def test_duplicate_paused_date_zero_write(self):
        r=self.recipe();p=self.plan(r,'2026-11-02');self.store.change({'id':p['id']},True)
        before=self.dump()
        with self.assertRaises(Error) as ctx:self.plan(r,'2026-11-02')
        self.assertEqual((ctx.exception.status,ctx.exception.code),(409,'already_exists'))
        self.assertEqual(before,self.dump())

    def test_invalid_inputs_zero_write(self):
        r=self.recipe();p=self.plan(r,'2026-11-02')
        before=self.dump()
        for value in (0,21,True,2.0,'2',None):
            with self.subTest(servings=value),self.assertRaises(Error):self.store.change({'id':p['id'],'servings':value})
        for value in ('0','-1','NaN','Infinity','1e2','1.001',1.5,' 1 '):
            with self.subTest(quantity=value),self.assertRaises(Error):self.recipe(value)
        for day in ('2026-02-30','2026-1-01','2026-11-02T00:00:00',None):
            with self.subTest(date=day),self.assertRaises(Error):self.plan(r,day)
        with self.assertRaises(Error):self.store.plan({'date':'2026-11-03','recipe_id':9999,'servings':2})
        self.assertEqual(before,self.dump())

    def test_duplicate_recipe_ingredient_rejected_atomically(self):
        before=self.dump()
        with self.assertRaises(Error):
            self.store.recipe({'name':'重复项','base_servings':2,'ingredients':[{'name':' SALT ','unit':'g','quantity':'1'},{'name':'salt','unit':'g','quantity':'2'}]})
        self.assertEqual(before,self.dump())

    def test_range_edges_and_week_isolation(self):
        r=self.recipe('300',2)
        self.plan(r,'2026-11-08',2);self.plan(r,'2026-11-09',4)
        self.assertEqual(self.state()['shopping']['items'][0]['quantity_minor'],30000)
        self.assertEqual(self.store.state('2026-11-09','2026-11-15')['shopping']['items'][0]['quantity_minor'],60000)
        self.assertEqual(date_range('2028-02-29','2028-02-29'),('2028-02-29','2028-02-29'))
        for a,b in [('2026-11-02','2026-11-09'),('2026-11-03','2026-11-02'),('bad','2026-11-02'),(None,'2026-11-02')]:
            with self.subTest(a=a,b=b),self.assertRaises(Error):date_range(a,b)

    def test_demo_only_initializes_new_database(self):
        # Already-created empty database must remain empty even with --demo.
        Store(self.path,demo=True)
        self.assertEqual(self.state()['recipes'],[])
        other=Path(self.temp.name)/'demo.sqlite3'
        store=Store(other,demo=True)
        self.assertEqual(len(store.state()['recipes']),1)
        p=store.state()['plans'][0]
        store.change({'id':p['id']},True)
        before=store.state()
        self.assertEqual(Store(other,demo=True).state(),before)

    def test_get_state_does_not_write(self):
        self.recipe('10.01')
        before=self.path.read_bytes()
        self.state();self.state()
        self.assertEqual(before,self.path.read_bytes())
        self.assertEqual(quantity_minor('001.20'),120)


class FormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.server.store=Store(Path(cls.temp.name)/'meal-plan.sqlite3')
        cls.base='http://127.0.0.1:'+str(cls.server.server_port)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join();cls.temp.cleanup()

    def setUp(self):
        self.server.store=Store(Path(self.temp.name)/(self._testMethodName+'.sqlite3'))

    def request(self,path,data=None):
        request=Request(self.base+path,None if data is None else urlencode(data).encode(),{'Content-Type':'application/x-www-form-urlencoded'})
        try:
            with urlopen(request) as response:return response.status,response.read().decode(),response.url
        except HTTPError as error:return error.code,error.read().decode(),error.url

    def test_form_error_escapes_and_preserves_input(self):
        payload={'name':'<script>alert(1)</script>','base_servings':'2','ingredients':'盐|g|NaN','start':'2026-11-02','end':'2026-11-08'}
        status,body,_=self.request('/recipes',payload)
        self.assertEqual(status,400)
        self.assertIn('未保存',body);self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;',body)
        self.assertNotIn('<script>alert(1)</script>',body);self.assertIn('盐|g|NaN',body)
        self.assertEqual(self.server.store.state()['recipes'],[])

    def test_create_outside_current_week_redirects_visible(self):
        recipe=self.server.store.recipe({'name':'<晚餐>','base_servings':2,'ingredients':[{'name':'番茄','unit':'g','quantity':'300'}]})
        status,body,url=self.request('/plans',{'date':'2027-01-05','recipe_id':recipe['id'],'servings':'4','start':'2026-11-02','end':'2026-11-08'})
        self.assertEqual(status,200);self.assertIn('start=2027-01-04',url)
        self.assertIn('晚餐已安排',body);self.assertIn('2027-01-05',body);self.assertIn('&lt;晚餐&gt;',body)
        self.assertIn('600',body)
        status,body,_=self.request('/plans',{'date':'2027-01-05','recipe_id':recipe['id'],'servings':'2','start':'2027-01-04','end':'2027-01-10'})
        self.assertEqual(status,409);self.assertIn('该日期已有晚餐计划',body)
        self.assertIn('value="2027-01-05"',body)

    def test_api_error_shape_and_unknown_recipe(self):
        request=Request(self.base+'/api/plans',json.dumps({'date':'2026-11-05','recipe_id':99999,'servings':2}).encode(),{'Content-Type':'application/json'})
        with self.assertRaises(HTTPError) as ctx:urlopen(request)
        self.assertEqual(ctx.exception.code,404)
        self.assertEqual(json.loads(ctx.exception.read())['error']['code'],'not_found')


if __name__=='__main__':unittest.main(verbosity=2)
