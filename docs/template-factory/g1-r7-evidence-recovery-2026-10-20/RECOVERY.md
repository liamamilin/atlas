# 准确停止点与恢复边界

本轮一次性补证恢复已经实际执行并通过，不需要、也不能再次消费该资格。

- 原生产任务 `job_3a658ba085e8417ea6faad5cb0cdd493`：同任务 attempt 2，completed。
- 追加 phase_acceptance：passed；五项原结果完整身份一致并复用；新六项总览 passed。
- 聚合独立审阅：passed；九份 R7 文件按原字节消费，author 0；候选已冻结。
- 当前阻断任务 `job_b01427592b164863aab5bedf7b3863bb`：attempt 1、needs_review，队列最后阶段 acceptance；真正阻断的 CLI 阶段是 cognitive-review。
- 实际 failure_code=cli_timeout、600.48 秒、exit 130；没有 result.json 或最终 text 事件，没有取得有效审阅报告。不能把超时包装成语义通过或内容 blocker。
- cognitive-review 逻辑 scope 的两次历史追加重试已用完，原记录均保留。当前调用是新冻结摘要的正常首次调用，不是另一次授权重试。总额剩余 420 不覆盖阶段重试上限。

已通过正式 BatchService/CLI pause 原计划及其子批次；活动预算为 0。G1_ASSESSMENT.json 为宿主正式 blocked 结果。

## 只读核对

在仓库根执行，以下 GET 不触发模型：

```sh
curl http://127.0.0.1:5199/api/factory/jobs/job_3a658ba085e8417ea6faad5cb0cdd493
curl http://127.0.0.1:5199/api/factory/jobs/job_b01427592b164863aab5bedf7b3863bb
curl http://127.0.0.1:5199/api/factory/budget/evidence-grants/egrant_dd03245306034022bbc046e3b9428955
```

原 prepare/grant/recover 请求及真响应在 operations/。原 request_key 为 `atlas-g1-r7-evidence-recovery-2026-10-20-once`，原文件不可替换。recover 的幂等返回是历史 attempt-2 queued 回执，不能替代当前 completed 状态查询。

## 当前没有可直接执行的合法继续请求

`recover-evidence` 和 `resume-evidence-result` 只绑定原生产任务的 phase 补证；后者只用于已经保存有效 phase 结果后的宿主组合错误。它们不能恢复另一个冻结审阅任务，更不能作为新的 CLI 资格。

如后续另获明确授权，应先绑定 FROZEN_REVIEW_RECOVERY_BINDING.json 中的同一冻结审阅 job、operation、原始输入/完整 payload/预算输入/提示/来源树摘要、原失败 reservation 和候选摘要，完成适用的正式受限恢复机制与对应源码检查/CI，再进行一次受控恢复。当前不存在这样一份授权或正式请求，本轮未建立或执行它。

绝对截止仍为北京时间 2026-10-20 19:21:52.855422，未延期、未重置。不得自动延长 timeout、重建 campaign/job、换摘要/样本或借用已消费的 grant。业务修复保持 7/7；若真实内容需要修改，另需明确修订授权与正式版本处理。

合格冻结审阅、发布、标准交接实际消费、真实 P0、冻结套件、独立浏览器、精确 phase proof 和宿主 G1 passed 都仍是顺序门禁。只有 G1 passed 后才继续 T08 原三场景；未运行步骤见 STOP_RECORD.json。
