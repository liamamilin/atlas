# 宿主独立代码审查（非模板模型独审）

审查发现并修复：

- 注册幂等回执临时标记不同导致检查点重放失败：仅固定稳定回执，重复登记不代表重新执行。
- 新author只输出reference但导入要求旧observations：来源来自宿主研究，保留可选旧字段严格兼容。
- 导入冻结输入摘要误比author封装：按原登记inputs重新校验。
- 官方研究检查点所在位置：由generation的同级official-checkpoints读取、核验并复制，保持原reservation/session。
- needs_changes未带回语义意见、图合法候选拒绝后继：校验原独审身份和读取证明，传回原意见，不重复假扮协议失败。
- 前驱凭路径后缀不足：精确绑定原sample/r2路径、BINDING/DELIVERED/RESULT、CLI摘要和原DB reservation。
- machine contract required集合次序不稳定：排序并以多个PYTHONHASHSEED子进程回归。
- 结构化审阅意见无法回传：不改原意见，规范序列化进入修订上下文。
- 切片错误被其他字段错误遮挡：独立汇总覆盖，不修改候选取得通过。

最终只读复核未发现未处理阻断；真实r2前驱对照两份原保存数据及原账本通过。其结论是源码审查，不是后续生成内容的独立pass。实际模型审阅、包摘要、入库和下载仍需运行证据。
