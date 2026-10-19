# 本轮准备合同与恢复入口

本轮没有真实模型调用或生产启动；原 G1 仍 blocked，T08 未启动。这里的 prepared 只是宿主检查完成，不是模板审阅、发布、运行或 G1 通过。

## 固定依据与精确差分

- failed job：`job_a53c47f3694047489c4f82cfc2e346be`，attempt 2。
- `blueprint-plan-1` 的 result 摘要：`b82eaafd6126d5e21e1ccd734a590b5e8a417f51497465e72a4574ab20873894`。这不是外层 checkpoint 记录摘要，两者不能混用。
- 原生产 plan：`plan_87059846caf345d2b2fe690657cf324f`，摘要 `1f7701fbf5f52dde011dee76196b2cb01697e10190c6ad17c1273f4b5dcc3d30`。
- 案例依据：`a22ff1c065d27aecb0cee21dc6b597f5607375bc8ebc297a3451e708f4da5589`；案例适配 checkpoint result：`9175773345975665f4ea3cd4b99633fc2a375a9e8d373c295618d56a2b74afa8`。
- 宿主仅接受本轮精确补丁摘要 `76673a0a9b28bd52aab8d44208ea58a6764aa78d0d9b541af2ff41e4d237241c`。旧值比对、字段白名单及固定身份都执行；该入口不是任意规格编辑器。

`prepare-revision-request.json` 保存 old/new 补丁；`current-draft.diff` 用相同键序显示真实差异，`case-design.diff` 单列适配差异。`current-draft-plan.json` 为宿主应用补丁的结果；未替换原 checkpoint。

改动仅包括 A04/A12 的 goal、架构末尾澄清、`acceptance/p0_organize.py` 的 purpose，以及宿主生成的错误分支及其引用。角色、功能、阶段、其余用例、limits、其他文件计划和 reuse 标记保持原值。搜索适配只改第 7 项 capability/reason，保留 evidence_ids、disposition、其他适配和原案例研究。

| 操作 | HTML | JSON | 缺省与显式空值 | 错误码 |
|---|---|---|---|---|
| 分类创建/重命名 A04 | name 为名称 | name 为名称 | 省略、空、纯空白、121 字符非法；JSON null 非法 | invalid_name |
| 书签保存 A12 | category 为名称 | category 为名称 | 省略默认未整理；JSON null 默认未整理；显式空/纯空白/121 字符非法 | invalid_category |
| 书签移动 A12 | category_id 为已有 ID，先解析成名称 | category 为名称，不新增 category_id API | HTML 省略/空/未知 ID 非法；JSON 省略/null/空/纯空白/121 字符非法 | invalid_category |

有效新名称可自动创建；未知 ID 不可被当成名称创建。HTML 没有原生 JSON null；字符串 `null` 不是 null。未知 GET category 筛选仍返回空结果。失败零写入；HTML 有可读 form-error、保留输入和可重试表单，JSON 返回结构化 error。重名、默认分类保护、删除迁移、恢复、阶段及原断言意图保留。

`contract_coverage.error_contract` 含 32 个宿主固定错误分支，每个明确 transport/operation/field/value_kind/status/code、零写入、功能/用例/实现文件。coverage 的 F03/F04/F10 和 organize 文件计划均有分支 ID 引用。宿主在准备服务及 `validate_file_plan`/`validate_contract_coverage` 检查遗漏、混码、错引用；独立审阅仍要判断文本与代码是否兑现。

## 规范与审阅输入

新生成格式只要求 `{spec: {contract_coverage: ...}, file_plan: ...}`。旧的精确外层 `{spec, contract_coverage, file_plan}` 仅在内层不存在 coverage 时无损规范化；内外重复、额外字段或不合法类型不猜测。原始返回、stdout 与规范化收据分别保留。

书签指导由宿主绑定上述 scenario/product，预算及会议笔记不接收这份策略。搜索合同仅为 title/hostname/description 的大小写不敏感子串，并叠加分类。架构预审收到 CASE_DESIGN 和 CASE_ADAPTATION_POLICY；缓存身份包含适配/策略摘要，旧审阅不被当成新材料的通过证据。历史结论和 source 不覆盖。

## 真实接口与本轮已执行请求

只读准备 API（200，无队列、worker 或预算预留）：

```text
POST /api/factory/v1/jobs/job_a53c47f3694047489c4f82cfc2e346be/prepare-revision
body: prepare-revision-request.json
```

已通过同一服务 CLI 在实际库执行，并重复取得完全相同结果，见 `prepare-revision-response.json` 和 `preparation-replay-proof.json`：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli \
  prepare-revision job_a53c47f3694047489c4f82cfc2e346be \
  --request docs/template-factory/g1-preparation-2026-10-19/prepare-revision-request.json
```

下一次正式修订入口已接通，但本轮没有执行：

```text
POST /api/factory/artifacts/tpl_7f4c17e834c342e7b462e6bb8b6379e4/repair
body: formal-repair-request-NOT-EXECUTED.json
```

该请求的 `prepared_revision` 携带原始准备请求，服务重新检查 failed job、plan、case basis、checkpoint 和精确补丁；不信任客户端上传的 effective_plan。有效计划和修订后适配进入后续 job snapshot，由宿主保留未改字段，不再付费重新生成整份计划或重新做案例适配。仍需独立设计预审、限定文件生成、聚合语义审阅和冻结后审阅。prepared 修订不隐式附加第二轮业务修复。

**当前仍是 4/4，正式修订会被既有预算门阻止。** 此文件不是追加修复、重置历史、延长窗口或恢复 plan 的授权；没有自动登记新 amendment，也不执行上述 POST。后续若恢复生产，必须先有相应明确授权和正式预算处理，再调用真实接口。原截止时间、52 次调用、4 轮修复和全部失败证据保留。
