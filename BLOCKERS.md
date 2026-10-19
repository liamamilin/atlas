# Blockers and Explicit Non-Goals

T002-T024 的本地实现与回归门禁已完成；T025 浏览器 backup/restore、T026 provider artifact containment、T027 分类 provider 门禁、T029 本地安全审查、T030 旧验收迁移、T031 backup 生命周期和 T032 错误契约已完成并通过本地/真实 disposable smoke；当前仅剩 T028。以下事项不能在当前环境中被伪装成已验证，因此阻止最终发布级 `PROJECT_ACCEPTED` 标记。

## External verification required

- 分类 provider 已验证：`qwen3.8-flash` 成功，`opencode-go/deepseek-v4.1-flash` 返回 `model_unavailable`；不自动切换模型。目标发布环境仍需复验。
- T028 需要的远程 GitHub Actions runner、发布 SHA、macOS 签名身份、公证凭据、目标机器和发布渠道当前不可用；本地检查不能替代这些证据。
- 当前固定验证器和本地工作区检查不是 OS/容器沙箱；不能把它们描述为完整隔离证明。
- T025-T027/T029/T031 已在本地和 disposable real provider smoke 中固定受控 restore、runtime containment、分类错误边界、显式 backup 清理和威胁模型；这些边界不是 OS/容器沙箱证明。

## Product follow-ups outside this cycle

- 任务输入门禁、execution/baseline/需求修订/验收条件快照、逐条件人工结果和旧数据 dry-run migration 已落地。
- generation/provider/backup/restore 长尾错误契约已落地；目标发布环境复验仍未完成。
- 需要目标平台环境后，再执行完整发布验收和人工安全审查。

这些限制不被自动重放、自动写入、自动删除或提交/推送所掩盖；解除条件是提供相应环境、凭据或明确的产品决策。阶段顺序和验收条件见 [U17 剩余产品收口与发布打磨计划](docs/U17_REMAINING_PRODUCT_PLAN.md)。
