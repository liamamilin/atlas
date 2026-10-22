# 两样本修订操作

全量暂停，不运行 produce_all_leaves resume/start。案例/输入/研究不改。模型 open-design/deepseek-v4.1-flash。

经精确源码CI通过后追加正式 host revision；prepare 固定父候选/旧失败/本轮用户请求/输入/提示和源码CI摘要，run 通过 begin_revision 正式登记后受原账本控制调用 author/review。阶段在原phase内，独审使用新会话，实际读取覆盖和全部观察逐条核验。静态通过才冻结参考ZIP并经 ReferenceCatalog 正式导入。

```sh
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_revision.py prepare --leaf bookmark-manager
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_revision.py run --leaf bookmark-manager
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_revision.py prepare --leaf polling-application
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_revision.py run --leaf polling-application
```

只有r2真实内容问题且原每叶限额仍有余量时，用 --revision r3 --parent-revision r2 准备集中后继。不得删除LAUNCH_INTENT重新调用，不得用新job绕过已经计账的阶段。来源/状态不明则停止本试跑并核查。模型 needs_changes不是协议错误。单样本失败留记录，另一固定样本继续。

### 已交付审阅的零调用读取证明恢复

只适用于三项真实交付已保存、独立审阅已经通过、宿主仅因读取覆盖证明失败的同一候选。先使证明修复的精确源码CI通过并追加正式host revision，再运行：

```sh
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_revision.py recover-read-proof --leaf bookmark-manager --revision r4
```

入口核验原注册请求、固定输入、当前正式源码、暂停和账本，并提供禁止模型调用的回调。原 `OUTCOME.json` 不变，新结果写入 `RECOVERY_OUTCOME.json`。标准结构副本未完全读取时，只有原始事件证明完整读取等价的权威JSON、长字段全部分页和所有源码材料，且与原绑定、独审会话和返回完全一致，才生成明确标识 `canonical_equivalent` 的证明。冻结包绑定该证明，正式入库重新计算而不信任单独声明。不能把这种恢复用于内容拒绝、缺交付、错误输入或真正缺失的读取；恢复不增加任何调用资格。

其他叶子合法增加共享账本后，再次执行恢复会保留首份回执，并写入按内容摘要命名的 `RECOVERY_REPLAY.*.json`，记录本次真实的零调用前后状态。重复相同状态复用该证明；历史回执不能代替当前状态查询。

### 读取不完整的拒绝意见

投票r2的原始独审提出14项修改，且COPYING与Poll.php未被完整读取；原失败及 `REVIEW_RESULT.json` 缺失保持不变。严格验证原输入、候选、来源、原始模型交付、独立会话及完成的计费记录后，只把该拒绝作为明确标识的**未合格修订线索**，写入新版本lineage及diagnostics。它不能授权通过、发布或入库。不得把原始pass、协议无效或身份不符的结果当作该类线索。

新的r3仍需新的生成和独审会话，完整读取全部规定源文件（不限于已引用行）、全部规定长字段分页（包括重复内容），并重新通过完整门禁。仅使用投票剩余2次调用；原每叶6次及全量暂停不变。

目录入口 /factory?view=references；GET /api/factory/product-references，GET /<ref_id> 和 /<ref_id>/download。该类是完整产品认知参考包，不是含执行代码/验收程序的旧标准开发包，应用仍未运行；正式发布区与严格G1/T08不改。入库幂等复用，同输入恢复不重复模型或案例。
