# G1 生产前修复准备交付

本轮准备已完成。**没有追加额度、延长/激活窗口、恢复真实生产、发布模板或把 G1 标为通过。** 原 failed job 和全部失败记录保留，G1 仍 blocked，T08 未启动。

## 实现与草案

1. 新建宿主上下文 JSON 使用确定键序。完整 Pipeline 回归覆盖首次生成、持久化、DB 重载、上下文重建、严格来源比对、恢复成功交付、计划 checkpoint 保存及再次恢复完成。canonical 内层、旧外层和 V1 聚合修复三条正向路径均完成，生成 CLI 仅 1 次。原 input/stdout/result/summary/source 保持不变。篡改 source 的负控被严格门禁拒绝，不用 JSON 值相等替代字节证明。
2. 新生成提示词和示例统一 `spec.contract_coverage`；无歧义旧外层兼容保留。书签规则由 exact scenario/product 绑定，预算和会议笔记不接收。架构预审接收适配与策略，报告与缓存绑定相应摘要。
3. 只读准备服务固定当前 `blueprint-plan-1` 摘要 `b82eaafd…`，宿主只接受本轮精确补丁，并保留未修改字段。A04 分类创建/重命名 name 的错误码为 invalid_name；A12 仅书签保存/移动的非法 category/category_id 为 invalid_category。HTML/JSON、名称/ID、省略/null/空字符串分别说明。
4. 宿主生成 32 个错误分支并建立功能、用例、文件计划引用。真实 produce 函数的 spy 回归确认：混码、漏分支、漏文件引用在模型预审前失败，代理调用为 0。不能以模型声称覆盖替代宿主合同检查。
5. 案例适配只对齐 title/hostname/description 搜索，保留来源版本、证据和其他设计。不重做案例研究。后续正式修订消费已检查计划/适配，不再生成整份规格；独立预审、程序与冻结审阅仍执行。

精确交付文件：`prepare-revision-request.json`、`prepare-revision-response.json`、`current-draft-plan.json`、`current-draft.diff`、`case-design.diff`。有效草案摘要 `f190b65275ab7c7136f523ba92aecde7c9392440d7676b070393e62ff9137b58`。

## 实际检查

`verification/full/checks.json`：13 项全部通过，执行期间源摘要无漂移：`a8b3d5d2b7478bd436bd3fa13a29f7dd3c4c8a7cc4cbeb4bdf03935c3dc0afd1`。

| 检查 | 实际结果 |
|---|---|
| 后端 | 587 项通过，8 项既有可选跳过 |
| 前端单元 | 9 项通过 |
| 默认页面端到端 | 17 项通过 |
| 工厂页面端到端 | 27 项通过 |
| 严格 Docker 集成 | 20 项通过，0 跳过 |
| Python/npm 审计、ruff、数据导出/生成/校验、类型检查、构建 | 全部通过 |
| 本轮聚焦回归 | 16 项及 2 个子用例通过 |
| 独立验收器原有合同测试 | Python 23 项；书签 fixture 与真实 Chromium 正负控通过 |

完整恢复证据见 `verification/recovery-byte-evidence.json`，包含首次/重建 source 文件摘要、原始交付摘要、恢复收据、checkpoint 摘要、CLI 次数和最终临时 job 状态。`recovery_proof_runner.py` 可重新执行；这是临时库/假 CLI 证据，**不是本轮真实模型或真实下游应用运行**。

独立 Sol 代码复核未发现未解决问题，范围和限制见 `CODE_REVIEW.md`。prepared 消费测试在首次独立设计预审 spy 处停止，后续真实作者/独立运行本轮未执行。

## 真实只读接口与预算状态

实际库的 CLI 准备重复结果一致；实际本地 HTTP `POST /api/factory/v1/jobs/job_a53c47f3694047489c4f82cfc2e346be/prepare-revision` 返回 200，结果与 CLI 相同，见 `prepare-http-proof.json`。本地 API 和页面已恢复运行，生产仍暂停。

`production-unchanged-proof.json` 确认所有 31 张逻辑表及 15,742 份 job/artifact 历史文件摘要均未变：原 campaign 52 次调用、4 轮修复，原 amendment/截止时间不变，当前 job 仍 failed。案例库、应用实证与历史 checkpoint 也包含在此只读比对中。

下一次真实修订的接口、请求和恢复前提详见 `CONTRACTS.md`。`formal-repair-request-NOT-EXECUTED.json` 已接入现有 artifact repair 服务，但本轮从未发送。临时库使用既有 2→4 amendment 和 4 次历史修复，正式 queue_repair 实测返回 budget_repair_limit 且队列/账本回滚。当前实际 4/4，因此不会自动执行；不得通过新 job、重试或更改窗口绕过。

后续顺序保持：有明确授权并通过正式预算处理后，消费精确补丁 → 独立预审 → 限定程序生成/语义审阅 → 冻结 → 独立冻结审阅 → 正式发布 → 标准交接实际消费 → 真实 P0/独立运行/phase proof → 宿主 G1 评估。此次准备完成不代替任何后续通过证据。
