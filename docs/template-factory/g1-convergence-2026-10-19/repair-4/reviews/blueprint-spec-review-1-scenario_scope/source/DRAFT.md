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
  "features": [
    {
      "acceptance": [
        "A01",
        "A02",
        "A03"
      ],
      "applicability": "current required",
      "id": "F01",
      "name": "保存收藏（URL 必填，标题/描述可选）",
      "phase": "P0",
      "reason": "场景流程第1-2步要求看到想记住的页面即主动保存；上游记录了新记录默认字段与保存落盘（S02、S06），并把 URL 校验与编辑回填收敛在表单（S04）。",
      "sources": [
        "S02",
        "S04",
        "S06",
        "S17"
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
      "reason": "场景流程第3步要求未整理的链接先进入默认归类；上游只有 Home/Archived 视图、无默认桶（S16），故按场景新增默认收件区，并借鉴其标签聚合思路（S20）。",
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
      "reason": "场景验收第3条要求可新建归类；上游明确没有 collections/folders（S16），因此归类实体与增删改必须新设计并落库。",
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
      "reason": "场景验收第2条与流程第5步要求打开记录即回到原页；上游 Visit 以 window.open(noopener,noreferrer) 打开并由 URL
派生域名（S15、S08），保留打开与派生、去掉访问计数。",
      "sources": [
        "S15",
        "S08"
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
      "reason": "场景验收第1条要求多次会话之间持久保留；源包以 Dexie/IndexedDB 落盘并在启动时全量载入（S09、S13、S06），README 定位 local-
first（S11）。目标保留本地单用户与跨会话/跨重启持久化的行为，但把存储实现调整为 Python 服务端 SQLite：不宣称浏览器 profile 持久化、多设备同步或客户端内存映射是目标设计；每个请求从数据库查询。",
      "sources": [
        "S09",
        "S13",
        "S06",
        "S11"
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
      "reason": "场景要求可恢复的失败；上游删除配 5 秒 Undo 恢复（S07），去掉“仅归档可删”前置限制，保留删除加恢复的兜底。",
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
      "reason": "上游以 Valibot 约束 http/https、标题长度与标签数量（S04），并由 getHostname 派生域名（S08）；场景把标签必填改为可选归类，需要显式错误的保存与移动契约。",
      "sources": [
        "S04",
        "S08"
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
      "reason": "场景是单用户本地工具；源包 index.html 提供 #root 并由客户端入口挂载 SPA（S10、S18）。目标外壳调整为 Python 服务端渲染的 HTML
页面与表单（POST/redirect/GET），保留保存—浏览—检索—打开的用户闭环与空库就绪视图，不采用 SPA 挂载或客户端对话框状态。",
      "sources": [
        "S10",
        "S18"
      ]
    },
    {
      "acceptance": [
        "A13"
      ],
      "applicability": "later",
      "id": "F12",
      "name": "元数据与图标增强（离线降级）",
      "phase": "P1",
      "reason": "场景希望一眼辨认商品页/教程/灵感图，但上游依赖 api.microlink.io、images.weserv.nl 与 Google favicon 三个未验证端点且失败仅
console.error（S14、S21、S08）；因此把可用性依赖降为本地域名派生，外部抓取降级为可选增强。",
      "sources": [
        "S14",
        "S21",
        "S08"
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
      "reason": "互操作是成熟产品的标准配置，但上游 manifest 没有导入/导出（S22 无测试脚本、无导入导出能力），属场景后期新增。",
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
      "reason": "成熟产品趋向一址一记录，上游未实现去重（S16、S17 无重复处理）；P1 在保存与导入路径新增服务层重复检测（D06），P0 核心用例不依赖该能力。",
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
      "reason": "记录只保证引用而非内容（场景与原类型定义如此）；是否保存副本依赖外部抓取与存储，离线验收不可验证，需用户明确要求后再定。",
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
      "reason": "上游 Visit 会累加 visitCount 与 visitedAt（S15、S17）；场景只需打开动作，不需访问统计，故不保留这两个字段。",
      "sources": [
        "S15",
        "S17"
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
  "phases": [
    {
      "acceptance": [
        "A01",
        "A02",
        "A03",
        "A04",
        "A05",
        "A06",
        "A07",
        "A08",
        "A09",
        "A10",
        "A11",
        "A12"
      ],
      "features": [
        "F01",
        "F02",
        "F03",
        "F04",
        "F05",
        "F06",
        "F07",
        "F08",
        "F09",
        "F10",
        "F11"
      ],
      "goal": "用户可保存链接（可选归类或落入未整理）、按归类或关键字找回、打开原页、清理并撤销，且全部数据跨会话与重启保留，非法输入得到可恢复的明确错误。",
      "id": "P0",
      "status": "not implemented",
      "title": "个人收藏箱核心旅程"
    },
    {
      "acceptance": [
        "A13",
        "A14",
        "A15"
      ],
      "features": [
        "F12",
        "F13",
        "F14"
      ],
      "goal": "在离线可用的前提下增强记录可辨识度（本地派生图标、外部抓取仅作增强），并支持浏览器书签格式的导入导出与重复链接检测，用于长期库维护。",
      "id": "P1",
      "status": "not implemented",
      "title": "成熟增强：元数据、互操作与库清理"
    }
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
  "title": "生活待购与灵感收藏夹"
}