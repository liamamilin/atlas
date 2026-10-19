# 阶段与验收

## P0 · 个人收藏箱核心旅程

用户可保存链接（可选归类或落入未整理）、按归类或关键字找回、打开原页、清理并撤销，且全部数据跨会话与重启保留，非法输入得到可恢复的明确错误。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 保存一条链接后，同进程与重启后的新进程都能读到该记录，且 id 与内容稳定。 | acceptance/p0_library.py |
| A02 | negative | 缺协议、非 http/https、无点域名的 URL 被拒绝并返回结构化错误，且库中不新增记录。 | acceptance/p0_library.py |
| A03 | positive | 不选归类保存时记录落入“未整理”，保存时给出的新归类名被自动创建，首启可见预置归类。 | acceptance/p0_library.py |
| A04 | positive | 可新建、重命名、删除归类；重名被拒；删除归类后其记录回到“未整理”。 | acceptance/p0_organize.py |
| A05 | positive | 在给定的 base_url 目标把记录从“未整理”移动到另一归类，并用独立实例证明该归属跨重启仍然有效。 | acceptance/p0_organize.py |
| A06 | positive | 按归类浏览只返回该归类记录，侧栏/接口给出的条目计数与实际一致。 | acceptance/p0_organize.py |
| A07 | positive | 关键字检索匹配标题、域名与描述，可与归类叠加，无匹配时返回空集而非错误。 | acceptance/p0_find_open.py |
| A08 | positive | 打开记录跳转到保存时的原始 URL（302 Location 等于保存值），未知 id 返回 404。 | acceptance/p0_find_open.py |
| A09 | positive | 在给定的 base_url 目标删除记录后默认视图排除它、撤销恢复后记录内容重新可见，并用独立实例证明删除跨重启保持。 | acceptance/p0_recovery.py |
| A10 | negative | 未知 id 与畸形请求返回结构化错误码，且不产生 5xx、不改变现有数据。 | acceptance/p0_recovery.py |
| A11 | positive | 健康检查返回就绪，首页外壳在空库下渲染录入表单与列表容器，入口不报错。 | acceptance/p0_library.py |
| A12 | negative | 保存或移动到空名/超长名的非法归类时返回 400 invalid_category，且现有归类与记录不变。 | acceptance/p0_organize.py |

## P1 · 成熟增强：元数据、互操作与库清理

在离线可用的前提下增强记录可辨识度（本地派生图标、外部抓取仅作增强），并支持浏览器书签格式的导入导出与重复链接检测，用于长期库维护。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A13 | positive | 外部网络不可用时保存仍然成功，图标与标题降级为本地派生结果，缺失增强不阻塞或报错。 | acceptance/p1_maturity.py |
| A14 | positive | 导出为浏览器书签 HTML 可包含已存记录，且导入该 HTML 后相应记录可再次检索到。 | acceptance/p1_maturity.py |
| A15 | negative | 重复 URL 默认被拒绝（409 duplicate_url）且库不变；显式允许重复时可新增第二条。 | acceptance/p1_maturity.py |
