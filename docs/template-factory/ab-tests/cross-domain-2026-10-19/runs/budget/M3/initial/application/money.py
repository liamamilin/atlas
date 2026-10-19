# -*- coding: utf-8 -*-
"""金额处理：以整数“分”为准，按两位小数渲染。

约定（D01）：金额一律以整数分存储与计算；超过两位小数或非正数输入
直接拒绝，绝不静默取整或裁剪；响应渲染为两位小数字符串。
"""

from decimal import Decimal, InvalidOperation

MAX_EXPONENT = -2  # 最小允许的小数位数（-2 => 两位）


class MoneyError(ValueError):
    """金额输入不合法。"""


def parse_positive_amount(value):
    """把外部金额输入解析为整数“分”；不合法时抛出 MoneyError。

    接受十进制字符串或整数；拒绝空值、非数字、非有限值、
    超过两位小数以及非正数。
    """
    if value is None:
        raise MoneyError("金额不能为空")
    if isinstance(value, bool):
        raise MoneyError("金额必须是数字")
    text = value.strip() if isinstance(value, str) else str(value)
    if not text:
        raise MoneyError("金额不能为空")
    try:
        decimal = Decimal(text)
    except (InvalidOperation, ValueError, ArithmeticError):
        raise MoneyError("金额必须是数字")
    if not decimal.is_finite():
        raise MoneyError("金额必须是有限数字")
    if decimal.as_tuple().exponent < MAX_EXPONENT:
        raise MoneyError("金额最多两位小数")
    cents = int(decimal.scaleb(2).to_integral_value())
    if cents <= 0:
        raise MoneyError("金额必须为正数")
    return cents


def format_cents(cents):
    """把整数“分”渲染为两位小数字符串（可为负，例如 "-15.00"）。"""
    cents = int(cents)
    sign = "-" if cents < 0 else ""
    magnitude = abs(cents)
    return "%s%d.%02d" % (sign, magnitude // 100, magnitude % 100)
