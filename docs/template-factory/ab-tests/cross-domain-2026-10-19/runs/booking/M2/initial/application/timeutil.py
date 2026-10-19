"""ISO8601 时间解析与规范化（全部按真实时刻处理）。

- 输入必须是带显式时区偏移（或 Z）的 ISO8601；缺少时区一律拒绝。
- 解析为 UTC epoch 整数用于存储与比较；渲染统一为 +00:00 的 ISO8601。
"""

from datetime import datetime, timezone


def parse_iso_instant(value):
    """把带时区的 ISO8601 字符串解析为 epoch 整数；失败抛 ValueError（可读原因）。"""
    if not isinstance(value, str):
        raise ValueError('时间必须是 ISO8601 字符串')
    text = value.strip()
    if not text:
        raise ValueError('时间不能为空')
    if text[-1] in ('Z', 'z'):
        text = text[:-1] + '+00:00'
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        raise ValueError('无法解析 ISO8601 时间：%s' % value) from None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('时间必须包含显式时区偏移，例如 2035-01-01T10:00:00+08:00')
    return int(parsed.timestamp())


def epoch_to_iso(epoch):
    """把 epoch 整数渲染为规范化的 UTC ISO8601（秒精度）。"""
    moment = datetime.fromtimestamp(int(epoch), timezone.utc).replace(microsecond=0)
    return moment.isoformat()
