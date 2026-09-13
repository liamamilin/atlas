# Research Notes — Answer Engine

## Research Goal

从现实产品出发回答：**Answer Engine（答案引擎）这一 Application Type 的定义性结构是什么？** 它与邻近 Type（General Web Search Engine、AI Research Assistant、AI 聊天助手、Expert Q&A Platform、Knowledge Question Answering Application、Academic Search Engine）的边界在哪里？

## Initial Boundary（临时假设，非最终结论）

- 核心用途：用户提出信息类问题，系统**直接给出答案**，而不是返回文档链接列表。
- 主要用户：有信息需求的个人（消费者、学生、开发者、专业人员）。
- 最容易混淆的邻近 Types：
  - General Web Search Engine（返回链接列表 vs 返回答案）
  - AI 聊天助手 / AI Research Assistant（无检索接地 vs 有检索/计算接地；一次问答 vs 持续研究过程）
  - Expert Q&A Platform（人写答案 vs 机器产答案）
  - Knowledge Question Answering Application（受限知识库 QA vs 开放式答案引擎）
- 明显未知点：
  - 现代代表性产品（Perplexity 类）能否抓到 Tier-1 文档？
  - 历史样本（Ask Jeeves 一系）能否验证？
  - "引用/来源归属"是否应进定义核心？
  - 会话式追问（thread）是否定义性？

## Research Questions

1. 用户输入的形态是什么？（自然语言问句 vs 关键词）问题是不是主要输入？
2. "答案"由什么构成？系统如何产出答案（综合、计算、路由选择）？
3. 答案的根据（grounding）来自哪里？来源归属如何呈现？
4. 核心交互循环是什么？追问、上下文、历史如何工作？
5. 哪些对象/状态存在？（问题、答案、来源、线程、历史库）
6. 歧义如何处理？（问句歧义、多解释）
7. 深度分层？（快答 vs 深度分析/报告）
8. 交付形态？（web / mobile / 扩展 / API / 私有部署）
9. 与搜索引擎的嵌入关系？（搜索结果旁的答案面 vs 独立产品）
10. 商业模式与限制如何影响行为？

## Representative Products

选择原则：市场代表性 + 文档可得性 + 不同产品哲学 + 不同年代/区域。

| 产品 | 哲学/定位 | 年代 | 客户层 | 证据状态 |
|---|---|---|---|---|
| Wolfram\|Alpha | 计算/策展知识库（"computational knowledge engine"，明确自我定位"not by searching the web"） | 2009 | 消费者/教育/企业/API | **Tier-1 深度**（landing/tour/about/API 四页全可达） |
| Andi | AI 对话式搜索（"Instead of just links, Andi gives you answers"） | 近年 | 消费者 | Tier-2 落地页（JS 应用，内容薄） |
| 秘塔AI搜索 Metaso | 中文市场 AI 搜索（"没有广告，直达结果"） | 近年 | 消费者 | Tier-2 落地页（薄）+ API 端点存在性（401 响应） |
| Komo | AI Search Engine（带 History/library） | 近年 | 消费者 | Tier-2 应用壳（薄） |

替代说明：原首选 Perplexity（原型产品）、You.com、Phind（开发者垂直）均因抓取超时/403 两次而放弃；Ask.com（Ask Jeeves 历史谱系）、iAsk.ai、Brave Search AI、Duck.ai、Felo 同样不可达。样本以"计算哲学 + 现代 AI 搜索姿态"的两端构成，缺少 LLM 综合原型的 Tier-1 证据（见 Uncertainties）。

## Sources

### 可达来源（2026-09-06 实际抓取）

- Wolfram|Alpha landing — https://www.wolframalpha.com/ （含定位语、输入框、领域示例分类、Pro/Mobile/API/Enterprise 导航）
- Wolfram|Alpha Tour — https://www.wolframalpha.com/tour （引擎四段式流水线、使用场景、Pro 功能、API 入口）
- Wolfram|Alpha About — https://www.wolframalpha.com/about （范式声明、目标、历史）
- Wolfram|Alpha APIs — https://products.wolframalpha.com/api （API 全家族、典型部署、免费额度、Appliance/Custom）
- Wolfram|Alpha Timeline — https://www.wolframalpha.com/docs/timeline （可计算知识历史叙事）
- Andi — https://andisearch.com/ （定位语；/about 为同一 JS 壳）
- Metaso 秘塔AI搜索 — https://metaso.cn/ （定位语、功能面）；https://metaso.cn/api （401，端点存在）
- Komo — https://komo.ai/ （应用壳：History/Firsthand/Earn）

