"""Trusted fixture driver, executed only in a restricted container with the probe.

This is not a target application or runtime proof. In-memory responses exercise the
probe against correct and deliberately faulty contract behavior; no real data/API.
"""
import argparse
import copy
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import urllib.parse


HTML = '''<!doctype html><html lang="en"><head><meta charset="UTF-8"><title>Home Care</title></head><body>
<h1>Home Care Ledger</h1><form><fieldset><legend>Home equipment care plans</legend>
<label for="home-name">Home name</label><input id="home-name" name="name">
<label for="category">Equipment category</label><select id="category"><option>heating</option></select>
<label for="note">Completion note</label><textarea id="note"></textarea>
<button>Create home</button><button>Add equipment</button><button>Add plan</button><button>Record completion</button><button>Refresh</button>
</fieldset></form><div role="status" aria-live="polite">Complete task: saved / validation field feedback</div>
<table id="due-table"><caption>Due work</caption><thead><tr><th scope="col">Status</th><th scope="col">Due on</th></tr></thead><tbody></tbody></table>
<section id="history"><h2>Completion history</h2></section><script>/* inline API client placeholder: fixture only */</script></body></html>'''


class Fixture:
    def __init__(self, fault=None):
        self.home = None
        self.equipment = []
        self.plans = []
        self.logs = []
        self.transitions = []
        self.tick = 0
        self.fault = fault
        self.html = HTML
        substitutions = {
            'html_label': ('for="home-name"', 'for="missing-name"'),
            'html_fieldset': ('<legend>Home equipment care plans</legend>', ''),
            'html_caption': ('<caption>Due work</caption>', ''),
            'html_scope': ('scope="col"', 'scope="row"'),
            'html_status': ('role="status"', 'role="alert"'),
            'html_lang': ('lang="en"', 'lang="fr"'),
            'html_live': ('aria-live="polite"', 'aria-live="off"'),
        }
        if fault in substitutions:
            self.html = self.html.replace(*substitutions[fault])

    def stamp(self):
        self.tick += 1
        return f'2026-10-21T00:00:{self.tick:06d}Z'

    def response(self, status=200, value=None, code=None):
        if code:
            value = {'error': {'code': code, 'message': 'fixture error', 'field': None}}
        obj = copy.deepcopy(value)
        return status, obj, json.dumps(obj).encode(), 'application/json; charset=utf-8'

    def date(self, value):
        if not isinstance(value, str) or len(value) != 10:
            raise ValueError()
        result = dt.date.fromisoformat(value)
        if not 1900 <= result.year <= 2100:
            raise ValueError()
        return result

    def canonical(self, plan):
        p = copy.deepcopy(plan)
        p['completion_count'] = sum(c['plan_id'] == p['id'] for c in self.logs)
        due = self.date(p['due_on'])
        p['status'] = 'overdue' if due < dt.date.today() else 'due' if due == dt.date.today() else 'upcoming'
        return p

    def request(self, base, method, path, body=None):
        parsed = urllib.parse.urlsplit(path)
        route = parsed.path
        q = {k: v[-1] for k, v in urllib.parse.parse_qs(parsed.query).items()}
        if method == 'DELETE':
            return self.response(405, code='METHOD_NOT_ALLOWED')
        if route == '/':
            return 200, None, self.html.encode(), 'text/html; charset=utf-8'
        if route == '/health':
            return self.response(value={'status': 'ok', 'database': 'ready'})
        if route == '/api/home':
            if method == 'GET':
                return self.response(value={'home': self.home}) if self.home else self.response(404, code='HOME_NOT_FOUND')
            if method == 'POST':
                if self.home:
                    return self.response(409, code='HOME_EXISTS')
                self.home = dict(id='home', name=body['name'].strip(), address=body.get('address', '').strip(), created_at=self.stamp(), updated_at=self.stamp())
                return self.response(201, {'home': self.home})
            if method == 'PATCH':
                if not body:
                    if self.fault == 'empty_patch_write':
                        self.home['updated_at'] = self.stamp()
                    return self.response(422, code='VALIDATION_ERROR')
                self.home.update(body)
                self.home['updated_at'] = self.stamp()
                return self.response(value={'home': self.home})
        eq = next((e for e in self.equipment if route == '/api/equipment/' + e['id']), None)
        if route.startswith('/api/equipment/'):
            return self.response(value={'equipment': eq}) if eq else self.response(404, code='EQUIPMENT_NOT_FOUND')
        if route == '/api/equipment':
            home_id = body.get('home_id') if method == 'POST' else q.get('home_id')
            if not home_id:
                return self.response(422, code='VALIDATION_ERROR')
            if home_id != 'home':
                return self.response(404, code='HOME_NOT_FOUND')
            if method == 'GET':
                return self.response(value={'equipment': self.equipment})
            if not body.get('name', '').strip() or body.get('category') not in ('heating', 'cooling', 'plumbing', 'electrical', 'roof', 'exterior', 'appliance', 'safety', 'other'):
                if self.fault == 'invalid_category_write' and body.get('name', '').strip():
                    self.equipment.append({'id': 'invalid-write', **body})
                return self.response(422, code='VALIDATION_ERROR')
            eq = {'location': '', 'make': '', 'model': '', 'installed_on': None, **body}
            eq.update(id=f'eq_{len(self.equipment):032x}', created_at=self.stamp(), updated_at=self.stamp())
            self.equipment.append(eq)
            return self.response(201, {'equipment': eq})
        if route == '/api/plans' and method == 'POST':
            try:
                days = body['interval_days']
                if type(days) is not int or not 1 <= days <= 3650 or ('first_due_on' in body and 'last_completed_on' in body):
                    raise ValueError()
                last = self.date(body['last_completed_on']) if 'last_completed_on' in body else None
                due = self.date(body['first_due_on']) if 'first_due_on' in body else last + dt.timedelta(days=days) if last else dt.date.today()
            except (KeyError, ValueError):
                return self.response(422, code='VALIDATION_ERROR')
            plan = dict(id=f'pl_{len(self.plans):032x}', home_id=body['home_id'], equipment_id=body.get('equipment_id'), name=body['name'], interval_days=days, last_completed_on=last.isoformat() if last else None, due_on=due.isoformat(), notes=body.get('notes', ''), created_at=self.stamp(), updated_at=self.stamp())
            self.plans.append(plan)
            return self.response(201, {'plan': self.canonical(plan)})
        if route == '/api/plans':
            return self.response(value={'plans': [self.canonical(p) for p in self.plans if not q.get('equipment_id') or p['equipment_id'] == q['equipment_id']]})
        if route.startswith('/api/plans/'):
            plan_id = route.split('/')[3]
            plan = next((p for p in self.plans if p['id'] == plan_id), None)
            if not plan:
                return self.response(404, code='PLAN_NOT_FOUND')
            if route.endswith('/completions'):
                if method == 'GET':
                    logs = sorted((c for c in self.logs if c['plan_id'] == plan_id), key=lambda c: (c['completed_on'], c['created_at'], c['id']), reverse=True)
                    return self.response(value={'completions': logs})
                try:
                    day = self.date(body['completed_on'])
                    note = body.get('note', '').strip()
                    if day > dt.date.today() or len(note) > 500:
                        raise ValueError()
                except (ValueError, KeyError):
                    return self.response(422, code='VALIDATION_ERROR')
                completion = dict(id=f'cm_{len(self.logs):032x}', plan_id=plan_id, completed_on=day.isoformat(), note=note, created_at=self.stamp())
                latest = max(self.date(plan['last_completed_on']), day) if plan['last_completed_on'] else day
                new_due = latest + dt.timedelta(days=plan['interval_days'])
                if self.fault != 'missing_due_floor':
                    new_due = max(self.date(plan['due_on']), new_due)
                self.transitions.append({"before": copy.deepcopy(plan), "completion": copy.deepcopy(completion), "new_due_on": new_due.isoformat(), "latest": latest.isoformat()})
                self.logs.append(completion)
                plan.update(last_completed_on=latest.isoformat(), due_on=new_due.isoformat(), updated_at=self.stamp())
                return self.response(201, {'completion': completion, 'plan': self.canonical(plan)})
            return self.response(value={'plan': self.canonical(plan)})
        if route in ('/api/tasks/due', '/api/history'):
            if not q.get('home_id'):
                return self.response(422, code='VALIDATION_ERROR')
            if q['home_id'] != 'home':
                return self.response(404, code='HOME_NOT_FOUND')
            if q.get('equipment_id') and not any(e['id'] == q['equipment_id'] for e in self.equipment):
                return self.response(404, code='EQUIPMENT_NOT_FOUND')
            if route == '/api/tasks/due':
                try:
                    day = self.date(q.get('as_of', dt.date.today().isoformat()))
                    horizon = int(q.get('horizon_days', '0'))
                    if not 0 <= horizon <= 365:
                        raise ValueError()
                except ValueError:
                    return self.response(422, code='VALIDATION_ERROR')
                tasks = []
                for p in self.plans:
                    due = self.date(p['due_on'])
                    if due > day + dt.timedelta(days=horizon) or q.get('equipment_id') and p['equipment_id'] != q['equipment_id']:
                        continue
                    eq = next((e for e in self.equipment if e['id'] == p['equipment_id']), None)
                    task = {**p, 'home_name': self.home['name'], 'equipment_name': eq['name'] if eq else None, 'status': 'overdue' if due < day else 'due' if due == day else 'upcoming', 'days_until_due': (due - day).days}
                    tasks.append(task)
                tasks.sort(key=lambda p: (p['due_on'], p['created_at'], p['id']))
                if tasks and self.fault in ('due_extra', 'due_duplicate'):
                    tasks.append({**tasks[0], 'id': 'unexpected' if self.fault == 'due_extra' else tasks[0]['id']})
                if tasks and self.fault == 'due_missing':
                    tasks.pop(0)
                return self.response(value={'as_of': day.isoformat(), 'horizon_days': horizon, 'tasks': tasks})
            try:
                limit = int(q.get('limit', '100'))
                if not 1 <= limit <= 500:
                    raise ValueError()
            except ValueError:
                return self.response(422, code='VALIDATION_ERROR')
            history = []
            for c in self.logs:
                plan = next(p for p in self.plans if p['id'] == c['plan_id'])
                if q.get('equipment_id') and plan['equipment_id'] != q['equipment_id']:
                    continue
                eq = next((e for e in self.equipment if e['id'] == plan['equipment_id']), None)
                history.append({**c, 'home_id': 'home', 'home_name': self.home['name'], 'equipment_id': plan['equipment_id'], 'equipment_name': eq['name'] if eq else None, 'plan_name': plan['name']})
            history.sort(key=lambda c: (c['completed_on'], c['created_at'], c['id']), reverse=True)
            return self.response(value={'history': history[:limit]})
        return self.response(404, code='NOT_FOUND')


