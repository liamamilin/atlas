# TASKS

- [x] T001: 建立全页面审查矩阵和真实浏览器巡检
  - Goal: 覆盖所有用户路由、桌面/移动视口、加载/错误/空态证据。
  - Files: docs/U17_PAGE_AUDIT.md, docs/U17_PAGE_POLISH_PLAN.md
  - Validation: `git diff --check`
  - Status: done
  - Blocked By:

- [x] T002: 阻止草稿 dirty 正文绕过审阅直接发布
  - Goal: 查重、翻译、入库绑定 body revision/hash，dirty 或 revision 冲突时拒绝。
  - Files: atlas-web/src/routes/drafts.tsx, application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/promote_draft.py, application-atlas-production-pack/tests/test_reliability.py, atlas-web/e2e/tests/core.spec.ts
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability.CorpusTests.test_draft_body_revision_rejects_stale_save_and_promote -q`; `cd atlas-web && npx playwright test --grep "draft editor"`
  - Status: done
  - Blocked By:

- [x] T003: 修复草稿生成完成 hydration 和 generation 列表缓存
  - Goal: 生成结果及时进入编辑器，活跃 generation 不被旧缓存隐藏。
  - Files: atlas-web/src/routes/drafts.tsx, atlas-web/src/routes/project-detail.tsx, atlas-web/src/lib/atlas.ts, atlas-web/tests/atlas-request.test.ts, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npm test && npx playwright test --grep "draft generation completion"`
  - Status: done
  - Blocked By:

- [x] T004: 修复草稿发布状态冲突和 slug/写入并发
  - Goal: 发布状态唯一投影，slug namespace 和保存/查重/promote 跨进程互斥。
  - Files: application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/draft_new.py, application-atlas-production-pack/review_store.py, application-atlas-production-pack/tests/test_reliability.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（186 项通过，含并发/状态冲突回归）
  - Status: done
  - Blocked By:

- [x] T005: 修复草稿生成/翻译恢复、轮询和 SPA 导航保护
  - Goal: 中断可收口、翻译 single-flight、轮询可取消、dirty 导航不丢编辑。
  - Files: application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/draft_new.py, application-atlas-production-pack/tests/test_reliability.py, atlas-web/src/routes/drafts.tsx, atlas-web/src/main.tsx, atlas-web/e2e/tests/core.spec.ts
  - Validation: 后端 190 current/clean；`cd atlas-web && npx playwright test --repeat-each=3`（15/15）
  - Status: done
  - Blocked By:

- [x] T006: 修复类型页正式资料 source 映射和静态 fallback
  - Goal: 无正式资料时显示稳定空态；无 API 预览不产生未处理 404。
  - Files: atlas-web/src/routes/leaf.tsx, atlas-web/src/components/source-reader.tsx, atlas-web/src/lib/atlas.ts, atlas-web/vite.config.ts, application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/tests/test_reliability.py, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npx playwright test --grep "source fallback"`; backend source contract regression
  - Status: done
  - Blocked By:

- [x] T007: 补齐公共内容别名搜索、关系和数据门禁
  - Goal: aliases 可搜索，关系 key 唯一，Markdown 链接和静态数据可验证。
  - Files: atlas-web/scripts/gen-data.py, atlas-web/scripts/verify-web-data.py, atlas-web/src/lib/atlas.ts, atlas-web/src/routes/search.tsx, atlas-web/src/routes/leaf.tsx, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npm run gen && npm run verify-data && npx playwright test --repeat-each=3`（21/21）
  - Status: done
  - Blocked By:

- [x] T008: 修复工作台状态真实性、revision CAS 和项目切换隔离
  - Goal: 验收 focus 正确、旧 execution 不覆盖新状态、审批带 revision、项目级 state 不串数据。
  - Files: application-atlas-production-pack/project_store.py, application-atlas-production-pack/project_generation.py, application-atlas-production-pack/project_workflow.py, application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/tests/test_reliability.py, atlas-web/src/routes/project-detail.tsx, atlas-web/src/lib/atlas.ts, atlas-web/e2e/tests/core.spec.ts
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（195 passed）；`cd atlas-web && npx playwright test --repeat-each=3`（24/24）
  - Status: done
  - Blocked By:

