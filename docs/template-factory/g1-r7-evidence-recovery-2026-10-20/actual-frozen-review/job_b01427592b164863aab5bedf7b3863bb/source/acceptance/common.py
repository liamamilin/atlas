'''Atlas 验收共享工具（Python 3.12 标准库）。

所有验收程序通过本模块与真实目标交互：HTTP 请求、断言记录、
独立实例启动与重启持久化适配器。模块不导入应用实现，也不读取
应用自己的测试判定。
'''

from __future__ import annotations

import argparse
import json as _json
import os
import re
import signal
import socket
import subprocess
import sys
import threading
import time
import uuid
from collections.abc import Mapping
from http.client import HTTPException
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

RESULT_SCHEMA = 'atlas.acceptance-result.v1'
DEFAULT_CATEGORY = '未整理'
PRESET_CATEGORIES = ('未整理', '待购', '家居改造', '以后看看')
HEALTH_PATH = '/api/health'
KNOWN_CASES = frozenset(f'A{i:02d}' for i in range(1, 16))
RESTART_CASES = frozenset({'A01', 'A05', 'A09'})
DATA_DIR_CASES = frozenset({'A01', 'A05', 'A09', 'A14'})

_SENSITIVE_QUERY_KEYS = frozenset({
    'token', 'access_token', 'password', 'passwd', 'secret', 'key',
    'apikey', 'api_key', 'auth', 'authorization', 'session', 'cookie',
})
_URL_RE = re.compile(r'https?://\S+')


class AcceptanceError(RuntimeError):
    '''验收基础设施或目标行为错误。'''


class AppStartError(AcceptanceError):
    '''应用实例无法启动或未就绪。'''


class HttpRequestError(AcceptanceError):
    '''真实 HTTP 请求失败。'''


class ExternalNavigationBlocked(HttpRequestError):
    '''请求或重定向离开被验收目标。'''


def _redact_url(url: Any) -> str:
    try:
        parts = urlsplit(str(url))
    except (TypeError, ValueError):
        return '<invalid-url>'
    try:
        port = parts.port
    except ValueError:
        port = None
    if parts.username is not None or parts.password is not None:
        host = parts.hostname or ''
        if ':' in host and not host.startswith('['):
            host = f'[{host}]'
        netloc = host
        if port is not None:
            netloc = f'{netloc}:{port}'
    else:
        netloc = parts.netloc
    query = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        if key.lower() in _SENSITIVE_QUERY_KEYS:
            query.append((key, '***'))
        else:
            query.append((key, value))
    return urlunsplit((
        parts.scheme,
        netloc,
        parts.path,
        urlencode(query, doseq=True) if query else '',
        parts.fragment,
    ))


def _redact_text(value: Any, limit: int = 1200) -> str:
    text = str(value)
    text = _URL_RE.sub(lambda match: _redact_url(match.group(0)), text)
    if len(text) > limit:
        text = text[:limit] + '…'
    return text


def _origin(url: str) -> tuple[str, str, int]:
    parts = urlsplit(url)
    scheme = parts.scheme.lower()
    if scheme not in ('http', 'https'):
        raise ValueError('仅支持 http/https')
    if not parts.hostname:
        raise ValueError('缺少主机名')
    if parts.username is not None or parts.password is not None:
        raise ValueError('不得包含凭据')
    try:
        port = parts.port
    except ValueError as exc:
        raise ValueError('端口无效') from exc
    if port is None:
        port = 443 if scheme == 'https' else 80
    return (scheme, parts.hostname.lower(), port)


def _normalize_base_url(url: str) -> str:
    if not isinstance(url, str) or not url.strip():
        raise ValueError('不能为空')
    value = url.strip()
    parts = urlsplit(value)
    if parts.query or parts.fragment:
        raise ValueError('不得包含查询参数或片段')
    _origin(value)
    return urlunsplit((parts.scheme.lower(), parts.netloc, parts.path.rstrip('/'), '', ''))


def _has_header(headers: Mapping[str, Any], name: str) -> bool:
    target = name.lower()
    return any(str(key).lower() == target for key in headers)


