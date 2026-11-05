# 可能性图谱 · 两类型试点

生成日期：2026-11-05。工作分支：`codex/stabilize-atlas`。

依据用户指定分支上的 [possibility-mapping 技能](https://github.com/liamamilin/atlas/blob/codex/stabilize-atlas/.agents/skills/possibility-mapping/SKILL.md)，先选择其“第一批验证”指定的两类，并映射到 ATLAS 已有叶子。

| 阅读范围 | 已确认的 ATLAS 叶子 | 分类 | 本次产物 |
| --- | --- | --- | --- |
| B2C 单商家商城 | E-commerce Platform · `e-commerce-platform` | 05.01 | [B2C 电商商城 · 可能性图谱](e-commerce-platform.md) |
| 个人工作与生活任务管理 | Task Management Application · `task-management-application` | 03.06 | [个人任务管理软件 · 可能性图谱](task-management-application.md) |

这两个样本分别检验多种业务对象的联动，以及同一任务在不同时间、视图和重复规则下的变化。两份均包含期望状态、与状态对应的期望变化、实际阅读的依据和未验证边界。

选型以 `application-atlas-production-pack/DIRECTORY.md`、正式类型正文及 `atlas/atlas.json` 的叶子标识为依据。本地真实项目目录以只读方式查询，分别选取已关联的 PrestaShop 和 FlowWeek 继续核对 README；项目被目录关联，并不自动证明它覆盖全部类型能力。在线官方资料的实际阅读链接列在两份文档中。

## 本轮检查结果

已逐份对照技能检查：状态描述具体结果，变化说明触发、条件与结果，并明确关联相应状态；重要判断给出来源，跨材料归纳与未知部分分别标注。两份文档均未引入开发步骤、SOP、现实差距分析或图谱可视化。

重点保留了三个核对结果：电商订单产生可以早于付款；退款记账和实际资金返还需要区分；任务完成、日期紧迫性、每日视图归属及周期推进有不同含义。任务样本也保留了真实项目具有 `blocked` 附加状态这一观察，没有把仓库的二态抽象写成所有实现的硬性限制。

本轮完成资料核对、作者内容复核以及文件链接、来源引用和状态关联的静态检查。两份均为**待人工审查的试点草稿**，尚未获得用户内容确认；本轮未运行参考产品，也未接入网页或启动批量生产。
