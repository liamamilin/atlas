# 三场景辅助试产对照

本轮预算与会议场景按“固定范围 → 真实开源源码研究 → 独立的本地试用模板 → 标准开发包 → Codex实际读取交接 → 实现 → 浏览器旅程”完成。书签保留上一轮交付和数据，本轮未修改。

| 场景与固定案例 | 来源模板 / 标准开发包 | 实际应用 / 源码包 | 核心操作结果 | 仍需 Codex 介入与后置项 |
|---|---|---|---|---|
| 书签 scn_7756e0007f6a463a97316f3f49c15248 r2；[LakhindarPal/bookmark-manager](https://github.com/LakhindarPal/bookmark-manager/tree/539881bc67099d491e8ab6f85de0f443fa7de623)，原共享case r1 | [R8试用模板](../bookmark-assisted-trial-2026-10-20/packages/template-snapshot.zip) / [标准开发包](../bookmark-assisted-trial-2026-10-20/packages/development-package.zip) | [运行5273](http://127.0.0.1:5273/) / [源码ZIP](../bookmark-assisted-trial-2026-10-20/bookmark-trial-source.zip) / [报告](../bookmark-assisted-trial-2026-10-20/TRIAL_REPORT.md) | 原7条浏览器旅程已通过，本轮健康检查就绪；保留现有数据 | 原试用包提取、应用实现和真实浏览器仍由Codex完成；P1、导入导出、去重、同步后置，只修实际核心问题 |
| 个人极简月度预算 scn_6fb4896d9eb0428aa1c080df0a137813 r1；[Actual Budget](https://github.com/actualbudget/actual/tree/8fba0e87cf7a4cda6ab5ea8012477bd7051f6ebc)，case:assisted-budget-actual r1，MIT | [场景模板](budget/packages/template-snapshot.zip) / [标准开发包](budget/packages/development-package.zip) | [月有度5274](http://127.0.0.1:5274/) / [源码ZIP](budget/budget-source.zip) / [报告](budget/TRIAL_REPORT.md) | 1200计划；35.50+12.30=47.80，改后42.80；超支负数、等额转移；新月支出0、旧月不变；真实重启保留 | 案例选取/研究、认知定义与验收编写、调用现有导出函数、应用实现和浏览器操作由Codex完成；支出/分类删除、导出与复杂报表后置 |
| 多项目会议结论 scn_805c99ffe8da4532817592bb466a505e r1；[Joplin](https://github.com/laurent22/joplin/tree/cf57e5932584c0fbd894d8510f1a31a4d41f2251)，case:assisted-meetings-joplin r2，根AGPL-3.0-or-later | [场景模板](meetings/packages/template-snapshot.zip) / [标准开发包](meetings/packages/development-package.zip) | [会后有据5275](http://127.0.0.1:5275/) / [源码ZIP](meetings/meetings-source.zip) / [报告](meetings/TRIAL_REPORT.md) | 收件箱→项目；正文/表格原文保存与编辑；项目隔离；置顶/归档/正文检索；回收恢复原状态；真实重启保留 | 同预算，研究与应用均需Codex；自动保存、富文本/附件、导入导出、同步协作、项目删除后置 |

## 可追溯性与复用边界

- 新增两个共享case身份，预算r1、会议r1后追加纠正r2；两个当前case供应用实证API和各自模板复用。书签复用此前案例，无新研究。会议纠正原因和原r1完整保留，不改写历史。
- 预算/会议包在应用开始前导出，CONSUMPTION.json记录读入文档摘要；本地冻结与实际代码的 SOURCE.json相连。源码ZIP和模板ZIP不同，不把应用源码充作模板认知内容。
- 开源源码固定commit并保留逐文件SHA和许可证，包中upstream-evidence.zip可核对。Joplin仅参考研究，未复制实现和图标；未穷尽许可证例外。两案例均静态研究、独立证据审阅pending、上游运行not_run。下游真实运行不反向证明上游运行。
- 本轮只对已有导出/打包方式作小范围参数化，复用小型标准库HTML/HTTP帮助函数；没有新平台、宽松模式或恢复授权框架。两个新模板与应用均属本地辅助试产，正式模板/严格开发队列新增0，不宣称自动工厂已全流程生产。
- 本轮9项冻结HTTP程序（预算5、会议4）和6项单元回归通过，两个源码包均实际解压独立启动；浏览器证据分别保存。程序由Codex先于应用编写，不冒称独立agent验收。预算最初测试目标互相污染的失败原件保留，隔离重跑同一程序通过。

## 原台账和严格状态

[FINAL_STATE.json](FINAL_STATE.json)为正式库只读快照：工厂86次＋此前独立连通性1次＝**87/500**，本轮受控OpenCode新增0；原书签业务修复**8/8**。原R8任务failed，G1 **blocked**、T08 **not_started**，没有新增窗口、grant、业务修复或正式发布声明。三个应用都为辅助试用，三份数据独立持久化，未打包/提交GitHub。

预算提交ed38dcc40b0ff168eb6ac4adbbc7926ceb511047的[CI 39455244074](https://github.com/liamamilin/atlas/actions/runs/39455244074)已success；书签aba973c24033a6acc21584cf7645656314ee9224的[CI 39450762869](https://github.com/liamamilin/atlas/actions/runs/39450762869)已success。会议应用随后单独提交，在最终交付中报告准确提交与对应CI状态。

三个应用仅监听本机。重新启动参见各源码包README；备份先停进程、复制各自data目录。首要下一步是用户真实使用后反馈核心缺陷；不自动扩充P1或恢复严格G1。
