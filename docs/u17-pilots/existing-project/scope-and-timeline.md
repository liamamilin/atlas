# 范围与时间记录

状态：首轮实现、Atlas 迭代和独立验收完成；案例二已封存，待 Git 提交决定。

## 固定边界

- 案例目标：提升本地清单 CLI 的持久化可靠性，保持 `add`、`list`、`done` 兼容。
- 允许修改：`todo.py`、`test_todo.py`。
- 明确排除：新增命令、图形界面、多人协作、云同步、数据库迁移、改变任务字段语义。
- 当前基线：`python3 -m unittest -v` 通过 6 项。
- 源工作区：`application-atlas-production-pack/projects/workspaces/prj_fdee487646e84eb08793d6304ff13f60`。
- Atlas 分析项目：`prj_e6d8d97b6761428ab94c1cf1ff7a4419`。
- 改进后快照：`snap_3cf6a251ce664e27b023be423bdeda45`，内容指纹 `f76e35ac8b0709cd47755db63a6bd9cb17305d22c0646d0f665ea8cb0daafef1`。

## 已确认的首轮范围

1. `save_tasks` 使用同目录临时文件和原子替换；替换失败时原有 `tasks.json` 保持不变，临时文件清理。
2. `load_tasks` 遇到损坏 JSON 时输出包含路径和原因的 stderr，返回非零退出；不静默当作空列表，不覆盖原文件。
3. 正常 `add`、`list`、`done` 的输出、退出码和 `{id, title, done}` 字段保持兼容。
4. 增加损坏读取、写入失败旧文件不变、临时文件清理的回归测试，原有 6 项测试继续通过。

Atlas 建议的“损坏后自动返回空列表”与冻结的 EP2-R2 冲突，暂不采用。是否自动生成 `.corrupt` 备份属于实现细节，只有在不改变错误退出和原文件保护的前提下才可采用。

## 时间线

| 事件 | 时间（UTC） | 说明 |
|---|---|---|
| 协议冻结 | 2026-09-20 | 固定项目、文件指纹、目标、允许路径和验收命令 |
| 普通对照完成 | 2026-09-20T05:37:13Z | OpenCode `ses_f42af8fbdffe8UjignBY9I6618`，原始输出已封存 |
| Atlas 项目与参考创建 | 2026-09-20 | 项目 `prj_e6d8d97b6761428ab94c1cf1ff7a4419`，参考 `ref_aabf1594c9c044a29c9fe197db43e6d5` |
| 接受基线 | 2026-09-20T05:41:56Z | `snap_a49ae939134642dcaa5905900a38a5bf`，工作区干净 |
| Atlas 首轮运行 | 2026-09-20T05:45:25Z | `gen_08fd77daf9674c03abb9080f8f7315d7`，输出引用格式错误，校验失败 |
| Atlas 重试完成 | 2026-09-20T05:49:45Z | `gen_d68ed51ca06b4c50bb16ed5c1fd64ba7`，只读 current-state 分析完成 |
| 实现开始 | 2026-09-20 | 在案例工作区只修改 `todo.py`、`test_todo.py`，未扩大范围 |
| 实现验收 | 2026-09-20 | 10 项单元测试通过，手工 add → list → done → list 通过 |
| 基线复核 | 2026-09-20 | 旧基线中的 `tasks.json` 为测试运行产物；复核后采集新快照，代码范围仍只有两个允许路径 |
| Atlas 迭代完成 | 2026-09-20 | `itr_1c6a6a26621e42799ab801706029cb0e` 完成；任务 `tsk_feb708bba5894584bdce5ecee6194fb8` 验收通过 |

## 尚未观察

- 真正断电或进程 SIGKILL 未做破坏性测试；使用临时文件替换和模拟 `os.replace` 失败验证等价安全边界。
- 用户对错误文案和 `.corrupt` 备份偏好的观察尚未收集。