### 不可达来源（每源尝试 ≤2 次，按规则放弃）

- Perplexity — www.perplexity.ai、support.perplexity.ai（超时 ×2）
- You.com — www.you.com、you.com（超时 ×2）
- Phind — www.phind.com（403）、blog.phind.com（传输错误）
- Ask.com / about.ask.com（传输错误 + 超时）
- iAsk.ai — iask.ai、iask.ai/why（超时 ×2）
- Brave Search AI — brave.com/search-ai（超时 ×2）
- Duck.ai 帮助 — duckduckgo.com/duckduckgo-help-pages（超时 ×2）
- Google AI Overviews 支持页 — support.google.com/websearch/answer/13688549（超时 ×2）
- Felo — felo.ai（超时 ×1，未再试）

### 内部一致性参照（本地）

- research/ai-research-assistant.md §Boundary Findings（已处理叶子的家族判据与联合评审 flag）
- research/academic-search-engine.md（已处理；L0 = query → ranked record list）

## Product Observations

### Wolfram|Alpha（证据层 A — 直接观察，官方文档）

- **定位**："Compute verified, expert-level answers using Wolfram's breakthrough algorithms and knowledgebase"；About 页："defined a fundamentally new paradigm for getting knowledge and answers—**not by searching the web, but by doing dynamic computations based on a vast collection of built-in data, algorithms and methods**"。
- **输入**：单一输入框 "Enter what you want to calculate or know about"；支持 Natural Language 与 Math Input；About："accept completely free-form input"。
- **产出**：Tour："automatically answer questions, do analysis and generate reports"；四段流水线 = Linguistic Analysis（1,000+ 领域）→ Curated Data（"10+ trillion pieces of data from primary sources with continuous updating"）→ Dynamic Computation（"50,000+ types of algorithms & equations"）→ Computed Presentation（"5,000+ types of visual and tabular output"）。
- **领域范围**：Mathematics / Science & Technology / Society & Culture / Everyday Life 的示例分类树（通用知识面，非垂直）。
- **歧义处理**：API 页 Full Results API 明确含 "disambiguation, drilldown, asynchronous results delivery"；另有 Fast Query Recognizer API（"classify queries, and recognize ones that are likely to be handled by Wolfram|Alpha"）。
- **深度分层**：免费站为"tourist experience"；Pro 加 step-by-step solutions、file/data/image upload、Problem Generator、Web Apps（form-based interfaces）。
- **交付形态**：Web、Mobile Apps、Toolbars & Add-Ons、Notebook Edition、API 家族（Full Results / LLM / Simple / Short Answers / Fast Query Recognizer / Summary Boxes / Instant Calculators / Spoken Results）、Appliance（私有部署）、Custom enterprise solutions（"custom Wolfram|Alpha for organizational as well as public data"）。
- **API 免费额度**："up to 2,000 non-commercial API calls per month"（精确数字，直接观察；仅记于此）。
- **与搜索引擎的嵌入关系**：API 页 Typical Deployments 明确列出 Search Engines："Triage with the Fast Query Recognizer, then **display computational knowledge alongside search results**"。
- **与 LLM 的关系**：LLM API（"results optimized for use by a large language model"，含 JSON 结构化、长度控制）；Foundation Tool for LLM-Based Systems；LLM Solutions 页。
- **历史叙事**：About 引 "computers… would eventually have the kinds of question-answering capabilities"；Timeline 页把自身放入"computable knowledge"两万年叙事。

### Andi（证据层 A- 薄 — 落地页直接观察）

- 定位语："Andi is AI search for the next generation. **Instead of just links, Andi gives you answers** - like chatting with a smart friend."
- 顶栏三词："AI. Chat. Search."——同时自认 search 与 chat 两种表面。
- 应用为 JS 壳，操作细节不可直接观察（降级：不声称任何具体 UI/机制）。

