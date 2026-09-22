# 执行与验收记录

状态：范围已确认；四份开发文档已生成并应用到 Atlas 工作区；三个 P1 实现决策已记录；T1–T5 已完成并通过产品验收。T1–T4 为契约文档应用，T5 为只读端到端分析；尚未接入真实供应商或模拟适配器。

## 计划中的最小任务

1. 建立三类记录的主记录与稳定 ID 契约。
2. 建立项目工作项到个人日程事件的单向交接和冲突恢复。
3. 建立交付物到客户审批请求的单向交接、退回和超时处理。
4. 建立审批结果返回项目计划的状态映射、幂等键和人工接管。
5. 导出独立开发文档包并由新会话核对范围、依赖和验收条件。
6. 评审四份已应用文档，拆解首轮可执行开发任务。
7. T1–T5 首轮以契约和只读分析完成验收；模拟适配器或真实供应商接入另立范围，不在本案例完成边界内。

## 验收条件

- 任何交接都能回答来源 ID、目标 ID、当前状态、责任人和时间戳。
- 审批批准不被误写成项目已完成；项目完成仍由工作项的明确完成条件决定。
- 审批退回、超时、重复回调和日程冲突有可见状态与恢复动作。
- 导出包不依赖当前会话，且清楚区分类型事实、项目假设、推断和待决问题。
- 首轮没有自动双向同步、自动资源排程或客户认证/计费实现。

## 实际证据

普通方案：`ordinary-output.md`；Atlas 分析运行：`gen_7c411b80bad04bbca883058301eaf1f2`；Atlas 结果：`atlas-output.json`。六项候选需求已确认并记录决策 `dec_4f086362a61446d9ad3c27abd39a9b1a`。文档生成运行：`gen_dc3d1f8c3da247619e876be60009d57c`，四份文档已应用到 Atlas 工作区；本地副本为 `generated-product-requirements.md`、`generated-technical-plan.md`、`generated-development-plan.md`、`generated-acceptance-plan.md`。


## Atlas 工作区候选需求

- `req_a8038841aea54049acda239ef0e6a5c0`（current）：明确三类资料的主记录归属：Agile PM 系统为项目交付和工作项的系统记录，Calendar 为个人时间锚点和可用时段的系统记录，Approval Workflow 为审批决定和审计轨迹的系统记录。任何跨系统引用均以引用方式链接，不复制主记录。
- `req_8d71b08faa644d9591a08e39921bac89`（current）：为跨系统引用定义稳定 ID 映射规则：审批请求 ID、工作项 ID、日历事件 ID 各自作为稳定标识符，通过关联表记录三者之间的链接关系，不合并为统一 ID。
- `req_bdc3a472862e440bb2cc5f1726ceb23d`（current）：定义审批决定到项目工作项的状态交接协议：审批通过触发工作项创建或状态推进，审批拒绝触发工作项关闭或标记，审批退回触发工作项修订。交接为单向触发，不自动反向同步。
- `req_f3a3f6d8e46a47e9b0ee0f821ad89692`（current）：定义跨系统权限边界：审批工作流中的 requester/approver/admin 角色与敏捷 PM 中的 team member/planner/team lead 角色之间的权限隔离规则，以及日历共享权限与项目角色的对应关系。
- `req_846261511acb4fd1a31d9dad57e4e71f`（current）：定义三类失败场景的恢复协议：(1) 审批请求停滞通过提醒和升级机制恢复；(2) 工作项阻塞通过看板标记和团队协调恢复；(3) 日历同步失败通过手动重新同步或事件重建恢复。每类恢复保留完整审计轨迹。
- `req_daef6b4dd9804830bc377c4317c1dd33`（current）：明确跨系统同步的取舍原则：审批工作流与敏捷 PM 之间的状态同步为单向（审批到项目），不承诺自动双向同步；日历事件与项目迭代之间为只读引用（日历显示迭代时间块），不自动创建日历事件。同步边界和例外情况需文档化。


## 文档生成与应用证据

- 产品需求：`doc_2aec9277b13b471b91e9a312fa47f368` / `dver_8911cbdcc9ce448bbd578b0105cfda24`
- 技术方案：`doc_9f72f5f119c4464db4fb8af20622bf4d` / `dver_ab7b18a63b194a88a1c05c8cc5e2104d`
- 开发计划：`doc_9259791325d14ef8b6fdf924c597ad35` / `dver_616984bc45cd4f80a6e31b876f7c64bf`
- 验收计划：`doc_c73f217fc18f43db9c062bc4b75347b6` / `dver_de68c86b18c14931919c76d810fe068a`
- 生成模型：OpenCode `opencode-go/mimo-v2.5`；状态：completed。

## 实现决策证据

- 日历只读投影：`dec_f09b752a574548fa83ae147097d06348`
- 审批批准后的工作项关联：`dec_521ec3d8963e457f9832d9376014b4c5`
- 失败恢复初始阈值：`dec_3d702cc86126424f8703d6bf3ee6c7e9`
- 任务拆解：`implementation-task-breakdown.md`
- Atlas 迭代：`itr_a750761320744c4b98543ff8ef81c07e`
- 五项任务：`tsk_8b48ce2c414b41be8bb5fb66afdce872`、`tsk_ce239372c539454a805fd0c6e661f1fc`、`tsk_23d65fff61084be5838790963db1b57f`、`tsk_94d68a786e0b47d3814c10477e82ace6`、`tsk_0d37b11dafe5455eaba85ce059083c43`

## T1 执行与验收

- OpenCode 执行 `exe_3e9789366db142b68a9ec77320156905` 已完成，生成 `contracts/cross-system-mapping.md`，差异范围合规并已应用。
- 产品验收状态：`passed`；验收证据覆盖契约内容和范围检查。
- 首次失败执行 `exe_99df9621ff324c78b289d0ec28a1076f` 保留：运行时 `serve --pure` 与当前 OpenCode CLI 不兼容，且 CLI 权限配置禁止编辑，导致无文件差异；修复后重试成功。
- T2 执行 `exe_30cdbb897bcb4595a607d7eeb01e4cbc` 已完成并应用 `contracts/approval-to-project-handoff.md`；产品验收状态：`passed`。
- T3 执行 `exe_b94bd5c8c8084c948faf10ea08e86cc3` 已完成并应用 `contracts/calendar-readonly-projection.md`；产品验收状态：`passed`。
- T4 执行 `exe_6558300bb9434cbeb2e1c5d59f1b06d1` 已完成并应用 `contracts/permissions-and-recovery.md`；产品验收状态：`passed`。
- T5 执行 `exe_5b4fad2544fd447ca7795f96f705efc3` 已完成；应用状态：`not_applicable`；产品验收状态：`passed`。分析覆盖正常、幂等、拒绝、退回、撤回、交接失败、超时、阻塞、日历失败、权限和反向写入边界，六项需求均满足。
- T5 限制：没有调用真实 provider API，也没有运行模拟适配器；结果用于验证契约和验收覆盖，不能当作真实供应商集成证据。
