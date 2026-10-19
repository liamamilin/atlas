# Atlas 模板工厂 V1：工作包与验收对照

用户任务日期：2026-10-19。输入：`ATLAS_TEMPLATE_FACTORY_V1_CODEX_INSTRUCTIONS.txt`，按完整 T01–T08 执行。参考与实际起点均为 `d0a206dd749e866619379e152b26a880d1d3c104`，初始工作区干净；不重置历史。

## 固定交付边界

主链：叶子 → 固定场景 → 真实源码快照 → 共享案例版本/证据 → 认知构造 → 独立审阅 → 正式目录 → 阶段包 → 下游运行。

首期认知运行支持 **python-web（Python 标准库/SQLite，Linux Docker）**；现有其他 starter/runtime profiles 保持兼容，但不宣称本轮认知 G1 覆盖。生产继续 OpenCode CLI，默认 `opencode-go/deepseek-v4.1-flash`，不静默切模型。环境/凭据不进入模板。上游源码只读取，不在来源阶段执行。独立静态审阅不等于任何目标的运行通过。

案例库使用 `factory.sqlite`，不写可重建的 `atlas.sqlite`。旧33个应用保留目录身份、slug、引用指纹；新增 `atlas:case` 固定版本引用。旧认知模板保留原字节，缺失案例依据显示 legacy/unverified。发布与审阅、具体目标/阶段运行分轴，发布使用 expected_digest。

G1 与首批共用最多500次可控 CLI 会话；provider 内部请求数/费用未知。生产并发2、运行并发1、单产品业务修复最多2轮、同项同阶段瞬时追加重试最多2次。G1/T08生产各最多8小时，从各自正式启动时固定截止时间，暂停不延长。已有更低配置优先。不足即保留检查点，不抬限额。首批最多10个不同场景产品，含G1；至少3个不同场景抽验在看结果前固定。G1未通过不得启动首批。

## 工作包

| 包 | 交付与验收 | 当前状态/证据 |
| --- | --- | --- |
| T01 | 基线、数据/资源/发布合同，真实环境，隔离配置与浅克隆测试 | 已核对；实际基线 d0a206d、初始干净；[合同](CONTRACTS.md)、[环境/CI](verification/local-ci.md) |
| T02 | 版本迁移、33应用、共享案例、多对多、旧引用、固定版本、回滚 | 已实现并专项验证；迁移 v1/v2，12项案例合同测试；旧资料指纹保持 |
| T03 | 实际发现/固定SHA/源码研究/独立证据审阅/事务提交 | 真实书签案例已完成并可从应用实证读取；[规范记录](g1-real-sample/case-record.json)、[固定引用](g1-real-sample/fixed-reference.json)；其他场景尚未生产 |
| T04 | 固定案例输入、结构/语义审阅、认知发布/撤回/修订/目录 | 代码与专项合同已接通；本轮书签候选 tpl_7f4c17e834c342e7b462e6bb8b6379e4 已冻结（digest 8d9229d3895b…），独立审阅返回 uncertain（URL/畸形JSON合同待澄清），尚无正式发布或下游通过；[实际冻结内容](g1-real-sample/template-8d9229d3895b/manifest.json) |
| T05 | 标准导出/导入、阶段必要证据、真实P0、来源/套件绑定 | 服务、API、合同与独立执行器已实现；当前真实下游尚未生成/运行，保持未通过 |
| T06 | 固定预览、幂等、预算、累计计数、恢复、报告、四处UI | 已实现；跨worker、outbox、预算竞争、取消/暂停、请求重放专项测试；已补无本地缓存的计划深链恢复、逐目标运行状态回归；前端专项定点与最新完整27项均通过 |
| T07 | 全量离线、工厂E2E、必要真实Docker、G1机器与可读报告 | [当前源码完整门禁通过](verification/FINAL_CHECKS.md)：后端545项（537执行通过/8已知可选skip）、网页单元9/主线17/工厂27、严格Docker20零skip；source_changed=false。失败及修复过程归档保留；真实G1样例受质量与业务修复上限阻断，已正式评估未通过 |
| T08 | G1后自动启动固定最多10产品；预定3场景运行抽验/首批报告 | 未启动；[3个预定抽验场景](SAMPLING_PLAN.json)，不替换失败场景、不降低门槛；G1通过后按同campaign剩余额度启动 |


## 必须逐项核对的证据

