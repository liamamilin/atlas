#!/usr/bin/env python3
'''acceptance/run.py —— P0 回环本地目标的真实验收检查器（纯标准库，非下游应用）。

本程序独立运行，通过真实 HTTP 请求驱动显式提供的回环目标；绝不模拟目标
响应、绝不写夹具、绝不安装依赖，也不在生成期运行。所有断言针对真实目标，
失败即以非零退出码结束并打印最小 JSON 摘要。

运行契约：
  python3 acceptance/run.py --base-url http://127.0.0.1:PORT
      [--app app.py --data-dir DIR --port PORT]
      [--admin-user U --admin-pass P --resident-user U2 --resident-pass P2
       --resident2-user U3 --resident2-pass P3] [--timeout SEC]

两种模式：
  A) web 目标模式：只使用显式提供的回环 origin/port，拒绝跨源跳转。
  B) 生命周期模式：额外提供 --app/--data-dir/--port 时，以 shell=False
     启动/重启目标，覆盖 A14 真实重启用例。

安全约束：
  - 只接受 http 回环 origin，且只信任该精确 host:port；不豁免所有回环。
  - base-url 不得内嵌凭据；除服务端 Cookie 会话外不支持其他认证模式，
    并在发起任何请求前显式失败。
  - 重定向在传输层按 origin 校验，跨源跳转被阻断；Cookie 不跨源发送。
  - 口令仅用于登录配置，绝不写入日志或 URL；失败摘要会脱敏。

用例：A01..A16（见 CASES）。退出码：0 全通过；1 存在失败；2 配置/用法错误。
'''

import argparse
import http.cookiejar
import json
import os
import re
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

DEFAULT_TIMEOUT = 15.0
ANCHOR = 2051222400  # 2035-01-01T00:00:00Z，固定未来锚点，不依赖当前日期
LOOPBACK_HOSTS = ('127.0.0.1', 'localhost', '::1')
DEFAULT_ACCOUNTS = {
    'admin': ('admin', 'AtlasDemo-Admin-9!'),
    'resident': ('alice', 'AtlasDemo-Alice-9!'),
    'resident2': ('bob', 'AtlasDemo-Bob-9!'),
}


class ConfigError(Exception):
    '''配置或用法错误（退出码 2）。'''


class OriginViolation(Exception):
    '''检测到跨源跳转或跨源请求，已在传输层阻断。'''


# ---------------------------------------------------------------------------
# origin 与传输层安全工具
# ---------------------------------------------------------------------------

def _hostport(host, port):
    if ':' in host:
        return '[%s]:%s' % (host, port)
    return '%s:%s' % (host, port)


def _origin_key(url):
    parts = urllib.parse.urlsplit(url)
    scheme = (parts.scheme or '').lower()
    host = (parts.hostname or '').lower()
    if parts.port is not None:
        port = parts.port
    elif scheme == 'http':
        port = 80
    elif scheme == 'https':
        port = 443
    else:
        port = None
    return (scheme, host, port)


def same_origin(a, b):
    ka = _origin_key(a)
    kb = _origin_key(b)
    return ka == kb and ka[1] != ''


def parse_base_url(base_url):
    try:
        parts = urllib.parse.urlsplit(base_url)
        port = parts.port
    except ValueError:
        raise ConfigError('base-url 端口非法') from None
    if parts.scheme not in ('http',):
        raise ConfigError('base-url 必须为 http 回环目标')
    if parts.username or parts.password:
        raise ConfigError('base-url 不得内嵌凭据')
    if parts.query or parts.fragment:
        raise ConfigError('base-url 不得包含查询或片段')
    if parts.path not in ('', '/'):
        raise ConfigError('base-url 不得包含路径')
    host = (parts.hostname or '').lower()
    if host not in LOOPBACK_HOSTS:
        raise ConfigError('base-url 必须为回环主机（127.0.0.1、localhost 或 ::1）')
    if port is None:
        raise ConfigError('base-url 必须显式包含端口')
    return 'http://%s' % _hostport(host, port)


