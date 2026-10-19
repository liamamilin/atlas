# 冻结 v0.1.6 的限定修订：规范与验收一致

仍是已授权的书签认知生产与独立审阅。复用原调研，不搜索、不安装、不运行生成程序/应用/浏览器/重启适配器、不发布。只做局部规范补充及两个现有程序的小范围修改，保留 25 个能力、9 个决策、P0–P2、A01–A33 与既有全部正负向断言。其余程序字节复用。阶段 not implemented、案例 not_run；静态审阅不冒充运行。

完整独立审阅已确认范围、产品闭环、默认决策、Agent 交接与证据诚实性通过；两个阻断项是规范/程序一致性与 HTML 表单安全负例。本轮不追逐报告中的全部可选建议，不新增功能或案例身份。输入的旧报告保持原结论，仅作修订依据，修改后必须重新独立预审及完整审阅。

## 一、只澄清架构的既有行为，不重写全篇

1. POST /api/bookmarks、PATCH /api/bookmarks/:id、POST /api/bookmarks/:id/restore 的显式 categoryId 在形状合法但资源不存在或已 tombstone 时，统一 400 invalid_category，details.reason=unknown_or_deleted。省略/null/空串/类型等规则保持；归类删除独有的 target_unavailable/self_target/target_not_allowed 保持，不能混用。无须为其它未指定错误发明 reason。
2. §8 所有写入 HTML 表单明确 method=post；查询仍 method=get。包括新建/重命名/删除归类、保存与重复另存、移动、编辑、软删除、恢复、单条永久删除、清空。成功 303 Location 明确：新建归类到首页；重命名到 /c/{id}；保存、重复另存、移动、编辑、软删除、归类删除 move/purge、恢复到首页；单条永久删除和清空到 /trash，均带 basePath。保留现有 flash 约定及既有失败输入保留/零写入。一般字段错误 200+form-error；归类删除目标失效继续 400+dialog-error。Host/Origin/Fetch 安全拒绝在业务表单前返回 400 invalid_host /403 forbidden_origin JSON 错误信封，不被普通表单 200 渲染覆盖。
3. 浏览器渐进增强开启时，未勾选 trash-delete-confirm 或 trash-clear-confirm 点击提交必须本地阻止、显示非空可见 form-error 或 role=alert，不导航、不发变更请求。服务器独立验证确认，不能只靠 JS；无 JS 时服务端仍拒绝未确认请求且零写入。单条 HTML 永久删除需要 confirm=true；这不改变单条 JSON API DELETE /api/trash/:id 无 confirm 参数的契约。全局 HTML 清空确认正例仍只在专用实例手工核对，本轮不生成/执行确认清空调用。保留归类 purge 的 dialog-error 与双独立表单约定。
4. 当前 category-link 与 bookmark-category 元素内文本是归类名；计数如显示，放在这些被测试元素之外。不要改变归类名、十进制 ID 或已有选择器。§8 保存表单 P0 也渲染 categoryId 下拉，但仅含默认归类；P1 才显示全部活跃归类，不让 A28 调用 P1 接口。

## 二、只改 acceptance/p0-limits.cjs、acceptance/p1-edit.cjs

必须先读取现有 common/support 导出与目标文件。使用精确替换/局部追加，不重写巨型文件。不删原断言、不放宽错误/零写入要求、不伪造响应。file_plan 对这两个路径 reuse=false 并说明责任，其余 reuse=true；文件清单与接口保持。

### A09 / p0-limits.cjs：P0 原生保存表单

保留所有既有 API、URL/字符/大小/读 Host/客户端边界断言。追加 POST /bookmarks 的四类安全负例：错误 Host、Origin:null、外站 Origin、Sec-Fetch-Site:cross-site。body 必须是真实 application/x-www-form-urlencoded（URLSearchParams(...).toString()），字段是合法 runId 网址/标题/备注，不能 JSON body 冒充表单。通过 common.request 仅向已配置目标发请求，redirect manual，坏头只作为该目标请求头，无外站访问。期待错误 Host=400 invalid_host，其余=403 forbidden_origin，只有错误信封且无数据正文；操作前后真实基础列表/归类计数和探测记录内容保持，不提前调用 P1/P2 接口。A09.goal 追加该代表性 HTML 保存负例范围即可。

### A20 / p1-edit.cjs：P1 表单与归类写入边界

保留 A19/A20 全部原断言。在 A20 中以本 run 独立且由 tracker 管理的活跃归类、目标归类、活跃书签、回收站书签为前置，扩充四类坏头矩阵（同 A09）：

- HTML POST /bookmarks/{id}/move、/bookmarks/{id}/edit、/bookmarks/{id}/delete、/categories、/categories/{id}/rename、/categories/{id}/delete（mode=move 到本 run 活跃目标）、/trash/{id}/restore、/trash/{id}/delete、/trash/clear；均 application/x-www-form-urlencoded，语义合法字段。永久删除/清空探针必须不带 confirm 或 confirm=false，绝不发送 HTML 全局 confirm=true；中间件正确仍先返回 400/403，可检测绕过，又不在中间件失效时清空整个实例。不得因这些探针调用全局 DELETE /api/trash 或绕过 common 的 --allow-destructive 护栏。
- JSON POST /api/categories、PATCH /api/categories/{id}、DELETE /api/categories/{id}?mode=move&targetCategoryId={ownedTarget}，覆盖同样坏头。坏 Host 的 GET /api/trash 也应只有400错误信封而无数据正文。
- 每一矩阵步骤后或分组后，以实际 API 读回/完整归类快照/本 run 活跃及回收记录证明零写入，保留 title/note/categoryId/updatedAt/来源字段和计数。测试对自己夹具操作，不能假设全库为空或回收站为0；不清理非本 run 记录。旧 tracker 的实际接口必须保留，失败要保留诊断而非捕获后假通过。

A20.goal 追加该 P1 安全负例范围；保留原参考/阶段，不增删 ID。文档无需把未修改程序描述为实现这些新增矩阵。别把后续建议的空状态、标签、导入导出等升级为本轮门槛。

## 停止与报告

补丁须准确回传 input.json 的 base_proposal_digest；architecture_markdown 只允许唯一原文片段替换；A09/A20.goal 可用同版本锁定的 path+new，完整保留原承诺。所有未涉及字段保持原值。若预审仅指出可选完善或无依据的夹具猜测，保留待确认，不无限扩张；真正契约矛盾仍必须阻断。冻结后做独立完整静态审阅和主机 node --check，不能宣称应用/验收已运行。
