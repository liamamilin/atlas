"""ISO8601 时区时间解析与规范化。

输入必须带显式时区偏移，按真实时刻（epoch 秒）比较；
输出统一为 UTC ISO8601 字符串。
"""
from datetime import datetime, timezone


class TimeError(ValueError):
    pass


def parse_instant(value):
    """把带时区的 ISO8601 字符串解析为 epoch 秒（float）。

    遇到无时区、格式错误或非字符串一律抛出 TimeError（交由上层转成 400）。
    """
    if not isinstance(value, str) or not value.strip():
        raise TimeError("时间必须是带时区的 ISO8601 字符串")
    text = value.strip()
    if text.endswith("Z") or text.endswith("z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        raise TimeError("无法解析时间：%s" % value)
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise TimeError("时间必须包含时区偏移，例如 2026-11-01T10:00:00+08:00")
    return dt.timestamp()


def to_iso(ts):
    """epoch 秒 -> UTC ISO8601 字符串。"""
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def now_iso():
    return datetime.now(timezone.utc).isoformat()
