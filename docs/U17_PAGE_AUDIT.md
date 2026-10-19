# U17 页面系统审查

日期：2026-09-24  
范围：`atlas-web/src/app.tsx`、全局壳层、10 个用户路由、页面共用组件、前端 API 契约和对应本地 API 路由。  
方法：静态代码审查 + 隔离本地 API/前端真实浏览器巡检 + 现有单元/E2E/后端回归证据。  
状态：首轮页面巡检和独立草稿流程审查结果已记录；T002–T019 已完成并以回归证据复核；最终跨环境验证仍待单独记录。

## 1. 总结

- 当前有效页面均能在隔离本地服务中打开；桌面巡检没有发现 `pageerror`。
- 类型叶子页存在一个可复现的功能缺口：没有对应正式资料 slug 时，`SourceReader` 仍无条件请求 `/api/sources/<leaf-slug>`，产生 404；页面主体可见，但正式资料阅读器显示错误。
- 草稿生成轮询忽略轮询请求错误，页面可能长时间显示旧进度而没有“已断开/重试”提示。
- 移动视口存在真实横向溢出：类型叶子页约 425px/375px，浏览页约 380px/375px；草稿详情有一个无可访问名称的正文 textarea。
- 项目列表切换当前项目时，资料集依赖通用 `useAsync` 保留旧 data；需要在慢网络/缓存命中条件下补充回归，确认不会显示或操作旧项目资料。
- `/search` 没有页面内搜索输入；无查询或无结果时只能返回其他页面，无法直接改写查询。
- 英文模式只切换壳层和局部文案，教程正文仍直接加载中文 `TUTORIAL.md`。
- 未知路由当前静默渲染首页，HTTP 仍为 200；这会让用户误以为路径有效。
- 当前浏览器自动化只覆盖 3 个核心 E2E 场景，页面矩阵、移动视口、错误注入、语言切换和项目切换仍缺少可重复门禁。

首轮浏览器巡检没有发现立即导致服务完全不可用的 P0；但独立草稿流程静态审查确认了可导致错误发布和生成结果丢失的严重正确性缺口，草稿发布门禁应按 P0/P1 处理。

## 2. 巡检证据

### 2.1 真实浏览器巡检

隔离启动 `e2e/start-api.mjs` 和 Vite 后访问：

`/`、`/browse`、一个 `/types/:slug`、`/search?q=notion`、`/apps`、`/drafts`、`/drafts/e2e-draft`、`/projects`、一个 `/projects/:id`、`/tutorial` 和未知路径。

桌面结果：

- 以上有效路由均有 `main` 和 `h1`，无 page error。
- 唯一 HTTP 错误：
  - `GET /api/sources/business-messaging-application` → `404`
  - 来源：`atlas-web/src/routes/leaf.tsx:113` 无条件挂载 `SourceReader`；`atlas-web/src/components/source-reader.tsx:24` 无条件请求 source manifest。
- 未知路径 `/route-that-does-not-exist` 返回首页内容，未显示 404/路径不存在提示。

375px 移动视口结果：

- `/browse`：`scrollWidth=380`，视口 375。
- `/types/business-messaging-application`：`scrollWidth=425`，视口 375；长 URL 是主要溢出元素。
- `/drafts/e2e-draft`：发现 1 个没有可访问名称的表单控件；对应正文编辑 textarea（`drafts.tsx:540-547`）。
- 其他已巡路由没有检测到 body 横向溢出或无名称按钮。

### 2.2 自动测试覆盖

- 前端单元测试目前 6 项，主要覆盖项目状态纯函数和请求契约。
- Playwright 核心 E2E 3 项，重复 3 次共 9/9 通过：类型叶子、草稿保存/删除、API 恢复/跨源拒绝。
- 后端当前 180 项回归通过，干净 Python 3.11 环境通过。
- 尚未有逐页面的：加载失败、空数据、API 404、移动视口、语言切换、项目切换、未知路由 E2E。

## 3. 页面清单与当前判断