1. 迁移数量/旧指纹/重复/回滚；案例与场景双向多对多。
2. 场景、源码或研究更新不改旧模板依据；预览冲突零调用零半批写入。
3. 应用实证/模板同case revision/evidence digest；模板失败仍能读取案例。
4. 声明、代码观察、推断、上游/下游运行不互相升级；错误引用/摘要/审阅禁止发布。
5. 制品与后继审阅恢复、lease fencing、多worker、取消迟到、预算竞争。
6. 新job/retry/repair不重置预算；新验证新run，目标/套件变化不沿用旧通过。
7. 程序通过但必要证据缺失不算阶段通过；队列终态与质量结果分开。
8. 浏览器场景→案例版本→证据→模板→阶段导出；旧应用加入项目保留。

## 基线环境与执行记录

- OS Darwin arm64；Python3.10.13，Node22.21.1；Docker CLI28.3.2。
- OpenCode普通沙箱版本探测因日志目录不可写报EPERM，尚不能作为provider不可用结论；后续使用获授权执行范围探测。
- README、PROJECT_STATE、工厂计划/认知设计/指南/验证、Sol/Luna约定已读取；PROJECT_STATE中的U17远程签名发布阻塞独立于本里程碑，不据此中止本地工厂开发。
- 开始前后端全量命令：`python3 -m unittest discover -s application-atlas-production-pack/tests`，442项、8 skip。尚未真实执行的门禁保持未通过。
- 本文件随工作包推进更新。证据、规范与摘要入Git；原始源码归档/模型工作区/运行临时文件按现有本地artifact规则保留，报告明确定位。

## 本轮真实运行定位

- campaign：`atlas-v1-first-production-2026-10-19`。G1 plan：`plan_87059846caf345d2b2fe690657cf324f`，digest `1f7701fbf5f52dde011dee76196b2cb01697e10190c6ad17c1273f4b5dcc3d30`。
- 书签场景 r2 `scn_7756e0007f6a463a97316f3f49c15248`；case `case:product-c42848f63251507bd9d911a5:faa52e6b1414` r1。
- 上游 `lakhindarpal/bookmark-manager` 固定 SHA `539881bc67099d491e8ab6f85de0f443fa7de623`；这是源码研究及独立证据审阅，不是上游运行通过。
- 研究 job `job_d59605a1fbac430e84966ff143871068` 已完成。模板 job `job_d0d9d80dc9f64dd9890fc0b728bd9a5d` 已冻结候选，后继独立认知审阅第三次取得有效 uncertain 结论，前两次provider协议错误和有限重试均保留；累计预算scope与受控规范修订已实现、专项和独立审查通过；正式第2轮修订job_4f30d0f41ce94a2cbd16ae7996fb27ab完成限定文本patch，但product_completeness与architecture_contract仍blocked；继续修订在第3轮调用前被budget_repair_limit阻止，job保留paused_budget，计划已正式pause，业务修复2/2，原deadline不变。首次独立运行协议审阅 blocked 后计入第1轮业务修正，原意见保留。审阅 JSON 协议失败及程序文件生成的 provider 流缺少 finish_reason 均使用同 job/checkpoint 的有限瞬态重试，计入调用；未更换模型或提高限额。
- 调用台账在首次模型启动前持久化；正式起点 epoch `1792389754.633465`，G1截止 `1792418554.633465`，不因恢复延长。费用、provider内部请求数、无事件证明的模型身份保持未知；原始step计量分项保留，不把重叠token字段相加。
- 实际源码归档、CLI原始会话和运行工作区保存在仓库既有本地 `application-atlas-production-pack/atlas/template-factory/`，规范记录、报告和受控摘要在本目录。未运行的证据不补造。

## 本轮停止边界

- 生产共42/500次CLI调用、活动0；停止原因是产品级业务修复2/2用尽，不能因全局余额458而续开该产品。不是当前provider不可用；此前provider协议失败与本次设计缺陷分别保留。
- 限定patch的精确变更和[阻断维度报告](g1-real-sample/repair-2/blueprint-spec-review-0/report.json)已归档。新版本未冻结；原候选仍draft/uncertain；没有真实P0应用、运行或独立运行proof。
- [宿主G1评估](G1_ASSESSMENT.json)为blocked；[批次报告](G1_BATCH_REPORT.json)保留实际队列、案例增量、用量和限额。
- [T08报告](T08_REPORT.json)明确not_started，三个抽验均not_run，不替换、不伪造通过。首批固定请求仍保留，未正式preview/run。
- 执行器与host门禁解析器的缺陷属于可继续完成的代码工作，修复/验证不会消耗生产业务修复额度，不据此重新启动模型生产。
