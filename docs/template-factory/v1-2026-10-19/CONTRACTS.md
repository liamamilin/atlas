# V1 数据、接口与运行合同

本轮支持范围：认知模板（product-blueprint），Linux Docker 中的 python-web，Python 3.12 标准库与 SQLite。认知模板交付完整资料库、当前阶段执行包和独立验收契约，不以源码量或克隆上游作为模板质量指标。P1/P2 可保留后续能力；P0 必须完成已准入场景的完整核心旅程。原 runnable-starter 模式与历史认知包仍可读取。

## 规范记录与迁移

规范业务库为 `application-atlas-production-pack/atlas/template-factory/factory.sqlite`；`atlas.sqlite` 仍是可重建分类库。`schema_migration` 的 v1 在同一事务中创建案例表和导入 33 个旧目录身份，v2 保留旧分类元数据。失败回滚，重复启动不重复导入。旧目录数据文件及 `atlas-app-catalog-v1` 引用输入不变。

| 逻辑实体 | 持久实现与身份 |
| --- | --- |
| 应用 | case_app；稳定 app_id、legacy_slug、aliases、目录分类；catalog_only 不等于研究通过 |
| 源码快照 | source_snapshot；规范仓库、完整 commit、采集策略唯一；归档/文件/许可证及 NOTICE 摘要；默认分支仅用于发现 |
| 案例研究 | case_revision；case_id + revision 不可变，研究输入摘要、范围、未知项、创建任务 |
| 场景关联 | scenario_case_link；scenario_id/revision × case_id/revision 多对多；流程支持、采用/排除范围及 evidence IDs |
| 观察 | evidence_observation；documentation、code_observation、inference、runtime_verification 分开；定位成功不等于结论审阅通过 |
| 独立证据审阅 | evidence_review；按创建时间及写入顺序选择最新意见；已拒绝观察不能作为借鉴事实 |
| 固定模板依据 | artifact provenance.case_basis、冻结 template.json 与 inputs/case-basis.json 必须一致 |
| 批次 | v1_plan 固定清单/digest，v1_execution 幂等执行；后继作业保留同 plan/campaign/product 身份 |
| 调用与限额 | tf_budget_*；调用前事务预占；无法证明未启动的调用保持计费口径占用 |

`CaseLibrary` 是工厂与应用实证的共享读取/写入服务。案例提交先于模板构造；模板失败时案例仍在 `/apps` 可查询和复用。源码观察必须匹配固定版本实际文件和行号/符号，模型不能指定正式身份或授予状态。来源阶段只读取数据，不执行上游代码。没有实际上游 run 的观察不带上游运行通过。

新增固定引用为 `atlas:case`，引用响应带 revision、digest 与独立 `atlas-case-reference-v1` 语义；旧 `atlas:app` 指纹不会因研究增量过期。引用新研究需显式选新版本。

## 生产及发布

预览固定叶子 fingerprint、场景 revision/digest、准入策略、已有案例依据、模型请求、资源限额、抽验目标。无合格案例的场景标记 case-research，而非 template_input_ready。执行在事务中再次核对输入；冲突拒绝且不写半批次、不调用模型。

研究作业先保存仓库选择与 commit，再采集源码和研究。故障重试保留 SHA 与已完成 checkpoint；显式新研究和重放不同。源路径纠正仅允许确定的 source/ 挂载前缀；无法定位的观察及依赖推断隔离保留，不编造位置。剩余观察仍须严格校验及独立审阅。原始响应和隔离凭据保留。

模型依据已提交证据提出 adopted / adjusted / new_design / not_adopted 设计。借鉴只允许最新独立审阅 accepted 的观察，未采用的拒绝证据可保留解释。完整案例记录保留事实、推断、未知和历史意见。

发布状态 draft / published / withdrawn，认知审阅 passed / blocked / uncertain / unavailable，与具体 runtime target/phase/run 分开。最新审阅请求未完成或失败时，旧 passed 不会覆盖。发布检查 expected_digest、冻结内容、canonical case basis、语义审阅和 runner 合同。reviewed / not_run 可以正式入库，但不能显示 P0 运行通过。旧包无依据时显示 legacy/unverified，不补造来源。

