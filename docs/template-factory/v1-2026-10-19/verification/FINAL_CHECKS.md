# V1 当前源码完整检查

实际命令：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.v1_checks --output docs/template-factory/v1-2026-10-19/verification/final
```

当前完整执行结果 `passed=true`、`source_changed_during_checks=false`。精确 argv/cwd/env、开始时间、耗时、退出码、测试数与 skip、日志 SHA 和源码前后摘要均在 [final/checks.json](final/checks.json)。源码摘要包含工厂、共享运行模块、测试、网页源文件/脚本/配置和CI，排除实时数据库、模型工作区和报告。测试运行时以4ea4a59为HEAD且工作区有本次修复；后续提交不改已测源码时由相同源码摘要关联，不伪称先前Git commit已经包含这些改动。

| 检查 | 实际结果 |
| --- | --- |
| 后端完整发现 | 544项；536执行通过，8项已知可选Docker skip |
| 数据导出、网页数据生成与校验 | 通过；1805叶子、270分区、原33目录应用 |
| 前端类型检查、构建 | 通过 |
| 前端单元 | 9项通过 |
| 默认浏览器 | 17项通过 |
| 工厂浏览器 | 27项通过；包括计划深链恢复、逐目标运行状态及运行断言深链 |
| 必需Docker | 20项、0 skip；8项实际Docker路径，12项fixture/协议路径，不是20个真实生成应用 |
| Ruff、Python依赖审计 | 通过 |
| npm高危阈值审计 | 通过；2项moderate另存审计记录，不强制破坏性降级 |

这些结果证明代码、协议和基础执行能力。fixture/synthetic证据不替代本轮真实G1生成应用、独立核心旅程和阶段必要证据。G1未通过时不启动T08。

## 已修正并保留的失败

- `facts-fixture-failure/`：7个开发fixture错误，原因是模拟校验未返回真实case basis；改为真实fixture规范案例和审阅，不弱化生产校验。原日志530项、7errors、8skip；旧计数parser错误记录skip0，现已修复并回归。
- `pre-final-facts-view/`：1个认知说明文案断言失败，恢复“不等于工厂重新验收”的保守说明，原断言保留。
- `interrupted-publication-copy/`：操作者停止本任务专属重复checker进程组的部分记录，不作完成证据。
- `source-change-concurrent-browser/`：源码热更新与并行focused Playwright共用test-results，出现trace ENOENT及locator失败；不同端口不足以隔离输出。最终完整执行期间禁止其他浏览器测试并发，定点执行使用独立output。
- `pre-final-scope/`：所有命令成功但执行中修正manifest协议重试分支，source_changed=true，不能授权G1。
- 各归档的ARCHIVE/INTERRUPTED文件记录原日志位置映射；原检查记录和日志不倒改为成功。`pre-final-1/`保留更早的源码变更检测记录。

## 真实环境可靠性

本轮真实API与scheduler曾在rollback journal下发生锁等待/磁盘I/O中断。仅停止本任务进程后quick_check=ok；采用WAL、缓存API初始化、避免重复DDL，并补并发快照/初始化回归。恢复通过正式预算服务释放已证明退出的活动占用，原消耗不退还；attempt-3/recovery-proof.json保留原证明。修复后16次并发API读取全部200（约1–26ms）。

Docker28.3.2短名标签inspect曾假报NoSuchImage；镜像ID可读且实际无网络容器可运行。改为同一官方镜像完整引用 docker.io/library/python:3.12-slim 和 docker.io/library/node:22-bookworm-slim，不换版本、不放宽断言。当前20项严格门禁实际通过。
