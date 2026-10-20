# 冻结独审恢复工作包与验收对照

本轮仅恢复 job_b01427592b164863aab5bedf7b3863bb。授权原文件已保存，SHA256 为 65976f3c72613dfc7208d86cea7ce4c9ec0688ef04c881efba8abacf7f642101。原候选、payload、source 与九份交付程序不得改变；呈现、prompt 末尾与只读权限增量单独绑定。业务修复 7/7、CLI 80/500 起点、历史资格保留。

| 工作包 | 验收边界 | 证据入口 | 当前状态 |
|---|---|---|---|
| F01 基线与授权 | 正式读取任务、预算、旧 unavailable、快照与原文件 | BASELINE.json、authorization/ | 已核对 |
| F02 无损阅读材料 | 全部实际长字符串、六份程序差分、原始 SHA 与 round-trip、确定派生 | READABILITY_MANIFEST.json、test_factory_frozen_materials.py | 已实现，fixture通过 |
| F03 提示及 ACL | 原 prompt 字节前缀、严格只读清单、原引用校验不放宽 | PROMPT_AND_PERMISSION_DELTA.json | 已实现，fixture通过 |
| F04 一次性恢复 | 类型隔离、幂等、同 job 1→2、原子占用、lease/启动/消费 | test_factory_frozen_link.py、test_factory_frozen_recovery_contract.py | 已实现，fixture通过，正式执行待门禁 |
| F05 提交与只读续交 | 原失败保留、合法交付与精确 attempt、禁止第二次模型 | test_factory_frozen_saved_result.py | 已实现，三项fixture通过 |
| F06 代码门禁 | 必要回归、13 项检查、精确源码 CI 两项成功 | verification/、ci-source.json | 完整13组已通过，远端精确SHA CI待提交/核对 |
| F07 真实恢复 | 最多一次 1800 秒；启动余量至少 2700 秒 | operations/、actual-attempt-2/ | 未登记、未运行 |
| F08 下游 G1/T08 | passed 后才发布、实际标准交接及真实 P0/独立运行；宿主 G1 后 T08 | DELIVERY.md 或 STOP_RECORD.json | 条件未满足 |

绝对截止为北京时间 2026-10-20 19:21:52.855422，最迟真实启动时间为 18:36:52.855422。时间不足时不登记/入队/启动，保留未启动证据；不增加窗口或业务修复。Fixture 与真实证据分别报告。
