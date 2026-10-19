# V1 操作与恢复

本轮正式业务根目录沿用 `application-atlas-production-pack/atlas/template-factory/`，请保留整个目录；不能仅拷贝 factory.sqlite 丢弃源码快照、制品、会话、应用提交与证据。SQLite 使用 WAL；进程运行时备份应使用 SQLite backup API 或既有备份服务，不直接复制单个数据库文件。

## 查看与控制当前 G1

以下入口的 --help、实际预览、执行、状态和报告均已在本轮使用，使用同一 BatchService：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli status plan_87059846caf345d2b2fe690657cf324f
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli report plan_87059846caf345d2b2fe690657cf324f
```

需要暂停/恢复/取消时，把 `status` 换为 `pause` / `resume` / `cancel`。暂停不延长截止时间；cancel不可恢复为running，已生成历史仍保留。子批次随计划原子变更，领取再次核对父状态。失败重试通过 `POST /api/factory/jobs/{id}/retry`；它恢复原 job 的 checkpoint，不清空预算。前端 V1 页给出相应按钮和报告。

预算停止时先读 report 中的 budget 和失败码，不手改计数、不新建campaign绕过原额度。若为截止时间/累计调用/修复/瞬时重试耗尽，当前轮次保留 paused_budget，后续扩大范围需要明确的新决策。unknown调用不能视为未启动返还。

## G1 门禁与首批

完整本地检查使用：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.v1_checks --output docs/template-factory/v1-2026-10-19/verification/final
```

需要已安装 requirements、ruff、pip-audit、网页npm依赖与Playwright Chromium，以及 Docker daemon 和 `docker.io/library/python:3.12-slim` / `docker.io/library/node:22-bookworm-slim` 镜像。runner只执行检查，不调用模型、不授予G1；所有命令保存日志/hash/测试数与skip。CI端口5188/5199/5208/5209必须空闲，先停止自己启动的本地验证服务，不停止无关程序。生产worker与CI时间分别记录。

真实样例还必须通过标准导出→P0开发作业→校验过交付→正式运行队列→独立核心旅程证明。宿主 `BatchService.assess_g1(plan_id, manifest_path)` 验证完整CI记录与实际规范业务记录、归档、当前审阅及精确运行绑定；没有公开“把G1设为通过”的接口。manifest不能仅写 passed=true。

只有本轮G1真实通过后，才对 [t08-request.json](t08-request.json) 调用正式 preview；执行必须使用刚返回的 plan ID/digest 和稳定幂等键。预定三场景来自 [SAMPLING_PLAN.json](SAMPLING_PLAN.json)，失败不更换。首批最多3个实际产品（总上限10、含G1）；G1已发表的同依据模板复用，另外两个场景由明确 reviewed-draft-v1 策略准入，保留草案属性，不伪称用户逐条确认。T08仍使用同campaign剩余额度。

## 外部依赖恢复

- provider/网络：保留 stage 的 input.json、process.json、events.jsonl、stdout/stderr、cli-summary.json 和已完成检查点；恢复同job，不重新解析固定源码HEAD。请求模型与观测模型分别保留，无观测不填实测。
- Docker/镜像：真实运行保持 unavailable/blocked_external，按日志恢复daemon或补齐声明镜像；通过正式acceptance入口新建run，不沿用旧通过。
- 本机 Docker 28.3.2 曾对短名 `python:3.12-slim` / `node:22-bookworm-slim` 的 inspect 返回 No such image，但镜像清单、ID inspect 和无网络容器启动均成功。已将运行器的固定镜像引用写全为同一官方镜像的 `docker.io/library/...`，实际严格门禁20项/0 skip通过；没有换镜像版本、放宽断言或绕过检查。镜像ID仍由宿主解析并写入运行环境。更新运行代码后只在无活动作业/调用的边界重启本任务worker。
- API/worker重启：scheduler专属锁阻止两个调度器同时恢复；outbox补齐后继审阅，lease/token拒绝迟到写入。进程清理只针对已证明属于本任务的PID/PGID/工作区或标签容器。没有证明时活动调用保持uncertain及原计数。
- 案例已提交而模板失败：从应用实证读取固定case版本，修复模板阶段；不删除研究、不重做搜索掩盖失败。
- 验收程序本身错误：走模板正式repair生成新版本、重新审阅、重新导出与运行；不能直接修改冻结包或弱化断言。应用实现错误则绑定真实失败报告修应用，模板不变。
