#!/usr/bin/env python3
'''Acceptance orchestrator for the daily-expense / monthly-category web target.

Covers A01-A05 of the leaf acceptance set. Python standard library only. It
does not implement the target: it drives the target and inspects what the
target persisted.

Mode 1 (recommended, the probe manages the process):
    python3 probe.py --server-cmd './expense-tracker --addr {ADDR} --data-dir {DATA_DIR}'
The probe creates a disposable temporary data directory, starts the target on
it, runs A01-A04, stops the process, starts it again on the same directory and
finishes with A05 (reopen persistence).

Mode 2 (already running instance):
    python3 probe.py --base-url http://127.0.0.1:8099 --allow-write --store-file /path/store.json
--allow-write is mandatory because the probe writes probe-* records. The
process-restart leg of A05 is reported as not_run in this mode; restart the
target by hand and re-run with --phase persist to check the reopened data.

The probe only writes inside its own temporary directory (or the directory the
operator points it at) and never deletes existing records.
'''
import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

PASS = 'PASS'
FAIL = 'FAIL'
SKIP = 'NOT_RUN'
CATEGORIES = ['probe-餐饮', 'probe-交通', 'probe-购物']
RENAME = CATEGORIES[1] + '出行'
MONTHS = ['2026-09', '2026-10', '2026-11', '2026-12']


class Failure(Exception):
    '''An assertion inside an acceptance case failed.'''


def fail(message):
    raise Failure(message)


def req(method, url, payload=None, timeout=20):
    '''Return (status, parsed_body) for one JSON HTTP call.'''
    data = None
    headers = {'Accept': 'application/json'}
    if payload is not None:
        data = json.dumps(payload).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8', 'replace')
            status = resp.status
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode('utf-8', 'replace')
        status = exc.code
    body = None
    if raw.strip():
        try:
            body = json.loads(raw)
        except ValueError:
            body = {'raw': raw}
    return status, body


def get_html(url, timeout=20):
    '''Return (status, content_type, text) for one HTML request.'''
    request = urllib.request.Request(url, headers={'Accept': 'text/html'}, method='GET')
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            return resp.status, resp.headers.get('Content-Type', ''), resp.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as exc:
        return exc.code, exc.headers.get('Content-Type', ''), exc.read().decode('utf-8', 'replace')


def expect(status, body, want, what):
    if status != want:
        fail('%s: expected HTTP %d, got %d, body=%s' % (what, want, status, json.dumps(body, ensure_ascii=False)[:300]))
    return body


def wait_healthy(base_url, timeout=30):
    deadline = time.time() + timeout
    last = 'no answer'
    while time.time() < deadline:
        try:
            status, body = req('GET', base_url + '/api/health', timeout=3)
            if status == 200:
                return body
            last = 'HTTP %d' % status
        except Exception as exc:
            last = repr(exc)
        time.sleep(0.25)
    fail('target did not become healthy at %s (%s)' % (base_url, last))


class Target(object):
    '''Runs the target process against a disposable data directory.'''

    def __init__(self, command, addr, data_dir):
        self.command = command
        self.addr = addr
        self.data_dir = data_dir
        self.proc = None
        self.log = None

    @property
    def base_url(self):
        return 'http://' + self.addr

    def argv(self):
        argv = []
        for token in shlex.split(self.command):
            token = token.replace('{ADDR}', self.addr).replace('{DATA_DIR}', self.data_dir)
            argv.append(token)
        return argv

    def start(self):
        env = dict(os.environ)
        env['DATA_DIR'] = self.data_dir
        env['EXPENSE_ADDR'] = self.addr
        self.log = tempfile.NamedTemporaryFile(prefix='expense-probe-log-', suffix='.txt', delete=False)
        self.proc = subprocess.Popen(self.argv(), stdout=self.log, stderr=subprocess.STDOUT, env=env)
        wait_healthy(self.base_url, 30)

    def stop(self):
        if self.proc is not None and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait(timeout=10)
        self.proc = None
        if self.log is not None:
            self.log.close()
            self.log = None


