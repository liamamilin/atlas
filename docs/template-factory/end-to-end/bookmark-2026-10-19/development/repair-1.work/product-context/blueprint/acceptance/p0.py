'''acceptance/p0.py — P0 薄聚合器与可执行入口（A01–A10）。

本脚本以 __file__ 定位套件根（sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))）后导入 acceptance.common、acceptance.p0_core 与
acceptance.p0_find，确保以 `python /suite/acceptance/p0.py` 运行且 cwd 非 /suite
时导入仍可用。

职责仅为聚合：合并 acceptance.p0_core.CASES（A01–A05）与
acceptance.p0_find.CASES（A06–A10），交由 acceptance.common.main 以
`--case A01..A10 --base-url <url> [--data-dir <dir>] [--app-root <dir>]` 逐例执行。
一个用例一次进程，stdout 恰一个 atlas.acceptance-result.v1 JSON，诊断写 stderr，
失败非零退出。本模块不实现任何用例逻辑、不硬编码任何结论、不使用 mock，也不读取
应用数据库；spec.acceptance 中 A01–A10 的 implementation 均指向本文件。
'''

import os
import sys

_SUITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SUITE_ROOT not in sys.path:
    sys.path.insert(0, _SUITE_ROOT)

from acceptance import p0_core
from acceptance import p0_find
from acceptance.common import fail_explicit, main

__all__ = ['CASES']

# P0 阶段规范要求覆盖的验收用例 ID 集合；缺项或多项即为套件装配错误。
_EXPECTED_P0_CASES = frozenset([
    'A01', 'A02', 'A03', 'A04', 'A05',
    'A06', 'A07', 'A08', 'A09', 'A10',
])


def _merge_cases(*sources):
    '''合并各阶段模块的 CASES，重复、缺失与多余 ID 均显式失败。'''
    merged = {}
    for source in sources:
        for case_id, func in source.items():
            if case_id in merged:
                fail_explicit('duplicate P0 case id %r across phase modules' % case_id)
            if not callable(func):
                fail_explicit('P0 case %r is not callable' % case_id)
            merged[case_id] = func
    missing = sorted(_EXPECTED_P0_CASES - set(merged))
    if missing:
        fail_explicit('missing P0 case implementations: ' + ', '.join(missing))
    unexpected = sorted(set(merged) - _EXPECTED_P0_CASES)
    if unexpected:
        fail_explicit('unexpected P0 case ids: ' + ', '.join(unexpected))
    return merged


CASES = _merge_cases(p0_core.CASES, p0_find.CASES)


if __name__ == '__main__':
    main(CASES, sys.argv[1:])
