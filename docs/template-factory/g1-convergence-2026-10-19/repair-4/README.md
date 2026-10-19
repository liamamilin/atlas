# 当前真实停止样例：第4轮内部规格修复

本目录对应job_a53c47f3694047489c4f82cfc2e346be、attempt2、blueprint-plan-1；不是冻结模板或真实应用。旧attempt1返回保存在../repair-3，不能与当前ARCHITECTURE混用。

- blueprint-plan-0/1.json：正式持久检查点，含原提案与精确修复后的提案。
- context-SCOPE_FAILURE_0.json：本次实际越界及应恢复的基线limits。
- context-SPEC_REVISION_1.json、blueprint-generate-1-*：模型明确补丁、原始交付与CLI摘要，第4轮正式计费。
- CURRENT_ARCHITECTURE.md：当前提案架构。
- blueprint-design-check-1-*.json：各独立审阅的正式检查点。
- blueprint-spec-review-1-runtime-v1.json：宿主聚合的规格预审，五项通过、一项阻断。
- reviews/：六项审阅实际input/result/cli-summary及source快照；仅规格预审，没有运行程序。
- canonical-case-current.json：从正式共享案例服务读取的固定r1。源码观察不是上游运行证据。

历史程序输入的完整基线仍在[原冻结样例](../../v1-2026-10-19/g1-real-sample/template-8d9229d3895b/)，摘要8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9。未编辑旧归档，也没有把旧程序冒充本轮新程序。