def snapshot(base_url, months):
    '''Capture the observable state of the target for later comparison.'''
    status, body = req('GET', base_url + '/api/categories')
    expect(status, body, 200, 'snapshot categories')
    result = {'categories': body.get('categories')}
    for month in months:
        status, body = req('GET', base_url + '/api/expenses?month=' + month)
        expect(status, body, 200, 'snapshot ' + month)
        result[month] = {
            'total_cents': body.get('total_cents'),
            'total_display': body.get('total_display'),
            'by_category': body.get('by_category'),
            'expenses': body.get('expenses'),
        }
    return result


def breakdown(body):
    '''Turn a summary by_category array into a category -> cents mapping.'''
    totals = {}
    for row in body.get('by_category', []) or []:
        totals[row.get('category')] = row.get('total_cents')
    return totals


def case_a01(ctx):
    '''A01 categories: create, rename, conflict and rejection semantics.'''
    base = ctx['base_url']
    status, body = req('GET', base + '/api/categories')
    expect(status, body, 200, 'initial category list')
    initial = body.get('categories')
    if not isinstance(initial, list):
        fail('GET /api/categories did not return a categories array')
    for name in CATEGORIES:
        status, body = req('POST', base + '/api/categories', {'name': name})
        expect(status, body, 201, 'create category ' + name)
    status, body = req('GET', base + '/api/categories')
    expect(status, body, 200, 'category list after create')
    names = body.get('categories')
    for name in CATEGORIES:
        if name not in names:
            fail('category %s is missing after create' % name)
    if len(names) != len(initial) + len(CATEGORIES):
        fail('category count after create is %d, expected %d' % (len(names), len(initial) + len(CATEGORIES)))
    status, body = req('POST', base + '/api/categories', {'name': CATEGORIES[0]})
    if status != 409:
        fail('duplicate category: expected HTTP 409, got %d' % status)
    for bad in ('', '   ', 'x' * 21):
        status, body = req('POST', base + '/api/categories', {'name': bad})
        if status != 400:
            fail('invalid category %r: expected HTTP 400, got %d' % (bad, status))
    status, body = req('PATCH', base + '/api/categories/' + urllib.parse.quote(CATEGORIES[1]), {'name': RENAME})
    expect(status, body, 200, 'rename category')
    status, body = req('GET', base + '/api/categories')
    names = body.get('categories')
    if RENAME not in names:
        fail('renamed category %s is missing' % RENAME)
    if CATEGORIES[1] in names:
        fail('old category %s is still listed after the rename' % CATEGORIES[1])
    status, body = req('PATCH', base + '/api/categories/' + urllib.parse.quote('probe-不存在'), {'name': 'probe-其它'})
    if status != 404:
        fail('rename of an unknown category: expected HTTP 404, got %d' % status)
    status, body = req('PATCH', base + '/api/categories/' + urllib.parse.quote(CATEGORIES[0]), {'name': CATEGORIES[2]})
    if status != 409:
        fail('rename onto an existing name: expected HTTP 409, got %d' % status)
    status, body = req('DELETE', base + '/api/categories/' + urllib.parse.quote(CATEGORIES[0]))
    if status != 405:
        fail('delete category: expected HTTP 405, got %d' % status)
    status, body = req('GET', base + '/api/categories')
    final = body.get('categories')
    if len(final) != len(initial) + len(CATEGORIES):
        fail('category count changed after rejected calls: %d' % len(final))
    if sorted(final) != sorted(names):
        fail('category list changed after rejected calls')
    ctx['state']['categories'] = final


