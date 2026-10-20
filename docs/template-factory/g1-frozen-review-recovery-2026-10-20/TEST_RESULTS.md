# 本轮宿主验证结果

以下全部为当前宿主代码的实际检查；fixture不代表生产调用或真实模板通过。

宿主源码树 SHA256：`6d4ecacc74fbf419d175249ff949096b985144c75d31639a7484b71364dcfdb1`。13组全部通过，检查期间源码未变。

| 检查 | 结果 | 测试数 / 跳过 | 日志 |
|---|---|---|---|
| python_audit | passed | None / 0 | [日志](verification/full-final/python_audit.txt) |
| ruff | passed | None / 0 | [日志](verification/full-final/ruff.txt) |
| backend_tests | passed | 719 / 8 | [日志](verification/full-final/backend_tests.txt) |
| atlas_export | passed | None / 0 | [日志](verification/full-final/atlas_export.txt) |
| web_gen | passed | None / 0 | [日志](verification/full-final/web_gen.txt) |
| web_verify_data | passed | None / 0 | [日志](verification/full-final/web_verify_data.txt) |
| npm_audit | passed | None / 0 | [日志](verification/full-final/npm_audit.txt) |
| web_typecheck | passed | None / 0 | [日志](verification/full-final/web_typecheck.txt) |
| web_unit | passed | 9 / 0 | [日志](verification/full-final/web_unit.txt) |
| web_build | passed | None / 0 | [日志](verification/full-final/web_build.txt) |
| default_e2e | passed | 17 / 0 | [日志](verification/full-final/default_e2e.txt) |
| factory_e2e | passed | 27 / 0 | [日志](verification/full-final/factory_e2e.txt) |
| docker_integration | passed | 20 / 0 | [日志](verification/full-final/docker_integration.txt) |

新增回归包含：原input字节与leaf companion、无损差分和确定派生、精确只读ACL、同job唯一资格与幂等恢复、输入/模型/材料/时限篡改拒绝、普通路径绕过拒绝、失效lease、宿主源码变化、八维完整结果与实际原响应绑定、已知framing凭据、合法交付后宿主中断的无CLI续交、同overall passed但checks篡改拒绝、latest-attempt优先。

旧phase/protocol/evidence及CLI可靠性回归均纳入719项后端检查。真实生产资格尚未登记；远端新提交CI待独立核对。
