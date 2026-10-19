# U17 本地安全审查记录

日期：2026-09-25  
范围：本地单用户 Application Atlas；T025–T027/T031 收口后的本地代码与发布边界  
结论：**本地威胁模型和代码边界审查通过；这不是 OS/容器沙箱证明，也不替代远程 CI、签名/公证或目标平台验收。**

## 1. 审查范围

本次审查覆盖：

- loopback API 的 Host、Origin、Fetch Metadata、JSON body 和请求大小边界；
- OpenCode V1/V2 权限策略、runtime project root、provider 产物路径和固定验证器；
- execution workspace 的 baseline、复制、symlink、apply journal 和显式恢复；
- backup/restore 的归档校验、opaque restore target、restore journal、删除和中断清理；
- provider/执行证据的脱敏、用户源码排除和凭据读取边界；
- GitHub Actions、本地回归和发布文档中可能出现的过度安全声明。

不在本次范围内：多用户认证、云端服务、远程 provider 托管、完整容器/虚拟机隔离、macOS 签名和公证。

## 2. 威胁模型

| 资产/边界 | 已有控制 | 证据 | 剩余风险与结论 |
| --- | --- | --- | --- |
| 本地 API 与浏览器 | 仅 loopback；校验 Host、Origin、Fetch Metadata、Content-Type、Content-Length；写请求需要 JSON | `drafts_api.py` request boundary tests；路由回归 | 同一 macOS 用户下的恶意进程和浏览器扩展仍可能读取本地用户文件；保持本地单用户边界，不宣称强认证 |
| 用户源码工作区 | accepted baseline/hash-bound 复制；拒绝绝对路径、symlink 越界和未声明结果；apply 前 journal；恢复拒绝替换后的内容 | `execution_workspace.py`；workspace/apply crash fixtures | 注册验证器、项目测试代码和同用户恶意进程仍可能主动访问外部路径；固定验证器不是 OS/容器沙箱 |
| OpenCode 执行权限 | V1/V2 Atlas-owned policy；默认拒绝 shell、web、external directory、MCP、subagent、skill、Code Mode；一次性权限请求 | `opencode_permissions.py`、CLI/HTTP permission tests | provider、全局配置、插件和验证器本身仍是高权限边界；不能把 permission policy 描述为进程隔离 |
| Generation 产物 | disposable Git project root；V2 `.opencode/opencode.json`；edit 仅允许 `result.json`；源码树新增/修改/删除 fail closed | T026 tests；真实 `opencode-go/deepseek-v4.1-flash` smoke | 这是路径和变更检测门禁，不是防止同用户恶意进程写入的 OS 沙箱 |
| Backup/restore | schema/hash 校验；只恢复新空库；opaque `restore_id`；restore root 不与源码重叠；journal/fingerprint 恢复；删除和中断清理需固定确认令牌 | T025/T031 API、backend、E2E | 仍需目标平台上的备份介质、磁盘故障和签名发布验证；不自动 prune |
| 凭据和证据 | provider 凭据从本地认证存储惰性读取；日志/导出/备份脱敏；不把 key 写入报告或配置 | T027 classification error tests；脱敏回归 | 脱敏不能证明任意模型输出没有敏感信息；凭据一旦泄露仍需 provider 侧撤销/轮换 |

## 3. 人工审查发现

### 已关闭或可接受的风险

1. **源码树 provider 污染**：T026 真实 generation 曾暴露 `result.json` 落入仓库路径；现在通过显式 project root、V2 配置位置、精确 edit policy 和运行前后树快照阻断，越界证据写入 Atlas-owned violation 文件，不自动删除用户文件。
2. **浏览器 restore 越界**：浏览器只发送 opaque `restore_id` 和固定确认令牌；任意 `target_store`、symlink、已有目标库和与源码工作区重叠的 restore root 均拒绝。
3. **危险清理**：backup 删除和中断 restore 清理都要求明确确认；只删除归档或 journal 记录且指纹未变化的 Atlas 产物，不删除项目数据库或用户源码。
4. **分类 provider 误用**：T027 真实记录 `qwen3.8-flash` 成功和 `opencode-go/deepseek-v4.1-flash` `model_unavailable`；失败不自动 fallback，不将分类结果升级为需求或入库。
5. **秘密泄漏**：本地凭据扫描未发现未允许的 key/token/secret 格式；扫描统计为 `opencode_key=0`、`sk_key=0`、`secret_json_value=0`，Bearer 命中为已知测试脱敏夹具。该扫描不是通用秘密检测器，也不扫描 SQLite/二进制压缩内容。

### 明确的 release blocker

- 尚未在远程 GitHub Actions 上复验同一发布 SHA；
- 尚未在目标 macOS 环境完成签名、公证、启动、升级和回滚；
- 未在独立进程/容器/虚拟机中验证恶意项目测试代码的隔离；
- 未完成目标平台的完整人工安全审查和发布签字。

这些限制不能被 loopback、文件权限、权限策略、固定验证器或本地复制目录替代。

## 4. 本次验证

- `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`：219 passed；
- T025–T027/T031 相关 backend contract、symlink、journal、分类 provider 和 backup 生命周期测试通过；
- frontend `npm run typecheck`、7 项 unit、build 和 backup E2E 通过；
- 关键 Python 路径 Ruff、compile 和 `git diff --check` 通过；
- 真实 generation containment smoke：provider 产物 `artifact_root=runtime`，仓库无新增 provider artifact；
- 真实 classification smoke：`qwen3.8-flash` 成功；v4.1 model unavailable 失败路径安全返回。

## 5. 发布前解除条件

1. 在目标发布 SHA 上完成远程 CI，并保存可复核日志和 artifact checksum。
2. 在目标 macOS 机器完成签名、公证、启动、升级、回滚和 restore 验证。
3. 若要宣称更强隔离，提供独立容器/进程/虚拟机测试证据；否则继续使用本文件中的明确非目标表述。
4. 由目标环境维护者复核凭据轮换、日志保留、备份保留和用户源码责任边界。
5. 在上述条件满足前，不写入 `PROJECT_ACCEPTED`，不自动 commit、push、发布或执行远程高影响操作。

## 6. 审查结论

Atlas 当前可以作为**本地单用户、受控证据和显式恢复边界清晰**的开发工具继续使用；它不能被描述为多用户服务、强认证系统或完整 OS/容器隔离环境。T029 的本地审查完成，外部 release blocker 继续由 `BLOCKERS.md` 和发布检查清单管理。
