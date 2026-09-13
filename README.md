# Application Atlas

软件应用类型资料库及本地工作台。当前正式语料包含 1,805 个类型、29 个大域、270 个目录节点及 33 个产品实例。

- `application-atlas-production-pack/applications/`：正式英文档案，内容真相源。
- `application-atlas-production-pack/research/`：对应的研究笔记及边界依据。
- `application-atlas-production-pack/DIRECTORY.md`：分类目录。
- `application-atlas-production-pack/atlas/*.jsonl`：持久化翻译记录，纳入版本管理。
- `atlas-web/`：React + TypeScript + Vite 前端。
- `application-atlas-production-pack/drafts_api.py`：本地草稿 API（127.0.0.1:5199）。

## 启动

需要 Python 3.10+、Node.js 22，以及安装了 bge-m3 的 Ollama（向量检索时需要）。Python 依赖版本来自已验证的本地环境。

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd atlas-web
npm ci
npm run gen
npm run dev
```

另一终端在项目根目录启动草稿服务：

```sh
source .venv/bin/activate
python3 application-atlas-production-pack/drafts_api.py
```

打开 http://localhost:5188 。现有 macOS 启动器在 `apps/`，其中路径仍对应此电脑的工作区。

初次克隆不包含派生数据库和网页数据，先运行：

```sh
python3 application-atlas-production-pack/export_atlas.py
ollama pull bge-m3
python3 application-atlas-production-pack/embed_leaves.py
cd atlas-web
npm run gen
```

导出会载入已保存的翻译。已有数据库中的向量仅在输入内容未变时保留；新增或修改的类型由 `embed_leaves.py` 补齐。导出遇到目录缺失、重复或孤立正文会失败，并保留旧数据库。

## 模型与凭据

阅读网页、导出、离线测试不需要模型凭据。语义检索需要本地 Ollama；分类、查重及翻译会使用外部模型 API。凭据按需从 `ATLAS_API_KEY` 环境变量读取，未设置时读取本机 OpenCode 的 `~/.local/share/opencode/auth.json`。不要把凭据提交到仓库。

分类模型通过 `ATLAS_ADJUDICATOR` 配置，默认 `qwen3.8-flash`；查重默认 `mimo-v2.5`。草稿生成还需要 OpenCode CLI。

## 入库规则

1. 生成或编辑完整草稿并通过结构检查，新增类型必须有研究笔记。
2. 对当前正文执行查重。正文、身份、研究笔记或正式数据库变更后，旧裁决失效。
3. `new` 裁决才可新增；`same/variant` 只能合并到裁决指定的类型。
4. 入库在临时语料副本中执行导出、翻译、向量补齐、网页生成及固定样本回归。
5. 固定回归达到 90%、没有请求错误，且数据完整后才更新正式语料。失败保留原始草稿和正式数据。

一次只允许一个语料更新任务。数据库最后通过原子替换切换，分类器自动重新加载；草稿 ID 保持稳定，成功后提供正式类型链接。发布过程有回滚记录；若进程中断，重启 API 或再次导出会恢复未完成的切换。不要在更新过程中用其他脚本绕过锁直接写数据库。

中文译文是已有翻译资产，部分历史翻译在生成时已截短；此次修复不会凭空补齐译文。详情页保留完整英文各章节、来源及完整原始档案，供核对。

## 验证

不访问模型、不产生 API 费用：

```sh
python3 -m unittest discover -s application-atlas-production-pack/tests -v
python3 application-atlas-production-pack/gate_check.py --score-only application-atlas-production-pack/atlas/gate_regression.json
cd atlas-web
npm run typecheck
npm run build
```

`--score-only` 只重算现有结果，未达标返回非零。现有结果原始准确率为 44/52（84.6%），纳入路线图已明确接受的三个替代标签后为 46/52（88.5%）；这不是本轮修改后的在线分类成绩。

运行 `python3 application-atlas-production-pack/gate_check.py` 会重新调用分类 API，生成 `gate_regression.json` 和 `gate_summary.json`。正式入库必须执行本次临时库上的新回归，不接受旧报告替代。

CI 执行离线行为测试、类型检查和构建；仓库尚未配置远程地址，工作流待推送后才会实际运行。纯静态构建只提供阅读功能，草稿页面需要本地 API 配合。
