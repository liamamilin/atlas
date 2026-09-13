# Application Atlas — Research & Production Workflow

## 0. Purpose

本 Workflow 规定：

> Agent 如何从一个 Application Type 出发，自主研究现实产品，并产出一篇厂商无关、结构清晰、足够完整的 Application Document。

它统一的是 **工作过程**，不是强迫所有 Application 使用相同的研究 Schema。

不同 Application 的核心结构可以完全不同：

```text
CRM
→ Contact / Account / Deal / Activity / Pipeline

Video Editor
→ Project / Media / Timeline / Track / Clip / Effect

Hotel PMS
→ Guest / Reservation / Room / Stay / Folio / Room Status

Trading Platform
→ Instrument / Quote / Order / Position / Portfolio
```

因此：

> Workflow 必须统一；Research Questions 和最终展开方式必须自适应。

---

# 1. Input

每次任务输入一个目录中的 Application Type，例如：

```text
Restaurant POS
CRM
Hotel PMS
Raster Image Editor
Fleet Management System
AI Coding Agent
```

目录提供“研究对象是什么”。

Agent 不应自行扩大任务到整个 Family 或整个 Domain。

---

# 2. Output

每个 Application Type 最终至少产出两个文件：

```text
research/<application-type>.md
applications/<application-type>.md
```

其中：

## Research Notes

记录研究过程：

- 研究目标
- Application Type 边界
- 代表产品
- 研究问题
- 来源
- 产品观察
- 跨产品比较
- 共性与厂商特性
- 不确定项
- 最终抽象结果

## Application Document

记录最终结论：

> “这一类 Application 到底是什么，以及它通常如何工作。”

最终文档不是产品评测，也不是功能堆砌。

---

# 3. Workflow Overview

整个流程固定为：

```text
1. Understand
2. Plan
3. Sample
4. Research
5. Model
6. Compare
7. Synthesize
8. Write
9. Review
10. Cite
```

中文：

```text
理解
→ 计划
→ 选样
→ 研究
→ 建模
→ 比较
→ 归纳
→ 写作
→ 审查
→ 留证
```

---

# 4. Step 1 — Understand

## Goal

先理解目标 Application Type，而不是立刻开始搜资料。

Agent 应先建立一个临时假设：

```text
这是什么软件？
谁可能使用？
它主要解决什么问题？
最容易和什么 Application Type 混淆？
```

这一步的结论不是最终事实，只用于指导研究。

## Required Questions

至少回答：

```text
1. 这个 Application Type 的核心用途可能是什么？
2. 主要用户可能是谁？
3. 它最邻近的 Application Types 是什么？
4. 它与邻近 Type 的边界可能在哪里？
5. 目前有哪些明显未知点？
```

## Boundary Awareness

例如：

```text
Hotel Booking Platform
vs
Hotel PMS
```

不能因为两者都有 Reservation 就默认相同。

初步理解阶段就应记录这种潜在边界。

---

# 5. Step 2 — Plan

## Goal

根据当前 Application Type，自主决定“最值得研究什么”。

不要套固定字段表。

Agent 应问：

> 为了让一个从未使用过这类软件的人真正理解它，我必须搞清楚哪些问题？

然后生成一组针对当前 Application 的 Research Questions。

## Example — CRM

```text
- Lead、Contact、Account、Deal 分别是什么？
- 它们之间是什么关系？
- 一个潜在客户如何进入销售流程？
- Deal 如何移动？
- Activity 如何附着到客户关系？
- Sales rep 和 manager 分别做什么？
```

## Example — Video Editor

```text
- Project 与 Media 的关系是什么？
- Timeline、Track、Clip 如何组成编辑模型？
- Trim / Cut / Transition / Effect 如何工作？
- Audio 如何参与编辑？
- Render / Export 是怎样的终点？
```

## Example — IAM

```text
- Identity 是什么？
- User / Group / Role / Permission 如何关联？
- Authentication 和 Authorization 如何区分？
- Provision / Deprovision 如何发生？
- Policy 如何决定访问？
- Admin 与 end user 的界面分别是什么？
```

## Rule

Research Questions 可以因 Application 完全不同。

这正是 Workflow 的设计目标。

---

# 6. Step 3 — Sample

## Goal

选择足够代表市场结构的现实产品。

默认研究：

```text
2–5 个代表产品
```

不是固定数量。

## Selection Principles

优先组合：

```text
市场代表性
+
文档完整度
+
不同产品哲学
+
不同客户层级
```

例如：

```text
CRM
→ Salesforce / HubSpot / Zoho

Video Editor
→ Premiere Pro / DaVinci Resolve / Final Cut Pro

Restaurant POS
→ Toast / Square for Restaurants / Lightspeed Restaurant
```

