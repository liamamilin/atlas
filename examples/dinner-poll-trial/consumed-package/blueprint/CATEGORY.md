# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

同一共享案例记录的静态研究与明确的设计推断；完整定位见inputs/shared-case-record.json。

## S01 · Atlas confirmed input

inputs/scenario.json · scn_0da5ffd0b2124edf8183c82506cb2c61@1

为聚餐问题预设地点选项，成员用代号单选并可改票，查看汇总，在结束后冻结投票，必要时重开。

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · ev_assisted_dinner_poll_1

https://github.com/nextcloud/polls/blob/65bf4627ee9a76c52034e796eda75ae5112ad7c3/lib/Db/Vote.php · 65bf4627ee9a76c52034e796eda75ae5112ad7c3

code_observation: Vote实体包含pollId、userId、voteOptionId与voteAnswer，定义yes/no/maybe；目标采用单选，与上游多选偏好语义不同。

AGPL-3.0-or-later（Vote.php SPDX及COPYING）

https://github.com/nextcloud/polls/blob/65bf4627ee9a76c52034e796eda75ae5112ad7c3/LICENSE

只参考设计；不复制上游代码。独立审阅pending，上游运行not_run。

## S03 · ev_assisted_dinner_poll_2

https://github.com/nextcloud/polls/blob/65bf4627ee9a76c52034e796eda75ae5112ad7c3/lib/Db/Poll.php · 65bf4627ee9a76c52034e796eda75ae5112ad7c3

code_observation: Poll声明datePoll与textPoll、private/open访问以及always/closed/never结果可见策略；目标采用文字选项与显式关闭。

AGPL-3.0-or-later（Vote.php SPDX及COPYING）

https://github.com/nextcloud/polls/blob/65bf4627ee9a76c52034e796eda75ae5112ad7c3/LICENSE

只参考设计；不复制上游代码。独立审阅pending，上游运行not_run。

## S04 · ev_assisted_dinner_poll_design

https://github.com/nextcloud/polls/blob/65bf4627ee9a76c52034e796eda75ae5112ad7c3/LICENSE · 65bf4627ee9a76c52034e796eda75ae5112ad7c3

inference: 目标不嵌入Nextcloud，也不复制其身份体系。使用本机共享界面、代号casefold去重、单选替换、显式open/closed状态；代号不是身份认证，不能用于正式选举。

AGPL-3.0-or-later（Vote.php SPDX及COPYING）

https://github.com/nextcloud/polls/blob/65bf4627ee9a76c52034e796eda75ae5112ad7c3/LICENSE

只参考设计；不复制上游代码。独立审阅pending，上游运行not_run。

## 待验证

- 证据独立审阅pending
- 上游not_run
- Codex静态研究和编写，证据独审pending；上游未安装运行
- 只供本机辅助试用，非严格G1/T08；不改旧应用或数据
- 本机同屏、代号非身份认证；不做远程分享、权限隔离、防恶意刷票或正式选举用途
