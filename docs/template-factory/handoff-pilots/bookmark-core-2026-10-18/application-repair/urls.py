"""URL 校验与最小规范化比较键。

仅接受 http/https；比较键只做最小规范化（trim、scheme/host 小写、去默认端口、
去路径末尾多余斜杠），保留 query 与 fragment 作为身份的一部分。
"""

import urllib.parse

HTTP_SCHEMES = ("http", "https")


def validate_url(raw):
    """返回 (原始URL, 错误信息)。错误信息为 None 表示通过。"""
    text = (raw or "").strip()
    if not text:
        return None, "请填写链接 URL（必填）。"
    for ch in text:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            return None, "链接无效：包含不允许的控制字符，请修正后重试。"
    try:
        parts = urllib.parse.urlsplit(text)
        _ = parts.port  # 触发非法端口解析
    except ValueError:
        return None, "链接无效：格式不正确，请修正后重试。"
    scheme = (parts.scheme or "").lower()
    if scheme not in HTTP_SCHEMES:
        return None, "链接无效：仅支持 http 或 https 协议。"
    if not parts.netloc:
        return None, "链接无效：缺少主机名，例如 https://example.com/。"
    return text, None


def url_key(raw):
    """最小规范化键：同一页面视为相同的判定基准。"""
    text = (raw or "").strip()
    try:
        parts = urllib.parse.urlsplit(text)
        port = parts.port
    except ValueError:
        return text
    scheme = (parts.scheme or "").lower()
    host = (parts.hostname or "").lower()
    netloc = host
    default_port = (scheme == "http" and port == 80) or (scheme == "https" and port == 443)
    if port is not None and not default_port:
        netloc = "%s:%d" % (host, port)
    if parts.username:
        userinfo = parts.username
        if parts.password:
            userinfo += ":" + parts.password
        netloc = userinfo + "@" + netloc
    path = parts.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/") or "/"
    return urllib.parse.urlunsplit((scheme, netloc, path, parts.query, parts.fragment))
