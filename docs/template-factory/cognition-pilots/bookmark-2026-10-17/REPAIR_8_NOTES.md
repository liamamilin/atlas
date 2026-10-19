# 本轮修订：补齐当前场景的用户主线与一致契约

基于冻结 v0.1.5；本轮 reuse_spec=false，必须修订规范并经过独立设计预审，预审之后才编写受影响程序。仍是“生活待购与灵感收藏夹”，不新增企业能力，不发布、不安装、不运行任何生成程序或应用。复用已有结构化调研，不搜索新资料。标题与架构标题用不含版本号的产品名称；移除架构开头过时的文件修订名单/历史迭代叙述。尽量保持 25 个能力、9 个决策、P0–P2、A01–A33 的身份与阶段，只扩展受影响现有用例的行为和映射；不要为了数量凑要求。

## 真正要修好的体验

1. P1 列表行提供单条软删除表单 bookmark-delete-form（POST {basePath}/bookmarks/{id}/delete，按钮 bookmark-delete-submit）。成功 303 回首页并显示非空 flash，可逆软删除不强制再确认。P1 页面提供真实 trash-link 导航到带前缀的 /trash；回收站提供 home-link 返回库。A31 必须从真实列表点击软删除，用真实导航进入回收站，恢复到原活跃归类；另外用独立记录验证明确选择另一活跃归类恢复。API 可用于准备前置和旁路确认，但不能用 API DELETE 替代这次用户点击删除。保留 id/url/createdAt、计数与刷新持久断言。不得假设 A30 的 purge 记录就是 A31 的原归类记录。
2. P0 重复保存的完整恢复：默认不写入，显示 form-error 并保留用户字段；duplicate-existing-link 链接指向已存在记录的 /b/{existingId}；提供显式 duplicate-save-form + duplicate-save-submit（同 POST /bookmarks，隐藏 allowDuplicate=true，带回原始 url/title/note/categoryId），明确“仍然保存一份”。只可在冲突后显示该操作，首次普通提交不自动带 true。成功 303，创建新 id，既有记录原样；A28 覆盖提示、链接 href、未确认零写入、显式另存后 +1 且新旧两条都存在。P0 不调用创建归类或检索 API。A28 的真实打开外部夹具/分页/空状态已有边界保留。
3. P1 保存表单 select[name=categoryId] 列出所有活跃归类、默认选默认归类，tombstone 不出现。A29 用 UI 新建归类后回首页，直接选择该归类保存，断言 DOM/data-category-id/API/刷新后保持；原移动、重命名、编辑断言保留，并加重名归类失败不写入。category 视图不必有首页 bookmark-form，当前 reloadHome 在归类页会错误等待它，必须 gotoHome 后再检查/重返归类。不要发明 browser.cjs 未导出的助手。
4. F04 的 URL 与创建时间实落到 bookmark-url 与 time[data-testid=bookmark-created][datetime]；文本 URL 与原始 URL 一致，datetime 与 API createdAt 一致；A28 对自己新建行断言，不要求具体本地化日期格式。

## 安全与数据契约