class LoopbackRedirectHandler(urllib.request.HTTPRedirectHandler):
    '''只允许跳转到显式提供的回环 origin，其余一律阻断。'''

    def __init__(self, allowed_origin):
        super().__init__()
        self.allowed_origin = allowed_origin

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not same_origin(newurl, self.allowed_origin):
            raise OriginViolation('拒绝跨源跳转')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _redact(text, secrets):
    out = text or ''
    for secret in secrets:
        if secret:
            out = out.replace(secret, '[redacted]')
    out = ' '.join(out.split())
    return out[:400]


def _self_check_origin_guard():
    allowed = 'http://127.0.0.1:1'
    other_port = 'http://127.0.0.1:2'
    other_host = 'http://localhost:1'
    if same_origin(allowed, other_port):
        raise ConfigError('origin 守卫错误地豁免了全部回环端口')
    if same_origin(allowed, other_host):
        raise ConfigError('origin 守卫错误地豁免了全部回环主机')
    if not same_origin(allowed, allowed):
        raise ConfigError('origin 守卫自检失败')
    handler = LoopbackRedirectHandler(allowed)
    try:
        handler.redirect_request(None, None, 302, 'Found', {}, other_port + '/x')
    except OriginViolation:
        return
    raise ConfigError('origin 守卫未能阻断跨源跳转')


# ---------------------------------------------------------------------------
# HTTP 会话与断言辅助
# ---------------------------------------------------------------------------

class Response:
    def __init__(self, status, headers, body, path):
        self.status = status
        self.headers = headers
        self.body = body
        self.path = path
        self._json = None
        self._parsed = False

    @property
    def json(self):
        if not self._parsed:
            self._parsed = True
            try:
                self._json = json.loads(self.body.decode('utf-8'))
            except Exception:
                self._json = None
        return self._json

    def text(self):
        return self.body.decode('utf-8', 'replace')

    def content_type(self):
        return (self.headers.get('Content-Type') or '').lower()


class Session:
    def __init__(self, base_url, origin, timeout=DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip('/')
        self.origin = origin
        self.timeout = timeout
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            LoopbackRedirectHandler(origin),
            urllib.request.HTTPCookieProcessor(self.jar),
            urllib.request.ProxyHandler({}),
        )

    def request(self, method, path, payload=None, headers=None, timeout=None):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', path):
            url = path
        else:
            url = self.base_url + '/' + path.lstrip('/')
        if not same_origin(url, self.origin):
            raise OriginViolation('拒绝跨源请求')
        data = None
        request_headers = {'Accept': '*/*'}
        if headers:
            request_headers.update(headers)
        if payload is not None:
            data = json.dumps(payload).encode('utf-8')
            request_headers['Content-Type'] = 'application/json'
        elif method in ('POST', 'PUT', 'PATCH'):
            data = b''
        req = urllib.request.Request(url, data=data, headers=request_headers, method=method)
        try:
            with self.opener.open(req, timeout=timeout or self.timeout) as fp:
                return Response(fp.status, fp.headers, fp.read(), path)
        except urllib.error.HTTPError as exc:
            return Response(exc.code, exc.headers, exc.read(), path)
        except OriginViolation:
            raise AssertionError('跨源跳转被传输层阻断') from None
        except urllib.error.URLError as exc:
            raise AssertionError('请求失败 %s：%s' % (path, type(exc.reason).__name__)) from None


def new_session(base_url, allowed_origin=None, timeout=DEFAULT_TIMEOUT):
    origin = allowed_origin or base_url
    return Session(base_url, origin, timeout)


def login(session, username, password):
    return session.request('POST', '/api/login', {'username': username, 'password': password})


def assert_status_json(resp, code):
    codes = code if isinstance(code, (tuple, list, set)) else (code,)
    if resp.status not in codes:
        raise AssertionError('期望状态 %s，实际 %s（%s）' % (sorted(codes), resp.status, resp.path))
    if resp.json is None:
        raise AssertionError('状态 %s 的响应体不是 JSON（%s）' % (resp.status, resp.path))
    return resp.json


def concurrency_probe(n, task):
    '''并发启动 n 个真实线程，尽量同时调用 task(i)。
    返回 [(i, kind, value)]，kind 为 value 或 error。'''
    barrier = threading.Barrier(n)
    results = [None] * n

    def worker(i):
        try:
            barrier.wait()
        except threading.BrokenBarrierError:
            pass
        try:
            results[i] = (i, 'value', task(i))
        except BaseException as exc:  # noqa: BLE001
            results[i] = (i, 'error', exc)

    threads = [threading.Thread(target=worker, args=(i,), daemon=True) for i in range(n)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=120)
    if any(item is None for item in results):
        raise AssertionError('并发探测超时：部分线程未完成')
    return results


