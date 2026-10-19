# 当前开发交接 / Current handoff · P0

## 先读 / Start here

- 检查已有项目、指令和用户决定；阅读 CURRENT_PHASE.json 与 PROJECT_DECISIONS.json。
- Check the existing project, instructions and confirmed user decisions; read those two JSON files.
- 摘要包含当前及前期能力、相应验收目标和全部决策触发条件。前期能力不是已实现，先核实再补齐或回归。
- The summary includes selected and prerequisite capabilities, case goals and all decision triggers. Earlier phases are prerequisites, not claims of completed work. Verify, complete or regress them.
- 对照完整的已确认 workflow/acceptance 检查阶段范围。旧包可能把核心流程分到后期；发现缺口要明确报告或请求新修订，不能擅改冻结阶段、跳过用户需求或声称完整场景已完成。
- Compare phase scope with the full confirmed scenario. Legacy phases may split the core journey. Report gaps or request a revision; do not silently rephase, skip requirements or claim full scenario completion.

## 按任务读取 / Load when needed

| 时机 / When | 材料 / Reference |
| --- | --- |
| 选择技术栈、实现相关数据/接口/UI 或处理错误之前 / Before related implementation | blueprint/ARCHITECTURE.md 的相关契约；核对现有栈和安全、持久化边界 / relevant contracts, existing stack, security and persistence boundaries |
| 查需求理由、来源或不适用范围 / Scope and rationale | blueprint/PRODUCT.md, blueprint/template.json |
| 选型或复用外部资源之前 / Before reuse or sourcing | blueprint/CATEGORY.md 的来源、许可证、未知项 / sources, licenses and unknowns |
| 遇到决策触发条件 / A decision trigger occurs | PROJECT_DECISIONS.json, blueprint/DECISIONS.md |
| 配置并执行验收之前 / Before testing | blueprint/acceptance/README.md，CURRENT_PHASE.json 中实现路径对应的执行器及依赖 / listed case implementations and dependencies |
| 需要补充开发约定 / Additional development guidance | blueprint/AGENT.md |
| 规划下一阶段 / Next phase | blueprint/ROADMAP.md |

材料路径均相对开发包根目录；验收 implementation 路径相对 blueprint/。共用执行器可能包含后期用例：先检查能否选择本阶段，不能时报告适配缺口，不能删断言或假报通过。

References are relative to this package; acceptance implementation paths are relative to blueprint/. Shared runners may include later cases: check phase selection support, report adapter gaps, and never delete assertions or fabricate passes.

## 完成条件 / Finish and report

实现已选阶段及未满足的必要前置能力，保留失败/恢复和数据完整性行为。在专用测试实例执行当前及前期回归；记录实际命令、版本、通过、失败和未运行。若改栈，记录与原契约的差异和等价验收适配；不要把模板默认值当成用户硬约束。

Deliver the selected capability and missing prerequisites, including failure, recovery and data integrity. Run current and prerequisite regressions on an isolated target. Record commands, version, passes, failures and unrun cases. Document stack changes and equivalent acceptance adapters; defaults are not user mandates.

导出未运行任何程序，包内历史报告不等于本项目通过。完成当前交付后停止扩展后期功能，报告剩余差距；没有授予联网、发送资料、凭据、发布或破坏性操作权限。

Export executes nothing; historical reports are not this project's acceptance. Stop after the selected delivery and report gaps. No network, data transfer, credential, publication or destructive permissions are granted.

See EXPERIMENT_NOTICE.md.
