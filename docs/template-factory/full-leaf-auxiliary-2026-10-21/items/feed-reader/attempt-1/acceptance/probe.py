#!/usr/bin/env python3
'''Acceptance orchestrator for the feedreader self-hosted feed reader service.

Scenario: morning triage of a self-hosted subscription list.
Cases: A01 standing intake, A02 reading state, A03 OPML round trip,
       A04 subscription list management, A05 reader view navigation.

This file is the verifier only. It never implements the target service: it
drives the JSON API of a running instance and asserts observable results.

Usage:
    FEEDREADER_BASE_URL=http://127.0.0.1:8080
    FEEDREADER_API_KEY=acceptance-key
    python3 probe.py

Exit codes:
    0  every executed check passed (not_run checks are listed in the summary)
    1  at least one check failed
    2  the target was unreachable or not configured, nothing was executed
'''
import datetime
import hashlib
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_URL = os.environ.get('FEEDREADER_BASE_URL', 'http://127.0.0.1:8080').rstrip('/')
API_KEY = os.environ.get('FEEDREADER_API_KEY', '')
INTAKE_TIMEOUT = float(os.environ.get('FEEDREADER_INTAKE_TIMEOUT', '60'))
STRICT = os.environ.get('FEEDREADER_STRICT', '').strip().lower() not in ('', '0', 'false', 'no')
FIXTURE_HOST = os.environ.get('FEEDREADER_FIXTURE_HOST', '127.0.0.1')
FIXTURE_PORT = int(os.environ.get('FEEDREADER_FIXTURE_PORT', '0'))
FIXTURE_BASE_OVERRIDE = os.environ.get('FEEDREADER_FIXTURE_BASE', '').strip()

RESULTS = []
FIXTURE_LOCK = threading.Lock()
FIXTURES = {
    'alpha': {'title': 'Probe Alpha', 'site': 'https://probe.invalid/alpha', 'ttl': None, 'items': []},
    'beta': {'title': 'Probe Beta', 'site': 'https://probe.invalid/beta', 'ttl': None, 'items': []},
    'gamma': {'title': 'Probe Gamma', 'site': 'https://probe.invalid/gamma', 'ttl': None, 'items': []},
    'delta': {'title': 'Probe Delta', 'site': 'https://probe.invalid/delta', 'ttl': 120, 'items': []},
}
CREATED_FEEDS = {}
CREATED_CATEGORIES = {}
FIXTURE_LOCAL_BASE = ''
FIXTURE_FEED_BASE = ''


class TargetUnreachable(Exception):
    pass


def record(case, name, status, detail=''):
    RESULTS.append({'case': case, 'check': name, 'status': status, 'detail': detail})
    print('[%s] %s %s%s' % (status.upper().ljust(7), case, name, (' :: ' + detail) if detail else ''))


def check(case, name, ok, detail=''):
    record(case, name, 'pass' if ok else 'fail', detail if ok else (detail or 'assertion failed'))
    return bool(ok)


def not_run(case, name, reason):
    record(case, name, 'not_run', reason)


def api(method, path, body=None, raw=None, ctype='application/xml', timeout=30):
    url = BASE_URL + path
    data = None
    headers = {'Accept': 'application/json'}
    if API_KEY:
        headers['X-Api-Key'] = API_KEY
    if body is not None:
        data = json.dumps(body).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    elif raw is not None:
        data = raw.encode('utf-8') if isinstance(raw, str) else raw
        headers['Content-Type'] = ctype
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, dict(response.headers.items()), response.read()
    except urllib.error.HTTPError as exc:
        extra = dict(exc.headers.items()) if exc.headers else {}
        return exc.code, extra, exc.read()
    except urllib.error.URLError as exc:
        raise TargetUnreachable('%s %s: %s' % (method, url, exc))
    except OSError as exc:
        raise TargetUnreachable('%s %s: %s' % (method, url, exc))


