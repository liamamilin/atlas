#!/usr/bin/env python3
"""Frozen independent outcome tests; only reviewed real applications may execute."""
from __future__ import annotations
import argparse
import concurrent.futures
import csv
import hashlib
import http.client
import io
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import threading
import time
from urllib.parse import urlencode

HERE = Path(__file__).resolve().parent

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')

def hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts}

def toolchain_hashes():
    # Never recursively include growing application evidence in a tool manifest.
    frozen = json.loads((HERE/'freeze.json').read_text(encoding='utf-8'))
    return {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
            for name in [*frozen['source_sha256'], 'freeze.json']}

def env(evidence):
    return {'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', 'HOME': str(evidence),
            'TMPDIR': str(evidence), 'LANG': 'en_US.UTF-8', 'LC_ALL': 'en_US.UTF-8',
            'PYTHONIOENCODING': 'utf-8', 'PYTHONUNBUFFERED': '1', 'PYTHONDONTWRITEBYTECODE': '1'}

class CheckFailure(AssertionError):
    pass

def require(condition, message):
    if not condition:
        raise CheckFailure(message)

class HTTP:
    def __init__(self, port, events, cookie=''):
        self.port, self.events, self.cookie = port, events, cookie
    def call(self, method, path, body=None, expected=None):
        require(path.startswith('/') and not path.startswith('//'), 'Local relative API path required')
        raw = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
        headers = {'Content-Type': 'application/json'} if raw is not None else {}
        if self.cookie:
            headers['Cookie'] = self.cookie
        conn = http.client.HTTPConnection('127.0.0.1', self.port, timeout=8)
        try:
            conn.request(method, path, body=raw, headers=headers)
            response = conn.getresponse()
            data = response.read(4_000_001)
            require(len(data) <= 4_000_000, 'Response exceeds diagnostic limit')
            event = {'method': method, 'path': path, 'request': body,
                     'status': response.status, 'response': data.decode('utf-8', errors='replace')}
            self.events.append(event)
            cookie = response.getheader('Set-Cookie')
            if cookie:
                self.cookie = cookie.split(';', 1)[0]
            if expected is not None:
                require(response.status in expected, f'{method} {path}: {response.status} not in {expected}')
            if path.startswith('/api/export'):
                return response.status, data.decode('utf-8-sig')
            if path == '/':
                return response.status, data.decode('utf-8', errors='replace')
            try:
                result = json.loads(data)
            except (ValueError, UnicodeError) as error:
                raise CheckFailure(f'{method} {path}: response is not JSON: {error}') from error
            if response.status >= 400:
                require(isinstance(result, dict) and bool(result), 'Error must include JSON explanation')
            return response.status, result
        finally:
            conn.close()
    def ok(self, method, path, body=None):
        return self.call(method, path, body, range(200, 300))[1]
    def reject(self, method, path, body=None, statuses=None):
        return self.call(method, path, body, statuses or range(400, 600))[1]

class Server:
    def __init__(self, app, evidence, booking=False):
        self.app, self.evidence, self.booking = app, evidence, booking
        self.data = evidence / 'data'
        self.data.mkdir()
        self.epochs, self.events, self.proc, self.log = [], [], None, None
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            self.port = sock.getsockname()[1]
    def start(self):
        cmd = [sys.executable, '-B', 'app.py', '--port', str(self.port), '--data-dir', str(self.data)]
        if self.booking:
            cmd.append('--init-demo')
        logpath = self.evidence / f'server-{len(self.epochs)+1}.log'
        self.log = logpath.open('wb')
        self.proc = subprocess.Popen(cmd, cwd=self.app, env=env(self.evidence), stdout=self.log,
                                     stderr=subprocess.STDOUT, start_new_session=True)
        epoch = {'pid': self.proc.pid, 'command': cmd, 'log': str(logpath), 'started': time.time()}
        self.epochs.append(epoch)
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError(f'Startup exited {self.proc.returncode}; see {logpath}')
            try:
                status, _ = HTTP(self.port, []).call('GET', '/')
                if 200 <= status < 500:
                    epoch['ready'] = time.time()
                    return
            except OSError:
                pass
            time.sleep(.1)
        raise RuntimeError('Startup readiness timeout')
    def stop(self):
        if self.proc:
            if self.proc.poll() is None:
                self.proc.send_signal(signal.SIGTERM)
                try:
                    self.proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    self.proc.kill()
                    self.proc.wait(timeout=5)
            self.epochs[-1].update(stopped=time.time(), returncode=self.proc.returncode)
            self.proc = None
        if self.log:
            self.log.close()
            self.log = None
    def restart(self):
        before = self.epochs[-1]['pid']
        self.stop()
        self.start()
        require(before != self.epochs[-1]['pid'], 'Restart must use a new real process')
    def client(self):
        return HTTP(self.port, self.events)

