# 已知验收工具局限 / Known test-tool limits

独立静态审阅：7 项 passed，phase_acceptance uncertain，没有 blocked。完整 17 用例尚未运行，不能声称通过。核心产品目标不因此删减。

A08 的空库检查应在实际空库完成，不能要求应用为测试常驻隐藏空态容器。A13 的 20000 兜底不是产品长度要求；采用并记录合理的明确上限，验收按已声明上限检查显式拒绝与原有数据安全，不能静默裁剪已接受内容。A10 的 OPERATOR_CONFIRMED 只是人工声明，不是实际重启证据；应记录自有进程前后 PID、同一数据目录及 UI 读回，不能以刷新冒充重启。归类名失败和规范化变体仍需后续测试，现不声称覆盖。

These are limitations of the authored suite, not reasons to distort the product. Do not add hidden empty-state placeholders or an arbitrary 20000 limit for a test. A confirmation flag is not process-restart evidence. Retain negative behaviors, data integrity and explicit unsupported/unrun states. The separate operator will test the actual shared workflow, real process restarts, long notes and double saves.
