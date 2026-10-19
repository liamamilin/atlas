# 书签管理器 P0 核心收藏闭环：浏览器验收说明

本目录（`acceptance/`）是书签管理器 P0 阶段的浏览器验收程序：它用真实浏览器驱动真实运行中的目标应用，逐条断言正常行为与硬性负面行为。除本说明中明确声明的命令外，不提供任何替代执行方式。所有命令均相对本目录 `acceptance/` 执行。

## 1. 前置条件

- Node.js 18+（本目录为 Node CommonJS，`package.json` 标记 `private: true`，入口为 `run.cjs`）。
- Playwright 及其浏览器：在 `acceptance/` 内执行 `npm install`，即可安装 `devDependencies.playwright`（`^1.48.0`）及其随附浏览器；若浏览器未随安装下载成功，可再执行 `npx playwright install chromium`。
- Python 3：用于启动被测应用。被测应用按架构仅使用 Python 3 标准库（`http.server` + `sqlite3`），**无需安装任何应用依赖**。

验收程序自身不安装、不构建、不嵌入被测应用；应用必须由操作员以真实进程在回环地址启动后被驱动。

## 2. 以真实目标运行被测应用

在应用目录中启动：

```
python3 app.py --port PORT --data-dir DIR
```

- 应用仅绑定回环地址（127.0.0.1），全部持久数据写入 `DIR`（不存在时创建）。
- `PORT` 为监听端口，`DIR` 为数据目录，由操作员选择。
- 界面为中文；验收只依赖可访问角色与中文可见标签，不依赖模板专用 `data-testid`。

## 3. 环境变量

### 必需

- `TARGET_URL`：被测应用的真实回环地址，例如 `http://127.0.0.1:8080/`。缺失或非法时验收显式失败，绝不猜测地址。

### 可选

- `PORT`：端口；当 `TARGET_URL` 未含端口时，用于生成 A10 的操作员重启命令与就绪探测。
- `DATA_DIR`：数据目录；用于生成 A10 的操作员重启命令（`python3 app.py --port PORT --data-dir DIR`）。
- `APP_ARGV`：JSON 字符串数组，例如 `["python3","app.py"]`。仅当希望用例自身以固定 argv（不启用 shell 插值）安全启动并持有应用进程时提供；此时 A10 自行启动进程，并仅重启该自有 PID。未提供时 A10 默认走操作员 before/after 重启。
- `UI_SELECTORS`：JSON 对象，把逻辑控件名映射到选择器，用于语义等价但结构不同的 UI。可用名（连字符或驼峰写法均可）：`saveUrl`、`saveTitle`、`saveNote`、`saveCategorySelect`、`saveCategoryNew`、`saveSubmit`、`formError`、`categoryList`、`categoryItem`、`recordList`、`recordCard`、`recordOpen`、`recordCategory`、`recordMoveSelect`、`recordMoveSubmit`、`searchInput`、`searchSubmit`、`emptyLibrary`、`noSearchMatch`、`categoryCreateInput`、`categoryCreateSubmit`、`duplicateConfirm`。未提供时按可访问角色与中文标签解析，并回退到架构给出的建议选择器。
- `AUTH_USER` / `AUTH_PASS`：可选认证，仅作用于显式配置的目标。二者必须同时提供，只提供其一会显式失败为不完整。认证只注入到显式 `TARGET_URL` 来源，绝不附加到外部导航或夹具，且不打印、不记录凭据值。`AUTH_SCHEME` 或 `AUTH_MODE` 默认为 `basic`；不支持的模式（例如 digest）在发起任何请求前显式抛基础设施/不完整错误，不静默跳过。
- `UI_TIMEOUT_MS`：等待超时毫秒数，默认 15000。
- `HEADLESS`：设为 `0` 或 `false` 时显示浏览器窗口；默认无头。
- `OPERATOR_CONFIRMED`：设为 `1` 时，A10 视为操作员已完成 before/after 真实重启（供无法交互的环境明确声明）；它本身不代替真实重启。

## 4. 运行验收

在 `acceptance/` 内：

```
export TARGET_URL=http://127.0.0.1:8080/
npm test
```

等价于：

```
node run.cjs
```

`run.cjs` 按固定顺序合并并执行三个行为组：保存/归类 → 检索/浏览/打开 → 持久化。

单个行为组也可独立运行（退出码规则相同）：

```
node p0-save-classify.cjs
node p0-find-open.cjs
node p0-persistence.cjs
```

## 5. 网络策略

