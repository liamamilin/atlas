# R7 同任务补证恢复工作包

授权原文件及 SHA-256 见 authorization/SOURCE.json；本工作包不扩大授权。

固定任务 job_3a658ba085e8417ea6faad5cb0cdd493，campaign atlas-v1-first-production-2026-10-19，计划 plan_87059846caf345d2b2fe690657cf324f。起点为 77/500 调用、业务修复 7/7、旧协议 grant 已消费 1/1。截止北京时间 2026-10-20 19:21:52.855422。

| 工作包 | 完成依据 | 证据入口 |
|---|---|---|
| E01 基线与授权 | 原文件原字节保存、摘要；原任务、预算、11 个检查点读回 | authorization/、BASELINE.json |
| E02 补证材料与六维身份 | 新 phase 使用同一九文件/23 项材料；其他五项完整身份逐字重建核验；严格引用不放宽 | evidence_views.py；真实 prepare 输出 |
| E03 一次性资格与恢复 | 正式 prepare/register/recover；原子资格占用、实际 attempt、启动不确定性、幂等 | evidence_grants.py、evidence_recovery.py；回归和正式回执 |
| E04 追加审阅与有效组合 | 原单项/总览保留；新 phase 和组合另建键；零 author；复用五项；结果落盘只复用 | cognition.py；跨模块回归、真实检查点 |
| E05 文档遗漏 | A11 参数表已知遗漏如实登记；仅未应用差分 | README_A11_ERRATUM.json、README-A11-NOT-APPLIED.diff |
| E06 门禁 | 完整 13 组、本轮精确源码 check/docker-integration | verification/full-final/、ci-source.json |
| E07 真实恢复与主线 | 正式登记/恢复、状态读回、原计划 resume、唯一 CLI；只有正式 G1 通过再 T08 | operations/、最终报告 |

开发分工按仓库 sol-luna-development 技能执行：主代理整合与恢复，Luna 分别负责资格/计账/CLI 和服务/跨模块测试，独立 Sol 审查边界。所有测试 fixture 与真实生产证据分别保存。

停止条件：唯一补证审阅非通过、真实内容缺陷需修改交付或第八轮业务修复、截止/预算/CI/外部服务门禁。保留历史，不伪造 G1/P0 或替换 T08 样本。

## 最终状态

E01–E06 完成并保存真实证据。E07 已实际恢复、补证通过、六项组合通过、聚合通过、冻结一个候选；后续冻结认知审阅超时且逻辑阶段重试 2/2 已耗尽，正式 pause。G1 blocked、T08 未启动。详见 DELIVERY.md / STOP_RECORD.json。
