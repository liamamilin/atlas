旧补充工具未区分 JSON LF 与 HTML textarea 传输的 CRLF；Y 的完整逻辑输入被标未验证。新工具保留原始提交文本并仅将 form-urlencoded 的 CRLF 还原为 textarea 逻辑 LF，双方按相同规则完整重跑。没有修改应用或改变备注长度。
