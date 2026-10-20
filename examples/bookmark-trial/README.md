# 留存 · 个人收藏夹（辅助试用版）

Python 3.10+，零第三方依赖；无需安装包或修改源码。仅供单人本机使用。

```sh
python3 app/serve.py --port 5273 --demo
```

在本目录执行，然后打开 **http://127.0.0.1:5273/**。在 Atlas 仓库根目录则执行：

```sh
python3 examples/bookmark-trial/app/serve.py --port 5273 --demo
```

按 Ctrl+C 停止；再次执行同一命令即可继续使用原数据。`--demo` 仅在新数据库首次初始化时加入两条标有“[演示]”的示例，不会在重启时重复添加。

使用方法：

1. 在“保存一个链接”填完整的 HTTP(S) URL，可选标题与描述，点击“保存收藏”。
2. 分类框可选现有名称或直接输入新名称；也可到“管理分类”创建、重命名或删除。列表中选择新分类并点“移动”。
3. 搜索标题、域名或描述，可与分类筛选叠加；关键词不匹配时显示空结果。
4. 点击收藏标题，在新标签打开原始链接。移入回收站后仍可恢复；删除分类只把记录迁回“未整理”。

数据默认保存在本应用 `data/bookmarks.sqlite3`，与 Atlas 正式业务库完全分开。可通过 `--data-dir /绝对路径` 改位置；重启时务必使用同一目录。备份时先停止应用，再复制整个 data 目录。源码包不包含个人数据库。

已知缺口：无账户/云同步/公网部署；不抓取正文或元数据；未实现 P1 导入导出和去重。完整错误矩阵、并发压力和严格 P0 独立认证未作为本轮结论。不要把本机无认证应用暴露公网。

本应用是 Codex 直接消费 R8 本地标准开发包后实现的辅助试用，不是正式工厂队列产物。来源和范围见 `SOURCE.json`、`TRIAL_SCOPE.md`，真实浏览器七旅程记录见仓库 `docs/template-factory/bookmark-assisted-trial-2026-10-20/TRIAL_REPORT.md`。

针对性回归（与真实浏览器记录分开）：

```sh
python3 -m unittest discover -s tests -v
```

需要重新导出来源包时，在完整 Atlas 仓库执行 `python3 examples/bookmark-trial/export_trial.py --destination /新的输出目录`。导出脚本依赖 Atlas 宿主模块；独立应用的运行、演示数据与测试不依赖它。
