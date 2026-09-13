# 技术方案：Application Atlas 项目创建与切换入口

## 后端

在 EP-S1 增加按 `updated_at DESC, id` 稳定排序的 `list_projects()`。在 EP-S2 增加：

- `GET /api/projects`：返回项目摘要列表。
- `POST /api/projects`：校验 JSON 字段后调用 ProjectStore。
- `GET /api/projects/<prj_id>`：读取单个项目；不存在返回 404。

ProjectStore 路径继续由 `ATLAS_PROJECT_STORE` 覆盖，默认值保持独立于语料数据库。Handler 只把已知的 `ValueError` 和 `ProjectStoreError` 转换为 4xx；未知异常仍作为服务错误暴露到日志，不吞掉。

## 前端

在 EP-S3 定义 `AtlasProject`、列表/创建/读取请求。创建入口先以可移动组件实现，避免在 EP-U1 解决前把布局耦合进搜索页。当前项目 ID 保存在本地 UI 状态；每次使用前由服务重新读取，满足 EP-R3。

## 一致性与边界

- EP-R1、EP-R2 使用同一个项目库，创建后立即可列出。
- EP-R3 通过请求中的项目 ID 和 ProjectStore 外键边界继续扩展。
- EP-R4 的失败请求必须在事务外校验或由事务回滚。
- EP-R5、EP-U2 不在本次 API 中加入伪目录选择能力。

项目 API 不触碰 `atlas/atlas.sqlite`，不改变现有 `/api/sources` 和 `/api/drafts` 行为。
