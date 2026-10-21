#!/usr/bin/env python3
'''Acceptance probe for the Home Care Ledger target.

Usage:
  python3 probe.py --base-url http://127.0.0.1:8765 --case A01
'''

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

TIMEOUT = 10
SUFFIX = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d%H%M%S%f') + '-' + str(os.getpid())


class ProbeFailure(AssertionError):
    pass


def check(condition, message):
    if not condition:
        raise ProbeFailure(message)


def request(base_url, method, path, body=None):
    url = base_url.rstrip('/') + path
    headers = {'Accept': 'application/json'}
    data = None
    if body is not None:
        data = json.dumps(body, separators=(',', ':')).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            raw = response.read()
            status = response.status
            ctype = response.headers.get('Content-Type', '')
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        status = exc.code
        ctype = exc.headers.get('Content-Type', '')
    parsed = None
    if raw:
        try:
            parsed = json.loads(raw.decode('utf-8'))
        except (UnicodeDecodeError, json.JSONDecodeError):
            parsed = None
    return status, parsed, raw, ctype


def api(base_url, method, path, body=None, expected=200):
    status, parsed, raw, ctype = request(base_url, method, path, body)
    check(status == expected, f'{method} {path}: expected HTTP {expected}, got {status}; body={raw[:300]!r}')
    check('application/json' in ctype.lower(), f'{method} {path}: expected JSON, got {ctype!r}')
    check(isinstance(parsed, dict), f'{method} {path}: expected a JSON object')
    return parsed


def expect_error(base_url, method, path, body, expected_status, expected_code):
    status, parsed, raw, ctype = request(base_url, method, path, body)
    check(status == expected_status, f'{method} {path}: expected HTTP {expected_status}, got {status}; body={raw[:300]!r}')
    check('application/json' in ctype.lower(), f'{method} {path}: expected JSON error, got {ctype!r}')
    check(isinstance(parsed, dict), f'{method} {path}: expected a JSON error object')
    error = parsed.get('error', {})
    check(error.get('code') == expected_code, f'{method} {path}: expected {expected_code}, got {error!r}')
    check(isinstance(error.get('message'), str) and error['message'], f'{method} {path}: error message required')
    return error


def ensure_home(base_url):
    status, parsed, raw, ctype = request(base_url, 'GET', '/api/home')
    if status == 404:
        check(isinstance(parsed, dict) and parsed.get('error', {}).get('code') == 'HOME_NOT_FOUND', 'fresh GET /api/home must be HOME_NOT_FOUND')
        return api(base_url, 'POST', '/api/home', {'name': 'Probe home ' + SUFFIX, 'address': '1 Probe Lane'}, 201)['home']
    check(status == 200, f'GET /api/home: expected 200 or 404, got {status}')
    check(isinstance(parsed, dict), 'GET /api/home: expected a JSON object')
    return parsed['home']


def create_equipment(base_url, home_id, tag, category='heating'):
    payload = {'home_id': home_id, 'name': 'Probe equipment ' + tag + ' ' + SUFFIX, 'category': category, 'location': 'Test area', 'installed_on': '2020-02-29'}
    return api(base_url, 'POST', '/api/equipment', payload, 201)['equipment']


def list_equipment(base_url, home_id):
    query = urllib.parse.urlencode({'home_id': home_id})
    return api(base_url, 'GET', '/api/equipment?' + query)['equipment']


def create_plan(base_url, home_id, tag, interval_days, equipment_id=None, first_due_on=None, last_completed_on=None):
    payload = {'home_id': home_id, 'name': 'Probe plan ' + tag + ' ' + SUFFIX, 'interval_days': interval_days}
    if equipment_id is not None:
        payload['equipment_id'] = equipment_id
    if first_due_on is not None:
        payload['first_due_on'] = first_due_on
    if last_completed_on is not None:
        payload['last_completed_on'] = last_completed_on
    return api(base_url, 'POST', '/api/plans', payload, 201)['plan']


