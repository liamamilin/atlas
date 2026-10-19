"""URL 校验、保守归一与 WHATWG 风格 ASCII 序列化。

只依赖 Python 3 标准库。输入为字符串（来自 JSON 或表单），不发起任何网络请求。
"""

import re
import unicodedata

# JavaScript String.prototype.trim 的空白集合（Unicode WhiteSpace + LineTerminator）
_JS_WS = set(
    "\t\n\x0b\x0c\r \xa0\u1680"
    "\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a"
    "\u2028\u2029\u202f\u205f\u3000\ufeff"
)

MAX_URL_CODE_POINTS = 2048
DEFAULT_PORTS = {"http": 80, "https": 443}

# WHATWG 禁止出现在主机里的码点（简化实现；IPv6 括号由解析逻辑单独处理）
_FORBIDDEN_HOST_CHARS = set('\x00\t\n\r #%/:?@\\^|<>"')

# 各组件不进行百分号编码的 ASCII 字符集合的补集
_PATH_UNSAFE = set(' "#<>?`{}')
_QUERY_UNSAFE = set(" \"#<>'")
_FRAG_UNSAFE = set(' "<>`')

_DECIMAL = re.compile(r"^[0-9]+$")
_SCHEME_RE = re.compile(r"^([A-Za-z][A-Za-z0-9+.\-]*):")


class UrlError(Exception):
    """URL 相关校验失败。code/reason 对应统一错误信封。"""

    def __init__(self, code, reason=None, message=None, field=None):
        self.code = code
        self.reason = reason
        self.field = field
        if message is None:
            message = {
                "invalid_url": "URL 不合法",
                "unsupported_protocol": "只支持 http 与 https 地址",
                "invalid_field": "字段类型不合法",
            }.get(code, "URL 不合法")
        super().__init__(message)


def js_trim(value):
    text = str(value)
    start = 0
    end = len(text)
    while start < end and text[start] in _JS_WS:
        start += 1
    while end > start and text[end - 1] in _JS_WS:
        end -= 1
    return text[start:end]


def nfkc(value):
    return unicodedata.normalize("NFKC", value)


def nfkc_lower(value):
    return nfkc(value).lower()


def has_control_char(value):
    for ch in value:
        o = ord(ch)
        if o <= 0x1F or o == 0x7F:
            return True
    return False


def is_decimal_id(value):
    return isinstance(value, str) and _DECIMAL.match(value) is not None


class ParsedUrl(object):
    __slots__ = ("scheme", "host", "host_ascii", "port", "path", "query",
                 "has_query", "fragment", "has_fragment", "is_ipv6")

    def __init__(self):
        self.scheme = "http"
        self.host = ""
        self.host_ascii = ""
        self.port = None
        self.path = "/"
        self.query = ""
        self.has_query = False
        self.fragment = ""
        self.has_fragment = False
        self.is_ipv6 = False

    @property
    def default_port(self):
        return DEFAULT_PORTS.get(self.scheme)

    def effective_port(self):
        return self.port

    def host_for_title(self):
        return self.host


def _host_to_ascii(host, is_ipv6):
    if is_ipv6:
        return "[" + host.lower() + "]"
    lowered = host.lower()
    if all(ord(c) < 128 for c in lowered):
        return lowered
    try:
        return lowered.encode("idna").decode("ascii")
    except Exception:
        return lowered


def _split_authority(authority):
    is_ipv6 = False
    if authority.startswith("["):
        end = authority.find("]")
        if end < 0:
            raise UrlError("invalid_url", "unparsable")
        host = authority[1:end]
        rest = authority[end + 1:]
        if rest == "":
            port_text = None
        elif rest.startswith(":"):
            port_text = rest[1:]
        else:
            raise UrlError("invalid_url", "unparsable")
        is_ipv6 = True
        return host, port_text, is_ipv6
    if authority.count(":") > 1:
        raise UrlError("invalid_url", "unparsable")
    if ":" in authority:
        host, _, port_text = authority.partition(":")
    else:
        host, port_text = authority, None
    return host, port_text, is_ipv6


