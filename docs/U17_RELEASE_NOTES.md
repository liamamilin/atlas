# U17 发布候选说明

日期：2026-09-22  
分支：`codex/stabilize-atlas`

## 本候选版本交付什么

- 从首页、搜索或类型树进入类型叶子，并从类型叶子创建项目或加入当前项目。
- 项目工作台按“理解项目 → 确定范围 → 冻结计划 → 执行与验收”组织资料、需求、决定、文档、迭代和任务。
- 当前迭代的阻塞项与可选建议分开显示；已完成迭代显示完成，不会被历史建议误导为仍有阻塞。
- OpenCode 作为首个执行后端，在隔离工作副本中执行任务；Atlas 保存基线、权限、差异、验证、应用和验收证据。
- 首页提供新想法、已有项目改进和 Agent Harness 调研三条案例入口；教程提供首次使用的完整路径。
- 案例入口直接说明适用场景和预期产出；尚未建立迭代的新项目工作台提供固定资料、确认范围、冻结计划三步起步提示。
- 活动迭代在页面顶部显示 OpenCode/provider 执行准备状态；未配置或失败时提供执行区和教程入口，已完成项目不会被该提示打扰。
- 失败、停止、超时、应用冲突、验收失败和清理失败均保留记录，并提供继续或安全结束动作。

## 启动

手动启动前端和 API：

```sh
cd atlas-web
npm ci
npm run dev -- --host 127.0.0.1 --port 5188

# 另一终端，在仓库根目录
python3 application-atlas-production-pack/drafts_api.py --port 5199
```

打开 <http://127.0.0.1:5188/>。也可以使用 `apps/Atlas.app` 或 `apps/atlas-launch.sh` 启动本地服务。

## 发布前验证

```sh
cd atlas-web
npm run typecheck
npm run build -- --emptyOutDir false

cd ../application-atlas-production-pack
python3 -m unittest discover -s tests -p 'test_*.py'
node --check projects/workspaces/prj_e6299aa777e645b4a8c9157a31364e0c/static/app.js

cd ..
git diff --check
```

2026-09-22 的候选验证结果：前端类型检查、生产构建、后端 132 项回归、静态脚本检查、API 健康检查和核心浏览器路径全部通过。构建仍会提示主 JS chunk 约 686 kB；当前没有加载失败，代码分包列为后续性能工作。

## 当前限制

- OpenCode 是当前唯一已接入的执行后端；Atlas 已保存自己的状态和证据，但多 provider、云端执行和自研通用 harness 不在本候选范围。
- 首版不提供自动回滚、运行中接管、多任务并行、团队治理、账号和自动发布；应用后的回退由项目自己的 Git 或备份策略负责。
- 本版本面向本地单用户运行；OpenCode CLI、模型凭据和项目本地服务仍需用户按教程配置。
- 生产构建的 chunk 体积提示尚未处理，不影响当前功能门槛。

## 推荐后续顺序

1. 先收集真实用户从案例入口完成首次路径的反馈，修正文案和阻塞状态，而不是扩展功能面。
2. 根据 OpenCode 的实际使用记录决定 provider 抽象和兼容性策略。
3. 单独立项处理前端分包、性能预算和更完整的安装/诊断体验。
