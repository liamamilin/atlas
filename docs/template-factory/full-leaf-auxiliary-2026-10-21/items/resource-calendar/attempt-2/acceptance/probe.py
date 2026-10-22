#!/usr/bin/env python3
# Portable acceptance probe for the Aurora Resource Calendar web target.
# Standard library only. It does not install, start, or modify the target.
import json
import os
import sys
import uuid
from datetime import date, datetime, timedelta, timezone
from urllib import error, parse, request

BASE = os.environ.get('ATLAS_BASE_URL', 'http://127.0.0.1:8080').rstrip('/')
ROOM = os.environ.get('ATLAS_ROOM_ID', 'aurora')
WEEK = os.environ.get('ATLAS_WEEK_START', '2026-10-19')
OFFSET = os.environ.get('ATLAS_UTC_OFFSET', '+08:00')
ACTOR = 'probe-' + uuid.uuid4().hex[:10]
OTHER = 'probe-other-' + uuid.uuid4().hex[:10]


def die_not_run(reason):
    payload = {'status': 'not_run', 'reason': reason, 'base_url': BASE, 'week_start': WEEK}
    print(json.dumps(payload, indent=2))
    sys.exit(2)


def parse_offset(value):
    if len(value) != 6 or value[0] not in '+-' or value[3] != ':':
        raise ValueError('offset must look like +08:00')
    sign = 1 if value[0] == '+' else -1
    return timezone(sign * timedelta(hours=int(value[1:3]), minutes=int(value[4:6])))


try:
    parse_offset(OFFSET)
except Exception as exc:
    die_not_run('invalid ATLAS_UTC_OFFSET: ' + repr(exc))

try:
    WEEK_DATE = date.fromisoformat(WEEK)
except ValueError:
    die_not_run('ATLAS_WEEK_START must be YYYY-MM-DD')

if WEEK_DATE.weekday() != 0:
    die_not_run('ATLAS_WEEK_START must be a Monday')

THURSDAY = WEEK_DATE + timedelta(days=3)


def stamp(hour, minute, day=None):
    value = day if day is not None else THURSDAY
    return value.isoformat() + 'T' + ('%02d:%02d:00' % (hour, minute)) + OFFSET


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError('time is not a string')
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def instant(value):
    parsed = parse_time(value)
    if parsed.tzinfo is None:
        raise ValueError('time lacks a UTC offset: ' + str(value))
    return parsed.astimezone(timezone.utc)


def same_instant(left, right):
    try:
        return instant(left) == instant(right)
    except Exception:
        return False


def decode(raw):
    if not raw:
        return None
    text = raw.decode('utf-8', 'replace')
    try:
        return json.loads(text)
    except ValueError:
        return text


def call(method, path, body=None, actor=ACTOR, role=None, timeout=10):
    headers = {'Accept': 'application/json', 'X-Actor': actor}
    if role:
        headers['X-Role'] = role
    data = None
    if body is not None:
        data = json.dumps(body).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    req = request.Request(BASE + path, data=data, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=timeout) as response:
            return response.status, decode(response.read()), dict(response.headers)
    except error.HTTPError as exc:
        return exc.code, decode(exc.read()), dict(exc.headers)


def week_path(week=None):
    return '/api/rooms/' + parse.quote(ROOM, safe='') + '/week?weekStart=' + (week or WEEK)


def collection_path():
    return '/api/rooms/' + parse.quote(ROOM, safe='') + '/reservations'


def own_path(week=None):
    return collection_path() + '?weekStart=' + (week or WEEK)


def res_path(rid):
    return collection_path() + '/' + parse.quote(str(rid), safe='')


def error_obj(body):
    if isinstance(body, dict) and isinstance(body.get('error'), dict):
        return body['error']
    return {}


def error_code(body):
    return error_obj(body).get('code')


def reservation_of(body):
    if isinstance(body, dict) and isinstance(body.get('reservation'), dict):
        return body['reservation']
    return None


def rows_of(body):
    if isinstance(body, dict) and isinstance(body.get('reservations'), list):
        return [row for row in body['reservations'] if isinstance(row, dict)]
    return None


def busy_of(body):
    if isinstance(body, dict) and isinstance(body.get('busy'), list):
        return [row for row in body['busy'] if isinstance(row, dict)]
    return None


