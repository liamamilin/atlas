# M0：OpenCode CLI 环境预检与版本冒烟

**执行时间：** 2026-09-20 18:39（Asia/Shanghai）  
**执行方式：** Atlas 隔离工作副本中的只读预检与最小连通性冒烟；随后通过独立文档任务生成并应用兼容基线。  
**Atlas 任务：** `tsk_96fd82a42cef4cd8b1ba0c4f6270eb4c`  
**兼容基线任务：** `tsk_45f6ed0862924657872652b5d4ab2fe2`

## 结果

| 检查项 | 结果 |
|---|---|
| CLI 是否存在 | 通过：`/opt/homebrew/bin/opencode` |
| CLI 版本 | 通过：`1.18.31` |
| 包名与安装来源 | 通过：包名 `opencode`，Homebrew `anomalyco/tap/opencode` |
| 二进制类型 | 通过：Mach-O 64-bit executable arm64 |
| Provider 配置检查 | 通过：OpenCode Go、OpenAI、OpenCode Zen、commandcode；只记录名称和状态，不读取密钥值 |
| 最小模型连通性冒烟 | 通过：`opencode run --format json "echo hello" --dir /tmp`，exit 0 |
| Atlas 任务执行 | 通过：第二次执行完成，源工作区保持 0 条变化 |
| 兼容基线文件 | 通过：`.atlas/harness.json` 已生成并应用；`python3 -m json.tool .atlas/harness.json`，exit 0 |

## 判定

M0 **已通过**。OpenCode CLI、精确版本、Homebrew 安装来源、provider 配置状态和最小模型请求均有 Atlas 执行证据。`.atlas/harness.json` 已作为项目兼容基线写入工作区，最低兼容版本固定为 `1.18.31`，并已重新对齐迭代基线。

M0 的源工作区保护也已验证：只读预检执行没有修改源工作区；后续文档任务只在声明范围 `.atlas/harness.json` 内写入，应用后才更新项目基线。

## 已知说明

- `npm list -g opencode` 和 `npm info opencode version` 的警告不是失败：当前安装方式是 Homebrew，npm registry 中不存在同名包。
- Provider 凭证仍由 OpenCode 管理；Atlas 只记录 provider 名称和可用状态，不保存任何凭证值。
- `atlas harness.json` 中的冒烟时间已按实际执行时间校准，并通过 JSON 验证。

## 下一步

进入 M1 后已完成 CLI 适配层、显式 CLI 执行分支、启动前预检门、运行摘要映射、固定验证步骤和最小终端入口；后续扩展交互式 TUI 与取消路径。M1 必须读取 `.atlas/harness.json` 的精确兼容线，在版本不满足或 provider 不可用时阻止创建工作副本，并保留可识别的诊断证据。

本记录不包含任何凭证值，也没有读取或修改用户现有凭证文件。
