# Home Care Ledger 局部修订与真实复审

本轮完成。新辅助模板静态审阅通过，应用未运行；旧撤回候选、严格G1/T08、原预算/失败/grant全部保留。没有启动批量生产或开发代表应用。

## 可用入口与固定身份

- [新修订制品](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_d3c38917d0404fa98b984955adde3e11)
- [标准开发包下载](http://127.0.0.1:5188/api/factory/assisted-templates/tpl_d3c38917d0404fa98b984955adde3e11/files/development)；仓库内 home-care-r1/atlas-development-package.zip。SHA256：72b029ac8476abadb6d8910674ec6d9befc500c474b247764f9b8b2dc08b2f26。
- 旧父制品tpl_d610fc5e84644092b880b30fbf691c29仍withdrawn，原冻结/首审/补审/失败记录不变，辅助下载仍409。新MODEL_PRODUCTION与冻结包都保存parent id/digest、case_ref和revision_request_digest，页面可回查父版本。
- 新导入摘要6b81fb4bcbb30b6d7e86ac790cdd9a9368cf72d750f15a4d893facb5aa8b74d2；冻结摘要见IMPORT_RECEIPT.json。静态独审输入摘要9d63418403336b739fe4f3f8dca46623af7a5ab7d8b4b9dae5923964a77b7637。
- 原场景scn_802f9221599a491781b3dafa4f27a033 r1不变。案例case:auxiliary-go-pilot-2026-10-21:home-care r1，digest f42187b6993942a959c4ca954c82e14d45472e9c1793cd908851311b7f4b28aa；micasa-dev/micasa @ ca69a88f998dec25c1e285121e428a4f7621dc68。无新研究；15条原来源观察不变，原共享记录整体复用。

## 五项修正及证据

|问题|本轮结果|证据|
|---|---|---|
|A01空PATCH|成功PATCH返回的完整patched对象作为基线，保留updated_at比较|probe.py:169–172；fixture合法时间更新通过，空PATCH写入负例被识别|
|A01非法分类|其余合法字段、枚举外category返回422 VALIDATION_ERROR，整个设备列表不变|probe.py:182–183；invalid_category_write被识别|
|历史日期|latest保存真实最近完成日；new_due=max(old due,latest+interval)；事务内读取、历史追加、计划更新，保留闰日/月末/跨年/后续补录|VIEW_ARCH.md:11/77/83/152；probe.py:285–301；显式到期与创建日首次补录均通过，缺下限负例被识别|
|A02完整集合|独立设备隔离，完整ID集合、数量及去重，保留状态/边界/筛选/排序|probe.py:129–133/191–246；额外/遗漏/重复任务全部被识别|
|A05结构|HTMLParser检查for/id、fieldset/legend、caption、th scope、status/live、lang及原状态词|probe.py:347–418；7种结构错误均被识别，未声称完整无障碍认证|

完整可读差分home-care-r1/CONTENT.diff；原JSON为权威，长字段精确解码VIEW_ARCH.md及READ_VIEWS.json含pointer与SHA。模型只返回受限字段更新和两份验收文件；宿主保留姓名、用户、功能、15来源观察和推断等未改字段。

## 真实执行与复用

修订author会话ses_ea208589fffeY8gRHkM8pRFG1I，独审会话ses_ea2047897ffeOOj8bA7xqsiYKj，均指定opencode-go/deepseek-v4.1-flash。独审新会话完整阅读架构，各长字段实际读取覆盖通过；七项true，15观察accepted，issues=[]，verdict=pass。未复用旧pass，完整原始返回、events、BINDING、DELIVERED和摘要在audit/。独审结果及MODEL_PRODUCTION绑定最终冻结内容；VERIFY在重载/导出时再次核对。

一次修订+一次独审，共2/6次，91→93/500，活动0；无第二内容修订、无技术恢复。新辅助phase从首次真实预留启动固定24h，重放不重置。原修复8/8、历史grants/窗口/有效时间来源不变，见REAL_API_RESULTS/BUDGET_BEFORE/AFTER。

同一请求实际重放（REPLAY.log）复用两个成功检查点、同一案例和同一制品，新增调用0、案例0。正式导入与下载回执不是模拟结果。开发包中HANDOFF、KNOWLEDGE、CURRENT_PHASE、ACCEPTANCE_CONTRACT、APP_DELIVERY、PROJECT_DECISIONS全部存在，案例记录逐对象等于原r1。

## 检查与保护

- 宿主工具24项通过，含6项新修订回归：成功持久化/重载、旧pass隔离、失败不能导出、改输入拒绝、跨job/实例累计限额和固定窗口。HOST_TESTS.log。
- 完整后端773项通过，8项按既有条件跳过。最初19项受沙箱socket限制的失败日志保留；正常权限重跑成功。BACKEND_TESTS_UNSANDBOXED.log。
- ruff通过；前端类型、9项单元、构建通过；入口E2E8项通过。最终源码完整CI见精确GitHub提交。
- 隔离容器19项fixture检查通过，包含A01–A05正例、两种首次补录及13个故障注入。模型程序只在无网络、只读、非特权容器执行；这些不是实际应用运行。FIXTURE_RESULTS/EXECUTION.json。fixture自身两处初始修正不改变模型交付，保留错误日志。
- 真实浏览器验证叶子→场景→新模板→同案例；可见静态通过/应用未运行/旧版本链接与下载。NEW_REVISION.png、DETAIL_BROWSER/CASE_BROWSER.txt。
- 原16份标准包逐一实际下载核对SHA；112个既有ZIP/数据文件不变，包含六应用数据库。原16记录除指定库存路径外未改；原家庭保养失败记录和冻结包未覆盖。
- 库存源码路径按要求修正，目标与原SHA一致，实际下载通过，不重新打包。

## 数量和边界

可用辅助模板从16增至17；目录总18条=17可用+1待修订历史。6份原有核心运行示例、12条应用未运行（含旧撤回历史）。本轮新增可用模板1、共享案例0（复用1）、应用运行0、严格正式发布0。严格G1/T08未推进，未冒称通过。

内容仍为英文；本机单用户、单住房、无通知/账户/删除等原限制保留。持久化重启、真实服务API/UI、应用事务行为均待将来实际开发后验证；本轮仅静态审阅与隔离fixture。未用调用额度不是自动追加生产许可。
