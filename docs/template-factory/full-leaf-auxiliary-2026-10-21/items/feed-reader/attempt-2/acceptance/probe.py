#!/usr/bin/env python3
'''Acceptance orchestrator for the feedreader self-hosted feed reader service.

Scenario: morning triage of a self-hosted subscription list.

Cases:
  A01 standing intake        - a new item arrives through the scheduler, once, attributed
  A05 reader view navigation - the reader view and previous/next over the read entries
  A02 reading state          - mark read, bulk mark read, starred independence, counts
  A04 subscription list      - subscribe with a feed URL or a site URL, and the rejections
  A03 OPML round trip        - export, re-import, no duplicates

This file is the verifier only. It never implements the target service: it
drives the JSON API of a running instance and asserts observable results,
including the negative cases.

Usage:
    FEEDREADER_BASE_URL=http://127.0.0.1:8080
    FEEDREADER_API_KEY=acceptance-key
    python3 probe.py

Exit codes:
    0  every executed check passed (not_run checks are listed in the summary)
    1  at least one check failed
    2  the target was unreachable or the instance is not disposable, nothing ran
'''
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
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_URL = os.environ.get('FEEDREADER_BASE_URL', 'http://127.0.0.1:8080').rstrip('/')
API_KEY = os.environ.get('FEEDREADER_API_KEY', '')
INTAKE_TIMEOUT = float(os.environ.get('FEEDREADER_INTAKE_TIMEOUT', '60'))
HTTP_TIMEOUT = float(os.environ.get('FEEDREADER_HTTP_TIMEOUT', '30'))
REPORT_PATH = os.environ.get('FEEDREADER_REPORT', '')
PROBE_PREFIX = 'probe-'
RESULTS = []


class TargetUnreachable(Exception):
    '''Raised when the service under test cannot be reached at all.'''


def trim(text, limit=160):
    flat = ' '.join((text or '').split())
    return flat[:limit]


def record(case, name, status, message):
    RESULTS.append({'case': case, 'check': name, 'status': status, 'message': message})


def expect(case, name, ok, message):
    record(case, name, 'pass' if ok else 'fail', message)
    return bool(ok)


def not_run(case, name, message):
    record(case, name, 'not_run', message)


def api(method, path, body=None, raw=None, content_type=None):
    '''Call the target API. Returns (status, parsed_json_or_None, text).'''
    url = BASE_URL + path
    data = None
    headers = {'Accept': 'application/json'}
    if API_KEY:
        headers['X-Api-Key'] = API_KEY
    if raw is not None:
        data = raw if isinstance(raw, bytes) else raw.encode('utf-8')
        headers['Content-Type'] = content_type or 'application/octet-stream'
    elif body is not None:
        data = json.dumps(body).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT) as response:
            payload = response.read()
            status = response.status
            content_type_seen = response.headers.get('Content-Type', '')
    except urllib.error.HTTPError as exc:
        payload = exc.read()
        status = exc.code
        content_type_seen = exc.headers.get('Content-Type', '') if exc.headers else ''
    except (urllib.error.URLError, OSError) as exc:
        raise TargetUnreachable('%s %s: %s' % (method, url, exc))
    text = payload.decode('utf-8', 'replace')
    parsed = None
    if 'json' in content_type_seen.lower() or text.lstrip()[:1] in ('{', '['):
        try:
            parsed = json.loads(text)
        except ValueError:
            parsed = None
    return status, parsed, text


def xml_escape(value):
    return (value.replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def rfc2822(moment):
    return moment.strftime('%a, %d %b %Y %H:%M:%S +0000')


class FixtureFeed:
    '''One RSS 2.0 fixture feed whose item list the probe can extend.'''

    def __init__(self, name, title, item_count):
        self.name = name
        self.title = title
        self.link = 'https://probe.invalid/%s' % name
        self.items = []
        self.last_modified = datetime.now(timezone.utc)
        for index in range(1, item_count + 1):
            self.items.append(self.make_item(index))

    def make_item(self, index, title=None):
        published = datetime.now(timezone.utc) - timedelta(seconds=(10 - index) * 60)
        return {
            'guid': '%s-%d' % (self.name, index),
            'title': title or 'Probe %s item %d' % (self.name, index),
            'link': 'https://probe.invalid/%s/%d' % (self.name, index),
            'pubdate': rfc2822(published),
            'description': '<p>Body of probe %s item %d</p>' % (self.name, index),
        }

    def body(self):
        parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
                 '<title>%s</title>' % xml_escape(self.title),
                 '<link>%s</link>' % xml_escape(self.link),
                 '<description>probe fixture feed</description>']
        for item in self.items:
            parts.append('<item><title>%s</title><link>%s</link>'
                         '<guid isPermaLink="false">%s</guid><pubDate>%s</pubDate>'
                         '<description>%s</description></item>' % (
                             xml_escape(item['title']), xml_escape(item['link']),
                             xml_escape(item['guid']), item['pubdate'],
                             item['description']))
        parts.append('</channel></rss>')
        return ''.join(parts).encode('utf-8')


