# 补证恢复数据与接口合同

本轮是宿主恢复机制，不是模板内容版本。原九份 R7 文件、规格、案例 r1、20 条事实与业务修复 7/7 均保持。

## 持久记录

- `tf_evidence_recovery_grant`：同 campaign/job 唯一资格，稳定 request_key、完整 prepare 提案和摘要；记录实际 `call_attempt` 与唯一 reservation。注册重放先返回原记录，不因任务/截止已变化而铸造新资格。
- `tf_evidence_recovery_grant_use`：每次原子占用的追加历史。只有可证实未启动才释放当前资格关联，旧 not_started 记录保留；started/uncertain 不自动释放。
- `tf_evidence_recovery`：同任务唯一初始恢复，保留旧状态、错误、attempt、snapshot、检查点和 event 摘要。与资格排队和 job attempt 2 在同一事务提交。
- `tf_evidence_saved_resume`：仅宿主后处理修复时，追加新源码门禁与已保存结果摘要；相同输入、已完成 reservation、有效 phase pass；不产生 CLI 资格。允许后续 attempt 消费实际 charged attempt 的结果。

新增表通过服务/现有 BudgetLedger 初始化，`call_attempt` 为幂等附加迁移；不重写原历史表或原检查点。失败事务全部回滚。旧 V1/V2/R5/R6/R7 和旧协议 grant 语义保持。

## 正式入口

CLI 模块 `template_factory.batch_cli`，显式 `--root` 与 `--pack`：

| CLI | HTTP POST | 请求 schema |
|---|---|---|
| evidence-prepare JOB --request FILE | /api/factory/jobs/JOB/prepare-evidence | atlas.evidence-recovery-prepare.v1 |
| evidence-grant-register --request FILE | /api/factory/budget/evidence-grants | {prepared_proposal,request} |
| recover-evidence JOB --request FILE | /api/factory/jobs/JOB/recover-evidence | atlas.evidence-recovery.v1 |
| resume-evidence-result JOB --request FILE | /api/factory/jobs/JOB/resume-evidence-result | atlas.evidence-saved-result-resume.v1 |

GET `/api/factory/budget/evidence-grants/ID` 读取真实资格与占用状态。prepare 无生产写入；register/recover 不启动 worker；状态读回后才 resume 原计划。未知 schema/字段拒绝。请求文件、真实响应和重放记录会归档于 operations/。

## 身份与追加审阅

完整 payload digest（含 language）、预算规范化 input digest、input.json 原始字节 SHA-256 分别记录，不能互换；提示、模型、CLI 配置、来源树、projection、案例/事实、原 CP 和 prepared 文件均绑定。重读排序后的持久 JSON 时使用原始 input SHA 校验，不能重新序列化推断原字节。

原单项和原六项总览不删除、不覆盖。新键后缀为 `-evidence-<grant_id>`；新 phase 记录旧 CP、提案、投影、grant/reservation、实际调用 attempt；新总览的 effective_review_selection 明确选择新 phase 与五个原通过项。每个维度对自身投影严格验证，六项总览对同字节补证镜像严格验证，引用不清除、不降级。blocked/uncertain/无效协议均不是通过。

CLI 启动前，在同一写事务核对 deadline、当前 job token/lease 并同时占用预算与资格；启动意图在 Popen 前持久化，启动不确定时保持占用。普通无预算 CLI 调用仍保留原真实失败摘要。
