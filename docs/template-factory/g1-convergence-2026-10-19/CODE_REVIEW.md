# 收敛实现独立代码审查

审查角色：Sol reviewer，独立上下文、只读当前 diff 和原始续作指令；未调用生产模型、未改业务记录。以下为代码缺陷及处置索引，不能替代模板独立审阅或真实 P0 验收。

| 发现 | 风险 | 处置/待验证 |
|---|---|---|
| 程序范围门禁误比较整个 source 树 | 宿主更新 PRODUCT/template/派生 inputs 也被拒，合法聚合修订不能冻结 | 程序范围单独检查，增加真实 render/produce 回归 |
| 应用修复记账缺 plan_id | 原书签合法追加额度不能被应用路径消费 | 所有实际调用链补 plan_id，其他计划不继承例外 |
| resume-product 可省略 repair_scope | 从受限恢复入口绕过作者字段及程序路径限制 | 强制本轮 scope/general repair/五文件范围；拒绝旧 spec-only/reuse 模式 |
| 已激活窗口到期仍可恢复 | 在过期后收费、终结旧任务并入队 | 同一事务内检查激活后的有效 deadline；失败完整回滚 |
| 同产品的其他候选/任务可代替固定对象 | 附件授权的原始证据链发生漂移 | 首次恢复固定原 job/artifact/digest，并交叉核对旧任务 baseline |
| 文件路径检查不能判断允许文件中的断言削弱 | assert→pass 可在冻结后才被语义审阅发现 | 添加预冻结独立精确差分语义审查，必须 passed，保留原始报告；冻结后审阅仍独立执行 |
| 浏览器搜索对照不含同关键词跨分类记录 | 忽略 category、仅按 q 也可能通过 | 跨分类对照含同 token；纯关键词包含、组合与真实 UI 排除，并加 query-only 负控 |
| 宿主时间戳进入语义检查点摘要 | 同输入重启重复审阅，不同合法修订被误算同操作重试 | 稳定语义摘要只绑定作者字段/程序/适配/scope；操作绑定内容摘要、retry scope保持原计数 |
| blocked/uncertain 在保存检查点之前抛错 | 普通重试可能换出新的审阅结论 | 结构有效否决先保存，之后通过门禁；重启复用否决不重调模型；uncertain finding也拒绝 |
| 旧数据库没有 amendment 表 | 首次直接正式登记可能 OperationalError | 服务执行幂等schema初始化；真实旧schema回归保留42/2通过 |
| diff_digest 计算晚于写入候选 inputs | 冻结文件为null而provenance/审阅identity为真摘要 | 第一遍完整检查期间发现；已提前计算后持久化，真实produce回归验证冻结文件/provenance/语义identity三方相等且非空；final-2重新全检 |

根级集成另修两处测试环境问题：旧事实视图测试的 agent stub 接收新增预算上下文参数，原拒绝已撤回证据断言保留；恢复测试从已提交的完整冻结样例读取，避免依赖本机被忽略的生产目录。相关38项回归通过，实际样例 `verify_frozen` 摘要8d9229…通过。第一遍失败记录保留，不覆盖。

另已核查：新 case-adaptation-aggregate-v1 是正式新输入和检查点，包含 Python/SQLite/SSR 与 URL 政策；原案例事实不改。规范与程序差分检查时点在生成完成后、冻结前。独立运行器读取宿主固定摘要的正式预算响应并核对 job/plan/product/segment，分界检查绝对有效截止时间。

最终 focused/full CI 与真实生产状态另见本目录后续证据；未执行的真实模型、应用、phase proof 均不在此标记通过。