def case_a02(ctx):
    '''A02 record expenses: positive integer-cent amounts, real calendar dates.'''
    base = ctx['base_url']
    ids = {}
    plan = [
        ('2026-10-05', 2350, CATEGORIES[0], 'probe: lunch 23.50'),
        ('2026-10-12', 1500, CATEGORIES[0], 'probe: delivery 15.00'),
        ('2026-10-20', 900, RENAME, 'probe: metro 9.00'),
        ('2026-09-28', 4200, CATEGORIES[2], 'probe: supplies 42.00'),
        ('2026-11-02', 600, CATEGORIES[2], 'probe: next month 6.00'),
    ]
    for date, cents, category, note in plan:
        payload = {'date': date, 'amount_cents': cents, 'category': category, 'note': note}
        status, body = req('POST', base + '/api/expenses', payload)
        expect(status, body, 201, 'create expense on ' + date)
        expense = body.get('expense') if isinstance(body, dict) else None
        if not isinstance(expense, dict):
            fail('POST /api/expenses returned no expense object: %s' % json.dumps(body, ensure_ascii=False)[:200])
        for key in ('id', 'date', 'amount_cents', 'category', 'note'):
            if key not in expense:
                fail('created expense is missing the field %s' % key)
        if type(expense['amount_cents']) is not int:
            fail('amount_cents must be an int, got %r' % (expense['amount_cents'],))
        if expense['amount_cents'] != cents:
            fail('amount_cents round trip failed: %r != %d' % (expense['amount_cents'], cents))
        if expense['date'] != date:
            fail('date round trip failed: %r != %s' % (expense['date'], date))
        if expense['category'] != category:
            fail('category round trip failed: %r != %s' % (expense['category'], category))
        if expense['note'] != note:
            fail('note round trip failed: %r != %s' % (expense['note'], note))
        if not isinstance(expense['id'], str) or not expense['id']:
            fail('the expense id must be a non-empty string')
        ids[date] = expense['id']
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    expect(status, body, 200, 'october summary')
    if body.get('total_cents') != 4750:
        fail('october total_cents is %r, expected 4750' % (body.get('total_cents'),))
    if len(body.get('expenses', []) or []) != 3:
        fail('october should hold 3 records, found %d' % len(body.get('expenses', []) or []))
    bad_payloads = [
        {'date': '2026-10-05', 'amount_cents': 0, 'category': CATEGORIES[0]},
        {'date': '2026-10-05', 'amount_cents': -100, 'category': CATEGORIES[0]},
        {'date': '2026-10-05', 'amount_cents': 12.5, 'category': CATEGORIES[0]},
        {'date': '2026-10-05', 'amount_cents': '2350', 'category': CATEGORIES[0]},
        {'date': '2026-10-05', 'category': CATEGORIES[0]},
        {'date': '2026-13-01', 'amount_cents': 100, 'category': CATEGORIES[0]},
        {'date': '2026-02-30', 'amount_cents': 100, 'category': CATEGORIES[0]},
        {'date': '2026-10-5', 'amount_cents': 100, 'category': CATEGORIES[0]},
        {'date': '2026-10-05', 'amount_cents': 100, 'category': 'probe-不存在'},
        {'date': '2026-10-05', 'amount_cents': 100, 'category': CATEGORIES[0], 'note': 'n' * 61},
    ]
    for payload in bad_payloads:
        status, body = req('POST', base + '/api/expenses', payload)
        if status != 400:
            fail('invalid expense %s: expected HTTP 400, got %d (%s)' % (json.dumps(payload, ensure_ascii=False)[:120], status, json.dumps(body, ensure_ascii=False)[:200]))
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    if body.get('total_cents') != 4750 or len(body.get('expenses', []) or []) != 3:
        fail('rejected expenses changed the october summary: total=%r rows=%d' % (body.get('total_cents'), len(body.get('expenses', []) or [])))
    ctx['state']['ids'] = ids


