# 有限验证的持久接续

最新宿主 `b5704bc0e883c6124b909aee85399c5ea0c03d88` 的 CI `39632490333` 已通过并经正式 host revision 激活。API 已用原生产根目录重启；18 个旧可用开发包摘要相同，真实 workflow JSON 字节和 Content-Type 正确。见 SOURCE_CI_FINAL、HOST_FINAL_REVISION_RECEIPT、ACTUAL_WORKFLOW_EVIDENCE_READ。

同一计划及验证门禁继续，未开放全量。日历真实重放为零新增调用（CALENDAR_REPLAY_FINAL.log），支出已用过的协议恢复没有重复扣费，字典和电子书失败被隔离。订阅阅读的首次独审为 needs_changes，三项合同问题仅进入一次集中内容修订，不按技术恢复抽取 pass；研究成功的 15 条观察已保存到同一共享案例。正式恢复后的开始记录在 VALIDATION_RESUMED_FINAL_HOST、START_FINAL_HOST，仍为原首次启动后的 30 天截止。

## 协调者结束后的动作

1. 读取正式 status、WorkflowService.gate/detail、实际 launchctl 和各叶子的 LATEST_FAILURE/IMPORT/DELIVERY 记录。只在原五叶子验证清单全部终态、无 repair_pending、plan paused 且 active_calls=0 时评估。仍有运行调用则等待，不启动副本。
2. 确认订阅阅读的新 attempt 是否 ready_not_run。独立审阅必须有效 passed，生成和审阅会话不同，八步输入/产物摘要吻合，download 为完成而非历史复用；标准开发包有固定案例及 HANDOFF，文件真实可下载。新产物必须是验证门禁登记之后完成，不能用旧日历替代。
3. 有至少一个合格的新 ready_not_run 时：真实重放这个新产物，检查新增调用为 0，案例身份/版本没有重复；保存回执副本。补充界面检查（原进度页），把各叶子实际结果、完整八步和下载/案例绑定、原恢复与失败隔离证明写入 WORKFLOW_VALIDATION.json。该文件使用 schema/kind `atlas.auxiliary-workflow-validation.v1`，至少有 `static_checks_passed: true`、`replay_new_calls: 0`、`resume_verified: true`、`failed_leaf_isolated: true`、真实 `fresh_ready_leaves`。布尔值必须引用已存在的运行/检查证据；不能只写布尔值代替证据。
4. 用既有正式 CLI `workflow-open-full --evidence docs/template-factory/workflow-hardening-2026-10-21/WORKFLOW_VALIDATION.json`。宿主会再次核验全清单终态和真实新产物。通过后继续原计划 `resume` 和 `start`，确认真实自动派发下一批，既有2并发/每批20和原账本生效。保存新正式 gate、实际 PID/状态、首批新调用。不要停在“可以开始”。
5. 若没有合格新产物或存在真实未解决门禁：保持 full gate 关闭，正式 pause 原计划并记录 `workflow_validation_failed` 的具体失败原因；准确报告成功/失败/未处理和各限额，不自行给任何叶子追加协议恢复或业务修订次数。一次失败不能改成 pass，也不能用旧模板充当新验证。此时完整全量并未完成。
6. 原应用运行新增始终为0，严格 G1/T08不恢复。聚合结束项和本轮证据提交推送，精确核对CI；保护未知 dashboard 文件、原应用/数据、冻结包及所有旧失败。不在运行中改已绑定宿主源码。

当前模板质量尚不能声称稳定：三个新验证叶子均遇到首次生成协议错误；字典和电子书已失败，订阅阅读尚在有限修订/复审。工作流失败隔离和计账表现与模板通过率必须分别报告。