class FixtureState:
    '''Mutable state of the loopback fixture server.'''

    def __init__(self):
        self.lock = threading.Lock()
        self.feeds = {}
        self.requests = []
        self.base_url = ''

    def add(self, name, title, item_count):
        feed = FixtureFeed(name, title, item_count)
        self.feeds[name] = feed
        return feed

    def publish(self, name, title=None):
        with self.lock:
            feed = self.feeds[name]
            item = feed.make_item(len(feed.items) + 1, title)
            feed.items.append(item)
            feed.last_modified = datetime.now(timezone.utc)
            return item

    def republish(self, name, guid, title):
        '''Republish an already known identifier with a changed title.'''
        with self.lock:
            feed = self.feeds[name]
            for item in feed.items:
                if item['guid'] == guid:
                    item['title'] = title
                    item['description'] = '<p>Body changed</p>'
                    feed.last_modified = datetime.now(timezone.utc)
                    return item
        return None

    def record(self, path, headers):
        with self.lock:
            self.requests.append({'path': path, 'headers': headers, 'at': time.time()})

    def requests_for(self, path):
        with self.lock:
            return [row for row in self.requests if row['path'] == path]


class FixtureHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    server_version = 'feedreader-probe-fixture/1.0'

    def log_message(self, *args):
        pass

    def do_GET(self):
        state = self.server.state
        path = urllib.parse.urlparse(self.path).path
        headers = {key.lower(): value for key, value in self.headers.items()}
        state.record(path, headers)

        if path.startswith('/feeds/') and path.endswith('.xml'):
            name = path[len('/feeds/'):-4]
            feed = state.feeds.get(name)
            if feed is None:
                self.respond(404, b'no such feed', 'text/plain; charset=utf-8')
                return
            body = feed.body()
            etag = '"%s"' % hashlib.sha1(body).hexdigest()
            if headers.get('if-none-match', '').strip() == etag:
                self.send_response(304)
                self.send_header('ETag', etag)
                self.send_header('Content-Length', '0')
                self.end_headers()
                return
            self.send_response(200)
            self.send_header('Content-Type', 'application/rss+xml; charset=utf-8')
            self.send_header('ETag', etag)
            self.send_header('Last-Modified', format_datetime(feed.last_modified, usegmt=True))
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if path == '/sites/with-feed.html':
            body = ('<html><head><title>probe site</title>'
                    '<link rel="alternate" type="application/rss+xml" href="%s/feeds/epsilon.xml">'
                    '</head><body>probe site</body></html>' % state.base_url).encode('utf-8')
            self.respond(200, body, 'text/html; charset=utf-8')
            return

        if path == '/sites/no-feed.html':
            body = (b'<html><head><title>probe site without a feed</title></head>'
                    b'<body>nothing to subscribe to</body></html>')
            self.respond(200, body, 'text/html; charset=utf-8')
            return

        if path == '/not-a-feed.txt':
            self.respond(200, b'this is not a feed', 'text/plain; charset=utf-8')
            return

        self.respond(404, b'not found', 'text/plain; charset=utf-8')

    def respond(self, status, body, content_type):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def start_fixture():
    state = FixtureState()
    state.add('alpha', 'Probe Alpha', 1)
    state.add('beta', 'Probe Beta', 2)
    state.add('gamma', 'Probe Gamma', 3)
    state.add('delta', 'Probe Delta', 1)
    state.add('epsilon', 'Probe Epsilon', 1)
    state.add('zeta', 'Probe Zeta', 2)
    server = ThreadingHTTPServer(('127.0.0.1', 0), FixtureHandler)
    server.state = state
    host, port = server.server_address[0], server.server_address[1]
    state.base_url = 'http://%s:%d' % (host, port)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, state