- 验收安装网络守卫，拦截全部请求：仅放行 `TARGET_URL` 来源与回环地址，其余地址一律中止，测试环境不产生真实外连。
- 唯一的对外导航是用户显式点击“打开原页”，指向记录保存时的原始 URL（含 query 与 fragment），并在新标签页打开；被尝试打开的 URL 会被捕获，用于 A09 断言。
- 任何后台外发请求（元数据抓取、遥测、非用户触发的导航）都会被记录为违规，并使相关断言失败。P0 不抓取元数据、不发遥测。
- 凭据绝不附加到外部导航（断言导航 URL 不含用户名与密码）。

## 6. 真实重启控制契约（A10）

- 默认由操作员控制 before/after：用例先经 UI 保存记录与分类，随后输出停止并以 `python3 app.py --port PORT --data-dir DIR` 重启的步骤并等待其完成；完成后用例再经 UI 读回数据。未完成的操作员步骤不得计为通过（该用例状态为待操作员，退出码非零）。
- 仅当用例自身以固定 argv（`APP_ARGV`，`shell:false`）启动并安全持有该子进程时，才可以只终止自己启动的 PID 并重新启动，且断言新旧 PID 不同；绝不执行任意 shell 命令，绝不终止无关进程。
- 刷新页面不是重启；数据文件存在或新建 SQLite 连接都不是重启证明；验收也不要求应用暴露内部数据库连接状态。

## 7. 退出码语义

- `0`：全部用例通过。
- `1`：存在断言失败，或配置/基础设施错误（例如缺少 `TARGET_URL`）；不得视为通过。
- `2`：无断言失败但存在待操作员未决项（A10 未完成真实重启）；未决项不得计入通过。

## 8. 用例清单（阶段 P0）

| 用例 | 类型 | 目标 | 所属行为组 |
| --- | --- | --- | --- |
| A01 | 正 | 仅填写 URL 即可保存，落入未分类并立即出现；缺省标题回退为 URL | `p0-save-classify.cjs` |
| A02 | 正 | 带标题与备注保存；重载后标题与备注完整可见 | `p0-save-classify.cjs` |
| A03 | 正 | 选择已存在分类保存；记录出现在该分类浏览结果中 | `p0-save-classify.cjs` |
| A04 | 正 | 保存时新建分类并归入；重载后新分类与归属保持 | `p0-save-classify.cjs` |
| A05 | 正 | 记录跨分类移动；重载后归属更新且不再出现在原分类 | `p0-find-open.cjs` |
| A06 | 正 | 分类浏览只含该分类记录，且默认按添加时间倒序 | `p0-find-open.cjs` |
| A07 | 正 | 关键字命中标题/URL/备注/分类名，且不返回无关记录 | `p0-find-open.cjs` |
| A08 | 负 | 空库提示与检索无匹配提示必须是两条不同文案 | `p0-find-open.cjs` |
| A09 | 正 | 点击记录在新标签打开原始 URL，保留 query 与 fragment（外连被拦截，仅断言被尝试打开的 URL 与新标签行为） | `p0-find-open.cjs` |
| A10 | 正 | 数据写入 `--data-dir`，经真实进程重启后仍可经 UI 读回记录与分类 | `p0-persistence.cjs` |
| A11 | 负 | 重复 URL 出现显式“已存在”提示，可显式继续保存为另一条记录 | `p0-save-classify.cjs` |
| A12 | 负 | 同一保存按钮快速双击提交，只产生一条记录 | `p0-save-classify.cjs` |
| A13 | 负 | 超限备注显式报错且不落库，不出现静默截断后保存 | `p0-save-classify.cjs` |
| A14 | 负 | 无效 URL 与非 http(s) 协议显式报错且不落库 | `p0-save-classify.cjs` |
| A15 | 正 | 保存失败后表单保留已输入内容，修正后重试成功 | `p0-save-classify.cjs` |
| A16 | 正 | 含中文与 emoji 的标题与备注保存、显示与检索均正确 | `p0-save-classify.cjs` |
| A17 | 负 | 仅回环可达；除显式点击打开原页外无后台外发；认证只作用于显式目标，不支持的模式显式失败 | `p0-find-open.cjs` |

## 9. 验收范围与明确不做

- 验收只断言被测应用的真实、用户可见行为；不在验收中执行应用逻辑判断以外的任何替代。
- 不使用 mock 目标响应，不以数据文件存在性或内部连接状态代替用户行为，也不弱化声明的断言。
- 用例不硬编码已知夹具值：URL、标题、备注与分类名均在运行时随机生成。
- 应用必须真实运行；验收程序不启动、不嵌入、不伪造应用行为。
- P0 不含编辑、删除/回收站、分类重命名/删除、分页、导入/导出、批量操作、标签、账号、计费与管理后台；这些能力属后续阶段或明确不适用，不在本验收范围。