def parse_url(raw):
    """把已 trim 的字符串解析成 ParsedUrl；失败抛 UrlError。"""
    match = _SCHEME_RE.match(raw)
    if match is None:
        raise UrlError("invalid_url", "unparsable")
    scheme = match.group(1).lower()
    if scheme not in ("http", "https"):
        raise UrlError("unsupported_protocol", "unsupported_protocol")

    rest = raw[match.end():]
    # 特殊协议：忽略 scheme 之后的多余斜杠与反斜杠（http:///path -> host=path）
    index = 0
    while index < len(rest) and rest[index] in "/\\":
        index += 1
    rest = rest[index:]

    cut = len(rest)
    for i, ch in enumerate(rest):
        if ch in "/\\?#":
            cut = i
            break
    authority = rest[:cut]
    remainder = rest[cut:]

    if "@" in authority:
        at = authority.rfind("@")
        userinfo = authority[:at]
        hostport = authority[at + 1:]
        if userinfo != "":
            raise UrlError("invalid_url", "userinfo_not_allowed")
    else:
        hostport = authority

    host, port_text, is_ipv6 = _split_authority(hostport)
    if host == "":
        raise UrlError("invalid_url", "host_required")
    if not is_ipv6:
        for ch in host:
            if ch in _FORBIDDEN_HOST_CHARS or ord(ch) <= 0x20:
                raise UrlError("invalid_url", "unparsable")

    port = None
    if port_text is not None and port_text != "":
        if not _DECIMAL.match(port_text):
            raise UrlError("invalid_url", "unparsable")
        port = int(port_text)
        if port > 65535:
            raise UrlError("invalid_url", "unparsable")

    fragment = ""
    has_fragment = False
    if "#" in remainder:
        remainder, _, fragment = remainder.partition("#")
        has_fragment = True
    query = ""
    has_query = False
    if "?" in remainder:
        remainder, _, query = remainder.partition("?")
        has_query = True
    path = remainder.replace("\\", "/")
    if path == "":
        path = "/"

    parsed = ParsedUrl()
    parsed.scheme = scheme
    parsed.host = host.lower()
    parsed.host_ascii = _host_to_ascii(host, is_ipv6)
    parsed.port = port
    parsed.path = path
    parsed.query = query
    parsed.has_query = has_query
    parsed.fragment = fragment
    parsed.has_fragment = has_fragment
    parsed.is_ipv6 = is_ipv6
    return parsed


def validate_url_value(value):
    """校验并返回 (stored_url, ParsedUrl)。失败抛 UrlError。"""
    if value is None:
        raise UrlError("invalid_url", "required")
    if not isinstance(value, str):
        raise UrlError("invalid_field", field="url", message="URL 必须是字符串")
    if has_control_char(value):
        raise UrlError("invalid_url", "control_character")
    trimmed = js_trim(value)
    if trimmed == "":
        raise UrlError("invalid_url", "required")
    if len(trimmed) > MAX_URL_CODE_POINTS:
        raise UrlError("invalid_url", "url_too_long")
    parsed = parse_url(trimmed)
    return trimmed, parsed


def _percent_encode(text, unsafe):
    out = []
    for ch in text:
        o = ord(ch)
        if o < 0x20 or o == 0x7F or o > 0x7E or ch in unsafe:
            for byte in ch.encode("utf-8", "surrogatepass"):
                out.append("%%%02X" % byte)
        else:
            out.append(ch)
    return "".join(out)


def serialize(parsed):
    """WHATWG URL serializer 的 ASCII 结果（用于 302 Location）。"""
    default = parsed.default_port
    if parsed.port is not None and parsed.port != default:
        authority = "%s:%d" % (parsed.host_ascii, parsed.port)
    else:
        authority = parsed.host_ascii
    path = parsed.path if parsed.path else "/"
    result = parsed.scheme + "://" + authority + _percent_encode(path, _PATH_UNSAFE)
    if parsed.has_query:
        result += "?" + _percent_encode(parsed.query, _QUERY_UNSAFE)
    if parsed.has_fragment:
        result += "#" + _percent_encode(parsed.fragment, _FRAG_UNSAFE)
    return result


def url_key(parsed):
    """D05 保守归一：scheme/host 小写、去默认端口、去非根末尾斜杠、忽略 fragment。"""
    default = parsed.default_port
    if parsed.port is not None and parsed.port != default:
        authority = "%s:%d" % (parsed.host_ascii, parsed.port)
    else:
        authority = parsed.host_ascii
    path = parsed.path if parsed.path else "/"
    if len(path) > 1:
        stripped = path.rstrip("/")
        path = stripped if stripped != "" else "/"
    key = parsed.scheme + "://" + authority + path
    if parsed.has_query:
        key += "?" + parsed.query
    return key


def derived_title(parsed):
    """缺省标题时由主机名派生的可读标题。"""
    host = parsed.host_for_title()
    if parsed.is_ipv6:
        return "[" + host + "]"
    return host if host != "" else parsed.host_ascii