| 页面 | 用户任务 | 当前状态 | 主要缺口 | 优先级 |
|---|---|---|---|---|
| AppShell | 导航、语言切换、全局元信息 | 可用 | meta 请求失败无局部反馈；无 skip-link；窄屏导航依赖横向滚动 | P2 |
| `/` | 理解产品、搜索、进入案例/项目 | 可用 | 搜索空提交也进入空搜索页，需明确空查询语义 | P3 |
| `/browse` | 按领域浏览类型树 | 可用 | 移动端轻微横向溢出；同一领域只保留一个展开子域 | P2 |
| `/types/:slug` | 阅读定义、边界、关系、正式资料 | 部分可用 | 无正式资料时 404；长 URL 移动溢出；资料阅读器错误反馈过重 | P1/P2 |
| `/search` | 查找类型和应用 | 部分可用 | 无页面内搜索框；无结果时不能直接改写查询；无加载分页/大查询策略 | P2 |
| `/apps` | 浏览真实应用并固定到项目 | 可用 | 无空态文案、过滤/搜索；目录级资料与类型资料深度差异需更明显 | P2/P3 |
| `/drafts` | 新建、查看生成中的草稿 | 部分可用 | 轮询错误被吞掉；缺少断开提示和手动重试；错误仍可能只显示 HTTP 状态 | P1/P2 |
| `/drafts/:slug` | 编辑、查重、删除、晋升草稿 | 基本可用 | 正文 textarea 无可访问名称；生成/晋升失败后的下一步不够集中；页面较长 | P2 |
| `/projects` | 创建、切换、备份、删除项目 | 部分可用 | 资料集需验证项目切换时旧数据清理；fromType 状态需随 URL 变化重置；备份下载失败反馈有限 | P1/P2 |
| `/projects/:id` | 资料→范围→文档→执行→验收 | 基本可用但密度高 | 1433 行单文件；长页面操作密度高；需继续保证历史/错误/恢复动作可解释 | P2 |
| `/tutorial` | 学习完整路径 | 中文可用 | 英文模式正文仍是中文原始 Markdown；版本/路径说明需定期同步 | P2 |
| `*` | 处理未知 URL | 缺口 | 静默回首页，没有 404 语义或返回/搜索入口 | P2 |

## 4. 问题清单

### PAGE-001 · P1 · 类型页正式资料 404

- **证据**：`leaf.tsx:113` 对每个叶子无条件渲染 `SourceReader`；`source-reader.tsx:24-30` 直接以叶子 slug 请求 source manifest。
- **复现**：访问 `/types/business-messaging-application`，正式资料显示主体，但 `/api/sources/business-messaging-application` 返回 404，浏览器 console 出现资源错误。
- **影响**：用户无法区分“该类型没有正式资料”与“Atlas/API 临时故障”；页面产生错误噪声。
- **打磨要求**：建立叶子到正式资料 source manifest 的显式映射；无资料时渲染稳定的“暂无正式资料”状态，不发起预期 404；有资料时保留分页、版本和收藏动作。
- **状态**：✅ T006 已修复；缺失 manifest API 返回 200 空契约，前端使用 `full_md` 静态 fallback，Vite preview 复用受限 API proxy。

### PAGE-002 · P1 · 草稿轮询失败被静默忽略

- **证据**：`drafts.tsx:85-93`、`drafts.tsx:744-752` 的 interval 请求失败回调为空。
- **复现**：生成期间让 `/api/drafts` 或 `/api/drafts/:slug` 暂时失败，页面继续显示上一次进度，没有断开状态或重试按钮。
- **影响**：用户可能误以为 agent 仍在生成，或在旧正文上继续操作。
- **打磨要求**：区分首次加载错误和轮询断开；显示最后成功更新时间、下一次重试倒计时和手动刷新；恢复后明确提示数据已重新同步。

### PAGE-003 · P1（需慢网/缓存复现）· 项目列表资料集的项目切换隔离

- **证据**：`projects.tsx:252-262` 的 `ProjectReferences` 使用通用 `useAsync`；`components/loaders.tsx:11-17` 在依赖变化时保留旧 `data`。
- **风险**：切换当前项目时，旧项目 references 可能在请求完成前显示；用户点击保存备注时请求已经使用新 `projectId`，造成错误目标或误导。
- **打磨要求**：增加 `key={projectId}` 或 data identity guard；慢网络、缓存命中、失败和快速连续切换均需回归。

### PAGE-004 · P1 · 项目详情子面板的局部状态未完全绑定项目/迭代身份

