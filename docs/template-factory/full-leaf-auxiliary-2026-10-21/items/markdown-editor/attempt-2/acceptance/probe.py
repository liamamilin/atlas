#!/usr/bin/env python3
'''Acceptance orchestrator for the README markup editor template.

Adapter: Node.js >=18 imports the target browser module app/src/core.js and
runs the pure contracts that app/src/app.js wires to the DOM. The browser
shell is verified manually with acceptance_files/README.md.

Exit codes: 0 = all cases pass, 1 = failure, 2 = not_run.
'''

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CASES = {
    'A01': 'selection-based markup insertion',
    'A02': 'derived preview from markup only',
    'A03': 'markup-only save and reopen',
    'A04': 'rendered word and character counts',
}
REQUIRED = ('index.html', 'styles.css', 'package.json', 'src/core.js', 'src/app.js')
MAX_DETAIL = 1200

DRIVER = r'''
import { pathToFileURL } from 'node:url';

const corePath = process.argv[2];
const core = await import(pathToFileURL(corePath).href + '?probe=' + Date.now());
const NL = String.fromCharCode(10);
const CR = String.fromCharCode(13);
const BOM = String.fromCharCode(0xFEFF);
const EMOJI = String.fromCodePoint(0x1F600);
const failures = { A01: [], A02: [], A03: [], A04: [] };

function fail(message) {
  throw new Error(message);
}

function ok(condition, label) {
  if (!condition) fail(label);
}

function eq(actual, expected, label) {
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e) fail(label + ' expected ' + e + ' got ' + a);
}

function eqDoc(actual, expected, label) {
  eq(actual.text, expected.text, label + ' text');
  eq(actual.start, expected.start, label + ' start');
  eq(actual.end, expected.end, label + ' end');
}

function detail(err) {
  return err && err.message ? err.message : String(err);
}

function check(caseId, label, fn) {
  try {
    fn();
  } catch (err) {
    failures[caseId].push(label + ': ' + detail(err));
  }
}

function need(name) {
  if (typeof core[name] !== 'function') fail('missing export ' + name);
}

function throwsCode(code, label, fn) {
  let actual = null;
  try {
    fn();
  } catch (err) {
    actual = err && err.code ? err.code : null;
  }
  if (actual !== code) {
    fail(label + ' expected error code ' + code + ' got ' + String(actual));
  }
}

const doc = (text, start, end) => ({ text: text, start: start, end: end });

check('A01', 'bold wraps the selection', () => {
  need('applyMarkup');
  const original = doc('A plain phrase.', 2, 7);
  const result = core.applyMarkup(original, 'bold');
  eq(result.text, 'A **plain** phrase.', 'bold text');
  eq(result.start, 4, 'bold start');
  eq(result.end, 9, 'bold end');
  eq(result.text.slice(result.start, result.end), 'plain', 'bold selected phrase');
  eq(original.text, 'A plain phrase.', 'input not mutated');
});

check('A01', 'h1 prefixes and is idempotent', () => {
  const result = core.applyMarkup(doc('Title' + NL + 'Body', 0, 5), 'h1');
  eq(result.text, '# Title' + NL + 'Body', 'h1 text');
  eq(result.start, 2, 'h1 start');
  eq(result.end, 7, 'h1 end');
  const again = core.applyMarkup(result, 'h1');
  eq(again.text, result.text, 'idempotent text');
  eq(again.start, 2, 'idempotent start');
  eq(again.end, 7, 'idempotent end');
});

check('A01', 'h1 skips blank lines and existing headings', () => {
  const result = core.applyMarkup(doc('One' + NL + NL + 'Body' + NL, 0, 9), 'h1');
  eq(result.text, '# One' + NL + NL + '# Body' + NL, 'multi-line text');
  eq(result.start, 2, 'multi-line start');
  eq(result.end, 13, 'multi-line end');
  eq(result.text.slice(result.start, result.end), 'One' + NL + NL + '# Body', 'multi-line span');
  const h2 = core.applyMarkup(doc('## Sub', 0, 6), 'h1');
  eq(h2.text, '## Sub', 'existing h2');
});

check('A01', 'empty and blank documents are unchanged', () => {
  const empty = core.applyMarkup(doc('', 0, 0), 'h1');
  eqDoc(empty, { text: '', start: 0, end: 0 }, 'empty doc');
  const blankText = '  ' + NL + '  ';
  const blank = core.applyMarkup(doc(blankText, 0, 0), 'h1');
  eqDoc(blank, { text: blankText, start: 0, end: 0 }, 'blank doc');
});

check('A01', 'caret insertion and UTF-16 offsets', () => {
  const caret = core.applyMarkup(doc('ab', 1, 1), 'bold');
  eq(caret.text, 'a****b', 'caret text');
  eq(caret.start, 3, 'caret start');
  eq(caret.end, 3, 'caret end');
  const wideText = 'a' + EMOJI + 'b';
  const wide = core.applyMarkup(doc(wideText, 1, 3), 'bold');
  eq(wide.text, 'a**' + EMOJI + '**b', 'astral text');
  eq(wide.start, 3, 'astral start');
  eq(wide.end, 5, 'astral end');
});

check('A01', 'invalid selections and actions use coded errors', () => {
  throwsCode('INVALID_SELECTION', 'negative start', () => core.applyMarkup(doc('abc', -1, 1), 'bold'));
  throwsCode('INVALID_SELECTION', 'reversed range', () => core.applyMarkup(doc('abc', 2, 1), 'bold'));
  throwsCode('INVALID_SELECTION', 'past end', () => core.applyMarkup(doc('abc', 0, 4), 'bold'));
  throwsCode('INVALID_SELECTION', 'fractional offset', () => core.applyMarkup(doc('abc', 0.5, 1), 'bold'));
  throwsCode('INVALID_SELECTION', 'non-string text', () => core.applyMarkup({ text: 3, start: 0, end: 0 }, 'bold'));
  throwsCode('UNKNOWN_ACTION', 'unsupported action', () => core.applyMarkup(doc('abc', 0, 1), 'italic'));
});

check('A02', 'headings and strong render from markup', () => {
  need('renderMarkdown');
  const html = core.renderMarkdown('# Title' + NL + NL + 'A **bold** phrase.');
  ok(html.indexOf('<h1>Title</h1>') >= 0, 'missing h1');
  ok(html.indexOf('<strong>bold</strong>') >= 0, 'missing strong');
  ok(html.indexOf('**') < 0, 'literal bold markers remain');
});

check('A02', 'inline code and emphasis render with escaping', () => {
  const html = core.renderMarkdown('Use *care* and `x<y`.');
  ok(html.indexOf('<em>care</em>') >= 0, 'missing em');
  ok(html.indexOf('<code>x&lt;y</code>') >= 0, 'missing escaped code');
  ok(html.indexOf('<y') < 0, 'raw less-than leaked');
  const escaped = core.renderMarkdown('<script>alert(1)</script>');
  ok(escaped.indexOf('&lt;script&gt;') >= 0, 'missing escaped tag');
  ok(escaped.indexOf('<script>') < 0, 'raw script tag leaked');
});

check('A02', 'heading levels, paragraphs and CRLF equivalence', () => {
  ok(core.renderMarkdown('### Sub').indexOf('<h3>Sub</h3>') >= 0, 'missing h3');
  const paragraphs = core.renderMarkdown('one' + NL + 'two' + NL + NL + 'three');
  ok(paragraphs.indexOf('<p>one' + NL + 'two</p>') >= 0, 'soft break lost');
  ok(paragraphs.indexOf('<p>three</p>') >= 0, 'second paragraph missing');
  eq(core.renderMarkdown('A' + CR + NL + 'B'), core.renderMarkdown('A' + NL + 'B'), 'CRLF differs');
  eq(core.renderMarkdown('**x** *y*'), core.renderMarkdown('**x** *y*'), 'not deterministic');
  ok(core.renderMarkdown('**open').indexOf('<strong>') < 0, 'unmatched bold created strong');
});

check('A02', 'non-string render input is rejected', () => {
  throwsCode('INVALID_CONTENT', 'null render', () => core.renderMarkdown(null));
});

check('A03', 'save payload contains markup text only', () => {
  need('createSavePayload');
  need('openText');
  const source = '# T' + NL + 'A **b** phrase.';
  const payload = core.createSavePayload(doc(source, 0, 0));
  eq(payload.filename, 'README.md', 'default filename');
  eq(payload.mime, 'text/markdown', 'mime');
  eq(payload.body, source, 'body identity');
  ok(payload.body.indexOf('<strong>') < 0, 'html styling in body');
  ok(payload.body.indexOf('style=') < 0, 'style data in body');
  const reopened = core.openText(payload.body);
  eq(reopened.text, payload.body, 'reopened body');
  eq(core.renderMarkdown(reopened.text), core.renderMarkdown(source), 'reopened preview');
});

check('A03', 'custom name, CRLF, BOM and reopen identity', () => {
  const named = core.createSavePayload(doc('# T', 0, 0), 'NOTES.MD');
  eq(named.filename, 'NOTES.MD', 'custom filename');
  const crlfSource = 'a' + CR + NL + 'b';
  const crlf = core.createSavePayload(doc(crlfSource, 0, 0));
  eq(crlf.body, crlfSource, 'CRLF preserved on save');
  const bomSource = BOM + '# T';
  const bom = core.createSavePayload(doc(bomSource, 0, 0));
  eq(bom.body, bomSource, 'BOM preserved on save');
  const bomOpen = core.openText(bom.body);
  eq(bomOpen.text, bom.body, 'BOM preserved on open');
  eq(bomOpen.start, 0, 'open start');
  eq(bomOpen.end, 0, 'open end');
  const roundTrip = core.openText(crlf.body);
  eq(roundTrip.text, crlfSource, 'CRLF open identity');
  eq(core.renderMarkdown(roundTrip.text), core.renderMarkdown(crlfSource), 'preview after reopen');
});

check('A03', 'blank saves and unsafe names are refused', () => {
  throwsCode('EMPTY_DOCUMENT', 'empty save', () => core.createSavePayload(doc('', 0, 0)));
  throwsCode('EMPTY_DOCUMENT', 'whitespace save', () => core.createSavePayload(doc('  ' + NL + '  ', 0, 0)));
  const names = ['../README.md', 'nested/README.md', 'README.txt', 'READ ME.md', '.md', 'README.md '];
  for (const name of names) {
    throwsCode('INVALID_FILENAME', 'unsafe name ' + name, () => core.createSavePayload(doc('# T', 0, 0), name));
  }
  const tooLong = 'a'.repeat(118) + '.md';
  throwsCode('INVALID_FILENAME', 'too long name', () => core.createSavePayload(doc('# T', 0, 0), tooLong));
  throwsCode('INVALID_FILENAME', 'non-string name', () => core.createSavePayload(doc('# T', 0, 0), 42));
});

check('A03', 'invalid content and the size cap use coded errors', () => {
  throwsCode('INVALID_CONTENT', 'null doc', () => core.createSavePayload(null));
  throwsCode('INVALID_CONTENT', 'non-string text', () => core.createSavePayload({ text: 42, start: 0, end: 0 }));
  throwsCode('INVALID_CONTENT', 'non-string open', () => core.openText(42));
  const limit = 1048576;
  eq(core.openText('x'.repeat(limit)).text.length, limit, 'limit boundary accepted');
  throwsCode('FILE_TOO_LARGE', 'oversized open', () => core.openText('x'.repeat(limit + 1)));
  throwsCode('FILE_TOO_LARGE', 'oversized save', () => core.createSavePayload(doc('x'.repeat(limit + 1), 0, 0)));
  eq(core.openText('').text, '', 'empty open allowed');
});

check('A04', 'counts reflect rendered text and exclude markup', () => {
  need('countText');
  const counts = core.countText('# Title' + NL + NL + 'A **bold** phrase.');
  eq(counts.words, 4, 'words');
  eq(counts.chars, 17, 'chars');
  eq(Object.keys(counts), ['words', 'chars'], 'key order');
  const plain = core.countText('A plain phrase.');
  const bolded = core.countText('A **plain** phrase.');
  eq(plain.words, 3, 'plain words');
  eq(plain.chars, 13, 'plain chars');
  eq(bolded.words, 3, 'bold words');
  eq(bolded.chars, 13, 'bold chars');
  eq(core.countText('# Title').chars, 5, 'heading prefix counted');
});

check('A04', 'empty text, inline code and UTF-16 counting', () => {
  eq(core.countText('').words, 0, 'empty words');
  eq(core.countText('').chars, 0, 'empty chars');
  eq(core.countText('   ' + NL + '  ').chars, 0, 'blank chars');
  eq(core.countText('**x**').chars, 1, 'markers excluded');
  const code = core.countText('`npm test`');
  eq(code.words, 2, 'code words');
  eq(code.chars, 7, 'code chars');
  eq(core.countText(EMOJI).chars, 2, 'UTF-16 units');
});

check('A04', 'count input must be a string', () => {
  throwsCode('INVALID_CONTENT', 'null count', () => core.countText(null));
});

console.log(JSON.stringify({ failures: failures }));
'''