# ---------------------------------------------------------------------------
# 断言与数据提取工具
# ---------------------------------------------------------------------------

def _error_text(data):
    if not isinstance(data, dict):
        return None
    for key in ('error', 'reason', 'message', 'detail'):
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _expect_error(resp, code):
    codes = code if isinstance(code, (tuple, list, set)) else (code,)
    if resp.status not in codes:
        raise AssertionError('期望错误状态 %s，实际 %s（%s）'
                            % (sorted(codes), resp.status, resp.path))
    data = resp.json
    if data is None:
        raise AssertionError('错误响应体不是 JSON（%s，状态 %s）' % (resp.path, resp.status))
    text = _error_text(data)
    if not text:
        raise AssertionError('错误响应缺少可读原因（%s）' % resp.path)
    return data


def _user_obj(data):
    if isinstance(data, dict):
        user = data.get('user')
        if isinstance(user, dict):
            return user
        return data
    return {}


def _booking_obj(data):
    if isinstance(data, dict):
        booking = data.get('booking')
        if isinstance(booking, dict):
            return booking
        return data
    return {}


def _role_of(data):
    return _user_obj(data).get('role')


def _name(prefix):
    return '%s-%s' % (prefix, uuid.uuid4().hex[:8])


def _iso(epoch, offset_hours=0):
    tz = timezone(timedelta(hours=offset_hours))
    return datetime.fromtimestamp(epoch, tz).replace(microsecond=0).isoformat()


def _parse_instant(value):
    if not isinstance(value, str):
        return None
    text = value.strip()
    if text.endswith('Z') or text.endswith('z'):
        text = text[:-1] + '+00:00'
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return int(parsed.timestamp())


def _slot_matches(slot, start_epoch, end_epoch):
    if not isinstance(slot, dict):
        return False
    return (_parse_instant(slot.get('start')) == int(start_epoch)
            and _parse_instant(slot.get('end')) == int(end_epoch))


def _session(ctx):
    return new_session(ctx.base_url, ctx.origin, ctx.timeout)


def _login(ctx, role):
    session = _session(ctx)
    cred = ctx.creds[role]
    assert_status_json(login(session, cred['username'], cred['password']), 200)
    return session


def _whoami(session):
    return _user_obj(assert_status_json(session.request('GET', '/api/me'), 200))


def _create_resource(session, name):
    data = assert_status_json(session.request('POST', '/api/resources', {'name': name}), (200, 201))
    rid = data.get('id')
    if rid is None:
        raise AssertionError('创建资源响应缺少 id')
    return rid


def _book(session, resource_id, start_epoch, end_epoch, note='', offset_hours=0):
    data = assert_status_json(session.request('POST', '/api/bookings', {
        'resource_id': resource_id,
        'start': _iso(start_epoch, offset_hours),
        'end': _iso(end_epoch, offset_hours),
        'note': note}), (200, 201))
    bid = data.get('id')
    if bid is None:
        raise AssertionError('创建预约响应缺少 id')
    return bid


def _cancel(session, booking_id):
    return assert_status_json(session.request('POST', '/api/bookings/%s/cancel' % booking_id), 200)


def _availability(session, resource_id):
    query = urllib.parse.urlencode({'resource_id': resource_id})
    return session.request('GET', '/api/availability?' + query)


def _has_testid(html, name):
    dq = chr(34)
    sq = chr(39)
    return ('data-testid=' + dq + name + dq in html) or ('data-testid=' + sq + name + sq in html)


def _contains_chinese(text):
    for ch in text:
        if 0x4e00 <= ord(ch) <= 0x9fff:
            return True
    return False


# ---------------------------------------------------------------------------
# 用例 A01..A16
# ---------------------------------------------------------------------------

