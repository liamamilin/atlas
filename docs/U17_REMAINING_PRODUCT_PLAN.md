# U17 剩余产品收口与发布打磨计划

日期：2026-09-25  
状态：规划中；本地核心闭环已完成，发布级收口尚未完成  
范围：本地单用户 Application Atlas；不扩展云端、协作或自动危险副作用

## 1. 当前基线

### 已完成

- 任务队列：T001-T027、T029-T032 已完成；仅 T028 进入外部发布工程队列。
- 本地验收：31/31 项通过；后端当前回归 221 项通过，前端 typecheck/unit 9/9、build、backup E2E、分类 provider 成功/失败 smoke、backup 生命周期 E2E、安全审查、acceptance migration 和错误契约回归通过；干净 Python 3.11 离线回归的最近基线为 211 项通过，新增 T025-T027/T029-T032 回归已在当前环境通过。
- 前端：数据校验 1,805 leaves / 270 sections / 33 apps；typecheck、unit、build 通过；Playwright 51/51 通过；npm audit 0 vulnerabilities。
- 真实 provider：`opencode-go/deepseek-v4.1-flash` 已完成临时隔离的 analysis、code execution、固定验证、apply、generation、backup 和 restore-to-empty-store。
- 核心原则：用户源码不进入 Atlas backup；不自动重放、删除、覆盖或入库；高影响动作必须显式确认。

### 尚未完成

1. **P0：发布工程门禁**：远程 CI、发布 SHA、macOS 签名/公证和发布渠道尚未验证。

## 2. 计划原则

- 先处理可能污染源码、覆盖数据或误报成功的问题，再做体验优化。
- provider 产物只能在 Atlas 创建的临时 runtime 或明确登记的 artifact 目录中出现；源码树出现新文件应使验证失败并报警。
- 浏览器不得接受任意主机路径作为 restore 目标；目标必须由服务端在受控 restore root 下生成。
- 任何 restore、apply、删除、迁移回填和 provider 重试都保持显式确认；失败后只报告并保留证据。
- 不把 loopback、固定验证器、文件权限或 V2 permission policy 描述为完整 OS/容器隔离。
- 每个任务必须同时有：代码行为、用户可见反馈、双语文案、自动测试、文档和限制记录。

## 3. 分阶段路线图

### Phase 0：基线冻结与安全清理（已完成）

**目标**：确保计划期间不继续污染工作树。

- 保持当前工作树未提交，不自动 commit/push。
- 对 provider 生成的仓库根目录 `result.json` 做路径隔离回归。
- 记录当前凭据只从 OpenCode 本地认证存储读取；不把 key、access token、refresh token 写入仓库、日志或报告。
- 完成 T026 后冻结新的本地验收基线。

**退出条件**：工作树中没有 provider 临时产物（既有审计改动单独保留）；路径隔离测试通过；凭据扫描无命中。

### Phase 1：P0 provider 产物隔离（T026）

**目标**：generation 结果永远不能落入源码树或其他未登记目录。

**实现范围**：

- 固定 OpenCode generation 的实际 project root/cwd；禁止依赖全局项目发现结果。
- 只接受 runtime、generation engine 和登记的 artifact 目录中的 `result.json`；对其他路径写入 fail closed。
- 启动前后记录并比较源码树文件集合；发现新增/修改立即报告，不自动覆盖或删除。
- 保留严格 JSON shape/fingerprint 校验和 engine log 脱敏。
- 增加中断、错误输出、provider 只返回文本和路径越界回归夹具。

**验收**：临时真实 generation 成功；仓库 `git status` 无新增 provider 文件；越界写入测试失败且不吞掉原始证据。

**状态**：已完成（T026）；本地 215 项后端回归和真实 `opencode-go/deepseek-v4.1-flash` disposable smoke 通过。

### Phase 2：P0 浏览器 backup/restore（T025）

**目标**：让用户不接触任意主机路径即可安全查看并恢复 backup。

**实现范围**：

- 后端提供受控 backup 列表、校验摘要和 restore-status API。
- restore target 由服务端在专用 restore root 下生成，拒绝已存在路径、symlink 和越界路径。
- 浏览器显示备份时间、大小、hash 摘要、包含/排除范围和恢复目标。
- 恢复前显示明确确认：只恢复到新的空项目库，不覆盖当前库，不包含用户源码。
- restore 失败显示可恢复原因；不自动重试、不自动清理 journal。
- 增加 backup 列表、空态、错误、确认、下载和恢复后的 E2E。

