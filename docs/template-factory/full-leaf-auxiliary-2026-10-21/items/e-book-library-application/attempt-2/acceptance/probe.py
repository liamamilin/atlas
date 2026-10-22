#!/usr/bin/env python3
'''Stdlib-only acceptance verifier for the Sideloaded Shelf template (A01-A05).

The target is any HTTP service that honours the contract in README.md and is
startable with --start (default: npm start). Fixtures are built in a disposable
temp directory; no existing library is read or modified.
'''

import argparse
import hashlib
import json
import os
import shutil
import signal
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
import zlib
from xml.sax.saxutils import escape as xml_escape

PNG_SIG = bytes([137, 80, 78, 71, 13, 10, 26, 10])
CONTAINER = ('<?xml version="1.0" encoding="UTF-8"?>'
             '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
             '<rootfiles><rootfile full-path="OEBPS/content.opf" '
             'media-type="application/oebps-package+xml"/></rootfiles></container>')
XHTML = ('<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Chapter</title></head>'
         '<body><p>Chapter one.</p></body></html>')


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as handle:
        for block in iter(lambda: handle.read(65536), b''):
            digest.update(block)
    return digest.hexdigest()


def tree_hashes(root):
    result = {}
    for dirpath, _, names in os.walk(root):
        for name in names:
            full = os.path.join(dirpath, name)
            result[os.path.relpath(full, root)] = sha_file(full)
    return result


def solid_png(rgb=(40, 80, 120), size=8):
    def chunk(tag, payload):
        return (struct.pack('>I', len(payload)) + tag + payload +
                struct.pack('>I', zlib.crc32(tag + payload) & 0xffffffff))
    raw = b''.join(bytes([0]) + bytes(rgb) * size for _ in range(size))
    ihdr = struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)
    return (PNG_SIG + chunk(b'IHDR', ihdr) + chunk(b'IDAT', zlib.compress(raw, 9)) +
            chunk(b'IEND', b''))


def make_epub(path, title, author, identifier, cover=True):
    meta = ''
    if title is not None:
        meta += '<dc:title>' + xml_escape(title) + '</dc:title>'
    if author is not None:
        meta += '<dc:creator>' + xml_escape(author) + '</dc:creator>'
    meta += '<dc:identifier>' + xml_escape(identifier) + '</dc:identifier><dc:language>en</dc:language>'
    if cover:
        meta += '<meta name="cover" content="cover-image"/>'
    opf = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<package xmlns="http://www.idpf.org/2007/opf" version="2.0">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">' + meta + '</metadata>'
           '<manifest><item id="cover-image" href="cover.png" media-type="image/png"/>'
           '<item id="ch1" href="ch1.xhtml" media-type="application/xhtml+xml"/></manifest>'
           '<spine><itemref idref="ch1"/></spine></package>')
    with zipfile.ZipFile(path, 'w') as zf:
        zf.writestr('mimetype', 'application/epub+zip', zipfile.ZIP_STORED)
        zf.writestr('META-INF/container.xml', CONTAINER, zipfile.ZIP_DEFLATED)
        zf.writestr('OEBPS/content.opf', opf, zipfile.ZIP_DEFLATED)
        zf.writestr('OEBPS/ch1.xhtml', XHTML, zipfile.ZIP_DEFLATED)
        if cover:
            zf.writestr('OEBPS/cover.png', solid_png(), zipfile.ZIP_DEFLATED)


