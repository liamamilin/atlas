# 固定规范的两处 CommonJS 接口修复

同一已授权书签认知生产/必要修复/独立审阅。基于冻结 v0.1.10，reuse_spec=true，只改 acceptance/ui-p1.cjs 与 acceptance/browser.cjs，其余18文件字节复用；规范、调研、所有身份、阶段、默认值及断言保持。不研究、不安装、不执行生成程序、应用、浏览器或重启适配器，不发布，状态仍not_run。

独立审阅与主机只读 TypeScript AST 检查均确认以下两个静态接口缺陷；没有运行生成模块。18个CJS的直接本地 CommonJS 导入/导出检查无不支持接口，发现项只有这两类（第二类被多个调用点引用）。

1. ui-p1.cjs 的 require('./support.cjs') 解构 uniqueName，但 support.cjs 不导出它；common.cjs 已实际导出 uniqueName。把 uniqueName 从 support 解构列表移动到 common 解构列表。不要更名/重写函数，不改变调用或其它导入。
2. browser.cjs 已有完整实现 `async function waitForRowWithCategory(page, title, categoryId)`，且 ui-p1.cjs 的所有调用确实使用 title/categoryId，参数相容；但 module.exports 的对象没有它。只在 module.exports 的 waitForRow/waitForRowById 相邻位置增加 waitForRowWithCategory。函数实现、导出中其它成员全部保留。

使用唯一原文片段精确替换，预期只是导入位置和一个导出字段的变化。严禁重写 helper、删除/弱化断言、修改 browser.withPage 的认证拒绝/安全约束，或顺手修可选建议。保持已补三处 await、真实排序/分页/归类点击、生命周期及安全用例。先读真实模块的导出，不根据名称猜接口。

冻结后用主机只读 AST、node --check 和规范/字节差异检查复核，另做完整独立静态审阅。编译/接口检查不等于应用运行通过；未知的动态接口或未执行项要保留，不伪造证据。原审阅的可选建议和待澄清项保留，不升级为新功能或额外发布门槛。
