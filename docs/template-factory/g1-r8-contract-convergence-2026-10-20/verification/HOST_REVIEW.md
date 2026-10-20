# 本轮宿主独立代码审查

Sol reviewer 只读审查 frozen_revision、v4 resume/queue、v5 登记/激活/时间解析、输入材料及预算上下文。最终未发现有充分证据支持的新 correctness finding。审查不执行模型、不代表真实 G1。

审查确认授权/准备摘要、4 replace/5 reuse、零模板 author 路径、相关预审与聚合实际文件、Go/1800配置、旧结论保留、激活/计修复/唯一后继/回执同事务、external1累计和T08时间隔离。条件性发现的旧 CI archive 目录限制由 root 修为模板工厂内规范 JSON 路径，保留精确HEAD/tree/原始CI摘要/两项成功job验证；现有测试涵盖两旧目录及R8目录，并拒绝目录越界/路径归一化绕过/非JSON。

程序审查曾发现 A13 解析器会接收目标行之外的链接，以及修复过程中的布局深度假设；两个问题均已修复并经独立复核关闭。最终程序fixture 13项通过，包含正反例。reviewer明确没有运行真实P0，也未把合成fixture当网络隔离证据。

按审查建议补齐真实 PreparedRevisionService→BudgetAmendmentService→ProductRecoveryService/queue_repair 联合fixture（只有外部CI边界替身），覆盖回滚、唯一计修复/后继、基线漂移、并发相同重放及冲突拒绝；六项projection与render检查真实程序哈希和单标题。最终完整门禁结果以 verification/verified/checks.json及日志为准。

完整回归中的测试隔离修复：初次759项暴露程序fixture importlib在归档source写入common.pyc，已改为内存compile/exec并恢复sys.modules，增加不写证据目录的回归。复跑另暴露两条历史时间fixture先触发真实Pipeline的lease_lost；只把临时数据库中的测试lease设置为实际与模拟时钟两者都有效，未改变生产lease/预算顺序或门禁。初次失败与修复后定点输出保留在initial-failed/及bytecode-isolation-fixed.txt。
