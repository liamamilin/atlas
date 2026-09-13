# Application Atlas — Writing Guide

## 0. Purpose

本 Guide 规定：

> Research 完成后，Agent 应如何把研究结果写成一篇高质量 Application Document。

它不规定研究方法。
研究方法见：

```text
WORKFLOW.md
```

本 Guide 只回答：

```text
最终文档应该写什么？
写到什么程度？
怎么组织？
什么叫清楚？
什么叫失败？
```

---

# 1. Writing Goal

Application Document 的目标不是：

- 写产品介绍
- 写营销文案
- 写技术架构
- 写数据库设计
- 写 Feature List
- 写行业百科
- 写厂商对比

它的目标是：

> 让一个从未使用过这种软件的人，读完后真正理解这种 Application 是什么、里面有哪些核心结构、用户如何使用、工作如何流动、重要状态和规则是什么，以及它和邻近 Application Type 有什么区别。

---

# 2. Core Writing Principle

始终围绕：

```text
What is it?
Who uses it?
What exists inside it?
What do users do?
How does work move?
What does the user see?
What can change?
What rules matter?
What is it not?
```

不要为了章节数量写内容。

不要为了完整性制造不存在的结构。

---

# 3. Recommended Document Skeleton

最终文档建议使用以下骨架：

```text
# <Application Type>

## Overview

## Users & Context

## Core Model

## How It Works

## Interfaces

## Important Rules / Behaviors

## Variants

## Related Application Types

## Representative Products

## Sources
```

这是默认骨架，不是机械模板。

允许根据 Application 类型增加、合并或弱化章节。

---

# 4. Overview

## Goal

用最短篇幅说明：

```text
它是什么？
它主要解决什么问题？
它的核心边界在哪里？
```

建议包含：

- Definition
- Primary Purpose
- Typical Context
- Canonical Boundary

## Good Example

> A Restaurant POS is an operator-facing transaction application used to create and manage food-and-beverage orders, apply restaurant-specific menu and service rules, collect payment, and close checks.

这句话已经告诉读者：

- 谁用：operator
- 核心动作：order + payment
- 特殊性：restaurant-specific rules
- 核心对象：checks

## Bad Example

> Restaurant POS software helps restaurants streamline operations, improve efficiency, and provide better customer experiences.

问题：

- 没说系统是什么
- 没说里面有什么
- 没说用户做什么
- 是营销语言

---

# 5. Users & Context

## Goal

说明：

```text
谁在使用？
为什么使用？
在什么工作环境下使用？
```

不要只列职位。

需要说明角色与 Application 的关系。

## Example

```text
Primary users:
- server: creates and modifies guest orders
- cashier: takes payment and closes transactions
- bartender: manages tabs and beverage orders

Secondary users:
- shift manager: handles overrides, voids and exceptions
- administrator: configures menu, permissions and settings
```

比：

```text
Users:
Server
Manager
Admin
```

更有价值。

## Rule

简单 Application 可以简写。

复杂 Application 应重点说明不同角色如何影响 workflow 和 permission。

---

# 6. Core Model

## This Is the Most Important Section

`Core Model` 是整篇文档的中心。

它回答：

> 这个 Application 的“世界”由什么组成？

不同 Application 可以有完全不同的模型。

## Examples

### CRM

```text
Lead
Contact
Account
Deal
Activity
Pipeline
```

### Video Editor

```text
Project
Media
Timeline
Track
Clip
Effect
Export
```

### Hotel PMS

```text
Guest
Reservation
Room
Stay
Folio
Room Status
```

### Team Messaging

```text
Workspace
Channel
Conversation
Message
Thread
Member
```

## What to Explain

不要只列名词。

应解释：

```text
对象是什么
对象为什么存在
对象之间如何关联
哪个对象是中心
哪个对象会推动 workflow
```

## Good Style

```text
A Deal represents a potential commercial outcome.
It is normally associated with one or more Contacts and an Account,
owned by a sales user, and placed in a Pipeline Stage.
```

这比：

```text
Deal: sales opportunity
```

好很多。

---

# 7. Use Diagrams When They Help

简单文本关系图非常适合：

```text
Lead
  ↓ qualify
Contact + Account
  ↓
Deal
  ↓
Pipeline Stages
  ↓
Won / Lost
```

或：

```text
Guest
  ↓
Reservation
  ↓ assigned to
Room
  ↓
Stay
  ↓
Folio / Payment
```

不要为了形式画复杂图。

图的目标只有一个：

> 让核心结构更容易理解。

---

# 8. How It Works

## Goal

解释：

> 用户真正如何使用这种 Application。

不要写成 Feature List。

应写：

- Core Workflow
- Interaction Loop
- Lifecycle
- Transaction Flow
- Editing Process
- Operational Flow

具体形式由 Application 决定。

## Example — Restaurant POS

```text
Select table
→ Create order
→ Add items
→ Apply modifiers
→ Send order
→ Take payment
→ Close check
```

## Example — Video Editor