class Context:
    def __init__(self, state):
        self.state = state
        self.uid = uuid.uuid4().hex[:8]
        self.categories = {}
        self.intake_window = 0.0
        self.intake_reason = 'the scheduled intake check was not attempted'

    def cat(self, key):
        for category_id, category in self.categories.items():
            if category['key'] == key:
                return category_id
        raise KeyError('unknown probe category %r' % key)

    def fixture_url(self, path):
        return self.state.base_url + '/' + str(path).lstrip('/')


def list_feeds(ctx):
    status, payload, _text = api('GET', '/api/v1/feeds')
    if status != 200 or not isinstance(payload, dict):
        return None
    return payload.get('feeds') or []


def list_categories(ctx):
    status, payload, _text = api('GET', '/api/v1/categories')
    if status != 200 or not isinstance(payload, dict):
        return None
    return payload.get('categories') or []


def entries_for(ctx, params):
    status, payload, _text = api('GET', '/api/v1/entries?' + urllib.parse.urlencode(params))
    if status != 200 or not isinstance(payload, dict):
        return None
    return payload


def unread_counts(ctx):
    status, payload, _text = api('GET', '/api/v1/unread_count')
    if status != 200 or not isinstance(payload, dict):
        return None
    result = {'total': payload.get('total', 0), 'by_feed': {}}
    for row in payload.get('by_feed') or []:
        result['by_feed'][row.get('feed_id')] = row.get('unread_count', 0)
    return result


def entry_by_url(listing, url):
    for entry in (listing or {}).get('entries') or []:
        if entry.get('url') == url:
            return entry
    return None


def setup(ctx):
    '''Create the disposable probe categories, or refuse to run.'''
    feeds = list_feeds(ctx)
    if feeds is None:
        raise TargetUnreachable('GET /api/v1/feeds did not answer with a feed list')
    categories = {}
    for category in list_categories(ctx) or []:
        categories[category.get('id')] = category.get('title') or ''
    foreign = []
    for feed in feeds:
        title = categories.get(feed.get('category_id'), '')
        if not title.startswith(PROBE_PREFIX):
            foreign.append(feed)
    if foreign:
        print('refusing to run: the instance already holds %d subscription(s) outside the probe categories.'
              % len(foreign))
        print('the probe marks the whole account read in A02 and deletes its own records, so it needs a disposable instance.')
        return False
    for key in ('main', 'a', 'b', 'c', 'g'):
        title = '%s%s-%s' % (PROBE_PREFIX, ctx.uid, key)
        status, payload, text = api('POST', '/api/v1/categories', {'title': title})
        if status != 201 or not isinstance(payload, dict):
            print('cannot create the probe category %s: %s %s' % (title, status, trim(text)))
            return False
        ctx.categories[payload.get('id')] = {'id': payload.get('id'), 'title': title, 'key': key}
    return True