def _short_repr(value: Any, limit: int = 300) -> str:
    try:
        text = _json.dumps(value, ensure_ascii=False, default=str)
    except (TypeError, ValueError):
        text = repr(value)
    if len(text) > limit:
        text = text[:limit] + '…'
    return _redact_text(text, limit + 10)


def _lookup_path(value: Any, field: Any) -> tuple[bool, Any]:
    if field is None or field == '' or field == '$':
        parts: list[str] = []
    elif isinstance(field, (list, tuple)):
        parts = [str(part) for part in field]
    else:
        text = str(field)
        if text.startswith('/'):
            parts = [part.replace('~1', '/').replace('~0', '~') for part in text.split('/')[1:]]
        else:
            parts = text.split('.')
    current = value
    for part in parts:
        if isinstance(current, Mapping):
            if part not in current:
                return False, None
            current = current[part]
        elif isinstance(current, list):
            try:
                index = int(part)
            except ValueError:
                return False, None
            if index < 0:
                index += len(current)
            if index < 0 or index >= len(current):
                return False, None
            current = current[index]
        else:
            return False, None
    return True, current


class HttpResponse:
    def __init__(self, status: int, headers: Any, body: bytes, method: str, url: str, elapsed: float = 0.0):
        self.status = int(status)
        self.headers = headers if headers is not None else {}
        self.body = body or b''
        self.method = method
        self.url = _redact_url(url)
        self.elapsed = elapsed

    @property
    def status_code(self) -> int:
        return self.status

    @property
    def code(self) -> int:
        return self.status

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300

    def header(self, name: str, default: Any = None) -> Any:
        try:
            value = self.headers.get(name)
        except AttributeError:
            value = None
        if value is not None:
            return value
        try:
            items = self.headers.items()
        except AttributeError:
            return default
        target = name.lower()
        for key, item in items:
            if str(key).lower() == target:
                return item
        return default

    @property
    def location(self) -> str | None:
        value = self.header('Location')
        return None if value is None else str(value)

    @property
    def content_type(self) -> str:
        return str(self.header('Content-Type') or '')

    @property
    def text(self) -> str:
        content_type = self.content_type
        match = re.search(r'charset=([\w.-]+)', content_type, re.IGNORECASE)
        charset = match.group(1) if match else 'utf-8'
        if charset.lower().replace('_', '-') in ('utf-8', 'utf8'):
            charset = 'utf-8-sig'
        try:
            return self.body.decode(charset, 'replace')
        except LookupError:
            return self.body.decode('utf-8', 'replace')

    def json(self) -> Any:
        return _json.loads(self.text)

    def get_json(self) -> Any:
        return self.json()

    def __repr__(self) -> str:
        return f'<HttpResponse {self.status} {self.method} {self.url}>'


