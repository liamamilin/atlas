# 十模板辅助批次交付报告

交付核验：2026-10-21T06:00:18.823578+00:00。十项全部登记，新增十份共享案例研究。两个代表样本在首次生产前固定，均由新的开发上下文消费标准包后实现。前一批六份模板与四个应用保留。

本轮为Codex辅助生产；上游均未运行，静态证据独审pending。两个代表应用取得真实核心浏览器/重启结果，其余八项明确not_run。不是严格G1/T08通过，也不是OpenCode自动调研。

## 十项成果与入口

| 场景 / 叶子 | Atlas与开发包 | 固定来源 / 许可证 | 结果、主要后置范围 |
|---|---|---|---|
| 每周晚餐计划与合并采购清单<br>`meal-planning-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_6949040b690c40b3ad7415eec367242c) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/aedea3c52526466397bf5abcbcd1573b) · [本地包](meal-plan/atlas-development-package.zip) | [Mealie@9b66aa319d32](https://github.com/mealie-recipes/mealie/tree/9b66aa319d32ea5dbdf112fe6bcda60015702721)<br>AGPL-3.0根LICENSE；参考研究，不复制实现 | 浏览器与重启通过；仅晚餐/7天窗口；菜谱不可变，无营养建议、单位自动换算、附件、抓取、同步或采购下单 |
| 同机聚餐地点投票<br>`polling-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_e1761c3db0a941348f9a97fb47c279b3) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/f5cc8122626f4cb88a2bcfebc587612d) · [本地包](dinner-poll/atlas-development-package.zip) | [Nextcloud Polls@65bf4627ee9a](https://github.com/nextcloud/polls/tree/65bf4627ee9a76c52034e796eda75ae5112ad7c3)<br>AGPL-3.0-or-later（Vote.php SPDX及COPYING） | 浏览器与重启通过；本机同屏、代号非身份认证；不做远程分享、权限隔离、防恶意刷票或正式选举用途 |
| 个人书架与阅读进度<br>`reading-library-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_ae75820e56d148ca98ecab408a68ad92) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/18f4eb7bede84fe999ff6cad8badb361) · [本地包](reading-log/atlas-development-package.zip) | [Calibre-Web@6e840acbda8d](https://github.com/janeczku/calibre-web/tree/6e840acbda8d62fdd159bf3855c01872d629a914)<br>GPL-3.0（根LICENSE；只研究，不复制实现） | 模板已登记；应用未运行；不管理书籍文件/版权下载、读书社交、ISBN抓取或多书架关系。 |
| 两日城市行程与顺序安排<br>`travel-itinerary-planner` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_a7f570f681834f778db88dfe41d1b631) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/61476cc19dcd43e9a5314020b21451c3) · [本地包](weekend-trip/atlas-development-package.zip) | [TRIP@856b1edfe81a](https://github.com/itskovacs/trip/tree/856b1edfe81a735fce4b544c2e16a6518cebf164)<br>MIT（license.txt；只研究，不复制实现） | 模板已登记；应用未运行；无地图、路线最优解、天气、订票或远程协作，地址正确性由人确认。 |
| 零工项目工时与日汇总<br>`time-tracking-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_d4404c1ab4c8429db472a572e412d04b) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/a7d38468cc1c4d18b7e7ef4465272d69) · [本地包](work-log/atlas-development-package.zip) | [Kimai@acc17ef21c2f](https://github.com/kimai/kimai/tree/acc17ef21c2f1466a0b399cf6595fd4b20b1f085)<br>AGPL-3.0（LICENSE；只研究，不复制实现） | 模板已登记；应用未运行；不做计费、发票、自动计时、跨午夜或夏令时跨度计算。 |
| 力量训练组次与训练量回查<br>`workout-tracking-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_737c65d52051433ab3510b8f148494ee) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/eea9f8d22e7c43fe800e2a7d0c319710) · [本地包](workout-log/atlas-development-package.zip) | [wger@8eed3c6d8406](https://github.com/wger-project/wger/tree/8eed3c6d8406f09874eda6e402fb68c52d6c8392)<br>AGPL-3.0（LICENSE.txt；只研究，不复制实现） | 模板已登记；应用未运行；不含动作视频、身体指标、营养/康复建议、lb换算或器械联动。 |
| 文章大纲的分支折叠与重组<br>`outliner` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_ac5ce1eedef94a539fe2047e60754416) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/190b98d2c2de4da4b70c6909e65e1623) · [本地包](writing-outline/atlas-development-package.zip) | [Logseq@e8c4c37ed432](https://github.com/logseq/logseq/tree/e8c4c37ed43299f22ca36ef898466eae02f45416)<br>AGPL-3.0（LICENSE.md；只研究，不复制实现） | 模板已登记；应用未运行；无双向链接、图谱、多人编辑、附件、富文本或撤销栈。 |
| 今日工作时间块与未完事项顺延<br>`time-blocking-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_31f54a064df949379ae9450a27c2858a) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/4572a66e4911487ebf42eff0b13ba8d9) · [本地包](day-blocks/atlas-development-package.zip) | [Super Productivity@0556bdb84d09](https://github.com/super-productivity/super-productivity/tree/0556bdb84d09faeff18d6c18abf867e28f3c1f69)<br>MIT（LICENSE；只研究，不复制实现） | 模板已登记；应用未运行；不接外部日历、通知、自动番茄钟或真实工时统计；顺延日如需补录先列待办，不静默绕过封存。 |
| 个人办事流程图与连接保持<br>`diagramming-application` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_47afbb4ac70d4dc1be628047b75e89ca) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/f68f72fb6ce741ebaeb48e6abeb68a04) · [本地包](process-sketch/atlas-development-package.zip) | [draw.io@17b367b91dba](https://github.com/jgraph/drawio/tree/17b367b91dbab91804f852645788d7ffb46dcb79)<br>Apache-2.0（LICENSE；只研究，不复制实现） | 模板已登记；应用未运行；无图形智能布局、BPMN验证、协作、图片/PDF导出或工作流执行。 |
| 指定沙箱目录的文件整理与重命名预览<br>`file-manager` | [制品页](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_de2df547557e4539a91c4d7e93542ff3) · [下载](http://127.0.0.1:5188/api/factory/development-downloads/b088eba9daf648b3becc8f2b94852f9d) · [本地包](folder-tidy/atlas-development-package.zip) | [File Browser@833d908884d5](https://github.com/filebrowser/filebrowser/tree/833d908884d5c801f30f5c098d7977177eb3a36b)<br>Apache-2.0（LICENSE；只研究，不复制实现） | 模板已登记；应用未运行；不做删除、批量规则、外盘跨FS、压缩/上传、目录树移动或权限修改。 |

各项目保留叶子摘要、场景r1、共享案例r1及摘要、固定源码/许可证ZIP、作者输入、规格、冻结验收、模板快照、开发包、导入及幂等回执。`PACKAGE_CHECKS.json`记录全部制品和下载摘要；`INTEGRATION_RESULTS.json`记录十份实际下载、验收字节和案例一致性。正式案例API额外增加只读fixed_reference/templates元数据，除这两项外逐字段一致；开发包包含原规范记录，不用另写摘要替代。

## 代表应用

| 应用 | 源码与来源包 | 实际结果 |
|---|---|---|
| [一周晚餐](http://127.0.0.1:5277/) | [源码](../../../examples/meal-plan-trial/source-package.zip) · [说明](../../../examples/meal-plan-trial/README.md) · [来源包](meal-plan/atlas-development-package.zip) | 两天2/4人：900g番茄、6个鸡蛋；改人数600g/4个；暂停300g/2个、恢复还原；周隔离；刷新及同目录换进程重启相等。 |
| [聚餐投票](http://127.0.0.1:5278/) | [源码](../../../examples/dinner-poll-trial/source-package.zip) · [说明](../../../examples/dinner-poll-trial/README.md) · [来源包](dinner-poll/atlas-development-package.zip) | 1/1平票总2；同代号改票0/2仍2；关闭禁投、重开保留；第三人后1/2总3；刷新及同目录换进程重启相等。 |

每个CONSUMPTION记录包SHA、阅读文件SHA及消费早于实现时间。两应用各自A01–A04均直接执行冻结HTTP旅程并真重启，另有11+10单测通过。最终源码ZIP经共用工具打包，在临时目录独立解压、核对全部源码SHA和真实A04，通过见`FINAL_SOURCE_CHECKS.json`。无用户数据库。没有冻结runner.json适配器，不能冒称工厂独立容器runner通过。

两个试用地址当前运行，仓库根目录启动命令：

```sh
python3 examples/meal-plan-trial/app/serve.py --port 5277 --data-dir examples/meal-plan-trial/data
python3 examples/dinner-poll-trial/app/serve.py --port 5278 --data-dir examples/dinner-poll-trial/data
```

每个代表目录的BROWSER_RESULTS、逐步页面文本及截图保留五组操作；完整重启前后状态及不同PID见`REPRESENTATIVE_RESTART.json`。Atlas中实际完成检索“聚餐”、阅读产品定义、回查同一共享案例、创建标准包和点击下载，UI检查包另存，不替换开发时的来源包。

## 收尾、验证与返工

- Vite 7.3.6→7.3.7，保持high审计阈值：high0/critical0，moderate2保留未强制降级。原CI39547271157失败及跳过步骤留证；修复提交fb3887b64ca5d9db81e208de1dbe20592ed18ca2对应CI39549472878全部success，前端类型检查、单测、构建、常规及工厂E2E实际完成，见closeout/remote-ci.json。
- export_trial增加acceptance/相对路径和原始字节摘要比较。旧回执从原冻结ZIP恢复比较，排除宿主生成plan.json；增删/重命名/内容变化均拒绝复用，要求新版本或输出；四项回归通过，历史不重写。
- E2E的API/页面端口改为可配置以隔离生产。首次常规与工厂E2E并行发生test-results清理冲突，初次失败保留；随后串行常规17/17、工厂27/27，本地类型检查、单测9/9、构建也通过。
- 实际复用package_app发现目标ZIP位于应用内时可能将上次ZIP/自身回执打入，已做目标排除；新增回归通过。与导出回归合计5项。
- 大纲/时间块首次输入使用documentation_claim，但CaseLibrary只接受documentation；修正枚举后保留原场景续跑成功。failure-first-attempt与RESOLUTION并存，当前manifest不残留旧错误。未覆盖旧冻结文件，没有模型重试。
- 初筛BookWyrm许可证有使用者限制，保留排除说明，未入库；改用GPL3 Calibre-Web固定版本。
- 不同仓库许可证路径由作者显式license_path输入支持。聚餐初版来源表license_url仍沿用旧LICENSE默认；真实COPYING/SPDX及文件摘要保存在共享案例和来源ZIP。后续可修订此展示链接，不改本轮冻结字节。
- 案例一致性现场核验最初把API增加的fixed_reference/templates显示元数据当作记录差异；定位后明确核验这两个扩展字段，规范记录其他字段及包内JSON全部一致。未修改案例或模板去匹配检查。

## 重跑与保护

十项整批完成后又实际重复：同case/r1/制品ID、冻结ZIP均复用；全库案例修订17未增长。`REPEAT_BEFORE.json`和`FINAL_STATE.json`保留预算、grant、job、batch及G1门禁表摘要一致证据，原四库字节不变。原32份跟踪ZIP与此前提交完全一致，见PREEXISTING_ARCHIVES；六个应用健康检查通过。

新增受控OpenCode调用0；原工厂86+历史连通测试1=87/500，业务修复8/8，活动调用0。严格G1仍blocked，T08未启动，未重置或改变记录。日常Codex推理与两个开发上下文不冒称OpenCode CLI会话；未取得token/成本数据不编造。

统一重跑入口：

```sh
python3 examples/assisted-trials/produce_batch.py --manifest docs/template-factory/assisted-batch-10-2026-10-21/MANIFEST.json
```

可加`--item <key>`。研究选型、具体场景、规范/验收编写仍由Codex介入；脚本负责正式服务持久化、已有冻结/导出/导入和幂等核对。两个新开发上下文只消费各自包实现应用；主上下文负责实际浏览器/交付。修改冻结输入需新版本/新输出。八份未运行模板后续须消费包开发和实测，文件整理应先用练习沙箱完成安全专项，不直接操作珍贵原文件。

最终10/10模板登记、2/2代表应用核心可用，无未解决生产失败；首次输入及环境问题真实保留。所有限制/后置范围在各AUTHOR_INPUT、TRIAL_SCOPE和报告中可查。
