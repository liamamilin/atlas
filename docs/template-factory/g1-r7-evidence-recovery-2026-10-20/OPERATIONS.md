# 正式操作顺序

正式 pack 为仓库 application-atlas-production-pack，生产根为 application-atlas-production-pack/atlas/template-factory。所有命令显式传 --pack、--root，不继承临时 ATLAS_FACTORY_ROOT。

1. 完成本轮 13 组验证，提交并推送；获取该精确源码 HEAD 的成功 check 和 docker-integration 原始 JSON，保存 ci-source.json。
2. 使用 atlas.evidence-recovery-prepare.v1 请求经 batch_cli evidence-prepare 只读重建完整提案，绑定授权 SOURCE_REF/SHA、当前 source_commit、64 位 source_tree_digest、CI 文件摘要/运行 ID。
3. evidence-grant-register 接收 {prepared_proposal,request}；稳定 request_key 不变。登记不启动 worker。
4. recover-evidence 原 job，atlas.evidence-recovery.v1，绑定实际 grant_id、同 request_key、提案摘要。原子排队 attempt 2，子/父批次仍 paused。幂等读回不替代任务/预算/检查点实际查询。
5. 核对之后 resume 原计划。唯一补证调用启动前同事务锁住预算、当前 token/lease 与 grant；已启动或不确定不释放、不补调。
6. 结果与原始输出落盘，追加新 phase 和有效六维检查点；零 author 消费九份已准备文件；依次聚合、冻结、独立审阅、发布、标准交接消费、真实 P0、独立运行与 phase proof、宿主评估 G1。未通过不启动 T08。

登记到恢复完成前，checkout 只允许 ci_evidence 指定的 CI 文件有未提交变化；请求/响应先写 /tmp，恢复后再归档。源码门禁不接受旧 CI 代替新增源码。

若唯一审阅已经完整通过，仅宿主后处理发生可修复错误：修复宿主并完成新源码检查/精确 CI，通过 resume-evidence-result 正式追加源码门禁与同任务下一 attempt。请求 atlas.evidence-saved-result-resume.v1 包含 grant_id、稳定 request_key、source_gate、expected_saved_result_sha256。服务核实原实际 call_attempt 的 result/input/source、已完成 reservation 和完全相同的被审阅材料；不创建 CLI 资格，不改变原 grant/proposal。语义未通过、材料改变、启动不明均不可走此入口。