- **证据**：`WorkspaceBaselinePanel`（`project-detail.tsx:714-740`）、`GenerationPanel`（`832-887`）和 `TaskForm`（`522-546`）在 `projectId`/`iteration` 改变时依赖异步 effect 清理，但 effect 运行前仍保留旧 baselines、runs、selected document/requirement IDs。
- **风险**：快速切换项目或迭代时，旧基线/生成历史/选择项可能短暂可见；提交动作虽然通常会被后端拒绝，但用户会得到错误目标印象。
- **打磨要求**：为项目级面板加 `key={projectId}`，为任务表单加 `key={iteration.id}`，或在 render 层验证状态 identity；慢网和连续切换必须进 E2E。

### PAGE-005 · P1 · 执行尝试实时数据只按 ID 同步

- **证据**：`ExecutionTaskCard` 的 `useEffect`（`project-detail.tsx:568-573`）依赖 `executions[0]?.id`，同一 execution ID 的状态/证据更新不会重新同步到 `live`。
- **风险**：后台 reconcile、恢复或外部刷新后，任务卡可能继续显示旧的完成/验证/权限信息，直到下一次轮询或重新挂载。
- **打磨要求**：以 execution `updated_at`/状态版本作为 identity，或直接由 workspace props 驱动并在 live 与 server 状态不一致时显示“正在刷新”。

### PAGE-006 · P2 · 搜索页没有直接改写查询的入口

- **证据**：`search.tsx:58-135` 只展示结果/空态和跳转链接，没有输入框。
- **影响**：无结果或误搜后，用户必须返回首页/浏览器后退才能改词；`q` 也没有长度/规范化提示。
- **打磨要求**：页面内提供搜索输入、提交/清除和最近查询；明确本地名称/定义检索范围；保留 URL 可分享状态。

### PAGE-007 · P2 · 英文模式的教程正文未本地化

- **证据**：`tutorial.tsx:4,18-20` 直接加载中文 `TUTORIAL.md`；`TUTORIAL.md:1` 为中文标题和正文。
- **影响**：壳层显示英文，但长教程突然切换为中文；与全局语言承诺不一致。
- **打磨要求**：提供英文教程源或明确“当前仅中文”的语言提示；链接、命令和路径保持原样，不做机器翻译式替换。

### PAGE-008 · P2 · 未知路由静默变成首页

- **证据**：`app.tsx:31` 的 `path="*"` 渲染 `Home`。
- **复现**：访问 `/route-that-does-not-exist`，HTTP 200、标题和内容均为首页。
- **影响**：用户无法知道链接失效，搜索引擎/监控也无法区分 404。
- **打磨要求**：增加明确的 Not Found 页面、返回首页/浏览/搜索入口；SPA fallback 是否返回 404 由部署边界决定，不把它包装成完整服务器 404。

### PAGE-009 · P2 · 窄屏横向溢出

- **证据**：真实 375px 巡检中 `/browse` 为 380px，`/types/:slug` 为 425px；长 URL 链接是叶子页主要溢出元素。
- **影响**：移动端出现横向滚动，长链接阅读和点击体验差。
- **打磨要求**：区分导航内部滚动和 body 溢出；修复内容 box sizing/长 URL/code 的换行策略；在 320/375/768px 加浏览器门禁。
- **状态**：✅ T012 已修复；Prose/长内容局部滚动，375px Browse/Leaf/Draft body 无横向溢出。

### PAGE-010 · P2 · 草稿正文编辑控件无可访问名称

- **证据**：`drafts.tsx:540-547` 的 `<textarea>` 没有 `<label>`、`aria-label` 或 `aria-labelledby`。
- **影响**：屏幕阅读器无法说明编辑区域用途；自动巡检已复现 1 个未命名控件。
- **打磨要求**：增加本地化 label、错误关联和读-only 状态说明；保持中文/英文同步。
- **状态**：✅ T012 已修复；正文 textarea 提供中英文 accessible name。

### PAGE-011 · P2 · 全局错误恢复和懒加载失败边界不足

- **证据**：`app.tsx:37-39` 只有 `Suspense` loading fallback；`components/loaders.tsx:31-44` 的错误态主要提供整页 reload。
- **影响**：API 错误缺少页面级返回路径；懒加载 chunk 下载失败时没有用户可理解的错误边界。
- **打磨要求**：增加 route error boundary、返回上一页/相关列表按钮和重试；不要把整页 reload 作为唯一恢复动作。
- **状态**：✅ T011 已修复；未知路由有 404 页面，data-router error boundary 提供 home/reload 恢复。