def list_plans(base_url, home_id, equipment_id=None):
    params = {'home_id': home_id}
    if equipment_id is not None:
        params['equipment_id'] = equipment_id
    return api(base_url, 'GET', '/api/plans?' + urllib.parse.urlencode(params))['plans']


def get_plan(base_url, plan_id):
    return api(base_url, 'GET', '/api/plans/' + plan_id)['plan']


def due_path(home_id, as_of, horizon_days=0, equipment_id=None):
    params = {'home_id': home_id, 'as_of': as_of, 'horizon_days': str(horizon_days)}
    if equipment_id is not None:
        params['equipment_id'] = equipment_id
    return '/api/tasks/due?' + urllib.parse.urlencode(params)


def due_tasks(base_url, home_id, as_of, horizon_days=0, equipment_id=None):
    return api(base_url, 'GET', due_path(home_id, as_of, horizon_days, equipment_id))['tasks']


def check_task_ids(tasks, expected_ids, context):
    ids = [task['id'] for task in tasks]
    check(len(ids) == len(expected_ids), f'{context}: expected {len(expected_ids)} tasks, got {len(ids)}: {ids}')
    check(len(set(ids)) == len(ids), f'{context}: duplicate task ids in {ids}')
    check(set(ids) == set(expected_ids), f'{context}: expected ids {sorted(expected_ids)}, got {sorted(ids)}')


def create_completion(base_url, plan_id, completed_on, note=''):
    payload = {'completed_on': completed_on, 'note': note}
    return api(base_url, 'POST', '/api/plans/' + plan_id + '/completions', payload, 201)


def list_completions(base_url, plan_id):
    return api(base_url, 'GET', '/api/plans/' + plan_id + '/completions')['completions']


def history_path(home_id, equipment_id=None, limit=None):
    params = {'home_id': home_id}
    if equipment_id is not None:
        params['equipment_id'] = equipment_id
    if limit is not None:
        params['limit'] = str(limit)
    return '/api/history?' + urllib.parse.urlencode(params)


def history_entries(base_url, home_id, equipment_id=None, limit=None):
    return api(base_url, 'GET', history_path(home_id, equipment_id, limit))['history']


def case_a01(base_url):
    health = api(base_url, 'GET', '/health')
    check(health.get('status') == 'ok', 'health status must be ok')
    home = ensure_home(base_url)
    check(home.get('id') == 'home', 'single home id must be home')
    for field in ('name', 'address', 'created_at', 'updated_at'):
        check(field in home, 'home missing field ' + field)
    before = api(base_url, 'GET', '/api/home')['home']
    expect_error(base_url, 'POST', '/api/home', {'name': 'Second home', 'address': ''}, 409, 'HOME_EXISTS')
    after = api(base_url, 'GET', '/api/home')['home']
    check(after == before, 'duplicate home must not mutate stored home')
    patched = api(base_url, 'PATCH', '/api/home', {'name': before['name'], 'address': before['address']})['home']
    check(patched['id'] == 'home' and patched['name'] == before['name'] and patched['address'] == before['address'], 'home patch round trip failed')
    expect_error(base_url, 'PATCH', '/api/home', {}, 422, 'VALIDATION_ERROR')
    check(api(base_url, 'GET', '/api/home')['home'] == patched, 'empty patch must not mutate the patched home object')
    equipment = create_equipment(base_url, home['id'], 'A01')
    check(equipment['home_id'] == home['id'], 'equipment must be anchored to home')
    check(equipment['installed_on'] == '2020-02-29', 'equipment date round trip failed')
    detail = api(base_url, 'GET', '/api/equipment/' + equipment['id'])['equipment']
    check(detail == equipment, 'equipment detail must match creation')
    before_equipment = list_equipment(base_url, home['id'])
    check(any(item['id'] == equipment['id'] for item in before_equipment), 'created equipment must be listed')
    expect_error(base_url, 'POST', '/api/equipment', {'home_id': home['id'], 'name': '   ', 'category': 'heating'}, 422, 'VALIDATION_ERROR')
    check(list_equipment(base_url, home['id']) == before_equipment, 'blank equipment name must write nothing')
    expect_error(base_url, 'POST', '/api/equipment', {'home_id': home['id'], 'name': 'Probe bad category ' + SUFFIX, 'category': 'not-a-category'}, 422, 'VALIDATION_ERROR')
    check(list_equipment(base_url, home['id']) == before_equipment, 'invalid equipment category must write nothing')
    expect_error(base_url, 'POST', '/api/equipment', {'home_id': 'missing-home', 'name': 'Ghost', 'category': 'other'}, 404, 'HOME_NOT_FOUND')
    check(list_equipment(base_url, home['id']) == before_equipment, 'unknown home must write nothing')
    expect_error(base_url, 'GET', '/api/equipment', None, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'GET', '/api/equipment?home_id=missing-home', None, 404, 'HOME_NOT_FOUND')
    expect_error(base_url, 'GET', '/api/equipment/eq_missing', None, 404, 'EQUIPMENT_NOT_FOUND')