def japi(method, path, body=None, raw=None, ctype='application/xml'):
    status, headers, payload = api(method, path, body=body, raw=raw, ctype=ctype)
    data = None
    if payload:
        try:
            data = json.loads(payload.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            data = None
    return status, headers, data


def render_feed(name):
    fixture = FIXTURES[name]
    parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0">', '<channel>']
    parts.append('<title>' + fixture['title'] + '</title>')
    parts.append('<link>' + fixture['site'] + '</link>')
    parts.append('<description>acceptance fixture feed</description>')
    if fixture['ttl'] is not None:
        parts.append('<ttl>' + str(fixture['ttl']) + '</ttl>')
    for item in fixture['items']:
        parts.append('<item>')
        parts.append('<title>' + item['title'] + '</title>')
        parts.append('<link>' + item['link'] + '</link>')
        parts.append('<guid isPermaLink="false">' + item['guid'] + '</guid>')
        parts.append('<pubDate>' + item['pubdate'] + '</pubDate>')
        parts.append('<description>' + item['body'] + '</description>')
        parts.append('</item>')
    parts.append('</channel>')
    parts.append('</rss>')
    return '\n'.join(parts)


class FixtureHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def log_message(self, *args):
        pass

    def respond(self, status, body=b'', ctype='text/plain; charset=utf-8', extra=None):
        self.send_response(status)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(body)))
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path.startswith('/feed/') and path.endswith('.xml'):
            name = path[len('/feed/'):-len('.xml')]
            if name not in FIXTURES:
                self.respond(404, b'unknown fixture')
                return
            body = render_feed(name).encode('utf-8')
            etag = '"' + hashlib.sha256(body).hexdigest()[:32] + '"'
            if (self.headers.get('If-None-Match') or '').strip() == etag:
                self.send_response(304)
                self.send_header('ETag', etag)
                self.end_headers()
                return
            self.respond(200, body, 'application/rss+xml; charset=utf-8', {'ETag': etag})
            return
        if path == '/not-a-feed':
            self.respond(200, b'<html><body>not a feed</body></html>', 'text/html; charset=utf-8')
            return
        self.respond(404, b'not found')

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        length = int(self.headers.get('Content-Length') or 0)
        raw = self.rfile.read(length) if length > 0 else b''
        if path == '/publish':
            payload = json.loads(raw.decode('utf-8'))
            with FIXTURE_LOCK:
                FIXTURES[payload['fixture']]['items'].append({
                    'guid': payload['guid'],
                    'title': payload['title'],
                    'link': payload['link'],
                    'pubdate': payload.get('pubdate', 'Mon, 05 Oct 2026 09:00:00 +0000'),
                    'body': payload.get('body', 'acceptance fixture body'),
                })
            self.respond(200, b'{"ok": true}', 'application/json')
            return
        self.respond(404, b'not found')