def overlaps_any(busy, start_value, end_value):
    if not isinstance(busy, list):
        return []
    try:
        start = instant(start_value)
        end = instant(end_value)
    except Exception:
        return []
    hits = []
    for block in busy:
        try:
            block_start = instant(block.get('start'))
            block_end = instant(block.get('end'))
        except Exception:
            continue
        if start < block_end and block_start < end:
            hits.append(block)
    return hits


def busy_signature(busy):
    if not isinstance(busy, list):
        return []
    signature = []
    for block in busy:
        try:
            start = instant(block.get('start')).isoformat()
            end = instant(block.get('end')).isoformat()
        except Exception:
            start = str(block.get('start'))
            end = str(block.get('end'))
        signature.append((block.get('reservationId'), start, end))
    return sorted(signature)


def row_ids(rows):
    return set(row.get('id') for row in rows if isinstance(row.get('id'), str))


ORDER = ['A01', 'A02', 'A03', 'A04']
DESCRIPTIONS = {
    'A01': 'Week view identity, seven days, setup block, privacy, and non-Monday refusal',
    'A02': 'Zero-length and empty-purpose refusals store nothing; the purpose claim is accepted once',
    'A03': 'Overlap refusal carries the existing id and both windows, stores nothing, and adjacency is accepted',
    'A04': 'Non-owner cancel is forbidden; owner cancel reopens the window; re-cancel is not found',
}
CHECKS = {case: 0 for case in ORDER}
FAILURES = []
IDS = {'setup': None, 'claim': None, 'adjacent': None, 'reclaimed': None}


def check(case, condition, message):
    CHECKS[case] += 1
    if not condition:
        FAILURES.append({'case': case, 'message': message})


def run_case(case, fn):
    try:
        fn()
    except Exception as exc:
        check(case, False, 'unexpected exception: ' + repr(exc))


def preflight():
    try:
        status, body, _ = call('GET', week_path())
    except Exception as exc:
        die_not_run('week view request failed: ' + repr(exc))
    if status != 200:
        die_not_run('week view returned HTTP ' + str(status))
    busy = busy_of(body)
    if busy is None:
        die_not_run('week view has no busy array')
    windows = [
        ('09:00-10:00', stamp(9, 0), stamp(10, 0)),
        ('14:00-16:00', stamp(14, 0), stamp(16, 0)),
        ('14:30-15:30', stamp(14, 30), stamp(15, 30)),
        ('16:00-17:00', stamp(16, 0), stamp(17, 0)),
    ]
    occupied = []
    for label, start, end in windows:
        if overlaps_any(busy, start, end):
            occupied.append(label)
    if occupied:
        die_not_run('baseline windows are occupied on Thursday: ' + ', '.join(occupied) + '; use an empty disposable database')