def case_a02(base_url):
    home = ensure_home(base_url)
    equipment = create_equipment(base_url, home['id'], 'A02')
    other_equipment = create_equipment(base_url, home['id'], 'A02X')
    baseline = len(list_plans(base_url, home['id']))
    far = create_plan(base_url, home['id'], 'A02F', 90, equipment_id=equipment['id'], first_due_on='2026-03-01')
    old = create_plan(base_url, home['id'], 'A02O', 30, equipment_id=equipment['id'], first_due_on='2026-01-01')
    decoy = create_plan(base_url, home['id'], 'A02X', 10, equipment_id=other_equipment['id'], first_due_on='2026-02-01')
    check(far['due_on'] == '2026-03-01', 'first_due_on must be preserved')
    check(far['equipment_id'] == equipment['id'], 'plan equipment anchor lost')
    check(old['due_on'] == '2026-01-01', 'second plan due date wrong')
    check(decoy['equipment_id'] == other_equipment['id'], 'decoy plan equipment anchor lost')
    for interval in (0, 3651, -1):
        expect_error(base_url, 'POST', '/api/plans', {'home_id': home['id'], 'name': 'Bad interval ' + SUFFIX, 'interval_days': interval}, 422, 'VALIDATION_ERROR')
    for interval in (1.5, True, '30'):
        expect_error(base_url, 'POST', '/api/plans', {'home_id': home['id'], 'name': 'Bad type ' + SUFFIX, 'interval_days': interval}, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'POST', '/api/plans', {'home_id': home['id'], 'name': 'Two anchors ' + SUFFIX, 'interval_days': 10, 'last_completed_on': '2025-01-01', 'first_due_on': '2025-02-01'}, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'POST', '/api/plans', {'home_id': home['id'], 'name': 'Bad date ' + SUFFIX, 'interval_days': 10, 'first_due_on': '2026-02-30'}, 422, 'VALIDATION_ERROR')
    check(len(list_plans(base_url, home['id'])) == baseline + 3, 'invalid plans must not be stored')
    tasks = due_tasks(base_url, home['id'], '2026-02-28', 0, equipment['id'])
    check_task_ids(tasks, [old['id']], 'horizon zero before far due')
    by_id = {task['id']: task for task in tasks}
    check(by_id[old['id']]['status'] == 'overdue', 'old plan must be overdue on 2026-02-28')
    check(far['id'] not in by_id, 'future plan must be excluded at horizon zero')
    tasks = due_tasks(base_url, home['id'], '2026-03-01', 0, equipment['id'])
    check_task_ids(tasks, [old['id'], far['id']], 'as_of on far due date')
    by_id = {task['id']: task for task in tasks}
    check(by_id[old['id']]['status'] == 'overdue', 'old plan still overdue on 2026-03-01')
    check(by_id[far['id']]['status'] == 'due' and by_id[far['id']]['days_until_due'] == 0, 'far plan must be due on its due date')
    tasks = due_tasks(base_url, home['id'], '2026-02-28', 1, equipment['id'])
    check_task_ids(tasks, [old['id'], far['id']], 'horizon one before far due')
    by_id = {task['id']: task for task in tasks}
    check(by_id[far['id']]['status'] == 'upcoming' and by_id[far['id']]['days_until_due'] == 1, 'horizon one must expose tomorrow as upcoming')
    check(by_id[old['id']]['status'] == 'overdue', 'horizon one must keep old plan overdue')
    tasks = due_tasks(base_url, home['id'], '2026-03-02', 0, equipment['id'])
    check_task_ids(tasks, [old['id'], far['id']], 'day after far due')
    by_id = {task['id']: task for task in tasks}
    check(by_id[far['id']]['status'] == 'overdue' and by_id[far['id']]['days_until_due'] == -1, 'next day must be overdue')
    ordered = due_tasks(base_url, home['id'], '2026-03-01', 0, equipment['id'])
    check_task_ids(ordered, [old['id'], far['id']], 'ordered due query')
    check([task['id'] for task in ordered] == [old['id'], far['id']], 'due tasks must sort by due_on')
    dates = [task['due_on'] for task in ordered]
    check(dates == sorted(dates), 'due tasks must sort by due_on')
    filtered = due_tasks(base_url, home['id'], '2026-03-01', 0, other_equipment['id'])
    check_task_ids(filtered, [decoy['id']], 'other equipment due filter')
    check(filtered[0]['status'] == 'overdue', 'decoy plan must stay overdue in its own scope')
    filtered_plans = list_plans(base_url, home['id'], equipment['id'])
    check(len(filtered_plans) == 2, 'plan equipment filter must return exactly two plans')
    check({plan['id'] for plan in filtered_plans} == {old['id'], far['id']}, 'plan equipment filter must isolate the fresh scope')
    other_plans = list_plans(base_url, home['id'], other_equipment['id'])
    check([plan['id'] for plan in other_plans] == [decoy['id']], 'plan equipment filter must isolate the decoy scope')
    detail = get_plan(base_url, far['id'])
    check(detail['due_on'] == '2026-03-01' and detail['completion_count'] == 0, 'plan detail must expose due date and count')
    for as_of, horizon in (('2026-02-30', 0), ('2026-02-29', 0), ('2026-03-01', -1), ('2026-03-01', 366)):
        expect_error(base_url, 'GET', due_path(home['id'], as_of, horizon, equipment['id']), None, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'GET', '/api/tasks/due?as_of=2026-03-01', None, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'GET', due_path('missing-home', '2026-03-01', 0, equipment['id']), None, 404, 'HOME_NOT_FOUND')
    check(len(list_plans(base_url, home['id'])) == baseline + 3, 'due query errors must not write plans')