def start_fixture_server():
    httpd = ThreadingHTTPServer((FIXTURE_HOST, FIXTURE_PORT), FixtureHandler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    host, port = httpd.server_address[0], httpd.server_address[1]
    local_host = '127.0.0.1' if host in ('0.0.0.0', '') else host
    return httpd, 'http://' + local_host + ':' + str(port)


def publish(name, guid, title, link, pubdate=None):
    payload = {'fixture': name, 'guid': guid, 'title': title, 'link': link}
    if pubdate:
        payload['pubdate'] = pubdate
    request = urllib.request.Request(FIXTURE_LOCAL_BASE + '/publish',
                                     data=json.dumps(payload).encode('utf-8'),
                                     headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(request, timeout=10) as response:
        response.read()


def create_category(name):
    return japi('POST', '/api/v1/categories', body={'title': name})


def create_feed(feed_url, category_id):
    return japi('POST', '/api/v1/feeds', body={'feed_url': feed_url, 'category_id': category_id})


def list_categories():
    status, _, data = japi('GET', '/api/v1/categories')
    if status != 200 or not isinstance(data, list):
        return []
    return data


def list_feeds():
    status, _, data = japi('GET', '/api/v1/feeds')
    if status != 200 or not isinstance(data, list):
        return []
    return data


def list_entries(status_filter=None, feed_id=None, category_id=None, starred=None):
    params = {}
    if status_filter is not None:
        params['status'] = status_filter
    if feed_id is not None:
        params['feed_id'] = feed_id
    if category_id is not None:
        params['category_id'] = category_id
    if starred is not None:
        params['starred'] = 'true' if starred else 'false'
    query = urllib.parse.urlencode(params)
    status, _, data = japi('GET', '/api/v1/entries?' + query)
    if status != 200 or not isinstance(data, list):
        return []
    return data


def unread_counts():
    status, _, data = japi('GET', '/api/v1/unread-counts')
    return data if status == 200 and isinstance(data, dict) else {}


def refresh_feed(feed_id):
    return japi('POST', '/api/v1/feeds/%d/refresh' % feed_id, body={'force': True})


def mark_read(entry_id, new_status):
    return japi('PUT', '/api/v1/entries/%d' % entry_id, body={'status': new_status})


def set_starred(entry_id, value):
    return japi('PUT', '/api/v1/entries/%d' % entry_id, body={'starred': bool(value)})


def mark_all_read(scope):
    return japi('POST', '/api/v1/entries/mark-all-read', body=scope)


def parse_ts(value):
    if not value:
        return None
    text = str(value).strip().replace('Z', '+00:00')
    try:
        stamp = datetime.datetime.fromisoformat(text)
    except ValueError:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=datetime.timezone.utc)
    return stamp.timestamp()


def seconds_until(value):
    stamp = parse_ts(value)
    if stamp is None:
        return None
    return stamp - time.time()


def wait_for_unread(feed_id, expected, timeout):
    deadline = time.time() + timeout
    seen = []
    while time.time() < deadline:
        seen = list_entries(status_filter='unread', feed_id=feed_id)
        if len(seen) >= expected:
            return True, seen
        time.sleep(1.0)
    return False, seen


def opml_feed_outlines(xml_text):
    root = ET.fromstring(xml_text)
    parents = {}
    for parent in root.iter():
        for child in parent:
            parents[id(child)] = parent
    found = []
    for outline in root.iter('outline'):
        url = outline.get('xmlUrl')
        if not url:
            continue
        category = None
        ancestor = parents.get(id(outline))
        while ancestor is not None:
            if ancestor.tag == 'outline' and not ancestor.get('xmlUrl'):
                category = ancestor.get('title') or ancestor.get('text')
                break
            ancestor = parents.get(id(ancestor))
        found.append({'url': url, 'category': category,
                      'title': outline.get('title') or outline.get('text')})
    return found


def entry_state(entry_id):
    status, _, data = japi('GET', '/api/v1/entries/%d' % entry_id)
    if status != 200 or not isinstance(data, dict):
        return None
    return data


def teardown():
    for feed_id in sorted(CREATED_FEEDS.keys(), reverse=True):
        japi('DELETE', '/api/v1/feeds/%d' % feed_id)
    for category_id in sorted(CREATED_CATEGORIES.keys(), reverse=True):
        japi('DELETE', '/api/v1/categories/%d' % category_id)
    print('teardown: %d subscription(s) and %d category(ies) left on the instance'
          % (len(list_feeds()), len(list_categories())))


def finish():
    teardown()
    failed = [r for r in RESULTS if r['status'] == 'fail']
    skipped = [r for r in RESULTS if r['status'] == 'not_run']
    passed = len(RESULTS) - len(failed) - len(skipped)
    print('---')
    print('checks: %d passed, %d failed, %d not_run' % (passed, len(failed), len(skipped)))
    for item in skipped:
        print('not_run: %s %s :: %s' % (item['case'], item['check'], item['detail']))
    for item in failed:
        print('FAIL: %s %s :: %s' % (item['case'], item['check'], item['detail']))
    if failed:
        return 1
    if skipped and STRICT:
        print('strict mode: not_run results are treated as failures')
        return 1
    return 0


def preflight():
    try:
        status, _, _ = japi('GET', '/healthz')
    except TargetUnreachable as exc:
        print('not_run: target unreachable at %s (%s)' % (BASE_URL, exc))
        return None
    if status != 200:
        print('not_run: /healthz returned %s' % status)
        return None
    try:
        status, _, _ = japi('GET', '/api/v1/feeds')
    except TargetUnreachable as exc:
        print('not_run: target unreachable at %s (%s)' % (BASE_URL, exc))
        return None
    if status in (401, 403):
        print('not_run: the API needs credentials, set FEEDREADER_API_KEY')
        return None
    if status != 200:
        print('not_run: GET /api/v1/feeds returned %s' % status)
        return None
    return True


def main():
    global FIXTURE_LOCAL_BASE, FIXTURE_FEED_BASE
    print('=== feedreader acceptance probe ===')
    print('target: ' + BASE_URL)
    if preflight() is None:
        return 2

    config = {}
    status, _, data = japi('GET', '/api/v1/config')
    if status == 200 and isinstance(data, dict):
        config = data
    polling = int(config.get('polling_interval_seconds', 3600) or 3600)
    print('configured polling interval: %s seconds' % polling)

    # remove leftovers of an earlier probe run, refuse foreign data
    for feed in list_feeds():
        title = feed.get('title') or ''
        host = urllib.parse.urlparse(feed.get('feed_url') or '').hostname or ''
        if title.startswith('Probe ') or host in ('127.0.0.1', 'localhost', '::1'):
            japi('DELETE', '/api/v1/feeds/%d' % int(feed['id']))
    for category in list_categories():
        if (category.get('title') or '').startswith('probe-'):
            japi('DELETE', '/api/v1/categories/%d' % int(category['id']))
    remaining = list_feeds()
    if remaining:
        print('not_run: the instance already holds %d subscription(s) that this probe did not '
              'create; run against a disposable instance because mark all as read is account wide'
              % len(remaining))
        return 2

    httpd, local_base = start_fixture_server()
    FIXTURE_LOCAL_BASE = local_base
    FIXTURE_FEED_BASE = FIXTURE_BASE_OVERRIDE or local_base
    feed_base = FIXTURE_FEED_BASE

    publish('alpha', 'urn:probe:alpha:1', 'Alpha item one', 'https://probe.invalid/alpha/1')
    publish('beta', 'urn:probe:beta:1', 'Beta item one', 'https://probe.invalid/beta/1')
    publish('gamma', 'urn:probe:gamma:1', 'Gamma item one', 'https://probe.invalid/gamma/1')
    publish('delta', 'urn:probe:delta:1', 'Delta item one', 'https://probe.invalid/delta/1')

    token = uuid.uuid4().hex[:8]
    cat_news = 'probe-' + token + '-news'
    cat_misc = 'probe-' + token + '-misc'
    cat_empty = 'probe-' + token + '-empty'
    for name in (cat_news, cat_misc, cat_empty):
        status, _, data = create_category(name)
        if status not in (200, 201) or not isinstance(data, dict):
            record('setup', 'create category ' + name, 'fail', 'status=' + str(status))
            httpd.shutdown()
            return finish()
        CREATED_CATEGORIES[int(data['id'])] = name

    # ---------------- A01 standing intake ----------------
    case = 'A01'
    status, _, feed = create_feed(feed_base + '/feed/alpha.xml', CREATED_CATEGORIES[cat_news])
    if not check(case, 'A01.1 a feed URL can be subscribed', status == 201 and isinstance(feed, dict),
                 'status=' + str(status) + ' body=' + json.dumps(feed)[:200]):
        httpd.shutdown()
        return finish()
    alpha_id = int(feed['id'])
    CREATED_FEEDS[alpha_id] = 'alpha'
    check(case, 'A01.2 the subscription carries the feed title and its category',
          (feed.get('title') == 'Probe Alpha'
           and int(feed.get('category_id', -1)) == CREATED_CATEGORIES[cat_news]),
          'title=' + str(feed.get('title')) + ' category_id=' + str(feed.get('category_id')))

    entries = list_entries(status_filter='unread', feed_id=alpha_id)
    check(case, 'A01.3 the first published item is stored as unread', len(entries) == 1,
          'unread entries=' + str(len(entries)))
    if entries:
        first = entries[0]
        check(case, 'A01.4 the item carries the feed title and the canonical link',
              first.get('feed_title') == 'Probe Alpha'
              and first.get('url') == 'https://probe.invalid/alpha/1'
              and first.get('status') == 'unread',
              'feed_title=' + str(first.get('feed_title')) + ' url=' + str(first.get('url'))
              + ' status=' + str(first.get('status')))

    counts = unread_counts()
    check(case, 'A01.5 the unread counts report the new item',
          int(counts.get('total', -1)) == 1
          and int((counts.get('feeds') or {}).get(str(alpha_id), -1)) == 1,
          'counts=' + json.dumps(counts))

    publish('alpha', 'urn:probe:alpha:2', 'Alpha item two', 'https://probe.invalid/alpha/2')
    arrived, seen = wait_for_unread(alpha_id, 2, INTAKE_TIMEOUT)
    if arrived:
        check(case, 'A01.6 the scheduler delivered the newly published item', len(seen) == 2,
              'unread entries=' + str(len(seen)))
    elif polling > INTAKE_TIMEOUT:
        not_run(case, 'A01.6 the scheduler delivered the newly published item',
                'the configured polling interval is ' + str(polling) + 's, longer than the probe '
                'timeout of ' + str(int(INTAKE_TIMEOUT)) + 's')
        status, _, res = refresh_feed(alpha_id)
        check(case, 'A01.6b an explicit refresh delivers the newly published item',
              status == 200 and isinstance(res, dict) and int(res.get('new_entries', -1)) == 1,
              'status=' + str(status) + ' body=' + json.dumps(res)[:200])
        seen = list_entries(status_filter='unread', feed_id=alpha_id)
    else:
        check(case, 'A01.6 the scheduler delivered the newly published item', False,
              'no new item within ' + str(int(INTAKE_TIMEOUT)) + 's (unread=' + str(len(seen)) + ')')

    links = sorted(e.get('url', '') for e in seen)
    check(case, 'A01.7 every known item is listed exactly once',
          links == ['https://probe.invalid/alpha/1', 'https://probe.invalid/alpha/2'],
          'links=' + str(links))

    status, _, res = refresh_feed(alpha_id)
    check(case, 'A01.8 a repeated refresh does not duplicate known items',
          status == 200 and isinstance(res, dict) and int(res.get('new_entries', -1)) == 0,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200])
    after = list_entries(status_filter='unread', feed_id=alpha_id)
    check(case, 'A01.9 the unread list still holds each item once', len(after) == 2,
          'unread=' + str(len(after)))

    status, _, delta = create_feed(feed_base + '/feed/delta.xml', CREATED_CATEGORIES[cat_news])
    if check(case, 'A01.10 a feed that declares a TTL can be subscribed',
             status == 201 and isinstance(delta, dict), 'status=' + str(status)):
        delta_id = int(delta['id'])
        CREATED_FEEDS[delta_id] = 'delta'
        refresh_feed(delta_id)
        delta_feed = {}
        for item in list_feeds():
            if int(item['id']) == delta_id:
                delta_feed = item
        delay = seconds_until(delta_feed.get('next_check_at'))
        check(case, 'A01.11 the feed TTL pushes the next check further out',
              delay is not None and delay >= 110,
              'next_check_at=' + str(delta_feed.get('next_check_at')) + ' delay_s=' + str(delay))

    # ---------------- A02 reading state ----------------
    case = 'A02'
    publish('alpha', 'urn:probe:alpha:3', 'Alpha item three', 'https://probe.invalid/alpha/3')
    refresh_feed(alpha_id)
    status, _, beta = create_feed(feed_base + '/feed/beta.xml', CREATED_CATEGORIES[cat_misc])
    if not check(case, 'A02.0 a second feed can be subscribed in another category',
                 status == 201 and isinstance(beta, dict), 'status=' + str(status)):
        httpd.shutdown()
        return finish()
    beta_id = int(beta['id'])
    CREATED_FEEDS[beta_id] = 'beta'
    publish('beta', 'urn:probe:beta:2', 'Beta item two', 'https://probe.invalid/beta/2')
    refresh_feed(beta_id)

    alpha_entries = list_entries(status_filter='unread', feed_id=alpha_id)
    beta_entries = list_entries(status_filter='unread', feed_id=beta_id)
    check(case, 'A02.1 each feed delivers its own items',
          len(alpha_entries) == 3 and len(beta_entries) == 2,
          'alpha=' + str(len(alpha_entries)) + ' beta=' + str(len(beta_entries)))
    if not alpha_entries:
        httpd.shutdown()
        return finish()
    target = alpha_entries[0]

    before = unread_counts()
    status, _, updated = mark_read(target['id'], 'read')
    check(case, 'A02.2 an item can be marked read',
          status == 200 and isinstance(updated, dict) and updated.get('status') == 'read',
          'status=' + str(status) + ' body=' + json.dumps(updated)[:200])
    after = unread_counts()
    check(case, 'A02.3 the unread count drops for the feed and in total',
          int(after.get('total', -1)) == int(before.get('total', 0)) - 1
          and int((after.get('feeds') or {}).get(str(alpha_id), -1))
          == int((before.get('feeds') or {}).get(str(alpha_id), 0)) - 1,
          'before=' + json.dumps(before) + ' after=' + json.dumps(after))
    still_unread = list_entries(status_filter='unread', feed_id=alpha_id)
    check(case, 'A02.4 the read item left the unread view',
          all(int(e['id']) != int(target['id']) for e in still_unread),
          'unread=' + str(len(still_unread)))

    status, _, starred = set_starred(target['id'], True)
    check(case, 'A02.5 an item can be starred',
          status == 200 and isinstance(starred, dict) and starred.get('starred') is True,
          'status=' + str(status) + ' body=' + json.dumps(starred)[:200])
    status, _, again = mark_read(target['id'], 'read')
    counts2 = unread_counts()
    check(case, 'A02.6 marking an already read item again changes nothing',
          status == 200 and int(counts2.get('total', -1)) == int(after.get('total', -2)),
          'status=' + str(status) + ' total=' + str(counts2.get('total')))
    starred_list = list_entries(starred=True)
    check(case, 'A02.7 the starred item appears in the starred list',
          any(int(e['id']) == int(target['id']) for e in starred_list),
          'starred entries=' + str(len(starred_list)))

    refresh_feed(alpha_id)
    after_refresh = [e for e in list_entries(starred=True) if int(e['id']) == int(target['id'])]
    check(case, 'A02.8 an intake refresh keeps the read state and the starred flag',
          len(after_refresh) == 1 and after_refresh[0].get('status') == 'read'
          and after_refresh[0].get('starred') is True,
          'entries=' + json.dumps(after_refresh)[:200])

    status, _, res = mark_all_read({'feed_id': alpha_id})
    check(case, 'A02.9 marking a whole feed read touches only that feed',
          status == 200 and isinstance(res, dict) and int(res.get('updated', -1)) == 2
          and len(list_entries(status_filter='unread', feed_id=alpha_id)) == 0
          and len(list_entries(status_filter='unread', feed_id=beta_id)) == 2,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200])

    status, _, res = mark_all_read({'category_id': CREATED_CATEGORIES[cat_misc]})
    delta_unread = 0
    for item in list_feeds():
        if int(item['id']) == delta_id:
            delta_unread = int(item.get('unread_count', 0))
    check(case, 'A02.10 marking a whole category read leaves the other categories alone',
          status == 200 and isinstance(res, dict) and int(res.get('updated', -1)) == 2
          and delta_unread == 1,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200] + ' delta_unread=' + str(delta_unread))

    status, _, res = mark_all_read({'category_id': CREATED_CATEGORIES[cat_empty]})
    check(case, 'A02.11 marking an empty scope read is a no-op',
          status == 200 and isinstance(res, dict) and int(res.get('updated', -1)) == 0,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200])

    status, _, res = mark_all_read({})
    counts3 = unread_counts()
    check(case, 'A02.12 marking everything read clears the backlog',
          status == 200 and int(counts3.get('total', -1)) == 0,
          'status=' + str(status) + ' counts=' + json.dumps(counts3))
    still_starred = [e for e in list_entries(starred=True) if int(e['id']) == int(target['id'])]
    check(case, 'A02.13 the starred flag survives the bulk read',
          len(still_starred) == 1 and still_starred[0].get('status') == 'read',
          'entries=' + json.dumps(still_starred)[:200])

    status, _, _ = mark_read(99999999, 'read')
    check(case, 'A02.14 marking an unknown item read is rejected', status == 404,
          'status=' + str(status))
    status, _, _ = mark_read(target['id'], 'sideways')
    check(case, 'A02.15 an invalid reading status is rejected', status == 400,
          'status=' + str(status))

    # ---------------- A03 OPML round trip ----------------
    case = 'A03'
    status, _, payload = api('GET', '/api/v1/opml/export')
    check(case, 'A03.1 the subscription list exports as OPML',
          status == 200 and b'<opml' in payload.lower(),
          'status=' + str(status) + ' bytes=' + str(len(payload)))
    outlines = opml_feed_outlines(payload.decode('utf-8'))
    expected = sorted([feed_base + '/feed/alpha.xml', feed_base + '/feed/beta.xml',
                       feed_base + '/feed/delta.xml'])
    urls = sorted(o['url'] for o in outlines)
    check(case, 'A03.2 there is one outline per subscribed feed', urls == expected,
          'urls=' + str(urls))
    alpha_outline = [o for o in outlines if o['url'] == feed_base + '/feed/alpha.xml']
    check(case, 'A03.3 the feed outline sits inside its category outline',
          len(alpha_outline) == 1 and alpha_outline[0]['category'] == cat_news,
          'outlines=' + json.dumps(alpha_outline))
    beta_outline = [o for o in outlines if o['url'] == feed_base + '/feed/beta.xml']
    check(case, 'A03.4 the second feed outline sits inside its own category outline',
          len(beta_outline) == 1 and beta_outline[0]['category'] == cat_misc,
          'outlines=' + json.dumps(beta_outline))

    status, _, _ = japi('DELETE', '/api/v1/feeds/%d' % beta_id)
    check(case, 'A03.5 the removed feed left the subscription list',
          status in (200, 204) and beta_id not in [int(f['id']) for f in list_feeds()],
          'status=' + str(status))
    status, _, res = japi('POST', '/api/v1/opml/import', raw=payload.decode('utf-8'),
                          ctype='application/xml')
    check(case, 'A03.6 re-importing the exported file recreates the subscription',
          status == 200 and isinstance(res, dict) and int(res.get('created', -1)) == 1
          and int(res.get('skipped', -1)) == 2,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200])
    restored = [f for f in list_feeds() if f.get('feed_url') == feed_base + '/feed/beta.xml']
    check(case, 'A03.7 the restored feed keeps its url and its category',
          len(restored) == 1
          and int(restored[0].get('category_id', -1)) == CREATED_CATEGORIES[cat_misc],
          'restored=' + json.dumps(restored)[:200])
    if restored:
        CREATED_FEEDS.pop(beta_id, None)
        beta_id = int(restored[0]['id'])
        CREATED_FEEDS[beta_id] = 'beta'

    status, _, res = japi('POST', '/api/v1/opml/import', raw=payload.decode('utf-8'),
                          ctype='application/xml')
    check(case, 'A03.8 importing the same file twice creates no duplicate subscription',
          status == 200 and isinstance(res, dict) and int(res.get('created', -1)) == 0
          and len(list_feeds()) == 3,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200]
          + ' feeds=' + str(len(list_feeds())))

    status, _, _ = japi('POST', '/api/v1/opml/import', raw='<opml><body><outline',
                        ctype='application/xml')
    check(case, 'A03.9 a malformed OPML file is rejected', status == 400, 'status=' + str(status))
    check(case, 'A03.10 the rejected import changed nothing', len(list_feeds()) == 3,
          'feeds=' + str(len(list_feeds())))
    empty_opml = ('<opml version="2.0"><head><title>empty</title></head><body>'
                  '<outline text="folder only"/></body></opml>')
    status, _, res = japi('POST', '/api/v1/opml/import', raw=empty_opml, ctype='application/xml')
    check(case, 'A03.11 an OPML folder without feeds creates no subscription',
          status == 200 and isinstance(res, dict) and int(res.get('created', -1)) == 0
          and len(list_feeds()) == 3,
          'status=' + str(status) + ' body=' + json.dumps(res)[:200])

    # ---------------- A04 subscription list management ----------------
    case = 'A04'
    feeds = list_feeds()
    check(case, 'A04.1 the subscription list shows every feed with its category',
          len(feeds) == 3 and all(f.get('category_title') for f in feeds),
          'feeds=' + json.dumps(feeds)[:300])
    status, _, res = create_feed(feed_base + '/feed/alpha.xml', CREATED_CATEGORIES[cat_news])
    check(case, 'A04.2 subscribing the same feed url twice is rejected',
          status == 409 and len(list_feeds()) == 3,
          'status=' + str(status) + ' feeds=' + str(len(list_feeds())))
    status, _, res = create_feed(feed_base + '/feed/gamma.xml', 999999999)
    check(case, 'A04.3 subscribing into an unknown category is rejected',
          status in (400, 404) and len(list_feeds()) == 3,
          'status=' + str(status) + ' feeds=' + str(len(list_feeds())))
    status, _, res = create_feed(feed_base + '/not-a-feed', CREATED_CATEGORIES[cat_news])
    check(case, 'A04.4 subscribing a url that is not a feed is rejected',
          status == 400 and len(list_feeds()) == 3,
          'status=' + str(status) + ' feeds=' + str(len(list_feeds())))
    status, _, res = create_feed('this is not a url', CREATED_CATEGORIES[cat_news])
    check(case, 'A04.5 a malformed feed url is rejected',
          status == 400 and len(list_feeds()) == 3,
          'status=' + str(status) + ' feeds=' + str(len(list_feeds())))

    status, _, gamma = create_feed(feed_base + '/feed/gamma.xml', CREATED_CATEGORIES[cat_news])
    if check(case, 'A04.6 a new feed can be subscribed and appears in the list',
             status == 201 and isinstance(gamma, dict)
             and any(int(f['id']) == int(gamma['id']) for f in list_feeds()),
             'status=' + str(status) + ' body=' + json.dumps(gamma)[:200]):
        gamma_id = int(gamma['id'])
        CREATED_FEEDS[gamma_id] = 'gamma'
        subscribed = set(int(f['id']) for f in list_feeds())
        stored = list_entries()
        check(case, 'A04.7 every stored item belongs to a subscribed feed',
              len(stored) > 0 and all(int(e['feed_id']) in subscribed for e in stored),
              'items=' + str(len(stored)))
    else:
        httpd.shutdown()
        return finish()

    # ---------------- A05 reader view and navigation ----------------
    case = 'A05'
    status, _, view = japi('GET', '/api/v1/entries/%d' % int(target['id']))
    check(case, 'A05.1 the reader view opens the item', status == 200 and isinstance(view, dict),
          'status=' + str(status) + ' body=' + json.dumps(view)[:200])
    if not isinstance(view, dict):
        httpd.shutdown()
        return finish()
    check(case, 'A05.2 the reader view carries the content, the feed title and the canonical link',
          view.get('feed_title') == 'Probe Alpha'
          and view.get('url') == 'https://probe.invalid/alpha/1'
          and bool(view.get('content')),
          'feed_title=' + str(view.get('feed_title')) + ' url=' + str(view.get('url')))
    neighbours = [n for n in (view.get('prev_entry_id'), view.get('next_entry_id')) if n is not None]
    neighbour_states = []
    for neighbour in neighbours:
        state = entry_state(int(neighbour))
        neighbour_states.append(state.get('status') if isinstance(state, dict) else None)
    check(case, 'A05.3 navigation moves through already read items',
          len(neighbours) > 0
          and all(s == 'read' for s in neighbour_states)
          and int(target['id']) not in [int(n) for n in neighbours],
          'neighbours=' + str(neighbours) + ' states=' + str(neighbour_states))

    gamma_entries = list_entries(status_filter='unread', feed_id=gamma_id)
    if gamma_entries:
        gamma_entry = gamma_entries[0]
        status, _, gview = japi('GET', '/api/v1/entries/%d' % int(gamma_entry['id']))
        check(case, 'A05.4 the reader view opens an unread item too',
              status == 200 and isinstance(gview, dict) and gview.get('status') == 'unread',
              'status=' + str(status) + ' body=' + json.dumps(gview)[:200])
        g_neighbours = [n for n in (gview.get('prev_entry_id'), gview.get('next_entry_id'))
                        if n is not None]
        g_states = []
        for neighbour in g_neighbours:
            state = entry_state(int(neighbour))
            g_states.append(state.get('status') if isinstance(state, dict) else None)
        check(case, 'A05.5 navigation from an unread item still points at read items',
              all(s == 'read' for s in g_states)
              and int(gamma_entry['id']) not in [int(n) for n in g_neighbours],
              'neighbours=' + str(g_neighbours) + ' states=' + str(g_states))
        check(case, 'A05.6 the unread item never becomes a neighbour of a read item',
              int(gamma_entry['id']) not in [int(n) for n in neighbours],
              'neighbours=' + str(neighbours))
    else:
        not_run(case, 'A05.4 the reader view opens an unread item too',
                'the unread fixture item was not stored, so the unread navigation check was skipped')

    status, _, _ = japi('GET', '/api/v1/entries/99999999')
    check(case, 'A05.7 an unknown item id is reported as not found', status == 404,
          'status=' + str(status))
    status, _, _ = japi('GET', '/api/v1/entries/not-a-number')
    check(case, 'A05.8 a malformed item id is rejected', status in (400, 404),
          'status=' + str(status))

    httpd.shutdown()
    return finish()


if __name__ == '__main__':
    sys.exit(main())
