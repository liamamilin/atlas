# 同任务第三次调用的正式恢复

本页记录实际执行，不替代初次恢复附件、旧 OPERATIONS.md 或旧停止记录。用户随后明确撤销了旧启动余量的阻挡；原始文本及 SHA 保存在 TIMING_OVERRIDE_AUTHORIZATION.txt 和正式 proposal 中。旧 18:36:52 启动界限与 19:21:52 绝对期限作为历史字段保留，本次正式 time-resume 记录成为该产品 G1 的有效期限依据。

## 已执行

- 运行源码：da15a23a4007fa60158a87ee5a24e3d7b86852a7；CI 39415837779 的 check、docker-integration 均成功。
- 根目录：本仓库 application-atlas-production-pack/atlas/template-factory；没有临时测试数据库。
- CLI `frozen-review-prepare`、`frozen-review-grant-register`、`recover-frozen-review` 使用 operations/ 内固定请求；实际响应与重放回执一并保留。
- 新 grant：egrant_5168847ee98d4b7f980779bb9199f44f；恢复 receipt：frec_60a38757ec0c4363a193b922155df22a。
- 原 job_b01427592b164863aab5bedf7b3863bb 从 attempt 2 恢复为 attempt 3；恢复时父、子批次仍暂停。重放未再次激活时间或增加 attempt。随后正式 resume 原 plan_87059846caf345d2b2fe690657cf324f。
- 真实 reservation：bud_2b188bf21f09446c843877b9025c1841，opencode-go/deepseek-v4.1-flash，单次最大 1800 秒。

## 有限时间恢复

以旧额度失败被正式记录时刻 1792490680.244128 为暂停点，恢复剩余 4632.611294 秒。首次正式恢复于 1792496531.354074 原子激活，有效截止 1792501163.965368，即北京时间 2026-10-20 20:59:23.965368。幂等重放不再顺延。该例外只绑定原书签产品、原计划及 G1；不扩展 T08 或其他产品。

500 次总额度、7/7 业务修复及全部已消费资格不变。独立诊断调用 1 次纳入保守总额；本次启动后工厂台账 82、诊断 1，合计 83/500。禁止本次调用失败后自动补调、引用修复或第八轮业务修复。

输入、叶子、冻结 source 与已批准提示的字节核验见 operations/ATTEMPT3_IMMUTABILITY.json；历史台账和原审阅未改写见 operations/HISTORY_PRESERVATION.json。本页只证明正式恢复与实际启动，不证明独审或 G1 通过，最终状态以本轮交付报告和真实服务记录为准。