5. Host 检查覆盖所有读取页面、打开重定向和 API（GET /、/c/:id、/trash、/b/:id、/api/bookmarks、单条、/api/categories、/api/trash；health 也可一致检查）。所有请求的 Host 必须等于配置 origin 的 host（含非默认端口），不信任任意 X-Forwarded-Host。Origin/Fetch Metadata 限制用于 unsafe method，允许没有这些头的原生 HTTP 客户端。PUBLIC_ORIGIN 明确默认 http://127.0.0.1:3000；端口/主机变更或代理部署必须显式配置；非法配置启动失败；默认仅绑定 127.0.0.1。该单人版本没有内置账号认证，“本机访问边界”不是认证，不得继续写成已实现无匿名读取；向非回环网络开放必须先配认证反向代理。Host 防护是 DNS rebinding 防线，不代替认证。A09 错误 Host 的 GET（数据 API 与首页/打开路由的代表项）返回 400 invalid_host，无数据正文；保留原 unsafe Origin/FetchMetadata 负例与无写入断言。只向已配置测试目标发送伪造 Host，不访问任何外站。
6. POST categoryId 缺省或 null -> 默认归类；PATCH categoryId null/空串 -> 400 invalid_category，其余非法形状保持 invalid_category。不要破坏 A03 两次保存和默认归类断言。
7. URL 在 trim/WHATWG 解析前检查原始输入，含任何 C0 U+0000–001F 或 DEL U+007F -> 400 invalid_url, details.reason=control_character；不让 WHATWG 静默去掉 CR/LF。Location 输出前再次检验已存 URL，历史非法值不得输出头，应返回 500 internal。A09 加 CR/LF/Tab 等代表性 POST 负例及零写入。title/note 只拒绝索引分隔符 U+0001（invalid_title/invalid_note），其他已有合法 Tab/换行备注与派生标题语义保持；q 含 U+0001 -> 400 invalid_query（P2），防止跨字段匹配。相应 A09/A21–A27 受影响现有用例覆盖，阶段不提前调用后期 API。
8. common.request 必须在获取/附加认证头和发起请求前验证 URL：仅允许配置 origin、无 userinfo、且处于配置 basePath 的路径段边界内（/bookmarks 不包含 /bookmarks-evil 或 /other）。拒绝绝对外域、协议相对外域、路径穿越归一后的越界；新 URL 的规范化结果用于检查和实际请求。redirect 始终 manual，拒绝 follow，不带头跟随外域。错误作为 infrastructure/incomplete（ATLAS_TARGET_BOUNDARY），不输出凭据或带 userinfo URL。relative /api/... 仍是相对配置 appBase 拼接，保留子路径。可在 A09 用合成 Authorization 哨兵做无网络前置拒绝断言，不读真实凭据。browser.cjs 现有 withPage 非空 auth 在 browser/context/page 创建前拒绝且不设置全局 extraHTTPHeaders 的修复原样保留。
9. success JSON 的资源 id/categoryId/existingId/targetCategoryId/deletedCategoryId/restoredToCategoryId/trashedFromCategoryId 统一十进制字符串，允许契约明确的 null。可在 common 的 API wrapper 或 request 成功 JSON 返回处集中断言字段，防止各测试先 String() 掩盖类型；不要把 health.instanceId/version 等当十进制资源 ID，也不要破坏错误信封原值检查。
10. A14 归类 purge 检查 trashedFromCategoryId、trashedFromCategoryName 来自已 tombstone 原归类，同时保留已有回收项的来源不变；A15 对默认归类 mode=purge&confirm=true 也应 409 default_category_protected，零写入。保留名称 tombstone 后可复用语义。

## 验收的安全和可重复性

11. 为全局清空回收站加 --allow-destructive 布尔 flag（无隐式环境默认授权）。run.cjs 传到 ctx.allowDestructive；common.request 在任何 DELETE /api/trash（精确路由，无论 query）发请求前拒绝缺少 true 的 ctx，infrastructure ATLAS_DESTRUCTIVE_NOT_ACKNOWLEDGED，A18 因此记 incomplete/退出 2，不能跳过后声称全通过。普通 DELETE /api/trash/:ownedId 的本次夹具清理不受影响；有 flag 也仅可对专用实例运行。health.stage 继续是 P0/P1/P2，不能伪造为 test。此 flag 是下游运行者的确认开关，不是本次执行程序的授权。A30 UI 全局清空正例仍为显式未运行手工项，不能清现有库凑测试。README 命令/退出码与架构统一。
12. A33 用真实 UI 翻页验证 q、categoryId、sort、limit 的保留，使用本 run 的独立记录；分页不会对全库空白作假设。如果当前结构不便，使用 home query categoryId 页面验证交集再点真实 next/prev，仍需存在对应 DOM 契约与结果断言。
13. 不要破坏已有修复：A19 countsBefore 在创建记录之后；A03 缺省与空白标题两次保存 +2；A30 同一次 suite runId 可能带此前 A20 回收项，不能断言 baseline trashed=0，preexistingTrashIds 必须原样保留；staleSnapshotBefore 是操作前真实快照；basePath 浏览器导航通过已有 browser.appUrl/pathFor 或等价可靠拼接；浏览器实际 flag 是 --with-ui，不能杜撰 --runner。

