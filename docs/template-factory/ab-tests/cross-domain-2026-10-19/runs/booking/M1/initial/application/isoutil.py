"""ISO8601 时刻解析与规范化。

契约要求：时段必须是带显式时区偏移的 ISO8601，按真实时刻（UTC 实例）
比较；内部统一存为 UTC epoch 整数，对外渲染为 UTC ISO8601 字符串。
"""
import datetime

_UTC = datetime.timezone.utc


def parse_instant(value):
    """把带显式时区偏移的 ISO8601 字符串解析为 UTC epoch 整数。

    非法格式或缺少时区偏移时抛出 ValueError（由调用方转为 400）。
    """
    if not isinstance(value, str):
        raise ValueError("时间必须是字符串")
    text = value.strip()
    if not text:
        raise ValueError("时间不能为空")
    if text[-1] in ("Z", "z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.datetime.fromisoformat(text)
    except ValueError:
        raise ValueError("时间格式非法，需为带时区偏移的 ISO8601，例如 2035-01-01T00:00:00+08:00")
    if parsed.tzinfo is None:
        raise ValueError("时间必须包含显式时区偏移，例如 2035-01-01T00:00:00+08:00")
    return int(parsed.timestamp())


def format_instant(epoch):
    """把 UTC epoch 整数渲染为规范化 ISO8601（UTC，偏移 +00:00）。"""
    moment = datetime.datetime.fromtimestamp(int(epoch), _UTC).replace(microsecond=0)
    return moment.isoformat()