def case_a03(ctx):
    '''A03 corrections recompute the selected month immediately.'''
    base = ctx['base_url']
    ids = ctx['state'].get('ids')
    if not ids:
        fail('A02 did not complete, no recorded expense ids are available')
    target = ids['2026-10-05']
    url = base + '/api/expenses/' + urllib.parse.quote(target)
    status, body = req('PATCH', url, {'amount_cents': 3000})
    expect(status, body, 200, 'edit the amount')
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    if body.get('total_cents') != 5400:
        fail('after the amount edit the october total is %r, expected 5400' % (body.get('total_cents'),))
    totals = breakdown(body)
    if totals.get(CATEGORIES[0]) != 3000:
        fail('the category total after the amount edit is %r, expected 3000' % (totals.get(CATEGORIES[0]),))
    status, body = req('PATCH', url, {'category': CATEGORIES[2]})
    expect(status, body, 200, 'edit the category')
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    totals = breakdown(body)
    if totals.get(CATEGORIES[0]) != 1500 or totals.get(CATEGORIES[2]) != 3000:
        fail('the category totals after the recategorisation are %s' % json.dumps(totals, ensure_ascii=False))
    status, body = req('PATCH', url, {'note': 'probe: corrected lunch'})
    expect(status, body, 200, 'edit the note')
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    if body.get('total_cents') != 5400:
        fail('a note only edit changed the october total')
    status, body = req('PATCH', url, {'date': '2026-11-03'})
    expect(status, body, 200, 'edit the date')
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    if body.get('total_cents') != 2400:
        fail('the october total after moving a record to november is %r, expected 2400' % (body.get('total_cents'),))
    for expense in body.get('expenses', []) or []:
        if expense.get('id') == target:
            fail('the moved record is still listed under october')
    status, body = req('GET', base + '/api/expenses?month=2026-11')
    if body.get('total_cents') != 3600:
        fail('the november total after the move is %r, expected 3600' % (body.get('total_cents'),))
    moved = [e for e in body.get('expenses', []) or [] if e.get('id') == target]
    if len(moved) != 1 or moved[0].get('date') != '2026-11-03' or moved[0].get('amount_cents') != 3000:
        fail('the moved record was not found intact in the november details')
    status, body = req('PATCH', base + '/api/categories/' + urllib.parse.quote(CATEGORIES[2]), {'name': 'probe-采购'})
    expect(status, body, 200, 'rename a category that has history')
    status, body = req('GET', base + '/api/expenses?month=2026-11')
    totals = breakdown(body)
    if totals.get('probe-采购') != 3600:
        fail('after the rename the november category totals are %s' % json.dumps(totals, ensure_ascii=False))
    if CATEGORIES[2] in totals:
        fail('the old category name is still part of the summary after the rename')
    status, body = req('GET', base + '/api/expenses?month=2026-09')
    totals = breakdown(body)
    if totals.get('probe-采购') != 4200:
        fail('after the rename the september category totals are %s' % json.dumps(totals, ensure_ascii=False))
    invalid = [({'amount_cents': 0}, 400), ({'amount_cents': -5}, 400), ({'amount_cents': 1.5}, 400), ({'date': '2026-11-31'}, 400), ({'category': 'probe-不存在'}, 400), ({}, 400)]
    for payload, want in invalid:
        status, body = req('PATCH', url, payload)
        if status != want:
            fail('invalid patch %s: expected HTTP %d, got %d' % (json.dumps(payload, ensure_ascii=False), want, status))
    status, body = req('PATCH', base + '/api/expenses/exp_does_not_exist', {'amount_cents': 100})
    if status != 404:
        fail('patch of an unknown id: expected HTTP 404, got %d' % status)
    status, body = req('GET', base + '/api/expenses?month=2026-11')
    if body.get('total_cents') != 3600:
        fail('rejected patches changed the november total')


