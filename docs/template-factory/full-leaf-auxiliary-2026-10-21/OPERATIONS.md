# 全量辅助计划操作

以下命令在仓库根目录执行。生产模型固定 opencode-go/minimax-m3.1-flash-free，禁止自动fallback。只有本 full_plan_id 可用新增7200；历史99和旧500记录保留，不叠加原401。真实起点以登记回执为准。

```sh
python3 examples/assisted-trials/produce_all_leaves.py freeze
python3 examples/assisted-trials/produce_all_leaves.py register
python3 examples/assisted-trials/produce_all_leaves.py start
python3 examples/assisted-trials/produce_all_leaves.py status
python3 examples/assisted-trials/produce_all_leaves.py pause
python3 examples/assisted-trials/produce_all_leaves.py resume
python3 examples/assisted-trials/produce_all_leaves.py start
python3 examples/assisted-trials/produce_all_leaves.py stop
```

freeze/register 是准备和正式限额登记，不是模型启动。start 使用 macOS launchd，持久任务为 `gui/$(id -u)/com.atlas.full-leaf-auxiliary-20261021`，配置保存在本目录 coordinator.plist。resume 只恢复正式派发资格；如进程已退出，再执行start。`run`是可选的前台执行入口，与launchd共用唯一协调锁，不能同时运行。stop永久停止该计划的自动派发，暂停使用pause。

```sh
launchctl print gui/$(id -u)/com.atlas.full-leaf-auxiliary-20261021
tail -f docs/template-factory/full-leaf-auxiliary-2026-10-21/runner.log
cat docs/template-factory/full-leaf-auxiliary-2026-10-21/PROGRESS.json
```

运行不依赖聊天/终端常驻；本机休眠、关机、离线时不会生产。30天窗口从首次真实受控预留激活，恢复不重置。开机/登录后如launchd未重新加载，用start恢复。START_RECEIPT、PROCESS和launchctl实际PID一起证明进程是否存在，不能用历史回执推断当前在线。

协调者每批最多20项，最多两个依赖串行的叶子worker，模型预留仍受全局事务约束。首轮全部处理后才进入一次内容修订队列；协议恢复同一叶子合计至多一次。新attempt绑定旧失败摘要，新审阅不接收作者会话或旧审阅结论。budget_concurrency等待槽位，不算内容失败。

失败的原文、summary和调用预留保留。只重放已交付检查点不新增调用；失败/不确定启动不能删除意图再调用。已证明未启动的预留可以带原summary建立后继工作目录；不确定真实启动先暂停，对照process.json、原始输出和账本核对。不得将uncertain改成not_started。必要时仅在确认自有进程全部停止后使用既有 BudgetLedger.mark_recovered_unknowns 服务保留计数释放并发，并记录停止证明；再按一次协议恢复与每叶子6次界限接续。

来源网络/认证/额度或全局授权损坏暂停计划，保留pending/paused。单项真实研究无源、格式或内容问题单项记录后继续；未运行应用默认not_run。低于5GiB可用磁盘暂停，不删除原模板/应用/用户数据。

原始calls是本机权威恢复材料；已结束项audit的重复副本压缩到audit-evidence.zip及逐文件摘要，固定上游材料有upstream-evidence.zip。只清理可从权威副本恢复的材料和冻结ZIP展开副本，不删除原始调用。源码/授权/冻结范围/限制变更会触发完整性停止，不改FROZEN_SCOPE绕过。

SOURCE/CASE/模板绑定与标准包由正式服务完成。已有18份及六应用不重建。实际状态由PROGRESS、RESULTS和CALL_LEDGER分别给出已尝试、已处理、可用、失败、未开始、在途与暂停。handled包括明确的失败终态，覆盖率仅按不同叶子的reused/ready_not_run算。

历史严格G1/T08仍blocked/未启动；全量任务不改变其grant/修复/期限。新增模板只代表辅助独立静态审阅，不代表上游运行、目标应用运行或正式严格发布。

## 最新 workflow 门禁

用户要求先在少量叶子上验证自动执行、恢复、自动接续，当前全量派发保持暂停。新宿主源码通过精确CI并追加 host revision 后，先用 `workflow-validation --leaf ...` 登记固定验证清单，`workflow-replay --leaf calendar-application` 校验已有完成项不新增调用，再 resume/start。验证模式在预算预留事务中限制范围，不仅过滤内存列表；缺门禁不能启动。

具体清单及最新状态见 `../workflow-hardening-2026-10-21/WORK_PACKAGE.md` 和该目录真实回执。验证清单完成后协调者自动暂停。仅当真实新产物的八步、摘要与下载均通过，恢复/失败隔离证据完整时，使用 `workflow-open-full --evidence <真实验证报告JSON>` 正式开放全量；不能把旧模板接纳或fixture当新产物通过。开放门禁本身不启动模型，仍需原计划resume/start。原30天窗口、账本和失败保持。

只读进度：`http://127.0.0.1:5188/factory?view=workflow`；接口 `/api/factory/auxiliary-workflows` 及 `/<plan_id>?offset=0&limit=20&state=&q=`。步骤产物下载仅允许正式记录中摘要吻合的文件，不能传任意路径。