def build_fixture(root, outside):
    os.makedirs(os.path.join(root, 'nested'))
    os.makedirs(os.path.join(root, 'copies'))
    os.makedirs(outside)
    paths = {
        'The Dispossessed.epub': os.path.join(root, 'The Dispossessed.epub'),
        'Kindred.epub': os.path.join(root, 'nested', 'Kindred.epub'),
        'mystery draft.epub': os.path.join(root, 'mystery draft.epub'),
        'dispossessed-copy.epub': os.path.join(root, 'copies', 'dispossessed-copy.epub'),
        'broken.epub': os.path.join(root, 'broken.epub'),
        'escape.epub': os.path.join(root, 'escape.epub'),
    }
    make_epub(paths['The Dispossessed.epub'], 'The Dispossessed', 'Ursula K. Le Guin', 'urn:isbn:9780061054884')
    make_epub(paths['Kindred.epub'], 'Kindred', 'Octavia E. Butler', 'urn:isbn:9780807083697', cover=False)
    make_epub(paths['mystery draft.epub'], None, None, 'urn:uuid:0f4b2f6e-4d3a-4a0e-9d1c-3d2f1a6b7c88')
    with open(paths['The Dispossessed.epub'], 'rb') as handle:
        original = handle.read()
    with open(paths['dispossessed-copy.epub'], 'wb') as handle:
        handle.write(original)
    with open(paths['broken.epub'], 'wb') as handle:
        handle.write(b'this is not a zip archive')
    outside_book = os.path.join(outside, 'secret.epub')
    make_epub(outside_book, 'Outside Book', 'Nobody', 'urn:uuid:11111111-2222-3333-4444-555555555555')
    escape_ok = True
    try:
        os.symlink(outside_book, paths['escape.epub'])
    except (OSError, NotImplementedError):
        escape_ok = False
    hashes = {}
    for name in ('The Dispossessed.epub', 'Kindred.epub', 'mystery draft.epub'):
        hashes[name] = sha_file(paths[name])
    return {'root': root, 'outside': outside, 'paths': paths, 'hashes': hashes, 'escape_ok': escape_ok}


class Resp:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def json(self):
        try:
            return json.loads(self.body.decode('utf-8'))
        except Exception:
            return None

    def header(self, name):
        for key, value in self.headers.items():
            if key.lower() == name.lower():
                return value
        return None


class Api:
    def __init__(self, base):
        self.base = base

    def call(self, method, path, body=None, headers=None):
        data = None
        hdrs = {'Accept': 'application/json'}
        if body is not None:
            data = json.dumps(body).encode('utf-8')
            hdrs['Content-Type'] = 'application/json'
        if headers:
            hdrs.update(headers)
        request = urllib.request.Request(self.base + path, data=data, method=method, headers=hdrs)
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return Resp(response.status, dict(response.headers), response.read())
        except urllib.error.HTTPError as error:
            return Resp(error.code, dict(error.headers), error.read())

    def get(self, path):
        return self.call('GET', path)

    def book(self, book_id):
        return self.call('GET', '/api/books/' + urllib.parse.quote(str(book_id)))

    def scan(self, root):
        return self.call('POST', '/api/scans', {'root': root})

    def search(self, term):
        return self.call('GET', '/api/books?' + urllib.parse.urlencode({'q': term}))


def free_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


class Service:
    def __init__(self, cmd, env, log_path):
        self.cmd = cmd
        self.env = env
        self.log_path = log_path
        self.proc = None
        self.api = None
        self.log = None

    def start(self):
        port = free_port()
        env = dict(self.env)
        env['PORT'] = str(port)
        self.log = open(self.log_path, 'ab')
        self.proc = subprocess.Popen(self.cmd, env=env, stdout=self.log,
                                     stderr=subprocess.STDOUT, start_new_session=True)
        self.api = Api('http://127.0.0.1:' + str(port))
        deadline = time.time() + 90
        while time.time() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError('target exited during startup with code ' + str(self.proc.returncode))
            try:
                with urllib.request.urlopen(self.api.base + '/healthz', timeout=3) as response:
                    if response.status == 200:
                        return self.api
            except Exception:
                pass
            time.sleep(0.25)
        raise RuntimeError('target /healthz was not ready within 90s')

    def stop(self):
        proc = self.proc
        self.proc = None
        if proc is None:
            return
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except Exception:
            proc.terminate()
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            except Exception:
                proc.kill()
            proc.wait(timeout=10)
        if self.log is not None:
            self.log.close()
            self.log = None


