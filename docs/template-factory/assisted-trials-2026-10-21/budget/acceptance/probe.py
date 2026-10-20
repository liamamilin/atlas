"""Real HTTP checks for an isolated monthly-budget trial. Never a UI/browser proof."""
import argparse
import json
from pathlib import Path
import secrets
import socket
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def request(base, path, data=None):
    req = Request(base + path, data=None if data is None else json.dumps(data).encode(),
                  headers={'Content-Type':'application/json'})
    try:
        with urlopen(req, timeout=10) as response:
            return response.status, json.load(response)
    except HTTPError as error:
        return error.code, json.load(error)


def journey(base, case):
    month = f'{2200 + secrets.randbelow(7000)}-01'
    next_month = month[:4] + '-02'
    assert request(base, '/api/months/start', {'month':month})[0] == 201
    assert request(base, '/api/income', {'month':month,'income':'5000.00'})[0] == 200
    status, food = request(base, '/api/categories', {'month':month,'name':'测试食品','amount':'1000.00'})
    assert status == 201
    status, transit = request(base, '/api/categories', {'month':month,'name':'测试交通','amount':'200.00'})
    assert status == 201
    status, first = request(base, '/api/expenses', {'month':month,'date':month+'-03','category_id':food['id'],'amount':'35.50','note':'早餐'})
    assert status == 201
    assert request(base, '/api/expenses', {'month':month,'date':month+'-04','category_id':food['id'],'amount':'12.30','note':'午餐'})[0] == 201
    def state(m=month):
        status, value = request(base, '/api/state?month='+m)
        assert status == 200
        return value
    s=state()
    assert s['totals']=={'planned_minor':120000,'spent_minor':4780,'remaining_minor':115220,'unallocated_minor':380000}
    assert request(base, '/api/expenses/update', {'id':first['id'],'month':month,'date':month+'-03','category_id':food['id'],'amount':'30.50','note':'更正'})[0] == 200
    assert state()['totals']['spent_minor'] == 4280
    before=state()
    for amount in ['-1','0','NaN','1.234','1e3']:
        assert request(base,'/api/expenses',{'month':month,'date':month+'-05','category_id':food['id'],'amount':amount})[0] == 400
        assert state() == before
    assert request(base,'/api/transfer',{'month':month,'source_id':food['id'],'target_id':transit['id'],'amount':'20.00'})[0]==200
    s=state()
    assert s['totals']['planned_minor']==120000
    assert [c['planned_minor'] for c in s['categories']]==[98000,22000]
    assert request(base,'/api/template',{'month':month})[0]==200
    assert request(base,'/api/months/start',{'month':next_month})[0]==201
    assert state(next_month)['totals']['planned_minor']==120000
    assert state(next_month)['totals']['spent_minor']==0
    assert state()['totals']['spent_minor']==4280
    return month, state()


def restart(base, root):
    assert request(base,'/api/health')[0]==200
    with tempfile.TemporaryDirectory(prefix='budget-restart-') as tmp:
        with socket.socket() as sock:
            sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
        url=f'http://127.0.0.1:{port}'
        command=[sys.executable,str(Path(root)/'app/serve.py'),'--port',str(port),'--data-dir',str(Path(tmp)/'data')]
        def start():
            proc=subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            for _ in range(100):
                try:
                    if request(url,'/api/health')[0]==200:return proc
                except OSError:pass
                time.sleep(.05)
            proc.terminate();proc.wait();raise RuntimeError('restart instance not ready')
        proc=start()
        try:month,before=journey(url,'B05')
        finally:proc.terminate();proc.wait(timeout=10)
        proc=start()
        try:assert request(url,'/api/state?month='+month)[1]==before
        finally:proc.terminate();proc.wait(timeout=10)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url',required=True)
    p.add_argument('--case',choices=['B01','B02','B03','B04','B05'],required=True)
    p.add_argument('--app-root')
    args=p.parse_args()
    try:
        if args.case=='B05':
            if not args.app_root:raise ValueError('B05 requires --app-root for a real process restart')
            restart(args.base_url,args.app_root)
        else:journey(args.base_url,args.case)
    except Exception as error:
        print(json.dumps({'case':args.case,'status':'failed','error':str(error),'browser_verified':False}));return 1
    print(json.dumps({'case':args.case,'status':'passed','scope':'real HTTP or owned process restart; not browser proof','browser_verified':False}));return 0

if __name__=='__main__':sys.exit(main())