def run(probe_path):
    spec = importlib.util.spec_from_file_location('generated_probe', probe_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    results = []
    correct = Fixture()
    module.request = correct.request
    for name, case in module.CASES.items():
        case('http://fixture.invalid')
        results.append({'check': name, 'expected': 'pass', 'result': 'pass'})
    initial = [t for t in correct.transitions if t['before']['last_completed_on'] is None]
    explicit = [t for t in initial if t['before']['due_on'] == '2026-03-01' and t['completion']['completed_on'] == '2025-01-01' and t['before']['interval_days'] == 30]
    assert explicit and all(t['new_due_on'] == '2026-03-01' and t['latest'] == '2025-01-01' for t in explicit), 'missing explicit initial historical-backfill fixture'
    today = dt.date.today().isoformat()
    default = [t for t in initial if t['before']['due_on'] == today and t['completion']['completed_on'] < today]
    assert default and all(t['new_due_on'] == today for t in default), 'missing creation-day initial historical-backfill fixture'
    results.append({'check': 'two_initial_backfill_branches', 'expected': 'pass', 'result': 'pass', 'explicit': explicit, 'creation_day': default})
    mutations = {'empty_patch_write': 'A01', 'invalid_category_write': 'A01', 'missing_due_floor': 'A03', 'due_extra': 'A02', 'due_duplicate': 'A02', 'due_missing': 'A02', **{key: 'A05' for key in ('html_label', 'html_fieldset', 'html_caption', 'html_scope', 'html_status', 'html_lang', 'html_live')}}
    for fault, name in mutations.items():
        fixture = Fixture(fault)
        module.request = fixture.request
        try:
            module.CASES[name]('http://fixture.invalid')
        except AssertionError as error:
            results.append({'check': fault, 'expected': 'detected', 'result': 'detected', 'message': str(error)})
        else:
            raise AssertionError('probe failed to detect ' + fault)
    return {'kind': 'isolated_fixture_not_application_runtime', 'status': 'passed', 'probe_sha256': hashlib.sha256(Path(probe_path).read_bytes()).hexdigest(), 'checks': results, 'application_runtime': 'not_run', 'upstream_runtime': 'not_run'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('probe', type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.probe), indent=2))

