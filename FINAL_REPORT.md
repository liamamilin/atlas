# FINAL REPORT

## Acceptance Status

本轮已完成 T002–T024 的本地单用户范围审查与修复、T025–T032 的剩余产品收口计划、T026 provider artifact containment、T025 浏览器 backup/restore 管理、T027 分类 provider 门禁、T029 本地安全审查、T030 旧验收迁移、T031 backup 生命周期 和 T032 长尾错误契约。公共页面、项目生命周期、restore journal、任务/验收 provenance、逐条件验收结果、真实 OpenCode Go execution/apply、真实 generation→backup→restore、受控浏览器恢复、分类成功/失败边界、backup 清理确认、威胁模型、历史验收迁移和稳定错误恢复均有回归证据；当前本地验收为 31/31 项通过。本报告不写 `PROJECT_ACCEPTED`，因为远程发布环境、签名/公证和完整 OS/容器边界不在本轮可验证范围，且仍有一些已记录的 P2 产品跟进项。

## Completed Features

- 完成 10 个公共/项目路由的正常、注入错误、代表性空态、语言、375/768px 和可访问名称矩阵。
- 草稿 dirty revision、生成 hydration、轮询 stale/retry、发布状态冲突、导航保护和 fingerprint 握手均 fail closed。
- 类型与应用 aliases 可搜索；Apps/关系字段有双语投影；分类来源、方法和分数证据可见；canonical `.md` 链接转换到类型路由。
- 项目详情已拆出 generation、workspace baseline、document 三个领域组件，并保留共享表单/状态辅助。
- generation/apply/backup/delete 使用项目生命周期线程锁和文件锁；删除不会与运行中的 generation 竞态。
- restore journal schema 2 记录数据库与制品 ownership fingerprint，制品使用原子 rename；hard-link crash window 和替换后误删都有显式恢复夹具。
- 加载、空态、错误、focus-visible、reduced-motion 和窄屏溢出有共享门禁。
- API 新任务必须固定至少一份文档版本和一条已确认需求；验收记录保存 Atlas 生成的 execution、baseline、文档版本、需求修订和验收条件快照，详情页可展开审查。
- 新验收决策必须为每条 pinned condition 保存明确的通过/失败/免验结果和可选说明；旧记录缺少结果时明确显示未回填，不从总体状态推断逐条件结论。
- 真实 OpenCode Go `deepseek-v4.1-flash` 已在临时隔离工作区完成 analysis execution、带固定单测/范围检查/显式 apply 的 code execution，以及 generation→backup→restore；`deepseek-v4-flash` 的 access-disabled 响应被保留为 provider 限制证据。
- generation 使用显式 disposable Git project root、V2 `.opencode/opencode.json` 和仅允许 `result.json` 的 edit policy；源码树出现 provider 新增、修改或删除会记录 `provider-artifact-violation.json` 并 fail closed。T026 的真实 disposable generation smoke 返回 `artifact_root=runtime`，仓库未产生 provider artifact。
- 浏览器 backup/restore 管理可列出校验通过的归档、创建 opaque `restore_id`、显示受控目标、要求明确确认，并只恢复到新的空项目库；API/UI 不接受或返回任意主机路径，restore root 不能与源码工作区重叠。
- 分类 provider 已完成真实成功/失败门禁：`qwen3.8-flash` 成功返回候选，`opencode-go/deepseek-v4.1-flash` 明确失败并映射为不可重试的 `model_unavailable`；错误脱敏、无自动 fallback，分类结果不改变需求或正式语料。
- Backup 生命周期支持浏览器显式删除归档和清理中断恢复；两种操作都需要固定确认令牌，删除后列表缓存失效，Atlas 不自动 prune，也不删除项目或用户源码。
- T029 已完成本地威胁模型和安全边界审查，明确 API、workspace/apply、provider runtime、backup/restore、凭据和发布残余风险；loopback、权限策略、固定验证器和路径检测不被描述为 OS/容器沙箱。
- T030 提供旧 acceptance binding 的 dry-run 报告和显式 backfill；缺失历史逐条件结果只标记 `not_backfilled`，不改变历史状态、不推断结论，迁移事务幂等且导出包含摘要。
- T032 统一 generation/provider/backup/restore 错误 envelope，API 返回 `code/retryable/details`，generation run 保存 `error_code`，前端提供双语恢复建议且不自动重试。

## Validation Evidence

- `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`：221 passed（T032 后通过；含受控 backup/restore、runtime containment、分类 provider 成功/失败、backup 删除/中断清理、acceptance migration、错误契约和源码树越界回归）。
- `uv run --offline --python 3.11 --with-requirements requirements.txt python -m unittest application-atlas-production-pack.tests.test_reliability -q`：211 passed（缓存依赖；普通联网拉取本轮遇到 PyPI 超时）。
- 真实 provider 临时隔离验证：`opencode-go/deepseek-v4.1-flash` analysis `completed`；code task `verification_passed=true`、`scope_compliant=true`、`application_status=applied`，新基线已采用；generation `completed`、backup schema 1 校验通过、restore 到新空库后 generation result 可读；T026 另完成 disposable generation containment smoke，`artifact_root=runtime` 且源码树无新增 provider artifact；未自动记录 acceptance。
- `cd atlas-web && npm run gen && npm run verify-data`：1,805 leaves、270 sections、33 apps；无缺失/过期生成文件或 provenance/死链门禁错误。
- `cd atlas-web && npm run typecheck`：通过。
- `cd atlas-web && npm test`：9/9 passed。
- `cd atlas-web && npm run build`：通过；主入口约 379.01 kB，低于 500 kB 预算。
- `cd atlas-web && npx playwright test --repeat-each=3`：51/51 passed（含 10 路由矩阵，重复三次）；backup/restore 管理场景单独 1/1 passed。
- `npm_config_registry=https://registry.npmjs.org npm audit --audit-level=high`：0 vulnerabilities。
- `git diff --check`：通过。

详细页面证据见 `docs/U17_PAGE_AUDIT.md`、`docs/U17_PAGE_POLISH_PLAN.md` 和 `WORKLOG.md`；外部限制与解除条件见 `BLOCKERS.md`。

## Next Plan

剩余工作的分阶段顺序、依赖、外部条件和验证矩阵见 [`docs/U17_REMAINING_PRODUCT_PLAN.md`](docs/U17_REMAINING_PRODUCT_PLAN.md)。T025-T027、T029-T032 已完成；下一步仅剩 T028 的远程 CI、签名、公证和目标平台环境。

## Remaining Blockers

- 分类 provider 的真实成功/失败门禁已完成；当前可用模型为 `qwen3.8-flash`，`opencode-go/deepseek-v4.1-flash` 的不可用状态已记录为 provider 限制。目标发布环境仍需复验。
- 远程 CI、macOS 签名/公证和完整 OS/容器隔离没有在本轮范围内验证；固定验证器不能被描述为 OS 沙箱。
- T026 已在本地和 disposable real provider smoke 中固定 runtime containment；目标发布环境仍需重复验证，且该边界不是 OS/容器沙箱证明。
- 仍有已记录的产品 P2 跟进项，例如目标发布环境复验和未纳入本轮的长期运维策略。
- 工作树包含本轮及此前审计的未提交修改；没有自动 commit、push 或创建 PR。

## Run Instructions

See `README.md`, `docs/U17_PAGE_POLISH_PLAN.md` and `docs/U17_REMAINING_PRODUCT_PLAN.md`.

## Final Marker

`PROJECT_ACCEPTED` is intentionally not written until the declared external verification and remaining product follow-ups are explicitly resolved; local T025-T027/T029-T032 acceptance is complete.