def case_a03(base_url):
    home = ensure_home(base_url)
    equipment = create_equipment(base_url, home['id'], 'A03')
    plan = create_plan(base_url, home['id'], 'A03', 30, equipment_id=equipment['id'], first_due_on='2024-01-01')
    before_plan = get_plan(base_url, plan['id'])
    before_logs = list_completions(base_url, plan['id'])
    future = (dt.date.today() + dt.timedelta(days=2)).isoformat()
    expect_error(base_url, 'POST', '/api/plans/' + plan['id'] + '/completions', {'completed_on': future, 'note': 'future'}, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'POST', '/api/plans/' + plan['id'] + '/completions', {'completed_on': '2026-02-30', 'note': 'bad'}, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'POST', '/api/plans/' + plan['id'] + '/completions', {'completed_on': '2025-01-01', 'note': 'x' * 501}, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'POST', '/api/plans/pl_missing/completions', {'completed_on': '2025-01-01', 'note': ''}, 404, 'PLAN_NOT_FOUND')
    check(get_plan(base_url, plan['id']) == before_plan, 'invalid completions must not change plan')
    check(list_completions(base_url, plan['id']) == before_logs, 'invalid completions must not append history')
    first = create_completion(base_url, plan['id'], '2024-02-29', '  Leap-day check  ')
    check(first['completion']['note'] == 'Leap-day check', 'note must be trimmed')
    check(first['plan']['last_completed_on'] == '2024-02-29', 'leap completion must set last date')
    check(first['plan']['due_on'] == '2024-03-30', 'leap completion must advance thirty days')
    check(first['plan']['completion_count'] == len(before_logs) + 1, 'completion count must increment')
    back = create_completion(base_url, plan['id'], '2024-01-15', 'Backdated')
    check(back['plan']['last_completed_on'] == '2024-02-29', 'backdated completion must not regress last date')
    check(back['plan']['due_on'] == '2024-03-30', 'backdated completion must not regress due date')
    year = create_completion(base_url, plan['id'], '2024-12-31', 'Year end')
    check(year['plan']['due_on'] == '2025-01-30', 'year-end plus thirty days failed')
    month_plan = create_plan(base_url, home['id'], 'A03M', 31, first_due_on='2024-01-01')
    month = create_completion(base_url, month_plan['id'], '2026-01-31', 'Month end')
    check(month['plan']['due_on'] == '2026-03-03', 'month-end plus thirty-one days failed')
    leap_plan = create_plan(base_url, home['id'], 'A03L', 1, first_due_on='2024-02-28')
    leap_one = create_completion(base_url, leap_plan['id'], '2024-02-28', 'Leap start')
    check(leap_one['plan']['due_on'] == '2024-02-29', 'leap day plus one day failed')
    leap_two = create_completion(base_url, leap_plan['id'], '2024-02-29', 'Leap day')
    check(leap_two['plan']['due_on'] == '2024-03-01', 'post-leap day plus one day failed')
    note_plan = create_plan(base_url, home['id'], 'A03N', 10, first_due_on='2025-01-01')
    note_result = create_completion(base_url, note_plan['id'], '2025-01-01', 'x' * 500)
    check(len(note_result['completion']['note']) == 500, 'five hundred code point note must be accepted')
    backfill = create_plan(base_url, home['id'], 'A03B', 30, first_due_on='2026-03-01')
    check(backfill['due_on'] == '2026-03-01', 'initial backfill plan due date wrong')
    backfilled = create_completion(base_url, backfill['id'], '2025-01-01', 'Initial backfill')
    check(backfilled['plan']['last_completed_on'] == '2025-01-01', 'initial backfill must store the actual completion as latest')
    check(backfilled['plan']['due_on'] == '2026-03-01', 'initial backfill must keep the existing due date')
    backfill_logs = list_completions(base_url, backfill['id'])
    check([entry['completed_on'] for entry in backfill_logs] == ['2025-01-01'], 'initial backfill must append the actual completion date')
    check(backfill_logs[0]['note'] == 'Initial backfill', 'initial backfill must append the note')
    today = dt.date.today().isoformat()
    anchorless = create_plan(base_url, home['id'], 'A03D', 30)
    check(anchorless['due_on'] == today, 'no-anchor plan must be due on creation day')
    anchorless_back = create_completion(base_url, anchorless['id'], '2025-01-01', 'No anchor backfill')
    check(anchorless_back['plan']['last_completed_on'] == '2025-01-01', 'no-anchor plan must store the actual completion as latest')
    check(anchorless_back['plan']['due_on'] == today, 'no-anchor backfill must keep the creation-day due date')
    anchorless_today = create_completion(base_url, anchorless['id'], today, 'No anchor today')
    check(anchorless_today['plan']['last_completed_on'] == today, 'latest completion must win over an older completion')
    check(anchorless_today['plan']['due_on'] == (dt.date.today() + dt.timedelta(days=30)).isoformat(), 'no-anchor completion must advance from the latest date')
    logs = list_completions(base_url, plan['id'])
    dates = [entry['completed_on'] for entry in logs]
    check(dates == ['2024-12-31', '2024-02-29', '2024-01-15'], 'plan history order failed')


