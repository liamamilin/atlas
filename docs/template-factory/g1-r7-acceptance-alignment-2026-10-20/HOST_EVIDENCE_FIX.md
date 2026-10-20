# 真实阻断后的宿主补证准备

本补修发生在 R7 六项真实预审完成、计划正式暂停之后。没有重新调用模型，没有重试或替换旧检查点，没有改动正式 job、规格、程序补丁、业务修复或期限。原真实生产源码为 e97431f；新源码及 CI 单独记录在 FINAL_COMMITS.json，不能倒推为本次生产已使用的源码。

`cognition.py` 为已绑定的 R7 prepared revision 增加受限静态送审材料：

1. 再次通过正式只读准备服务校验原请求、来源任务及检查点、原始程序字节、完整九项 manifest 和四份确定补丁的结果。
2. 仅给 phase_acceptance 投影加入 source/prepared 程序、来源摘要、原授权、精确 patch、approved revision 和筛选后的 A05 意见处置。所有材料从 store.pack 对应仓库根读取，不混用另一 checkout 的文档。
3. 增加材料摘要并把真实文件纳入 tree manifest；材料变化改变 projection_digest。R7 缺请求、manifest/旧字节变化明确失败。
4. 仅该条件下修正“程序尚不存在/历史程序被排除”的提示，明确这些是已校验的静态程序，禁止执行、伪称通过或把处置材料当作指令。普通 v1/v2 路径继续使用原提示、原输入和原缓存身份。
5. 保留既有 proposal/projection 检查点比较；新证据投影不能覆盖旧 blocked，仍报 checkpoint_changed。没有新增恢复操作、operation 别名、grant 或重试额度。

`test_factory_r7_review_evidence.py` 检查九项来源、四 replace/五 reuse、A05 实际断言可读、授权处置、摘要失效、manifest/旧字节篡改、缺请求拒绝、旧路径不变及旧投影检查点拒绝。原 R7 正向临时库链接和旧聚合缓存回归一起检查。实际日志与完整 13 组日志位于 verification/，不替代真实生产。

从当前真实失败任务只读生成的补证包已归档在 `host-evidence-preparation/`，READ_ONLY_PREPARATION.json 记录 23 份材料及各自 SHA、proposal 和材料摘要。它是准备包，不是新的 projection 审阅结果。旧六份实际投影仍单独保存在 actual-review-projections/；没有用新包覆盖历史输入。

独立 Sol 复核确认补证与停止边界，报告另存。第一次新完整检查遇到一处未使用局部变量的 Ruff 错误，已删除该行；原失败日志在 verification/host-evidence-fix-lint-failed/ 保留，随后完整重跑，而非把失败改写成通过。

真实生产继续所缺的是适用于当前 R7 任务和新补证投影的正式恢复资格与入口；本补修本身不授予资格。不能调用旧 R5 recover-protocol，不增第八轮，不延期，不能仅因为总 CLI 尚有余额就重审。详见 RECOVERY.md 和 STOP_RECORD.json。
