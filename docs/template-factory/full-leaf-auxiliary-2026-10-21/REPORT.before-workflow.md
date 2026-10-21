# 全量辅助计划：已实际持续运行，尚未全量完成

观察时间：2026-10-21T14:45:21.335535+00:00。当前正式计划 `full-leaf-auxiliary-2026-10-21` 在原 campaign 中运行。实时状态见 [PROGRESS.json](PROGRESS.json)、[逐叶子结果](RESULTS.json)及[调用账本](CALL_LEDGER.json)；本报告是检查点，不把排队或模型生成中计为完成。

## 范围、预算与实际数量

[冻结范围](FROZEN_SCOPE.json)：1805个有效叶子，18个已覆盖且开发包可下载，1787个待生产，排除0。撤回旧版本保留，不能算额外覆盖。支出跟踪、日历优先，后续按冻结目录顺序。原附件ZIP、授权原文与摘要已保存，见 [ATTACHMENT_RECEIPT.json](ATTACHMENT_RECEIPT.json)。附件proposed状态没有冒充正式授权。

[正式登记](REGISTRATION.json)的历史起点99，新增7200只供这个固定计划；累计最多7299，不叠加旧401。固定 `opencode-go/minimax-m3.1-flash-free`，并发最多2，每叶子新增最多6，合计最多一次协议恢复及一次内容修订＋新独审。优先保障全部首轮，再处理内容修订队列。旧500规则及严格G1/T08授权没有扩大。

首次真实调用：北京时间2026-10-21 21:35:44.123177；30天绝对截止2026-11-20 21:35:44.123177。恢复没有重置。本轮scope、prompt/profile和叶子输入固定；宿主纠错通过追加的源码修订服务登记，原scope文件不重写。

| 指标 | 数量 |
|---|---:|
| 正式叶子总数 / 原可用复用 | 1805 / 18 |
| 本轮真实尝试过的叶子 | 3 |
| 新增可用辅助模板 ready_not_run | 1 |
| 正在执行 / 暂停 | 2 / 0 |
| 未开始 | 1784 |
| failed / needs_revision / source_unavailable / unsupported | 0 / 0 / 0 / 0 |
| 本计划新增调用（含失败、在途） | 9 |
| 历史累计 / 本计划剩余 | 108 / 7191 |
| 活动调用 | 2 |
| 新案例身份 / 新案例固定版本 | 1 / 2 |
| 本轮真实应用运行 | 0 |

辅助目录现在20条：19份可用，1份待修订历史；六份既有核心运行示例保留，其余14份应用未运行。新增日历为静态独审通过，不是运行通过或严格发布。完整状态快照：[CHECKPOINT_002.json](CHECKPOINT_002.json)。费用、provider内部请求数与未观测的返回模型身份均为unknown；free名称不等于费用核验。

## 第一份完整链路成果与恢复证据

[日历模板入口](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_bbc868df7d214cd4844df7f8fc42554d)，[标准开发包](items/calendar-application/attempt-1/atlas-development-package.zip)。场景是单用户桌面月视图日程管理，非通用管理后台。案例固定 `elementary/calendar@14ee18015422bf195cd0df1cbab7170525166f9a`；同一共享案例r1保留被接受来源观察，r2关联正式场景和模板，新增案例身份1。上游源码运行、下游应用运行均not_run。

日历实际消费4次CLI：研究、生成、首独审（JSON协议失败）、唯一协议恢复独审（有效通过）。原始坏JSON和失败记录保留，没有补引号或拿旧pass替代。恢复导入复用了完整生成与审阅检查点，新增CLI为0。标准包实际HTTP下载并核验SHA、共享案例r2摘要、8份开始文件和20份blueprint文件；从 `HANDOFF.md` 开始，当前阶段在 `CURRENT_PHASE.json`。重复生产返回相同制品，新增调用0、案例版本0，见 [CALENDAR_DELIVERY_VALIDATION.json](CALENDAR_DELIVERY_VALIDATION.json)。初次人工核包使用过旧文件名的检查另存，不修改交付包掩盖差异。

真实启动暴露的宿主缺陷已修复并正式追溯：

