# U17 页面打磨计划

日期：2026-09-24  
依据：[U17_PAGE_AUDIT.md](U17_PAGE_AUDIT.md)  
目标：在不扩大云端/provider 能力、不削弱本地安全边界的前提下，让每个页面的状态、下一步、错误和恢复都可理解、可验证。

## 1. 优先级和原则

### P1：先保证页面不说错、不让用户误操作

- PAGE-001 类型页正式资料 404。
- PAGE-002 草稿轮询失败静默沿用旧状态。
- PAGE-003 项目列表资料集的项目切换隔离。
- 其他任何会导致错误项目、错误执行状态、错误完成结论的问题。

### P2：完成可用性和可访问性闭环

- 搜索页可直接改写查询。
- 教程语言一致。
- 未知路由有明确 404 语义。
- 移动端横向溢出、表单 label、错误边界和返回路径。
- 页面级 E2E 覆盖。

### P3：内容密度和维护性

- Apps 空态/过滤。
- 空搜索语义。
- AppShell meta 降级。
- 项目工作台按领域拆分，不改变状态模型。

## 2. 阶段计划

### Phase 0 · 建立页面门禁（先做）

**目标**：让后续每次修改都能知道影响哪些页面。

1. 建立路由清单测试：首页、浏览、叶子、搜索、应用、草稿列表、草稿详情、项目列表、项目详情、教程、未知路由。
2. 每个关键页面至少覆盖：正常、加载失败、空数据、API 404/409、移动 375px。
3. 加入语言切换检查：壳层、主要按钮、错误/空态、教程正文。
4. 加入项目切换慢网测试：mock 延迟 A/B 项目 workspace 和 references，断言旧数据不渲染、不发送写操作。
5. 加入未知路由和长内容测试：长 URL、长 slug、长错误信息不撑破 body。

**完成标准**：

- 页面矩阵在 CI 可重复运行。
- 失败报告包含 route、viewport、状态和 console/network 证据。
- 不把真实 provider 调用放进页面 E2E。

### Phase 1 · 正确性和恢复（阻断项）

#### T-P0-001：草稿正文不可绕过 dirty 状态发布

- 文件：`atlas-web/src/routes/drafts.tsx`、`application-atlas-production-pack/drafts_api.py`、`promote_draft.py`。
- 设计：查重、翻译、入库都必须绑定当前 `body_revision`/hash；dirty 时前端禁用，服务端对 revision 不一致返回 409。
- 验收：未保存正文不能发布；并发修改后直接调用 API 也不能发布旧/混合内容。

#### T-P0-002：生成完成 hydration 与 generation 列表新鲜度

- 文件：`atlas-web/src/routes/drafts.tsx`、`atlas-web/src/routes/project-detail.tsx`、`atlas-web/src/lib/atlas.ts`。
- 设计：无本地修改时自动同步生成正文；活跃 generation 列表禁用 15 秒缓存；响应带 identity/sequence，禁止旧响应覆盖新状态。
- 验收：初次空正文 → 轮询完成 → 一个周期内显示生成正文；启动 run 后下一轮仍显示 queued/running。

#### T-P0-003：发布状态冲突 fail closed

- 文件：草稿 API、review store、promotion 发布流程、`drafts.tsx`。
- 设计：frontmatter、review、canonical 文件必须形成唯一有效状态；不一致时只读并显示恢复动作。
- 验收：现有“已发布但仍为草稿”记录不会再开放编辑/删除；迁移或显式修复有测试。

#### T-P1-001：正式资料 source 映射

- 文件：`atlas-web/src/routes/leaf.tsx`、`atlas-web/src/components/source-reader.tsx`、`atlas-web/src/lib/atlas.ts`、必要时 `application-atlas-production-pack/atlas_sources.py`。
- 设计：区分“叶子 slug”和“正式资料 source slug”；无资料时显示稳定空态，不发预期 404。
- 验收：选有资料和无资料叶子各一个；无 404 console error；收藏仍固定正确 source kind/version。
- 验证：Playwright 双场景 + API source manifest 回归。

#### T-P1-002：草稿轮询状态机

