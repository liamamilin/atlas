# 品类认知与来源

查阅日期：2026-10-17。以下为来源事实及本样板推导，未运行这些第三方产品；不把单个产品的扩展当作品类必须具备的能力。

## S01 · Atlas 已确认书签场景 r2

[原始资料](inputs/scenario.json) · scn_7756e0007f6a463a97316f3f49c15248@2

事实：保存个人 URL 引用；可归类、检索、再次进入保留并返回原网页。

许可证记录：既有项目资料；不作为第三方代码许可证

选型判断：需求来源，不复制完整上游代码。

## S02 · Raindrop：归类

[原始资料](https://help.raindrop.io/collections/) · 2026-10-17 查阅；在线文档未固定 commit

事实：提供收件箱、分类移动与回收站；说明组织与删除恢复是不同生命周期。

许可证记录：文档用于研究；本包未取得其 SaaS 源码复用许可

选型判断：行为研究，不复制 UI、源码或文案。

## S03 · Raindrop：导出与备份

[原始资料](https://help.raindrop.io/export/) · 2026-10-17 查阅；在线文档未固定 commit

事实：区分全量与部分导出，并提供可迁移的备份路径。

许可证记录：文档用于研究，不作为代码复用依据

选型判断：为数据可带走能力提供依据，不承诺与该服务格式完全兼容。

## S04 · linkding

[原始资料](https://github.com/sissbruecker/linkding) · 2026-10-17 查阅 master；未固定源码，不直接复制

事实：自托管书签工具，提供标签、批量编辑、导入导出和 REST API。

许可证记录：MIT · [原文](https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt)

选型判断：若目标是自托管账户型服务可考虑部署或集成；本地样板只参考能力，未复制代码。

## S05 · Linkwarden

[原始资料](https://github.com/linkwarden/linkwarden/blob/main/README.md) · 2026-10-17 查阅 main；未固定源码，不直接复制

事实：协作与网页保存型产品，包含成员权限和网页副本；说明此类能力会改变部署与范围。

许可证记录：GNU AGPL version 3（原文名称；未断言 only/or-later） · [原文](https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md)

选型判断：协作/存档需求出现时再评估；本场景不复制或依赖其代码。

## S06 · 既有本地书签代码候选

[原始资料](https://github.com/LakhindarPal/bookmark-manager/tree/539881bc67099d491e8ab6f85de0f443fa7de623) · 539881bc67099d491e8ab6f85de0f443fa7de623

事实：Atlas 旧试产已验证保存、归类、检索、重开与外链；这不证明本认知包或后续阶段已通过。

许可证记录：MIT · [原文](https://github.com/LakhindarPal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/LICENSE)

选型判断：可选参考；旧代码和旧验收保持原版本，本样板不包含该仓库代码。

## S07 · MDN：IndexedDB

[原始资料](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB) · 2026-10-17 查阅

事实：浏览器结构化持久存储及事务机制；用于本地库默认选型。

许可证记录：平台文档研究；参考模块为本项目新编写

选型判断：使用平台 API；写入成功需以事务 complete 为准。

## S08 · MDN：localStorage

[原始资料](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) · 2026-10-17 查阅

事实：浏览器本地存储属于来源；不能把浏览器存储当作云同步或备份保证。

许可证记录：平台文档研究

选型判断：本样板默认 IndexedDB；明确存储被清理的边界。

## 复用、自建与待验证

直接使用现成 SaaS 适合接受其账户/托管方式的人；自托管账户型需求可先评估 linkding，协作与网页副本需求可评估 Linkwarden。当前选择自建轻量本地库，是针对当前场景的默认，不是认定这些产品不好用。未复制任何上游源码；后续若复用，需先固定版本、核对具体文件及许可，不能根据仓库标题推断全部模块都可直接复制。

本地 IndexedDB、JSON 可带走、URL 校验等选择是设计推导，不是上述产品均采用的共同架构。托管权限、计费、后台、审计与备份恢复均已进入能力地图，是否实现由场景和项目决策决定。
