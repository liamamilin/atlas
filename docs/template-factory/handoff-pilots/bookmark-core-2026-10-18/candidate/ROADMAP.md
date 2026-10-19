# 阶段与验收

## P0 · 核心收藏闭环

用户能保存外部链接（仅 URL 必填）、选择或新建简单归类、把未归类记录移动到位、按分类浏览或关键字找到记录、打开原页，且数据在真实进程重启后仍在。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 仅填写 URL 即可保存成功；记录未经选择时进入未分类并立即出现，缺省标题回退为 URL。 | acceptance/p0-save-classify.cjs |
| A02 | positive | 保存带标题与备注的记录成功；重新加载后标题与备注完整可见，未被改写或丢失。 | acceptance/p0-save-classify.cjs |
| A03 | positive | 保存时选择一个已存在分类，记录出现在该分类浏览结果中。 | acceptance/p0-save-classify.cjs |
| A04 | positive | 保存时新建分类并把记录归入；重新加载后新分类与归属关系保持。 | acceptance/p0-save-classify.cjs |
| A05 | positive | 把记录从一个分类移动到另一个分类；重新加载后其归属已更新且不再出现在原分类。 | acceptance/p0-find-open.cjs |
| A06 | positive | 分类浏览只显示该分类记录，且默认按添加时间倒序（新在前）。 | acceptance/p0-find-open.cjs |
| A07 | positive | 关键字检索能命中标题、URL、备注或分类名中的匹配记录，且不返回无关记录。 | acceptance/p0-find-open.cjs |
| A08 | negative | 空库状态与检索无匹配状态呈现彼此不同的提示，二者不被混为一谈。 | acceptance/p0-find-open.cjs |
| A09 | positive | 点击记录在新标签页打开原始 URL，且原 URL 的 query 与 fragment 均被保留；测试环境拦截该外部请求以避免真实外连，仅断言被尝试打开的 URL 与新标签行为。 | acceptance/p0-find-open.cjs |
| A10 | positive | 数据写入 --data-dir；经真实进程重启后，先前保存的记录与分类仍可经 UI 读回。默认由操作员执行 before/after 步骤；若由用例自身安全持有应用进程，则仅重启该自有进程并断言 PID 变化。刷新不得被当作重启，文件存在或新建 SQLite 连接不得作为证明。 | acceptance/p0-persistence.cjs |
| A11 | negative | 保存已存在的相同 URL 时出现显式“已存在”提示，用户可显式选择继续保存为另一条记录；不发生静默拒绝或静默重复。 | acceptance/p0-save-classify.cjs |
| A12 | negative | 在同一保存表单上快速双击提交，只产生一条记录（重复提交不导致两条）。 | acceptance/p0-save-classify.cjs |
| A13 | negative | 提交超过声明上限的备注时显式报错且不落库；不出现备注被静默截断后保存的情况。 | acceptance/p0-save-classify.cjs |
| A14 | negative | 提交无效 URL 或非 http(s) 协议地址时显式报错且不落库。 | acceptance/p0-save-classify.cjs |
| A15 | positive | 保存失败后表单保留用户已输入内容，用户修正后重试可成功保存。 | acceptance/p0-save-classify.cjs |
| A16 | positive | 含中文与 emoji 的标题与备注保存、显示与检索均正确，无乱码或字符丢失。 | acceptance/p0-save-classify.cjs |
| A17 | negative | 应用仅绑定回环地址；除用户显式点击“打开原页”外，P0 流程不发起任何后台外发请求（无元数据抓取、无遥测）；测试环境阻止对外部地址的真实连接；若配置认证参数则仅作用于显式指定的目标且不记录凭据值，不支持的模式显式失败。 | acceptance/p0-find-open.cjs |