### PAGE-012 · P2 · 项目工作台单文件密度和操作可解释性

- **证据**：`project-detail.tsx` 约 1433 行，包含状态、生成、文档、执行、权限、验收、恢复和历史多个领域。
- **影响**：后续修复容易互相影响；用户很难判断当前动作影响哪个状态对象。
- **打磨要求**：先补状态/动作矩阵和 E2E，再按领域拆组件；不以视觉重排掩盖状态语义问题。每个危险动作都要有前置条件、结果和下一步文案。

### PAGE-013 · P2 · 页面级回归覆盖不足

- **证据**：当前只有 3 个核心 Playwright 场景和 6 个前端单元测试。
- **影响**：加载/错误/空态、项目切换、移动布局、语言切换和未知 URL 的回归只能靠人工发现。
- **打磨要求**：建立 10 路由 × 桌面/移动 × 正常/错误/空态矩阵；先覆盖 P1 页面，不追求一次性覆盖所有组合。

### PAGE-014 · P3 · 小型内容和空态完善

- `/apps` 数据为空时没有专门空态，应用数量少时没有过滤/搜索。
- `/` 空搜索提交应明确提示，而不是进入一个空结果页。
- AppShell meta 失败时页脚/头部静默显示省略号，需局部降级文案。
- 研究资料 reference 的链接类型需要确认：`atlas:research` 不应默认跳到叶子类型页。

## 5. 独立草稿流程审查（回收结果）

独立只读审查进一步确认草稿页是当前发布候选的主要阻断区。以下问题不是视觉偏好，而是可能造成错误发布、正文丢失或状态误报。

### DRAFT-001 · P0 · dirty 正文仍可查重/翻译/入库

- **证据**：`drafts.tsx:316-337,581-629` 允许编辑后保留 dirty 状态，但 promote 条件没有检查 dirty；`promote_draft.py:175-225` 从磁盘读取服务器旧正文。
- **影响**：用户眼前的修改可能被静默忽略，入库的是未审阅的旧正文。
- **门禁**：dirty 时禁用三类动作；API 增加 `body_revision`/hash 条件，不一致返回 409；UI 和 HTTP 都要测试。
- **状态**：✅ T002 已修复；dirty 状态和 stale hash 均有 UI/API 回归。

### DRAFT-002 · P0 · 生成完成后编辑器不载入新正文

- **证据**：`drafts.tsx:316-324` 只在首次 slug 加载时初始化 `body`；`726-754` 轮询只更新 `data`；`540-547` textarea 仍绑定旧本地 body。
- **影响**：创建后立即进入详情时，生成完成后 textarea 可能仍为空；用户编辑并保存会覆盖完整生成结果。
- **门禁**：无本地修改时，权威状态从 generating 转为 draft/failed 后一个轮询周期内同步正文；有本地修改时显示版本冲突，不静默覆盖。
- **状态**：✅ T003 已修复 hydration/轮询不重叠；dirty 状态下服务端变更提示仍归 T005。

### DRAFT-003 · P0 · generation 列表 15 秒缓存隐藏新运行

- **证据**：`atlas.ts:1-18,1030-1058` 使用 15 秒 Promise 缓存；`project-detail.tsx:832-900` 依赖列表结果决定是否继续轮询。
- **影响**：启动 generation 后下一次轮询可能读到旧列表，`hasActiveRun` 变 false，正在运行的任务从页面消失并停止刷新。
- **门禁**：活跃 generation 列表使用 no-store/不缓存请求；启动后下一轮必须看到 queued/running；旧响应不能覆盖较新状态。
- **状态**：✅ T003 已修复；generation 列表使用 `cache: "no-store"`，并有前端回归。

### DRAFT-004 · P1 · 已发布与仍是草稿的状态矛盾

- **证据**：现有 `drafts/cli-accounting-tool.md` frontmatter 仍为 `status: draft`，但 `drafts/review.json` 有 `promoted: true`，canonical 文件已存在；API 原样组合两种状态，`drafts.tsx:429-455,620-629` 会同时显示“草稿”和“已入库”，编辑/删除仍开放。
- **影响**：用户可能编辑或删除已经进入正式语料的条目。
- **门禁**：统一发布状态投影；frontmatter、review、canonical 文件不一致时默认只读并进入“状态冲突/需恢复”。
- **状态**：✅ T004 已修复；冲突状态只读，保存/查重/删除均 fail closed。