### Metaso 秘塔AI搜索（证据层 A- 薄 — 落地页直接观察）

- 定位语："**没有广告，直达结果**"（无广告、直达结果）——直达"结果"而非链接列表的姿态。
- 功能面（导航/入口直接观察）：学点啥（学习向）、视频生成、幻灯片（slides 生成）、上传文件、API、新建自定义技能、手机端（QR）。
- 观察：现代中文 AI 搜索产品已把"答案引擎"外延扩展为内容生成/技能平台；核心仍是问→结果直达。
- API 端点 https://metaso.cn/api/ 返回 401（需鉴权）→ API 交付形态存在。

### Komo（证据层 A- 薄 — 应用壳直接观察）

- 自我标注："Komo — AI Search Engine"。
- 应用壳直接观察：New search、**History（library）**、Firsthand、Earn、Sign in。
- 观察：搜索/问答历史作为持久库是现代 AI 搜索产品的常见结构（单薄证据，跨产品对照 Wolfram 无此结构强调）。

### 不可达产品的处理

Perplexity / You.com / Phind / Ask.com / iAsk 等完全未获直接证据。**研究笔记中不作任何操作性断言**；仅在家族叙事中作为市场背景提及（标记为 Tier-3/未验证），最终文档不引用它们的具体机制。

### 历史样本（§24 检查）

- **Wolfram|Alpha（2009）即为最强历史校验样本**：它的存在迫使抽象脱离"LLM 综合网页摘要"这一当代实现——答案可以是**计算产出**而非综合文本。任何把"LLM 综合 + 行内引用"写进定义核心的尝试都会把 2009 年的原型产品排除在外。
- **Ask Jeeves（1990s，未验证）**：市场史上以自然语言问句路由到人工策展答案页著称（Tier-3 常识，未获官方来源；不写入最终文档的操作性断言）。它提示第三种产出姿态：**路由/选择**既有答案而非综合或计算。由于不可达，L0 不依赖它，但其存在支持"系统产出答案"的三姿态抽象（综合/计算/选择）而非单一姿态。
- 平台原生语音助手（Siri 等）回答问题但属多功能助手，答案只是能力之一 → 不进本 Type（无对应叶子，仅记录）。

## Cross-product Comparison

| 维度 | Wolfram\|Alpha | Andi | Metaso | Komo |
|---|---|---|---|---|
| 主要输入 | 自然语言问句/数学式 | 问句（对话式） | 问句（AI 搜索） | 问句（AI 搜索） |
| 主要产出 | 计算出的直接答案（可视化/表格/报告） | 直接答案（对话面） | 直达结果 | 直接答案（搜索面） |
| 接地来源 | 自有策展数据 + 算法（明确"not by searching the web"） | 自称 AI search（索引姿态，细节不可观察） | 自称 AI 搜索（细节不可观察） | 自称 AI search engine（细节不可观察） |
| 来源归属呈现 |策展数据"from primary sources"；Pro step-by-step；API drilldown | 不可观察 | 不可观察 | 不可观察 |
| 会话/追问 | 单问单答为主（API disambiguation/drilldown 处理歧义） | "chatting with a smart friend" | 不可观察 | History/library 存在 |
| 历史库 | 未见强调 | 不可观察 | 不可观察 | History 直接观察 |
| 深度分层 | Free vs Pro（step-by-step/上传/报告） | 不可观察 | 上传文件/幻灯片/技能 | 不可观察 |
| API | 完整 API 家族 + 免费额度 | 未见 | API 端点存在 | 未见 |
| 部署 | Web/Mobile/Add-ons/Appliance/Custom | Web | Web/手机端 | Web |
| 跨界外延 | LLM API、嵌入搜索结果旁 | — | 视频生成/幻灯片/技能 | Firsthand/Earn |

### 跨产品共性（证据层 B）

