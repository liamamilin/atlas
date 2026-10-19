# 阶段与验收

## P0 · 个人收藏箱核心旅程

用户可保存链接（可选归类或落入未整理）、按归类或关键字找回、打开原页、清理并撤销，且全部数据跨会话与重启保留，非法输入得到可恢复的明确错误。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 保存一条链接后，同进程与重启后的新进程都能读到该记录，且 id 与内容稳定。 | acceptance/p0_library.py |
| A02 | negative | 保存表单与 JSON 均接受绝对可解析的 http/https URL（含单标签主机，如 http://localhost）并保留原始字符串；缺协议、非 http/https、空/非法 hostname 被拒绝为 400 invalid_url，且库中不新增记录。 | acceptance/p0_library.py |
| A03 | positive | 不选归类保存时记录落入“未整理”，保存时给出的新归类名被自动创建，首启可见预置归类。 | acceptance/p0_library.py |
| A04 | positive | 通过真实归类页表单完成新建、重命名、删除：重名、非法名与默认归类保护给出可读 form-error 且不改数据；删除归类后活动与软删除记录都迁回“未整理”，软删记录仍可恢复。 新建与重命名各自通过 HTML 和 JSON 验证 name 省略、空字符串、纯空白和 121 字符（JSON 另测 null）均为 400 invalid_name；保留全部重名、保护、迁移与恢复断言。 | acceptance/p0_organize.py |
| A05 | positive | 在给定的 base_url 目标把记录从“未整理”移动到另一归类，并用独立实例证明该归属跨重启仍然有效。 | acceptance/p0_organize.py |
| A06 | positive | 通过真实归类页/记录表单浏览与计数：侧栏与接口的 count 只计活动记录，并在移动、软删除、恢复后与实际列表和 JSON 保持一致。 | acceptance/p0_organize.py |
| A07 | positive | 从真实归类页提交 category 与 q：页面保留所选归类与查询并显示匹配/明确空结果；同一关键字在两个归类分别命中各自记录，且 JSON 检索仍覆盖标题、域名与描述、大小写不敏感。 | acceptance/p0_find_open.py |
| A08 | positive | 打开记录跳转到保存时的原始 URL（302 Location 等于保存值），未知 id 返回 404。 | acceptance/p0_find_open.py |
| A09 | positive | 通过真实记录表单软删除并恢复：默认视图排除、回收站可见、恢复后字段与归类回归；删除归类时软删记录迁回“未整理”仍可恢复，且删除状态跨重启保持。 | acceptance/p0_recovery.py |
| A10 | negative | 未知 id 与畸形 JSON 返回结构化错误（bad_request/not_found）且不产生 5xx、不改变数据；真实表单的非法 URL 显示可读 form-error、保留输入，并在修正后成功保存。 | acceptance/p0_recovery.py |
| A11 | positive | 健康检查返回就绪，首页外壳在空库下渲染录入表单与列表容器，入口不报错。 | acceptance/p0_library.py |
| A12 | negative | 仅验证书签保存与移动的非法归类：HTML 保存使用归类名 category，HTML 移动使用归类 ID category_id；JSON 保存/移动使用归类名 category。非法归类 400 invalid_category，HTML 显示可读 form-error 并保留提交值，JSON 返回结构化错误；归类集合、记录集合与被移动记录归属均不变。保存省略 category（JSON 另含 null）进入未整理，不作为非法值；移动省略值/JSON null、显式空值/纯空白/超长归类名，以及 HTML 移动空/未知 category_id 为非法。有效新归类名保存或 JSON 移动时自动创建，不把未知 ID 当作名称。分类创建/重命名 name 的 invalid_name 分支仅属 A04。 | acceptance/p0_organize.py |

## P1 · 成熟增强：元数据、互操作与库清理

在离线可用的前提下增强记录可辨识度（本地派生图标、外部抓取仅作增强），并支持浏览器书签格式的导入导出与重复链接检测，用于长期库维护。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A13 | positive | 外部网络不可用时保存仍然成功，图标与标题降级为本地派生结果，缺失增强不阻塞或报错。 | acceptance/p1_maturity.py |
| A14 | positive | 导出为浏览器书签 HTML 可包含已存记录，且导入该 HTML 后相应记录可再次检索到。 | acceptance/p1_maturity.py |
| A15 | negative | 重复 URL 默认被拒绝（409 duplicate_url）且库不变；显式允许重复时可新增第二条。 | acceptance/p1_maturity.py |
