# 固定规范的单文件确定缺陷修复：等待异步 DOM 断言

同一已授权书签认知生产/必要修复/独立审阅。基于冻结 v0.1.9，reuse_spec=true；所有规范、调研、角色/能力/决策/阶段/案例身份原值不变，只修改 acceptance/ui-p2.cjs，其余19文件字节复用。不研究、不安装、不执行生成程序、浏览器、应用或重启适配器，不发布，所有用例仍not_run。

人工静态核对确认：ui-p2.cjs 第188行 `async function assertRowsBelongToCategory(...)` 内含真实 Playwright await，但第582、624、642行的三个调用是裸表达式，没有 await。可能导致断言未完成就继续/关闭浏览器，或未处理的拒绝。此结论来自源码，不是已发生运行失败；原版本与报告保持，不能修改冻结文件。

只在这三个调用之前加 await：

1. `assertRowsBelongToCategory(page, targetId, targetName, ids, label);`
2. `assertRowsBelongToCategory(page, targetId, targetName, afterReloadIds, 'A33 刷新后 offset=' + lastOffset);`
3. `assertRowsBelongToCategory(page, targetId, targetName, ids, 'A33 page-prev offset=' + offset);`

它们所在函数/回调已经是 async，先读实际源码确认，再给三个唯一原文片段的精确替换。保持函数定义、顺序、所有断言/接口/夹具/真实 sort-form 操作与有序分页比较，不得改为 catch-ignore、void、Promise.resolve 或删除调用。不要顺手重构其它函数或追逐任何可选建议。预期只有三行前缀变化，字节与字段保护由主机核对。

冻结后独立完整静态审阅；主机只做 node --check 和源码差异检查，不声称应用或验收运行通过。
