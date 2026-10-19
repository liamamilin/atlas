# G1 一次性协议恢复：实际交付与停止点

本次已实际消费唯一协议机会并继续生产，最终因固定规格的来源引用与当前场景证据视图不兼容而正式暂停。**G1 blocked；T08 未启动。** 当前原 job `job_7742b1c124be4c9ab3a0096da5cdd772` 为 attempt4 / failed，最后事件 stage 为 `blueprint-code-0-7`；真正失败位置是五文件生成后的 `render_candidate` 来源结构校验，不是该 README 模型调用失败。

|项目|实际结果|
|---|---|
|累计 CLI|64/500，活动0；本次续作从56增加8次（3项预审+5份文件），没有第二次额外协议重试|
|书签业务修复|5/5，未增加第6轮；预算与会议笔记未启动、本轮各0轮|
|协议机会|历史阶段追加2保留；新 grant 已登记、唯一消费1/1，phase_acceptance 完整通过|
|有效截止|UTC2026-10-19 19:13:43.754534 / 北京2026-10-20 03:13:43.754534，原值未变；停止时未到期|
|模板与P0|本轮新冻结0、正式发布0、真实P0开发0/通过0；旧未发布冻结候选1保留|
|案例|本轮新增0、复用原规范案例r1共1；应用实证和模板仍用同一规范记录|
|生产源码|`f94dc8c05d59819927d445074a8f6a733c84b1fa`；最终交付HEAD在Git历史及最终CI证据中另列|
|源码CI|`39300021349` completed/success，check、docker-integration均通过|

## 已取得的真实证据

1. 精确重读 `5df2209`/CI39282029202 和 `51350f8`/CI39283376657，均成功，保存 `ci-resumption-verified.json`。原授权文件、grant-request、幂等键未替换。
2. 正式登记 grant `pgrant_f3595368c14d4b23b6ab536f6d198007`；唯一消费 reservation `bud_9a81a7a4adc14f49b46239ec68ee2fdb`，已completed。授权原文件SHA256为 `6592fdddfa743947cba4fcd685e3dc36d62e665203cac2c9a20ba029ee3f5829`。
3. 正式 recover-protocol 将原 job 从attempt2恢复到attempt3；恢复前后实际查询同snapshot、prepared plan、案例依据、前三检查点及父暂停，登记/恢复幂等重放均未重复消费或增加attempt。见 `actual-recovered-before-resume.json`、`actual-protocol-execution-proof.json`。
4. 唯一额外 phase_acceptance 完整通过，正常首次 decisions_defaults、runtime_protocol 通过。原始输入、输出、事件、summary、result/report在 `actual-attempt-3/`；前三旧检查点继续保留。
5. 真实发现宿主汇总审阅材料缺失，仅新增共享 `CASE_ADAPTATION_POLICY.json` 的稳定写入；不修改严格校验、投影、提示、规格或检查点。独立审查无明确问题；完整恢复回归证明六项缓存审阅直接汇总，无新预审调用。
6. 新源码13项门禁全部通过，源树摘要 `c14e6ad87cf501e367ad25620908472351fde7959283fc9b8ed16ed3246f3a28` 检查前后相同。后端613项（8项既有可选跳过），前端单测9，普通E2E17，工厂E2E27，Docker20（零跳过），其他审计/ruff/导出/数据/类型/构建通过。回归与fixture不算真实应用验收。
7. 新SHA远端CI成功后，经正式普通failed retry进入原job attempt4，实际核对59/5/grant1、六CP原文、父暂停，再resume原计划。首个新调用为文件生成。五个授权文件完整返回，不在修改范围的4份程序原样复用。见 `actual-six-checkpoint-reuse-proof.json`、`actual-final-checkpoint-preservation.json`。
8. API和worker实际根目录均为原生产根，无临时测试库残留；见 `actual-attempt-4-process-root-proof.json`。全部原调用、修复、时间、失败及授权记录保留，最终台账见 `actual-final-ledger-history.json`。

## 当前真实阻断

固定功能引用数组继承旧模板，旧模板采用 `legacy_all_accepted`，覆盖29条案例观测；当前固定检查点采用 `accepted-linked-observations-only-v1`，只有20条关联到本场景的事实。渲染后有7个功能引用了6个不在当前视图内的来源：

|功能|缺失引用|
|---|---|
|F01|S17|
|F07|S08|
|F08|S09、S11|
|F10|S08|
|F11|S10、S18|
|F12|S08|
|F24|S17|

这6条观测在**案例层**均有摘要匹配的独立accepted审阅；它们因**未关联当前固定场景**被排除，并非全局拒绝或缺少案例审阅。详见 `actual-source-eligibility-proof.json` 和独立复核 `independent-source-scope-review.json`。

修改功能引用超出原精确规格修订字段；扩大场景事实/链接或恢复旧legacy策略会改变证据资格、事实视图、research及投影摘要，不能声称原输入/六项审阅仍有效。没有进行这些改动，也未重新登记grant、增加业务修复或放宽校验。候选快照在 `candidate-attempt-4-not-frozen/`，明确不属于正式模板。

原计划已通过正式API暂停，任务保持原失败。宿主 `assess_g1` 正式结果见 `G1_ASSESSMENT.json`，passed=false，保留未发布/无交接/无P0/无运行证据等原因。

## 未运行及后续入口

独立程序差分语义审阅、新冻结、冻结后审阅、发布、标准交接实际消费、真实P0、冻结套件运行、独立浏览器运行/phase proof和G1通过均未发生。原书签、月度预算、多项目会议笔记三个T08固定样本全部未启动；不替换失败样本。

当前不能仅重放retry解决：后续须先取得明确的新业务/依据修订范围授权，协调这7个功能引用与固定场景事实视图，重新绑定受影响输入并独立审阅；本次不预先创建第6轮任务、不提出新增grant或自动扩大限额。原G1截止仍约束任何后续生产，暂停不冻结或延长时间。建议后续把同一严格引用检查提前到程序生成前，减少无效文件生成；该改进列计划，未借其改写当前结果。

此前外部CI等待记录保留为 `*-EXTERNAL-CI-ARCHIVE.json`，attempt3宿主汇总缺陷与真实失败证据也保留；当前终态以 `STOP_RECORD.json` 为准。实际provider内部请求次数、真实观察模型身份和费用仍未知，不以CLI会话数推算。
