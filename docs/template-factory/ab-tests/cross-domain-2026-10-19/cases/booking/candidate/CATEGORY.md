# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

类别事实：Amenity Booking Platform 的核心是运营方定义的设施清单、封闭的居民/租户名单、设施×时段×预约人的限时预约以及楼宇侧控制面。成熟产品的可识别能力包括：可用性日历/时段、请求→审批（部分设施可自动批准）、按设施展示规则（客人上限、营业时间、费用、押金、材料要求）、取消/修改与闭馆封禁、通知、管理员代订与历史记录、列表与日历双视图。S02–S07 的厂商文档一致支持审批状态、自动批准、按设施规则、代订与日历视图等行为；S08–S10 显示开源侧多为通用资源/会议室预约（LibreBooking、MRBS）或轻量 Django 模块，并非针对建筑共享设施的完整实现。场景建议：本场景是本地回环最小演示（1 名管理员 + 2 名居民），应把类别核心做扎实——服务端权限不可伪造、ISO8601 带时区真实时刻比较、结束晚于开始、半开区间相邻可预约而重叠不可、并发下同一设施重叠最多一笔成功、不同设施互不阻塞、取消幂等且保留状态、重启后一致；S11 的区间/唯一或排除约束思路可作为防重复占用的实现参考（是否采用取决于所选数据库）。邮件、真实住户、支付、押金、公网身份、导出与审计等企业能力在本场景属非必需，仅需预留清晰的状态与记录字段以便后续扩展，不应强行引入。复用与自建：厂商产品（BuildingLink、Vantaca、CINC、Yardi）为闭源 SaaS，只能作为行为参考；开源备选均有许可与适配成本——LibreBooking 为 GPL-3.0、MRBS 为 GPL-2.0（copyleft，直接复用会带来许可义务），django-reservations 许可非标准且长期未维护；对如此小的本地演示，自建比引入 copyleft 或陈旧代码更合适。本次为模型报告的来源证据，非独立运行或法律核验。

## S01 · Atlas confirmed input

inputs/scenario.json · experiment-booking@1

管理员配置设施，居民登录后选择时段预约、查看自己的预约并取消；同一设施不能被重复占用，权限由服务端执行。

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · BuildingLink Staff Help Site — Amenity Reservations

https://help-staff.buildinglink.com/en/support/solutions/articles/42000098635-amenity-reservations · 访问日期 2026-10-19；仅经搜索呈现，未抓取完整页面

运营文档描述 Amenity Reservations 模块：非管理层用户提交的请求状态自动为 Requested，只有 Management/Security Officer 级用户可 Approve/Decline/Cancel；管理层录入时可把状态由 Requested 改为 Approved 以自动批准；可按设施类型设为免审批自动批准；支持代表居民创建预约、按重复方式排期、日历视图、给预约添加 Note/Log（如提醒补交材料或付款）；可配置新请求与变更的通知接收人，并让居民在批准或拒绝时自动收到通知；模块可设为 Internal Only。

非代码（厂商 SaaS 文档）



仅作行为参考，代码不可复用

## S03 · BuildingLink Staff Help — Product Update: Amenity Reservation Settings / Amenity Settings

https://help-staff.buildinglink.com/en/support/solutions/articles/42000111019-product-update-amenity-reservation-settings · 访问日期 2026-10-19；仅经搜索呈现

产品更新页面说明 Amenity Reservations 的通知默认选项在 Manage > Reservations > Settings 配置；Amenity Settings 页面说明 Manager 或 Security Officer 可在 Settings > Amenity Reservations 新增设施类型。

非代码（厂商 SaaS 文档）



仅作行为参考

## S04 · BuildingLink Resident Help Site — Amenity Reservations

https://help-resident.buildinglink.com/en/support/solutions/articles/42000104467-amenity-reservations · 访问日期 2026-10-19；仅经搜索呈现

居民侧文档说明居民在 Amenity Reservations 日历视图可见全部或仅部分请求取决于物业设置；不需要管理层批准的设施，请求提交后自动进入 Approved 状态。

非代码（厂商 SaaS 文档）



仅作行为参考

## S05 · Vantaca Support — Best Practice: Calendar & Amenity Reservations / Enabling Amenity Reservations for your Home Portal

https://support.vantaca.com/hc/en-us/articles/360056872551-Best-Practice-Calendar-Amenity-Reservations · 访问日期 2026-10-19；仅经搜索呈现

支持文章描述预约工作流步骤：第一步 Reservation Request Received 可自动流转到 Reservation Confirmed，某一步为 closing step；董事会成员可对 amenity reservation action items 执行 Approve 或 Decline；Enabling Amenity Reservations 文章提到可在日历上显示预约流程步骤以帮助业主了解所处阶段；官网博客称预约请求发送给管理方审批，业主可查看可用性并请求预约。

非代码（厂商 SaaS 文档）



仅作行为参考（协会/HOA 侧）

## S06 · CINC Systems — Boards + Residents（含 CINC Connect / RESERVE 与知识库）

https://cincsystems.com/boards-residents · 访问日期 2026-10-19；仅经搜索呈现

Boards + Residents 页面称居民可在线完成预约并在同一处查看详情，预约前可查看 rules、guest limits、fees、deposits 或其他要求；CINC Connect 公告列出 clubhouses、tennis courts、pools 等 amenity reservations；RESERVE 模块让业主在线预订、支付并管理社区设施预约；知识库含 How to Reserve an Amenity（仅见标题）。

