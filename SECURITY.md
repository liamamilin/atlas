# Application Atlas 安全边界

更新日期：2026-09-25

## 当前支持模型

Application Atlas 当前是 **本地单用户 macOS 开发工具**，不是多用户、团队协作或远程服务。

本次本地威胁模型审查记录见 [`docs/U17_SECURITY_REVIEW.md`](docs/U17_SECURITY_REVIEW.md)；它记录已验证控制和仍需外部环境解除的 release blocker，不把本地路径检查或权限策略描述为 OS/容器沙箱。

- 受信主体：启动 Atlas 的用户、该用户明确启动的 OpenCode/provider、Atlas 自身代码。
- 受信存储：用户目录中由 Atlas 管理的数据、隔离副本、证据和导出目录。
- 不可信输入：网页内容、用户提交的链接、资料摘录、模型输出、任务正文、验证命令输出和 provider stderr。
- API 只监听 loopback；Host、Origin、Fetch Metadata、JSON Content-Type、请求体大小和执行状态读写边界由服务端校验。
- 草稿 agent 和 U17 执行 agent 默认不能使用 shell、web、外部目录或子 agent；草稿仅在生成的临时策略中开放 Atlas 的只读 MCP，U17 默认连 MCP 也关闭。草稿只能写当前 slug 的三个输出文件，U17 写入还要经过任务范围复核。
- U17 默认由 Atlas 启动本机 standalone OpenCode，并临时安装可恢复的 V1/V2 权限策略；受管 V2 session 还携带 Atlas 生成的权限规则，项目/全局配置不被当作强隔离边界。V2 服务使用 Atlas 运行时生成的 Basic 认证密码，密码不写入项目证据或导出。
- 固定验证命令不经过 shell，只接受注册的无 shell 验证器、拒绝内联解释器代码和绝对路径参数，并使用白名单环境；HTTP/V2 完成/失败终态由 Atlas 在 agent 停止后独立重跑，模型自报验证只作为次级证据。U17 权限请求只允许一次性的安全动作，禁止动作和未知动作不能被网页/API 放行。验证器本身及其测试代码仍不是容器或 OS 沙箱。

## 明确不在当前威胁模型内

以下情况不能宣称已被 Atlas 完整隔离：

1. 同一 macOS 用户下的恶意或已被攻陷的本地进程。
2. 恶意网页与本机服务之间的零点击跨源调用；当前依赖 Origin/Host/Fetch Metadata 和 JSON 边界防御。
3. 注册验证器或项目测试代码主动读取工作区外绝对路径、访问网络或产生宿主副作用；Atlas 的 argv/路径约束不是 OS/容器沙箱，彻底解决仍需独立的进程或虚拟机边界。
4. OpenCode/provider 主动保留或上传的数据；Atlas 只能控制自己的持久化和导出边界。
5. 已被恶意内容污染的全局 OpenCode 配置、插件或 MCP 服务。
6. 多用户权限、远程访问、租户隔离和团队审计。
7. 未经 Atlas 启动和验证的 OpenCode 服务、插件或 MCP；`ATLAS_OPENCODE_URL` 只接受显式信任的未托管覆盖。

同用户进程若能读取用户文件，也能读取任何放在用户目录中的静态 token；因此一个看似复杂但仍可由浏览器或同用户程序自动取得的 token 不能被描述为强认证。加入账号系统前，Atlas 明确保持本地单用户边界。

## 数据处理

- 外部链接只允许公网 HTTP/HTTPS，阻断本机、私网、link-local、带凭据 URL；DNS 结果固定到连接，重定向逐跳复核。
- 原始执行状态、CLI stdout/stderr、generation engine 日志和项目导出在写入前进行已知密钥模式脱敏。
- 证据和导出目录使用用户私有权限；API 项目数据库、Web 数据生成和项目产物使用受控生命周期。
- 删除项目会删除数据库记录、generation、默认或自定义执行副本、执行证据和导出目录，但保留用户工作区源码。
- 项目备份只包含选定项目状态、generation、证据和 Atlas 导出；未应用的 execution result 会阻止备份，避免生成恢复后不可执行的孤立记录。恢复只允许写入新的空项目库，不覆盖当前库；restore journal schema 2 记录数据库/制品 ownership fingerprint，hard-link 崩溃窗口可显式恢复，内容被替换时拒绝清理，用户源码由 Git 或独立备份负责。
- Generation/provider 产物必须留在 Atlas 创建的 runtime 或登记的 artifact 根目录；源码树出现 provider 生成文件是路径隔离失败，不能作为可接受 fallback。T026 已将 disposable Git project root、V2 `.opencode` 配置、精确 edit 权限和源码树越界检测固定为回归门禁。
- 浏览器 restore 只接受服务端生成的 opaque `restore_id` 和固定确认令牌；目标由受控 restore root 派生，不能与项目源码工作区重叠，也不接受任意主机路径或覆盖已有项目库。
- Backup 归档删除和中断 restore 清理都必须通过固定确认令牌；Atlas 不自动 prune、不删除项目数据库或用户源码，清理只作用于 journal 记录且指纹未变化的 Atlas 产物。
- 文件 apply 在首次破坏性替换前写入 Atlas-owned journal；启动只报告中断并保留证据，只有用户明确调用 `recover-apply`/`restore_before` 才会尝试恢复 apply 前文件，绝不自动重放或自动覆盖。
- 已存在的项目执行记录在 API 启动时进行技术证据脱敏；备份副本也会脱敏历史证据，历史导出使用相同脱敏策略。
- Provider 凭据只通过 OpenCode 的本地认证存储读取；诊断、日志和报告不得打印 API key、access token、refresh token 或认证数据库行。若凭据曾出现在终端、issue 或日志中，应先在 provider 控制台撤销/轮换，再继续验证。

脱敏只能降低已知模式的风险，不能证明任意模型输出或用户正文不存在敏感信息。

## 发布前安全门禁

- Python 与 npm 依赖审计无未处理 High/Critical。
- 后端回归、前端单元测试、Playwright 核心路径、干净数据生成和构建全部通过。
- `file:`、私网、重定向到私网、错误 Host/Origin、跨源写请求和超大请求进入自动回归。
- 验收状态不能由未执行或未应用结果伪造。
- 文档不得把“loopback”“工作区隔离”或“脱敏”描述为完整沙箱或认证。

## 报告问题

如果 GitHub 仓库页面提供 **Security → Report a vulnerability**，请优先提交私密漏洞报告。不要在公开 issue 中粘贴 API key、provider 原始错误、用户正文、绝对路径或可复现敏感数据。提交前请移除凭据和真实项目内容。
