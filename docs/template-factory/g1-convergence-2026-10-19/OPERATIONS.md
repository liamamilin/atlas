# 本轮受限恢复操作

以下命令使用与 HTTP 相同的正式服务。CLI help 和临时库真实恢复集成测试已执行；实际生产登记、激活及后继响应将在本目录单独保存。不得把临时库测试记录当生产记录。

生产根沿用 `application-atlas-production-pack/atlas/template-factory`，保留整个目录及原 campaign。运行前必须在仓库根执行，已安装环境和原 provider 配置保持不变。

## 前置与登记

必须先完成最终本地完整检查及同一新提交远端全部检查；不要用 `verification/final` 的第一遍失败记录替代后续修复后的通过记录。仅在真正准备恢复时登记真实用户授权：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli amendment-register --request docs/template-factory/g1-convergence-2026-10-19/amendment-request.json
```

对应 `POST /api/factory/v1/budget/amendments`。登记只追加本次授权，不激活窗口、不扣调用或修复。源摘要必须匹配用户实际提供的续作附件；未发生管理员点击或其他授权事件。

## 正式恢复

从实际登记响应取得 amendment ID，以原暂停 job 的实际 `blueprint-plan-0` 检查点计算完整记录摘要，再将本目录固定的 `repair/aggregate-repair-request.json` 作为 `repair` 值构造 `resume-request.json`。完整字段：`old_job_id`、`artifact_id`、`expected_digest`、`checkpoint_name`、`checkpoint_digest`、`amendment_id`、`idempotency_key`、`repair`。服务验证全部固定身份及依据。

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli resume-product plan_87059846caf345d2b2fe690657cf324f --request docs/template-factory/g1-convergence-2026-10-19/resume-request.json
```

对应 `POST /api/factory/v1/plans/{plan_id}/resume-product`。该事务一次性激活最多八小时补充窗口、扣第3次业务修复、入队后继、撤销旧任务 token 并保留原 error、追加 supersession 及恢复父/相关子批次。任一步失败全部回滚。重放同一幂等请求返回原后继，不重复计费或延期；scope/依据/检查点改变则拒绝。实际 `resume-request.json` 仅在真实登记成功后生成，不能填造假的 ID。

普通 `retry`、batch `resume` 不能替代该操作或重置额度。第4次确有必要的业务修复仍须引用真实失败，走已有正式 repair；到达4次或有效 deadline 时停止，不追加授权。