1. **问句是主要输入，直接答案是主要产出**——四者全部成立（Wolfram："answer questions"；Andi："gives you answers"；Metaso："直达结果"；Komo："AI Search Engine"）。这是全样本最强共性。
2. **系统自己完成"作答"动作**——综合（AI 搜索姿态）或计算（Wolfram），而非用户自读链接。Andi 的 "Instead of just links" 是最直接的对照表述。
3. **答案背后有系统自备的知识材料**——Wolfram 明确（策展数据+算法）；Andi/Metaso/Komo 自称 "AI search"（以检索为中心的姿态）。注意：后三者仅定位语级证据。
4. **Web 为主表面，多形态交付**——四者皆 Web；Wolfram 扩至 Mobile/Add-ons/API/Appliance；Metaso 手机端 + API。
5. **账户/分层可用性**——Wolfram Pro、Komo Sign in、Metaso API 鉴权。

### 单产品观察（证据层 A，不外推）

- Wolfram：disambiguation/drilldown、Fast Query Recognizer、Spoken Results、Appliance、嵌入式部署（alongside search results）、LLM API。
- Komo：History/library、Firsthand、Earn。
- Metaso：幻灯片/学点啥/自定义技能。

## L0 / L1 / L2 / L3 四层抽象

### L0 — Defining Invariant（极小，三条）

1. **问句锚定的交互**：用户提出信息性问题；问题是主要输入（自然语言为主，关键词/公式亦容忍——Wolfram 接受 free-form 与 math input）。
2. **系统执行的作答**：系统本身产出对问题的直接答案——综合（AI 搜索）、计算（Wolfram）或选择/路由（历史形态）——并把它作为主要交付物呈现，而非文档链接列表。**反事实检验：去掉它 → General Web Search Engine。**
3. **问题时的接地（question-time grounding）**：答案针对该问题从系统自备的知识材料（索引/策展语料/知识库）中检索、计算或选择得出，而不是仅由模型记忆生成。**反事实检验：去掉它 → AI 聊天助手。**

反事实检验（整体）：去掉 L0-1（问句锚定）→ 它不再是问答系统；去掉 L0-2 → 搜索引擎；去掉 L0-3 → 聊天机器人。三者缺一即脱离 Type。

**历史/区域校验**：Wolfram|Alpha（2009，计算哲学）满足全部三条；当代 AI 搜索（Andi/Metaso/Komo，仅定位语级）满足 1、2，3 为姿态级证据；Ask Jeeves 类历史形态（未验证）在 2 上以"选择"姿态成立。结论：L0 不含 LLM、行内引用、会话线程、网页索引——它们都不是"去掉就不是答案引擎"的属性。

### L1 — Common Mature Structure（现代成熟产品的常见结构）

- **来源/根据的可见呈现**：网络接地型产品通常把来源链接挂在答案旁；计算型产品呈现推导/数据来源（Wolfram：primary sources、step-by-step、drilldown）。*措辞校准：跨产品直接证据有限（Wolfram 强、其余薄），用"通常/mature products typically"。*
- **会话式追问**：在上下文中继续问（Andi "chatting"；现代 AI 搜索普遍姿态）。
- **历史/线程库**：过往问答可回访（Komo History 直接观察；现代产品常见）。
- **答案的富呈现**：摘要 + 支撑细节 + 可视化/表格（Wolfram：5,000+ visual/tabular output 类型直接观察）。
- **歧义处理**：澄清/多解释分支（Wolfram API disambiguation 直接观察）。
- **深度分层**：快答 vs 深度模式（Pro/分析/报告——Wolfram 直接观察；Metaso 上传文件/幻灯片为扩展产出）。
- **多表面交付**：Web + Mobile + 扩展 + API（Wolfram、Metaso）。
- **账户与分层可用性**：免费/订阅/API 计量（Wolfram Pro + API 免费额度、Komo Sign in、Metaso API 鉴权）。
- **相关/追问建议**：常见于现代产品（本样本无直接证据，弱化处理，仅在"会话循环"中泛述）。

### L2 — Variant / Optional Structure