class _NoRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class HttpClient:
    def __init__(self, base_url: str, timeout: float = 20.0, follow_redirects: bool = True):
        self.base_url = _normalize_base_url(base_url)
        self.origin = _origin(self.base_url)
        self.timeout = float(timeout)
        self.follow_redirects = bool(follow_redirects)
        self._opener = build_opener(_NoRedirectHandler(), ProxyHandler({}))

    def close(self) -> None:
        return None

    def __enter__(self) -> 'HttpClient':
        return self

    def __exit__(self, exc_type, exc, traceback) -> bool:
        self.close()
        return False

    def _build_url(self, path: Any, params: Any) -> str:
        text = '' if path is None else str(path)
        parts = urlsplit(text)
        if parts.scheme:
            if parts.scheme.lower() not in ('http', 'https'):
                raise ExternalNavigationBlocked(f'拒绝非 http/https URL：{_redact_url(text)}')
            try:
                absolute_origin = _origin(text)
            except ValueError as exc:
                raise ExternalNavigationBlocked(f'拒绝无效 URL：{_redact_url(text)}') from exc
            if absolute_origin != self.origin:
                raise ExternalNavigationBlocked(f'拒绝访问目标以外的 URL：{_redact_url(text)}')
            url = text
        elif parts.netloc:
            raise ExternalNavigationBlocked('拒绝协议相对 URL')
        elif text.startswith('?'):
            url = self.base_url + text
        elif text.startswith('/'):
            url = self.base_url + text
        elif text:
            url = self.base_url + '/' + text
        else:
            url = self.base_url
        final = urlsplit(url)
        query = final.query
        if params:
            pairs = parse_qsl(query, keep_blank_values=True)
            if isinstance(params, Mapping):
                pairs.extend(params.items())
            else:
                pairs.extend(params)
            query = urlencode(pairs, doseq=True)
        return urlunsplit((final.scheme, final.netloc, final.path, query, ''))

    def request(self, method: str, path: str = '', *, params: Any = None, headers: Any = None,
                json: Any = None, data: Any = None, form: Any = None, accept: str | None = None,
                follow_redirects: bool | None = None, timeout: float | None = None,
                max_redirects: int = 5) -> HttpResponse:
        current_method = str(method).upper()
        if current_method not in ('GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'):
            raise ValueError('不支持的 HTTP 方法')
        body_kinds = (json is not None, data is not None, form is not None)
        if sum(1 for flag in body_kinds if flag) > 1:
            raise ValueError('json、data 与 form 只能提供一个')
        body: bytes | None = None
        content_type: str | None = None
        if json is not None:
            body = _json.dumps(json, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
            content_type = 'application/json; charset=utf-8'
        elif form is not None:
            pairs = form.items() if isinstance(form, Mapping) else form
            body = urlencode(list(pairs), doseq=True).encode('utf-8')
            content_type = 'application/x-www-form-urlencoded; charset=utf-8'
        elif data is not None:
            if isinstance(data, str):
                body = data.encode('utf-8')
            elif isinstance(data, (bytes, bytearray)):
                body = bytes(data)
            else:
                raise TypeError('data 必须是 str 或 bytes')
        prepared = {str(key): str(value) for key, value in (headers or {}).items()}
        for key in prepared:
            if key.lower() in ('authorization', 'proxy-authorization'):
                raise ValueError('目标不需要认证，不支持认证头')
        if not _has_header(prepared, 'Accept'):
            prepared['Accept'] = accept or 'application/json'
        if not _has_header(prepared, 'User-Agent'):
            prepared['User-Agent'] = 'atlas-acceptance/1.0'
        if not _has_header(prepared, 'Accept-Encoding'):
            prepared['Accept-Encoding'] = 'identity'
        if body is not None and content_type and not _has_header(prepared, 'Content-Type'):
            prepared['Content-Type'] = content_type
        follow = self.follow_redirects if follow_redirects is None else bool(follow_redirects)
        resolved_timeout = self.timeout if timeout is None else float(timeout)
        current_url = self._build_url(path, params)
        current_body = body
        current_headers = prepared
        redirects = 0
        while True:
            request = Request(
                current_url,
                data=current_body if current_method not in ('GET', 'HEAD') else None,
                headers=current_headers,
                method=current_method,
            )
            started = time.monotonic()
            try:
                with self._opener.open(request, timeout=resolved_timeout) as raw:
                    status = int(getattr(raw, 'status', raw.getcode()))
                    response_headers = raw.headers
                    response_body = raw.read()
            except HTTPError as exc:
                status = int(exc.code)
                response_headers = exc.headers if exc.headers is not None else {}
                try:
                    response_body = exc.read()
                except Exception:
                    response_body = b''
                finally:
                    try:
                        exc.close()
                    except Exception:
                        pass
            except (URLError, HTTPException, TimeoutError, OSError, ValueError) as exc:
                reason = getattr(exc, 'reason', exc)
                raise HttpRequestError(
                    f'{current_method} {_redact_url(current_url)} 请求失败：{_redact_text(reason, 300)}'
                ) from exc
            elapsed = time.monotonic() - started
            response = HttpResponse(status, response_headers, response_body, current_method, current_url, elapsed)
            if not follow or status not in (301, 302, 303, 307, 308):
                return response
            location = response.location
            if not location:
                return response
            if redirects >= max_redirects:
                raise HttpRequestError(f'重定向次数超过 {max_redirects}：{_redact_url(current_url)}')
            redirects += 1
            next_url = urljoin(current_url, location.strip())
            try:
                next_origin = _origin(next_url)
            except ValueError as exc:
                raise ExternalNavigationBlocked(f'拒绝重定向到无效目标：{_redact_url(next_url)}') from exc
            if next_origin != self.origin:
                raise ExternalNavigationBlocked(f'拒绝跨源重定向：{_redact_url(next_url)}')
            if status == 303 or (status in (301, 302) and current_method == 'POST'):
                current_method = 'GET'
                current_body = None
                current_headers = {
                    key: value for key, value in current_headers.items()
                    if key.lower() not in ('content-type', 'content-length')
                }
            current_url = next_url

    def get(self, path: str = '', *, params: Any = None, headers: Any = None,
            accept: str | None = None, follow_redirects: bool | None = None,
            timeout: float | None = None) -> HttpResponse:
        return self.request('GET', path, params=params, headers=headers, accept=accept,
                            follow_redirects=follow_redirects, timeout=timeout)

    def post_form(self, path: str, fields: Any, *, headers: Any = None, accept: str | None = None,
                  follow_redirects: bool | None = None, timeout: float | None = None) -> HttpResponse:
        return self.request('POST', path, form=fields, headers=headers, accept=accept,
                            follow_redirects=follow_redirects, timeout=timeout)

    def post_json(self, path: str, payload: Any, *, headers: Any = None, accept: str | None = None,
                  follow_redirects: bool | None = None, timeout: float | None = None) -> HttpResponse:
        return self.request('POST', path, json=payload, headers=headers, accept=accept,
                            follow_redirects=follow_redirects, timeout=timeout)

    def patch_json(self, path: str, payload: Any, *, headers: Any = None, accept: str | None = None,
                   follow_redirects: bool | None = None, timeout: float | None = None) -> HttpResponse:
        return self.request('PATCH', path, json=payload, headers=headers, accept=accept,
                            follow_redirects=follow_redirects, timeout=timeout)


class AppProcess(subprocess.Popen):
    def __init__(self, args, *, base_url: str, scratch_dir: str, app_root: str, port: int,
                 log_path: str, log_handle: Any, **kwargs):
        super().__init__(args, **kwargs)
        self.base_url = base_url
        self.scratch_dir = scratch_dir
        self.app_root = app_root
        self.port = port
        self.log_path = log_path
        self.log_handle = log_handle
        self._atlas_group = bool(kwargs.get('start_new_session')) and os.name == 'posix'

    @property
    def instance_dir(self) -> str:
        return self.scratch_dir

    @property
    def process(self) -> 'AppProcess':
        return self

    def __iter__(self):
        yield self
        yield self.base_url
        yield self.scratch_dir

    def stop(self, timeout: float = 10.0) -> None:
        stop_app(self, timeout=timeout)

    def __enter__(self) -> 'AppProcess':
        return self

    def __exit__(self, exc_type, exc, traceback) -> bool:
        stop_app(self)
        return False


_REGISTRY_LOCK = threading.RLock()
_SCRATCH_BY_KEY: dict[tuple[str, str], str] = {}
_ACTIVE_BY_KEY: dict[tuple[str, str], AppProcess] = {}


def _tail(path: Any, limit: int = 4000) -> str:
    if not path:
        return ''
    try:
        with open(str(path), 'rb') as handle:
            handle.seek(0, os.SEEK_END)
            position = handle.tell()
            handle.seek(max(0, position - limit))
            data = handle.read()
    except OSError:
        return ''
    return _redact_text(data.decode('utf-8', 'replace'), limit)


def wait_health(base_url: str, timeout: float = 30.0, proc: AppProcess | None = None) -> bool:
    base = _normalize_base_url(base_url)
    deadline = time.monotonic() + max(0.0, float(timeout))
    last_error = '尚未收到健康响应'
    while True:
        if proc is not None and proc.poll() is not None:
            tail = _tail(getattr(proc, 'log_path', None))
            suffix = f'；日志尾部：{tail}' if tail else ''
            raise AppStartError(f'应用进程在就绪前退出（code={proc.returncode}）{suffix}')
        remaining = deadline - time.monotonic()
        try:
            client = HttpClient(base, timeout=max(0.5, min(2.0, remaining if remaining > 0 else 0.5)))
            response = client.get(HEALTH_PATH)
            if response.status == 200:
                try:
                    payload = response.json()
                except Exception as exc:
                    last_error = f'健康检查返回非 JSON：{_redact_text(exc, 200)}'
                else:
                    if isinstance(payload, dict):
                        return True
                    last_error = '健康检查 JSON 不是对象'
            elif response.status in (401, 403):
                raise AppStartError('目标要求认证，当前验收适配器不支持认证')
            else:
                last_error = f'健康检查返回 HTTP {response.status}'
        except AppStartError:
            raise
        except Exception as exc:
            last_error = _redact_text(exc, 300)
        if time.monotonic() >= deadline:
            break
        time.sleep(min(0.2, max(0.02, deadline - time.monotonic())))
    tail = _tail(getattr(proc, 'log_path', None)) if proc is not None else ''
    message = f'等待 {_redact_url(base)}/api/health 就绪超时：{last_error}'
    if tail:
        message += f'；日志尾部：{tail}'
    raise AppStartError(message)


def _prepare_app_root(app_root: Any) -> tuple[str, str]:
    if not app_root:
        raise AppStartError('--app-root 不能为空')
    root = os.path.realpath(os.path.abspath(os.path.expanduser(str(app_root))))
    if not os.path.isdir(root):
        raise AppStartError('--app-root 不存在或不是目录')
    script = os.path.join(root, 'app', 'serve.py')
    if not os.path.isfile(script):
        raise AppStartError('--app-root 中缺少 app/serve.py')
    return root, script


def _ensure_directory(path: Any, label: str) -> str:
    if not path:
        raise AppStartError(f'{label} 不能为空')
    target = os.path.realpath(os.path.abspath(os.path.expanduser(str(path))))
    try:
        os.makedirs(target, mode=0o700, exist_ok=True)
    except OSError as exc:
        raise AppStartError(f'{label} 无法创建') from exc
    if not os.path.isdir(target):
        raise AppStartError(f'{label} 不是目录')
    return target


def _new_instance(instances_root: str) -> str:
    path = os.path.join(instances_root, uuid.uuid4().hex)
    try:
        os.makedirs(path, mode=0o700, exist_ok=False)
    except OSError as exc:
        raise AppStartError('无法创建每实例隔离 scratch') from exc
    return os.path.realpath(path)


def _validate_instance(instances_root: str, instance_dir: str) -> str:
    candidate = os.path.realpath(os.path.abspath(os.path.expanduser(str(instance_dir))))
    try:
        common = os.path.commonpath([instances_root, candidate])
    except ValueError as exc:
        raise AppStartError('实例目录必须位于 data_dir/instances 下') from exc
    if common != instances_root or candidate == instances_root:
        raise AppStartError('实例目录必须位于 data_dir/instances 下')
    try:
        os.makedirs(candidate, mode=0o700, exist_ok=True)
    except OSError as exc:
        raise AppStartError('无法创建实例目录') from exc
    return candidate


def _close_log(proc: Any) -> None:
    handle = getattr(proc, 'log_handle', None)
    if handle is not None:
        try:
            handle.close()
        except Exception:
            pass
        try:
            proc.log_handle = None
        except Exception:
            pass


def _forget_active(proc: Any) -> None:
    with _REGISTRY_LOCK:
        for key, active in list(_ACTIVE_BY_KEY.items()):
            if active is proc:
                _ACTIVE_BY_KEY.pop(key, None)


def _send_signal(proc: Any, sig: int) -> None:
    if getattr(proc, '_atlas_group', False) and hasattr(os, 'killpg'):
        try:
            os.killpg(os.getpgid(proc.pid), sig)
            return
        except (ProcessLookupError, PermissionError, OSError):
            pass
    try:
        proc.send_signal(sig)
    except (ProcessLookupError, OSError):
        pass


def stop_app(proc: Any, timeout: float = 10.0) -> None:
    if proc is None:
        return
    try:
        if proc.poll() is None:
            _send_signal(proc, signal.SIGTERM)
            try:
                proc.wait(timeout=float(timeout))
            except subprocess.TimeoutExpired:
                _send_signal(proc, getattr(signal, 'SIGKILL', signal.SIGTERM))
                try:
                    proc.wait(timeout=5.0)
                except (subprocess.TimeoutExpired, OSError):
                    pass
        else:
            try:
                proc.wait(timeout=1.0)
            except (subprocess.TimeoutExpired, OSError):
                pass
    finally:
        _close_log(proc)
        _forget_active(proc)


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('127.0.0.1', 0))
        return int(sock.getsockname()[1])


