# -*- coding: utf-8 -*-
"""统一的可预期错误类型。

CLI 层只把 AppError 当作「操作被拒绝/失败」处理：向 stderr 打印说明并非零退出，
且绝不向 stdout 输出任何 JSON（避免假成功）。
"""


class AppError(Exception):
    """可预期的用户侧错误（非法输入、冲突、越界、状态损坏等）。"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message
