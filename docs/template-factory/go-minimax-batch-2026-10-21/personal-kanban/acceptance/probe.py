#!/usr/bin/env python3
'''Acceptance probe for the Personal Project Board target (localhost, single user).

Usage:
    python3 probe.py --base-url http://127.0.0.1:8765 --case A01
    python3 probe.py --base-url http://127.0.0.1:8765 --case all

Cases (one per feature): A01 boards, A02 columns, A03 cards,
A04 movement and ordering, A05 board read model.

The probe writes to a live local server. Each case creates its own disposable
board and deletes only the records that this probe created; no pre-existing
record is ever deleted. Every rejected request is followed by a re-read that
proves the rejected write did not happen.
'''

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
import uuid

PROBE_START = int(time.time())
FEATURE_COUNT = 5
CASE_IDS = ('A01', 'A02', 'A03', 'A04', 'A05')


class ProbeFailure(Exception):
    '''Raised when an assertion about the documented API fails.'''


def check(condition, message):
    if not condition:
        raise ProbeFailure(message)


def parse_json(raw):
    if raw is None:
        return None
    text = raw.strip()
    if text == '':
        return None
    try:
        return json.loads(text)
    except ValueError:
        return {'_raw': text}


def http(base, method, path, payload=None, raw_body=None):
    url = base.rstrip('/') + path
    data = None
    headers = {'Accept': 'application/json'}
    if raw_body is not None:
        data = raw_body.encode('utf-8')
        headers['Content-Type'] = 'application/json'
    elif payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, parse_json(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        return error.code, parse_json(error.read().decode('utf-8'))


def expect_error(status, body, want_status, want_code):
    check(status == want_status, 'expected HTTP %s, got %s (%s)' % (want_status, status, body))
    error = {}
    if isinstance(body, dict):
        error = body.get('error') or {}
    check(error.get('code') == want_code, 'expected error code %s, got %s' % (want_code, body))


def snapshot(base, board_id):
    status, body = http(base, 'GET', '/api/boards/%d' % board_id)
    check(status == 200, 'GET /api/boards/%d failed: %s %s' % (board_id, status, body))
    check(isinstance(body, dict) and 'columns' in body, 'board snapshot has no columns: %s' % body)
    return body


def board_state(snap):
    '''Everything the target stores for one board, for exact zero-write comparison.'''
    return {
        'columns': [(c['id'], c['name'], c['position'], c['card_count']) for c in snap['columns']],
        'cards': [[(card['id'], card['title'], card['description'], card['position'],
                    card['column_id'], card['updated_at']) for card in c['cards']]
                  for c in snap['columns']],
    }


def column_ids(snap):
    return [column['id'] for column in snap['columns']]


def column_names(snap):
    return [column['name'] for column in snap['columns']]


def column_positions(snap):
    return [column['position'] for column in snap['columns']]


def cards_in(snap, column_id):
    for column in snap['columns']:
        if column['id'] == column_id:
            return [card['id'] for card in column['cards']]
    raise ProbeFailure('column %s is not part of the board snapshot' % column_id)


def card_positions(snap, column_id):
    for column in snap['columns']:
        if column['id'] == column_id:
            return [card['position'] for card in column['cards']]
    raise ProbeFailure('column %s is not part of the board snapshot' % column_id)


def card_of(snap, card_id):
    for column in snap['columns']:
        for card in column['cards']:
            if card['id'] == card_id:
                return card
    raise ProbeFailure('card %s is not part of the board snapshot' % card_id)


def make_board(base, name=None, columns=None):
    payload = {'name': name or ('probe-%s' % uuid.uuid4().hex[:8])}
    if columns is not None:
        payload['columns'] = columns
    status, body = http(base, 'POST', '/api/boards', payload)
    check(status == 201, 'board creation failed: %s %s' % (status, body))
    check(isinstance(body, dict) and 'board' in body, 'board response has no board: %s' % body)
    return body['board'], body.get('columns', [])


def make_card(base, board_id, title, column_id, description=None):
    payload = {'title': title, 'column_id': column_id}
    if description is not None:
        payload['description'] = description
    status, body = http(base, 'POST', '/api/boards/%d/cards' % board_id, payload)
    check(status == 201, 'card creation failed: %s %s' % (status, body))
    return body['card']


def drop_board(base, board_id):
    status, body = http(base, 'DELETE', '/api/boards/%d' % board_id)
    check(status == 204, 'board cleanup failed: %s %s' % (status, body))


def case_a01(base):
    status, body = http(base, 'GET', '/api/health')
    check(status == 200, 'GET /api/health failed: %s %s' % (status, body))
    check(isinstance(body, dict) and body.get('status') == 'ok', 'health payload is not ok: %s' % body)

    status, body = http(base, 'GET', '/api/boards')
    check(status == 200, 'GET /api/boards failed: %s %s' % (status, body))
    before = len(body['boards'])

    board, columns = make_board(base, columns=[])
    board_id = board['id']
    check(isinstance(board_id, int) and board_id > 0, 'board id must be a positive integer')
    check(columns == [], 'a board must be created without columns')
    check(isinstance(board['created_at'], int), 'created_at must be an integer epoch second')
    check(isinstance(board['updated_at'], int), 'updated_at must be an integer epoch second')
    check(board['updated_at'] >= board['created_at'], 'updated_at must not be before created_at')
    check(PROBE_START - 10 <= board['created_at'] <= int(time.time()) + 2, 'created_at outside the probe window')
    check(board.get('column_count') == 0 and board.get('card_count') == 0, 'a new board must report empty counts')

    status, body = http(base, 'GET', '/api/boards')
    check(status == 200, 'GET /api/boards failed: %s %s' % (status, body))
    check(len(body['boards']) == before + 1, 'the board list must grow by exactly one board')
    listed = [entry for entry in body['boards'] if entry['id'] == board_id]
    check(len(listed) == 1, 'the created board must appear exactly once in the list')
    check(listed[0]['name'] == board['name'], 'the list must carry the same board name')

    snap = snapshot(base, board_id)
    check(snap['board']['name'] == board['name'], 'GET board must return the same name')
    check(snap['columns'] == [], 'GET board must return no columns for a new board')

    rejections = (
        ({'name': ''}, 422, 'NAME_REQUIRED'),
        ({'name': '   '}, 422, 'NAME_REQUIRED'),
        ({'name': 'x' * 121}, 422, 'NAME_TOO_LONG'),
        ({'name': 'ok', 'status': 'doing'}, 422, 'FORBIDDEN_FIELD'),
        ({'name': 'ok', 'assignee': 'me'}, 422, 'FORBIDDEN_FIELD'),
        ({'name': 'ok', 'colour': 'red'}, 422, 'UNKNOWN_FIELD'),
    )
    for payload, want_status, want_code in rejections:
        status, body = http(base, 'POST', '/api/boards', payload)
        expect_error(status, body, want_status, want_code)
        status, body = http(base, 'GET', '/api/boards')
        check(status == 200, 'GET /api/boards failed: %s %s' % (status, body))
        check(len(body['boards']) == before + 1, 'a rejected board creation wrote a board (%s)' % want_code)

    status, body = http(base, 'POST', '/api/boards', raw_body='{not json')
    expect_error(status, body, 400, 'MALFORMED_JSON')
    status, body = http(base, 'GET', '/api/boards')
    check(len(body['boards']) == before + 1, 'a malformed request wrote a board')

    status, body = http(base, 'GET', '/api/boards/999999999')
    expect_error(status, body, 404, 'BOARD_NOT_FOUND')

    renamed = 'probe-renamed-%s' % uuid.uuid4().hex[:8]
    status, body = http(base, 'PATCH', '/api/boards/%d' % board_id, {'name': renamed})
    check(status == 200, 'board rename failed: %s %s' % (status, body))
    check(body['board']['name'] == renamed, 'the rename was not applied')
    check(body['board']['id'] == board_id, 'the rename changed the board id')
    check(body['board']['updated_at'] >= board['created_at'], 'updated_at went backwards')

    drop_board(base, board_id)
    status, body = http(base, 'GET', '/api/boards/%d' % board_id)
    expect_error(status, body, 404, 'BOARD_NOT_FOUND')
    status, body = http(base, 'GET', '/api/boards')
    check(len(body['boards']) == before, 'the board list must return to its original size')
    return 'boards: create/list/read/rename/delete plus 7 rejected writes with zero-write re-reads'


def case_a02(base):
    board, columns = make_board(base, columns=['待办', '进行中', '完成'])
    board_id = board['id']
    check(len(columns) == 3, 'expected three seeded columns, got %d' % len(columns))
    check([c['name'] for c in columns] == ['待办', '进行中', '完成'], 'seeded column names or order differ')
    check([c['position'] for c in columns] == [1, 2, 3], 'seeded column positions must be 1..3')
    first, second, third = [c['id'] for c in columns]

    snap = snapshot(base, board_id)
    check(column_ids(snap) == [first, second, third], 'board columns are not in the seeded order')
    check(column_positions(snap) == [1, 2, 3], 'board column positions must be 1..3')
    check([c['card_count'] for c in snap['columns']] == [0, 0, 0], 'new columns must be empty')

    status, body = http(base, 'POST', '/api/boards/%d/columns' % board_id, {'name': '阻塞'})
    check(status == 201, 'column creation failed: %s %s' % (status, body))
    fourth = body['column']['id']
    check(body['column']['position'] == 4, 'a new column must be appended at the end')
    snap = snapshot(base, board_id)
    check(column_ids(snap) == [first, second, third, fourth], 'the new column is not at the end')

    status, body = http(base, 'PATCH', '/api/columns/%d' % first, {'name': '待处理'})
    check(status == 200, 'column rename failed: %s %s' % (status, body))
    check(body['column']['name'] == '待处理', 'the column rename was not applied')
    check(body['column']['position'] == 1, 'a rename must not change the column position')

    status, body = http(base, 'PUT', '/api/columns/%d/position' % fourth, {'position': 1})
    check(status == 200, 'column reorder failed: %s %s' % (status, body))
    expected = [fourth, first, second, third]
    check([c['id'] for c in body['columns']] == expected, 'the reorder response order is wrong')
    check([c['position'] for c in body['columns']] == [1, 2, 3, 4], 'the reordered positions must be 1..4')
    snap = snapshot(base, board_id)
    check(column_ids(snap) == expected, 'the reorder was not persisted')
    check(column_positions(snap) == [1, 2, 3, 4], 'the persisted positions must be 1..4')
    check(column_names(snap) == ['阻塞', '待处理', '进行中', '完成'], 'the names did not follow their columns')

    state = board_state(snapshot(base, board_id))
    for payload, want_status, want_code in (
        ({'position': 0}, 422, 'POSITION_OUT_OF_RANGE'),
        ({'position': 99}, 422, 'POSITION_OUT_OF_RANGE'),
    ):
        status, body = http(base, 'PUT', '/api/columns/%d/position' % fourth, payload)
        expect_error(status, body, want_status, want_code)
        check(board_state(snapshot(base, board_id)) == state, 'a rejected column move changed the board')
    status, body = http(base, 'PATCH', '/api/columns/%d' % fourth, {'name': ''})
    expect_error(status, body, 422, 'NAME_REQUIRED')
    check(board_state(snapshot(base, board_id)) == state, 'a rejected rename changed the board')
    status, body = http(base, 'PATCH', '/api/columns/%d' % fourth, {'name': '进行中'})
    expect_error(status, body, 409, 'DUPLICATE_COLUMN_NAME')
    check(board_state(snapshot(base, board_id)) == state, 'a rejected duplicate name changed the board')
    status, body = http(base, 'POST', '/api/boards/%d/columns' % board_id, {'name': '新列', 'task_limit': 3})
    expect_error(status, body, 422, 'FORBIDDEN_FIELD')
    status, body = http(base, 'POST', '/api/boards/%d/columns' % board_id, {'name': '新列', 'wip_limit': 3})
    expect_error(status, body, 422, 'FORBIDDEN_FIELD')
    status, body = http(base, 'POST', '/api/boards/%d/columns' % board_id, {'name': '新列', 'colour': 'red'})
    expect_error(status, body, 422, 'UNKNOWN_FIELD')
    check(board_state(snapshot(base, board_id)) == state, 'a rejected column creation changed the board')

    card = make_card(base, board_id, '占位卡片', fourth)
    status, body = http(base, 'DELETE', '/api/columns/%d' % fourth)
    expect_error(status, body, 409, 'COLUMN_NOT_EMPTY')
    snap = snapshot(base, board_id)
    check(cards_in(snap, fourth) == [card['id']], 'a rejected column delete dropped the card')

    status, body = http(base, 'DELETE', '/api/cards/%d' % card['id'])
    check(status == 204, 'card cleanup failed: %s %s' % (status, body))
    status, body = http(base, 'DELETE', '/api/columns/%d' % fourth)
    check(status == 204, 'column delete failed: %s %s' % (status, body))
    snap = snapshot(base, board_id)
    check(column_ids(snap) == [first, second, third], 'the column was not deleted')
    check(column_positions(snap) == [1, 2, 3], 'the remaining columns must be renumbered 1..3')

    solo_board, solo_columns = make_board(base, columns=['唯一列'])
    status, body = http(base, 'DELETE', '/api/columns/%d' % solo_columns[0]['id'])
    expect_error(status, body, 409, 'LAST_COLUMN')
    status, body = http(base, 'GET', '/api/boards/%d' % solo_board['id'])
    check(status == 200 and len(body['columns']) == 1, 'the last column was removed')
    drop_board(base, solo_board['id'])
    drop_board(base, board_id)
    return 'columns: seed/add/rename/reorder plus 7 rejected writes, delete guards, renumbering to 1..N'


def case_a03(base):
    board, columns = make_board(base, columns=['待办', '进行中'])
    board_id = board['id']
    first, second = [c['id'] for c in columns]

    status, body = http(base, 'POST', '/api/boards/%d/cards' % board_id,
                        {'title': '写 README', 'description': '补齐使用说明', 'column_id': first})
    check(status == 201, 'card creation failed: %s %s' % (status, body))
    card = body['card']
    check(card['position'] == 1, 'the first card of a column must have position 1')
    check(card['column_id'] == first, 'the card must be created in the requested column')
    check(card['description'] == '补齐使用说明', 'the description must be stored verbatim')
    check(card['moved_at'] == card['created_at'], 'moved_at must equal created_at on creation')
    check(card['updated_at'] == card['created_at'], 'updated_at must equal created_at on creation')
    check(card['board_id'] == board_id, 'the card must carry the board id')
    first_card = card['id']

    status, body = http(base, 'POST', '/api/boards/%d/cards' % board_id,
                        {'title': '第二张卡', 'column_id': first})
    check(status == 201, 'second card creation failed: %s %s' % (status, body))
    second_card = body['card']['id']
    check(body['card']['position'] == 2, 'the second card must be appended at position 2')

    snap = snapshot(base, board_id)
    check(cards_in(snap, first) == [first_card, second_card], 'the card order inside the column is wrong')
    check(card_positions(snap, first) == [1, 2], 'the card positions must be contiguous')
    check(snap['board']['card_count'] == 2, 'the board card_count must be 2')
    check([c['card_count'] for c in snap['columns']] == [2, 0], 'the column card counts are wrong')

    before = board_state(snapshot(base, board_id))
    rejections = (
        ({'title': '', 'column_id': first}, 422, 'TITLE_REQUIRED'),
        ({'title': 'x' * 201, 'column_id': first}, 422, 'TITLE_TOO_LONG'),
        ({'title': 'ok', 'description': 'y' * 501, 'column_id': first}, 422, 'DESCRIPTION_TOO_LONG'),
        ({'title': 'ok'}, 422, 'COLUMN_REQUIRED'),
        ({'title': 'ok', 'column_id': 999999999}, 404, 'COLUMN_NOT_FOUND'),
        ({'title': 'ok', 'column_id': first, 'status': 'doing'}, 422, 'FORBIDDEN_FIELD'),
        ({'title': 'ok', 'column_id': first, 'due_date': '2026-12-31'}, 422, 'FORBIDDEN_FIELD'),
        ({'title': 'ok', 'column_id': first, 'recurrence_trigger': 'daily'}, 422, 'FORBIDDEN_FIELD'),
        ({'title': 'ok', 'column_id': first, 'assignee': 'me'}, 422, 'FORBIDDEN_FIELD'),
        ({'title': 'ok', 'column_id': first, 'priority': 3}, 422, 'FORBIDDEN_FIELD'),
        ({'title': 'ok', 'column_id': first, 'swimlane_id': 2}, 422, 'FORBIDDEN_FIELD'),
        ({'title': 'ok', 'column_id': first, 'colour': 'red'}, 422, 'UNKNOWN_FIELD'),
    )
    for payload, want_status, want_code in rejections:
        status, body = http(base, 'POST', '/api/boards/%d/cards' % board_id, payload)
        expect_error(status, body, want_status, want_code)
    after = board_state(snapshot(base, board_id))
    check(after == before, 'a rejected card creation changed the board state')

    status, body = http(base, 'PATCH', '/api/cards/%d' % first_card, {'title': '写 README（修订）'})
    check(status == 200, 'card edit failed: %s %s' % (status, body))
    edited = body['card']
    check(edited['title'] == '写 README（修订）', 'the edited title was not stored')
    check(edited['description'] == '补齐使用说明', 'an edit must not drop the description')
    check(edited['position'] == 1, 'an edit must not change the position')
    check(edited['column_id'] == first, 'an edit must not change the column')
    check(edited['moved_at'] == edited['created_at'], 'an edit must not change moved_at')
    check(edited['updated_at'] >= edited['created_at'], 'updated_at went backwards')

    status, body = http(base, 'PATCH', '/api/cards/%d' % first_card, {'column_id': second})
    expect_error(status, body, 422, 'COLUMN_CHANGE_REQUIRES_MOVE')
    status, body = http(base, 'PATCH', '/api/cards/%d' % first_card, {'position': 2})
    expect_error(status, body, 422, 'POSITION_CHANGE_REQUIRES_MOVE')
    snap = snapshot(base, board_id)
    check(cards_in(snap, first) == [first_card, second_card], 'a rejected patch moved the card')

    status, body = http(base, 'GET', '/api/cards/%d' % first_card)
    check(status == 200, 'GET card failed: %s %s' % (status, body))
    check(body['card']['id'] == first_card, 'GET card returned another card')
    status, body = http(base, 'GET', '/api/cards/999999999')
    expect_error(status, body, 404, 'CARD_NOT_FOUND')

    drop_board(base, board_id)
    return 'cards: create/read/edit plus 12 rejected writes, board state byte-identical before and after'


def case_a04(base):
    board, columns = make_board(base, columns=['待办', '进行中', '完成'])
    board_id = board['id']
    first, second, third = [c['id'] for c in columns]
    card_a = make_card(base, board_id, 'A', first)['id']
    card_b = make_card(base, board_id, 'B', first)['id']
    card_c = make_card(base, board_id, 'C', first)['id']
    card_d = make_card(base, board_id, 'D', second)['id']

    snap = snapshot(base, board_id)
    check(cards_in(snap, first) == [card_a, card_b, card_c], 'the setup order in the first column is wrong')
    check(cards_in(snap, second) == [card_d], 'the setup order in the second column is wrong')
    check(card_positions(snap, first) == [1, 2, 3], 'the setup positions are wrong')

    status, body = http(base, 'POST', '/api/cards/%d/move' % card_a,
                        {'column_id': second, 'position': 1})
    check(status == 200, 'cross column move failed: %s %s' % (status, body))
    moved = body['card']
    check(moved['column_id'] == second, 'the moved card is not in the target column')
    check(moved['position'] == 1, 'the moved card is not at the requested slot')
    check(moved['moved_at'] >= moved['created_at'], 'moved_at is before created_at')
    check([c['card_ids'] for c in body['columns']] == [[card_b, card_c], [card_a, card_d], []],
          'the move response does not show the renumbered columns')

    snap = snapshot(base, board_id)
    check(cards_in(snap, first) == [card_b, card_c], 'the source column order is wrong after the move')
    check(card_positions(snap, first) == [1, 2], 'the source column was not renumbered to 1..M-1')
    check(cards_in(snap, second) == [card_a, card_d], 'the target column order is wrong after the move')
    check(card_positions(snap, second) == [1, 2], 'the target column positions are not contiguous')
    check(snap['board']['card_count'] == 4, 'a move must not change the board card count')

    status, body = http(base, 'POST', '/api/cards/%d/move' % card_c,
                        {'column_id': first, 'position': 1})
    check(status == 200, 'in column reorder failed: %s %s' % (status, body))
    snap = snapshot(base, board_id)
    check(cards_in(snap, first) == [card_c, card_b], 'the in column reorder is wrong')
    check(card_positions(snap, first) == [1, 2], 'the in column reorder positions are wrong')

    status, body = http(base, 'POST', '/api/cards/%d/move' % card_b,
                        {'column_id': third, 'position': 1})
    check(status == 200, 'move to the third column failed: %s %s' % (status, body))
    snap = snapshot(base, board_id)
    check(cards_in(snap, third) == [card_b], 'the card did not land in the third column')
    check(cards_in(snap, first) == [card_c], 'the source column was not emptied')
    check(card_positions(snap, first) == [1], 'the emptied column must be renumbered to 1')

    before = board_state(snapshot(base, board_id))
    for payload, want_status, want_code in (
        ({'column_id': second, 'position': 99}, 422, 'POSITION_OUT_OF_RANGE'),
        ({'column_id': second, 'position': 0}, 422, 'POSITION_OUT_OF_RANGE'),
        ({'column_id': 999999999, 'position': 1}, 404, 'COLUMN_NOT_FOUND'),
    ):
        status, body = http(base, 'POST', '/api/cards/%d/move' % card_a, payload)
        expect_error(status, body, want_status, want_code)
        check(board_state(snapshot(base, board_id)) == before, 'a rejected move changed the board')

    other_board, other_columns = make_board(base, columns=['别的看板'])
    status, body = http(base, 'POST', '/api/cards/%d/move' % card_a,
                        {'column_id': other_columns[0]['id'], 'position': 1})
    expect_error(status, body, 422, 'COLUMN_BOARD_MISMATCH')
    check(board_state(snapshot(base, board_id)) == before, 'a rejected cross board move changed the board')
    drop_board(base, other_board['id'])

    status, body = http(base, 'POST', '/api/cards/999999999/move',
                        {'column_id': first, 'position': 1})
    expect_error(status, body, 404, 'CARD_NOT_FOUND')

    status, body = http(base, 'POST', '/api/cards/%d/move' % card_a,
                        {'column_id': second, 'position': 1})
    check(status == 200, 'the idempotent move failed: %s %s' % (status, body))
    snap = snapshot(base, board_id)
    check(cards_in(snap, second) == [card_a, card_d], 'a no-op move changed the column order')

    drop_board(base, board_id)
    return 'movement: cross column move, in column reorder, renumbering, 4 rejected moves with zero-write re-reads'


def case_a05(base):
    board, columns = make_board(base, columns=['待办', '进行中', '完成'])
    board_id = board['id']
    first, second, third = [c['id'] for c in columns]
    make_card(base, board_id, '写文档', first, '整理需求')
    make_card(base, board_id, '复习', first)
    make_card(base, board_id, '备课', second)
    make_card(base, board_id, '收尾', third)

    expected = {'待办': ['写文档', '复习'], '进行中': ['备课'], '完成': ['收尾']}
    snap = snapshot(base, board_id)
    check(column_names(snap) == ['待办', '进行中', '完成'], 'the column order is wrong')
    check(column_positions(snap) == [1, 2, 3], 'the column positions must be 1..3')
    check(snap['board']['column_count'] == 3, 'the board column_count must be 3')
    check(snap['board']['card_count'] == 4, 'the board card_count must be 4')
    titles = {}
    for column in snap['columns']:
        check(column['card_count'] == len(column['cards']),
              'card_count must equal the card list length in column %d' % column['id'])
        check([card['position'] for card in column['cards']] == list(range(1, len(column['cards']) + 1)),
              'the card positions of column %d are not contiguous' % column['id'])
        titles[column['name']] = [card['title'] for card in column['cards']]
    check(titles == expected, 'the card distribution differs: %s' % titles)
    check(sum(column['card_count'] for column in snap['columns']) == 4, 'the column counts must sum to 4')

    snap2 = snapshot(base, board_id)
    check(snap2 == snap, 'two consecutive board reads are not identical')

    status, body = http(base, 'GET', '/api/boards')
    check(status == 200, 'GET /api/boards failed: %s %s' % (status, body))
    entry = [item for item in body['boards'] if item['id'] == board_id]
    check(len(entry) == 1, 'the board must appear exactly once in the list')
    check(entry[0]['card_count'] == 4 and entry[0]['column_count'] == 3, 'the list counts are wrong')

    now = int(time.time())
    for column in snap['columns']:
        for card in column['cards']:
            check(isinstance(card['created_at'], int), 'created_at must be an integer')
            check(isinstance(card['updated_at'], int), 'updated_at must be an integer')
            check(isinstance(card['moved_at'], int), 'moved_at must be an integer')
            check(card['created_at'] <= card['updated_at'], 'updated_at is before created_at')
            check(card['created_at'] <= card['moved_at'], 'moved_at is before created_at')
            check(PROBE_START - 10 <= card['created_at'] <= now + 2, 'created_at is outside the probe window')

    drop_board(base, board_id)
    return 'read model: 3 columns, 4 cards, exact counts and sets, contiguous positions, stable second read'


def main(argv=None):
    parser = argparse.ArgumentParser(description='Acceptance probe for the Personal Project Board')
    parser.add_argument('--base-url', default='http://127.0.0.1:8765',
                        help='base URL of the running target')
    parser.add_argument('--case', action='append', choices=['all'] + list(CASE_IDS),
                        help='case id A01..A05 or all; repeatable')
    args = parser.parse_args(argv)
    check(len(CASE_IDS) == FEATURE_COUNT, 'the number of cases must match the number of features')

    selected = args.case if args.case else ['all']
    case_ids = []
    for item in selected:
        if item == 'all':
            case_ids = list(CASE_IDS)
            break
        case_ids.append(item)

    base = args.base_url.rstrip('/')
    runners = {'A01': case_a01, 'A02': case_a02, 'A03': case_a03, 'A04': case_a04, 'A05': case_a05}
    failures = []
    for case_id in case_ids:
        started = time.time()
        try:
            summary = runners[case_id](base)
        except urllib.error.URLError as error:
            failures.append(case_id)
            print('ERROR %s: cannot reach the target at %s (%s)' % (case_id, base, error))
        except ProbeFailure as error:
            failures.append(case_id)
            print('FAIL %s: %s' % (case_id, error))
        except Exception as error:
            failures.append(case_id)
            print('ERROR %s: %s: %s' % (case_id, type(error).__name__, error))
        else:
            print('PASS %s (%.2fs) %s' % (case_id, time.time() - started, summary))
            if case_id == 'A05':
                print('     note: cross process restart durability is an operator step documented in')
                print('           README.md; the probe does not stop or start the server and does')
                print('           not report on it.')
    print('cases run: %d, failures: %d' % (len(case_ids), len(failures)))
    if failures:
        print('failed cases: %s' % ', '.join(failures))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
