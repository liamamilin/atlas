# U17 发布检查清单

这份清单用于每次发布前重复确认核心主线、错误恢复和文案收口。它是发布门槛，不替代 M5 试点记录；试点仍需保存输入、运行记录和结果证据。

## 1. 检查前提

- [x] 当前分支和工作区状态已确认，未把生成的本地工作区文件当成源码变更。
- [x] API 服务运行在 `5199`，前端开发服务运行在 `5188`；浏览器检查使用当前构建。
- [x] 本轮检查不会删除项目、覆盖工作区或修改正式资料数据。

## 2. 自动检查

在仓库根目录执行：

```bash
cd atlas-web
npm run typecheck
npm run build -- --emptyOutDir false

cd ../application-atlas-production-pack
python3 -m unittest discover -s tests -p 'test_*.py'
node --check projects/workspaces/prj_e6299aa777e645b4a8c9157a31364e0c/static/app.js

cd ..
```

此时已回到仓库根目录，再执行：

```bash
git diff --check
```

生产构建中的大包拆分提示需要记录，但在没有实际加载问题时不阻断本轮产品收口。

## 3. 浏览器核心路径

按顺序打开并记录结果：

1. `/`：默认中文、导航可用、语言切换后主要页面文案同步。
2. `/browse`：类型树可加载；展开领域和子领域后，类型数量和卡片可见；长导航不换行撑高页面。
3. `/types/task-management-application`：叶子页正文、正式资料、关联类型和“基于这个类型开发项目”入口可见；技术标识默认收起。
4. `/projects?fromType=task-management-application`：创建表单可用，类型上下文和来源链接保留。
5. `/projects` 与 `/projects?mode=existing`：项目卡片显示状态和下一步；工作区绝对路径默认收起；已有项目入口正确预选项目类型；加载失败、空状态和删除反馈可理解。
6. `/projects/:id`：首屏显示阶段位置、当前迭代、下一项动作和待处理事项；基线、分析、需求、范围、文档、迭代、执行与验收可以继续操作。Agent Harness 变更任务验收已记录为单文件执行、应用、独立验收和清理通过；停止执行复验也已通过，证据清理保留正常。
7. `/tutorial` 与 `/projects?fromType=ai-coding-agent`：首次使用六步说明、Atlas/OpenCode 职责边界和 Agent Harness 类型起点可见。
8. 项目完成或失败后刷新、返回并重新进入：状态仍正确，下一步动作不会回到过期的暂态；已完成项目显示“当前没有阻塞项”。

## 4. 状态与安全反馈

- [x] 加载中、空状态、请求失败和刷新重试均有明确反馈；原始异常只在技术详情中显示。
- [x] 基线过期、执行失败、应用失败和验收失败都有可继续或安全结束的动作。
- [x] 只读导出明确说明范围，不修改工作区或源代码。
- [x] 数据备份、最近删除和恢复前安全快照说明保存范围、创建时机、ID 冲突和替换影响；中英文保持同步（由 M5 本地日计划器案例的真实 HTTP 验收和案例文档覆盖）。
- [x] 内部 ID、会话、指纹、哈希、绝对路径和版本标识默认收起，但仍可按需核对。

### 4.1 本地安全审查复验

- [x] `docs/U17_SECURITY_REVIEW.md` 已记录 API、workspace/apply、provider runtime、backup/restore、凭据和发布边界。
- [x] 已明确 loopback、权限策略、固定验证器、路径检测和工作区复制都不是 OS/容器沙箱证明。
- [x] 本地 key/token/secret 模式扫描无未允许命中；扫描结果和限制已记录。
- [ ] 目标发布 SHA 的远程 CI、macOS 签名/公证、目标平台人工审查和独立进程/容器/VM 证据仍待外部环境。

## 5. 发布判定

- 所有核心路径和 P0 自动检查通过，才允许进入发布评审。
- 若只有构建体积提示或其他已记录的 P1/P2 项，需在发布记录中写明影响和后续计划。
- 发布收口后，只有在明确立项并补齐范围、权限和验收协议时，才启动新的 provider、模拟适配器或 coding agent 后端评估；当前 M5 案例不再重复建立。