def case_a01():
    status, body, _ = call('GET', week_path())
    check('A01', status == 200, 'week view expected 200, got ' + str(status))
    if status != 200 or not isinstance(body, dict):
        return
    room = body.get('room')
    check('A01', isinstance(room, dict), 'room object is missing')
    if isinstance(room, dict):
        check('A01', room.get('id') == ROOM, 'room.id expected ' + ROOM)
        check('A01', room.get('name') == 'Aurora Conference Room', 'room.name mismatch')
        check('A01', room.get('timezone') == 'Asia/Shanghai', 'room.timezone mismatch')
    days = body.get('days')
    check('A01', isinstance(days, list) and len(days) == 7, 'days must contain seven entries')
    if isinstance(days, list):
        expected = [(WEEK_DATE + timedelta(days=index)).isoformat() for index in range(7)]
        actual = [item.get('date') if isinstance(item, dict) else None for item in days]
        check('A01', actual == expected, 'days dates mismatch: ' + repr(actual))
    busy = busy_of(body)
    check('A01', busy is not None, 'busy must be an array')
    check('A01', not overlaps_any(busy or [], stamp(14, 0), stamp(16, 0)), '14:00-16:00 must be free before the claim')
    next_day = (WEEK_DATE + timedelta(days=1)).isoformat()
    bad_status, bad_body, _ = call('GET', week_path(next_day))
    check('A01', bad_status == 400, 'non-Monday weekStart expected 400, got ' + str(bad_status))
    check('A01', error_code(bad_body) == 'INVALID_WEEK_START', 'non-Monday weekStart expected INVALID_WEEK_START, got ' + str(error_code(bad_body)))
    create_status, created, _ = call('POST', collection_path(), body={'start': stamp(9, 0), 'end': stamp(10, 0), 'purpose': 'Probe setup block'})
    check('A01', create_status == 201, 'setup claim expected 201, got ' + str(create_status))
    reservation = reservation_of(created)
    if not isinstance(reservation, dict) or not isinstance(reservation.get('id'), str):
        check('A01', False, 'setup 201 response lacks reservation.id')
        return
    IDS['setup'] = reservation['id']
    check('A01', same_instant(reservation.get('start'), stamp(9, 0)), 'setup start mismatch: ' + repr(reservation.get('start')))
    check('A01', same_instant(reservation.get('end'), stamp(10, 0)), 'setup end mismatch: ' + repr(reservation.get('end')))
    check('A01', reservation.get('purpose') == 'Probe setup block', 'setup purpose not preserved')
    check('A01', reservation.get('status') == 'confirmed', 'setup status must be confirmed')
    status, body, _ = call('GET', week_path())
    check('A01', status == 200, 'week view after setup expected 200, got ' + str(status))
    busy = busy_of(body) if isinstance(body, dict) else None
    check('A01', busy is not None, 'week view after setup lacks busy array')
    blocks = [block for block in (busy or []) if block.get('reservationId') == IDS['setup']]
    check('A01', len(blocks) == 1, 'setup block must appear exactly once, got ' + str(len(blocks)))
    if len(blocks) == 1:
        block = blocks[0]
        check('A01', same_instant(block.get('start'), stamp(9, 0)), 'setup block start mismatch')
        check('A01', same_instant(block.get('end'), stamp(10, 0)), 'setup block end mismatch')
        check('A01', block.get('mine') is True, 'setup block must be mine for the owner')
        check('A01', block.get('purpose') == 'Probe setup block', 'owner week view must expose own purpose')
    check('A01', not overlaps_any(busy or [], stamp(14, 0), stamp(16, 0)), '14:00-16:00 must remain free after setup')
    other_status, other_body, _ = call('GET', week_path(), actor=OTHER)
    check('A01', other_status == 200, 'other week view expected 200, got ' + str(other_status))
    other_busy = busy_of(other_body) if isinstance(other_body, dict) else None
    other_blocks = [block for block in (other_busy or []) if block.get('reservationId') == IDS['setup']]
    check('A01', len(other_blocks) == 1, 'setup block must be visible to other staff')
    if len(other_blocks) == 1:
        block = other_blocks[0]
        check('A01', block.get('mine') is False, 'setup block must not be mine for other staff')
        check('A01', block.get('purpose') is None, 'other staff must not see the purpose')