def A01(ctx):
    '''A01：登录/登出/me。'''
    anon = _session(ctx)
    assert_status_json(anon.request('GET', '/api/me'), 401)
    for role, expected in (('admin', 'admin'), ('resident', 'resident')):
        session = _session(ctx)
        cred = ctx.creds[role]
        assert_status_json(login(session, cred['username'], cred['password']), 200)
        me = assert_status_json(session.request('GET', '/api/me'), 200)
        if _role_of(me) != expected:
            raise AssertionError('%s 登录后 /api/me 角色应为 %s' % (role, expected))
        out = session.request('POST', '/api/logout')
        if out.status not in (200, 204):
            raise AssertionError('登出应返回 200/204，实际 %s' % out.status)
        assert_status_json(session.request('GET', '/api/me'), 401)


def A02(ctx):
    '''A02：未登录访问受保护资源返回 401。'''
    anon = _session(ctx)
    assert_status_json(anon.request('GET', '/api/bookings'), 401)
    assert_status_json(anon.request('GET', '/api/me'), 401)
    assert_status_json(anon.request('POST', '/api/bookings', {
        'resource_id': 1, 'start': _iso(ANCHOR), 'end': _iso(ANCHOR + 3600)}), 401)


def A03(ctx):
    '''A03：角色伪造 403；owner 取自会话。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    admin_id = _whoami(admin).get('id')
    resident_id = _whoami(resident).get('id')
    name = _name('a03')
    _expect_error(resident.request('POST', '/api/resources', {'name': name}), 403)
    listing = assert_status_json(admin.request('GET', '/api/resources'), 200)
    if any(item.get('name') == name for item in listing['resources']):
        raise AssertionError('居民越权创建的设施被写入')
    rid = _create_resource(admin, _name('a03r'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    resp = resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': _iso(t0), 'end': _iso(t1), 'note': '伪造',
        'user_id': admin_id, 'owner_id': admin_id, 'role': 'admin'})
    bid = assert_status_json(resp, (200, 201)).get('id')
    if bid is None:
        raise AssertionError('预约响应缺少 id')
    detail = _booking_obj(assert_status_json(resident.request('GET', '/api/bookings/%s' % bid), 200))
    if detail.get('owner_id') != resident_id:
        raise AssertionError('owner 未取自会话，而是信任了请求参数')


def A04(ctx):
    '''A04：管理员创建资源后出现在列表。'''
    admin = _login(ctx, 'admin')
    name = _name('a04')
    rid = _create_resource(admin, name)
    listing = assert_status_json(admin.request('GET', '/api/resources'), 200)
    found = [item for item in listing['resources'] if item.get('id') == rid]
    if not found or found[0].get('name') != name:
        raise AssertionError('管理员创建的设施未出现在列表中')


def A05(ctx):
    '''A05：可用性只含 active 且不含他人隐私。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    resident2 = _login(ctx, 'resident2')
    rid = _create_resource(admin, _name('a05'))
    s1, e1 = ANCHOR, ANCHOR + 3600
    s2, e2 = ANCHOR + 7200, ANCHOR + 10800
    s3, e3 = ANCHOR + 14400, ANCHOR + 18000
    _book(resident, rid, s1, e1)
    _book(resident2, rid, s2, e2)
    cancelled = _book(resident, rid, s3, e3)
    _cancel(resident, cancelled)
    data = assert_status_json(_availability(resident, rid), 200)
    slots = data['slots']
    if not any(_slot_matches(slot, s1, e1) for slot in slots):
        raise AssertionError('可用性缺少 active 时段')
    if not any(_slot_matches(slot, s2, e2) for slot in slots):
        raise AssertionError('可用性缺少他人 active 时段')
    if any(_slot_matches(slot, s3, e3) for slot in slots):
        raise AssertionError('可用性包含已取消时段')
    for slot in slots:
        if set(slot.keys()) - {'start', 'end'}:
            raise AssertionError('可用性泄露了非时段字段：%s' % sorted(slot.keys()))