**验收**：浏览器路径可完成 backup→选择→确认→restore-status；任意路径输入被拒绝；失败后可重新进入且状态真实。

**状态**：已完成（T025）；浏览器 backup/restore E2E、API contract、目标路径拒绝和 215 项后端回归通过。

### Phase 3：P0 provider 分类/裁决验证（T027）

**目标**：补齐真实 provider 分类与验收链，而不是只验证 execution。

- 明确 `ATLAS_ADJUDICATOR` 的 provider/model 格式、账户权限和费用边界。
- 在 disposable project 中运行分类 smoke、结果校验和失败路径。
- 验证分类结果只作为建议/证据，不自动确认需求、不自动入库。
- 记录模型 ID、输入指纹、输出 hash 和脱敏错误；不记录凭据。
- provider 不稳定时保持 fail closed，不自动切换模型。

**验收**：至少一个真实分类成功和一个 provider 失败路径可重复；前端显示可理解的错误和建议。

**状态**：已完成（T027）；`qwen3.8-flash` 成功 smoke 和 `opencode-go/deepseek-v4.1-flash` `model_unavailable` 失败路径通过，错误不泄露凭据且不自动 fallback。

### Phase 4：P0 发布工程与平台门禁（T028）

**目标**：让同一发布 SHA 在目标环境可重复构建和审查。

- 固定 Node/Python/OpenCode 版本与依赖锁。
- 远程 CI 重跑数据生成、Python、前端、E2E、pip-audit、npm audit 和 diff 检查。
- 生成发布 artifact、checksums、SBOM/依赖清单和可复现运行说明。
- macOS 签名、公证、 entitlements、启动权限和升级/回滚流程在目标机器验证。
- CI 失败时保留原始日志但脱敏；不使用本地手工绿色结果替代远程结果。

**验收**：目标发布 SHA 的 CI 全绿；签名/公证产物可验证；安装、启动、卸载和回滚步骤有记录。

**状态**：阻塞（T028）；当前环境没有远程 runner、macOS 签名/公证凭据或目标机器，不能用本地结果替代。

### Phase 5：P0 安全边界与人工审查（T029）

**目标**：明确 Atlas 能保证什么、不能保证什么。

- 更新威胁模型：同用户恶意进程、provider 数据保留、恶意网页、项目测试代码、插件/MCP 和 restore 越界。
- 对固定验证器、权限策略、隔离副本、apply/restore journal 做人工攻击路径审查。
- 明确 loopback、权限策略和文件锁不是 OS/容器沙箱。
- 检查日志、备份、导出和错误响应中的 secret/PII 脱敏。
- 对发现的问题建立回归测试或明确的 release blocker。

**验收**：安全审查报告逐项签字；高风险项关闭或阻断发布；文档不使用“完整隔离”等过度表述。

**状态**：已完成（T029）；审查记录见 `docs/U17_SECURITY_REVIEW.md`，外部 OS/容器/目标平台证据仍明确列为 release blocker。

### Phase 6：P1 旧验收数据连续性（T030）

**目标**：让旧记录可读、可解释、可安全迁移，不伪造历史结论。

- 识别没有 `condition_results` 的旧 acceptance binding。
- 提供 dry-run migration 报告：项目、任务、时间、缺失数量、不可判断项。
- 只回填可证明的结构信息；没有历史人工结论时保持 `not_backfilled`。
- 迁移支持 dry-run、幂等、备份和失败回滚。
- UI 显示迁移状态和原始记录来源。

**验收**：迁移前后项目数量、任务数量、文档版本和证据 hash 不变；历史未知不被推断为通过。

**状态**：已完成（T030）；dry-run、固定确认、事务幂等 backfill、导出摘要和工作台报告均有回归证据。

### Phase 7：P1 backup 生命周期与错误契约（T031/T032）

**目标**：补齐长期使用中最容易造成误解的运维体验。

- backup 历史、保留策略、清理前确认和 restore-status 页面化。
- 统一 generation/provider/backup/restore 错误 envelope：稳定 code、用户消息、技术详情、是否可重试。
- 统一前端中英文错误映射，避免把 409/503/422 显示成泛化失败。
- 为 backup/restore/generation 增加长尾 E2E 和 API contract tests。
- 记录 bundle/数据库/文件系统增长和清理失败，但不自动删除用户源码。