def case_a02():
    if not IDS['setup']:
        check('A02', False, 'setup reservation is missing; A02 cannot run')
        return
    status, before_body, _ = call('GET', own_path(), actor=ACTOR)
    check('A02', status == 200, 'own reservations expected 200, got ' + str(status))
    before_rows = rows_of(before_body)
    check('A02', before_rows is not None, 'own reservations array is missing')
    before_rows = before_rows or []
    before_ids = row_ids(before_rows)
    check('A02', IDS['setup'] in before_ids, 'setup reservation missing from own list')
    for row in before_rows:
        try:
            if instant(row.get('start')) == instant(row.get('end')):
                check('A02', False, 'baseline contains a zero-length row: ' + str(row.get('id')))
        except Exception:
            check('A02', False, 'baseline row has invalid times: ' + str(row.get('id')))
    week_status, week_before, _ = call('GET', week_path())
    check('A02', week_status == 200, 'baseline week view expected 200, got ' + str(week_status))
    before_busy = busy_of(week_before) if isinstance(week_before, dict) else None
    check('A02', before_busy is not None, 'baseline week view lacks busy')
    before_signature = busy_signature(before_busy or [])
    zero_status, zero_body, _ = call('POST', collection_path(), body={'start': stamp(14, 0), 'end': stamp(14, 0), 'purpose': 'Zero length'})
    check('A02', zero_status == 400, 'zero-length claim expected 400, got ' + str(zero_status))
    zero_code = error_code(zero_body)
    check('A02', zero_code in ('INVALID_INTERVAL', 'INVALID_DURATION'), 'zero-length claim expected INVALID_INTERVAL or INVALID_DURATION, got ' + str(zero_code))
    status, after_zero_body, _ = call('GET', own_path(), actor=ACTOR)
    check('A02', status == 200, 'own list after zero-length expected 200, got ' + str(status))
    after_zero_rows = rows_of(after_zero_body)
    check('A02', after_zero_rows is not None, 'own list after zero-length lacks reservations')
    after_zero_rows = after_zero_rows or []
    added = row_ids(after_zero_rows) - before_ids
    check('A02', not added, 'rejected zero-length claim added rows: ' + repr(sorted(added)))
    check('A02', len(after_zero_rows) == len(before_rows), 'rejected zero-length claim changed row count')
    for row in after_zero_rows:
        try:
            if instant(row.get('start')) == instant(row.get('end')):
                check('A02', False, 'zero-length row was stored: ' + str(row.get('id')))
        except Exception:
            check('A02', False, 'stored row has invalid times: ' + str(row.get('id')))
    week_status, week_after_zero, _ = call('GET', week_path())
    check('A02', week_status == 200, 'week view after zero-length expected 200')
    after_zero_busy = busy_of(week_after_zero) if isinstance(week_after_zero, dict) else None
    check('A02', busy_signature(after_zero_busy or []) == before_signature, 'rejected zero-length claim changed busy blocks')
    purpose_status, purpose_body, _ = call('POST', collection_path(), body={'start': stamp(14, 0), 'end': stamp(16, 0), 'purpose': '   '})
    check('A02', purpose_status == 400, 'empty purpose expected 400, got ' + str(purpose_status))
    check('A02', error_code(purpose_body) == 'INVALID_PURPOSE', 'empty purpose expected INVALID_PURPOSE, got ' + str(error_code(purpose_body)))
    status, after_purpose_body, _ = call('GET', own_path(), actor=ACTOR)
    check('A02', status == 200, 'own list after empty purpose expected 200')
    after_purpose_rows = rows_of(after_purpose_body)
    check('A02', after_purpose_rows is not None, 'own list after empty purpose lacks reservations')
    after_purpose_rows = after_purpose_rows or []
    check('A02', row_ids(after_purpose_rows) == before_ids, 'empty-purpose refusal changed stored rows')
    claim_status, claim_body, _ = call('POST', collection_path(), body={'start': stamp(14, 0), 'end': stamp(16, 0), 'purpose': 'Training session'})
    check('A02', claim_status == 201, 'main claim expected 201, got ' + str(claim_status))
    claim = reservation_of(claim_body)
    if not isinstance(claim, dict) or not isinstance(claim.get('id'), str):
        check('A02', False, 'main claim 201 lacks reservation.id')
        return
    IDS['claim'] = claim['id']
    check('A02', same_instant(claim.get('start'), stamp(14, 0)), 'main claim start mismatch')
    check('A02', same_instant(claim.get('end'), stamp(16, 0)), 'main claim end mismatch')
    check('A02', claim.get('purpose') == 'Training session', 'main claim purpose not preserved')
    check('A02', claim.get('status') == 'confirmed', 'main claim status must be confirmed')
    status, after_claim_body, _ = call('GET', own_path(), actor=ACTOR)
    check('A02', status == 200, 'own list after claim expected 200')
    after_claim_rows = rows_of(after_claim_body)
    after_claim_rows = after_claim_rows or []
    matches = [row for row in after_claim_rows if row.get('id') == IDS['claim']]
    check('A02', len(matches) == 1, 'claim must appear exactly once in own list, got ' + str(len(matches)))
    if len(matches) == 1:
        check('A02', matches[0].get('purpose') == 'Training session', 'own list purpose mismatch')
        check('A02', matches[0].get('status') == 'confirmed', 'own list status must be confirmed')
    check('A02', row_ids(after_claim_rows) - row_ids(after_purpose_rows) == {IDS['claim']}, 'claim must add exactly one stored row')
    status, week_claim_body, _ = call('GET', week_path(), actor=ACTOR)
    check('A02', status == 200, 'week view after claim expected 200')
    busy = busy_of(week_claim_body) if isinstance(week_claim_body, dict) else None
    busy = busy or []
    hits = overlaps_any(busy, stamp(14, 0), stamp(16, 0))
    check('A02', len(hits) == 1 and hits[0].get('reservationId') == IDS['claim'], '14:00-16:00 must show only the accepted claim')
    matches = [block for block in busy if block.get('reservationId') == IDS['claim']]
    check('A02', len(matches) == 1, 'claim block must appear exactly once')
    if len(matches) == 1:
        check('A02', matches[0].get('purpose') == 'Training session', 'owner must see the claim purpose')
        check('A02', matches[0].get('mine') is True, 'claim must be mine for the owner')