- **接地基底**：开放 Web 索引（AI 搜索姿态）vs 策展结构化语料 + 计算（Wolfram）vs 混合。
- **语料范围**：通用 vs 领域限定（开发者/学术/医疗等垂直姿态；样本内 Wolfram 为通用，垂直姿态为市场常识，未验证）。
- **作答姿态**：综合 / 计算 / 路由选择（历史）。
- **会话深度**：单问单答 vs 持续对话线程。
- **嵌入 vs 独立**：独立产品 vs 搜索引擎内嵌答案面 / 搜索结果旁的计算知识（Wolfram API 明确支持"alongside search results"部署）；反向地，搜索引擎加答案面仍是搜索引擎（能力 vs Type）。
- **区域市场形态**：中文 AI 搜索把答案引擎外延为内容/技能平台（Metaso：幻灯片、学点啥、自定义技能）。
- **交付形态**：私有部署（Wolfram Appliance）、SMS/OTT 答案服务、可穿戴/AR 输出（Wolfram API 部署列表）。
- **商业模式**：免费/订阅/API 计量/企业定制。

### L3 — Vendor-specific（仅存本笔记）

- Wolfram：Fast Query Recognizer（<10ms）、Summary Boxes API、Instant Calculators、Spoken Results、LLM Foundation Tool、2,000 次/月免费 API、NKS/Wolfram Language 叙事、Problem Generator、Web Apps、Notebook Edition。
- Metaso：幻灯片、学点啥、自定义技能、视频生成。
- Komo：Firsthand、Earn。
- Andi："smart friend" 定位语。

## Vendor-specific Findings（汇总）

见 L3。要点：**不得把 Wolfram 的 API 产品线、disambiguation 机制、部署清单，或 Metaso 的技能/幻灯片外延写进 Canonical Core**。Wolfram 的 disambiguation/drilldown 是处理问句歧义的一个强实现，可支撑 L1"歧义处理"的常见性，但其形态属厂商实现。

## Rejected Findings（拒绝的候选定义）

- ❌ "Answer Engine = 用 LLM 综合网页并附行内引用的应用" ——会把 2009 年的计算型原型排除；且当代样本引用证据薄弱。降为 L1/L2（综合姿态 + 来源呈现）。
- ❌ "Answer Engine = 对话式搜索" ——会话是常见表面（L1），Wolfram 单问单答仍成立；对话深度是 L2 变体轴。
- ❌ "Answer Engine = 独立产品" ——嵌入部署（搜索结果旁、LLM 内部、Appliance）是真实形态（Wolfram 直接观察）；独立性不是定义属性。
- ❌ "Answer Engine = 消费者产品" ——API/企业/教育层（Wolfram）与开发者垂直（市场常识）都在 Type 内；客户层是变体轴。
- ❌ "有广告的是搜索引擎、无广告的是答案引擎" ——商业模式不改变结构（Metaso 以"无广告"作营销姿态，Wolfram 免费层含广告栏营销？未见直接证据——不采用）。
- ❌ 把"无广告/直达结果"的口号语言当作结构证据——仅作为定位证据使用。

## Boundary Findings（含"去掉什么就变成另一个 Type"判据）

