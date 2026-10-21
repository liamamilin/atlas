# 冻结核心验收

仅测试自有临时目录，不指向用户库。`python3 acceptance/probe.py --case A01 --app-root /absolute/app-root`，A01–A04均执行完整核心旅程与真正重启。或 --base-url 指向每次全新临时服务；固定日期不得与已有测试重复。失败不得改套件来迁就实现。浏览器操作另记。