## Avoid

不要：

- 只研究同一厂商多个版本
- 只选极小众产品
- 只选营销资料特别多但帮助文档很弱的产品
- 因为某产品功能很多就把它当作行业全部结构

---

# 7. Step 4 — Research

## Goal

研究“这种软件真实怎么工作”。

不是研究厂商故事。

## Source Priority

### Tier 1 — Official Operational Documentation

优先：

```text
Help Center
User Guide
Product Documentation
Support Articles
Official Training / Academy
Official Tutorials
```

这些最适合确认：

- 对象
- 页面
- 操作
- 流程
- 状态
- 规则

### Tier 2 — Official Product Pages

用于确认：

- 定位
- 目标用户
- 模块边界
- 产品范围

营销页不能单独证明复杂业务流程。

### Tier 3 — External Sources

当官方资料不足时：

```text
Professional tutorials
Product walkthroughs
Independent reviews
YouTube demonstrations
Community discussions
Screenshots
```

外部资料用于补缺，不应替代高质量官方文档。

---

# 8. What to Look For During Research

Agent 不需要机械寻找所有项目，但应尽量理解以下问题：

```text
Who?
谁在使用？

What?
系统里有哪些核心“东西”？

Do What?
用户围绕这些东西做什么？

Where?
这些动作发生在哪些界面 / 交互表面？

How?
典型工作是如何一步步完成的？

State?
哪些东西有生命周期或状态变化？

Rules?
哪些约束、权限、条件决定动作是否合法？

Exceptions?
真实使用中有哪些重要异常情况？
```

这些是观察视角，不是强制文档章节。

---

# 9. Step 5 — Model

## Goal

从产品细节里提取：

> 这个 Application 自己的“世界模型”。

不要急着写文章。

先回答：

```text
这个系统主要由什么构成？
这些东西怎么关联？
用户对它们做什么？
```

## Examples

### Team Messaging

```text
Workspace
→ Channel / Conversation
→ Message
→ Thread
→ Member / Access
```

### Restaurant POS

```text
Menu
→ Item / Modifier
→ Order / Check
→ Restaurant Fulfillment Context
→ Payment
→ Close
```

### Hotel PMS

```text
Guest
+
Reservation
+
Room / Space
+
Stay
+
Folio
+
Housekeeping / Room Status
```

### Image Editor

```text
Document
→ Canvas
→ Layer
→ Selection / Mask
→ Tool / Adjustment
→ History
→ Export
```

## Rule

模型结构必须由 Application 决定。

不要为了统一性，把所有软件硬塞成同一种对象图。

---

# 10. Step 6 — Compare

## Goal

比较代表产品，区分：

```text
Application Type 共性
vs
厂商实现差异
```

Agent 应持续问：

> 这是这种 Application 的特点，还是这个 Product 的特点？

## Evidence Strength

### Core

如果没有它，这种 Application 基本难以成立。

通常应有多个产品支持。

### Common

大量产品都有，但不是定义性结构。

### Optional

部分产品提供，可能是模块、扩展或更完整 Suite 的能力。

### Advanced

复杂用户或高级场景使用。

### Vendor-specific

目前主要是某个产品的独有设计。

不应写进 Canonical Core。

## Example

Toast 有：

```text
Payroll
Marketing
Loyalty
```

不能推出：

```text
Restaurant POS
= Payroll + Marketing + Loyalty
```

但多个 Restaurant POS 都稳定存在：

```text
Menu
Order
Modifier
Check
Payment
```

这些更接近 Canonical Core。

---

# 11. Step 7 — Synthesize

## Goal

从产品研究转向 Application Type 研究。

这一步必须去掉：

```text
品牌名称
厂商模块名
定价套餐差异
单厂商特性
纯 UI 皮肤差异
营销概念
```

保留：

```text
稳定用户
稳定核心结构
稳定工作方式
稳定界面形态
稳定生命周期
稳定规则
稳定异常
```

最终形成：

> Canonical Application Model

## Boundary Check

再次与邻近 Application Type 比较：

```text
Users
Core Model
Primary Jobs
Interfaces
Flows
Rules
```

如果研究表明当前目录节点实际只是 Variant / Alias / Capability，应记录问题，而不是硬写成完全独立 Type。

但不要擅自重构整个目录。

---

# 12. Step 8 — Write

## Goal

按照这种 Application 最自然的结构写最终文档。

最终文档使用：

> 固定骨架 + 自适应内容

推荐基础骨架：

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

## Important

`Core Model` 和 `How It Works` 是全文最重要的两个部分。

允许根据 Application 类型自由展开。

例如：

### CRM

