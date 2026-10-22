# 分轮运行

保留原 full-leaf-auxiliary-2026-10-21、全部1805固定叶子、Open Design DeepSeek模型和账本。每叶累计六次、并发二、7200本计划新增上限、原30天截止不变。

## 三叶修订验证

先完成精确源码CI并正式激活host revision，再从原paused状态执行：

```sh
python3 examples/assisted-trials/produce_all_leaves.py workflow-round --evidence docs/template-factory/workflow-rounds-2026-10-22/PILOT_ROUND_REQUEST.json
python3 examples/assisted-trials/produce_all_leaves.py start --leaf e-book-library-application --leaf markdown-editor --leaf resource-calendar
```

pilot_complete只调原三叶已有的一轮内容修订和新独审；不重新研究，不重置次数。完成后自动暂停。首次生效的正式请求/回执及实际状态优先于历史幂等receipt。

## 全量首轮

新修订真实独审、入库、下载及零调用重放通过后，固定原1805全范围：

```sh
python3 examples/assisted-trials/produce_all_leaves.py workflow-round --evidence docs/template-factory/workflow-rounds-2026-10-22/FULL_ROUND_REQUEST.json
python3 examples/assisted-trials/produce_all_leaves.py start
python3 examples/assisted-trials/produce_all_leaves.py status
```

`.prepared.json`只表示草案，不能当已激活或已运行。实际FULL_ROUND_REQUEST含本轮新验证证据摘要；FULL_START_RECEIPT和正式状态证明真实启动。start复用同一launchd，移除原三叶参数前核验旧进程退出且活动调用0，不启动第二个协调者。

首轮按批20自动接续，仅first lane。原已完成/复用/失败结果不覆盖，原暂停未完成项走合法检查点续作。单项已知错误记录后继续，整轮后暂停；不自动进入内容修订第二轮。`ROUND_REPORT.json`及`round-reports/<timestamp>.json`记录叶子、状态、失败阶段、错误码、原因、证据目录和制品。

```sh
launchctl print gui/501/com.atlas.full-leaf-auxiliary-20261021
cat docs/template-factory/full-leaf-auxiliary-2026-10-21/PROGRESS.json
cat docs/template-factory/full-leaf-auxiliary-2026-10-21/ROUND_REPORT.json
```

不需要逐叶人工盯守。已识别的协议错误（含有限恢复耗尽）、模板内容、无源、单项交付错误保留证据继续；固定输入或来源完整性损坏、未知宿主异常、数据库故障、磁盘不足、总预算/到期、调用状态不明和持续公共服务故障必须正式暂停。保留检查点，不盲目补调或直接改库。

本机休眠/关机/离线时不保证继续；恢复使用同一任务与正式状态，不重领授权。全量结束后集中分析原因，再决定第二轮，不在首轮看到低通过率就逐项修或改变门禁。严格G1/T08及应用开发不在本轮。


## 本轮宿主修复后续作

全量full_first_round已正式登记、实际在运行时不重复激活、start或resume。当前原三叶pilot已完成（两通过一待修订），原暂停兼容问题已由fa630f8及CI39709062560修复。真实状态以FULL_RESUMED_STARTED及正式status为准，不将旧暂停回执当当前状态。

若之后出现正式全局暂停，先读原因/在途状态；不能对uncertain或完整性故障盲目resume。只有已核实故障解除、同一全量范围仍有效且active0时，沿原服务control/resume及既有start续作，保留当前轮次，不重领授权。当前全量首轮结束后应等待集中分析，不自动resume第二轮。后台日志和根ROUND_REPORT持续写，跟进每6小时轻量读取全局，普通单项错误不触发人工逐叶干预。
