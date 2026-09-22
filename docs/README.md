# 项目文档

本目录只把当前决策、下一步计划和仍会继续更新的验证记录放在顶层。已经完成的阶段记录移入 `archive/`，保留证据但不再作为当前任务入口。

## 当前工作文档

- [U17 产品设计](U17_DESIGN.md)：产品边界、用户流程、项目模型和执行架构。
- [U17 开发规划](U17_DEVELOPMENT_PLAN.md)：已完成范围、剩余里程碑、优先级与完成条件。
- [U17 项目工作台设计检查](U17_PROJECT_WORKBENCH_REVIEW.md)：项目页面的状态语义、操作闭环、风险分级、处理记录与重构顺序。
- [U17 产品打磨计划](U17_PRODUCT_POLISH_PLAN.md)：当前阶段的产品收口顺序、完成定义和恢复 M5 的条件。
- [U17 产品化收口开发计划](U17_PRODUCT_CLOSURE_PLAN.md)：本轮发布前的开发阶段、执行循环、完成条件和当前队列。
- [U17 M5 试点计划](U17_M5_PILOT_PLAN.md)：产品打磨完成后的三个真实案例、普通生成对照和后端决策办法。
- [U17 核心主线验证](U17_CORE_PATH_VALIDATION.md)：最近一次从类型入口到完成迭代的全绿证据。
- [U17 发布检查清单](U17_RELEASE_CHECKLIST.md)：可重复执行的自动化、浏览器和安全反馈发布前检查。
- [U17 发布候选说明](U17_RELEASE_NOTES.md)：当前候选版本的交付范围、启动方式、验证结果和已知限制。
- [U17 最佳实践案例](U17_BEST_PRACTICES.md)：已验证的新想法与已有项目案例，以及多类型需求、Agent Harness 产品调研、高风险数据恢复、中断恢复等待验证模板。

## 当前试点材料

- [新想法样例](u17-samples/new-idea/)：M5 简单新想法案例的输入参考。
- [已有项目样例](u17-samples/existing-project/)：M5 已有项目改进案例的输入参考。
- [Agent Harness 产品调研案例](u17-pilots/agent-harness-product/)：已完成通过 Atlas 调研 Agent Harness、形成 27 项决定、生成并批准六份当前文档（分析 v7、产品/技术/开发/验收 v6、交互 v5）、处理冲突、刷新导出包并建立首版实现迭代；M0 CLI、provider、连通性冒烟和兼容基线已通过，M1 的 preflight、CLI 证据、固定验证、显式清理和最小终端入口已接入，详见 [M1 适配层契约](u17-pilots/agent-harness-product/m1-cli-adapter-contract.md) 与 [M1 终端切片](u17-pilots/agent-harness-product/m1-terminal-slice.md)。
- [高风险数据恢复案例模板](u17-pilots/data-recovery-migration/)：验证备份、预览、回滚和独立验收的规划记录，尚未开始实际试点。
- [中断恢复案例模板](u17-pilots/interrupted-session-recovery/)：验证交接包、新会话核对和避免重复副作用的规划记录，尚未开始实际试点。

样例只提供起点。正式 M5 试点仍需从产品界面重新建立项目、固定输入并保存原始运行记录。

## 历史档案

- [U17 M0–M4 验证档案](archive/u17/README.md)：已完成阶段的实现范围、测试和浏览器证据。

归档文档用于追溯，不用于判断当前下一步。当前状态以开发规划和 M5 试点计划为准。
