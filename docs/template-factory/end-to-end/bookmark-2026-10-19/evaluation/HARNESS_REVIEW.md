# 预验收 Harness 修订记录

Sol 在真实产品验收开始前对独立 harness 做了四项静态审查。本记录只说明 harness 适配与合成自检；四项均不是应用失败，也不构成产品验收通过。冻结的 `PLAN.md`、`SCOPE_NOTE.md`、`freeze.json` 未修改。

审查对象为冻结候选模板 `tpl_934bc93157f948b982459a9affa72c79`，digest `3bbcbb2a2685f188756e5b47dd27ac606f11f72359910e09023084758bd972c1`，位于 `application-atlas-production-pack/atlas/template-factory/jobs/job_b33d0a3f57cd4c628f4b4070750f7cd0/attempt-3/bundle`。

| 静态发现 | 修订 | 合成验证 |
| --- | --- | --- |
| 保存第二条书签后，旧 UI 流程只验证搜索命中，未确认其链接最终指向准确 URL。 | 初次保存时实际点击第二条书签；重复提交前后、以及真实 Docker 重启后，对每条匹配记录实际导航并比对精确目标 URL，同时记录 id、标题、href、可见行文本和导航方式。 | [`synthetic-review/ui-final-2/result.json`](synthetic-review/ui-final-2/result.json)：本地 fixture 证明直链和 `/go/<id>` 均实际到达精确 fixture URL。 |
| 重复保存会把标题改为 `Repeated`，但重启检查仍拿最初标题比较，可能误报合法 upsert 更新为持久化失败。 | 保存重复操作前后的完整可见行快照与实际目标导航；通过 id、标题、href、行文本和最终 URL 对照重启后观察状态。将行为分类为新建、更新、拒绝、无可见变化或记录集合变化。默认仅记录风险观察；只有调用者明确指定冻结契约 `unique-url` 或 `idempotent` 才按该承诺判失败。idempotent 通过同一更新 payload 的精确重放并比较快照判断。 | 同一 evidence 的 `duplicateOutcomes` 覆盖 upsert 更新、新建、拒绝、无变化与 idempotency 快照比较。冻结模板 `ARCHITECTURE.md` 将规范化 URL 唯一索引明确列为 P1；A14 亦为 P1。因此本次 P0 默认使用 `observe`，不把 P1 规则加到冻结 P0 验收门槛。 |
| XSS 标记只在搜索页检查，可能漏掉只在保存后首响应执行、之后被导航清除的脚本。 | 在首次导航前安装 browser init observer，将 `window.__atlasXss` 被赋值的事实写入同源 `sessionStorage`；保存响应返回后立即检查，并在后续导航后再次检查；重启阶段也检查 observer 记录。 | [`synthetic-review/ui-final-2/result.json`](synthetic-review/ui-final-2/result.json) 中合成保存响应的 onerror 执行被记录为 `1`，且安全导航后记录仍在，证明传感器能发现该时序。此处合成响应故意执行脚本，只验证观察机制，不是应用测试。 |
| Docker 镜像缺失或 daemon 不可用时抛出的 `CalledProcessError` 会落为 `failed`，从而把环境阻塞归为产品失败。 | runner 增加 daemon、镜像、本地网络和容器创建阶段标记。daemon/image/setup 阶段错误归类为 `blocked` 并记录 `failure_kind`；应用启动后的 readiness 失败仍保留为产品或验收失败。 | [`synthetic-review/docker-classification.json`](synthetic-review/docker-classification.json) 使用合成异常验证 daemon/image/setup 为 blocked，应用 readiness 为 failed。没有访问 Docker daemon、启动镜像或应用。 |

候选架构确认了字段与页面契约：捕获表单 `POST /bookmarks`（`url`、`title`、可选 `collection_id`），归类表单 `POST /collections`（`name`），移动表单 `POST /bookmarks/<id>/move`，检索 `GET /?collection=&q=`；bookmark/collection 列表项使用 `li.bookmark[data-bookmark-id]`、`li.collection[data-collection-id][data-default]`。架构允许通过记录标题链接或 `/go/<id>` 打开原页；harness 对两种形式都要求真实到达保存 URL。A08 的 HTTP 套件只检查 302 Location 而不跟随外部跳转，故实际浏览器点击由独立 UI harness 补足。

冻结模板 P0 另明确 A09 不重启服务；本 harness 的 Docker restart 证据是独立补充项，不能由 A09 替代。模板的 acceptance suite 和候选应用都没有在此过程中运行。

## 后续 UI 导航适配复核

Sol 后续发现 fixture 标题检查和点击后的页面状态恢复需要覆盖第二条记录。`openOriginal` 现在按已知 fixture 路径分别检查 `/original` 与 `/second` 的标题；验证 URL、页面内容并截图后，始终回到 `APP_URL`，有传入归类 ID 时重新打开该归类。弹窗先验证并关闭，再恢复父页的应用状态。重复记录快照采集器随后恢复关键词结果页。

