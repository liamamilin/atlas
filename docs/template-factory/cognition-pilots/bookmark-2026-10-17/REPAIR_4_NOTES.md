# v0.1.2 复审的核心问题修复（在 v0.1.3 上继续）

依据真实独立复审 job_4951e6356c7c46ec9e9417676eaaaed5。v0.1.3 只修浏览器认证头边界，以下原问题仍需修。保持同一场景、调研、25 能力、9 决策、三阶段、33 个 A01–A33 ID；更新现有 case 内容与双向映射，不新增企业功能或 P3 实现，不联网、不运行代码/应用、不安装、不发布。其他未选中文件由主机按冻结字节复用，不能要求重写。新包仍是未实现/未运行候选。

## 必须修复的明确矛盾

1. A19 的 countsBefore 在创建测试书签前采集，最后却断言同一计数，是正确实现也无法通过的假失败。把“编辑不改变记录数量”的基线移到创建之后（或明确加 1），保留所有编辑、非法输入与状态断言，不删除计数检查。
2. A03 已实际保存两条默认归类记录、断言 bookmarkCount 增加 2。统一 spec 中 goal、阶段文字与程序元数据为两次保存增加 2，不删掉新增的空白标题测试，不继续宣称 +1。
3. ARCHITECTURE 请求体 categoryId 的非法/非数字类型统一 400 invalid_category，不再允许 invalid_field 二选一；原因按上下文分别 unknown_or_deleted、target_unavailable、自指等既有契约。PATCH 显式 url 一律 400 invalid_field、details.field=url，整笔零写入；仅未知字段/空 body 400 empty_patch。对已回收书签的合法形状 PATCH 为 404 not_found。归类 purge 将本次 active 书签的 trashed_from_category_id 设为原归类并保留 tombstone；已回收记录的来源不被本次操作覆盖。读取现有 A17/A20，确保规范与其实际数据生命周期一致，不改错误码迎合不明确文本。
4. 排序和分页状态写入 URL query，刷新/重开保持：sort=created_asc/created_desc、limit、offset；改变归类或排序时 offset 归零。API openPath 仍是不带部署前缀的 /b/{id}，UI href 才加 basePath。A28 的 URL input 使用 type=text 或 form novalidate，让非法输入到服务端并显示 form-error，避免测试要求与原生阻止提交冲突。note 的数据保存不 trim（检索可另行标准化），搜索索引在标题/备注编辑后同步更新。

## 补齐已承诺用户能力的 UI 契约和现有浏览器用例

不是新增产品能力：F08 的归类重命名、F12 的标题/备注编辑、F04 的分页、F10 的安全 move 删除以及 F13 的单条永久删除都已经是 current required，不能只让 HTTP 客户端用到。

- 架构列出真实表单路径、字段、data-testid、303/错误反馈及持久化预期。推荐：category-rename-form（绑定 data-category-id，name 字段）、bookmark-edit-form（绑定 data-bookmark-id，title/note 字段）、page-prev/page-next（真实 href，边界不可点击）、trash-delete 的明确确认控件。测试可直接用明确 DOM selector，不需要改 browser helper 的既有接口。保留 v0.1.3 的浏览器认证头前置拒绝，不重新引入全局头。
- A29 扩展现有 P1 浏览器流程：创建/重命名归类（正常、空名称反馈）、编辑已有书签标题与原样备注（正常、纯空白标题反馈），刷新后读回且数量稳定；保持原本的移动和空 PATCH 断言。需要的 F08/F12 等双向映射一并更新。不要把只发 HTTP 当 UI 编辑成功。
- A30 保留取消、purge、回收站恢复断言，增加 mode=move 的真实选择/提交及“移动后仍在库且不是 purge”的检查；可用实际 API 在对话框打开后使目标失效来测试 stale target 零写入，不伪造响应/改 DOM。补单条永久删除的 UI 确认与其他回收记录未误删。已有清空 UI 继续保留；不要为了测试清空真实库，只运行在以后明确提供的专用实例，本次不执行。
- A28 补分页控件的真实点击、URL 参数与前后页不同记录/边界行为，使用当前已创建夹具或专用实例可用记录；不得依赖 P1 删除、P2 q 或客户端伪造服务端分页。首页/空归类/空搜索/空回收站的 DOM 文案与状态写清楚。首页空库可列明“对全新专用实例手工核对，状态未运行”，不要为此清库、增加隔离代理框架或跳过后谎称自动测试已覆盖；A28 自身只宣称其实际断言覆盖。

## 当前范围内的少量关键负例

- p1-edit 在现有用例验证 PATCH url 拒绝、categoryId=null、仅未知字段不写入；备注前后空白保留；对应现有规范，不加阶段。
- p2-search 在现有 P2 case 验证修改标题/备注后旧词不再命中、新词命中，走真实服务端 q，允许依赖已交付 P1 PATCH。
- p0-limits 的现有归一用例补非默认端口保留、路径大小写保留、WHATWG 可解析的 http:///path 正常归一。不要错误地把它判成缺 host；https:// 才不可解析。
- 声明所有变更数据的 API/表单都校验配置的 Host；unsafe 请求若有 Origin 必须与配置 origin 完全一致，Origin:null 和外站均 403 forbidden_origin；Sec-Fetch-Site=cross-site 也拒绝。允许没有 Origin/Fetch Metadata 的显式原生 HTTP 验收客户端，不能因此要求其他 18 个 helper 都重写。Host 非配置值 400 invalid_host，防 DNS 重绑定。D06 说明现代浏览器跨站表单威胁及远程部署配置边界，不要求部署公开无认证服务。p0-limits 现有请求拒绝用例加入实际目标的错误 Origin/Host、无部分写入检查；通过 common.request 的 settings.headers 传头，仅请求 ctx.baseUrl，不实际访问恶意站点。保持正常 UI 同源提交与原生 HTTP case 可运行；不把“监听回环”当成完整 CSRF 防护。

## 文件与交接

只允许修改 acceptance/p0-save.cjs、acceptance/p0-limits.cjs、acceptance/p1-edit.cjs、acceptance/p2-search.cjs、acceptance/ui-p0.cjs、acceptance/ui-p1.cjs、acceptance/README.md（主机 edit_paths）。完整计划仍列出原 20 个生成文件，其他 13 个 reuse=true，既有 helper/runner/依赖不改。可在 spec 的架构与已有能力/用例说明中补以上内容，但不扩展数量。不要输出未列入范围的新文件。

README 写“20 个作者生成文件 + Atlas 的 plan.json，共 21 个 acceptance 文件”，列出准确入口/真实部署前缀/专用实例前提/未实现及未运行状态。保持 HTTP 认证参数与浏览器不支持认证参数的事实边界。不要声称通过应用验收；独立静态审阅不替代执行。可选建议与未执行的手工观察明确列为未验证，不额外制造本轮 release 硬要求。
