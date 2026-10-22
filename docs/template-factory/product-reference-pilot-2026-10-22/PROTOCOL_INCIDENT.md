# 真实试跑发现的研究元数据协议缺口

两个样本各完成一次 Open Design 研究会话。书签返回 24 条观察，投票返回 32 条观察；都在进入 author 之前被宿主拦截：`observation is not bound to a trusted upstream source`。

原因是研究提示使用 `kind` 占位符，但未给出宿主接受的枚举。模型使用 `readme/doc/license/source`，书签还使用了实际阅读工具中的 `source/upstream/` 路径前缀。原文、固定文件 SHA 和行号没有变化。这一结果不能算作模板生成或独审通过，也不能归结为模型缺乏研究内容。

局部修复只做可逆元数据适配：`readme/doc/license` → `documentation`，`source` → `code_observation`；路径已有固定相对形式则原样保留，否则只移除精确的 `source/upstream/` 前缀。文件必须仍在原 manifest 中，摘要、顺序、行号和观察文字不能改变；未知类型、越界范围和路径穿越仍拒绝。

原始 `research/RESULT.json` 和 CLI 返回保留；原失败记录存为 `OUTCOME.initial-protocol.json`，原汇总存为 `RESULTS.initial-protocol.json`。`PROTOCOL_ADAPTATION.json` 记录逐条转换、原字节摘要和派生结果摘要。新通过的认知包也将包含原研究和适配证明。提示摘要、场景、案例、输入及上游版本不变。

同一试跑通过正式 `align_host` 登记经 CI 验证的宿主修正，追加来源链；不改写原登记，不新建 campaign，不追加调用或重置时间。只允许已有终态 research、尚未启动 author/review 的这个检查点进行一次宿主衔接；后续从已有 research 的持久结果继续，不重做研究。业务内容修订不包含在这次格式恢复中。

此时实际用量为本试跑 2/6，原计划 176/7200 新增，历史累计 275；剩余四次用于两份样本各自的 author 和独立 review。全量继续暂停，严格 G1/T08 与应用运行状态不变。实际证据预检已通过，后续真实结果见最终报告，不以本说明代替生产完成。