def launch_app(app_root: str, data_dir: str, port: int, *, instance_dir: str | None = None,
               fresh: bool = False, timeout: float = 30.0,
               env: Mapping[str, str] | None = None) -> AppProcess:
    root, script = _prepare_app_root(app_root)
    data_root = _ensure_directory(data_dir, '--data-dir')
    try:
        numeric_port = int(port)
    except (TypeError, ValueError) as exc:
        raise AppStartError('port 必须是整数') from exc
    if numeric_port <= 0:
        numeric_port = free_port()
    if numeric_port < 1 or numeric_port > 65535:
        raise AppStartError('port 超出范围')
    instances_root = _ensure_directory(os.path.join(data_root, 'instances'), '实例根目录')
    key = (root, data_root)
    with _REGISTRY_LOCK:
        previous = _ACTIVE_BY_KEY.get(key)
        if previous is not None and previous.poll() is None:
            raise AppStartError('该 data_dir 已有运行中的实例，请先调用 stop_app')
        if previous is not None:
            _close_log(previous)
            _ACTIVE_BY_KEY.pop(key, None)
        if instance_dir is not None and fresh:
            raise AppStartError('instance_dir 与 fresh 不能同时使用')
        if instance_dir is not None:
            scratch = _validate_instance(instances_root, instance_dir)
        elif fresh or key not in _SCRATCH_BY_KEY or not os.path.isdir(_SCRATCH_BY_KEY[key]):
            scratch = _new_instance(instances_root)
        else:
            scratch = _SCRATCH_BY_KEY[key]
        _SCRATCH_BY_KEY[key] = scratch
        logs_dir = _ensure_directory(os.path.join(scratch, 'logs'), '实例日志目录')
        log_path = os.path.join(logs_dir, f'app-{int(time.time() * 1000)}-{uuid.uuid4().hex[:8]}.log')
        log_handle = open(log_path, 'ab', buffering=0)
        command = [
            sys.executable or 'python3', script,
            '--host', '127.0.0.1',
            '--port', str(numeric_port),
            '--data-dir', scratch,
        ]
        child_env = os.environ.copy()
        if env:
            child_env.update({str(name): str(value) for name, value in env.items()})
        child_env['PYTHONUNBUFFERED'] = '1'
        child_env['PYTHONDONTWRITEBYTECODE'] = '1'
        for proxy_name in (
            'HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY', 'NO_PROXY',
            'http_proxy', 'https_proxy', 'all_proxy', 'no_proxy',
        ):
            child_env.pop(proxy_name, None)
        try:
            proc = AppProcess(
                command,
                base_url=f'http://127.0.0.1:{numeric_port}',
                scratch_dir=scratch,
                app_root=root,
                port=numeric_port,
                log_path=log_path,
                log_handle=log_handle,
                cwd=root,
                env=child_env,
                stdin=subprocess.DEVNULL,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
                close_fds=True,
                start_new_session=(os.name == 'posix'),
            )
        except OSError as exc:
            log_handle.close()
            _SCRATCH_BY_KEY.pop(key, None)
            raise AppStartError('无法启动应用进程') from exc
        except Exception:
            log_handle.close()
            _SCRATCH_BY_KEY.pop(key, None)
            raise
        _ACTIVE_BY_KEY[key] = proc
    try:
        wait_health(proc.base_url, timeout=timeout, proc=proc)
    except AppStartError as exc:
        stop_app(proc)
        with _REGISTRY_LOCK:
            _SCRATCH_BY_KEY.pop(key, None)
        raise AppStartError(f'{exc}；启动日志：{log_path}') from exc
    except BaseException:
        stop_app(proc)
        raise
    return proc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='acceptance',
        description='Atlas 真实目标验收参数（python-web）',
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('--case', required=True, choices=sorted(KNOWN_CASES), help='验收用例 ID，如 A01')
    parser.add_argument('--base-url', required=True, help='已部署应用的根 URL')
    parser.add_argument('--app-root', help='只读应用源码根目录，用于重启持久化适配器')
    parser.add_argument('--data-dir', help='验收者可变草稿目录；实例数据库位于其 instances 子目录')
    return parser


