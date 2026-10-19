# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

类别事实：leaf 把预算应用的四项定义锁定为『绑定期间的支出计划 + 分配到用途的额度 + 应用内实际支出 + 计划/实际/剩余比较态』，成熟产品的差异集中在实现方式。YNAB/Goodbudget 走信封或零基路线且把 Fill/分配当作显式动作；Monarch 与 Quicken Simplifi 以收入自动生成计划并强调一个『还剩多少』数字（Left this month / Remaining）；Fudget 证明无账户、无银行连接的最小清单形态（计划项 − 实际项 = 剩余）即可成立。跨产品的共同行为：消费前的剩余额是核心输出；未分配额是被推导而非直接输入的；超支是合法状态（负剩余，可结转进下月，如 Monarch 的 Rollover 公式）；对过去日期的补记/改账会按 running balance 重算当前余额（Goodbudget 明确说明）；计划可随时修改、按期间隔离、不追溯；导出以 CSV 为主。金额精度上，YNAB 用整数 milliunits，Python decimal 文档给出精确十进制与 quantize 的会计级做法，避免二进制浮点误差。
针对本场景（单个本地用户、人民币、无银行/支付连接、按月中文本地数据）：适用的是 Fudget/Goodbudget 的手动核心加 Monarch 的负 rollover 语义；银行同步、多用户分享、审批/报销、企业预算/公共预算、账户净值与投资视图不属于本类型核心，也不适用于本场景。验收中的『超支显示负剩余且不阻止记账』与 rollover 负值语义一致；『改删后即时重算』与 running balance 一致，但主流产品未验证提供完整编辑历史，故审计宜以可导出记录与定期备份为主；『导出当月 CSV、中文/引号/换行可往返』应对齐 RFC 4180（含特殊字符的字段用双引号包裹、字段内双引号写成两个），并使用语言内置库（如 Python csv 的 QUOTE_MINIMAL 与 newline=''）；两位小数用 decimal 的 quantize 或整数分表示。
复用 vs 自建：类别行为与格式规范可直接参考产品文档、RFC 4180 与标准库；开源实现里 Actual Budget（MIT）可参考甚至有限复用，Firefly III（AGPL-3.0）因 copyleft 不宜复制代码。由于本场景功能面小（单用户、单机、无账户层、无同步），建议自建薄实现并复用内置 CSV/十进制能力，而不是引入大型应用；权限、计费、多租户管理等企业特性在此不适用，仅保留『导出即审计/恢复起点』这一最小关切。单机数据生命周期还应自行落实原子写入与备份目录策略，这一点在多数商业产品文档中并未公开说明。

## S01 · Atlas confirmed input

inputs/scenario.json · experiment-budget@1

按月为用途设置预算，记录和纠正实际支出，在消费前看到准确的计划、已花和剩余，并导出自己的记录。

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · YNAB API 官方文档（REST/OpenAPI）

https://api.ynab.com/ · OpenAPI spec 版本 1.87.0（文档页；访问 2026-10-19）

官方 REST API：Plan 为顶层容器，其下含 accounts、categories（按 category groups 组织）、payees、transactions、scheduled transactions、months 与 money movements；分类的 assigned/activity/available 金额按月（月内）取值，可通过带 month 的端点读写；金额以 milliunits（整数）表示；账户分 on budget / tracking；账户间转账用特殊 transfer payee 表示，交易可拆分为 subtransactions；scheduled transactions 表示定期但尚未入账的条目。

not code / 官方文档未声明开源许可



作为计划/月度/分类比较态的数据模型参考；不复用代码

## S03 · YNAB 官方方法页（The YNAB Method）

https://www.ynab.com/ynab-method · 网页内容；访问 2026-10-19（未固定版本）

官方方法强调 give every dollar a job（把当前持有的每一美元分配到分类，而非按凭空数字），并把拥抱真实支出（把汽车保险、年费等非月度支出平摊为月度预留）、roll with the punches（超支时从别的分类挪钱，计划是随时可改的活对象）、age your money 作为配套实践。

not code / 商业产品文档



方法、术语与超支调整语义参考；不复用代码

## S04 · Goodbudget 官方帮助中心（信封预算）

https://goodbudget.com/help/ · 多篇帮助文章（部分标注 2020-02-21、2023-11-16、2024-04-22 等）；访问 2026-10-19

