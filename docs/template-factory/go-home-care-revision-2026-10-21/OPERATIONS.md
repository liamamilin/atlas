# 受限修订入口与恢复

仅本轮家庭保养辅助样本，固定 REQUEST.json。CLI台账通过 BudgetLedger.register_auxiliary_revision 正式服务登记，reserve事务同时检查本阶段6次、原500次及固定24小时窗口。不修改G1/T08/grant或业务修复记录。注册不启动时钟，首次预留启动24h，后续重载不滚动。

```sh
python3 examples/assisted-trials/revise_with_opencode.py --request docs/template-factory/go-home-care-revision-2026-10-21/REQUEST.json --until generated
# 对当前probe在无网络只读容器中执行home_care_fixture.py，结果存本版本FIXTURE_RESULTS.json。参见CI同名步骤及FIXTURE_EXECUTION.json。
python3 examples/assisted-trials/revise_with_opencode.py --request docs/template-factory/go-home-care-revision-2026-10-21/REQUEST.json
```

本轮已成功，不应再次生产；最后命令只会核验复用检查点、正式导入身份及下载。不删除旧 LAUNCH_INTENT、原始返回或失败文件。未知启动/失败不会盲目补调；先查对应 CLI 摘要和正式 reservation。

若首轮有效审阅needs_changes且仍在范围/额度内，保留r1，使用 --round 2 创建内容新版本，重复相同隔离检查再独审。needs_changes不是协议失败，不能原样重抽审阅。技术恢复只有在证实先前会话关闭且无完整有效交付后才可使用新的受控检查点；本轮未使用此保留额度，默认入口不会自动消费它。

冻结前验证真实模型返回与合并内容、固定来源、叶子、原案例r1、场景r1、新审阅摘要与实际读全覆盖。export_trial再次核验修订来源及派生definition；失败审阅不能冻结/导出。通过后正式POST /api/factory/blueprints/import；同ZIP复用同artifact。POST /api/factory/artifacts/{id}/development-package 生成标准包，然后实际GET下载并核对6份开始文件和完整案例记录。

原始模型审计普通文件位于audit/，calls/中的OpenCode私有.git与展开源码不提交为gitlink。review-materials.zip保留完整新审阅材料。