`Core Model` 可以重点写：

```text
Lead
Contact
Account
Deal
Activity
Pipeline
```

### Video Editor

则可以写：

```text
Project
Media
Timeline
Track
Clip
Effect
Export
```

### CLI Tool

Interfaces 不必写成 Pages。

可以写：

```text
Commands
Arguments
Prompts
Output
Configuration
```

## Rule

不要为了模板完整而制造不存在的内容。

例如：

- Calculator 不需要硬写复杂 Permission
- Image Editor 不一定有多角色体系
- IAM 的 Permission 则应成为核心章节

---

# 13. Step 9 — Review

完成文档后，必须做一次独立审查。

## Review Questions

```text
1. 这篇写的是 Application Type，还是某个 Product？
2. 是否混入厂商专有功能？
3. 是否真正解释了这类软件如何工作？
4. 是否只是功能清单？
5. 是否找到了核心结构？
6. 是否遗漏关键 workflow / lifecycle？
7. 是否把 Common / Optional 当成 Core？
8. 是否和邻近 Type 边界不清？
9. 是否存在靠猜测写出的规则？
10. 一个没用过这类软件的人能否读懂？
```

## Failure Pattern

以下文本通常意味着研究失败：

> “该系统通过多种强大功能帮助企业提升效率和优化流程。”

这种描述没有解释 Application 本身。

---

# 14. Step 10 — Cite

## Goal

保留研究来源，使文档可追溯。

至少记录：

```text
Representative Products
Official Sources
Research Date
Important Uncertainties
```

最终文档可以保持简洁来源列表。

详细证据和研究过程保存在 Research Notes。

---

# 15. Research Notes Recommended Structure

Research Notes 推荐而不强制使用：

```text
# Research Notes — <Application Type>

## Research Goal

## Initial Boundary

## Research Questions

## Representative Products

## Sources

## Product A
### Key observations

## Product B
### Key observations

...

## Cross-product Comparison

## Canonical Model

## Vendor-specific Findings

## Boundary Findings

## Uncertainties

## Final Synthesis
```

如果某类 Application 需要不同结构，可以调整。

---

# 16. Application Document Recommended Structure

```text
# <Application Type>

## Overview

说明：
- 它是什么
- 解决什么问题
- 基本边界

## Users & Context

说明：
- 谁使用
- 在什么场景使用

## Core Model

解释：
- 这个 Application 世界里最重要的对象 / 概念 / 结构
- 它们之间如何关联

这是全文核心。

## How It Works

解释最重要的：

- interaction loop
- workflow
- transaction
- lifecycle
- editing process
- operational flow

根据 Application 自适应。

## Interfaces

解释用户真正看到和操作的主要界面。

## Important Rules / Behaviors

记录真正影响系统行为的重要：

- state rules
- permissions
- constraints
- business rules
- exceptional behavior

没有重要规则则可以简写。

## Variants

说明行业、用户、部署或 workflow 变体。

## Related Application Types

解释邻近 Type 以及区别。

## Representative Products

列出用于理解该 Type 的典型市场产品。

## Sources

列出主要研究来源。
```

---

# 17. Research Depth

研究深度应根据 Application 自适应。

## Simple Application

例如：

```text
Calculator
Pomodoro Timer
Image Viewer
```

不需要为了形式研究十几页。

## Complex Application

例如：

```text
EHR
ERP
Hotel PMS
WMS
Trading Platform
IAM
```

必须研究：

- 多角色
- 多对象
- 状态
- 复杂 workflow
- 权限
- exception

因此：

> Workflow 统一，研究成本不统一。

---

# 18. Stop Conditions

Agent 可以停止继续研究，当：

```text
1. 已经能够解释该 Application 的核心模型
2. 主要 workflow 已经清楚
3. 代表产品之间的稳定共性已经出现
4. 新增产品主要只是在重复已有证据
5. 邻近 Type 边界已经足够清楚
```

不要为了“研究得更多”无限扩展资料。

---

# 19. Escalation Conditions

如果发现以下问题，写入 Research Notes：

## Type Boundary Problem

当前节点可能与已有 Type 重复。

## Variant Problem

当前节点可能只是 Industry / Audience / Surface Variant。

## Product Mismatch

原本选中的代表产品实际上属于邻近 Type。

## Insufficient Evidence

无法找到可靠资料确认关键工作方式。

## Taxonomy Problem

现实产品研究与现有目录分类明显冲突。

此时：

> 记录问题，不擅自大规模修改目录。

---

# 20. Definition of Done

一篇 Application Document 完成后，一个没有使用过这种软件的人应该能够回答：

