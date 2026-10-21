# 两项收尾

核对CI39547271157：339dff4的docker-integration通过，check在npm audit失败；后续前端组合检查和工厂E2E确实skipped，未声称执行通过。

按官方GHSA-587h-7wmj-h5pm升级Vite7.3.6→7.3.7，同一主版本，package.json与lock一并更新，high阈值不变。修复后0high/0critical，仍有2项moderate（typography/postcss-selector-parser），未强制降级或忽略告警。

本地实际执行：类型检查通过；前端单元9项通过；生产构建通过；普通E2E17项通过；工厂E2E27项通过。普通E2E原端口与正在运行的Atlas冲突，因此只参数化测试端口（默认保留CI原端口），使用5218/5219和隔离测试库。首次并行普通/工厂测试清理了同一Playwright产物目录，原失败日志保留；工厂结束后顺序重跑普通套件通过。没有连接或清理生产数据。

export_trial现将acceptance/每个文件的相对路径和原始内容SHA纳入新导出来源，并在reuse时比较。新增/删除/改名/改内容都要求新版本或输出。旧收据未记录该清单时，从原已校验freeze中读取验收字节（去除宿主生成的plan.json）；不改历史收据或冻结包。4项回归通过，包括真实旧预算包兼容复用与改变后拒绝、旧ZIP不变。

新批次继续复用原有入口；本次收尾不建设额外恢复或调度平台。准确审计JSON和测试日志在本目录。