**验收**：备份生命周期可从浏览器理解和恢复；长尾错误有稳定契约；核心路径不回归。

**状态**：T031/T032 已完成（221 项后端、9 项前端 unit、51/51 E2E）；长尾错误 envelope、retryable 标志和前端恢复映射均有证据。

## 4. 任务依赖图

```text
T024 provider generation hardening
        │
        ├── T026 provider artifact containment ──┐
        ├── T027 adjudicator/classification     │
        └── T028 release engineering            │
                                                   ├── T029 security review
T025 browser backup/restore ── T031 backup lifecycle
        └── T032 API error contract
T022 acceptance provenance ─── T030 legacy acceptance migration
```

- 只有标记为 release-required 的任务通过后，才考虑写入 `PROJECT_ACCEPTED`；P1 数据连续性任务若延期，必须在发布记录中明确其影响和非目标范围。
- T026 是所有新的真实 provider 验证的前置门禁。
- T025 与 T026 可以在不同周期开发，但发布验收必须同时通过。
- T028/T029 依赖目标 CI、macOS 身份和安全审查环境；环境未提供时保持 blocked，不伪造完成。
- T030/T031/T032 是发布前可并行但不应扩大核心范围的产品化任务。

## 5. 统一验证矩阵

### 每个本地代码任务

```bash
python3 -m unittest application-atlas-production-pack.tests.test_reliability -q
uv run --offline --python 3.11 --with-requirements requirements.txt \
  python -m unittest application-atlas-production-pack.tests.test_reliability -q
cd atlas-web && npm run gen && npm run verify-data
cd atlas-web && npm run typecheck && npm test && npm run build
npx playwright test --repeat-each=3
npm_config_registry=https://registry.npmjs.org npm audit --audit-level=high
cd .. && git diff --check
```

### 真实 provider 任务

- 使用 disposable project 和 disposable workspace。
- 模型通过显式环境变量传入；凭据不进入 argv、仓库或报告。
- 先做只读 smoke，再做明确的 execution/generation；apply、restore、delete、migration 必须单独确认。
- 运行前后检查源码树、git status、artifact 目录和 secret scan。
- 记录 model ID、input fingerprint、状态、证据目录和 hash，不记录原始 secret。

### 发布任务

- 远程 CI 必须针对发布 SHA 重跑，不接受本地结果替代。
- 签名、公证、启动、升级、回滚和 restore 需要目标 macOS/发布环境。
- 任何 OS/容器隔离声明必须有对应测试环境；否则只描述为权限/工作流边界。

## 6. 完成定义与发布门槛

一个任务只有同时满足以下条件才可标记 done：

1. 正常、空、失败、取消和恢复路径都有用户可见反馈。
2. 刷新、返回、切换项目和重试不会产生旧状态或重复副作用。
3. 中英文文案、错误码、技术详情和文档同步。
4. 至少一个匹配的自动测试；涉及 provider/发布时还要有真实环境证据。
5. 不泄露凭据、用户源码或未脱敏 provider 输出。
6. `git diff --check`、目标测试和必要的安全检查通过。
7. `WORKLOG.md` 记录结果、限制和下一步。

只有以下条件全部满足，才考虑写入 `PROJECT_ACCEPTED`：

- T025–T029 中定义为发布必需的项全部通过。
- 目标 CI、签名/公证和人工安全审查完成。
- provider 分类/裁决链和最终产品验收完成。
- 没有未解释的高风险安全发现。
- 工作树、版本、artifact 和运行说明与发布 SHA 一致。

## 7. 需要外部提供的条件

- OpenCode Go 的有效模型访问和 `ATLAS_ADJUDICATOR`/分类 provider 配置。
- 远程 CI 运行环境和发布权限。
- macOS 签名身份、公证凭据和目标机器。
- 一个明确的 OS/容器隔离测试环境，或接受“不宣称完整沙箱”的发布边界。
- 浏览器 restore 目标已落地为服务端受控 root，backup 生命周期采用“不自动 prune、逐项确认删除”的保守默认；若要自动保留策略，仍需产品决策。
- 旧验收数据是否允许 dry-run migration/backfill 的明确决定。

## 8. 立即执行顺序

1. **T028**：补齐远程 CI、发布 SHA、macOS 签名/公证和安装回滚门禁。

当前建议：先不扩展云端、协作、多 provider 自动路由或新的 coding-agent harness；这些不属于发布收口，且会扩大凭证、隔离和运维风险。