class Suite:
    def __init__(self):
        self.results = []
    def check(self, id_, action):
        start = time.monotonic()
        try:
            detail = action()
            result = {'id': id_, 'status': 'passed', 'detail': detail}
        except CheckFailure as error:
            result = {'id': id_, 'status': 'failed', 'error': str(error)}
        except Exception as error:
            result = {'id': id_, 'status': 'setup_or_tool_error_unverified', 'error': f'{type(error).__name__}: {error}'}
        result['seconds'] = round(time.monotonic()-start, 4)
        self.results.append(result)


def budget(server, suite):
    api = server.client()
    def state(month='2030-01'):
        return api.ok('GET', '/api/state?' + urlencode({'month': month}))
    def category(name, amount, month='2030-01'):
        return api.ok('POST', '/api/categories', {'month': month, 'name': name, 'budget': amount})['id']
    def expense(cat, amount, note='', date='2030-01-05'):
        return api.ok('POST', '/api/transactions', {'date': date, 'category_id': cat, 'amount': amount, 'note': note})['id']
    def money(s, planned, spent, remaining):
        require(s['totals'] == {'budget': planned, 'spent': spent, 'remaining': remaining}, f'Incorrect decimal totals: {s["totals"]}')
    def core():
        require(state()['transactions'] == [], 'Fresh store must be empty')
        food = category('餐饮', '0.20')
        unused = category('未使用', '10.00')
        expense(food, '0.10', '第一笔')
        expense(food, '0.20', '第二笔')
        s = state()
        money(s, '10.20', '0.30', '9.90')
        row = next(c for c in s['categories'] if c['id'] == food)
        require(row['remaining'] == '-0.10', 'Overspend must remain visible as negative')
        require(any(c['id'] == unused and c['spent'] == '0.00' for c in s['categories']), 'Unused category missing')
        return {'exact_cents_and_overspend': True}
    suite.check('B01', core)
    def isolation():
        cat = category('餐饮', '50.00', '2030-02')
        expense(cat, '3.45', date='2030-02-03')
        money(state('2030-02'), '50.00', '3.45', '46.55')
        money(state(), '10.20', '0.30', '9.90')
        api.reject('POST', '/api/transactions', {'date': '2030-01-03', 'category_id': cat, 'amount': '1.00', 'note': '跨月应拒绝'})
        money(state('2030-02'), '50.00', '3.45', '46.55')
    suite.check('B02', isolation)
    def edit_delete():
        cat = category('可纠正', '100.00', '2030-03')
        tx = expense(cat, '8.75', date='2030-03-01')
        api.ok('PUT', f'/api/transactions/{tx}', {'date': '2030-03-02', 'category_id': cat, 'amount': '2.35', 'note': '改正'})
        money(state('2030-03'), '100.00', '2.35', '97.65')
        require(state('2030-03')['transactions'][0]['note'] == '改正', 'Edited row not saved')
        api.ok('PUT', f'/api/categories/{cat}', {'budget': '200.00'})
        money(state('2030-03'), '200.00', '2.35', '197.65')
        api.ok('DELETE', f'/api/transactions/{tx}')
        money(state('2030-03'), '200.00', '0.00', '200.00')
        require(state('2030-03')['transactions'] == [], 'Deleted row remains')
    suite.check('B03', edit_delete)
    def invalid():
        cat = category('验证', '20.00', '2030-04')
        tx = expense(cat, '1.00', '原始数据', '2030-04-02')
        before = state('2030-04')
        for amount in ['0', '-1.00', '0.001', 'NaN', 'Infinity', 'abc']:
            api.reject('POST', '/api/transactions', {'date': '2030-04-02', 'category_id': cat, 'amount': amount, 'note': '不应保存'})
        api.reject('POST', '/api/categories', {'month': '2030-04', 'name': '验证', 'budget': '3.00'})
        api.reject('PUT', f'/api/transactions/{tx}', {'date': '2030-02-30', 'category_id': cat, 'amount': '3.00', 'note': '无效日期'})
        api.reject('PUT', f'/api/transactions/{tx}', {'date': '2030-04-02', 'category_id': 'absent', 'amount': '3.00', 'note': '不存在'})
        require(state('2030-04') == before, 'Rejected mutations changed valid records')
    suite.check('B04', invalid)
    def export():
        note = '中文,"引号"\n下一行'
        cat = category('导出,"分类"', '10.00', '2030-05')
        expense(cat, '1.23', note, '2030-05-03')
        _, text = api.call('GET', '/api/export?month=2030-05', expected=range(200,300))
        rows = list(csv.DictReader(io.StringIO(text, newline='')))
        require(rows == [{'date': '2030-05-03', 'category': '导出,"分类"', 'amount': '1.23', 'note': note}], f'CSV roundtrip mismatch: {rows}')
        _, empty = api.call('GET', '/api/export?month=2031-01', expected=range(200,300))
        require(list(csv.DictReader(io.StringIO(empty))) == [], 'Export leaks another month')
    suite.check('B05', export)
    def restart():
        snapshots = {m: state(m) for m in ['2030-01','2030-02','2030-03','2030-04','2030-05']}
        server.restart()
        require({m: state(m) for m in snapshots} == snapshots, 'Real restart changed persisted state')
    suite.check('B06', restart)


