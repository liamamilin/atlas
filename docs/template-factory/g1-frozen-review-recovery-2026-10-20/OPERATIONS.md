# 正式操作与停止入口

生产根目录必须显式设置为 `application-atlas-production-pack/atlas/template-factory` 的本仓库绝对路径；不得沿用临时测试根。所有真实请求从正式服务/CLI执行，禁止直接更新数据库。

## 请求合同

只读准备：`POST /api/factory/v1/jobs/job_b01427592b164863aab5bedf7b3863bb/prepare-frozen-review`（以实际 V1 路由前缀为准，CLI等效 `frozen-review-prepare`）。请求为 `schema=atlas.frozen-review-prepare.v1`、固定 `request_key=atlas-g1-r7-frozen-review-recovery-2026-10-20-once`、原授权 source_ref/source_digest 和绑定新源码提交/树/CI原文的 source_gate。

登记：CLI `frozen-review-grant-register --request register-request.json`，包含完整 `prepared_proposal` 与原 `request`。正式存入现有 evidence grant/use 表；不会启动 worker。

恢复：CLI `recover-frozen-review job_b01427592b164863aab5bedf7b3863bb --request recover-request.json`，请求为 `schema=atlas.frozen-review-recovery.v1`、实际返回的 `grant_id`、原固定 request_key、proposal_digest。原子地恢复同 job attempt 1→2，父批次保持暂停。读取真实 job/batch/grant，核原 snapshot/checkpoints/source/artifact 后，才 `resume plan_87059846caf345d2b2fe690657cf324f`。

## 唯一调用与异常

真实调用的请求模型固定为 opencode-go/deepseek-v4.1-flash，operation 与 logical scope 保持原值；此次专用 timeout 1800 秒不改原 snapshot 的600秒。reserve 与 spawn 均核原期限，spawn前剩余必须至少2700秒。

读取源码检查点和CI未在北京时间18:36:52.855422前就绪，则不启动。唯一调用出现超时、无效协议/引用、blocked/uncertain，或需要交付修改时，通过原 plan pause 正式暂停。资格已启动或不确定时绝不补调。真实 unavailable 与原失败均保留。

仅当真实合法 result 已交付、宿主提交前中断时，可使用 `resume-frozen-review-result`；请求 `schema=atlas.frozen-review-saved-result-resume.v1`、实际grant_id、稳定续交request_key、新 source_gate、expected_result_sha256。服务重新核完整八维、真实来源、正常完成的reservation、raw→result→report及实际call_attempt，设置 `cli_allowed=false`。缺合法结果不适用。

任何正式请求与响应将存入 operations/；实际授权、恢复与停止结果以这些回执和现场读查询为准，此操作说明不证明已执行或已通过 G1。