def case_a01(ctx):
    '''Standing intake: the scheduler delivers a new item exactly once.'''
    case = 'A01'
    feed_url = ctx.fixture_url('feeds/alpha.xml')
    status, payload, text = api('POST', '/api/v1/feeds',
                                {'feed_url': feed_url, 'category_id': ctx.cat('a')})
    if not expect(case, 'A01.1 the feed URL is accepted', status == 201,
                  'POST /api/v1/feeds -> %s %s' % (status, trim(text))):
        return
    feed = payload if isinstance(payload, dict) else {}
    feed_id = feed.get('id')
    expect(case, 'A01.2 the feed carries the title of the parsed feed',
           feed.get('title') == 'Probe Alpha', 'title=%r' % feed.get('title'))
    expect(case, 'A01.3 the item published before subscribing is stored unread',
           feed.get('unread_count') == 1, 'unread_count=%r' % feed.get('unread_count'))
    listing = entries_for(ctx, {'status': 'unread', 'feed_id': feed_id, 'limit': 50})
    if not expect(case, 'A01.4 the unread view holds exactly that item',
                  bool(listing) and listing.get('total') == 1,
                  'unread total for the feed: %r' % (listing.get('total') if listing else None)):
        return
    first = (listing.get('entries') or [None])[0]
    expect(case, 'A01.5 the item is attributed to its feed',
           bool(first) and (first.get('feed') or {}).get('title') == 'Probe Alpha',
           'feed title=%r' % ((first.get('feed') or {}).get('title') if first else None))

    published = ctx.state.publish('alpha')
    delivered = None
    if ctx.intake_window > 0:
        deadline = time.time() + ctx.intake_window
        while time.time() < deadline:
            listing = entries_for(ctx, {'status': 'unread', 'feed_id': feed_id, 'limit': 50})
            if listing and listing.get('total', 0) >= 2:
                delivered = listing
                break
            time.sleep(1.0)
        expect(case, 'A01.6 the scheduled refresh delivers the new item', delivered is not None,
               'unread total for the feed after the publish: %r (waited up to %ss)'
               % (listing.get('total') if listing else None, ctx.intake_window))
    else:
        not_run(case, 'A01.6 the scheduled refresh delivers the new item', ctx.intake_reason)
        api('PUT', '/api/v1/feeds/%d/refresh' % feed_id)
        delivered = entries_for(ctx, {'status': 'unread', 'feed_id': feed_id, 'limit': 50})
    fresh = entry_by_url(delivered, published['link'])
    expect(case, 'A01.7 the delivered item carries the feed title and its canonical link',
           fresh is not None and (fresh.get('feed') or {}).get('title') == 'Probe Alpha'
           and fresh.get('url') == published['link'],
           'delivered=%r' % (None if fresh is None else {'url': fresh.get('url'),
                                                         'feed': (fresh.get('feed') or {}).get('title')}))

    before = entries_for(ctx, {'status': 'unread', 'feed_id': feed_id, 'limit': 50})
    before_ids = {}
    for entry in (before or {}).get('entries') or []:
        before_ids[entry.get('url')] = entry.get('id')
    ctx.state.republish('alpha', 'alpha-1', 'Probe Alpha item 1 changed')
    api('PUT', '/api/v1/feeds/%d/refresh' % feed_id)
    after = entries_for(ctx, {'status': 'unread', 'feed_id': feed_id, 'limit': 50})
    after_ids = {}
    for entry in (after or {}).get('entries') or []:
        after_ids[entry.get('url')] = entry.get('id')
    first_url = 'https://probe.invalid/alpha/1'
    expect(case, 'A01.8 a republished identifier is not inserted twice',
           (after or {}).get('total') == (before or {}).get('total')
           and after_ids.get(first_url) == before_ids.get(first_url),
           'total before=%r after=%r, id before=%r after=%r'
           % ((before or {}).get('total'), (after or {}).get('total'),
              before_ids.get(first_url), after_ids.get(first_url)))
    requests = ctx.state.requests_for('/feeds/alpha.xml')
    conditional = [row for row in requests[1:]
                   if row['headers'].get('if-none-match') or row['headers'].get('if-modified-since')]
    expect(case, 'A01.9 the refresh is conditional', bool(conditional),
           '%d of %d fixture requests carried If-None-Match or If-Modified-Since'
           % (len(conditional), len(requests)))


def case_a05(ctx):
    '''Reader view: content, attribution, navigation over the read entries.'''
    case = 'A05'
    feed_url = ctx.fixture_url('feeds/gamma.xml')
    status, payload, text = api('POST', '/api/v1/feeds',
                                {'feed_url': feed_url, 'category_id': ctx.cat('g')})
    if not expect(case, 'A05.1 the feed URL is accepted', status == 201,
                  'POST /api/v1/feeds -> %s %s' % (status, trim(text))):
        return
    feed = payload if isinstance(payload, dict) else {}
    feed_id = feed.get('id')
    expect(case, 'A05.2 the three published items are unread', feed.get('unread_count') == 3,
           'unread_count=%r' % feed.get('unread_count'))
    listing = entries_for(ctx, {'status': 'unread', 'feed_id': feed_id, 'limit': 50})
    by_url = {}
    for entry in (listing or {}).get('entries') or []:
        by_url[entry.get('url')] = entry
    oldest = 'https://probe.invalid/gamma/1'
    middle = 'https://probe.invalid/gamma/2'
    newest = 'https://probe.invalid/gamma/3'
    if not expect(case, 'A05.3 the item to read is present', middle in by_url,
                  'unread urls=%r' % sorted(by_url.keys())):
        return
    target = by_url[middle]
    for url in (oldest, middle, newest):
        entry = by_url.get(url)
        if entry is None:
            continue
        api('PUT', '/api/v1/entries/%d' % entry.get('id'), {'status': 'read'})
        time.sleep(1.1)
    status, payload, text = api('GET', '/api/v1/entries/%d' % target.get('id'))
    if not expect(case, 'A05.4 the reader view answers', status == 200,
                  'GET /api/v1/entries/%d -> %s' % (target.get('id'), status)):
        return
    view = payload if isinstance(payload, dict) else {}
    expect(case, 'A05.5 the reader view keeps the canonical link of the selected entry',
           view.get('url') == target.get('url'),
           'view url=%r, list url=%r' % (view.get('url'), target.get('url')))
    expect(case, 'A05.6 the reader view names the feed',
           (view.get('feed') or {}).get('title') == 'Probe Gamma',
           'feed title=%r' % (view.get('feed') or {}).get('title'))
    expect(case, 'A05.7 the reader view carries the stored content',
           bool((view.get('content') or '').strip()),
           'content length=%d' % len(view.get('content') or ''))
    expected_prev = by_url[newest].get('id') if newest in by_url else None
    expected_next = by_url[oldest].get('id') if oldest in by_url else None
    expect(case, 'A05.8 the previous entry is the more recently changed read entry',
           view.get('prev_entry_id') == expected_prev,
           'prev_entry_id=%r expected=%r' % (view.get('prev_entry_id'), expected_prev))
    expect(case, 'A05.9 the next entry is the older read entry',
           view.get('next_entry_id') == expected_next,
           'next_entry_id=%r expected=%r' % (view.get('next_entry_id'), expected_next))
    status, _payload, _text = api('GET', '/api/v1/entries/99999999')
    expect(case, 'A05.10 an unknown item id is reported as not found', status == 404,
           'GET /api/v1/entries/99999999 -> %s' % status)


