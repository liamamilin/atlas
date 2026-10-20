# 独立宿主代码审阅

审阅由独立 sol_reviewer 执行，只读检查本轮作用域，不调用生产provider，不替代运行验收。

发现并修复三项具体问题：

1. 旧schema缺少call_attempt列时，ALTER追加列与重建表的列顺序不同；SELECT *迁移可能错置旧created_at。已改为显式列名复制，并增加原时间戳、row、custom index与版本回执回归。
2. 取消固定45分钟余量后，reserve到实际spawn之间的等待可能使预计算timeout越过实际有效截止。CLI现在传递reservation绝对截止，在准备前、spawn前重新裁剪，并在进程运行中检查，保留未启动释放/已启动消费语义；新增fake-process负向回归。

3. 独立执行器新增时间记录读取时，需要把外层实际运行的campaign/plan/product与时间记录再次比对，不能只校验嵌套记录自身。已加严格比对和“外层及expected_binding同时换成另一产品”的负向回归；运行job ID仍独立绑定真实下游任务。

最终限定代码审阅未留下有证据支持的可操作阻断项。审阅者阅读了追加授权、同任务attempt3、只消费一次、旧grant不可复活、固定剩余窗口、latest-grant交付绑定、迁移与负向测试代码。

审阅限制：审阅者未运行检查或接触provider；实际本地全量检查、精确SHA远端CI、真实grant和CLI结果以本轮verification/、ci-source.json及operations/为准。此报告不声明G1通过。
