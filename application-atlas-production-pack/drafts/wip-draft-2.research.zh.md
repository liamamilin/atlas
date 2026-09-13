# 研究笔记 —— 小说写作应用

研究日期：**2026-09-13**

研究方法：直接阅读 `applications/` 目录中现有的语料库叶子节点、`DIRECTORY.md` 类别索引，以及本次研究期间获取的官方产品/供应商页面。`application-atlas` MCP 服务器（`search_similar` / `get_leaf`）在此环境中未作为工具暴露，因此最近邻发现是通过直接列出和阅读语料库完成的（见“不确定性”部分）。

以下使用的证据等级：

- **A** — 获取并阅读了多个官方供应商页面及产品文档
- **B** — 获取并阅读了官方产品/功能页面（营销/概述层面）
- **C** — 直接语料库检查，并基于至少两个产品进行推理
- **D** — 单一来源或未在其他地方确认的推理

## 边界发现

### 1. Novel Writing Application 与 Distraction-free Writing Application

- 配对：`novel-writing-application`（提议） ↔ `distraction-free-writing-application`（现有叶子）。
- 区分测试：从小说写作应用中移除手稿树、连续性层和编译设置，只留下编辑器；如果产品的核心承诺依然成立，那么它就是无干扰写作应用。从无干扰写作应用中移除注意力表面，你得到的是一个普通编辑器，而不是小说写作应用。
- 证据：无干扰写作叶子将其核心定义为持久化文本文档 + 无干扰的写作表面 + 起草优先，并明确将组织功能置于写作表面之下；Scrivener 的概述文档记载其核心是活页夹、研究区域、软木板/大纲器、目标、快照和编译，全屏写作只是其中一种可选模式。**等级 A。**
- 结果：不同的类型。重心相反（表面 vs 项目）。

### 2. Novel Writing Application 与 Outliner

- 配对：提议 ↔ `outliner`（现有叶子）。
- 区分测试：在大纲器中，项目树*即*内容；删除散文和故事材料后，小说写作应用剩下的树是一个情节大纲，这属于大纲器的范畴。在大纲器中，为项目添加长篇散文是一种覆盖层，而非产品存在的理由。
- 证据：大纲器叶子将项目定义为原子单元，子树操作是其定义性行为；Scrivener 的活页夹是一个有序树，其叶子是单独编写的散文文档，而树本身是编译后书籍的目录。Manuskript 文档既包含层次化的大纲器，也包含一个单独的写作编辑器，其中设有角色/情节/世界观。**等级 A（两个产品）→ 整体 B。**
- 结果：不同的类型；共享表面（嵌套列表），但意义单位不同。

### 3. Novel Writing Application 与 Document Editor / Word Processor

- 配对：提议 ↔ `document-editor`（现有叶子）。
- 区分测试：移除结构化树和连续性层——如果剩下的只是一个连续的、有格式的文档，且这本身仍然是一个完整的产品，那么它就是文档编辑器。移除这些后的小说写作应用将不再有手稿，只剩下文本片段。
- 证据：b2b/2d 示例和类别索引将文档编辑器置于“文档与写作”下，作为一个平面文档类型；Dabble 自身的对比将 Google Docs 和 Word 定位为“难以处理大型手稿”的编辑器，而它自己则将章节/场景/情节分开组织。**等级 B。**
- 结果：不同的类型；文档编辑器是通才型的始祖。

### 4. Novel Writing Application 与 Note-taking / Personal Knowledge Management

- 配对：提议 ↔ `note-taking-application`、`personal-knowledge-management`（现有叶子）。
- 区分测试：移除手稿，保留连续性层——如果产品仍然可以独立作为一个链接笔记/维基产品存在，那么它就是 PKM。从小说写作应用中移除连续性记录，手稿仍然成立；而对于 PKM 工具，情况正好相反。
- 证据：大纲器叶子的边界讨论区分了库级组织和内容内树；Novelcrafter 的 Codex 明确是一个为单一叙事服务的辅助维基（“为了真正洞察你的世界”），而非通用笔记网络。Campfire 的世界观构建模块服务于故事。**等级 B。**
- 结果：不同的类型，共享类似维基的表面。

### 5. Novel Writing Application 与 Storyboard Application

- 配对：提议 ↔ `storyboard-application`（现有叶子）。
- 区分测试：如果规划的单元以图像（一个绘制的帧）作为其主要内容，那么它是故事板；如果它以散文和概要为主，那么它是小说写作应用的规划表面。移除散文和故事圣经，Plottr 式的场景卡仍然存在——但如果没有图像，它们仍然是大纲卡，而不是故事板。
- 证据：语料库中的故事板应用归类于 04.19 Storyboarding；2D 动画叶子将故事板描述为没有动画的静态规划面板。**等级 C**（语料库结构加定义对比；本次未获取故事板供应商页面）。
- 结果：不同的类型；仅通过“生产前规划”相邻。

### 6. Novel Writing Application 与 Script Breakdown Application

- 配对：提议 ↔ `script-breakdown-application`（现有叶子，已完整阅读）。
- 区分测试：分解应用需要剧本作为源记录，并生成按场景分类的元素清单和类别报告；小说写作应用既不解析场景为生产类别，也不生成分解表。
- 证据：分解叶子的核心定义是剧本 + 场景记录 + 元素标签 + 分解输出。小说写作产品集（Scrivener, Dabble, Novelcrafter, Campfire, bibisco, Manuskript）中没有任何产品能生成生产元素清单。**等级 A（分解叶子）→ B。**
- 结果：不同的类型，仅通过“场景作为一个单位”的共享概念相邻。