```text
它到底是什么？
谁会使用？
这个软件世界里有哪些核心东西？
用户围绕这些东西做什么？
主要工作是怎么流转的？
用户通常面对什么界面？
哪些状态、规则或权限很重要？
它和类似软件有什么区别？
现实世界有哪些代表产品？
```

如果能回答这些问题，这篇文档就是有效的。

---

# 21. Core Principle

整个 Workflow 最终只服务一个目标：

> 从现实产品中理解一种 Application，而不是从抽象模板里想象一种 Application。

因此长期遵循：

```text
Directory Node
→ Real Product Research
→ Application Model
→ Application Document
```

以及：

> **统一方法，不统一答案。**
---

# 22. Canonical Abstraction Hierarchy

When synthesizing an Application Type, do **not** treat every repeated feature in the sampled products as part of the Canonical Core.

Always separate findings into four abstraction levels.

## Level 0 — Defining Invariant

The smallest stable structure without which the Application Type would stop being recognizable as that Type.

Ask:

```text
If this property disappeared,
would this still clearly be the same Application Type?
```

Examples:

```text
Instant Messaging
→ identity / participants
→ private addressable conversation
→ message
→ persistent conversation history

CRM
→ relationship records
→ associations
→ activity/history
→ commercial workflow

Restaurant POS
→ menu-configured order
→ transaction/check
→ payment
```

Level 0 should be deliberately small.

## Level 1 — Common Mature Structure

Capabilities or objects that are very common in mature modern products but are not required to define the Type.

Examples:

```text
Instant Messaging:
- group conversation
- delivery/read state
- media messages
- profile
- presence
- voice/video calls
```

These may be highly expected in the market without belonging in the strict definition.

## Level 2 — Variant / Optional Structure

Features that depend on:

- market segment
- geography
- deployment
- security posture
- customer scale
- business model
- workflow variant

Examples:

```text
phone-number identity
username discovery
public channels
payments
stories/status
self-hosting
default end-to-end encryption
```

## Level 3 — Vendor-specific Structure

Product-specific modules, terminology, limits, defaults or branded workflows.

These remain in Research Notes unless they are useful as examples.

## Anti-overfitting Rule

A shared implementation pattern across the sampled products is not automatically a defining invariant.

Example:

```text
WhatsApp + Signal + Telegram
all commonly use phone-number-based onboarding
```

does not by itself prove:

```text
Instant Messaging
= phone-number identity
```

The canonical abstraction may instead be:

```text
personal addressable identity
```

with phone number documented as a common implementation.

---

# 23. Evidence → Assertion Rule

The strength of a written claim must not exceed the strength of the available evidence.

Use three evidence layers.

## A. Directly Observed

Supported by an official source for a specific product.

Write:

```text
Product X supports...
Product X exposes...
In Product X...
```

Do not automatically generalize.

## B. Cross-product Commonality

Observed across multiple representative products.

Write:

```text
Common implementations include...
Mature products commonly...
Across the researched sample...
```

This can support Level 1 findings.

## C. Canonical Inference

A higher-level abstraction derived from cross-product comparison and Type-boundary reasoning.

Write:

```text
A useful canonical abstraction is...
The Type can be modeled as...
The defining structure is best understood as...
```

Canonical inference must be visibly more abstract than vendor implementation details.

## Precision Rule

Do not state precise operational facts unless the evidence supports that precision.

Avoid unsupported statements such as:

```text
messages can usually be edited for 15 minutes
groups are normally a few dozen people
the phone is always the canonical identity holder
```

unless these claims have been deliberately researched across the relevant sample.

Prefer:

```text
some products limit message editing to a defined time window
group-scale limits vary substantially by product
many mobile-first IM products use a phone-centered identity model
```

## Single-source Rule

If a claim is supported by only one product:

- keep it product-specific, or
- classify it as Optional / Variant / Unverified

Do not promote it directly to Canonical Core.

## Source-access Limitation

If official operational documentation cannot be accessed:

1. record the limitation in Research Notes
2. reduce assertion strength
3. avoid precise workflow/rule claims that depend on inaccessible evidence
4. do not compensate by silently filling detail from model memory

---

# 24. Historical / Market-Sample Check

Representative products describe the current market, not the timeless definition of an Application Type.

Before freezing the Canonical Core, ask:

```text
Would older, regional, platform-native, or differently positioned products
still fit this definition?
```

Use this check to avoid defining a Type by the current dominant implementation.

Example:

```text
Modern mobile IM often uses phone-number onboarding.
Older or platform-native IM may use usernames, email, device accounts, or social accounts.
```

Therefore the higher-level canonical concept is more likely:

```text
addressable personal identity
```

than:

```text
phone number
```

This check is especially important for long-lived Application Types.
