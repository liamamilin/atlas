# 冻结规格与验收程序修订合同

本轮复用现有 `prepare-revision`、`amendment-register`、`resume-product` 和 `resume`，不为 R8 新建队列或 author。原附件及用户授权的原始 SHA 见 authorization/RECORD.json。

| 正式入口 | 请求/效果 |
| --- | --- |
| `POST /api/factory/jobs/{job_id}/prepare-revision` / `batch_cli prepare-revision` | `atlas.frozen-plan-revision.v1`；完整实际请求为 prepare-request.json。验证最新冻结独审、acceptance、源码归档、producer 四份检查点、已确认事实/案例、受限补丁及九文件字节，不扣调用、修复，不启动窗口。 |
| `POST /api/factory/budget/amendments` / `batch_cli amendment-register` | `atlas.budget-amendment.v3`；来源原文件、精确源码/原始 CI、prepared 输入及所有摘要、limits 与 supersedes 时间来源必须匹配授权。存储 version=5 的惰性追加记录；不消费修复、不启动窗口。 |
| `POST /api/factory/plans/{plan_id}/resume-product` / `batch_cli resume-product` | `atlas.product-resume.v4`；同一写事务复核基线、激活新时间/上限、扣唯一第8次修复、入队唯一新 producer、保存前驱关联及幂等回执。父计划和子批次保持 paused，旧 blocked job 不改写。任一步异常整笔回滚。 |
| `batch_cli resume plan_87059846caf345d2b2fe690657cf324f` | 核对已激活作业后正式恢复原计划，使用现有 worker。新 producer 没有 author 生成；六项新输入预审、聚合、冻结独审按现有预算及历史重试规则执行。 |

规格仅可变 `architecture_markdown` 与 A03.goal；宿主保留其余 authored 字段。file_plan 允许同步九文件 reuse，purpose 只可改四份 replace。四文件 after SHA 与 prepared-programs 实际字节一致，其余五份直接复用 predecessor；精确前后清单见 program-manifest.json，规格/文件计划差分见 SPEC_AND_PLAN.diff。旧 schema 保持独立分派，不能冒名承载新修订。

预审中 phase_acceptance、architecture_contract、runtime_protocol 接收实际九文件 before/after、manifest、来源授权、原 blocked 报告及有限一致性材料；六项均以实际新 spec 输入身份决定首次/复用/重试。聚合材料还包含原始可读程序 diff 与架构，冻结候选在 inputs/frozen-revision 留存相同静态依据。静态检查不替代真实运行。

登记不计时。成功事务的 `activated_at + 86400` 明确替代已绑定的旧时间来源，旧 grant/time_resume 不删除；幂等重放不延长。external=1 独立累计，factory 与 external 共用500上限；所有 reserved/spawn_intent/started/uncertain 都算活动。T08 仍按原阶段首次8小时，不继承书签特殊 G1 时间及其他产品以外的修复上限。独立执行器接受同一正式预算上下文的 amendment_superseding_timing 并验证其父时间、授权及24小时关系。

本轮请求模型固定 opencode-go/deepseek-v4.1-flash，language=zh，timeout=1800，repair_attempts=0；实际 provider 模型无法观测则 unknown。author=0 只适用于模板修订，后续首次真实 P0 开发是另有正式预算的正常调用。旧追加重试2/2、已消费 grants 和历史账目不重置。