def case_a04(base_url):
    home = ensure_home(base_url)
    eq_a = create_equipment(base_url, home['id'], 'A04A', 'heating')
    eq_b = create_equipment(base_url, home['id'], 'A04B', 'plumbing')
    plan_a = create_plan(base_url, home['id'], 'A04A', 10, equipment_id=eq_a['id'], first_due_on='2025-01-01')
    plan_b = create_plan(base_url, home['id'], 'A04B', 20, equipment_id=eq_b['id'], first_due_on='2025-01-01')
    create_plan(base_url, home['id'], 'A04C', 30, first_due_on='2025-01-01')
    c_a1 = create_completion(base_url, plan_a['id'], '2025-01-10', '  A one  ')['completion']
    c_a2 = create_completion(base_url, plan_a['id'], '2025-02-10', 'A two')['completion']
    c_b1 = create_completion(base_url, plan_b['id'], '2025-02-15', 'B one')['completion']
    check(c_a1['note'] == 'A one', 'history note must be trimmed')
    entries = history_entries(base_url, home['id'], limit=500)
    for left, right in zip(entries, entries[1:]):
        check(left['completed_on'] >= right['completed_on'], 'history must sort by completed_on descending')
    positions = {entry['id']: index for index, entry in enumerate(entries)}
    check(positions[c_b1['id']] < positions[c_a2['id']] < positions[c_a1['id']], 'history ordering across plans failed')
    for completion in (c_a1, c_a2, c_b1):
        entry = entries[positions[completion['id']]]
        for field in ('plan_id', 'plan_name', 'home_id', 'home_name', 'equipment_id', 'equipment_name', 'completed_on', 'note', 'created_at'):
            check(field in entry, 'history entry missing field ' + field)
    filtered_a = history_entries(base_url, home['id'], eq_a['id'], 500)
    ids_a = {entry['id'] for entry in filtered_a}
    check(c_a1['id'] in ids_a and c_a2['id'] in ids_a and c_b1['id'] not in ids_a, 'equipment A history filter failed')
    check(all(entry['equipment_id'] == eq_a['id'] for entry in filtered_a), 'equipment A filter leaked another equipment')
    filtered_b = history_entries(base_url, home['id'], eq_b['id'], 500)
    ids_b = {entry['id'] for entry in filtered_b}
    check(c_b1['id'] in ids_b and c_a1['id'] not in ids_b, 'equipment B history filter failed')
    plan_logs = list_completions(base_url, plan_a['id'])
    check([entry['completed_on'] for entry in plan_logs] == ['2025-02-10', '2025-01-10'], 'plan completion history order failed')
    limited = history_entries(base_url, home['id'], limit=1)
    check(len(limited) == 1, 'history limit one failed')
    before_count = len(list_plans(base_url, home['id']))
    expect_error(base_url, 'GET', '/api/history', None, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'GET', history_path('missing-home'), None, 404, 'HOME_NOT_FOUND')
    expect_error(base_url, 'GET', history_path(home['id'], 'eq_missing'), None, 404, 'EQUIPMENT_NOT_FOUND')
    expect_error(base_url, 'GET', history_path(home['id'], limit=0), None, 422, 'VALIDATION_ERROR')
    expect_error(base_url, 'GET', history_path(home['id'], limit=501), None, 422, 'VALIDATION_ERROR')
    check(len(list_plans(base_url, home['id'])) == before_count, 'history errors must not write plans')


class UIParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html_lang = None
        self.input_ids = []
        self.label_targets = set()
        self.fieldsets = []
        self.closed_fieldsets = []
        self.tables = []
        self.closed_tables = []
        self.status_regions = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html' and self.html_lang is None:
            self.html_lang = attrs.get('lang')
        if tag == 'label' and attrs.get('for'):
            self.label_targets.add(attrs['for'])
        if tag == 'input':
            self.input_ids.append(attrs.get('id'))
        if tag == 'fieldset':
            self.fieldsets.append({'has_legend': False})
        if tag == 'legend' and self.fieldsets:
            self.fieldsets[-1]['has_legend'] = True
        if tag == 'table':
            self.tables.append({'caption': '', 'in_caption': False, 'th_scopes': []})
        if tag == 'caption' and self.tables:
            self.tables[-1]['in_caption'] = True
        if tag == 'th' and self.tables:
            self.tables[-1]['th_scopes'].append(attrs.get('scope'))
        if (attrs.get('role') or '').lower() == 'status':
            self.status_regions.append({'aria_live': attrs.get('aria-live')})

    def handle_endtag(self, tag):
        if tag == 'fieldset' and self.fieldsets:
            self.closed_fieldsets.append(self.fieldsets.pop())
        if tag == 'caption' and self.tables:
            self.tables[-1]['in_caption'] = False
        if tag == 'table' and self.tables:
            self.closed_tables.append(self.tables.pop())

    def handle_data(self, data):
        if self.tables and self.tables[-1]['in_caption']:
            self.tables[-1]['caption'] += data