def emit(payload, as_json):
    if as_json:
        print(json.dumps(payload, indent=2))
        return
    print('status: ' + str(payload.get('status')))
    reason = payload.get('reason')
    if reason:
        print('reason: ' + reason)
    for case_id, case in payload.get('cases', {}).items():
        print(case_id + ' ' + case['status'].upper() + ' - ' + case['description'])
        for item in case.get('failures', []):
            print('  ' + item)

def not_run(reason, as_json):
    emit({'status': 'not_run', 'reason': reason, 'cases': {}}, as_json)
    return 2

def failed(reason, as_json):
    emit({'status': 'fail', 'reason': reason, 'cases': {}}, as_json)
    return 1

def main():
    parser = argparse.ArgumentParser(description='Verify the README markup editor core through its ES module contracts.')
    parser.add_argument('target', nargs='?', default='app', help='path to the app directory')
    parser.add_argument('--json', action='store_true', help='print machine-readable JSON')
    args = parser.parse_args()
    target = Path(args.target).resolve()
    if not target.is_dir():
        return failed('target directory not found: ' + str(target), args.json)
    missing = [name for name in REQUIRED if not (target / name).is_file()]
    if missing:
        return failed('missing required files: ' + ', '.join(missing), args.json)
    node = shutil.which('node')
    if not node:
        return not_run('Node.js >=18 was not found on PATH', args.json)
    try:
        version = subprocess.run([node, '--version'], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return not_run('could not run node --version: ' + str(exc), args.json)
    raw_version = version.stdout.strip()
    try:
        major = int(raw_version.lstrip('v').split('.')[0])
    except ValueError:
        return not_run('could not parse Node version: ' + raw_version, args.json)
    if major < 18:
        return not_run('Node.js >=18 required, found ' + raw_version, args.json)
    core_path = target / 'src' / 'core.js'
    with tempfile.TemporaryDirectory(prefix='readme-editor-probe-') as temp_dir:
        driver_path = Path(temp_dir) / 'driver.mjs'
        driver_path.write_text(DRIVER, encoding='utf-8')
        try:
            proc = subprocess.run([node, str(driver_path), str(core_path)], capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            return failed('driver timed out after 60 seconds', args.json)
        except OSError as exc:
            return failed('could not start driver: ' + str(exc), args.json)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or 'no output').strip()
        return failed('driver exited ' + str(proc.returncode) + ': ' + detail[:MAX_DETAIL], args.json)
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    if not lines:
        return failed('driver produced no JSON', args.json)
    try:
        observed = json.loads(lines[-1])
    except json.JSONDecodeError as exc:
        return failed('driver output was not JSON: ' + str(exc), args.json)
    failures = observed.get('failures')
    if not isinstance(failures, dict):
        return failed('driver JSON has no failures object', args.json)
    cases = {}
    all_ok = True
    for case_id, description in CASES.items():
        items = failures.get(case_id)
        if not isinstance(items, list):
            items = ['case did not run']
        passed = len(items) == 0
        all_ok = all_ok and passed
        cases[case_id] = {
            'description': description,
            'status': 'pass' if passed else 'fail',
            'failures': items,
        }
    emit({'status': 'pass' if all_ok else 'fail', 'reason': '', 'cases': cases}, args.json)
    return 0 if all_ok else 1

if __name__ == '__main__':
    sys.exit(main())