def booking(server, suite):
    anon = server.client()
    users = {}
    def login(name):
        client = server.client()
        suffix = {'admin':'Admin','alice':'Alice','bob':'Bob'}[name]
        value = client.ok('POST', '/api/login', {'username': name, 'password': f'AtlasDemo-{suffix}-9!'})
        require(bool(client.cookie), 'Login did not set a session cookie')
        require(value.get('user', value)['username'] == name, 'Wrong login identity')
        users[name] = client
        return client
    def login_test():
        anon.reject('GET', '/api/me', statuses=[401])
        anon.reject('POST', '/api/login', {'username':'admin','password':'wrong'})
        for name in ['admin','alice','bob']:
            login(name)
        require((lambda x: x.get('user', x))(users['alice'].ok('GET','/api/me'))['role'] != 'admin', 'Resident login became admin')
    suite.check('K01', login_test)
    resources = {}
    def roles():
        a = users['alice']
        a.reject('POST','/api/resources', {'name':'伪造设施','role':'admin','user_id':'admin'}, [401,403])
        for name in ['会议室','活动室']:
            resources[name] = users['admin'].ok('POST','/api/resources', {'name':name})['id']
        require(len(a.ok('GET','/api/resources')['resources']) == 2, 'Resource list mismatch')
    suite.check('K02', roles)
    def create(client, res, start, end, note='普通预约', **extra):
        return client.ok('POST','/api/bookings', {'resource_id':res,'start':start,'end':end,'note':note,**extra})['id']
    ids = {}
    def intervals():
        a, b = users['alice'], users['bob']
        res = resources['会议室']
        ids['a'] = create(a,res,'2030-06-01T10:00:00+08:00','2030-06-01T11:00:00+08:00','私密甲')
        ids['b'] = create(b,res,'2030-06-01T11:00:00+08:00','2030-06-01T12:00:00+08:00','私密乙')
        b.reject('POST','/api/bookings', {'resource_id':res,'start':'2030-06-01T02:30:00Z','end':'2030-06-01T03:30:00Z','note':'同真实时刻冲突'}, [409])
        create(a,resources['活动室'],'2030-06-01T10:00:00+08:00','2030-06-01T11:00:00+08:00')
        for start,end in [('2030-06-01T10:00:00','2030-06-01T11:00:00'),('2030-06-01T12:00:00Z','2030-06-01T12:00:00Z'),('2030-06-01T13:00:00Z','2030-06-01T12:00:00Z'),('bad','bad')]:
            a.reject('POST','/api/bookings', {'resource_id':res,'start':start,'end':end,'note':'无效'},[400])
    suite.check('K03', intervals)
    def ownership():
        a,b,admin = users['alice'],users['bob'],users['admin']
        a.reject('GET', f'/api/bookings/{ids["b"]}', statuses=[403,404])
        a.reject('POST', f'/api/bookings/{ids["b"]}/cancel', {'user_id':'admin','role':'admin'}, [401,403,404])
        listing = a.ok('GET','/api/bookings')['bookings']
        require(all(row['id'] != ids['b'] and row['note'] != '私密乙' for row in listing), 'Resident list exposes another resident')
        available = a.ok('GET', '/api/availability?'+urlencode({'resource_id':resources['会议室']}))
        require(isinstance(available,dict) and isinstance(available.get('slots'),list), 'Availability lacks real slots list')
        require(all(isinstance(x,dict) and isinstance(x.get('start'),str) and x['start'] and isinstance(x.get('end'),str) and x['end'] for x in available['slots']), 'Availability slot lacks start/end times')
        private_keys={'owner','ownerid','user','userid','username','resident','residentid','email','phone','note','notes'}
        def has_private(value):
            if isinstance(value,dict):
                return any(str(k).lower().replace('_','').replace('-','') in private_keys or has_private(v) for k,v in value.items())
            if isinstance(value,list):
                return any(has_private(v) for v in value)
            return isinstance(value,str) and any(secret in value for secret in ['私密甲','私密乙'])
        require(not has_private(available), 'Availability exposes resident identity/private notes')
        # Public resource metadata/counts are not an unstated schema violation.
        require(len(admin.ok('GET','/api/bookings')['bookings']) >= 3, 'Admin cannot manage all records')
        bid = create(a,resources['会议室'],'2030-06-02T10:00:00Z','2030-06-02T11:00:00Z',user_id=(lambda x: x.get('user', x))(admin.ok('GET','/api/me'))['id'],role='admin')
        actual = a.ok('GET',f'/api/bookings/{bid}')
        actual = actual.get('booking', actual)
        me = a.ok('GET','/api/me'); me = me.get('user', me)
        require(actual['owner_id'] == me['id'], 'Client forged booking owner')
    suite.check('K04', ownership)
    def cancellation():
        a,b = users['alice'],users['bob']
        for _ in range(2):
            value = a.ok('POST', f'/api/bookings/{ids["a"]}/cancel', {})
            value = value.get('booking', value)
            require(value['status'] == 'cancelled', 'Cancel response lacks retained cancelled status')
        history = a.ok('GET','/api/bookings')['bookings']
        require(any(x['id'] == ids['a'] and x['status'] == 'cancelled' for x in history), 'Cancellation deleted history')
        create(b,resources['会议室'],'2030-06-01T10:00:00+08:00','2030-06-01T11:00:00+08:00','释放后重订')
    suite.check('K05', cancellation)
    def concurrent_conflict():
        barrier = threading.Barrier(2)
        def compete(name):
            client = server.client()
            client.cookie = users[name].cookie
            barrier.wait(timeout=5)
            status,result = client.call('POST','/api/bookings', {'resource_id':resources['会议室'],'start':'2030-06-03T10:00:00Z','end':'2030-06-03T11:00:00Z','note':'并发'+name})
            return {'status':status,'body':result}
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(compete,n) for n in ['alice','bob']]
            outcomes = [f.result(timeout=15) for f in futures]
        require(sum(200 <= x['status'] < 300 for x in outcomes) == 1, f'Concurrent successes != 1: {outcomes}')
        require(sum(x['status'] == 409 for x in outcomes) == 1, f'Conflict did not return 409: {outcomes}')
        rows = users['admin'].ok('GET','/api/bookings')['bookings']
        require(sum(x['note'].startswith('并发') for x in rows) == 1, 'Concurrent conflict left extra record')
        return {'genuine_two_connection_barrier': True, 'outcomes':outcomes}
    suite.check('K06', concurrent_conflict)
    def restart():
        before = users['admin'].ok('GET','/api/bookings')['bookings']
        server.restart()
        admin = login('admin')
        after = admin.ok('GET','/api/bookings')['bookings']
        require(sorted(before,key=lambda x:str(x['id'])) == sorted(after,key=lambda x:str(x['id'])), 'Restart reset or changed booking history')
        a = login('alice')
        a.ok('POST','/api/logout', {})
        a.reject('GET','/api/me', statuses=[401])
    suite.check('K07', restart)