官方信封式预算：先建 Envelopes，再从 Available 把钱 Fill 进信封（可选 Add budgeted amount 结转余额或 Set to budget amount 补足，并可 Schedule 自动 Fill）；支出记入信封使余额下降，且录入预先安排的支出会先计入当前信封余额；未分配的钱称 Available（原 Unallocated），是『还没分配用途』的推导额而非直接编辑；用 running balance 计算当前余额，余额不受单月限制，因此补记/改账过去日期会改变当前信封余额；新月份需重新 Fill，上月交易仍可见。

not code / 商业产品文档



行为与边界参考（结转、补记重算、Available 推导）

## S05 · Monarch Money 官方帮助中心：Rollover Budgets

https://help.monarchmoney.com/hc/en-us/articles/4411119762196-Rollover-Budgets · 帮助文章，Last Updated 2026-08-14；访问 2026-10-19

官方 rollover 规则：把上月剩余（可为负，即超支）带入下月，公式 Rollover(上月) + Planned(本月) − Actual(本月) = Remaining(下月)；rollover 仅可用于支出分类（不适用于收入分类）；示例中上月 −25 的超支会以负 rollover 进入下月；分类可 Exclude this category from the budget（排除后该分类及其交易从预算中隐藏）；rollover 可对单个分类或整个 bucket 启用，Flex 与 Category 两种预算方式并存。

not code / 商业产品文档



月末结转与超支负值语义参考

## S06 · Quicken Simplifi 官方帮助中心：Understanding Your Spending Plan

https://support.simplifi.quicken.com/en/articles/4212702-understanding-your-spending-plan · 帮助文章，Written June 11, 2026；访问 2026-10-19

官方 Spending Plan 把月度分为 Income、Bills、Planned Spend、Other Spend、Goals 等部分，并给出 Left this Month 作为当月真实可用余额；Spending Plan 只针对当月交易、不包含既有账户余额；删除 recurring 项会永久移除；计划不追溯生效，从订阅开始的月份起算；为避免双计，链接了 recurring reminder 的交易归入 Bills 而非 Planned Spend；建立 Planned Spend 时可填写 rollover remaining balance。

not code / 商业产品文档



自动生成计划与 Left to spend 表面参考；适用于消费前查看剩余的场景

## S07 · Fudget 官方产品页与商店描述（最小计划清单形态）

https://fudget.com/ · 官网与 App Store/Google Play 描述（更新 2025-09-26）；访问 2026-10-19

官方描述为无银行连接、手动录入的最简预算：设定收入与支出后即时显示 running balance（what's left）；支持按月/周或事件/项目（婚礼、装修）预算、把条目标记为已付、在预算之间结转余额（carry over balance）、多币种与自定义货币符号、备注；CSV 导出与打印等多在付费层（Fudget Plus）。基础版免费，付费为订阅制，属专有商业软件，无公开源码。

专有商业软件（未提供开源许可）



作为无账户、无银行连接的最小形态参考；不可复用代码

## S08 · Actual Budget 开源仓库

https://github.com/actualbudget/actual · 默认分支 master（未固定 commit）；访问 2026-10-19

README 称其为本地优先（local-first）个人财务工具，100% 免费开源、以 NodeJS 编写，带同步机制；以信封预算（envelope budgeting）为核心，可选端到端加密、多设备同步与可自行托管的同步服务，并有本地桌面应用；提供预算、账户管理、报表等文档。LICENSE.txt 文本为 MIT 许可（Copyright James Long）。

MIT License（LICENSE.txt）

https://github.com/actualbudget/actual/blob/master/LICENSE.txt

MIT 宽松，可参考并有限复用；但其为大型 NodeJS 应用，与本任务单用户小工具规模不匹配，建议以行为/数据模型参考为主

## S09 · Firefly III 开源仓库

https://github.com/firefly-iii/firefly-iii · 默认分支 main（未固定 commit）；访问 2026-10-19

README 称其为自托管的开源个人财务管理器，支持预算、分类与标签，提供导入工具与多种财务报表；官方站点描述其核心为复式记账（double-entry bookkeeping）并支持多币种记账。仓库标明 AGPL-3.0，代码文件 LICENSE 为 GNU Affero General Public License v3。

GNU Affero General Public License v3 (AGPL-3.0)

https://github.com/firefly-iii/firefly-iii/blob/main/LICENSE

AGPL 属强 copyleft 且含网络使用条款，建议仅作功能参考，不复制其代码

## S10 · RFC 4180：CSV 通用格式与 MIME 类型

https://www.rfc-editor.org/rfc/rfc4180.html · RFC 4180，Info 类，2005 年 10 月；访问 2026-10-19

CSV 的信息性事实标准：记录以 CRLF 结尾；末行可无结尾换行；可选首行表头；字段含逗号、双引号或换行时应用双引号包裹；字段内双引号以两个双引号转义；每行字段数应一致，末字段后不应有逗号；注册 MIME 类型 text/csv。

