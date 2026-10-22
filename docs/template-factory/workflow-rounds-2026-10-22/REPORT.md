# 分轮流水线验证与全量首轮

用户批准先跑通现有流水线，再全量执行首轮，单叶失败记录后继续，整轮结束集中分析第二轮。本轮沿用原1805叶子、原campaign与7200新增调用授权、每叶六次、并发二及原30天绝对截止；模型为 `open-design/deepseek-v4.1-flash`。不恢复严格G1/T08，不开发应用。

## 三叶真实结果

| 叶子 | 本轮结果 | 入口 |
|---|---|---|
| Markdown编辑器 | 独立静态审阅通过，八步完成，真实开发包下载及零调用重放通过；应用未运行 | [模板](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_082f2b3dc06847beb29654649ba43591) |
| 资源日历 | 独立静态审阅通过，八步完成，真实开发包下载及零调用重放通过；应用未运行 | [模板](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_e69bb928d000493a81a21ea19c4fa147) |
| 电子书库 | 集中修订后独审仍needs_changes：状态/顺序、来源、修订断言、删除错误码、MOBI路径及README调用仍有合同不一致；保留候选，不入可用目录 | 原工作目录 `items/e-book-library-application/attempt-2` |

原研究复用，新研究调用0；三叶各增加一次内容修订和一次独立审阅，共6次。计划新增127→133，历史累计226→232，结束时活动0。每叶累计5次，第六次仅限原协议恢复规则，不赋予第二次业务修订。原127次记录逐项未变，123个原保护文件（含六应用数据）及19个历史案例版本未变，18旧包重载后实际下载摘要匹配。

证据：[真实终态与八步/下载/零调用重放](PILOT_ROUND_RESULTS.json)、[阅读和包检查](FRESH_PIPELINE_VERIFIED.json)、[案例历史保护](PILOT_CASE_HISTORY_PRESERVED.json)。通过检查点复用、修订、全新独审、冻结、入库与实际下载均有本轮真实证据。此小样本2/3通过不代表全目录质量或严格同输入A/B结论。

## 全量首轮与一次宿主兼容故障

`FULL_ROUND_REQUEST.json`已正式绑定原1805全范围、原授权、当前模型及本轮新验证报告摘要。每批20、并发2，只执行剩余首轮；预算事务拒绝repair lane。已处理/复用结果保留，单项问题保留叶子、步骤、码、原因、工作目录和证据；首轮结束自动暂停并写`ROUND_REPORT.json`及时间戳副本。第二轮待集中分析。

首次全量start在未新增调用时暂停：matchmaking的旧MiniMax未真正启动intent，被宿主按当前OpenDesign模型拒绝；relationship只受到同一全局暂停连带影响。未删旧intent或伪造通过。[原始故障](UNLAUNCHED_MODEL_INCIDENT.json)、[恢复前正式账本核验](UNLAUNCHED_RECOVERY_BEFORE.json)保留。

修复限定为：依据正式模型修订链接受合法历史binding；冻结scope父目录仍是计划根；有任何启动痕迹或预留状态不明继续拒绝；旧summary保留旧模型，新后继才使用当前模型。双worker全局故障通过同一写事务保留首个暂停原因。104项辅助工厂、46项预算回归、ruff和独立代码复核通过；fixture未冒充真实模板或应用运行。新源码`fa630f882334669b3b999ffcd98bead00c9e75b5`及精确CI/正式host/真实恢复结果分别保存，不用旧CI替代。

当前运行状态以`FULL_RESUMED_STARTED.json`（若存在）与正式status为准，旧start回执仅是历史。后台无需聊天或人工逐叶盯守；本机休眠、关机、离线会停止进展。低频跟进只在整轮终态或全局安全停止时分析通知，不因普通失败或低通过率中断。

[进度页](http://127.0.0.1:5188/factory?view=workflow)。查询与恢复说明见[OPERATIONS](OPERATIONS.md)。原严格G1/T08、旧失败、预算与grant均保持真实状态。

## 实际恢复检查点

源码 `fa630f882334669b3b999ffcd98bead00c9e75b5` 的 [CI 39709062560](https://github.com/liamamilin/atlas/actions/runs/39709062560) 已completed/success，check与docker-integration全部通过。已通过正式服务追加宿主版本；API原根重载健康、18旧包实际下载摘要及ZIP类型均通过。

[真实全量启动快照](FULL_RESUMED_STARTED.json)：同一launchd PID60542，原1805范围、full_first_round，计划新增135 / 历史累计234，活动2，两个新会话均为Open Design DeepSeek。旧MiniMax BINDING/input/LAUNCH_INTENT原字节未变，正式无启动证明保留原模型；新协议后继只有一条受控收费预留，并有process和tool_use/step_finish事件，未新建campaign或重复领资格。

启动时：已处理63（18复用、5新增可用、15待修订、16失败、9无源），执行中2、未开始1740、unsupported0、暂停0；已实际尝试46个叶子。可用覆盖23个不同叶子，不代表全量完成。辅助目录还有历史撤回条目，不能计作可用覆盖。数字是启动快照，以后台正式状态更新为准。

已将跟进降为每6小时的轻量全局核对；普通单叶失败不通知，不逐项补调/改内容。首轮自动暂停生成完整逐叶报告后再分析第二轮；明确的全局安全停止仍保留并报告。修复源码与已结束三叶及启动证据分别提交，保留未知dashboard和在途原始调用目录。
