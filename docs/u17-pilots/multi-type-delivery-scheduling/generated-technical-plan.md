# M5 案例三 · 客户项目交付与个人排程 — 技术方案

## 1. 架构概览

本方案定义三类系统之间的集成架构，核心原则为主记录归属明确、跨系统引用通过稳定 ID 映射、状态交接为单向触发。

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Approval        │     │  Agile PM        │     │  Calendar        │
│  Workflow        │────▶│  System          │────▶│  Application     │
│                  │     │                  │     │                  │
│ 主记录：审批请求 │     │ 主记录：工作项   │     │ 主记录：日历事件 │
│ 审计轨迹         │     │ backlog、看板    │     │ 时间锚点         │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                         ┌─────────────────┐
                         │  Cross-System    │
                         │  Mapping Table   │
                         │  (关联表)         │
                         └─────────────────┘
```

## 2. 数据架构

### 2.1 关联表（Cross-System Mapping）

用于记录跨系统 ID 映射：

```sql
CREATE TABLE cross_system_mapping (
    id              UUID PRIMARY KEY,
    source_system   VARCHAR(32) NOT NULL,  -- 'approval' | 'agile_pm' | 'calendar'
    source_id       VARCHAR(256) NOT NULL,  -- 对应系统的实体 ID
    target_system   VARCHAR(32) NOT NULL,
    target_id       VARCHAR(256) NOT NULL,
    relation_type   VARCHAR(32) NOT NULL,  -- 'triggers' | 'references' | 'schedules'
    created_at      TIMESTAMP NOT NULL,
    created_by      VARCHAR(128) NOT NULL,
    status          VARCHAR(16) DEFAULT 'active',  -- 'active' | 'superseded'
    
    CONSTRAINT uq_mapping UNIQUE (source_system, source_id, target_system, target_id)
);
```

**约束**：
- 每个数据实体有且仅有一个系统记录归属
- 跨系统引用使用稳定 ID 链接，不复制主记录
- ID 映射记录不可物理删除，仅通过 status 标记废弃

### 2.2 各系统 ID 体系

| 系统 | ID 类型 | 生成方式 | 特征 |
|---|---|---|---|
| 审批工作流 | 请求 ID | 系统生成 UUID | 唯一标识审批请求完整生命周期 |
| 敏捷 PM | 工作项 key | 项目前缀 + 序号（如 PROJ-123） | 标识一个工作项 |
| 日历 | 事件 UID | 日历服务生成 | 标识事件及其重复规则 |

---

## 3. 集成接口设计

### 3.1 审批到项目：单向 Handoff

**触发条件**：审批决定（approve/reject/return/withdraw）

**流程**：
1. 审批系统记录决定
2. 审批系统发布事件到内部事件总线
3. 集成服务接收事件，查询关联表获取目标工作项 ID
4. 集成服务调用敏捷 PM API 更新工作项状态
5. 集成服务在关联表中记录交接事件
6. 两个系统的审计轨迹分别记录该交接

**API 接口**：

```http
POST /api/v1/handoff/approval-to-project
Content-Type: application/json

{
  "approval_request_id": "req-uuid",
  "decision": "approved",  // approved | rejected | returned | withdrawn
  "decision_comment": "...",
  "approver_id": "user-uuid",
  "decision_timestamp": "2026-01-01T00:00:00Z"
}
```

**响应**：
```json
{
  "handoff_id": "handoff-uuid",
  "target_work_item": "PROJ-123",
  "status": "completed",
  "audit_trail_ref": {
    "approval_system": "audit-entry-uuid",
    "project_system": "work-item-history-id"
  }
}
```

### 3.2 项目到日历：只读时间块引用

**触发条件**：Sprint 开始/结束、里程碑日期变更

**流程**：
1. 敏捷 PM 系统检测到 Sprint 或里程碑时间变更
2. 集成服务查询关联表获取关联的日历事件 UID
3. 集成服务调用日历 API 更新只读时间块（或创建新引用）
4. 用户可在日历中查看、隐藏或删除该时间块

**约束**：
- 日历事件由用户管理，系统仅创建引用
- 不自动创建可编辑的日历事件
- 用户可选择隐藏项目相关时间块

### 3.3 关联表 CRUD 接口

```http
POST   /api/v1/mappings          # 创建映射
GET    /api/v1/mappings          # 查询映射（支持 source/target 过滤）
GET    /api/v1/mappings/{id}     # 获取单个映射
PUT    /api/v1/mappings/{id}     # 更新映射状态
DELETE /api/v1/mappings/{id}     # 软删除（status→superseded）
```

---

## 4. 审计架构

### 4.1 审计事件格式

```json
{
  "event_id": "uuid",
  "event_type": "handoff.completed | handoff.failed | mapping.created | ...",
  "source_system": "approval | agile_pm | calendar",
  "actor": "user-uuid",
  "timestamp": "ISO-8601",
  "payload": { ... },
  "correlation_id": "用于跨系统追踪的关联 ID"
}
```

### 4.2 审计存储

- 各系统保留本系统的审计轨迹
- 跨系统审计通过 correlation_id 关联
- 关联表本身的变更（创建、废弃）也记录审计事件
- 审计日志不可修改、不可删除

---

## 5. 权限架构

### 5.1 各系统独立鉴权

- 审批工作流：基于 Requester/Approver/Admin 角色
- 敏捷 PM：基于 Team member/Planner/Team lead 角色
- 日历：基于 Owner/Delegate/Invitee 权限层级

### 5.2 跨系统权限隔离

- 集成服务以系统身份（service account）执行跨系统操作
- 系统身份仅拥有执行 handoff 所需的最小权限
- 人工跨系统操作需要显式权限提升审批
- 所有权限变更记录审计日志

### 5.3 服务账户权限矩阵

| 操作 | 审批系统权限 | 项目系统权限 | 日历权限 |
|---|---|---|---|
| 读取审批决定 | Read | - | - |
| 更新工作项状态 | - | Write | - |
| 创建/更新日历引用 | - | Read | Write |
| 读取关联表 | Read | Read | Read |

---

## 6. 失败恢复技术方案

### 6.1 审批停滞恢复

- 基于 SLA 计时器检测审批请求超时
- 自动发送提醒通知给当前审批者
- 超过升级阈值时自动转派给上级审批者
- 所有提醒和升级事件记录审计日志

### 6.2 工作项阻塞恢复

- 看板上 Blocked 状态超过阈值时标记告警
- 团队 standup 时协调解除阻塞
- 阻塞事件记录在工作项历史中

### 6.3 跨系统交接失败恢复

- 交接失败时保留原始事件和目标状态
- 通过通知告警相关角色
- 提供手动重新触发接口
- 失败事件记录审计日志，包含失败原因

```http
POST /api/v1/handoff/retry/{handoff_id}
```

### 6.4 日历同步失败恢复

- 只读引用更新失败时记录告警
- 提供手动重新同步接口
- 用户也可直接在日历中手动编辑

---

## 7. 部署与扩展

### 7.1 首期范围

- 三类系统的核心集成 API
- 关联表服务
- 审批到项目的单向 handoff
- 项目到日历的只读引用
- 基础审计日志

### 7.2 后续扩展点

- 双向状态同步（需用户决策后实现）
- 日历事件自动创建（需用户决策后实现）
- 客户认证与计费集成
- 资源级自动排程
