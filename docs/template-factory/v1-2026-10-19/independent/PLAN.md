# Independent acceptance plan — frozen 2026-10-19

This plan fixes the first three real downstream targets before any runtime result is inspected. The selection is copied from the prescribed sampling plan and checked against `FactoryStore.scenarios()`; no app implementation or app-specific UI contract was used to choose assertions.

The plan hash is recorded in `PLAN.sha256` and covers `machineplan.json`. Do not edit the frozen machine plan. If a scenario revision/acceptance changes or a test requirement changes, create a new plan revision with a new digest and retain this one.

## Frozen targets

| Scenario | Leaf | Revision | Observed status | Execution gate |
|---|---|---:|---|---|
| 生活待购与灵感收藏夹 (`scn_7756e0007f6a463a97316f3f49c15248`) | `bookmark-manager` | 2 | `ready` | current admission policy must permit launch |
| 个人极简月度预算：先查剩余再消费 (`scn_6fb4896d9eb0428aa1c080df0a137813`) | `budgeting-application` | 1 | `draft` | current admission policy must permit launch |
| 多项目会议结论的归档与回查 (`scn_805c99ffe8da4532817592bb466a505e`) | `note-taking-application` | 1 | `draft` | current admission policy must permit launch |

The current store showed the bookmark target as `ready`, and the budget and meeting-note targets as `draft`. The draft targets remain preselected; the machine plan requires their current batch-admission rule to be satisfied before runtime execution. No draft is relabeled ready or treated as individually confirmed. A blocked admission does not authorize sample replacement.

## Independent core journeys

### 生活待购与灵感收藏夹

Scenario revision 2 has these fixed acceptance statements:
- 用户主动保存的链接在多次会话之间持久保留，形成不断增长的个人收藏
- 每条记录都以 URL 锚定到外部网页，打开记录即跳转到该页面
- 用户可以在归类之间移动记录或新建归类，操作结果在重新打开后仍然有效
- 通过归类浏览或关键字检索，用户能找到此前存入的特定链接

The runtime-specific high-risk cases fixed before execution are:
- save bookmark with title and URL
- assign category then move it to another category
- find by category and by keyword
- open and verify exact original URL using a controlled local fixture
- restart the same app container with the same persistent state and verify records remain
- reject malformed/non-http(s) URL without creating a record
- run concurrent independent saves and verify every acknowledged write is present exactly once

### 个人极简月度预算：先查剩余再消费

Scenario revision 1 has these fixed acceptance statements:
- 计划页对每个分配项同时显示计划金额、实际金额与剩余额度，并在录入支出后立即更新
- 任何一笔支出录入后，其所属分配项的剩余额度按该支出金额减少
- 分配项的实际支出超过计划金额后，其剩余额度显示为负数或明确的超支标记，而不是归零或隐藏
- 从分配项 A 转移金额到分配项 B 后，A 的剩余减少额与 B 的剩余增加额相同，计划总额不变
- 进入下一期后各分配项的计划金额回到模板数值，上一期剩余不被带入（未启用结转时）

The runtime-specific high-risk cases fixed before execution are:
- create a monthly plan and allocations with exact decimal money
- record spending and verify exact planned/actual/remaining arithmetic without binary-float drift
- exercise over-budget negative/explicit overrun state and balanced transfer
- cross a month boundary and verify new allocations reset to configured template amounts when rollover is off
- restart the same app container with the same persistent state and verify ledger and period values persist

### 多项目会议结论的归档与回查

Scenario revision 1 has these fixed acceptance statements:
- 笔记移入某项目笔记本后出现在该笔记本列表中，且同一时刻只归属一个容器
- 被置顶的笔记在所属容器列表的固定位置保持可见，不随按日期或标题排序而移动
- 删除笔记后它进入可恢复的回收状态，在保留期内可被恢复并回到库中原有位置
- 归档后的笔记不再出现在默认活跃列表，但通过全库搜索仍能找到并打开

The runtime-specific high-risk cases fixed before execution are:
- capture notes then move each into the intended project notebook with one-container ownership
- pin a note and verify stable top placement across sorting/reload
- archive notes out of active list while retaining full content
- search archived/history content across projects and open the exact retained note
- delete and restore within retention, verifying original container/content are restored
- restart the same app container with the same persistent state and verify archive/search/retention state persists

## Execution and evidence contract

- Profile: `python-web`; run the exact frozen application source and acceptance suite through the supplied delivery/runtime contract.
- Read application source only. Compute a deterministic source manifest and digest before running and again after the last assertion; any difference invalidates the result.
- Use a real Chromium browser against the running application and an owned loopback HTTP fixture for exact URL behavior. Do not permit external browser requests during the journey.
- Use a real local Docker image already available on the host; do not pull images. Mount the frozen application source read-only and persistent application state separately. Restart the same container and verify the same state after restart.
- The checks listed in the machine plan are mandatory; extra app-specific selectors or API/UI details may only be added from the frozen acceptance target contract once the parent supplies it. They may not narrow the fixed cases.
- Each `planned_core_cases` entry must appear verbatim as a mandatory assertion ID in the run's assertion manifest and in the browser adapter output. The runner checks the plan digest, selected scenario/revision, and that no frozen case was omitted.
- An all-pass result requires every mandatory assertion for that scenario, true process/container restart, persistence, unchanged source, complete logs and environment metadata. Any failure remains attached to that target.
- Emit `atlas.phase-evidence.v1` only after real execution. Required binding: `requirement_id=independent-core-journey`, `target_digest=store.digest(acceptance.target_binding)` from the actual target binding, scenario/revision, case basis, frozen target/source digest, template and suite digests, phase, environment, actual per-case assertions, and log references. Executor identity is `independent_executor / atlas-independent-acceptance-v1 / 1.0.0`.
- `target_binding` in the frozen plan is the selected scenario and acceptance snapshot used to fix the sample. The runtime proof digest is calculated from the separate, host-pinned generated-application `acceptance.target_binding` supplied for that actual run; the runner does not substitute the plan snapshot for the runtime binding.
- Do not register runtime evidence until actual application IDs and the target binding are provided. This preparation creates no runtime proof and asserts no G1 pass.

## Current readiness

Plan frozen. Runtime execution is pending delivery of real application identifiers, frozen target/acceptance bindings, suite digest, and parent confirmation that the current admission contract permits each selected target. No external model or paid service is needed or called.