class Checker:
    def __init__(self):
        self.failures = []

    def check(self, condition, message):
        if condition:
            print('  ok   ' + message)
        else:
            print('  FAIL ' + message)
            self.failures.append(message)
        return bool(condition)

    def case(self, heading):
        print('')
        print(heading)
        return len(self.failures)

    def end(self, heading, mark):
        added = len(self.failures) - mark
        print(heading + ' ' + ('PASS' if added == 0 else 'FAIL (' + str(added) + ')'))
        return added == 0


def find_entry(api, title):
    listing = api.get('/api/books').json() or {}
    for item in listing.get('items') or []:
        if item.get('title') == title:
            return item
    return None


def case_a01(api, fixture, ck):
    scan = api.scan(fixture['root'])
    ck.check(scan.status == 200, 'scan returns 200, got ' + str(scan.status))
    report = scan.json() or {}
    counts = report.get('counts') or {}
    ck.check(counts.get('created') == 3, 'first scan creates 3 entries, got ' + str(counts.get('created')))
    ck.check(counts.get('duplicates') == 1, 'byte-identical copy reported as duplicate, got ' + str(counts.get('duplicates')))
    by_name = {}
    for item in report.get('items') or []:
        by_name[os.path.basename(item.get('path') or '')] = item
    ck.check((by_name.get('The Dispossessed.epub') or {}).get('status') == 'created', 'primary EPUB ingested')
    ck.check((by_name.get('dispossessed-copy.epub') or {}).get('status') == 'duplicate', 'second copy reported duplicate')
    ck.check((by_name.get('broken.epub') or {}).get('status') == 'failed', 'invalid EPUB reported failed')
    if fixture['escape_ok']:
        escape = by_name.get('escape.epub') or {}
        ck.check(escape.get('status') in ('failed', 'ignored') and 'outside' in (escape.get('reason') or ''),
                 'escaping symlink rejected with an outside-root reason')
    listing = api.get('/api/books').json() or {}
    ck.check(listing.get('total') == 3, 'catalog holds 3 entries after first scan, got ' + str(listing.get('total')))
    entries = {}
    for item in listing.get('items') or []:
        entries[item.get('title')] = item
    ck.check((entries.get('The Dispossessed') or {}).get('author') == 'Ursula K. Le Guin', 'embedded author read')
    ck.check((entries.get('The Dispossessed') or {}).get('metadata_source') == 'embedded', 'embedded metadata provenance recorded')
    ck.check((entries.get('mystery draft') or {}).get('metadata_source') == 'filename', 'missing title derived from the filename')
    for title in ('The Dispossessed', 'Kindred', 'mystery draft'):
        entry = entries.get(title) or {}
        cover = api.get(entry.get('cover_url') or '/no-cover')
        ck.check(cover.status == 200 and (cover.header('Content-Type') or '').startswith('image/'), title + ' has a resolvable cover image')
        ck.check(entry.get('cover_source') in ('embedded', 'sidecar', 'placeholder'), title + ' records a cover source')
    dispossessed = (entries.get('The Dispossessed') or {}).get('files') or []
    ck.check(len(dispossessed) == 1 and dispossessed[0].get('sha256') == fixture['hashes']['The Dispossessed.epub'], 'entry file hash matches the fixture bytes')
    ids_before = sorted(str(item.get('id')) for item in entries.values())
    second = api.scan(fixture['root'])
    counts2 = (second.json() or {}).get('counts') or {}
    ck.check(second.status == 200 and counts2.get('created') == 0, 'second scan creates nothing, got ' + str(counts2.get('created')))
    listing2 = api.get('/api/books').json() or {}
    ck.check(listing2.get('total') == 3, 'second scan keeps the catalog at 3')
    ck.check(sorted(str(item.get('id')) for item in listing2.get('items') or []) == ids_before, 'entry ids are stable across rescan')