### DRAFT-005 · P1 · generating 异常后永久卡住

- **证据**：`drafts_api.py:934-978` 的部分异常可能绕过失败收口；启动恢复只处理 promoting，不处理 generating；页面会无限轮询且后端拒绝保存/删除。
- **门禁**：启动时依据 lease/heartbeat 收口无 owner 的 queued/generating；提供显式重新生成；所有 assemble/identity 写入使用原子替换。
- **状态**：✅ T005 已修复；重启将无 owner generating 收口为 failed，不自动重放，并提供显式重新生成。

### DRAFT-006 · P1 · slug 创建 TOCTOU、空 slug 和旧 review 污染

- **证据**：`drafts_api.py:1720-1738` 先检查再覆盖；`draft_new.py` 的 WIP slug 同样无锁；删除不清理 review 记录；`review_store.py:32-37` merge 会继承旧字段。
- **影响**：并发同名请求可启动多个引擎；`"!!!"` 可产生空 slug；删除重建同名可能继承 promoted/identity/verdict。
- **门禁**：文件锁或 O_EXCL namespace；空/超长/非规范 slug 返回 400；同名并发恰好一个 201，其余稳定 409；删除清理所有 sidecar/review 或使用不可复用内部 ID。
- **状态**：✅ T004 已修复；per-slug 文件锁、空 slug 400、并发单赢家和 review 清理均有回归。

### DRAFT-007 · P1 · 保存/查重/入库缺少不可变 revision

- **证据**：PUT、`/api/dedupe`、`/api/promote` 没有跨 API 进程的 `expected_revision`/hash；`PROMOTE_LOCK` 仅进程内，异常路径可能把已发布状态写回 draft。
- **影响**：最后写入者覆盖前一浏览器；双进程 promotion 可能发布后又回退状态。
- **门禁**：所有写操作绑定 body revision；查重 single-flight；promotion 状态转换使用跨进程锁，异常只由 owner 回滚。
- **状态**：✅ T002/T004 已修复；save/dedupe/promote 绑定 hash，per-slug 文件锁拒绝并发写入。

### DRAFT-008 · P1 · 翻译没有 single-flight、版本绑定和定时器清理

- **证据**：`drafts_api.py:1647-1654` 无状态启动线程；`drafts.tsx:407-419,507-515` 可重复点击并使用固定 60 秒 reload；保存正文不会使旧翻译失效。
- **影响**：并发写 sidecar、旧翻译覆盖新正文、删除后线程重新创建文件、离开页面后误刷新。
- **门禁**：持久化 translating 状态和 source hash；只允许一个任务；保存立即使旧翻译失效；Abort/cleanup 取代固定 reload。
- **状态**：✅ T005 已修复；translation marker、single-flight、hash 校验、保存失效和可取消轮询均已接入。

### DRAFT-009 · P1 · 轮询无取消/slug 校验，可能跨草稿串数据

- **证据**：`drafts.tsx:84-94,726-754` 没有 AbortController、请求序号或 `data.slug` 校验；慢请求可乱序返回。
- **影响**：A 的延迟响应可能覆盖 B 页面正文；多标签页/慢请求会放大轮询和 lint 风暴。
- **门禁**：同一 hook 最多一个请求；切换/卸载 abort；响应校验 slug 和序号；错误显示断线/重试。
- **状态**：✅ T005 已修复；AbortController、slug 校验、退避重试、stale/last-success 展示和客户端断开静默处理均已覆盖。

### DRAFT-010 · P1 · beforeunload 不保护 SPA 导航

- **证据**：`drafts.tsx:329-337` 只注册 beforeunload；顶部导航、列表 Link 和浏览器后退不会触发。
- **影响**：未保存正文可通过应用内导航或后退静默丢失。
- **门禁**：使用 Router blocker 统一保护 dirty 状态；保存成功后解除；导航、后退、刷新和语言切换都进 E2E。
- **状态**：✅ T005 已修复；data Router blocker 保护 SPA 导航，刷新由 beforeunload 保护，E2E 已覆盖取消导航。

### DRAFT-011 · P1 · 生成失败不可诊断且异常日志可能泄露原文