- [x] T009: 收紧权限资源、验证器完整性和扫描资源上限
  - Goal: 权限回复校验 resource/pattern；验证保护测试文件；工作区扫描拒绝根目录和超大输入。
  - Files: application-atlas-production-pack/execution_service.py, application-atlas-production-pack/opencode_permissions.py, application-atlas-production-pack/workspace_snapshot.py, application-atlas-production-pack/tests/test_reliability.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（198 passed）；source Ruff/compile；frontend typecheck/unit/build; full E2E 24/24
  - Status: done
  - Blocked By:

- [x] T010: 建立草稿轮询 stale/retry 状态机
  - Goal: 轮询失败时显示最后成功更新时间和手动重试，不静默使用旧状态。
  - Files: atlas-web/src/routes/drafts.tsx, atlas-web/tests/
  - Validation: 已由 T005 覆盖；`cd atlas-web && npx playwright test --grep "draft polling"`
  - Status: done
  - Blocked By: T003

- [x] T011: 补齐未知路由、错误返回和 route error boundary
  - Goal: 404/加载失败/懒加载失败都有明确下一步。
  - Files: atlas-web/src/app.tsx, atlas-web/src/main.tsx, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npx playwright test --repeat-each=3`（27/27）；typecheck/build
  - Status: done
  - Blocked By:

- [x] T012: 修复移动溢出和表单可访问名称
  - Goal: 320/375/768px无非预期 body overflow，草稿正文控件有 label。
  - Files: atlas-web/src/components/prose.tsx, atlas-web/src/routes/drafts.tsx, atlas-web/src/routes/browse.tsx, atlas-web/src/components/source-reader.tsx, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npx playwright test --grep "mobile"`；full E2E 30/30
  - Status: done
  - Blocked By:

- [x] T013: 搜索页和教程语言闭环
  - Goal: 搜索可直接改写 query；英文教程不混入长段中文。
  - Files: atlas-web/src/routes/search.tsx, atlas-web/src/routes/tutorial.tsx, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npm run typecheck && npm test && npx playwright test --repeat-each=3`（33/33）
  - Status: done
  - Blocked By: T007

- [x] T014: 拆分项目详情领域组件
  - Goal: 在行为测试保护下降低 1433 行单文件复杂度。
  - Files: atlas-web/src/routes/project-detail.tsx, atlas-web/src/components/
  - Validation: `cd atlas-web && npx playwright test --grep "project"`（1/1）；typecheck/unit/build；full E2E 36/36
  - Status: done
  - Blocked By: T008

- [x] T015: 资料收藏 fingerprint 握手
  - Goal: 收藏请求绑定用户看到的来源 fingerprint，版本变化返回 409。
  - Files: application-atlas-production-pack/drafts_api.py, atlas-web/src/lib/atlas.ts, atlas-web/src/components/source-reader.tsx, application-atlas-production-pack/tests/test_reliability.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（199 passed）；frontend typecheck/E2E 33/33
  - Status: done
  - Blocked By: T006

- [x] T016: Apps hash 深链和公共链接可访问性
  - Goal: hash 目标可靠滚动/聚焦，失效 hash 有明确空态。
  - Files: atlas-web/src/routes/apps.tsx, atlas-web/e2e/tests/core.spec.ts
  - Validation: `cd atlas-web && npx playwright test --grep "apps hash"`；full E2E 36/36
  - Status: done
  - Blocked By: T007

- [x] T017: 公共内容英文/链接/来源 provenance 收口
  - Goal: Apps/关系标签双语可解释，canonical Markdown 内部链接可导航，分类证据可见。
  - Files: atlas-web/scripts/gen-data.py, atlas-web/src/routes/apps.tsx, atlas-web/src/routes/leaf.tsx, atlas-web/src/components/prose.tsx, atlas-web/scripts/verify-web-data.py
  - Validation: `cd atlas-web && npm run gen && npm run verify-data`（1,805/270/33）；typecheck/unit/build；full E2E 39/39
  - Status: done
  - Blocked By: T016

- [x] T018: generation/delete 与 restore journal 生命周期锁
  - Goal: 项目删除和 generation 共享生命周期锁；restore 每个崩溃窗口可验证。
  - Files: application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/project_generation.py, application-atlas-production-pack/project_backup.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（204 passed，含 lifecycle lock、hard-link、artifact replacement crash fixtures）
  - Status: done
  - Blocked By: T008

- [x] T019: 全页面错误/空态/语言/无障碍矩阵
  - Goal: 10 路由覆盖正常、错误、空态、375/768px 和语言切换，形成持续门禁。
  - Files: atlas-web/e2e/, atlas-web/src/components/loaders.tsx, atlas-web/src/styles.css
  - Validation: `cd atlas-web && npx playwright test --repeat-each=3`（51/51）；typecheck/unit/build；`git diff --check`
  - Status: done
  - Blocked By: T011, T012

- [x] T020: 最终跨环境验证与报告收口
  - Goal: 复跑当前/干净 Python、前端构建与完整 E2E，记录 audit、差异和外部限制，不扩大安全声明。
  - Files: FINAL_REPORT.md, PROJECT_STATE.md, WORKLOG.md, TASKS.md
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && uv run --python 3.11 --with-requirements requirements.txt python -m unittest application-atlas-production-pack.tests.test_reliability -q && cd atlas-web && npm run gen && npm run verify-data && npm run typecheck && npm test && npm run build && npx playwright test --repeat-each=3 && npm_config_registry=https://registry.npmjs.org npm audit --audit-level=high && cd .. && git diff --check`
  - Status: done
  - Blocked By:

- [x] T021: 任务输入门禁与验收 provenance 绑定
  - Goal: API 新任务不能脱离固定文档/需求；验收记录绑定 execution、baseline、需求修订和条件快照，详情页可审查。
  - Files: application-atlas-production-pack/execution_service.py, application-atlas-production-pack/project_store.py, atlas-web/src/routes/project-detail.tsx, atlas-web/src/lib/atlas.ts, application-atlas-production-pack/tests/test_reliability.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（206 passed，重复 5 次）；干净 Python 3.11 206 passed；`npm run gen && npm run verify-data`（1,805/270/33）；typecheck/unit/build；`npx playwright test --repeat-each=3`（51/51）；`npm audit --audit-level=high`（0 vulnerabilities）；`git diff --check`
  - Result: API 任务创建拒绝空文档/需求输入；验收证据由 Atlas 生成不可伪造的 execution、baseline、固定文档、需求修订和验收条件快照；工作台展示绑定详情；并发草稿测试不再污染全局 collision mock。
  - Status: done
  - Blocked By:

- [x] T022: 逐条件人工验收结果与历史兼容
  - Goal: 新验收决策为每条固定验收条件记录明确结果和说明；旧记录继续可读并清楚标记未回填，不伪造历史结论。
  - Files: application-atlas-production-pack/project_store.py, application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/atlas_cli.py, atlas-web/src/lib/atlas.ts, atlas-web/src/routes/project-detail.tsx, application-atlas-production-pack/tests/test_reliability.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（207 passed，重复 3 次）；干净 Python 3.11 207 passed；`npm run gen && npm run verify-data`（1,805/270/33）；typecheck/unit/build；`npx playwright test --repeat-each=3`（51/51）；`npm audit --audit-level=high`（0 vulnerabilities）；`git diff --check`
  - Result: 新验收要求每条 pinned condition 有明确结果和可选说明，服务端校验完整性并拒绝伪造/不匹配结果；任务响应带不可变 requirement snapshot；工作台逐条编辑并展示结果，旧记录明确显示未回填；CLI 保持兼容并提交整体决定的条件投影。
  - Status: done
  - Blocked By: T021

- [x] T023: 真实 OpenCode Go provider 闭环与轮询硬化
  - Goal: 用临时隔离项目验证真实 provider execution/apply，并修复 OpenCode 可选端点 404 和多段 assistant 消息造成的过早 unknown。
  - Files: application-atlas-production-pack/opencode_client.py, application-atlas-production-pack/execution_state.py, application-atlas-production-pack/tests/test_reliability.py, docs/U17_EXECUTION_BACKEND_DECISION.md, TASKS.md, ACCEPTANCE.md, BLOCKERS.md, FINAL_REPORT.md, PROJECT_STATE.md, WORKLOG.md
  - Validation: current/clean Python 209 passed；真实 `opencode-go/deepseek-v4.1-flash` analysis completed；临时 code task fixed verification passed、scope compliant、apply adopted new baseline；`ruff`/`git diff --check` passed
  - Result: `deepseek-v4-flash` 对当前凭据被 provider 明确拒绝；`deepseek-v4.1-flash` 的真实 session、Atlas execution、独立固定验证和显式 apply 均成功；凭据未写入仓库或报告；未自动产品验收。
  - Status: done
  - Blocked By: T021