def case_a02(state, fixture, ck, service):
    api = state['api']
    entry = find_entry(api, 'mystery draft')
    if not ck.check(entry is not None, 'derived entry is present for correction'):
        return
    book_id = entry['id']
    revision = entry['revision']
    stale = api.call('PATCH', '/api/books/' + str(book_id), {'revision': revision + 50, 'title': 'Stale Write'})
    ck.check(stale.status == 409 and (stale.json() or {}).get('error') == 'revision_conflict', 'stale revision rejected with 409 revision_conflict')
    bad = api.call('PATCH', '/api/books/' + str(book_id), {'revision': revision, 'isbn': '123'})
    ck.check(bad.status == 422 and (bad.json() or {}).get('error') == 'unknown_field', 'unsupported PATCH field rejected with 422 unknown_field')
    patched = api.call('PATCH', '/api/books/' + str(book_id), {'revision': revision, 'title': 'The Analytical Engine', 'author': 'Ada Lovelace'})
    body = patched.json() or {}
    ck.check(patched.status == 200 and body.get('title') == 'The Analytical Engine' and body.get('author') == 'Ada Lovelace', 'valid PATCH corrects title and author')
    ck.check(body.get('revision') == revision + 1, 'revision increments by one, got ' + str(body.get('revision')))
    ck.check(body.get('metadata_source') == 'manual' and set(body.get('manual_fields') or []) == {'title', 'author'}, 'correction records manual provenance')
    created = api.call('POST', '/api/collections', {'name': 'To Read'})
    ck.check(created.status == 201, 'collection creation returns 201, got ' + str(created.status))
    duplicate = api.call('POST', '/api/collections', {'name': 'To Read'})
    ck.check(duplicate.status == 409 and (duplicate.json() or {}).get('error') == 'collection_exists', 'duplicate collection name rejected')
    assigned = api.call('PUT', '/api/books/' + str(book_id) + '/collections', {'names': ['To Read']})
    assigned_body = assigned.json() or {}
    ck.check(assigned.status == 200 and assigned_body.get('collections') == ['To Read'], 'entry assigned to To Read')
    unknown = api.call('PUT', '/api/books/' + str(book_id) + '/collections', {'names': ['No Such Shelf']})
    ck.check(unknown.status == 422 and (unknown.json() or {}).get('error') == 'unknown_collection', 'unknown collection rejected')
    still = api.book(book_id).json() or {}
    ck.check(still.get('collections') == ['To Read'], 'rejected collection write leaves the assignment unchanged')
    service.stop()
    state['api'] = service.start()
    api = state['api']
    after = api.book(book_id).json() or {}
    ck.check(after.get('title') == 'The Analytical Engine' and after.get('author') == 'Ada Lovelace', 'corrected metadata survives restart')
    ck.check(after.get('collections') == ['To Read'], 'collection assignment survives restart')
    rescan = api.scan(fixture['root'])
    ck.check(((rescan.json() or {}).get('counts') or {}).get('created') == 0, 'rescan adds nothing')
    final = api.book(book_id).json() or {}
    ck.check(final.get('title') == 'The Analytical Engine' and final.get('author') == 'Ada Lovelace' and final.get('collections') == ['To Read'], 'rescan does not revert manual curation')


