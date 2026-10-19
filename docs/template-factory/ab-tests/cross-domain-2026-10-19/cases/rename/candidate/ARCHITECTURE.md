# 架构与契约

## 默认技术栈与理由
默认：Python 3 标准库单进程 CLI（argparse、os、json、pathlib/stat，内容哈希可选 hashlib），入口 `python3 app.py --root DIR COMMAND ...`。理由：运行时已确认为 Python 标准库、无依赖安装、无网络、无 shell/子进程（CONTRACT、GUIDANCE）；改名是同文件系统内的元数据操作，标准库 os.rename/os.replace、os.lstat/os.stat、os.listdir/scandir 足以完成 list/preview/apply/undo。替代方案：Go/Rust 类工具（F2/brename/RnR）能力强但需额外安装，且以模式/正则驱动、支持递归、作用域更大，与『字面替换、单目录、非递归、拒绝冲突、显式 --confirm、幂等』不一致（S06-S09），故只借用其设计模式（默认预览、冲突整体拒绝、journal 撤销、明确退出码），不复用代码；util-linux rename 默认『没有任何保护』（S06），不作为默认。

## 数据模型
- 目标根 DIR：仅操作其内部立即普通文件；不递归、不处理目录与符号链接。
- 状态目录 DIR/.atlas-renamer/：存放不可变计划与执行回执；list 排除该目录。
- 计划 JSON（多行可读、创建后不改写）：{version,created_at,find,replace,root,operations:[{old,new,identity:{dev,ino,size,mtime_ns,可选sha256}}]}。
- 回执 JSON：本批次每步旧名/新名与身份证据、时间戳、applied 标记，供后续进程 undo 与重复 apply 检测。

## 命令 / 错误 / 状态契约
- stdout 仅输出 JSON；中文帮助/错误走 stderr；操作失败必须非零退出且不得输出假成功。
- list -> {files:[{name,size}]}；排除目录、符号链接与内部 .atlas-renamer。
- preview --find TEXT --replace TEXT --plan PATH -> {status:"preview",operations:[{old,new}],plan:PATH}；PATH 必须位于状态目录内；不改动原文件。
- apply --plan PATH --confirm -> {status:"applied",operations:[{old,new}],receipt:PATH}；缺 --confirm 拒绝；执行前整批冲突预检；已应用计划与陈旧计划被拒绝。
- undo --receipt PATH --confirm -> {status:"undone"}；缺 --confirm 拒绝；遇新冲突或数据被改动时拒绝且不破坏。
- 退出码：0 表示成功；非零 + stderr 错误信息表示拒绝或失败。
- 路径安全：plan/receipt 解析后必须位于 DIR/.atlas-renamer 内，拒绝 ..、绝对路径逃逸与经外部符号链接的写入；错误分类借 PEP 3151 子类（FileExistsError/PermissionError/IsADirectoryError/NotADirectoryError，S04），不解析 errno。

## 测试用适配契约（UI/CLI）
acceptance/run.py 不导入应用代码，而是以 shell=False 子进程调用 `python3 <app.py> --root <fixture_root> COMMAND ...`，仅用 Python 标准库；夹具目录由 run.py 在一次性临时目录内自行创建与清理，绝不使用真实 HOME/Downloads 或应用源码目录；按各命令解析 stdout 的单一 JSON 对象，结合退出码判定成功或拒绝。不提供任何测试专用端点，只通过公开 CLI 契约观察用户可见行为。

## 非功能需求
- 失败安全：绝不覆盖既有目标；失败后旧数据不丢失（POSIX 同文件系统改名原子，S03/S05）。
- 幂等与防过期：计划携带原始身份证据，重复 apply 与陈旧源均被拒绝。
- 可观测：逐条 operations 回执 + plan/receipt 文件，作为轻量审计替代。
- 作用域限定：非递归、不处理目录/符号链接、不越出根目录。
- 无网络、无依赖安装、应用自身无 shell/子进程调用。