```text
Create project
→ Import media
→ Arrange clips on timeline
→ Trim / edit
→ Add effects / audio
→ Preview
→ Export
```

## Example — IAM

可能不是单条 flow，而是多条：

```text
User provisioning
Authentication
Authorization
Access review
Deprovisioning
```

## Rule

优先解释最典型、最定义性的 workflow。

不要把每个按钮都写成流程。

---

# 9. Interfaces

## Goal

说明用户面对的主要操作表面。

根据 Application 自适应：

### GUI Application

可以写：

- List
- Detail
- Board
- Calendar
- Editor
- Dashboard
- Checkout
- Settings

### CLI Application

可以写：

- Commands
- Arguments
- Prompts
- Output
- Configuration

### IDE / Editor

可以写：

- Workspace
- Sidebar
- Editor
- Inspector
- Console
- Toolbar

### Monitoring System

可以写：

- Overview
- Resource Explorer
- Detail
- Metrics
- Events
- Alerts

## Page Description Minimum

每个重要界面最好回答：

```text
Purpose
Typical information
Primary actions
```

## Bad

```text
Contacts Page
Deals Page
Reports Page
```

## Good

```text
Deals / Pipeline

Purpose:
Manage potential sales outcomes through defined stages.

Typical information:
- deal name
- account
- owner
- amount
- stage
- expected close

Primary actions:
- create deal
- move stage
- assign owner
- log activity
- close won/lost
```

---

# 10. Important Rules / Behaviors

## Goal

解释：

> 什么条件真正决定系统行为？

可以包括：

- state transitions
- permission rules
- business constraints
- validation
- eligibility
- lifecycle dependencies
- exception handling

## Example — Hotel PMS

```text
A confirmed reservation does not guarantee immediate room occupancy.

Check-in may still depend on:
- room assignment
- room readiness
- housekeeping status
- payment requirements
```

这是高价值规则。

## Example — Image Editor

可能更适合写：

```text
- non-destructive adjustments preserve original pixel data
- layer order affects compositing result
- masks control where an operation applies
```

## Rule

不要为了章节完整硬编 Business Rules。

没有复杂规则时，可以简短。

---

# 11. States

States 不一定单独成章。

如果 Lifecycle 很重要，应明确表达。

## Good Candidates

```text
Order
Reservation
Ticket
Deal
Job
Document
Incident
Deployment
Room
Subscription
```

## Example

```text
Deal:
Open Stages
→ Closed Won
or
→ Closed Lost
```

## Important

不要把厂商具体状态名伪装成行业统一标准。

可以写：

> Canonical conceptual states; exact labels vary by product.

---

# 12. Permissions

只有在权限真正重要时展开。

例如：

```text
IAM
ERP
EHR
CRM
POS
Government systems
Admin systems
```

权限可能决定：

- visibility
- edit
- approve
- override
- export
- assign
- delete
- configure

对于 Calculator、Image Viewer 等简单工具，不需要硬写 Role Model。

---

# 13. Exceptions / Edge Cases

复杂运营软件尤其应该写。

高价值 Exception 通常来自：

```text
normal flow breaks
state conflicts
duplicate records
partial completion
failed payment
cancellation
reassignment
resource unavailable
permission failure
```

## Example — Restaurant POS

```text
- partial payment
- split check
- item unavailable
- void after item sent
- refund after closure
```

## Example — CRM

```text
- duplicate contact
- lead matches existing account
- person changes employer
- lost deal reopens
```

简单工具可以不单独写。

---

# 14. Capabilities

不要平铺 30–80 个功能。

推荐：

```text
Core
Common
Optional / Advanced
```

## Core

没有它，这个 Application Type 很难成立。

## Common

市场上非常常见，但不定义 Type。

## Optional / Advanced

部分厂商、特定客户或成熟版本中出现。

## Example

Restaurant POS:

```text
Core:
- order entry
- menu item selection
- modifiers
- payment
- close check

Common:
- table service
- split payment
- discount
- receipt

Optional:
- loyalty
- payroll
- delivery dispatch
- deep inventory
```

---

# 15. Variants

Variant 部分回答：

> 这种 Application 常见的不同形态是什么？

可以按：

- audience
- industry
- workflow
- deployment
- scale
- regulatory context

例如：

```text
Restaurant POS
- full-service
- quick-service
- bar
- cafe
```

如果一个 Variant 已经改变核心用户、对象、流程和规则，应提示可能是独立 Type。

---

# 16. Related Application Types

这是避免目录混乱的重要部分。

至少解释最容易混淆的邻近 Type。

推荐表格：

| Type | Relationship | Distinction |
|---|---|---|

例如：

| Type | Relationship | Distinction |
|---|---|---|
| Retail POS | adjacent | generic product transaction rather than restaurant service semantics |
| Restaurant Management System | broader | includes wider back-office operations |
| KDS | adjacent | kitchen production is primary |
| Online Ordering | customer-side adjacent | remote customer order capture is primary |

重点不是列 related links。

而是：

> 解释为什么它们不是同一个 Type。

---

# 17. Representative Products

