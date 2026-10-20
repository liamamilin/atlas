{
  "confirmed_scenario": {
    "acceptance": [
      "用户主动保存的链接在多次会话之间持久保留，形成不断增长的个人收藏",
      "每条记录都以 URL 锚定到外部网页，打开记录即跳转到该页面",
      "用户可以在归类之间移动记录或新建归类，操作结果在重新打开后仍然有效",
      "通过归类浏览或关键字检索，用户能找到此前存入的特定链接"
    ],
    "audience": "习惯先把感兴趣的网页存起来、之后再回头处理的普通网络用户",
    "id": "scn_7756e0007f6a463a97316f3f49c15248",
    "leaf": "bookmark-manager",
    "leaf_name": "书签管理器",
    "name": "生活待购与灵感收藏夹",
    "objective": "把偶然看到但当下不处理的外部网页链接留存，日后需要时能重新找到并回到原页面",
    "revision": 2,
    "status": "ready",
    "updated_at": "2026-10-16T14:18:20.407897+00:00",
    "workflow": [
      "用户在浏览时看到想记住的商品页、教程或灵感图片，主动保存该链接",
      "保存时选择一个简单归类，如“待购”“家居改造”或“以后看看”",
      "未经整理的链接可先进入默认归类，之后再手动移动到更合适的位置",
      "用户在需要实际处理时打开个人库，浏览或检索相关归类",
      "用户从记录打开链接，回到原始网页继续购买、阅读或参考"
    ]
  },
  "decisions": [
    {
      "default": "单选归类（bookmark.category_id 标量外键）。场景流程明确“选择一个简单归类”，单归属让移动、计数与浏览语义无歧义；未来若需多值可迁移到关联表而不丢数据。",
      "id": "D01",
      "impact": "决定数据模型（标量外键 vs 关联表）以及浏览、计数与检索的实现路径。",
      "question": "记录应归属于单一“归类”，还是允许像标签一样同时属于多个？",
      "status": "decided",
      "when_to_ask": "当真实用户反馈同一条记录必须同时属于多个主题，或需要跨主题交叉检索时再评估多标签。"
    },
    {
      "default": "落入默认“未整理”，保存始终成功。场景流程第3步要求未经整理的链接可先进入默认归类，快速保存不应打断浏览。",
      "id": "D02",
      "impact": "决定保存接口是否允许缺省 category，以及首启预置数据内容。",
      "question": "保存时不选归类，应阻止保存还是落入默认“未整理”？",
      "status": "decided",
      "when_to_ask": "当目标用户群要求强制归类（例如团队共享库）时再改为必选。"
    },
    {
      "default": "自动创建（名称大小写不敏感去重），重名则复用现有归类；保持保存流程不中断。",
      "id": "D03",
      "impact": "决定 categories 的唯一约束、写入事务边界与 409/400 的语义；HTML 归类表单与 JSON API 共用服务层，重名、非法名与默认归类保护都不得产生部分写入。",
      "question": "在保存或移动界面输入一个尚不存在的归类名，应自动创建还是报错？",
      "status": "decided",
      "when_to_ask": "当出现拼写错误导致归类碎片化的证据时，改为只允许从既有归类中选择。"
    },
    {
      "default": "软删除：记录标记 trashed_at，默认视图排除，提供撤销恢复；场景要求可恢复的失败。",
      "id": "D04",
      "impact": "决定数据模型的 trashed_at 列、默认列表过滤条件、/restore 恢复路径，以及删除归类时活动与软删记录同迁默认归类；不引入 purge 或永久删除接口。",
      "question": "删除是立即物理删除，还是软删除到可恢复区并支持短时撤销？",
      "status": "decided",
      "when_to_ask": "当用户要求彻底清除隐私数据或回收站增长需要释放空间时，再提供永久删除与清空。"
    },
    {
      "default": "本地优先：图标由域名派生本地路由，第三方元数据抓取为可选增强且失败静默降级，保证离线可保存。",
      "id": "D05",
      "impact": "决定保存流程的时延与可用性依赖，以及收藏响应中的 favicon/title 字段形态。",
      "question": "标题、描述与图标是否依赖第三方抓取服务？",
      "status": "decided",
      "when_to_ask": "当部署环境确认可访问外部服务且用户需要富预览时再启用增强。"
    },
    {
      "default": "自 P1/F14 起默认检测并返回 409 duplicate_url（附已有 id 供跳转查看），保存方显式 allow_duplicate 时可强制新增；P0
核心用例不依赖去重，软删除记录不参与判定；场景与成熟产品都倾向一址一记录。",
      "id": "D06",
      "impact": "决定服务层去重查询、allow_duplicate 语义与导入时的合并或跳过策略（不使用 url 唯一索引）。",
      "question": "同一 URL 再次保存时，阻止还是允许？",
      "status": "decided",
      "when_to_ask": "当用户明确需要对同一地址保留多个不同上下文的记录时再放宽。"
    },
    {
      "default": "标题加域名(hostname)加描述，大小写不敏感，可与归类过滤叠加；不检索正文（无抓取）。",
      "id": "D07",
      "impact": "决定查询实现与检索参数语义：category 与 q 可叠加，HTML 归类检索表单必须同时保留两者；计数与列表只统计未软删记录，移动、删除、恢复后保持一致。",
      "question": "关键字应匹配哪些字段？",
      "status": "decided",
      "when_to_ask": "当需要按网页正文全文检索时再引入抓取与索引（属后期能力）。"
    },
    {
      "default": "python-web 加 Python 3.12 标准库 http.server 加单文件 SQLite；满足离线、单用户与可独立验收，无需外部依赖。",
      "id": "D08",
      "impact": "决定交付 profile 为 python-web（Python 3.12 标准库 + SQLite + 服务端渲染 HTML），验收通过独立 HTTP 实例与真实表单提交进行。",
      "question": "采用何种运行时与持久化方式？",
      "status": "decided",
      "when_to_ask": "当需要多用户、并发写入或托管部署时再引入 Web 框架与服务端数据库。"
    },
    {
      "default": "默认无认证；交付进程在独立验收网络中监听测试者可路由的接口（`--host 0.0.0.0`），日常本机使用可绑定 127.0.0.1；不引入凭据文件，符合个人本地库的定位。",
      "id": "D09",
      "impact": "决定部署方式与验收的认证契约（验收默认不携带凭据）。",
      "question": "是否需要登录或口令？",
      "status": "decided",
      "when_to_ask": "当应用需要暴露到局域网或公网时，必须加入认证，否则只允许本机绑定。"
    },
    {
      "default": "Netscape 浏览器书签 HTML（本类型的交换约定），归类映射为文件夹或标签字段。",
      "id": "D10",
      "impact": "决定 P1 导入/导出的解析与生成实现。",
      "question": "导入/导出采用什么格式？",
      "status": "decided",
      "when_to_ask": "当需要与某个具体产品双向同步时再适配其专有格式。"
    },
    {
      "default": "P0 不做：本地单实例，数据在单一 SQLite 文件；跨设备属后期能力。",
      "id": "D11",
      "impact": "影响运行形态与数据归属，不阻塞 P0 核心旅程。",
      "question": "是否提供云同步或多用户共享？",
      "status": "deferred",
      "when_to_ask": "当用户明确需要在多设备访问同一库时再设计同步或托管。"
    },
    {
      "default": "P0 使用扁平单选归类加“未整理”收件区；嵌套与标签属成熟能力，按需在后期启用。",
      "id": "D12",
      "impact": "影响侧栏结构与检索实现，可后续迁移而不破坏现有数据。",
      "question": "归类是否需要嵌套层级，或与标签并存？",
      "status": "deferred",
      "when_to_ask": "当扁平归类数量增长到难以浏览，或需要交叉主题时。"
    },
    {
      "default": "本期不做：抓取与归档在离线验收下不可验证；先保证引用记录与打开回跳。",
      "id": "D13",
      "impact": "涉及外部抓取与存储扩展，属后期可选能力，不纳入 P0/P1 验收。",
      "question": "是否需要保存网页副本并检测失效链接？",
      "status": "open",
      "when_to_ask": "当用户明确要求内容留存，或需要清理死链时再评估。"
    }
  ],
  "features": [
    {
      "acceptance": [
        "A01",
        "A02",
        "A03",
        "A12"
      ],
      "applicability": "current required",
      "id": "F01",
      "name": "保存收藏（URL 必填，标题/描述可选）",
      "phase": "P0",
      "reason": "场景流程第1-2步要求看到想记住的页面即主动保存；S02 记录新记录字段、hostname 派生及编辑时保留的身份字段，S04 记录上游表单 URL 与其他字段校验，S06
记录保存写入。标题/描述可选及本模板保存合同是目标设计，不把 S04 当作编辑回填观察。",
      "sources": [
        "S02",
        "S04",
        "S06"
      ]
    },
    {
      "acceptance": [
        "A03"
      ],
      "applicability": "current required",
      "id": "F02",
      "name": "默认“未整理”与预置归类集合",
      "phase": "P0",
      "reason": "场景流程第3步要求未整理的链接先进入默认归类；S16/S20 提供标签筛选与聚合计数的借鉴。默认“未整理”收件区与独立归类实体是目标新设计，依据当前场景事实中的标签必填/归类限制推断及既有 case-
design；不把单条列表筛选观察当作整个项目没有默认归类的证明。",
      "sources": [
        "S16",
        "S20"
      ]
    },
    {
      "acceptance": [
        "A04"
      ],
      "applicability": "current required",
      "id": "F03",
      "name": "归类管理（新建/重命名/删除）",
      "phase": "P0",
      "reason": "场景验收第3条要求可新建归类；独立归类实体及其新建、重命名、删除和持久化是目标新设计。S16/S20 记录标签筛选和聚合行为，当前场景事实与既有 case-design
的归类限制推断说明标签模型与目标归类实体的差异；不以单条筛选观察证明整个项目的能力缺失。",
      "sources": [
        "S16",
        "S20"
      ]
    },
    {
      "acceptance": [
        "A05",
        "A12"
      ],
      "applicability": "current required",
      "id": "F04",
      "name": "记录在归类间移动",
      "phase": "P0",
      "reason": "场景验收第3条要求记录可在归类之间移动且重开后仍有效；上游检索按标签交集筛选（S16），这里把多值交集改造为单一归属迁移。",
      "sources": [
        "S16"
      ]
    },
    {
      "acceptance": [
        "A06"
      ],
      "applicability": "current required",
      "id": "F05",
      "name": "归类浏览与条目计数",
      "phase": "P0",
      "reason": "场景验收第4条要求通过归类浏览找回；上游侧栏按标签聚合计数（S20、S16），改为按归类聚合与筛选。",
      "sources": [
        "S16",
        "S20"
      ]
    },
    {
      "acceptance": [
        "A07"
      ],
      "applicability": "current required",
      "id": "F06",
      "name": "关键字检索（标题/域名/描述）",
      "phase": "P0",
      "reason": "场景验收第4条要求关键字检索；上游仅匹配标题小写（S16），需扩展到域名与描述以覆盖只记得来源的场景。",
      "sources": [
        "S16"
      ]
    },
    {
      "acceptance": [
        "A08"
      ],
      "applicability": "current required",
      "id": "F07",
      "name": "打开原始网页（URL 锚定与回跳）",
      "phase": "P0",
      "reason": "场景验收第2条与流程第5步要求打开记录即回到原页；S15 直接记录 Visit 更新访问计数/时间后以 window.open(item.url, _blank, noopener,noreferrer)
打开原 URL。目标保留原 URL 导航与打开的安全意图，去掉访问统计，不依赖额外工具或字段类型来源来证明打开行为。",
      "sources": [
        "S15"
      ]
    },
    {
      "acceptance": [
        "A01",
        "A05",
        "A09"
      ],
      "applicability": "current required",
      "id": "F08",
      "name": "多会话持久化（跨重启保留）",
      "phase": "P0",
      "reason": "场景验收第1条（S01）要求跨会话持久保留；S06 记录保存/删除写入，S13 记录组件创建时从数据库载入记录到内存映射。Python 服务端
SQLite、跨服务端重启保留、事务处理与逐请求数据库查询是目标设计，不冒充上游实现；不宣称浏览器 profile 持久化、多设备同步或客户端内存映射是目标存储合同。",
      "sources": [
        "S01",
        "S06",
        "S13"
      ]
    },
    {
      "acceptance": [
        "A09"
      ],
      "applicability": "current required",
      "id": "F09",
      "name": "删除与撤销恢复",
      "phase": "P0",
      "reason": "场景要求可恢复的失败；S07 记录仅归档条目可删除及 Undo
调用保存恢复，但未给出精确恢复时长。目标删除/恢复合同保持不变：去掉“仅归档可删”前置限制，以可恢复回收状态提供兜底，不从源观察推导固定秒数。",
      "sources": [
        "S07"
      ]
    },
    {
      "acceptance": [
        "A02",
        "A10",
        "A12"
      ],
      "applicability": "current required",
      "id": "F10",
      "name": "输入校验与错误合同",
      "phase": "P0",
      "reason": "S04 记录上游 Valibot 表单对 URL、标题、描述和标签的约束，S02 记录新记录保存派生 hostname。目标按既定合同使用绝对 HTTP(S) URL 解析、允许单标签
hostname、保留原始 URL 文本，并为保存与移动提供明确错误和无写入失败；这些是 adjusted 设计，不把上游点域名正则或标签必填作为目标规则。",
      "sources": [
        "S04",
        "S02"
      ]
    },
    {
      "acceptance": [
        "A11"
      ],
      "applicability": "current required",
      "id": "F11",
      "name": "本地应用外壳与首启（空库）",
      "phase": "P0",
      "reason": "本模板面向单用户本地工具；Python 服务端渲染的 HTML
页面与表单（POST/redirect/GET）、首启空库视图及保存—浏览—检索—打开闭环是目标交付设计，不宣称源包已经提供这些服务端行为，也不以未纳入当前来源索引的挂载入口作依据。",
      "sources": []
    },
    {
      "acceptance": [
        "A13"
      ],
      "applicability": "later",
      "id": "F12",
      "name": "元数据与图标增强（离线降级）",
      "phase": "P1",
      "reason": "S14 记录 Google favicon 经 images.weserv.nl 获取及失败日志，S21 记录 api.microlink.io 元数据和 images.weserv.nl logo
请求及失败处理。目标保留既定 P1 可选增强与离线降级定位，不使这些外部端点成为 P0 可用性依赖；本地 hostname 展示与增强降级属于目标设计，不把端点可用性写成已验证事实。",
      "sources": [
        "S14",
        "S21"
      ]
    },
    {
      "acceptance": [
        "A14"
      ],
      "applicability": "later",
      "id": "F13",
      "name": "导入/导出（浏览器书签 HTML）",
      "phase": "P1",
      "reason": "浏览器书签 HTML 导入/导出是本模板后期互操作设计选择，保留 F13/P1/A14；它是目标路线图，不构成对上游导入/导出能力存在或缺失的断言。",
      "sources": []
    },
    {
      "acceptance": [
        "A15"
      ],
      "applicability": "later",
      "id": "F14",
      "name": "重复链接检测",
      "phase": "P1",
      "reason": "重复链接检测是本模板后期设计选择，保留 F14/P1/A15、原 D06 以及保存/导入路径的既定目标；P0
核心用例不依赖该能力。不以列表筛选或记录类型观察证明上游完全没有去重，也不宣称已经验证其能力缺失。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F15",
      "name": "浏览器扩展/分享目标抓取",
      "phase": null,
      "reason": "场景交付为本地 Web 工具，扩展与移动分享目标不在本期范围，手工录入与打开回跳已覆盖核心旅程。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F16",
      "name": "多设备与云同步",
      "phase": null,
      "reason": "本期是单机单实例的本地库，数据在单一 SQLite 文件；跨设备同步属后期形态，不阻塞核心旅程。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "decision needed",
      "id": "F17",
      "name": "网页留存副本/快照",
      "phase": null,
      "reason": "本模板 P0 只保存 URL 引用而不保存网页副本；网页留存仍为 decision needed，须用户明确需求后再决定外部抓取与存储方案。此处说明目标范围，不据当前不可用类型来源断言上游完整能力边界。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "decision needed",
      "id": "F18",
      "name": "失效链接检测与修复",
      "phase": null,
      "reason": "链接腐坏是本类型的结构性风险，但检测需要主动外呼，外部网络在验收中禁用；先保证引用与打开回跳，是否检测待用户决定。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "decision needed",
      "id": "F19",
      "name": "嵌套归类与多标签并存",
      "phase": null,
      "reason": "场景明说“选择一个简单归类”，扁平单选加收件区已足够；嵌套/标签是成熟能力，待归类数量或交叉主题增长时再评估。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F20",
      "name": "置顶/归档与多排序模式",
      "phase": null,
      "reason": "上游置顶与归档、三种排序属书签阅读器语境（S19、S16、S03），会给编辑与删除增加前置条件，与快速保存、快速清理相冲突，故不采用。",
      "sources": [
        "S19",
        "S16",
        "S03"
      ]
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F21",
      "name": "公开分享与协作库",
      "phase": null,
      "reason": "场景是私有个人收藏箱，分享不在核心旅程内；公开或协作需要多用户身份与权限，属不同类型定位。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F22",
      "name": "阅读稍后与未读标记",
      "phase": null,
      "reason": "场景重心是留存引用并可回跳，而非消费队列；未读标记会使产品向 Read-it-later 漂移。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F23",
      "name": "复制 URL 动作",
      "phase": null,
      "reason": "上游提供 Copy URL（S12），但本场景终点是打开原页而非分发链接，去掉可减少每条记录的操作噪音。",
      "sources": [
        "S12"
      ]
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F24",
      "name": "访问计数与最近访问时间",
      "phase": null,
      "reason": "S15 直接记录 Visit 更新 visitCount 与 visitedAt 后打开原 URL；场景只需打开动作，目标不保留这两个访问统计字段，不再额外引用未纳入当前场景来源索引的类型定义。",
      "sources": [
        "S15"
      ]
    }
  ],
  "limits": [
    "不实现云同步、多用户共享或托管部署（D11、F16、F21）。",
    "不保存网页快照、不做正文全文检索、不做失效链接检测（F17、F18、D13）。",
    "不引入置顶/归档、多排序模式、复制 URL 与访问计数（F20、F23、F24）。",
    "归类为扁平单选，不支持嵌套层级或多标签并存（F19、D01）。",
    "第三方元数据与图标抓取未验证可达性，仅作可选增强且失败静默降级（F12、D05）。",
    "验收不携带认证凭据；若目标要求认证，验收必须显式报告基础设施未就绪而非跳过或通过（D09）。",
    "不设置未经验证的性能或成本目标。"
  ],
  "roles": [
    {
      "id": "R01",
      "name": "收藏者（个人用户）",
      "responsibility": "在浏览时主动保存外部网页链接，选择或新建简单归类、把未整理的链接移动到合适归类、按归类或关键字找回、打开记录回到原页，并清理误存条目。"
    },
    {
      "id": "R02",
      "name": "本地收藏应用（服务端与页面外壳）",
      "responsibility": "校验录入、派生域名、持久化收藏与归类、提供保存/浏览/检索/打开/恢复接口，并在离线条件下保持可用。"
    },
    {
      "id": "R03",
      "name": "独立验收执行者",
      "responsibility": "以 URL 与 CLI 参数驱动真实目标，执行正负向行为断言、重启持久化验证与错误恢复验证，不修改应用、不自报运行结果。"
    }
  ],
  "source_citation_matrix": {
    "facts_view_digest": "241bf3d99ff497c30be8349cbc70529e08df6146736cb749b55268271889aa4b",
    "features": [
      {
        "feature_id": "F01",
        "source_ids": [
          "S02",
          "S04",
          "S06"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_05babdea64ba9858",
            "id": "S02",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_1596da4a90687ca5",
            "id": "S04",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_35e41aab676021eb",
            "id": "S06",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F02",
        "source_ids": [
          "S16",
          "S20"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_9ab6b0e51811a16d",
            "id": "S16",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_c4ad7e52e5713628",
            "id": "S20",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F03",
        "source_ids": [
          "S16",
          "S20"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_9ab6b0e51811a16d",
            "id": "S16",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_c4ad7e52e5713628",
            "id": "S20",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F04",
        "source_ids": [
          "S16"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_9ab6b0e51811a16d",
            "id": "S16",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F05",
        "source_ids": [
          "S16",
          "S20"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_9ab6b0e51811a16d",
            "id": "S16",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_c4ad7e52e5713628",
            "id": "S20",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F06",
        "source_ids": [
          "S16"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_9ab6b0e51811a16d",
            "id": "S16",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F07",
        "source_ids": [
          "S15"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_93ff254508846f11",
            "id": "S15",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F08",
        "source_ids": [
          "S01",
          "S06",
          "S13"
        ],
        "sources": [
          {
            "evidence_id": null,
            "id": "S01",
            "kind": "confirmed_input",
            "source_path": "inputs/scenario.json",
            "version": "scn_7756e0007f6a463a97316f3f49c15248@2"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_35e41aab676021eb",
            "id": "S06",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_86ed2327f33a3ca8",
            "id": "S13",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F09",
        "source_ids": [
          "S07"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_4c56ef30a1785be1",
            "id": "S07",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F10",
        "source_ids": [
          "S04",
          "S02"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_1596da4a90687ca5",
            "id": "S04",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_05babdea64ba9858",
            "id": "S02",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F11",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F12",
        "source_ids": [
          "S14",
          "S21"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_8e11efc61a4650ba",
            "id": "S14",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_ec303a2fd1afa287",
            "id": "S21",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F13",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F14",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F15",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F16",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F17",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F18",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F19",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F20",
        "source_ids": [
          "S19",
          "S16",
          "S03"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_b1ca64cf2ad02998",
            "id": "S19",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_9ab6b0e51811a16d",
            "id": "S16",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          },
          {
            "evidence_id": "ev_ba200adf6e2c_06c81a165e03c96a",
            "id": "S03",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F21",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F22",
        "source_ids": [],
        "sources": []
      },
      {
        "feature_id": "F23",
        "source_ids": [
          "S12"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_7150b0ac7a5678db",
            "id": "S12",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      },
      {
        "feature_id": "F24",
        "source_ids": [
          "S15"
        ],
        "sources": [
          {
            "evidence_id": "ev_ba200adf6e2c_93ff254508846f11",
            "id": "S15",
            "kind": "code_observation",
            "source_path": "src/App.tsrx",
            "version": "539881bc67099d491e8ab6f85de0f443fa7de623"
          }
        ]
      }
    ],
    "schema": "atlas.source-citation-matrix.v1"
  },
  "source_manifest_digest": "2353618bca8208641f5333320abc536d4e495c2b78c1f26c16e9d1f2ad6c4e03"
}