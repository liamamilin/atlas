# 停止后的诊断与恢复边界

当前正式停止点：同冻结job attempt2，provider HTTP429 quota，未生成真实报告。计划及父/子批次已暂停，活动调用0，G1 blocked，T08未开始。

本次资格已实际启动并消费1/1。provider拒绝在产生内容之前发生，也不能把CLI资格退还。没有有效result/report，不能使用host-only续交。原register/recover请求的相同重放只会返回历史回执，不会产生新机会。

## 可执行的只读核对

在本仓库 `application-atlas-production-pack` 目录执行：

```sh
python3 -m template_factory.batch_cli   --root '/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/atlas/template-factory'   --pack '/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack'   status plan_87059846caf345d2b2fe690657cf324f

curl --fail --silent --show-error   http://127.0.0.1:5199/api/factory/v1/budget/evidence-grants/egrant_c06325f363b84bd9bb1c8fa46f93f945
```

预期：原job attempt2/needs_review，parent及child paused；CLI81/500，修复7/7，grant consumed，reservation failed，call_attempt2。原空checkpoint集合不需要人为补齐；本轮冻结独审没有phase checkpoint合并流程。

## 继续真实生产需要的条件

1. 先在provider侧核实额度恢复。此次错误只给出“5 hour”窗口名称，没有reset时间；不能据此编造可重启时刻，也不以新模型调用探测是否恢复。
2. 当前授权已经耗尽。只有另一次明确授权并通过正式机制后才可能新增调用资格；不得复用本grant、普通retry、新job/campaign或更换provider绕过。此文档不是新增授权，也不发起追加请求。
3. 绝对截止仍为北京时间2026-10-20 19:21:52.855422。本轮完整调用的启动边界为18:36:52.855422；不改系统时钟、不自动延长窗口。
4. 若后续获得新的明确授权，仍先读取同campaign/plan/product/job、81/500历史、7/7修复、已消费旧资格及冻结身份，绑定实际新授权和精确通过CI的宿主源码，以正式服务追加恢复；不覆盖本轮证据。
5. 只有真实独审八维有效通过才继续原发布→标准交接实际消费→首次真实P0→冻结套件与独立运行→phase proof→宿主G1；G1正式通过后才运行原三个T08样本。

冻结交付的已知限制（含README A11表格遗漏等）保持原字节。没有新独审内容结论；不得把本次额度错误解读为内容通过或内容不通过。
