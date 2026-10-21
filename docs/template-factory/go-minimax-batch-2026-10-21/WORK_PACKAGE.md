# MiniMax 三叶子辅助生产验收对照

- [x] 模型参数化、历史 DeepSeek 检查点兼容、9次原子上限回归：HOST_TESTS.log、HISTORICAL_REUSE.json。
- [x] 三个不同叶子/场景在调用前固定：BATCH_REQUEST.json、REGISTRATION.json。
- [x] 看板研究→固定源码→生成→新独审→辅助入库及真实下载：personal-kanban/IMPORT_RECEIPT.json、REAL_API_RESULTS.json。
- [x] 支出真实执行，来源检查失败保留，其他项继续：daily-expenses/FAILURE.json；未审阅/入库，不算通过。
- [x] 日历真实研究，协议失败保留：personal-calendar/FAILURE.json；未固定源码/生成/审阅/入库，不算通过。
- [x] 实际幂等重放，0新调用/案例/制品：REPLAY_RESULT.json。
- [x] 原17份包、18个案例版本、六份应用数据及严格历史保护：REAL_API_RESULTS.json。
- [x] 真实调用、失败、来源、审阅摘要与限制汇总：REPORT.md、USAGE.json。

本轮完整成功1/3，累计99/500；不是3份模板通过。提交、推送及精确源码 CI 结果在最终交付附 GitHub SHA/链接；未取得远端通过前不将其视为通过。
