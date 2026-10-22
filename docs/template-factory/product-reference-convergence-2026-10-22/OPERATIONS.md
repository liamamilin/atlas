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

目录入口 /factory?view=references；GET /api/factory/product-references，GET /<ref_id> 和 /<ref_id>/download。该类是完整产品认知参考包，不是含执行代码/验收程序的旧标准开发包，应用仍未运行；正式发布区与严格G1/T08不改。入库幂等复用，同输入恢复不重复模型或案例。
