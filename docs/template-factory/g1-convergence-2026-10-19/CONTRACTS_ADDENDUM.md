# 收敛实现合同增量

本文件记录已实现接口与数据边界；实际执行状态以G1_REPORT和原始响应为准。它不声明模板或应用运行通过。原共享案例、旧引用迁移及下游交付合同见[原CONTRACTS](../v1-2026-10-19/CONTRACTS.md)。

## 数据与迁移

- `tf_budget_amendment`：追加保存授权来源摘要、固定campaign/product/plan、原/新修复上限、幂等键、版本、原deadline、窗口及创建/激活时间。基础额度与原调用/修复行保留；普通配置不得提高额度。
- `tf_job_supersession`：保存旧/后继job、plan、理由、旧state/error/stage/attempt/更新时间。取代只终结旧job，不取消整个计划。旧token失效，普通retry以409/job_superseded拒绝重排旧job。
- 初始化采用已有库的幂等schema迁移，旧库首次登记可用；普通retry兼容没有supersession表的旧库。没有手写SQL改生产结果。
- 共享案例revision、case_basis、source commit、观察及引用不可变；新目标适配保存在正式case-adaptation-aggregate-v1输入/检查点中，不修改案例。研究失败或模板失败不删除已入库研究。

## 正式接口

| 接口 | 边界 |
|---|---|
| POST `/api/factory/v1/budget/amendments` | 本轮仅原书签2→4；登记不激活，原42/2基线保留，幂等重放不叠加 |
| POST `/api/factory/v1/plans/{plan}/resume-product` | 校验原paused_budget任务、旧候选/摘要、检查点与精确scope；原子激活一次窗口、扣第3轮、取代/入队及恢复父/子批次 |
| POST `/api/factory/jobs/{job}/retry` | 仅既有可重试终态；不能恢复paused_budget或superseded旧job，不能清零累计限额；本轮attempt2保留原job身份 |
| GET `/api/factory/v1/jobs/{job}/effective-budget` | 宿主校验固定campaign/plan/product/segment，返回原/有效deadline及授权来源；G1例外不传播到T08 |
| POST `/api/factory/v1/plans/{plan}/pause` | 正式暂停原计划；本轮停止响应单独保存，不将失败job改成成功 |
| `BatchService.assess_g1(plan, manifest_path)` | 宿主核对真实队列、固定案例、目录、审阅、交付、运行、独立proof及13项源码绑定检查；manifest布尔值不能授予通过 |

现有amendment服务刻意只支持本次唯一授权，不是能任意提升到5或更高的通用接口。已经激活的补充窗口不会被暂停、重试或重启延长。

## 生产与审阅合同

- 规则版本`atlas.current-required-contract.v1`；coverage schema为`atlas.contract-coverage.v1`。每项current-required P0功能关联design_basis、entry、action、success_state、navigation、failure、recovery和acceptance_ids。宿主检查引用/类型/版本，独立模型检查实际语义。
- 范围版本`atlas.aggregate-repair-scope.v1`；本轮固定17条作者路径和5个程序路径。作者越界在规格预审/程序生成前拒绝，生成完成后再核对程序差分。只有A02单标签hostname负例转正获得既有断言语义替换授权。
- 来源事实、目标设计、规格预审、冻结候选审阅、发布、具体目标运行分别保存。预审通过不能替代冻结后审阅，发布不能替代真实运行。
- 外层coverage仅作无损、无歧义兼容，保留raw及normalization receipt。已交付结果恢复要求相同job和阶段、完整input/source/model及成功CLI/原stdout/result核对；实际键序漂移拒绝复用，已记录新增调用。
- 独立预冻结语义审阅绑定baseline、scope、作者字段和程序精确差分；结构有效否决先持久化，再拒绝。普通重试不能抹掉否决。

## 交接与运行

标准`develop`路径从正式development-package接口导出并下载handoff.zip，实际消费的archive/digest进入development-export与application-delivery检查点。P0交付必须含真实application.zip及正式delivery receipt；runtime绑定template、suite、app_root、scenario、case_basis和phase；独立执行器验证同目标、network none、无发布端口、同容器真实重启、全部确认写入和清理，再由宿主登记phase proof。

上述下游路径本轮没有执行。本轮phase_acceptance否决在新程序作者之前生效，因此没有新的交接包、应用归档、运行结果或proof。执行器只取得fixture证据，版本摘要见verification/trash-executor，原machineplan不变。
