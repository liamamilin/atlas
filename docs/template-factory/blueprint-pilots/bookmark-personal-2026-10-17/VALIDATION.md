# 首个认知模板下游试用记录

2026-10-17。样板 0.1.1 的修订与首阶段试用完成，未发布，也未修改旧模板或既有场景。

- [包内验证说明](../../blueprints/bookmark-personal/VALIDATION.md)区分审阅、结构、工具、参考模块和真实应用证据。
- [实际 P0 验收](p0-acceptance.json)：10/10 通过；[负向对照](negative-control.json)：取消提交后 A01 如预期失败。
- [首次审阅](review-1.json)、[修订复审](review-2.json)、[最后两项闭合](review-3.json)保留所有问题和结论；最后一轮只复查 A05/A06。
- [P0 试用代码](p0-trial/README.md)与[截图](p0-trial.png)；[输入快照](input-snapshots.json)及[CLI 会话/报告用量](provider-calls.json)。
- run_pilot.py 复用已有 OpenCode CLI 只读适配器；同一已授权 model；独立会话，未开启搜索。再次运行会调用 provider 并可能计费，不应把它当作纯本地测试。
- 开发会话读取 0.1.0，未修订应用源码；最终使用 0.1.1 的补强用例验收。没有进行新旧提示 A/B 对照。
- P1/P2 未实现，通用认知工厂未接入。试用代码独立保存，不混入认知模板默认源码。

## 复现 P0

在 p0-trial 目录使用本地静态 HTTP 服务（README 给出命令），再运行认知包 acceptance/run.cjs --phase P0。浏览器使用新临时数据；复查不需要再次调用模型。查看 result.json 获取摘要及制品 SHA256。
