# G1 收敛实测报告

G1 **blocked**；T08 **not_started**。本轮新增冻结模板0、正式发布产品0、真实P0通过产品0；案例修订新增0、应用记录新增0，复用原共享案例1份。原旧候选仍为draft/uncertain，不计作正式模板。

停止依据为 [STOP_RECORD.json](STOP_RECORD.json)、[宿主评估](G1_ASSESSMENT.json)、[正式暂停响应](pause-at-repair-limit-response.json)。宿主先在实际调用结束、队列空闲时评估，再正式暂停原计划；没有通过修改状态排除失败。宿主评估不再包含旧暂停任务导致的queue_not_quiescent，当前计划的paused是本次明确停止动作。

## 已完成的实现与验证

- 修复浅历史CI，保留历史来源断言；统一current-required合同、coverage映射、精确repair scope与案例目标适配。
- 聚合修订先检查作者字段，越界保存原提案及明确还原反馈；使用正式修复计费。冻结前范围与独立语义门禁、冻结后独立审阅保留。
- 实现append-only单产品授权、一次窗口激活、原子取代/恢复。普通retry拒绝已被取代的旧任务，保留普通取消重试及旧库兼容。
- 修复外层coverage返回格式。严格原交付恢复核对没有放宽来源字节比较；实际重试因宿主JSON键序漂移走正常计费生成，偏差已记录，未声称复用了旧CLI返回。
- 独立浏览器执行器补充真实分类管理、移动、搜索、计数、错误与恢复；修正恢复表单应从回收站读取的路径。原machineplan摘要未改。

最终本地完整检查见 [trash-adapter-final/checks.json](verification/trash-adapter-final/checks.json)：13项全部通过，571后端（8项原有可选skip）、9前端单元、17默认E2E、27工厂E2E、20严格Docker（0skip）；源码摘要c5084b5b37c04b32ff0b218c5b08d4484ad8dc00675b918ccbe4883683ad1ae2，执行期间无漂移。此前失败记录保留。npm原有2项moderate告警保留，未作无关依赖升级。

[独立执行器fixture](verification/trash-executor/checks.json)实际运行Chromium，覆盖仅回收站呈现恢复表单、控件缺失和无效提交，恢复通过HTML表单而非API。它没有运行生成应用，不能充当phase proof。新adapter SHA为aac08fb0bed2f77b4f2f6388205659e38cb97ad6168d77eea2e0adc24f56b488；runner SHA为7dfa5cc10d61adde10178818d5e161bec5f79261cf552d45857ba9065d0bb508；machineplan仍为5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a。

代码提交76db363的远端完整CI已实际通过：[39247348464](https://github.com/liamamilin/atlas/actions/runs/39247348464)，原始记录见ci-recovery-fenced-*。包含回收站执行器最终修复的784dedc9e27f53325a5774bb8f599b5546d25922已再次远端全部通过：[39252090447](https://github.com/liamamilin/atlas/actions/runs/39252090447)，两job及必要步骤均success，包含真实Chromium正负控；原始结果和日志为ci-final-*。后续提交仅归档这次CI与截图，源码/执行器摘要保持一致。

## 本轮真实生产结果

保留原campaign `atlas-v1-first-production-2026-10-19`、plan `plan_87059846caf345d2b2fe690657cf324f`、product `product-c42848f63251507bd9d911a5`。原job_4f30…正式取代为job_a53c47f3694047489c4f82cfc2e346be，旧错误、计数和检查点保留。

| 步骤 | 实际结果 |
|---|---|
| 共享案例及目标适配 | 原案例r1及29条观察保留，新的case-adaptation-aggregate-v1完成 |
| 第3轮聚合规格 | 首次完整CLI交付因coverage位置不匹配失败；原始返回留存 |
| 同job attempt2 | 来源JSON值相同但键序改变，严格恢复拒绝；重新生成计入第45次CLI |
| 第4轮内部修复 | 原提案额外增加limits文字，宿主拦截；正式精确补丁恢复基线，未静默改写 |
| 独立规格预审 | scenario_scope、product_completeness、architecture_contract、decisions_defaults、runtime_protocol通过；phase_acceptance阻断 |
| 新验收程序、语义审阅、冻结和完整独立审阅 | 因规格阻断未进入；旧程序只作为基线输入 |
| 发布、标准交接被实际消费、真实P0、独立运行、phase proof | 未执行，无通过记录 |

当前提案与旧attempt1严格分开保存：[repair-4](repair-4/)是当前plan-1及六项原始预审；[repair-3](repair-3/)保留旧交付与恢复偏差。旧attempt1中的HTML新归类歧义不属于当前plan-1，未移植为当前阻断。

具体阻断见 [phase_acceptance原始结果](repair-4/reviews/blueprint-spec-review-1-phase_acceptance/result.json)：A04承诺验证非法归类名称，但p0_organize的文件计划遗漏空名/超长名的invalid_name分支；A12的文件计划把归类管理表单与保存/移动表单混为invalid_category，违反架构中管理表单应为invalid_name的合同。不能在该计划下继续作者程序、忽略否决或重试换出passed。

宿主G1阻断为：正式目录准入未达、模板审阅未通过、真实开发交付检查点缺失、P0运行缺失、标准交接导出缺失。没有新的冻结artifact或可供发布的合格版本。

## 限额与时间

累计52/500次受控CLI会话，活动0；书签业务修复4/4，其他产品仍2。原42次调用和2轮修复全部保留。新增会话依次为案例适配、首次生成、键序漂移后的生成、内部精确补丁、六项规格预审，共10次；不能将CLI会话数解释为底层provider请求数。实际模型身份、provider请求数和可靠货币费用仍为unknown。

amendment `bamd_9378738d1e274c409f756d92ec9c2ac5` 在1792408423.754534激活一次；有效截止1792437223.754534，即北京时间2026-10-20 03:13:43.754534。原start/deadline均保留。当前停止原因是修复额度，未重置或再次延长窗口。

## 案例与首批

[案例增量](catalog-after.json)与起点逐项对照：规范案例1份、应用记录34份，均无新增。原规范案例[当前正式读取](repair-4/canonical-case-current.json)的修订摘要仍d58ca8ae…，case_basis仍a22ff1c0…，上游commit仍539881bc67099d491e8ab6f85de0f443fa7de623。静态源码观察、设计推断和文档声明不等于上游应用运行，研究成果在模板失败后仍可从应用实证复用。

[T08_STATUS.json](T08_STATUS.json)固定原书签、月度预算、多项目会议笔记，分母3，运行通过0；实际T08计划查询为空，未preview/run、未激活T08窗口。G1未通过，不能移入T08绕过失败。恢复前置与限额建议见[OPERATIONS.md](OPERATIONS.md)。

实际页面截图：[失败项](ui/formal-stop-failure.png)、[用量和未发布状态](ui/formal-stop.png)。页面批次quality汇总仍显示in_progress，不能将其作为G1通过；正式宿主评估为blocked，计划已暂停。
