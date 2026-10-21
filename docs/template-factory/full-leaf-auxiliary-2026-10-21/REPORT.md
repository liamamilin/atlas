# 可靠 workflow：已部署，有限真实验证继续

八步持久 workflow、受限恢复、失败隔离、门禁和只读进度页已实现。宿主收尾源码 `b5704bc0e883c6124b909aee85399c5ea0c03d88` 已通过 CI 39632490333，并经正式 host revision 激活。5199 API 已按用户授权使用原生产目录重启；健康检查、18 个旧可用开发包摘要、真实 JSON 文件字节与 text/plain 类型全部通过。日历完成项再次重放新增调用为 0；123 个保护文件摘要未变。

当前仅派发五叶子验证清单，**全量门禁尚未开放**。最新检查点新增 CLI 20，历史累计 119，活动 1；实时情况以正式 status 和 PROGRESS.json 为准。冻结范围 1805，原复用 18，现有新增日历模板 1；字典、电子书与旧即时通讯、支出失败保留。订阅阅读首次完整独审发现三项合同问题，原授权内集中修订已从 attempt-2 自动启动，尚未取得新复审或入库通过。

新研究已新增 2 个共享案例身份、3 个版本，原 19 个案例版本保留。订阅阅读研究的 15 条已接受观察可独立复用，模板仍需修订。新增应用运行 0，严格 G1/T08 不变。

实时进度入口：`http://127.0.0.1:5188/factory?view=workflow`。后台任务为原 launchd 单协调者，原 7200 新增/每叶子 6 次/并发 2/30 天窗口均保留。唯一订阅阅读内容修订结束后按 [持久接续说明](../workflow-hardening-2026-10-21/VALIDATION_FOLLOWUP.md) 评估真实门禁；合格新产物通过后才正式开放并实际继续全量，否则准确暂停。

详细验收见 [工作包](../workflow-hardening-2026-10-21/WORK_PACKAGE.md)、[本轮检查点](../workflow-hardening-2026-10-21/CHECKPOINT_AFTER_RESTART.json)、[重启与下载证据](../workflow-hardening-2026-10-21/ACTUAL_WORKFLOW_EVIDENCE_READ.json)、[操作说明](OPERATIONS.md)。后台每 30 秒更新的 PROGRESS/RESULTS/CALL_LEDGER 是现场状态；提交中的快照只代表各自 observed_at。未把排队、生成文件、fixture 或静态审阅当作应用运行通过。
