# v0.1.2 的单点修复：浏览器认证头边界

人工静态检查在 acceptance/browser.cjs 的 withPage 中看到 browser.newContext({baseURL, extraHTTPHeaders: authHeaders})。全局 extraHTTPHeaders 会覆盖上下文全部页面请求；A28 需要点击外部夹具并打开新页面，不应把目标应用认证头发送到该外链。当前没有运行程序或提供凭据。这是生成的辅助程序的实际边界缺陷，不是要增加用户产品的认证功能。

只改这一问题，不继续扩大产品范围或修其他可选建议。保持同一场景、固定研究、25 feature、9 decision、33 case、三阶段及全部 ID/归属；用例仍 not_run，阶段仍 not implemented，不联网、不运行程序、不安装、不开发下游应用、不发布。

采用最小充分修复：HTTP 验收的显式 --auth-header 支持维持原状；本轮通用浏览器 driver 不支持任意认证头模式。有非空 ctx.authHeader 或 ctx._auth 时，在创建 browser/context/page 及发送任何请求之前抛出明确 infrastructure 错误 ATLAS_BROWSER_AUTH_UNSUPPORTED，错误文字不含凭据值，不能跳过后伪装 passed。没有认证头的专用测试实例仍走原有真实 Playwright 交互。删除 context 的全局 extraHTTPHeaders 配置。不要为此增加路由代理、伪造响应、跳过失败、静默忽略认证参数或开发复杂认证框架。通用受保护浏览器会话适配属未提供能力，明确记录即可。

修改 architecture_markdown 与 acceptance/README.md：--auth-header 仅用于 HTTP runner；--runner browser/all 遇到认证参数会明确报环境未完成。可以使用私有、专用、无真实个人数据的测试实例；不得建议公开部署无认证实例或关闭真实系统安全设置。不需要新 phase/feature/case，不改 HTTP case 或 UI case 的行为覆盖。

文件计划必须完整保留以下文件。只有 acceptance/browser.cjs 和 acceptance/README.md 两项可生成（reuse=false）；其他 18 项必须 reuse=true，逐字复用冻结包。不要改 helper 接口；如果有别的模块已调用 authHeadersFor，保留导出但让浏览器上下文初始化的前置拒绝保证不会发送请求。不要把本次扩成几十个程序重写。

- acceptance/common.cjs: reuse=true
- acceptance/support.cjs: reuse=true
- acceptance/browser.cjs: reuse=false
- acceptance/p0-save.cjs: reuse=true
- acceptance/p0-library.cjs: reuse=true
- acceptance/p0-limits.cjs: reuse=true
- acceptance/p0.cjs: reuse=true
- acceptance/p1-categories.cjs: reuse=true
- acceptance/p1-trash.cjs: reuse=true
- acceptance/p1-edit.cjs: reuse=true
- acceptance/p1.cjs: reuse=true
- acceptance/p2-search.cjs: reuse=true
- acceptance/p2-browse.cjs: reuse=true
- acceptance/p2.cjs: reuse=true
- acceptance/ui-p0.cjs: reuse=true
- acceptance/ui-p1.cjs: reuse=true
- acceptance/ui-p2.cjs: reuse=true
- acceptance/run.cjs: reuse=true
- acceptance/package.json: reuse=true
- acceptance/README.md: reuse=false

只在规范的架构段落说明本次边界；其他已正确内容保持。title 不要嵌入易过期的版本号，版本由 Atlas 所有。新候选完成后另开独立静态审阅，检查本项前置拒绝、无全局头、无凭据日志及既有契约/阶段一致性。