- **证据**：failed 后 UI 不显示 progress/log，也没有 retry；`drafts_api.py:956-963` 异常字符串可能绕过脱敏并进入 progress log。
- **门禁**：失败显示阶段、时间、稳定 error code 和重试；所有错误/日志统一 `redact_text`；敏感异常回归必须检查 API 和 UI。

### DRAFT-012 · P2 · 输入/错误 envelope/国际化契约不足

- **证据**：`_create` 对字段类型、长度、控制字符和未知字段校验不足；前端 `get()` 只保留 `HTTP 404`；创建/入库直接 `r.json()`；服务端错误大量硬编码中文。
- **门禁**：统一 schema 和 `{code,message,retryable,details?}`；前端按 code 本地化；非 JSON/网络错误有稳定 fallback。

### DRAFT-013 · P2 · generation 队列无上限、取消和 GET 写状态

- **证据**：`drafts_api.py:133-134,178-226` 接受无限 queued run，GET/list 会把无 owner 任务改成失败，没有 cancel API。
- **门禁**：每项目最多一个活跃 generation；队列/成本上限；显式 cancel；普通 GET 只读。

### DRAFT-014 · P2 · provider 数据最小化和用户告知不足

- **证据**：完整 link、摘录、research 会进入 provider；创建页没有明确告知哪些字段会外发。
- **门禁**：显示 provider 数据范围；默认去除 fragment/敏感 query；只传必要公开字段；保留本地单用户边界说明。

### DRAFT-015 · P2 · 草稿表单可访问性和焦点行为不足

- **证据**：正文 textarea 无 label；radio 缺 fieldset/name；toggle 无 expanded 状态；错误使用 status 而非 alert；refetch 会回 Loading。
- **门禁**：键盘和自动扫描无 critical/serious；控件有程序化名称/描述；保存/生成焦点可追踪。

## 6. 公共内容页独立审查（回收结果）

公共页没有发现 P0 级越权或数据销毁问题，但以下 P1 会直接影响内容可信度和可发现性：

- **P1-别名搜索缺失**：`search.tsx` 只搜索 slug、名称和定义核心；生成器丢弃 `aliases_zh` 和应用 aliases。`待办事项软件`、`缺陷跟踪器`、`TickTick` 等已知别名无法命中。应把别名加入索引和数据回归。
- **状态**：✅ T007 已修复；类型/应用 aliases 已进入生成索引、搜索评分和 E2E。
- **P1-静态预览没有正式资料 fallback**：`SourceReader` 永远请求 `/api/sources/*`，`vite preview`/静态托管无 API 时只能显示错误；leaf JSON 虽有 `full_md` 但未使用。需要明确 API-only 或使用 `full_md` fallback。
- **状态**：✅ T006 已修复；无 API/无 source 时显示 `full_md` 快照或稳定空态，preview proxy 与开发 proxy 对齐。
- **P1-关系重复 key**：至少 3 组 `(kind,to)` 重复，`leaf.tsx` 使用 `r.to` 作为 key，会产生 React duplicate key 和重复卡片。需要稳定关系 ID/复合 key 和数据验证。
- **状态**：✅ T007 已修复；生成数据提供稳定 relation id，React 使用 id/复合 key，校验器检查目标与 id 唯一性。
- **P1-英文内容不完整**：教程正文仍是中文；应用 tagline/leafName 和关系标签缺少英文映射；relation kind 还有 snake_case fallback。
- **P1-搜索结果不可改写、Apps hash 不可靠**：搜索页没有输入/提交/清空；Apps 没有 hash 滚动处理，异步加载或 SPA 跳转可能停在顶部。
- **状态**：✅ T007 已修复搜索编辑器；Apps hash 仍归后续页面打磨任务。
- **P1-收藏版本无握手**：SourceReader 收藏不发送当前 fingerprint，服务端可能重新读取并保存用户未看到的新版本。
- **状态**：✅ T015 已修复；SourceReader 发送 displayed fingerprint，服务端版本变化返回 409。

公共页 P2 还包括 canonical Markdown 相对死链、section 统计语义、静态 `full_md` 体积、搜索无结果上限、空态/错误态、关系/别名/来源引用数据验证、应用分类 provenance、slug 编码、localStorage 异常、对比度/ARIA、引用死链、启动 readiness、Vite `fs.allow` 暴露父目录等。

## 7. 项目工作台独立审查（回收结果）

项目工作台没有确认 P0，但有多项 P1 状态真实性/并发问题：