def case_a05(base_url):
    status, parsed, raw, ctype = request(base_url, 'GET', '/')
    check(status == 200, f'GET /: expected 200, got {status}')
    check('text/html' in ctype.lower(), f'GET /: expected HTML, got {ctype!r}')
    document = raw.decode('utf-8')
    text = document.lower()
    for token in ('<html lang=', '<label', '<form', '<button', 'aria-live', 'home', 'equipment', 'due', 'history', 'complete'):
        check(token in text, 'UI missing token ' + token)
    check('<script src=' not in text, 'UI must not load external scripts')
    parser = UIParser()
    parser.feed(document)
    parser.close()
    check((parser.html_lang or '').lower() == 'en', 'html lang must be en')
    check(parser.input_ids, 'UI must contain form inputs')
    for input_id in parser.input_ids:
        check(input_id, 'every input must have an id')
        check(input_id in parser.label_targets, 'input ' + input_id + ' must have a matching label for')
    check(parser.closed_fieldsets, 'UI must group fields with fieldset')
    check(all(item['has_legend'] for item in parser.closed_fieldsets), 'every fieldset must contain a legend')
    due_tables = [table for table in parser.closed_tables if 'due' in table['caption'].lower()]
    check(due_tables, 'UI must have a due table with a caption')
    for table in due_tables:
        check(table['th_scopes'], 'due table must use th cells')
        check(all((scope or '').lower() == 'col' for scope in table['th_scopes']), 'every due table th must use scope=col')
    check(parser.status_regions, 'UI must include a state feedback region')
    check(any((region['aria_live'] or '').lower() == 'polite' for region in parser.status_regions), 'state feedback region must use aria-live=polite')
    health = api(base_url, 'GET', '/health')
    check(health.get('status') == 'ok', 'health status must be ok')
    expect_error(base_url, 'GET', '/api/unknown', None, 404, 'NOT_FOUND')
    expect_error(base_url, 'DELETE', '/api/home', None, 405, 'METHOD_NOT_ALLOWED')


CASES = {'A01': case_a01, 'A02': case_a02, 'A03': case_a03, 'A04': case_a04, 'A05': case_a05}


def main():
    parser = argparse.ArgumentParser(description='Home Care Ledger acceptance probe')
    parser.add_argument('--base-url', default='http://127.0.0.1:8765')
    parser.add_argument('--case', required=True, choices=sorted(CASES))
    args = parser.parse_args()
    try:
        CASES[args.case](args.base_url)
    except ProbeFailure as exc:
        print('FAIL ' + args.case + ': ' + str(exc))
        return 1
    except Exception as exc:
        print('ERROR ' + args.case + ': ' + type(exc).__name__ + ': ' + str(exc))
        return 1
    print('PASS ' + args.case)
    return 0


if __name__ == '__main__':
    sys.exit(main())