def A06(ctx):
    '''A06：带显式偏移的 ISO8601 预约，含半开相邻区间。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    rid = _create_resource(admin, _name('a06'))
    t0, t1, t2 = ANCHOR, ANCHOR + 3600, ANCHOR + 7200
    b1 = _book(resident, rid, t0, t1, offset_hours=8)
    b2 = _book(resident, rid, t1, t2, offset_hours=8)
    listing = assert_status_json(resident.request('GET', '/api/bookings'), 200)
    ids = [item.get('id') for item in listing['bookings']]
    if b1 not in ids or b2 not in ids:
        raise AssertionError('相邻半开区间预约未同时出现在本人列表中')
    detail = _booking_obj(assert_status_json(resident.request('GET', '/api/bookings/%s' % b1), 200))
    if _parse_instant(detail.get('start')) != t0 or _parse_instant(detail.get('end')) != t1:
        raise AssertionError('带偏移的 ISO8601 未按真实时刻存储与比较')


def A07(ctx):
    '''A07：end<=start 或非法/缺时区 ISO8601 返回 400。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    rid = _create_resource(admin, _name('a07'))
    t = ANCHOR
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': _iso(t), 'end': _iso(t)}), 400)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': _iso(t + 3600), 'end': _iso(t)}), 400)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': 'not-a-date', 'end': _iso(t + 3600)}), 400)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid,
        'start': '2035-01-01T00:00:00',
        'end': '2035-01-01T01:00:00'}), 400)


