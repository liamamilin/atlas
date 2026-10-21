# OpenCode Go 辅助模板单样本验证报告

结论：真实跑通了联网发现、固定源码研究、认知生成、独立会话审阅、共享案例保存和辅助候选入库/导出。**本样本未通过完整材料独审，已正式撤回；新增可用模板为0，不能据此宣布Go自主批量生产已经验收。** 生产入口和失败门禁已实施，原16份辅助模板与六个应用的数据保留。

## 本轮样本和产物

- 叶子：home-maintenance-application；用户指定模型：opencode-go/deepseek-v4.1-flash。
- 场景：自住房/设备锚定、每N天保养、到期回查、完成备注、下一到期日和历史。生成标题Home Care Ledger，正文为英文，这是当前样本的展示限制。
- 真实来源：https://github.com/micasa-dev/micasa @ ca69a88f998dec25c1e285121e428a4f7621dc68，许可证Apache-2.0。宿主固定8份文件摘要，代码/文档观察15条；上游未运行。
- 场景ID：scn_802f9221599a491781b3dafa4f27a033 r1。
- 新共享案例：case:auxiliary-go-pilot-2026-10-21:home-care r1；新增1，复用0。应用实证与模板使用相同case_id/revision/digest及同一case-record.json。研究在模板失败后仍可读取复用。
- 辅助候选：tpl_d610fc5e84644092b880b30fbf691c29，导入摘要4b466e1fe6fd062b170341287addae5a3cc8eb92d0dbfbe87ca4c6c9f45438f8；原冻结摘要a869427a057907eaf0e3ab1182e8acb2279b47953ea6f399022e30a559ad0cf0。
- 页面：[待修订草案](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_d610fc5e84644092b880b30fbf691c29)；[对应叶子](http://127.0.0.1:5188/types/home-maintenance-application)。
- 原冻结包、标准包、开发API下载回执及来源摘要在home-care/packages/、home-care/atlas-development-package.zip、IMPORT_RECEIPT.json。这些是**待修订历史草案**，不是通过验收的开发来源。标准辅助下载入口与新开发包导出被409门禁拦截；原冻结包仍可下载供回查。
- 独审完整材料另存home-care/readable-review-materials.zip，包含原JSON、其精确解码的阅读视图、原验收程序和固定上游源码；没有改写冻结内容。

## 真实执行结果

|步骤|结果与证据|
|---|---|
|发现|Go模型真实联网，9次成功搜索、13次成功webfetch，选择micasa；宿主固定commit/许可证/文件摘要。calls/discovery、SOURCE_PIN.json|
|研究/生成|第二会话产出5项P0能力、数据/API/日期错误合同、probe.py与README。原返回与AUTHOR_INPUT.json保留|
|首审|第三会话返回pass，15条源码引用接受，随后已导出并辅助入库。现场发现arch在JSON单行中被read工具截断；首审不能替代完整材料审阅。原结果未删除|
|补充独审|用户追加授权最多1次同内容审阅；第四个独立会话实际读全架构168行，返回needs_changes，架构/验收两维不通过，五条阻断意见。SUPPLEMENTAL_FAILURE.json|
|停止与入库状态|通过正式POST artifacts/id/review withdraw撤回唯一新增候选；WITHDRAW_RECEIPT.json保留。目录展示待修订，不冒称可用/正式发布；共享案例保留|
|重复执行|第4次审阅检查点实际重放，不启动第五次调用、不新增案例/制品；仍按失败停止。REPLAY_RESULT.json|

完整材料复审指出：A01旧updated_at基线导致误报；缺非法category负例；首次历史完成的日期公式与“到期不倒退”承诺冲突；A02未断言完整集合；A05只检测HTML关键字。逐条原文在calls/blueprint-spec-review-aux-readable/RESULT.json；最小后续方案见REVISION_PLAN.md。**本轮不改冻结内容、不继续加调用。**

## 宿主改造

新增examples/assisted-trials/produce_with_opencode.py，复用已有CLI、BudgetLedger、CaseLibrary、produce_batch、export_trial、正式导入和阶段导出。模型没有写库、赋予来源身份或执行源码权限。只将模型提案的验收程序做AST语法检查，不在宿主执行。

- CLI启动前持久预算预留；沿用原campaign/500总限额，新的稳定辅助phase锚定本轮8小时，不改G1/T08时间与授权。原3个会话+本轮显式追加1次，不盲目补调。
- 提示、原始输入、叶子字节、源码文件清单及结果摘要绑定检查点。成功交付可复用；交付后落盘中断可从原返回恢复；失败/启动不明默认停止。
- 长JSON字符串展开为精确阅读文件并保存JSON pointer与SHA；新生产默认首次审阅即采用格式2，持久化格式版本避免重载后提示漂移。要求实际工具返回包含每个长字段视图全部行。
- 七项检查全部true、独立实际session、逐源码观察接受、问题为空才可入库；发现完整材料失败后，旧批次入口也不可绕过。
- 模型来源写入冻结 provenance 与inputs/model-production.json；原Codex16份模板和旧包结构/摘要不变。研究、模型静态审阅、下游运行、正式发布分别展示。
- 辅助待修订状态和证据按摘要绑定；新候选被撤回，推荐下载/新开发包导出被拦截，原冻结仍可审查。

## 检查与保护

- 辅助工具回归18项；目录/门禁11项；蓝图21项；共享案例12项；预算25项；CLI用量2项，共89项相关Python检查通过。各日志在本目录。
- 前端typecheck、9项单元测试和构建通过；入口E2E7项通过（ENTRY_E2E.log），含失败模板不推荐为可用包。最终提交的完整CI以GitHub该提交的精确运行记录为准，交付时提供链接。
- REAL_API_RESULTS.json核对原16份标准包实际下载SHA；新模板needs_changes、共享案例可读、原开发包内6份交接文件和案例记录一致；辅助下载409。
- PRESERVATION_BEFORE/AFTER核对107个既有ZIP/数据文件全部不变，含六个原应用数据库；HISTORY_CHECK确认原修复、窗口、grants均不变。
- 本轮未开发/运行代表应用，未执行生成probe或上游服务；没有伪造真实应用通过证据。

## 调用、上下文与边界

实际新增4次CLI会话，共用原账本87→91/500，活动0；书签历史业务修复8/8，历史grant与失败保留。严格G1仍blocked，T08仍未启动。本轮辅助失败不替代或恢复这些严格任务。

CALL_METRICS.json按step_finish去重记录：input 206667、output 8624、reasoning 67234、cache_read 681088、cache_write 0。它们是各步骤累计值（输入会重复），不是单次峰值上下文。CLI cost未标币种，不能当作实际账单。CLI指定Go/DeepSeek模型，事件未提供observed_model，不编造额外模型身份。

本机模型目录标注context 1000000、output 384000 tokens；任务无额外token覆盖，未实测服务端极限。此次问题是读取工具单行2000字符截断，增大token上限不能修复。补审后发现的是实际合同/验收缺陷。

Codex介入：选择试点范围、实现执行入口与宿主门禁、检查API/浏览器并提交代码；研究提案、模板内容及两次审阅确由Go模型完成。尚未证明不同叶子稳定产出、自动业务修复和应用运行；下一步应只修订这五项、复用原案例并完整复审，不先扩大批量。

审计可移植性：OpenCode在调用工作目录自动初始化的嵌套Git保持本地，不作为子模块交付；audit/<stage>/提供逐字节相同的普通审计文件和FILES.json，calls/<stage>/是当前工作区原始路径。固定源码与阅读视图另在两个证据ZIP中，未删除本地工作区或历史。
