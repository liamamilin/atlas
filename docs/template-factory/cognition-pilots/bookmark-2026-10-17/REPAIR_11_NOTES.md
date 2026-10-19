# 固定 v0.1.7 规范，只补必要验收及路径说明

这是同一已授权书签认知生产/必要修复/独立审阅范围。reuse_spec=true：完整规范、调研、角色/能力/决策/阶段/案例身份和既有默认值不变；不研究、不安装、不执行任何生成程序/应用/浏览器/重启适配器、不发布。仅改 acceptance/p1-trash.cjs、acceptance/p1-categories.cjs、acceptance/README.md；其它 17 个程序逐字复用。各阶段 not implemented、案例 not_run。已有 25/9/33 结构不变。

v0.1.7 完整独立审阅七项通过，阶段验收阻断。核对后，两条覆盖缺口成立；路径推断不成立，原报告必须保持，不把误报当成程序故障。也顺便修正 A17 的一个确定夹具/契约分歧。不要追逐旧报告中所有可选 UI/Host 建议，不新增验收身份或功能。使用小范围精确替换/追加，先读真实 support/common 的导出和现有断言，不重写整个程序。

## 一、p1-trash.cjs：软删除后重新保存同址

在 A16 中加独立、自包含分支，不改变原恢复路径/断言：

1. 用本 run 独立 URL 创建书签，立即 tracker.bookmark，软删除；读回旧回收项并保存真实基线。不要重用已经恢复为 active 的原分支记录，也不依赖 A18 的全局清空。
2. 对同一原始 URL 再 POST 保存，不传 allowDuplicate（或明确 false），必须 201 且新十进制字符串 id 与原 id 不同；登记新 id。新记录活跃，旧项仍在回收站，旧的 url/title/note/createdAt/trashedAt/来源字段不变；active 比软删除后基线 +1，trashed 不变，总数 +1，归类 bookmarkCount 只增加这条活跃记录。不要假设全库空或回收条目为0。
3. 对该 URL 再普通 POST，必须409 duplicate_url，details.existingId 指向刚创建的新活跃项，不是旧回收项；读回确认新旧均保持，失败零写入。原 P0/HTML 显式 allowDuplicate 已有用例，保留即可，不为此改 UI 文件。

### A17 的明确夹具修正

现有 `const ghostId = 'ghost-' + uniqueName('category')` 是非法形状，却强制 reason=unknown_or_deleted。固定规范只对形状合法、引用不存在/已删的归类给该 reason。因此把此处“引用失效”夹具改成真实快照最大 category.id 的 BigInt + 1000000n，再转十进制字符串；确认不在活跃快照中，沿用 unknown_or_deleted 断言。已 tombstone ID 的第二负例保留。可保留原非数字形状作为额外 invalid_category/400 负例，但不得要求未定义的 reason。API 与错误码不改，不修改其它文件中已经正确的十进制 ghost ID。

## 二、p1-categories.cjs：同一归类 active+trashed 混合删除

现有 A14 的 priorGroup 与 groupPurge 分属两个归类，不能证明同一归类里混合状态的正确行为。保留现有全部分支，在 A14 追加两个独立夹具（move 与 purge 不能共用已 tombstone 的源）：

- 每个源归类准备两条活跃记录和一条已经软删除的记录；记录都登记 tracker，软删除后从真实回收站取旧项快照。另建活跃目标供 move，不能动其它 run 的记录。
- move：mode=move 到该目标，moved=2、trashed=0；只有两条活跃记录转目标，源归类 tombstone，源旧回收项仍回收，categoryId 和 trashedFromCategoryId/name、trashedAt/updatedAt/url/title/note/createdAt 不变。categoryDeleted 从 false 变 true 是源 tombstone 的正常派生变化，不把它错当“不变字段”；categoryName 仍为源名。读回目标计数 +2，active/trashed/total 全部守恒。
- purge：独立源归类 mode=purge&confirm=true，moved=0、trashed=2；两条活跃项新进回收站、来源字段指向该源，原回收项的来源、trashedAt、updatedAt 与正文不被覆盖；categoryDeleted 变 true，仍是该源名称。active 比操作前 -2，trashed +2，总数不变；源从活跃归类消失，三条都能在回收站按 id 找到。
- 此处 confirm=true 仅为归类 purge（软删除），绝不是全局回收站清空；不得新增全局 DELETE /api/trash。所有比较使用 seeding/软删除后的真实基线。保留原默认归类保护、非法/失效目标、独立夹具、来源字段和其它先前回收项检查。

## 三、验收 README：澄清实际路径约定，不能照误报改代码

架构已明确所有应用页面与 API 都挂在 PUBLIC_BASE_PATH 下。业务保存路由本身是 `/bookmarks`，并不是部署前缀。common.request 的参数是相对应用根的业务路径，实际 resolveTarget 为 `new URL(ctx.baseUrl + path)`；不能换成 `new URL(path, ctx.baseUrl)` 丢掉子路径，也不能把业务子路由缩成 `/{id}/move`。

给出简短对照表和原生拼接示例（只写说明，不运行生成程序）：

| --base-url（部署根） | request 业务路径 | 目标 pathname |
| --- | --- | --- |
| http://127.0.0.1:3000 | /bookmarks | /bookmarks |
| http://127.0.0.1:3000/app | /bookmarks/42/move | /app/bookmarks/42/move |
| http://127.0.0.1:3000/bookmarks | /bookmarks/42/move | /bookmarks/bookmarks/42/move |

最后一行是部署前缀与业务资源名相同，两个 bookmarks 分别有作用，属于正确路径。API 同理，例如 /bookmarks/api/bookmarks。这不是放宽安全边界：common 仍校验配置 origin、无 userinfo、basePath 段边界与 redirect manual；原坏头矩阵只发往已配置目标，p0-limits/p1-edit 本轮不能改。保留所有已有 CLI、重启、破坏性开关、浏览器认证限制与真实证据说明。

验收 README 简要补充两个新增 API 回归的归属与未运行状态；不声称规范或程序已执行通过。只改这三个指定文件，固定作者规范全部原值。冻结后另开完整独立审阅；原审阅中的路径推断与其它可选建议仍留在历史中，不改写旧结论。
