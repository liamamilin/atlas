# OpenCode Go 模型切换与最小实测

日期：2026-10-19；OpenCode CLI v2.0.30。按用户要求切换到 OpenCode Go，并按后续更正用 Beam Free 替代 Cat Jam Free。

项目的 `application-atlas-production-pack/opencode.json` 默认模型改为 `opencode-go/deepseek-v4.1-flash`。工厂页面初始化时优先选这个确实出现在 CLI 目录的模型，其次 LongCat；用户手动选择优先，不会被轮询覆盖。两个目录都不可用时保留既有的 DeepSeek Flash 回退逻辑。用户全局 provider、密钥、历史批次、冻结模板和旧实验模型记录不改。

| 模型 | 完整标识 | 实际调用 | CLI 记录秒数 |
| --- | --- | --- | ---: |
| LongCat 2.5 Preview Free | `opencode-go/longcat-2.5-preview-free` | 通过 | 15.67 |
| Beam Free | `opencode-go/beam-free` | 通过 | 3.91 |
| DeepSeek V4.1 Flash | `opencode-go/deepseek-v4.1-flash` | 通过，项目默认 | 8.97 |

三项都是新的独立 CLI 会话，通过实际工厂 CLI 适配器，发送脚本内的简短合成 JSON，核对固定 schema、记录数和非法 scheme 的判断字段。不发送 Atlas 叶子、模板、应用源码或凭据作为任务输入；阶段只读，禁用联网、执行和写文件。宿主保存原始日志、响应和摘要。不是应用行为、安全或模型质量评测，也没有重跑书签端到端流程。

最初 Cat Jam 调用已开始时用户更正为 Beam。保留该原始结果：`opencode-go/cat-jam-free` 返回 `provider.no-route / Model unavailable`，没有算作成功；随后只补测 Beam，没有重复运行已通过的另两个模型。CLI 的 `cli_status=completed` 只描述进程完成；本记录以有效模型响应和宿主校验结果判断调用通过。

结果见 [results.json](results.json)，目录见 [catalog.json](catalog.json)。`probe.py --model 完整标识` 可单独试调用；不带参数会真实调用三个模型，可能消耗 provider 配额。重复运行会更新汇总，应使用新证据目录保留不同轮次。

工厂页面刷新后默认 Go DeepSeek；要换用其余模型，在“OpenCode 模型（provider/model）”填入表中完整标识。每个新批次固定所选模型，不改写已启动任务。

官方当前 [Go 文档](https://opencode.ai/v2/docs/console/go/) 列出 LongCat、Beam 及 DeepSeek。免费标识和可用性会变，应以调用时目录及实际响应为准；本轮秒数仅为一次短请求记录，不作吞吐、长期费用或生产质量结论。

配置变更通过前端 TypeScript 检查与 `git diff --check`。