## 文件边界与真实证据

只生成 edit_paths 内确需改动文件，未选文件复制字节不变。预计：common.cjs、run.cjs、p0-limits.cjs、p1-categories.cjs、p2-search.cjs、ui-p0.cjs、ui-p1.cjs、ui-p2.cjs、README.md。逐文件读现有依赖的真实导出后再改，优先精确替换/小范围补充，不重写整个巨型文件。file_plan 的目的需说明上述哪几项由该文件负责，既有文件职责/导出不能随意改变。被要求复用的文件不能在新 spec 中声称它们实现了新增断言。所有阶段仍 not implemented，所有案例 not_run；即使设计或静态程序审阅通过也不是运行通过，不添加证据。独立设计审阅若提出无法从草案证明的历史实现猜测，按当前明确契约判断，不扩张为与场景无关的门槛。


## 本轮追加且优先的 URL 存储与 HTTP 传输契约

独立架构复审已确认：把含中文、IDN 或空格的合法原始 URL 直接放进 HTTP Location，不符合当前 Node/Fastify 目标的响应头约束。主机只调用 Node 内建 http.validateHeaderValue 验证固定合成 URL（没有运行应用/模板程序或发网络请求），原始中文值抛 ERR_INVALID_CHAR，new URL(raw).href 的 ASCII 值通过。参考 Node 22 HTTP 文档 https://nodejs.org/docs/latest-v22.x/api/http.html#httpvalidateheadervaluename-value 与 URL serializer https://url.spec.whatwg.org/#concept-url-serializer 。这是修正技术契约，不是缩减功能或新增业务决策。

1. 数据库 bookmark.url、API JSON url、列表 bookmark-url 保留通过输入校验并 trim 后的原始 Unicode 字符串，逐字符往返。不要把数据存储改成 canonical URL，也不要改变 url_key 的保守去重策略。
2. GET /b/:id 的 Location 固定为 new URL(bookmark.url).href（WHATWG URL serializer 的 ASCII 结果）：IDN 转 ASCII 主机名，路径/查询/片段需要编码的字符按标准编码。保持查询参数、UTM 与 fragment 的意义，不删除、不排序。不能继续承诺 Location 与原始输入逐字符相等；应断言 Location 与该序列化结果逐字符相等。浏览器真实导航断言也比较 URL 序列化结果。
3. C0/DEL/CRLF 的输入拒绝与打开前重新检查保持；非法旧数据返回 500 internal，不能靠序列化默默修复控制字符。无须抓取目标、改变来源授权或实现下游应用。
4. 原 A05 身份/阶段不变，扩展其 goal 和 acceptance/p0-library.cjs：保留现有 ASCII 打开、精确目标/302、不跟随重定向及未找到负例，另保存一个含中文/IDN/空格的固定合成 .invalid URL，验证 API 读回原始字符串、Location 为标准序列化且可作合法 ASCII 头值。所有 HTTP 请求仍只发配置目标，绝不能联网访问 .invalid 地址。不要先 new URL(...).href 再保存，否则没有验证原始 Unicode 往返。
5. 必须将现有 acceptance/p0-library.cjs 的 file_plan reuse 改为 false（file_plan_changes），更新其 A05 职责。改动许可范围从原九文件扩为十文件；其余未选程序仍字节复用。可按需要局部澄清 F05 reason、D05 default/impact、A05 goal 与架构的混淆表述；保留角色/能力/决策/阶段/案例身份及所有无关承诺。其它已经明确的主流程、活跃记录去重、双表单 purge、计数/安全护栏均保留。不要因一个 URL 传输问题重写整个规范。