def parse_case_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.base_url = _normalize_base_url(args.base_url)
    except ValueError as exc:
        parser.error(f'--base-url 无效：{exc}')
    args.case_id = args.case
    if args.app_root:
        args.app_root = os.path.abspath(os.path.expanduser(args.app_root))
        if not os.path.isdir(args.app_root):
            parser.error('--app-root 不存在或不是目录')
    if args.data_dir:
        args.data_dir = os.path.abspath(os.path.expanduser(args.data_dir))
        if os.path.realpath(args.data_dir) == os.path.realpath(os.sep):
            parser.error('--data-dir 不能是文件系统根目录')
        try:
            os.makedirs(args.data_dir, mode=0o700, exist_ok=True)
        except OSError:
            parser.error('--data-dir 无法创建')
        if not os.path.isdir(args.data_dir):
            parser.error('--data-dir 不是目录')
        if not os.access(args.data_dir, os.W_OK):
            parser.error('--data-dir 不可写')
    if args.app_root and args.data_dir:
        if os.path.realpath(args.app_root) == os.path.realpath(args.data_dir):
            parser.error('--data-dir 不得与 --app-root 相同')
    if args.case in RESTART_CASES:
        if not args.app_root:
            parser.error(f'--case {args.case} 需要 --app-root')
        serve_script = os.path.join(args.app_root, 'app', 'serve.py')
        if not os.path.isfile(serve_script):
            parser.error('--app-root 中缺少 app/serve.py')
        if not args.data_dir:
            parser.error(f'--case {args.case} 需要 --data-dir')
    if args.case in DATA_DIR_CASES and not args.data_dir:
        parser.error(f'--case {args.case} 需要 --data-dir')
    return args


