# 月有度：首份预算辅助试用交付

可打开 **http://127.0.0.1:5274/**；仓库根目录启动 `python3 examples/budget-trial/app/serve.py --port 5274 --demo`。源码目录examples/budget-trial，独立源码包budget-source.zip（不含数据库）。

先定来源/范围，再导出模板，CONSUMPTION.json记录应用尚未开始时实际读取的交接文件摘要；随后才创建应用。未倒填开发来源。

## 核心浏览器结果

| 旅程 | 实际结果 | 证据 |
|---|---|---|
| 月度预算与收入 | 从空库创建2026-10，收入5000，食品1000＋交通200＝计划1200、未分配3800 | 01-start、02-plans |
| 金额与修改重算 | 页面记35.50与12.30＝47.80；编辑早餐为30.50后总支出42.80、计划剩余1157.20 | 03-first-expense、03-sum-47-80、04-edit-open、04-recomputed-42-80 |
| 超支与计划调整 | 食品计划临时改20，显示-22.80；恢复1000后转20给交通，980/220，计划总额仍1200 | 05-overspent、05-transfer |
| 新月与隔离 | 显式保存模板，2026-11创建后支出0、计划1200；返回2026-10支出42.80保持不变 | 06-template-saved、06-next-month-zero-spent、06-back-to-old-month-verified |
| 真实重启 | 停原PID59055并验证连接拒绝，以同data-dir启动新PID59579；两个月全部字段相同，真实浏览器重载后仍可见 | 07-before/stopped/after-restart、07-browser-after-restart |

页面截图evidence/final-home.png。浏览器月份控件首次快速切换后立即reload打断导航，旧记录06-back-to-old-month实际仍为11月；保留该观察，后续等待控件与导航完成的06-back-to-old-month-verified才作为返回旧月证据。不将失败操作冒充通过。

## 真实案例和模板

共享case `case:assisted-budget-actual r1`，digest `36729c5ed3f35e8732580af41fa69c27e16eacaaa067f38b9e73bfc0eaff12f0`。固定[Actual Budget](https://github.com/actualbudget/actual/tree/8fba0e87cf7a4cda6ab5ea8012477bd7051f6ebc)；MIT许可证随upstream-evidence.zip保存。源码定位月/分类SUM、整数cents CLI、重算；无结转/收入/极简模型标为目标推断。CaseLibrary.commit_research正式服务保存，原应用实证API读取同一记录，模板inputs/shared-case-record.json逐字引用，证据独立审阅pending，上游运行not_run。

正式场景 `scn_6fb4896d9eb0428aa1c080df0a137813 r1`原记录仍draft；用户明确授权此固定场景辅助开发，本地副本注明确认来源，不修改正式场景或通过状态。

模板digest `bb0412f604e04d6f6343c18d111d05e368be0b2268d6e852f43e78e66c5b190c`；模板ZIP SHA `e5f58d0641f02ecaa27b06bd89a8844c3ab0ba7a7a2184f6c9875681c5896d79`；标准包ZIP SHA `1f78e45513dde3f3a50f1ea88fd708f5bd8a5095b00f359409b5e4852dcb6fc7`。本地freeze只固定输入；完整定义、研究、可执行验收程序在实现前已固定。来源case-record/definition与包均交付，不登记正式tpl、不冒充application-development队列消费。

## 检查、迭代和缺口

- 开发前冻结的B01–B05程序均在各自隔离真实HTTP应用通过；B05包含自有进程停止/同目录重启。与浏览器真实旅程分别留证。
- 首次复用同一测试目标时，前一用例保存的全局模板影响后续前提，B02/B03/B04失败；原件在evidence/initial-shared-target。改用每用例独立实例后，同一字节程序全部通过；未修改断言或用户库。
- 三项定向单元回归通过：整数分/非法金额、跨月日期零写入与GET无写入、模板不复制支出/超支负数/重复月份不覆盖。ruff检查通过。
- 应用初版后修正重复HTML label id，关闭连接/同源保护复用书签已验证方式；格式化不改变业务。上述属于辅助实现迭代，不记作严格第九轮修复。
- 源码ZIP SHA `5385e7e0c449fd406e8f030dca8067145ea5e0f2b2ed69f4c67f8ff1b58608c3`，所有文件摘要见SOURCE_MANIFEST.json；解压独立启动另留evidence/standalone-result.json。
- 后置：支出/分类删除、导入导出、复杂报表、银行连接、账户/同步、多币种、并发压力和完整错误矩阵。只供本机单人顺序使用；无严格认证声明。

本轮受控OpenCode新增0；原factory86＋external1＝87/500、业务修复8/8不变。严格G1 blocked/T08 not_started；本轮辅助预算应用1，正式模板/严格开发队列新增0。书签应用和原数据保留。
