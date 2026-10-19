# 阶段与验收

## P0 · 单目录预览式批量重命名与撤销（完整核心旅程）

用户能在一个明确指定的本地根目录上：list 立即普通文件 → 用非空字面查找/替换生成并持久化旧名到新名计划（不改动原文件）→ 经整批冲突预检 → 显式 --confirm 执行并取得逐条回执 → 查看当前文件名 → 显式 --confirm 撤销本次执行并核对文件名与内容恢复；全过程在冲突、陈旧计划、重复执行与撤销冲突时安全拒绝，绝不覆盖、不假成功、不越出根目录。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 对指定根目录运行 list，stdout 为单一 JSON 对象 {files:[{name,size}]}，仅含立即普通文件，排除子目录、符号链接与 .atlas-renamer 状态目录；退出码 0。 | acceptance/run.py |
| A02 | positive | preview --find --replace --plan 生成计划 JSON（含逐条 old→new 与原始身份证据）写入根目录 .atlas-renamer 内，stdout 返回 {status:"preview",operations,plan}；预览后原文件字节内容与文件名完全未变。 | acceptance/run.py |
| A03 | negative | 非法输入被显式拒绝并非零退出且无任何改动：空查找文本、替换串含路径分隔符或经 .. 的目录穿越、新名解析后不是单个文件名。 | acceptance/run.py |
| A04 | negative | 整批冲突预检：目标已存在、两个源指向同一新名、或新名落在源集合内（含 a↔b 环）时整体拒绝并非零退出，且拒绝后无任何文件被改名。 | acceptance/run.py |
| A05 | positive | apply --plan --confirm 执行整批改名，stdout 为 {status:"applied",operations,receipt}；磁盘上文件名与新名一致、内容不改，未选文件不受影响，回执文件可被后续进程读取。 | acceptance/run.py |
| A06 | negative | apply 不带 --confirm 时拒绝并非零退出，文件名与内容均无变化。 | acceptance/run.py |
| A07 | negative | 对同一已应用计划再次 apply，不产生第二轮改名：返回显式 already-applied 或非零拒绝；磁盘文件名保持不变。 | acceptance/run.py |
| A08 | negative | 预览与执行之间源文件内容或身份被改动时，apply 判定计划陈旧并拒绝，非零退出且无部分改名；回执不误报成功。 | acceptance/run.py |
| A09 | positive | undo --receipt --confirm 恢复本批次全部旧名，stdout 为 {status:"undone"}；恢复后文件名与内容均与执行前一致，且不影响未参与批次的文件。 | acceptance/run.py |
| A10 | negative | 撤销安全：undo 不带 --confirm 时拒绝；撤销时若旧名已被新文件占用或数据被改动，则拒绝且不覆盖、不删除现有数据，非零退出。 | acceptance/run.py |
| A11 | negative | 状态路径边界：plan/receipt 指向根目录 .atlas-renamer 之外（或经外部符号链接指向外部的状态文件）时被拒绝，应用不在根目录之外写入或改名。 | acceptance/run.py |
| A12 | negative | 失败安全与真实报错：任一步失败时非零退出并在 stderr 说明错误、stdout 不产生假成功 JSON；失败后既有文件与内容不丢失（不覆盖、不删源）。 | acceptance/run.py |