def case_a03():
    if not IDS['claim']:
        check('A03', False, 'main claim is missing; A03 cannot run')
        return
    status, before_body, _ = call('GET', week_path())
    check('A03', status == 200, 'baseline week view expected 200')
    before_busy = busy_of(before_body) if isinstance(before_body, dict) else None
    check('A03', before_busy is not None, 'baseline week view lacks busy')
    before_signature = busy_signature(before_busy or [])
    other_status, other_before_body, _ = call('GET', own_path(), actor=OTHER)
    check('A03', other_status == 200, 'other own list expected 200')
    other_before = row_ids(rows_of(other_before_body) or [])
    status, body, _ = call('POST', collection_path(), actor=OTHER, body={'start': stamp(14, 30), 'end': stamp(15, 30), 'purpose': 'Overlap attempt'})
    check('A03', status == 409, 'overlap expected 409, got ' + str(status))
    error = error_obj(body)
    check('A03', error.get('code') == 'SLOT_CONFLICT', 'overlap expected SLOT_CONFLICT, got ' + str(error.get('code')))
    conflicts = error.get('conflicts')
    check('A03', isinstance(conflicts, list) and len(conflicts) >= 1, 'conflicts must be a non-empty array')
    conflicts = conflicts if isinstance(conflicts, list) else []
    matches = [item for item in conflicts if isinstance(item, dict) and item.get('id') == IDS['claim']]
    check('A03', len(matches) == 1, 'conflicts must name the existing reservation exactly once')
    if len(matches) == 1:
        check('A03', same_instant(matches[0].get('start'), stamp(14, 0)), 'conflict start mismatch')
        check('A03', same_instant(matches[0].get('end'), stamp(16, 0)), 'conflict end mismatch')
    message = error.get('message')
    check('A03', isinstance(message, str), 'conflict message must be a string')
    if isinstance(message, str):
        tokens = [IDS['claim'], THURSDAY.isoformat(), '14:00', '16:00', '14:30', '15:30']
        for token in tokens:
            check('A03', token in message, 'conflict message must name ' + token)
    status, after_body, _ = call('GET', week_path())
    check('A03', status == 200, 'week view after overlap expected 200')
    after_busy = busy_of(after_body) if isinstance(after_body, dict) else None
    check('A03', after_busy is not None, 'week view after overlap lacks busy')
    check('A03', busy_signature(after_busy or []) == before_signature, 'refused overlap changed busy blocks')
    status, other_after_body, _ = call('GET', own_path(), actor=OTHER)
    check('A03', status == 200, 'other own list after overlap expected 200')
    other_after = row_ids(rows_of(other_after_body) or [])
    check('A03', other_after == other_before, 'refused overlap added a row for the other actor')
    status, body, _ = call('POST', collection_path(), actor=OTHER, body={'start': stamp(16, 0), 'end': stamp(17, 0), 'purpose': 'Adjacent follow-up'})
    check('A03', status == 201, 'adjacent claim expected 201, got ' + str(status))
    adjacent = reservation_of(body)
    if not isinstance(adjacent, dict) or not isinstance(adjacent.get('id'), str):
        check('A03', False, 'adjacent 201 lacks reservation.id')
        return
    IDS['adjacent'] = adjacent['id']
    check('A03', same_instant(adjacent.get('start'), stamp(16, 0)), 'adjacent start mismatch')
    check('A03', same_instant(adjacent.get('end'), stamp(17, 0)), 'adjacent end mismatch')
    status, body, _ = call('GET', week_path())
    busy = busy_of(body) if isinstance(body, dict) else None
    busy = busy or []
    claim_blocks = [block for block in busy if block.get('reservationId') == IDS['claim']]
    adjacent_blocks = [block for block in busy if block.get('reservationId') == IDS['adjacent']]
    check('A03', len(claim_blocks) == 1 and len(adjacent_blocks) == 1, 'existing and adjacent blocks must both remain')


