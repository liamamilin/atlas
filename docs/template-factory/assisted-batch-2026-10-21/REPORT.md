# 可重复的小批量模板生产：本轮交付

原书签、预算、会议应用及数据保留；三个进程现场已停止，已按原目录重启，未启用演示初始化。Atlas仍使用默认生产根目录，未设置临时ATLAS_FACTORY_ROOT。本轮新增家庭库存、专注计时、语言学习三个叶子的辅助模板，只开发预先固定的家庭库存代表应用。

## 固定批次与实际结果

[MANIFEST.json](MANIFEST.json)在生产前固定代表场景、顺序、案例线索及输出目录；[EXECUTION.md](EXECUTION.md)为统一说明。全部通过同一个 `produce_batch.py` / `export_trial.py` 入口，重用现有场景服务、CaseLibrary、render/freeze、标准阶段导出和制品导入。没有新调度平台或宽松模式。

| 叶子 / 明确场景 | 固定来源与共享案例 | 目录和下载入口 | 处理结果 |
|---|---|---|---|
| home-inventory-application · 搬家前家庭物品盘点 | [Homebox @ 1fd28822](https://github.com/sysadminsmedia/homebox/tree/1fd28822634a3d5935c002d569559ef46530d4a0)；case:assisted-batch-home-inventory r1 | [Atlas目录](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_c4f9d29ee90e4ddebd300f34d66666cb) · [标准包下载](http://127.0.0.1:5188/api/factory/development-downloads/bfb7c14d60ce409aad2d7b92487a8055) · [固定离线包](home-inventory/atlas-development-package.zip) · [来源模板](home-inventory/packages/template-snapshot.zip) | 5组浏览器旅程、刷新及真实同目录重启通过；[运行5276](http://127.0.0.1:5276/) |
| focus-timer · 写作前的一轮专注与休息 | [Pomotroid @ dda06e6b](https://github.com/Splode/pomotroid/tree/dda06e6bf412bebe5ef8668a4357c52d974dc874)；case:assisted-batch-focus r1 | [Atlas目录](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_cfeddf44187a403ba0148e3264c5627d) · [标准包下载](http://127.0.0.1:5188/api/factory/development-downloads/fc21bf88ef0b4d8b8dd14023e1e66b4a) · [固定离线包](focus/atlas-development-package.zip) · [来源模板](focus/packages/template-snapshot.zip) | **尚未开发/运行应用（not_run）** |
| language-learning-application · 出行英语三课：问路、入住、点餐 | [LibreLingo (archived) @ 3c4bcfb3](https://github.com/kantord/LibreLingo/tree/3c4bcfb3ef999ae48ee3d361afb0c4a5fa317dee)；case:assisted-batch-travel-english r1 | [Atlas目录](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_b91f50c7d8c741aa8d04715852f8effa) · [标准包下载](http://127.0.0.1:5188/api/factory/development-downloads/a21a01a97672459d8c9f15e5a7f909bd) · [固定离线包](travel-english/atlas-development-package.zip) · [来源模板](travel-english/packages/template-snapshot.zip) | **尚未开发/运行应用（not_run）** |

[家庭库存源码包](home-inventory/home-inventory-source.zip)不含用户库；[使用说明](../../../examples/home-inventory-trial/README.md)。仓库根启动：

```sh
python3 examples/home-inventory-trial/app/serve.py --port 5276
```

正式场景服务保存为r1草案；用户本轮授权辅助生产，在本地导出副本注明确认来源，未伪装成人工正式确认。每项输入/案例/定义/接收回执分别保存在该项目录；CaseLibrary保存共享case，与应用实证API、模板inputs/shared-case-record.json保持相同case_id、revision和digest。文档的JSON缩进与宿主序列化可不同，完整记录对象一致。

## 原三份模板接入

[EXISTING_IMPORTS.json](EXISTING_IMPORTS.json)记录书签、预算、会议的Atlas目录链接、原摘要与导入摘要；[INTEGRATION_RESULTS.json](INTEGRATION_RESULTS.json)记录六份模板真实阅读、案例回查、下载→重新导入相同ID、阶段导出结果。原三份标准包也可从[existing-downloads](existing-downloads/)读取。

原ZIP结构为 `inventory.json + provenance.json + source/`，现有原始导入协议为根 `template.json + integrity.json`。适配先安全解包并校验完整原freeze，再检查共享case固定digest，将source交给既有导入器。新制品摘要因宿主导入来源而改变；原冻结摘要、原ZIP SHA、原provenance和固定案例引用完整保留在 `provenance.imported_snapshot/shared_case_refs`，不把两个摘要混为一谈。

重复导入按原冻结摘要复用，且支持下载后再导入仍复用当前ID。辅助模板下载现在保留宿主冻结外层；历史source-only存档不改写。UI增加名称/场景/叶子搜索、辅助来源标签、原摘要、固定案例回链；保留章节阅读、试用范围和阶段导出，不标为严格发布或独立审阅通过。

## 代表应用真实旅程

新的 `inventory_from_handoff` 开发上下文只接收已经完成并由Atlas实际导出的标准包，先读HANDOFF、CURRENT_PHASE、验收合同、架构/产品/决策六文件并记录摘要，再创建应用。消费记录见 [CONSUMPTION.json](../../../examples/home-inventory-trial/CONSUMPTION.json)，实际ZIP SHA保存在SOURCE_PACKAGE.json，未事后改写模板充来源。

| 旅程 | 实际结果 | 原始证据 |
|---|---|---|
| 空库与位置 | 创建书房、厨房，保留默认未分类 | home-inventory/evidence/01-* |
| 登记与汇总 | 书桌100、台灯20，总计2件120元 | 02-* |
| 修改、移动、刷新 | 书桌改90元并移厨房，总计110元；刷新保留；书房只剩台灯20元 | 03-*、04-old-room-only-lamp |
| 检索及归档恢复 | 备注maplemove找到书桌；归档后默认隐藏，归档视图找到；恢复保留位置和90元 | 04-* |
| 实际重启 | PID87623→89997；停机连接拒绝，同目录重启全字段一致，浏览器重载仍110元；格式化后再重启加载最终源码，数据再次一致 | 05-*、06-final-* |

以上为实际UI与进程证据，不由HTTP探针替代；准确PID以JSON原件为准。最终截图 home-inventory/evidence/final-home.png。示例物品明确带“试用”，不是真实家庭财产资料。估值由用户填写，不作保险或市场价格证明。

## 检查与复跑

- 认知包专项55项，47通过、8项Docker条件测试跳过；没有将未运行Docker标通过。另交接视图2项、共享案例12项通过。
- 代表应用4项回归与冻结A01–A04全部通过（A04自有进程真实重启）。无效金额/旧版本冲突零写入、HTML转义与失败原稿另有回归；新上下文发现并修复冲突渲染问题后重跑通过。
- ruff、TypeScript检查通过；最终源码包在仓库外解压后实际--demo启动，4件示例物品，无仓库运行依赖。[PACKAGE_CHECKS.json](PACKAGE_CHECKS.json)核对三个原冻结包、摘要与嵌入共享案例。
- [REPEAT_PROOF.json](REPEAT_PROOF.json)实际重复家庭库存完成项：共享案例身份/修订、全部制品ID与摘要、原固定ZIP及标准包、原三个用户数据库字节摘要均不变。服务返回case_replayed=true，导出返回reused=true。复跑不覆盖既有包，不重复新增案例。
- 新增模板生产失败0。开发时测试fixture缺mvp_apps/重用排他ZIP路径曾失败，已修正夹具后通过；不是被隐藏的生产失败。模板未降低验收断言。专注/英语的探针仅静态交付，未运行，不计入通过数量。

复跑当前生产根目录的一个完成项：

```sh
python3 examples/assisted-trials/produce_batch.py --manifest docs/template-factory/assisted-batch-2026-10-21/MANIFEST.json --item home-inventory
```

输入变化会停止并要求新版本，不覆盖旧输出；单项异常保留failure.json，继续其他项。当前清单引用当前生产库的场景/案例身份，不声称把全新空库回放成相同生产身份。新批次另建manifest及AUTHOR_INPUT/固定source-snapshot/acceptance，batch_id用于任务与幂等命名；Codex仍需研究、编写和核验。

## 缺口和人工步骤

研究选源、阅读判断、具体场景及模板/验收编写仍由Codex完成；脚本执行服务保存、结构检查、冻结、导出、登记和复用。代表应用由新的Codex上下文实现，主上下文操作真实浏览器；没有独立模型审阅通过声明，也不是无人值守自动工厂。

全部上游仅静态研究、未安装运行；证据独审pending。Homebox/Pomotroid有代码定位；LibreLingo保留课程/练习文档依据与归档状态（最初候选URL重定向，实际固定kantord/LibreLingo），不推荐按此旧版本部署，不复制课程、媒体或上游实现。三份证据ZIP都保留许可证；源文档观察、设计推断、上游/下游运行分别标识。

家庭库存后置照片/收据附件、层级位置、导出、多人协作；专注后置长周期、网站拦截、通知可靠性；英语后置语音/听力/SRS和教学审阅。后两应用未开发、未运行，不能把模板导出称为应用可用。

[FINAL_STATE.json](FINAL_STATE.json)：新增辅助模板3、接入原模板3、新应用1；原调用86＋此前连通性1＝87/500，本轮OpenCode新增0，原业务修复8/8。严格G1仍blocked，T08未启动，历史失败、grant、预算和时间记录未重置。本轮不恢复严格生产。
