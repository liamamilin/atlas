# v0.1.1 复审后的窄修订

保持同一已确认场景、调研和来源不变，不联网、不执行生成代码、不开发应用、不发布。冻结包与原报告保留。沿用 25 个 feature、9 个 decision、33 个 A01–A33 case 的 ID 与阶段归属；修订现有用例内容，不新增阶段/企业能力，不重写已正确程序。完整 file_plan 应列全 20 个文件，对兼容未变文件标 reuse=true；改动文件优先精确 replacements。不为可选打磨无限追加 release 要求。

1. ARCHITECTURE 与功能/决策统一：POST title 缺省/null/空串/纯空白均派生主机名标题；PATCH title=null 重新派生，空串/纯空白=400 invalid_title。POST categoryId 不存在或 tombstone=400 invalid_category，事务不写入。PATCH 空 body=400 empty_patch。SQLite 内部整数 ID 在 JSON 序列化为十进制字符串，客户端按 opaque string 使用；不得一处 number 一处 string。同步已有 A01/A03/A20/A29 相关断言与说明。P0 非法 categoryId 可使用保证不存在的字符串，不调用 P1 创建/删除分类接口。
2. 在已有 A14/A15 中增加真正影响数据完整性的负例：mode=move 指向已 tombstone 分类，按现有 target_unavailable 契约失败；mode=purge 携带 targetCategoryId，按 target_not_allowed 契约失败。保留现有准确 HTTP status，不任意改错码。断言源记录/分类状态与数量不变、无部分写入。A20 覆盖 POST tombstone categoryId；A29 覆盖 PATCH 空 body 无写入。以既有用例语义为准补足，不把 case 重新编号/换阶段。
3. 在现有 P0 用例补 URL 长度 2048 成功/2049 失败、真正无主机名 URL（如 https://）失败、POST 空白标题与字符串 ID 断言。不要把 WHATWG 能归一化的 http:///path 当无效 URL；边界夹具长度按完整 URL 算，不改产品上限迎合测试。已有用例中加入这些断言即可，不引入新 runner/framework。
4. 修 browser.cjs 的实际错误：context 的 baseURL 统一末尾斜线，内部导航按部署前缀解析；gotoHome/gotoCategory/gotoTrash 不能以根路径覆盖 /bookmarks 前缀。保持 helper 接口，既有 UI case 检查实际 pathname 保留 base URL 的路径前缀；在 acceptance README 说明以真实部署于 /bookmarks 的专用实例运行的命令。只写程序，不实际运行、不 mock target。
5. 可在已有 A28 的 P0 表单交互补空白标题派生、非法 URL 与重复 URL form-error，P1 现有 UI case 补空分类空态。不为测试空库清空真实用户数据；真实测试必须专用实例。不要扩大为穷举低风险组合。分类/移动的重新打开指刷新/新页面后从服务端读回；只有 A02 声明真实进程重启。保持这一可观察边界，不把所有流程重新扩成重启项目。
6. Atlas 主机已修复 CATEGORY 重复来源、历史原稿日期与访问日期的解释，以及 AGENT 的 proposed 决策/阶段/证据记录指引。你不应生成或修改这些保留文件。仅在 acceptance README 与架构中保持一致。原文来源不刷新，不伪造新访问日期或许可证。

本轮目标是修复复审指出的真正矛盾与高风险漏测，保留相同用户故事与可复用产物。所有 phase 仍 not implemented，case 仍 not_run；静态审阅通过不等于下游应用通过。