非代码（厂商 SaaS 文档）



仅作行为参考

## S07 · Yardi — Concierge IQ / RentCafe Resident Portal

https://www.yardi.com/product/concierge-iq/ · 访问日期 2026-10-19；经搜索呈现（含一份 RentCafe 说明 PDF 片段）

Concierge IQ 产品页称允许居民通过 RentCafe Resident Portal 直接预订 clubhouse 或 hospitality 空间，并把预订接入门户以保持管理可控；RentCafe Resident Portal 产品页把 amenity 相关能力列为居民门户的一部分；搜索到的 RentCafe 说明 PDF 片段称部分设施需在 Resident Services Team 批准请求后立即支付 250 美元押金。

非代码（厂商 SaaS 文档）



仅作行为参考（押金/审批与账单衔接）

## S08 · LibreBooking — 开源资源预约系统（GitHub）

https://github.com/LibreBooking/librebooking · develop 分支（未固定提交），访问日期 2026-10-19

开源资源预约解决方案；特性含多资源预约与 waitlist、基于角色的访问控制（RBAC）、预约配额与 credits、细粒度使用报表、插件架构、通过 ics 的 Outlook/Thunderbird 集成；fork 自 Booked Scheduler 2020 年最后开源版；README 安全公告称 7.1.0 之前 Remember Me cookie 可被伪造以冒充任意用户（含管理员），7.0.0 之前存在管理员接管漏洞。

GPL-3.0

https://github.com/LibreBooking/librebooking/blob/develop/LICENSE.md

代码为 copyleft（GPL-3.0），直接复用会带来传染性许可义务；建议仅参考其多资源/配额/RBAC 行为模型，不复制源码

## S09 · MRBS (Meeting Room Booking System)（GitHub）

https://github.com/meeting-room-booking-system/mrbs-code · master 分支（未固定提交），访问日期 2026-10-19

PHP 会议/资源预约系统，房间按 building/area 分组并以并列视图展示；默认 db 认证下首个用户创建管理员；要求 PHP 7.2+ 与 MySQL 5.5.3+/PostgreSQL 8.2+；定位为自托管、可自行掌控数据的共享空间预约。

GPL-2.0（另打包第三方组件 MIT / LGPL-2.1 / Apache-2.0 / CC BY-SA 4.0）

https://github.com/meeting-room-booking-system/mrbs-code/blob/master/LICENSE

GPL-2.0 copyleft；作为相邻类别（通用房间/资源）行为参考，源码复用需满足 GPL 义务

## S10 · bernii/django-reservations（GitHub）

https://github.com/bernii/django-reservations · master 分支（未固定提交），访问日期 2026-10-19

Django 预约模块：可自定义预约模型、设置单次/多次与每日/每月预约上限、Ajax 日历、预约相关自动邮件、自定义 Django Admin、i18n；仓库仅 14 次提交，配置停留在 travis 与 syncdb 时代，维护活跃度低。

WOW License（作者自定义非标准宽松许可，非 OSI 标准名称），许可文本声明 No rights reserved 并授予自由使用

https://github.com/bernii/django-reservations/blob/master/LICENSE

许可宽松但非标准且项目老旧未维护，跨栈复用价值不确定；建议只参考其配额与邮件思路

## S11 · PostgreSQL 官方文档 — Range Types（含 exclusion constraints）

https://www.postgresql.org/docs/current/rangetypes.html · current 版本文档，访问日期 2026-10-19；仅经搜索呈现，未抓取完整文档

官方文档说明内置 range 类型（含带时区时间戳范围 tstzrange）及 exclusion constraint 可表达诸如“不得重叠”的约束，防止任何重叠值写入；范围默认边界约定为下含上不含 [)。

非代码（PostgreSQL 官方文档）



可作为数据层防重叠/并发写入的技术模式参考（前提是选用 PostgreSQL），属实现技术而非类别产品

## 待验证

- BuildingLink、Vantaca、CINC、Yardi 各页面仅通过搜索结果呈现获得，未抓取完整文档（webfetch 仅允许 github/raw/docs.python.org/docs.npmjs.com），因此其重叠时段是硬阻止还是依赖审批、精确的时长/容量/通知规则均未确认
- 没有任何厂商完整文档确认以带时区 ISO8601 存储时段、半开区间相邻可预约的语义，也未确认并发竞争下“同一设施重叠最多一笔成功”的强保证
- Vantaca/CINC/Yardi 的审批、取消释放、闭馆封禁等流程细节为片段级证据，未经完整文档核实
- 未找到有文档的、面向建筑共享设施的专属开源项目；S08–S10 均为相邻的通用资源/会议室预约或轻量模块，类别不完全等同
- 厂商产品的审计轨迹、导出、数据生命周期、恢复与账单/押金自动化细节未获官方文档确认；CINC/HomeHerald 的第三方比较页与 Yardi Relay 博客属非官方来源，未采用为事实
- django-reservations 的 WOW License 为非标准自定许可，非 OSI 认可名称，法律含义未核验
- PostgreSQL 文档条目为搜索呈现，未抓取完整页面；未验证本场景实际使用的数据库是否支持 exclusion constraint
- 未评估任何具体实现栈（语言/框架/数据库），故复用与自建建议停留在模式层面