def A08(ctx):
    '''A08：同设施重叠返回 409 且未写入新记录。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    rid = _create_resource(admin, _name('a08'))
    t0, t2 = ANCHOR, ANCHOR + 7200
    _book(resident, rid, t0, t2)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': _iso(t0 + 1800), 'end': _iso(t2 + 1800)}), 409)
    listing = assert_status_json(resident.request('GET', '/api/bookings'), 200)
    active = [b for b in listing['bookings']
              if b.get('resource_id') == rid and b.get('status') == 'active']
    if len(active) != 1:
        raise AssertionError('重叠被拒后写入异常：active=%d' % len(active))


def A09(ctx):
    '''A09：不同设施同一时刻互不阻塞。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    r1 = _create_resource(admin, _name('a09a'))
    r2 = _create_resource(admin, _name('a09b'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    _book(resident, r1, t0, t1)
    _book(resident, r2, t0, t1)


def A10(ctx):
    '''A10：居民不能查看/取消他人预约。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    resident2 = _login(ctx, 'resident2')
    resident_id = _whoami(resident).get('id')
    rid = _create_resource(admin, _name('a10'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    bid = _book(resident2, rid, t0, t1)
    _expect_error(resident.request('GET', '/api/bookings/%s' % bid), 403)
    listing = assert_status_json(resident.request('GET', '/api/bookings'), 200)
    for booking in listing['bookings']:
        if booking.get('id') == bid:
            raise AssertionError('居民列表泄露了他人预约')
        if booking.get('owner_id') not in (None, resident_id):
            raise AssertionError('居民列表包含非本人 owner 的预约')
    _expect_error(resident.request('POST', '/api/bookings/%s/cancel' % bid), 403)
    detail = _booking_obj(assert_status_json(resident2.request('GET', '/api/bookings/%s' % bid), 200))
    if detail.get('status') != 'active':
        raise AssertionError('越权取消后他人预约状态被破坏')


def A11(ctx):
    '''A11：取消幂等、保留状态并释放时段。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    rid = _create_resource(admin, _name('a11'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    bid = _book(resident, rid, t0, t1)
    first = _booking_obj(_cancel(resident, bid))
    if first.get('status') != 'cancelled':
        raise AssertionError('取消失败：status 未变为 cancelled')
    data = assert_status_json(_availability(resident, rid), 200)
    if any(_slot_matches(slot, t0, t1) for slot in data['slots']):
        raise AssertionError('取消后原时段未从可用性中释放')
    second = _booking_obj(_cancel(resident, bid))
    if second.get('status') != 'cancelled' or second.get('id') != bid:
        raise AssertionError('重复取消未幂等返回同一记录')
    listing = assert_status_json(resident.request('GET', '/api/bookings'), 200)
    same = [b for b in listing['bookings'] if b.get('id') == bid]
    if len(same) != 1:
        raise AssertionError('取消产生了重复记录')


def A12(ctx):
    '''A12：管理员可查看全部并取消任意预约。'''
    admin = _login(ctx, 'admin')
    resident2 = _login(ctx, 'resident2')
    rid = _create_resource(admin, _name('a12'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    bid = _book(resident2, rid, t0, t1)
    listing = assert_status_json(admin.request('GET', '/api/bookings'), 200)
    if not any(b.get('id') == bid for b in listing['bookings']):
        raise AssertionError('管理员列表未包含全部预约')
    cancelled = _booking_obj(_cancel(admin, bid))
    if cancelled.get('status') != 'cancelled':
        raise AssertionError('管理员取消他人预约失败')


def A13(ctx):
    '''A13：并发重叠最多一笔成功。'''
    admin = _login(ctx, 'admin')
    rid = _create_resource(admin, _name('a13'))
    n = 6
    t0, t1 = ANCHOR, ANCHOR + 3600
    sessions = [_login(ctx, 'resident') for _ in range(n)]

    def task(i):
        resp = sessions[i].request('POST', '/api/bookings', {
            'resource_id': rid, 'start': _iso(t0), 'end': _iso(t1), 'note': ''})
        return resp.status

    outcomes = concurrency_probe(n, task)
    errors = [value for _, kind, value in outcomes if kind == 'error']
    if errors:
        raise AssertionError('并发请求异常：%s' % type(errors[0]).__name__)
    statuses = [value for _, kind, value in outcomes if kind == 'value']
    ok = [status for status in statuses if 200 <= status < 300]
    conflicts = [status for status in statuses if status == 409]
    if len(ok) != 1 or len(conflicts) != n - 1:
        raise AssertionError('并发重叠应恰好 1 笔成功、%d 笔 409，实际 成功=%d 冲突=%d'
                            % (n - 1, len(ok), len(conflicts)))
    listing = assert_status_json(admin.request('GET', '/api/bookings'), 200)
    active = [b for b in listing['bookings']
              if b.get('resource_id') == rid and b.get('status') == 'active']
    if len(active) != 1:
        raise AssertionError('并发后 active 记录数应为 1，实际 %d' % len(active))


def A14(ctx):
    '''A14：刷新与（生命周期模式下的）真实重启一致。'''
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    rid = _create_resource(admin, _name('a14'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    bid = _book(resident, rid, t0, t1)
    refreshed = _login(ctx, 'resident')
    detail = _booking_obj(assert_status_json(refreshed.request('GET', '/api/bookings/%s' % bid), 200))
    if detail.get('id') != bid:
        raise AssertionError('刷新后预约 id 不一致')
    if ctx.lifecycle is None:
        return
    ctx.lifecycle.restart()
    after = _login(ctx, 'resident')
    detail2 = _booking_obj(assert_status_json(after.request('GET', '/api/bookings/%s' % bid), 200))
    if detail2.get('id') != bid or detail2.get('status') != 'active':
        raise AssertionError('真实重启后预约状态不一致')
    admin2 = _login(ctx, 'admin')
    listing = assert_status_json(admin2.request('GET', '/api/bookings'), 200)
    if not any(b.get('id') == bid for b in listing['bookings']):
        raise AssertionError('真实重启后管理员列表缺少该预约')
    resources = assert_status_json(admin2.request('GET', '/api/resources'), 200)
    if not any(item.get('id') == rid for item in resources['resources']):
        raise AssertionError('真实重启后资源丢失')


def A15(ctx):
    '''A15：GET / 提供中文 UI 与必需 data-testid，并据此完成真实登录与预约。'''
    session = _session(ctx)
    resp = session.request('GET', '/')
    if resp.status != 200:
        raise AssertionError('GET / 应返回 200，实际 %s' % resp.status)
    if 'html' not in resp.content_type():
        raise AssertionError('GET / 未返回 HTML')
    html = resp.text()
    required = ['login-username', 'login-password', 'login-submit', 'resource-name',
                'resource-save', 'booking-resource', 'booking-start', 'booking-end',
                'booking-note', 'booking-save', 'logout']
    missing = [name for name in required if not _has_testid(html, name)]
    if missing:
        raise AssertionError('缺少必需 data-testid：%s' % ','.join(missing))
    if not _contains_chinese(html):
        raise AssertionError('UI 缺少中文内容')
    for token in ('/api/login', '/api/bookings'):
        if token not in html:
            raise AssertionError('UI 未引用真实接口 %s' % token)
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    rid = _create_resource(admin, _name('a15'))
    bid = _book(resident, rid, ANCHOR, ANCHOR + 3600)
    listing = assert_status_json(resident.request('GET', '/api/bookings'), 200)
    if not any(b.get('id') == bid for b in listing['bookings']):
        raise AssertionError('通过真实接口创建的预约未出现在本人列表')


def A16(ctx):
    '''A16：各类失败均为非 2xx JSON 且含原因。'''
    anon = _session(ctx)
    _expect_error(anon.request('GET', '/api/bookings'), 401)
    admin = _login(ctx, 'admin')
    resident = _login(ctx, 'resident')
    resident2 = _login(ctx, 'resident2')
    _expect_error(resident.request('POST', '/api/resources', {'name': _name('a16x')}), 403)
    rid = _create_resource(admin, _name('a16'))
    t0, t1 = ANCHOR, ANCHOR + 3600
    bid = _book(resident, rid, t0, t1)
    _expect_error(resident2.request('GET', '/api/bookings/%s' % bid), 403)
    _expect_error(resident2.request('POST', '/api/bookings/%s/cancel' % bid), 403)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': _iso(t0 + 1800), 'end': _iso(t1 + 1800)}), 409)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': rid, 'start': 'bogus', 'end': _iso(t1 + 7200)}), 400)
    _expect_error(admin.request('GET', '/api/bookings/999999999'), 404)
    _expect_error(resident.request('POST', '/api/bookings', {
        'resource_id': 999999999, 'start': _iso(t0 + 7200), 'end': _iso(t1 + 7200)}), (400, 404))
    bad = _session(ctx)
    _expect_error(login(bad, ctx.creds['admin']['username'], 'Invalid-' + uuid.uuid4().hex), 401)


# ---------------------------------------------------------------------------
# 目标生命周期（shell=False 启动/重启）与上下文
# ---------------------------------------------------------------------------

class Context:
    def __init__(self, base_url, origin, creds, timeout, lifecycle=None):
        self.base_url = base_url
        self.origin = origin
        self.creds = creds
        self.timeout = timeout
        self.lifecycle = lifecycle


class Lifecycle:
    '''以 shell=False 启动/重启显式提供的目标进程。'''

    def __init__(self, app_path, data_dir, port, base_url, timeout):
        self.app_path = app_path
        self.data_dir = data_dir
        self.port = port
        self.base_url = base_url
        self.timeout = timeout
        self.workdir = os.path.dirname(os.path.abspath(app_path))
        self.proc = None

    def start(self, init_demo=True):
        argv = [sys.executable, self.app_path, '--port', str(self.port),
                '--data-dir', self.data_dir]
        if init_demo:
            argv.append('--init-demo')
        self.proc = subprocess.Popen(
            argv, shell=False, cwd=self.workdir,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self._wait_ready()

    def restart(self):
        self.stop()
        self.start(init_demo=False)

    def stop(self):
        proc = self.proc
        self.proc = None
        if proc is None or proc.poll() is not None:
            return
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass

    def _wait_ready(self):
        host = urllib.parse.urlsplit(self.base_url).hostname
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            if self.proc.poll() is not None:
                raise AssertionError('目标进程在启动阶段退出')
            try:
                with socket.create_connection((host, self.port), timeout=1.0):
                    time.sleep(0.1)
                    return
            except OSError:
                time.sleep(0.2)
        raise AssertionError('目标未在限期内就绪')


# ---------------------------------------------------------------------------
# 参数、配置与运行
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        prog='acceptance/run.py',
        description='P0 回环本地目标真实验收检查器（A01..A16）')
    parser.add_argument('--base-url', required=True,
                        help='目标回环 origin，例如 http://127.0.0.1:8000')
    parser.add_argument('--app', help='生命周期模式：目标 app.py 路径')
    parser.add_argument('--data-dir', help='生命周期模式：一次性数据目录')
    parser.add_argument('--port', type=int, help='生命周期模式：目标监听端口')
    parser.add_argument('--admin-user', help='管理员演示账号用户名')
    parser.add_argument('--admin-pass', help='管理员演示账号口令')
    parser.add_argument('--resident-user', help='居民演示账号用户名')
    parser.add_argument('--resident-pass', help='居民演示账号口令')
    parser.add_argument('--resident2-user', help='第二个居民演示账号用户名')
    parser.add_argument('--resident2-pass', help='第二个居民演示账号口令')
    parser.add_argument('--timeout', type=float, default=DEFAULT_TIMEOUT,
                        help='单次请求超时秒数')
    return parser


def _pair(user, password, default, label):
    default_user, default_pass = default
    if user is None and password is None:
        return {'username': default_user, 'password': default_pass}
    if user is None or password is None:
        raise ConfigError('%s 需同时提供用户名与口令' % label)
    if not user.strip() or not password:
        raise ConfigError('%s 不得为空' % label)
    return {'username': user, 'password': password}


def _build_creds(args):
    return {
        'admin': _pair(args.admin_user, args.admin_pass,
                       DEFAULT_ACCOUNTS['admin'], '管理员账号'),
        'resident': _pair(args.resident_user, args.resident_pass,
                          DEFAULT_ACCOUNTS['resident'], '居民账号'),
        'resident2': _pair(args.resident2_user, args.resident2_pass,
                           DEFAULT_ACCOUNTS['resident2'], '第二居民账号'),
    }


def _build_lifecycle(args, base_url):
    if not args.app or not args.data_dir or args.port is None:
        raise ConfigError('生命周期模式需同时提供 --app、--data-dir 与 --port')
    if not (1 <= args.port <= 65535):
        raise ConfigError('--port 超出范围')
    app_path = os.path.abspath(args.app)
    if not os.path.isfile(app_path):
        raise ConfigError('--app 必须是存在的文件')
    data_dir = os.path.abspath(args.data_dir)
    if not os.path.isdir(data_dir):
        raise ConfigError('--data-dir 必须是存在的目录')
    home = os.path.abspath(os.path.expanduser('~'))
    downloads = os.path.join(home, 'Downloads')
    if data_dir == home or data_dir == downloads or data_dir.startswith(downloads + os.sep):
        raise ConfigError('--data-dir 必须是自有的临时目录，不能是 HOME 或 Downloads')
    if _origin_key(base_url)[2] != args.port:
        raise ConfigError('base-url 端口必须与 --port 一致')
    return Lifecycle(app_path, data_dir, args.port, base_url, args.timeout)


CASES = [
    ('A01', A01), ('A02', A02), ('A03', A03), ('A04', A04),
    ('A05', A05), ('A06', A06), ('A07', A07), ('A08', A08),
    ('A09', A09), ('A10', A10), ('A11', A11), ('A12', A12),
    ('A13', A13), ('A14', A14), ('A15', A15), ('A16', A16),
]


def run_cases(ctx):
    secrets = [c['password'] for c in ctx.creds.values() if c.get('password')]
    results = {}
    failures = []
    for case_id, func in CASES:
        try:
            func(ctx)
            results[case_id] = 'pass'
        except AssertionError as exc:
            results[case_id] = 'fail'
            failures.append({'case': case_id, 'reason': _redact(str(exc), secrets)})
        except Exception as exc:  # noqa: BLE001
            results[case_id] = 'error'
            failures.append({'case': case_id,
                             'reason': _redact(type(exc).__name__ + ': ' + str(exc), secrets)})
    return results, failures


def main(argv=None):
    args = _build_parser().parse_args(argv)
    secrets = []
    lifecycle = None
    try:
        base_url = parse_base_url(args.base_url)
        creds = _build_creds(args)
        secrets = [c['password'] for c in creds.values() if c.get('password')]
        if args.timeout <= 0:
            raise ConfigError('--timeout 必须为正数')
        _self_check_origin_guard()
        if args.app or args.data_dir or args.port is not None:
            lifecycle = _build_lifecycle(args, base_url)
        ctx = Context(base_url, base_url, creds, args.timeout, lifecycle)
        if lifecycle is not None:
            lifecycle.start(init_demo=True)
        results = None
        failures = None
        results, failures = run_cases(ctx)
    except ConfigError as exc:
        print(json.dumps({'ok': False, 'mode': 'config',
                          'error': _redact(str(exc), secrets)}, ensure_ascii=False))
        return 2
    except AssertionError as exc:
        print(json.dumps({'ok': False, 'mode': 'setup',
                          'error': _redact(str(exc), secrets)}, ensure_ascii=False))
        return 1
    finally:
        if lifecycle is not None:
            lifecycle.stop()
    summary = {
        'ok': not failures,
        'mode': 'lifecycle' if lifecycle is not None else 'web',
        'total': len(CASES),
        'passed': sum(1 for value in results.values() if value == 'pass'),
        'failed': len(failures),
        'cases': results,
    }
    if failures:
        summary['failures'] = failures
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == '__main__':
    sys.exit(main())