- [x] T024: 真实 generation→backup→restore 与结果契约硬化
  - Goal: 让 generation 在 OpenCode 事件只返回文本时仍能安全恢复完整结果，并验证临时 generation 备份可恢复到新的空项目库。
  - Files: application-atlas-production-pack/project_generation.py, application-atlas-production-pack/tests/test_reliability.py, docs/U17_EXECUTION_BACKEND_DECISION.md, TASKS.md, ACCEPTANCE.md, BLOCKERS.md, FINAL_REPORT.md, PROJECT_STATE.md, WORKLOG.md
  - Validation: current Python 211 passed；clean Python 3.11 offline cache 211 passed；真实 `opencode-go/deepseek-v4.1-flash` generation completed；backup schema 1 validated；restore 到新空库后 generation/result 可读；`ruff`/`git diff --check` passed
  - Result: generation 固定输入以内联方式传给模型；仅接受完整 shape 与 fingerprint 匹配的 JSON 文本 fallback；不接受 symlink/超大/不完整结果；未 apply 生成结果，备份不含用户源码。
  - Status: done
  - Blocked By: T021

- [x] T025: 浏览器 backup/restore 管理入口
  - Goal: 在不暴露任意主机路径的前提下，让用户查看备份、选择受控恢复目标并明确确认恢复到新的空项目库。
  - Files: application-atlas-production-pack/project_backup.py, application-atlas-production-pack/drafts_api.py, atlas-web/src/lib/atlas.ts, atlas-web/src/routes/projects.tsx, application-atlas-production-pack/tests/test_reliability.py, atlas-web/e2e/tests/core.spec.ts
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && cd atlas-web && npm run typecheck && npm test && npx playwright test --grep "backup"`（215 passed；typecheck/unit/build 通过；backup E2E 1/1；`git diff --check` 通过）
  - Result: 浏览器可列出并校验备份、下载备份、准备 opaque `restore_id`、查看受控目标、显式确认恢复到新的空项目库并查看 restore status；API/UI 不接受任意主机路径，不返回 archive/store 绝对路径；restore root 拒绝与源码工作区重叠；用户源码不进入备份。
  - Status: done
  - Blocked By: T024

- [x] T026: Provider 产物路径隔离与 generation 输出契约
  - Goal: 保证 OpenCode generation 产物只进入 Atlas runtime/登记 artifact 目录，源码树出现 provider 文件时 fail closed。
  - Files: application-atlas-production-pack/project_generation.py, application-atlas-production-pack/opencode_cli_adapter.py, application-atlas-production-pack/privacy.py, application-atlas-production-pack/tests/test_reliability.py, SECURITY.md
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && git diff --check && git status --short`（213 passed；project_generation Ruff passed；真实 `opencode-go/deepseek-v4.1-flash` disposable generation passed；源码树无新增 provider artifact）
  - Result: V2 runtime 现在显式初始化临时 Git project root，写入 `.opencode/opencode.json`，只允许 edit `result.json`；运行前后扫描源码树，越界新增/修改/删除会写入 `provider-artifact-violation.json` 并 fail closed；runtime、engine、run artifact 仍可作为受控结果来源；真实 provider smoke 未写入仓库。
  - Status: done
  - Blocked By: T024

