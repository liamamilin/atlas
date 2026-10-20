# OpenCode Go 单次连通性测试

用户明确授权独立的1次测试，不恢复G1。2026-10-20北京时间18:31:54启动，18:32:04完成。

- 指定模型：`opencode-go/deepseek-v4.1-flash`。
- 提示仅要求返回OK；隔离临时工作区，全部工具权限拒绝，不附带项目资料。
- 实际CLI启动1次，耗时10.695秒，退出码0；原始text事件为`OK`，stderr为空。此响应证明本次请求成功，不保证后续生产额度或大任务可用。
- 原始事件未单独给出实际后端模型或token用量，不据此推断。
- 此诊断依据新增的独立授权单独记账，不领取、不恢复、不修改原G1 grant。工厂原累计CLI仍81/500；另记本次诊断1次，两者合计已观察CLI启动82次，诊断不是工厂恢复调用。
- 原冻结job仍attempt2/needs_review，父子批次仍paused；现场只读状态见production-state-after.json。G1仍未通过。

原始响应见stdout.jsonl，启动前持久意图和结果见diagnostic.json。
