# 项目文档

本目录只把当前决策、下一步计划和仍会继续更新的验证记录放在顶层。已经完成的阶段记录移入 `archive/`，保留证据但不再作为当前任务入口。

- [现有产品逐页走查与修复](product-review-2026-10-22/REPORT.md)：问答与案例状态、工厂导航、设置错误恢复及手机布局、教程和中文内容校正；包含页面对照、逻辑梳理、回归与旧数据保护。模板生产保持暂停；并行的首页/发现项目改版单独验证。

## GitHub 阶段交付

用户于 2026-10-19 授权将当前开发成果及后续完成并验证的阶段成果提交、推送到 `git@github.com:liamamilin/atlas.git`。沿用当前工作分支，每阶段提交前核对改动、凭据、可分发文件和相应验证；不强制推送或覆盖远程历史。源码、文档、汇总证据及明确保留的交付包进入版本库；本地数据库、凭据、依赖、构建输出与模型运行的嵌套 Git 工作区留在本机。后者由 `template-factory/.gitignore` 明确列出，避免误提交为无法克隆的子模块；原文件不删除。推送本身不代表已发布产品或远程 CI 已通过。

## 模板工厂

- [认知模板目标与执行偏差记录](template-factory/COGNITIVE_TEMPLATE_ALIGNMENT_2026-10-22.md)：以用户三份完整产品参考样稿为内容标准；保留本次目标纠正、未确定方案和真实停止点。两样本仅书签静态通过入库，投票未通过；全量与试跑暂停，不将历史辅助成果或技术检查升级为新工厂已稳定完成。

- [家庭保养 Go 局部修订与真实复审](template-factory/go-home-care-revision-2026-10-21/REPORT.md)：新辅助修订静态通过、应用未运行；原案例复用，17可用+1待修订历史，93/500调用。

- [Atlas 辅助模板工厂 V1 收口与用户入口](template-factory/assisted-v1-user-entry-2026-10-21/REPORT.md)：当前16份辅助模板的叶子/场景/案例入口、6份核心示例与10份未运行、标准包和Codex交接。下方严格V1历史受控链仍保持原状态，不因辅助交付升级。
- [十模板辅助批次交付](template-factory/assisted-batch-10-2026-10-21/REPORT.md)：十个不同叶子、十份固定共享案例、两个新上下文开发的代表应用；真实浏览器/重启、幂等复用、CI审计修复及未运行范围分别记录。
- [V1 交付总览与真实阻断](template-factory/v1-2026-10-19/DELIVERY.md)：G1 正式评估、固定首批未启动报告、完整测试和恢复步骤；未取得真实 P0 运行证明。
- [模板工厂 V1 实施与验收](template-factory/v1-2026-10-19/IMPLEMENTATION.md)：共享案例库、固定案例依据、正式认知目录、受控批次及本轮真实 G1 / 首批进展。当前是否达标以该目录实际报告为准，历史实验不替代本轮。
- [V1 数据与交接合同](template-factory/v1-2026-10-19/CONTRACTS.md)。

叶子类型与应用场景构成生产目录。当前已实现场景生产及代码候选模板流程；模板主线为“认知模板包”，提供成熟产品判断、开发决策、分期与可执行验收，结合必要代码交给开发 agent 使用。认知包支持 OpenCode 多源研究、独立规范预审、联合生成、完整审阅、修订及冻结阅读；开发包按完整认知、当前执行和独立验收组织。声明冻结 runner 的包可提交源码进行 Docker 阶段验收；旧包缺适配器明确不可用。真实试产阻断、运行和修订证据分别记录，V1 新增受固定案例依据和当前独立审阅约束的认知发布入口；历史包不自动升级。

- [自动认知生产与独立审阅验证](template-factory/2026-10-17-cognitive-production.md)
- [完整认知库、阶段执行与独立验收改造](template-factory/2026-10-19-factory-refactor/README.md)：交付协议、CLI 可靠性、容器运行边界与本轮验证。
- [使用/不使用认知模板的真实开发 A/B](template-factory/ab-tests/bookmark-2026-10-18/REPORT.md)：同一 commandcode/DeepSeek V4.1 Flash 开发两份应用、真实浏览器及持久化实测、独立匿名配对评测；核心流程均通过，边界差异、开发用量和 CLI 失败分别记录。
- [阶段摘要交接与本地导出验证](template-factory/handoff-pilots/bookmark-2026-10-18/README.md)：当前能力、前期回归和决策先读，完整原包按任务查阅；不等于新一轮模型开发或成本验证。
- [完整核心 P0 的书签后续试用](template-factory/handoff-pilots/bookmark-core-2026-10-18/README.md)：新规范、OpenCode 开发、分类与请求截断缺陷、必要修复及真实复测；首轮和修复结果分别保留，不改旧 A/B 成绩。
- [跨品类模板与交接形式对照](template-factory/ab-tests/cross-domain-2026-10-19/REPORT.md)：预算、设施预约、批量改名，比较无模板、完整附件和同包分层交接；真实运行、修复与探索性边界差异分开记录，没有通用获胜或成本结论。另见[模板形式建议](template-factory/ab-tests/cross-domain-2026-10-19/FORM_ANALYSIS.md)。
- [认知包工厂接入验证](template-factory/2026-10-17-cognitive-factory-integration.md)
- [认知模板设计与当前实施顺序](TEMPLATE_COGNITION_DESIGN.md)
- [个人书签认知模板样板](template-factory/blueprints/bookmark-personal/README.md)：规范、开发指令与阶段验收；已完成独立审阅修订和下游 P0 十项实测，范围及证据见包内 VALIDATION.md。

- [开发计划与范围](TEMPLATE_FACTORY_PLAN.md)
- [使用说明](TEMPLATE_FACTORY_GUIDE.md)
- [验证记录](TEMPLATE_FACTORY_VALIDATION.md)

## 当前工作文档

- [U17 产品设计](U17_DESIGN.md)：产品边界、用户流程、项目模型和执行架构。
- [U17 开发规划](U17_DEVELOPMENT_PLAN.md)：已完成范围、剩余里程碑、优先级与完成条件。
- [U17 项目工作台设计检查](U17_PROJECT_WORKBENCH_REVIEW.md)：项目页面的状态语义、操作闭环、风险分级、处理记录与重构顺序。
- [U17 产品打磨计划](U17_PRODUCT_POLISH_PLAN.md)：当前阶段的产品收口顺序、完成定义和恢复 M5 的条件。
- [U17 产品化收口开发计划](U17_PRODUCT_CLOSURE_PLAN.md)：本轮发布前的开发阶段、执行循环、完成条件和当前队列。
- [U17 剩余产品收口与发布打磨计划](U17_REMAINING_PRODUCT_PLAN.md)：T025-T032 的优先级、依赖、外部条件、验证矩阵和 `PROJECT_ACCEPTED` 门槛。
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

归档文档用于追溯，不用于判断当前下一步。当前状态以开发规划、M5 试点计划和[剩余产品收口与发布打磨计划](U17_REMAINING_PRODUCT_PLAN.md)为准。