def case_a02(ctx):
    '''Reading state: individual and bulk marks, counts, independent starred flag.'''
    case = 'A02'
    status, payload, text = api('POST', '/api/v1/feeds',
                                {'feed_url': ctx.fixture_url('feeds/beta.xml'),
                                 'category_id': ctx.cat('b')})
    if not expect(case, 'A02.1 the feed URL is accepted', status == 201,
                  'POST /api/v1/feeds -> %s %s' % (status, trim(text))):
        return
    feed = payload if isinstance(payload, dict) else {}
    beta_id = feed.get('id')
    expect(case, 'A02.2 the two published items are unread', feed.get('unread_count') == 2,
           'unread_count=%r' % feed.get('unread_count'))
    counts = unread_counts(ctx)
    expect(case, 'A02.3 the unread count names the feed',
           bool(counts) and counts['by_feed'].get(beta_id) == 2,
           'by_feed=%r' % (counts['by_feed'] if counts else None))
    listing = entries_for(ctx, {'status': 'unread', 'feed_id': beta_id, 'limit': 50})
    by_url = {}
    for entry in (listing or {}).get('entries') or []:
        by_url[entry.get('url')] = entry
    first_url = 'https://probe.invalid/beta/1'
    second_url = 'https://probe.invalid/beta/2'
    if not expect(case, 'A02.4 both items are listed',
                  first_url in by_url and second_url in by_url,
                  'unread urls=%r' % sorted(by_url.keys())):
        return
    first = by_url[first_url]
    second = by_url[second_url]
    total_before = counts['total'] if counts else 0

    status, payload, text = api('PUT', '/api/v1/entries/%d' % first.get('id'), {'starred': True})
    starred = payload if isinstance(payload, dict) else {}
    expect(case, 'A02.5 starring keeps the item unread',
           status == 200 and starred.get('starred') is True and starred.get('status') == 'unread',
           'status=%r starred=%r' % (starred.get('status'), starred.get('starred')))

    status, payload, text = api('PUT', '/api/v1/entries/%d' % first.get('id'), {'status': 'read'})
    read = payload if isinstance(payload, dict) else {}
    expect(case, 'A02.6 marking read keeps the starred flag',
           status == 200 and read.get('status') == 'read' and read.get('starred') is True,
           'status=%r starred=%r' % (read.get('status'), read.get('starred')))

    listing = entries_for(ctx, {'status': 'unread', 'feed_id': beta_id, 'limit': 50})
    expect(case, 'A02.7 the read item left the unread view', (listing or {}).get('total') == 1,
           'unread total for the feed: %r' % (listing or {}).get('total'))
    counts = unread_counts(ctx)
    expect(case, 'A02.8 the unread count fell by one',
           bool(counts) and counts['by_feed'].get(beta_id) == 1
           and counts['total'] == total_before - 1,
           'total=%r (was %r), by_feed=%r'
           % (counts['total'] if counts else None, total_before,
              counts['by_feed'] if counts else None))

    starred_listing = entries_for(ctx, {'starred': 'true', 'limit': 100})
    starred_entry = None
    for entry in (starred_listing or {}).get('entries') or []:
        if entry.get('id') == first.get('id'):
            starred_entry = entry
    expect(case, 'A02.9 the starred item is still listed as starred and read',
           starred_entry is not None and starred_entry.get('starred') is True
           and starred_entry.get('status') == 'read',
           'entry=%r' % (None if starred_entry is None else {'status': starred_entry.get('status'),
                                                           'starred': starred_entry.get('starred')}))

    status, payload, text = api('PUT', '/api/v1/feeds/%d/entries' % beta_id, {'status': 'read'})
    expect(case, 'A02.10 marking the whole feed read is accepted', status == 200,
           '-> %s %s' % (status, trim(text)))
    status, payload, text = api('GET', '/api/v1/entries/%d' % second.get('id'))
    counts = unread_counts(ctx)
    expect(case, 'A02.11 the feed has no unread entry left',
           status == 200 and (payload or {}).get('status') == 'read'
           and bool(counts) and counts['by_feed'].get(beta_id, 0) == 0,
           'second item status=%r, by_feed=%r'
           % ((payload or {}).get('status'), counts['by_feed'] if counts else None))

    status, payload, text = api('POST', '/api/v1/feeds',
                                {'feed_url': ctx.fixture_url('feeds/zeta.xml'),
                                 'category_id': ctx.cat('c')})
    if expect(case, 'A02.12 the second feed of the category is accepted', status == 201,
              '-> %s %s' % (status, trim(text))):
        zeta_id = (payload or {}).get('id')
        api('PUT', '/api/v1/categories/%d/entries' % ctx.cat('c'), {'status': 'read'})
        counts = unread_counts(ctx)
        expect(case, 'A02.13 marking the whole category read clears it',
               bool(counts) and counts['by_feed'].get(zeta_id, 0) == 0,
               'by_feed=%r' % (counts['by_feed'] if counts else None))

    status, payload, text = api('PUT', '/api/v1/entries/read-all', {'status': 'read'})
    counts = unread_counts(ctx)
    expect(case, 'A02.14 marking everything read clears the total',
           status == 200 and bool(counts) and counts['total'] == 0,
           'total=%r' % (counts['total'] if counts else None))
    status, _payload, text = api('PUT', '/api/v1/entries/%d' % second.get('id'), {'status': 'archived'})
    expect(case, 'A02.15 an unknown status is refused', status == 400,
           '-> %s %s' % (status, trim(text)))


