# 架构与契约

## 数据与信任边界
单机同屏轮流投票，不宣称网络分发、身份认证或防冒名。Python标准库HTTP+SQLite。polls(id,title,status open|closed)，options(id,poll_id,label,position)，votes(poll_id,participant_key,participant_label,option_id, UNIQUE(poll_id,participant_key))。participant_key=strip().casefold()，1–40字符；相同代号更新票而非新增。问题1–160，2–8选项，每项1–80，trim/casefold去重。无永久删除，关闭可重开。
关闭状态只读，投票和改票均409poll_closed；在同事务检查状态、选项归属并upsert。计数从votes派生，默认全部结果可见；总数为投票人数，不把改票算新增。0票显示暂无投票；平票显示并列，不自动决定赢家；整数票数为真相，不用舍入百分比决定结果。
## 接口
GET /api/health；GET /api/polls -> {polls:[{id,title,status}]}；GET /api/polls/{id} -> {id,title,status,options:[{id,label,count}],total_votes}。
POST /api/polls {title,options:[文字]}->201 返回完整投票；POST /api/votes {poll_id,participant,option_id}->200返回完整投票；POST /api/polls/close {id}->200；POST /api/polls/reopen {id}->200。400invalid_title/invalid_options/invalid_participant/invalid_option，404not_found，409poll_closed；JSON{error:{code,message}}。同一次close/reopen可幂等返回当前状态，无新票。
## 界面及启动
首页新建、投票列表；详情含代号输入、选项radio、投票按钮、各项票数及总数；关闭时禁用投票并显示原因，重开入口明确。成功后刷新结果，错误保留代号/选项，所有文字转义。标明“同机共享，代号不是身份认证”，不使用第三方资源。
--port5278，独立--data-dir，--demo只新库首次初始化。采样使用虚构代号和地点，不传外部。浏览器验证create→vote→change→close拒绝→reopen→reload及实际进程重启。