### 7. Novel Writing Application 与 Publishing Editorial Workflow / Book Publishing Management

- 配对：提议 ↔ `publishing-editorial-workflow`、`book-publishing-management`（现有叶子）。
- 区分测试：如果系统的记录单元是一个经过角色分配的编辑关卡并有截止日期的出版作品，那么它是编辑工作流；如果其核心是书目损益、合同、版税和元数据，那么它是出版管理。小说写作应用的单元是作者的手稿，其用户是作者，而非出版商。
- 证据：出版编辑工作流叶子指出该工作流“跟踪过程；它不进行编辑”，写作/修订在其外部的编辑器中进行。**等级 A。**
- 结果：不同的类型；它们在提交/交接点相遇，而非在结构中。

### 8. Novel Writing Application 与 Desktop Publishing / E-book Production

- 配对：提议 ↔ `desktop-publishing-application`（现有叶子）。
- 区分测试：如果产品的核心是用于印刷或零售的页面排版和字体设计，那么它是 DTP。小说写作应用的编译产生的是手稿或基础的 DOCX/PDF/EPUB 导出，而非设计过的页面；Scrivener 自身的编译描述是“准备你的手稿以供分享”，EPUB 生成只是众多格式之一。
- 证据：Scrivener 概述（编译/导出）和 Campfire 独立的出版路径。**等级 B。**
- 结果：不同的类型；编译是通往外部的桥梁，而非排版创作。

### 9. Novel Writing Application 与 plot-outlining companion (Plottr)

- 配对：提议 ↔ 一个可能的“Plot Outlining Application”（未发现现有叶子）。
- 区分测试：产品是否创作散文？Plottr 的文档记载了可视化时间线、模板、角色表、系列圣经，以及导出“到 MS Word & Scrivener”，作者在外部写作；它有意将自己定位为规划伴侣，而非写作表面。
- 证据：Plottr 产品页面，已获取。**等级 B。**
- 结果：Plottr 被视为相邻/边界语境，而非代表性成员，因为产品内的散文起草是 L0 核心的一部分。标记：如果未来创建了“Plot Outlining Application”叶子，两者必须相互链接。

### 10. Story bible formality（内部边界）

- 类型内测试：Scrivener 的连续性层是一个研究文件夹加可复用模板，而非类型化的实体记录；bibisco 将角色、地点和故事情节作为结构化区域呈现；Novelcrafter 的 Codex 是类型化且支持链接的；Campfire 提供独立的世界观构建模块。
- 证据：六个代表性产品网站均已获取。**等级 B。**
- 结果：连续性层的正式程度是一个变体轴，而非定义性要求——记录此点是为了避免该类型对 Codex 风格产品过度拟合。

## 不确定性

1.  **yWriter 未验证。** `https://www.spacejock.com/yWriter7.html` 在本次研究中返回 HTTP 500 错误。yWriter 完全未出现在代表产品和来源中；没有任何声明依赖于它。（等级：验证失败。）
2.  **文档深度。** 对于所有六个代表性产品，仅能阅读其产品、功能和概述页面；未获取完整的用户手册/帮助中心。因此，所有能力声明都基于概述层面，未断言任何数字限制、默认设置、功能数量或确切的阶段术语。（等级 B。）
3.  **仅规划工具。** 像 Plottr 这样没有散文的大纲器，究竟是一个子变体还是一个独立类型，确实存在争议。本次研究决定其为*独立/相邻*，因为产品内的散文创作是已确立的 L0 核心的一部分。合理的审查者可能会将边界划在别处。（等级 C，标记供联合审查。）
4.  **AI 中心性。** AI 原生小说平台是同一类型还是一个新兴的子类型，尚未解决。本次研究将 AI 视为叠加在同一核心上的可选加速器，因为 Novelcrafter 的文档表明其界面可在不使用 AI 的情况下使用。未主张单独的 AI 原生类型。（等级 C。）
5.  **语料库中不存在剧本写作叶子。** 剧本写作应用与小说工具共享场景/大纲结构，且多个产品同时服务于两者。由于在 `applications/` 或 `DIRECTORY.md` 中未找到 `screenwriting-application` 叶子，剧本写作关系仅在变体/相关部分描述，未来若创建叶子则需要进行边界划分。（等级 C。）
6.  **MCP 搜索不可用。** 说明书中提到的 `search_similar` / `get_leaf` MCP 工具在此环境中不可用。最近邻是通过列出 1806 个应用文件、阅读 `DIRECTORY.md` 并在整个语料库中搜索 `novel|fiction|manuscript|screenplay|story bible` 找到的。可能遗漏了索引集之外新建的叶子；完整阅读的四个最近现有叶子是 `distraction-free-writing-application`、`outliner`、`script-breakdown-application` 和 `publishing-editorial-workflow`。（等级：流程限制。）
7.  **中文显示层。** 身份文件中的中文名称和论述是创作提示；根据语料库策略，翻译后的显示层是单独生成的，因此正文中未出现中文文本。