def case_a04(ctx):
    '''Subscription list: accepted sources and refused ones.'''
    case = 'A04'
    main = ctx.cat('main')
    status, payload, text = api('POST', '/api/v1/feeds',
                                {'feed_url': ctx.fixture_url('feeds/delta.xml'),
                                 'category_id': main})
    if not expect(case, 'A04.1 a feed URL is accepted into the category', status == 201,
                  '-> %s %s' % (status, trim(text))):
        return
    feed = payload if isinstance(payload, dict) else {}
    delta_id = feed.get('id')
    expect(case, 'A04.2 the feed carries the title of the parsed feed',
           feed.get('title') == 'Probe Delta', 'title=%r' % feed.get('title'))
    feeds = list_feeds(ctx) or []
    listed = [row for row in feeds
              if row.get('category_id') == main and row.get('id') == delta_id]
    expect(case, 'A04.3 the feed is listed inside the category', len(listed) == 1,
           'feeds in the category: %r'
           % [row.get('title') for row in feeds if row.get('category_id') == main])
    expect(case, 'A04.4 the listed feed carries its unread count',
           bool(listed) and listed[0].get('unread_count') == 1,
           'unread_count=%r' % (listed[0].get('unread_count') if listed else None))
    before = len(feeds)

    status, _payload, text = api('POST', '/api/v1/feeds',
                                 {'feed_url': ctx.fixture_url('feeds/delta.xml'),
                                  'category_id': main})
    expect(case, 'A04.5 a duplicate feed URL is refused', status == 409,
           '-> %s %s' % (status, trim(text)))
    after_duplicate = len(list_feeds(ctx) or [])
    expect(case, 'A04.6 the refused duplicate wrote nothing', after_duplicate == before,
           'feeds before=%d after=%d' % (before, after_duplicate))

    status, _payload, text = api('POST', '/api/v1/feeds',
                                 {'feed_url': ctx.fixture_url('feeds/epsilon.xml'),
                                  'category_id': 999999})
    expect(case, 'A04.7 an unknown category is refused', status == 404,
           '-> %s %s' % (status, trim(text)))
    after_category = len(list_feeds(ctx) or [])
    expect(case, 'A04.8 the refused subscription wrote nothing', after_category == before,
           'feeds before=%d after=%d' % (before, after_category))

    status, _payload, text = api('POST', '/api/v1/feeds',
                                 {'feed_url': 'not a url', 'category_id': main})
    expect(case, 'A04.9 a malformed URL is refused', status == 400,
           '-> %s %s' % (status, trim(text)))

    status, _payload, text = api('POST', '/api/v1/feeds',
                                 {'feed_url': ctx.fixture_url('sites/no-feed.html'),
                                  'category_id': main})
    expect(case, 'A04.10 a page that advertises no feed is refused', status == 400,
           '-> %s %s' % (status, trim(text)))

    status, _payload, text = api('POST', '/api/v1/feeds',
                                 {'feed_url': ctx.fixture_url('not-a-feed.txt'),
                                  'category_id': main})
    expect(case, 'A04.11 a body that is not a feed is refused', status == 400,
           '-> %s %s' % (status, trim(text)))
    after_refusals = len(list_feeds(ctx) or [])
    expect(case, 'A04.12 no refused attempt wrote a subscription', after_refusals == before,
           'feeds before=%d after=%d' % (before, after_refusals))

    status, payload, text = api('POST', '/api/v1/feeds',
                                {'feed_url': ctx.fixture_url('sites/with-feed.html'),
                                 'category_id': main})
    discovered = payload if isinstance(payload, dict) else {}
    expect(case, 'A04.13 a site URL resolves to the feed it advertises',
           status == 201 and discovered.get('feed_url') == ctx.fixture_url('feeds/epsilon.xml'),
           '-> %s feed_url=%r expected=%r'
           % (status, discovered.get('feed_url'), ctx.fixture_url('feeds/epsilon.xml')))
    expect(case, 'A04.14 the discovered feed is listed in the category',
           any(row.get('feed_url') == ctx.fixture_url('feeds/epsilon.xml')
               and row.get('category_id') == main
               for row in list_feeds(ctx) or []),
           'feeds=%r' % [row.get('feed_url') for row in list_feeds(ctx) or []])


