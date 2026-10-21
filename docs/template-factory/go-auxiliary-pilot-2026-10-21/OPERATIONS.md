# Go 辅助生产操作说明

固定模型 `opencode-go/deepseek-v4.1-flash`，使用本机已有可信 provider 配置，不复制凭据。

```sh
python3 examples/assisted-trials/produce_with_opencode.py --manifest docs/template-factory/go-auxiliary-pilot-2026-10-21/MANIFEST.json
```

每项最多三个会话：discovery（联网）、blueprint-generate-aux（固定源码只读研究/生成）、blueprint-spec-review-aux（新会话，固定候选只读审阅）。由现有 CLI 调 BudgetLedger，先持久预留再启动，计入原 campaign 的500总上限。辅助阶段使用稳定batch_id锚定首次8小时，不修改任何严格G1/T08记录。

发现返回仓库和文件线索，宿主通过GitHub API固定一次commit、许可证及最多8个文件（单文件180KB）；不执行上游。模型不能指定已接受证据身份、摘要或入库状态。生成返回认知设计和验收程序文本；宿主只做语法解析，不执行模型代码。

独审必须不同真实session，绑定全部作者结果和固定源码，七类检查全部通过、逐观察接受、阻断问题为空才继续。案例和观察审阅通过CaseLibrary正式服务保存，模板使用同一案例记录。固定包由现有export_trial导出，正式API导入辅助目录并生成开发包；不发布为正式模板、不声明应用运行通过。目录登记复用已有CATALOG摘要绑定。

再次执行同一命令：验证提示/输入/源码/输出绑定、复用三个检查点，服务按稳定幂等键复用案例和模板；不覆盖旧冻结包和用户数据。最终交付前实际验证重复执行新增会话0。

停止和恢复：失败或启动状态不明时保存FAILURE、LAUNCH_INTENT、原始响应、CLI summary、events和BUDGET_AFTER。不自动再启动该阶段，不换job或batch绕过。CLI已完成交付、仅宿主结果落盘中断时可从原始返回恢复同一结果；摘要不一致拒绝恢复。已有有效RESULT/DELIVERED则逐字节/对象身份核对后复用。

研究与生成由Go模型完成；Codex仍负责编写本轮执行入口、选择范围、处理宿主缺陷、校验并提交代码。尚未验证全叶子自治批量生产，也不承诺模型审阅等于运行正确。

## 本次真实停止点

本试点原三次已执行；用户另外授权一次同内容可读材料独审，记录在home-care/READABLE_REVIEW_AUTHORIZATION.json。第4次结果needs_changes，唯一新增候选经正式API撤回，当前累计91/500。

`--complete-readable-review`只能复用此一次检查点；重复执行仍返回真实失败，不补调。新生产默认review_format=2并持久固定，使长字段首次即可完整阅读。本批不执行第5次调用；修订范围见REVISION_PLAN.md，原冻结ZIP不改。