not code / IETF RFC（信息性文档）



作为导出/导入 CSV 的格式规范复用

## S11 · Python 标准库 csv 模块文档

https://docs.python.org/3/library/csv.html · Python 3.15.0 文档（页面更新 2026-10-18）；访问 2026-10-19

csv 提供 reader/writer、DictReader/DictWriter 与方言机制；QUOTE_MINIMAL（默认）只对含分隔符、引号、'\r'/'\n' 等特殊字符的字段加引号；doublequote 默认为 True，把字段内引号写成两个引号；读写文件应使用 newline=''，否则含换行的引号字段会被错误解析或写出多余 '\r'；读取默认按 UTF-8 解码，可用 encoding 指定其他编码。

Python Software Foundation License Version 2.0（文档；示例另按 Zero Clause BSD）

https://docs.python.org/3/license.html

复用（若实现语言为 Python），可直接得到符合 RFC 4180 的引号/换行处理

## S12 · Python 标准库 decimal 模块文档

https://docs.python.org/3/library/decimal.html · Python 3.15.0 文档；访问 2026-10-19

decimal 提供精确十进制浮点运算，文档称其被会计类应用首选：0.1+0.1+0.1-0.3 精确为 0，而二进制浮点得 5.55e-17；可保留有效位（1.30+1.20=2.50）；quantize 可把结果舍入到固定小数位（如 Decimal('.01')）；上下文可设精度与舍入模式（默认 ROUND_HALF_EVEN，另有 HALF_UP、DOWN 等）并可把 Inexact/Rounded 等信号设为异常以显式暴露舍入。

Python Software Foundation License Version 2.0（文档）

https://docs.python.org/3/license.html

复用；或改用整数最小单位（分）避免浮点误差

## S13 · Actual Budget 官方 API 文档（本地存储、导入导出）

https://actualbudget.org/docs/api/ · 官方文档页，经搜索快照获取（未逐字核对全文，未固定版本）；访问 2026-10-19

官方 API 文档称：预算数据在本地缓存于 dataDir（默认为当前工作目录，浏览器端为 IndexedDB 且留在设备上），无 serverURL 时不发起网络请求；exportBudget 把当前预算导出为 zip（db.sqlite 与 metadata.json），importBudget 可再导入还原；可导入 YNAB4/YNAB5 导出；主要用途之一即自定义导入/导出。

not code / 官方文档未声明开源许可



数据生命周期、导出与恢复策略的参考；不复用代码

## 待验证

- webfetch 仅允许 github.com / raw.githubusercontent.com / docs.python.org / docs.npmjs.com；YNAB、Goodbudget、Monarch、Quicken Simplifi、Fudget、Actual 官网与帮助中心的正文未能以完整文档形式核验，除这里明确取得的页面文本外，其余属搜索快照证据。
- YNAB 用户端帮助中心据 leaf 记录为 JavaScript 外壳，无法取到正文；本报告据官方 API 文档与方法页，未覆盖其帮助中心的用户操作细节。
- Quicken Simplifi 与 Monarch 的准确数值限制（分类上限、历史保留、rollover 的具体取整规则）未从完整官方文档证实，故不作断言。
- Goodbudget 的 Available 计算式与 running balance 补记重算规则来自帮助文章片段，未逐条核对完整文档；其『审计/Audit』相关文章正文未取得。
- 未见任一主流预算产品（据可用一手文档）提供完整的编辑历史/审计日志；改账是否留痕、如何回溯为未验证项。
- 第三方产品 CSV 导入/导出对中文、字段内引号与嵌入换行的实际往返行为未逐字验证；RFC 4180 与 Python csv 仅提供应遵循的格式与库行为依据。
- 人民币（CNY，ISO 4217）的两位小数与符号格式未引用官方货币/本地化一手来源验证，仅依场景约定。
- Fudget 的 CSV 导出位于付费订阅层，具体字段与编码未从官方完整文档获得；其数据存储位置与备份策略未验证。
- Firefly III 与 Actual Budget 的实际存储格式、迁移/备份流程未运行或逐文件核验；许可结论仅据仓库 LICENSE 文件。
- 单机数据持久化（原子写入、崩溃恢复、备份轮换）缺少针对本场景的一手约定或标准引用；SQLite/WAL 等具体实现细节未在本报告中作为证据核实。
- 未发现与本场景完全对应的中文单机预算应用官方文档；类别行为证据主要来自国际产品，迁移到本地中文场景需自行验证。