新的原始合成证据为 [`synthetic-review/ui-page-recovery-3/result.json`](synthetic-review/ui-page-recovery-3/result.json)。同一运行覆盖 `/original` 和 `/second` 的直链与 `/go/<id>` 302；其中 `/second` 直链使用新标签页。四次点击均核对最终 URL 与各路径对应的 heading，均记录 `restoredApp: true` 和归类 `7`；最后成功读取归类列表。此结果只证明 harness 的导航、恢复与 fixture 适配，不代表产品通过。

## Runner 可靠性修订（Docker 不可用期间）

初次真实 runner 启动曾因 Docker CLI 阶段长期等待而在 cleanup 中被中断。原 `evaluation/initial/interruption.json` 保留为不完整环境事件；没有据此归因应用，也没有覆盖初次目录。

后续 runner 修复只在 harness 中完成：Docker CLI 默认超时 30 秒，daemon/image 预检 10 秒，网络建立 15 秒，restart 30 秒，inspect/cleanup 10 秒；浏览器依赖发现和 UI 阶段也有明确上限。超时成为明确的环境阻塞类别。runner 在创建临时数据目录、fixture server、Docker 网络或容器前原子写入初始 `run.json`，含唯一资源名与计划命令；阶段切换前后更新原子日志。cleanup 各步骤分别有界调用、独立捕获异常并继续，逐步原子记录 remove/absence verification、fixture、临时数据的结果；清理不完整会明确留下 failed 状态。

[`test_runner_reliability.py`](test_runner_reliability.py) 的三个 mock-only 单元检查通过，结果在 [`synthetic-review/reliability-1/result.json`](synthetic-review/reliability-1/result.json)，原始测试输出在同目录 `unittest-output.txt`。测试覆盖 Docker timeout 有界且归类环境阻塞、一个 cleanup 步骤失败后继续执行并仍落盘、初始日志在受控资源创建前写入。所有 Docker 调用均由 mock 替代，没有发送 Docker CLI 命令，也没有运行应用。

本轮又补入中断标记：主流程的 `KeyboardInterrupt` 写入独立 `interruption.json`；若中断发生在 cleanup 某一步，该步会被记录为失败，仍尝试后续 cleanup，并保留中断阶段。此行为由 [`synthetic-review/reliability-2/result.json`](synthetic-review/reliability-2/result.json) 中的第四项 mock 检查验证。它与 `initial/interruption.json` 是不同运行的记录，不覆盖初次环境中断证据。

## 真实运行中的 harness 适配记录

`initial-retry-1` 保留首轮 Docker 已启动、但 Playwright 在临时 `HOME` 下解析出不存在的浏览器缓存路径的原始失败；补充 `classification-correction.json` 将其归类为 harness 路径解析阻塞。修订后的浏览器可执行文件发现使用 allowlist 环境解析 Playwright 已安装二进制，真正启动 Chromium 时仍使用临时 `HOME`。独立的真实 Chromium 合成启动证据在 [`synthetic-review/browser-preflight-1/result.json`](synthetic-review/browser-preflight-1/result.json)。

`initial-retry-2` 保留 UI 脚本在 XSS sentinel 输入前尝试显式选择默认归类、但没有匹配 option 的中断。核心脚本前序流程已运行到 HTML 安全测试前，但初始阶段和重启阶段都没有完成，因此该目录不是验收通过；这次失败分类为 harness UI 适配阻塞，不归为产品失败。修正后的 sentinel 提交省略 `collection_id`，与冻结计划的默认归类用户操作一致。原 run.json 未修改，补充分类说明为 `initial-retry-2/classification-correction.json`。

Sol 针对 cleanup 的后续静态复核发现：清理中断可能覆盖此前的主失败；cleanup 前后日志持久化受到 `KeyboardInterrupt` 时会跳过回收。runner 现将原故障复制到 `primary_failure`，cleanup 中断写入单独 `cleanup_interruptions` 和 `interruption.json`，cleanup 各步的 journal 写入异常被记录后仍继续回收。五个 mock-only 测试通过，覆盖原故障保留和 journal 中断后继续 cleanup；新证据在 [`synthetic-review/reliability-3/result.json`](synthetic-review/reliability-3/result.json)。

## 事后 HTTP 探针解析复核与 cleanup 最终汇总

Sol 复核发现 `posthoc-http-1/2` 的 HTML 计数依据不足：页面含有嵌套列表，`data-collection-id` 也可能出现在非归类节点。两轮原始 `run.json` 未改动，`classification-correction.json` 明确将其标为 harness 测量无效，不作产品证据。探针现只统计 `li` 的精确 `collection` / `bookmark` class token，按 ID 去重并保存每轮 HTML；先用临时创建的已知分类与应用实际 HTML 做数量/ID 交叉核验，再评估目标输入。修订后的 `posthoc-http-3/run.json` 和 HTML 快照给出 CRLF 与并发观察；它们是冻结 P0 后的独立探索。

Sol 追加的 cleanup 聚合审查也已关闭：最终汇总统一检查资源移除、cleanup journal 错误和中断；成功流程遇到 evidence OSError 不会保持 `passed`，遇到 cleanup KeyboardInterrupt 则标为 `interrupted` 并以 130 退出。已有 `primary_failure` 不会被 cleanup 事件覆盖。七项 mock-only 检查覆盖该行为，证据见 [`synthetic-review/reliability-4/result.json`](synthetic-review/reliability-4/result.json)。
