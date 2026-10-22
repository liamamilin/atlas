# Open Design 三叶验证

本轮正式模型为 `open-design/deepseek-v4.1-flash`。同一全量计划保留原模型授权与全部调用来源；历史 MiniMax 检查点可零调用重放，新会话按当前模型计账。原窗口、7200 次新增上限、每叶子 6 次及并发 2 不变。严格 G1/T08 不恢复。

先按 PILOT_MANIFEST.json 固定的三个未开始叶子执行。限定范围与计划恢复在同一事务登记，预算预留也检查范围；启动参数丢失会继承持久化范围。单独 resume 不用于本轮。

```sh
python3 examples/assisted-trials/produce_all_leaves.py start --leaf e-book-library-application --leaf markdown-editor --leaf resource-calendar
python3 examples/assisted-trials/produce_all_leaves.py status
launchctl print gui/501/com.atlas.full-leaf-auxiliary-20261021
tail -f docs/template-factory/full-leaf-auxiliary-2026-10-21/runner.log
```

只有精确源码 CI 通过并追加 host revision 后才执行 start。start 复用同一 launchd；活动调用或协调器仍运行时不能改选。三项首轮完成后自动暂停，不自动打开其他叶子。失败保留原始返回与正式账本，原协议恢复和内容修订限额不增加。

阅读 PILOT_STARTED.json（若存在）中的实际启动证据；PREPARED 文件只是历史准备快照。最终成功率以独立审阅、冻结入库与下载验证结果统计，不能以会话启动或换模型推断改善。不同叶子的试跑用于 operational validation，不作为严格同输入模型 A/B。
