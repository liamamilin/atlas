# 固定规范：服务器端 HTML 确认负例与清空人工验收步骤

同一已授权书签认知生产/必要修复/独立审阅范围。基于 v0.1.11，reuse_spec=true，只改 acceptance/p1-trash.cjs 与 acceptance/README.md，其余18文件字节复用；完整规范、原研究、身份、阶段、默认值和所有原断言不变。不研究、不安装、不执行生成程序、浏览器、应用或重启适配器，不发布，阶段not implemented、用例not_run。

前一份独立报告确认：坏头请求先被安全中间件拒绝，前端本地拦截也不能证明服务器独立校验确认。因此应补真实 HTTP 表单负例。模块接口和三处 await 已单独修复并受保护；不再为此更动它们。上一候选的重复完整复审已在无验收登记时取消，原事件与取消理由保留；不要推断其通过。

## p1-trash.cjs：在 A16 中补独立服务器确认分支

新增一个小的 async helper，并在 A16 末尾 await 调用；不能放到 A18 全局 DELETE /api/trash 护栏之后，避免缺少 --allow-destructive 时先终止而未做这些安全负例。不新增案例ID、阶段或功能，不删除原恢复/同址重存断言。

1. 用现有 createCategory/createBookmark/trashBookmark 及 tracker 创建本 run 独立非默认归类、其中一条活跃书签、一条已回收书签；保留源归类、活跃/回收记录的真实基线。读取完整归类快照、run活跃/回收记录及全局 GET /api/trash 的 total；不假设全库空或回收站为0。
2. 用现有 common.request 向已配置目标发送真实 application/x-www-form-urlencoded POST，redirect=manual，正常默认 Host，不伪造坏 Origin/Fetch 头（原生HTTP客户端无这些头是契约允许的）。不使用浏览器 JS，不 mock、拦截或直接改存储。这次必须进入业务确认检查，不能再靠坏头中间件拒绝。
3. 三种表单路径，各覆盖 confirm 缺省、字符串 false、字符串 yes：
   - /categories/{ownedSourceId}/delete，body 的 mode=purge，没有 targetCategoryId；
   - /trash/{ownedTrashedId}/delete；
   - /trash/clear。
   **新增分支绝不发送 confirm=true**，尤其不发送全局已确认清空，也不调用任何全局 DELETE /api/trash。原 A18 的显式 --allow-destructive 护栏和专用实例限制原样保留。
4. 固定规范只明确这些表单未确认时必须由服务器拒绝并零写入，未逐个锁定确认错误的 HTML 状态。因此新断言接受合理的两种既有呈现：200 HTML 重渲染且有非空可见错误结构（form-error、dialog-error 或 role=alert）；或400/409，其JSON错误码为 confirmation_required/invalid_confirm（或有相同意义的非空HTML错误结构）。不接受3xx、2xx成功页面、5xx、403/404等与确认无关的拒绝。不要为一个未锁定的HTTP呈现发明新硬契约，也不要放宽任何原有明确状态断言。
5. HTML 错误结构可用小的本地解析助手和 common.stripTags/decodeEntities（先读实际导出）提取匹配错误元素的非空内容；不能只检查整页含 error 字样、空占位符或HTTP200。JSON按统一错误信封校验。所有响应不跟随重定向、不访问外站、不回显认证材料。
6. 每个请求后读回真实数据，完整归类快照、本run活跃/回收行与计数、源归类存在性、原回收项来源/时间/正文、全局trash.total均不变。读回活跃记录按id核对，不能靠自比较或夹具常量冒充操作前快照。误实现若直接放行会导致本分支失败；测试只准备/清理自己记录，不清理其它run。

只加这个确定安全分支；不扩展其它UI、q/sort、导出、企业功能或一般输入负例。用精确小补丁，保留全部原代码和接口。新增的异步断言调用必须 await，导入只能来自真实导出；不靠未安装依赖。

## README：明确人工确认清空正例，而非自动执行

保留空库/空回收站当前体验的必需人工观察与未运行状态。在第15节给确认清空UI补一个可执行的人工步骤及验收标准，但本轮不执行，也不新增自动confirm=true请求：

- 仅全新专用、无个人数据、无需认证的测试实例；准备至少两条自己拥有的回收项和一条活跃项，记录实例/目标版本、实际基线数量和记录id。不得用真实个人库或为造空态删除别人的数据。
- 打开带basePath的 /trash，核对 trash-clear-form 的 method=post、action={basePath}/trash/clear；实际勾选确认并点击 trash-clear-submit，通过真实浏览器网络记录确认提交 confirm=true，而非API代替这次用户点击。
- 预期303 Location={basePath}/trash，发生真实导航；回收站列表为空，显示 data-empty-kind=trash，API只读核对total=0，原活跃项仍在、计数不变；记录实际命令/操作、目标版本、网络响应和截图/日志。未实际操作就记未完成，不能用A18的API结果代替UI正例。
- 这是已有 F11/§8 体验的人工验证设计，不是新功能或额外发布流程，不改变制品等级/自动用例数量；所有手工项和A01–A33目前均未运行、无pass证据。

现有CLI、--allow-destructive、浏览器认证拒绝、正确子路径、旧版本与安全说明保持。最终只允许这两个文件改变；冻结后做语法/AST接口与异步检查，再独立完整静态审阅。审阅不执行程序，不把可选建议全部升级为硬门。