## 6. 最近一次复验记录（2026-09-22）

- 后端回归：`python3 -m unittest discover -s application-atlas-production-pack/tests -p 'test_*.py'`，132 项通过。
- 前端检查：`npm run typecheck` 和 `npm run build -- --emptyOutDir false` 通过；生产构建保留约 686 KB 主 JS 的拆包提示，当前不阻断。
- 静态脚本与文档检查：`node --check`、`git diff --check` 和案例 manifest JSON 校验通过。
- API：`http://127.0.0.1:5199/api/health` 正常；前端开发服务已在 `5188` 重新启动。
- Agent Harness 项目：首版纵向切片迭代已通过 API 收口为 `completed`；工作台刷新后显示“最近迭代已完成”和 `9/9 项已完成`。
- 浏览器路径：默认中文；首页案例入口、浏览类型、任务管理叶子页、项目列表、已有项目预选、Agent Harness 类型起点、教程和 Agent Harness 项目详情均可加载；草稿已有数据，未触发删除或覆盖操作。
- 本次未执行项目删除、源工作区覆盖或正式资料发布；浏览器中发现的连接拒绝来自前端服务未运行，重启后页面加载正常。

## 7. 当前工作树加固复验（2026-09-24）

- 后端 199 项回归在当前环境及干净 Python 3.11 环境通过；此前全新 Python 3.10 虚拟环境的 155 项复验也通过。
- 前端 7 项单元测试、12 项 Playwright E2E（重复 3 次共 36/36 通过）、类型检查和生产构建通过；E2E 覆盖类型叶子、无 API 资料 fallback、别名搜索、未知路由 404、Apps hash 深链、移动视口溢出、英文教程、草稿 dirty 保存/删除、SPA 导航阻断、生成完成 hydration、轮询 stale/retry、项目切换身份、API 恢复初始化、跨源拒绝和备份下载。
- 网页数据从 Markdown 重新导出后验证为 1,805 leaves、270 sections、33 apps，无缺失或 stale 文件。
- 依赖审计：干净 Python 3.11 环境对锁定 requirements 的 `pip-audit --no-deps --disable-pip` 无已知漏洞，当前 `npm audit` 为 0；完整解析式 `pip-audit` 仍由 CI 在发布 SHA 重新执行，关键 Python 路径 Ruff 通过。
- OpenCode 2.0.16 实际 `debug config` 已验证 Atlas V2 项目策略加载并在终态恢复原配置；托管 V2 服务的 Basic 认证、`/api/info`、session create/prompt/reconcile 传输已做本机冒烟；受管 V2 session 权限规则已回读确认，U17 shell/MCP/web/外部目录默认拒绝，草稿 MCP 进程也以只读模式拒绝分类副作用，HTTP/V2 完成/失败终态固定验证由 Atlas 独立执行，权限交互不提供持久授权且禁止/未知动作只能拒绝。Apply 现在有 durable journal、进程崩溃回归和显式 `recover-apply`，Restore 也有 journal、进程崩溃回归和显式 `restore-status`/`recover-restore`，备份/删除对未应用结果和并发 mutation fail closed；固定验证拒绝 shell、内联解释器代码、绝对路径和未注册执行器。
- 生产构建已按路由拆包；主 JS 约 376.77 kB，最大页面 chunk 约 158.06 kB，不再触发 500 kB 拆包警告。
- 页面逐项审查和后续任务记录在 `docs/U17_PAGE_AUDIT.md` / `docs/U17_PAGE_POLISH_PLAN.md`；其中 source 404、草稿轮询错误、项目切换隔离和移动溢出仍需按优先级处理。
- 当前改动尚未提交或推送，GitHub Actions 尚未验证同一发布 SHA；分类门禁、macOS 签名/公证和完整执行沙箱仍未完成，因此当前仍不满足公开发布条件。