def case_a04(ctx):
    '''A04 month switching, detail lookup and integer-cent arithmetic.'''
    base = ctx['base_url']
    status, body = req('GET', base + '/api/expenses?month=2026-10')
    expect(status, body, 200, 'october summary')
    if body.get('total_cents') != 2400:
        fail('october total_cents is %r, expected 2400' % (body.get('total_cents'),))
    if body.get('total_display') != '24.00':
        fail('october total_display is %r, expected 24.00' % (body.get('total_display'),))
    rows = body.get('by_category', []) or []
    names = sorted(row.get('category') for row in rows)
    expected = sorted([CATEGORIES[0], RENAME])
    if names != expected:
        fail('the october breakdown covers %s, expected %s' % (names, expected))
    for row in rows:
        if type(row.get('total_cents')) is not int:
            fail('a breakdown total_cents must be an int')
        if 'total_display' not in row:
            fail('a breakdown row is missing total_display')
    details = body.get('expenses', []) or []
    if len(details) != 2:
        fail('october should expose 2 detail rows, found %d' % len(details))
    for expense in details:
        if type(expense.get('amount_cents')) is not int:
            fail('a detail amount_cents must be an int')
        if str(expense.get('date'))[:7] != '2026-10':
            fail('a detail row from another month leaked into october: %s' % expense.get('date'))
    status, body = req('GET', base + '/api/expenses?month=2026-09')
    expect(status, body, 200, 'september summary')
    if body.get('total_cents') != 4200 or len(body.get('expenses', []) or []) != 1:
        fail('the september summary is wrong: total=%r rows=%d' % (body.get('total_cents'), len(body.get('expenses', []) or [])))
    status, body = req('GET', base + '/api/expenses?month=2026-11')
    expect(status, body, 200, 'november summary')
    if body.get('total_cents') != 3600 or len(body.get('expenses', []) or []) != 2:
        fail('the november summary is wrong: total=%r rows=%d' % (body.get('total_cents'), len(body.get('expenses', []) or [])))
    status, body = req('GET', base + '/api/expenses?month=2026-08')
    expect(status, body, 200, 'empty month summary')
    if body.get('total_cents') != 0 or body.get('total_display') != '0.00':
        fail('an empty month must report zero, got %r / %r' % (body.get('total_cents'), body.get('total_display')))
    if (body.get('by_category') or []) != [] or (body.get('expenses') or []) != []:
        fail('an empty month must report an empty breakdown and no details')
    for bad in ('2026-13', '2026-1', 'abc', '2026-00', '2026-10-01'):
        status, body = req('GET', base + '/api/expenses?month=' + urllib.parse.quote(bad))
        if status != 400:
            fail('month=%s: expected HTTP 400, got %d' % (bad, status))
    status, body = req('GET', base + '/api/expenses')
    if status != 400:
        fail('a missing month parameter: expected HTTP 400, got %d' % status)
    for cents in (10, 20, 30, 1005, 2010):
        payload = {'date': '2026-12-07', 'amount_cents': cents, 'category': CATEGORIES[0], 'note': 'probe: float trap'}
        status, body = req('POST', base + '/api/expenses', payload)
        expect(status, body, 201, 'create the float trap expense')
    status, body = req('GET', base + '/api/expenses?month=2026-12')
    if body.get('total_cents') != 3075:
        fail('december total_cents is %r, expected 3075' % (body.get('total_cents'),))
    if body.get('total_display') != '30.75':
        fail('december total_display is %r, expected 30.75' % (body.get('total_display'),))
    status, ctype, html = get_html(base + '/')
    if status != 200:
        fail('GET / returned HTTP %d' % status)
    if 'text/html' not in ctype.lower():
        fail('GET / did not return HTML, content-type was %r' % ctype)
    for hook in ('id="month-total"', 'id="category-breakdown"', 'id="expense-form"', 'id="prev-month"', 'id="next-month"', 'id="expense-list"'):
        if hook not in html:
            fail('the dashboard HTML is missing %s' % hook)
    status, ctype, html = get_html(base + '/settings')
    if status != 200:
        fail('GET /settings returned HTTP %d' % status)
    for hook in ('id="category-list"', 'id="new-category-name"', 'id="category-form"'):
        if hook not in html:
            fail('the settings HTML is missing %s' % hook)


def case_a05(ctx):
    '''A05 reopening the target keeps every record and every aggregate.'''
    base = ctx['base_url']
    before = snapshot(base, MONTHS)
    target = ctx.get('target')
    if target is not None:
        target.stop()
        target.start()
        after = snapshot(base, MONTHS)
        if after != before:
            fail('the state changed across a restart of the target process')
        ctx['state']['restart_leg'] = PASS
    else:
        ctx['state']['restart_leg'] = SKIP
    store = ctx.get('store_file')
    if not store:
        ctx['state']['store_leg'] = SKIP
        return
    if not os.path.exists(store):
        fail('the store file %s is missing although the target promised to persist' % store)
    with open(store, 'r', encoding='utf-8') as handle:
        raw = handle.read()
    try:
        data = json.loads(raw)
    except ValueError as exc:
        fail('the store file is not valid JSON: %s' % exc)
    expenses = data.get('expenses')
    if not isinstance(expenses, list):
        fail('the store file has no expenses array')
    for expense in expenses:
        if type(expense.get('amount_cents')) is not int:
            fail('a stored amount_cents is not an integer: %r' % (expense.get('amount_cents'),))
        if 'amount' in expense:
            fail('the store file still carries a float money field: %r' % (expense.get('amount'),))
    for match in re.finditer(r'"amount_cents"\s*:\s*(-?\d+(?:\.\d+)?)', raw):
        if '.' in match.group(1):
            fail('the store file contains a fractional money literal: %s' % match.group(1))
    stored_categories = data.get('categories')
    if stored_categories is not None and stored_categories != before['categories']:
        fail('the stored categories differ from the served categories')
    for month in MONTHS:
        rows = [e for e in expenses if str(e.get('date', ''))[:7] == month]
        stored_total = sum(e['amount_cents'] for e in rows)
        if stored_total != before[month]['total_cents']:
            fail('the store sum for %s is %d but the API reports %r' % (month, stored_total, before[month]['total_cents']))
        if len(rows) != len(before[month]['expenses']):
            fail('the store holds %d rows for %s but the API lists %d' % (len(rows), month, len(before[month]['expenses'])))
    ctx['state']['store_leg'] = PASS