def _normalize_assertions(assertions: Any) -> list[dict[str, Any]]:
    if hasattr(assertions, 'assertions'):
        assertions = assertions.assertions
    if assertions is None:
        assertions = []
    if isinstance(assertions, Mapping):
        assertions = [assertions]
    items: list[dict[str, Any]] = []
    for index, item in enumerate(assertions, start=1):
        if isinstance(item, Mapping):
            raw_id = item.get('id')
            passed = item.get('passed', False)
            detail = item.get('detail', '')
        elif isinstance(item, (tuple, list)) and len(item) >= 3:
            raw_id, passed, detail = item[0], item[1], item[2]
        else:
            raise TypeError('断言必须是包含 id/passed/detail 的映射')
        clean_id = _redact_text(raw_id, 120).strip() if raw_id is not None else ''
        if not clean_id:
            clean_id = f'assertion-{index}'
        items.append({
            'id': clean_id,
            'passed': bool(passed),
            'detail': _redact_text(detail, 1200),
        })
    return items


def _fit_result(result: dict[str, Any]) -> str:
    text = _json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    while len(text.encode('utf-8')) > 60000:
        changed = False
        for item in result['assertions']:
            detail = item['detail']
            if len(detail) > 40:
                item['detail'] = detail[:max(40, len(detail) // 2)]
                changed = True
        if not changed:
            for item in result['assertions']:
                if len(item['id']) > 24:
                    item['id'] = item['id'][:24]
                    changed = True
        if not changed:
            break
        text = _json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    while len(text.encode('utf-8')) > 60000 and len(result['assertions']) > 1:
        result['assertions'].pop()
        text = _json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    return text


def emit_result(case_id: str, assertions: Any, status: str | None = None) -> int:
    if case_id is None or not str(case_id).strip():
        raise ValueError('case_id 不能为空')
    case_text = _redact_text(case_id, 120).strip()
    items = _normalize_assertions(assertions)
    has_failure = any(not item['passed'] for item in items)
    if status is None:
        final_status = 'failed' if has_failure or not items else 'passed'
    else:
        if status not in ('passed', 'failed', 'unverified'):
            raise ValueError('status 只能是 passed、failed 或 unverified')
        final_status = status
        if has_failure:
            final_status = 'failed'
        elif not items and final_status == 'passed':
            final_status = 'failed'
    result = {
        'schema': RESULT_SCHEMA,
        'case_id': case_text,
        'status': final_status,
        'assertions': items,
    }
    text = _fit_result(result)
    payload = (text + chr(10)).encode('utf-8')
    buffer = getattr(sys.stdout, 'buffer', None)
    if buffer is not None:
        buffer.write(payload)
        buffer.flush()
    else:
        sys.stdout.write(text + chr(10))
        sys.stdout.flush()
    failures = [item['id'] for item in items if not item['passed']]
    if failures:
        failure_text = ', '.join(failures)
        print(f'[atlas] {case_text}: {final_status}; 失败断言: {failure_text}', file=sys.stderr, flush=True)
    else:
        print(f'[atlas] {case_text}: {final_status}; 断言 {len(items)} 条', file=sys.stderr, flush=True)
    return 0 if final_status == 'passed' else 1


class Recorder:
    def __init__(self, case_id: str | None = None):
        self.case_id = case_id
        self.assertions: list[dict[str, Any]] = []
        self.failed = False

    @property
    def ok(self) -> bool:
        return not self.failed

    @property
    def passed(self) -> bool:
        return bool(self.assertions) and not self.failed

    def check(self, aid: Any, passed: Any, detail: Any = '') -> bool:
        index = len(self.assertions) + 1
        if aid is None:
            clean_id = f'assertion-{index}'
        else:
            clean_id = _redact_text(aid, 120).strip() or f'assertion-{index}'
        value = bool(passed)
        if not value:
            self.failed = True
        detail_text = _redact_text(detail, 1200)
        entry = {
            'id': clean_id,
            'passed': value,
            'detail': detail_text,
        }
        self.assertions.append(entry)
        state = 'PASS' if value else 'FAIL'
        print(f'[{clean_id}] {state} {detail_text}', file=sys.stderr, flush=True)
        return value

    def expect_status(self, response: Any, expected: Any, aid: Any = None, detail: Any = None) -> Any:
        if isinstance(expected, int) and not isinstance(expected, bool):
            wanted = [int(expected)]
        else:
            wanted = [int(item) for item in expected]
        actual = getattr(response, 'status', None)
        if actual is None:
            actual = getattr(response, 'status_code', None)
        value = actual in wanted
        if detail is None:
            method = getattr(response, 'method', '?')
            url = getattr(response, 'url', '?')
            wanted_text = '/'.join(str(item) for item in wanted)
            detail = f'{method} {url} -> HTTP {actual}（期望 {wanted_text}）'
        index = len(self.assertions) + 1
        self.check(aid if aid is not None else f'status-{index}', value, detail)
        return response

    def expect_json_field(self, response: Any, field: Any, expected: Any, aid: Any = None,
                          detail: Any = None) -> Any:
        index = len(self.assertions) + 1
        try:
            payload = response.json()
        except Exception as exc:
            self.check(aid if aid is not None else f'json-{index}', False,
                       f'响应不是合法 JSON：{_redact_text(exc, 200)}')
            return response
        found, value = _lookup_path(payload, field)
        actual_text = _short_repr(value) if found else '字段不存在'
        passed = False
        error_text = ''
        if found:
            try:
                if callable(expected):
                    passed = bool(expected(value))
                elif isinstance(expected, re.Pattern):
                    passed = bool(expected.search(str(value)))
                elif isinstance(expected, type):
                    passed = isinstance(value, expected)
                else:
                    passed = value == expected
            except Exception as exc:
                error_text = _redact_text(exc, 200)
        if detail is None:
            detail = f'字段 {field} = {actual_text}（期望 {_short_repr(expected)}）'
            if error_text:
                detail += f'；比较异常：{error_text}'
        self.check(aid if aid is not None else f'json-{index}', passed, detail)
        return response

    def finish(self, case_id: str | None = None, status: str | None = None) -> int:
        return emit_result(case_id or self.case_id or '', self.assertions, status=status)


__all__ = [
    'DEFAULT_CATEGORY',
    'PRESET_CATEGORIES',
    'RESULT_SCHEMA',
    'AcceptanceError',
    'AppProcess',
    'AppStartError',
    'ExternalNavigationBlocked',
    'HttpClient',
    'HttpRequestError',
    'HttpResponse',
    'Recorder',
    'build_parser',
    'emit_result',
    'free_port',
    'launch_app',
    'parse_case_args',
    'stop_app',
    'wait_health',
]
