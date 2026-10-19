# V1 当前源码完整检查

本轮完整命令：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.v1_checks --output docs/template-factory/v1-2026-10-19/verification/final
```

真实执行的 argv、cwd、开始时间、耗时、退出码、测试数、skip 数与日志 SHA 均保存在 [final/checks.json](final/checks.json)。最终 `passed=true`、`source_changed_during_checks=false`。该摘要覆盖当前工厂、共享运行模块、测试、网页源文件/脚本/配置与 CI，不包含模型工作区/实时数据库。

| 检查 | 实际结果 |
| --- | --- |
| 后端完整发现 | 521 项；通过，8 项已知可选 Docker skip 如实保留 |
| 数据导出、网页数据生成与校验 | 通过；1805 叶子、270 分区、原33目录应用 |
| 前端类型检查、构建 | 通过 |
| 前端单元测试 | 9 项通过 |
| 默认浏览器测试 | 17 项通过 |
| 工厂浏览器专项 | 25 项通过 |
| 必需 Docker 门禁 | 20 项、0 skip，通过；8 项实际 Docker 路径、12 项 fixture/协议路径，不是20个真实生成应用 |
| Ruff、Python 依赖审计 | 通过 |
| npm 高危阈值审计 | 通过；2项 moderate 已记录，不自动应用破坏性降级 |

这些结果验证代码、协议和基础执行能力。门禁中的 synthetic/fixture 明确属于测试记录；它们不替代本轮真实 G1 生成应用、独立核心旅程与阶段证据。G1 未完成前不能据此开启 T08。

`pre-final-1/` 保留较早一次全部命令退出成功但执行中源码发生修复的记录；其 `passed=false`，不能作为最终源码门禁。最终使用 `final/`。

真实页面联调曾发现 rollback journal 下 API 与 scheduler 并发锁等待并中断。停止仅本任务进程后数据库 quick_check=ok；改为 WAL、复用 API 初始化实例、避免重复 DDL 写锁，并通过持有读快照的并发提交/多线程初始化回归。恢复通过正式预算服务释放已证明退出进程的活动占用，原消耗不退还；原证据在研究根目录 job 的 attempt-3/recovery-proof.json。修复后的16次真实并发API读取全部200，约0.001–0.026秒。完整检查包含该修复和回归。
