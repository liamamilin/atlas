# 全量辅助计划：已正式启动，持续运行中

本报告是启动检查点，不是全量完成报告。权威实时进度由原正式数据库中的 full_plan_id=full-leaf-auxiliary-2026-10-21 及本目录 PROGRESS.json / RESULTS.json / CALL_LEDGER.json 给出。查看命令见 [OPERATIONS.md](OPERATIONS.md)。

## 冻结范围与授权

当前目录解析器、正式本地索引、实际制品服务及18份标准包下载核对一致：1,805个有效叶子，18个不同叶子已有可用辅助模板，1,787个待处理，排除0。撤回的家庭保养旧候选仍是历史，不作为额外覆盖。首两项固定为支出跟踪、日历，后续按当前目录顺序，不替换失败项。

[FROZEN_SCOPE.json](FROZEN_SCOPE.json)保存每叶子正文SHA、分类路径、覆盖制品/案例/包摘要、旧失败、来源复用及profile。原附件ZIP、解压原文及CHECKSUMS均已保存并核对，见 [ATTACHMENT_RECEIPT.json](ATTACHMENT_RECEIPT.json)；附件proposed内容没有冒充正式登记。

[授权请求](AUTHORIZATION_REQUEST.json)已由 FullAuxiliaryService.register 正式写入原campaign，见 [REGISTRATION.json](REGISTRATION.json)。基线99，新增最多7200，仅此计划可用，累计最多7299，不再叠加旧401。旧500规则、8轮书签修复、旧grant与期限均不变，G1/T08未恢复。每叶子最多6次新增；每叶子最多一次协议追加，以及一轮内容修订/新独审；先保留所有未开始项与在途项的首轮预算。模型固定 opencode-go/minimax-m3.1-flash-free，未授权fallback。

本计划首次受控真实启动：2026-10-21T21:35:44.123177+08:00；30天绝对截止：2026-11-20T21:35:44.123177+08:00。不继承旧三叶子8小时窗口，恢复不重置。实际重复登记已核对同回执/同期限/同7200上限，见 [REGISTRATION_REPLAY.json](REGISTRATION_REPLAY.json)。

## 此检查点的实际数量

观察时间：2026-10-21T13:48:13.338514+00:00。这些是实际状态；固定批次清单不等于已处理。

| 指标 | 数量 |
|---|---:|
| 正式范围 | 1805 |
| 复用原可用模板 | 18 |
| 本计划真实启动过的叶子 | 2 |
| 新完成可用模板（ready_not_run） | 0 |
| 需要内容修订 | 0 |
| 已失败终态 | 0 |
| 已研究但无源 / unsupported | 0 / 0 |
| 正在处理 / 暂停 | 2 / 0 |
| 尚未开始 | 1785 |
| 本计划新增受控调用（失败和在途均计） | 5 |
| 实际历史累计调用 | 104 |
| 本计划剩余额度 | 7195 |
| 本轮新案例身份 / 新案例版本 | 0 / 0 |
| 本轮新应用运行 | 0 |

已取得真实日历研究回执并固定 elementary/calendar commit 14ee18015422bf195cd0df1cbab7170525166f9a，6份文件；原始响应、session/reservation、摘要见 [FIRST_STAGE_RECEIPT.json](FIRST_STAGE_RECEIPT.json)。支出来源复用旧 ExpenseOwl 固定源码，未重复无关研究。正在生成/独审不冒充可用模板。当前具体阶段与调用索引见 [CHECKPOINT_001.json](CHECKPOINT_001.json)。

## 持续任务与恢复

launchd标识 `gui/501/com.atlas.full-leaf-auxiliary-20261021`，启动实际协调PID 87586，命令及本机日志路径保存在 [START_RECEIPT.json](START_RECEIPT.json)、[PROCESS.json](PROCESS.json)。启动后真实阶段交付和再次launchctl查询已核对，不仅是创建plist或排队。一个协调者、每执行批20项、最多两个模型调用，完成后自动接续；只有全量首轮结束才处理内容修订队列。控制命令不会新建campaign/叶子身份。