def case_a03(ctx):
    '''Portability: export the list, re-import it, create no duplicate.'''
    case = 'A03'
    status, _payload, text = api('GET', '/api/v1/export')
    if not expect(case, 'A03.1 the subscription list exports as OPML',
                  status == 200 and '<opml' in text, '-> %s' % status):
        return
    export_body = text
    feeds = list_feeds(ctx) or []
    categories = {}
    for category in list_categories(ctx) or []:
        categories[category.get('id')] = category.get('title')
    try:
        root = ET.fromstring(export_body.encode('utf-8'))
    except (ET.ParseError, ValueError) as exc:
        expect(case, 'A03.2 the export is well formed XML', False, 'parse error: %s' % exc)
        return
    expect(case, 'A03.2 the export is well formed XML', True,
           'parsed %d outlines' % len(list(root.iter('outline'))))
    outlines = []

    def walk(node, parent):
        for child in node.findall('outline'):
            title = child.get('title') or child.get('text') or ''
            if (child.get('xmlUrl') or '').strip():
                outlines.append((parent, child))
                walk(child, title)
            else:
                walk(child, title)

    body = root.find('body')
    walk(body if body is not None else root, '')
    expected = {}
    for feed in feeds:
        expected[feed.get('feed_url')] = feed
    expect(case, 'A03.3 the export holds one outline per subscribed feed',
           len(outlines) == len(feeds),
           '%d feed outlines for %d feeds' % (len(outlines), len(feeds)))
    urls = [outline.get('xmlUrl') for _parent, outline in outlines]
    expect(case, 'A03.4 every subscribed feed URL appears exactly once',
           sorted(urls) == sorted(expected.keys()), 'outline urls=%r' % sorted(urls))
    nested = True
    titled = True
    for parent, outline in outlines:
        feed = expected.get(outline.get('xmlUrl'))
        if feed is None or categories.get(feed.get('category_id')) != parent:
            nested = False
        if feed is not None and outline.get('title') != feed.get('title'):
            titled = False
    expect(case, 'A03.5 every feed outline sits inside its category outline', nested,
           'categories=%r' % categories)
    expect(case, 'A03.6 every feed outline carries the feed title', titled,
           'outline titles=%r' % [outline.get('title') for _parent, outline in outlines])

    for feed in feeds:
        api('DELETE', '/api/v1/feeds/%d' % feed.get('id'))
    left = len(list_feeds(ctx) or [])
    expect(case, 'A03.7 the feeds were removed for the round trip', left == 0,
           'feeds left=%d' % left)

    status, payload, text = api('POST', '/api/v1/import', raw=export_body,
                                content_type='text/x-opml')
    imported = payload if isinstance(payload, dict) else {}
    expect(case, 'A03.8 the exported list is imported back',
           status == 200 and imported.get('created') == len(feeds),
           '-> %s created=%r expected=%d errors=%r'
           % (status, imported.get('created'), len(feeds), imported.get('errors')))
    restored = [row.get('feed_url') for row in list_feeds(ctx) or []]
    expect(case, 'A03.9 the same subscriptions exist again',
           sorted(restored) == sorted(expected.keys()), 'restored=%r' % sorted(restored))

    status, payload, text = api('POST', '/api/v1/import', raw=export_body,
                                content_type='text/x-opml')
    again = payload if isinstance(payload, dict) else {}
    expect(case, 'A03.10 importing the same file again creates nothing',
           status == 200 and again.get('created') == 0 and again.get('existing') == len(feeds),
           '-> %s created=%r existing=%r expected=%d'
           % (status, again.get('created'), again.get('existing'), len(feeds)))
    final = [row.get('feed_url') for row in list_feeds(ctx) or []]
    expect(case, 'A03.11 no duplicate subscription was created',
           len(final) == len(restored) and sorted(final) == sorted(restored),
           'feeds=%r' % sorted(final))