## 观察和运行

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli report plan_87059846caf345d2b2fe690657cf324f
```

`GET /api/factory/v1/budget/amendments?campaign_id=atlas-v1-first-production-2026-10-19` 同时返回基础账本和授权记录。真实 runtime job 的 `GET /api/factory/v1/jobs/{job_id}/effective-budget` 返回宿主绑定快照；独立执行器保存该原始响应并固定文件 SHA-256，参数必须与实际 campaign/plan/product/segment/job 一致。G1 用合法激活后的有效 deadline；T08 只能用自身 base deadline。

独立执行器 help 已实际运行；完整调用须等正式提交、runtime binding 和 suite/application 摘要存在后构造。不得用 fixture、旧应用或自造 target 提前登记 phase proof。

## T08

仅宿主重新评估 G1 真正 passed 后，使用原 `docs/template-factory/v1-2026-10-19/t08-request.json` 正式 preview，保存新 plan/digest 后用稳定幂等键 run。固定书签、月度预算、多项目会议笔记三个分母；不替换失败样本，不扩大到十个。全局500和其他产品2轮不变，T08首次正式运行开启自己的八小时窗口。

## 已发生的第3轮及协议恢复

本次实际 amendment 为 `bamd_9378738d1e274c409f756d92ec9c2ac5`，已在正式 resume-product 时激活：1792408423.754534，截止1792437223.754534（北京时间2026-10-20 03:13:43.754534）。不得再次登记/激活以延期。旧任务已正式取代，新任务 `job_a53c47f3694047489c4f82cfc2e346be` 的 attempt1 完成案例适配及生成CLI交付后，被宿主 coverage 外层/内层不匹配拒绝；44次调用、3轮修复，父plan已正式pause。

协议修复完成并取得新代码完整本地/远端通过后，可通过已有 `POST /api/factory/jobs/job_a53c47f3694047489c4f82cfc2e346be/retry` 入队同一任务，再用原plan正式resume。此处普通retry仅恢复这个 failed 后继，不能复用为 paused_budget 的通用恢复，也不能再调用首次 resume-product。恢复 receipt 必须证明旧生成交付的完整input/source/model/stdout/result均匹配；原CLI已收费，不退款、不重复生成。严格源树只读恢复核对见 `repair-3/recovery-readonly-check.json`，它不代表实际重试已执行。

若早期scope检查发现原提案越界，保存精确还原反馈后使用既有index1业务修复，占用第4轮。达到4后不允许额外模板/内部规格/应用业务修复；瞬时协议重试也不重置历史。停止时保留正式状态和原失败，不能通过改job身份继续。

## 本轮最终停止与恢复边界

已正式停止：原后继attempt2为failed（cognition_design_blocked），原plan为paused；六项预审五过一阻断，52/500次CLI、4/4轮业务修复、活动0。原失败、窗口和全部身份保留，T08尚未preview/run。具体不一致及全部raw见G1_REPORT、STOP_RECORD和repair-4；新模板/P0/phase proof未取得。

现在可执行的只读检查：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli report plan_87059846caf345d2b2fe690657cf324f
```

API的`GET /api/factory/jobs/job_a53c47f3694047489c4f82cfc2e346be`及`GET /api/factory/v1/jobs/job_a53c47f3694047489c4f82cfc2e346be/effective-budget`可核对失败与原有效截止时间。生产根整个目录应保留（含DB/WAL、jobs、源快照、制品、检查点），仅复制报告不能恢复业务库。

当前没有获授权的第5轮执行命令。普通retry会复用已有blocked预审，不能改规格、抹掉否决或增加修复额度；再次调用首次resume-product也不会获得新窗口。现有amendment实现只接本次2→4的唯一例外，不能编造更高的register请求。

若后续另有明确追加授权，先在原append-only服务中支持该明确增量并验证历史/并发/时间边界，再通过正式新修订绑定本次failed job、plan-1和phase_acceptance证据。最小业务修正为：A04程序计划补创建/重命名空名与121字符名的invalid_name、form-error、无写入断言；A12仅处理保存/移动category字段的invalid_category，不把归类管理表单混入。保留全部原断言及本轮URL政策，不能通过改变case、阶段或更换样本避开失败。随后仍须完成预审、五程序修订、精确差分语义审阅、冻结后独立审阅、发布、标准交接真实消费、P0、独立运行/proof及宿主评估。窗口到期后需要相应明确时间授权；不自动延期。

G1实际通过后才启动原三个场景的T08；本次未授权或排队其他候选。限额建议是先处理这一个确定根因，保持全局500、并发2/1和其他产品2轮，不清零历史、不预先扩到十个。

后续生产前还应修正宿主源JSON的确定性渲染：本轮ACCEPTED_CASE_FACTS/CASE_DESIGN首次返回与检查点重载仅键序不同，导致严格raw恢复保守拒绝并多用一次CLI。当前没有放宽源字节门禁；正式checkpoint复用与累计记账保留。后续应以真实V1首次生成→持久重载回归验证稳定渲染，不能把本轮局部只读rehearsal当作该完整路径已通过。

页面的`quality=in_progress`是批次汇总，`limits.product_repairs=2`是不可变基础额度；原书签有效4轮及新deadline在amendments中。正式G1结论以G1_ASSESSMENT为blocked为准。后续UI应更直接显示宿主门禁与有效额度，避免将基础值或汇总进度当成通过结论；本轮截图保留实际表现。