制品提交与后继审阅使用事务 outbox；恢复重放幂等。全局领取限制生产及静态审阅合计 2、运行 1。计划暂停/取消对当前后继批次原子传播，子任务领取再次检查父计划状态；取消撤销租约，迟到提交被拒绝。

## 正式接口

路由均为 `/api/factory` 前缀，共用既有本地服务请求防护。

| 方法/路径 | 用途 |
| --- | --- |
| GET v1/applications | 共享应用目录 |
| GET v1/cases?scenario_id=… 或 app_id=… | 案例版本、观察、审阅与关联 |
| GET v1/cases/{case_id}/revisions/{revision} | 固定版本、固定引用及相关模板 |
| GET v1/case-reference?ref=…&digest=… | 固定资料读取 |
| GET v1/scenarios/{id}/basis | 可生产性及具体证据阻塞 |
| POST v1/plans/preview | 固定计划，无模型调用 |
| POST v1/plans/{id}/run | expected_plan_digest + idempotency_key |
| GET v1/plans/{id}/report | 队列状态、质量、运行目标、限额及恢复入口 |
| POST v1/plans/{id}/pause、resume、cancel | 受控操作，不延长原截止时间 |
| GET v1/gates?campaign_id=… | 当前 campaign 的真实门禁评估 |
| POST artifacts/{id}/review | 发布/撤回，expected_digest 与说明 |
| POST artifacts/{id}/development-package | 导出标准资料/当前阶段/验收合同 |
| POST artifacts/{id}/develop | 当前审阅通过版本的 P0 开发；request_key、expected_digest、phase=P0 |
| GET jobs/{id}/delivery | 已完成开发作业的校验过应用 ZIP |
| POST jobs/{id}/verify-delivery | expected_archive_sha256 + execution_confirmed，经正式运行队列执行 |
| POST artifacts/{id}/accept | 新验证形成新 run，冻结目标与套件 |
| POST artifacts/{id}/repair | 新冻结模板版本；同规范请求重放已有 job，不免费新开修复轮次 |
| POST jobs/{id}/retry | 从原 job/checkpoint 重试；累计调用、瞬时重试及业务修复不清零 |

## 阶段交付与独立证据

标准包包含完整认知资料、HANDOFF.md、CURRENT_PHASE.json、ACCEPTANCE_CONTRACT.json，以及冻结验收程序。suite_digest 对应完整冻结 blueprint source 清单；program_inventory_digest 单独表达程序清单。API 导出不修改模板。

开发模型只收到标准交接包，按只读协议返回 UTF-8 文件和 delivery.json。宿主限制归档大小、路径和文件清单，校验 runtime 合同，不在宿主执行应用。业务修复必须引用真实失败的绑定运行及原应用；交付协议修正共享原逻辑阶段瞬时重试额度。

运行绑定包括 target_kind=generated_application、application_digest、template/artifact digest、suite digest、phase、scenario revision、case_basis digest、selected_case_ids、环境/镜像和断言日志。上传后再次变更源码、归档、receipt、套件或输入则拒绝复用。运行开始时重新检查 campaign 截止时间，不能靠排队或暂停延长。

suite_status 和 phase_status 独立。冻结套件全部通过而独立核心旅程证据缺失时，phase 仍 unverified。独立执行器在同一固定应用上验证用户入口、场景关键风险、适用的真正进程重启/并发写入等；`register_phase_evidence` 仅为宿主内部服务，核对真实证据文件、执行者身份、SHA 与目标绑定。应用上传字段及模型自报不能满足该项，也没有任意 HTTP 标记通过入口。

## 限额及恢复

同 campaign 最多 500 个可控 OpenCode CLI 会话，G1 与 T08 共用；provider 内部请求数和未证明的计量保持 unknown。每产品业务修复最多 2 轮（含规格、模板与应用），每逻辑阶段追加瞬时重试最多 2 次；新 job ID、修复版本或请求别名不清零。G1/T08 各 8 小时，从正式启动持久化，暂停不延长，调用 timeout 不超过剩余时间。

进程崩溃后，仅当宿主证明当前作业的专属 PID/PGID、可执行程序及工作区匹配并全部终止，才释放活动并发占用；已耗用会话仍计数。无法证明的结果 uncertain，不能返还调用。预算或截止时间耗尽保留检查点为 paused_budget；不自动提高限额。凭据/网络/镜像真实缺失记 blocked_external，未取得的运行证据不得通过。