- 文件：`atlas-web/src/routes/drafts.tsx`。
- 设计：`connected / stale / reconnecting / failed`；记录最后成功更新时间；失败后显示重试，不再吞错。
- 验收：模拟生成中 API 失败、恢复、组件卸载；旧数据有明确“可能已过期”提示；恢复后更新时间刷新。
- 验证：fake timer/网络拦截 E2E + 前端状态单元测试。

#### T-P1-003：项目列表资料切换隔离

- 文件：`atlas-web/src/routes/projects.tsx`、`atlas-web/src/components/loaders.tsx`。
- 设计：项目 ID 变化立即清空旧 data，或用 project identity guard；保存/刷新按钮在 data identity 不匹配时禁用。
- 验收：A→B 慢网切换时看不到 A 资料，也不能用 A 资料操作 B；失败后显示 B 的错误。
- 验证：Playwright 双项目/双 reference 场景。

#### T-P1-004：项目详情子状态绑定

- 文件：`atlas-web/src/routes/project-detail.tsx`。
- 设计：项目级 panel 用 project key，任务表单用 iteration key；baseline/generation/selected IDs 在 identity 变化时同步清理。
- 验收：快速切换项目/迭代时没有旧基线、旧运行或旧选择项；提交不会携带旧 identity。

#### T-P1-005：执行尝试版本同步

- 文件：`atlas-web/src/routes/project-detail.tsx`、`atlas-web/src/lib/atlas.ts`。
- 设计：同一 execution ID 的 `updated_at`、状态和证据变化也触发 live state 更新；避免只依赖 `id`。
- 验收：reconcile、恢复、后台刷新后任务卡在一次刷新内显示最新事实。

#### T-P1-006：草稿生成 lease、失败收口和原子写入

- 文件：`application-atlas-production-pack/drafts_api.py`、`draft_new.py`、`project_generation.py` 相关恢复逻辑。
- 设计：无 owner 的 queued/generating 启动时收口；可重试；主文件、identity、research、翻译 sidecar 原子替换。
- 验收：在 assemble/identity/refresh 各阶段中断后，旧完整版本仍可读，页面不无限 generating。

#### T-P1-007：slug namespace 与跨 API 写入互斥

- 文件：`drafts_api.py`、`draft_new.py`、`review_store.py`。
- 设计：O_EXCL/文件锁；严格 slug schema；删除清理 sidecar/review；保存/查重/promote 绑定 revision；promotion 跨进程锁。
- 验收：100 个同名并发请求恰好一个成功；空/非法 slug 400；revision 冲突 409；无双进程回退状态。

#### T-P1-008：翻译任务和 dirty 导航保护

- 文件：草稿 API、`drafts.tsx`、路由 blocker。
- 设计：single-flight、source hash、状态轮询、Abort/cleanup；Router blocker 保护所有离开路径。
- 验收：重复点击/删除/保存/离开不会产生旧翻译覆盖或正文丢失。

#### T-P1-009：统一页面级错误和返回路径

- 文件：`atlas-web/src/components/loaders.tsx`、`atlas-web/src/app.tsx`、各 route 错误出口。
- 设计：API 错误显示可读原因、返回列表/上一页、重试和 details；增加 route error boundary。
- 验收：项目不存在、草稿不存在、资料 API 失败、chunk 加载失败都有下一步，不依赖浏览器后退。

### Phase 1.5 · 公共内容与工作台 P1 收口

#### T-P1-010：搜索索引和结果页

- 文件：`atlas-web/scripts/gen-data.py`、`atlas-web/src/lib/atlas.ts`、`atlas-web/src/routes/search.tsx`。
- 设计：保留 aliases、应用别名和双语字段；页面内搜索编辑；高结果量分页/上限。
- 验收：待办事项软件、缺陷跟踪器、TickTick 等别名可命中；无结果可直接改词；查询 URL 可回退/前进。

#### T-P1-011：资料阅读器和关系数据

- 文件：`leaf.tsx`、`source-reader.tsx`、`gen-data.py`、`verify-web-data.py`、`vite.config.ts`。
- 设计：无 API 使用 `full_md` fallback 或明确 API-only；关系使用稳定唯一 ID；校验所有目标和重复关系。
- 验收：preview 无 API 不出现未处理 404；全量 leaf crawl 无 duplicate key/死链。