def case_a04():
    if not IDS['claim']:
        check('A04', False, 'main claim is missing; A04 cannot run')
        return
    status, body, _ = call('DELETE', res_path(IDS['claim']), actor=OTHER)
    check('A04', status == 403, 'non-owner cancel expected 403, got ' + str(status))
    check('A04', error_code(body) == 'FORBIDDEN', 'non-owner cancel expected FORBIDDEN, got ' + str(error_code(body)))
    status, body, _ = call('GET', week_path())
    busy = busy_of(body) if isinstance(body, dict) else None
    blocks = [block for block in (busy or []) if block.get('reservationId') == IDS['claim']]
    check('A04', len(blocks) == 1, 'non-owner cancel must leave the block')
    status, body, _ = call('DELETE', res_path(IDS['claim']), actor=ACTOR)
    check('A04', status == 204, 'owner cancel expected 204, got ' + str(status))
    status, own_body, _ = call('GET', own_path(), actor=ACTOR)
    rows = rows_of(own_body) if isinstance(own_body, dict) else None
    rows = rows or []
    matches = [row for row in rows if row.get('id') == IDS['claim']]
    check('A04', len(matches) == 1, 'cancelled claim must remain in own audit list')
    if len(matches) == 1:
        check('A04', matches[0].get('status') == 'cancelled', 'cancelled claim status mismatch')
    status, body, _ = call('GET', week_path())
    busy = busy_of(body) if isinstance(body, dict) else None
    busy = busy or []
    check('A04', not [block for block in busy if block.get('reservationId') == IDS['claim']], 'cancelled block must leave availability')
    check('A04', not overlaps_any(busy, stamp(14, 0), stamp(16, 0)), '14:00-16:00 must read free after cancellation')
    status, body, _ = call('POST', collection_path(), actor=OTHER, body={'start': stamp(14, 0), 'end': stamp(16, 0), 'purpose': 'Reclaimed window'})
    check('A04', status == 201, 'fresh claim expected 201, got ' + str(status))
    reclaimed = reservation_of(body)
    if not isinstance(reclaimed, dict) or not isinstance(reclaimed.get('id'), str):
        check('A04', False, 'fresh claim 201 lacks reservation.id')
        return
    IDS['reclaimed'] = reclaimed['id']
    status, body, _ = call('GET', week_path())
    busy = busy_of(body) if isinstance(body, dict) else None
    check('A04', busy is not None, 'week view after fresh claim lacks busy')
    hits = overlaps_any(busy or [], stamp(14, 0), stamp(16, 0))
    check('A04', len(hits) == 1 and hits[0].get('reservationId') == IDS['reclaimed'], 'freed window must show only the fresh claim')
    status, body, _ = call('DELETE', res_path(IDS['claim']), actor=ACTOR)
    check('A04', status == 404, 'repeat cancel expected 404, got ' + str(status))
    check('A04', error_code(body) == 'NOT_FOUND', 'repeat cancel expected NOT_FOUND, got ' + str(error_code(body)))


def cleanup():
    results = []
    for key, actor in (('setup', ACTOR), ('adjacent', OTHER), ('reclaimed', OTHER)):
        rid = IDS.get(key)
        if not rid:
            continue
        try:
            status, _, _ = call('DELETE', res_path(rid), actor=actor)
            results.append({'id': rid, 'status': status})
        except Exception as exc:
            results.append({'id': rid, 'error': repr(exc)})
    return results


def main():
    preflight()
    run_case('A01', case_a01)
    run_case('A02', case_a02)
    run_case('A03', case_a03)
    run_case('A04', case_a04)
    cleanup_results = cleanup()
    cases = []
    failed = False
    for case in ORDER:
        case_failures = [item for item in FAILURES if item.get('case') == case]
        status = 'fail' if case_failures else 'pass'
        if case_failures:
            failed = True
        cases.append({'id': case, 'description': DESCRIPTIONS[case], 'status': status, 'checks': CHECKS[case]})
    payload = {
        'status': 'fail' if failed else 'pass',
        'base_url': BASE,
        'room': ROOM,
        'week_start': WEEK,
        'actor': ACTOR,
        'cases': cases,
        'failures': FAILURES,
        'cleanup': cleanup_results,
    }
    print(json.dumps(payload, indent=2))
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()