class Rename:
    def __init__(self, app, evidence):
        self.app,self.evidence,self.events = app,evidence,[]
        self.index=0
    def fixture(self):
        self.index += 1
        root = self.evidence / f'fixture-{self.index:02d}'
        root.mkdir()
        (root/'.atlas-renamer').mkdir()
        return root
    def call(self, root, *args, success=True):
        command=[sys.executable,'-B','app.py','--root',str(root),*map(str,args)]
        try:
            proc=subprocess.run(command,cwd=self.app,env=env(self.evidence),capture_output=True,timeout=12)
        except subprocess.TimeoutExpired as error:
            self.events.append({'command':command,'timeout':12})
            raise RuntimeError('CLI exceeded 12s timeout') from error
        event={'command':command,'returncode':proc.returncode,'stdout':proc.stdout.decode('utf-8',errors='replace'),'stderr':proc.stderr.decode('utf-8',errors='replace')}
        self.events.append(event)
        if success:
            require(proc.returncode==0, f'CLI failed: {event}')
            try:
                return json.loads(event['stdout'])
            except ValueError as error:
                raise CheckFailure('Successful CLI stdout is not JSON') from error
        require(proc.returncode!=0, f'Unsafe or invalid command reported success: {event}')
        require(bool(event['stderr'].strip() or event['stdout'].strip()), 'Failure has no explanation')
        return event
    @staticmethod
    def snapshot(root):
        return {str(p.relative_to(root)):p.read_bytes().hex() for p in root.rglob('*') if p.is_file() and not p.is_symlink() and '.atlas-renamer' not in p.relative_to(root).parts}
    def preview(self, root, find='old', replace='new'):
        plan=root/'.atlas-renamer'/'plan.json'
        result=self.call(root,'preview','--find',find,'--replace',replace,'--plan',plan)
        require(result['status']=='preview' and plan.is_file(), 'Preview did not save its real plan')
        return plan,result

