# 首轮单叶选源失败隔离修复

本轮实际故障：live-video-chat-application研究返回GitHub仓库TokTok/c-toxcore，规范共享案例为toktok/c-toxcore，固定commit和六个文件一致。宿主字面比较失败并误发全局workflow_integrity，连带dating-community暂停。142次调用及全部原失败保留，无在途调用。

修复只针对宿主选源比较/错误边界及回归，不改模型提示、场景、研究原文、案例或预算。规范验证后的GitHub owner/repo身份不区分大小写；文件路径、内容哈希、commit和case revision保持严格。有效共享来源原地复用，不重新研究；指定不存在案例或不匹配文件集时该叶failed，明确source_selection_invalid，不自动换源或当成功。

验收：大小写等价复用同一固定案例、选错case/files局部终态并继续后续叶子，明确非法选源与被包装的真实404/410属于单叶；403/429/5xx/网络共享故障、真实来源/固定输入/包摘要损坏、未知宿主、数据库、预算或不确定启动继续受原全局保护。不得泛化吞掉所有异常，不新增恢复资格。

相关宿主回归和精确提交CI通过后，追加原计划host revision并通过原服务恢复同一full_first_round/launchd。不重新注册plan/model，不重置30天窗口/7200/每叶6，不启动第二轮。真实恢复要复用discovery检查点并验证其原字节未变，随后交后台运行。