1. **vs General Web Search Engine（§02.02）**：判据 = 主要交付物。系统产出的直接答案是主要交付物 → Answer Engine；排序后的可精炼文档/记录列表是主要交付物 → 搜索引擎（academic-search-engine 叶子 L0 即 "query → ranked record list"）。混合形态真实存在：搜索引擎把机器生成答案面嵌在结果上方（本环境未获 Tier-1 验证，措辞降级）；Wolfram API 反向嵌入搜索结果旁。**去掉"系统作答" → 搜索引擎；去掉"链接探索/文档访问" → 答案引擎（但现代答案引擎通常仍保留来源链接）。**
2. **vs AI 聊天助手/聊天机器人（目录内最近邻为 AI Research Assistant 一系及 Enterprise AI Assistant）**：判据 = 问题时的接地与归属。答案从问题时的知识材料中检索/计算/选择并通常可见来源 → 答案引擎；答案主要来自模型参数记忆、无问题时的外部接地 → 聊天助手。聊天产品加联网检索会向本 Type 漂移；判据是"接地是否为作答的主要机制"。**去掉接地 → 聊天助手。**
3. **vs AI Research Assistant（已处理，联合评审 flag）**：判据 = 研究材料基底 + 持续多步研究过程 + 持久研究工件（库/表/报告）。答案引擎 = 单问快答、无持续研究过程、无持久工件为核。该叶子记录的 removal test "remove persistence entirely and answer from the open web → Answer Engine" 与本叶一致。漂移风险：答案引擎加"deep research/项目工作区"功能向助手漂移（与该叶子记录的市场 straddling 相互印证）。**本次联合评审维持边界成立，无需 taxonomy 变更。**
4. **vs Expert Q&A Platform（§02.03 同族）**：判据 = 答案作者。人（专家/社区）写答案 → Q&A 平台；机器在问题时刻产答案 → 答案引擎。
5. **vs Knowledge Question Answering Application（§02.03 同族，待处理）**：判据 = 语料归属与用途。答案引擎跨开放/通用语料面向公众问题；KQA 绑定在组织定义的知识库（产品/企业 KB）上服务其用户/支持场景。梯度风险：Wolfram Custom（"organizational as well as public data"）与企业化答案引擎会逼近 KQA。**Flag：KQA 叶子处理时需联合评审此边界。**
6. **vs Online Encyclopedia / Dictionary / General Reference Database（§02.05）**：判据 = 内容时间性。百科/词典呈现固定的策展条目供查阅；答案引擎在问题时刻针对该问题产出响应。预生成内容（如 Wolfram Summary Boxes "pre-generated summary boxes"）出现在边缘，但主循环仍是按问生成/计算。
7. **vs Metasearch / Vertical Search Engine（§02.02）**：同 1，它们交付记录列表，不交付答案。

## Uncertainties

1. **原型产品（Perplexity 类）的 Tier-1 证据缺失**：现代 LLM 综合答案引擎的机制细节（行内引用形态、焦点模式、空间/收藏结构、深度研究模式）全部未经直接观察。最终文档只以抽象语言覆盖（综合姿态、来源呈现、会话追问），并记录局限。
2. **Andi/Metaso/Komo 的操作性细节不可观察**（JS 应用壳/薄落地页）：三者的检索机制、引用呈现、会话行为均为不可观察；所有相关 L1 断言以"常见/通常"措辞并注明证据强度。
3. **Ask Jeeves 历史谱系未验证**：历史形态（路由/选择姿态）仅作研究笔记内的 Tier-3 背景，不进最终文档断言。
4. **"搜索结果内嵌答案面"未获 Tier-1 验证**（Google/Bing 支持页超时）：边界讨论中以抽象措辞呈现，不点具体产品机制。
5. **KQA 叶子未处理**：边界 5 的判据为临时判据，待该叶子研究后联合评审。
6. **中文样本的功能外延**（Metaso 幻灯片/技能）是否代表区域趋势还是单厂商扩张，未知。

## Final Synthesis

**Answer Engine 是一种以问句为主要输入、以系统自身产出的直接答案为主要交付物的应用**：系统在问题时刻从自备的知识材料（开放索引、策展语料或知识库）中检索、计算或选择，综合/计算出对问题的响应并呈现为答案，而不是返回供用户自读的文档列表。定义核心极小且跨时代稳定：问句锚定 + 系统作答 + 问题时的接地。现代成熟产品普遍加：来源归属呈现、会话式追问、历史库、富答案呈现、歧义处理、深度分层、多表面交付与分层可用性。主要变体轴：接地基底（Web 索引 vs 策展计算语料）、语料范围、作答姿态、会话深度、独立 vs 嵌入、区域市场形态、部署与商业模式。与搜索引擎的分界在交付物（答案 vs 记录列表），与聊天助手的分界在问题时的接地，与 AI Research Assistant 的分界在持续研究过程与持久工件（联合评审维持），与 Expert Q&A 的分界在答案作者，与 KQA 的分界在语料归属（flag 待联合评审）。

STATUS 一句话（L0）：question-anchored interaction + system-performed answer (composed/computed/selected) as primary deliverable + question-time grounding in the system's own knowledge material；source attribution / conversational follow-up / history / rich presentation / disambiguation / depth tiers / multi-surface delivery are L1；grounding substrate, corpus scope, composition posture, embedded-vs-standalone, regional forms, deployment, business model are L2。