def rename(tool,suite):
    def journey():
        root=tool.fixture()
        (root/'old-甲.txt').write_text('中文内容\n',encoding='utf-8')
        (root/'old-2.bin').write_bytes(bytes(range(256)))
        (root/'keep.txt').write_text('未选文件')
        (root/'directory').mkdir()
        (root/'directory'/'old-child').write_text('不得递归')
        (root/'alias.txt').symlink_to('old-甲.txt')
        listing=tool.call(root,'list')['files']
        require({x['name'] for x in listing}=={'old-甲.txt','old-2.bin','keep.txt'},'List includes dirs/symlinks/internal state or misses files')
        before=tool.snapshot(root)
        plan,result=tool.preview(root)
        require(tool.snapshot(root)==before,'Preview changed source data')
        require({(x['old'],x['new']) for x in result['operations']}=={('old-甲.txt','new-甲.txt'),('old-2.bin','new-2.bin')}, 'Preview operations mismatch')
        tool.call(root,'apply','--plan',plan,success=False)
        require(tool.snapshot(root)==before,'Unconfirmed apply changed files')
        applied=tool.call(root,'apply','--plan',plan,'--confirm')
        require(applied['status']=='applied','Apply status incorrect')
        require((root/'new-甲.txt').read_bytes()==bytes.fromhex(before['old-甲.txt']),'Text contents changed')
        require((root/'new-2.bin').read_bytes()==bytes(range(256)),'Binary contents changed')
        require((root/'keep.txt').read_bytes()==bytes.fromhex(before['keep.txt']),'Unselected file changed')
        after=tool.snapshot(root)
        # Explicit already-applied success or nonzero refusal are both allowed.
        try:
            repeat=tool.call(root,'apply','--plan',plan,'--confirm')
            require(repeat.get('status') in ['already_applied','already-applied','applied'], 'Unexpected repeat status')
        except CheckFailure:
            # The invocation above records evidence; inspect its actual exit rather than hide an application failure.
            require(tool.events[-1].get('returncode',0)!=0,'Repeat apply invalid success')
        require(tool.snapshot(root)==after,'Repeat apply mutated a second time')
        receipt=Path(applied['receipt'])
        if not receipt.is_absolute():
            receipt=root/receipt
        require(receipt.resolve().is_relative_to((root/'.atlas-renamer').resolve()),'Receipt outside internal state')
        tool.call(root,'undo','--receipt',receipt,success=False)
        require(tool.snapshot(root)==after,'Unconfirmed undo changed files')
        undone=tool.call(root,'undo','--receipt',receipt,'--confirm')
        require(undone['status']=='undone' and tool.snapshot(root)==before,'Undo did not restore exact names/content')
    suite.check('F01',journey)
    def conflict():
        root=tool.fixture()
        for name in ['old-a','new-a','old-b']:
            (root/name).write_text(name)
        before=tool.snapshot(root)
        try:
            plan,_=tool.preview(root)
        except CheckFailure:
            require(tool.events[-1]['returncode']!=0,'Preview must report conflict honestly')
        else:
            tool.call(root,'apply','--plan',plan,'--confirm',success=False)
        require(tool.snapshot(root)==before,'Conflict changed any original')
    suite.check('F02',conflict)
    def stale():
        root=tool.fixture(); (root/'old-a').write_text('before')
        plan,_=tool.preview(root); (root/'old-a').write_text('after')
        before=tool.snapshot(root)
        tool.call(root,'apply','--plan',plan,'--confirm',success=False)
        require(tool.snapshot(root)==before,'Stale plan lost changed source content')
    suite.check('F03',stale)
    def traversal():
        root=tool.fixture(); (root/'old-a').write_text('safe')
        before=tool.snapshot(root)
        for replacement in ['../escaped','/absolute/escape','sub/name']:
            try:
                plan,_=tool.preview(root,replace=replacement)
            except CheckFailure:
                require(tool.events[-1]['returncode']!=0,'Traversal preview false success')
            else:
                tool.call(root,'apply','--plan',plan,'--confirm',success=False)
            require(tool.snapshot(root)==before,'Traversal mutated originals')
        tool.call(root,'preview','--find','','--replace','x','--plan',root/'.atlas-renamer'/'empty.json',success=False)
    suite.check('F04',traversal)
    def tamper():
        root=tool.fixture(); (root/'old-a').write_text('safe')
        plan,_=tool.preview(root)
        parsed=json.loads(plan.read_text())
        def replace_names(value):
            if isinstance(value,dict):
                return {k:replace_names(v) for k,v in value.items()}
            if isinstance(value,list):
                return [replace_names(v) for v in value]
            if value in ['new-a','./new-a']:
                return '../escape'
            if value==str(root/'new-a'):
                return str(root.parent/'escape')
            return value
        edited=replace_names(parsed)
        if edited==parsed:
            raise RuntimeError('Tamper probe could not locate bare or assigned-root absolute target filename in this legitimate JSON plan format; product containment remains unverified')
        plan.write_text(json.dumps(edited))
        before=tool.snapshot(root)
        tool.call(root,'apply','--plan',plan,'--confirm',success=False)
        require(tool.snapshot(root)==before and not (root.parent/'escape').exists(),'Tampered plan escaped or changed data')
    suite.check('F05',tamper)
    def symlink_state():
        root=tool.fixture(); (root/'old-a').write_text('safe')
        outside=tool.evidence/'owned-outside-state'; outside.mkdir()
        (outside/'sentinel').write_text('unchanged')
        (root/'.atlas-renamer').rmdir(); (root/'.atlas-renamer').symlink_to(outside,target_is_directory=True)
        tool.call(root,'preview','--find','old','--replace','new','--plan',root/'.atlas-renamer'/'plan.json',success=False)
        require({p.name for p in outside.iterdir()}=={'sentinel'} and (outside/'sentinel').read_text()=='unchanged','Symlink state wrote outside assigned root')
    suite.check('F06',symlink_state)
    def undo_conflict():
        root=tool.fixture(); (root/'old-a').write_text('source')
        plan,_=tool.preview(root); applied=tool.call(root,'apply','--plan',plan,'--confirm')
        receipt=Path(applied['receipt']); receipt=receipt if receipt.is_absolute() else root/receipt
        (root/'old-a').write_text('new unrelated file')
        before=tool.snapshot(root)
        tool.call(root,'undo','--receipt',receipt,'--confirm',success=False)
        require(tool.snapshot(root)==before,'Undo conflict overwrote current data')
    suite.check('F07',undo_conflict)
    def literal():
        root=tool.fixture(); (root/'a.b.txt').write_text('dot'); (root/'axb.txt').write_text('x')
        plan,result=tool.preview(root,find='a.b',replace='renamed')
        require(result['operations']==[{'old':'a.b.txt','new':'renamed.txt'}] or {(x['old'],x['new']) for x in result['operations']}=={('a.b.txt','renamed.txt')},'Find treated literal text as regex')
        tool.call(root,'apply','--plan',plan,'--confirm')
        require((root/'axb.txt').read_text()=='x','Literal replacement touched unmatched filename')
    suite.check('F08',literal)
    def swapped_symlink():
        root=tool.fixture(); (root/'old-a').write_text('source')
        outside=tool.evidence/'owned-outside-source'; outside.write_text('untouched')
        plan,_=tool.preview(root)
        (root/'old-a').unlink(); (root/'old-a').symlink_to(outside)
        tool.call(root,'apply','--plan',plan,'--confirm',success=False)
        require((root/'old-a').is_symlink() and not (root/'new-a').exists() and outside.read_text()=='untouched', 'Apply followed or renamed substituted symlink')
    suite.check('F09',swapped_symlink)
    def outside_plan():
        root=tool.fixture(); (root/'old-a').write_text('source')
        outside=tool.evidence/'owned-outside-plan.json'
        before=tool.snapshot(root)
        tool.call(root,'preview','--find','old','--replace','new','--plan',outside,success=False)
        require(not outside.exists() and tool.snapshot(root)==before,'Preview wrote plan outside internal state')
    suite.check('F10',outside_plan)
    def changed_undo():
        root=tool.fixture(); (root/'old-a').write_text('source')
        plan,_=tool.preview(root); applied=tool.call(root,'apply','--plan',plan,'--confirm')
        receipt=Path(applied['receipt']); receipt=receipt if receipt.is_absolute() else root/receipt
        (root/'new-a').write_text('new valuable content')
        before=tool.snapshot(root)
        try:
            result=tool.call(root,'undo','--receipt',receipt,'--confirm')
            require(result.get('status')=='undone' and (root/'old-a').read_text()=='new valuable content' and not (root/'new-a').exists(), 'Successful undo overwrote edited content')
        except CheckFailure:
            require(tool.events[-1].get('returncode',0)!=0 and tool.snapshot(root)==before, 'Changed-content undo lost data or falsely succeeded')
    suite.check('F11',changed_undo)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,choices=['budget','booking','rename'])
    parser.add_argument('--app',required=True,type=Path)
    parser.add_argument('--evidence',required=True,type=Path)
    parser.add_argument('--source-reviewed',action='store_true')
    parser.add_argument('--browser',action='store_true',help='Run separate real UI happy-path probe after API tests')
    args=parser.parse_args()
    if not args.source_reviewed:
        parser.error('Manually review all generated source first, then pass --source-reviewed')
    app=args.app.resolve(); evidence=args.evidence.resolve()
    if not (app/'app.py').is_file():
        parser.error('app/app.py missing')
    if evidence.exists():
        parser.error('Evidence directory must be new; preserve every earlier round')
    evidence.mkdir(parents=True)
    before=hashes(app)
    provenance={'case':args.case,'application':str(app),'source_reviewed_operator_assertion':True,
                'application_sha256_before':before,'toolchain_sha256':toolchain_hashes(),
                'python':sys.version,'started':time.time(), 'external_network_permitted':False,
                'browser_status':'not_run; HTTP/CLI checks do not establish UI usability',
                'credentials':'booking uses only common-contract synthetic demo accounts',
                'warning':'Not an OS sandbox. Source review required; child env contains no inherited provider credentials.'}
    dump(evidence/'provenance.json',provenance)
    suite=Suite(); service=None; tool=None
    try:
        if args.case=='rename':
            tool=Rename(app,evidence); rename(tool,suite)
        else:
            service=Server(app,evidence,args.case=='booking')
            service.start()
            {'budget':budget,'booking':booking}[args.case](service,suite)
            if args.browser:
                def browser_probe():
                    command=['/Users/milin/.nvm/versions/node/v22.21.1/bin/node',str(HERE/'browser.cjs'),args.case,f'http://127.0.0.1:{service.port}/',str(evidence)]
                    with (evidence/'browser.log').open('wb') as stream:
                        browser_env=env(evidence)
                        browser_env['PLAYWRIGHT_BROWSERS_PATH']='/Users/milin/Library/Caches/ms-playwright'
                        proc=subprocess.Popen(command,env=browser_env,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
                        try:
                            proc.wait(timeout=90)
                        except subprocess.TimeoutExpired:
                            os.killpg(proc.pid, signal.SIGKILL)
                            proc.wait(timeout=5)
                            raise RuntimeError('Browser probe timed out; its owned process group was stopped')
                    require((evidence/'browser-result.json').is_file(), 'Browser infrastructure produced no result; inspect browser.log')
                    value=json.loads((evidence/'browser-result.json').read_text())
                    if value.get('error','').startswith('browserType.launch:'):
                        raise RuntimeError('Browser launch infrastructure failed; inspect browser-result.json')
                    require(proc.returncode==0 and value.get('status')=='passed', 'Browser probe did not pass; inspect browser-result.json')
                    return {'result':'browser-result.json','screenshot':'captured, not independently visually assessed'}
                suite.check('BROWSER',browser_probe)
    except Exception as error:
        suite.results.append({'id':'SETUP','status':'setup_or_tool_error_unverified','error':f'{type(error).__name__}: {error}'})
    finally:
        if service:
            service.stop()
            dump(evidence/'http-events.json',service.events)
            dump(evidence/'processes.json',service.epochs)
        if tool:
            dump(evidence/'cli-events.json',tool.events)
        provenance['application_sha256_after']=hashes(app)
        provenance['application_unchanged']=before==provenance['application_sha256_after']
        provenance['browser_status']='see browser-result.json' if (evidence/'browser-result.json').exists() else 'not_run; HTTP/CLI checks do not establish UI usability'
        provenance['finished']=time.time(); dump(evidence/'provenance.json',provenance)
        dump(evidence/'result.json',{'case':args.case,'tests':suite.results,
             'browser_status':'see browser-result.json' if args.browser and args.case!='rename' else 'not_run','all_executed_checks_passed':bool(suite.results) and all(x['status']=='passed' for x in suite.results)})
    print(json.dumps({'evidence':str(evidence),'tests':suite.results},ensure_ascii=False))
    return 0 if suite.results and all(x['status']=='passed' for x in suite.results) else 1

if __name__=='__main__':
    raise SystemExit(main())