这里只列代表产品。

不要写成长篇评测。

作用：

```text
给读者现实锚点
+
说明研究依据
```

通常 2–5 个即可。

---

# 18. Sources

最终文档 Sources 保持简洁。

至少包括：

```text
Product / Vendor
Official source title
URL
Research date
```

详细研究记录留在 Research Notes。

---

# 19. Writing Style

## Prefer

- precise
- concrete
- structural
- explanatory
- neutral
- product-oriented

## Avoid

### Marketing language

```text
powerful
seamless
best-in-class
revolutionary
streamline everything
boost productivity
```

除非是在引用厂商定位，并且有必要。

### Empty abstractions

```text
manage business processes
improve collaboration
optimize workflow
enhance efficiency
```

除非随后明确解释“管理什么、怎么管理”。

### Excessive academic abstraction

不要为了显得系统而创造不必要的理论术语。

### Implementation drift

不要展开：

```text
microservices
database schema
API gateway
event sourcing
backend architecture
```

除非目标 Application 本身就是这类开发/基础设施产品，而且这些概念是用户直接操作的对象。

---

# 20. Specificity Rule

每个重要段落都应该能回答：

> “具体是什么？”

Bad:

> The platform supports collaboration.

Better:

> Members work inside persistent channels, send messages, reply in threads, share files, and search prior conversation history.

Bad:

> The system manages reservations.

Better:

> Staff create and modify reservations, associate them with guests, assign rooms, process arrivals, and move the stay through check-in and check-out.

---

# 21. Product Pollution Check

写完每个章节，都可以问：

> 如果把厂商名字删掉，这段仍然成立吗？

如果不成立：

可能是：

- vendor-specific
- implementation detail
- marketing concept
- product module

需要重新判断是否应该保留。

---

# 22. Adaptive Depth

不同 Application 文档长度不必一致。

## Simple

例如：

```text
Calculator
Pomodoro Timer
Image Viewer
```

可能 1000–2000 字已经足够。

## Medium

例如：

```text
Team Messaging
Task Management
CRM
Video Editor
```

可能 2500–5000 字。

## Complex

例如：

```text
ERP
EHR
WMS
Hotel PMS
IAM
Trading Platform
```

可能 5000–10000+ 字。

目标不是达到字数。

目标是：

> 把关键结构讲清楚。

---

# 23. Recommended Writing Order

不要从 Overview 开始即兴写。

推荐内部写作顺序：

```text
1. Core Model
2. How It Works
3. Interfaces
4. Rules / States
5. Users
6. Related Types
7. Overview
8. Variants
9. Representative Products
10. Sources
```

原因：

> Overview 应该是研究结果的摘要，不是研究之前的想象。

---

# 24. Review Checklist

完成后检查：

```text
[ ] Overview 是否能一句话说清楚这是什么？
[ ] 是否明确主要用户？
[ ] Core Model 是否真正解释了系统内部结构？
[ ] 是否至少解释了最重要的 workflow / interaction loop？
[ ] 是否描述主要界面，而不是只列页面名？
[ ] 是否识别重要 state / rule / permission？
[ ] 是否区分 Core / Common / Optional？
[ ] 是否排除了厂商特有模块？
[ ] 是否解释了邻近 Type 的区别？
[ ] 是否能被没用过这种软件的人读懂？
[ ] 是否有可追溯来源？
```

---

# 25. Failure Modes

## Failure 1 — Feature Dump

```text
Features:
CRM
Analytics
Automation
AI
Reports
Integration
Dashboard
...
```

没有模型，没有流程。

失败。

## Failure 2 — Vendor Manual

把一个厂商帮助中心重新整理一遍。

失败。

## Failure 3 — Marketing Summary

充满：

```text
efficiency
optimization
seamless
powerful
```

但读完仍不知道软件怎么运作。

失败。

## Failure 4 — Schema Worship

为了模板完整：

- 硬写不存在的权限
- 硬写不存在的状态
- 硬写不存在的角色

失败。

## Failure 5 — Excessive Abstraction

把简单 Application 写成复杂 ontology。

失败。

## Failure 6 — Implementation Article

开始讨论：

```text
database
service
API
deployment
algorithm
```

却没有解释用户如何使用产品。

失败。

---

# 26. Gold Standard

一篇优秀 Application Document 应达到：

> 读者不需要安装或购买任何产品，也能在脑中建立这种 Application 的基本运行模型。

读完后，他应该可以大致想象：

```text
谁坐在软件前
→ 看见什么
→ 操作什么
→ 哪些对象发生变化
→ 工作怎样向前推进
→ 什么情况下会失败或被限制
```

这就是 Application Atlas 文档的标准。

---

# 27. Final Principle

Application Document 的核心不是：

> “这个软件有哪些功能？”

而是：

> **“这种软件世界是怎么组织起来并运行的？”**

因此：

```text
Research discovers reality.
Model explains structure.
Writing makes the structure understandable.
```

最终坚持：

> **结构优先于功能清单，理解优先于格式统一。**
