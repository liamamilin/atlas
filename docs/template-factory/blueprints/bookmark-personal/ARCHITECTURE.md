# 架构、数据与契约

## 默认架构与边界

单人静态 Web：UI → 领域校验/查询 → IndexedDB 仓储。无需服务器数据库、账号、支付或云 API。此为 D01/D02 的可调整默认，不是品类硬约束。纯本地并不等于加密保管或云备份：同一来源内脚本可访问数据，浏览器清理和来源/端口变化可能使库不可见。P1 导出负责可带走；不承诺跨设备同步。

## 数据模型

Bookmark = {id: UUID, title: 非空字符串, url: 校验后的绝对 HTTP(S) URL, category: 非空字符串, createdAt: ISO8601, updatedAt: ISO8601, deletedAt: null | ISO8601}。P0 deletedAt 始终 null；P1 启用回收站。分类从有效记录派生或持久存储，添加新分类必须可选且修改原记录 id。搜索在 title/url/category 上做大小写无关包含匹配，再与选定 category 取交集。

## 仓储契约（本地 API，不是假设的 HTTP 服务）

list({query,category,includeDeleted}) → Bookmark[]；save({id?,title,url,category}) → Bookmark（完成持久事务后 resolve）；trash(id)/restore(id) → Bookmark；exportAll() → {format:'atlas-bookmarks/1',records:Bookmark[]}；importAddOnly(payload) → {added,conflicts}；bulkMove(ids,category) → Bookmark[]。未找到 id 报 not_found；非法 URL/内容报 validation；存储打开失败报 storage_unavailable；事务失败报 storage_write。UI 不要求暴露全局 JS 测试后门。

所有写操作错误均要保留原数据和用户输入，事务完成后才能重绘成功状态。save 快速重复提交期间锁定操作，不能新建两条。读取失败不当作空库覆盖。P1 导入先验证整个 payload（格式版本、字段、URL、重复 id），再在一个写事务中新增；同 id 的本地值保持，报告冲突。P2 批量移动也必须单事务。

## UI 适配契约

一个可提交 form（novalidate 并自行提供可访问错误）；有准确标签“标题”“链接地址”“分类”；保存按钮“保存书签”，编辑时仍可提交；输入“搜索书签”，select“筛选分类”，空值表示全部。每条记录为 article，标题为 heading，显示分类文本及“编辑”按钮，链接 accessible name 为“打开原网页”，href 为记录 URL，target=_blank，rel 含 noopener。默认分类“收件箱”。有 role=status 显示已保存/已更新，有 role=alert 显示校验/存储错误，空搜索结果显示“没有匹配的书签”。正常就绪后按钮可用；异步保存期间可以禁用。页面初始数据读取完成后再允许保存；打开或读取失败时必须禁用保存，明确提示恢复存储后重载，避免把读取失败当成空库覆盖。

P1：article 的“删除”软删除，工具栏“回收站”切换与“全部书签”返回，回收站 article 有“恢复”；“导出全部书签”触发 JSON 下载；file input 标签“导入备份”，按钮“确认导入”，反馈 added/conflicts 数量，中文格式“新增 N，冲突 M”。未知版本或非法数据用 alert 表示。P2：“查找重复链接”通过 role=status 报告列出重复 URL 与各记录标题，且不删数据；article checkbox 名“选择 <标题>”，输入“批量分类”，按钮“应用分类”。

这些名称是样板验收适配协议，不是所有项目的不可变产品文案。已有项目可实现等价适配器并记录映射，不能把行为断言删除来适配。


## 验收适用范围

当前 acceptance/run.cjs 针对 D02 默认 IndexedDB 的故障注入；换用其他仓储时必须实现等价故障适配器，不能直接套用 A06/A07/A16 并声称覆盖。A01 用独立临时浏览器 profile，覆盖关页重开及关闭浏览器后使用同一 profile 重启。P0 各用例记录外部请求尝试，只有 A04 明确点击原链接允许一次目标导航；预览服务阻止外网，CSP 阻止的尝试也会失败。该检查覆盖测试操作与末尾短观察窗，不承诺证明任意延时或全部网络侧信道。