- macOS大小写不敏感导致 `SCENARIO.json` 与正式 `scenario.json` 冲突；保留旧字节及迁移回执，研究场景改用 `SELECTED_SCENARIO.json`。同时从场景服务读取规范记录，避免列表附带审阅字段改变冻结输入。
- 完整计划元数据没有旧导出器必填的调用聚合字段；从真实reservation回执派生计数，保留无回执的中断输出为 `packages.incomplete-N` 后重新导出。
- 暂停发生在写启动意图后、正式预算预留前的两个检查点：正式服务核对同任务预算无已启动/不确定预留且无进程/输出证据，追加 `NOT_STARTED_PROOF.json`，保留原意图，在后继目录正常受控调用。任何可能已启动的调用仍拒绝免费恢复。

这些是宿主纠错，不是额外模板内容修订；原始失败、输入、模型结果、授权、计数、时间全部保留。[第一次宿主修订](HOST_REVISION_RECEIPT.json)、[第二次宿主修订](HOST_REVISION_2_RECEIPT.json)。支出跟踪与即时通讯仍在真实生产；其旧失败不是当前最终结果，不能把在途算通过。

## 持久运行和操作

真实launchd任务 `gui/501/com.atlas.full-leaf-auxiliary-20261021`，本次协调PID 8077，当前state=running，核对见 [SUPERVISOR_CHECK_002.json](SUPERVISOR_CHECK_002.json)。每批20项，两个有依赖顺序的worker，单叶子失败记录后继续。每30秒更新实时状态，阶段完成保存检查点；每批自动接续。命令见 [OPERATIONS.md](OPERATIONS.md)：

```sh
python3 examples/assisted-trials/produce_all_leaves.py status
python3 examples/assisted-trials/produce_all_leaves.py pause
python3 examples/assisted-trials/produce_all_leaves.py resume
python3 examples/assisted-trials/produce_all_leaves.py start
```

协调任务脱离聊天与终端运行；机器需保持运行、联网，并维持Atlas API `http://127.0.0.1:5199`。休眠/关机不会生产，重启登录可能需start。API不是本次新建的常驻系统服务；若停止，按OPERATIONS启动原API后恢复。原30天时钟持续。共享服务故障有限退避、持续故障暂停；低于5GiB暂停。只压缩结束项的重复audit/材料副本，原始调用与固定ZIP不删除。

已登记本聊天的每小时跟进任务 `atlas`：检查实际状态，状态无变化时保持安静；仅在必要修复、有效进展或停止时行动/报告，约100项聚合提交证据。它不创建新计划、不重置预算、不重复领取模型调用。日志为本目录runner.log/runner.stderr.log；不能以历史启动回执冒充进程此刻在线。

## 验证、CI与历史保护

完整后端773项通过（8项跳过），预算专项46项通过。早先受限沙箱端口失败另存，允许本机端口后重跑通过。最新相关宿主回归45项通过，Ruff通过；fixture只证明宿主逻辑，不计真实模板/应用。schema、来源分区、合法JSON、完整阅读覆盖、独立会话、包/摘要和下载门禁逐项检查，生成验收代码不在宿主执行。

精确生产宿主源码：`cfeb8705db6596825927c8af48b09aa002551a36`，[CI 39617893359](https://github.com/liamamilin/atlas/actions/runs/39617893359) completed/success，check与docker-integration通过，证明见 [SOURCE_CI_RECOVERY_2.json](SOURCE_CI_RECOVERY_2.json)。前序 b001b675/cb10e49 的CI和登记也保留。源码纠错与本次生产成果分别提交。

原18份标准包再次实际下载，摘要相同；撤回候选开发包仍409；原123个包/六应用数据文件未改变，原19份案例版本不变。原修复、重试、grant、窗口、500限制都保持，见 [CATALOG_VALIDATION.json](CATALOG_VALIDATION.json)、[PRESERVATION_CHECK.json](PRESERVATION_CHECK.json)、[HISTORY_PROTECTION.json](HISTORY_PROTECTION.json)。严格G1/T08仍保持历史未通过/未运行状态。

Codex承担宿主、对账、服务集成与证据核对；研究、内容编写和新独立审阅由指定Go模型真实会话完成。未完成的1787项生产目标不写成全量完成。最终只有无pending/running/paused且每项均有真实终态，才报告处理完成；覆盖率仅按不同叶子的reused+ready_not_run计算。