机器需保持运行、联网，并维持本机Atlas API 127.0.0.1:5199；它当前健康。协调者由launchd管理，不依赖本次聊天常驻。休眠/关机不会执行模型；重启登录后可能需要start。若API关闭，按共享服务故障暂停，启动原API `python3 application-atlas-production-pack/drafts_api.py --port 5199` 后按操作文档恢复；不假称服务永远在线。

共享provider故障全计划最多两次短退避恢复，恢复仍走正常有偿预留/每叶子限制；持续失败后保留pending/paused，不扩散成大量产品失败。原始来源/JSON/失败谱系保留；不确定启动先对账，不盲目补调。低于5GiB可用盘暂停。本机启动前约22GiB可用；已结束项只压缩重复audit副本和移除可恢复展开副本，权威原始calls与冻结ZIP保留。

## 改造、验证与保护

- Scoped full授权真正接入原全局reserve，而不只是绕过阶段限制；模型、scope、identity、stage、每叶子/计划用量与并发都在事务内检查。旧严格任务不能借用新池。
- 来源分为Atlas需求、固定上游事实、目标设计推断，生成只认宿主给出的source IDs；研究使用短合法JSON/schema，错误字节不补引号、不截断拼接。新attempt保存旧失败、输入、profile谱系。旧生产/DeepSeek及旧三叶子重放保留。
- 不把所有叶子硬套Web CRUD；允许Web/桌面/CLI/库/服务等profile；标准包带原始认知、source-partitions和固定共享案例。独审有独立新会话、完整长文本视图及实际读取覆盖门禁。源码与设计验收依然阻断真实核心矛盾。
- 单独确认的来源事实先进入共享案例，模板失败仍可从应用实证复用；新版本沿同一案例身份追加固定版本，不改写旧模板依据。通过项才辅助导入并实际下载标准开发包，默认静态通过、应用未运行。
- 完整后端773项通过/跳过8；预算46项通过。原受限沙箱的19项端口权限失败另留原日志，允许本机端口后重跑通过，不冒充环境无失败。
- 工具回归41项通过，含20+20+1自动续批/失败隔离/并发2的调度fixture、跨500授权、原旧池不叠加、模型/来源分区、窗口/每叶子累计、协议原文保留/后继、不确定启动与已证明未启动的区别。fixture数量不计本轮真实叶子或模型调用。
- 生产宿主提交 b001b67562250e0f68c493b8b4d96e0044f17385 的 [CI 39608518041](https://github.com/liamamilin/atlas/actions/runs/39608518041) completed/success，check和docker-integration均通过，启动前已核对，见 [SOURCE_CI.json](SOURCE_CI.json)。新增的调度fixture与此启动检查点单独提交，实际生产宿主文件摘要与冻结值相同。
- 正式数据库已有SQLite一致备份，路径在本机原生产root/operator-evidence/full-leaf-auxiliary-2026-10-21/factory-before.sqlite。123个原冻结包及六应用数据库摘要仍相同，旧案例版本及严格授权历史不变，见 [PRESERVATION_CHECK.json](PRESERVATION_CHECK.json)、[HISTORY_PROTECTION.json](HISTORY_PROTECTION.json)。

Codex本轮负责宿主改造、对账/冻结、正式登记、真实启动和核对；研究、模板编写与新独立静态审阅由指定Go模型会话完成。原有应用和数据未被改造为本批样例；本轮不开发应用，不恢复严格G1/T08。

全量尚未完成。后续报告应按不同叶子的实际终态统计，不能把1787个pending计划行写成完成。原始阶段证据位于items/<leaf>/attempt-*/calls/；完成项另有audit-evidence.zip、固定源码upstream-evidence.zip和标准包，失败有FAILURE与后继谱系。按约100项或合适检查点聚合后续内容成果提交，不逐调用触发完整CI。