def case_a03(api, fixture, ck):
    response = api.search('author:"Ada Lovelace"')
    payload = response.json() or {}
    items = payload.get('items') or []
    ck.check(response.status == 200 and payload.get('total') == 1 and items and items[0].get('title') == 'The Analytical Engine', 'quoted author search finds only the corrected entry')
    response = api.search('title:DISpossessed')
    ck.check(response.status == 200 and (response.json() or {}).get('total') == 1, 'title field search is case-insensitive')
    response = api.search('collection:"To Read"')
    ck.check(response.status == 200 and (response.json() or {}).get('total') == 1, 'collection field search finds the assigned entry')
    response = api.search('author:"Nobody Known"')
    ck.check(response.status == 200 and (response.json() or {}).get('total') == 0, 'unmatched author returns no entries')
    response = api.search('collection:"No Such Shelf"')
    ck.check(response.status == 200 and (response.json() or {}).get('total') == 0, 'unmatched collection returns no entries')
    response = api.search('isbn:9780061054884')
    ck.check(response.status == 422 and (response.json() or {}).get('error') == 'unknown_field', 'unsupported field rejected with 422 unknown_field')
    response = api.search('title:"The Dispossessed" author:"Ursula K. Le Guin"')
    ck.check(response.status == 200 and (response.json() or {}).get('total') == 1, 'multiple field terms are ANDed')


def case_a04(api, fixture, ck):
    entry = find_entry(api, 'The Dispossessed')
    if not ck.check(entry is not None, 'download fixture entry present'):
        return
    path = '/api/books/' + str(entry['id']) + '/file'
    response = api.get(path)
    ck.check(response.status == 200, 'file GET returns 200, got ' + str(response.status))
    ck.check(sha_bytes(response.body) == fixture['hashes']['The Dispossessed.epub'], 'downloaded bytes are identical to the shelf file')
    ck.check((response.header('Content-Type') or '').split(';')[0] == 'application/epub+zip', 'EPUB content type reported')
    ck.check('attachment' in (response.header('Content-Disposition') or '').lower(), 'download is an attachment')
    head = api.call('HEAD', path)
    ck.check(head.status == 200 and head.header('Content-Length') == str(len(response.body)) and head.body == b'', 'HEAD reports the same size with an empty body')
    missing = api.get(path + '?format=mobi')
    ck.check(missing.status == 404 and (missing.json() or {}).get('error') == 'format_not_found', 'missing mobi format returns 404 format_not_found')
    unknown = api.get('/api/books/99999999/file')
    ck.check(unknown.status == 404 and (unknown.json() or {}).get('error') == 'book_not_found', 'unknown entry file returns 404 book_not_found')
    traversal = api.get(path + '?format=' + urllib.parse.quote('../../etc/passwd'))
    ck.check(traversal.status in (400, 404, 422) and b'root:' not in traversal.body, 'path-like format token is rejected without leaking files')
    ck.check(api.book(99999999).status == 404, 'unknown entry detail returns 404')


def case_a05(api, fixture, ck):
    entry = find_entry(api, 'The Analytical Engine')
    if not ck.check(entry is not None, 'removal fixture entry present'):
        return
    book_id = entry['id']
    before = tree_hashes(fixture['root'])
    bare = api.call('DELETE', '/api/books/' + str(book_id))
    ck.check(bare.status in (400, 409, 422), 'removal requires an explicit file policy, got ' + str(bare.status))
    ck.check(api.book(book_id).status == 200, 'rejected removal keeps the entry')
    bad = api.call('DELETE', '/api/books/' + str(book_id) + '?file_policy=delete')
    ck.check(bad.status == 422 and (bad.json() or {}).get('error') == 'invalid_file_policy', 'file-deleting policy refused with 422 invalid_file_policy')
    removed = api.call('DELETE', '/api/books/' + str(book_id) + '?file_policy=catalog_only')
    ck.check(removed.status == 204 and removed.body == b'', 'catalog-only removal returns 204 with no body')
    ck.check(api.book(book_id).status == 404, 'removed entry is gone from the catalog')
    listing = api.get('/api/books').json() or {}
    ck.check(listing.get('total') == 2, 'removal reduces the catalog to 2 entries')
    ck.check((api.search('title:"The Analytical Engine"').json() or {}).get('total') == 0, 'removed entry is no longer searchable by its corrected title')
    ck.check((api.search('collection:"To Read"').json() or {}).get('total') == 0, 'removed entry leaves no collection hit')
    again = api.call('DELETE', '/api/books/' + str(book_id) + '?file_policy=catalog_only')
    ck.check(again.status == 404, 'second removal of the same id returns 404')
    unknown = api.call('DELETE', '/api/books/99999999?file_policy=catalog_only')
    ck.check(unknown.status == 404, 'removing an unknown id returns 404')
    after = tree_hashes(fixture['root'])
    ck.check(after == before, 'catalog-only removal leaves every shelf file byte-identical')
    rescan = api.scan(fixture['root'])
    ck.check(((rescan.json() or {}).get('counts') or {}).get('created') == 1, 'rescan re-adds the still-present file once')
    ck.check((api.get('/api/books').json() or {}).get('total') == 3, 'catalog returns to 3 entries after rescan')
    readded = find_entry(api, 'mystery draft')
    if ck.check(readded is not None, 're-added entry reappears with derived metadata'):
        ck.check(str(readded.get('id')) != str(book_id), 're-added entry receives a new id')
        ck.check(readded.get('collections') == [], 're-added entry carries no prior collection assignment')
    ck.check((api.search('author:"Ada Lovelace"').json() or {}).get('total') == 0, 'manual correction is not resurrected by rescan')
    third = api.scan(fixture['root'])
    ck.check(((third.json() or {}).get('counts') or {}).get('created') == 0 and (api.get('/api/books').json() or {}).get('total') == 3, 'third scan is idempotent')


