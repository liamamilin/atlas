# 固定 v0.1.8 规范：补当前 UI 主流程的语义断言

同一已授权书签认知生产/必要修复/独立审阅范围。完整规范、调研、25/9/33 的身份/阶段/默认值全部不变，reuse_spec=true。只改 acceptance/ui-p0.cjs、acceptance/ui-p1.cjs、acceptance/ui-p2.cjs、acceptance/README.md，其余16文件字节复用。不研究、不安装、不执行任何生成程序/浏览器/重启适配器/下游应用，不发布。阶段仍 not implemented，用例 not_run。

最新完整静态报告七项通过，仅阶段验收阻断；同址重存、混合状态删除、错误归类引用、表单安全与正确子路径均已修好。本轮只关闭排序/归类的真实用户交互验证与空态说明分歧，不追逐全部可选负例、企业功能、P3 或新案例。先读真实文件与 browser/support/common 导出，用小范围精确替换/补充，不整文件重写，不删除原断言，不伪造请求响应，不加固定等待代替行为检查。

## ui-p2.cjs / A33

保留 q/categoryId/sort/limit、真实 next/prev、交集/并集/无重复/offset与刷新保持的全部断言，新增：

- 在首页真实使用现有 browser.setSort（先读其签名；它已支持自动提交及 sort-submit 回退），通过可见 sort-form 控件将 created_desc 改为 created_asc，等待真实导航/请求；原 URL 中 q/categoryId/limit 保留，offset 归零，sort-select 与 URL 是 created_asc。不能只 goto 一个带 sort 的 URL 冒充用户修改。
- 根据明确的排序契约（createdAt 升序，时间相同时十进制 id 升序）或已经由独立 API 排序用例验证的真实 API created_asc 结果，逐项比较页面 rowIds。不能仅断言下拉值或 URL，也不能把集合排序后比较，必须验证 DOM 中实际顺序。
- 真实翻到下一页再返回前一页，每页按其 offset/limit 与独立排序结果切片比较，保留原本所有筛选、并集/无重复和查询参数断言。测试本 run 夹具，不能假设全库空；若页面有其它 run 记录，使用原既定隔离筛选或按实际 API 全集比较，而不是删除其它记录。

## ui-p0.cjs / A28

保留真实保存、外部本地夹具打开、原始 URL/创建时间、默认归类、重复冲突与显式另存等既有断言。P0 不调用 P1/P2 接口或 q/filter/sort 参数。在默认 created_desc 的真实分页处，对每页 DOM 书签 id 顺序与基础 API 的默认 created_desc/offset/limit 结果逐项比较，或对属于本 run 的记录按 createdAt DESC、id DESC 计算期望；不能只检查集合无重复/并集。保留现有子路径、sort/limit/offset URL、首末页与真实导航断言，不能假设当前首页只有本 run 记录。

## ui-p1.cjs / A29

保留移动、保存归类、编辑、重命名、软删除/恢复等既有程序范围。A29 将记录移到 emptyId 的既有分支后，从首页真正点击该 id 的 category-link（核对现有选择器与 basePath href），真实进入 /c/{emptyId}；不要用 goto 或 API 替代该次点击。断言页面有对应 bookmark-item 的 id、标题、data-category-id，并保留 API 旁路、刷新持久与后续重命名检查。归类页不保证首页 bookmark-form，别重新引入等待错误表单的旧缺陷。

这个非空页面沿用 §8 的通用 bookmark-item/title/category 约定，符合既有 F14 归类浏览，不新增路由、角色或功能。不要顺手增加未知/tombstone页面、所有Host读路由、HTML转义等报告中的可选扩展。本轮不动已正确的公共 helper、路由拼接或任何 API 程序。

## acceptance/README.md：空态是承诺，手工检查不是功能后置

原 §14/§15 将空库、空回收站说成“手工、非发布硬要求”，容易与 current required F04/F11 及架构空态承诺混淆。只修正说明：这两项仍是当前阶段应交付的体验；自动套件不为了造空态清空现有数据，必须在全新、专用、无个人数据实例做人工观察，并单独记录目标版本/实际操作/结果/截图或日志。未执行就记未完成，不能仅凭自动套件通过宣称阶段完整验收。这里不引入新发布流程或修改生产制品等级，也不把功能改为 later。

明确操作：全新空库检查 data-empty-kind=library，空回收站检查 data-empty-kind=trash；不得为核对而清空用户现有库。当前两项都未运行，未有证据；A01–A33 也未运行。原 README 的所有安全开关、重启、认证、正确子路径示例与非授权声明保留。只补上述当前用户闭环，不扩大到 P3、可选负例或批量运行。

停止：严格保持固定规范与所有案例身份，四个指定文件，其余字节复用；冻结后另做独立完整静态审阅及 node --check。任何“未运行”不能冒充通过，人工核对原审阅中不成立的推断也不能改写原模型报告。
