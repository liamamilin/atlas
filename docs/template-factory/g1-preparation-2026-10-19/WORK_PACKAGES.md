# G1 生产前修复准备

起点 `b1de0144858bf867fec616eec549d67d5ec17eb6`，工作区干净。此次授权仅包括本地实现、草案与回归，不允许追加额度、延长/激活窗口或真实生产。

| 包 | 交付与验收 | 证据 |
|---|---|---|
| P01 | 首次生成、持久化、重载、完整 V1 上下文重建和成功交付恢复；输入与 source 字节相同、不额外生成；篡改拒绝 | verification/recovery-paths.txt、recovery-byte-evidence.json：3 个测试，3 条正向路径均 completed/生成 1 次，负向篡改拒绝 |
| P02 | `spec.contract_coverage` 规范、无歧义旧格式兼容、书签指导绑定身份、架构审阅消费适配依据 | test_factory_scenario_policy、test_factory_context_recovery_v1；预算/会议隔离、缓存绑定、内外格式恢复 |
| P03 | 绑定当前 plan-1 摘要的宿主受限补丁；A04/A12、格式/名称/ID/缺省/空值区分；保留其余规格 | prepare-revision-request/response、current-draft.diff、current-draft-plan；精确补丁摘要钉住，原字段由宿主保留 |
| P04 | 覆盖矩阵有明确错误分支/用例/功能/文件引用；模型预审前拒绝漏项、错误码混用 | 32 个宿主分支；实际 produce 代理 spy：混码、漏分支、漏文件引用均 error_contract_invalid，模型调用为 0 |
| P05 | 当前搜索适配只对齐标题、hostname、描述；不修改案例研究 | case-design.diff 仅第 7 项 capability/reason；案例库逻辑表摘要未变 |
| P06 | 正式只读准备服务、接口/请求和后续修订消费接口；预算保持原约束；独立复核和回归 | 只读服务真实库重复结果一致；临时库正式 queue_repair 4/4 拒绝且回滚；produce 消费计划不重新生成；完整检查与独立复核见 DELIVERY |

`production-before.json` 是只读 SQL 和历史文件摘要。结束后再次比对：原 campaign 52 次调用、4 轮修复、原窗口、failed job、检查点与历史失败必须保留。测试使用临时库与假 CLI，不冒充真实模型或下游运行。G1 仍 blocked，T08 不启动。
