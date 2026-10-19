# 阶段与验收

## P0 · 核心闭环：保存 → 归类 → 找回 → 打开

普通用户能在浏览器中主动保存外部网页链接，指定或新建简单归类，按归类浏览与关键字检索找回记录，并从记录打开真实原网页；数据在服务进程重启后仍然存在。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 把一个合法 http/https URL 保存到指定已有归类后，库列表出现该记录，且标题、URL 与所属归类与提交值一致。 | acceptance/p0.py |
| A02 | negative | 提交空 URL、非 http(s) 协议（javascript:、data:）或畸形 URL 时被拒绝并返回可见错误，库中记录数保持不变。 | acceptance/p0.py |
| A03 | positive | 保存时未选择归类，记录进入默认收件箱，并可在默认收件箱视图中浏览到。 | acceptance/p0.py |
| A04 | positive | 新建归类后该归类出现在归类侧栏，且可将记录保存或移动到该新归类。 | acceptance/p0.py |
| A05 | positive | 把记录从归类 A 移动到归类 B 后，记录出现在 B 的浏览结果，且不再出现在 A。 | acceptance/p0.py |
| A06 | positive | 按归类浏览只返回该归类的记录，不会串入其他归类的记录。 | acceptance/p0.py |
| A07 | positive | 关键字检索命中标题、URL 或备注中匹配的记录，并排除不匹配的记录。 | acceptance/p0.py |
| A08 | positive | 访问记录的开原页入口返回指向所存 URL 的 http(s) 跳转（3xx Location 或含真实原始链接的页面），且不代理或返回目标网页正文。 | acceptance/p0.py |
| A09 | positive | 保存记录后，一个全新无会话的 HTTP 客户端仍能通过浏览或检索读回该记录，表明数据已由服务端持久保存；进程重启后的数据仍在由独立浏览器验收覆盖，本套件不重启服务、不直接读取应用数据库，也不得声称已完成进程重启。 | acceptance/p0.py |
| A10 | negative | 无匹配关键字的检索返回空结果集而不误报；未暴露的公开或分享类路由返回 404 且不泄露库内容。 | acceptance/p0.py |

## P1 · 整理与维护

用户能编辑记录、删除并恢复、避免重复、按时间/归类/关键字筛选排序，并用子归类与标签重塑组织结构。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A11 | positive | 编辑记录标题与备注后，列表与详情显示新值且更改持久保留。 | acceptance/p1.py |
| A12 | positive | 删除记录后移入回收站、从常规浏览与检索排除；从回收站恢复后重新可见。 | acceptance/p1.py |
| A13 | negative | 已删除记录不出现在浏览与检索；对不存在或已删除 id 的编辑、移动与恢复请求返回 404 且库状态不变。 | acceptance/p1.py |
| A14 | negative | 再次保存同一 URL 不产生第二条记录，且原记录被更新而非复制。 | acceptance/p1.py |
| A15 | positive | 列表默认按加入时间倒序；按归类与关键字筛选返回正确子集与顺序。 | acceptance/p1.py |
| A16 | positive | 在父归类下新建子归类后，可在父与子层级浏览并把记录移动到子归类。 | acceptance/p1.py |
| A17 | positive | 重命名归类生效；删除归类时其记录回退到默认收件箱而不被级联删除。 | acceptance/p1.py |
| A18 | positive | 为记录添加与移除标签，并按标签浏览或检索出对应记录。 | acceptance/p1.py |

## P2 · 互操作与可选增强

用户能导入与导出 Netscape 书签 HTML 完成迁移与轻量备份，并在显式开启时使用元数据抓取、失效链接清单、可选存档与 bookmarklet 捕获入口。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A19 | positive | 导出整个库为 Netscape 书签 HTML，解析后包含归类结构与记录的 URL 与标题。 | acceptance/p2.py |
| A20 | positive | 从 Netscape 书签 HTML 导入时文件夹映射为归类，并保留 URL、标题与添加日期。 | acceptance/p2.py |
| A21 | negative | 导入畸形、空或超过大小上限的文件被明确拒绝并给出错误，库内容保持不变。 | acceptance/p2.py |
| A22 | negative | 元数据抓取默认关闭，保存不触发外发请求；即使启用，指向私网或回环地址的抓取也被拒绝为安全错误。 | acceptance/p2.py |
| A23 | positive | 在无外网环境下失效链接检查明确报告为 unavailable 或未验证，不伪报全部正常，也不改动记录本身。 | acceptance/p2.py |
| A24 | negative | 在未配置存档能力时请求网页副本，返回明确的未实现或不可用，而不是伪造或空的存档内容。 | acceptance/p2.py |
| A25 | positive | 预填捕获入口 GET /?add=1&url=&title= 返回带预填值的真实保存表单，供 bookmarklet 或扩展调用。 | acceptance/p2.py |