#### T-P1-012：工作台状态和版本 CAS

- 文件：`project_store.py`、`project_baseline.py`、`project-detail.tsx`、`atlas.ts`。
- 设计：验收使用正确 ignore 配置；最新 execution 投影；文档/需求 approval 带 expected version/revision。
- 验收：focus、空 focus、.git/node_modules、旧 execution 迟到更新和 stale approval 均有回归。

#### T-P1-013：权限、验证和扫描资源边界

- 文件：`execution_service.py`、`opencode_permissions.py`、`workspace_snapshot.py`、`project_backup.py`。
- 设计：权限回复校验 resource/pattern；固定验证保护测试/fixture；扫描和复制有根目录/文件数/字节上限。
- 验收：越界权限拒绝；agent 改测试不能产生 Atlas 通过；大目录快速失败。

#### T-P1-014：generation/delete 和 restore journal 对齐

- 文件：`drafts_api.py`、`project_generation.py`、`project_backup.py`。
- 设计：共享项目生命周期锁；old fingerprint fail closed；hard-link marker 和目标 identity 可验证。
- 验收：删除后无新 artifact；每个 restore 崩溃窗口都有明确可恢复/人工介入状态。

### Phase 2 · 页面完成度

#### T-P2-001：搜索页查询编辑

- 文件：`atlas-web/src/routes/search.tsx`、`atlas-web/src/lib/lang.tsx`。
- 设计：页面内 input、清空、提交、URL 同步、查询长度/空查询提示；保留类型/应用结果分组。
- 验收：空查询、无结果、修改查询、刷新/分享 URL 都可恢复。

#### T-P2-002：未知路由和移动溢出

- 文件：`atlas-web/src/app.tsx`、`atlas-web/src/components/app-shell.tsx`、`atlas-web/src/components/prose.tsx`、页面布局容器。
- 设计：Not Found 页面；长 URL/code/路径使用安全换行；区分导航内部横向滚动和 body overflow。
- 验收：320/375/768px 无非预期 body 横向滚动；导航仍可键盘访问。

#### T-P2-003：表单可访问性和统一文案

- 文件：草稿详情、项目表单、公共 Field/TextArea 组件。
- 设计：所有输入有 label；错误用 `aria-describedby`；readonly、busy、danger 状态可读；中英文同步。
- 验收：自动扫描无未命名可见控件；键盘可完成创建、保存、删除确认和恢复确认。

#### T-P2-004：教程语言和版本同步

- 文件：`TUTORIAL.md`、英文教程源（如采用）、`atlas-web/src/routes/tutorial.tsx`。
- 设计：英文模式不混用长段中文；命令、路径、危险边界原文保留；教程中的版本/能力与发布清单同步。
- 验收：中文/英文各跑一次首页→教程→项目入口；无失效路径或过时承诺。

#### T-P2-005：草稿 API 错误契约、队列和 provider 告知

- 文件：`drafts_api.py`、`drafts.tsx`、`lang.tsx`、创建页文案。
- 设计：严格 schema、稳定错误 code、队列上限/取消、GET 只读、provider 外发字段提示和敏感 URL 最小化。
- 验收：类型/长度/控制字符/未知字段、非 JSON、409/413/415/500 均有可读本地化反馈。

#### T-P2-006：应用目录和空态

- 文件：`atlas-web/src/routes/apps.tsx`、必要时 `lang.tsx`。
- 设计：空数据文案、搜索/过滤、目录级资料深度说明、未归类产品的下一步。
- 验收：0、1、33 条数据都可理解；移动端卡片操作不溢出。

### Phase 3 · 工作台维护性和性能

#### T-P3-001：拆分项目详情领域组件

- 文件：`atlas-web/src/routes/project-detail.tsx` 及新建同目录组件。
- 顺序：状态头/基线、生成与开放项、需求决定文档、迭代任务、执行结果、验收/导出。
- 约束：先补行为测试，再拆分；不重新发明状态模型。
- 验收：每个组件有 props/状态边界；项目详情关键 E2E 不回归；单文件明显缩短。

#### T-P3-002：请求取消和缓存策略

