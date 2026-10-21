# 待修订的五项问题（尚未修改冻结内容）

来源：第4次独立会话的完整材料审阅 RESULT.json。原15条代码/文档观察全部获接受；失败集中于目标合同和验收程序。辅助草案已经正式API撤回。原16份可用辅助模板不变。

1. A01 成功PATCH之后，以返回的最新住房对象作为空PATCH的零写入基线，包含updated_at；不再与成功PATCH之前的旧对象比较。
2. A01 增加非法equipment.category（不在枚举内）请求，核对422及设备列表不变，覆盖场景验收中明确要求的分支。
3. 明确首次补录历史完成日期时的下次到期日下限。建议保留“不得倒退”意图，以原due_on为下限：max(原due_on, max(旧last_completed_on或本次completed_on, 本次completed_on)+interval_days)。新增last_completed_on=NULL、first_due_on=2026-03-01、completed_on=2025-01-01、interval=30的断言，确保新due_on仍为2026-03-01，同时历史正常保存。此为待确认修订设计，未倒填进原规格。
4. A02 在独立测试设备范围内，对overdue/due/upcoming完整ID集合及数量做精确断言，不能只检查部分记录存在；额外记录必须导致测试失败。
5. A05 用标准库HTMLParser校验既有合同要求的label for/id关联、fieldset/legend、caption、th scope=col、role=status及lang=en结构；不扩大无障碍范围，不以单纯关键字出现代替结构检查。

下一步最小工作：同一场景、同一案例commit、同一业务范围下生成修订候选；保留此原始冻结版。先做上述合同/验收对齐，再进行一次新的完整材料独审。当前获准4次会话已用完，不擅自执行第5次调用；不是恢复严格G1/T08。