def main(argv=None):
    parser = argparse.ArgumentParser(description='Verify A01-A05 of the Sideloaded Shelf template over HTTP.')
    parser.add_argument('--start', nargs=argparse.REMAINDER, default=None,
                        help='target start command; default: npm start')
    parser.add_argument('--keep', action='store_true', help='keep disposable fixtures and the service log')
    args = parser.parse_args(argv)
    cmd = args.start or ['npm', 'start']
    tmp = tempfile.mkdtemp(prefix='shelf-accept-')
    ck = Checker()
    service = None
    results = []
    status = 0
    try:
        fixture = build_fixture(os.path.join(tmp, 'shelf'), os.path.join(tmp, 'outside'))
        env = dict(os.environ)
        env.update({
            'ATLAS_DATA_DIR': os.path.join(tmp, 'data'),
            'ATLAS_LIBRARY_ROOT': fixture['root'],
            'HOST': '127.0.0.1',
        })
        service = Service(cmd, env, os.path.join(tmp, 'service.log'))
        state = {'api': service.start()}
        cases = [
            ('A01', 'scan, covers, idempotent rescan', lambda: case_a01(state['api'], fixture, ck)),
            ('A02', 'correction, collections, restart durability', lambda: case_a02(state, fixture, ck, service)),
            ('A03', 'field-qualified search', lambda: case_a03(state['api'], fixture, ck)),
            ('A04', 'file handoff and negative responses', lambda: case_a04(state['api'], fixture, ck)),
            ('A05', 'catalog-only removal lifecycle', lambda: case_a05(state['api'], fixture, ck)),
        ]
        for label, description, run in cases:
            heading = label + ' ' + description
            mark = ck.case(heading)
            try:
                run()
            except Exception as error:
                ck.check(False, heading + ' raised ' + type(error).__name__ + ': ' + str(error))
            results.append((label, ck.end(heading, mark)))
        service.stop()
        service = None
        passed = [label for label, ok in results if ok]
        print('')
        print('summary: ' + str(len(passed)) + '/' + str(len(results)) + ' cases passed')
        if ck.failures:
            print('failures:')
            for failure in ck.failures:
                print(' - ' + failure)
            status = 1
    except Exception as error:
        print('probe error: ' + type(error).__name__ + ': ' + str(error))
        status = 2
    finally:
        if service is not None:
            service.stop()
        if args.keep:
            print('fixtures kept at ' + tmp)
        else:
            shutil.rmtree(tmp, ignore_errors=True)
    return status


if __name__ == '__main__':
    sys.exit(main())