- 文件：`atlas-web/src/lib/atlas.ts`、公共 loader。
- 设计：AbortController、依赖切换取消旧请求；读写后统一失效；避免旧请求覆盖新项目。
- 验收：快速切换/刷新不会被过期响应覆盖；重复轮询不产生泄漏。

#### T-P3-003：性能预算

- 文件：`atlas-web/vite.config.ts`、路由入口、公共组件。
- 设计：保留当前路由懒加载，设定主入口/页面 chunk 预算；记录真实加载指标。
- 验收：构建无 500 kB 警告；首屏和项目详情首次加载时间可记录；不牺牲错误边界。

## 3. 页面级验收矩阵

| 页面 | 正常 | 空/无权限 | 错误 | 移动 | 语言 |
|---|---|---|---|---|---|
| AppShell | 导航/语言 | meta 缺失降级 | API 失败提示 | 导航不撑 body | 标签/状态切换 |
| Home | 搜索/案例入口 | meta 缺失 | 数据失败可重试 | 320/375px | 主要文案 |
| Browse | 展开/叶子跳转 | 无领域 | 单领域重试 | 无 body overflow | 全部标题 |
| Leaf | 正文/关系/收藏 | 无正式资料 | source API 失败 | 长 URL 换行 | 双语正文 |
| Search | 结果/清除 | 无查询/无结果 | index 失败 | 输入可用 | 查询提示 |
| Apps | 卡片/类型链接 | 0 apps | data 失败 | 卡片不溢出 | 深度说明 |
| Drafts | 新建/轮询 | 无草稿 | 轮询断开/重试 | 表单可用 | 状态/错误 |
| Draft detail | 编辑/保存/删除 | 无 generation log | 保存/删除失败 | textarea 可访问 | 全流程 |
| Projects | 创建/切换/备份/删除 | 无项目/无资料 | 409/备份失败 | 表单/卡片 | 确认文案 |
| Project detail | 四阶段主路径 | 无迭代/无基线 | 执行/应用/验收失败 | 长 evidence | 状态/恢复 |
| Tutorial | 阅读/入口 | 缺章节 | raw import 失败 | 长代码/路径 | 正文语言 |
| Not Found | 返回/搜索 | — | — | 375px | 全部文案 |

## 4. 每项工作的完成定义

1. 页面状态由后端事实或明确的前端状态机驱动。
2. 正常、空、加载、错误、处理中、成功和恢复状态都有可读反馈。
3. 高影响动作有明确前置条件、确认和结果。
4. 中英文文案、错误、文档和教程同步。
5. 至少一条真实浏览器路径和一条失败/恢复路径通过。
6. 不新增自动重放、自动删除、越权写入或未声明的网络/文件副作用。
7. 记录证据和剩余限制到发布清单。

## 5. 非目标

- 不通过本计划扩展云端、多人协作、provider 矩阵或自动发布。
- 不把 loopback、Basic 认证、隔离副本或固定验证器描述为 OS/容器沙箱。
- 不为了页面视觉重排而改变执行、权限、验收和恢复事实。
- 不在 provider 凭据缺失时伪造真实模型成功结果。

## 6. 推荐执行顺序

1. Phase 0 页面门禁。
2. 先关闭 DRAFT-001/002/003 三个 P0：dirty 发布、生成 hydration、generation 缓存。
3. 关闭 DRAFT-004 发布状态冲突和 DRAFT-005～010 的恢复/并发/导航问题。
4. 再处理 source 404、项目 identity、移动溢出、搜索、教程语言和可访问性。
5. 最后再做 Apps 空态、项目详情拆分和性能预算。

## 7. 当前状态

- [x] 页面静态清单和首轮浏览器巡检
- [x] 记录已复现的 source 404、移动溢出、textarea label 和 fallback 问题
- [x] 回收并记录独立草稿流程审查的 P0/P1/P2 发现
- [x] Phase 0 页面 E2E 门禁（T019：10 路由正常/错误/代表空态、语言、无障碍、375/768px；51/51）
- [x] Phase 1 草稿 P0/P1 正确性修复（T002–T005、T015）
- [x] Phase 2 页面完成度（T006–T017、T019）
- [x] Phase 3 工作台拆分与性能（T008–T010、T014、T018；主入口仍低于 500 kB）