def teardown(ctx):
    '''Remove only the records the probe created.'''
    if not ctx.categories:
        return
    try:
        for feed in list_feeds(ctx) or []:
            if feed.get('category_id') in ctx.categories:
                api('DELETE', '/api/v1/feeds/%d' % feed.get('id'))
        for category in list_categories(ctx) or []:
            if (category.get('title') or '').startswith(PROBE_PREFIX):
                api('DELETE', '/api/v1/categories/%d' % category.get('id'))
    except Exception as exc:
        print('teardown could not finish cleanly: %s' % exc)


def print_summary():
    print('')
    for row in RESULTS:
        print('%-5s %-8s %s' % (row['case'], row['status'].upper(), row['message']))
    failed = [row for row in RESULTS if row['status'] == 'fail']
    skipped = [row for row in RESULTS if row['status'] == 'not_run']
    summary = {
        'cases': sorted({row['case'] for row in RESULTS}),
        'checks': len(RESULTS),
        'passed': len(RESULTS) - len(failed) - len(skipped),
        'failed': len(failed),
        'not_run': len(skipped),
        'failures': [{'case': row['case'], 'check': row['check'], 'message': row['message']}
                     for row in failed],
    }
    print('')
    print(json.dumps(summary, indent=2, sort_keys=True))
    if REPORT_PATH:
        with open(REPORT_PATH, 'w', encoding='utf-8') as handle:
            json.dump({'summary': summary, 'results': RESULTS}, handle, indent=2, sort_keys=True)


def main():
    server, state = start_fixture()
    ctx = Context(state)
    exit_code = 0
    try:
        status, payload, text = api('GET', '/api/v1/config')
        polling = payload.get('polling_interval_seconds') if (
            status == 200 and isinstance(payload, dict)) else None
        if not isinstance(polling, (int, float)) or polling <= 0:
            ctx.intake_reason = ('the service does not report polling_interval_seconds on '
                                 'GET /api/v1/config, so the probe cannot size the wait for '
                                 'the scheduler')
        elif polling > INTAKE_TIMEOUT:
            ctx.intake_reason = ('the configured polling interval is %ss, above the probe '
                                 'intake timeout of %ss' % (polling, INTAKE_TIMEOUT))
        else:
            ctx.intake_window = max(INTAKE_TIMEOUT, polling * 4)
        if not setup(ctx):
            return 2
        case_a01(ctx)
        case_a05(ctx)
        case_a02(ctx)
        case_a04(ctx)
        case_a03(ctx)
        failed = [row for row in RESULTS if row['status'] == 'fail']
        exit_code = 1 if failed else 0
    except TargetUnreachable as exc:
        print('the target service is not reachable: %s' % exc)
        exit_code = 2
    finally:
        teardown(ctx)
        server.shutdown()
        server.server_close()
    print_summary()
    return exit_code


if __name__ == '__main__':
    sys.exit(main())