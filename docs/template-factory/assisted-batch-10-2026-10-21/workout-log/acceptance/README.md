# 核心验收（待真实应用运行）

A01–A04使用同一完整核心旅程，--app-root在临时目录启动并真正停机重启；或--base-url只指向一次性自有空库。例：`python3 acceptance/probe.py --case A01 --app-root /absolute/app-root`。文件管理模板另需实现约定 --sandbox-root 的测试沙箱；本轮未运行。不得指向已有用户库。代码可执行不等于已通过；当前只有语法编译检查。浏览器验收、完整安全矩阵均另记。