- **P1-验收 focus 参数错误**：`project_store.py` 将 `focus_paths` 传给 `snapshot_workspace` 的 `ignore_names`，常见 `focus_paths=["src"]` 项目验收必失败；空 focus 又可能覆盖默认忽略项。
- **状态**：✅ T008 已修复；验收始终使用默认忽略集合，并增加 focus/ignore 回归。
- **P1-旧 execution 可覆盖 task 状态**：旧轮询迟到更新会无条件改写 task.execution_status，页面可能把新 running 任务显示为 completed。
- **状态**：✅ T008 已修复；只有 task 最新 execution 可更新投影，并有迟到回写回归。
- **P1-文档批准/需求确认缺 revision CAS**：旧页面可以批准新文档版本或确认已修改需求。
- **状态**：✅ T008 已修复；API/UI 强制 expected version/revision，冲突返回 409。
- **P1-权限回复不校验 resource/pattern**：`once` 只校验 action，可能批准 write_paths 之外的 edit/write 请求。
- **状态**：✅ T009 已修复；写入权限要求明确相对 resource/pattern 且必须落在 task write_paths。
- **P1-固定验证器运行在 agent 可修改的 workdir**：测试/fixture 可被改写，当前“独立固定验证”不能等价为可信产品证明。
- **状态**：✅ T009 已修复；Atlas 对测试、fixture、验证脚本和配置做 hash 保护，变更时不执行固定验证并记录失败。
- **P1-restore journal hard-link 窗口**：数据库安装和 `database_installed` marker 之间仍有崩溃窗口，清理只按路径可能误删后来替换的目标。
- **状态**：✅ T018 已修复；restore journal schema 2 预记录数据库/制品指纹，数据库 hard-link 窗口可显式恢复，内容被替换时 fail closed。
- **P1-工作区扫描无总量上限**：`/`、home 或超大目录可能造成 CPU/磁盘/内存耗尽。
- **状态**：✅ T009 已修复；拒绝根/home/Atlas pack、过深目录和超文件数/字节/单文件上限。
- **P1-generation/delete 没有共享项目锁**：删除后后台 generation 仍可能创建 artifact。
- **状态**：✅ T018 已修复；generation、apply、backup、delete 共享线程/文件生命周期锁，删除遇到运行中工作 fail closed。
- **P1-旧 generation 缺 basis fingerprint 会被当作未过期**：必须把 `stale_known=false` 视为需要人工确认。
- **状态**：✅ T008 已修复；后端 apply 对 unknown basis fail closed，前端显示不可验证状态。
- **P1-项目切换子面板 identity 不隔离**：baseline、generation、references 和 task selections 可能短暂显示旧项目数据。
- **状态**：✅ T008 已修复；详情子树按 projectId remount，旧项目操作在切换期间不可见。
- **P1-任务/验收绑定不足**：任务可无需求/文档，验收没有持久化 execution/baseline/逐条件结果。

项目页 P2 还包括 starter 异步覆盖用户模式、baseline 错误永久 checking、轮询重叠/无 stale、mutation 无幂等键、删除项目不清 backup、网页无 restore 入口、generation/open-item 导出不完整、旧 pin 未迁移、API 错误契约、health/ready 区分、baseline/export/provider 脱敏、项目详情缺资料管理入口、状态聚合混历史/当前、动态错误/对比度/尝试选择语义等。

## 8. 已确认的良好基础

- 所有已巡有效路由都有明确 `h1`、`main`、加载和基础错误组件。
- 页面默认中文，壳层支持中英文切换，主要业务动作已有双语文案。
- 草稿 dirty 状态、删除确认、项目删除确认、项目执行权限和恢复动作已经存在。
- API 读写边界、状态真实性、固定验证和项目备份安全边界已有后端回归支撑。
- 路由懒加载已完成，主 JS 约 318 kB；页面 chunk 体积已下降。

## 9. 审计限制

- 本次没有设置真实 provider 凭据，因此未执行真实模型生成/执行页面闭环。
- 项目切换旧资料的结论需要慢网/缓存专项 E2E 固化；当前代码存在风险窗口，但普通快速巡检未稳定复现。
- 浏览器巡检使用 Chromium，不代表 Safari/Firefox 的所有视觉和辅助技术行为。
- 本页记录的是当前工作树，不代表已发布、已签名或已通过远端 CI 的版本。