CASES = [
    ('A01', 'category management', case_a01),
    ('A02', 'record expenses', case_a02),
    ('A03', 'correction and immediate recompute', case_a03),
    ('A04', 'month switching and detail lookup', case_a04),
    ('A05', 'reopen persistence', case_a05),
]


def main(argv=None):
    parser = argparse.ArgumentParser(description='Acceptance orchestrator for the daily expense tracker web target (A01-A05).')
    parser.add_argument('--base-url', help='base URL of an already running target')
    parser.add_argument('--server-cmd', help='command that starts the target; {ADDR} and {DATA_DIR} are substituted')
    parser.add_argument('--addr', default='127.0.0.1:8099')
    parser.add_argument('--data-dir', help='explicit disposable data directory (default: a new temporary directory)')
    parser.add_argument('--store-file', help='path of the target store file, for the on-disk checks')
    parser.add_argument('--phase', default='all', help='all | A01 | A02 | A03 | A04 | A05 | persist')
    parser.add_argument('--allow-write', action='store_true', help='required with --base-url: the probe writes probe-* records')
    parser.add_argument('--keep-data', action='store_true', help='keep the temporary data directory for inspection')
    args = parser.parse_args(argv)

    if not args.base_url and not args.server_cmd:
        parser.error('one of --base-url or --server-cmd is required')
    if args.base_url and not args.allow_write:
        parser.error('--base-url requires --allow-write: the probe writes probe-* records into the running instance')

    temp_dir = None
    target = None
    data_dir = args.data_dir
    if args.server_cmd:
        if data_dir is None:
            temp_dir = tempfile.mkdtemp(prefix='expense-probe-')
            data_dir = temp_dir
        else:
            os.makedirs(data_dir, exist_ok=True)
        target = Target(args.server_cmd, args.addr, data_dir)
        target.start()
        base_url = target.base_url
    else:
        base_url = args.base_url.rstrip('/')
        wait_healthy(base_url, 15)
        print('note: writing probe-* categories and expenses into the running instance')

    store_file = args.store_file
    if store_file is None and data_dir:
        store_file = os.path.join(data_dir, 'store.json')

    ctx = {'base_url': base_url, 'target': target, 'store_file': store_file, 'state': {}}
    results = []
    try:
        for case_id, title, func in CASES:
            phase = args.phase.lower()
            if phase == 'all':
                run = True
            elif phase == 'persist':
                run = case_id == 'A05'
            else:
                run = phase in (case_id.lower(), case_id)
            if not run:
                continue
            started = time.time()
            status = PASS
            detail = ''
            try:
                func(ctx)
            except Failure as exc:
                status = FAIL
                detail = str(exc)
            except Exception as exc:
                status = FAIL
                detail = 'unexpected error: %r' % (exc,)
            if case_id == 'A05' and status == PASS:
                if ctx['state'].get('restart_leg') == SKIP and ctx['state'].get('store_leg') == SKIP:
                    status = SKIP
                    detail = 'no persistence evidence: run with --server-cmd, or pass --store-file'
            results.append({'id': case_id, 'title': title, 'status': status, 'detail': detail})
            print('%-4s %-40s %-8s %.2fs %s' % (case_id, title, status, time.time() - started, detail))
    finally:
        if target is not None:
            target.stop()
        if temp_dir and not args.keep_data:
            shutil.rmtree(temp_dir, ignore_errors=True)

    failed = [r for r in results if r['status'] == FAIL]
    skipped = [r for r in results if r['status'] == SKIP]
    print('')
    print('cases run: %d, failed: %d, skipped: %d' % (len(results), len(failed), len(skipped)))
    for item in skipped:
        print('not_run: %s %s' % (item['id'], item['detail']))
    if failed:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