- [x] T027: Adjudicator/分类 provider 真实门禁
  - Goal: 明确并验证分类 provider、模型和失败边界，不把分类结果自动升级为需求或入库决定。
  - Files: application-atlas-production-pack/classify.py, application-atlas-production-pack/classify_pilot.py, application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/tests/test_reliability.py, docs/U17_EXECUTION_BACKEND_DECISION.md
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && git diff --check`（218 passed；真实 `qwen3.8-flash` classification success；`opencode-go/deepseek-v4.1-flash` failure mapped to `model_unavailable`；Ruff/compile passed）
  - Result: 分类 provider 现在返回脱敏、稳定错误码和 retryable 标志；不自动切换模型、不把分类结果升级为需求/入库；`classify_pilot.py` 不再在 import 时读取固定 key，默认遵循 `ATLAS_ADJUDICATOR`。
  - Status: done
  - Blocked By: T026

- [ ] T028: 发布 CI、构建产物与 macOS 签名门禁
  - Goal: 针对发布 SHA 重跑 CI、生成可校验 artifact，并完成目标 macOS 的签名/公证/安装回滚验证。
  - Files: .github/workflows/checks.yml, atlas-web/package.json, docs/U17_RELEASE_CHECKLIST.md, docs/U17_RELEASE_NOTES.md, SECURITY.md
  - Validation: `git diff --check && cd atlas-web && npm run typecheck && npm test && npm run build`
  - Status: blocked
  - Blocked By:

- [x] T029: OS/容器边界与人工安全审查
  - Goal: 完成威胁模型、权限/验证器/restore 越界审查，并明确哪些行为不是 OS/容器沙箱。
  - Files: SECURITY.md, docs/U17_SECURITY_REVIEW.md, application-atlas-production-pack/execution_workspace.py, application-atlas-production-pack/project_backup.py, application-atlas-production-pack/tests/test_reliability.py, docs/U17_RELEASE_CHECKLIST.md
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && git diff --check`（219 passed；本地凭据模式扫描无未允许命中；安全审查记录已写入）
  - Result: 已记录 API、workspace/apply、provider runtime、backup/restore、凭据和发布边界；明确 loopback、权限策略、固定验证器和路径检测不是 OS/容器沙箱；远程 CI、签名/公证和独立进程/容器验证仍为 release blocker。
  - Status: done
  - Blocked By:

- [x] T030: 旧验收数据 dry-run migration/backfill
  - Goal: 为历史 acceptance binding 提供可审计、幂等、不可伪造结论的迁移报告和回填流程。
  - Files: application-atlas-production-pack/project_store.py, application-atlas-production-pack/project_export.py, application-atlas-production-pack/drafts_api.py, atlas-web/src/routes/project-detail.tsx, application-atlas-production-pack/tests/test_reliability.py
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && cd atlas-web && npm run typecheck && npm test`（221 passed；typecheck/unit 8/8；迁移 API/导出/幂等回归通过；`git diff --check` 通过）
  - Result: 新增只读 dry-run 报告和固定确认令牌 backfill；缺失历史逐条件结果只标记 `not_backfilled`，不改变 acceptance_status、不推断 pass/fail；迁移在事务中幂等执行，导出包含迁移摘要，工作台显示待复核记录。
  - Status: done
  - Blocked By: T022

- [x] T031: Backup 生命周期、restore-status 与保留策略
  - Goal: 页面化展示 backup 历史、校验摘要、restore status、失败恢复和清理前确认。
  - Files: application-atlas-production-pack/project_backup.py, application-atlas-production-pack/drafts_api.py, atlas-web/src/routes/projects.tsx, atlas-web/src/lib/atlas.ts, application-atlas-production-pack/tests/test_reliability.py, atlas-web/e2e/tests/core.spec.ts
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && cd atlas-web && npm run typecheck && npm test && npx playwright test --grep "backup"`（219 passed；typecheck/unit 7/7；backup E2E 1/1；`git diff --check` 通过）
  - Result: backup 列表、校验摘要、restore status、显式归档删除和中断恢复清理均页面化；删除/清理需要固定确认令牌，列表缓存正确失效，Atlas 不自动清理或删除任何归档。
  - Status: done
  - Blocked By: T025

- [x] T032: Generation/provider/backup/restore 长尾错误契约
  - Goal: 统一稳定错误码、用户恢复建议、技术详情和前端中英文映射，避免泛化失败或错误重试。
  - Files: application-atlas-production-pack/drafts_api.py, application-atlas-production-pack/project_backup.py, application-atlas-production-pack/project_generation.py, atlas-web/src/lib/atlas.ts, atlas-web/src/components/project-detail-shared.tsx, application-atlas-production-pack/tests/test_reliability.py, atlas-web/e2e/tests/core.spec.ts
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q && cd atlas-web && npm run typecheck && npm test && npx playwright test --repeat-each=3`（221 passed；typecheck/unit 9/9；E2E 51/51；Ruff/compile/diff check passed）
  - Result: generation/provider/backup/restore 相关 API 错误带 `code/retryable/details`；generation run 保存 `error_code`；前端 `AtlasApiError` 和中英文 actionError 提供稳定恢复建议，不自动泛化重试。
  - Status: done
  - Blocked By: T025, T027
