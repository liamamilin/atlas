# 自动书签认知包 v0.1.7：本轮结果

2026-10-18。仍使用已授权 `open-design/deepseek-v4.1-flash`，没有新调研、生成下游应用、安装依赖或执行模板程序，也没有发布。

## 已完成

- v0.1.6 的产品完整性已通过独立静态审阅；本轮补清归类引用错误、写表单 method/成功跳转、单条永久删除/清空确认，以及 P0 默认归类选择器的契约。
- 模型局部修订与主机复算完全相等；角色、功能、阶段、限制、标题及所有行 ID 保留，见[规范完整性](revision-10-spec-integrity.json)、[原始补丁](revision-10-model-patch.json)、[修订摘要](revision-10-spec-revision.json)。改动仅涉及架构、D07.default 和 A03/A09/A17/A20.goal，不是整份蓝图重写。
- [五项独立规范预审](revision-10-design-review.json)全部通过，随后完成两个指定程序，冻结 v0.1.7：`tpl_91c8e24a75214faeab0ee5a832310bfa`，摘要 `b1133bdf2be47d9aa23bf5d91c1f3f7e1264f25c858e4457c239da370e555301`。
- [冻结与字节核对](revision-10-frozen-integrity.json)通过：仅 p0-limits.cjs、p1-edit.cjs 改变，其余 18 个验收文件字节相同。两文件增加真实表单编码、错误 Host/Origin/Fetch Metadata 负例、请求后数据/计数读回检查；永久删除/清空探针不携带 confirm=true。

## 完整审阅及人工核对

[第八份原始完整报告](review-8.json)七项通过，阶段验收阻断。原报告与原始事件保持，不覆盖模型结论。分项核对如下：

| 发现 | 核对与处理 |
| --- | --- |
| 回收站记录不参与重复判断缺少实际重存负例 | 成立；A06 验证活跃重复，A16/A18 未重新 POST 已软删除的同 URL。需在既有 P1 用例补 201 新 id、旧回收项保留及随后 409 指向新活跃项。 |
| 同一归类混有活跃/已回收项的删除未验证 | 成立；A14 的 priorGroup 与 groupPurge 是不同归类，只证明跨归类既有回收项保留。需分别补独立 move/purge 混合夹具及来源/计数守恒。 |
| `/bookmarks/bookmarks/...` 是子路径重复错误 | 不成立；前一段是部署前缀，后一段是架构明确的业务路由。common.resolveTarget 按 ctx.baseUrl + path 拼接，恰符合所有业务路由带前缀的契约；照建议改成 /{id}/move 反而丢掉业务命名空间。[纯主机路径核对](revision-10-route-diagnostic.json)没有执行模板或发请求。保留正确代码，在 README 加示例。 |
| A17 的非数字 ghostId 强制 unknown_or_deleted | 人工另发现的确定分歧：规范将该 reason 限定为形状合法的失效引用，A17 用 ghost- 前缀。应改十进制失效引用，非法形状如保留只断言 invalid_category/400。A03/A20 已有十进制夹具，不需改。 |

后续按 [REPAIR_11_NOTES.md](REPAIR_11_NOTES.md) 固定全部规范与原研究，只修改 p1-trash.cjs、p1-categories.cjs 和验收 README，不重做规划/规范预审。完整报告中的其它 UI/覆盖建议保持可选，不升级成新门槛。原始 v0.1.7 仍为 L0/draft、未发布，运行成绩为空；后续版本结果单独登记。
