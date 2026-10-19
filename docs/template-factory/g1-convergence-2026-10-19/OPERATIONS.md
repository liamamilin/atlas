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
